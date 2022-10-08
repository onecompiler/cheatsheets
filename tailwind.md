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


