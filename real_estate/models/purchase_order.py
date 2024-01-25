from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # @api.model
    # def create(self, vals):
        # if vals.get('name', 'New') == 'New':
        #     vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order') + ' ('+ self.env.company.currency_id.name +')'

        # lines = super().create(vals)
        # lines['name'] = lines['name'] + ' ('+ self.env.company.currency_id.name +')'
        # return lines

    # def write(self, vals):
    #     # vals['name'] = 'New'
    #     name = vals['name']
    #
    #     company = vals['company_id']
    #
    #     vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order') + ' ('+ company.currency_id.name +')'
    #
    #     return super().write(vals)