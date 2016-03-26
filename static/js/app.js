$(function(){
	// logic for setting active class for navbar
	$('a').click(function (e) {
		$('li').removeClass('active');
		$(this).parent().addClass('active');
	})
	// start up logic, turn pic black and white and bring in intro text
	//
	//$(".name-banner-image").attr("data-image-src", "/static/img/self_japan_bench_clear_sky_bluered.jpg")
	/*
	$(".name-banner-image").fadeOut(400, function() {
		$(".name-banner-image").attr("data-image-src", "/static/img/self_japan_bench_clear_sky_bluered.jpg");
	})
	.fadeIn(400);
	*/

	// Animate text for name and description
	 $('.name-header').textillate({
	 	in:{
	 		effect: 'fadeInBigLeft',
	 		delayScale: 1.5,
		    // set the delay between each character
		    delay: 50,
		    // set to true to animate all the characters at the same time
		    sync: false,
		    // randomize the character sequence 
		    // (note that shuffle doesn't make sense with sync = true)
		    shuffle: false,
		    // reverse the character sequence 
		    // (note that reverse doesn't make sense with sync = true)
		    reverse: false,
		    // callback that executes once the animation has finished
		    callback: function () {}
	 	}
	 });
})