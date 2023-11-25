from odoo import fields, models, api, _


class LogicCustodyProperties(models.Model):
    _name = 'logic.custody.properties'
    _description = 'Custody Properties'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'property_id'

    property_id = fields.Many2one('logic.total.assets', string='Name')
    serial_number = fields.Char(string='Serial Number')
    property_from = fields.Selection(
        [('empty', 'No Connection'), ('product', 'Products')], default='empty', string='Property From'
    )
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=1)
    current_user_id = fields.Many2one('res.users', string='Current User')
    purchase_price = fields.Float(string='Purchase Price')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    description = fields.Html(string='Description')
    property_photo = fields.Binary(string='Property Photo')
    rep_ids = fields.One2many('repair.logic.property', 'rep_id', string='Rep')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'), ('scrap', 'Scrap')], default='draft', string='State',
        tracking=True
    )
    added_date = fields.Date(string='Added Date', default=fields.Date.today())

    def action_confirm(self):
        self.state = 'confirm'

    def action_scrap(self):
        self.state = 'scrap'

    def action_return_to_draft(self):
        self.state = 'draft'


class RepairCustody(models.Model):
    _name = 'repair.logic.property'
    _description = 'Repair Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Date(string='Date')
    description = fields.Char(string='Description')
    repair_cost = fields.Float(string='Repair Cost')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    rep_id = fields.Many2one('logic.custody.properties', string='Rep')
