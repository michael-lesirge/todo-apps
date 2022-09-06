
UpdateCreateFormVisablity();

function UpdateCreateFormVisablity(){        
    if (getCookie('show-create-form') === "false"){
        document.getElementById('create-form').classList.add('d-none');
    }
    else{
        document.getElementById('create-form').classList.remove('d-none');
    }
}

function setCookie(cname, cvalue) {
    document.cookie = cname + '=' + cvalue + ';'
}

function getCookie(cname) {
    let name = cname + '=';
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return '';
}

document.getElementById('toggle-btn').onclick = function ToggleVisablity(){
    let cookie_info = getCookie('show-create-form')
    if (cookie_info === ''){
        cookie_info = "true"
    }
    UpdateCreateFormVisablity();
    setCookie('show-create-form', cookie_info === "false")
    
}
