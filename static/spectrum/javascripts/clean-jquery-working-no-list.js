$(document).ready(function() {

$('#extra').hide();

$('a#extra_toggle').click(function() {
  $('#extra').slideToggle();
  return false;
});

});