from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class UniversityStudentBadge(models.Model):
    _name = 'university.student.badge'
    _description = 'University Student Badges List'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Badge')
    student_count = fields.Integer(string='Students', compute='_compute_student_count', store=True)

    student_ids = fields.One2many('university.student', 'badge_ids')

    _sql_constraints = [
        ('check_student_badge', 'unique(name)', 'Badge name must be Unique')
    ]

    @api.depends('student_ids')
    def _compute_student_count(self):
        self.student_count = len(self.student_ids)

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