from odoo import fields, models, api


class Location(models.Model):
    _inherit = 'stock.location'
    _order = 'id'


    sequence = fields.Integer(string='Sequence')
