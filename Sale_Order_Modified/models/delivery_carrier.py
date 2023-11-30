from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'delivery.carrier'

    @api.model
    def create(self, vals_list):
        product_id = self.env['product.product'].create({
            'name': vals_list.get('name'),
            'type': 'service',
            'list_price': 0.0,
            'categ_id': self.env.ref('delivery.product_category_deliveries').id,
        })
        vals_list.update({'product_id': product_id.id, 'fixed_price': 0.0})
        return super().create(vals_list)
