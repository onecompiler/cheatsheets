---
title: Dotenv (Javascript Library)
description: This module is used to loads environment variables from .env file to process.env and we can access those variables through config file.
created: 2019-10-09
updated: 2019-10-09
---

This module is used to loads environment variables from .env file to process.env and we can access those variables through config file.

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
To use this .env file we need to create a .env file in the root directory of the project. Now we can add environment specific variables in the form of key = value.

```javascript
//.env file
ABS_REDIS_HOSTS=127.0.0.1
ABS_REDIS_PASSWORD=null
ABS_REDIS_SENTINAL=false
ABS_REDIS_SENTINAL_NAME=172.32.45.23
ABS_REDIS_CLUSTER=false
ABS_REDIS_PORT=6379
```

Now we can access these values using **process.env**.

```javascript
const redisHosts = process.env.ABS_REDIS_HOSTS
const redisPassword = process.env.ABS_REDIS_PASSWORD
```
We can use config file to define all environment variables at one place so that if there is any changes made .env file we can easily change at one place with out changes in multiple places in the code.

``` javascript

require("dotenv").config()
export const authorization = "Bearer 4b9926b8-7b21-332d-a688-b490cfe3e67c"
export const currentTenantCredentials = apiCredentials
export const analyticsBaseUrl = process.env.ANALYTICS_GATEWAYURL || "https://127.0.0.1"
export const gatewayBaseUrl = process.env.GATEWAYURL || "https://127.0.0.1:8243"
export const current = process.env.DEVELOPMENT || ""
export const internalCoreUrl = process.env.INTERNAL_CORE_URL || "http://127.1.1.1:5000"
export const internalDSUrl = process.env.INTERNAL_DS_URL || "http://127.0.1.1:8080"
export const url = process.env.URL
export const absBuildType = process.env.BUILD_TYPE || "Dev"

```

we can use this confilg files in our project by importing it in the file.

```javascript
//.js file

import { authorization } from "../config"

```










