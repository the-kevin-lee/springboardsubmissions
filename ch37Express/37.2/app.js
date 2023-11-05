const express = require("express");

// import routes
const groceryRoutes = require("./groceryRoutes");


// instantiate express
const app = express();


app.use(express.json());


app.use((req,res,next) => {
    console.log(`${req.method} ${req.path}`);
    next();
});

//dummy test function
app.get('/test', (req,res) => {
    res.send("Test route is working!")
;})



// routing
app.use('/items', groceryRoutes)








module.exports = app;