{
    'name': 'School Management System',
    'version': '16.0',
    'author': 'Aman Deep',
    'depends': ['base','mail','sale_management','product'],
    'auto_install': True,
    'installable': True,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'wizard/cancel_admission.xml',
        'views/school_form.xml',
        'views/teacher.xml',
        'views/sale_order_view.xml',
        'views/school_menu.xml',
    ],
    'demo': ['data/demo.xml']
}
