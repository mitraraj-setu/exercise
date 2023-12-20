from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import OrderedSet


class StockMove(models.Model):
    _inherit = 'stock.move'

    # def _action_assign(self, force_qty=False):
    #     super()._action_assign(force_qty=force_qty)
    #     StockMove = self.env['stock.move']
    #     assigned_moves_ids = OrderedSet()
    #     partially_available_moves_ids = OrderedSet()
    #     move_line_vals_list = []
    #     moves_to_redirect = OrderedSet()
    #     for move in self:
    #         move._do_unreserve()
    #         need = move.product_uom_qty
    #         rounding = move.product_id.uom_id.rounding
    #         for location in (self.location_id.child_ids + self.location_id).sorted(lambda answer: answer.sequence):
    #             forced_package_id = move.package_level_id.package_id or None
    #             available_quantity = move._get_available_quantity(location, package_id=forced_package_id)
    #             if available_quantity <= 0:
    #                 continue
    #             taken_quantity = move._update_reserved_quantity(need, available_quantity, location,
    #                                                             package_id=forced_package_id, strict=False)
    #             if float_is_zero(taken_quantity, precision_rounding=rounding):
    #                 continue
    #             moves_to_redirect.add(move.id)
    #             if float_compare(need, taken_quantity, precision_rounding=rounding) == 0:
    #                 assigned_moves_ids.add(move.id)
    #             else:
    #                 partially_available_moves_ids.add(move.id)
    #     self.env['stock.move.line'].create(move_line_vals_list)
    #     StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
    #     StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
    #     StockMove.browse(moves_to_redirect).move_line_ids._apply_putaway_strategy()

