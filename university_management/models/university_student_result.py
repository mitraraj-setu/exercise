from odoo import fields, models, api


class UniversityStudentResult(models.Model):
    _name = 'university.student.result'
    _description = 'University Student Results'

    student_id = fields.Many2one('university.student','Student')
    semester = fields.Selection(string='Semester', selection=[('first', 'First'),
                                                        ('second', 'Second'),
                                                        ('third', 'Third'),
                                                        ('fourth', 'Fourth')])
    mathematics = fields.Float(string='Maths')
    science = fields.Float(string='Science')
    social_science = fields.Float(string='Social Science')
    english = fields.Float(string='English')
    hindi = fields.Float(string='Hindi')
    total_marks = fields.Float(string='Total Marks', compute='_compute_total_marks', store=True)
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    result = fields.Char(string='Result', compute='_compute_result', store=True)

    @api.depends('mathematics', 'science', 'social_science', 'english', 'hindi')
    def _compute_total_marks(self):
        for record in self:
            record.total_marks = record.mathematics + record.science + record.social_science + record.english + record.hindi

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