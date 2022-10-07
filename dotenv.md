---
title: dotenv (Nodejs Library)
description: dotenv loads the environment variables from .env file to process.env
created: 2019-06-21
updated: 2019-06-21
---

dotenv loads environment variables from .env file to process.env

## Installation

```sh
npm install dotenv
```

## Usage
Add the folllowing line in the beginning of your Node application. This loads the environemnt variables from `.env` file to process.env

```javascript
require('dotenv').config()
```

## `.env` file syntax

```sh
APPLICATION_PORT=8080
```

once this is defined you can access using `process.env.APPLICATION_PORT`
