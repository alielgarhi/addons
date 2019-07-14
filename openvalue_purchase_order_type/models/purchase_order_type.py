# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrderType(models.Model):
    _name = 'purchase.order.type'
    _description = 'Purchase Order Type'
    _inherit = ['mail.thread']

    name = fields.Char(required=True)
    active = fields.Boolean('Active', default=True, track_visibility='onchange')
    incoterm_id = fields.Many2one('account.incoterms', 'Incoterm')
    picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', domain="[('code', '=', 'incoming')]")
    po_return = fields.Boolean('Return PO')
