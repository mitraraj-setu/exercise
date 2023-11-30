from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offers'
    _order = 'price desc'

    price = fields.Float(string='Offered Price')
    offer_status = fields.Selection(string='Status', selection=[('accepted','Accepted'),('refused','Refused')], copy=False, default='N/A')
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    property_type_id = fields.Many2one('estate.property.type')
    # property_state = fields.Selection(related='property_id.state')

    _sql_constraints = [
        ('check_offer_price', 'CHECK(offer_price > 0)', 'The offer price must be strictly positive')
    ]

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     if self.env.context.get('property_name'):
    #         property_offers = self.env['estate.property'].search([('name', '=', self.env.context.get('property_name'))])
    #         args = (args or []) + [('id', 'not in', property_offers.partner_id.mapped('id'))]
    #         return self._search(args, limit=limit, access_rights_uid=name_get_uid)
    #     return super()._name_search(name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)

    @api.model
    def create(self, vals_list):
        temp = super().create(vals_list)
        self.property_id.state = 'offer received'
        return temp

    def write(self, vals):
        temp = super().write(vals)
        return temp

    def unlink(self):
        temp = super().unlink()
        return temp

# Buttons
    def button_accept_offer(self):
        if not self.offer_status:
            self.offer_status = 'accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id.id
        self.property_id.state = 'offer accepted'

    def button_reject_offer(self):
        if not self.offer_status:
            self.offer_status = 'refused'
        # elif self.status is 'accepted':
        #     self.status = 'refused'
        self.property_id.selling_price = 0
        self.property_id.buyer_id = ''
