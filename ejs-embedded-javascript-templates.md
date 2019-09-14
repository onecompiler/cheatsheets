---
title: EJS ( Embedded JavaScript templates )
description: EJS ( Embedded JavaScript templates ) is a simple templating language to generate HTML. Your code is plain Javascript in EJS, EJS itself does not introduce any new syntax. You can use EJS at client side or server side. 
created: 2018-10-24
updated: 2018-10-24
---

EJS - EJS ( Embedded JavaScript templates ) is a simple templating language to generate HTML. Your code is plain Javascript in EJS, EJS itself does not introduce any new syntax. You can use EJS at client side or server side.


#### Sample Syntax

```javascript
<% if (user.email) { %>
  <h1><%= user.email %></h1>
<% } %>
```

##### Usage - 1

```javascript
var templateString = '<h1> Hello, <%= userName %> </h1>';
var options = {};

var template = ejs.compile(templateString, options);

var data = {
    userName : 'Foo Bar'
}

var outputString = template(data); // outputString -> <h1> Hello, Foo Bar </h1>
```

##### Usage - 2

```javascript
var outputString = ejs.render(templateString, data, options);
```

##### Usage - 3 (Template as a separate file)

```javascript
ejs.renderFile(templateFilePath, data, options, function(err, outputString){
    console.log(outputString);
});
```

##### Options
| Option | Description |
|--------|--------|
|cache|To cache the compiled functions|
|filename|used by `cache` and `includes`|
|context|Function execution context|
|compileDebug|enable/ disable debug|
|rmWhitespace|removes leading and trailing whitespaces|


### Tags

| Tag | Desctiption |
|--------|--------|
|`<% `|This is a Scriptlet tag, used for control flows. This does not output anything|
|`<%_ _%>`|'Whitespace Slurping' tag, this removes all whitespaces before it.|
|`<%= %>`|Produces HTML escaped value|
|`<%- %>`|HTML unescaped value (useful if you have generated html in database )|
|`<%# %>`|Comment tag|
|`<%%`| to output literal `<%`|
|`%>`|Ending tag|
|`-%>`|Trims following new line|
|`_%>`|Remove white spaces after it|


### Includes

##### include
To include a tempate, needs a file name option, paths are relative

```javascript
<%- include('partials/navbar.ejs', data) %>
  <h1> Title <h1>
  <p> content </p>
<%- include('partials/footer.ejs', data) %>
```

### References
Official Website: https://ejs.co/

GitHub Repository: https://github.com/mde/ejs

NPM Pacjage: https://www.npmjs.com/package/ejs

