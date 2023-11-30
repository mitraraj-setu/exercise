from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Real Estate Properties list'
    _order = 'id desc'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal Code')
    date_availability = fields.Date(string='Availability Date', copy=False)
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    status = fields.Char(string='Status')

    bedrooms = fields.Integer(string='No of Bedrooms', default=2)
    living_areas = fields.Integer(string='No of Living Areas')
    living_area = fields.Float(string='Living Area', default=0)
    facades = fields.Integer(string='No of Facades')
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_areas = fields.Integer(string='No of Gardens')
    garden_area = fields.Float(string='Garden Area', default=0)
    garden_orientation = fields.Selection(string='Garden Orientation',
                                          selection=[('east', 'East'),
                                                     ('west', 'West'),
                                                     ('north', 'North'),
                                                     ('south', 'South')])
    total_area = fields.Float(string='Total Area', compute='_compute_total_area', store=True)
    state = fields.Selection(string='State', selection=[('new', 'New'),
                                                        ('offer received', 'Offer Received'),
                                                        ('offer accepted', 'Offer Accepted'),
                                                        ('sold', 'Sold'),
                                                        ('cancelled', 'Cancelled')])
    best_price = fields.Float(string='Best Offer Price', compute='_compute_best_price', default=0)

    tag_ids = fields.Many2many('estate.property.tag', 'tag_property_rel', 'property', 'tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    salesman_id = fields.Many2one('res.users', string='Salesperson', required=True, default=lambda self: self.env.uid)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    type_id = fields.Many2one('estate.property.type')

    _sql_constraints = [
        ('check_name', 'unique(name)', 'The property name must be unique'),
        ('check_expected_price', 'CHECK(expected_price > 0)', 'The property expected price must be strictly positive')
        # ('check_selling_price', 'CHECK(selling_price > 0)', 'The property selling price must be positive'),
    ]

    # def name_get(self):
    #     print('estate.property model  -> name_get() -> called')
    #     result = []
    #     for property in self:
    #         name = property.name or ''
    #         if property.garden_orientation:
    #             name += ' (' + property.garden_orientation + ')'
    #         result.append((property.id, name))
    #     return result

    # def _cron_auto_property_invoice(self):
    #     prop_ids = self.search([('state','=','sold')])
    #     for prop in prop_ids:
    #         create_invoice_wizard = self.env['sale.advance.payment.inv'].create()
    #         try:
    #             create_invoice_wizard.create_invoices()
    #         except Exception as e:
    #             continue


    def button_open_invoice(self):
        action = self.env['ir.actions.actions']._for_xml_id('account.action_move_out_invoice_type')
        action['domain'] = [('property_id', '=', self.id)]
        return action

    @api.model
    def create(self, vals_list):
        temp = super().create(vals_list)
        # temp = self.create({{'name':'abc', 'postcode':'5684'},
        #                    {'name':'abcd', 'postcode':'5685'}})
        self.state = 'new'
        return temp

    def write(self, vals):
        temp = super().write(vals)
        return temp

    # def unlink(self):
    #     temp = super().unlink()
    #     return temp

    def unlink(self):
        if self.state == 'cancelled':
            temp = super().unlink()
            return temp
        else:
            raise UserError(_("New or cancelled properties cannot be deleted"))

    @api.ondelete(at_uninstall=False)
    def _unlink_if_not_new_or_cancelled(self):
        if self.search([('state','in',['new offer received','cancelled'])]):
            raise UserError(_('You cannot delete a new or cancelled property.'))

    # Buttons
    def button_garden(self):
        if self.garden:
            self.write({'garden': False})
        else:
            self.write({'garden': True})

    def button_sold_property(self):
        if not self.status:
            self.status = 'Sold'
            self.state = 'sold'
        elif self.status == 'Cancelled':
            raise UserError(_("Cancelled properties cannot be sold"))

    def button_cancel_property(self):
        if not self.status:
            self.status = 'Cancelled'
            self.state = 'cancelled'
        elif self.status == 'Sold':
            raise UserError(_("Sold properties cannot be cancelled"))

    # def button_estate_property_invoice(self):
    #     action = self.env['ir.actions.act_window']._for_xml_id('real_estate.estate_property_invoice_action')
    #     action['domain'] = [('id', 'in', self.student_ids.ids)]
    #     return action

# Compute Field Methods--------------------------------------------------------------------------------------
    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            if len(record.offer_ids) == 0:
                record.best_price = 0.0
                break
            record.best_price = max([i for i in record.offer_ids.mapped('price')])
            break

    @api.constrains('expected_price', 'selling_price')
    def _check_lowest_selling_price(self):
        if self.selling_price != 0:
            if self.selling_price < (0.9 * self.expected_price):
                raise ValidationError(_("The selling price must be more than 90 percent of the expected price"))

    @api.constrains('selling_price')
    def _check_lowest_selling_price(self):
        if self.selling_price != 0:
            if self.selling_price < 0:
                raise ValidationError(_("The selling price must be positive"))

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'

    def _inverse_garden(self):
        if self.garden == False:
            self.garden_area = 0
