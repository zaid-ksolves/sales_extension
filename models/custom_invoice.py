from odoo import fields,models,_

class custom_invoice(models.Model):
    _inherit ='account.move'
    _description = 'Sales custom line'

    custom_invoice_line = fields.One2many('custom.invoice.line', 'invoice_order_id', string='Custom Order Line')

