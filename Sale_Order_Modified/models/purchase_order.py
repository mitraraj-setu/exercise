from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals_list):
        # for line in vals_list.get('order_line'):
        #     po_line = line[-1]
        #     po_lines = self.env['purchase.order.line'].search([('product_id','=',po_line.get('product_id'))], limit=1)
        #     if po_line.get('price_unit') < po_lines.price_unit:
        #         self.price_unit_check = 'low'
        #     elif po_line.get('price_unit') > po_lines.price_unit:
        #         self.price_unit_check = 'high'
        #     elif po_line.get('price_unit') == po_lines.price_unit:
        #         self.price_unit_check = 'equal'
        return super().create(vals_list)
