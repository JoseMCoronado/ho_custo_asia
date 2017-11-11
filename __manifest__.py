# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Harbour Customizations US --> Asia',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
A variety of commissioned changes to Harbour's US database migrated to v11 for Asia.
        """,
    'depends': ['base','sale','purchase','stock','website_quote','account','sale_order_dates'],
    'data':
        [
            'data/ir_model.xml',
            'data/ir_model_access.xml',
            'data/ir_model_fields.xml',
            'data/base_automation.xml',
            'data/ir_actions_server.xml',
            'data/ir_ui_view_new.xml',
            'data/ir_actions_act_window.xml',
            'data/ir_ui_menu.xml',
            'data/ir_ui_view.xml',
        ],
    'installable': True,
}
