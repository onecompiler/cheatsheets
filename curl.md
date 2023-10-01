---
title: cURL Command
description: cURL is a cross platform command line tool which helps to make requests to server. Mainly used for making http calls but it can also do FILE, FTP, IMAP, LDAP, POP3, SCP, SFTP, SMTP, TELNET, TFTP and many more
created: 2019-06-17
updated: 2019-06-17
---

## Fetch content from a URL
```sh
curl <url>
```
Example
```sh
curl https://onecompiler.com/
```

## More Options

|Option|Description|Example|
|---|---|---|
|`-O`|To download a file|`curl -O https://static.onecompiler.com/images/logo/logo_transparent.png`|
|`-OC`|To download a file with resume capability|`curl -OC https://static.onecompiler.com/images/logo/logo_transparent.png`|
|`-L`|Follow url redirects|`curl -L https://onecompiler.com/`|
|`--max-redirs`|Maximum redirects|`curl -L --max-redirs 5 https://onecompiler.com/`|
|`-v`|Verbose mode to see request, response headers & Connection information|`curl -v https://onecompiler.com/`|
|`-H`|To ser request headers|`curl -H 'User-Agent: Robot' https://onecompiler.com/`|
|`-X`|To specify request method|`curl -X POST https://httpbin.org/post`|


## Frequently used Headers
Following are some of the commonly used headers with examples

1. User-Agent
example: 
```sh
curl -H 'User-Agent: Robot' https://onecompiler.com/
```

2. Host
example:
```sh
curl -H 'Host: onecompiler.com' https://onecompiler.com/
```

