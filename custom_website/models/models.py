# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class Custom_website(models.Model):
    _name = 'custom.website'
    _description = 'custom.website'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class EmployeeSnippet(models.Model):
    _name='employee.snippet'

    emp_name = fields.Char("Employee name = ")
    emp_code = fields.Char("Employee code = ")
    emp_img=fields.Binary("Employee image = ")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string='City/State')
