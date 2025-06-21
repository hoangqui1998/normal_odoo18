from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    loan_type = fields.Selection([
        ('conventional', 'Conventional'),
        ('fha', 'FHA'), 
        ('USDA_rural_housing', 'USDA Rural Housing'),
        ('va', 'VA'),
        ('heloc', 'HELOC'),
        ('heloan', 'HELOAN'),
        ('others', 'Others')
    ], string='Loan Type')

    rate_type = fields.Many2one(
        'crm.program.config',
        string='Rate Type',
    )

    program = fields.Many2one(
        'crm.program.config',
        string='Program',
    )


    @api.onchange('rate_type')
    def _onchange_rate_type(self):
        self.program = False

    @api.onchange('loan_type')
    def _onchange_loan_type(self):
        self.rate_type = False

    

