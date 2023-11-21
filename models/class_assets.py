from odoo import models, fields, api, _


class LogicCustodyScrapsForm(models.Model):
    _name = 'logic.custody.class.assets'
    _description = 'Class Assets'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    class_id = fields.Many2one('logic.base.class', string='Class')
    batch_id = fields.Many2one('logic.base.batch', string='Batch')
    branch = fields.Selection([('corporate_office', 'Corporate Office'), ('cochin_campus', 'Cochin Campus'),
                               ('kottayam_campus', 'Kottayam Campus'), ('calicut_campus', 'Calicut Campus'),
                               ('malappuram_campus', 'Malappuram Campus'), ('trivandrum_campus', 'Trivandrum Campus'),
                               ('palakkad_campus', 'Palakkad Campus'), ('dubai_campus', 'Dubai Campus')],
                              string='Branch')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, readonly=1)

