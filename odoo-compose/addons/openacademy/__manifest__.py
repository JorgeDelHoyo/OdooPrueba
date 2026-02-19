# -*- coding: utf-8 -*-
{
	'name': "Open Academy", # Nombre de mi modulo
    'summary': "modulo de prueba en odoo 19",
    'description': "modulo prueba odoo 19",
    'author': "Jorge del Hoyo",
    'website': "http://www.iespabloserrano.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'odoo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/board_views.xml',
        'reports/reports.xml',
	# 'vistas/matches.xml',
	# 'vistas/maps.xml',
	# 'vistas/characters.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}