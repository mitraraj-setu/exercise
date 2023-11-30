from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class StockMove(models.Model):
    _inherit = 'stock.move'

    # def _prepare_move_line_vals(self, quantity=None, reserved_quant=None):
    #     self.ensure_one()
    #     vals = {
    #         'move_id': self.id,
    #         'product_id': self.product_id.id,
    #         'product_uom_id': self.product_uom.id,
    #         'location_id': self.sale_line_id.location_id.id,
    #         'location_dest_id': self.location_dest_id.id,
    #         'picking_id': self.picking_id.id,
    #         'company_id': self.company_id.id,
    #     }
    #     if quantity:
    #         rounding = self.env['decimal.precision'].precision_get('Product Unit of Measure')
    #         uom_quantity = self.product_id.uom_id._compute_quantity(quantity, self.product_uom, rounding_method='HALF-UP')
    #         uom_quantity = float_round(uom_quantity, precision_digits=rounding)
    #         uom_quantity_back_to_product_uom = self.product_uom._compute_quantity(uom_quantity, self.product_id.uom_id, rounding_method='HALF-UP')
    #         if float_compare(quantity, uom_quantity_back_to_product_uom, precision_digits=rounding) == 0:
    #             vals = dict(vals, reserved_uom_qty=uom_quantity)
    #         else:
    #             vals = dict(vals, reserved_uom_qty=quantity, product_uom_id=self.product_id.uom_id.id)
    #     package = None
    #     if reserved_quant:
    #         package = reserved_quant.package_id
    #         vals = dict(
    #             vals,
    #             location_id=reserved_quant.location_id.id,
    #             lot_id=reserved_quant.lot_id.id or False,
    #             package_id=package.id or False,
    #             owner_id =reserved_quant.owner_id.id or False,
    #         )
    #     return vals
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super().create(vals_list)
    #     for val in res:
    #         val.write({'location_id': val.sale_line_id.location_id})
    #     return res

    # def _action_confirm(self, merge=True, merge_into=False):
    #     for move in self:
    #         if

    # def _get_available_quantity(self, location_id, lot_id=None, package_id=None, owner_id=None, strict=False, allow_negative=False):
    #     self.ensure_one()
    #     location_id = self.sale_line_id.location_id
    #     if location_id.should_bypass_reservation():
    #         return self.product_qty
    #     return self.env['stock.quant']._get_available_quantity(self.product_id, location_id, lot_id=lot_id, package_id=package_id, owner_id=owner_id, strict=strict, allow_negative=allow_negative)
    #
    # def _update_reserved_quantity(self, need, available_quantity, location_id, lot_id=None, package_id=None,
    #                               owner_id=None, strict=True):
    #     location_id = self.sale_line_id.location_id
    #     res = super()._update_reserved_quantity(need, available_quantity, location_id, package_id=None,
    #                               owner_id=None, strict=True)
    #     return res