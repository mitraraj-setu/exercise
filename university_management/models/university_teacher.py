from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class UniversityTeacher(models.Model):
    _name = 'university.teacher'
    _description = 'University Teachers List'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'code'

    code = fields.Integer(string='Teacher Code', required=True)
    firstname = fields.Char(string='Firstname', required=True)
    lastname = fields.Char(string='Lastname', required=True)
    phone = fields.Char(string='Contact Number')
    email = fields.Char(string='Email ID')
    date_of_birth = fields.Date(string='Birthdate', copy=False)
    joining_date = fields.Date(string='Joining Date')
    teacher_aadhaar_no = fields.Char(string='Teacher Aadhaar No', copy=False)

    subject = fields.Char(string='Subject', copy=False)
    student_pass_ratio = fields.Float(string='Students Pass Ratio', copy=False)

    student_ids = fields.One2many('university.student', 'teacher_ids')

    _sql_constraints = [
        ('check_teacher_aadhaar_no', 'unique(teacher_aadhaar_no)', 'Aadhaar Number must be Unique'),
        ('check_code', 'unique(code)', 'Teacher Code must be Unique')
    ]

    def name_get(self):
        result = []
        for rec in self:
            name = rec.firstname+' '+rec.lastname+' ('+str(rec.code)+')'
            result.append((rec.id, name))
        return result

    @api.model
    def create(self, vals_list):
        rec = super().create(vals_list)
        return rec

    def write(self, vals):
        rec = super().write(vals)
        return rec

    def unlink(self):
        rec = super().unlink()
        return rec