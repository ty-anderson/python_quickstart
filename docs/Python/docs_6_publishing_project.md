# Publishing a Project

You can create your own python library and publish it to PyPI. First you'll need to create an account and download
your API keys. Once you have those established, you can create your project and then:

Super summary:

1. Create the pyproject.toml file and fill out the fields 
2. run ``python -m build ``
3. use twine to send to pypi.


## With UV

```toml
[project]
name = "wws-api"
version = "0.1.0"
description = "Simplifies the process for calling the Workday Web Services API asyncronously."
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
   "aiohttp>=3.12.15",
   "lxml>=6.0.0",
   "pyarrow>=21.0.0",
   "xmltodict>=0.14.2",
]

[build-system]
requires = ["uv_build>=0.8.7,<0.9.0"]
build-backend = "uv_build"

[tool.uv.build-backend]
# module name is the normalized project name (dash -> underscore)
module-name = "wws_api"
# module root "" = repo root (i.e., not using src/)
module-root = ""

[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Build wheel file with uv build system:
``uv build``

Publish project to test PyPI
``uv publish --index testpypi --token <api token>``

Publish project to production PyPI
``uv publish --token <api token>``


## Without UV

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
   ```
   pip install --upgrade build
   pip install twine
   ```
4. Run the build - ``python -m build``
5. Send to PyPI test - ``twine upload --repository testpypi dist/*``
6. Send to PyPI - ``twine upload dist/*``

Make sure your build dependencies are not stored in your project dependencies.

Another TOML file might look like this:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "py_simple_sharepoint"  # actual name that will get used for pip install.
version = "0.1.1"  # anytime you submit an update to PyPI, you must change the version.
description = "A SharePoint file management tool for python programs."
readme = "README.md"
requires-python = ">=3.10"
dependencies = [  # package dependencies, does install when pip installed
    "office365-rest-python-client>=2.6.2",
]

[project.optional-dependencies]  # build dependencies (does not install when pip installed)
dev = [
    "build",
    "twine"
]
```
	
https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files

There are also new tools coming out such as poetry and uv. 
The community has started to heavily embrace [UV](https://astral.sh/blog/uv) due to its speed and tooling.
