from odoo import models, fields





class Crm(models.Model):
    _inherit = 'crm.lead'
    _description = 'model for crm'

    property_id = fields.Many2one('property', string="Property")
    is_customer = fields.Boolean()
    partner_id = fields.Many2one('res.partner',domain=[('state_patient','=', True)])
    name = fields.Char(default='property')

