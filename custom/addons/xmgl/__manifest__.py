# -*- coding: utf-8 -*-
{
    'name': "项目管理",

    'summary': """
        包含采购项目管理和非代理项目管理两类项目管理功能""",

    'description': """
        支持采购项目登记,采购文件审核,中标通知书管理,项目档案管理,资格预审项目管理,项目统计管理
    """,

    'author': "JiuYing",
    'website': "http://www.jiuying.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'data/dict_package_status.xml',
        'data/dict_project_fundsource.xml',
        'data/dict_project_property.xml',
        'data/dict_project_purchasestyle.xml',
        'data/dict_project_status.xml',
        'data/dict_project_type.xml',
#         'data_packages.xml',
#         'data_projects.xml',
        'security/xmgl_security.xml',
        'security/ir.model.access.csv',
        'views/xmgl_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}