#-*- coding:utf-8 -*-
from odoo import models, fields, _, api
from odoo.exceptions import Warning
import pandas

from odoo.exceptions import ValidationError


# from odoo.tools.safe_eval import safe_eval
class SetuPythonEditor(models.Model):
    _name = "setu.python.editor"
    _description = "setu.python.editor"

    name = fields.Char(string='Name', size=1024, required=True)
    code = fields.Text(string='Python Code')
    result = fields.Text(string='Result')
    editor_type = fields.Selection([('python', 'Python'), ('sql', 'PSQL')],
                                     string='Editor Type', required=True, default='python')

    def get_code(self):
        return {'code': self.code, 'output': self.result, 'self': self.id, 'name': self.name, 'editor_type': self.editor_type}

    def execute_code(self, args = False):
        if self.editor_type == 'python':
            if args:
                self.code = args[0]
                self.result = args[1]
            localdict = {'self': self, 'user_obj': self.env.user}
            for obj in self:
                try:
                    res = exec(obj.code, localdict)
                    if localdict.get('result', False):
                        self.write({'result': localdict['result']})
                        return self.result
                    else:
                        self.write({'result': ''})
                        return self.result
                except Exception as e:
                    return e
        else:
            if args:
                self.code = args[0]
                self.result = args[1]
                try:
                    query = self.code
                    self._cr.execute(query)
                    if 'update' in query or 'Update' in query:
                        self.write({'result': 'Update Successfully'})
                        return 'Update Successfully'
                        pass
                    if 'delete' in query or 'Delete' in query:
                        self.write({'result': 'Deleted Successfully'})
                        return 'Deleted Successfully'
                        pass
                    if 'Truncate' in query or 'truncate' in query:
                        self.write({'result': 'Truncate Successfully'})
                        return 'Truncate Successfully'
                        pass
                    datas = self._cr.dictfetchall()
                    df = pandas.DataFrame(datas)
                    datas = df.to_html(table_id='output_ed', index=False)
                    self.write({'result': datas})
                    return datas
                except Exception as e:
                    raise ValidationError(e)
