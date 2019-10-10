---
title: Jsonata (Javascript Library)
description: Jsonata is a Javascript library which is used to querying and transforming JSON data
created: 2019-10-21
updated: 2019-06-21
---

Jsonata is a Javascript library which is used to querying and transforming JSON data

##Installation

``` sh
$ npm install jsonata
```

``` javascript
const jsonata = require('jsonata')

var orders = {
  "Account": {
    "Account Name": "Firefly",
    "Order": [
      {
        "OrderID": "order103",
        "Product": [
          {
            "Product Name": "Bowler Hat",
            "ProductID": 858383,
            "Price": 34.45,
            "Quantity": 2
          },
          {
            "Product Name": "Trilby hat",
            "ProductID": 858236,
            "Price": 21.67,
            "Quantity": 1
          }
        ]
      },
      {
        "OrderID": "order104",
        "Product": [
          {
            "Product Name": "Bowler Hat",
            "ProductID": 858383,
            "Price": 34.45,
            "Quantity": 4
          },
          {
            "ProductID": 345664,
            "Product Name": "Cloak",
            "Price": 107.99,
            "Quantity": 1
          }
        ]
      }
    ]
  }
}

var totalPrice = jsonata("$sum(Account.Order.Product.(Price*Quantity)");
console.log(totalPrice.evaluate(orders));  // prints 336.36

var totalQuantity = jsonata("Account.$sum(Order.Product.Quantity)");
console.log(totalQuantity.evaluate(orders));   // prints 8

var productDetails = jsonata("Account.Order.Product")
console.log(productDetails.evaluate(orders));  // Prints all product details

```
We can write these kind of expressions using jsonata and also querying and extracting values.
