function fileValidation(){
    let fileInput = document.getElementById('myFile');
    // Get file name
    const fileName = fileInput.files[0].name;
    
    // Gets the file path 
    const filePath = fileInput.value;

    // Gets the file extension
    const fileExtension = filePath.substring(filePath.indexOf('.') + 1).toLowerCase();

    //Check for file extension validation
    if (fileExtension === 'txt' || fileExtension === 'csv' || fileExtension === 'xlsx'
     || fileExtension === 'excel' || fileExtension === "JSON") {
        console.log("File accepted")
    }
    else{
        fileInput.value = "";
        alert("Invalid file type!")
    }
}

// allows the dat
$(function() {
    $('input[name="daterange"]').daterangepicker({
      opens: 'left'
    }, function(start, end, label) {
      console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
    });
  });

const uploadButton = document.getElementById("upload");
const date = document.getElementById("dateSelector");

uploadButton.addEventListener("click", function(e){
    const dateVal = date.value
    const startDate = dateVal.slice(0, 10);
    const endDate = dateVal.slice(14, 23);
    e.preventDefault();
    console.log("the button was clicked!");
    console.log(`${date.value} is the date`);
    console.log(`${startDate}, ${endDate} are the start and end dates`);

})