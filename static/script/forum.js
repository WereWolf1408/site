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
				$('.wait_save_comment').css({"display": "none"});
			});
		},
		beforeSend: function(xhr, settings) {
        	if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        	}
			$('.wait_save_comment').css({"display": "block"});
			$('.wait_save_comment').animate({'opacity': 1}, 1000);
		}
	})
}

function delete_forume_them(url, id){
	$.ajax({
		url: url,
		type: "POST",
		data: {'id': id},
		success: function(data){
			console.log(data);
			$('#forum_content').html(data);
			$('.wait_save_comment').animate({'opacity': 0}, 1000, function(){
				$('.wait_save_comment').css({"display": "none"});
			});
		},
		beforeSend: function(xhr, settings) {
        	if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        	}
			$('.wait_save_comment').css({"display": "block"});
			$('.wait_save_comment').animate({'opacity': 1}, 1000);
		}
	})
}

$('.bt_new_them_add_ext').on('click', function(){
	var id = $('#ex_forum_id').text();
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

$('#forum_content').on('click', function(event){
	var elem = event.target;
	if (elem.tagName == "INPUT") {
		if($(elem).attr('id') == 'delele_them'){
			var forum_id = $(elem).siblings('#forum_id').html();
			delete_forume_them('/site/forum/delete/', forum_id);
		} else if ($(elem).attr('id') == 'delele_them_ext'){
			var forum_id = $(elem).siblings('#forum_id').html();
			delete_forume_them('/site/forum/ext_them_delete/', forum_id);
		}
	}
})



