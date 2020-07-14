# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product order pricelist',
    'version': '1.0',
    'summary': 'Product order pricelist',
    'description': """
    Allow to add pricelist in sale order line.
  """,
    'category': 'sale',
    'depends': ['sale'],
    'data': [
        'views/sale_order.xml',
    ],
}
