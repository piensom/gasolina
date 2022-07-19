# -*- coding: utf-8 -*-
{
    'name': 'POS Megaprint - Get NIT',
    'version': '15.0.0.1',
    'category': 'Point Of Sale',
    'summary': 'POS Megaprint - Get NIT',
    'description': """POS Megaprint - Get NIT""",
    'author': 'Piensom',
    'website': 'piensom.com',
    # 'depends': ['fel_g4s', 'point_of_sale'],
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_megaprint_get_nit/static/src/js/pos_client_widget.js',
        ],
        'web.assets_qweb': [
            'pos_megaprint_get_nit/static/src/xml/*',
        ],
    },
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}
