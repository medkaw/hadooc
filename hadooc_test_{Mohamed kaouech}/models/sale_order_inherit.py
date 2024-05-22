# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('to_approve', 'Approved')
    ], ondelete={'to_approve': 'set default'})
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('to_approve', 'To Approve'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    is_manager = fields.Boolean(compute='_compute_is_manager', store=False)
    
    
    def action_to_approve(self):
        self.write({'state': 'to_approve'}) 


    @api.depends('user_id', 'state')
    def _compute_is_manager(self):
        for order in self:
            if self.env.user.has_group('sales_team.group_sale_manager') and order.state == 'to_approve':
                order.is_manager = True
                print('moi1',order.is_manager)
            elif not self.env.user.has_group('sales_team.group_sale_manager') and order.state == 'draft':
                order.is_manager = True
                print('moi',order.is_manager)
            else:
                order.is_manager = False



    