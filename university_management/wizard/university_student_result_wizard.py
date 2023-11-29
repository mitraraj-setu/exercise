from odoo import fields, models, api


class UniversityStudentResultWizard(models.TransientModel):
    _name = 'university.student.result.wizard'

    student_id = fields.Many2one('university.student', 'Student')
    semester = fields.Selection(string='Semester', selection=[('first', 'First'),
                                                              ('second', 'Second'),
                                                              ('third', 'Third'),
                                                              ('fourth', 'Fourth')])
    mathematics = fields.Float(string='Maths')
    science = fields.Float(string='Science')
    social_science = fields.Float(string='Social Science')
    english = fields.Float(string='English')
    hindi = fields.Float(string='Hindi')


    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['student_id'] = self.env.context.get('active_id')
        return res

    def submit_result(self):
        result_obj = self.env["university.student.result"]
        result_id = result_obj.search([('student_id','=', self.student_id.id), ('semester','=', self.semester)])
        vals = {
            'student_id': self.student_id.id,
            'semester': self.semester,
            'mathematics': self.mathematics,
            'social_science': self.social_science,
            'english': self.english,
            'hindi': self.hindi
        }
        result_id.write(vals) if result_id else result_obj.create(vals)
