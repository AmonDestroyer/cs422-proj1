const refresh = document.getElementById("refresh"); 
const problemTable = document.getElementById("problem-table");
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

function insertHeader(solutionTable){
    const newHeader = solutionTable.insertRow()
    const header = ["Solution #", "Set Name", "Contributor First Name", 
            "Contributor Last Name", "Paper References", "Paper Link", "Error"];
    for(let i = 0; i < header.length; i++){
        let cell = newHeader.insertCell(); 
        const name = document.createTextNode(header[i]);
        cell.appendChild(name);
    }
}

refresh.addEventListener("click", function(e){
    problemTable.innerHTML = "";
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
            for(let key in data){
                //New problem Row
                let newProblem = problemTable.insertRow();
                let problemName = key;


                //Populate Table
                generateTable(newProblem, problemName);

                // view solution button
                let solutionButton = document.createElement("button"); 
                solutionButton.innerHTML = "View Solution";
                generateButton(newProblem, solutionButton);

                let {lightbox, lightBoxContent} = generateLightBox();
    
                solutionButton.addEventListener("click", function(e){
                    lightbox.style.display = "block";
                })


                //Solution Table 
                const solutionTable = document.createElement("table");
                solutionTable.id = "solution-table";
                insertHeader(solutionTable);
    
                //Access contributor name and set name
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

