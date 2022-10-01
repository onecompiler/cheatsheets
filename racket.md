---
title: Racket 
description: Racket cheatsheet gives you a quick reference to code syntax with examples makes it handy while coding.
created: 2020-07-03
updated: 2020-07-03
---

## Sample program

```racket
#lang racket/base
(print "Hello, World!")
```
* **`#lang`** : to define the language you are using
* **`print`** : To display the output in the console
* **`;`** : To comment a single line
* **`;;`** : To mark important comments
* **`#;`** : To comment the following s-expression

## Data types

| Datatype | Description|
|----|----|
|Numbers| represents integers, float and complex numbers|
|Boolean| `#t` and `#f` are the two boolean literals|
|Strings| To represent sequence of characters, double quotes("") are used to represent strings|

## Variables

Both let and define can be used to define variables.

```racket
(let ([id value-expression] ...) body ...+)

(let proc-id ([id init-expression] ...) body ...+)
```

```racket
define id expression
```

### Example

```racket
(let ([x 10]) x)
```

## Lists
```racket
(list values)
```
### Example
```racket
(list 1 2 3 4 5)
```
|List Functions|Usage|Description
|----|----|----|
|length|(length (list 1 2 3 4 5)) | returns length of the list|
|list-ref|(list-ref (list "a" "b" "c") 0) | returns list item at an index|
|append|(append (list "a" "b") (list "c")) | to append two lists|
|reverse| (reverse (list "a" "b" "c"))| to reverse a list|
|member|(member "g" (list "a" "b" "c"))| checks if an element is present in a list|

## Conditional statements

### 1. If
```racket
(if cond-expr then-expr)
```

### 2. If-else
```racket
(if cond-expr then-expr else-expr)
```

## Loops
### 1. For

```racket
(for (for-clause ...) body-or-break ... body)
```
where 

**for-clause** = [id seq-expr] | [(id ...) seq-expr] | #:when guard-expr | #:unless guard-expr | break-clause
 	 	 	 	  	 	 	 	 
**body-or-break**= body | break-clause


## Functions

```racket
(def fn functionName args body ...+)
```

### Example
```racket
#lang racket/base
(define (square y) (* y y))
(square 5)
```

## Procedures
```racket
(lambda (argument-id ...)
  body ...+)
```