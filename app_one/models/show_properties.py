from odoo import models, fields ,api
import re



class ShowProperties(models.Model):
    _name = 'show.properties'

    property_id = fields.Many2one('property')
    date_availability = fields.Date()
    price= fields.Float()
    location = fields.Text()
    phone_customer=fields.Char()

    @api.constrains('phone_customer')
    def number_phone_condition(self):
        phone_num = re.compile(r'\d{3}-\d{4}-\d{2}')
        for rec in self:
            if rec.phone_customer and not phone_num.match(rec.phone_customer):
                raise models.ValidationError("The phone customer must be in the format ddd-dddd-dd")
