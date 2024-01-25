from odoo import fields, models, api
from odoo.osv import expression

class ProductProduct(models.Model):
    _inherit = 'product.product'

    lot_name_type = fields.Selection(string='Lot Name Type', selection=[('prefix', 'Prefix'), ('suffix', 'Suffix')])
    lot_name = fields.Char(string='Lot Name')

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     if self.env.context.get('sale_customer'):
    #         sale_orders = self.env["sale.order"].search([('partner_id','=', self.env.context.get('sale_customer'))])
    #         args = (args or []) + [('id', 'not in', sale_orders.order_line.product_id.mapped('id'))]
    #         return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    #     return super()._name_search(name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)