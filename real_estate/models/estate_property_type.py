from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Types'
    _order = 'name'

    name = fields.Char(string='Property Type', required=True)
    sequence = fields.Integer(string='Sequence')
    # property_type_id = fields.One2many('estate.property')
    property_ids = fields.One2many('estate.property', 'type_id')
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer(string='Offers', compute='_compute_offer_count', store=True)
    properties_count = fields.Integer(string='Properties', compute='_compute_properties_count')

    _sql_constraints = [
        ('check_property_type_name', 'unique(name)', 'The property name must be unique')
    ]

    @api.model
    def create(self, vals_list):
        temp = super().create(vals_list)
        return temp

    def write(self, vals):
        temp = super().write(vals)
        return temp

    def unlink(self):
        temp = super().unlink()
        return temp

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        self.offer_count = len(self.offer_ids)

    def button_show_offers(self):
        action = self.env['ir.actions.act_window']._for_xml_id('real_estate.count_and_show_offers')
        action['domain'] = [('id', 'in', self.offer_ids.ids)]
        return action


    @api.depends('offer_ids')
    def _compute_properties_count(self):
        self.properties_count = len(self.property_ids)

    def button_show_properties(self):
        action = self.env['ir.actions.act_window']._for_xml_id('real_estate.count_and_show_properties')
        action['domain'] = [('id', 'in', self.property_ids.ids)]
        return action