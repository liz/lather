window.addEvent('domready', function(){
	$('extra').setStyle('height','200px');
	var mySlide = new Fx.Slide('extra').hide();
	$('extra').setStyle('visibility','visible');
 
	$('extra_toggle').addEvent('click', function(e){
		e = new Event(e);
		mySlide.toggle();
		e.stop();
	});
	$('extra_toggle').addEvent('click', function(e){
		e = new Event(e);
		mySlide.slideOut();
		e.stop();
	});
});