$(document).ready(function()
{
	$("#triggerbell").bind({
		mouseenter: function() {
		var $counter = $('.notification-counter');
		var val = parseInt($counter.text());
		val++;
		val=val.toString();
		$counter.text(val);
		},
		click: function() {
		var $counter=$('.notification-counter');
		$counter.text("0");
		}

	});
});
