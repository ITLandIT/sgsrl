/** @odoo-module **/

import ajax from 'web.ajax';

var startTime;
var timerInterval;

function startTimer() {
    startTime = new Date().getTime();
    timerInterval = setInterval(updateTimer, 1000);
}

function stopTimer(slide_id) {
    clearInterval(timerInterval);
    var endTime = new Date().getTime();
    var timeSpent = (endTime - startTime) / 1000; // tempo in secondi
    ajax.jsonRpc('/slide/track_time', 'call', {
        'slide_id': slide_id,
        'time_spent': timeSpent
    });
}

function updateTimer() {
    var currentTime = new Date().getTime();
    var timeSpent = (currentTime - startTime) / 1000; // tempo in secondi
    document.getElementById('timer-display').innerText = 'Time spent: ' + Math.floor(timeSpent) + ' seconds';
}

$(document).ready(function () {
    var slide_id = parseInt($('.oe_slide').data('slide-id'));
    startTimer();
    $(window).on('beforeunload', function () {
        stopTimer(slide_id);
    });

    // Aggiungi l'elemento HTML per il timer
    var timerElement = document.createElement('div');
    timerElement.id = 'timer-display';
    timerElement.style.position = 'absolute';
    timerElement.style.top = '10px';
    timerElement.style.right = '10px';
    timerElement.style.padding = '5px 10px';
    timerElement.style.backgroundColor = 'yellow';
    timerElement.style.zIndex = '1000';
    document.body.appendChild(timerElement);
});
