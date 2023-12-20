from odoo import fields, models, api, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit_check = fields.Selection(string='State', selection=[('low', 'Low'),
                                                                   ('equal', 'Equal'),
                                                                   ('high', 'High')], invisible=True)

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            po_line = self.env['purchase.order.line'].search([('product_id', '=', values.get('product_id'))], order='id desc', limit=1)
            if values.get('price_unit') < po_line.price_unit:
                values['price_unit_check'] = 'low'
            elif values.get('price_unit') > po_line.price_unit:
                values['price_unit_check'] = 'high'
            elif values.get('price_unit') == po_line.price_unit:
                values['price_unit_check'] = 'equal'
        return super().create(vals_list)

    def write(self, values):
        temp = super().write(values)
        # if values.get('price_unit'):
        #     po_line = self.env['purchase.order.line'].search(['|', ('id', '!=', self.id), ('product_id', '=', values.get('product_id')),
        #                                                       ('product_id', '=', self.product_id.id)], order='id desc', limit=1)
        #     if values.get('price_unit') < po_line.price_unit:
        #         values['price_unit_check'] = 'low'
        #     elif values.get('price_unit') > po_line.price_unit:
        #         values['price_unit_check'] = 'high'
        #     elif values.get('price_unit') == po_line.price_unit:
        #         values['price_unit_check'] = 'equal'
        # if values.get('product_id'):
        #     po_line = self.env['purchase.order.line'].search([('id', '!=', self.id),
        #                                                       ('product_id', '=', values.get('product_id'))], order='id desc', limit=1)
        #     if self.price_unit < po_line.price_unit:
        #         values['price_unit_check'] = 'low'
        #     elif self.price_unit > po_line.price_unit:
        #         values['price_unit_check'] = 'high'
        #     elif self.price_unit == po_line.price_unit:
        #         values['price_unit_check'] = 'equal'
        return temp

    def action_product_price_unit_history(self):
        context = self.env.context.copy()
        context.update({'default_purchase_line_id': self.id})
        current_po_line = self.env['purchase.order.line'].browse(self.env.context.get('active_id'))
        unit_prices = self.env['purchase.order.line'].search(
            [('id', '!=', current_po_line.id), ('product_id', '=', current_po_line.product_id.id)], order='id desc',
            limit=5).mapped('price_unit')
        wiz = self.env['unit.price.history.wizard'].create({
            'purchase_line_id': self.id,
            'wiz_lines':  [(0, 0, {'price': 10,}) for price in unit_prices]
        })
        return {
            'type': 'ir.actions.act_window',
            'target': 'new',
            'name': _('History'),
            'view_mode': 'form',
            'res_model': 'unit.price.history.wizard',
            'view_id': self.env.ref('Sale_Order_Modified.unit_price_history_wizard_form_view').id,
            'context': context,
            'res_id' : wiz.id,
            'domain': [('id','=', wiz.id)]
        }

    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        for rec in self:
            preceding_po_line = self.env['purchase.order.line'].search(
                [('id', '<', rec._origin.id), ('product_id', '=', self.product_id.id)], order='id desc', limit=1)
            if self.price_unit < preceding_po_line.price_unit:
                self.price_unit_check = 'low'
            elif self.price_unit > preceding_po_line.price_unit:
                self.price_unit_check = 'high'
            elif self.price_unit == preceding_po_line.price_unit:
                self.price_unit_check = 'equal'
            succeeding_po_line = self.env['purchase.order.line'].search(
                [('id', '>', rec._origin.id), ('product_id', '=', self.product_id.id)], limit=1)
            if self.price_unit < succeeding_po_line.price_unit:
                succeeding_po_line.price_unit_check = 'high'
            elif self.price_unit > succeeding_po_line.price_unit:
                succeeding_po_line.price_unit_check = 'low'
            elif self.price_unit == succeeding_po_line.price_unit:
                succeeding_po_line.price_unit_check = 'equal'

    # @api.ondelete(at_uninstall=False)
    # def _unlink_and_call_onchange_price_unit(self):
    #     for line in self:
