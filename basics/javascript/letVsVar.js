// let vs var
// var can be re-declared and modified throughout the code
// let is block scoped

// var: 
console.log(a); // in case of var declarations: undefined
var a = 19;
console.log(a); // 19
// block example
{
    var a = 20;
    console.log(a); // 20
}
console.log(a); // 20
// var is not block scoped

// let:
// console.log(b); // ERROR=> ReferenceError: b is not defined
let b = 25;
console.log(b) // 25
// block example
{
    let b = 29;
    console.log(b) // 29
}
console.log(b) // 25
// let is block scoped

// let cant be re-declared:
let pName = "bharat"
console.log(pName) // bharat
// let pName = "mohan" // Cannot redeclare block-scoped variable 'pName'

// const can't be updated nor re-declared
const gender = "Male"
console.log(gender) // Male
// const gender = "Female" // Cannot redeclare block-scoped variable 'gender'
{
    const gender = "Female"
    console.log(gender) // Female
}
console.log(gender) // Male



