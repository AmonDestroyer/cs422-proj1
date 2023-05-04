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



async function handleFiles(solutionFile){
    let solution = {};

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

    const [valid, badFile] = validate([solution])
    if (!valid) {
        const e = document.querySelector('#upError')
        e.style.display = "inline";
        e.innerHTML = "Invalid file format. Please check " + badFile
    } else {
        const doubleJson = {trainSet: trainJson}
        sendFile(JSON.stringify(doubleJson))
    }
}

const sendFile = (json) => {
    fetch('/_solution/', {
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