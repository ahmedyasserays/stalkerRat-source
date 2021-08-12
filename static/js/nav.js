let inp = document.getElementById("Search");
let plh = document.querySelector(".placeholder");
let spanx = document.querySelector(".spanx");
let but = document.getElementById("bu-sub");
let searchBar = document.querySelector(".search-bar");
let overlay = document.querySelector(".overlay");

but.addEventListener("click", (e) => {
    if (getComputedStyle(inp).width == getComputedStyle(inp).height) {
        but.type = "button";
        document.querySelector("#logo").style.display = "none";
        document.querySelector("#tex").style.display = "none";
        document.querySelector(".rit").style.display = "none";
        searchBar.style.width = "70%";
        inp.style.width = "100%";
        inp.style.paddingLeft = "20px";
        but.style.right = "4%";
        inp.focus();
    } else {
        but.type = "submit";
    };
});

overlay.addEventListener("click", (e) => {
        inp.blur();
        document.querySelector("#logo").style.display = "block";
        document.querySelector("#tex").style.display = "block";
        document.querySelector(".rit").style.display = "block";
        overlay.classList.remove("open-overlay");
        inp.style.width = "40px";
        but.style.right = "42%";
        inp.style.color = "#000";
})


inp.onfocus = function () {
    plh.classList.add("plac-top");
    if (getComputedStyle(inp).width == getComputedStyle(inp).height) {
        spanx.style.display = "inline";
        inp.style.color = "#fff";
        overlay.classList.add("open-overlay");
    }
};
inp.onblur = function(){
    if(inp.value !== ''){
        plh.classList.add("plac-top")
    }else{
        plh.classList.remove("plac-top");
    }
}

// plh.onclick = function () {inp.focus();};

spanx.onclick = function () {
    inp.value = '';
    inp.focus();
}