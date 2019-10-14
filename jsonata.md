---
title: Jsonata (Javascript Library)
description: Jsonata is a Javascript library which is used to querying and transforming JSON data
created: 2019-10-10
updated: 2019-10-14
---

Jsonata is a Javascript library which is used to querying and transforming JSON data

## Installation

``` sh
1. Using NPM

$ npm install jsonata
```

## Sample Usage
``` javascript
const jsonata = require('jsonata');

var empdetails = {
    "employeeDetails": {
      "companyName": "xyz", 
    "details":[{
      "name": "Sasi",
      "age": 25,
      "role": "Software Engineer",
      "salary": 500000,
      "joiningDate": "23/10/2019"
    },
    {
      "name": "Varun",
      "age": 31,
      "role": "Android Developer",
      "salary": 600000,
      "joiningDate": "30/05/2016"
    },
    {
      "name": "Krishna",
      "age": 29,
      "role": "Devops",
      "salary": 400000,
      "joiningDate": "12/09/2018"
    },
    {
      "name": "Sravani",
      "age": 23,
      "role": "Devops",
      "salary": 300000,
      "joiningDate": "23/10/2019"
    }
    ]
  }

var employeeNames = jsonata("employeeDetails.details.name");  
console.log(employees.evaluate(empdetails));  //=>  [Sasi, Varun, Krishna, Sravani]

var numberOfEmployees = jsonata("employeeDetails.$count(details)");  
console.log(numberOfEmployees.evaluate(empdetails));   //=> 4

var totalSalaryPerMonth = jsonata("employeeDetails.($sum((details.salary)))/12");
console.log(totalSalaryPerMonth.evaluate(empdetails));  //=> 150000


var roles = jsonata("employeeDetails.details.role");
console.log(roles.evaluate(empdetails));   //=> [Software Engineer, Android Developer, Devops, Devops]

var employees = jsonata("employeeDetails.details{name:{"role": role, "Salary": salary}}")
console.log(empoyees.evaluate(empDetails));  /* => {
  "Sasi": {
    "role": "Software Engineer",
    "Salary": 500000
  },
  "Varun": {
    "role": "Android Developer",
    "Salary": 600000
  },
  "Krishna": {
    "role": "Devops",
    "Salary": 400000
  },
  "Sravani": {
    "role": "Devops",
    "Salary": 300000
  }
} */


```
We can write these kind of expressions using jsonata and also query the data.
