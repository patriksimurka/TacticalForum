
if ( window.history.replaceState ) {
          window.history.replaceState( null, null, window.location.href );
}

setTimeout(function(){
for (var i=0; i<m.length; i++) {
  m[i].classList.add('hide');
  }
}, 5000);

function set_active(){
	console.log(window.location.href);
	console.log();
	for(i of $("nav li a")){
		console.log(i.href);
		if(i.href === window.location.href || i.href === window.location.href.substring(0, window.location.href.length - 1)){
			$(i).parent().addClass('active');
		}
		else{
			$(i).parent().removeClass('active');
		}
	}
}