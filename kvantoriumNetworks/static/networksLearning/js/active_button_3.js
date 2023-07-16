var time_to_7 = 1000;
var time_to_8 = 10000;
var time_to_9 = 120000;
var time_to_10 = 240000;

var button7 = document.getElementById("7");
var button8 = document.getElementById("8");
var button9 = document.getElementById("9");
var button10 = document.getElementById("10");

setTimeout(function() {
    button7.disabled = false;
}, time_to_7);
setTimeout(function() {
    button8.disabled = false;
}, time_to_8);
setTimeout(function() {
    button9.disabled = false;
}, time_to_9);
setTimeout(function() {
    button10.disabled = false;
}, time_to_10);