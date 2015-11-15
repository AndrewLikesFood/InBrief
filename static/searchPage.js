$(document).ready(function () {
	$("#briefSubmit").click(function () {
    	var searchQuery = $('#briefInput').val().trim();
    	if (searchQuery == '') {
            // handle error here
            $("#submitError").css("display", "block");
            console.log("Nothing entered, fool.");
    	} else {
            $("#submitError").css("display", "none");
      	    console.log("input is: " + $('#briefInput').val());
            window.location.href = "http://127.0.0.1:5000/" + searchQuery;
    	}
    	
    	/*$.ajax({
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
    	});*/
    });
});