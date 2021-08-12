

// Getting an instance of the widget.
const widget = uploadcare.Widget('[role=uploadcare-uploader]');
// Selecting an image to be replaced with the uploaded one.
const preview = document.getElementById('photo');
// "onUploadComplete" lets you get file info once it has been uploaded.
// "cdnUrl" holds a URL of the uploaded file: to replace a preview with.
let info;

widget.onUploadComplete(fileInfo => {
    info = fileInfo;
    document.getElementById("id_hidden_image").value = fileInfo.cdnUrl
    preview.src = fileInfo.cdnUrl;
});


let icon = document.querySelector(".edit-icon");
let btn = document.querySelector(".uploadcare--widget__button_type_open");
btn.style.display = 'hidden';
icon.addEventListener("click", ()=>{
    btn.click();
})