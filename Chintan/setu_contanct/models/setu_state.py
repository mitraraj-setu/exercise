from odoo import fields , models

class SetuState(models.Model):
    _name='setu.state'
    _description='Information about state'

    name = fields.Char(string="State Name", required=True)
    country_id = fields.Many2one('setu.country', string="Country", required=True)
    city_ids = fields.One2many('setu.city', 'state_id', string="Cities")