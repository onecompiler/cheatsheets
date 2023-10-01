# Setup !
Install __TS__ gobally on your machine

```bash
$ npm i -g typescript
```
# Check version .
```bash
$ tsc -V
```
---
# Create the tscofing.json file .
```
$ tsc --init
```
__Setup the the root (to compile TS files) directories in__  tsconfig.json
```
"rootDir":"./src",
"outDir" : ./public",
```
# Compiling
compile a specefic __TS__ file into as __JS__ file of hte same name, into the same directory (i.e. index.ts to index.js).
```
$ tsc index.ts
```
Tell tsc to compile specified file whenever a change is saved by adding teh watch flag (-w)
```
$ tsc index.ts -w
```
Compile specidied file into specified output file
```
$ tsc index.ts --outfileout/script.js
```
if no file is specified, tsc will compile all __TS__ files in  the "rootDir" and and output in the "outDir". Add __-w__ to watch for changes.

```
$ tsc -w
```
# Strict Mode
In tsconfig.json, is recommended to set strict  mode is No Implicit Any;
```typescript
//Error: Parameter 'a' implicitly has an 'any' type
function logName(a){
    console.log(a.name);
}

```

# Primitive Types
there 7 primitive types in **JS:** string number, bigInt, boolean, undefined, null, symbol.

**Explicit type annotation**
```typescript
let firstname: string = 'superuser'
```
# Union Types
A variable that can be assigned more than one type
```typescript
let age: number | string ;
age = 26;
age = "26";
```
# Dynamic Types 
the any type basically reverts **TS** back to **JS**

```typescript
let age: any = 100;
age = true;
```
# Literal Types
We can refer to specific strings & numbers in type positions
```typescript
let direction: 'UP' | 'DOWN';
direction = 'UP';
```

# Objects
objects in **TS** must have all the correct properties & value types
```typescript
let person:{
    name: string;
    isProgrammer: boolean;
};
person ={
    name: 'Superuser',
    isProgramer: true;
};
person.age = 26; //Error - no age prop on person object
person.isProgrammer = 'yes'; //Error - should be boolean
```
# Arrays
 We can define what kind of data an array can contain
 ```typescript
 let id: number[] = [];
 id.push(1);
 id.push("2") //Error
 ```
 # Tuples
 A tuple is special types of array with fixed size & known data types each index. They're stricter than regular arrays.
 ```typescript
 let options: [string, number];
 options = ['UP', 10];
 ```
# Functions
we can define the types of the arguments and the return. Below, **:string** could be omitted because **TS** would infer the return type.
```typescript
function circle(diameter: number) : string {
    return 'Circmf = ' + Math.PI * diameter;
}
```
***The same function as on ES arrow***
```typescript
const circle = (diameter: number): string =>
    return 'Circumference =  ' + Math.PI * diameter;
```
if we want to declare a function, but not define it, use a function signature

```typescript
let sayHi: (name: string) => void;

sayHi = (name: string) =>
console.log('Hi' + name);

sayHi('Superuser'); //Hi Superuser
```
# Type Aliases
Allow you to create a new name for an existing type. They can help to reduce code duplication. They can help to reduce code duplication. They're similar to interfaces, but can also describe primitive types.
```typescript
type StringOrNum = string | number;
let id: StringOrNum = 24;

```
# Interfaces
Interfaces are used to describe objects.
Interfaces can always be reopened & extended, unlike Type Aliases. Notices that **'name'** is **'readonly'**
```typescript
interface Person {
    name: string;
    isProgrammer: boolean;
}

let Person1: Person ={
    name:'sudo',
    isProgrammer: false,
};

person1.name = 'user'; // Error - read only
```
**Two ways to describe a function in an interface**
```typescript
interface Speech {
    sayHi(name: string):string;
    sayBye: (name: string) => string;
}
let speech: Speech = {
    sayHi: function (name: string){
        return 'Hi' + name; 
    },
    sayBye:function (name: string) => 'Bye' + name,
};

```
**Extending an interface**
```typescript
interface Animal {
    name: string;
}
interface Dog extends Animal {
    breed: string;
}
```
# The DOM & Type Casting
**TS** does't have access to the DOM, so use the non-null operator, **!** to tell **TS** the expression isn't null or undefined

```typescript
const form = document.getElementById('signup-form') as HTMLFormElement;

```
# Generics

Generics allow fo type safety in components where the arguments & return types are unknown ahead of time. 
```typescript
interface HasLength {
    length: number;
}
//logLength accepts all types with a length property
cont logLength = <T extends HasLength> (a : T) => {
    console.log(a.length)
};

// TS "captures" the type implicitly
logLength('Hello'); // 5

//Can also explicitly pass teh type to T
logLength<number[]>([1,2,3]);// 3
```
**Declare a type, T, which can change in your interface.**
```typescript
interface Dog<T> {
    breed: string;
    treats; T;
}

// We have to pass in a type arguments
let labrador: Dog<string> ={
    breed: 'labrador';
    treats: T;
}
// We have to pass in  a type argument
let labrador: Dog<string> = {
    breed: 'labrador',
    treats:['turkey','haggis']
};
```
# Enums
A set of related values, as a set of descriptive constants
```typescript
enum ResourceType {
    BOOK,
    FILE,
    FILM,
}
ResourceType.BOOK; // 0
ResourceType.FILE; // 1

```
# Narrowing
Occurs when a variables moves form a less precise type to a more precise type
```typescript
let age = getUserAge();
age // string | number

if (typeof age === 'string') {
    age; // string
}
```

