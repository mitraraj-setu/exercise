from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    buyer = fields.Boolean(string='Buyer')
    seller = fields.Boolean(string='Seller')

    # def _find_children(self, customer):
    #     children = []
    #     for child in customer.child_ids:
    #         if child.child_ids:
    #             temp = self._find_children(child)
    #             for child in temp:
    #                 children.append(child.name)
    #         else:
    #             children.append(child.name)
    #     return children

    def _find_children(self, customer):
        children = []
        childrens = customer.child_ids
        while childrens:
            if childrens[0].child_ids:
                childrens += childrens[0].child_ids
            else:
                children.append(childrens[0].name)
            childrens -= childrens[0]
        return children
