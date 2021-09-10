# -*- coding: utf-8 -*-
{
    'name': "Lockheed Inventory",

    'summary': "iMartin Dynamics Corp.",
    'sequence' : 1,
    'description': "",

    'author': "Team SS",
    'website': "https://bjitgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application/Inventory Management',
    'version': 'alpha',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/product_view.xml',
        'views/warehouse_view.xml',

        
    ],
    

    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
