
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
            for(const key in data){
                for(const solution in data[key]){
                    // Problem Set Information
                    const setName = data[key][solution]["set name"];
                    console.log(data[key][solution]["paper link"]);

            //         console.log(setName);
            //         const contributorFName = data[key][solution]["contributor first name"];
            //         const problemName = key;
            //         const errorCalc = data[key][solution]["error"];
                    
            //         // Insert a new problem row 
            //         const newProblem = problem_table.insertRow();

            //         // Insert cells for row information
            //         const SetNameCell = newProblem.insertCell();
            //         const ContriNameFCell = newProblem.insertCell();
            //         const problemCell = newProblem.insertCell();
            //         const solutionViewCell = newProblem.insertCell();
            //         const errorCell = newProblem.insertCell();

            //         // Create Text Node to add to cell
            //         const ContriNameFText = document.createTextNode(contributorFName);
            //         const setNameText = document.createTextNode(setName);
            //         const problemNameText = document.createTextNode(problemName);
            //         const errorText = document.createTextNode(errorCalc);

            //         //Create solution button
            //         const solutionButton = document.createElement("button");
            //         solutionButton.innerHTML = "View Solution";
            //         // Add text to cell
            //         SetNameCell.appendChild(setNameText);
            //         ContriNameFCell.appendChild(ContriNameFText);
            //         problemCell.appendChild(problemNameText);
            //         solutionViewCell.appendChild(solutionButton);
            //         errorCell.appendChild(errorText);

            //         // Create Solution Div 
            //         const solutionDiv = document.createElement("div");
            //         solutionDiv.id = "solutionDiv";
            //         solutionBox.appendChild(solutionDiv);

            //         // Create exit solution div button 
            //         const exitButton = document.createElement("button"); 
            //         exitButton.innerText = "Exit";
            //         exitButton.id = "exit"
            //         solutionDiv.appendChild(exitButton);

            //         solutionButton.addEventListener("click", function(e){
            //             console.log("solution button was clicked"); 
            //             solutionDiv.style.display = "block";
            //         });
            //         exitButton.addEventListener("click", function(e){
            //             console.log("Exit button was clicked"); 
            //             solutionDiv.style.display = "none";
            //         })
                }
             }
        })
        .catch(error => {
            console.error(error);
        });
});
