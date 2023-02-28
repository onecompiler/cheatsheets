---
title: OneCompiler Enterprise APIs
description: OneCompiler Enterprise APIs to integrate the Editor, APIs and Challenges into external applications
created: 2022-11-01
updated: 2022-11-01
---

If you are looking for basic code execution APIs or Editor embedding check details here https://onecompiler.com/cheatsheets/onecompiler-apis

## User Creation
Following is the sample cURL request to create new user programatically 

```sh
curl --location --request POST 'https://onecompiler.com/api/v1/createUser?access_token=your_access_token' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Peter Griffin",
    "email": "peter@gmail.com"
}'
```

On successful creation you get a response like below

```json
{
    "_id": "3yhxfe7yu",
    "name": "Peter Griffin",
    "userId": "petergriffin",
    "email": "peter+your_api_id@gmail.com",
    "picture": "https://static.onecompiler.com/images/blank-profile.png",
    "thumbnail": "https://static.onecompiler.com/images/blank-profile.png",
    "hidePicture": true,
    "status": "unlisted",
    "created": "2022-10-04T11:36:27.105Z",
    "api": {
        "createdBy": "your_api_id",
        "token": "zag5vxxxxxxxxxxxxxxxxxxxxxx555"
    }
}
```

Please capture the `api.token` data and store it. You can start using this to make API calls as the above created user. 

## Signing In a user programatically
To make a user login automatically for a session. Add the following query parameters to the eligible URL (ex. Embedded challenges)

1. `apiKey`
2. `userApiToken`

Example URL: https://onecompiler.com/embed/challenges/3w7dby3mt/beginners-coding-challenge?apiKey=your_api_id&userApiToken=user_specific_token

## Pricing

|Plan Name| E1 | E2  | E3 | More/Custom |
|---|---|---|---|---|
|Price|$1,000 per month | $2,000 per month | $3,000 per month | Contact Us|
|Calls per month| 10M| 20M| 30M|  Unlimited* |
|Internet Permission| No| Yes| Yes| Yes| 
|Priority Execution| Yes| Yes| Yes| Yes| 
|Write Access| Yes| Yes| Yes| Yes| 
|Max runtime| 10s| 20s| 30s| Custom| 


> Note: Get 2 months free when you purchase yearly plans!
