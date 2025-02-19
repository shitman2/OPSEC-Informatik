// function for copy to clipboard
function copy_to_clipboard( elm_id ) {
            
    var text = document.getElementById( elm_id ).innerHTML;

    navigator.clipboard.writeText( text );

  }

// Make all text black by default
var all = document.getElementsByTagName("*");

for (var i=0, max=all.length; i < max; i++) {
all[i].style.color = "black";
}