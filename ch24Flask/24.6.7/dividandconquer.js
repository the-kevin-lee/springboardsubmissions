//  FUNCTION countZeros

const countZeroes = (arr) => {
    let count = 0;
    for (i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            count++;
        }
    }
    return count;
}


// FUNCTION sortedFrequency

const sortedFrequency = (arr, val) => {
    let count = 0;
    for (i = 0; i < arr.length; i++) {
        if (arr[i] === val) {
            count++;
        }
    }
    return count;
}


// FUNCTION findRotatedIndex

const findRotatedIndex = (arr,val) => {
    for (i = 0; i < arr.length; i++) {
        if (arr[i] === val) {
            const theIndex = arr.indexOf(arr[i]);
            return theIndex;
        }
    }
    return -1;
}

// FUNCTION findRotationCount

const findRotationCount = (arr) => {
    let n = 0 
    for (let i = 0; i < arr.length; i++) {
        // logging the point at which the rotation has stopped
        if (arr[i] < arr[i-1]) {
            n=i;
            break;
        }
    }
    return n;
}




findRotationCount([15, 18, 2, 3, 6, 12]) // 2


// FUNCTION findFloor

const findFloor = (arr, x) => {
    let floor = -1;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === x) {
            return arr[i];
        }
        if (arr[i] < x) {
            floor = arr[i];
        }
        if (arr[i] > x) {
            break;
        }
    }   
    return floor;
}