---
title: Bcrpyt
description: The bcrypt hashing function allows us to build a password security platform.
created: 2021-10-15
updated: 2021-10-15
---


Bcrypt is among the most popular and safest, one-way hashing functions for passwords.

## Installation

```sh
npm install bcryptjs
```

## Usage - Sync

**To hash a password:**

```javascript
var bcrypt = require('bcryptjs');
var salt = bcrypt.genSaltSync(10);
var hash = bcrypt.hashSync("B4c0/\/", salt);
// Store hash in your password DB.
```

**To check a password:**
```javascript
// Load hash from your password DB.
bcrypt.compareSync("B4c0/\/", hash); // true
bcrypt.compareSync("not_bacon", hash); // false
```

**Auto-gen a salt and hash:**
```javascript
var hash = bcrypt.hashSync('bacon', 8);
```

## Usage - Async

**To hash a password:**
```javascript
var bcrypt = require('bcryptjs');
bcrypt.genSalt(10, function(err, salt) {
    bcrypt.hash("B4c0/\/", salt, function(err, hash) {
        // Store hash in your password DB.
    });
});
```

**To check a password:**
```javascript
// Load hash from your password DB.
bcrypt.compare("B4c0/\/", hash, function(err, res) {
    // res === true
});
bcrypt.compare("not_bacon", hash, function(err, res) {
    // res === false
});
// As of bcryptjs 2.4.0, compare returns a promise if callback is omitted:
bcrypt.compare("B4c0/\/", hash).then((res) => {
    // res === true
});
```

**Auto-gen a salt and hash:**
```javascript
bcrypt.hash('bacon', 8, function(err, hash) {
});
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
