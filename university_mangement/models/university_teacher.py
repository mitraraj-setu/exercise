from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class UniversityTeacher(models.Model):
    _name = 'university.teacher'
    _description = 'University Teachers List'

    code = fields.Integer(string='Teacher Code', required=True)
    firstname = fields.Char(string='Firstname', required=True)
    lastname = fields.Char(string='Lastname', required=True)
    phone = fields.Char(string='Contact Number')
    email = fields.Char(string='Email ID')
    date_of_birth = fields.Date(string='Birthdate', copy=False)
    joining_date = fields.Date(string='Joining Date')
    subject = fields.Char(string='Subject', copy=False)
    teacher_aadhaar_no = fields.Integer(string='Teacher Aadhaar No', copy=False)
    student_pass_ratio = fields.Float(string='Students Pass Ratio', copy=False)

    _sql_constraints = [
        ('check_teacher_aadhaar_no', 'unique(teacher_aadhaar_no)', 'Aadhaar Number must be Unique')
    ]