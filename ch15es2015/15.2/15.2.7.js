// ES2015 Global Constants

const PI = 3.14;

PI = 42 // Will throw an error


// 1) The difference between var and let is that var is function/global scoped while let is 
// block scoped. Var can be redeclared and reassigned while let cannot be redeclared but can be reassigned.
// Var can be accessed during hoisting before its actually assigned a value while let cannot.

// 2) Var is function/global scoped while const is block scoped. Var can be redeclared and reassigned while
// const can neither be redeclared or reassigned. Var can be accessed during hoisting before it's actually 
// assigned a value while const cannot.

// 3) Let and const work similarly in that they cannot be accessed during hoisting, cannot be redeclared, but 
// with let you can reassign a variable while const cannot be reassigned.

// 4) Hoisting is the rearrangement of any variable within the scope of which they're declared in. 
// Variables are moved to the top of the scope. For var, it can be accessed before its actual initialization,
// while let and const cannot be. Accessing let and const before their initalization will throw a ReferenceError
// while var will be undefined. 