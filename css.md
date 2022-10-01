---
title: CSS
description: Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML
created: 2022-07-02
updated: 2022-07-02
---

## CSS

### 1. Inline CSS

`style` attribute is used to define CSS properties at each HTML element.

```html
<h1 style = "color:blue; font-size:40px; font-style: italic;"> One Compiler </h1>
```

### 2. Internal CSS

You can define CSS properties using `<style>` tag in `<head>` section.

```html
<head>
    <style>
        body {background-color: pink;}
        h1   {color: red;}
        h2   {color: green; font-size : 40px; font-style: italic;}
    </style>
</head>
```

### 3. External CSS

`<link>` tag is used to refer an external CSS file.

```html
    <link rel="stylesheet" href="styles.css" />
```

### 4. CSS Selectors

you can select elements based on their name 

```css
    div {
        font-familt:'Inter',sans-serrif;
        max-width:400px;
    }
```

or you can use both class based or id base css selection 

```css
    // classed based 
    .container {
        background:red;
        height:600px;
    }
    // id based
    #container {
        background:purple;
        margin:10px;
    }
```
### 5. Display Properites

The display CSS property sets whether an element is treated as a block or inline element and the layout used for its children, such as flow layout, grid or flex.
Formally, the display property sets an element's inner and outer display types. 

```
.container {
        // various display values 
        display: block;
        display: inline;
        display: inline-block;
        display: flex;
        display: inline-flex;
        display: grid;
        display: inline-grid;
        display: flow-root;
}





### 6. FlexBox

you can use Flexbox to properly align your elements 

to use Flexbox give this property to the parent element

```css
    .parent {
        display:flex;
    }
```

to align the elements towards the main axis By default it's horizontail we use  `justify-content`

| Vlaues | description |
|---|---|
| flex-start | Items are packed towards the start  | 
| center | Items are packed on the center  | 
| flex-end | Items are packed towards the end  | 
| space-around | Items are equally distributed with equal space aroun them |
| space-between| Items are evenly distributed .first item at the start and last items at the end |
| space-evenly | Items are evenly spaced with same amount space between them | 

to align the elments towards the cross-axis we use `align-items`


| Vlaues | description |
|---|---|
| flex-start | Items are packed towards the start of cross axis  | 
| center | Items are packed on the center of cross axis  | 
| flex-end | Items are packed towards the end of the cross axis  | 

By default flex works in a horizontal way to use flex in a vartical way use

### The direction of flex is consider the main axis and the other axis consider as cross axis

```css 
    .parent {
        display:flex;
        flex-direction:column;
    }
```

### 7. CSS Grid
Css grid is another way to properly align your html elements

to create a new  grid use  

```css
    .box {
        display:grid;
    }
```

grid are made of two things columns and rows  using `grid-template-rows` and `grid-template-columns` you can define how many rows and columns you want

```css 
    .box {
        display:grid;
        grid-template-columns:400px 300px 200px;
        grid-template-rows:50px 70px  60px;
    }

```

you can use grid using a special unit called  `Fr (fraction)` which means portions of remaining space

```css 
    .box {
        display:grid;
        grid-template-columns:1fr 1fr 1fr;
        // or 
        grid-template-columns: repeat(3,1fr)
    }
```
```
#BOX PROPERTIES

    Margin-Top
    Sets the top margin of an element by specifying a length or a
    percentage.
    BODY { margin-top: 5pt; }

   Margin-Right
   Sets the right margin of an element by specifying a length or a
   percentage.
   P.narrow { margin-right: 50%; }

   Margin-Bottom
   sets the bottom margin of an element by specifying a length or
   a percentage.
   DT { margin-bottom: 3em; }

    Margin-Left
    sets the left margin of an element by specifying a length or a
   percentage.
   ADDRESS { margin-left: 50%; }

    Margin
    Sets the margins of an element by specifying top, bottom, left
    and right margins -- all either specifying length or percentage.
    BODY { margin: 5em; } /* all margins 5em */
    P { margin: 2em 4em; } /* top & bottom 2em, left & right 4em */
    DIV { margin: 1em 2em 3em 4em; }
     /* top margin 1em, right 2em, bottom 3em, left 4em */


   Padding-Top
   Describes the amount of space between the top border and
   the content of the selector.
   P { padding-top: 20%; }

   Padding-Right
   Describes the amount of space between the right border and
   the content of the selector.
   P { padding-right: 20 px; }

   Padding-Bottom
   Describes the amount of space between the bottom border
   and the content of the selector.
    P { padding-bottom: 5 em; }

  Padding-Left
  Describes the amount of space between the left border and
  the content of the selector.
  P { padding-left: 15 pt; }

   Padding
  Shorthand for the padding-top, padding-right, padding-bottom,
  and padding-left properties.
  BLOCKQUOTE { padding: 2em 4em 5em 4em; }

  Border-Top-Width
  Used to specify the width of an element's top border.
  P { border-top: 20%; }

  Border-Right-Width
  Used to specify the width of an element's right border.
  P { border-right: 20%; }

  Border-Bottom-Width
  Used to specify the width of an element's bottom border.
  P { border-bottom: 20%;}

  Border-Left-Width
  Used to specify the width of an element's left border.
  P { border-left: 20%; }

  Border-Width
  Used to set the width of an element's border (either all
  borders, or specifying top border, right border, bottom border,
  l eft border).
  P { border-width: 20%; }
  P { border-width: 10px 5px 10px 5px; }

  Border-Color
  Used to set the color of an element's border.
  P { border-color: #00000; }

  Border-Style
  Sets style of a border - none, dotted, dashed, solid, double.
   P { border-style: dotted; }

   Border-Top
   Sets the width, style, and color of an element's top border.
   P { border-top: 10px, red, double; }

   Border-Right
    Sets the width, style, and color of an element's right border.
    P { border-right: 10px, red, double; }

   Border-Bottom
   Sets the width, style, and color of an element's bottom border.
   P { border-bottom: 10px, red, double; }

  Border-Left
  Sets the width, style, and color of an element's left border.
  P { border-left: 10px, red, double; }

  Border
  Sets the width, style, and color of an element's border.
  P { border: 10px, red, double; }

  Width
  Each block-level or replaced element can be given a width,
  specified as a length, a percentage, or as auto.
  P { width: 15px; }
  H1 { width: 35%; }
. foo { width: auto; }

  Height
  Each block-level or replaced element can be given a height,
  specified as a length or as auto.
  P { height: 15px; }
  H1 { height: 35%; }
  .foo { height: auto; }

  Float
  Allows text to wrap around an element (left, right, none).
  P { float: left; }
  H1 { float: right; }
  .foo { float: none; }

  Clear
  Specifies whether an element allows floating elements to its
  sides (left, right, none).
  P { clear: left; }
 H1 { clear: right; }
. foo { clear: none; }
    
  
