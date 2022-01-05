// Get the modal
var modal = document.getElementById('dlogin');
var mod = document.getElementById('plogin');
var m = document.getElementById('register');
// Get the button that opens the modal
var btn = document.getElementById("doc");
var bt = document.getElementById("pat");
var b = document.getElementById('r');
// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
  mod.style.display = "none";
  m.style.display = "none";
}
bt.onclick = function() {
  mod.style.display = "block";
  modal.style.display = "none";
  m.style.display = "none";
}
b.onclick = function() {
  mod.style.display = "none";
  m.style.display = "block";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    m.style.display = "block";
  }
  else if (event.target == mod) {
      mod.style.display = "none";
      m.style.display = "block";
  }
}
