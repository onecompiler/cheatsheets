---
title: Nodemon
description: Nodemon helps NodeJS applications to restart on file changes
created: 2019-08-13
updated: 2019-08-13
---

Nodemon helps NodeJS applications to restart on file changes

## Installation

```sh
npm install -g nodemon
```

## Installing as development dependency, specific to project

```sh
npm install --save-dev nodemon
```

## Starting application with nodemon
If you are doing `node index.js` to start your NodeJS application, then start doing the following to start with Nodemon
```sh
nodemon index.js
```

## Monitoring multiple directories
By default Nodemon monitors current working directory, If you want override that behaviour with your specific directories, you can do the following 
```sh
nodemon --watch server --watch docs --watch client server/index.js
```

In this case Nodemon watches `./server`, `./docs`. `./client` folders
