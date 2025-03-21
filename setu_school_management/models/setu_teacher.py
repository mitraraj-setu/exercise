from odoo import models, fields



class SetuTeacher(models.Model):
    _name = 'setu.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Teacher', required=True)
    age = fields.Integer(string='Age', copy=False)
    subject = fields.Char(string='Subject', required=True)
    experience = fields.Integer(string='Experience', help="Enter experience in number of years", copy=False)


