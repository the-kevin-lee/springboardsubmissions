const fs = require('fs');
const process = require('process');
const axios = require('axios');


const cat = (path) => {
    fs.readFile(path, 'utf-8', function(err,data) {
        if (err) {
            console.error(`Error in reading ${path}: ${err}`)
            process.exit(1);
        }
        console.log(data);
    })
}


// part 2 

async function webCat(url) {
    try {
        let resp = await axios.get(url);
        console.log(resp.data);
    } catch (err) {
        console.log(`Error fetching ${url}: ${err}`);
        process.exit(1);
    }
}

let path = process.argv[2];

if (patch.slice(0,4) === 'http') {
    webCat(path);
} else {
    cat(path);
}