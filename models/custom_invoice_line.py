from odoo import fields,models,_

class custom_invoice_line(models.Model):
    _name ='custom.invoice.line'
    _description = 'Custom invoice line'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order Id')
    invoice_order_id = fields.Many2one('account.move',string="Custom Invoice Order")
    product_id = fields.Many2one('product.template',string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    taxes_ids = fields.Many2many('account.tax',string='Taxes')
    tax_excl = fields.Char(string='Tax excl.')