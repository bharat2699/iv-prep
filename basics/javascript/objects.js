// Dictionary in Python == Object in JS == JSON is Love == HashMap is nerdy

const myDetails = {
    "name": "Bharat",
    "age": 24,
    "wife": undefined,
    "is_cat": null,
    "income": BigInt(960000)
}
// Access values via . operator
console.log(myDetails.name) // Bharat
console.log(myDetails.cat) // undefined as key is not available
console.log(myDetails["is_cat"]) // Access value via key as index

