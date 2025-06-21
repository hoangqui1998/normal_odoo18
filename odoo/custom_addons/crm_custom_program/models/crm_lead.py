from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_loan_type = fields.Selection([
        ('conventional', 'Conventional'),
        ('fha', 'FHA'), 
        ('USDA_rural_housing', 'USDA Rural Housing'),
        ('va', 'VA'),
        ('heloc', 'HELOC'),
        ('heloan', 'HELOAN'),
        ('others', 'Others')
    ], string='Loan Type')

    x_rate_type = fields.Many2one(
        'crm.program.config',
        string='Rate Type',
    )

    x_program = fields.Many2one(
        'crm.program.config',
        string='Program',
    )

    @api.onchange('x_loan_type')
    def _onchange_x_loan_type(self):
        self.x_rate_type = False

    @api.onchange('x_rate_type')
    def _onchange_x_rate_type(self):
        self.x_program = False

    

