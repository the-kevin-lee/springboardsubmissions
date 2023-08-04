// function createInstructor(firstName, lastName){
//     return {
//       firstName: firstName,
//       lastName: lastName
//     }
//   }


//  OBJECT SHORTHAND

function createInstructor(firstName, lastName) {
    return {
        firstName,
        lastName
    }
}




// var favoriteNumber = 42;

// var instructor = {
//   firstName: "Colt"
// }

// instructor[favoriteNumber] = "That is my favorite!"



// COMPUTED PROPERTY NAME
const favoriteNumber = 42;

const instructor  = {
    firstname: "Colt",
    [favoriteNumber]: "That is my favorite!"

}



// var instructor = {
//     firstName: "Colt",
//     sayHi: function(){
//       return "Hi!";
//     },
//     sayBye: function(){
//       return this.firstName + " says bye!";
//     }
//   }


  //OBJECT METHODS


  const instructor = {
    firstName: "Colt",
    sayHi() {
        return "Hi!";
    } ,
    sayBye () {
        return this.firstName + "says bye!";
    }



  }



// createAnimal function



function createAnimal (species, verb, sound) {
    return obj = {
        species,
        [verb]: sound,
        [sound]: verb, 
    }
}