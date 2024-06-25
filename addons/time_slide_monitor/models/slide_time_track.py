from odoo import models, fields, api

class SlideTimeTrack(models.Model):
    _name = 'slide.time.track'
    _description = 'Slide Time Tracking'
    _rec_name = 'slide_id'

    user_id = fields.Many2one('res.users', string='User', required=True)
    slide_id = fields.Many2one('slide.slide', string='Slide', required=True)
    time_spent = fields.Float(string='Time Spent (seconds)', default=0.0)

    @api.model
    def create(self, vals):
        if not self.env.user.has_group('base.group_user'):
            raise AccessError("You do not have the necessary permissions to create this record.")
        return super(SlideTimeTrack, self).create(vals)

    @api.multi
    def write(self, vals):
        if not self.env.user.has_group('base.group_user'):
            raise AccessError("You do not have the necessary permissions to modify this record.")
        return super(SlideTimeTrack, self).write(vals)

    @api.multi
    def unlink(self):
        if not self.env.user.has_group('base.group_user'):
            raise AccessError("You do not have the necessary permissions to delete this record.")
        return super(SlideTimeTrack, self).unlink()
