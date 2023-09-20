# -*- coding: utf-8 -*-
from odoo.exceptions import UserError 
from odoo import models

class WebsiteForm(models.Model):
    _inherit='employee.snippet'


    # def action_totp_enable_wizard(self):
    #     if self.env.user != self:
    #         raise UserError(("Login required"))
        
    #     w = self.env['employee.snippet'].create({
    #         'emp_name': self.id,
    #         'emp_code': self.code,
    #     })
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #         'res_model': 'website_form.employee_form_popup',
    #         'name': ("Two-Factor Authentication Activation"),
    #         'res_id': w.id,
    #         'views': [(False, 'form')],
    #         'context': self.env.context,
    #     }
    


