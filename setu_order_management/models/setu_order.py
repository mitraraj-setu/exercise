from odoo import models, fields

class SetuOrder(models.Model):
    _name='setu.order'
    _description='Order Information'

    name = fields.Char(string='Customer Name', required=True)
    product = fields.Char(string='Product Name', required=True )
    quantity=fields.Integer(string='Quantity', required=True)
    amount = fields.Float(string='Total Amount', required=True)