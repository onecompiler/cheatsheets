---
title: Http Status Codes
description: Http is what protocol ussed by the modern internet, there are multiple codes returned on the basis of what comes an outcome to a http request.
created: 2022-10-05
updated: 2020-10-05
---

## Http Status Codes

Http is what protocol ussed by the modern internet, there are multiple codes returned on the basis of what comes an outcome to a http request

> Do note that the code not mentioned in the cheatsheet are not officially assigned and upto the server manager to assign for their convinence

### Http classes

| Class | Info                   |
| ----- | ---------------------- |
| 1xx   | informational response |
| 2xx   | successful             |
| 3xx   | redirection            |
| 4xx   | client error           |
| 5xx   | server error           |

#### **1xx informational response**

| Status Code | Meaning             |
| ----------- | ------------------- |
| 100         | Continue            |
| 101         | Switching Protocols |

#### **Success Responses**

| Status Code | Meaning                     |
| ----------- | --------------------------- |
| 200         | OK
| 201         | Created                     |
| 202         | Accepted                    |
| 203         | Non-Authoritive Information |
| 204         | No Content                  |
| 205         | Reset Content               |
| 206         | Partial Content             |
| 226         | IM Used                     |

#### **Redirection Responses**

| Status Code | Meaning            |
| ----------- | ------------------ |
| 300         | Multiple Choices   |
| 301         | Moved Permanently  |
| 302         | Found              |
| 303         | See Other          |
| 304         | Not Modified       |
| 305         | Use Proxy          |
| 306         | Switch Proxy       |
| 307         | Temporary Redirect |
| 308         | Permanent Redirect |

#### **Client Error Responses**

| Status Code | Meaning                         |
| ----------- | ------------------------------- |
| 400         | Bad Request                     |
| 401         | Unauthorized                    |
| 402         | Payment Required                |
| 403         | Forbidden                       |
| 404         | Not Found                       |
| 405         | Method Not Allowed              |
| 406         | Not Acceptable                  |
| 407         | Proxy Authentication Required   |
| 408         | Request Timeout                 |
| 409         | Conflict                        |
| 410         | Gone                            |
| 411         | Length Required                 |
| 412         | Precondition Failed             |
| 413         | Payload Too Large               |
| 414         | URI Too Long                    |
| 415         | Unsupported Media Type          |
| 416         | Range Not Satisfiable           |
| 417         | Expectation Failed              |
| 418         | I’m a teapot                    |
| 421         | Misdirected Request             |
| 426         | Upgrade Required                |
| 428         | Precondition Required           |
| 429         | Too Many Requests               |
| 431         | Request Header Fields Too Large |
| 451         | Unavailable For Legal Reasons   |

#### **Server Error Responses**

| Status Code | Meaning                         |
| ----------- | ------------------------------- |
| 500         | Internal Server Error           |
| 501         | Not Implemented                 |
| 502         | Bad Gateway                     |
| 503         | Service Unavailable             |
| 504         | Gateway Timeout                 |
| 505         | HTTP Version Not Supported      |
| 506         | Variant Also Negotiates         |
| 510         | Not Extended                    |
| 511         | Network Authentication Required |
