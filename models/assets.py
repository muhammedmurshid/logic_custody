from odoo import models, fields, api, _


class LogicTotalAssets(models.Model):
    _name = 'logic.total.assets'
    _description = 'Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'asset_name'

    asset_name = fields.Char(string='Asset Name', required=1)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=1)
    added_person = fields.Many2one('res.users', string='Added By', default=lambda self: self.env.user)
    asset_photo = fields.Binary(string='Asset Photo')
    added_date = fields.Date(string='Added Date', default=fields.Date.today())

    def _compute_display_name(self):
        for rec in self:
            if rec.asset_name:
                rec.display_name = 'Asset' + ' ' + rec.asset_name




