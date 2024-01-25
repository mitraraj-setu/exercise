from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_update_quantity(self):
        if not self.order_line:
            raise UserError(_("To update the quantity kindly add the product in the sale order first."))
        wiz = self.env['update.quantity.wizard'].create({
            'wiz_lines': [(0, 0, {'product_id': line.product_id.id,
                                  'quantity': False}) for line in self.order_line if line.product_id.detailed_type == 'product']
        })
        return {
            'type': 'ir.actions.act_window',
            'target': 'new',
            'name': _('Update Quantity'),
            'view_mode': 'form',
            'res_model': 'update.quantity.wizard',
            'view_id': self.env.ref('update_quantity.update_quantity_wizard_form_view').id,
            'res_id': wiz.id,
        }
