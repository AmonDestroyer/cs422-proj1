// import csvDownload from 'json-to-csv-export';

const refresh = document.getElementById("refresh"); 
const problemContainer = document.getElementById("problem-container");
// const solutionTable = document.getElementById("solution-table");

function generateTable(row, name){
    const nameCell = row.insertCell();
    const textName = document.createTextNode(name);
    nameCell.appendChild(textName)
}

function generateButton(row, button){
    const cell = row.insertCell();
    cell.appendChild(button);
}

function generateLightBox(){
    const lightbox = document.createElement("div");
    lightbox.id = "lightbox"; 

    const lightBoxContent = document.createElement("div"); 
    lightBoxContent.id = "boxContent"; 

    lightbox.appendChild(lightBoxContent);
    document.body.appendChild(lightbox); 
 
    return {lightbox, lightBoxContent};
}

function insertHeader(table, header){
    const newHeader = table.insertRow()
    
    for(let i = 0; i < header.length; i++){
        let cell = newHeader.insertCell(); 
        const name = document.createTextNode(header[i]);
        cell.appendChild(name);
    }
}

const jsonToCsv = (json, setId) => {
    let csv = ""
    for (let item in json['SolutionMetadata']) {
        csv += json['SolutionMetadata'][item] + ","
    }
    csv = csv.replace(/.$/,"\n")

    for (let item in json['TrainingSet']['setMeta']) {
        csv += json['TrainingSet']['setMeta'][item] + ","
    }
    csv = csv.replace(/.$/,"\n")

    for (let item in json['TrainingSet']['seriesMeta']) {
        csv += json['TrainingSet']['seriesMeta'][item] + ",\n"
    }

    csv += json['TrainingSet']["seriesMeta"]["TS Name"] + ",\n"
    for (let item in json['TrainingSet']['seriesData']) {
        csv += json['TrainingSet']['seriesData'][item] + ",\n"
    }

    console.log(csv);
    downloadFile(`solution${setId}.csv`, csv)
}

function downloadFile(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

function downloadSet(setId){
    fetch(`/_download-train-data?set_id=${setId}`)
        .then(function(response){
            if(response.ok){
                return response.text();
            }
            else{
                throw new Error("Failed to retrieve data!");
            }
        })
        .then(function(data){
            // downloadFile(`solution${setId}.json`, (data))
            console.log(data);
            jsonToCsv(JSON.parse(data), setId)
        })
        .catch(function(error) {
            console.log(error);
        });
}


refresh.addEventListener("click", function(e){
    const problemTable = document.createElement("table"); 
    problemContainer.innerHTML = "";
    document.getElementById("problem-container").appendChild(problemTable);
    fetch("/_get-solution")
        .then(function(response){
            if(response.ok){
                return response.json();
            }
            else{
                throw new Error("Failed to retrieve data!");
            }
        })
        .then(function(data){
            console.log(data);
            problemTable.id = "problem-table";
            
            const problemHeader = ["Problem Set Number", "Solution", "Download"]; 
            insertHeader(problemTable, problemHeader);
            for(let key in data){
                //New problem Row
                let newProblem = problemTable.insertRow();
                let problemName = `Set ID: ${key}`;

                //Populate Table
                generateTable(newProblem, problemName);
                

                // view solution button
                let solutionButton = document.createElement("button"); 
                solutionButton.innerHTML = "View Solution";
                solutionButton.id = "solutionButton";
                generateButton(newProblem, solutionButton);

                //Download Button 
                let download = document.createElement("button"); 
                download.innerHTML = "Download";
                download.id = "download";
                generateButton(newProblem, download);
                download.addEventListener("click", function(e){
                    downloadSet(key);
                    console.log(key);
                })
                
                let {lightbox, lightBoxContent} = generateLightBox();
    
                solutionButton.addEventListener("click", function(e){
                    lightbox.style.display = "block";
                })

                //Solution Table 
                const solutionTable = document.createElement("table");
                solutionTable.id = "solution-table";
                const header = ["Solution #", "Set Name", "Contributor First Name", 
            "Contributor Last Name", "Paper References", "Paper Link", "Error"];
                insertHeader(solutionTable, header);
    
                //Access Table header
                for(let solution in data[key]){    
                    const newSolution = solutionTable.insertRow();    
                    let setName = data[key][solution]["set name"];
                    let contributorFName = data[key][solution]["contributor first name"];
                    let contributorLName = data[key][solution]["contributor last name"];
                    let paperLink = data[key][solution]["paper link"];
                    let paperRef = data[key][solution]["paper reference"];
                    let error = data[key][solution]["error"];
                    let solutionNum = solution;
                    generateTable(newSolution, solutionNum);
                    generateTable(newSolution, setName);
                    generateTable(newSolution, contributorFName);
                    generateTable(newSolution, contributorLName);
                    generateTable(newSolution, paperRef);
                    generateTable(newSolution, paperLink);
                    generateTable(newSolution, error);
                }
                lightBoxContent.appendChild(solutionTable);

                //create exit button
                const exit = document.createElement("button"); 
                exit.innerHTML = "Exit";
                exit.id = "exit"; 
                lightBoxContent.appendChild(exit);

                exit.addEventListener("click", function(e){
                    lightbox.style.display = "none";
                })
            }
        })
        .catch(function(error) {
            console.log(error);
            // Re-enable the button on error
 
        });
})

