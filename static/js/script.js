let search_bar = document.querySelector('.navbar input[type=search]');
let search_style = search_bar.style;
let login = document.querySelectorAll('.register-btn')[0];
let sign_up = document.querySelectorAll('.register-btn')[1];
let login_style = login.style;
let sign_up_style = sign_up.style;


let restyler = ()=>{
    if (window.innerWidth < 900){
        search_bar.style.width = '200px';
        sign_up.style = 'width:80px;padding:5px 0px';
        login.style = 'width:80px;padding:5px 0px';
        if (window.innerWidth < 700){
            search_bar.style.display = 'none';
            if (window.innerWidth <570){ sign_up.style.margin = '10px 10px';login.style.margin = '10px 0px'}
            if (window.innerWidth < 500){
                sign_up.style.display = 'none';
                login.style.display = 'none';
            }else{
                sign_up.style.display = 'inline-block';
                login.style.display = 'inline-block';
            }
        }else{
            search_bar.style.display = 'inline-block';
        }
    }else{
        search_bar.style = search_style;
        sign_up.style = sign_up_style;
        login.style = login_style;
    }
};

restyler();

window.onresize = restyler;