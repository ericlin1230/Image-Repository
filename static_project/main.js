$(document).ready(function () {
    $('#modal-but').click(function(){
        $('.ui.modal')
        .modal('show')
        ;
    })
})

function showOnClick() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }