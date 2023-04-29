document.addEventListener("click", (event) => {
    if (event.target.id === "upload") {
        handleFiles(document.getElementById('trainFile'), document.getElementById('testFile'))
    }
})

const jsonToCsv = (json) => {
    let csv = ""
    for (const [key, value] of Object.entries(json['setMeta'])) {
        csv += value + ","
    }
    csv = csv.replace(/.$/,"\n")
    for (const [key, value] of Object.entries(json['seriesMeta'])) {
        csv += value + ",\n"
    }
    csv += json["seriesMeta"]["TS Name"] + ",\n"
    for (const [key, value] of Object.entries(json['seriesData'])) {
        csv += value + ",\n"
    }

    console.log(csv);
    download("test.csv", csv)
}


function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
  
    document.body.removeChild(element);
  }




function xlsxToJson(file) {

    // return new Promise((resolve, reject) => {
    //     const reader = new FileReader();
    //     reader.readAsText(file);
    //     reader.onload = () => resolve(
    //         process(reader.result)
    //     );
    // })

    // function process(result) {
    //     let data = result;
    //     let workbook = XLSX.read(data, {type: 'binary'});
        
    //     workbook.SheetNames.forEach(function(sheetName) {
    //         let XL_row_object = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], {header: 1});

    //         const setMeta = {
    //             "TS Set Name": XL_row_object[0][0],
    //             "Description": XL_row_object[0][1],
    //             "Application Domain(s)": XL_row_object[0][2],
    //             "Keywords": XL_row_object[0][3],
    //             "Vector Size": XL_row_object[0][4],
    //             "Min Length": XL_row_object[0][5],
    //             "Max Length": XL_row_object[0][6],
    //             "Number of TS in the Set": XL_row_object[0][7],
    //             "Start Datetime": XL_row_object[0][8],
    //             "Contributors": XL_row_object[0][9],
    //             "Related Paper Reference(s)": XL_row_object[0][10],
    //             "Related Paper Link": XL_row_object[0][11]
    //         }

    //         const seriesMeta = {
    //             "TS Name": XL_row_object[10][0],
    //             "Description": XL_row_object[2][0],
    //             "Domain(s)": XL_row_object[3][0],
    //             "Units": XL_row_object[4][0],
    //             "Keywords": XL_row_object[5][0],
    //             "Scalar/Vector": XL_row_object[6][0],
    //             "Vector Size": XL_row_object[7][0],
    //             "Length": XL_row_object[8][0],
    //             "Sampling Period": XL_row_object[9][0]
    //         }

    //         let seriesData = {}
    //         for (let i = 11; i < XL_row_object.length; i++) {
    //             seriesData["point" + String(i-11)] = XL_row_object[i][0]
    //         }
            

    //         const fullJson = {
    //             "setMeta": setMeta,
    //             "seriesMeta": seriesMeta,
    //             "seriesData": seriesData
    //         }
    //         console.log(fullJson);

    //         return fullJson
    //     })
    // }
}


function csvToJson(file) {

    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsText(file);
        reader.onload = () => resolve(
            process(reader.result)
        );
    })

    function process(result) {
        const data = result
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

        return fullJson
    }
}


const readJson = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsText(file);
        reader.onload = () => resolve(
           JSON.parse(reader.result)
        );
    })
}


const validate = (files) => {
    let goodInput = true
    let badFile = "trainFile"

    for (const file of files) {
        console.log(file);

        const setMeta = file['setMeta']
        const seriesMeta = file['seriesMeta']

        if (
            setMeta['TS Set Name'] === "" ||
            setMeta['Min Length'] === "" ||
            setMeta['Max Length'] === "" ||
            setMeta['Contributors'] === "" ||
            setMeta['Start Datetime'] === "" ||

            seriesMeta['TS Name'] === "" ||
            seriesMeta['Units'] === "" ||
            seriesMeta['Scalar/Vector'] === "" ||
            seriesMeta['Length'] === "" ||
            seriesMeta['Sampling Period'] === ""
            ) {
                goodInput = false
                break
        }
        badFile = "testFile"
    }
    return [goodInput, badFile]
}


async function handleFiles(trainFile, testFile){
    let trainJson = {}
    let testJson = {}

    const trainFilePath = trainFile.value;
    const trainFileExtension = trainFilePath.substring(trainFilePath.indexOf('.') + 1).toLowerCase();
    switch (trainFileExtension) {
        case "json":
            trainJson = await readJson(trainFile.files[0])
            break;

        case "csv":
            trainJson = await csvToJson(trainFile.files[0])
            break;

        // case "xlsx":
        //     convXlsx(trainFile.files[0])
        //     break;

        // case "xls":
        //     convXlsx(trainFile.files[0])
        //     break;


        default:
            alert("Invalid file type")
            break;
    }

    const testFilePath = testFile.value;
    const testFileExtension = testFilePath.substring(testFilePath.indexOf('.') + 1).toLowerCase();
    switch (testFileExtension) {
        case "json":
            testJson = await readJson(testFile.files[0])
            break;

        case "csv":
            testJson = await csvToJson(testFile.files[0])
            break;

        // case "xlsx":
        //     convXlsx(trainFile.files[0])
        //     break;

        // case "xls":
        //     convXlsx(trainFile.files[0])
        //     break;


        default:
            alert("Invalid file type")
            break;
    }


    const [valid, badFile] = validate([trainJson, testJson])
    if (!valid) {
        const e = document.querySelector('#upError')
        e.style.display = "inline";
        e.innerHTML = "Invalid file format. Please check " + badFile
    } else {
        const doubleJson = {trainSet: trainJson, testSet: testJson}
        sendFile(JSON.stringify(doubleJson))
    }

}


const sendFile = (json) => {
    fetch('/_upload-data/', {
        method: 'POST',
        body: json
    })
    .then(response => {
        console.log(response)
        if (response.status === 200) {
            document.querySelector('#upSuccess').style.display = "inline";
        } else {
            document.querySelector('#upError').style.display = "inline";
        }

    })
    .catch(error => console.log(error))
}
