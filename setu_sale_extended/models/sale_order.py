from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total',"order_line.extra_price")
    def _compute_amounts(self):

        super(SaleOrder, self)._compute_amounts()
        for order in self:
            amount_untaxed = sum(order.order_line.mapped(lambda line: line.price_subtotal))
            print("amount_untaxed  ",amount_untaxed)
            amount_tax = sum(order.order_line.mapped(lambda line: line.price_tax))
            print("amount_tax  ", amount_tax)

            order.amount_untaxed =amount_untaxed
            order.amount_tax = amount_tax
            order.amount_total =  amount_untaxed + amount_tax


#