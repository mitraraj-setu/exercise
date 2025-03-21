from odoo import models , fields

class SetuProduct(models.Model):
    _name='setu.product'
    _description='Product Information'

    name = fields.Char(string='Product Name',required=True)
    vendor = fields.Char(string='Vendor Name',required=True)
    base_price = fields.Float(string='Base Price')
    selling_price = fields.Float(string='Selling Price')
