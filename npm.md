## What is npm?

NPM is a package manager for Node.js packages, or modules if you like.

www.npmjs.com hosts thousands of free packages to download and use.

The NPM program is installed on your computer when you install Node.js

Open-source developers use npm to share software.

Many organizations also use npm to manage private development.

### Using npm is Free
npm is free to use.

You can download all npm public software packages without any registration or logon.

### Command Line Client
npm includes a CLI (Command Line Client) that can be used to download and install software:
```
Windows Example
C:\>npm install <package>
```
```
Mac OS Example
>npm install <package>
```


### Installing npm
npm is installed with Node.js

This means that you have to install Node.js to get npm installed on your computer.

Download Node.js from the official Node.js web site: https://nodejs.org


### What is a Package?
A package in Node.js contains all the files you need for a module.

Modules are JavaScript libraries you can include in your project.

### How to Download a Package?
Downloading a package is very easy.

Open the command line interface and tell NPM to download the package you want.

I want to download a package called "upper-case":
```
Download "upper-case":
C:\Users\Your Name>npm install upper-case
```

Now you have downloaded and installed your first package!

NPM creates a folder named "node_modules", where the package will be placed. All packages you install in the future will be placed in this folder.

My project now has a folder structure like this:
```
C:\Users\My Name\node_modules\upper-case
```

### Using a Package
Once the package is installed, it is ready to use.

Include the "upper-case" package the same way you include any other module:
```
var uc = require('upper-case');
```
Create a Node.js file that will convert the output "Hello World!" into upper-case letters:
```
Example
var http = require('http');
var uc = require('upper-case');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(uc.upperCase("Hello World!"));
  res.end();
}).listen(8080);
```

### Software Package Manager
The name npm (Node Package Manager) stems from when npm first was created as a package manager for Node.js.

All npm packages are defined in files called package.json.

The content of package.json must be written in JSON.

At least two fields must be present in the definition file: name and version.
```
Example
{
"name" : "foo",
"version" : "1.2.3",
"description" : "A package for fooing things",
"main" : "foo.js",
"keywords" : ["foo", "fool", "foolish"],
"author" : "John Doe",
"licence" : "ISC"
}
```
### Managing Dependencies
npm can manage dependencies.

npm can (in one command line) install all the dependencies of a project.

Dependencies are also defined in package.json.

### Sharing Your Software
If you want to share your own software in the npm registry, you can sign in at:

https://www.npmjs.com

### Publishing a Package
You can publish any directory from your computer as long as the directory has a package.json file.

Check if npm is installed:
```
C:\>npm
```
Check if you are logged in:
```
C:\>npm whoami
```
If not, log in:
```
C:\>npm login
Username: <your username>
Password: <your password>
```
Navigate to your project and publish your project:
```
C:\Users\myuser>cd myproject
C:\Users\myuser\myproject>npm publish
```
