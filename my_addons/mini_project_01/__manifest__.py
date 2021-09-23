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
    'depends': ['base','hr','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group_view.xml',
        
        'wizard/lockheed_wizard.xml',
        
        'views/menu.xml',
        'views/product_view.xml',
        'views/warehouse_view.xml',
        'views/lock_emp_view.xml',
        'views/website_form.xml',
        'views/product_web.xml',
        'views/shop_website.xml',
        
        'reports/report.xml',
        'reports/pdf_lockheed.xml',
        'reports/sale_inherit.xml',

        
    ],
    

    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
