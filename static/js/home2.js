let searchBox = document.querySelector(".search-box");
let serText = document.querySelector(".textt");

serText.onclick = function() {
    serText.classList.toggle("top-textt");
    searchBox.focus();
};

searchBox.onfocus = function() {
    serText.classList.add("top-textt");
};

searchBox.onblur = function () {
    if(searchBox.value == ""){
        serText.classList.remove("top-textt");
    }
};
document.querySelector(".spanx").onclick = function(){
    searchBox.value = '';
    serText.classList.remove("top-textt");
    document.querySelector(".search-icon .spanx").style.display = 'none';
};

searchBox.addEventListener('input', () =>{
    if(searchBox.value !== ""){
        document.querySelector(".search-icon .spanx").style.display = 'inline-block';
    }else{
        document.querySelector(".search-icon .spanx").style.display = 'none';
    }
});
