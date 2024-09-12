from odoo import models, fields



class Ownre(models.Model):
    _name = 'owner'
    _description = 'owner_app'

    name = fields.Char()
    property_id = fields.One2many('property', 'owner_id')
    phone = fields.Char()
