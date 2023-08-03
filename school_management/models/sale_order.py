from odoo import fields, models
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    transaction_field = fields.Many2one('res.users', string='Inherited field')
