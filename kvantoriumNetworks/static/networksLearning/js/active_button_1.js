var time_to_1 = 10000;
var time_to_2 = 60000;
var time_to_3 = 240000;

var button1 = document.getElementById("1");
var button2 = document.getElementById("2");
var button3 = document.getElementById("3");

setTimeout(function() {
    button1.disabled = false;
}, time_to_1);
setTimeout(function() {
    button2.disabled = false;
}, time_to_2);
setTimeout(function() {
    button3.disabled = false;
}, time_to_3);

