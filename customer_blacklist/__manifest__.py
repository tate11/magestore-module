# -*- coding: utf-8 -*-
{
    'name': "customer_blacklist",

    'summary': """
        Setting allow/reject/warring user create sale order while customer in blacklist """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Magestore.com",
    'website': "magestore.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_view.xml',
        'views/account_config_setting.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}