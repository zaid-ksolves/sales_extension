{
    'name': 'Sales Extended',
    'author': 'Zaid Ansari',
    'summary': 'This is sales extended module',

    'depends': ['base', 'sale'],

    'installable': True,
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'views/custom_sale_view.xml',
        'views/custom_invoice_view.xml',
        'wizard/sales_custom_wizard.xml',

    ]
}
