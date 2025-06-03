from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_rate_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('adjustable', 'Adjustable')
    ], string='Rate Type')

    x_program = fields.Many2one(
        'crm.program.config',
        string='Program',
    )


