# controllers.py
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class SaleOrderPortal(http.Controller):

    @http.route('/my/orders/approve', type='json', auth='user')
    def approve_order(self, order_id):
        try:
            order = request.env['sale.order'].browse(order_id)
            if order.exists() and order.state == 'draft':
                order.write({'state': 'sale'})
                # Add additional logic if needed, like sending confirmation email or any other operations.
                return {'status': 'success', 'message': 'Order approved successfully.'}
            else:
                return {'status': 'error', 'message': 'Order not found or not in draft state.'}
        except Exception as e:
            _logger.error('Error approving order: %s', str(e))
            return {'status': 'error', 'message': 'An error occurred while approving the order.'}
