if ( window.history.replaceState ) {
          window.history.replaceState( null, null, window.location.href );
}

setTimeout(function(){
	for (el of [m, n]){
		for (var i=0; i<el.length; i++) {
		  el[i].classList.add('hide');
		}
	}
}, 5000);


function set_active(){
	if (window.location.href.endsWith('#')) {
		return false;
	}
	for(i of $("nav li a")){
		if(i.href === window.location.href || i.href === window.location.href.substring(0, window.location.href.length - 1)){
			$(i).parent().addClass('active');
		}
		else {
			$(i).parent().removeClass('active');
		}
	}
}