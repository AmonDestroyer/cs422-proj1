const request = document.getElementById("problem");
const lightbox = document.getElementById("light-box");
const exit = document.getElementById("close");

const next = document.getElementsById("next");
const back = document.getElementById("back");


request.addEventListener("click", function(e){
    console.log("Request sent")
    lightbox.style.display = "block";
});

exit.addEventListener("click", function(e){
    console.log("Close request")
    lightbox.style.display = "none";
})