from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_compare, float_round

class CalculationResultWizard(models.TransientModel):
    _name = 'calculation.result.wizard'

    first_value = fields.Float(string='First Value', digits=(12,8))
    second_value = fields.Float(string='Second Value', digits=(12,8))
    result = fields.Float()

    def submit_result(self):
        operator = self.env.context.get('operator')
        vals = {
            'first_value': self.first_value,
            'second_value': self.second_value,
        }
        if operator == 'do_div' and not self.second_value:
            raise ValidationError(_('Second value cannot be zero'))

        self.result = getattr(self.env['calculation'],operator)(self.first_value, self.second_value)
        vals.update({'operation': operator, 'result': self.result})
        self.env['calculation'].create(vals)
        return self.display()


    def display(self):
        return {
            'type': 'ir.actions.act_window',
            'target': 'new',
            'name': _('You have chosen %s operation') % (self.env.context.get('operator')),
            'view_mode': 'form',
            'context': {'default_first_value': self.first_value, 'default_second_value': self.second_value, 'default_result': self.result},
            'res_model': 'calculation',
            'view_id': self.env.ref('Sale_Order_Modified.result_display_wizard_form_view').id,
        }