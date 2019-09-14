---
title: Redis
description: Redis is an in-memory data structure store, used as a database, cache and message broker.
created: 2018-09-22
updated: 2018-09-22
---

### Hash

```sh
HSET colors white fffff
HSET colors black 000000
HSET colors blue 0000FF
HGET colors white
HDEL colors white
```

### List

```sh
LPUSH tasks task1
LPUSH tasks task2
RPUSH tasks task3
RPOP tasks # removes and get last element in list
LPOP tasks # removes and get first element in list
LRANGE tasks 5 10 # returns elements in specified range
BRPOP tasks # blocking RPOP
BLPOP tasks # blocking LPOP
LLEN tasks # list length
```

### Set

```sh
SADD colors white
SADD colors black
SADD colors black
SADD colors blue
SREM colors white
SMEMBERS myset
```

### SortedSets

```
Takes score and sort by that
```

### String

```sh
SET welcomeMessage "Hello"
APPEND welcomeMessage " World"

SET masterServer host123 EX 60 NX # EX - Set the specified expire time, in seconds
                                  # PX - Set the specified expire time, in milliseconds
                                  # NX - Only set the key if it does not already exist.
                                  # XX - Only set the key if it already exist.
```

### MISC

```sh
FLUSHALL
FLUSHDB
```

### Use Cases

* Cache layer
* Distributed Locking
* Pub/Sub
* Async communication
* Batch processing (Jobs in queues)
* session
* Redis + Elasticsearch
* Redis + Logstash
* Leaderboards ( Counting )
* Geospatial queries