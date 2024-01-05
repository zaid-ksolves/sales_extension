from odoo import fields,models,_

class custom_sale_line(models.Model):
    _inherit ='sale.order'
    _description = 'Sales custom line'

    custom_order_line = fields.One2many('custom.order.line','sale_order_id',string='Custom Order Line')

    def action_custom_invoice_btn(self):
        invoice_lines = []
        order_lines = self.custom_order_line

        if self.custom_order_line.sale_order_id.invoice_ids:
            for order_line in order_lines:
                invoice_line = {
                    'sale_order_id': order_line.sale_order_id.id,
                    'invoice_order_id': order_line.sale_order_id.invoice_ids[0].id,
                    'product_id': order_line.product_id.id,
                    'description': order_line.description,
                    'quantity': order_line.quantity,
                    'unit_price': order_line.unit_price,
                    'taxes_ids': [(6, 0, order_line.taxes_ids.ids)],
                    'tax_excl': order_line.tax_excl,
                }
                invoice_lines.append(invoice_line)
            self.env['custom.invoice.line'].create(invoice_lines)
        else:
            print("Invoice is null")

        return {
            'res_model':'account.move',
            'res_id':'self.custom_order_line.id',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            # 'view_id':self.env['account.view_move_form'].id,
        }