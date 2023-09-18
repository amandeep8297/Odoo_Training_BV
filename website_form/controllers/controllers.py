from odoo import http
from odoo.http import request

class EmployeeForm(http.Controller):

    @http.route(['/employee/form'], type='http', auth="public", website=True)
    def employee_form(self, **post):
        return request.render("website_form.employee_form_data", {})
    
    @http.route('/employee/form/submit', type='http', website=True, auth='user', csrf=False)
    def create_employee_form(self, **post):
        if request.env.user.partner_id:
            employee = request.env['employee.snippet'].sudo().create({
                'emp_name': post.get('emp_name'),
                'emp_code': post.get('emp_code'),
            })
            vals = {
                'employee': employee,
            }
            return request.render("website_form.employee_form_data", vals)
        else:
            return "The user must be logged in to submit the data."
        
