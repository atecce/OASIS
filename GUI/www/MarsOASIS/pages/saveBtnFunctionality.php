<script>
				$(".saveBtn").click(function() 
				{
					var id = $(this).attr("id");
					var dataString = 'id='+id;
					//alert(dataString);
					var start,stop,p1,p2,p3,p4,p5,m1,m2,p6,p7,p9,p10,p11,p12,m6,m7,m8,m18,la,st,f1;
					start=stop=p1=p2=p3=p4=p5=m1=m2=p6=p7=p9=p10=p11=p12=m6=m7=m8=m18=la=st=f1=0;
					
					if((id.indexOf("start") > -1))
					{
						$('#toggleStart_loader').css('display', 'inline');
						//alert("Start save button : "+(id.indexOf("start") > -1));
						start = $('#startonoffswitch').prop('checked')?1:0;
						stop = $('#stoponoffswitch').prop('checked')?1:0;
						dataString += "&start="+start+"&stop="+stop;
					}
					if((id.indexOf("stop") > -1))
					{
						$('#toggleStop_loader').css('display', 'inline');
						//alert("Stop save button : "+(id.indexOf("stop") > -1));
						start = $('#startonoffswitch').prop('checked')?1:0;
						stop = $('#stoponoffswitch').prop('checked')?1:0;
						dataString += "&start="+start+"&stop="+stop;
					}
					if((id.indexOf("WFC") > -1))
					{
						$('#toggleWFCBody_loader').css('display', 'inline');
						//alert("Display Pumps save button : "+(id.indexOf("pumps") > -1));
						p1 = $('#p1onoffswitch').prop('checked')?1:0;
						p2 = $('#p2onoffswitch').prop('checked')?1:0;
						dataString += "&p1="+p1+"&p2="+p2;
					}
					if((id.indexOf("WC") > -1))
					{
						$('#toggleWCBody_loader').css('display', 'inline');
						//alert("Display Valves save button : "+(id.indexOf("valves") > -1));
						m1 = $('#m1onoffswitch').prop('checked')?1:0;
						m2 = $('#m2onoffswitch').prop('checked')?1:0;
						p3 = $('#p3onoffswitch').prop('checked')?1:0;
						p4 = $('#p4onoffswitch').prop('checked')?1:0;
						p5 = $('#p5onoffswitch').prop('checked')?1:0;
						dataString += "&m1="+m1+"&m2="+m2+"&p3="+p3+"&p4="+p4+"&p5="+p5;
					}
					
					if((id.indexOf("AM") > -1))
					{
						$('#toggleAMBody_loader').css('display', 'inline');
						//alert("Display Valves save button : "+(id.indexOf("valves") > -1));
						m6 = $('#m6onoffswitch').prop('checked')?1:0;
						m7 = $('#m7onoffswitch').prop('checked')?1:0;
						m8 = $('#m8onoffswitch').prop('checked')?1:0;
						v3 = $('#v3onoffswitch').prop('checked')?1:0;
						v4 = $('#v4onoffswitch').prop('checked')?1:0;
						p10 = $('#p10onoffswitch').prop('checked')?1:0;
						p12 = $('#p12onoffswitch').prop('checked')?1:0;
						dataString += "&m6="+m6+"&m7="+m7+"&m8="+m8+"&v3="+v3+"&v4="+v4+"&p10="+p10+"&p12="+p12;
					}
					
					if((id.indexOf("LI") > -1))
					{
						//alert("Display Valves save button : "+(id.indexOf("valves") > -1));
						la = $('#la-value').val()+"";
						var value_1 = parseInt(la);
						if(value_1<0 || value_1>100)
						{
							alert("Value for Camera Location should be between 0 - 100");
							return;	
						}
						//la = la.slice(0, -1); // remove %
						st = $('#st-value').val()+"";
						value_1 = parseInt(st);
						if(value_1<0 || value_1>100)
						{
							alert("Value for Bracket Rotation should be between 0 - 100");
							return;	
						}
						//st = st.slice(0, -1); // remove %
						m18 = $('#m18-value').val()+"";
						value_1 = parseInt(m18);
						if(value_1<0 || value_1>100)
						{
							alert("Value for LED% Brightness should be between 0 - 100");
							return;	
						}
						//m18 = m18.slice(0, -1); // remove %
						$('#toggleLIBody_loader').css('display', 'inline');
						dataString += "&la="+la+"&st="+st+"&m18="+m18;
					}
					
					if((id.indexOf("SM") > -1))
					{
						$('#toggleSMBody_loader').css('display', 'inline');
						//alert("Display Valves save button : "+(id.indexOf("valves") > -1));
						p6 = $('#p6onoffswitch').prop('checked')?1:0;
						p7 = $('#p7onoffswitch').prop('checked')?1:0;
						p9 = $('#p9onoffswitch').prop('checked')?1:0;
						p11 = $('#p11onoffswitch').prop('checked')?1:0;
						f1 = $('#f1onoffswitch').prop('checked')?1:0;
						dataString += "&p6="+p6+"&p7="+p7+"&p9="+p9+"&p11="+p11+"&f1="+f1;
					}
					//alert(dataString);
					
					//$('.p_text').html(""); //removing data from all p tags				
					//$('#'+title).html(""); //removing data only from current p tag
					
					dataString += "&user_id=<?php echo $user_id; ?>";
					//alert(dataString);
					$.ajax({
						type: "POST",
						url: "saveUpdatedOperations.php",
						data: dataString,
						cache: false,
						dataType: 'json',
						success: function(result)
						{
							//alert(result+"");
							if(id == result.id)
							{
								if((id.indexOf("start") > -1))
								{
									alert(" Values for Start Updated Successfully");
									$('#toggleStart_loader').hide();
								}	
								if((id.indexOf("stop") > -1))
								{
									alert(" Values for Stop Updated Successfully");
									$('#toggleStop_loader').hide();
								}	
								if((id.indexOf("WFC") > -1))
								{
									alert(" Values for Water Flow Control Updated Successfully");
									$('#toggleWFCBody_loader').hide();
								}	
								if((id.indexOf("WC") > -1))
								{
									alert(" Values for Water Conditioning Updated Successfully");
									$('#toggleWCBody_loader').hide();
								}
								if((id.indexOf("AM") > -1))
								{
									alert(" Values for Atmospheric Management Updated Successfully");
									$('#toggleAMBody_loader').hide();
								}	
								if((id.indexOf("LI") > -1))
								{
									alert(" Values for Lighting & Imagery Updated Successfully");
									$('#toggleLIBody_loader').hide();
								}
								if((id.indexOf("SM") > -1))
								{
									alert(" Values for System Maintenance Updated Successfully");
									$('#toggleSMBody_loader').hide();
								}
							}
						}
					});					
				});
				</script>