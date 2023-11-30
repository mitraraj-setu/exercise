{
    'name' : 'Real Estate',
    'application' : True,
    'depends': ['base', 'mail', 'purchase'],
    'data' : [

        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        # 'views/inherited_res_users_model_views.xml'

    ]
}