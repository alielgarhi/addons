# -*- coding: utf-8 -*-
# Copyright (c) Open Value All Rights Reserved 

{
    "name": "Purchase Order Type",
    "summary": 'Purchase Order Type',
    "version": "12.0.1.1.0",
    "category": "Purchase",
    "website": '',
    "author": "Open Value",
    "support": 'opentechvalue@gmail.com',
    "license": "LGPL-3",
    "price": 0.00,
    "currency": 'EUR',
    'description': "",
    "depends": [
        "purchase",
        "purchase_stock",
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/view_purchase_order_type.xml",
        "views/view_purchase_order.xml",
        "views/view_res_partner.xml",
        "data/purchase_order_type.xml",
    ],
    "demo": [],
    "images": ['static/description/banner.png'],
    "application": False,
    "installable": True,
    "auto_install": False,
}
