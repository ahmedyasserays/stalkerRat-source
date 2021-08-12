let firstNameField = document.getElementById("id_first_name");
firstNameField.setAttribute("placeholder", 'First Name');
firstNameField.setAttribute("autocomplete", 'given-name');
firstNameField.focus();
firstNameField.style.paddingRight = '0px';
let lastNameField = document.getElementById("id_last_name");
lastNameField.setAttribute("placeholder", 'Last Name');
lastNameField.setAttribute("autocomplete", 'family-name');
lastNameField.style.paddingRight = '0px';
let userNameField = document.querySelector("input[name=username]");
userNameField.setAttribute("placeholder", 'User Name');
userNameField.setAttribute("autocomplete", 'username');
let emailField = document.querySelector("input[type=email]");
emailField.setAttribute("placeholder", 'Email');
emailField.setAttribute('autocomplete', 'email');
let firstPassword = document.getElementById("id_password1");
firstPassword.setAttribute("placeholder", "password");
firstPassword.setAttribute("autocomplete", "new-password");
let secondPassword = document.getElementById("id_password2");
secondPassword.setAttribute("placeholder", "Repeat your password");
secondPassword.setAttribute("autocomplete", "new-password");

if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}