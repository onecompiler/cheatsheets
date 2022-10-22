---
title : jQuery
description : jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.
created : 2022-10-05
updated: 2022-10-05
---

## jQuery

### Adding jQuery to Your Web Pages
There are several ways to start using jQuery on your web site. You can:

### 1. Download the jQuery library from jQuery.com

The jQuery library is a single JavaScript file, and you reference it with the HTML `<script>` tag (notice that the <script> tag should be inside the `<head>` section):
  
```html
<head>
<script src="jquery-3.6.0.min.js"></script>
</head>
 ```
Tip: Place the downloaded file in the same directory as the pages where you wish to use it.
  
### 2. Include jQuery from a CDN, like Google
  
  If you don't want to download and host jQuery yourself, you can include it from a `CDN (Content Delivery Network)`.

Google is an example of someone who host jQuery:
```html
Google CDN:
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
  ```
  
  ### jQuery Syntax
The jQuery syntax is tailor-made for selecting HTML elements and performing some action on the element(s).

 ```html
Basic syntax is: $(selector).action()
```

  <p> i)  A $ sign to define/access jQuery </p>
  <p> ii)  A (selector) to "query (or find)" HTML elements</p>
  <p>iii) A jQuery action() to be performed on the element(s)</p>
  
  ## jQuery Selectors
  jQuery selectors allow you to select and manipulate HTML element(s).
  
 ### The element Selector
The jQuery element selector selects elements based on the element name.
  You can select all <p> elements on a page like this:`$("p")`
```html
Example
$(document).ready(function(){
  $("button").click(function(){
    $("p").hide();
  });
});
  ```
  
###  The #id Selector
The jQuery #id selector uses the id attribute of an HTML tag to find the specific element.


To find an element with a specific id, write a hash character, followed by the id of the HTML element: `$("#test")`

```html
Example
$(document).ready(function(){
  $("button").click(function(){
    $("#test").hide();
  });
});
```
  ### The .class Selector
The jQuery .class selector finds elements with a specific class.

To find elements with a specific class, write a period character, followed by the name of the class:`$(".test")`
```html
Example
$(document).ready(function(){
  $("button").click(function(){
    $(".test").hide();
  });
});
```
 <br>
 More Examples of jQuery Selectors
  
| Selector | What it does? |
|---|---|
|$("*") |	Selects all elements|
|$(this) | Selects the current HTML element	|
|$("p.intro") |	Selects all <p> elements with class="intro"	|
|$("p:first")	| Selects the first <p> element |	
|$("ul li:first")	| Selects the first <li> element of the first <ul> |	
|$("ul li:first-child") |	Selects the first <li> element of every <ul> |
|$("[href]") |	Selects all elements with an href attribute	|
|$("a[target='_blank']")	| Selects all <a> elements with a target attribute value equal to "_blank" |
|$("a[target!='_blank']") |	Selects all <a> elements with a target attribute value NOT equal to "_blank"	|
|$(":button")	| Selects all <button> elements and <input> elements of type="button" |	
|$("tr:even")	| Selects all even <tr> elements |
|$("tr:odd")	| Selects all odd <tr> elements |
  
### jQuery Event Methods
 <p>What are `Events`?</p>
All the different visitors' actions that a web page can respond to are called events.
  
### jQuery Syntax For Event Methods
In jQuery, most DOM events have an equivalent jQuery method.

To assign a click event to all paragraphs on a page, you can do this:```$("p").click();```
  
The next step is to define what should happen when the event fires. You must pass a function to the event:

```
  $("p").click(function(){
  // action goes here!!
});
  ```
  <br>
  
| Event | What it does? |
|---|---|
| $(document).ready() | allows us to execute a function when the document is fully loaded |
| click() | attaches an event handler function to an HTML element.The function is executed when the user clicks on the HTML element. |
| dblclick() | attaches an event handler function to an HTML element.The function is executed when the user double-clicks on the HTML element. |
| mouseenter() | attaches an event handler function to an HTML element.The function is executed when the mouse pointer enters the HTML element. |
| mouseleave() | attaches an event handler function to an HTML element.The function is executed when the mouse pointer leaves the HTML element. |
| mousedown() | attaches an event handler function to an HTML element.The function is executed, when the left, middle or right mouse button is pressed down, while the mouse is over the HTML element. |
| mouseup() | attaches an event handler function to an HTML element.The function is executed, when the left, middle or right mouse button is released, while the mouse is over the HTML element |  
| hover() | takes two functions and is a combination of the mouseenter() and mouseleave() methods.The first function is executed when the mouse enters the HTML element, and the second function is executed when the mouse leaves the HTML element. |
| focus() |  attaches an event handler function to an HTML form field.The function is executed when the form field gets focus. |
| blur() | attaches an event handler function to an HTML form field.The function is executed when the form field loses focus. |
| The on() Method | attaches one or more event handlers for the selected elements.Attach a click event to a <p> element. |
  <br>
  
 ## jQuery - AJAX
  
### What is AJAX?
AJAX = Asynchronous JavaScript and XML.
In short; AJAX is about loading data in the background and display it on the webpage, without reloading the whole page.
Examples of applications using AJAX: Gmail, Google Maps, Youtube, and Facebook tabs.


### What About jQuery and AJAX?
jQuery provides several methods for AJAX functionality.With the jQuery AJAX methods, you can request text, HTML, XML, or JSON 
from a remote server using both HTTP Get and HTTP Post - And you can load the external data directly into the selected HTML elements of your web page.
  
<h3> jQuery load() Method</h3>
The jQuery load() method is a simple, but powerful AJAX method.

The load() method loads data from a server and puts the returned data into the selected element.
```  
Syntax:
$(selector).load(URL,data,callback);
  ```
  <h3>jQuery - AJAX get() and post() Methods</h3>
  
### jQuery $.get() Method
The $.get() method requests data from the server with an HTTP GET request.
```
Syntax:
$.get(URL,callback);
 ```

  
### jQuery $.post() Method
The $.post() method requests data from the server using an HTTP POST request.
```
Syntax:
$.post(URL,data,callback);
 ```

 
 ## jQuery Effect Methods
The following table lists all the jQuery methods for creating animation effects.

| Method	| Description |
|---|---|
|animate()	| Runs a custom animation on the selected elements |
|clearQueue()	| Removes all remaining queued functions from the selected elements |
|delay()	| Sets a delay for all queued functions on the selected elements |
|dequeue()	| Removes the next function from the queue, and then executes the function |
|fadeIn()	| Fades in the selected elements |
|fadeOut()	| Fades out the selected elements |
|fadeTo()	| Fades in/out the selected elements to a given opacity |
|fadeToggle()	| Toggles between the fadeIn() and fadeOut() methods |
|finish()	| Stops, removes and completes all queued animations for the selected elements |
|hide()	| Hides the selected elements |
|queue()	| Shows the queued functions on the selected elements |
|show()	| Shows the selected elements |
|slideDown() |	Slides-down (shows) the selected elements |
|slideToggle() |	Toggles between the slideUp() and slideDown() methods |
|slideUp() |	Slides-up (hides) the selected elements |
|stop()	| Stops the currently running animation for the selected elements |
|toggle() |	Toggles between the hide() and show() methods |
  <br>
  
## jQuery HTML / CSS Methods
The following table lists all the methods used to manipulate the HTML and CSS.

The methods below work for both `HTML` and `XML` documents. Exception: the html() method.

|Method	|Description|
|---|---|
|addClass()	| Adds one or more class names to selected elements
|after()	| Inserts content after selected elements
|append()	| Inserts content at the end of selected elements
|appendTo() |	Inserts HTML elements at the end of selected elements
|attr()	| Sets or returns attributes/values of selected elements
|before()	| Inserts content before selected elements
|clone() |	Makes a copy of selected elements
|css() |	Sets or returns one or more style properties for selected elements
|detach() |	Removes selected elements (keeps data and events)
|empty() |	Removes all child nodes and content from selected elements
|hasClass() |	Checks if any of the selected elements have a specified class name
|height() |	Sets or returns the height of selected elements
|html() |	Sets or returns the content of selected elements
|innerHeight() |	Returns the height of an element (includes padding, but not border)
|innerWidth() |	Returns the width of an element (includes padding, but not border)
|insertAfter() |	Inserts HTML elements after selected elements
|insertBefore() |	Inserts HTML elements before selected elements
|offset()	| Sets or returns the offset coordinates for selected elements (relative to the document)
|offsetParent()	| Returns the first positioned parent element
|outerHeight()	| Returns the height of an element (includes padding and border)
|outerWidth()	| Returns the width of an element (includes padding and border)
|position()	| Returns the position (relative to the parent element) of an element
|prepend()	| Inserts content at the beginning of selected elements
|prependTo()	| Inserts HTML elements at the beginning of selected elements
|prop()	| Sets or returns properties/values of selected elements
|remove()	| Removes the selected elements (including data and events)
|removeAttr()	| Removes one or more attributes from selected elements
|removeClass()	| Removes one or more classes from selected elements
|removeProp()	| Removes a property set by the prop() method
|replaceAll()	| Replaces selected elements with new HTML elements
|replaceWith()	| Replaces selected elements with new content
|scrollLeft()	| Sets or returns the horizontal scrollbar position of selected elements
|scrollTop() |	Sets or returns the vertical scrollbar position of selected elements
|text()	| Sets or returns the text content of selected elements
|toggleClass() |	Toggles between adding/removing one or more classes from selected elements
|unwrap()	| Removes the parent element of the selected elements
|val()	Sets or returns the value attribute of the selected elements (for form elements)
|width()	| Sets or returns the width of selected elements
|wrap()	| Wraps HTML element(s) around each selected element
|wrapAll() |	Wraps HTML element(s) around all selected elements
|wrapInner() |	Wraps HTML element(s) around the content of each selected element
  <br>
  
 ## jQuery Traversing
 jQuery traversing, which means "move through", are used to "find" (or select) HTML elements based on their relation to other elements. 
 Start with one selection and move through that selection until you reach the elements you desire.
  
 ### Traversing the DOM
jQuery provides a variety of methods that allow us to traverse the DOM.
The largest category of traversal methods are tree-traversal.

### jQuery Traversing Methods
|Method	| Description |
 |---|---|
|add()	| Adds elements to the set of matched elements |
|addBack()	| Adds the previous set of elements to the current set |
|andSelf()	| Deprecated in version 1.8. An alias for addBack() |
|children()	| Returns all direct children of the selected element |
|closest()	| Returns the first ancestor of the selected element |
|contents() |	Returns all direct children of the selected element (including text and comment nodes) |
|each()	| Executes a function for each matched element |
|end()	| Ends the most recent filtering operation in the current chain, and return the set of matched elements to its previous state|
|eq()	| Returns an element with a specific index number of the selected elements |
|filter()	| Reduce the set of matched elements to those that match the selector or pass the function's test |
|find()	| Returns descendant elements of the selected element |
|first() |	Returns the first element of the selected elements |
|has() |	Returns all elements that have one or more elements inside of them |
|is()	| Checks the set of matched elements against a selector/element/jQuery object, and return true if at least one of these elements matches the given arguments |
|last()	| Returns the last element of the selected elements |
|map()	| Passes each element in the matched set through a function, producing a new jQuery object containing the return values |
|next()	 | Returns the next sibling element of the selected element |
|nextAll() |	Returns all next sibling elements of the selected element |
|nextUntil() |	Returns all next sibling elements between two given arguments |
|not() | Returns elements that do not match a certain criteria |
|offsetParent()	| Returns the first positioned parent element |
|parent()	| Returns the direct parent element of the selected element |
|parents()	| Returns all ancestor elements of the selected element |
|parentsUntil() |	Returns all ancestor elements between two given arguments |
|prev()	| Returns the previous sibling element of the selected element |
|prevAll()	| Returns all previous sibling elements of the selected element |
|prevUntil()	| Returns all previous sibling elements between two given arguments |
|siblings() |	Returns all sibling elements of the selected element |
|slice() |	Reduces the set of matched elements to a subset specified by a range of indices |
  
