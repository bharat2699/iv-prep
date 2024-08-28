//1. creating a string variable and adding number 1 to it
let a = "hello";
let b = a + 1
console.log(b) // hello1
// string concatenation


//2. tyeof of previous output
console.log(typeof b) //string, as expected




//3. creating a const object in JS and changing this const object to hold number
const obj1 = {
    "name": "bharat",
    "age": 24
}
// Ninja Tech: block scope with let and const 
{
    const obj1 = 24
    console.log(obj1) // 24
}
console.log(obj1) // { name: 'bharat', age: 24 }

//4. adding a key to const object
obj1["is_king"] = true
console.log(obj1) // { name: 'bharat', age: 24, is_king: true }
// Dual behavior of const 
// if its object => it can be updated/modified
// if its primitive DT => it can not be update/modified



