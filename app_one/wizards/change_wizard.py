from odoo import models, fields


class ChangeWizard(models.TransientModel):
    _name = "change.wizard"

    property_id = fields.Many2one('property')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Progress'),
    ])
    reason = fields.Char()

    def action_confirm(self):
        if self.property_id.state == 'close':
         self.property_id.state = self.state
         self.property_id.create_history_record('close', self.state, self.reason)

