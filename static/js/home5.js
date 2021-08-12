document.getElementById("copyText").onclick = function(){
    let userLink = document.getElementById("userLink");
    userLink.select();
    userLink.setSelectionRange(0, 99999)
    document.execCommand("copy");
}