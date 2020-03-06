// MaterializeCSS scrollspy
$(document).ready(function(){
    $('.scrollspy').scrollSpy();
  });

// Plugin slick slideshow  
$(document).ready(() => {
  $('.slick').slick({
      fade: true,
      adaptiveHeight: true,
      prevArrow: '<i class="material-icons md-48 md-dark slick-prev" alt="Slide image to left">keyboard_arrow_left</i>',
      nextArrow: '<i class="material-icons md-48 md-dark slick-next" alt="Slide image to right">keyboard_arrow_right</i>',
  });

  $('.slick-portfolio-travel').slick({
    fade: true,
    // adaptiveHeight: true,
    draggable: false,
    prevArrow: '<i class="material-icons md-48 md-dark slick-prev" onclick="changeTravelPrev()" alt="Slide image to left">keyboard_arrow_left</i>',
    nextArrow: '<i class="material-icons md-48 md-dark slick-next" onclick="changeTravelNext()" alt="Slide image to right">keyboard_arrow_right</i>',
  });

  $('.slick-portfolio-stationary').slick({
    fade: true,
    // adaptiveHeight: true,
    draggable: false,
    prevArrow: '<i class="material-icons md-48 md-dark slick-prev" onclick="changeStationaryPrev()" alt="Slide image to left">keyboard_arrow_left</i>',
    nextArrow: '<i class="material-icons md-48 md-dark slick-next" onclick="changeStationaryNext()" alt="Slide image to right">keyboard_arrow_right</i>',
  });

  $('.slick-portfolio-logo').slick({
    fade: true,
    // adaptiveHeight: true,
    draggable: false,
    prevArrow: '<i class="material-icons md-48 md-dark slick-prev" onclick="changeLogoPrev()" alt="Slide image to left">keyboard_arrow_left</i>',
    nextArrow: '<i class="material-icons md-48 md-dark slick-next" onclick="changeLogoNext()" alt="Slide image to right">keyboard_arrow_right</i>',
  });
});


  
