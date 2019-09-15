---
title: PropTypes
description: PropTypes used to typechecking the props that are passed to a React component.  
created: 2019-09-15
updated: 2019-09-15
---

PropTypes used to typechecking the props that are passed to a React component.

## Syntax

```javascript
import PropTypes from 'prop-types';

class Greetings extends React.Component {
  render() {
    return (
      <p>Hello, {this.props.name}!</p>
    );
  }
}

Greetings.propTypes = {
  name: PropTypes.string
};
```

## PropType Validators

Following code snippet shows different types of PropType Validators available. 

```javascript
import PropTypes from 'prop-types';

MyComponent.propTypes = {
  // By default all propTypes are optional.

  optionalBool: PropTypes.bool, 
  optionalNumber: PropTypes.number,
  optionalString: PropTypes.string,
  optionalSymbol: PropTypes.symbol,
  optionalArray: PropTypes.array,
  optionalObject: PropTypes.object,
  optionalFunc: PropTypes.func,


  // Anything that can be rendered: numbers, strings, elements or an array or a fragment with these type values
  optionalNode: PropTypes.node,

  // A React element
  optionalElement: PropTypes.element,

  // A React element type
  optionalElementType: PropTypes.elementType,
  
  // Enums
  optionalEnum: PropTypes.oneOf(['Red', 'Green', 'Blue']),

  // An object that could be one of many types
  optionalUnion: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number
  ]),

  // An array of a certain type, array of numbers in the following example
  optionalArrayOf: PropTypes.arrayOf(PropTypes.number),

  // An object with property values of a certain type, strings in the following case
  optionalObjectOf: PropTypes.objectOf(PropTypes.string),

  // An object taking on a particular shape
  optionalObjectWithShape: PropTypes.shape({
    name: PropTypes.string,
    age: PropTypes.number
  }),
  
  // An object with warnings on extra properties
  optionalObjectWithStrictShape: PropTypes.exact({
    name: PropTypes.string,
    age: PropTypes.number
  }),   

  // You can chain any of the above with `isRequired`, it shows warning if not provided 
  requiredFunc: PropTypes.func.isRequired,

  // A value of any data type
  requiredAny: PropTypes.any.isRequired,

  // You can also specify a custom validator. It should return an Error
  
  customProp: function(props, propName, componentName) {
    if (!props[propName].startsWith("#")) {
      return new Error(
        'Invalid color code `' + propName + '` supplied to' +
        ' `' + componentName + '`. Validation failed.'
      );
    }
  },
```
