---
title: crontab Linux Command
description: crontab Linux command is used to run specified tasks at regular interval of time.
created: 2019-09-10
updated: 2019-09-10
---

crontab Linux command is used to run specified tasks at regular interval of time.

# Syntax 

```sh
[cron_expression] [command]
```
```
cron_expression -> [Minute] [hour] [Day_of_the_Month] [Month_of_the_Year] [Day_of_the_Week] 
```

# Commands


```sh
crontab -l   # Lists the crontab entries for the current user
```

```sh
crontab -u <username> -l # lists crontab entries for given user
```

```sh
crontab -e # Opens crontab file for current user, where user can add more entries
```

```sh
crontab -u <username> -e # opens crontab file of specified user
```


# Examples

```sh
* * * * * ./batch_script.sh
| | | | | |_ script/ command to run at regular interval of time
| | | | |___ day of week (0 - 7) 0,7 are for sunday
| | | |_____ month of year (1 - 12)
| | |_______ day of month (1- 31)
| |_________ hour (0 - 23)
|___________ minute (0 - 59)
```

|Expression | Description|
|---|---|
| */5 * * * * |Every 5 Minutes|
| */30 * * * * |Every 30 Minutes|
| * */1 * * * |Every 1 Hour|
| * */3 * * * |Every 3 Hours|
| 0 0 * * * |Everyday at 00:00|
| 0 1 * * * | Everyday at 1AM|
| 0 0 * * SUN | Every Sunday|
| 0 0 * * 0 | Every Sunday|
| 0 0 1 * * | Every Month 1st day 00:00|
| 0 0 1 1 * | Every year 1st month 1st day 00:00|