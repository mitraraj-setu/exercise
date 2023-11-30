{
    'name' : 'Estate Account',
    'application' : True,
    'depends': ['base', 'mail','real_estate','account'],
    'data' : [

        'security/ir.model.access.csv',
        # 'views/estate_account_views.xml'

    ]
}