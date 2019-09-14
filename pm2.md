---
title: PM2 ( Process Manager for NodeJS )
description: PM2 is a popular NodeJS process manager that will help you run your NodeJS application in production
created: 2019-07-22
updated: 2019-07-22
---

PM2 is a popular NodeJS process manager that will help you run your NodeJS application in production

## Installation

```sh
npm install pm2 -g
```

## Starting application
You can start the application ( let's say your starting point is app.js ) using following command
```sh
pm2 start app.js
```

Following are some of the options you can use along with it

|Option|Description|
|---|---|
|--name|Specifying the app with a name, helps to look after it later|
|--watch|application will restart on file changes|

## Managing processes

#### Restarting the application
```sh
pm2 restart app_name/app_id
```

#### Stopping the application
```sh
pm2 stop app_name/app_id
```

#### Deleting the application

```sh
pm2 delete app_name/app_id
```