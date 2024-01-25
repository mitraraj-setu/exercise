import csv
from odoo import fields, models, api
from odoo.fields import Datetime


class StockQuant(models.Model):
    _inherit = 'stock.quant'


    # def read_file(self, file):
    #     # file = "/home/vivek/workspace/inventory_adj_1.csv"
    #     # vals_list = []
    #
    #     with open(file) as f:
    #         csv_file = csv.DictReader(f)
    #         for val in csv_file:
    #             product = self.env['product.product'].search([('name', '=ilike', val.get('Product'))])
    #             loc_str = val.get('Location')
    #             loc_list = loc_str.rsplit("/")
    #             if len(loc_list) == 2:
    #                 loc_name = loc_list[1]
    #                 loc_location_id = loc_list[0]
    #             else:
    #                 loc_name = loc_name[-1]
    #                 loc_location_id = loc_list[-2]
    #             location = self.env['stock.location'].search([('location_id', '=ilike', loc_location_id), ('name', '=ilike', loc_name)])
    #             quants = self.search([('product_id', '=', product.id),
    #                                   ('location_id', '=', location.id)])
    #             if quants:
    #                 quants.write({'inventory_quantity': float(val.get('Counted Quantity')), 'inventory_date': Datetime.now()})
    #                 quants.action_apply_inventory()
    #                 product.write({'standard_price': float(val.get('Cost'))})
    #             else:
    #                 self.env['stock.quant'].create({
    #                     'product_id': product.id,
    #                     'inventory_quantity': int(val.get('Counted Quantity')),
    #                     'location_id': location.id
    #                 }).action_apply_inventory()
    #     f.close()




