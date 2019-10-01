---
title: Request (Javascript Library)
description: Request is a Javascript library which are used to make rest calls to the other servers return value of the request is callback
created: 2019-09-29
updated: 2019-06-29
---
Request is a Javascript library which are used to make rest calls to the other servers return value of the request is callback.

## Usage
1 Using NPM

```sh
npm i request
```

## Hitting rest methods

#### GET
``` javascript
var request = require("request");

var options = { method: 'GET',
  url: 'https://jsonplaceholder.typicode.com/todos/1',
  headers: 
   { 'postman-token': 'a29243a0-a992-8332-a713-b22c3e244082',
     'cache-control': 'no-cache' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

#### POST

``` javascript
var request = require("request");

var options = { method: 'POST',
  url: 'https://jsonplaceholder.typicode.com/todos/1',
  headers: 
   { 'postman-token': 'a29243a0-a992-8332-a713-b22c3e244082',
     'cache-control': 'no-cache' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

## Streaming

We can stream response to a file using request
``` javascript
request('https://jsonplaceholder.typicode.com/todos/1').pipe(fs.createWriteStream('todo.txt'))
```
We can also stream a file to the PUT/POST method using request method.
```javascript
fs.createReadStream('file.json').pipe(request.put('http://mysite.com/obj.json'))
```
#### Promises and async/await

We can also return promises instead of callbacks for this we need to use interface wrapper for request. We can also use async/await using request..

