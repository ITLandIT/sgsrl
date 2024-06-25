# __manifest__.py
{
    'name': 'Slide Time Tracking',
    'version': '1.0',
    'author': 'ITLand',
    'depends': ['base', 'web', 'website_slides'],
    'data': [
        'views/slide_template.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
