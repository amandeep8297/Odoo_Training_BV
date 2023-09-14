# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeSnippet(models.Model):
    _name='employee.snippet'

    emp_name = fields.Char("Employee name = ")
    emp_code = fields.Char("Employee code = ")
    emp_img=fields.Binary("Employee image = ")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string='City/State')
