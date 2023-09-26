from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Students List'

    enrollment_no = fields.Integer(string='Enrollment No', required=True)
    firstname = fields.Char(string='Firstname', required=True)
    lastname = fields.Char(string='Lastname', required=True)
    guardian_name = fields.Char(string="Guardian's name", required=True)
    phone = fields.Char(string='Contact Number')
    guardian_contact = fields.Char(string="Guardian's Contact")
    email = fields.Char(string='Email ID')
    date_of_birth = fields.Date(string='Student Birthdate', copy=False)
    joining_date = fields.Date(string='Student Joining Date')
    standard = fields.Integer(string='Standard')
    student_aadhaar_no = fields.Integer(string='Student Aadhaar No', copy=False)
    mathematics = fields.Float(string='Maths')
    science = fields.Float(string='Science')
    social_science = fields.Float(string='Social Science')
    english = fields.Float(string='English')
    hindi = fields.Float(string='Hindi')
    total_marks = fields.Float(string='Total Marks', compute='_compute_total_marks', store=True)
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    result =

    _sql_constraints = [
        ('check_student_aadhaar_no', 'unique(student_aadhaar_no)', 'Aadhaar Number must be Unique')
    ]

    @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    def _compute_total_marks(self):
        for record in self:
            record.total_marks = record.mathematics + record.science + record.social_science + record.english +record.hindi

    @api.depends('total_marks')
    def _compute_percentage(self):
        for record in self:
            record.percentage = record.total_marks/5.0

