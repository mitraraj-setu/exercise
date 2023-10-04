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

    pass_students_count = fields.Integer(string='Pass Students Count', compute='_compute_pass_student_count')
    fail_students_count = fields.Integer(string='Fail Students Count', compute='_compute_fail_student_count')
    total_students_count = fields.Integer(string='Total Students Count', compute='_compute_total_student_count')
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

# Total students count---------------------------------------------------------------
    @api.depends('student_ids')
    def _compute_total_student_count(self):
        self.total_students_count = len(self.student_ids)

    def button_university_total_student_count(self):
        action = self.env['ir.actions.act_window']._for_xml_id('university_management.university_total_student_count_action')
        action['domain'] = [('id', 'in', self.student_ids.ids)]
        return action

# Fail students count----------------------------------------------------------------
    @api.depends('student_ids')
    def _compute_fail_student_count(self):
        student_ids = self.student_ids.filtered(lambda student: student.result == 'Fail')
        self.fail_students_count = len(student_ids)

    def button_university_fail_student_count(self):
        action = self.env['ir.actions.act_window']._for_xml_id('university_management.university_fail_student_count_action')
        student_ids = self.student_ids.filtered(lambda student: student.result=='Fail')
        action['domain'] = [('id', 'in', student_ids.ids)]
        return action

# Pass students count----------------------------------------------------------------
    @api.depends('student_ids')
    def _compute_pass_student_count(self):
        student_ids = self.student_ids.filtered(lambda student: student.result == 'Pass')
        self.pass_students_count = len(student_ids)

    def button_university_pass_student_count(self):
        action = self.env['ir.actions.act_window']._for_xml_id('university_management.university_pass_student_count_action')
        student_ids = self.student_ids.filtered(lambda student: student.result == 'Pass')
        action['domain'] = [('id', 'in', student_ids.ids)]
        return action

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