---
title: OneCompiler APIs
description: OneCompiler APIs to integrate the Editor also the APIs to run the code
created: 2021-09-08
updated: 2021-10-12
---

# Embedding Editor 
OneCompiler's Editor can be embedded into 3rd party websites as an iFrame. 
Following are the different options available to embed the editor

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

## More options via query parameters 

| Query Parameter  | Description |
| ----------- | ----------- |
| `availableLanguages=true`| To limit the languages in the Language selection popup|
| `hideLanguageSelection=true`   | To hide the language selection button|
| `hideNew=true` |To hide the 'New' button |
| `hideStdin=true` |To hide the STDIN section |
| `hideResult=true` |To hide the Result section including STDIN |
| `hideTitle=true` |To hide the Title/Code ID|
| `listenToEvents=true`| Editor will keep listening for events like code change/ run from parent website|

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

## Changing the Editor code programatically 
The parent websites can send the code to the Editor with follwong event 

```javascript
var iFrame = document.getElementById('oc-editor'); // add an ID for the <iframe tag
 iFrame.contentWindow.postMessage({
     eventType: 'populateCode',
     language: 'python',
     files: [
      {
        "name": "HelloWorld.py",
        "content": "your code...."
      }
  ]
 }, "*");
```
Note: Make sure you have enabled `listenToEvents` flag via query parameter
## Run code in editor programatically 
The parent websites can trigger the Run code button programatically, using the following code 

```javascript
var iFrame = document.getElementById('oc-editor');
iFrame.contentWindow.postMessage({
    eventType: 'triggerRun'
}, "*");
```

Note: Make sure you have enabled `listenToEvents` flag via query parameter

## Demo
https://editor-demo.w3spaces.com/

## API to run the code 
Users can integrate the API from their backend servers and execute the code programatically. 
Following is the cURL to call the `/run` API to execute code

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
