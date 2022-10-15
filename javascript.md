---
title: Javascript
description: Javascript cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2020-04-22
updated: 2020-04-22
---

## Data Types

Javascript is a dynamically typed language and hence though there are data types, variables are not bound to them.

|Data Type | Description |
|----|----|
|number| Represents numbers like integers, floating values, etc.|
|string| Represents one or more characters|
|bigint| Represents integers of arbitrary length|
|null| Represents unknown values|
|undefined| Represents undefined values|
|object| Represents complex data structures|
|boolean| Represents either true or false|

## Variables

|Keyword|Description|Scope|
|----|----|----|
|var| var is used to declare variables (old way of declaring variables) | Function or global scope|
|let| let is also used to declare variables (new way). The value of these variables can change after assignment. |Global or block Scope|
|const| const is used to declare constant values. The value of these variables cannot be changed after assignment. |Global or block Scope|

```javascript
let variable-name; // Just declaration
let variable-name = value; // declaring variable and assigning it with some value
let var1 = value1, var2 = value2, var3 = value3; // multiple variables declaration with their assigned values
```
## Basics

### On page script

```javascript
<script type="text/javascript">  ...
</script>
```
### To include external javascript file

```javascript
<script src="filename.js"></script>
```
### Comments

* Single line comments - //
* Multi line comments - /* */

### Output

```javascript
console.log("hello");       // to display message to the browser console
document.write(x);    // to write to HTML
prompt("Your name?","friend");    // input dialog. Second argument is the initial value
alert(x); // writes in an alert box
```
### Strict mode

```javascript
"use strict";  // throw errors for some of javascript silent errors and tells browser to be more strict.
```

## Conditional Statements

### If
```javascript
let age = 20; 

if (age > 18) {
  console.log('Adult');
}
```

### If-else
```javascript

let age=7;

if(age<0) {
console.log('invalid age');
} else if (age<5 && age >0) {
console.log('Infant');
} else if (age>=5 && age<=18) {
  console.log('child');
} else if (age>18) {
  console.log("Adult");
}
```

### Switch
```javascript
// what is hello in different languages
let language = "italian";
switch(language){
  case "french" :
    console.log('BONJOUR');
    break;
  
  case "spanish":
    console.log('Hola');
    break;
  
  case "hindi" :
    console.log("Namaste");
    break;
  
  default:
    console.log('Hello');
}
```


## Loops

### for

```javascript
console.log('simple for loop');
for(let i=1;i<=10;i++) {
  console.log(i);
}
```
### for..in

```javascript
let info = {
  name: "foo",
  id: 123
}

for (let x in info) {
  console.log(x); // prints keys of info which are name and id
}
```
### for..of

```javascript
let mobiles = [ "iPhone", "Samsung", "OnePlus", "Pixel"];
for(let mbl of mobiles) {  
    console.log(mbl);
} 
```
### while
```javascript
let i=1;
while(i<=10) {
  console.log(i);
  i++;
}
```
### do-while
```javascript
let i=1;
do {
  console.log(i);
  i++;
} while(i<=10);
```
## Operators

|Type|Operators|
|----|----|
|Arithmetic Operators| +  -  *  /  %  ++  --|
|Comparision Operators| ==  ===  !=  !==  >  >=  <  <=|
|Bitwise Operators| &  ^  \| ^ ~ << >> >>>|
|Logical Operators| &&  \|\| ! |
|Assignment Operators|=  +=  -=  *=  /=  %=|
|Special Operators| `? :`,  `,`, new, typeof, void, yield, delete, in, instanceof |

## Arrays

```javascript
let arrayName = [value1, value2,..etc];
// or
let arrayName = new Array("value1","value2",..etc);
```
### Array Methods

|Method name | Syntax|
|----|----|
|forEach()| arrayname.forEach(function(err, doc){ //code });|
|map()| arrayName.map(function(err, doc)){ //code });|
|filter()| arrayName.filter(function(err, doc)) { //code });|
|reduce()| arrayName.reduce(function(err, doc)) { //code });|
|find()| arrayName.find(function(err, doc)) { //code }); |
|indexOf()| arrayName.indexOf(element);|
|from()| Array.from(arrayLike[, mapFn[, thisArg]]);|
|every()| Array.every(callback(element[, index[, array]])[, thisArg])|
|some()| Array.some(callback(element[, index[, array]])[, thisArg])|
|includes()| arrayName.includes(value-to-be-checked[, starting-search-index])|

## Functions

```javascript
// declaring a function
function function-name(parameters){ // here parameters are optional
    //code
}
function-name(parameters); // calling a function
```

## Arrow function

```javascript    
(argument-list) => expression
```
### Example
```javascript    
let sum= (a,b,c) => {
    return a+b+c;
}
console.log(sum(10,20,30));
```

## Methods

### String Methods

|Method Name| Usage|
|----|----|
|search()|let sindex=str.search("sub-string");|
|slice(start,end)|let sub-str=str.slice(starting position,ending position);|
|substring(start,end|let sub-str=str.substring(starting position,ending position);|
|substr(start,length)|let sub-str=str.substr(starting position,length);|
|trim()|let str1= str.trim();|
|charAt()|let c=str.charAt(position);|
|charCodeAt()|let c=str.charCodAt(position);|
|split()|let array=str.split("");|
|length|let vln = str.length()|
|indexOf()|let index=str.indexOf("sub-string");|
|lastIndexOf()|let index=str.lastIndexOf("sub-string");|
|toUpperCase()|let str1=str.toUpperCase();|
|toLowerCase()|let str1=str.toLowerCase();|
|replace()|let x=str.replace("string to replace","replacement string")|
|concat()| let str3=str1.concat(" ",str2);|

### Number related Methods

|Method Name| Usage|
|----|----|
|Number()|Number(x);|
|parseInt()|parseInt(x);|
|parseFloat()|parseFloat(x);|
|toString()|let x = num.toString();|
|toFixed()|let x=num.toFixed(no of decimals)|
|toExponential()|let x=num.toExponential();|
|toPrecision()|let x=num.toPrecision(length)|
|valueOf()|let x= num.valueOf();|

### Date Methods

considering date = new Date() for the below methods.

|Method| Usage|comments|
|----|----|----|
|getDay()|	date.getDay()| returns day as number 0 to 6|
|Date.now()|let now = Date.now()| returns date and time
|getFullYear()| date.getFullYear();| returns yyyy i.e., 2020|
|setFullYear()| let year = date.setFullYear(2020);| sets year as 2020|
|getMonth()| date.getMonth();| returns month as a number (0-11)|
|setMonth()| let month = date.setMonth(10);| sets month as 10 means november|
|getDate()|date.getDate();| retuns date as number 1 to 31|
|setDate()|let day = date.setDate(20);|sets date as 20|
|getHours()| date.getHours();|to get the hour (0-23)|
|setHours()| let hrs = date.setHours(20);|to set the hour (0-23)|
|getMinutes()| date.getMinutes();| to get the minute (0-59)|
|setMinutes()| let min = date.setMinutes(40);|	to set the minutes (0-59)|
|getSeconds()| date.getSeconds(); | to get the second (0-59)|
|setSeconds()|	let sec = date.setSeconds(30);|to set the seconds (0-59)|
|getMilliseconds()| date.getMilliseconds();|to get the millisecond (0-999)|
|setMilliseconds()| let milli = date.setMilliseconds(500);| to	set the milliseconds (0-999)|
|setTime()| let dateTime = date.setTime(1582268856705);| to set the time (milliseconds since January 1, 1970)|
|getTime()| date.getTime()| to get the time (milliseconds since January 1, 1970)|

### Math functions

|Function| Comments|
|----|----|
|Math.PI; |returns pi value 3.141592653589793|
|Math.round(10.4);| returns 10|
|Math.round(10.5);| returns 5|
|Math.pow(2,3);| returns 8 which is 2 to the power of 3|
|Math.sqrt(100);| returns 10|
|Math.abs(-5.3);| returns 5.3|
|Math.ceil(22.12);| returns 23 by rounding up|
|Math.floor(22.92);| returns 22 by rounding down|
|Math.min(2, 5, -7, 3);| returns the lowest value which is -7|
|Math.max(2, 5, -7, 3);| returns the highest value which is 5|
|Math.log(1);| returns log value as 0|
|Math.random();| returns a random number between 0 and 1|
|Math.sin(0);| returns 0|
|Math.cos(Math.PI);| to use tan, atan, asin, acos|

## Promises

```javascript
let promise = new Promise(function(resolve, reject){
    //code
}); 
```

## Async-Await
### Syntax
```javascript
async function functioname(parameters){
	//code
}
```

### Example

```javascript
async getTodos(userObj){
	const res = await fetch([url]);
	const data = await res.json()    
	return data;
}

let data = await getTodos({fn: "foo"});
```

## Error Handling

```javascript
try {
    //code
} catch(err) {
    //code
}
```
### throw error

```javascript
throw "Error message";    // throw error text to user
```

### Regular expressions

### Syntax
```javascript
/pattern/modifiers;
```
|Modifiers|Description|
|----|----|
|g|	Performs a global match and finds all|
|i|	Performs case-insensitive matching|
|m|	Performs multiline matching|

## Javascript DOM

The Javascript DOM (Document Object Model) is an interface that allows developers to manipulate the content, structure and style of a website.The browser creates a representation of the document known as Document Object Model (DOM). This document enables Javascript to access and manipulate the HTML elements (called Nodes). 

### Node Properties
|Property Name| Usage|
|----|----|
|attributes|Returns a live collection of all attributes registered to an element|
|baseURI | Provides the absolute base URL of an HTML element|
|childNodes | Gives a collection of an element’s child nodes|
|firstChild | Returns the first child node of an element|
|lastChild | The last child node of an element|
|nextSibling | Gives you the next node at the same node tree level|
|nodeName | Returns the name of a node|
|nodeType | Returns the type of a node|
|nodeValue | Sets or returns the value of a node|
|ownerDocument | The top-level document object for this node|
|parentNode | Returns the parent node of an element|
|previousSibling | Returns the node immediately preceding the current one|
|textContent | Sets or returns the textual content of a node and its descendants|

### Node Methods
|Method Name| Usage|
|----|----|
|appendChild() | Adds a new child node to an element as the last child node|
|cloneNode() | Clones an HTML element|
|compareDocumentPosition() | Compares the document position of two elements|
|getFeature() | Returns an object which implements the APIs of a specified feature|
|hasAttributes() | Returns true if an element has any attributes, otherwise false|
|hasChildNodes() | Returns true if an element has any child nodes, otherwise false|
|insertBefore() | Inserts a new child node before a specified, existing child node|
|isDefaultNamespace() | Returns true if a specified namespaceURI is the default, otherwise false|
|isEqualNode() | Checks if two elements are equal|
|isSameNode() | Checks if two elements are the same node|
|isSupported() | Returns true if a specified feature is supported on the element|
|lookupNamespaceURI() | Returns the namespace URI associated with a given node|
|lookupPrefix() | Returns a DOMString containing the prefix for a given namespace URI if present|
|normalize() | Joins adjacent text nodes and removes empty text nodes in an element|
|removeChild() | Removes a child node from an element|
|replaceChild() | Replaces a child node in an element|

### Element Methods
|Method Name| Usage|
|----|----|
|getAttribute() | Returns the specified attribute value of an element node|
|getAttributeNS() | Returns string value of the attribute with the specified namespace and name|
|getAttributeNode() | Gets the specified attribute node|
|getAttributeNodeNS() | Returns the attribute node for the attribute with the given namespace and name|
|getElementsByTagName() | Provides a collection of all child elements with the specified tag name|
|getElementsByTagNameNS() |  Returns a live HTMLCollection of elements with a certain tag name belonging to the given namespace|
|getElementById()|Returns a single element with the specified id|
|getElementsByClassName()|Returns an array of elements with the specified class name|
|querySelector()|Returns the first element that matches a specified CSS selector|
|querySelectorAll()|Returns all elements that fit the CSS Selector|
|hasAttribute() | Returns true if an element has any attributes, otherwise false|
|hasAttributeNS() | Provides a true/false value indicating whether the current element in a given namespace has the specified attribute|
|removeAttribute() | Removes a specified attribute from an element|
|removeAttributeNS() | Removes the specified attribute from an element within a certain namespace|
|removeAttributeNode() | Takes away a specified attribute node and returns the removed node|
|setAttribute() | Sets or changes the specified attribute to a specified value|
|setAttributeNS() |  Adds a new attribute or changes the value of an attribute with the given namespace and name|
|setAttributeNode() | Sets or changes the specified attribute node|
|setAttributeNodeNS() | Adds a new namespaced attribute node to an element|

## Working with the user Browser
Besides HTML elements, JavaScript is also able to take into account the user browser and incorporate its properties into the code.

### Window Properties
|Property Name| Usage|
|----|----|
|closed | Checks whether a window has been closed or not and returns true or false|
|defaultStatus | Sets or returns the default text in the status bar of a window|
|document | Returns the document object for the window|
|frames | Returns all `<iframe`> elements in the current window|
|history | Provides the History object for the window|
|innerHeight | The inner height of a window’s content area|
|innerWidth | The inner width of the content area|
|length | Find out the number of  `<iframe>` elements in the window|
|location | Returns the location object for the window|
|name | Sets or returns the name of a window|
|navigator | Returns the Navigator object for the window|
|opener | Returns a reference to the window that created the window|
|outerHeight | The outer height of a window, including toolbars/scrollbars|
|outerWidth | The outer width of a window, including toolbars/scrollbars|
|pageXOffset | Number of pixels the current document has been scrolled horizontally|
|pageYOffset | Number of pixels the document has been scrolled vertically|
|parent | The parent window of the current window|
|screen | Returns the Screen object for the window|
|screenLeft | The horizontal coordinate of the window (relative to the screen)|
|screenTop | The vertical coordinate of the window|
|screenX | Same as screenLeft but needed for some browsers|
|screenY | Same as screenTop but needed for some browsers|
|self | Returns the current window|
|status | Sets or returns the text in the status bar of a window|
|top | Returns the topmost browser window|

### Window Methods
|Method Name| Usage|
|----|----|
|alert() | Displays an alert box with a message and an OK button|
|blur() | Removes focus from the current window|
|clearInterval() | Clears a timer set with setInterval()|
|clearTimeout() | Clears a timer set with setTimeout()|
|close() | Closes the current window|
|confirm() | Displays a dialogue box with a message and an OK and Cancel button|
|focus() | Sets focus to the current window|
|moveBy() | Moves a window relative to its current position|
|moveTo() | Moves a window to a specified position|
|open() | Opens a new browser window|
|print() | Prints the content of the current window|
|prompt() | Displays a dialogue box that prompts the visitor for input|
|resizeBy() | Resizes the window by the specified number of pixels|
|resizeTo() | Resizes the window to a specified width and height|
|scrollBy() | Scrolls the document by a specified number of pixels|
|scrollTo() | Scrolls the document to specified coordinates|
|setInterval() | Calls a function or evaluates an expression at specified intervals|
|setTimeout() | Calls a function or evaluates an expression after a specified interval|
|stop() | Stops the window from loading|

### Screen Properties
|Property Name| Usage|
|----|----|
|availHeight | Returns the height of the screen (excluding the Windows Taskbar)|
|availWidth | Returns the width of the screen (excluding the Windows Taskbar)|
|colorDepth | Returns the bit depth of the color palette for displaying images|
|height | The total height of the screen|
|pixelDepth | The color resolution of the screen in bits per pixel|
|width | The total width of the screen|


## Javascript Events
Events are things that can happen to HTML elements and are performed by the user. The programming language can listen for these events and trigger actions in the code.

### Mouse
|Event Name| Usage|
|----|----|
|onclick | The event occurs when the user clicks on an element|
|oncontextmenu | User right-clicks on an element to open a context menu|
|ondblclick | The user double-clicks on an element|
|onmousedown | User presses a mouse button over an element|
|onmouseenter | The pointer moves onto an element|
|onmouseleave | Pointer moves out of an element|
|onmousemove | The pointer is moving while it is over an element|
|onmouseover | When the pointer is moved onto an element or one of its children|
|onmouseout | User moves the mouse pointer out of an element or one of its children|
|onmouseup | The user releases a mouse button while over an element|

### Keyboard
|Event Name| Usage|
|----|----|
|onkeydown | When the user is pressing a key down|
|onkeypress | The moment the user starts pressing a key|
|onkeyup | The user releases a key|

### Frame
|Event Name| Usage|
|----|----|
|onabort | The loading of a media is aborted|
|onbeforeunload | Event occurs before the document is about to be unloaded|
|onerror | An error occurs while loading an external file|
|onhashchange | There have been changes to the anchor part of a URL|
|onload | When an object has loaded|
|onpagehide | The user navigates away from a webpage|
|onpageshow | When the user navigates to a webpage|
|onresize | The document view is resized|
|onscroll | An element’s scrollbar is being scrolled|
|onunload | Event occurs when a page has unloaded|

### Form
|Event Name| Usage|
|----|----|
|onblur | When an element loses focus|
|onchange | The content of a form element changes (for `<input>`, `<select>` and `<textarea>`)|
|onfocus | An element gets focus|
|onfocusin | When an element is about to get focus|
|onfocusout | The element is about to lose focus|
|oninput | User input on an element|
|oninvalid | An element is invalid|
|onreset | A form is reset|
|onsearch | The user writes something in a search field (for `<input="search">`)|
|onselect | The user selects some text (for `<input>` and `<textarea>`)|
|onsubmit | A form is submitted|

### Drag
|Event Name| Usage|
|----|----|
|ondrag | An element is dragged|
|ondragend | The user has finished dragging the element|
|ondragenter| The dragged element enters a drop target|
|ondragleave | A dragged element leaves the drop target|
|ondragover | The dragged element is on top of the drop target|
|ondragstart | User starts to drag an element|
|ondrop | Dragged element is dropped on the drop target|

### Clipboard
|Event Name| Usage|
|----|----|
|oncopy | User copies the content of an element|
|oncut | The user cuts an element’s content|
|onpaste | A user pastes the content in an element|

### Media
|Event Name| Usage|
|----|----|
|onabort | Media loading is aborted|
|oncanplay | The browser can start playing media (e.g. a file has buffered enough)|
|oncanplaythrough | The browser can play through media without stopping|
|ondurationchange | The duration of the media changes|
|onended | The media has reached its end|
|onerror | Happens when an error occurs while loading an external file|
|onloadeddata | Media data is loaded|
|onloadedmetadata | Metadata (like dimensions and duration) are loaded|
|onloadstart |  The browser starts looking for specified media|
|onpause | Media is paused either by the user or automatically|
|onplay | The media has been started or is no longer paused|
|onplaying | Media is playing after having been paused or stopped for buffering|
|onprogress | The browser is in the process of downloading the media|
|onratechange | The playing speed of the media changes|
|onseeked | User is finished moving/skipping to a new position in the media|
|onseeking | The user starts moving/skipping|
|onstalled | The browser is trying to load the media but it is not available|
|onsuspend | The browser is intentionally not loading media|
|ontimeupdate | The playing position has changed (e.g. because of fast forward)|
|onvolumechange | Media volume has changed (including mute)|
|onwaiting | Media paused but expected to resume (for example, buffering)|

### Animation
|Event Name| Usage|
|----|----|
|animationend | A CSS animation is complete|
|animationiteration | CSS animation is repeated|
|animationstart | CSS animation has started|

### Other
|Event Name| Usage|
|----|----|
|transitionend | Fired when a CSS transition has completed|
|onmessage | A message is received through the event source|
|onoffline | The browser starts to work offline|
|ononline | The browser starts to work online|
|onpopstate | When the window’s history changes|
|onshow | A `<menu>` element is shown as a context menu|
|onstorage | A Web Storage area is updated|
|ontoggle | The user opens or closes the `<details>` element|
|onwheel | Mouse wheel rolls up or down over an element|
|ontouchcancel | Screen-touch is interrupted|
|ontouchend | User’s finger is removed from a touch-screen|
|ontouchmove | A finger is dragged across the screen|
|ontouchstart | A finger is placed on the touch-screen|

