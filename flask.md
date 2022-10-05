---
title: FLASK 
description: Flask cheat sheet gives you a quick reference of basic codes and attributes and is very handy while coding. 

created: 2022-10-05
updated: 2022-10-05
---

## Creating a Simple App
- Create a module called `app.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()
```




## Structure of a Flask app 
- Project tree for a project called `work`:
```
run.py
work/
	__init__.py
	config.py
	forms.py
	models.py
	admin/
		__init__.py
		routes.py
	main/
		__init__.py
		routes.py
	templates/
		index.html
	static/
		css/
			style.css
```


## Creating a route


This is to make different endpoints in our flask app.

```bash
@app.route("/")
```

## Allowed methods


Used to specify which methods are allowed for a request. Allowing get and post requests on an endpoint.

```bash
methods = ['GET', 'POST']
```

## Render page using Jinja


Jinja is a web template engine for the Python programming language. 

```bash
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/test")
def template_test():
    return render_template('template.html', my_string="Jinja Works!!")

if __name__ == '__main__':
    app.run(debug=True)
```
The HTML template
```bash
<html>
  <head>
    <title>Jinja Template Example</title>
  </head>
  <body>
    <div class="box">
      <p>Result: {{my_name}}</p>
    </div>
  </body>
</html>
```

## Importing SQLAlchemy


This is to make different endpoints in our flask app.

```bash
from flask_sqlalchemy import SQLAlchemy
```
## Database URI
This is the database's address
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name' 
```

## Initialization
This is used to initialize SQLAlchemy
```bash
db = SQLAlchemy(app)
```

Creating a Model
```bash
class TableName(db.Model): 
    column_1 = db.Column(db.Integer, primary_key=True)
    column_2 = db.Column(db.String(80), nullable=False)
    column_3 = db.Column(db.String(12), nullable=False)
```
