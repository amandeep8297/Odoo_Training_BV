{
    'name': 'School Management System',
    'version': '16.0',
    'author': 'Aman Deep',
    'depends': ['base','mail'],
    
    'installable': True,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'wizard/new_admission_view.xml',
        'views/school_form.xml',
        'views/demo.xml', 
    ]
}
