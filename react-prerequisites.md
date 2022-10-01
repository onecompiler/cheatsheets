---
title: React Prerequisites
description: Latest & Greatest Javascript features you need to know before starting with react
created: 2018-11-07
updated: 2018-11-07
---

## Pre-requisites to learn React

### Good to know
* Server Side Rendering (SSR), Client Side Rendering(CSR )
* JSX
* Transpiling (Babel)
* PWA (Progressive Web App)
* Chrome V8, Node, NPM
* TypeScript (Strict syntactical superset of JavaScript)


---

* Impure Functions with Side Effects & Pure Functions
		`Maintaining referential transparency`
* Stateful & Stateless 
		`Pure functions are stateless` 

* Mutability & Immutability
		`By design JS is mutable`
        `Object.freeze(obj)`, ` npm deep-freeze`
        `immutable.js, support from Lodash, underscorejs `
		` Immutable state tree is a must in Redux`       

* Imperative (how: `for`), Declarative (what: `.map`)
* Higher-order Functions

---


* Functional Programming with JS
* Observables (streams) Hot & Cold
* Reactive Programming (RxJS)
	`Propagating and responding to incoming events over time, declaratively`


---

## Javascript versions

| Version | Year | Version| Features added |
|--------|--------|--------|--------|
|5|2009|ECMAScript 5|strict mode, JSON support|
|6|2015|ECMAScript 2015 (ES 6)|let, const, Modules, Promises, Classes & Inheritance, Template Literals, Object destructing, Generators, Map and Set, default parameter values|
|7|2016|ECMAScript 2016|Array.includes(), `**`|
|8|2017|ECMAScript 2017|Async Functions, Object.entries|
|9|2018|ECMAScript 2018|Spread operator |

---

## JSON Support

```javascript
const userObj = {
	name: "Foo",
	age : 27,
	roles : ["admin", "user"]
};

const userObjString = JSON.stringify(userObj);
const userObjFromString = JSON.parse(userObjString);

```

---

##   let, const

* var has function scope, i.e its accessible inside the function it declared 

```javascript

var arr = [ "zero", "one", "two" ];
var functions = [];

for(var i=0; i<arr.length-1; i++) {
	functions.push(function() {
		return arr[i];
	});
}
console.log('0:', functions[0](), '1:', functions[1]());
        
```
* let block scope
* const also block scope 


---

## Arrow functions

```javascript
let square = function(inp){
	return inp ** 2
}

```
```javascript
let square = inp => inp ** 2
```

example
```javascript
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

const squaresOfEvenNumbers = numbers
.filter(ele => ele % 2 == 0)
.map(ele => ele ** 2)
.reduce((acc, ele) => acc + ele);

console.log(squaresOfEvenNumbers);


```
---

## String templating


<br>

```javasctipt
let name = 'foo';
console.log(`hello ${name} 2+2 is ${2+2}`);

```


---

## Object Destructuring

```javascript 
let user = { firstName: "foo", lastName: "bar", 
	     age: 27, junk: "bla"};

// Assigning to variables
let {firstName, age} = user;
let {firstName : f, age : a} = user;

// Using methods
function displayUserAge({firstName, age}){
	console.log(`${firstName}'s age: ${age}`)
}
```

---

## Default Values

```javascript 
function setName(name = "NA"){
	return name;
};
console.log(setName()); // NA
console.log(setName("foo")); // foo

func = function({x = 10,y = 11,z = 12} = {x:1,y:2,z:3}) {
    console.log(x,y,z);
};

func(); // ?
func({}); // ?

```

---

## Default Values

```javascript 
function setName(name = "NA"){
	return name;
};
console.log(setName()); // NA
console.log(setName("foo")); // foo

func = function({x = 10,y = 11,z = 12} = {x:1,y:2,z:3}) {
    console.log(x,y,z);
};

func(); //1 2 3  (hits the object literal default)
func({}); //10 11 12   (hits the value defaults)

```

---

## Spread Operators 

```javascript
const naturalNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const wholeNumbers = [0, ...naturalNumbers];

const negativeNumbers = naturalNumbers.map(ele => -ele);

const integers = [...negativeNumbers, ...wholeNumbers];
```

Example

```javascript
let obj = {a: 1, b:2, c:3, d:4, e: 5, f:6, g: 7};

let{a, b, ...others} = obj;

```

---

## Fetch API

```javascript
//GET
fetch('https://jsonplaceholder.typicode.com/todos')
      .then(res => res.json())
      .then(json => console.log(json))

//FORM POST
const userObj = {name: "Foo"}

fetch([url], { method: 'POST',
		body: Json.stringify(userObj)})
		.then(res => res.text())
		.then(text => console.log(text))

```
---

## ~~Flow Generators~~, Promise, Async & Await

```javascript
async getTodos(userObj){
	const res = await fetch([url]);
	const data = await res.json()    
	return data;
}

let data = await getTodos({fn: "foo"});

```

---

## Classes 

Classes are Functions (Functions are Objects)

```javascript
class User{

	constructor(name, age) {
		this.name = name;
		this.age = age;
	}
    
	sayHello(){
		return `Hi ${this.name}`
	}
}

const user1 = new User('foo', 27);
const user2 = new User('bar', 28);

```

---

## Module system


```javascript
\utils.js
--------

const username = "foo";
const password = "bar";

const config = { maxConn: 10, delay: 30000 };

function connect(username, password){
	return connection;
}

export { username, password };
export config;
export default connect; // at most one


\index.js
---------
import connect, {username as foo, config} from './utils.js';

```
---
## Classes with module  system

```javascript
user.js
-------
class User{

	constructor(name, age) {
		this.name = name;
		this.age = age;
	}
    
	sayHello(){
		return `Hi ${this.name}`
	}
}
export default User;

index.js
--------
import User from './user.js';

const user1 = new User('foo', 27);
const user2 = new User('bar', 28);

```

---
## NPM
```jsom
{
  "name": "my_package",
  "version": "1.0.0",
  "dependencies": {
    "my_dep_1": "2.1.0",
	"my_dep_2": "~version", // allows patch 
	"my_dep_3": "^version", // allows patch and minor updates
	"my_dep_4": "=version", // "my_dep_4": "version",
	"my_dep_5": ">version",
	"my_dep_6": ">=version",
	"my_dep_7": "<version",
	"my_dep_8": "<=version",
	"my_dep_9": "*",
	"my_dep_10": "latest",
  },
  "devDependencies" : {
    "my_test_framework": "3.1.0"
  }
}
```

---

Example Projects:

[https://codesandbox.io/s/4xx659x11x](https://codesandbox.io/s/4xx659x11x)
