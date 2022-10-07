---
title: Lodash (Javascript Library)
description: Lodash is a Javascript library that provides utility methods for convenience, which are not by default provided with the vanilla javascript. Lodash Library is very light weight (Just 4KB gzipped) and this is the top #1 library by downloads in NPM registry
created: 2019-06-21
updated: 2019-06-21
---

Lodash is a Javascript library that provides utility methods for convenience, which are not by default provided with the vanilla javascript. Lodash Library is very light weight (Just 4KB gzipped) and this is the top #1 library by downloads in NPM registry

## Usage
1. In Browser
Using a CDN
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.min.js"></script>
```
If you download lodash.js file
```html
<script src="lodash.js"></script>
```

2. Using NPM

```sh
npm i lodash
```

## Arrays

#### 1. chunk
Splits the given array into chunks with the chunk size provided
 ```javascriopt
_.chunk(['a', 'b', 'c', 'd', 'e'], 2); // => [['a', 'b'], ['c', 'd'], ['e]]
 ```

#### 2. compact
Removes `false, null, 0, "", undefined, NaN` from a given array

#### 3. concat
creates and returns a new array by concatinating fiven array elements/ raw elements
```javascript
_.concat([1, 2], 3, [4]); // => [1, 2, 3, 4]
```
Note: This only concatenate at 1 level of arrays, if you want to concatenate to multi level deep apply flatten too.

#### 4. drop
dropns given number of elements from an array from array start
```javascript
_.drop([1, 2, 3, 4], 2); // => [3, 4]
```
#### 5. flatten
flatten given array to single level deep. 
```javascript
_.flatten([0, 1, [2, 3, 4], [5, [6]], 7]) // => [0, 1, 2, 3, 4, 5, [6], 7]
```

#### 6. flattenDeep
Recursively flattens given array
```javascript
_.flatten([0, 1, [2, 3, 4], [5, [6]], 7]) // => [0, 1, 2, 3, 4, 5, 6, 7]
```

## String

#### 1. Capitalize
The  _.capitalize() method is used to convert the first character of string to upper case and the remaining to lower case.
```javascript
let str1 = _.capitalize("ONE__COMPILER__CHEATSHEETS");
console.log(str1);// "One__Compiler__Cheatsheets"
  
let str2 = _.capitalize("ONE COMPILER CHEATSHEETS");
console.log(str2);// "One Compiler Cheatsheets"
```

#### 2. camelCase
The _.camelCase() method is used to convert a string into a camel case string. The string can be space-separated, dash-separated, or can be separated by underscores.
```javascript
let str1 = _.camelCase("ONE__COMPILER__CHEATSHEETS");
console.log(str1);// "oneCompilerCheatsheets"
  
let str2 = _.camelCase("ONE COMPILER CHEATSHEETS");
console.log(str2);// "oneCompilerCheatsheets"
```

## Collection

#### 1. find
return the first element that matches predicate
```javascript
_.find([-1, 0, 1, 2, 3], ele => ele > 0) // => 1
```

## Date
#### 1. now
returns the current time in milliseconds
```javascript
_.now() // => 1561104924053
```

## Function
#### 1. delay
Invokes a function after given wait time (in milliseconds). extra args will be passed to the function when invoked. 
```javascript
_.delay(func, 1000, arg1, arg2, arg3);
```

## Lang
#### 1. isArray
return true if given arg is an array
```javascript
_.isArray([1, 2]); // => true
_.isArray(1); // => false
```

## Math
#### 1. mean
computes mean value of the values in given array
```javascript
_.mean([5,10,85, 100]); // => 50
```

## Number
#### 1. random
provides a random number. lower & upper numbers are optional. If you do not provide any lower or upper, it returns a random between 0 to 1
```javascript
_.random(100); // => integer between o and 100
_.random(); // => floating-point between 0 to 1
_.random(10, 20); // => integer between 10 to 20
```

## Object
#### 1. get
reads the value at given path
```javascript
const user = {
    _id: 1,
    address: {
        streetAddress : "Foo"
    }
}
_.get(user, 'address.streetAddress'); // => Foo
```
