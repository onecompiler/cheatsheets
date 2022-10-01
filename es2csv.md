---
title: es2csv
description: es2csv is a library written in python which provides command line utility to export documents based on query from elasticsearch to csv.
created: 2019-08-19
updated: 2019-08-19
---

es2csv is a library written in python which provides command line utility to export documents based on query from elasticsearch to csv.

## Installation
```sh
pip install git+https://github.com/taraslayshchuk/es2csv.git   #install from git source
pip install es2csv                                             #install using pip
```

## Query and save results to file
```sh
es2csv -q 'company: volkswagen' -o cars.csv    #documents matching query string will be saved to cars.csv file
```

## Export required fields
```sh
es2csv -f model releaseYear mileage -q 'company: volkswagen' -o cars.csv  #only specified fields like model,releaseYear and mileage will be saved to file
```

## Authorization
```sh
es2csv -a username:password -u http://onecompiler:9001/cars/ -q 'company: volkswagen' -o cars.csv
```

## More options with examples  

| Arguments | Description  | Default Value | Example Command |
|--------|--------|--------|--------|
|-u, --url| Elasticsearch host url | `http://localhost:9200` | es2csv -u `http://onecompiler:9001/cars/` -q 'company: volkswagen' -o cars.csv |
|-i, --index-prefixes|Index name prefix| logstash-* | es2csv -i cars -q 'company: volkswagen' -o cars.csv|
|-t, --tags|Query tags, can add more than 1 tag| | es2csv -t dev -q 'company: volkswagen' -o cars.csv|
|-d, --delimiter|Provide delimiter to be used in csv file| , | es2csv -d ':' -q 'company: volkswagen' -o cars.csv|
|-m, --max|Max results to be written in file| 0 | es2csv -m 100 -q 'company: volkswagen' -o cars.csv|
|-r, --raw-query|Can write query in Query DSL format| | es2csv -r -q '{"query": {"match": {"company": "volkswagen"}}}' -o cars.csv|
|--debug|Switches debug mode on| | |
|-h, --help|Shows help message| | |
