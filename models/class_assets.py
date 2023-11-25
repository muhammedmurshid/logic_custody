from odoo import models, fields, api, _


class LogicCustodyScrapsForm(models.Model):
    _name = 'logic.custody.class.assets'
    _description = 'Class Assets'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'display_name'

    class_id = fields.Many2one('logic.base.class', string='Class')
    batch_id = fields.Many2one('logic.base.batch', string='Batch')
    asset_photo = fields.Binary(string='Asset Photo')
    added_date = fields.Date(string='Added Date', default=fields.Date.today())
    branch = fields.Many2one('logic.base.branches', related='batch_id.branch_id', string='Branch')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=1)
    assets_list_ids = fields.One2many('logic.custody.assets.list', 'asset_id', string='Assets List')
    repair_assets_ids = fields.One2many('repair.logic.class.assets', 'rep_assets_id', string='Rep')

    def _compute_display_name(self):
        for rec in self:
            if rec.class_id:
                rec.display_name = rec.class_id.name + ' ' + 'Assets'


class LogicCustodyAssetsList(models.Model):
    _name = 'logic.custody.assets.list'

    asset_name = fields.Many2one('logic.total.assets', string='Asset Name', required=1)
    cost = fields.Float(string='Cost')
    serial_number = fields.Char(string='Serial Number')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    asset_id = fields.Many2one('logic.custody.class.assets', string='Asset')


class RepairClassAssetsCustody(models.Model):
    _name = 'repair.logic.class.assets'
    _description = 'Repair Assets'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Date(string='Date')
    asset_id = fields.Many2one('logic.total.assets', string='Asset', required=1)
    description = fields.Char(string='Description')
    repair_cost = fields.Float(string='Repair Cost')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    rep_assets_id = fields.Many2one('logic.custody.class.assets', string='Rep')


