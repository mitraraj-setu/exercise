from odoo import api, fields, models, modules, tools, _


class Module(models.Model):
    _inherit = "ir.module.module"

    def _button_immediate_function(self, function):
        res = super(Module, self)._button_immediate_function(function)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
            'params': {'menu_id': 5},
        }
