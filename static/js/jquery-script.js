$(document).ready(function() {
    // JQuery code to be added in here.
    var qText = $("#query_text").text()
    $("#post_text").mark(qText, {
        "element": "span",
        "className": "highlight"
    });
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
    
});