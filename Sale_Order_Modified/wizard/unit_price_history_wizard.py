from odoo import fields, models, api, _
import logging
_logger = logging.getLogger('__name__')


class UnitPriceHistoryWizard(models.TransientModel):
    _name = 'unit.price.history.wizard'

    purchase_line_id = fields.Many2one('purchase.order.line')
    wiz_lines = fields.One2many('unit.price.history.wizard.line', 'wiz_id')

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        current_po_line = self.env['purchase.order.line'].browse(self.env.context.get('active_id'))
        unit_prices = self.env['purchase.order.line'].search(
            [('id', '!=', current_po_line.id), ('product_id', '=', current_po_line.product_id.id)], order='id desc', limit=5).mapped('price_unit')
        _logger.info('dsadadsadasdasdas {}'.format(unit_prices))
        res['wiz_lines'] = [(0, 0, {
            'price': price,
            'selected' : False
        }) for price in unit_prices]
        return res

    def select_price(self):
        current_po_line = self.env['purchase.order.line'].browse(self.env.context.get('active_id'))
        selected_price = self.wiz_lines.search([('selected', '=', True)]).mapped('price')
        if selected_price:
            current_po_line.write({'price_unit': selected_price[0]})

    @api.model
    def create(self, vals):
        res = super().create(vals)
        print(res)
        return res


class UnitPriceHistoryWizardLine(models.TransientModel):
    _name = 'unit.price.history.wizard.line'

    wiz_id = fields.Many2one('unit.price.history.wizard')
    price = fields.Float()
    selected = fields.Boolean()
