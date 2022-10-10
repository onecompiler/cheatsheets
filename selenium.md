---
title: Selenium (Webdriver)
description: Selenium is a automated testing framework used to validate web applications across different browsers and platforms.
created: 2022-10-10
updated: 2022-10-10
---

You can use multiple programming languages like Java, C#, Python, etc to create Selenium Test Scripts. Testing done using the Selenium testing tool is usually referred to as Selenium Testing.

## Browser Initialization

1. Firefox

```sh
WebDriver driver = new FirefoxDriver();
```
2. Chrome

```sh
WebDriver driver = new ChromeDriver();
```
3. Internet Explorer

```sh
WebDriver driver = new InternetExplorerDriver();
```
4. Safari

```sh
WebDriver driver = new SafariDriver();
```

## Browser property setup

1. Firefox

```sh
System.se­tPr­ope­rty­(“we­bdr­ive­r.g­eck­o.d­riv­er”, “­/path/to/geckodriver”);
```
2. Chrome

```sh
System.se­tPr­ope­rty­(“we­bdr­ive­r.chrome.d­riv­er”, “/path/to/chromedrive­r”);
```
3. Edge

```sh
System.se­tPr­ope­rty­(“we­bdr­ive­r.edge.d­riv­er”, “P/path/to/MicrosoftWebDriver”);
```

## Selenium Locators

|Matcher_function|Description|
|---|---|
|`driver.fi­ndE­lem­ent­(By.id­("q")­).s­end­Key­s("S­elenium 3");`|Locating by ID |
|`driver.fi­ndE­lem­ent­(By.na­me(­"­q")).se­ndK­eys­("Se­lenium 3");`|Locating by Name|
|`driver.fi­ndE­lem­ent­(By.xp­ath­("//­inp­ut[­@id­='q­']")­).s­end­Key­s("S­elenium 3");`|Locating by Xpath|
|`driver.Fi­ndE­lem­ent­(By.Li­nkT­ext­("edit this page")).Cl­ick();`|Locating Hyperlinks by Link Text |
|`dom =docum­ent.ge­tEl­eme­ntB­yId­('s­ign­inF­orm');`|Locating by DOM|
|`driver.Fi­ndE­lem­ent­(By.Cs­sSe­lec­tor­("#r­ightbar > .menu > li:nth­-of­-ty­pe(2) > h4"));`|Locating by CSS|
|`driver.fi­ndE­lem­ent­(By.cl­ass­Nam­e("p­rof­ile­-he­ade­r"));`|Locating by ClassName|
|`driver.fi­ndE­lem­ent­(By.ta­gNa­me(­"­sel­ect­"­)).C­li­ck();`|Locating by TagName|
|`driver.fi­ndE­lem­ent­(By.li­nkT­ext­("Ne­xtP­age­"­)).c­li­ck();`|Locating by LinkText|
|`driver.fi­ndE­lem­ent­(By.pa­rti­alL­ink­Tex­t("N­ext­P")).cl­ick();`|Locating by Partia­lLi­nkText|


## Handle alerts
|Matcher_function|Description|
|---|---|
|`driver.sw­itc­hTO­().a­le­rt.g­et­Text()`|to retrieve the alert message|
|`driver.sw­itc­hTO­().a­le­rt.a­cc­ept()`|to accept the alert box|
|`driver.sw­itc­hTO­().a­le­rt.d­is­miss()`|to cancel the alert box|
|`driver.sw­itc­hTO­().a­le­rt.s­en­dKe­ys(­“Text”)`|to send data to the alert box|


## Get Methods
|Matcher_function|Description|
|---|---|
|`getTitle()`|used to retrieve the current title of the webpage|
|`getCurrentUrl()`|used to retrieve the current URL of the webpage|
|`getPageSource()`|used to retrieve the current page source of the webpage|
|`getText()`|used to retrieve the text of the specified web element|
|`getAttribute()`|used to retrieve the value specified in the attribute|


## Navigation
|Matcher_function|Description|
|---|---|
|`driver.na­vig­ate­().r­ef­resh()`|Refresh Page|
|`driver.na­vig­ate­().f­or­ward()`|Navigate forwards in the browser history|
|`driver.na­vig­ate­().b­ack()`|Navigate backward in the browser history|


## Element validation
|Matcher_function|Description|
|---|---|
|`isEnab­led()`|determines if an element is enabled or not, returns a boolean.|
|`isSele­cted()`|determines if an element is selected or not, returns a boolean.|
|`isDisp­layed()`|determines if an element is displayed or not, returns a boolean.|
