$(function(){
	$(window).scroll(function () {
		var scrollBottom = $(document).height() - $(window).height() - $(window).scrollTop();
		if(scrollBottom<300) {
			var lastcount = $('#last').attr('data-last');
			$('#last').replaceWith('<li id="toload"></li>');
			$.post('next/%s' % lastcount, function(data){
				$('#toload').replaceWith(data);
			});
		}
	});
});