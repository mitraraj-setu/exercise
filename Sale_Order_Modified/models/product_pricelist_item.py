from odoo import fields, models, api


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    product_tmpl_id = fields.Many2one('product.template',string="Product", ondelete='cascade', check_company=True,
        help="Specify a template if this rule only applies to one product template. Keep empty otherwise.")
    product_id = fields.Many2one('product.product', string="Product Variant", ondelete='cascade', check_company=True,
        help="Specify a product if this rule only applies to one product. Keep empty otherwise.")
    company_id = fields.Many2one(related='order_amt_pricelist_id.company_id', store=True)
    minimum_amount = fields.Float(string='Minimum Amount')
    maximum_amount = fields.Float(string='Maximum Amount')
    discount = fields.Float(string='Discount', required=True)

    order_amt_pricelist_id = fields.Many2one('product.pricelist', string="Pricelist", ondelete='cascade', required=True)
    # default = _default_pricelist_id
