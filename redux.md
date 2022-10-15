---
title: Redux
description: Redux is an open-source JavaScript library for managing and centralizing application state. It is most commonly used with libraries such as React or Angular for building user interfaces.
created: 2022-10-15
updated: 2022-10-15
---

## Installation

```sh
# NPM
npm install @reduxjs/toolkit

# Yarn
yarn add @reduxjs/toolkit
```
## Types


```javascript
type State = any // typically a primitive, a plain object with nothing complex like Dates, or an Immutable.js object

type Action = {
    type: string;
    payload?: object | any;
    error?: boolean;
}

// Async action will be transformed by middleware into an action (or series of actions)
// before being sent to the base dispatch() function
type AsyncAction = Promise | thunk | any

// Reducers must be pure functions, without API calls
// For an unrecogized action, it should return the state unmodified (to be compatible with `combineReducers`)
// If the given state is undefined, it should return an initial state that is not undefined.
type Reducer<S extends State, A extends Action> = (state: S, Action: A) => S

// Case reducers are functions intended to handle a specific action type. In Redux Toolbox, they can mutate the state rather than simply returning the new state.
type CaseReducer extends Reducer

// Synchronously sends an action to the store's reducer, along with the previous state
// returned by the store, to mutate the state. Returns the action it was passed.
type BaseDispatch = (a: Action) => Action

type Dispatch = (a: Action | AsyncAction) => any

// A store is an object that holds the application's state tree. There should only be a 
// single store in a Redux app. Instead of multiple stores, you can compose reducers.
type Store = {
    // Dispatches an action. This is the only way to trigger a state change.
    dispatch: BaseDispatch

    // Return the current state.
    getState: () => State

    // Add a change listener, which will be called every time the state changes.
    // The function returned unsubscribes the change listener.
    // Pretty low-level; you probably won't use this.
    subscribe: (listener: () => void) => () => void
    
    // Replaces the reducer used by the store. You probably won't use this.
    replaceReducer: (reducer: Reducer) => void
}

// Function that creates an action (and does not dispatch it)
type ActionCreator<A extends Action, P extends any[] = any[]> = (...args: P) => Action | AsyncAction

type Middleware = (api: { dispatch: Dispatch, getState: () => State }) => (next: Dispatch) => Dispatch

type StoreCreator = (reducer: Reducer, preloadedState: ?State) => Store

type StoreEnhancer = (next: StoreCreator) => StoreCreator

```
## Redux API

```javascript
import { createStore, combineReducers, applyMiddleware, bindActionCreators,
         compose } from 'redux'

// The reducer here should return an initial state if it is passed an undefined state.
// When a store is created, Redux dispatches a dummy action to your reducer to populate the store with the initial state.
createStore(reducer: Reducer, preloadedState?: State, enhancer?: StoreEnhancer): Store

// Combines reducers into a single reducer we can pass to `createStore`.
combineReducers(reducers: { [stateKey: string]: Reducer }): Reducer
// Example:
rootReducer = combineReducers({potato: potatoReducer, tomato: tomatoReducer})
// This would produce the following state object
{
  potato: {
    // ... potatoes, and other state managed by the potatoReducer ...
  },
  tomato: {
    // ... tomatoes, and other state managed by the tomatoReducer, maybe some nice sauce? ...
  }
}

applyMiddleware(...middlewares: Middleware[]): StoreEnhancer

// Returns a function or object of functions dispatching the given actions from the ActionCreator.
// Used if you want to pass some action creators to a component not aware of Redux.
bindActionCreators(actionCreators: ActionCreator | { [key: string]: ActionCreator },
                   dispatch: Dispatch): Function | { [key: string]: Function }

// Compose functions from left to right
compose(...functions: Function[]): Function
To make your store available to your entire application, wrap it in a <Provider> component:

const store = createStore(rootReducer)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```


**To make your store available to your entire application, wrap it in a <Provider> component:**
```javascript
const store = createStore(rootReducer)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)
```



