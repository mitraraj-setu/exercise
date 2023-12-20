from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'ProjectName.TableName'

    name = fields.Char()
