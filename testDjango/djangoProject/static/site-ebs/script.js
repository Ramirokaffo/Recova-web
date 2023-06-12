$(document).ready(function() {

  const listImg = document.querySelectorAll("figure")
  // console.log(document.getElementById("im"))

  function slider_effect(id) {
    const fig = document.getElementById(id)
    // console.log(fig)
  var posImg = fig.offsetTop;
    var posCurseur = this.pageYOffset;
    console.log(posCurseur)
    console.log(posImg)
    console.log(posImg - posCurseur)
    if(posImg-posCurseur<300){
      fig.style.left = 0;
      fig.style.opacity = 1;

    }else{
      fig.style.left = "160%";
      fig.style.opacity = 0;
    }
  }

  window.addEventListener("scroll", function (param) { slider_effect("im") });


  for (const fig of document.querySelectorAll("figure")) {
    // console.log(image)
  var posImg = fig.offsetTop;
  function effet(){
    var posCurseur = this.pageYOffset;
    if(posImg-posCurseur<100){
      fig.style.left = 0;
      fig.style.opacity = 1;

    }else{
      fig.style.left = "160%";
      fig.style.opacity = 0;
    }
  }
  // window.addEventListener("scroll", effet);


  }

  var $active = $('.slideshow img.active');
  // console.log($active)
  // console.log($('.slideshow img:first'))

  var $activeNav = $('.active-item');
  var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
  $next.addClass('active');
  var interval = setInterval(function() {
    var $active = $('.slideshow img.active');
  // console.log($active)
    var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
    $active.removeClass('active');
    $next.addClass('active');
  }, 5000);


});



// function laFonction () {
//     $(".filter-r")
//   }

