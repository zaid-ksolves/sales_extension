from odoo import models, fields, api
from datetime import datetime


class product_sale_view(models.TransientModel):
    _name = 'product.sale.view'
    _description = 'Product Sale View'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order Id')
    custom_order_line = fields.One2many('sales.custom.wizard', 'sale_order_line', string="Custom Order Lines")

    @api.model
    def default_get(self, fields):
        res = super(product_sale_view, self).default_get(fields)
        active_ids = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(active_ids)
        custom_order = []

        for order in sale_order.order_line:
            custom_order.append((0, 0, {
                'product_id': order.product_template_id,
                'description': order.name,
                'quantity': order.product_uom_qty,
                'unit_price': order.price_unit,
                'taxes_ids': order.tax_id,
                'tax_excl': order.price_subtotal,
            }))
        res['sale_order_id'] = active_ids
        res['custom_order_line'] = custom_order
        return res

    # @api.model
    # def default_get(self,fields_list):
    #     res = super(product_sale_view, self).default_get(fields_list)
    #     active_ids = self.env.context.get('active_ids')
    #     sale_order = self.env['sale.order'].browse(active_ids)
    #
    #     for order in sale_order.order_line:
    #         res.update({
    #             'product_id': order.product_id,
    #             'description': order.name,
    #             'quantity': order.product_uom_qty,
    #             'unit_price': order.price_unit,
    #             'taxes_ids': order.tax_id,
    #             'tax_excl': order.price_subtotal,
    #         })
    #         res['sale_order_id'] = active_ids
    #     return res

    def action_custom_sale(self):
        custom_order_lines_list = []
        for wizard in self.custom_order_line:
            custom_order = self.env['custom.order.line'].create({
                'product_id': wizard.product_id.id,
                'description': wizard.description,
                'quantity': wizard.quantity,
                'unit_price': wizard.unit_price,
                'taxes_ids': wizard.taxes_ids,
                'tax_excl': wizard.tax_excl,
                'sale_order_id': self.sale_order_id.id,
            })
            custom_order_lines_list.append(custom_order.id)
        # self.sale_order_id.write({
        #     'custom_order_line': [(6, 0, custom_order_lines_list)],
        # })

    # def action_custom_sale(self):
    #     sale_order = self.sale_order_id
    #     for rec in self.custom_order_line:
    #         val = {
    #             'product_id': rec.product_id.id,
    #             'description': rec.description,
    #             'quantity': rec.quantity,
    #             'unit_price': rec.unit_price,
    #             'taxes_ids': rec.taxes_ids,
    #             'tax_excl': rec.tax_excl,
    #         }
    #         sale_order.custom_order_line = [(0, 0, val)]
