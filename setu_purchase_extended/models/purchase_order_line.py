from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    previous_price = fields.Float(string="Previous Price", compute="_compute_previous_price", store=True)

    @api.depends('product_id')

    def _compute_previous_price(self):
        for line in self:
            if not line.product_id:
                line.previous_price = 0.0
                continue


            purchase_order_id = self.env['purchase.order'].search([
                ('order_line.product_id', '=', line.product_id.id),
                ('state', 'in', ['purchase', 'done']),
            ], order="create_date desc", limit=1)

            line.previous_price = 0.0

            if purchase_order_id:
                last_order_line = purchase_order_id.order_line.filtered(lambda ol: ol.product_id == line.product_id)
                line.previous_price = last_order_line[-1].price_unit if last_order_line else 0.0




