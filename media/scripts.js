$(function(){
	$(window).scroll(function () {
		var scrollBottom = $(document).height() - $(window).height() - $(window).scrollTop();
		if (scrollBottom<300) {
			var lastcount = $('#last').attr('data-last');
			if ($('#last').length) {
				$('#last').replaceWith('<li id="toload"></li>');
				$.post('next/'+lastcount+'/', function(data){
					$('#toload').replaceWith(data);
				});
			}
		}
	});
});