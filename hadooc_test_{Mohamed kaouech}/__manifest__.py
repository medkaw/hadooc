# -*- coding: utf-8 -*-
{
    'name': "hadooc_test",
    'sequence': 1,
    'summary': """ """,
    'description': """
        
             Odoo 15 Technical Test for the Hadooc Company for the sales module
 
        """,
    'license': 'LGPL-3',
    'author': "Mohamed Koauech ",
    'website': "",
    'category': 'Test',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # Security
        
        # Data
        
        # Views
        'views/inherit_sale_order.xml',
        'views/sale_order_portal_inherit.xml',
        'views/mail_templete.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'hadooc_test_{Mohamed kaouech}/static/src/js/approve_button.js',
        ],
    },
    
    
    'qweb': [''],

    'installable': True,
    'auto_install': False,
}
