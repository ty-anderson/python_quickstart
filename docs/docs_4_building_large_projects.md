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
