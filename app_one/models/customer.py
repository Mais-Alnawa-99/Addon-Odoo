from odoo import models, fields

class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name')

    address = fields.Text(groups="app_one.group_owner_access")
