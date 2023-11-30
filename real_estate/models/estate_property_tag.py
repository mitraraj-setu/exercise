from odoo import fields, models, api

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tags'
    _order = 'name'

    name = fields.Char(string='Tag Name', required=True)

    _sql_constraints = [
        ('check_property_tag_name', 'unique(name)', 'The property tag name must be unique')
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