from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError

class SlideTimeTrackController(http.Controller):

    @http.route('/slide/track_time', type='json', auth='user')
    def track_time(self, slide_id, time_spent):
        if not request.env.user.has_group('base.group_user'):
            raise AccessError("You do not have the necessary permissions to perform this action.")
        
        user_id = request.env.user.id
        request.env['slide.time.track'].create({
            'user_id': user_id,
            'slide_id': slide_id,
            'time_spent': time_spent,
        })
        return {'status': 'success'}
