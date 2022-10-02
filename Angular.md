# Angular CLI

| Command                                     |  Meaning                                                                              |
|-----------------------------------------|--------------------------------------------------------------------------------|
|                                         |                                                                                |
| npm install -g @angular/cli             | To install the Angular CLI into our local machine using npm, run this command. |
| ng version                              |                                                                                |
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
