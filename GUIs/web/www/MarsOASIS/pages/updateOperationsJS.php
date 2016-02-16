<script type="text/javascript">
	function handlePercent(input)
	{
		var id = input.id;
		id = id.substring(0, id.length - 6);
		var value = input.value;
		$("#"+id).html(value+"%");
	}
	$(document).ready(function() {
		$(".modeOnWaring").hide();
		var interval = null;
		
		$('.WFC_values').click(function(){
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				var size = id.indexOf("o");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = 0;
				if($("#"+id).prop("checked"))
				{
					//alert(id_py + " : true");
					f = 1;
				}
				else
				{
					//alert(id_py + " : false");	
					f = 0;
				}
				var dataString = "wfc="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_wfc_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
								//alert("Result str : "+result.str)
						}
					});
		
			}
		});
		
		$('.WC_values').click(function(){
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				var size = id.indexOf("o");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = 0;
				if($("#"+id).prop("checked"))
				{
					//alert(id_py + " : true");
					f = 1;
				}
				else
				{
					//alert(id_py + " : false");	
					f = 0;
				}
				var dataString = "wc="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_wc_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
								//alert("Result str : "+result.str)
						}
					});
			}
		});
		
		$('.AM_Type_1').click(function()
		{
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				//alert(id+"=>"+id.indexOf("-"));
				var size = id.indexOf("o");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = 0;
				if($("#"+id).prop("checked"))
				{
					//alert(id_py + " : true");
					f = 1;
				}
				else
				{
					//alert(id_py + " : false");	
					f = 0;
				}
				var dataString = "am="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_am_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
							//alert("Result str : "+result.str)
						}
					});
			}
				
		});
		
		$('.AM_Type_2').on("change",function(){
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				//alert(id+"=>"+id.indexOf("-"));
				var size = id.indexOf("-");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = $(this).val();
				//alert(id_py+" = "+f)
				var dataString = "am="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_am_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
							//alert("Result str : "+result.str)
						}
					});
				
			}
		});
		
		$('.LI_values').on("change",function(){
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				var size = id.indexOf("-");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = $(this).val();
				//alert(id_py+" = "+f)
				var dataString = "li="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_li_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
								//alert("Result str : "+result.str)
						}
					});
			}
		});
		
		$('.SM_values').click(function(){
			if($('#modifyonoffswitch').prop('checked'))
			{
				var id = $(this).attr('id');
				var size = id.indexOf("o");
				var id_py = "";
				for(i = 0; i < size; i++)
					id_py += id[i];
				var f = 0;
				if($("#"+id).prop("checked"))
				{
					//alert(id_py + " : true");
					f = 1;
				}
				else
				{
					//alert(id_py + " : false");	
					f = 0;
				}
				var dataString = "sm="+id_py+"&flag="+f;
				$.ajax({
						type: "POST",
						url: "py/save_sm_data.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert("Result : "+result.flag)
								//alert("Result str : "+result.str)
						}
					});
			}
		});
		
		$('#modifyonoffswitch').click(function(){
			//alert("Hi : "+$('#modifyonoffswitch').prop('checked'));
			if($('#modifyonoffswitch').prop('checked'))
			{
				$(".LI_values").prop('disabled',false);
				clearInterval(interval); // stop the interval
				alert("Now you can modify the values!");
				
				if($(".toggleWFCBody").is(':visible'))
				{
					$("#WFC_Warning").show();
				}
				if($(".toggleWCBody").is(':visible'))
				{
					$("#WC_Warning").show();
				}
				if($(".toggleAMBody").is(':visible'))
				{
					$("#AM_Warning").show();
				}
				if($(".toggleLIBody").is(':visible'))
				{
					$("#LI_Warning").show();
					$(".LI_values").prop('disabled',false);
				}
				if($(".toggleSMBody").is(':visible'))
				{
					$("#SM_Warning").show();
				}
				if($(".toggleStart").is(':visible'))
				{
					$("#START_Warning").show();
				}
				if($(".toggleStop").is(':visible'))
				{
					$("#STOP_Warning").show();
				}
			}
			else
			{
				//WFC,WC,AM,LI,SM
				interval = setInterval(poll, 2000);
				$(".modeOnWaring").hide();
				alert("You can't modify the values!");
			}
		});
		
		$('#startonoffswitch').click(function()
		{
			if($('#startonoffswitch').prop('checked'))
			{
				$('#stoponoffswitch').prop('checked',false);
			}
			else
			{
				$('#stoponoffswitch').prop('checked',true);
			}
		});
		
		$('#stoponoffswitch').click(function()
		{
			if($('#stoponoffswitch').prop('checked'))
			{
				$('#startonoffswitch').prop('checked',false);
			}
			else
			{
				$('#startonoffswitch').prop('checked',true);
			}
		});
		
		function poll(){
        var jsonUrl = 'updateOperations.php';
        $.ajaxSetup({
            cache: false
        });
        $.ajax({
            type: 'GET',
            url: jsonUrl,
            data: {},
            dataType: 'json',
            success: function (data) {
                //$('#display').html(data.start + ' and ' + data.stop);
				//alert(data+"");
				var start,stop,p1,p2,p3,p4,p5,m1,m2,p6,p7,p8,p9,p10,p11,p12,v3,v4,m6,m7,m8,m18,la,st,f1;
				start=stop=p1=p2=p3=p4=p5=m1=m2=p6=p7=p8=p9=p10=p11=p12=v3=v4=m6=m7=m8=m18=la=st=f1=0;
				if(data.start != null)
					 start = parseInt(data.start);
				if(data.stop != null)
					 stop = parseInt(data.stop);
				if(data.p1 != null)
					 p1 = parseInt(data.p1);
				if(data.p2 != null)
					 p2 = parseInt(data.p2);
				if(data.p3 != null)
					 p3 = parseInt(data.p3);
				if(data.p4 != null)
					 p4 = parseInt(data.p4);
				if(data.p5 != null)
					 p5 = parseInt(data.p5);
				if(data.p6 != null)
					 p6 = parseInt(data.p6);
				if(data.p7 != null)
					 p7 = parseInt(data.p7);
				if(data.p8 != null)
					 p8 = parseInt(data.p8);
				if(data.p9 != null)
					 p9 = parseInt(data.p9);
				if(data.p10 != null)
					 p10 = parseInt(data.p10);
				if(data.p11 != null)
					 p11 = parseInt(data.p11);
				if(data.p12 != null)
					 p12 = parseInt(data.p12);
				 
				if(data.v3 != null)
					 v3 = parseInt(data.v3);
				if(data.v4 != null)
					 v4 = parseInt(data.v4);
				
				if(data.m1 != null)
					 m1 = parseInt(data.m1);
				if(data.m2 != null)
					 m2 = parseInt(data.m2);
				if(data.m6 != null)
					 m6 = parseInt(data.m6);
				if(data.m7 != null)
					 m7 = parseInt(data.m7);
				if(data.m8 != null)
					 m8 = parseInt(data.m8);
				if(data.m18 != null)
					 m18 = parseInt(data.m18);
				if(data.la != null)
					 la = parseInt(data.la);
				if(data.st != null)
					 st = parseInt(data.st);
				if(data.f1 != null)
					 f1 = parseInt(data.f1);
				//alert(start+" - "+stop+"! 1");
				//start switch
				if(start == 1)
					$('#startonoffswitch').prop('checked',true);
				else
					$('#startonoffswitch').prop('checked',false);
				//stop switch
				if(stop == 1)
					$('#stoponoffswitch').prop('checked',true);
				else
					$('#stoponoffswitch').prop('checked',false);
				//pumps(12) switches
				if(p1 == 1)
					$('#p1onoffswitch').prop('checked',true);
				else
					$('#p1onoffswitch').prop('checked',false);
				if(p2 == 1)
					$('#p2onoffswitch').prop('checked',true);
				else
					$('#p2onoffswitch').prop('checked',false);
				if(p3 == 1)
					$('#p3onoffswitch').prop('checked',true);
				else
					$('#p3onoffswitch').prop('checked',false);
				if(p4 == 1)
					$('#p4onoffswitch').prop('checked',true);
				else
					$('#p4onoffswitch').prop('checked',false);
				if(p5 == 1)
					$('#p5onoffswitch').prop('checked',true);
				else
					$('#p5onoffswitch').prop('checked',false);
				if(p6 == 1)
					$('#p6onoffswitch').prop('checked',true);
				else
					$('#p6onoffswitch').prop('checked',false);
				if(p7 == 1)
					$('#p7onoffswitch').prop('checked',true);
				else
					$('#p7onoffswitch').prop('checked',false);
				if(p8 == 1)
					$('#p8onoffswitch').prop('checked',true);
				else
					$('#p8onoffswitch').prop('checked',false);
				if(p9 == 1)
					$('#p9onoffswitch').prop('checked',true);
				else
					$('#p9onoffswitch').prop('checked',false);
				if(p10 == 1)
					$('#p10onoffswitch').prop('checked',true);
				else
					$('#p10onoffswitch').prop('checked',false);
				if(p11 == 1)
					$('#p11onoffswitch').prop('checked',true);
				else
					$('#p11onoffswitch').prop('checked',false);
				if(p12 == 1)
					$('#p12onoffswitch').prop('checked',true);
				else
					$('#p12onoffswitch').prop('checked',false);
				if(v3 == 1)
					$('#v3onoffswitch').prop('checked',true);
				else
					$('#v3onoffswitch').prop('checked',false);
				if(v4 == 1)
					$('#v4onoffswitch').prop('checked',true);
				else
					$('#v4onoffswitch').prop('checked',false);
				if(m1 == 1)
					$('#m1onoffswitch').prop('checked',true);
				else
					$('#m1onoffswitch').prop('checked',false);
				if(m2 == 1)
					$('#m2onoffswitch').prop('checked',true);
				else
					$('#m2onoffswitch').prop('checked',false);
				if(m8 == 1)
					$('#m8onoffswitch').prop('checked',true);
				else
					$('#m8onoffswitch').prop('checked',false);
				$('#m6-value-range').val(m6);
				$('#m7-value-range').val(m7);
				$('#m6-value').html(m6+"%");
				$('#m7-value').html(m7+"%");
				$('#m18-value-range').val(m18);
				$('#st-value-range').val(st);
				$('#la-value-range').val(la);
				$('#m18-value').html(m18+"%");
				$('#st-value').html(st+"%");
				$('#la-value').html(la+"%");
				if(f1 == 1)
					$('#f1onoffswitch').prop('checked',true);
				else
					$('#f1onoffswitch').prop('checked',false);
			}
		}); //end ajax

		};
		interval = setInterval(poll, 2000);
	});
		
   
		
	</script>