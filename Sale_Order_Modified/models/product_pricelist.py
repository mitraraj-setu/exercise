from odoo import fields, models, api


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    order_amt_based = fields.Boolean(string='Based on Order Amount')

    order_amt_item_ids = fields.One2many('product.pricelist.item', 'order_amt_pricelist_id')
