$(document).ready(function () {
	$("#briefSubmit").click(function () {
    	var searchQuery = $('#briefInput').val().trim();
    	if (searchQuery == '') {
        console.log("Nothing entered, fool.");
    	} else {
      	console.log("input is: " + $('#briefInput').val());
    	}
    	$.ajax({
        	url: '/results',
        	data: searchQuery,
        	dataType: "json",
        	type: 'POST',
        	contentType: "application/json",
        	success: function(response) {
           		console.log("success");
        	},
        	error: function(error) {
            	console.log(error);
            	console.log("failure!");
        	}
    	});
    });
});