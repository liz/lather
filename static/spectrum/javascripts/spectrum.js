$(document).ready(function() {

Cufon.replace([ '.exit_tag', '.month_title_small', ]);

Cufon.replace(':header a', {
    hover: true
});

$('#twitter-topper').click(function() {
  $('#twitter-color').slideToggle();
  $('.twitter-minus').toggle();
  $('.twitter-plus').toggle();
  $('#tumbles-color').slideUp();
  $('#words-color').slideUp();
  $('#flickr-color').slideUp();
  $('#delicious-color').slideUp();
  $('#lastfm-color').slideUp();
  $('.tumbles-minus').hide();
  $('.tumbles-plus').show();
  $('.words-minus').hide();
  $('.words-plus').show();
  $('.flickr-minus').hide();
  $('.flickr-plus').show();
  $('.delicious-minus').hide();
  $('.delicious-plus').show();
  $('.lastfm-minus').hide();
  $('.lastfm-plus').show();
  return false;
});

$('#tumbles-topper').click(function() {
  $('#tumbles-color').slideToggle();
  $('.tumbles-minus').toggle();
  $('.tumbles-plus').toggle();
  $('#words-color').slideUp();
  $('#flickr-color').slideUp();
  $('#delicious-color').slideUp();
  $('#lastfm-color').slideUp();
  $('#twitter-color').slideUp();
  $('.words-minus').hide();
  $('.words-plus').show();
  $('.flickr-minus').hide();
  $('.flickr-plus').show();
  $('.delicious-minus').hide();
  $('.delicious-plus').show();
  $('.lastfm-minus').hide();
  $('.lastfm-plus').show();
  $('.twitter-minus').hide();
  $('.twitter-plus').show();
  return false;
});

$('#words-topper').click(function() {
  $('#words-color').slideToggle();
  $('.words-minus').toggle();
  $('.words-plus').toggle();
  $('#flickr-color').slideUp();
  $('#delicious-color').slideUp();
  $('#lastfm-color').slideUp();
  $('#twitter-color').slideUp();
  $('#tumbles-color').slideUp();
  $('.flickr-minus').hide();
  $('.flickr-plus').show();
  $('.delicious-minus').hide();
  $('.delicious-plus').show();
  $('.lastfm-minus').hide();
  $('.lastfm-plus').show();
  $('.twitter-minus').hide();
  $('.twitter-plus').show();
  $('.tumbles-minus').hide();
  $('.tumbles-plus').show();
  return false;
});

$('#flickr-topper').click(function() {
  $('#flickr-color').slideToggle();
  $('.flickr-minus').toggle();
  $('.flickr-plus').toggle();
  $('#delicious-color').slideUp();
  $('#lastfm-color').slideUp();
  $('#twitter-color').slideUp();
  $('#words-color').slideUp();
  $('#tumbles-color').slideUp();
  $('.delicious-minus').hide();
  $('.delicious-plus').show();
  $('.lastfm-minus').hide();
  $('.lastfm-plus').show();
  $('.twitter-minus').hide();
  $('.twitter-plus').show();
  $('.tumbles-minus').hide();
  $('.tumbles-plus').show();
  $('.words-minus').hide();
  $('.words-plus').show();
  return false;
});

$('#delicious-topper').click(function() {
  $('#delicious-color').slideToggle();
  $('.delicious-minus').toggle();
  $('.delicious-plus').toggle();
  $('#lastfm-color').slideUp();
  $('#twitter-color').slideUp();
  $('#words-color').slideUp();
  $('#tumbles-color').slideUp();
  $('#flickr-color').slideUp();
  $('.lastfm-minus').hide();
  $('.lastfm-plus').show();
  $('.twitter-minus').hide();
  $('.twitter-plus').show();
  $('.tumbles-minus').hide();
  $('.tumbles-plus').show();
  $('.words-minus').hide();
  $('.words-plus').show();
  $('.flickr-minus').hide();
  $('.flickr-plus').show();
  return false;
});

$('#lastfm-topper').click(function() {
  $('#lastfm-color').slideToggle();
  $('.lastfm-minus').toggle();
  $('.lastfm-plus').toggle();
  $('#twitter-color').slideUp();
  $('#words-color').slideUp();
  $('#tumbles-color').slideUp();
  $('#flickr-color').slideUp();
  $('#delicious-color').slideUp();
  $('.twitter-minus').hide();
  $('.twitter-plus').show();
  $('.tumbles-minus').hide();
  $('.tumbles-plus').show();
  $('.words-minus').hide();
  $('.words-plus').show();
  $('.flickr-minus').hide();
  $('.flickr-plus').show();
  $('.delicious-minus').hide();
  $('.delicious-plus').show();
  return false;
});

$('#top-menu').animateMenu($('#top-menu li:first a').css('left'));

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

$.fn.animateMenu = function(initialPos) {
	$this = this;
	var el = $('li.animated:first a', $this);
	var pos = el.css('left');

	el.css({'left': initialPos}).animate( { left: pos, opacity: 1 }, 600, function() {
		$(this).parents('li:first').removeClass('animated');
		$this.animateMenu(pos);
	});
};