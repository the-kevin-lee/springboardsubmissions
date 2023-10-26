const axios = require('axios');

let chosenNum = 5;
let baseURL = "https://numbersapi.com";


// 1. 
axios.get( `${baseURL}/${chosenNum}?json`)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.log('Error', error)
    });

// 2.

let bestNums = [1,2,3]
axios.get(`${baseURL}/${bestNums}?json`)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.log('Error', error);
    });


    // 3. Making four identical requests and appending the returned text to the body
Promise.all(
    Array.from({ length: 4 }, () => {
      return axios.get(`${baseURL}/${bestNums}?json`);
    })
  )
  .then(responses => {
    responses.forEach(response => {
      document.body.innerHTML += `<p>${response.data.text}</p>`; // Assuming this is running in a browser
    });
  })
  .catch(error => {
    console.log('Error', error);
  });