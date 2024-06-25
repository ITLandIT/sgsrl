# controllers/slide_time_track.py
from odoo import http
from odoo.http import request

class SlideTimeTrackController(http.Controller):

    @http.route('/slide/track_time', type='json', auth='user')
    def track_time(self, slide_id, time_spent):
        user_id = request.env.user.id
        request.env['slide.time.track'].create({
            'user_id': user_id,
            'slide_id': slide_id,
            'time_spent': time_spent,
        })
        return {'status': 'success'}
