from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


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

    def write(self, values):
        temp = super().write(values)
        # if 'order_line' in values.keys():
        #     if self.picking_ids:
        #         for value in values.get('order_line'):
        #             if type(value[1]) != type(0):
        #                 raise UserError(_("Cannot add a new line for a confirmed purchase order"))
        #             self.write({'order_line': value})
        return temp
