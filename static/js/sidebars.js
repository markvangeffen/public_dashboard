// Toggle organisatie elements:
var flag = true;
function showdiv(id) {
    var div = document.getElementById(id);
    div.style.display = flag ? 'none' : 'block';
    flag = !flag;

// Toggle organisatie elements / function not working on first click, do not know why?:
  // function toggle_margin_top (id) {
  //     var e = document.getElementById(id);
  //     if(e.style.display == 'block')
  //       e.style.display = 'none';
  //     else
  //       e.style.display = 'block';
  // }


  }