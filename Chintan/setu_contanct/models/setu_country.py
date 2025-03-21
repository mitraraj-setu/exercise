from odoo import fields , models

class SetuCountry(models.Model):
    _name='setu.country'
    _description='Information about country'

    name = fields.Char(string="Country Name", required=True)
    code = fields.Char(string="Country Code", required=True)
    state_ids = fields.One2many('setu.state', 'country_id', string="States")