// Do something like this in the stylesheet (or any damn thing you wanna do with it :P)
// -----------------------------------------
// 	.red { list-style-type: circle }
// 	.blue { list-style-type: square }
// 	.yellow { list-style-type: georgian }
// 	.orange { list-style-type: hiragana }
// 	.black { list-style-type: katakana }

var color_classes = new Array("red", "blue", "yellow", "orange", "black")

// Start script
$(document).ready(function(){
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


