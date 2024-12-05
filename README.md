# Getting Started with Python as Fast as Possible


# What is Python?

- Python is a general purpose programming language (its good at a lot of things).
- Its one of the most readable languages that exist. It also has one of the biggest communities
which means there are a lot of people and resources to learn.


### lets get more technical
- Python is an interpreted language, there is no compiling required.
- Python is a dynamic language, no need to declare data types.
- There are several flavors of python, some of the most popular are:
  - CPython - the typical, most common, flavor of python. This is usually what people refer to when they say "python". 
  This is written in the C programming language and maintained by a large group of individuals.
  - Jython - Instead of the C language, this flavor of python is written in Java.
  - IronPython (aka IPython) - Instead of the C language, this flavor of python is written in .NET.
  - Anaconda - This flavor of python comes with many common data analysis packages pre-installed. This is maintained by
  the Anaconda, Inc. company. Personally I think this is just CPython with bloat.
  - PyPy - A fast, minimal version of python that uses a JIT compiler. A little more difficult to configure.
  - Brython - A version of python that can run in a web browser, translating python code into JavaScript.


# How to use Python
1. Download the python interpreter from https://www.python.org/downloads/
2. Python files end with ``.py`` for example ``new_file.py``. Notice all lowercase and underscore format. 
Python heavily uses this **snake case** formatting.
3. In your ``.py`` file, you will write python code and then run it through the interpreter by using the terminal. 
4. Reference the interpreter and then the .py file like the example below.
   - Example: ``C:\username\python\bin\python.exe path\to\your\python\file.py``
   - Note you'll modify this to the correct paths on your computer.

### About the package manager (pip)
- The python community has a place where people can create and upload their own python packages. https://pypi.org/
- Python has a built-in manager that allows you to install packages from PyPI directly. This manager is called ``pip``
- There are many very popular libraries. Some popular and well utilized ones are:
  - For data there is [Pandas](https://pandas.pydata.org/docs/index.html), [SQLAlchemy](https://www.sqlalchemy.org/), 
  [DuckDB](https://duckdb.org/), [Polars](https://docs.pola.rs/)
  - API handling - [Requests](https://requests.readthedocs.io/en/latest/), [aiohttp](https://docs.aiohttp.org/en/stable/)
  - Markup parsing - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [lxml](https://lxml.de/)
  - Web servers - [Flask](https://flask.palletsprojects.com/en/stable/), [Django](https://docs.djangoproject.com/en/5.1/), [FastAPI](https://fastapi.tiangolo.com/)
  - File transfer - [Paramiko](https://www.paramiko.org/) (SFTP)
  - Environment variable usage - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - So much more...
- To make use of these, we need to use ``pip`` to install them into our python interpreter. But we don't want to install everything to the same python interpreter. 
That would cause it to become bloated if every project used the same interpreter. For this reason, every python project 
should have its own interpreter (see [Best practices for using python](#best-practices-for-using-python))

### Best practices for using python
- Every python project should have its own interpreter, called a virtual environment or shortened to "venv". To do this, we need to create a copy of the python interpreter 
for each project. PyCharm can manage this for you, or you can do it manually. If using PyCharm, you can skip to the pip commands.
  - To do this manually, you should use the terminal to navigate to the folder your project files will exist in and type ``python -m venv venv``
  This runs a python built-in command (``python``) in module mode (``-m``) to run the module venv (``venv``) and names the new interpreter venv (``venv``).
  - After you create the venv folder with the command, you'll need to activate it to install the libraries. To activate, 
  run the command ``venv\Scripts\activate``. For linux or mac the command is ``venv/bin/activate``.
  - From here you should see the terminal change to ``(venv) C:\users\username\directory``. In PyCharm, you can open the terminal and this will already be setup.
- Now you can run pip commands like: 
  - ``pip install pandas`` - install a package by using their PyPI name.
  - ``pip install pandas sqlalchemy duckdb`` - you can install more than one by chaining package names.
  - ``pip uninstall pandas`` - uninstall package by PyPI name.
  - ``pip install --upgrade pandas`` - upgrade already installed packages when a new version comes out.
  - ``pip list`` - show a list of installed packages.
  - ``pip freeze > requirements.txt`` - save the names and versions of installed packages to a file. 
  Good for saving and distributing dependencies so others can clone and use your project.
- Use the venv the same way ``C:\path\to\venv\python\bin\python.exe path\to\your\python\file.py``. PyCharm will automatically use these commands when you right-click and run a script.

# Writing Python Code

Python uses white-space and tabs, instead of curly-braces and semicolons like other common languages.

The simplest python script. This will print text to your terminal window.
```py
print('This is my first python script')
```

## Data Types

Native data types in python include:
- Integer ``int`` - whole number ie: 5
- Float ``float``- decimal number ie: 7.9
- String ``str``- text surrounded by single or double quotes ie: 'This is a string' or "This is a string"
- List, Tuple ``list, tuple``- grouped data combined into a collection that can be iterated over. Lists use square brackets ie: a 
list of integers ``[1, 2, 3, 4]``. Tuples use parenthesis ie: ``(1, 2, 3, 4)``. Lists can be mutated and tuples cannot.
- Dictionary ``dict``- key value pair collection of data, using curly-braces. ie: ``{'key 1': 'value 1', 'key 2': 'value 2'}``

## Variables

Any of the data types can be loaded into a variable that can then be referenced later:

```py
x = 14
variable_01 = 'This is a variable'
also_a_variable = {'foo': 'bar'}
```

Variables can be named almost anything, you just can't start a variable with a number and no special characters. 

You can perform mathematical operations, just like most programming languages.

```py
x = 5  # set variable
x = x + 1  # add 1 to x variable
x = x * 10  # multiply x by 10
x = x / 4  # divide x by 4
x = x ** 2  # raise x to the power of 2
```

## If Statements

If statements are great for checking conditions and running code if certain conditions are met.

```py
x = 10
if x > 8:
    print('x is greater than 8')
elif x <= 1:
    print('x is less or equal to 1')
else:
    print('x is between 1 and 8')
```

Keep in mind that checking equality should be done with two equal signs ``==`` because a single ``=`` is for assigning variables.

```py
x = 100

if x == 100:
    print('x is equal to 100')
```

## Loops

Types of loops:
- For - iterate over an object.
- While - loop until a condition is met.
- List comprehension - single line loop over an object.

For loop
```py
numbers = [2, 4, 6, 8, 10]

for number in numbers:
    print(number)  # will print each number in the list
```

While loop
```py
x = 0
while x < 10:
    print(x)
    x = x + 1  # add 1 to x on each loop
    # this loop will terminate once x is greater than 10
```

List comprehension - this is like a single line for loop
```py
numbers = [2, 4, 6, 8, 10]

# if we want to do a simple change to all the numbers in this list, such as double the amounts, we can use list comprehension
numbers = [number * 2 for number in numbers]
```


## Comments

Add comments to your code:
- ``#`` - single line comments
- ``""" """`` - multi-line comments
  ```py
  # single line comment.
  
  """
  Multi like comment
  Use this to describe 
  many things.
  """
  ```

## Importing other libraries

Python comes with the "Python Standard Library" which has a lot of powerful modules ready to go, no installing required.

[Python Standard Library Docs](https://docs.python.org/3/library/index.html)

To use any of these, or to use any libraries installed with pip, they must be imported. This is typically done at the top of the .py file.

```py
import os  # standard library, lets you interact with objects on your operating system like files.
import pandas as pd  # third-party library installed with pip. This imports the package and renames it as pd
from sqlalchemy import select, insert  # this imports specific parts of the sqlalchemy library, avoiding importing everything.
```

Load a csv file into a DataFrame using pandas.

```py
import pandas as pd

df = pd.read_csv('path/to/file.csv')
```

Connect to a database with sqlalchemy:

```py
# import library
from sqlalchemy import create_engine, text

# create an engine object to connect
engine = create_engine('postgresql+psycopg2://username:password@servername:port/database')

# connect to the database and query a table
with engine.connect() as conn:
    query = 'SELECT * FROM table'
    result = conn.execute(text(query))
```

## Function

Use the ``def`` keyword to define a function. You can use parameters to pass data into the function, process the data, and return a result.

```py
def example_function():
    pass


def repeat(message):
    print(f'You said {message}')  # this will print back your message and uses f-strings to inject your message to another string.
    

def add_numbers(number_1, number_2):
    return number_1 + number_2

```

You can create dynamic parameters using *args and **kwargs
```py
def add_numbers(*args):
    return_value = 0
    for value in args:
        return_value = return_value + value
    
    return return_value
```

## Class

Classes are good for grouping similar data and functions into one object. 
It's great for maintaining state of data, and performing certain operations on that data.

```py
import time


class Car:
  def __init__(self, year, make, model):
    # This function runs when the class is first used. Good for loading data right at the beginning.
    self.year = year
    self.make = make
    self.model = model
    self.current_speed = 0

  def accelerate(self):
    self.current_speed = 10
    # make car go

  def stop(self):
    self.current_speed = 0
    # make care brake


car = Car(2024, 'Tesla', 'Model Y')  # create the car object
car.accelerate()                     # run the accelerate function (when it's in a class it's called a method)
time.sleep(5)                        # wait 5 seconds
car.stop()                           # run the stop method
```


## Building Large Projects


Detail on how python import system works

How to run scripts in module mode and why its helpful

Python convert to byte-code

