---
title: Dotenv (Javascript Library)
description: This module is used to loads environment variables from .env file to process.env and user can access the variables through config file.
created: 2019-10-09
updated: 2019-10-10
---

This module is used to load environment variables from .env file to process.env and user can access the variables through config file.

## Install

```sh
//Using npm
$ npm install

// Using Yarn
$ yarn install
```

## Usage
``` javascript
require(.env).config
```
To use this .env file we need to create a .env file in the root directory of the project. Now user can add environment specific variables in the form of key = value.

```javascript
//.env file
ABS_REDIS_HOSTS=127.0.0.1
ABS_REDIS_PASSWORD=null
ABS_REDIS_SENTINAL=false
ABS_REDIS_SENTINAL_NAME=172.32.45.23
ABS_REDIS_CLUSTER=false
ABS_REDIS_PORT=6379
```

Now user can access these values using **process.env**.

```javascript
NODE_ENV=development
SEC_KEY=12345
port=8000
```
We can use config file to define all environment variables at one place so that if there is any changes made .env file we can easily change at one place with out changes in multiple places in the code.

``` javascript

require("dotenv").config()

export const environment = process.env.NODE_ENV || "development"
export const key = process.env.SEC_KEY 
export const port = process.env.port || 8000
```

we can use this confilg files in our project by importing it in the file.

```javascript
//.js file

import { environment, key, port } from "../config"

```










