// Getting DOM elements for server name input, server form, and server table body
let serverNameInput = document.getElementById('serverName');
let serverForm = document.getElementById('serverForm');
let serverTbody = document.querySelector('#serverTable tbody');

// Object to hold all servers and a variable for server ID
let allServers = {};
let serverId = 0;

// Adding an event listener to the server form for the submit event
serverForm.addEventListener('submit', submitServerInfo);

// Function to create a server object, add it to allServers, update the HTML table, and reset the input
function submitServerInfo(evt) {
  if (evt) evt.preventDefault(); // Preventing the default form submission action, especially when running tests

  let serverName = serverNameInput.value; // Getting the value of the server name input

  // If serverName is not empty, create a new server entry
  if (serverName !== '') {
    serverId++; // Increment server ID
    allServers['server' + serverId] = { serverName }; // Add new server object to allServers

    updateServerTable(); // Update the server table in the HTML

    serverNameInput.value = ''; // Reset the server name input
  }
}

// Function to update the server table in the HTML
function updateServerTable() {
  serverTbody.innerHTML = ''; // Clearing the table body

  // Looping through all servers in allServers object
  for (let key in allServers) {
    let curServer = allServers[key]; // Current server object

    let newTr = document.createElement('tr'); // Creating a new table row element
    newTr.setAttribute('id', key); // Setting the ID attribute of the table row

    let tipAverage = sumPaymentTotal('tipAmt') / Object.keys(allServers).length; // Calculating the average tip

    appendTd(newTr, curServer.serverName); // Appending the server name to the table row
    appendTd(newTr, '$' + tipAverage.toFixed(2)); // Appending the average tip to the table row

    serverTbody.append(newTr); // Appending the new table row to the table body
  }
}
