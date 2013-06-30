$(document).ready(function()
{
	$(".subheaders h2").hover(
		function() {
			if(! $(this).is(':animated')) {
				$(this).fadeOut(100);
				$(this).fadeIn(300);
			}
		}
	);

	$("#faq h2").click(
		function() {
			$("#faq .info").slideToggle(100);
		}
	);
	$("#about h2").click(
		function() {
			$("#about .info").slideToggle(100);
		}
	);
	$("#privacy h2").click(
		function() {
			$("#privacy .info").slideToggle(100);
		}
	);
	$("#tips h2").click(
		function() {
			$("#tips .info").slideToggle(100);
		}
	);

	$("li").click(
		function() {
			var parent = $(this).parent().parent().attr("id");
			var index = $(this).index() + 1 ;
			var id = "#" + parent + " #info-" + index;
			$(id).slideToggle(100);
		}
	);


	$("#filter").keyup(function(){
 		
 		if ($(this).val() == "") {
 			$("#faq .info").hide(100);
 			$("#faq .info").children("li").show(100);
 			$("#about .info").hide(100);
 			$("#about .info").children("li").show(100);
 			$("#privacy .info").hide(100);
 			$("#privacy .info").children("li").show(100);
 			$("#tips .info").hide(100);
 			$("#tips .info").children("li").show(100);
 			return;
 		}
        // Retrieve the input field text and reset the count to zero
        var filter = $(this).val();
 
        // Loop through the comment list
        $(".info li").each(function(){
 
            // If the list item does not contain the text phrase fade it out
            if ($(this).text().search(new RegExp(filter, "i")) < 0) {
                $(this).fadeOut();
 
            // Show the list item if the phrase matches and increase the count by 1
            } else {
            	var parent = $(this).parent().parent().attr("id");
            	var id = "#" + parent + " .info";
            	$(id).show(100);
                $(this).show();
            }
        });
    });

});