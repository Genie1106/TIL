// Array Helper Methods

// case1.
// ES5
var colors = ['red','blue','green']

for (var i=0; i<colors.length; i++){
    console.log(colors[i])
}

// ES6+ - forEach
const colors1 = ['red','blue','yellow']

colors1.forEach(function(color) { // callback function
    console.log(color)
})

// case 2.
// ES5
var numbers = [1,2,3]
var doubleNumbers = []

for (var i=0; i<numbers.length; i++){
    doubleNumbers.push(numbers[i]*2)
}

console.log(doubleNumbers)

// ES6+ - map
const numbers1 = [1,2,3]

const doubleNumbers1 = numbers1.map(function(number){
    return number*2
})

console.log(doubleNumbers1)

// case 3.
// ES6+ - filter
const products = [
    {name : 'cucmber', type : 'vegetable'},
    {name : 'banana', type : 'fruit'},
    {name : 'carrot', type : 'vegetable'},
    {name : 'apple', type : 'fruit'},
]

const fruitProducts = products.filter(function(product) {
    return product.type === "fruit"
    // 해당 조건이 true일 경우, item을 가져와 배열애 넣음
})

console.log(fruitProducts)

// case 4.
// ES6+ - find

const users = [
    {name : 'nwith'},
    {name : 'admin'},
    {name : 'zzuli'},
]

const founduser = users.find(function(user){
    return user.name === 'admin'
})

console.log(founduser)

// case 5.
// ES6+ - every & some

const computers = [
    {name : 'macbook', ram : 16},
    {name : 'gram', ram : 8},
    {name : 'series9', ram : 32},
]

const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16
})

const someComputersAvaliable = computers.some(function(computer){
    return computer.ram > 16
})

console.log(everyComputersAvailable)
console.log(someComputersAvaliable)