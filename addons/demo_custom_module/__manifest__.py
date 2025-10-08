{
    'name': 'Demo Custom Module',
    'version': '1.0',
    'summary': 'A basic custom module for Odoo 19 demo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_custom_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
}
