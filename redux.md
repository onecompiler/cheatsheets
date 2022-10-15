# Plugging redux in

The most straightforward way to plug in Redux:
1. Create initial state of your app
```js
// initial-state.js
const initialState = {
  user: null,
  todos: {
    active: [],
    completed: [],
  },
};

export default initialState;
```
2. Create all action types that will be modifying the state
```js
// actions.js
/**
 * Action creators - functions that will create action object
 * that will have required property `type` and optional property `payload`
 * Input argument of these functions will be the payload
 */
export const loginUser = (user) => ({
  type: 'LOGIN_USER',
  payload: user,
});

export const addTodo = (todo) => ({
  type: 'ADD_TODO',
  payload: todo,
});

export const completeTodo = (todoId) => ({
  type: 'COMPLETE_TODO',
  payload: todoId,
});
```
3. Create reducer, a function that will actually modify the state using given action
```js
// reducer.js

import initialState from './initial-state';

// Don't forget to pass initial state we've created in the first step as default parameter
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case 'LOGIN_USER':
      return {
        ...state,
        user: action.payload,
      };

    case 'ADD_TODO':
      return {
        ...state,
        todos: {
          ...state.todos,
          active: state.todos.active.concat(action.payload),
        },
      };

    case 'COMPLETE_TODO':
      const todo = state.todos.active.find((todo) => todo.id === action.payload);
      if (!todo) return state; // WE ALWAYS HAVE TO RETURN STATE!!!
      return {
        ...state,
        todos: {
          ...state.todos,
          active: state.todos.active.filter((activeTodo) => activeTodo !== todo),
          completed: state.todos.completed.concat(todo),
        },
      };
    // NEVER FORGET ABOUT DEFAULT CASE!!!
    default:
      return state;
  }
};

export default reducer;
```
4. Create a store using the reducer you've just created
```js
// store.js

import { createStore } from 'redux';
import reducer from './reducer';

const store = createStore(reducer);

export default store;
```
5. (In React) Create Provider component that will take store as the only prop
```js
// provider.js

import { Provider } from 'react-redux';
import store from './store';

const StateProvider = ({ children }) => (
  <Provider store={store}>
    { children }
  </Provider>
);

export default StateProvider;
```
6. (In React) Wrap your application with Provider component
```js
// App.js

import StateProvider from './store/provider';
import MyAppRootComponent from './components/my-app-root';

const App = () => (
  <StateProvider>
    <MyAppRootComponent />
  </StateProvider>
);

export default App;
```

# Immutable CRUD operations

## Primitives

Primitives are immutable by default, just re-assign them ;)

## Objects

Follow this order:
1. Make a clone (using destructuring operator)
2. Modify property

*To simplify reasoning, put each step on the new line*

```js
return {
  ...state, // 1. Make a clone
  user: action.payload, // 2. Modify property
};
```

## Arrays

Modifying arrays in immutable way could be achieved with **3 magic methods**:
### CREATE (Push into array): `.concat`
```js
return {
  ...state,
  books: state.books.concat(action.payload)
};
```
### UPDATE (Find and replace something in the array): `.map`
```js
return {
  ...state,
  books: state.books.map((book) => book.id === action.payload.id ? action.payload : book),
};
```
### DELETE (Find and remove from the array): `.filter`
```js
return {
  ...state,
  books: state.books.filter((book) => book.id !== action.payload),
};
```

Only three methods to remember ;)