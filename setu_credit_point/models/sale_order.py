from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    use_credit_point = fields.Boolean(string=" Use Credit Points")
    credit_point = fields.Float(string="Credit Points", help="How many credit points you want to use?")

    def _create_discount_line(self, order, product, price, qty=1, name="Credit Point Discount", tax_ids=None):

        order.order_line.create({
            'order_id': order.id,
            'product_id': product.id,
            'name': name,
            'price_unit': price,
            'product_uom_qty': qty,
            'tax_id': [(6, 0, tax_ids)] if tax_ids else [(6, 0, [])],
        })

    def action_confirm(self):

        discount_product = self.env.ref("setu_credit_point.setu_discount_product_123", )

        if not discount_product:
            raise ValidationError("Discount Product is not found! Please create a discount product.")

        discount_variant = discount_product.product_variant_id

        use_credit_point = self.filtered(lambda o: o.use_credit_point)

        for order in use_credit_point:

            check_credit_point = order.partner_id.credit_point

            if order.credit_point > check_credit_point or order.credit_point < 0:
                raise ValidationError(
                    "You can not use more credit points than you have and you can not enter value less than 0")

            non_discount_lines = order.order_line.filtered(lambda line: line.product_id.id != discount_variant.id)

            if not non_discount_lines:
                raise ValidationError("You must add at least one product before using credit points.")

            discount_line = order.order_line.filtered(lambda line: line.product_id.id == discount_variant.id)

            if discount_line:
                discount_line.write({'price_unit': -order.credit_point})
            else:
                self._create_discount_line(
                    order=order,
                    product=discount_variant,
                    price=-order.credit_point,
                    qty=1,
                    name="Credit Point Discount",
                    tax_ids=[]
                )
                # order.order_line.create({
                #     'order_id': order.id,
                #     'product_id': discount_variant.id,
                #
                #     'name': "Credit Point Discount",
                #     'price_unit': -order.credit_point,
                #     'product_uom_qty': 1,
                #     'tax_id': [(6, 0, [])],
                # })

            order.partner_id.credit_point -= order.credit_point

            # points = order.amount_total * (0.02 if order.amount_total > 500 else 0.01)
            # order.partner_id.credit_point += points

            company = order.company_id or self.env.company
        percentage_for_le_500 = float(self.env['ir.config_parameter'].sudo().get_param('setu_credit_point.credit_point_for_le_500', 1.0))
        percentage_for_gt_500 = float(self.env['ir.config_parameter'].sudo().get_param('setu_credit_point.credit_point_for_gt_500', 2.0))



        points_percentage = percentage_for_gt_500 if self.amount_total > 500 else percentage_for_le_500
        points = self.amount_total * (points_percentage / 100)



        self.partner_id.credit_point += points

        return super(SaleOrder, self).action_confirm()











