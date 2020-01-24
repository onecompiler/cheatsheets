---
title: JavaScript Fetch API
description: The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline, such as requests and responses.
created: 2018-11-05
updated: 2018-11-05
color: #f4de50
---

## get

```javascript
fetch('https://jsonplaceholder.typicode.com/todos')
      .then(res => res.json())
      .then(json => console.log(json))
```

## post formdata

```javascript
const formData = new FormData();
formData.append('name', 'foo');

fetch(`[url]`, { method: 'POST', body: formData})
        .then(res => res.text())
        .then(text => console.log(text))
```

## post application/json

```javascript
await fetch(`[url]`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify([dataObject])
    }).then(res => res.json())
      .then(json => console.log(json))
```
