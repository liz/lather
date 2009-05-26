/**
 *ajaxContent - jQuery plugin for accessible, unobtrusive and easy ajax behaviour.
 * @Version 2.1 Beta
 * 
 * @requires jQuery v 1.2+
 * 
 * http://www.andreacfm.com/index.cfm/jquery-plugins
 *
 * Copyright (c) 2007 Andrea Campolonghi (andreacfm.com)
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 */
  //make $ surely available inside the PI as jQuery shortcut
(function($) {
	//call teh method with options arguments
	$.fn.ajaxContent = function(options) {
		//extend to defaults
		var defaults = $.extend({}, $.fn.ajaxContent.defaults, options);
			// debug if required		
			if(defaults.debug == 'true'){
				debug(this);
			};
			//Initilaize any instance looping on the match element
			return this.each(function(){
				//set local variables and extend to the metadata plugin if loaded
				var $obj = $(this);
				var href = $obj.attr('href');
				var o = $.metadata ? $.extend({}, defaults, $obj.metadata()) : defaults;
				// add binding change events on url if required
				if(o.bind != ''){
					var binds = o.bind.split(',');
					for(var i=0; i < binds.length ; i++){
						var queryString = setQueryString(binds);
						var url = href + queryString;
						$obj.attr({href:url});
						if ($(binds[i]).attr('type') == "radio" || $(binds[i]).attr('type') == "checkbox"){
							$('input[name=' + $(binds[i]).attr("name") + ']').change(function(){
								var queryString = setQueryString(binds);
								var url = href + queryString;
								$obj.attr({href:url});						
							});
							}else{
							$(binds[i]).change(function(){
								var queryString = setQueryString(binds);
								var url = href + queryString;
								$obj.attr({href:url});						
							});
						}							
					}
				}
				var $target = $(o.target);

			//bind the event
			$obj.bind(o.event, function(ev){
				// add loader if required
				if(o.loader == 'true'){
					if(o.loaderType == 'img'){
 							$target.html('<img src="' + o.loadingMsg + '"/>');
 						}else{
							 $target.html(o.loadingMsg);
 							}
 					} 
					//remove add current class
					$('a.' + o.currentClass).removeClass(o.currentClass);								
					$obj.addClass(o.currentClass);
					// make the call
					$.ajax({ 
  						type: o.type, 
  						url: $obj.attr('href'),
  						cache:'false',
  						beforeSend:function(){
  							if(typeof o.beforeSend == 'function'){
  								o.beforeSend($obj,$target,ev);
  								}
  						},
  						success: function(msg){ 
    						$target.html(msg);
    						if(o.extend == 'true'){
    							$(o.filter,$target).ajaxContent({
    								target:o.ex_target,
									type:o.ex_type,
									event:o.ex_event,
									loader:o.ex_loader,
									loaderType:o.ex_loaderType,
									loadingMsg:o.ex_loadingMsg,
									errorMsg:o.ex_errorMsg,
									currentClass:o.ex_currentClass,
									success:o.ex_success,
									beforeSend:o.ex_beforeSend,
									error:o.ex_error,
									bind:o.ex_bind
    							});
    						}
    						//if a callback exist pass arguments ( object,target and receive message)
    						if(typeof o.success == 'function'){
    							o.success($obj,$target,msg);
    							}  						
    						},
						error: function(){
							$target.html("<p>" + o.errorMsg + "</p>");
							if(typeof o.error == 'function'){
    							o.error($target);
    							}  						
    					 
						}
					});
				return false;
			});
		});
	};	
  	function debug($obj) {
    if (window.console && window.console.log)
     window.console.log('selection count: ' + $obj.size() + '  with class:' + $obj.attr('class'));
  	};
  	function setQueryString(binds){
  		//var queryString = '?';
		var queryString = '&';
  		for(var i=0; i < binds.length; i++){
  			if ($(binds[i]).attr('type') == "radio"){
				queryString += $('input[name=' + $(binds[i]).attr("name") + ']').fieldSerialize();
  			}else if($(binds[i]).attr('type') == "checkbox"){
  				queryString += $(binds[i]).attr("name") + '=' + $('input[name=' + $(binds[i]).attr("name") + ']').fieldValue();
  			}
  			else{
  				queryString += $(binds[i]).fieldSerialize();	
  			}	
  			if(i != binds.length - 1){
  				queryString += '&';
  			}
  		}
	return queryString;
  	};
})(jQuery);

$.fn.ajaxContent.defaults = {
		target: '#ajaxContent',
		type:'get',
		event:'click',
		loader:'true',
		loaderType:'text',
		loadingMsg:'Loading...',
		errorMsg:'An error occured durign the page requesting process!',
		currentClass:'selected',
		success:'',
		beforeSend:'',
		error:'',
		bind:'',
		debug:'false',
		extend:'false',
		filter:'',
		ex_target:'',
		ex_type:'get',
		ex_event:'click',
		ex_loader:'true',
		ex_loaderType:'text',
		ex_loadingMsg:'Loading...',
		ex_errorMsg:'An error occured durign the page requesting process!',
		ex_currentClass:'selected',
		ex_success:'',
		ex_beforeSend:'',
		ex_error:'',
		ex_bind:''
};





