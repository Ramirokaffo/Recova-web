$(document).ready(function() {

// (
  // function() {
  console.log("J'ai execute ca")
  alert(document.querySelectorAll("figure"))
  var fig = document.querySelectorAll("figure")[0];
  var posImg = fig.offsetTop;
  function effet(){
    var posCurseur = this.pageYOffset;
    if(posImg-posCurseur<300){
      fig.style.left = 0;
      fig.style.opacity = 1;
    }else{
      fig.style.left = "160%";
      fig.style.opacity = 0;
    }
  }
  window.addEventListener("scroll", effet);
// })();


  var $active = $('.slideshow img.active');
  var $next = $('.active-item');
  console.log("Oui je suis ici")
  var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
  $next.addClass('active');
  var interval = setInterval(function() {
    var $active = $('.slideshow img.active');
    var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
    $active.removeClass('active');
    $next.addClass('active');
  }, 5000);

});




