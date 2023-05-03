const request = document.getElementById("problem");
const lightbox = document.getElementById("light-box");
const exit = document.getElementById("close");

const next_ = document.querySelectorAll(".next");
const back_ = document.querySelectorAll("previous");
const pages = document.querySelectorAll(".page");

let pageNumber = 0;

function showPage(pageIndex){
    for(let i = 0; i < pages.length; i++){
        const page = pages[i];
        if(i == pageIndex){
            page.classList.add('active');
        }
        else{
            page.classList.remove('active');
        }
    }
}

function nextPage(){
    pageNumber++; 
    if(pageNumber >= pages.length){
        pageNumber = 0;
    }
    showPage(pageNumber);
}

function prevPage(){
    pageNumber--; 
    if(pageNumber < 0){
        pageNumber = pages.length - 1;
    }
    showPage(pageNumer);
}

request.addEventListener("click", function(e){
    console.log("Request sent")
    showPage(0)
    lightbox.style.display = "block";
});

exit.addEventListener("click", function(e){
    console.log("Close request")
    lightbox.style.display = "none";
})

next_.forEach(function(element) {
    element.addEventListener("click", function(e){
      nextPage();
    });
  });
  
  back_.forEach(function(element) {
    element.addEventListener("click", function(e){
      prevPage();
    });
  });
  