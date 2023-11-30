from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    buyer = fields.Boolean(string='Buyer')
    seller = fields.Boolean(string='Seller')
