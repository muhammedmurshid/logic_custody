from odoo import models, fields, api, _


class LogicCustodyForm(models.Model):
    _name = 'logic.custody'
    _description = 'Logic Custody'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')

