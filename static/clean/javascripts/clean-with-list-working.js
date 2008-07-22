$(document).ready(function() {

$('#extra').hide();

$('a#extra_toggle').click(function() {
  $('#extra').slideToggle();
  return false;
});

var color_classes = new Array("star1", "star2", "star3", "star4", "star5")

	$("ul").each(function() {
		if (!$(this).hasClass("no_change")) {
			index = 0;
			$(this).find("li").each(function() {
				$(this).addClass(color_classes[index]);
				index++;
				if (index == color_classes.length) {
					index = 0;
				}
			});
		}
	});

});