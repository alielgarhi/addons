# -*- coding: utf-8 -*-
from odoo import api,fields,models,_
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'
	
	split_id = fields.Many2one(string="Split From PO",
	                           comodel_name='purchase.order',
	                           help="PO Splited From Ref:")

	def btn_split_quotation(self):
		"""
		Define function to split PO ordeline when we click on button
		:return: View
		"""
		for record in self:
			if record.order_line:
				cnt = 0
				for rec in record.order_line:
					if rec.split:
						cnt += 1
				if cnt >= 1:
					po_id = record.copy()
					po_id.write({
						'split_id': record.id
					})

					if po_id:
						for line in po_id.order_line:
							if not line.split:
								line.unlink()
							else:
								line.split = False
					for order_line in record.order_line:
						if order_line.split:
							self.env['purchase.order.line'].browse(order_line.id).unlink()
					compose_tree = self.env.ref('purchase.purchase_order_tree', False)
					compose_form = self.env.ref('purchase.purchase_order_form', False)
					return {
						'name': 'PO Split Order',
						'type': 'ir.actions.act_window',
						'view_type': 'form',
						'view_mode': 'tree,form',
						'res_model': 'purchase.order',
						'views': [(compose_tree.id, 'tree'),(compose_form.id, 'form')],
						'view_id': compose_tree.id,
						'res.id': False,
						'target': 'current',
						'domain': [('id', 'in', [po_id.id])],
						'context': {},
					}
				
				else:
					raise ValidationError(_('Please Select Order Line To Split'))
