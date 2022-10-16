---
title: tailwind css
description: Tailwind CSS works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.Helpful in making responsive .
created: 2017-11-01
updated: 2017-11-01
---

##  Install Tailwind CSS
    Install tailwindcss via npm, and create your tailwind.config.js file.

-->npm install -D tailwindcss
-->npx tailwindcss init

##  Configure your template paths
    Add the paths to all of your template files in your tailwind.config.js file.

    /** @type {import('tailwindcss').Config}*/ 
  module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
  }

##  Add the Tailwind directives to your CSS
    Add the @tailwind directives for each of Tailwind’s layers to your main CSS file.


    @tailwind base;
    @tailwind components;
    @tailwind utilities;

## Start the Tailwind CLI build process
   Run the CLI tool to scan your template files for classes and build your CSS.

   npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch


##  Start using Tailwind in your HTML
    Add your compiled CSS file to the <head> and start using Tailwind’s utility classes to style your content. 
    
      
--> example
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/dist/output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>