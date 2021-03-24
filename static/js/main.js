;(function () {

    'use strict';

    var carousels = function() {
        $(".owl-carousel1").owlCarousel(
            {
                loop:true,
                center: true,
                margin:0,
                responsiveClass:true,
                nav:false,
                responsive:{
                    0:{
                        items:1,
                        nav:false
                    },
                    600:{
                        items:1,
                        nav:false
                    },
                    1000:{
                        items:3,
                        nav:true,
                        loop:false
                    }
                }
            }
        );

        $(".owl-carousel2").owlCarousel(
            {
                loop:true,
                center: false,
                margin:0,
                responsiveClass:true,
                nav:true,
                responsive:{
                    0:{
                        items:1,
                        nav:false
                    },
                    600:{
                        items:2,
                        nav:false
                    },
                    1000:{
                        items:3,
                        nav:true,
                        loop:true
                    }
                }
            }
        );
    }


    // svg responsive in mobile mode
    var checkPosition = function() {
        if ($(window).width() < 767) {
            $("#bg-services").attr("viewBox", "0 0 1050 800");

        }
    };

    (function($) {
        carousels();
        checkPosition();
    })(jQuery);


}());

// menu toggle button
function myFunction(x) {
    x.classList.toggle("change");
}
$(function () {
    $(document).scroll(function () {
      var $nav = $(".fixed-top");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
  });
  $(document).ready(function () {
    if ($(window).width() > 991){
    $('.navbar-light .d-menu').hover(function () {
            $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
        }, function () {
            $(this).find('.sm-menu').first().stop(true, true).delay(120).slideUp(100);
        });
        }
    });

 let error = document.getElementById('validate');
let label = document.getElementsByTagName("label");

document.getElementById("name")
  .addEventListener("keyup", function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
      next("name", "email");
    }
  });

  document.getElementById("email")
  .addEventListener("keyup", function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        next('email','phone');
    }
  });

  document.getElementById("phone")
  .addEventListener("keyup", function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        next('phone','location');
    }
  });

  document.getElementById("location")
  .addEventListener("keyup", function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
      next('location','message');
    }
  });
 

function next(from, to) {
    error.innerHTML = "";
    let value = document.getElementById(from).children[1].value;
    if(!value || value === "") {
        error.innerHTML = "Please enter a valid value";
    }
    else {
        error.innerHTML = "";
        document.getElementById(from).classList.remove('is-visible');
        document.getElementById(to).classList.add('is-visible');
    }
}

function previous(from , to) {
    error.innerHTML = "";
    document.getElementById(from).classList.remove('is-visible');
    document.getElementById(to).classList.add('is-visible');
}
