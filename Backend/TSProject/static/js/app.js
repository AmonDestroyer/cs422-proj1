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
    .then(response => {
        console.log(response)
        if (response.status === 200) {
            document.querySelector('#upSuccess').style.display = "inline";
        } else {
            document.querySelector('#upError').style.display = "inline";
        }
        document.getElementById('myFile').value = ""
    })
    .catch(error => console.log(error))
}


const convXlsx = (file) => {
    let reader = new FileReader();
    reader.readAsBinaryString(file);
    reader.onload = function() {
        let data = reader.result;
        let workbook = XLSX.read(data, {type: 'binary'});
        workbook.SheetNames.forEach(function(sheetName) {
            let XL_row_object = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], {header: 1});
            console.log(XL_row_object[0][11]);

            const setMeta = {
                "TS Set Name": XL_row_object[0][0],
                "Description": XL_row_object[0][1],
                "Application Domain(s)": XL_row_object[0][2],
                "Keywords": XL_row_object[0][3],
                "Vector Size": XL_row_object[0][4],
                "Min Length": XL_row_object[0][5],
                "Max Length": XL_row_object[0][6],
                "Number of TS in the Set": XL_row_object[0][7],
                "Start Datetime": XL_row_object[0][8],
                "Contributors": XL_row_object[0][9],
                "Related Paper Reference(s)": XL_row_object[0][10],
                "Related Paper Link": XL_row_object[0][11]
            }

            const seriesMeta = {
                "TS Name": XL_row_object[10][0],
                "Description": XL_row_object[2][0],
                "Domain(s)": XL_row_object[3][0],
                "Units": XL_row_object[4][0],
                "Keywords": XL_row_object[5][0],
                "Scalar/Vector": XL_row_object[6][0],
                "Vector Size": XL_row_object[7][0],
                "Length": XL_row_object[8][0],
                "Sampling Period": XL_row_object[9][0]
            }

            let seriesData = {}
            for (let i = 11; i < XL_row_object.length; i++) {
                seriesData["point" + String(i-11)] = XL_row_object[i][0]
            }
            

            const fullJson = {
                "setMeta": setMeta,
                "seriesMeta": seriesMeta,
                "seriesData": seriesData
            }
            console.log(fullJson);

            sendFile(JSON.stringify(fullJson))

        })
    }
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


    // DO THE FILE VALIDATION TO CHECK THAT ALL REQUIRED FIELD ARE FILLED IN


    switch (fileExtension) {
        case "txt":
            convCsv(fileInput.files[0])
            break;

        case "json":
            sendFile(JSON.stringify(fileInput.files[0]))
            break;

        case "csv":
            convCsv(fileInput.files[0])
            break;

        case "xlsx":
            convXlsx(fileInput.files[0])
            break;

        case "xls":
            convXlsx(fileInput.files[0])
            break;


        default:
            alert("Invalid file type")
            break;
    }
}
