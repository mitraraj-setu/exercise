from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    minimum_product_price_config = fields.Boolean('Minimum Price Config')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        minimum_product_price_config = IrDefault.get('res.config.settings', 'minimum_product_price_config')
        res.update(
            minimum_product_price_config=minimum_product_price_config)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrDefault = self.env['ir.default'].sudo()
        IrDefault.set('res.config.settings', 'minimum_product_price_config', self.minimum_product_price_config)

        # def set_values(self):
        #     super(ResConfigSettings, self).set_values()
        #     IrDefault = self.env['ir.default'].sudo()
        #
        #     IrDefault.set('product.template', 'allow_out_of_stock_order', self.allow_out_of_stock_order)
        #     IrDefault.set('product.template', 'available_threshold', self.available_threshold)
        #     IrDefault.set('product.template', 'show_availability', self.show_availability)
        #
        # @api.model
        # def get_values(self):
        #     res = super(ResConfigSettings, self).get_values()
        #     IrDefault = self.env['ir.default'].sudo()
        #     allow_out_of_stock_order = IrDefault.get('product.template', 'allow_out_of_stock_order')
        #
        #     res.update(
        #         allow_out_of_stock_order=allow_out_of_stock_order if allow_out_of_stock_order is not None else True,
        #         available_threshold=IrDefault.get('product.template', 'available_threshold') or 5.0,
        #         show_availability=IrDefault.get('product.template', 'show_availability') or False)
        #     return res
