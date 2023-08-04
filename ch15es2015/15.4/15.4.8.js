// function filterOutOdds() {
//     var nums = Array.prototype.slice.call(arguments);
//     return nums.filter(function(num) {
//       return num % 2 === 0
//     });
//   }


// #1 
function filterOutOdds(...nums) {
    return nums.filter(num => num % 2 === 0);
}




// #2 

const findMin = (...args) => {
    return  Math.min(...args);
}


// #3

function mergeObjects(obj1, obj2) {
    return {...obj1,...obj2};
}


// #4 

const doubleAndReturnArgs = (arr, ...addons) => [...arr,...addons.map(num => num * 2)];










// #5 SLICE AND DICE
//
/** remove a random element in the items array
and return a new array without that item. */

function removeRandom(items) {
    const ind = Math.floor(Math.random() * items.length);
    return [...items.slice(0,ind), ...items.slice(ind+1)];

}

/** Return a new array with every item in array1 and array2. */

function extend(array1, array2) {
    return [...array1,...array2];
}

/** Return a new object with all the keys and values
from obj and a new key/value pair */

function addKeyVal(obj, key, val) {
    const obj1 = {...obj};
    obj1[key] = val;
    return obj1;
}


/** Return a new object with a key removed. */

function removeKey(obj, key) {
    const newObj = {...obj};
    delete newObj[key];
    return newObj;
}


/** Combine two objects and return a new object. */

function combine(obj1, obj2) {
    const newerObj = {...obj1, ...obj2};
    return newerObj;
}


/** Return a new object with a modified key and value. */

function update(obj, key, val) {
    const someObj = {...obj};
    someObj[key] = val;
    return someObj;
}


