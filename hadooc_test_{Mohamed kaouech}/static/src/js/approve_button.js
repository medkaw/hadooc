odoo.define('hadooc_test_{Mohamed kaouech}.approve_button', function (require) {
  'use strict';



    var ajax = require('web.ajax');

    $(document).ready(function () {
        $('#approve_order_button').on('click', function (e) {
            e.preventDefault();
            var orderId = $(this).data('order-id');

            // Simulate an AJAX request to approve the order
            ajax.jsonRpc('/my/orders/approve', 'call', { order_id: orderId }).then(function (result) {
       
                    $('#approve_order_button').hide();
                    $('#sign_pay_button').removeClass('d-none');
                    $('#action_buttons_container').removeClass('d-none');
                // }
            });
        });
    });
});

