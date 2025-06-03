# models/crm_program_config.py
from odoo import models, fields

class CrmProgramConfig(models.Model):
    _name = 'crm.program.config'
    _description = 'CRM Program Configuration'

    name = fields.Char(string="Name", required=True)
    x_rate_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('adjustable', 'Adjustable')
    ], string='Rate Type', required=True)
