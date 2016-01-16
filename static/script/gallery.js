$('#prev').on('click', function(){
	$('#circle').css({'margin-left': '-750px'});
})

$('.gallery').on('click', function(event){
	elem = event.target;
	if (elem.tagName == 'IMG'){
		alert($(elem).prop('src'));
	}
})