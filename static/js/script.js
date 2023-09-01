$(document).ready(function() {
    var text = "Welcome to Car Dealership. We are pleased to have you !"; 
    var index = 0;
    var interval = setInterval(function() {
        if (index < text.length) {
            $('#animated-text').append(text.charAt(index));
            index++;
        } else {
            clearInterval(interval);
        }
    }, 100); // Adjust the delay (in milliseconds) between letters
});