# -*- encoding: utf-8 -*-

{
    'name': 'FEL Megaprint',
    'version': '15.0.1',
    'category': 'Custom',
    'description': """ Integración con factura electrónica de Megaprint """,
    'author': 'Rodrigo Fernandez',
    'website': 'http://aquih.com/',
    'depends': ['fel_gt'],
    'data': [
        'views/account_view.xml',
        'views/fel_megaprint_retornacliente.xml',
    ],
    'demo': [],
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
