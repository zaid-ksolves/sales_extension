from odoo import fields,models,_

class custom_order_line(models.Model):
    _name ='custom.order.line'
    _description = 'Sales custom line'

    sale_order_id = fields.Many2one('sale.order',string="Custom Sale Order")
    product_id = fields.Many2one('product.template',string='Product')
    description = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    taxes_ids = fields.Many2many('account.tax',string='Taxes')
    tax_excl = fields.Char(string='Tax excl.')