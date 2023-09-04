from odoo import fields, models, api

class InheritSession(models.Model):
    _inherit='pos.session'
    details=fields.Char("Additional Info")

    @api.model
    def _loader_params_res_partner(self):
        params=super(InheritSession,self)._loader_params_res_partner()
        params['search_params']['fields'].append('details')
        return params
    