const fileInput = document.getElementById('myFile');
function fileValidation(){
    // Get file name
    const fileName = fileInput.files[0].name;
    // Gets the file path 
    const filePath = fileInput.value;

    // Gets the file extension
    const fileExtension = filePath.substring(filePath.indexOf('.') + 1).toLowerCase();

    //Check for file extension validation
    if (fileExtension === 'txt' || fileExtension === 'csv' || fileExtension === 'xlsx'
     || fileExtension === 'excel' || fileExtension === "JSON") {
        console.log("File accepted");
    }
    else{
        fileInput.value = "";
        alert("Invalid file type!")
    }
}

const upload = document.getElementById("upload"); 
upload.addEventListener("click", function(e){
    fileInput.value = ""; 
})