from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_price = fields.Float(string='Minimum Unit Price')
    maximum_price = fields.Float(string='Maximum Unit Price')
    minimum_price_enable = fields.Boolean(compute='_compute_minimum_price_setting')

    @api.onchange('minimum_price','maximum_price')
    def _onchange_max_min_price(self):
        if self.minimum_price > self.maximum_price:
            return {'warning': {
                'title': _("Warning"),
                'message': _(
                    "The maximum unit price should always be greater than minimum unit price")
            }}

    def _compute_minimum_price_setting(self):
        temp = int(self.env['ir.default'].get('res.config.settings', 'minimum_product_price_config'))
        # temp = 1
        self.minimum_price_enable = 0
        if temp:
            self.minimum_price_enable = 1
