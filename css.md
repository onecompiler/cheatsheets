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

You can define CSS properties using the `<style>` tag in the `<head>` section.

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

`<link>` tag is used to refer to an external CSS file.

```html
    <link rel="stylesheet" href="styles.css" />
```

### 4. CSS Selectors

You can select elements based on their name

```css
    div {
        font-familt:'Inter',sans-serrif;
        max-width:400px;
    }
```

or you can use both class based or id based css selection. 

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

there are also more fun selectors for different use cases that could be helpful in the long run when you're having a massive project and making tons of classes won't be viable to handle, such as:

| Selector | What it does? |
|---|---|
| * | * selector selects and gives you all the elements individually, so you're essentially selecting all the elements one by one rather than having a parent controlling the styling  | 
| element1,element2 | The example of this syntax could be ```div,p{ ... }``` this allows you to select all element1 and element2 from the html  | 
| element1 element2 | Replacing the comma(,) with a space helps you in selecting all the element2 which are inside element1, for eg: ```div a{ ... }``` means all the anchor tags(a) which are inside a div | 
| element1 > element2 | Much like how the space works, it gives the all the element2 who are directly inside element1 for eg.: ```div>p{ ... }``` means all the ```<div><p> .... </p></div>``` will be selected but not ```<div><span><p></p></span></div>``` because p is not the direct child
| element1 + element2 | Quite rarely used but quite useful in some cases, it selects element2 which is directly after element1 for eg.: ```div+p{ ... }``` means all the ```<div> ... </div><p> ... </p>``` will be selected |
| element1 ~ element2 | Also quite rarely used but useful in some cases, it selects the same as the + selector but rather than what + does by selecting only a single element, it selects all the elements following |


```css 
    * {
        background:red;
        min-height:100vh;
    }
    div,p {
        background:purple;
    }
    div p {
        background:yellow;
    }
    div > p {
        background:green;
    }
    div + p {
        background:blue;
    }
    div ~ p {
        background:white;
    }
```


### 5. Display Properites

The display CSS property sets whether an element is treated as a block or inline element and the layout used for its children, such as flow layout, grid or flex.
Formally, the display property sets an element's inner and outer display types. 

```css
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
```

### 6. FlexBox

You can use Flexbox to manage alignment and position of your elements. 

To use Flexbox, give this property to the parent element:

```css
    .parent {
        display:flex;
    }
```

To align the elements towards the main axis (by default it's horizontal), we use  `justify-content`.

| Vlaues | description |
|---|---|
| flex-start | Items are packed towards the start  | 
| center | Items are packed on the center  | 
| flex-end | Items are packed towards the end  | 
| space-around | Items are equally distributed with equal space aroun them |
| space-between| Items are evenly distributed .first item at the start and last items at the end |
| space-evenly | Items are evenly spaced with same amount space between them | 

To align the elements towards the cross-axis, we use `align-items`.


| Vlaues | description |
|---|---|
| flex-start | Items are packed towards the start of cross axis  | 
| center | Items are packed on the center of cross axis  | 
| flex-end | Items are packed towards the end of the cross axis  | 

By default, the flex direction is set to row (horizontal). To switch the flex direction to column (vertical), use:

### The direction of flex is consider the main axis and the other axis consider as cross axis

```css 
    .parent {
        display:flex;
        flex-direction:column;
    }
```

### 7. CSS Grid
CSS grid is another way to properly align your HTML elements.

to create a new  grid use  

```css
    .box {
        display:grid;
    }
```

CSS grid is made of two things: columns and rows. Using `grid-template-rows` and `grid-template-columns`, you can define how many rows and columns you want.

```css 
    .box {
        display:grid;
        grid-template-columns:400px 300px 200px;
        grid-template-rows:50px 70px  60px;
    }

```

You can use grid with a special unit called `Fr (fraction)`, which refers to a portion of remaining space.

```css 
    .box {
        display:grid;
        grid-template-columns:1fr 1fr 1fr;
        // or 
        grid-template-columns: repeat(3,1fr)
    }
```

### 8. Variables

Variables are a great way to make your css more manageable, so you're not editing the values you want to be consistent on multiple instances of its usage. It promotes consistency and overall management of the code.

```css
    :root{
      --primary-color: #ffffff;
    }
    body{
      background-color: var(--primary-color);
    }
```

### 9. Animations
CSS animations allow one to animate transitions or other media files on the web page.

#### Animation-name
```css
animation-name: myanimation;
```

#### Animation-duration
```css
animation-duration: 10s;
```

#### Animation-timing-function
```css
animation-timing-function: ease;
```

### Animation-delay
```css
animation-delay: 5ms;
```

#### Animation-iteration-count
```css
animation-iteration-count: 3;
```

#### Animation-direction
```css
animation-direction: normal;
```

#### Animation-play-state
```css
animation-play-state: running;
```

#### Animation-fill-mode
```css
animation-fill-mode: both;
```

### 10. Transitions
Transitions let you define the transition between two states of an element.

#### Transition-property
```css
    transition-property: none;
```

#### Transition-duration
```css
    transition-duration: 2s;
```

#### Transition-timing-function
```css
    transition-timing-function: ease-in-out;
```

#### Transition-delay
```css
    transition-delay: 20ms;
```

