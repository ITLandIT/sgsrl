{
    'name': 'Slide Time Tracking',
    'version': '1.4',  # Aggiornato
    'author': 'ITLand',
    'depends': ['base', 'web', 'website_slides'],
    'data': [
        'views/slide_template.xml',
        'views/slide_time_tracking_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/time_slide_monitor/static/src/js/slide_timer.js',
        ],
    },
    'installable': True,
    'application': True,
}
