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

**Hooks**
```javascript
// selector will be run whenever an action is dispatched. selector should be pure.
// The return value of `selector` will be used as the return value of useSelector
// When an action is dispatched, useSelector() will do a reference comparison `===` of the previous selector result value and the current result value. If they are different, the component will be forced to re-render. If they are the same, the component will not re-render.
// For shallow equality, we can import { shallowEqual } from 'react-redux'.
useSelector(selector: (state: State) => any, equalityFn: Function): any

useDispatch(): Dispatch

useStore(): Store

```

**Redux Tool Kit**
```javascript
configureStore<S = any, A extends Action = AnyAction>(options: {
    /**
    * A single reducer function that will be used as the root reducer, or an
    * object of slice reducers that will be passed to `combineReducers()`.
    */
    reducer: Reducer<S, A> | { [stateKey: string]: Reducer<S, A> },
    middlewares: Middleware[] = getDefaultMiddleware(),
    devTools: boolean = true | DevToolsOptions, // whether to enable dev tools integration
    preloadedState?: S,
    enhancers?: StoreEnhancer[] | ConfigureEnhancersCallback
}): Store<S, A> {}

getDefaultMiddleware(): Middleware[]

/**
* Each case reducer handles one specific action type.
* These reducers are allowed to mutate the state.
*/
createReducer(initialState: State,
              caseReducers: { [actionType: string]: CaseReducer } | 
                            ActionReducerMapBuilder => void
             ): Reducer
// Builder callback notation: https://redux-toolkit.js.org/api/createReducer#builder-callback-notation
// Allows for better type checking by TypeScript
type ActionReducerMapBuilder = {
    // ActionCreator created by createAction
    addCase(actionName: ActionCreator | string, reducer: CaseReducer),
    // All matching matcher reducers will execute in order, even if a case reducer has already executed
    addMatcher((action: Action) => boolean, Reducer),
    // Executes if no case reducer or matcher reducer was executed
    addDefaultCase(Reducer)
}
// Example:
createSlice({
  name: 'counter',
  initialState: 0,
  reducers: {},
  extraReducers: builder =>
    builder
      .addCase(incrementBy, (state, action) => {
        // action is inferred correctly here if using TS
      })
      // You can chain calls, or have separate `builder.addCase()` lines each time
      .addCase(decrement, (state, action) => {})
      // You can match a range of action types
      .addMatcher(
        action => action.type.endsWith('rejected'),
        (state, action) => {}
      )
      // and provide a default case if no other handlers matched
      .addDefaultCase((state, action) => {})
})

// `prepareAction` can be used to convert the parameters passed to the action creator into the payload.
createAction(actionType: string, prepareAction?: (...args) => { payload: any }): ActionCreator
// Example:
const increment = createAction('counter/increment')
let action = increment() // { type: 'counter/increment' }
action = increment(3) // returns { type: 'counter/increment', payload: 3 }
increment.toString() // 'counter/increment'

createSlice({
    // A name, used in action types
    name: string,
    // The initial state for the reducer
    initialState: any,
    // An object of "case reducers". Key names will be used to generate actions.
    reducers: {
        [actionType: string]: CaseReducer | {
            reducer: CaseReducer,
            // `prepare` converts the parameters passed to the action creator into the payload.
            prepare: (...args) => { payload: any }
        }
    }
    // An additional object of "case reducers", where the keys should be other
    // action types, or a "builder callback" function used to add more reducers
    // This does not auto-generate action types or action creators for the given reducers.
    extraReducers?: {
        [actionType: string]: CaseReducer
    } | ((builder: ActionReducerMapBuilder<State>) => void)
}): {
    name: string,
    reducer: Reducer,
    actions: Record<string, ActionCreator>,
    caseReducers: Record<string, CaseReducer>
}

createSelector

createAsyncThunk

```

**Note that in TypeScript, you can't actually set defaults for object values the way I've written it here.**


