
$(function() {
	var pull 		= $('#pull');
		menu 		= $('.main-menu ul');
		menuHeight	= menu.height();

	$(pull).on('click', function(e) {
		e.preventDefault();
		var hidden = menu.is(":hidden");
		menu.slideToggle("fast");
		/*var s = $(document).scrollTop();
		//$( window ).scrollTo( s + 30 );
		window.scroll(0, 0) */
		//alert(s)
		/*if (!hidden)
		{
			//alert("Visible: "+!hidden);
			$(".bodyContent").css('margin-top', 20);
		}
		else
		{
			//alert("Hidden: "+hidden);
			$(".bodyContent").css('margin-top', 180);
		}*/
		return false;
	});
	
	$(document).click(function()
	{
		var w = $(window).width();
		if(w <= 690) 
			menu.slideUp();
		$(".bodyContent").css('margin-top', 20);
	});

	$(window).resize(function(){
		var w = $(window).width();
		if(w > 320 && menu.is(':hidden')) {
			menu.removeAttr('style');
		}
	});
});
