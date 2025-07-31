
# Writing Python Code

Python uses white-space and tabs, instead of curly-braces and semicolons like other common languages.

The simplest python script. This will print text to your terminal window.
```py
print('This is my first Python script')
```

## Data Types

Native data types in python include:

- Integer ``int`` - whole number ie: 5
- Float ``float``- decimal number ie: 7.9
- String ``str``- text surrounded by single or double quotes ie: 'This is a string' or "This is a string"
- List, Tuple ``list, tuple``- grouped data combined into a collection that can be iterated over. Lists use square brackets ie: a 
list of integers ``[1, 2, 3, 4]``. Tuples use parenthesis ie: ``(1, 2, 3, 4)``. Lists can be mutated and tuples cannot.
- Dictionary ``dict``- key value pair collection of data, using curly-braces. ie: ``{'key 1': 'value 1', 'key 2': 'value 2'}``

Dictionary methods:

- Get value from dictionary ``dict_name['key_name']'`` or ``dict_name.get('key_name')``
- Loop through the dict with:
```py
for k, v in dict_name.items():
   print(k, v) 
```

String methods:

- f-strings - inject variables into a string with curly braces ``print(f'Variable = {x}')``
- Combine iterable into string ``''.join(iterable)``

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

x = 7 // 3  # floor division (divide and round down to the nearest whole number)
# output: 2.333 but rounds down to 2
```

You can also use the math library in the python standard library to perform more complex mathematical functions.

[Math Standard Library Docs](https://docs.python.org/3/library/math.html)

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

```python
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
