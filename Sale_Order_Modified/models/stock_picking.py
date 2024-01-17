from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.tools.misc import clean_context, OrderedSet, groupby
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # @api.depends('move_ids')
    # def _compute_move_ids(self):
    #     for record in self:
    #         if self.picking_type_code == 'incoming':
    #             raise UserError(_("Cannot add a new line that is not in purchase order"))

    # @api.onchange('move_ids')
    # def _onchange_move_ids(self):
    #     if self.picking_type_code == 'incoming':
    #         raise UserError(_("Cannot add a new line that is not in purchase order"))

    @api.constrains('move_ids')
    def _check_move_line_ids(self):
        if self.picking_type_code == 'incoming':
            for move in self.move_ids:
                if not move.move_line_ids:
                    # if not any(line.product_id.id == move.product_id.id for line in self.purchase_id.order_line):
                    raise UserError(_("Cannot add a new line that is not in purchase order"))





    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super().create(vals_list)
    #     for record in self:
    #         record.carrier_id = record.sale_id.carrier_id
    #         if not record.sale_id and record.origin:
    #
    #     return res

    # def action_assign(self):
    #     res = super().action_assign()
    #     assigned_moves_ids = OrderedSet()
    #     partially_available_moves_ids = OrderedSet()
    #     StockMove = self.env['stock.move']
    #     for picking in self:
    #         picking.do_unreserve()
    #         for move in picking.move_ids:
    #             lot_ids = move.sale_line_id.lot_ids
    #             need = move.product_uom_qty - move.reserved_availability
    #             if not need:
    #                 continue
    #             for lot_id in lot_ids:
    #                 available_quantity = move._get_available_quantity(move.location_id, lot_id= lot_id)
    #                 taken_quantity = move._update_reserved_quantity(need, available_quantity, move.location_id, strict=False)
    #                 need -= taken_quantity
    #             if float_is_zero(need - taken_quantity, precision_rounding=move.product_id.uom_id.rounding):
    #                 assigned_moves_ids.add(move.id)
    #                 break
    #             partially_available_moves_ids.add(move.id)
    #     StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
    #     StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
    #     return res
    #
    # def action_assign(self):
    #     res = super().action_assign()
    #     assigned_moves_ids = OrderedSet()
    #     partially_available_moves_ids = OrderedSet()
    #     StockMove = self.env['stock.move']
    #     for picking in self:
    #         picking.do_unreserve()
    #         for move in picking.move_ids:
    #             location_id = move.sale_line_id.location_id
    #             need = move.product_uom_qty - move.reserved_availability
    #             if not need:
    #                 continue
    #             available_quantity = move._get_available_quantity(location_id)
    #             taken_quantity = move._update_reserved_quantity(need, available_quantity, location_id, strict=False)
    #             need -= taken_quantity
    #             if float_is_zero(need - taken_quantity, precision_rounding=move.product_id.uom_id.rounding):
    #                 assigned_moves_ids.add(move.id)
    #                 break
    #             partially_available_moves_ids.add(move.id)
    #     StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
    #     StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
    #     return res

    # def action_assign(self):
    #     res = super().action_assign()
    #     assigned_moves_ids = OrderedSet()
    #     partially_available_moves_ids = OrderedSet()
    #     StockMove = self.env['stock.move']
    #     for picking in self:
    #         picking.do_unreserve()
    #         for move in picking.move_ids:
    #             location_id = move.sale_line_id.location_id
    #             lot_ids = move.sale_line_id.lot_ids
    #             need = move.product_uom_qty - move.reserved_availability
    #             if not need:
    #                 continue
    #             for lot_id in lot_ids:
    #                 available_quantity = move._get_available_quantity(location_id, lot_id= lot_id)
    #                 taken_quantity = move._update_reserved_quantity(need, available_quantity, location_id, strict=False)
    #                 need -= taken_quantity
    #             if float_is_zero(need - taken_quantity, precision_rounding=move.product_id.uom_id.rounding):
    #                 assigned_moves_ids.add(move.id)
    #                 break
    #             partially_available_moves_ids.add(move.id)
    #     StockMove.browse(partially_available_moves_ids).write({'state': 'partially_available'})
    #     StockMove.browse(assigned_moves_ids).write({'state': 'assigned'})
    #     return res


