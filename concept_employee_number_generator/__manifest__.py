{
    'name': 'Employee Number Generator',
    'version': '17.0.1.0.0',
    'summary': 'Generate Employee Number dynamically using button & bulk actions',
    'description': """
        Assign sequential employee numbers automatically in Odoo HR, with bulk generation support in list view.
    """,
    'category': 'Human Resources',
    'author': 'Concept Solutions LLC',
    'website': 'https://www.csloman.com',
    'license': 'LGPL-3',
    'depends': ['hr'],
    'data': [
        'data/employee_number_sequence.xml',
        'data/employee_bulk_action.xml',
        'views/hr_employee_view.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/Screenshot1.png',
        'static/description/Screenshot2.jpeg',
        'static/description/Screenshot3.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
