# Kotlin Android Guide

This section presents coding convention used at Makimo for applications written
in Kotlin/Android.

The convention is based on [the official Kotlin style
guide](https://kotlinlang.org/docs/reference/coding-conventions.html).  In case
of omitted aspects of code style or some differences between the company policy
and Kotlin style guide, the following document gives preferred coding rules.

## Kotlin

### 1. Line length

Try not to exceed 100 characters per line. In some cases it is allowed to
use up to 120 characters. If your code line is longer than 120 characters,
please look at [the official Kotlin style
guide](https://kotlinlang.org/docs/reference/coding-conventions.html) to
reformat a piece of code.

### 2. Brackets around control flow statements and loops

Always use curly brackets around `if` and `when` when expression is multiline
as well as around loop statements. Put the opening curly brackets at the end of
the line and the closing one on a separate line aligned to the beginning of the
code block.

```kotlin
for (el in elements) {
    // do sth
}
```

```kotlin
if (bar) {
    // do sth
} else {
    // do sth else
}
```

```kotlin
when {
    x -> 1
    y -> 2
    else -> 3
}
```

In case of one-liners do not use brackets.

```kotlin
if (bar) doSth()
```

Also look at the official Kotlin style guide paragraph about
[formating](https://kotlinlang.org/docs/reference/coding-conventions.html#formatting)

### 3. Type declaration

Do not use type declarations in case of values and variables.

```kotlin
val x: Int = 5 // Bad
var y = "OK" // Good
```

### 4. Scope functions

Try to group code with scope functions such as `apply` if possible.

```kotlin
// Bad
val intent = Intent(this, SomeActivity::class.java)
intent.putExtra(VAL_1, 1)
intent.putExtra(VAL_2, 2)

// Good
val intent = Intent(this, SomeActivity::class.java).apply {
    putExtra(VAL_1, 1)
    putExtra(VAL_2, 2)
}
```

Other examples of scope functions are: `with`, `run`, `also` and `let`.

Look at the official Kotlin style guide section about [using scope functions]
(https://kotlinlang.org/docs/reference/coding-conventions.html#using-scope-functions-applywithrunalsolet)

### 5. Expressions

Many Kotlin's structure are expressions so try to use theirs advantages whenever possible.

#### 5.1 Control flow structures

```kotlin
// Bad
if (bar) {
    return 1
} else {
    return 2
}

// Good
return if (bar) {
    1
} else {
    2
}
```

```kotlin
// Bad
when (value) {
    x -> return 1
    y -> return 2
    else -> return 3
}

// Good
return when (value) {
    x -> 1
    y -> 2
    else -> 3
}
```

#### 5.2 Functions

```kotlin
// Bad
fun foo(x: Int): Int {
    return 2 * x
}

// Bad (unless context requires explicit type)
fun foo(x: Int): Int = 2 * x

// Good
fun foo(x: Int) = 2 * x
```

```kotlin
// Bad
fun foo(x: Int, y: String): Bar {
    val o = Bar()
    o.x = x
    o.y = y
    return o
}

// Good
fun foo(x: Int, y: String) = Bar().apply{
    this.x = x
    this.y = y
}
```

#### 6. Classes

##### 6.1 Formatting class definition

If declaration is below line length limit, put it on a single line, but
leave one single line after opening braces:

```kotlin
// Good:
class Foo(val b: Bar) {
    
    fun foo() {
        // ...
    }
}

// Bad:
class Foo(val b: Bar) {
    fun foo() {
        // ...
    }
}
```

If declaration is long, break it like so:

```kotlin
class Foo(
    val a: ClassA,
    val b: ClassB,
    val c: ClassC,
    val d: ClassD
): SomeInterface {
    
    fun foo() {
        // ^ Again one empty line above
    }
}
```

If you're declaring a `companion`, use one single line before and after:
```kotlin
class Foo {
    
    companion object {
        const val SOME_CONST = "some-const" // Notice no separator line here ^
    }
    
    val a = A()
}
```

## XML

### 1. Naming `layouts`

Good naming is an absolute must for an Android project. In order to make
searching for Android layout files easier, we use prefixes corresponding
to their function. Accordingly:

* `activity_` - Activity layout files;

* `fragment_` - Fragment layout files;

* `layout_` - Raw layouts; imported via `<layout name="...">`;

* `dialog_` - Dialog layout files;

* `item_` - List view item layout files;

* `view_` - View layout files, used by widgets and small self-contained widgets;


### 2. Naming `drawables`

* `btn_` - Custom button layout;

* `ic_` - Icon layout;

* `bkg_` - Background layout for a view;

* `view_` - Generic view layout (when other type does not fit);

* `selector_` - Selectors defining  different states of components;


### 3. Naming colors

Color names should correspond to the color they represent, *not* functionality
it is related to, such as `appBarColor` or `navBarBackgroundColor`.
Those are too hard to remember. 

It does not matter whether the color values ​​are written in uppercase or lowercase, 
But it's important to be consistent and stick to a chosen notation.

```xml
<!-- Bad -->
<color name="lightCerulean">#7bd3f7</color>
<color name="cerulean">#019FD9</color>
<color name="tealBlue">#007bb2</color>
<color name="pinkishRed">#F31F32</color>
```

```xml
<!-- Good -->
<color name="lightCerulean">#7bd3f7</color>
<color name="cerulean">#019fd9</color>
<color name="tealBlue">#007bb2</color>
<color name="pinkishRed">#f31f32</color>
```

```xml
<!-- Good -->
<color name="lightCerulean">#7BD3F7</color>
<color name="cerulean">#019FD9</color>
<color name="tealBlue">#007BB2</color>
<color name="pinkishRed">#F31F32</color>
```


### 4. Naming strings

Strings in most applications are divided into one-time specific strings
and generic informational strings, such as error-messages, confirmation
buttons, retry labels and so on. Accordingly, `strings` should reflect
this division. Examples of generic strings used throughout the application:

```xml
<string name="next">Next</string>
<string name="cancel">Cancel</string>
<string name="error_while_loading_data">There was a problem loading the data. Check your internet connection.</string>
```

Examples of specific strings:

```xml
<string name="next_event_date">Next event date: %1$s</string>
<string name="policy_number">Policy number: %1$s</string>
```

### 5. Naming dimens

When possible, dimensions should be divisible by 2, e.g.: 4, 8, 12, 16, 20,  24, 32, 50.
Most projects should use a finite set of standard paddings; e.g.:

```xml
<dimen name="xsmall_padding">4dp</dimen>
<dimen name="small_padding">8dp</dimen>
<dimen name="normal_padding">16dp</dimen>
<dimen name="large_padding">24dp</dimen>
<dimen name="xlarge_padding">32dp</dimen>
```

If the application contains a large number of dimens and naming them starts to be challenging 
it's a good practice to name them based on their value; eg.;

```xml
<dimen name="dim_8">8dp</dimen>  
<dimen name="dim_16">16dp</dimen>  
<dimen name="dim_24">24dp</dimen>  
<dimen name="dim_32">32dp</dimen>  
```

In the same way, you can define dimensions for text; eg.:

```xml
    <dimen name="h0">48sp</dimen>
    <dimen name="h1">24sp</dimen>
    <dimen name="h2">20sp</dimen>
    <dimen name="h3">18sp</dimen>  
	
	<dimen name="sp_4">4sp</dimen>
    <dimen name="sp_8">8sp</dimen>
    <dimen name="sp_10">10sp</dimen>
    <dimen name="sp_14">14sp</dimen>
```

### 6. Naming styles

Similar to naming colors, styles should be as generic as possible 
and correspond to their appearance or properties, not functionality.

```xml
<!-- Good -->
    <style name="RedButton">
        <item name=""></item>
    </style>
```

```xml
<!-- Bad -->
    <style name="NoInternetConnectionButton">
        <item name=""></item>
    </style>
```

It's also a good practice to separate the common base of different variants of styles, in such a case 
we should specify the variant name after the `ParentName.` beginning with a capital letter; eg.;

```xml
    <style name="RedButton">
        <item name=""></item>
    </style>

    <style name="RedButton.Large" parent="RedButton">
        <item name=""></item>
    </style>
	
	<style name="RedButton.Small" parent="RedButton">
        <item name=""></item>
    </style>
```

<a id="kt_js_import"></a>

## kt_js_import

<pre>
kt_js_import(<a href="#kt_js_import-name">name</a>, <a href="#kt_js_import-kwargs">kwargs</a>)
</pre>



**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="kt_js_import-name"></a>name |  <p align="center"> - </p>   |  none |
| <a id="kt_js_import-kwargs"></a>kwargs |  <p align="center"> - </p>   |  none |


<a id="kt_js_library"></a>

## kt_js_library

<pre>
kt_js_library(<a href="#kt_js_library-name">name</a>, <a href="#kt_js_library-kwargs">kwargs</a>)
</pre>



**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="kt_js_library-name"></a>name |  <p align="center"> - </p>   |  none |
| <a id="kt_js_library-kwargs"></a>kwargs |  <p align="center"> - </p>   |  none |


<!-- Generated with Stardoc: http://skydoc.bazel.build -->



<a id="#kt_javac_options"></a>

## kt_javac_options

kt_javac_options(<a href="#kt_javac_options-name">name</a>, <a href="#kt_javac_options-warn">warn</a>, <a href="#kt_javac_options-x_ep_disable_all_checks">x_ep_disable_all_checks</a>, <a href="#kt_javac_options-x_explicit_api_mode">x_explicit_api_mode</a>, <a href="#kt_javac_options-x_lint">x_lint</a>,
                 <a href="#kt_javac_options-xd_suppress_notes">xd_suppress_notes</a>)

                                                                                                
    Define java compiler options for `kt_jvm_*` rules with java sources.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_javac_options-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_javac_options-warn"></a>warn |  Control warning behaviour.   | String | optional | "report" |
|<a id="kt_javac_options-x_ep_disable_all_checks"></a>x_ep_disable_all_checks |  See javac -XepDisableAllChecks documentation   | Boolean | optional | False |
|<a id="kt_javac_options-x_explicit_api_mode"></a>x_explicit_api_mode |  Enable explicit API mode for Kotlin libraries.   | String | optional | "off" |
|<a id="kt_javac_options-x_lint"></a>x_lint |  See javac -Xlint: documentation   | List of strings | optional | [] |
|<a id="kt_javac_options-xd_suppress_notes"></a>xd_suppress_notes |  See javac -XDsuppressNotes documentation   | Boolean | optional | False |


<a id="#kt_jvm_binary"></a>

## kt_jvm_binary

kt_jvm_binary(<a href="#kt_jvm_binary-name">name</a>, <a href="#kt_jvm_binary-associates">associates</a>, <a href="#kt_jvm_binary-data">data</a>, <a href="#kt_jvm_binary-deps">deps</a>, <a href="#kt_jvm_binary-javac_opts">javac_opts</a>, <a href="#kt_jvm_binary-jvm_flags">jvm_flags</a>, <a href="#kt_jvm_binary-kotlinc_opts">kotlinc_opts</a>, <a href="#kt_jvm_binary-main_class">main_class</a>,
              <a href="#kt_jvm_binary-module_name">module_name</a>, <a href="#kt_jvm_binary-plugins">plugins</a>, <a href="#kt_jvm_binary-resource_jars">resource_jars</a>, <a href="#kt_jvm_binary-resource_strip_prefix">resource_strip_prefix</a>, <a href="#kt_jvm_binary-resources">resources</a>, <a href="#kt_jvm_binary-runtime_deps">runtime_deps</a>,
              <a href="#kt_jvm_binary-srcs">srcs</a>)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    Builds a Java archive ("jar file"), plus a wrapper shell script with the same name as the rule. The wrapper
        shell script uses a classpath that includes, among other things, a jar file for each library on which the binary
        depends.
        
        **Note:** This rule does not have all of the features found in [`java_binary`](https://docs.bazel.build/versions/master/be/java.html#java_binary).
        It is appropriate for building workspace utilities. `java_binary` should be preferred for release artefacts.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_jvm_binary-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_jvm_binary-associates"></a>associates |  Kotlin deps who should be considered part of the same module/compilation-unit             for the purposes of "internal" access. Such deps must all share the same module space             and so a target cannot associate to two deps from two different modules.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-data"></a>data |  The list of files needed by this rule at runtime. See general comments about <code>data</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-deps"></a>deps |  A list of dependencies of this rule.See general comments about <code>deps</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-javac_opts"></a>javac_opts |  Javac options to be used when compiling this target. These opts if provided will             be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_binary-jvm_flags"></a>jvm_flags |  A list of flags to embed in the wrapper script generated for running this binary. Note: does not yet         support make variable substitution.   | List of strings | optional | [] |
|<a id="kt_jvm_binary-kotlinc_opts"></a>kotlinc_opts |  Kotlinc options to be used when compiling this target. These opts if provided             will be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_binary-main_class"></a>main_class |  Name of class with main() method to use as entry point.   | String | required |  |
|<a id="kt_jvm_binary-module_name"></a>module_name |  The name of the module, if not provided the module name is derived from the label. --e.g.,         <code>//some/package/path:label_name</code> is translated to         <code>some_package_path-label_name</code>.   | String | optional | "" |
|<a id="kt_jvm_binary-plugins"></a>plugins |  -   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-resource_jars"></a>resource_jars |  Set of archives containing Java resources. If specified, the contents of these jars are merged into         the output jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-resource_strip_prefix"></a>resource_strip_prefix |  The path prefix to strip from Java resources, files residing under common prefix such as         <code>src/main/resources</code> or <code>src/test/resources</code> or <code>kotlin</code> will have stripping applied by convention.   | String | optional | "" |
|<a id="kt_jvm_binary-resources"></a>resources |  A list of files that should be include in a Java jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-runtime_deps"></a>runtime_deps |  Libraries to make available to the final binary or test at runtime only. Like ordinary deps, these will         appear on the runtime classpath, but unlike them, not on the compile-time classpath.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_binary-srcs"></a>srcs |  The list of source files that are processed to create the target, this can contain both Java and Kotlin         files. Java analysis occurs first so Kotlin classes may depend on Java classes in the same compilation unit.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |


<a id="#kt_jvm_import"></a>

## kt_jvm_import

kt_jvm_import(<a href="#kt_jvm_import-name">name</a>, <a href="#kt_jvm_import-deps">deps</a>, <a href="#kt_jvm_import-exported_compiler_plugins">exported_compiler_plugins</a>, <a href="#kt_jvm_import-exports">exports</a>, <a href="#kt_jvm_import-jar">jar</a>, <a href="#kt_jvm_import-jars">jars</a>, <a href="#kt_jvm_import-neverlink">neverlink</a>, <a href="#kt_jvm_import-runtime_deps">runtime_deps</a>,
              <a href="#kt_jvm_import-srcjar">srcjar</a>)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    Import Kotlin jars.
        
        ## examples
        
        ```bzl
        # Old style usage -- reference file groups, do not used this.
        kt_jvm_import(
            name = "kodein",
            jars = [
                "@com_github_salomonbrys_kodein_kodein//jar:file",
                "@com_github_salomonbrys_kodein_kodein_core//jar:file"
            ]
        )
        
        # This style will pull in the transitive runtime dependencies of the targets as well.
        kt_jvm_import(
            name = "kodein",
            jars = [
                "@com_github_salomonbrys_kodein_kodein//jar",
                "@com_github_salomonbrys_kodein_kodein_core//jar"
            ]
        )
        
        # Import a single kotlin jar.
        kt_jvm_import(
            name = "kotlin-stdlib",
            jars = ["lib/kotlin-stdlib.jar"],
            srcjar = "lib/kotlin-stdlib-sources.jar"
        )
        ```
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_jvm_import-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_jvm_import-deps"></a>deps |  Compile and runtime dependencies   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_import-exported_compiler_plugins"></a>exported_compiler_plugins |  Exported compiler plugins.<br><br>Compiler plugins listed here will be treated as if they were added in the plugins attribute of any targets that directly depend on this target. Unlike java_plugins' exported_plugins, this is not transitive   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_import-exports"></a>exports |  Exported libraries.<br><br>Deps listed here will be made available to other rules, as if the parents explicitly depended on these deps. This is not true for regular (non-exported) deps.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_import-jar"></a>jar |  The jar listed here is equivalent to an export attribute.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_import-jars"></a>jars |  The jars listed here are equavalent to an export attribute. The label should be either to a single class jar, or one or more filegroup labels.  The filegroups, when resolved, must contain  only one jar containing classes, and (optionally) one peer file containing sources, named <code>&lt;jarname&gt;-sources.jar</code>.<br><br>DEPRECATED - please use <code>jar</code> and <code>srcjar</code> attributes.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_import-neverlink"></a>neverlink |  If true only use this library for compilation and not at runtime.   | Boolean | optional | False |
|<a id="kt_jvm_import-runtime_deps"></a>runtime_deps |  Additional runtime deps.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_import-srcjar"></a>srcjar |  The sources for the class jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | //third_party:empty.jar |


<a id="#kt_jvm_library"></a>

## kt_jvm_library

kt_jvm_library(<a href="#kt_jvm_library-name">name</a>, <a href="#kt_jvm_library-associates">associates</a>, <a href="#kt_jvm_library-data">data</a>, <a href="#kt_jvm_library-deps">deps</a>, <a href="#kt_jvm_library-exported_compiler_plugins">exported_compiler_plugins</a>, <a href="#kt_jvm_library-exports">exports</a>, <a href="#kt_jvm_library-javac_opts">javac_opts</a>,
               <a href="#kt_jvm_library-kotlinc_opts">kotlinc_opts</a>, <a href="#kt_jvm_library-module_name">module_name</a>, <a href="#kt_jvm_library-neverlink">neverlink</a>, <a href="#kt_jvm_library-plugins">plugins</a>, <a href="#kt_jvm_library-resource_jars">resource_jars</a>, <a href="#kt_jvm_library-resource_strip_prefix">resource_strip_prefix</a>,
               <a href="#kt_jvm_library-resources">resources</a>, <a href="#kt_jvm_library-runtime_deps">runtime_deps</a>, <a href="#kt_jvm_library-srcs">srcs</a>)

                                                                                                
    This rule compiles and links Kotlin and Java sources into a .jar file.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_jvm_library-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_jvm_library-associates"></a>associates |  Kotlin deps who should be considered part of the same module/compilation-unit             for the purposes of "internal" access. Such deps must all share the same module space             and so a target cannot associate to two deps from two different modules.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-data"></a>data |  The list of files needed by this rule at runtime. See general comments about <code>data</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-deps"></a>deps |  A list of dependencies of this rule.See general comments about <code>deps</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-exported_compiler_plugins"></a>exported_compiler_plugins |  Exported compiler plugins.<br><br>Compiler plugins listed here will be treated as if they were added in the plugins attribute of any targets that directly depend on this target. Unlike <code>java_plugin</code>s exported_plugins, this is not transitive   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-exports"></a>exports |  Exported libraries.<br><br>Deps listed here will be made available to other rules, as if the parents explicitly depended on these deps. This is not true for regular (non-exported) deps.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-javac_opts"></a>javac_opts |  Javac options to be used when compiling this target. These opts if provided will             be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_library-kotlinc_opts"></a>kotlinc_opts |  Kotlinc options to be used when compiling this target. These opts if provided             will be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_library-module_name"></a>module_name |  The name of the module, if not provided the module name is derived from the label. --e.g.,         <code>//some/package/path:label_name</code> is translated to         <code>some_package_path-label_name</code>.   | String | optional | "" |
|<a id="kt_jvm_library-neverlink"></a>neverlink |  If true only use this library for compilation and not at runtime.   | Boolean | optional | False |
|<a id="kt_jvm_library-plugins"></a>plugins |  -   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-resource_jars"></a>resource_jars |  Set of archives containing Java resources. If specified, the contents of these jars are merged into         the output jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-resource_strip_prefix"></a>resource_strip_prefix |  The path prefix to strip from Java resources, files residing under common prefix such as         <code>src/main/resources</code> or <code>src/test/resources</code> or <code>kotlin</code> will have stripping applied by convention.   | String | optional | "" |
|<a id="kt_jvm_library-resources"></a>resources |  A list of files that should be include in a Java jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-runtime_deps"></a>runtime_deps |  Libraries to make available to the final binary or test at runtime only. Like ordinary deps, these will         appear on the runtime classpath, but unlike them, not on the compile-time classpath.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_library-srcs"></a>srcs |  The list of source files that are processed to create the target, this can contain both Java and Kotlin         files. Java analysis occurs first so Kotlin classes may depend on Java classes in the same compilation unit.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |


<a id="#kt_jvm_test"></a>

## kt_jvm_test

kt_jvm_test(<a href="#kt_jvm_test-name">name</a>, <a href="#kt_jvm_test-associates">associates</a>, <a href="#kt_jvm_test-data">data</a>, <a href="#kt_jvm_test-deps">deps</a>, <a href="#kt_jvm_test-env">env</a>, <a href="#kt_jvm_test-javac_opts">javac_opts</a>, <a href="#kt_jvm_test-jvm_flags">jvm_flags</a>, <a href="#kt_jvm_test-kotlinc_opts">kotlinc_opts</a>, <a href="#kt_jvm_test-main_class">main_class</a>,
            <a href="#kt_jvm_test-module_name">module_name</a>, <a href="#kt_jvm_test-plugins">plugins</a>, <a href="#kt_jvm_test-resource_jars">resource_jars</a>, <a href="#kt_jvm_test-resource_strip_prefix">resource_strip_prefix</a>, <a href="#kt_jvm_test-resources">resources</a>, <a href="#kt_jvm_test-runtime_deps">runtime_deps</a>, <a href="#kt_jvm_test-srcs">srcs</a>,
            <a href="#kt_jvm_test-test_class">test_class</a>)

                                                                                                                                                                                                                                                                                                                                                                                                    
    Setup a simple kotlin_test.
        
        **Notes:**
        * The kotlin test library is not added implicitly, it is available with the label
        `@com_github_jetbrains_kotlin//:kotlin-test`.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_jvm_test-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_jvm_test-associates"></a>associates |  Kotlin deps who should be considered part of the same module/compilation-unit             for the purposes of "internal" access. Such deps must all share the same module space             and so a target cannot associate to two deps from two different modules.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-data"></a>data |  The list of files needed by this rule at runtime. See general comments about <code>data</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-deps"></a>deps |  A list of dependencies of this rule.See general comments about <code>deps</code> at         [Attributes common to all build rules](https://docs.bazel.build/versions/master/be/common-definitions.html#common-attributes).   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-env"></a>env |  Specifies additional environment variables to set when the target is executed by bazel test.   | <a href="https://bazel.build/docs/skylark/lib/dict.html">Dictionary: String -> String</a> | optional | {} |
|<a id="kt_jvm_test-javac_opts"></a>javac_opts |  Javac options to be used when compiling this target. These opts if provided will             be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_test-jvm_flags"></a>jvm_flags |  A list of flags to embed in the wrapper script generated for running this binary. Note: does not yet         support make variable substitution.   | List of strings | optional | [] |
|<a id="kt_jvm_test-kotlinc_opts"></a>kotlinc_opts |  Kotlinc options to be used when compiling this target. These opts if provided             will be used instead of the ones provided to the toolchain.   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="kt_jvm_test-main_class"></a>main_class |  -   | String | optional | "com.google.testing.junit.runner.BazelTestRunner" |
|<a id="kt_jvm_test-module_name"></a>module_name |  The name of the module, if not provided the module name is derived from the label. --e.g.,         <code>//some/package/path:label_name</code> is translated to         <code>some_package_path-label_name</code>.   | String | optional | "" |
|<a id="kt_jvm_test-plugins"></a>plugins |  -   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-resource_jars"></a>resource_jars |  Set of archives containing Java resources. If specified, the contents of these jars are merged into         the output jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-resource_strip_prefix"></a>resource_strip_prefix |  The path prefix to strip from Java resources, files residing under common prefix such as         <code>src/main/resources</code> or <code>src/test/resources</code> or <code>kotlin</code> will have stripping applied by convention.   | String | optional | "" |
|<a id="kt_jvm_test-resources"></a>resources |  A list of files that should be include in a Java jar.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-runtime_deps"></a>runtime_deps |  Libraries to make available to the final binary or test at runtime only. Like ordinary deps, these will         appear on the runtime classpath, but unlike them, not on the compile-time classpath.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-srcs"></a>srcs |  The list of source files that are processed to create the target, this can contain both Java and Kotlin         files. Java analysis occurs first so Kotlin classes may depend on Java classes in the same compilation unit.   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_jvm_test-test_class"></a>test_class |  The Java class to be loaded by the test runner.   | String | optional | "" |


<!-- Generated with Stardoc: http://skydoc.bazel.build -->



<a id="#ktlint_config"></a>

## ktlint_config

ktlint_config(<a href="#ktlint_config-name">name</a>, <a href="#ktlint_config-android_rules_enabled">android_rules_enabled</a>, <a href="#ktlint_config-editorconfig">editorconfig</a>, <a href="#ktlint_config-experimental_rules_enabled">experimental_rules_enabled</a>)

                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            Used to configure ktlint.
                
        `ktlint` can be configured to use a `.editorconfig`, as documented at
        https://github.com/pinterest/ktlint/#editorconfig
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="ktlint_config-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="ktlint_config-android_rules_enabled"></a>android_rules_enabled |  Turn on Android Kotlin Style Guide compatibility   | Boolean | optional | False |
|<a id="ktlint_config-editorconfig"></a>editorconfig |  Editor config file to use   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="ktlint_config-experimental_rules_enabled"></a>experimental_rules_enabled |  Turn on experimental rules (ktlint-ruleset-experimental)   | Boolean | optional | False |


<a id="#ktlint_fix"></a>

## ktlint_fix

ktlint_fix(<a href="#ktlint_fix-name">name</a>, <a href="#ktlint_fix-config">config</a>, <a href="#ktlint_fix-srcs">srcs</a>)

                                                                                                
    Lint Kotlin files and automatically fix them as needed
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="ktlint_fix-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="ktlint_fix-config"></a>config |  ktlint_config to use   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="ktlint_fix-srcs"></a>srcs |  Source files to review and fix   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | required |  |


<a id="#ktlint_test"></a>

## ktlint_test

ktlint_test(<a href="#ktlint_test-name">name</a>, <a href="#ktlint_test-config">config</a>, <a href="#ktlint_test-srcs">srcs</a>)

                                                                                                
    Lint Kotlin files, and fail if the linter raises errors.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="ktlint_test-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="ktlint_test-config"></a>config |  ktlint_config to use   | <a href="https://bazel.build/docs/build-ref.html#labels">Label</a> | optional | None |
|<a id="ktlint_test-srcs"></a>srcs |  Source files to lint   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | required |  |


<!-- Generated with Stardoc: http://skydoc.bazel.build -->



<a id="#kt_compiler_plugin"></a>

## kt_compiler_plugin

kt_compiler_plugin(<a href="#kt_compiler_plugin-name">name</a>, <a href="#kt_compiler_plugin-compile_phase">compile_phase</a>, <a href="#kt_compiler_plugin-deps">deps</a>, <a href="#kt_compiler_plugin-id">id</a>, <a href="#kt_compiler_plugin-options">options</a>, <a href="#kt_compiler_plugin-stubs_phase">stubs_phase</a>, <a href="#kt_compiler_plugin-target_embedded_compiler">target_embedded_compiler</a>)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    Define a plugin for the Kotlin compiler to run. The plugin can then be referenced in the `plugins` attribute
        of the `kt_jvm_*` rules.
        
        An example can be found under `//examples/plugin`:
        
        ```bzl
        kt_compiler_plugin(
            name = "open_for_testing_plugin",
            id = "org.jetbrains.kotlin.allopen",
            options = {
                "annotation": "plugin.OpenForTesting",
            },
            deps = [
                "@com_github_jetbrains_kotlin//:allopen-compiler-plugin",
            ],
        )
        
        kt_jvm_library(
            name = "open_for_testing",
            srcs = ["OpenForTesting.kt"],
        )
        
        kt_jvm_library(
            name = "user",
            srcs = ["User.kt"],
            plugins = [":open_for_testing_plugin"],
            deps = [
                ":open_for_testing",
            ],
        )
        ```
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_compiler_plugin-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_compiler_plugin-compile_phase"></a>compile_phase |  Runs the compiler plugin during kotlin compilation. Known examples: <code>allopen</code>, <code>sam_with_reciever</code>   | Boolean | optional | True |
|<a id="kt_compiler_plugin-deps"></a>deps |  The list of libraries to be added to the compiler's plugin classpath   | <a href="https://bazel.build/docs/build-ref.html#labels">List of labels</a> | optional | [] |
|<a id="kt_compiler_plugin-id"></a>id |  The ID of the plugin   | String | required |  |
|<a id="kt_compiler_plugin-options"></a>options |  Dictionary of options to be passed to the plugin. Supports the following template values:<br><br>- <code>{generatedClasses}</code>: directory for generated class output - <code>{temp}</code>: temporary directory, discarded between invocations - <code>{generatedSources}</code>:  directory for generated source output   | <a href="https://bazel.build/docs/skylark/lib/dict.html">Dictionary: String -> String</a> | optional | {} |
|<a id="kt_compiler_plugin-stubs_phase"></a>stubs_phase |  Runs the compiler plugin in kapt stub generation.   | Boolean | optional | True |
|<a id="kt_compiler_plugin-target_embedded_compiler"></a>target_embedded_compiler |  Plugin was compiled against the embeddable kotlin compiler. These plugins expect shaded kotlinc             dependencies, and will fail when running against a non-embeddable compiler.   | Boolean | optional | False |


<a id="#kt_javac_options"></a>

## kt_javac_options

kt_javac_options(<a href="#kt_javac_options-name">name</a>, <a href="#kt_javac_options-warn">warn</a>, <a href="#kt_javac_options-x_ep_disable_all_checks">x_ep_disable_all_checks</a>, <a href="#kt_javac_options-x_explicit_api_mode">x_explicit_api_mode</a>, <a href="#kt_javac_options-x_lint">x_lint</a>,
                 <a href="#kt_javac_options-xd_suppress_notes">xd_suppress_notes</a>)

                                                                                                
    Define java compiler options for `kt_jvm_*` rules with java sources.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_javac_options-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_javac_options-warn"></a>warn |  Control warning behaviour.   | String | optional | "report" |
|<a id="kt_javac_options-x_ep_disable_all_checks"></a>x_ep_disable_all_checks |  See javac -XepDisableAllChecks documentation   | Boolean | optional | False |
|<a id="kt_javac_options-x_explicit_api_mode"></a>x_explicit_api_mode |  Enable explicit API mode for Kotlin libraries.   | String | optional | "off" |
|<a id="kt_javac_options-x_lint"></a>x_lint |  See javac -Xlint: documentation   | List of strings | optional | [] |
|<a id="kt_javac_options-xd_suppress_notes"></a>xd_suppress_notes |  See javac -XDsuppressNotes documentation   | Boolean | optional | False |


<a id="#kt_kotlinc_options"></a>

## kt_kotlinc_options

kt_kotlinc_options(<a href="#kt_kotlinc_options-name">name</a>, <a href="#kt_kotlinc_options-include_stdlibs">include_stdlibs</a>, <a href="#kt_kotlinc_options-java_parameters">java_parameters</a>, <a href="#kt_kotlinc_options-warn">warn</a>, <a href="#kt_kotlinc_options-x_allow_result_return_type">x_allow_result_return_type</a>,
                   <a href="#kt_kotlinc_options-x_backend_threads">x_backend_threads</a>, <a href="#kt_kotlinc_options-x_emit_jvm_type_annotations">x_emit_jvm_type_annotations</a>, <a href="#kt_kotlinc_options-x_explicit_api_mode">x_explicit_api_mode</a>,
                   <a href="#kt_kotlinc_options-x_inline_classes">x_inline_classes</a>, <a href="#kt_kotlinc_options-x_jvm_default">x_jvm_default</a>, <a href="#kt_kotlinc_options-x_lambdas">x_lambdas</a>, <a href="#kt_kotlinc_options-x_multi_platform">x_multi_platform</a>, <a href="#kt_kotlinc_options-x_no_call_assertions">x_no_call_assertions</a>,
                   <a href="#kt_kotlinc_options-x_no_optimize">x_no_optimize</a>, <a href="#kt_kotlinc_options-x_no_optimized_callable_references">x_no_optimized_callable_references</a>, <a href="#kt_kotlinc_options-x_no_param_assertions">x_no_param_assertions</a>,
                   <a href="#kt_kotlinc_options-x_no_receiver_assertions">x_no_receiver_assertions</a>, <a href="#kt_kotlinc_options-x_optin">x_optin</a>, <a href="#kt_kotlinc_options-x_report_perf">x_report_perf</a>, <a href="#kt_kotlinc_options-x_sam_conversions">x_sam_conversions</a>,
                   <a href="#kt_kotlinc_options-x_skip_prerelease_check">x_skip_prerelease_check</a>, <a href="#kt_kotlinc_options-x_use_k2">x_use_k2</a>)

                                                                                                
    Define kotlin compiler options.
    

**ATTRIBUTES**


| Name  | Description | Type | Mandatory | Default |
| :------------- | :------------- | :------------- | :------------- | :------------- |
|<a id="kt_kotlinc_options-name"></a>name |  A unique name for this target.   | <a href="https://bazel.build/docs/build-ref.html#name">Name</a> | required |  |
|<a id="kt_kotlinc_options-include_stdlibs"></a>include_stdlibs |  Don't automatically include the Kotlin standard libraries into the classpath (stdlib and reflect).   | String | optional | "all" |
|<a id="kt_kotlinc_options-java_parameters"></a>java_parameters |  Generate metadata for Java 1.8+ reflection on method parameters.   | Boolean | optional | False |
|<a id="kt_kotlinc_options-warn"></a>warn |  Control warning behaviour.   | String | optional | "report" |
|<a id="kt_kotlinc_options-x_allow_result_return_type"></a>x_allow_result_return_type |  Enable kotlin.Result as a return type   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_backend_threads"></a>x_backend_threads |  When using the IR backend, run lowerings by file in N parallel threads. 0 means use a thread per processor core. Default value is 1.   | Integer | optional | 1 |
|<a id="kt_kotlinc_options-x_emit_jvm_type_annotations"></a>x_emit_jvm_type_annotations |  Basic support for type annotations in JVM bytecode.   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_explicit_api_mode"></a>x_explicit_api_mode |  Enable explicit API mode for Kotlin libraries.   | String | optional | "off" |
|<a id="kt_kotlinc_options-x_inline_classes"></a>x_inline_classes |  Enable experimental inline classes   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_jvm_default"></a>x_jvm_default |  Specifies that a JVM default method should be generated for non-abstract Kotlin interface member.   | String | optional | "off" |
|<a id="kt_kotlinc_options-x_lambdas"></a>x_lambdas |  Change codegen behavior of lambdas   | String | optional | "class" |
|<a id="kt_kotlinc_options-x_multi_platform"></a>x_multi_platform |  Enable experimental language support for multi-platform projects   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_no_call_assertions"></a>x_no_call_assertions |  Don't generate not-null assertions for arguments of platform types   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_no_optimize"></a>x_no_optimize |  Disable optimizations   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_no_optimized_callable_references"></a>x_no_optimized_callable_references |  Do not use optimized callable reference superclasses. Available from 1.4.   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_no_param_assertions"></a>x_no_param_assertions |  Don't generate not-null assertions on parameters of methods accessible from Java   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_no_receiver_assertions"></a>x_no_receiver_assertions |  Don't generate not-null assertion for extension receiver arguments of platform types   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_optin"></a>x_optin |  Define APIs to opt-in to.   | List of strings | optional | [] |
|<a id="kt_kotlinc_options-x_report_perf"></a>x_report_perf |  Report detailed performance statistics   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_sam_conversions"></a>x_sam_conversions |  Change codegen behavior of SAM/functional interfaces   | String | optional | "class" |
|<a id="kt_kotlinc_options-x_skip_prerelease_check"></a>x_skip_prerelease_check |  Suppress errors thrown when using pre-release classes.   | Boolean | optional | False |
|<a id="kt_kotlinc_options-x_use_k2"></a>x_use_k2 |  Compile using experimental K2. K2 is a new compiler pipeline, no compatibility guarantees are yet provided   | Boolean | optional | False |


<a id="define_kt_toolchain"></a>

## define_kt_toolchain

<pre>
define_kt_toolchain(<a href="#define_kt_toolchain-name">name</a>, <a href="#define_kt_toolchain-language_version">language_version</a>, <a href="#define_kt_toolchain-api_version">api_version</a>, <a href="#define_kt_toolchain-jvm_target">jvm_target</a>, <a href="#define_kt_toolchain-experimental_use_abi_jars">experimental_use_abi_jars</a>,
                    <a href="#define_kt_toolchain-experimental_strict_kotlin_deps">experimental_strict_kotlin_deps</a>, <a href="#define_kt_toolchain-experimental_report_unused_deps">experimental_report_unused_deps</a>,
                    <a href="#define_kt_toolchain-experimental_reduce_classpath_mode">experimental_reduce_classpath_mode</a>, <a href="#define_kt_toolchain-experimental_multiplex_workers">experimental_multiplex_workers</a>, <a href="#define_kt_toolchain-javac_options">javac_options</a>,
                    <a href="#define_kt_toolchain-kotlinc_options">kotlinc_options</a>, <a href="#define_kt_toolchain-jacocorunner">jacocorunner</a>)
</pre>

Define the Kotlin toolchain.

**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="define_kt_toolchain-name"></a>name |  <p align="center"> - </p>   |  none |
| <a id="define_kt_toolchain-language_version"></a>language_version |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-api_version"></a>api_version |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-jvm_target"></a>jvm_target |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-experimental_use_abi_jars"></a>experimental_use_abi_jars |  <p align="center"> - </p>   |  <code>False</code> |
| <a id="define_kt_toolchain-experimental_strict_kotlin_deps"></a>experimental_strict_kotlin_deps |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-experimental_report_unused_deps"></a>experimental_report_unused_deps |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-experimental_reduce_classpath_mode"></a>experimental_reduce_classpath_mode |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-experimental_multiplex_workers"></a>experimental_multiplex_workers |  <p align="center"> - </p>   |  <code>None</code> |
| <a id="define_kt_toolchain-javac_options"></a>javac_options |  <p align="center"> - </p>   |  <code>Label("//kotlin/internal:default_javac_options")</code> |
| <a id="define_kt_toolchain-kotlinc_options"></a>kotlinc_options |  <p align="center"> - </p>   |  <code>Label("//kotlin/internal:default_kotlinc_options")</code> |
| <a id="define_kt_toolchain-jacocorunner"></a>jacocorunner |  <p align="center"> - </p>   |  <code>None</code> |


<a id="kt_register_toolchains"></a>

## kt_register_toolchains

<pre>
kt_register_toolchains()
</pre>

This macro registers the kotlin toolchain.



<!-- Generated with Stardoc: http://skydoc.bazel.build -->



<a id="kotlin_repositories"></a>

## kotlin_repositories

<pre>
kotlin_repositories(<a href="#kotlin_repositories-compiler_repository_name">compiler_repository_name</a>, <a href="#kotlin_repositories-compiler_release">compiler_release</a>, <a href="#kotlin_repositories-configured_repository_name">configured_repository_name</a>)
</pre>

Call this in the WORKSPACE file to setup the Kotlin rules.

**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="kotlin_repositories-compiler_repository_name"></a>compiler_repository_name |  for the kotlinc compiler repository.   |  <code>"com_github_jetbrains_kotlin"</code> |
| <a id="kotlin_repositories-compiler_release"></a>compiler_release |  version provider from versions.bzl.   |  <code>struct()</code> |
| <a id="kotlin_repositories-configured_repository_name"></a>configured_repository_name |  for the default versioned kt_* rules repository. If None, no versioned repository is created.   |  <code>"io_bazel_rules_kotlin_configured"</code> |

