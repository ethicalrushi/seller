$('.search').keyup(function(){

	var searchterm = $(this).val().toLowerCase();
	console.log(searchterm);
	$('.pro').each(function(){
		var data = $(this).text().toLowerCase();
		if (data.indexOf(searchterm)===-1){
			$(this).hide();

		}
		else{
			$(this).show();
		}

	})
		


});


