
from odoo import models, fields , api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    credit_point_for_le_500 = fields.Float(
        string="Credit Points (%) for Orders ≤ 500",
        config_parameter='setu_credit_point.credit_point_for_le_500',
        help="Set the credit points percentage for orders ≤ 500."
    )

    credit_point_for_gt_500 = fields.Float(
        string="Credit Points (%) for Orders > 500",
        config_parameter='setu_credit_point.credit_point_for_gt_500',
        help="Set the credit points percentage for orders > 500."
    )

    def set_values(self):

        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('setu_credit_point.credit_point_for_le_500', self.credit_point_for_le_500)
        self.env['ir.config_parameter'].sudo().set_param('setu_credit_point.credit_point_for_gt_500', self.credit_point_for_gt_500)

    @api.model
    def get_values(self):

            res = super(ResConfigSettings, self).get_values()
           
            res.update({
                'credit_point_for_le_500': float(self.env['ir.config_parameter'].sudo().get_param('setu_credit_point.credit_point_for_le_500', default=1.0)),
                'credit_point_for_gt_500': float(self.env['ir.config_parameter'].sudo().get_param('setu_credit_point.credit_point_for_gt_500', default=2.0)),
            })
            return res













