# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchase_type = fields.Many2one('purchase.order.type', string='Purchase Order Type')
