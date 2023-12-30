from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    no_of_days = fields.Boolean(string='No of days')
    days = fields.Integer(string='Days')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        no_of_days = IrDefault.get('res.config.settings', 'days')
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
