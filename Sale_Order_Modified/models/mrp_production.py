from odoo import fields, models, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _prepare_stock_lot_values(self):
        res = super()._prepare_stock_lot_values()
        adder = self.product_id.lot_name
        if self.product_id.lot_name_type == 'prefix':
            if adder:
                res['name'] = adder + res['name']
        if self.product_id.lot_name_type == 'suffix':
            if adder:
                res['name'] = res['name'] + adder
        return res
