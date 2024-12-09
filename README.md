# Getting Started with Python as Fast as Possible

### Table of Contents

- [What is Python?](#what-is-python)
  - [Lets Get More Technical](#lets-get-more-technical)
- [How to Use Python](#how-to-use-python)
  - [Pip Package Manager](#about-the-package-manager-pip)
  - [Best Practices](#best-practices-for-using-python)
- [Writing Python Code](#writing-python-code)
  - [Data Types](#data-types)
  - [Variables](#variables)
  - [If Statements](#if-statements)
  - [Loops](#loops)
  - [Comments](#comments)
  - [Imports](#importing-other-libraries)
  - [Functions](#functions)
  - [Classes](#classes)
  - [Building Large Projects](#building-large-projects)
- [Advanced Topics](#advanced-topics)
  - [Decorators](#decorators)
  - [Generators](#generators)
  - [More About the Import System](#python-import-system)
  - [Run Scripts in Module Mode](#run-scripts-in-module-mode)
  - [Asyncio](#asyncio)
  - [Cython](#cython)
  - [Other Helpful Tips](#other-helpful-tips)
  - [Publishing a Project](#publishing-a-project)

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

## Functions

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

## Classes

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

Large python projects can be extremely powerful, but they must be organized a certain way to work properly.

A project should always start with a root folder and other folders and files will be housed inside the root folder.

The file structure of a project might look something like this:
```
/project_root
   /db
       __init__.py
       model.py
       connectors.py
   /views
       __init__.py
       views.py
   /reports
       __init__.py
       report_01.py
       report_02.py
   .env
```

Notice other directories have a file called ``__init__.py``. This is a python file that tells python "this folder is
a python module" which means you can put python files with code inside the folder and use it. With this structure, 
you have code in the views.py file like:
```py
from db import model
from reports import report_01
```

If there is code in the ``__init__.py`` file, you can just import the module name like ``import db``. If there is
a function inside the ``__init__.py`` file called ``new_func`` you could ``from db import new_func``

To run various files in a larger project, see [run scripts in module mode](#run-scripts-in-module-mode)


# Advanced Topics

## Decorators

Decorators are a way to add extra functionality to other functions.

```py
import functools

def decorator_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before the wrapped function
        wrapper_value = func(*args, **kwargs)
        # do something after the wrapped function
        return wrapper_value
    return wrapper
```

To use this defined decorator, it would look something like this:
```py
@decorator_name
def wrapped_function():
    # regular function stuff
```

If you've defined the decorator to also take arguments, you can add them:
```py
import functools

def decorator_name(arg1, arg2):
    def decorator_wrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # do something before the wrapped function
            wrapper_value = func(*args, **kwargs)
            # do something after the wrapped function
            return wrapper_value
        return wrapper
    return decorator_name


@decorator_name(arg1, arg2)
def wrapped_function():
    # regular function stuff
```

Here is a more in-depth tutorial on decorators https://realpython.com/primer-on-python-decorators/

## Generators

Generators can be thought of as iterables that are not fully loaded into memory. This allows you can handle the 
same data, without worrying about memory consumption.

A generator is defined by a function that uses the keyword ``yield``. When a function is used, it is run and then 
looses all state afterward. A generator will maintain state and can be called again multiple times.

For example, imagine you need to pull API data using every individual for the last 20 years. Instead of loading all
dates into one big list, you can create a generator function to calculate it.

```py
import datetime
import requests

# this is a generator because it uses the keyword yield.
def date_generator(start_date):
    today = datetime.datetime.today()
    while start_date < today:
        yield start_date  # this gets returned. If this function is called again, it will start here.
        start_date = start_date + 1


url = 'example_url.com/api'
for date in date_generator(datetime.datetime.date(1990, 1, 1)):
    response = requests.get(f'{url}/date_param={date}')
```

If you don't want to loop over a generator, you can also use the ``.next()`` method.

```py
gen = generator_function()
next_value = gen.next()
```

More detailed info here https://wiki.python.org/moin/Generators

## Python Import System

Importing libraries can be tricky in certain cases. The typical use is to just import any python package such as 
``import sys``

The best option 99% of the time is going to be [run scripts in module mode](#run-scripts-in-module-mode). Read
below to learn more about how the python import system works.

A python interpreter or virtual environment has a list of directories to look for imports from.  
It will start to look for the import in the first item of the list and go through each directory 
until it finds the import or fails and raises an exception.  

If you are running a module that imports another module that you've created, in a directory 
outside of the current directory, then you might need to add that directory to the sys.path. 

- Option 1: Add a pth file in the virtual environment with the path you want to add.
  1. Go to venv/lib/python/site-packages/<create pth file like custom_path.pth>
  2. Add your path such as /home/tyranderson/snfStudyData
	
- Option 2: Hardcode the path directly into the activate file.
In a venv you can edit the bin/activate file and include: ``export PYTHONPATH="/the/path/you/want"``

- Option 3: Add into python script - within your script you can ``sys.path.append("/the/path/you/want")``
but this is temporary and the path will be dropped once the script is done running.  

More info here: https://help.pythonanywhere.com/pages/DebuggingImportError

## Run scripts in module mode

You can run scripts from a venv 2 different ways:
1. As a standalone script 
   1. This is the format path/to/venv/bin/python path/to/script
   2. If this script has imports to other files, it will have import errors. This is not the recommended way!!!!!!!
2. In module mode 
   1. Path/to/venv/bin/python -m path.to.script

Using module mode is considered best practice because it allows all modules to import from the project root properly.
If you have multiple python modules (.py files) you are importing from various directories within the project,
you will likely have import errors if you try to run using the standalone method. This is why its considered
best practice to run in module mode. (PyCharm does this for you when you run a script).

Linux
```bash
cd path/to/project
. venv/bin/activate -m path.to.python.file
```

Windows
```commandline
cd path\to\project
venv\Scripts\activate -m path.to.python.file
```

## Asyncio

All the code up to this point has been synchronous, meaning everything happens one step at a time.
Asynchronous (async) code can be used to handle multiple tasks at the same time.

Be aware, async code is more complicated than synchronous in any language, including python. 

When should I use async code?

If your code is...
- CPU Bound - use [Multi Processing](https://docs.python.org/3/library/multiprocessing.html)
- IO bound, fast IO, limited number of connections - use [Threading](https://docs.python.org/3/library/threading.html)
- IO bound, slow IO, many connections - use [Asyncio](https://docs.python.org/3/library/asyncio.html)

In other words....
```py
if io_bound:
    if io_very_slow:
        print('Use asyncio')
    else:
        print('Use threads')
else:
    print('Use Multi processing')
```
### General Info

The most important keywords: 
``async`` and ``await``

The most important functions:
``asyncio.run()`` and ``asyncio.gather()``

- ``async`` - this keyword is used to define a function that will be capable of running async. This turns the 
function into whats called a coroutine. If a function is a coroutine (has the async keyword), then it has to 
utilize the await keyword as well.
- ``await`` - is the keyword that is used to let python know that a function is going to take some time to resolve. 
It will stop trying to run the function and move on to another task while it waits for the task to resolve.
- ``asyncio.run()`` - this is the most common way to run a coroutine (function with async). A coroutine cannot be 
called like a normal function.
- ``asyncio.gather()`` - this is not required but is extremely useful and common. ``gather`` allows you to run 
multiple coroutines at the same time.

The best way to understand async code is to experiment with it. Lets look at some examples.

```py
import asyncio

# this is a coroutine
async def async_function(request_data):
    data = await some_async_task(request_data)
    return data

# this is a coroutine
async def main():
    results = await asyncio.gather(
      async_function('x'), 
      async_function('y'),
      async_function('z')
    )
    print(results)
    
if __name__ == '__main__':
    asyncio.run(main())  # this is how you run a coroutine
```

## Cython

One of the biggest criticisms of python is its performance. When you compare it to statically typed, compiled languages,
it doesn't have near the same speed. One option to improve performance is with something called Cython. Cython is
an extension of python that allows statically typed python that can be compiled to C code for performance enhancements.

[Official Cython Docs](https://cython.readthedocs.io/en/latest/index.html)

Example:

```py
# example.pyx file

def sum_integers(int n):
    cdef int i
    cdef int total = 0
    for i in range(n):
        total += i
    return total
	
```

Create setup.py file:

```py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("example.pyx")
)
```
run python setup.py build_ext --inplace

## Other Helpful Tips

**Unpacking Iterables** is a useful trick. If you have a list or other iterable that you want to perform an operation on
you can unpack it with an asterisk.

```py
# with unpacking
numbers = [1, 2, 3, 4]
print(*numbers)

# this gives the same result, but requires more code
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)
```

## Publishing a Project

You can create your own python library and publish it to PyPI. First you'll need to create an account and download
your API keys. Once you have those established, you can create your project and then:

Super summary:
1. Create the pyproject.toml file and fill out the fields 
2. run py -m build 
3. use twine to send to pypi.

More detailed steps:
1. Make sure all of your files are created inside a folder structure
2. Create pyproject.toml
```toml
[build-system] 
requires = ["setuptools", "wheel"] 
build-backend = "setuptools.build_meta"
  
[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
{ name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
]
		
[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```
3. Make sure all relevant build libs are installed:
   1. pip install --upgrade build
   2. pip install twine
4. Run the build
   1. py -m build
5. Send to PyPI
   1. py -m twine upload dist/*
	
https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files

There are also new tools coming out such as poetry and uv. 
The community has started to heavily embrace [UV](https://astral.sh/blog/uv) due to its speed and tooling.

# Important Libraries - Getting Started

## Pandas

## SQLAlchemy

## DuckDB

## Airflow

## Locust


# Documentation Tools

## Sphinx


## Mermaid


## MKDocs


# 
