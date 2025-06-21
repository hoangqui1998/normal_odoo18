# models/crm_program_config.py
from odoo import models, fields

class CrmProgramConfig(models.Model):
    _name = 'crm.program.config'
    _description = 'CRM Program Configuration'

    name = fields.Char(string="Name", required=True)

    loan_type = fields.Selection([
        ('conventional', 'Conventional'),
        ('fha', 'FHA'), 
        ('USDA_rural_housing', 'USDA Rural Housing'),
        ('va', 'VA'),
        ('heloc', 'HELOC'),
        ('heloan', 'HELOAN'),
        ('others', 'Others')
    ], string='Loan Type', required=True)

    rate_type = fields.Many2one(
        'crm.program.config',
        string='Rate Type',
    )

    program = fields.Many2one(
        'crm.program.config',
        string='Program',
    )
