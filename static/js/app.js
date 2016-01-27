$(function(){
	console.log('page has loaded')
	$('a').click(function (e) {
		e.preventDefault();
		console.log(this);
		$('li').removeClass('active');
		$(this).parent().addClass('active');
	})
})