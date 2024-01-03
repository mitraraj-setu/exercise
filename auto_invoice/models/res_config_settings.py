from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    no_of_days = fields.Boolean(string='No of days')
    days = fields.Integer(string='Days')

    @api.constrains('days')
    def _check_days(self):
        if self.days < 0:
            raise ValidationError(_("Number of Days must be zero or positive"))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        no_of_days = IrDefault.get('res.config.settings', 'no_of_days')
        days = IrDefault.get('res.config.settings', 'days')
        res.update(
            no_of_days=no_of_days,
            days=days)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrDefault = self.env['ir.default'].sudo()
        IrDefault.set('res.config.settings', 'days', self.days)
        IrDefault.set('res.config.settings', 'no_of_days', self.no_of_days)
