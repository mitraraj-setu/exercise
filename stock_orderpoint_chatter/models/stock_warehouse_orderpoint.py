from odoo import fields, models, api


class StockWarehouseOrderpoint(models.Model):
    _name = "stock.warehouse.orderpoint"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'stock.warehouse.orderpoint']

    location_id = fields.Many2one(
        'stock.location', 'Location', index=True,
        compute="_compute_location_id", store=True, readonly=False, precompute=True,
        ondelete="cascade", required=True, check_company=True, tracking=True)
    warehouse_id = fields.Many2one(
        'stock.warehouse', 'Warehouse',
        compute="_compute_warehouse_id", store=True, readonly=False, precompute=True,
        check_company=True, ondelete="cascade", required=True, tracking=True)
    route_id = fields.Many2one(
        'stock.route', string='Preferred Route', domain="[('product_selectable', '=', True)]", tracking=True)
    product_min_qty = fields.Float(
        'Min Quantity', digits='Product Unit of Measure', required=True, default=0.0,
        help="When the virtual stock goes below the Min Quantity specified for this field, Odoo generates "
             "a procurement to bring the forecasted quantity to the Max Quantity.", tracking=True)
    product_max_qty = fields.Float(
        'Max Quantity', digits='Product Unit of Measure', required=True, default=0.0,
        help="When the virtual stock goes below the Min Quantity, Odoo generates "
             "a procurement to bring the forecasted quantity to the Quantity specified as Max Quantity.", tracking=True)
    qty_to_order = fields.Float('To Order', compute='_compute_qty_to_order', store=True, readonly=False,
                                digits='Product Unit of Measure', tracking=True)
    trigger = fields.Selection([
        ('auto', 'Auto'), ('manual', 'Manual')], string='Trigger', default='auto', required=True, tracking=True)
    group_id = fields.Many2one(
        'procurement.group', 'Procurement Group', copy=False,
        help="Moves created through this orderpoint will be put in this procurement group. If none is given, the moves generated by stock rules will be grouped into one big picking.", tracking=True)
    qty_multiple = fields.Float(
        'Multiple Quantity', digits='Product Unit of Measure',
        default=1, required=True,
        help="The procurement quantity will be rounded up to this multiple.  If it is 0, the exact quantity will be used.", tracking=True)
    visibility_days = fields.Float(
        compute='_compute_visibility_days', inverse='_set_visibility_days', readonly=False,
        help="Consider product forecast these many days in the future upon product replenishment, set to 0 for just-in-time.\n"
             "The value depends on the type of the route (Buy or Manufacture)", tracking=True)


