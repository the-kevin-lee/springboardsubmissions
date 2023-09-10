
let scoreCount = 0;
let tries = 0;
const currScores = [];

let startTime = Date.now();
let timer = setInterval(function () {
    if (Date.now() - startTime >= 15000) {
        clearInterval(timer);
        alert("Time's up!");

        currScores.push(scoreCount);
        let highestScore = Math.max(currScores);

        axios.post('/finalized', { scoreCount: scoreCount, tries: tries, highestScore:highestScore }, {
            headers: { 'Content-Type': 'application/json' }
        }).then(finalresponse => {
            // let finalVals = finalresponse.data.result;
            
            console.log(finalresponse);
            window.location.href = '/end-of-game';


        })
        .catch(error => {
            console.log('Error!', error);
        })


    }
}, 1000)




$("#guess-form").on("submit", function (event) {

    event.preventDefault(); // prevents loading after submission

    let word = $("#guess").val();



    // AJAX request to server
    axios.post('/verify-word', { word: word }, {
        headers: { 'Content-Type': 'application/json' }
    })

        .then(response => {
            console.log(response.data.result); // logs the returned message


            // extracting the 'result' from the server to then analyze vvvvvvvv
            let result = response.data.result;


            tries ++;


            //  analysis and handling
            if (result === 'ok') {
                alert("Awesome!");
                scoreCount += word.length;
                $('#score-box').text(scoreCount.toString());
            } else if (result === 'not-on-board') {
                alert('Word is not on board!')
            } else {
                alert('Not a valid word!')
            }
        })
        .catch(error => {
            console.log('Error!', error)
        })

})


