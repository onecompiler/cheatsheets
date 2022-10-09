---
title: SWR (Javascript Library)
description: React Hooks for Data Fetching
created: 2022-10-09
updated: 2022-10-09
---


SWR is a strategy to first return the data from cache (stale), then send the fetch request (revalidate), and finally come with the up-to-date data.

## Installation

```sh
npm install swr
```

or with yarn

```sh
yarn add swr
```

For normal RESTful APIs with JSON data, first you need to create a fetcher function, which is just a wrapper of the native fetch:

```javascript
const fetcher = (...args) => fetch(...args).then(res => res.json())
```

Then you can import useSWR and start using it inside any function components:

```javascript
import useSWR from 'swr'

function Profile () {
  const { data, error } = useSWR('/api/user/123', fetcher)

  if (error) return <div>failed to load</div>
  if (!data) return <div>loading...</div>

  // render data
  return <div>hello {data.name}!</div>
}
```

Normally, there're 3 possible states of a request: "loading", "ready", or "error". You can use the value of data and error to determine the current state of the request, and return the corresponding UI.
