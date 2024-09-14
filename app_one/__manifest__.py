{
    'name': 'project_dream',
    'author': 'mais alnawa',
    'category': '',
    'version': "17.0.0.1.0",
    'depends': ['base', 'sale_management', 'account', 'mail','website',
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base.xml',
        'views/customer.xml',
        'views/owner.xml',
        'views/property_view.xml',
        'views/sale.xml',
        'views/history.xml',
        'views/show.xml',
        'views/templates.xml',
        'wizards/wizard.xml',
        'data/sequence.xml',
        "reports/report.xml",

    ],
    'assets': {
        'web.assets_backend': ['app_one\static\src\property.css'],
        'web.report_assets_common': ['app_one/static/src/font.css'],
    },
    'application': True,
}
