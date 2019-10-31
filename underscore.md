---
title: underscore (Javascript Library)
description: Underscore is a javascript library which supports usual function helpers like(map, reduce, filter, pick, each...) without extending any built-in objects.
created: 2019-10-19
updated: 2019-10-19
---

Underscore is a javascript library which supports usual function helpers like(map, reduce, filter, pick, each...) without extending any built-in objects.

## Installation

1. Using NPM:

```sh
npm install underscore
```

## Object functions

###pick   _.pick(object, keys)

``` javascript
const obj = {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19"}
_.pick(obj, userId, post, created);   // returns filtered object with selected keys
// prints { userId: "Madhav", post: "underscore.md",  "created": "2019-10-19"}
```, 

### extend    _.extend(object, newObject)

```javascript
const obj = {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19"}
_.extend(obj, {updated: "2019-10-19"})  // returns a object with updated key in it

// prints  {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19", updated: "2019-10-19"}
```

###invert    _.invert(object) 

``` javascript
const obj = {1: id, "underscore.md": "post", "Madhav": "userId"}
_.invert(obj);   // makes keys as values and values as keys
// prints {id: 1, post: "underscore.md", userId: "Madhav"}
```
### omit   _.omit(object, key)

``` javascript
const obj = {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19", updated: "2019-10-19"}
_.omit(obj, updated)  // removes the specified key from the object
// prints {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19"}
```
### clone    _.clone(obj)
``` javascript
_.clone({post: "underscore.md}) // prints {{post: "underscore.md}}
```

### has   _.has(obj, key)

``` javascript
const obj = {id: 1, post: "underscore.md", userId: "Madhav", "created": "2019-10-19", updated: "2019-10-19"}
_.has(obj, userId)  // returns boolean value as per given key
// prints  true

```

### isEmpty     _.isEmpty(obj)

``` javascript
_.isEmpty({id:1}) // returns boolean value
//prints true
```
### pairs  _.pairs(object)

``` javascript
_.pairs({id: 1, post: "underscore.md", userId: "Madhav"}) // converts object into an array
// prints [[id, 1],[post, "underscore.md"],[userId, Madhav]]
```

### keys  _.keys(object)

``` javascript
_.keys({name:"Madhav", age: 25})
// prints [name, age]
```
### values  _.values(object)

``` javascript
_.values({name:"Madhav", age: 25})
// prints [Madhav, 25]
```

### isObject(object)

``` javascript
_.isObject({}) //  prints true
```

##Array Functions

### first   _.first(array)

``` javascript
const arr = [1, 2, 3, 4, 5]
_.first(arr);
```

### indexOf    _.indexOf(array, value)

``` javascript
const arr = [1, 2, 3, 4, 5]
_.indexOf(arr, 2)  // Returns the index of the given value present in the array or returns -1 if value is not there
// prints 1(index of the value 2 in array)
```
### lastIndexOf     _.lastIndexOf(array, 2)

``` javascript
const arr = [1, 2, 3, 4, 2, 5]
_.lastIndexOf(arr, 2) // Returns the index of last occurrence of the given value or returns -1 if value is not there
// prints 4
```

### object   _.object(list, values)

``` javascript
_.object([name, age, mobile], ["Madhav", 25, "9056782792"])
//prints {name: "Madhav", age: 25, mobile: "9056782792"}
```

### range   _.range(startValue, endValue)
```javascript
_.range(10)   // Returns the list of integers from startValue
// prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_.range(1, 11)
// prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_.range([])
// prints 0
```

## Collection Functions

### each  _.each(list, method)

``` javascript
_.each([1, 2, 3, 4], alert) // display alert for four times
```

### map  _.map(list, context)

``` javascript
_.map([2, 4, 6], (num) => {num*3})
// prints [6, 12, 18]
```

### filter   

``` javascript
_.filter([2, 3, 4, 6, 8], (num) => {num % 2 == 0})
// prints [2, 4, 6, 8]

### find  

``` javascript
_.find([4, 6, 7, 8, 11], (num) => {isPrime})
// prints 7 because it prints first occurrence that passes
```

### reject  

``` javascript
var odds = _.reject([1, 2, 3, 4, 5, 6], (num)=> { num % 2 == 0 })
// prints [1, 3, 5]
```


















