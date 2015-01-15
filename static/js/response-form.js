$('.response-form').submit(function(event){
			event.preventDefault();
			
			$.ajax({
				url:'/townhall/answer/',
				type:'POST',
				data: $(this).serializeArray(),
				success: function(json){
					$('#thanks').html("<h4>" + json.response + "</h4>");
					console.log(json);
            		console.log("success"); 
				},
				error: function(xhr,errmsg,err){
					$('#thanks').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg); // add the error to the dom
            		console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
				}
			});
			
			$(this).fadeOut();
		});