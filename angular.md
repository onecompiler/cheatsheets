# Angular CLI

| Command                                     |  Meaning                                                                              |
|-----------------------------------------|--------------------------------------------------------------------------------|
|                                         |                                                                                |
| npm install -g @angular/cli             | To install the Angular CLI into our local machine using npm, run this command. |
| ng version                              | 	Displays the information about the currently installed CLI.                                                                               |
| ng new <application name>               | Using the ng new command, a new Angular application will be created.           |
| ng new <application name> --prefix best | New project is created, and the project prefix is set to new.                  |
| ng new --help                           | All available Angular commands are returned by this command.                   |
| ng lint my-app                          | Linting warnings are checked against this command in our entire application.   |
| ng lint my-app --fix                    | This command will correct any form of linting errors.                          |
| ng lint my-app --format stylish         | Our entire codebase is formatted using this command.                           |
| ng lint my-app --help                   | The list of linting commands is returned by this command.                      |
| ng build                                | An application is created and stored in the dist directory using this command. |
| ng serve                                         | The local development server is launched, and the app is served locally in the browser. Port and open are both specified. When you change any of the source files, the app is rebuilt and reloaded, and the page is changed automatically.                                                                               |
| ng serve -o                                        |  This command opens up the application in a browser using any port 4200 or any available port                                                                              |
| ng serve -ssl                                       |  This command enables the application to be accessed using SSL.                                                                              |
|  ng generate                                       | To produce elements, services, components, classes, providers, pipes, and other types of modules.                                                                               |
| ng g c MyComponent -d                                        | This dry runs the code and helps in cleaning the command line clean.                                                                                |
# Angular Lifecycle Hooks
| ngOnChanges            | The content is processed or child views are loaded before this hook is executed. It is also executed when the input properties of the component change.           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ngOnInit               | Data can be initialized in a component by calling this hook after input values are set. It is performed only once after input values are set.                     |
| ngOnDestroy            | You can use this hook to clean up memory and release resources and subscriptions after a component is destroyed.                                                  |
| ngDoCheck              | 	Any changes detected are handled using this hook.                                                                                                                |
| ngAfterContentInit     | After performing content projection into the component's view, Angular invokes this hook before evaluating the expression.                                        |
| ngAfterContentChecked	 | Angular's change detection mechanism checks the content of all components once every time they are rendered, so this hook is called each time change is detected. |
| ngAfterViewChecked     | This hook is invoked after every check of the component's views and its child views.                                                                              |
# DECORATORS
  | Class Decorators |  Details                                                                                                                                                      |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @Component({...}) class MyComponent() {}       | Metadata about a component is declared as part of the class definition.                                                                                                                                |
| @Directive({...})class MyDirective() {}        | Declares the class as a directive and provides metadata about the directive                                                                                                                            |
| @Pipe({...}) class MyPipe() {}                 | Declares the class as a pipe and provides metadata about the pipe.                                                                                                                                     |
| @Injectable() class MyService() {}             | This declares that class can be injected and provided. Without this decorator, the compiler does not generate enough metadata to allow the class to be created properly when it is injected somewhere. |
|     import { Directive, ... } from'@angular/core';                                            |    This imports the Directive from @angular/core                                                                                                                                                                                                       |
