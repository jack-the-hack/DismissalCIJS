var rload=document.getElementById("rload");
var bodycontent=document.getElementById("bodycontent");
function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
        end = dc.length;
        }
    }
    // because unescape has been deprecated, replaced with decodeURI
    //return unescape(dc.substring(begin + prefix.length, end));
    return decodeURI(dc.substring(begin + prefix.length, end));
} 

drpdwn=he.decode(dropdown);
console.log(drpdwn)
var user = getCookie("who");
  if (user == null) {
      bodycontent.innerHTML=drpdwn
  }else {
  rload.innerHTML="<meta http-equiv=\"refresh\" content=\"1\">";
  bodycontent.innerHTML="<div><h2 class=\"a4\">"+oldname1+"</h2><br><h2 class=\a3\">"+oldname2+"</h2><br><h2 class=\"a2\">"+oldname3+"</h2><br><h1 class=\"a1\">"+name+"</h1></div>";
  }