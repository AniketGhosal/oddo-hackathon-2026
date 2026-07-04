{
    'name': 'Advanced HRMS',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Premium HR Management',
    'depends': ['base', 'mail'],
    'data': [
        'security/hrms_security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/employee_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
