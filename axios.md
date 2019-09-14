---
title: axios (Javascript Library)
description: Axios is promise based HTTP client for both clientside and server side
created: 2019-06-21
updated: 2019-06-21
---


Axios is promise based HTTP client for both clientside and server side

## Installation

```sh
npm install axios
```

## Example GET request

```javascript
const axios = require('axios');

axios.get('https://httpbin.org/get')
        .then(function (response) {
            // handle success
            console.log(response);
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .finally(function () {
            // always executed
        });
```

## Example GET request (using async/ await)

```javascript
const response = await axios.get('https://httpbin.org/get');
console.log(response);

```

## Example POST request
```javascript
axios.post('https://httpbin.org/post', {
            foo: "bar"
        })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
```