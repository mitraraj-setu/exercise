from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Students List'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'enrollment_no'

    enrollment_no = fields.Integer(string='Enrollment No', required=True)
    firstname = fields.Char(string='Firstname', required=True)
    lastname = fields.Char(string='Lastname', required=True)
    guardian_name = fields.Char(string="Guardian's name", required=True)
    phone = fields.Char(string='Contact Number')
    guardian_contact = fields.Char(string="Guardian's Contact")
    email = fields.Char(string='Email ID')
    date_of_birth = fields.Date(string='Student Birthdate', copy=False)
    student_aadhaar_no = fields.Char(string='Student Aadhaar No', copy=False)

    joining_date = fields.Date(string='Student Joining Date')
    standard = fields.Integer(string='Standard')
    mathematics = fields.Float(string='Maths')
    science = fields.Float(string='Science')
    social_science = fields.Float(string='Social Science')
    english = fields.Float(string='English')
    hindi = fields.Float(string='Hindi')
    total_marks = fields.Float(string='Total Marks', compute='_compute_total_marks', store=True)
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    result = fields.Char(string='Result', compute='_compute_result', store=True)

    teacher_ids = fields.Many2many('university.teacher', string='Teachers')
    badge_ids = fields.Many2many('university.student.badge')

    _sql_constraints = [
        ('check_student_aadhaar_no', 'unique(student_aadhaar_no)', 'Aadhaar Number must be Unique'),
        ('check_student_enrollment_no', 'unique(enrollment_no)', 'Enrollment Number must be Unique')
    ]

    @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    def _compute_total_marks(self):
        for record in self:
            record.total_marks = record.mathematics + record.science + record.social_science + record.english +record.hindi

    @api.depends('total_marks')
    def _compute_percentage(self):
        for record in self:
            record.percentage = record.total_marks / 5.0

    @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    def _compute_result(self):
        for record in self:
            if (record.mathematics > 35 and record.science > 35 and
               record.social_science > 35 and record.english > 35 and record.hindi > 35):
                record.result = 'Pass'
            else:
                record.result = 'Fail'

    def name_get(self):
        result = []
        for rec in self:
            name = rec.firstname+' '+rec.lastname
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