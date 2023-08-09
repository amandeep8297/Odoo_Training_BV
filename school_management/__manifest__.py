{
    'name': 'School Management System',
    'version': '16.0',
    'summary': 'A comprehensive school management system for Odoo.',
    'author': 'Aman Deep',
    'depends': ['base','mail','sale_management','product','report_xlsx'],
    'license':'LGPL-3',
    'auto_install': True,
    'website':'https://github.com/amandeep8297',
    'sequence':'0',
    'category':'Education',
    'installable': True,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        'wizard/cancel_admission.xml',
        'views/school_form.xml',
        'views/teacher.xml',
        'views/sale_order_view.xml',
        'views/sports.xml',
        'views/school_menu.xml',
        'reports/student_report.xml',
        'reports/inherit_qweb.xml',
        'views/mail_template.xml',
        'views/cron.xml',
        'views/res_config_settings_views.xml',
        'reports/student_xlsx_report.xml'
    ],
    'images': ['static/description/icon.png'],
    'demo': ['data/demo.xml'],
}