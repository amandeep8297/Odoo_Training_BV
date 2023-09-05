from odoo import models,fields,api

class InheritOrderScreeen(models.Model):
    _inherit=['pos.order']

    details=fields.Char("Additional Info") 

    @api.model
    def _order_fields(self, ui_order):
        _older_fields = super(InheritOrderScreeen,self)._order_fields(ui_order)
        _older_fields.update({
            'details':ui_order.get('details'),
        })
        return _older_fields
    