# CSS | Specificity

When more than one set of CSS rules apply to the same element, the browser will have to decide which specific set will be applied to the element. The rules the browser follows are collectively called Specificity


## Specificity Rules include:  
- CSS style applied by referencing external stylesheet has lowest precedence and is overridden by Internal and inline CSS.
- Internal CSS is overridden by inline CSS.
- Inline CSS has highest priority and overrides all other selectors.



## Example-1

```html
<html>

<head>
	<link rel="stylesheet" type="text/css" href="external.css">
	<style type="text/css">
		h1 {
			background-color: red;
			color: white;
		}
		
		h2 {
			color: blue;
		}
	</style>
</head>

<body>
	<h1>
		Internal CSS overrides external CSS
	</h1>
	<h2 style="color: green;">
		Inline CSS overrides internal CSS
	</h2>
</body>

</html>

<-----code for external.css------>
h1{
	background-color: lightgreen;
}
h2{
	color: pink;
}

```


## Output

![Output](https://github.com/Aman1143/Analog-Clock/blob/master/outPUT1.png?raw=true)


## Specificity Hierarchy

- Inline style has highest priority.
- IdentifiersID have the second highest priority.
- Classes, pseudo-classes and attributes are come next.
- Elements and pseudo-elements have lowest priority. 


## Example-2

```html
<html>

<head>
	<style type="text/css">
		h1 {
			background-color: red;
			color: white;
		}
		
		#second {
			background-color: black;
			color: white;
		}
		
		.third {
			background-color: pink;
			color: blue;
		}
		
		#second1 {
			color: blue;
		}
		
		.third1 {
			color: red;
		}
	</style>
</head>

<body>
	<h1 id="second" class="third">
		ID has highest priority.
	</h1>
	<h1>
		Element selectors has lowest priority.
	</h1>
	<h1 class="third">
		Classes have higher priority than element selectors.
	</h1>

	<h2 style="color: green;" id="second1" class="third1">
		Inline CSS has highest priority. </h2>

</body>

</html>

```
## Output
![Output](https://github.com/Aman1143/Analog-Clock/blob/master/output2.png?raw=true)
## Note

- When two or more selectors have equal specificity, the last(latest) one counts.
- Universal selectors like body and inherited selectors have least specificity.

