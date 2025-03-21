from odoo import models, fields

class ResPartner(models.Model):
    _inherit = ["res.partner"]

    credit_point=fields.Float(string="Credit Points", readonly=True, help="Total credit points from sales orders.", tracking=True)


































