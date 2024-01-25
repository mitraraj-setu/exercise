{
    'name' : 'Update Quantity',
    'application' : True,
    'depends': ['sale'],
    'data' : [
        'security/ir.model.access.csv',
        'wizard/update_quantity_wizard_views.xml',
        'views/sale_order_views.xml',

    ]
}
