from odoo import models, fields

class DemoCustom(models.Model):
    _name = 'demo.custom'
    _description = 'Demo Custom'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
