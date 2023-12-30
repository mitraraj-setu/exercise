# {
#     'name': '$ModuleName',
#     'version': 'Version',
#     'summary': 'Summery',
#     'description': 'Description',
#     'category': 'Category',
#     'author': 'Author',
#     'website': 'Website',
#     'license': 'License',
#     'depends': ['Depends'],
#     'data': ['Data'],
#     'demo': ['Demo'],
#     'installable': True,
#     'auto_install': False
# }

{
    'name' : 'Auto Invoice',
    'application' : True,
    'depends': ['sale'],
    'data' : [

        'security/ir.model.access.csv',

        'data/automatic_invoice_cron.xml',

        'views/sale_order_views.xml',
        'views/res_config_settings_views.xml'

    ]
}
