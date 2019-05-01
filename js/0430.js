// 반복 1 - while
let i = 0
while (i < 20) {
    console.log(i)
    i++
}

// 반복 2 - for
for (let j=0; j < 10 ; j++){
    console.log(j)
}

// 반복 3  - for of
for (let number of [1,2,3,4,5]) { //const로도 선언 가능
    console.log(number)
}


const numbers = [1,2,3,4]

console.log(numbers[0]) // index로 접근 가능
console.log(numbers[-1]) // -1은 인식할 수 없음
numbers.length // 배열의 길이 출력
numbers.push('a') // append
numbers.pop() // pop
numbers.unshift('a') // 가장 앞쪽에 넣기 & 빼기
numbers.shift()
numbers.reverse() // Reverse 뒤집기
numbers.includes(1) // 리스트에 있는지 없는지 확인하여 True/False 값 반환
numbers.indexOf('a') // 값의 INDEX 반환(가장 앞쪽에 있는) / 값이 없다면 -1 반환
numbers.join('') // 배열 합치기
numbers.slice(2,4) // 배열 slice
numbers.filter(function(x){return x>1}) // 함수

const my ={
    name : 'GENIE',
    'phone number' : '01044215122',
    appleProduects: {
        ipad : true,
        iphone : 'X'
        }
}

// JSON - JavaScript Object Notation (JS 객체 표기법)
JSON.stringify() // Object -> JSON string
JSON.parse() // JSON string -> Object

// 함수
// 방법 1 - 선언식
function add(num1, num2) {
    return num1 + num2
}
console.log('add : ' + add(1,2))

// 방법 2 - 표현식
const sub = function(num1,num2) {
    return num1 - num2
}
console.log('sub : ' + sub(5,3))

// Arrow Function
// 기존 방법
// const mul = function (num1,num2){
//     return num1 * num2
// }

const mul = (num1,num2) => {
    return num1 * num2
}

let square = (num) => {
    return num ** 2
}

// return 문 단 한줄이면 {} & return 생략 가능
square = (num) => num ** 2

// ()안의 인자가 하나뿐이면 ()도 생략 가능, 0개 일때는 생략 불가능
square = num => num ** 2
let noArgs = () => 'No args'

// object를 return한다면?? 괄호가 없으면 {}를 함수의 {}로 인식하기 때문에 ()가 필요!
let returnObject = () => {key:'value'}

// 함수의 기본 인자
const sayHello = (name="noName") => `hi, ${name}`
sayHello('John')
sayHello()

// 익명 함수
function (num) { return num ** 3 } // 세제곱
(num) => { return num ** 0.5} // 제곱근

// 익명 함수 즉시 호출
(function (num) { return num ** 3 })(3)