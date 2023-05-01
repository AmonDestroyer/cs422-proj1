// add an event listener to the refresh button
const refreshButton = document.getElementById('refresh');
const solutionBox = document.getElementById("Solution-Box");
refreshButton.addEventListener('click', () => {
    fetch('/_get-solution/')
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        })
        .then(data =>
             {
                console.log(data);
            // do something with the retrieved data here
            const problem_table = document.getElementById('problem-table');
            for(const problem in data){
                for(const solution in data[problem]){
        
                    // Problem Set Information
                    const setName = data[problem][solution]["set name"];
                    const contributorFName = data[problem][solution]["contributor first name"];
                    const problemName = problem;
                    
                    // Insert a new problem row 
                    const newProblem = problem_table.insertRow();

                    // Insert cells for row information
                    const SetNameCell = newProblem.insertCell();
                    const ContriNameFCell = newProblem.insertCell();
                    const problemCell = newProblem.insertCell();
                    const solutionViewCell = newProblem.insertCell();

                    // Create Text Node to add to cell
                    const ContriNameFText = document.createTextNode(contributorFName);
                    const setNameText = document.createTextNode(setName);
                    const problemNameText = document.createTextNode(problemName);

                    //Create solution button
                    const solutionButton = document.createElement("button");
                    solutionButton.innerHTML = "View Solution";
                    // Add text to cell
                    SetNameCell.appendChild(setNameText);
                    ContriNameFCell.appendChild(ContriNameFText);
                    problemCell.appendChild(problemNameText);
                    solutionViewCell.appendChild(solutionButton);

                    // Create Solution Div 
                    const solutionDiv = document.createElement("div");
                    solutionDiv.id = "solutionDiv";
                    solutionBox.appendChild(solutionDiv);

                    // Create exit solution div button 
                    const exitButton = document.createElement("button"); 
                    exitButton.innerText = "Exit";
                    exitButton.id = "exit"
                    solutionDiv.appendChild(exitButton);

                    solutionButton.addEventListener("click", function(e){
                        console.log("solution button was clicked"); 
                        solutionDiv.style.disyplay = "block";
                    });
                    exitButton.addEventListener("click", function(e){
                        console.log("Exit button was clicked"); 
                        solutionDiv.style.display = "none";
                    })
                }
            }
        })
        .catch(error => {
            console.error(error);
        });
});
