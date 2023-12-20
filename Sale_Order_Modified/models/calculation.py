from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class Calculation(models.Model):
    _name = 'calculation'

    first_value = fields.Float(string='First Value', digits=(12,8))
    second_value = fields.Float(string='Second Value', digits=(12,8))
    operation = fields.Char(string='Operation')
    result = fields.Float(string='Result', digits=(5,10))

    def do_add(self, a, b):
        addition = a + b
        self.result = addition
        return addition

    def do_diff(self, a, b):
        subtraction = a - b
        self.result = subtraction
        return subtraction

    def do_multi(self, a, b):
        multiplication = a * b
        self.result = multiplication
        return multiplication

    def do_div(self, a, b):
        division = a / b
        self.result = division
        return division

    @api.model
    def create(self, vals_list):
        return super().create(vals_list)

    # def write(self, vals):
    #     return super().write(vals)

    def unlink(self):
        return super().unlink()
