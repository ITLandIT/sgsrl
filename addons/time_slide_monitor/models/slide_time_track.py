# models/slide_time_track.py
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SlideTimeTrack(models.Model):
    _name = 'slide.time.track'
    _description = 'Slide Time Tracking'

    user_id = fields.Many2one('res.users', string='User', required=True)
    slide_id = fields.Many2one('slide.slide', string='Slide', required=True)
    time_spent = fields.Float(string='Time Spent (seconds)', default=0.0)
    start_time = fields.Datetime(string='Start Time', default=fields.Datetime.now)

    @api.model
    def create(self, values):
        _logger.info('Creating new slide time track entry: %s', values)
        return super(SlideTimeTrack, self).create(values)
