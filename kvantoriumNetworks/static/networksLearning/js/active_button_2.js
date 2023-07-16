var time_to_4 = 10000;
var time_to_5 = 60000;
var time_to_6 = 240000;

var button4 = document.getElementById("4");
var button5 = document.getElementById("5");
var button6 = document.getElementById("6");

setTimeout(function() {
    button4.disabled = false;
}, time_to_4);
setTimeout(function() {
    button5.disabled = false;
}, time_to_5);
setTimeout(function() {
    button6.disabled = false;
}, time_to_6);