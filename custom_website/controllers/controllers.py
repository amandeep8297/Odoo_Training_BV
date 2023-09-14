# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class CustomWebsite(http.Controller):
    @http.route("/custom_website/custom_website", auth="public")
    def index(self, **kw):
        return "Hello, world"

    @http.route("/static_snippet", auth="public", website=True)
    def list(self, **kw):
        return http.request.render("custom_website.basic_snippet", {})
    
    @http.route('/employee/', auth="public", type="json", methods=['POST'])
    def all_cities(self):
        emp = http.request.env['employee.snippet'].search_read([], ['country_id', 'state_id', 'emp_img'])
        print("11111111111111123456789",emp)
        return emp


    