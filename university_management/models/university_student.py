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

    teacher_count = fields.Integer(string='Teachers', compute='_compute_teacher_count')
    teacher_ids = fields.Many2many('university.teacher', 'teacher_student_rel', string='Teachers')
    badge_ids = fields.Many2many('university.student.badge')
    result_ids = fields.One2many('university.student.result', 'student_id')

    _sql_constraints = [
        ('check_student_aadhaar_no', 'unique(student_aadhaar_no)', 'Aadhaar Number must be Unique'),
        ('check_student_enrollment_no', 'unique(enrollment_no)', 'Enrollment Number must be Unique')
    ]

    # @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    # def _compute_total_marks(self):
    #     for record in self:
    #         record.total_marks = record.mathematics + record.science + record.social_science + record.english +record.hindi
    #
    # @api.depends('total_marks')
    # def _compute_percentage(self):
    #     for record in self:
    #         record.percentage = record.total_marks / 5.0
    #
    # @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    # def _compute_result(self):
    #     for record in self:
    #         if (record.mathematics > 35 and record.science > 35 and
    #            record.social_science > 35 and record.english > 35 and record.hindi > 35):
    #             record.result = 'Pass'
    #         else:
    #             record.result = 'Fail'

    @api.depends('teacher_ids')
    def _compute_teacher_count(self):
        self.teacher_count = len(self.teacher_ids)

    def button_university_teacher_count(self):
        action = self.env['ir.actions.act_window']._for_xml_id('university_management.university_teacher_count_action')
        action['domain'] = [('id', 'in', self.teacher_ids.ids)]
        return action

    # def button_student_result_wizard(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #         'name': _('Result'),
    #         'view_mode': 'form',
    #         'res_model': 'university.student.result.wizard',
    #         'view_id': self.env.ref('university_management.university_student_result_wizard_form_view').id,
    #     }

    def student_result(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "university_management.university_student_result_action")
        action['domain'] = [('student_id','=', self.id)]
        return action

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
