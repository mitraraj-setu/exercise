from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError
import datetime


class SaleCommission(models.Model):
    _name = 'sale.commission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sale Commission rules list'

    user_id = fields.Many2one('res.users', string="Salesperson", store=True, required=True)
    sequence = fields.Integer(string='Sequence')
    product_temp_id = fields.Many2one('product.template', string='Product Template', required=True, copy=False)
    product_id = fields.Many2one('product.product', string='Product')
    rule = fields.Selection(string='Commission Rule', selection=[('order', 'Order'),
                                                                 ('product', 'Product')], required=True)
    start_date = fields.Date(string='Start Date', copy=False)
    end_date = fields.Date(string='End Date', copy=False)
    minimum = fields.Float(string='Minimum Amount', copy=False)
    maximum = fields.Float(string='Maximum Amount', copy=False)
    # minimum = fields.Integer(string='Minimum Quantity', copy=False)
    # maximum_qty = fields.Integer(string='Maximum Quantity', copy=False)
    commission_type = fields.Selection(string='Commission Type', selection=[('fixed', 'Fixed'),
                                                                            ('percentage', 'Percentage')], required=True, copy=False)
    fixed_amount = fields.Float(string='Fixed Amount', required=True, copy=False)
    percentage = fields.Float(string='Percentage', required=True, copy=False)

    @api.constrains('maximum', 'minimum')
    def _check_min_and_max_amount(self):
        if self.maximum < self.minimum:
            raise ValidationError(_("The maximum amount must be more than the minimum amount"))

    # @api.constrains('maximum_qty', 'minimum')
    # def _check_min_and_max_quantity(self):
    #     if self.maximum_qty < self.minimum:
    #         raise ValidationError(_("The maximum quantity must be more than the minimum quantity"))

    @api.constrains('start_date', 'end_date')
    def _check_start_and_end_date(self):
        if self.start_date > self.end_date:
            raise ValidationError(_("The start date must be before the end date"))

    @api.constrains('user_id','product_temp_id','rule','start_date','end_date','minimum','maximum')
    def _check_duplicate(self):
        dup_distance = self.env['sale.commission'].search(
            [('id','!=', self.id), ('user_id', '=', self.user_id.id),
             ('product_temp_id', '=', self.product_temp_id.id),
             ('rule', '=', self.rule),
             ('start_date', '=', self.start_date),
             ('end_date', '=', self.end_date), '|',
             ('minimum', '=', self.minimum),
             ('maximum', '=', self.maximum)])
        if dup_distance:
            raise ValidationError(_("Duplicate record"))

    @api.model
    def create(self, vals_list):
        return super().create(vals_list)

    def write(self, vals):
        temp = super().write(vals)
        return temp

    def unlink(self):
        return super().unlink()
