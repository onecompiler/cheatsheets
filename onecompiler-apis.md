---
title: OneCompiler APIs
description: OneCompiler APIs to integrate the Editor also the APIs to run the code
created: 2021-09-08
updated: 2021-09-08
---

# Embedding Editor 

## Embedding default editor


```html
<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/" 
 width="100%"
 ></iframe>
``` 

## Embedding a specific language

```html
<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/python" 
 width="100%"
 ></iframe>
```

## Embedding a code

```html
<iframe
 frameBorder="0"
 height="450px"  
 src="https://onecompiler.com/embed/javascript/3wyne344h" 
 width="100%"
 ></iframe>
```

## Capturing the code into parent website 
Add the `codeChangeEvent=true` query param
```html
<iframe 
 frameBorder="0" 
 height="450px"
 src="https://onecompiler.com/embed/python?codeChangeEvent=true"
 width="100%"
></iframe>
```

In the parent website catch the `onmessage` events. Following is the sample code to demonstrate 

```javascript
<script>
        window.onmessage = function (e) {
            if (e.data && e.data.language) {
                console.log(e.data)
                // handle the e.data which contains the code object
            }
        };
</script>
```

## Demo
https://editor-demo.w3spaces.com/

## API to run the code 
Users can integrate the API from their backend servers and execute the code programatically. 
Following is the cURL to call the `/run` API to execure code

```sh
curl --location --request POST 'https://onecompiler.com/api/v1/run?access_token=your_access_token' \
--header 'Content-Type: application/json' \
--data-raw '{
  "language": "python",
  "stdin": "Peter",
  "files": [
    {
      "name": "HelloWorld.py",
      "content": "import sys\nname = sys.stdin.readline()\nprint('\''Hello '\''+ name)"
    }
  ]
}'
```
Note: Replace the `your_access_token` with your account's access token. Reach out to support@onecompiler.com to get your acces token





