---
title: NodeJS 
description: Node.js cheatsheet 
created: 2020-01-14
updated: 2020-01-14
---

## 1. How to install dependent packages

```javascript
// initialize nodejs project
npm init

//Basic syntax
npm install <package-name>

//To install the package present in git
npm install <git remote url>
/* ---------------git remote url-----------
   <protocol>://[<user>[:<password>]@]<hostname>[:<port>][:][/]<path>[#<commit-ish> | #semver:<semver>]
   ----------------------------------------
   <protocol> can be git, git+ssh, git+http, git+https, or git+file
*/

// To install a package which is in filesystem and filename must contain `.tar` or `.tar.gz` or `.tgz`.
npm install <tarball file>

```

### Arguments

`--global` or `-g` : to install the package globally
`--production` : npm will not install modules listed in devDependencies

### Examples

```javascript
npm install express
npm install git+ssh://git@github.com:npm/cli.git#v1.0.10
```

## 2.  How to execute NodeJS file

```javascript
node filename.js
```

## 3. Modules

```javascript
const express = require('express'); // to refer the installed package

const route = require('./route.js'); //to load  the module named route.js
const router = express.Router();

module.exports=router;
```

## 4. Console

```javascript
console.log('Your Message'); //prints to stdout
console.error('error message'); //prints to stderr
console.info('Your message'); //same as console.log
console.warn('warning message'); //same as console.error
```

## 5. How to connect to mongodb

```javascript
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';

let db = null;

MongoClient.connect(url, function (err, client) {
    if (err) {
        console.log('db connection error');
    }
    else
        if (!err) {
            console.log("Connected successfully to database");
            db = client.db('dbname');
        }
});
```

