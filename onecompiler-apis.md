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
| `hideNewFileOption=true` |Disables new file creation button|
| `disableCopyPaste=true` |Disables copy/paste functionality|
| `hideStdin=true` |To hide the STDIN section |
| `hideResult=true` |To hide the Result section including STDIN |
| `hideTitle=true` |To hide the Title/Code ID|
| `listenToEvents=true`| Editor will keep listening for events like code change/ run from parent website|
| `theme=dark`| For Darkmode editor|

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
https://onecompiler.github.io/editor-embed-demo/

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
### Response: 

```json
{
	"status": "success",
	"exception": null,
	"stdout": "Hello Peter\n",
	"stderr": null,
	"executionTime": 41,
	"limitPerMonthRemaining": 74694
}
```

Note: Replace the `your_access_token` with your account's access token. Reach out to support@onecompiler.com to get your acces token

Following is the pricing for APIs

|Plan Name| P1 | P2 | P3 | P4 | Enterprise |
|---|---|---|---|---|---|
|Price|$5 per month | $10 per month | $25 per month | $50 per month | Contact Us|
|Calls per month| 10,000| 30,000| 100,000| 300,000| Unlimited* |

> Note: Get 2 months free when you purchase yearly plans!

You can also purchase the APIs online here at https://rapidapi.com/onecompiler-onecompiler-default/api/onecompiler-apis/pricing

Support Details: 

Plans P1, P2, P3 & P4 comes with `Email Only` support. Enterprise plans comes with additional Zoom call support. 

Zoom call support costs $50 per hour for non Enterprise plans.
