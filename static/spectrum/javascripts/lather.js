window.onload = function() {


 var myFx = new Fx.Style('extra', 'opacity').set(100);

 var kitty = new Fx.Slide('extra').hide()
  $('kittyness').addEvent('click', function(){
    kitty.toggle('vertical');
  });

 var markdown = new Fx.Slide('markdown_sheet', { wait: true }).hide();
  $('markdowness').addEvent('click', function(){
    markdown.toggle('vertical');
  });

};
