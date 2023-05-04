const refresh = document.getElementById("refresh"); 
const problemTable = document.getElementById("problem-table");

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

    const exit = document.createElement("button"); 
    exit.innerHTML = "Exit";
    exit.id = "exit"; 

    lightBoxContent.appendChild(exit);
    lightbox.appendChild(lightBoxContent);
    document.body.appendChild(lightbox); 
 
    return {lightbox, exit};
}


refresh.addEventListener("click", function(e){
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
            let setName;
            let contributorName;
            for(let key in data){
                //New problem Row
                let newProblem = problemTable.insertRow();
                let problemName = key;

                //Populate Table
                generateTable(newProblem, contributorName);
                generateTable(newProblem, setName);
                generateTable(newProblem, problemName);

                // view solution button
                let solutionButton = document.createElement("button"); 
                solutionButton.innerHTML = "View Solution";
                generateButton(newProblem, solutionButton);

                let {lightbox, exit} = generateLightBox();
                console.log(exit);
                solutionButton.addEventListener("click", function(e){
                    console.log("View Solution Button was clicked");
                    lightbox.style.display = "block";
                })

                exit.addEventListener("click", function(e){
                    lightbox.style.display = "none";
                })
                
                //Access contributor name and set name
                for(let solution in data[key]){
                    setName = data[key][solution]["set name"];
                    contributorName = data[key][solution]["contributor first name"]
                }
            }
        })
})

