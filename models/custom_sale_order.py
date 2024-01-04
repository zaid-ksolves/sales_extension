from odoo import fields,models,_

class custom_sale_line(models.Model):
    _inherit ='sale.order'
    _description = 'Sales custom line'

    custom_order_line = fields.One2many('custom.order.line','sale_order_id',string='Custom Order Line')