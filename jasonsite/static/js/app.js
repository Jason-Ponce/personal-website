// $(document).ready(() => {
//     $('.slideshow .slick').slick({
//       autoplay: true,
//       fade: true,
//       autoplaySpeed: 2000,
//       speed: 4000,
//       dots: true,
//       swipe: true
//     });
//   });


$(document).ready(() => {
    $('.slick').slick({
        fade: true,
        adaptiveHeight: true,
        // centerMode: true,
        prevArrow: '<i class="material-icons md-48 md-dark slick-prev" alt="Slide image to left">keyboard_arrow_left</i>',
        nextArrow: '<i class="material-icons md-48 md-dark slick-next" alt="Slide image to right">keyboard_arrow_right</i>',
    });

    $(".lazy").slick({
        lazyLoad: 'ondemand', // ondemand progressive anticipated
        infinite: true
      });
    });


  
//   console.log("hi jason")