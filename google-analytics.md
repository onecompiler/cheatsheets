---
title: Google Analytics
description: Google Analytics lets you measure your end user interactions on your websites and mobile apps. Google Analytics records all interactions and provides meaningful insights.
created: 2019-10-25
updated: 2019-10-25
---

Google Analytics lets you measure your end user interactions on your websites and mobile apps. Google Analytics records all interactions and provides meaningful insights.

## Available Platforms

1. Web
2. Android
3. iOS

## Adding Google Analytics to your Web application
Google analytics can be added to web applications by including the following script in head tag.

```javascript
<!-- Google Analytics-->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-xxxxx-x', 'auto');
  ga('send', 'pageview');
</script>

```

## Adding Google Analytics to your Android application

#### 1. Add `google-services` to your `build.gradle`

```groovy
dependencies {
  classpath 'com.google.gms:google-services:3.0.0'
}
```

#### 2. Add `play-services-analytics` to your `app/build.gradle`

```groovy
dependencies {
  compile 'com.google.android.gms:play-services-analytics:10.2.4'
}
```

#### 3. Create `app/src/res/xml/global_tracker.xml` to configure your Google Analytics tracker id

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string name="ga_trackingId" translatable="false">UA-xxxxx-x</string>
</resources>
```

#### 4. Create `AnalyticsApplication` by extending `android.app.Application` 

```java
package com.foo;
import android.app.Application;
import com.google.android.gms.analytics.GoogleAnalytics;
import com.google.android.gms.analytics.Tracker;

public class AnalyticsApplication extends Application {
  private static GoogleAnalytics googleAnalytics;
  private static Tracker tracker;

  @Override
  public void onCreate() {
    super.onCreate();
    googleAnalytics = GoogleAnalytics.getInstance(this);
  }

  synchronized public Tracker getDefaultTracker() {
    if (tracker == null) {
      tracker = googleAnalytics.newTracker(R.xml.global_tracker);
    }
    return tracker;
  }
}
```

#### 5. Start tracking your activities

```java
AnalyticsApplication application = (AnalyticsApplication) getApplication();
tracker = application.getDefaultTracker();
tracker.setScreenName("HomePage");
tracker.send(new HitBuilders.ScreenViewBuilder().build());
```
