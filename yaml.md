---
title: YAML (YAML Ain't Markup Language)
description: YAML is a human-friendly data serialization language. This is the most commonly used sytax for configuration files.
created: 2019-06-20
updated: 2019-06-20
color: #e74c3c
---

YAML is a human-friendly data serialization language. This is the most commonly used sytax for configuration files.


## Example YAML file
```yaml
---
title: Post Title
descrription: Post description
content: Post Content...........
tags:
- tag1
- tag2
- tag3
user:
  id: 1
  name: user name
  address:
    streetAddress: foo
    zip: '01234'
...    
```

## Rules
1. content starts with `---` & ends witth `...` (This is an optional rule)
2. Key value pairs are separated by colon & space( `: ` )
3. List values start with hyphen & space ( `- ` )
