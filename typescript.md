---
title: Typescript
description: tells about basic functions, variables and operations in typescript.
created: 2022-10-20
---
<br>

Basic hello world program<br>
```typescript
console.log(‘Hello World’);
```
Basic types in typescript and values compiler assumes<br>
Untyped => &nbsp; any<br>
A string => &nbsp; string<br>
A true/false value => &nbsp; boolean<br>
Explicitly empty value => &nbsp; null<br>
Uninitialised value => &nbsp; undefined

Declaring/ Using variables in typescript
```typescript
let age :  number = 10;
if (age < 50)
   age += 5;
console.log(age);
```
Literal types<br>
In Strings
```typescript
let hand: 'left' | 'right';
```
In Numeric
```typescript
let dice roll: 1 | 2 | 3 | 4 | 5 | 6;
```

Built-in types<br>
```typescript
let students: number = 123_456_321;
let course: string = ‘Typescript’;
let course : boolean = true;
```
Typescript can also define types on their own.
```typescript
let fruits = 4;
let medium = ‘English’;
```
Here, compiler understands and hence allots the type numeric to 4, and string to English.
<br><br>
Arrays in typescript
```typescript
let numbers = [1, 2, 3];
```
Array is used to store elements of same type.
Empty array is given by
```typescript
let numbers: number[]  = [];
```
Tuple in typescript
```typescript
let user: [number, string] = [1, ‘Surabhi’];
```
Tuples are greatly useful when we want to store two types of values like numeric-string, string-boolean,etc.

Typescript has a data type named Enum.
```typescript
enum Size { Small, Medium, Large};
//In this scenario compiler has assumed small to be 0.
//If we explicitly want to set values then
enum Size { Small = 1, Medium, Large}
enum Size { Small = ‘s’, Medium = ‘m’, Large= ‘l’ };
```
Pascal Code
```typescript
enum Size {Small=1, Medium, Large};
let mySize: Size = Size.Medium;
console.log(mySize);
```

<b>Functions</b>
```typescript  
  function calculateTax(income:number) : number{
if (income > 1000)
    return income * 1.2
return income*2
}
 ```
Constructors
```
new () => ConstructedType;
```

Functions with optional parameter
```typescript
function calculateTax(income: number, taxYear:number): number {
      if (taxYear < 2022)
          return income*2.2
return income*1.5
}
calculateTax( 2000, 2022);
```
We can perform operations like union and intersection in typescript.
Union
```typescript
function kgtolbs(weight: number | string) : number
```
Intersection
```typescript
let myIntersection : Engineering & Coding;
```
Utility types
```typescript
Record<'x' | 'y' | 'z', number>
```
is equivalent to
```typescript
{ x: number; y: number; z: number; }
```
Similarly
```typescript
type Excluded = Exclude<string | number, string>;
```
is equivalent to
```typescript
number
```
Similarly,
```typescript
type Extracted = Extract<string | number, string>;
```
is equivalent to
```typescript
string
```
