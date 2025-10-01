# Testing

Testing is a powerful way to catch any errors in your code, with code. Instead of 
trying to run your code and catch errors, testing libraries can help catch things
faster.

## pytest

``pytest`` is a 3rd party library, built on the standard library ``unittest``.

### Install

``pip install pytest`` or ``uv add pytest``

### Quickstart

In your project create a folder called ``test``. Add a test module for each 
module you want to test. Make sure to include the word "test" before
or after the name, like below.

```
- project
  - src
    - adapters
    - app
      - my_module.py
      - utils
      - tests
        - test_my_module.py
  - pyproject.toml
```

Inside the module you can add functions or classes/methods that do the testing.
Here is a simple example:

```python
# my_module.py

def add_numbers(*args):
    return sum(args)
```

```python
# test_my_module.py

from my_module import add_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
```

Once your tests are built, run ``pytest``. Pytest will search recursively for:

- All modules named ``test_*.py`` or ``*_test.py`` and then inside they look for...
- functions that start with ``test_``
- Classes with Test (that don't have an __init__)
- Methods inside those classes that start with ``test_``

Then run those tests.

### Strategy

It's best practice to write tests and run as you go. If you add new logic, create a test for it.
Otherwise you'll accumulate too much technical debt and it will be a big job to 
write tests for everything. Higher chance of missing something. 

### Commands

```bash
# run all tests
pytest

# run single test file
pytest tests/test_my_module.py

# run single test function
pytests tests/test_my_module.py::test_add_numbers
```
