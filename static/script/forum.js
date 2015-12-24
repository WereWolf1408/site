function add_forum_them(url, them_id){
	var value = $('.new_them_title').val();
	
	$.ajax({
		url: url,
		type: "POST",
		data: {'text': value, 'them_id': them_id},
		success: function(data){
			console.log(data);
			$('#forum_content').html(data);
			$('.wait_save_comment').animate({'opacity': 0}, 1000, function(){
				$('#send_comment').prop('disabled', false);
			});
		},
		beforeSend: function(xhr, settings) {
        	if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        	}
			$('#send_comment').prop('disabled', true);
			$('.wait_save_comment').animate({'opacity': 1}, 1000);
		}
	})
}

$('.bt_new_them_add_ext').on('click', function(){
	var id = $('.hide').text();
	add_forum_them("/site/forum/extend-them-save/", id);
})

$('.bt_new_them_add').on('click', function(){
	add_forum_them("/site/forum/save/");
})


$('.bt_new_them').on('click', function(){
	if($('.bt_new_them').val() == "New them"){
		$('.new_them').css('display', 'inline-block');
		$('.bt_new_them').val('Close');
	} else if ($('.bt_new_them').val() == "Close"){
		$('.new_them').css('display', 'none');
		$('.bt_new_them').val('New them');
	}
});


