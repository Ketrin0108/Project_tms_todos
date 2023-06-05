
function buttonClick() {
    alert("задача завершена");

};


window.onload = function() {
  var buttons = document.getElementsByTagName("button");
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", buttonClick);
    console.log("Check");
  }
};


