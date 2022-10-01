---
title: Arrow Functions in Javascript
description: Arrow Function usage in Javascript
created: 2019-10-15
updated: 2019-10-23
---

Arrow functions help developers in writing more concise code, and were introduced in ES6.
Arrow functions can be written in multiple ways. Below are couple of ways to use arrow functions, although, they can be written in many other ways as well:

## 1. With no argument

### Syntax

```javascript
() => expression
```

### Example

```javascript
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

const squaresOfEvenNumbers = numbers.filter(ele => ele % 2 == 0)
                                    .map(ele => ele ** 2);

console.log(squaresOfEvenNumbers);
```

## 2. With Multiple arguments

### Syntax

```javascript    
(a1,b1,c1) => expression
```

### Example
```javascript    
let sum= (a,b,c) => {
    return a+b+c;
}
console.log(sum(10,20,30));
```

## Benefits:

1. Shorter syntax
2. Bind this lexically
3. Simplify function scoping
