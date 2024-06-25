from odoo import models, fields

class SlideTimeTrack(models.Model):
    _name = 'slide.time.track'
    _description = 'Slide Time Tracking'

    name = fields.Char(string='Name', required=True)
