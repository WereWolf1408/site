$('#get_back').on('click', function(event){
	window.location.href = '/site/'
})
$('#login').on('click', function(event){
	var str1 = $('#pass').val();
	var str2 = $('#conf_pass').val();
	if (str1 != str2){
		$('#error_pass, #error_conf_pass').css({'display': 'block'});
		return false;
	} 
})
$('.btn-primary').on('click', function(){
	 if ($('.btn-primary').html() == 'Hide'){
	 	$('.show_panel').animate({'height': 0}, 500);
	 	$('.tools').css({'display': 'none'});
	 	$('.btn-primary').html('Show')
	 }else{
	 	$('.btn-primary').html('Hide');
	 	$('.show_panel').animate({'height': 400}, 1000);
		$('.tools').css({'display': 'block'});
	 }
	 
})
$('.pagination').on('click', function(event){
	if (event.target.tagName == 'A'){
		page = event.target.text
		if (page != '<<' && page != '>>'){
			window.location.href = '/site/page/' + page + '/';
		}
	}
	return false;
})