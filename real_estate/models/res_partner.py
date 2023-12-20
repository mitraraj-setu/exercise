from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        if self.env.context.get('property_id'):
            property_offers = self.env['estate.property.offer'].search([('property_id', '=', self.env.context.get('property_id'))])
            args = (args or []) + [('id', 'not in', property_offers.partner_id.mapped('id'))]
            return self._search(args, limit=limit, access_rights_uid=name_get_uid)
        return super()._name_search(name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)