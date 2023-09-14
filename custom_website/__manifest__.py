# -*- coding: utf-8 -*-
{
    "name": "Website Inherit",
    "summary": """
       Custom Website module
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "application": True,
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base","website","sale"],
    "assets":{
        "web.assets_frontend":[

       'custom_website/static/src/js/dynamic_snippet.js',
    #    'custom_website/static/src/js/dynamic_snippet_options.js',
    ]},
    "data": [
        "security/ir.model.access.csv",
        "views/templates.xml",
        "views/snippets/inherit_snippet.xml",
        "views/snippets/website_data.xml",
        "views/snippets/basic_snippet.xml",
        "views/snippets/basic_snippet2.xml",
        "views/snippets/dynamic_snippet.xml",
        "views/views.xml",
    ],
   
    # "assets":{"web.assets_backend":[
    #          ' custom_website/static/src/scss/basic_snippet1.scss',

    # ]},
    "demo": [
        "demo/demo.xml",
    ],
}
