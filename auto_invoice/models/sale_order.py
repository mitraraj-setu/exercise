import datetime
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # enable_auto_invoice = fields.Boolean(string='Enable Auto Invoice', default=True)

    # @api.onchange('partner_id')
    # def _onchange_partner_id(self):
    #     product = self.env['product.product'].search([('id', '=', 3)])
    #     order = self.env['sale.order'].search([('id', '=', 410)])
    #     order.order_line = [(0, 0, {
    #         'order_id': order.id,
    #         'name': product.name,
    #         'product_id': product.id,
    #         'product_uom_qty': 2,
    #         'product_uom': product.uom_id.id,
    #         'price_unit': 10
    #     })]

    #
    # def _cron_create_auto_invoice(self):
    #     days = self.env['ir.default'].get('res.config.settings', 'days')
    #     today = datetime.datetime.today()
    #     orders = self.env['sale.order'].search([('date_order', '<', (today-datetime.timedelta(days=days))),
    #                                              ('enable_auto_invoice', '=', True), ('state', '=', 'sale'),
    #                                              ('invoice_ids', '=', False)])
    #     for order in orders:
    #         if all(picking.state == 'done' for picking in order.picking_ids):
    #             ctx = {'active_model': 'sale.order', "active_ids": [order.id], 'active_id': order.id}
    #             create_invoice_wizard = self.env['sale.advance.payment.inv'].with_context(ctx).create(
    #                 {'advance_payment_method': 'delivered'})
    #             try:
    #                 create_invoice_wizard.create_invoices()
    #             except Exception as e:
    #                 continue
    #             order.invoice_ids[-1].write({'invoice_date': order.picking_ids[-1].scheduled_date})

