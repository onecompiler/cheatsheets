---
title: Path and query params 
description: Detail description of path and query params with examples in NodeJS
created: 2020-01-04
updated: 2020-01-04
---



## Path Params:

Path params is the variable part of the URL like `/:id` where you can print the details of a class based on its id. consider the below example where you are passing the number and you are accesing it in code using req.params.

Test it by hitting the url `http://localhost:2000/square/3`.

## Query Params:

Query params is a powerful query method where you will display a page based on a query. Consider the below example where you are passing the name as foo and you access it in code using req.query.

Test it by hitting the url `http://localhost:2000/hello?name=foo`


```javascript
const express = require('express');
const server = express();

server.get('/', (req, res) => {
    res.send('Hello World');
});

// query params
server.get('/hello', (req, res) => {
    let name = req.query.name || 'NA';
    res.send(`Hello ${name}`);
});

//path params
server.get('/square/:number', (req, res) => {
    let number = parseInt( req.params.number );
    res.send(`Square is ${ number ** 2}`);
});

server.listen(2000,()=>console.log('server started on 2000'));

```
