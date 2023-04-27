document.addEventListener("click", (event) => {
    if (event.target.id === "upload") {
        fileValidation(document.getElementById('myFile'))
    }
})


const sendFile = (file) => {
    fetch('/_upload-data/', {
        method: 'POST',
        body: file
    })
    .then(response => console.log(response))
}


const convCsv = (file) => {
    const reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function() {
        const data = reader.result;
        const arr = data.split('\n');

        const metaItems = arr[0].split(',');
        const setMeta = {
            "TS Set Name": metaItems[0],
            "Description": metaItems[1],
            "Application Domain(s)": metaItems[2],
            "Keywords": metaItems[3],
            "Vector Size": metaItems[4],
            "Min Length": metaItems[5],
            "Max Length": metaItems[6],
            "Number of TS in the Set": metaItems[7],
            "Start Datetime": metaItems[8],
            "Contributors": metaItems[9],
            "Related Paper Reference(s)": metaItems[10],
            "Related Paper Link": metaItems[11]
        }

        const seriesMeta = {
            "TS Name": arr[10].split(',')[0],
            "Description": arr[2].split(',')[0],
            "Domain(s)": arr[3].split(',')[0],
            "Units": arr[4].split(',')[0],
            "Keywords": arr[5].split(',')[0],
            "Scalar/Vector": arr[6].split(',')[0],
            "Vector Size": arr[7].split(',')[0],
            "Length": arr[8].split(',')[0],
            "Sampling Period": arr[9].split(',')[0]
        }

        let seriesData = {}
        for (let i = 11; i < arr.length; i++) {
            seriesData["point" + String(i-11)] = arr[i].split(',')[0]
        }

        const fullJson = {
            "setMeta": setMeta,
            "seriesMeta": seriesMeta,
            "seriesData": seriesData
        }

        console.log(fullJson)

        sendFile(JSON.stringify(fullJson))
    }

}


function fileValidation(fileInput){
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


    if (fileExtension === "csv") {
        convCsv(fileInput.files[0])
    }
}
