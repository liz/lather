$(document).ready(function() {
	
Cufon.replace([ 'h1', '.exit_tag', '.month_title_small' ]);

Cufon.replace('h2', {
    hover: true
});

Cufon.replace('h3', {
    hover: true
});

$('#twitter-topper').click(function() {
  $('#twitter-color').slideToggle();
  $('.twitter-minus').toggle();
  $('.twitter-plus').toggle();
  return false;
});

$('#tumbles-topper').click(function() {
  $('#tumbles-color').slideToggle();
  $('.tumbles-minus').toggle();
  $('.tumbles-plus').toggle()
  return false;
});

$('#words-topper').click(function() {
  $('#words-color').slideToggle();
  $('.words-minus').toggle();
  $('.words-plus').toggle()
  return false;
});

$('#flickr-topper').click(function() {
  $('#flickr-color').slideToggle();
  $('.flickr-minus').toggle();
  $('.flickr-plus').toggle()
  return false;
});

$('#delicious-topper').click(function() {
  $('#delicious-color').slideToggle();
  $('.delicious-minus').toggle();
  $('.delicious-plus').toggle()
  return false;
});

$('#lastfm-topper').click(function() {
  $('#lastfm-color').slideToggle();
  $('.lastfm-minus').toggle();
  $('.lastfm-plus').toggle()
  return false;
});


$('a[rel*=lightbox]').fancybox();

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