# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import UserError



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_type = fields.Many2one('purchase.order.type', string="Purchase Order Type")
    po_return = fields.Boolean('Return PO', related='order_type.po_return', store=True)

    
    @api.onchange('partner_id')
    def onchange_partner_id_purchase_order_type(self):
        if self.partner_id.purchase_type:
            self.order_type = self.partner_id.purchase_type.id

    @api.onchange('order_type')
    def onchange_purchase_order_type(self):
        if self.order_type:
            if self.order_type.incoterm_id:
                self.incoterm_id = self.order_type.incoterm_id.id
            if self.order_type.picking_type_id:
                self.picking_type_id = self.order_type.picking_type_id.id

    @api.constrains('po_return','partner_id')
    def _check_return_order(self):
        if self.po_return == True and self.partner_id.customer == False:
            raise UserError(_("in return PO, vendor has to be set as customer also"))
        return True
        
    @api.multi
    @api.constrains('order_line.price_unit', 'order_line.po_return_line')
    def _check_return_order2(self):
        for line in self.order_line:
            if line.po_return_line == True and not line.price_unit == 0.0:
                raise UserError(_("in return PO, price has to be zero"))
        return True


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'     
    
    po_return_line = fields.Boolean('Return PO', related='order_id.order_type.po_return', store=True)

    @api.multi 
    @api.constrains('price_unit', 'po_return_line')
    def _check_return_order_line(self):
        for record in self:
            if record.po_return_line == True and not record.price_unit == 0.0:
                raise UserError(_("in return PO, price has to be zero"))
        return True