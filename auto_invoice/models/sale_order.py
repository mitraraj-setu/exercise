import datetime
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    enable_auto_invoice = fields.Boolean(string='Enable Auto Invoice')

    def _cron_create_auto_invoice(self):
        orders = self.env['sale.order'].search([('enable_auto_invoice', '=', True), ('state', '=', 'sale')])
        for order in orders:
            temp = self.env['ir.default'].get('res.config.settings', 'days')
            today = datetime.datetime.today()
            if (order.date_order + datetime.timedelta(days=temp)) > today:
                if all(picking.state == 'done' for picking in order.picking_ids):
                    ctx = {'active_model': 'sale.order', 'active_id': order.id}
                    create_invoice_wizard = self.env['sale.advance.payment.inv'].with_context(ctx).create(
                        {'advance_payment_method': 'delivered'})
                    try:
                        create_invoice_wizard.create_invoices()
                    except Exception as e:
                        continue
                    order.invoice_ids[-1].write({'invoice_date': order.picking_ids[-1].scheduled_date})