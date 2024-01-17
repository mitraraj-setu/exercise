from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import OrderedSet


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _action_assign(self, force_qty=False):
        super()._action_assign(force_qty=force_qty)
        StockMove = self.env['stock.move']
        assigned_moves_ids = OrderedSet()
        partially_available_moves_ids = OrderedSet()
        move_line_vals_list = []
        moves_to_redirect = OrderedSet()
        # reserved_availability = {move: move.reserved_availability for move in self}
        # for move in self:
        #     move._do_unreserve()
        #     need = move.product_uom_qty
        #     rounding = move.product_id.uom_id.rounding
        #     for location in (self.location_id.child_ids + self.location_id).sorted(lambda answer: answer.sequence):
        #         forced_package_id = move.package_level_id.package_id or None
        #         available_quantity = move._get_available_quantity(location, package_id=forced_package_id)
        #         if available_quantity <= 0:
        #             continue
        #         taken_quantity = move._update_reserved_quantity(need, available_quantity, location,
        #                                                         package_id=forced_package_id, strict=False)
        #         if float_is_zero(taken_quantity, precision_rounding=rounding):
        #             continue
        #         moves_to_redirect.add(move.id)
        #         if float_compare(need, taken_quantity, precision_rounding=rounding) == 0:
        #             assigned_moves_ids.add(move.id)
        #             break
        #         else:
        #             partially_available_moves_ids.add(move.id)
        # self.env['stock.move.line'].create(move_line_vals_list)
        # StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
        # StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
        # StockMove.browse(moves_to_redirect).move_line_ids._apply_putaway_strategy()



        # for move in self:
            # move._do_unreserve()
            # need = move.product_uom_qty
            # rounding = move.product_id.uom_id.rounding
            # if not force_qty:
            #     missing_reserved_uom_quantity = move.product_uom_qty
            # else:
            #     missing_reserved_uom_quantity = force_qty
            # move._do_unreserve()
            # missing_reserved_uom_quantity -= reserved_availability[move]
        #     missing_reserved_quantity = move.product_uom._compute_quantity(missing_reserved_uom_quantity,
        #                                                                    move.product_id.uom_id,
        #                                                                    rounding_method='HALF-UP')
        #     need = missing_reserved_quantity
        #     for location in (self.location_id.child_ids + self.location_id).sorted(lambda answer: answer.sequence):
        #         if float_is_zero(move.product_uom_qty, precision_rounding=move.product_uom.rounding):
        #             assigned_moves_ids.add(move.id)
        #         elif not move.move_orig_ids:
        #             if move.procure_method == 'make_to_order':
        #                 continue
        #             # If we don't need any quantity, consider the move assigned.
        #             # need = missing_reserved_quantity
        #             if float_is_zero(need, precision_rounding=rounding):
        #                 assigned_moves_ids.add(move.id)
        #                 continue
        #             # Reserve new quants and create move lines accordingly.
        #             forced_package_id = move.package_level_id.package_id or None
        #             available_quantity = move._get_available_quantity(location, package_id=forced_package_id, strict=True)
        #             if available_quantity <= 0:
        #                 continue
        #             # move.location_id = location
        #             taken_quantity = move._update_reserved_quantity(need, available_quantity, location,
        #                                                             package_id=forced_package_id)
        #             if float_is_zero(taken_quantity, precision_rounding=rounding):
        #                 continue
        #             moves_to_redirect.add(move.id)
        #             if float_compare(need, taken_quantity, precision_rounding=rounding) == 0:
        #                 assigned_moves_ids.add(move.id)
        #             else:
        #                 partially_available_moves_ids.add(move.id)
        #             need -= taken_quantity
        #
        # self.env['stock.move.line'].create(move_line_vals_list)
        # StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
        # StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
        # if not self.env.context.get('bypass_entire_pack'):
        #     self.picking_id._check_entire_pack()
        # StockMove.browse(moves_to_redirect).move_line_ids._apply_putaway_strategy()

