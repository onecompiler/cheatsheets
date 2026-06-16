---
title: Swift language 
description: Swift Programming language cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2026-06-16
---

# Swift Cheat Sheet

Swift is a modern, general-purpose, compiled programming language developed by Apple, used to build apps across all Apple platforms (iOS, macOS, watchOS, tvOS) as well as server-side and cross-platform software. It combines safety, speed, and expressive syntax, supporting object-oriented, protocol-oriented, and functional programming styles.


## Table of Contents

- [Basics](#basics)
- [Strings](#strings)
- [Collections](#collections)
- [Control Flow](#control-flow)
- [Optionals](#optionals)
- [Functions](#functions)
- [Closures](#closures)
- [Enumerations](#enumerations)
- [Structures](#structures)
- [Classes & Objects](#classes--objects)
- [Initializers](#initializers)
- [Deinitialization](#deinitialization)
- [Properties](#properties)
- [Methods](#methods)
- [Inheritance](#inheritance)
- [Protocols](#protocols)
- [Access Control](#access-control)
- [Error Handling](#error-handling)
- [Standard Library](#standard-library)
- [Useful Tips](#useful-tips)

## Basics

`let` = constant, `var` = variable. Types are inferred or annotated. Primitives: `Int`, `Double`, `Float`, `Bool`, `String`, `Character`.

```swift
let name = "Swift"          // inferred String
let pi: Double = 3.14       // explicit type
let big = 1_000_000         // underscores allowed
print("Hello, \(name)!")    // string interpolation

10 % 3                  // 1  (modulo)
5 > 3; 5 == 5; !true    // comparison / logical -> Bool
1...5                   // closed range; 1..<5 is half-open
let label = age >= 18 ? "Adult" : "Minor"   // ternary
let value = optionalName ?? "Default"        // nil-coalescing
```

## Strings

```swift
var s = "Hello"
s += ", World"            // concatenation
s.count; s.uppercased(); s.lowercased(); s.isEmpty
s.hasPrefix("Hello"); s.hasSuffix("World"); s.contains("World")
let block = """
multi-line string
"""
```

## Collections

```swift
// Array
var nums = [1, 2, 3]
nums.append(4); nums[0] = 10
nums.count; nums.first; nums.last; nums.contains(2)
nums.remove(at: 0)

// Dictionary
var marks = ["Amit": 78, "Rohit": 85]
marks["Neha"] = 88                 // add / update
marks["Amit"]                      // Optional(78)
marks.removeValue(forKey: "Rohit")
for (name, score) in marks { print(name, score) }

// Set
var unique: Set = [1, 2, 2, 3]     // {1, 2, 3}
unique.insert(4); unique.contains(2)

// Tuple
let point = (10, 20)
point.0                            // 10
let student = (name: "Swapnil", marks: 90)   // named
let (x, y) = point                 // destructuring
```

## Control Flow

```swift
if age >= 18 { print("Adult") } else { print("Minor") }

switch age {                       // must be exhaustive
case 0...12:  print("Child")
case 13...19: print("Teen")
default:      print("Adult")
}

for i in 1...3 { print(i) }
for item in nums { print(item) }

var n = 3
while n > 0 { n -= 1 }
repeat { n += 1 } while n < 3       // runs at least once
```

## Optionals

An optional holds a value or `nil`.

```swift
var name: String? = "Amit"
name = nil

if let unwrapped = name {           // optional binding
    print(unwrapped)
}

func greet(_ name: String?) {
    guard let name = name else { return }   // early exit
    print("Hello \(name)")
}

let display = name ?? "Guest"       // nil-coalescing
let length  = name?.count           // optional chaining -> Int?
```

## Functions

```swift
func greet() { print("Welcome") }                      // no params/return
func add(a: Int, b: Int) -> Int { return a + b }       // params + return
add(a: 10, b: 20)                                      // 30

// Multiple return values via tuple
func calculate(a: Int, b: Int) -> (sum: Int, product: Int) { (a + b, a * b) }
calculate(a: 5, b: 3).sum                              // 8

// Default values & argument labels
func welcome(name: String = "Guest") { print("Welcome \(name)") }
func greet(to person: String) { }   // 'to' = label, 'person' = internal name
func multiply(_ a: Int, by b: Int) -> Int { a * b }    // '_' omits the label
multiply(5, by: 3)
```

### Variadic & `inout`

`inout` lets a function modify the caller's variable (params are constants by default).

```swift
func printNumbers(_ numbers: Int...) {                 // variadic: zero or more
    for n in numbers { print(n) }
}

func swapNumbers(_ a: inout Int, _ b: inout Int) {
    let temp = a; a = b; b = temp
}
var x = 5, y = 10
swapNumbers(&x, &y)                // must pass a 'var' with &; -> 10 5
```

### Collections, nesting, recursion & overloading

```swift
func addElement(_ arr: inout [Int]) { arr.append(100) }   // modify original

func outer(number: Int) -> Int {
    func square(_ n: Int) -> Int { n * n }    // nested: visible only inside
    return square(number)
}

func factorial(_ n: Int) -> Int {
    if n == 0 { return 1 }                    // base case
    return n * factorial(n - 1)               // recursive case
}

// Overloading: same name, different params (NOT return type alone)
func area(_ side: Int) -> Int { side * side }
func area(_ radius: Double) -> Double { 3.14 * radius * radius }
```

## Closures

A closure is an anonymous block of code, passable and storable: `{ (params) -> ReturnType in code }`.

```swift
let greet  = { print("Hello Swift") }
let square = { (n: Int) -> Int in n * n }
let add    = { (a: Int, b: Int) -> Int in a + b }
square(5)    // 25
```

### As function parameters & trailing closures

```swift
func performOperation(a: Int, b: Int, operation: (Int, Int) -> Int) -> Int {
    operation(a, b)
}
performOperation(a: 5, b: 3) { x, y in x + y }   // trailing closure -> 8
performOperation(a: 6, b: 3) { $0 * $1 }         // shorthand args -> 18
```

## Enumerations

A type-safe group of related values.

```swift
enum Direction { case north, south, east, west }
var move = Direction.north
if move == .north { print("North") }

enum TrafficLight { case red, yellow, green }
switch TrafficLight.red {
case .red:    print("Stop")
case .yellow: print("Wait")
case .green:  print("Go")
}
```

### Associated values, raw values & methods

```swift
enum Result { case success(String), failure(String) }   // associated values
switch Result.success("Loaded") {
case .success(let msg): print("Success:", msg)
case .failure(let err): print("Error:", err)
}

enum WeekDay: Int { case mon = 1, tue, wed }   // raw values auto-increment
WeekDay.tue.rawValue               // 2
enum Status: String { case pending = "Pending", approved = "Approved" }

enum Calculator {                  // enums can have methods
    case add, subtract
    func calc(a: Int, b: Int) -> Int {
        switch self {
        case .add:      return a + b
        case .subtract: return a - b
        }
    }
}
Calculator.add.calc(a: 10, b: 5)   // 15
```

## Structures

A `struct` is a **value type** (copied on assignment).

```swift
struct Student {
    var name: String
    var rollNo: Int
}
var s1 = Student(name: "Swapnil", rollNo: 101)   // memberwise init
```

### Mutating, value semantics, computed & static

```swift
struct Counter {
    var count = 0
    mutating func increment() { count += 1 }     // 'mutating' to change props
}

struct Person { var name: String }
var a = Person(name: "Swapnil"); var b = a
b.name = "Amit"                    // a.name unchanged -> value copy

struct Circle {
    var radius: Double
    var area: Double { 3.14 * radius * radius }  // computed property
    static let pi = 3.14                          // type property
}
```

### Struct vs Class

| Feature       | Structure      | Class            |
| ------------- | -------------- | ---------------- |
| Type          | Value type     | Reference type   |
| Inheritance   | Not supported  | Supported        |
| Memory        | Stack          | Heap             |
| Copy behavior | Copy created   | Reference shared |
| `mutating`    | Required       | Not required     |

## Classes & Objects

A class is a blueprint; classes are **reference types**.

```swift
class Student {
    var name = ""
    var rollNo = 0
    func display() { print("\(name) - \(rollNo)") }
}
let s1 = Student()                 // object
s1.name = "Swapnil"; s1.rollNo = 101

let s2 = s1                        // s1 and s2 share the same object
s1.name = "Amit"
print(s2.name)                     // Amit
```

## Initializers

`init` sets all stored properties before use.

```swift
class Student {
    var name: String
    var rollNo: Int
    init(name: String, rollNo: Int) {
        self.name = name
        self.rollNo = rollNo
    }
}
```

### Convenience & failable

```swift
class Employee {
    var name: String; var id: Int
    init(name: String, id: Int) { self.name = name; self.id = id }
    convenience init(name: String) { self.init(name: name, id: 0) }  // calls self.init
}

class User {
    var age: Int
    init?(age: Int) {              // failable -> returns nil on bad input
        if age < 0 { return nil }
        self.age = age
    }
}
User(age: -5)                      // nil
```

## Deinitialization

`deinit` runs automatically when an instance is deallocated (ARC). Classes only, no parameters, one per class.

```swift
class FileHandler {
    var fileName = "data.txt"
    deinit { print("Closing:", fileName) }
}
var handler: FileHandler? = FileHandler()
handler = nil                      // prints "Closing: data.txt"
```

## Properties

```swift
class Demo {
    var name = ""                              // stored
    var greeting: String { "Hi \(name)" }      // computed (read-only)
    lazy var data = loadHeavy()                // lazy: init on first access
    static var version = "1.0"                 // type property
}

class Temperature {
    var celsius: Double = 0
    var fahrenheit: Double {                   // computed get/set
        get { (celsius * 9/5) + 32 }
        set { celsius = (newValue - 32) * 5/9 }
    }
}

class Marks {
    var score: Int = 0 {
        willSet { print("Will change to \(newValue)") }   // before
        didSet  { print("Changed from \(oldValue)") }     // after
    }
}
```

Property kinds: **stored** (hold data), **computed** (calculate on access), **lazy** (defer expensive init), **type/static** (shared), **observers** (`willSet`/`didSet`).

## Methods

A method is a function attached to a type. Use `self` for the current instance; overloading and default params work as in functions.

```swift
class Calculator {
    func add(a: Int, b: Int) -> Int { a + b }   // instance method
    static func info() { print("v1") }          // type method
}
Calculator().add(a: 10, b: 20)     // 30
Calculator.info()
```

## Inheritance

Swift supports **single inheritance** only (use protocols for more).

```swift
class Person {
    var name = ""
    func displayName() { print("Name:", name) }
}
class Student: Person {            // inherits name + displayName
    var rollNo = 0
}

class Vehicle { func move() { print("Vehicle moves") } }
class Bike: Vehicle {
    override func move() {
        super.move()               // call superclass version
        print("Bike moves fast")
    }
}

final class Bank { }               // 'final' prevents subclassing/overriding
```

Subclasses initialize their own properties first, then call `super.init()`.

## Protocols

A protocol defines requirements a type must implement (the *what*, not the *how*).

```swift
protocol Greetable { func greet() }
class Person: Greetable {
    func greet() { print("Hello") }
}
```

### Property requirements & multiple conformance

```swift
protocol Identifiable { var id: Int { get } }
protocol Printable    { func printData() }

class Report: Identifiable, Printable {
    var id: Int
    init(id: Int) { self.id = id }
    func printData() { print("Report #\(id)") }
}
```

### As a type, inheritance & extensions

```swift
protocol Shape { func area() }
class Square: Shape { func area() { print("side²") } }
class Circle: Shape { func area() { print("πr²") } }
let shapes: [Shape] = [Square(), Circle()]
shapes.forEach { $0.area() }

protocol Person2: Identifiable { }     // protocol inheritance

extension Printable {
    func printData() { print("Default") }   // default implementation
}
```

## Access Control

Most to least restrictive:

| Level         | Scope                                     |
| ------------- | ----------------------------------------- |
| `open`        | Anywhere; subclassable outside module     |
| `public`      | Anywhere; not subclassable outside module |
| `internal`    | Same module (default)                     |
| `fileprivate` | Same file                                 |
| `private`     | Same scope/declaration                    |

```swift
class Account {
    private var pin = 1234         // only inside this class
    func showPin() { print(pin) }
}
public class Person {              // public types need an explicit public init
    public var name: String
    public init(name: String) { self.name = name }
}
```

## Error Handling

Uses `do`–`try`–`catch`. Errors conform to `Error`.

```swift
enum LoginError: Error { case invalidUsername, invalidPassword }

func validate(user: String, pass: String) throws {
    if user != "admin" { throw LoginError.invalidUsername }
    if pass != "1234"  { throw LoginError.invalidPassword }
}

do {
    try validate(user: "admin", pass: "1111")
    print("Success")
} catch LoginError.invalidUsername {
    print("Invalid Username")
} catch {
    print("Error:", error)
}
```

### try, try?, try!

```swift
let v = try? validate(user: "x", pass: "y")   // nil on error, no do-catch
// try! validate(user: "admin", pass: "1234") // crashes if it throws
```

| Form   | Behavior                                |
| ------ | --------------------------------------- |
| `try`  | Used with `do-catch`; safe              |
| `try?` | Converts error to `nil` (optional)      |
| `try!` | Assumes success; crashes if it throws   |

### Propagation, `defer` & custom description

A function calling a throwing one must itself be `throws`. `defer` runs on scope exit (even on error).

```swift
func runLogin() throws {               // propagates the error upward
    defer { print("Cleanup") }         // always runs
    try validate(user: "admin", pass: "1111")
}

enum PaymentError: Error, CustomStringConvertible {
    case invalidCard
    var description: String { "Card details invalid" }
}
```

## Standard Library

```swift
let nums = [1, 2, 3, 4, 5]
nums.map { $0 * 2 }            // [2,4,6,8,10]
nums.filter { $0 % 2 == 0 }   // [2,4]
nums.reduce(0, +)             // 15
nums.sorted(by: >)            // [5,4,3,2,1]
nums.contains(3); nums.max(); nums.min(); nums.isEmpty

"a,b,c".split(separator: ",")        // ["a","b","c"]
["a", "b"].joined(separator: "-")     // "a-b"
Int("42")                            // Optional(42)
```

## Useful Tips

- Prefer `let` over `var`; default to **structs**, use classes for reference semantics or inheritance.
- Unwrap with `if let` / `guard let`; avoid force-unwrap (`!`). Use `guard` for early exits.
- Use trailing closures and shorthand args (`$0`, `$1`) for concise call sites.
- Mark struct methods `mutating` only when they change stored properties.
- Mark classes `final` when not meant to be subclassed (better performance).
- Prefer `do-catch` or `try?` over `try!`; favor protocol-oriented design over deep class hierarchies.
