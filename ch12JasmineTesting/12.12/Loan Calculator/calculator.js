let banner;


window.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById("calc-form");

  if (form) {
    document.getElementById("calc-submit").addEventListener('click', function () {
      //retrieve values
      getData();
    })

  }


  if (form) {

    form.addEventListener("submit", function (e) {
      //prevents form from loading into another page
      e.preventDefault();
      // removes previous result
      if (banner) {
        banner.remove();
      }
      //update is the function that will 1) calculate the monthly payment & 2) add the value into the DOM for display
      update();

    });
  }
});



function getData() {

  let loanAmount = document.getElementById("loan-amount").value;

  let loanYears = document.getElementById("loan-years").value;

  let loanRate = document.getElementById("loan-rate").value;

  console.log(loanAmount);
  console.log(loanYears);
  console.log(loanRate);

  return {
    loanAmount: loanAmount,
    loanYears: loanYears,
    loanRate: loanRate,
  }

}


function update() {
  //initial part to access data from getData();
  let data = getData();


  //part 1: calculate
  let P = data.loanAmount;
  let n = data.loanYears * 12;
  let i = data.loanRate / 12;

  let numerator = P * i;
  let denominator = 1 + i;
  denominator = denominator ** n;
  denominator = 1 / denominator;
  denominator = 1 - denominator;

  let finalValue = (numerator / denominator).toFixed(2);
  console.log(finalValue);
  // part 2: add value to DOM

  let span = document.getElementById("monthly-payment");

  let para = document.createElement("p");
  para.innerText = finalValue;

  banner = span.appendChild(para);



}