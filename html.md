---
title: HTML 
description: HTML Cheat Sheet gives you a quick reference of basic HTML tags, codes and attributes and is very handy while coding. 
created: 2020-06-17
updated: 2023-10-20
---

## Sample program

```html
<!-- Sample program -->
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
      <h1>Hello World! </h1>
      <p> Good Morning!! </p>
  </body>
</html>
```

* **`<!DOCTYPE html>`>** : Specifies document type, here it is an HTML5 document
* **`<html>`** : root element of an HTML page
* **`<head>`** : Contains meta information about the HTML page
* **`<title>`** : Specifies a title for the HTML page to display
* **`<body>`** : body of the html document which contains headings, paragraphs, images, hyperlinks, tables, lists, etc.
* **`<h1>`** : defines Large heading
* **`<p>`** : defines Paragraph
* **`</body>`** : represents end of body
* **`</html>`** : represents end of html
* **`<!-- comment -->`** : comments

## HTML Tags

| HTML Tags | Description| Example|
|----|----|---|
| `<h1..h6>Headers </h1..h6>`| `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>` are the heading tags, where `<h1>` is most important heading and `<h6>` is least important heading. | `<h1>MY FIRST BLOG</h1>`|
|`<div>..</div>` | `<div>` is used to wrap a block of code as a single block | `<div> Block of code </div>`|
|`<span> … </span>` | Used to inject inline elements, like an image, icon etc without disturbing the formatting of the page.| `<span> icon image </span>`|
|`<p> … </p>`| Contains plain text like a paragraph| `<p> multi line text </p>`|
|`<br/>`| line break, used to write a new line.| `<br/>`|
|`<hr/>`| Similar to line break, additionally draws a horizontal bar to indicate the end of the section | `<hr/>`|
| `<meta/>`| Used to provide meta data information like description of the web page |`<meta charset="utf-8"/>`|
| `<a>..</a>`| Used to link external webpages to your web page| `<a href="https://onecompiler.com/" target="_blank"> OneCompiler</a>`|
| `<img />`| Used to insert an image | `<img src="/sample.jpg" alt="sample image" width="100" height="50" longdesc="image" />`|
|`<pre/>`| Text in a pre elementis displayed in a fixed-width font, and it preservesboth spaces and line breaks |`<pre> int i = 0; </pre>`|
|`<audio>`| It is used to embed sound content in the document. |` <audio controls> <source src="demo.mp3" type="audio/mpeg"> </audio>`|
|`<video>`| It is used to embed video in the webpage. |` <video width="480" height="320" controls> <source src="demo_move.mp4" type="video/mp4"> </video>`|
|`<source>`| Defines multiple media resources for media elements |` <source media="(min-width:650px)" srcset="img_pink_flowers.jpg"> `|
|`<svg>`| SVG is used to define vector-based graphics for the Web|` <svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green"/> </svg> `|
|`<iframe>`| It is used to specifies an inline frame. |` <iframe src=" https://onecompiler.com/" title="iframe element"></iframe> `|
|`<progress>`| It represents the completion progress of a task. |` <progress id="file" value="32" max="100"> 32% </progress> `|
|`<address>`| It defines contact information for the author/owner of a document. |` <address> You can contact us at: 123 Somewhere St. City, State</address> `|

## HTML formatting 

|Formatting Elements|Description|
|----|----|
|`<i>..</i>`| Italic |
|`<u>..</u>`| Underline |
|`<b>..</b>`| Bold |
|`<strong>..</strong>`| Important text|
|`<em>..</em>`| Emphasized text|
|`<mark>..</mark>`| Marked text|
|`<small>..</small>`| Smaller text|
|`<del>..</del>`| Deleted text|
|`<ins>..</ins>`| Inserted text|
|`<sub>..</sub>`| Subscript text|
|`<sup>..</sup>` | Superscript text|
|`<big>..</big>` | Larger text|
|`<kbd>..</kbd>` | keyboard input text|
|`<bdo>..</bdo>` | bidirectional override text|

## Tables

`<table>` tag is used to create a table and `<tr>` tag is used to create table rows and `<td>` tag is used to create data cells.

```html
   <table border = "1">
         <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
         </tr>
         
         <tr>
           <td>Row 2, Col 1</td>
            <td>Row 2, Col 2</td>
         </tr>
         
   </table>
```
## Lists

### 1. Ordered Lists

Numbering the list items

```html
<ol type = "1"> <!-- Numeric numbering, default case-->
<ol type = "I"> <!-- Uppercase roman numerals-->
<ol type = "i"> <!-- Lowercase roman numerals-->
<ol type = "A"> <!-- Uppercase letters-->
<ol type = "a"> <!-- Lowercase letters-->
```
```html
    <ol type = "1">
        <li>list item 1</li>
        <li>list item 2</li>
        <li>list item 3</li>
    </ol>
```
### 2. Unordered Lists

List items are displayed using bullets

```html
<ul type = "disc"> <!-- default case-->
<ul type = "square">
  <ul type = "circle">
    ```
```html
<ul type= "circle">
  <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
</ul>
```
### 3. Definition Lists

List the entries like in a dictionary or encyclopedia.

* `<dl>` : Start of the definition list
* `<dt>` : Term
* `<dd>` : Term definition
* `</dl>` : End of the definition list

```html
 <dl>
   <dt><b>OL</b></dt>
    <dd>Ordered Lists</dd>
    <dt><b>UL</b></dt>
    <dd>Unordered Lists</dd>
    <dt><b>DL</b></dt>
    <dd>Definition Lists</dd>
 </dl>
```

## Forms

`<form>` element is used to define a form.

```html
<form>
  <!--form elements like input select etc-->
</form>
```

### `<input>` element

|Type |	Description|
|----|----|
|`<input type="text">` | To define a single-line text input field|
|`<input type="number">` | To define a single-line number input field |
|`<input type="password">` | To define a single-line password input field|
|`<input type="radio">`| To define a radio button |
|`<input type="submit">`| To define a submit button |
|`<input type = "checkbox">`| To define a checkbox |
| `<input type = "file">`| To define a file upload box|
| `<input type = "range">`| To define a range slider control|
| `<input type = "color">`| To define a color picker interface|
| `<input type = "reset">`| To define a reset button|
| `<input type = "email">`| To define a single-line email input field|
| `<input type = "datetime-local">`| To define a single-line Date and time input field|
| `<input type="tel">`| To define a telephone number. |
| `<input type="url">`| To define a URL address. |
| `<input type="week">`| To define a selection of week & year. |
| `<input type="image">`| To take image format as an input. |

```html
 <form >
   ID : <input type = "text" name = "user-id" /> <br> <!-- Single line text input-->
   Password: <input type = "password" name = "password" /> <br> <!-- Single line password input-->
 </form>
```

## HTML 5 Semantic Tags
> Semantic tags are used to make the code easier to write and understand for the developer as well as instructs the browser on how to treat them.

| HTML Tags | Description| Example|
|----|----|---|
| `<article></article>`| It contains independent content which doesnt require any other context. | `<article>Hey, I'm an article tag!</article>`|
|`<aside></aside>` | It is used to place content in a sidebar i.e. aside the existing content. It is related to surrounding content. | `<aside>Hey, I'm an aside tag!</aside>`|
|`<details></details>` | It defines additional details that the user can hide or view. It basically acts as an accordians space. | `<details>Code Block</details>`|
|`<summary> … </summary>`| It defines a visible heading for a “details” element. It acts as an accordian | `<details> <summary> Hi, I'm a summary tag! </summary> </details>`|
| `<header></header>`| It is for the header of a section introductory of a page. There can be multiple headers on a page. | `<header>Hi, I'm a header tag!</header>`|
| `<footer></footer>`| Located at the bottom of any article or document, they can contain contact details, copyright information etc. There can be multiple footers on a page. | `<footer>Hi, I'm a footer tag!</footer>` |
| `<main></main>`| It defines the main content of the document. | `<main>Hi, I'm a main tag!</main>` |
| `<nav></nav>`| It defines the navigation bar of the document. | `<nav>Hi, I'm a nav tag!</nav>` |

## HTML Lazy Loading

```html
<img loading="lazy" src="url-or-directory.png" alt="lazy-load-images" />
```
# Useful HTML Character Entities

|Character|Description|Name|Unicode|
|:---:|---|:---:  |:---:|
| |Blank Space|`&nbsp;`|`&#160;`|
|<|Less than|`&lt;`|`&#60;`|
|>|Greater than|`&gt;`|`&#62;`|
|&|Ampersand|`&amp;`|`&#38;`|
|"|Double quotation mark|`&quot;`|`&#34;`|	
|'|Single quotation mark|`&apos;`|`&#39;`|
|~|Tilde|`&tilde;`|-|
|%|Percent|`&percnt;`|`&#37;`|
|₹|Indian Rupee|`&#x20B9;`|`&#x20B9;`|
|$|Dollar|`&dollar;`|`&#36;`|
|¢|Cent|`&cent;`|	`&#162;`|	
|£|Pound|`&pound;`|`&#163;`|	
|¥|Yen|`&yen;`|`&#165;`|
|€|Euro|`&euro;`|`&#8364;`|
|©|Copyright|`&copy;`|`&#169;`|	
|®|Registered|`&reg;`|`&#174;`|
|™|Trademark|`&trade;`|`&#8482;`|
