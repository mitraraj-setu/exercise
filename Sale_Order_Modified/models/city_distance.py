from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class CityDistance(models.Model):
    _name = 'city.distance'

    from_loc = fields.Char(string='Source City')
    to_loc = fields.Char(string='Destination City')
    distance = fields.Float(string='Distance')
    carrier_id = fields.Many2one('delivery.carrier', string='Service')
    delivery_charges = fields.Float(string='Charge')

    # @api.constrains('from_loc', 'to_loc', 'distance', 'carrier_id')
    # def _check_duplicate(self):
    #     dup_distance = self.env['sale.commission'].search(
    #         ['|', '|', ('carrier_id', '=', self.carrier_id), ('distance', '!=', self.distance), '|',
    #          '&', ('from_loc', '=ilike', self.to_loc), ('to_loc', '=ilike', self.from_loc),
    #          '&', ('from_loc', '=ilike', self.from_loc), ('to_loc', '=ilike', self.to_loc)])
    #     if dup_distance:
    #         raise ValidationError(_("Duplicate record"))

    @api.model
    def create(self, vals_list):
        dup_distance = (self.search(['|', '|', ('carrier_id', '=', vals_list.get('carrier_id')), ('distance', '!=', vals_list.get('distance')),
                                     '&', ('from_loc', '=ilike', vals_list.get('to_loc')), ('to_loc', '=ilike', vals_list.get('from_loc'))]) or
                        self.search(['|', '|', ('carrier_id', '=', vals_list.get('carrier_id')), ('distance', '!=', vals_list.get('distance')),
                                     '&', ('from_loc', '=ilike', vals_list.get('from_loc')), ('to_loc', '=ilike', vals_list.get('to_loc'))]))
        if dup_distance:
            raise ValidationError(_("Duplicate record"))
        return super().create(vals_list)

    def write(self, vals_list):
        for val in vals_list.keys():
            distance = self.env['city.distance']
            for vals in self.env['city.distance'].search_read([('to_loc', '=', vals_list.get(val))],['id']):
                for id in vals.values():
                    record = distance.browse(id)
                    if record['from_loc'] == self['from_loc'] or vals_list.get('from_loc'):
                        raise ValidationError(_("Duplicate record"))
            for vals in self.env['city.distance'].search_read([('from_loc', '=', vals_list.get(val))],['id']):
                for id in vals.values():
                    record = distance.browse(id)
                    if record['to_loc'] == self['to_loc'] or vals_list.get('to_loc'):
                        raise ValidationError(_("Duplicate record"))
        temp = super().write(vals_list)
        return temp

    def unlink(self):
        temp = super().unlink()
        return temp
