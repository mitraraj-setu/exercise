from odoo import models, fields,api


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line']

    extra_price = fields.Float(string="Extra Price")

    @api.depends('price_unit', 'extra_price', 'product_uom_qty', 'tax_id')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        for line in self:
            add_extraprice = line.extra_price * line.product_uom_qty

            line.price_subtotal += add_extraprice
            line.price_total += add_extraprice
        return res



