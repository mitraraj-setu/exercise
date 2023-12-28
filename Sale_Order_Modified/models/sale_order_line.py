from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_order_amt_based = fields.Float(string='Order Discount', compute='_compute_order_discount', store=True, readonly=False)
    discounted_subtotal = fields.Float(string='Discounted Subtotal', compute='_compute_discounted_amount', store=True)
    lot_ids = fields.Many2many('stock.lot', string='Serial')
    location_id = fields.Many2one('stock.location', string='Location')

    product_commission = fields.Float(string='Product Commission')

    @api.depends('price_subtotal')
    def _compute_order_discount(self):
        for line in self:
            line.discount_order_amt_based = 0
            if line.pricelist_item_id.order_amt_pricelist_id.order_amt_based:
                line.discount_order_amt_based = self.env['product.pricelist.item'].search([('minimum_amount', '<', line.price_subtotal),
                                                                          ('maximum_amount', '>', line.price_subtotal),
                                                                          ('product_tmpl_id', '=', line.product_template_id.id)]).discount

    @api.depends('price_subtotal', 'discount_order_amt_based')
    def _compute_discounted_amount(self):
        for line in self:
            line.discounted_subtotal = 0
            if line.discount_order_amt_based != 0:
                subtotal = (line.price_unit * line.product_uom_qty)
                dis = subtotal * (line.discount_order_amt_based / 100)
                line.discounted_subtotal = subtotal - dis

    # Maximum and minimum price range configuration
    # @api.constrains('price_unit')
    # def _check_minimum_price(self):
    #     if self.product_template_id.minimum_price_enable == 1:
    #         if self.price_unit < self.product_template_id.minimum_price:
    #             raise ValidationError(_("The unit price should be more than minimum product price"))
    #
    # @api.constrains('price_unit')
    # def _check_maximum_price(self):
    #     if self.price_unit > self.product_template_id.maximum_price:
    #         raise ValidationError(_("The unit price should be less than maximum product price"))

    # @api.constrains('price_unit')
    # def _check_unit_price_range(self):
    #     if self.product_template_id.maximum_price and self.product_template_id.minimum_price:
    #         if self.price_unit < self.product_template_id.minimum_price or self.price_unit > self.product_template_id.maximum_price:
    #             raise ValidationError(_("The unit price should be between minimum and maximum unit price"))
    #
    # @api.onchange('price_unit')
    # def _onchange_price_unit(self):
    #     if self.product_template_id.maximum_price and self.product_template_id.minimum_price:
    #         if self.price_unit < self.product_template_id.minimum_price or self.price_unit > self.product_template_id.maximum_price:
    #             return {'warning': {
    #                 'title': _("Warning"),
    #                 'message': _(
    #                     "The unit price should be between minimum and maximum unit price")
    #             }}

    @api.model_create_multi
    def create(self, vals_list):
        #     for line in vals_list:
        #         if line.state == 'sale':
        #             raise UserError(_("You cannot add a product after confirming quotation."))
        #         return super(SaleOrderLine, self).create(vals_list)

        lines = super().create(vals_list)
        # for line in lines:
        #     if line.state == 'sale':
        #         raise UserError(_("You cannot add a product after confirming quotation."))
                # temp = super().unlink()
                # return temp
        return lines
