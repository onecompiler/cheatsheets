---
title: Request (Javascript Library)
description: Request is a Javascript library which is used to make rest/API calls to the other servers, return value of the request is a callback
created: 2019-09-29
updated: 2019-09-29
---
Request is a Javascript library which is used to make rest/API calls to the other servers, return value of the request is a callback

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
                url: 'https://jsonplaceholder.typicode.com/todos/1'
              };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```

#### POST

``` javascript
var request = require("request");

var options = { method: 'POST',
  url: 'https://jsonplaceholder.typicode.com/todos',
  headers: { 
      'content-type': 'application/json' 
  },
  body: {
    foo: 'bar'
  },
  json: true 
};

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

We can also return promises instead of callbacks, for this we need to use interface wrapper for request. We can also use async/await using request.

