$(document).ready(function () {
	$("#briefSubmit").click(function () {
    var searchQuery = $('#briefInput').val().trim();
    if (searchQuery == '') {
      console.log("Nothing entered, fool.");
    } else {
      console.log("input is: " + $('#briefInput').val());
    }
  });
});