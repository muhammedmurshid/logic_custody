from odoo import fields, models, api, _


class LogicCustodyProperties(models.Model):
    _name = 'logic.custody.properties'
    _description = 'Custody Properties'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'property_id'

    property_id = fields.Many2one('logic.custody.type', string='Type')
    class_id = fields.Many2one('logic.base.class', string='Class', related='property_id.class_id')
    is_class_room = fields.Boolean(string='Is Class Room', related='property_id.is_class_room')
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

    @api.depends('rep_ids.repair_cost')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        total = 0
        for order in self.rep_ids:
            total += order.repair_cost
        self.update({
            'repair_amt': total,

        })

    repair_amt = fields.Float(string='Repair Amount', compute='_amount_all', store=True)


class RepairCustody(models.Model):
    _name = 'repair.logic.property'
    _description = 'Repair Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Date(string='Date')
    description = fields.Char(string='Description')
    repair_cost = fields.Float(string='Repair Cost')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    rep_id = fields.Many2one('logic.custody.properties', string='Rep')
