from odoo import models, fields


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name')

    address = fields.Text(groups="app_one.group_owner_access")
    user_id = fields.Many2one('res.users')

    customer_filter = fields.Char(compute='_compute_customer_filter', search='_search_customer_filter')

    def _compute_customer_filter(self):
        for rec in self:
         rec.customer_filter = "record for each customer"

    def _search_customer_filter(self, operator, value):
        current_user = self.env.user
        current_customer = self.env['customer'].search([('user_id', '=', current_user.id)])
        if current_customer:
            domain = [('id', 'in', current_customer.ids)]
        else:
            domain = []
        return domain

