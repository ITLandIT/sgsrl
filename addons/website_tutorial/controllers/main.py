from odoo import http
from odoo.http import request
import base64

class WebsiteTutorial(http.Controller):
    @http.route('/verifica-certificazioni', auth='public', website=True, methods=['GET', 'POST'])
    def hello(self, **kwargs):
        cert_id = kwargs.get('cert_id')
        participations = []
        if cert_id:
            clean_cert_id = str(int(cert_id))
            participations = request.env['survey.user_input'].sudo().search([('id', '=', int(clean_cert_id))])
        attachments = request.env['ir.attachment'].sudo().search([('res_model', '=', 'survey.user_input'), ('res_id', 'in', [p.id for p in participations])])
        attachment_dict = {att.res_id: att for att in attachments}
        return http.request.render('website_tutorial.hello_template', {
            'participations': participations,
            'attachments': attachment_dict,
            'cert_id': cert_id or '',
        })

    @http.route('/download_attachment/<int:attachment_id>', auth='public', methods=['GET'])
    def download_attachment(self, attachment_id, **kwargs):
        attachment = request.env['ir.attachment'].sudo().browse(attachment_id)
        if not attachment.exists():
            return request.not_found()
        filecontent = base64.b64decode(attachment.datas)
        return request.make_response(
            filecontent,
            headers=[
                ('Content-Type', attachment.mimetype),
                ('Content-Disposition', f'attachment; filename={attachment.name}')
            ]
        )
