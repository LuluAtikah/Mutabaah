# -*- coding: utf-8 -*-
{
    'name': "mutabaah",

    'summary': """
       """,

    'description': """
        This modul aims to manage mutabaah yaumiyah of santri karya in DPU DT
    """,

    'author': "L. Atikah",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/mutabaah.xml',
        #'report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}