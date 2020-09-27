(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

// Auto Int
document.addEventListener('DOMContentLoaded', function () {
  M.AutoInit();
});

$(document).ready(function(){
  $('.fixed-action-btn').floatingActionButton();
});

//Ties hidden divs with respective gallery image
// next-travel
var travel = ["travel-1","travel-2","travel-3","travel-4","travel-5","travel-6","travel-7","travel-8"];
var stationary = ["stationary-1","stationary-2","stationary-3","stationary-4","stationary-5","stationary-6"];
var logo = ["logo-1","logo-2"];
var c_travel = 0;
var c_stationary = 0;
var c_logo = 0;

//onclick for travel poster div section for travel text
function changeTravelNext(){
  document.getElementById(travel[c_travel]).style.display = "none";
  c_travel+=1;
  if(c_travel > 7){
    c_travel=0;
  };
  document.getElementById(travel[c_travel]).style.display = "inline";
}

// Binds next arrow key with div for stationary text
function changeStationaryNext(){
  document.getElementById(stationary[c_stationary]).style.display = "none";
  c_stationary+=1;
  if(c_stationary > 5){
    c_stationary=0;
  };
  document.getElementById(stationary[c_stationary]).style.display = "inline";
}

// Binds next arrow key with div for logo text
function changeLogoNext(){
  console.log("Logo button firing")
  document.getElementById(logo[c_logo]).style.display = "none";
  c_logo+=1;
  if(c_logo > 1){
    c_logo=0;
  };
  document.getElementById(logo[c_logo]).style.display = "inline";
}


// Binds prev arrow key with div for travel text
function changeTravelPrev(){
  document.getElementById(travel[c_travel]).style.display = "none";
  c_travel-=1;
  if(c_travel < 0){
    c_travel=7;
  };
  document.getElementById(travel[c_travel]).style.display = "inline";
}

// Binds prev arrow key with div for stationary text
function changeStationaryPrev(){
  document.getElementById(stationary[c_stationary]).style.display = "none";
  c_stationary-=1;
  if(c_stationary < 0){
    c_stationary=5;
  };
  document.getElementById(stationary[c_stationary]).style.display = "inline";
}

// Binds prev arrow key with div for logo text
function changeLogoPrev(){
  document.getElementById(logo[c_logo]).style.display = "none";
  c_logo-=1;
  if(c_logo < 0){
    c_logo=1;
  };
  document.getElementById(logo[c_logo]).style.display = "inline";
}


// Removes parent element for error messages
document.querySelector(".child-clear").addEventListener("click", removeParentError);

function removeParentError(){
  document.querySelector(".error-message").style.display = "none";
}