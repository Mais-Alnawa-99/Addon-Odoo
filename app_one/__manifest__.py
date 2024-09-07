{
    'name': 'project_dream',
    'author': 'mais alnawa',
    'category': '',
    'version': "17.0.0.1.0",
    'depends': ['base', 'sale_management', 'account', 'mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/base.xml',
        'views/property_view.xml',
        'views/sale.xml',
        'views/history.xml',
        'wizards/wizard.xml',
        "reports/report.xml",

    ],
    'assets': {
        'web.assets_backend': ['app_one\static\src\property.css'],
        'web.report_assets_common': ['app_one/static/src/font.css'],
    },
    'application': True,
}
