---
title: Maven commands
description: Maven is a software project management and comprehension tool with project object model (POM), It manages a project's build, reports, documentation from a central piece of information.
created: 2019-08-07
updated: 2019-08-07
---

## Simple clean, compile, install, build commands 

```sh
mvn compile                 #Compiles source code and stores classes to target/classes
mvn validate                #Validates project 
mvn test                    #Runs tests
mvn clean                   #Deletes target directory
mvn clean package           #Compiled code is packaged to WAR/JAR/deb etc
mvn clean install           #Install the artifact in local repository(.m2 Repo)
mvn clean deploy            #Copies the package(WAR/JAR/deb etc) to the remote repository
mvn verify
mvn clean verify
```

## Options 

```sh
mvn clean install -Dmaven.test.skip=true              #Skips compiling and running tests
mvn clean install -DskipTests=true                    #Compiles but skips running tests
mvn clean install -Dmaven.test.failure.ignore=true    #Compiles and executes tests but ignores if any tests failed
mvn verify Dit.test=TestName                          #Executes specified test
mvn clean install -T 4                                # -T is used to specify number of threads used, default 2 i.e., 2 threads per CPU.
mvn clean install -X/--debug                          #Enables debug mode
mvn clean package -U/--update-snapshots               #Force check on dependency updates 
mvn dependency:purge-local-repository                 #Removes local repository
```

## Dependency Plugin

```sh
mvn dependency:analyze                                 #Analyzes dependencies of the project
mvn dependency:tree                                    #Prints dependency tree
mvn versions:display-dependency-updates                #Displays dependency updates 
mvn dependency:analyze -DignoreNonCompile=true         #Shows unused dependencies
```

Creates pom.xml:
```sh
mvn archetype:create
```

## Create java project (JAR):

```sh
mvn archetype:create -DgroupId=org.onecompiler.project -DartifactId=one-compiler -DarchetypeArtifactId=maven-archetype-quickstart
```

## Create Web project (WAR):

```sh
mvn archetype:create -DgroupId=org.onecompiler.project -DartifactId=one-compiler -DarchetypeArtifactId=maven-archetype-webapp
```

## Eclipse sources:

```sh
mvn eclipse:eclipse                             #Eclipse creates .project, .settings, .classpath files based on pom.xml    
mvn eclipse:eclipse -DdownloadSources=true      #Also downloads dependencies
```

Create archetype from project:

```sh
mvn archetype:create-from-project
```

Lists all archetypes:

```sh
mvn archetype:generate
```

## Useful commands for Automatic deployment with tomcat plugin in your pom.xml

```sh
mvn tomcat:deploy                   #Deploys package
mvn tomcat:stop                     #Stops tomcat server
mvn tomcat:start                    #Starts tomcat server
```

Gives description of attributes plugin:

```sh
mvn help:describe -Dplugin=help
```

Describes single goal of plugin:

```sh
mvn help:describe -Dplugin=help -Dmojo=help
```

Displays the effective pom.xml for the current build, with the active profiles in it:

```sh
mvn help:effective-pom 
```

Displays active profiles:

```sh
mvn help:active-profiles
```
