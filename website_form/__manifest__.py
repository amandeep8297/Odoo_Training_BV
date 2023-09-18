# -*- coding: utf-8 -*-
{
    "name": "Website Page Form",
    "summary": """
       
    """,
    "author": "Aman Deep",
    "website": "https://www.yourcompany.com",
    "application": True,
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base","website","custom_website","web"],
    "assets": {
        "web.assets_frontend": [
            "website_form/static/src/scss/style.scss",
            "website_form/static/src/js/MessagePopup.js",
        ]
    },
    "data": [
        "security/ir.model.access.csv",
        # "views/EmployeeRecord.xml",
        "views/template.xml",
       "views/snippets/success.xml",
        # "views/menu.xml",
    ],
    
    "demo": [
        # "demo/demo.xml",
    ],
}
