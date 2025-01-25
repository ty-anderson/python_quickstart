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
