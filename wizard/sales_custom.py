from odoo import models, fields, api
from datetime import datetime

class sales_custom_wizard(models.TransientModel):
    _name = 'sales.custom.wizard'
    _description = 'Sales Custom Wizard'

    sale_order_line = fields.Many2one('product.sale.view', string='Sale Order Wizard')
    # sale_order_id = fields.Many2one('sale.order',string="Custom Sale Order")
    product_id = fields.Many2one('product.template',string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    taxes_ids = fields.Many2many('account.tax',string='Taxes')
    tax_excl = fields.Char(string='Tax excl.')

    # def action_custom_sale(self):
    #     custom_sale_order = self.env['custom.order.line']
    #     new_order = custom_sale_order.create({
    #         'product_id': self.product_id.id,
    #         'description': self.description,
    #         'quantity': self.quantity,
    #         'unit_price': self.unit_price,
    #         'taxes_ids': self.taxes_ids,
    #         'tax_excl': self.tax_excl,
    #     })
    #     return new_order
    #