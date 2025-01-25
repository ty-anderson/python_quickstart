# Advanced Topics

## Dynamic Function Parameters

If you have a function and you want to be able to pass any number of arguments
or keyword arguments, you can use args and kwargs.

```py
def function_name(*args, **kwargs):
    # in the function you can access args and kwargs
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)
```

You can also unpack dictionaries directly into a function call.
```py
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

data = {"name": "Alice", "age": 25}
greet(**data)  # Equivalent to greet(name="Alice", age=25)
```

## Context Managers

In programming there are a lot of instances where you'll need to open something
(file, database connection, etc.) and you'll need to make sure to close it
to free up resources and to protect the file from being corrupted or altered.

A very safe way to handle this is with context managers, using the ``with`` keyword.

Read, write, append to files.

```py
# write to file by opening in write mode 'w'
with open('file.txt', 'w') as write_file:
    write_file.write('Hello there')
# file is closed at this point

with open('file.txt', 'r') as read_only_file:
    file_data = read_only_file.read()

# close the file and use the data from it
print(file_data)

with open('file.txt', 'a') as append_file:
    append_file.write('This is how to append text to file.')

with open('file.txt', 'rw') as read_write_file:
    read_write_file.write('info')
    data = read_write_file.read()
```

Safely manage connections to a database.

```py
from sqlalchemy import create_engine

engine = create_engine('connection_string')

with engine.connect() as conn:
    conn.execute('query here')
```

You can create your own objects with context managers.

```py
class NewObject:
    def __init__(self, vars):
        self.vars = vars

    def __enter__(self):
        # open the connection using with statement
        self.open()

    def __exit__(self):
        # automatically run this on exiting with statement
        self.close()
```

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

Some favorite decorators:

```py
def time_it(func):
    """Prints the time it takes for a function to run"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        return_val = func(*args, **kwargs)
        print(f'{func.__name__} ran successfully in {datetime.datetime.now() - start_time}')
        return return_val
    return wrapper
```

```py
def avoid_day_of_week(day_of_week: List[int]):
    """
    Avoid running the decorated function on certain day of week.

    day_of_week:
        0 -> Mon
        1 -> Tue
        2 -> Wed
        3 -> Thu
        4 -> Fri
        5 -> Sat
        6 -> Sun
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_dt = utc_now()
            dow = calendar.weekday(current_dt.year, current_dt.month, current_dt.day)
            if dow in day_of_week:
                logit(f'Avoiding day of week {calendar.day_abbr[dow]} day integer ({dow})')
                return
            else:
                func(*args, **kwargs)

        return wrapper
    return decorator
```

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

## Global Interpreter Lock (GIL)

To achieve thread safety in python, there is something called the Global Interpreter Lock (GIL). The GIL is 
a bit of a double-edged sword because it achieves thread safety, but it also makes python slower due to running
everything on one thread. Python 3.13 has introduced an experimental mode where the GIL can be deactivated.
The most important thing here for now is to know it exists.

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

The double asterisk ** is for unpacking keyword arguments. This is why
they are used in functions with args and kwargs.

```py
def function_name(*args, **kwargs):
    # in the function you can access args and kwargs
    print(args[0])
    print(kwargs['item_01'])
    

function_name(1, 2, 3, item_01='value 1', item_02='value 2')
```