---
title: Angular CheatSheet
description: Angular cheatsheet contains basics of angular binding & angular CLI.
created: 2022-10-03
updated: 2022-10-03
---

# Angular Cheatsheet

Here I am going to mention the some basics of the angular.

#### Angular Binding:

 - One Way Binding:
	```
	<p>title</p>
	//No changes were reflected back to the variable.
	```
- Two Way Binding
	```
	<input [(ngMo­del­)]=­"­student.F­ir­stN­ame­">
	//Changes were reflected back to the variable
	```
- Property Binding
	```
	<img [src]=­"­student.profilePicUrl">
	```
- Attribute Binding
	```
	<button [attr.a­ri­a-l­abe­l]=­"­ok">­Ok<­/bu­tto­n>
	```
- Class Binding
	```
	<div [class.Focused]="isFocused">S­ele­cte­d</­div>
	```
- ngClass
	```
	<div [ngClass]="assignClasses()">
	  <h1>{{student.FirstName}}</h1>
	</div>
	```
- Style Binding
	```
	<p [style.co­lor­]="i­sSe­lected ? 'green' : 'red'">Option {{i}}</p>
	```
 - ngStyle
	 ```
	<div [ngStyle]="setStyles()">
	  {{student.name}}
	</div>
	```

- Component Binding
	```
	<student-details [student]="currStudent"></student-details>
	```
- Directive Binding
	```
	<div [ngClass] = "­{se­lected: isSele­cte­d}">­Student<­/di­v>
	```
- Event Binding
	```
	<button (click­)="test()">­Test</­but­ton>
	```
- $event
	```
	<input [value]="student.name"
	 (input)="student.name=$event.target.value">
	 ```

#### Angular CLI commands:

- To create a *new project*
	```
	ng new project-name
	```
	
- To generate a *component*
	```
	ng g component <name>
	```

- To generate *directive*
	```
	ng g directive <name>
	```

- To generate *pipe*
	```
	ng g pipe <name>
	```

- To generate *service*
	```
	ng g service <name>
	```

- To generate *class*
	```
	ng g class <name>
	```

- To g *interface*
	```
	ng g interface <name>
	```

- *Run application* in local server
	```
	ng serve
	```
- Create a build and change environment
	```
	ng build [--e=<name>]
	```

- *Testing* your application
	```
	ng test | e2e
	```
