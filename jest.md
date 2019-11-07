---
title: jest (Javascript Library)
description: Jest is a javascript library which privides utility functions to write unit tests
created: 2019-11-07
updated: 2019-11-07
---

Jest is a javascript library which privides utility functions to write unit tests.
Jest also consists of testrunner which is used to generate a test report by running program in command line.

## Installation

1. Using NPM

```sh
npm install jest --save--dev
```
 Note: Install jest as dev dependency

## Popular jest matcher functions

## Equality

|Matcher_function|Description|
|---|---|
|`expect(...).toBe();`|Check for the equality of data|
|`expect(...).toEqual()`|Check for the equality of data|

## Truthiness
|Matcher_function|Description|
|---|---|
|`expect(...).toBeDefined();`|To check whether a function returning data or not|
|`expect(...).toBeNull();`|Check whether something is null|
|`expect(...).toBeTruthy();`|Check whether it returns true|
|`expect(...).toBeFalsy();`|Check whether it returns false|

## Numbers 
|Matcher_function|Description|
|---|---|
|`expect(...).toBeGreaterThan();`|Checks whether number is greater or not |
|`expect(...).toBeGreaterThanOrEqual();`|Checks whether number is greater or equal|
|`expect(...).toBeLessThan()`| Checks whether number is smaller or not |
|`expect(...).toBeLessThanOrEqual()`|Checks whether number is smaller or equal|


## Strings
|Matcher_function|Description|
|---|---|
|`expect(...).toMatch(/regularExp/);`||



## Arrays
|Matcher_function|Description|
|---|---|
|`expect(...).toContain();`|Checks whether element is present in array or not|


## Objects
|Matcher_function|Description|
|---|---|
|`expect(...).toBe();`|Check for the equality of object|
|`expect(...).toEqual()`|Check for the equality of object|
|`expect(...).toMatchObject()`|Check for the equality of object|

## Exceptions
|Matcher_function|Description|
|---|---|
|`expect(() => { someCode }).toThrow();`|Check for the equality of exceptions|
