from odoo import fields, models, api


class UpdateQuantityWizard(models.TransientModel):
    _name = 'update.quantity.wizard'

    wiz_lines = fields.One2many('update.quantity.wizard.line', 'wiz_id')
    location_id = fields.Many2one('stock.location')

    def update_quantity(self):
        for line in self.wiz_lines:
            product = line.product_id
            location = self.location_id
            quant = self.env['stock.quant'].search([('location_id', '=', location.id), ('product_id', '=', product.id)])
            if quant:
                quant.write({'inventory_quantity':line.quantity})
                quant.action_apply_inventory()
            else:
                vals = {'product_id': product.id,
                        'location_id': location.id,
                        'inventory_quantity': line.quantity}
                quant = self.env['stock.quant'].create(vals)
                quant.action_apply_inventory()

    @api.model
    def create(self, vals):
        res = super().create(vals)
        return res



class UpdateQuantityWizardLine(models.TransientModel):
    _name = 'update.quantity.wizard.line'

    wiz_id = fields.Many2one('update.quantity.wizard')
    product_id = fields.Many2one('product.product')
    quantity = fields.Float()

