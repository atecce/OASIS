
$(function() {
	var pull 		= $('#pull');
		menu 		= $('.main-menu ul');
		menuHeight	= menu.height();

	$(pull).on('click', function(e) {
		e.preventDefault();
		var hidden = menu.is(":hidden");
		menu.slideToggle("fast");
		/*var s = $(document).scrollTop();
		$( window ).scrollTo( s + 30 );
		window.scroll(0, 0) */
		var w = $(window).width();
		//alert("Hidden: 2 "+hidden+" Width : "+w);
		if(w <= 680 && w > 321) 
		{
			if (!hidden)
			{
				//alert("Visible: "+!hidden);
				$(".bodyContent").css('margin-top', 10);
			}
			else
			{
				//alert("Hidden: "+hidden);
				$(".bodyContent").css('margin-top', 134);
			}
		}
		else if(w <= 304) // 304 <=> 321
		{
			if (!hidden)
			{
				//alert("Visible: "+!hidden);
				$(".bodyContent").css('margin-top', 10);
			}
			else
			{
				//alert("Hidden: 2 "+hidden+" Width : "+w);
				$(".bodyContent").css('margin-top', 216);
			}
		}
		
		
		return false;
	});
	
	$(document).click(function()
	{
		var w = $(window).width();
		if(w <= 680) 
			menu.slideUp();
		$(".bodyContent").css('margin-top', 10);
	});

	$(window).resize(function(){
		var w = $(window).width();
		if(w >= 321 && menu.is(':hidden')) {
			menu.removeAttr('style');
		}
	});
});
