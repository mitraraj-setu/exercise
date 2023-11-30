{
    'name' : 'Sale Order Modified',
    'application' : True,
    'depends': ['sale','product','delivery'],
    'data' : [

        'security/ir.model.access.csv',

        'data/create_invoice_cron.xml',
        'data/set_commission_cron.xml',

        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'views/product_template_views.xml',
        'views/res_config_settings.xml',
        'views/product_pricelist_views.xml',
        'views/product_product_views.xml',
        'views/city_distance_views.xml',
        'views/sale_commission_views.xml'
        # 'views/stock_move_views.xml',
        # 'views/stock_picking_views.xml'

    ]
}
