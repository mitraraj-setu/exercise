from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class StockMoveLines(models.Model):
    _inherit = 'stock.move.line'
