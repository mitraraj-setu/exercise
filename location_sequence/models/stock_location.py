from odoo import fields, models, api


class Location(models.Model):
    _inherit = 'stock.location'


    sequence = fields.Integer(string='Sequence')
