# __manifest__.py
{
    'name': 'Slide Time Tracking',
    'version': '1.0',
    'author': 'ITLand',
    'depends': ['base', 'web', 'website_slides'],
    'data': [
        'security/ir.model.access.csv',
        'views/slide_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/js/slide_timer.js',
        ],
    },
    'installable': True,
    'application': True,
}
