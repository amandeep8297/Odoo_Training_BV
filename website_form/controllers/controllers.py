from odoo import http
from odoo.http import request

class EmployeeForm(http.Controller):

    @http.route(['/employee/form'], type='http', auth="public", website=True, csrf=False)
    def employee_form(self):
        return request.render("website_form.employee_form_data")
    
    @http.route('/employee/form/submit', type='json', auth='public',)
    def create_employee_form(self, **post):
        try:
            # print(request.env.user.id)
            if request.env.user.id == 4:
                return {'msg': 'Login Required', 'stat':False, 'body':'Please Login or Signup before submission!'}

            request.env['employee.snippet'].create({
                'emp_name': post.get('emp_name'),
                'emp_code': post.get('emp_code'),
            })
            return {'msg': 'Data Submitted', 'stat':True, 'body':'Your data has been submitted successfully!'}

        except:

            return {'msg': 'Data Cannot be submitted', 'stat':True, 'body':'Technical Error.'}
