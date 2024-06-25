odoo.define('slide_time_tracking.slide_timer', function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var startTime;

    function startTimer() {
        startTime = new Date().getTime();
    }

    function stopTimer(slide_id) {
        var endTime = new Date().getTime();
        var timeSpent = (endTime - startTime) / 1000; // tempo in secondi
        ajax.jsonRpc('/slide/track_time', 'call', {
            'slide_id': slide_id,
            'time_spent': timeSpent
        });
    }

    $(document).ready(function () {
        var slide_id = parseInt($('.oe_slide').data('slide-id'));
        startTimer();
        $(window).on('beforeunload', function () {
            stopTimer(slide_id);
        });
    });
});
