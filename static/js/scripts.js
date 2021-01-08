
if ( window.history.replaceState ) {
          window.history.replaceState( null, null, window.location.href );
}

setTimeout(function(){
for (var i=0; i<m.length; i++) {
  m[i].classList.add('hide');
  }
}, 5000);

