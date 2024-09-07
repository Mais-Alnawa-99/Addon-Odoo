
from odoo import models, fields



class History(models.Model):
    _name = 'history'
    _description = 'history_app'
    user_id=fields.Many2one('res.users')
    property_id = fields.Many2one('property')
    old_state=fields.Char()
    new_state=fields.Char()
    reason=fields.Char()