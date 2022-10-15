---
title: Passport-http-bearer
description: This module lets you authenticate HTTP requests using bearer tokens.
created: 2021-10-15
updated: 2021-10-15
---


Passport's sole purpose is to authenticate requests, which it does through an extensible set of plugins known as strategies.

## Installation

```sh
npm install passport-http-bearer
```

## Usage

**Configure Strategy**

The HTTP Bearer authentication strategy authenticates users using a bearer token. The strategy requires a verify callback, which accepts that credential and calls done providing a user. Optional info can be passed, typically including associated scope, which will be set by Passport at req.authInfo to be used by later middleware for authorization and access control.

```javascript
passport.use(new BearerStrategy(
  function(token, done) {
    User.findOne({ token: token }, function (err, user) {
      if (err) { return done(err); }
      if (!user) { return done(null, false); }
      return done(null, user, { scope: 'all' });
    });
  }
));
// Store hash in your password DB.
```

**Authenticate Requests:**
Use passport.authenticate(), specifying the 'bearer' strategy, to authenticate requests. Requests containing bearer tokens do not require session support, so the session option can be set to false.

```javascript
app.get('/profile', 
  passport.authenticate('bearer', { session: false }),
  function(req, res) {
    res.json(req.user);
 });
```

**Authenticate Requests:**
Bearer tokens are typically issued using **OAuth 2.0**.[**OAuth2orize**](https://github.com/jaredhanson/oauth2orize) is a toolkit for implementing OAuth 2.0 servers and issuing bearer tokens. Once issued, this module can be used to authenticate tokens as described above.