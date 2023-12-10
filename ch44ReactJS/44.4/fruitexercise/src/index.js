import {fruits} from './foods';
import {choice, remove} from './helpers';



let chosenFruit = choice(fruits);
console.log(`I'd like one ${chosenFruit} please.`)
console.log(`Here you go: ${chosenFruit}`);
console.log(`Delicious, may I have another?`);


remove(fruits,chosenFruit);
let fruitsLeft = fruits.length;
console.log(`I'm sorry. We're all out. We have ${fruitsLeft} left.`);
