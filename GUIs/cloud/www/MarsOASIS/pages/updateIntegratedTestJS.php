	
	<script type="text/javascript">
		$(document).ready(function() 
		{
			$("#bodyContainer").css("min-height","85%");
			$(".clear").hide();
			$(".loader").fadeOut();
			$("#ee").click(function(){			
				$(".footer").css("bottom",0);
				$("#ee_clear").fadeToggle();
				$("#gm_clear").hide();
				$("#ie_clear").hide();
				$("#ltp_clear").hide();
				$(".toggle_ee").fadeToggle();
				$(".toggle_ie").hide();
				$(".toggle_ltp").hide();
				$(".toggle_gm").hide();				
			}); 
			$("#gm").click(function(){
				if (!$(".toggle_gm").is(":visible")) 
				{
					$(".footer").css("bottom",-30);
				}
				else
				{
					$(".footer").css("bottom",0);
				}
				$("#gm_clear").fadeToggle();
				$("#ee_clear").hide();				
				$("#ie_clear").hide();
				$("#ltp_clear").hide();
				$(".toggle_gm").fadeToggle();
				$(".toggle_ee").hide();
				$(".toggle_ie").hide();
				$(".toggle_ltp").hide();				
			}); 
			$("#ie").click(function(){			
				$(".footer").css("bottom",0);
				$("#ie_clear").fadeToggle();
				$("#ee_clear").hide();				
				$("#gm_clear").hide();
				$("#ltp_clear").hide();
				$(".toggle_ie").fadeToggle();
				$(".toggle_ee").hide();
				$(".toggle_gm").hide();
				$(".toggle_ltp").hide();				
			});
			$("#ltp").click(function(){
				if (!$(".toggle_ltp").is(":visible")) 
				{
					$(".footer").css("bottom",-50);
				}
				else
				{
					$(".footer").css("bottom",0);
				}
				$("#ltp_clear").fadeToggle();
				$("#ee_clear").hide();				
				$("#gm_clear").hide();
				$("#ie_clear").hide();
				$(".toggle_ltp").fadeToggle();
				$(".toggle_ee").hide();
				$(".toggle_gm").hide();
				$(".toggle_ie").hide();
			}); 
			
			$("#ee_clear").click(function(){				
				$(".ee_text").html("");
				$(".ee_text").hide();
			});
			
			$("#gm_clear").click(function(){				
				$(".gm_text").html("");
				$(".gm_text").hide();
			});
			
			$("#ie_clear").click(function(){				
				$(".ie_text").html("");
				$(".ie_text").hide();
			});
			
			$("#ltp_clear").click(function(){				
				$(".ltp_text").html("");
				$(".ltp_text").hide();
			});
			
			$(".sensor").click(function() 
			{
				var title = $(this).attr("id")+"";
				var dataString = 'var1='+title;
				//alert(dataString);
				
				//$('.p_text').html(""); //removing data from all p tags				
				$('#'+title).html(""); //removing data only from current p tag
				
				$('#'+title).show();
				//$('#'+title+'_loader').show();
				$('#p_'+title).hide();
				$('#'+title+'_loader').css('display', 'inline');
				$.ajax({
					type: "POST",
					url: "py/getSensorData.php",
					data: dataString,
					cache: false,
					success: function(result)
					{
						//alert(result.file);
						//alert(result.value+" - "+result.timestamp);
						//alert('p_'+title);
						$('#p_'+title).css('display','inline-block');
						if(result.value == "Not Defined" && result.timestamp == "Unknown")
						{
							$('#p_'+title).html("Value : "+result.value+",<br/> TimeStamp : "+result.timestamp+",<br/> Note : Python file execution failed.");
						}
						else
						{
							$('#p_'+title).html("Value : "+result.value+",<br/> TimeStamp : "+result.timestamp);												
						}
						$('#'+title+'_loader').hide();
					},
					error: function (jqXHR, exception) {
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Not connect.\n Verify Network.';
        } else if (jqXHR.status == 404) {
            msg = 'Requested page not found. [404]';
        } else if (jqXHR.status == 500) {
            msg = 'Internal Server Error [500].';
        } else if (exception === 'parsererror') {
            msg = 'Requested JSON parse failed.';
        } else if (exception === 'timeout') {
            msg = 'Time out error.';
        } else if (exception === 'abort') {
            msg = 'Ajax request aborted.';
        } else {
            msg = 'Uncaught Error.\n' + jqXHR.responseText;
        }
 	alert(msg);
		    }
				});
			});			   
		});			
	</script>