fetch('_get-train-data/', {
    method: 'GET',
    body: json
})
.then(response => {
    console.log(response);
    console.log("Sucessfully gotten data");

})
.then(data =>{
    console.log(data);
    // const problemDisplay = document.getElementById('table');
    // data.forEach(item=>{
    //     const row = document.createElement("tr");
    //     const nameCell = document.createElement("td");
    //     nameCell.textContent = item.namel; 
    //     c
    // })
})
.catch(error => {
    console.error(error);
});