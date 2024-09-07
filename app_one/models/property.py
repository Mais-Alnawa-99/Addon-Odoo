import re

import requests
from odoo import models, fields, api


class Property(models.Model):
    _name = 'property'
    _description = 'Apps'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(default='New', readonly=1)
    name = fields.Char(required=1, translate=True)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    phone_number = fields.Char()
    date_availability = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_price = fields.Float()
    price = fields.Float(compute='_compute_price', readonly=0)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garden = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),

    ], default='north')
    city = fields.Selection([
        ('lattakita', 'Lattakita'),
        ('tartous', 'Tartous'),

    ])
    expected_price_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Progress'),
        ('close', 'Close'),
        ('done', 'Done'),

    ], default='draft')

    line = fields.One2many('property.line', 'prop_id')
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'this name is exit')
    ]
    reason = fields.Char()
    address_id = fields.Many2one('res.partner', 'Address')
    part_id = fields.Many2one('res.partner', 'Part')

    def action_draft(self):
        for rec in self:
            rec.create_history_record(rec.state, 'draft', rec.reason)
            print("done draft")
            rec.state = 'draft'

    def show_all_rec(self):
        payload = dict({})
        response = requests.get('http://localhost:8069/properties', data=payload)
        print(response.content)

    @api.constrains('phone_number')
    def number_phone_condition(self):
        phone_num = re.compile(r'\d{3}-\d{4}-\d{2}')
        for rec in self:
            if rec.phone_number and not phone_num.match(rec.phone_number):
                raise models.ValidationError("The phone number must be in the format ddd-dddd-dd")

    def action_progress(self):
        for rec in self:
            rec.create_history_record(rec.state, 'progress', rec.reason)
            print("done progress")
            rec.state = 'progress'

    def action_close(self):
        for rec in self:
            rec.create_history_record(rec.state, 'close', rec.reason)
            print("done close")
            rec.state = 'close'

    def action_done(self):
        for rec in self:
            rec.create_history_record(rec.state, 'done', rec.reason)
            print("done")
            rec.state = 'done'

    def expected_selling_date(self):
        list_prop = self.search([])
        for rec in list_prop:
            if rec.expected_price_date and rec.expected_price_date < fields.date.today():
                rec.is_late = True

    @api.depends('selling_price', 'expected_price')
    def _compute_price(self):
        for rec in self:
            print("we compute price")
            rec.price = rec.selling_price - rec.expected_price

    @api.onchange('selling_price', 'expected_price')
    def _onchange(self):
        for rec in self:
            print("we compute price")

    def action_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.wizard_action')
        action['context'] = {'default_property_id': self.id}
        return action

    def create_history_record(self, old_state, new_state, reason):
        for rec in self:
            rec.env['history'].create({
                'user_id': rec.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason

            })

    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return res

    def group(self):
        res = super(Property, self).read_group(domain=[],fields=[],groupby=[])
        print('we copy this rec')
        return res



class PropertyLine(models.Model):
    _name = 'property.line'
    area = fields.Float()
    description = fields.Char()
    prop_id = fields.Many2one('property')
