from odoo import models, fields


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def button_sold_property(self):

        for record in self:
            self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': record.offer_ids.partner_id.mapped('id')[0],
                'journal_id': 1,
                'invoice_line_ids': [
                    (0, 0, {'name': record.name, 'quantity': 1, 'price_unit': ((record.selling_price * 0.06) + 100)}),
                    (0, 0, {'name': record.name, 'quantity': 1.5, 'price_unit': ((record.selling_price * 0.06) + 100)})],
                'property_id': record.id
            })

        return super().button_sold_property()


