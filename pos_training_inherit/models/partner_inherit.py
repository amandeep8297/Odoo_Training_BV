from odoo import models,fields,api

class InheritPartner(models.Model):
    _inherit="res.partner"

    details=fields.Char("Additional Info") 


    @api.model
    def _order_fields(self, ui_order):
        _older_fields = super(InheritPartner,self)._order_fields(ui_order)
        _older_fields.update({
            'details':ui_order.get('details'),
        })
        return _older_fields