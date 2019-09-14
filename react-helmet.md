---
title: React Helmet (React Component Library)
description: React Helmet is a React library used to change Document Head tags like title, meta etc.,
created: 2019-07-14
updated: 2019-07-14
---


React Helmet is a React library used to change Document Head tags like title, meta etc.,

## Installation

```sh
npm install react-helmet
```

## Example usage

```javascript
import React from "react";
import { Helmet } from "react-helmet";
 
class TermsAndConditions extends React.Component { 
    render (){
        return(
             <>
                {/* Helmet code for Head content */}
                <Helmet>
                    <title>{'Terms and Conditions'}</title>
                </Helmet>

                {/* Component content*/}
                <h1> Terms and Conditions </h1>
                <p>
                    ... 
                    .....
                    .......
                </p>

             </>   
        )
    }
}

export default TermsAndConditions;

```

## Possible tags 

```xml
<Helmet>
    <meta charSet="utf-8" />
    <title>{'Page Title'}</title>
    <meta name="description" content="description of the page" />

    <script src="http://foo.com/bar.js" type="text/javascript" />
    <link rel="stylesheet" href="http://foo.com/bar.css" />
</Helmet>
```