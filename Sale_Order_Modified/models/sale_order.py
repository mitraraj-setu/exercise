from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_commission = fields.Float(string='Order Commission')
    total_commission = fields.Float(string='Total Commission')

    buyer_partner = fields.Many2one('res.partner', string='Buyer')
    seller_partner = fields.Many2one('res.partner', string='Seller')

    def action_confirm(self):
        self.set_commission()
        # for sol in self.order_line:
        #     if sol.product_template_id.detailed_type == 'service':
        #         raise ValidationError(_("Service type product in sale order"))
        return super().action_confirm()

    def set_commission(self):
        temp = 0
        for line in self.order_line:
            rules = self.env['sale.commission'].search([('user_id', '=', self.user_id.id),
                                                        ('start_date', '<=', self.date_order),
                                                        ('end_date', '>=', self.date_order),
                                                        ('product_temp_id', '=', line.product_template_id.id)], order="sequence asc", limit=1)
            if rules.rule == 'order':
                if not self.order_commission:
                    if self.tax_totals.get('amount_total') >= rules.minimum and self.tax_totals.get(
                            'amount_total') <= rules.maximum:
                        if rules.commission_type == 'fixed':
                            self.order_commission = rules.fixed_amount
                            temp = temp + self.order_commission
                            continue
                        else:
                            self.order_commission = self.tax_totals.get(
                                'amount_total') * rules.percentage * 0.01
                            temp = temp + self.order_commission
                            continue
            if rules.rule == 'product':
                if line.product_uom_qty >= rules.minimum and line.product_uom_qty <= rules.maximum:
                    if rules.commission_type == 'fixed':
                        line.product_commission = rules.fixed_amount
                        temp = temp + line.product_commission
                        continue
                    else:
                        line.product_commission = line.price_subtotal * rules.percentage * 0.01
                        temp = temp + line.product_commission
                        continue
        self.total_commission = temp

    def _cron_set_commission(self):
        so_ids = self.env['sale.order'].search([('create_date', '<', datetime.datetime.today()+ datetime.timedelta(days=1)), ('state', '!=', 'cancel'),
                                                ('total_commission', '=', 0)])
        for so in so_ids:
            try:
                so.set_commission()
            except Exception as e:
                continue

    @api.model
    def create(self, vals_list):
        temp = super().create(vals_list)
        if vals_list.get('carrier_id'):
            carrier = self.env['delivery.carrier'].browse(vals_list.get('carrier_id'))
            vals = {'product_template_id': carrier.product_id.id,
                    'product_id': carrier.product_id.id,
                    'name': carrier.product_id.name,
                    'product_uom_qty': 1.0,
                    'price_unit': carrier.product_id.list_price,
                    'order_id': temp.id,
                    'customer_lead': carrier.product_id.sale_delay}
            self.env['sale.order.line'].create(vals)
        return temp

    def write(self, vals):
        carrier = self.carrier_id
        temp = super().write(vals)
        if ('carrier_id' in vals.keys()) and vals.get('carrier_id'):
            service_order_lines = self.order_line.filtered(lambda ol: ol.product_template_id.id == carrier.product_id.product_tmpl_id.id)
            carrier = self.carrier_id
            if service_order_lines:
                self.write({'order_line': [(1, service_order_lines.id, {'product_template_id': carrier.product_id.product_tmpl_id.id,
                                                'product_id': carrier.product_id.id,
                                                'order_id': self.id,
                                                'customer_lead': carrier.product_id.sale_delay})]})
            else:
                val = {'product_template_id': carrier.product_id.product_tmpl_id.id,
                       'product_id': carrier.product_id.id,
                       'order_id': self.id,
                       'customer_lead': carrier.product_id.sale_delay}
                self.env['sale.order.line'].create(val)
        elif ('carrier_id' in vals.keys()) and (not vals.get('carrier_id')):
            service_order_lines = self.order_line.filtered(lambda ol: ol.product_template_id.id == carrier.product_id.product_tmpl_id.id)
            service_order_lines.unlink()
        return temp

    def _cron_auto_invoice(self):
        # , ('create_date', '>', '2023-11-01 00:00:00')
        so_ids = self.env['sale.order'].browse(21)
        # so_ids = self.env['sale.order'].search([('delivery_status','in',['full','partial'])])
        for so in so_ids:
            ctx = {'active_model': 'sale.order', 'active_ids': so.ids}
            create_invoice_wizard = self.env['sale.advance.payment.inv'].with_context(ctx).create(
                {'advance_payment_method': 'delivered'})
            try:
                create_invoice_wizard.create_invoices()
            except Exception as e:
                continue
            so.invoice_ids[-1].write({'invoice_date': so.picking_ids[-1].scheduled_date})

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for record in self:
            warehouse = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)])
            warehouse_city = warehouse.partner_id.mapped('city')
            city_dist = self.env['city.distance'].search(['|', ('from_loc', '=', record.partner_id.city),('to_loc', '=', record.partner_id.city)])
            city_distance = 5000
            wh_city = ''
            del_charge = 100000
            service = ''
            # if record.partner_id.city in warehouse_city:
            #     record.warehouse_id = warehouse.filtered(lambda w: w.partner_id.city == record.partner_id.city)
            #     for val in city_dist:
            #         if del_charge > val['delivery_charges']:
            #             del_charge = val['delivery_charges']
            #             service = val['carrier_id']
            #     record.carrier_id = service
            # else:
            for val in city_dist:
                if city_distance >= val['distance']:
                    if city_distance == val['distance']:
                        if del_charge > val['delivery_charges']:
                            del_charge = val['delivery_charges']
                    city_distance = val['distance']
                    if val['from_loc'] in warehouse_city or val['to_loc'] in warehouse_city:
                        if val['from_loc'] in warehouse_city:
                            wh_city = val['from_loc']
                        else:
                            wh_city = val['to_loc']
                    service = val['carrier_id']

            record.warehouse_id = warehouse.filtered(lambda w: w.partner_id.city == wh_city)
            record.carrier_id = service
            # record.carrier_id.write({'display_name': service.display_name})
                # for val in record.picking_ids:
                #     val.carrier_id = service
