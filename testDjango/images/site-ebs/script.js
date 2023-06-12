$(document).ready(function() {
  var $active = $('.slideshow img.active');
  var $activeNav = $('.active-item');
  var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
  $next.addClass('active');
  var interval = setInterval(function() {
    var $active = $('.slideshow img.active');
    var $next = ($active.next().length > 0) ? $active.next() : $('.slideshow img:first');
    $active.removeClass('active');
    $next.addClass('active');
  }, 5000);

// $("#services").toggle(function () {
//   $("#services").addClass("active-item");
//   $(".acueil-page").hide();
//   $activeNav.removeClass("active-item");
//   $(".nos-services-page").show();
// }

// // , 
// // function () {
// //   $("#services").removeClass("active-item");
// //   $(".acueil-page").show();
// //   // $activeNav.removeClass("active-item");
// //   $(".acueil-page").show();
// // }
// );

// $("#services").click(function (e) { 
//   $("#services").addClass("active-item");

  // $("#services").toggle(function () {
  // $("#services").addClass("active-item");
  // $(".acueil-page").hide();
  // $activeNav.removeClass("active-item");
  // $(".nos-services-page").show();
// })


// });


});



