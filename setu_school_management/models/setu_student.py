from odoo import models, fields
from odoo.exceptions import UserError


class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Student Information'

    name = fields.Char(string='Student', required=True)
    age = fields.Integer(string='Age', help="This field is use to store Age of student", copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)
    mobile = fields.Char(string="Mobile Number", required=True)

    def create(self, vals):

        if vals.get('age', 0) < 5:
            raise UserError("Age must be at least 5 years old to enroll.")

        if 'name' in vals and 'age' in vals:
            vals['name'] = f"{ vals.get('name')} [ {vals.get('age', 0)} ]"
        return super(SetuStudent, self).create(vals)


