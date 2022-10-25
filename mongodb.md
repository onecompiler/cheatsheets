---
title: MongoDB
description: MongoDB is a cross platform document oriented NoSQL database.
created: 2019-06-17
updated: 2019-06-17
---

### 1. About MongoDB
MongoDB is a cross platform document oriented NoSQL database. 

### 2. Installation

On Mac

```sh
brew install mongodb
```
On Ubuntu (18.04)

```sh
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```
For other platforms you can get details here https://docs.mongodb.com/manual/administration/install-community/


### 3. Mongo Shell
Mongo Shell is easiest way to experiment with MongoDB in the beginning. 
You can login to shell by running command `mongo`



### 4. Mongo Commands

* list all databases
 ```sh
 show dbs
 ```
* create/ login to a database
 ```sh
 use <database_name>
* create collection
 ```sh
 db.createCollection('<collection_name>')
 ```

### 5. Mongo Queries

Lets take an use case, using which we can go over all MongoDB commands.
Lets build a 'Car Information' application which stores all cars with its specifications.

#### Inserting documents

* #### `db.collection.insert()`

 using `insert` you can either insert one document or array of documents 
 ```json
db.cars.insert({  "name" : "Volvo xc 60",  "type" : "SUV" });
db.cars.insert(
 [
   { "name" : "Volvo xc 60",  "type" : "SUV" },
   { "name" : "Volvo xc 90",  "type" : "SUV" },
   { "name" : "Volvo   S90",  "type" : "SUV" }
 ]
);
 ```


* #### `db.collection.insertOne()`

Inserts one document 
```json
db.cars.insert({  "name" : "Volvo xc 60",  "type" : "SUV" });
```

* #### `db.collection.insertMany`

Inserts multiple documents
```json
db.cars.insertMany(
  [
    { "name" : "Volvo xc 60",  "type" : "SUV" },
  ]
);
```

* #### `db.collection.save()`

 Upsert a document. If you provide _id which is already exist then it updates the document.
 ```json
 db.cars.save( { _id: 3, "name" : "Volvo xc 60",  "type" : "SUV"} );
 ```

#### Updating documents 

* #### `db.collection.update()`
 Updates one or more than one document(s) in collection based on matching document and based on `multi` option

Syntax:
```json
db.cars.update(
 <query>,
 <update>,
 <options>
);
```

Example: 

```json
db.cars.update(
  { type: "SUV" },
  { $set: { size : 5} },
  { multi: true}
)
```

* #### `db.collection.updateOne()`
Updates a single document based on matching query

* #### `db.collection.updateMany()`
Updates multiple documents based on query
 
* #### `db.collection.replaceOne()`
Replaces entire content of document except _id field

* #### `db.collection.findOneAndUpdate(<filter>, <update>, <options>)`
Updates a single document. Following are some of the options
  `upsert` : When true inserts a document.
  `returnNewDocument`: when true returns new document instead original document. When upsert is true and returnNewDocument is false then null will be returned in case of new document insertion.

#### Reading Documents

* #### `db.collection.findOne()`
Returns one document matching the given query
```sh
db.collection.findOne({ _id : 123}); # finding a document with _id
db.collection.findOne({ type : "SUV"}); # return one SUV
```
 findOne with projection (limiting the fields to return)

```sh
db.collection.findOne({ type : "SUV"}, {name: 1}); # returns _id & name fields only
```
* #### `db.collection.find()`
Returns a cursor with selected documents
```sh
 db.collection.find({ type : "SUV"}); # returns all SUVs
```

#### Deleting Documents

* #### `db.collection.deleteOne(<filter>, <options>)`
  Deletes a Single document from collection

* #### `db.collection.deleteMany(<filter>, <options>)`
  Deletes all documents with matching filter


### 6. Read Concern
We can control the consistency and isolation properties of data reads ( from replica sets & replica set shards) using `readConcern` option

Read Concern Levels:

1. local: data returns from the instace without guaranteing that its been written to majority of replica members
  Default for reads against primary & reads against secondaries
2. available: similar to local, gives lowest latancy for sharded collections.
  Default for reads against secondaries
3. majority: only if the data acknowledged by a majority of the replica set members.
4. linearizable: return data after all successful majority-acknowledged writes
5. snapshot: Only available for transactions on multi documents.

### 7. Write Concern
Using `Write Concern` we can set the level of acknowledgment for a given write operation.
This will be sent to mongod and mongos (in case of sharded collections)

Following are the fields that specify write concern 
```json
{
 w : <number>,
 j : <boolean>,
 wtimeout: <milli seconds>
}
```

w lavlues:
0: No acknowledgement requested.
1: This requests for an acknowledgement that is propegaded to standalone mongod or primary in replica set
Note: This is the default write concern value for MongoDB
Greater than 1: Requests acknowledgement from primary & given number -1 of secondaries

j option:
This requests acknowledgement on whether or not the write operation written onto on-disk journal files

wtimeout:
Operations will return error after specified limit, this prevent the client waiting indefinitely.
On failure MongoDB does not rollback the data, data may eventually get stored


### 8. Indexes
 ##### _id Index (Default index): 
 We can't drop this index
 ##### 1. Single Field:
 ##### 2. Multikey Field:
 ##### 3. Geospatial Index:
 ##### 4. Text Indexes: 
 
### 9. Aggregations 
 ##### 1. Aggregation Pipeline
 ##### 2. Map-Reduce
 ##### 3. Single Purpose
 
#### 10. MongoDB Shell Help
```json
help
``` 