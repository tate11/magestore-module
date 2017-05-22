# -*- coding: utf-8 -*-
{
    'name': "Convert Price Number to Character",

    'summary': """
        Convert price number to text and display in Sales Order, Purchase Order, Invoice. Support Vietnamese & English""",

    'description': """
        Convert price number to text and display in Sales Order, Purchase Order, Invoice. Support Vietnamese & English
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account/invoice_supplier_form_inherit.xml',
        'views/account/account_invoice_view.xml',
        'views/account/account_config_setting_view.xml',
        'views/purchase/purchase_oder_view.xml',
        'views/purchase/purchase_config_setting_view.xml',
        'views/sale/sale_config_setting_view.xml',
        'views/sale/sale_oder_view.xml',
    ],
    
    'application':True,
}