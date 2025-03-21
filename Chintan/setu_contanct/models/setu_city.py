from odoo import api, fields , models
import logging

_logger = logging.getLogger(__name__)

class SetuCity(models.Model):
    _name='setu.city'
    _description='City'
    _inherit = 'mail.thread'

    name = fields.Char(string="City", required=True, tracking=True)
    state_id = fields.Many2one('setu.state', string="State", required=True)
    country_id = fields.Many2one('setu.country', string="Country", related="state_id.country_id", store=True)
    
    @api.model
    def create(self, vals):
        _logger.info(vals)
        res = super(SetuCity, self).create(vals)

        return res
