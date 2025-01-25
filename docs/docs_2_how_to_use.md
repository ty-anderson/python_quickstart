
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
