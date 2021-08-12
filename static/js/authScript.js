let search_bar = document.querySelector('.navbar input[type=search]');
let search_style = search_bar.style;
let search_form = document.querySelector(".navbar form");
let sec_search_btn = document.getElementById('second-search-btn');

// let logout = document.querySelector("a.logout-btn");
// let logout_style = logout.style;


let restyler = ()=>{
    if(window.innerWidth < 700){   
        search_bar.style.width = '200px';
            if (window.innerWidth < 576){
                search_form.style.display = 'none';
                sec_search_btn.style.display = 'inline-block';
                document.querySelector(".nav-right form").style.marginTop = '0px';
                document.getElementById("profile-pic-btn").style.marginTop = '5px';
            }else{
                document.querySelector(".nav-right form").style.marginTop = '5px';
                document.getElementById("profile-pic-btn").style.marginTop = '0px';
                search_form.style.display = 'inline-block';
                sec_search_btn.style.display = 'none';
            }
    }else{
        search_bar.style = search_style;
    }
};

restyler();

window.onresize = restyler;


sec_search_btn.onclick = ()=>{
    
}

let profileBTN = document.querySelector("#profile-pic-btn button");
profileBTN.addEventListener('click', ()=>{
    document.getElementById("myDropdown").classList.toggle('show');
}
)

window.onclick = (e) =>{
    if (! e.target.matches("#profile-pic-btn button") && ! e.target.matches("#profile-pic-btn") && ! e.target.matches("#profile-pic-btn img")){
        let dropdown = document.getElementById("myDropdown");
        if (dropdown.classList.contains("show")){
            dropdown.classList.remove('show');
        }
        
    }
}