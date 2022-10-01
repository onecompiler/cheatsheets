---
title: VueJS
description: The Progressive JavaScript Framework. An approachable, performant and versatile framework for building web user interfaces.
created: 2022-10-01
updated: 2012-10-01
---

### Installation
> Requires NPM/ Yarn for using without CDN

|Command|Description|
|---|---|
|`npm install -g @vue/cli`|Install VueJS through NPM|
|`yarn global add @vue/cli`|Install VueJS through Yarn|

### Creating A Project

|Command|Description|
|---|---|
|`vue create <project-name>`|Creates and initializes the project with chosen features|
|`vue ui`|Opens a GUI in the browser. Recommended if not comfortable with CLI|

### Vue Template Syntax
> The Vue app is broken into 3 main components

##### Template/ HTML
```html
<template>
    HTML goes Here
</template>
```
##### Javascript
```html
<script>
    Javascript related things and Vue APIs
</script>
```
##### Styling
```html
<style>
    CSS goes here
</style>
```
> Basic Example

```html
<template>
  <h1 id="heading">{{ message }}</h1>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello World!'
    }
  }
}
</script>

<style>
    #heading {
        color: pink;
    }
</style>
```

### Vue Directives 
|Directive|Functionality|
|---|---|
|`v-if`|Puts el in DOM if true|
|`v-else-if`|Usual else if condition check|
|`v-else`|Usual condition if nothing holds true|
|`v-show`|Toggles display CSS value|
|`v-html`|Sets innerHTML|
|`v-for`|Loop through an array or object|
|`v-model`|Two way data binding|
|`v-bind or :`|Reactively updates an attribute|
|`v-on or @`|Listen to DOM events|

> Basic Example

```html
<template>
    <!-- Conditionals & Event Listening -->
  <h1 v-if="awesome">Vue is awesome! {{ message }}</h1>
  <h1 v-else>Oh no 😢</h1>
  <button v-on:click="awesome = !awesome">Toggle</button>
  
  <!-- Looping -->
  <li v-for="item in items" :key="item">
    <span>{{ item }}</span>
  </li>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello World!',
      awesome: false,
      items: [1, 2, 3],
    }
  }
}
</script>

<style>
</style>
```

### Vue Lifecycle Hooks
|Hook|Description|
|---|---|
|`beforeCreate()`|The beforeCreate hook runs at the initialization of your component - data has not been made reactive, and events have not been set up yet.|
|`created()`|The created hook runs before the templates and Virtual DOM have been mounted or rendered.|
|`beforeMount()`|The beforeMount hook runs right before the initial render happens and after the template or render functions have been compiled.|
|`mounted()`|In the mounted hook, you will have full access to the reactive component, templates, and rendered DOM (via this.$el).|
|`beforeUpdate()`|The beforeUpdate hook runs after data changes on your component and the update cycle begins, right before the DOM is patched and re-rendered.|
|`updated()`|The updated hook runs after data changes on your component and the DOM re-renders.|

> For detailed info visit this [article](https://www.digitalocean.com/community/tutorials/vuejs-component-lifecycle).


### Vue Object APIs
|API|Description|
|---|---|
|`data()`|Initializes the reactive data.|
|`props`|Data visible by Parent.|
|`components`|Registers children.|
|`methods`|Set of Vue methods.|
|`computed`|Similar to methods but these are reactive & cached.|
|`watchers`|Watches for a value change.|


### Some Top Libraries\Frameworks Used With VueJS
|Name|Description|
|---|---|
|`vuex`|State Management|
|`vue-router`|Handles routing for SPAs|
|`vuetify`|Material Design component framework.|
|`axios`|Promise based HTTP client for the browser and node.js|


