from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'salesman_id', domain="[('state','in',['new offer received','offer accepted']),('state','=','')]")
