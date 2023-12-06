from odoo import api, fields, models, _


class LogicCustodyType(models.Model):
    _name = 'logic.custody.type'
    _description = 'Custody Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    is_class_room = fields.Boolean(string='Is Class Room', )
    perishable = fields.Boolean(string='Perishable')
    scrappable = fields.Boolean(string='Scrappable')
    date = fields.Date(string='Date', default=fields.Date.today)
