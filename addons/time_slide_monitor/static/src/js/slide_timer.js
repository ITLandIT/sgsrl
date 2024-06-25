odoo.define('my_module.slide_timer', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var startTime = new Date().getTime();
    $(document).ready(function () {
        $(window).on('beforeunload', function () {
            var endTime = new Date().getTime();
            var timeSpent = (endTime - startTime) / 1000; // time in seconds
            ajax.jsonRpc('/slide/track_time', 'call', {
                'slide_id': parseInt($('.oe_slide').data('slide-id')),
                'time_spent': timeSpent
            });
        });
    });
});
