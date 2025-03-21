{
    'name': 'Setu Import order ',
    'summary': 'A simple Import order system',
    'author': 'Setu Consulting Pvt Ltd.',
    'depends': ['base','sale_management','sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/setu_sale_order_import_wizard.xml',
        'views/setu_sale_order_import_menu.xml',
        'views/sale_order_line_views.xml',


    ],
}
