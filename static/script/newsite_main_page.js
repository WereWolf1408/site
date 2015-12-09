var search = false;
// -------------------------------------------------
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
// ------------------------------------------------
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
$('.hp_button').on('click', function(){
	 if ($('.hp_button').html() == 'Hide'){
	 	$('.show_panel').animate({'height': 0}, 500);
	 	$('.tools').css({'display': 'none'});
	 	$('.hp_button').html('Show')
	 }else{
	 	$('.hp_button').html('Hide');
	 	$('.show_panel').animate({'height': 400}, 1000);
		$('.tools').css({'display': 'block'});
	 }
	 
})
$('.pagination').on('click', function(event){
	if (event.target.tagName == 'A'){
		page = event.target.text
		if (page != '<<' && page != '>>'){
			if (search == false) {
				window.location.href = '/site/page/' + page + '/';	
			} else if (search == true){
				window.location.href = '/search/page/' + page + '/';
			}
		}
	}
	return false;
})

$('#enot').on('click', function(event){
	$.ajax({
		url: '/ajaxexample/',
		type: 'POST',
		success: function(data){
			console.log(data);
			return false;
		},
		beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
	})
	return false;
})
$('.hide_button').on('click', function(event){
	if($('.hide_button').html() == "+"){
		$('.left_side').css({'display': 'block'});	
		$('.hide_button').html("-")
	} else{
		$('.left_side').css({'display': 'none'});
		$('.hide_button').html("+")
	}
	return false;
})
$('#logo_img').on('click', function(event){
	if (search == true){
		search = false;
	}
})
$('#search_button').on('click', function(event){
	var text = $('#search_text').val();
	if (text != ""){
		window.location.href = '/site/search?text=' + text;
	}
})

$('.main_content').on('click', function(event){
	elem = event.target;
	if (elem.text != 'More'){
		return false;
	}
})