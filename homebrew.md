---
title: Homebrew
description: Homebrew is a simple package management software for macOS & Linux. This Cheatsheat shows how to search, install, upgrade & uninstall softwares using Homebrew
created: 2019-06-16
updated: 2019-06-16
color: #2e2a24
---

## Installation for MacOS

####   Prerequisities
Install command-line tools if not already installed by running the following command 
```sh
xcode-select --install
```
Note: If you have installed Xcode already then your mac already have command-line tools. 

#### Install Homebrew


```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


## Installing a software
You can install brew available softwares by running the following command 
```sh
brew install <software_name>
```
example
```sh
brew install mongodb
```
If you want to install a specific version of a sooftware, you can mention the available version name using `@<version>`

Example
```sh
brew install mongodb@3.6
```

## Uninstalling a softwware
You can uninstall a installed software by running the following command 
```sh
brew remove <software_name>
```
example
```sh
brew remove mongodb
```

## Searching for a software 
You can search available softwares by running following command
```sh
brew search <software_name>
```
Example 
```sh
$ brew search mongodb
==> Formulae
mongodb ✔                                mongodb@3.2                              mongodb@3.6
mongodb@3.0                              mongodb@3.4                              percona-server-mongodb

==> Casks
mongodb                                  mongodb-compass-community                mongodbpreferencepane
mongodb-compass                          mongodb-compass-isolated-edition         nosqlbooster-for-mongodb
mongodb-compass-beta                     mongodb-compass-readonly                 orelord-mongodb
```

## Other useful commands


|Command|Use| Example|
|---|---|---|
|`brew doctor`| self-diagnose shows if the installatin is correct or not|NA|
|`brew upgrade <software_name>`|To Update a installed sooftware| `brew upgrade mongodb`|

## Uninstalling Homebrew
In case you decided to completely uninstall Homebrew from your Mac, you can run the followiong command to uninstall

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"

```

