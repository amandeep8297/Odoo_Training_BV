from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    global_config_field = fields.Integer(string='Global_config_setting', config_parameter='school_management.global_config_field')
