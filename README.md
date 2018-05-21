# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

## Setup:
```shell
$ git clone https://github.com/francois-le-ko4la/docstring-to-markdown.git
$ cd docstring-to-markdown
$ make install
```

## Test:

This module has been tested and validated on Ubuntu 17.10/18.04.
```shell
$ make test
```

## Use:

Use the script:
```shell
$ export_docstring2md.py -h
usage: main.py [-h] [-v] -i INPUT [-o FILE] [-t FILE] [-r FILE] [-uml FILE]
               [--toc | --no-toc] [--private-def | --no-private-def]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

optional arguments:
  --toc                 Enable the table of contents (DEFAULT)
  --no-toc              Disable the table of contents
  --private-def         Show private objects
  --no-private-def      Don't show private objects

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

required arguments:
  -i INPUT, --input INPUT
                        Input file name

optional arguments:
  -o FILE, --output FILE
                        Output file
  -t FILE, --runtime FILE
                        Runtime file
  -r FILE, --requirements FILE
                        requirements.txt file
  -uml FILE, --uml-diagramm FILE
                        UML file (PNG)

Enjoy...
```

## Project structure

```
.
├── bin
│   └── export_docstring2md.py
├── docstring2md
│   ├── __about__.py
│   ├── __config__.py
│   ├── convmd.py
│   ├── doc2md.py
│   ├── file.py
│   ├── __init__.py
│   ├── main.py
│   ├── module.py
│   └── objdef.py
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pictures
│   ├── classes_docstring2md.png
│   └── packages_docstring2md.png
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── test_docstring2md.py
    ├── test_doctest.py
    └── test_pycodestyle.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Add-on : decorator
- [X] Add-on : class properties
- [X] Add-on : runtime & requirements
- [X] Add-on : toc
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Release

## License

This package is distributed under the [GPLv3 license](./LICENSE)### Runtime

```
python-3.6.x

```
### Requirements

```
setuptools>=36.2.7
pycodestyle>=2.3.1

```
### UML Diagram
![alt text](pictures/classes_docstring2md.png)

### Objects
[MyConst()](#myconst)<br />
[LineType()](#linetype)<br />
[PythonObjType()](#pythonobjtype)<br />
[Tag()](#tag)<br />
[ObjVisitor()](#objvisitor)<br />
[ObjVisitor.get_tree()](#objvisitorget_tree)<br />
[ObjVisitor.visit_Module()](#objvisitorvisit_module)<br />
[ObjVisitor.visit_ClassDef()](#objvisitorvisit_classdef)<br />
[ObjVisitor.visit_FunctionDef()](#objvisitorvisit_functiondef)<br />
[ConvMD()](#convmd)<br />
[ConvMD.repl_str()](#convmdrepl_str)<br />
[ConvMD.repl_str.tags_decorator()](#convmdrepl_strtags_decorator)<br />
[ConvMD.repl_str.tags_decorator.func_wrapper()](#convmdrepl_strtags_decoratorfunc_wrapper)<br />
[ConvMD.repl_beg_end()](#convmdrepl_beg_end)<br />
[ConvMD.repl_beg_end.tags_decorator()](#convmdrepl_beg_endtags_decorator)<br />
[ConvMD.repl_beg_end.tags_decorator.func_wrapper()](#convmdrepl_beg_endtags_decoratorfunc_wrapper)<br />
[ConvMD.add_tag()](#convmdadd_tag)<br />
[ConvMD.add_tag.tags_decorator()](#convmdadd_tagtags_decorator)<br />
[ConvMD.add_tag.tags_decorator.func_wrapper()](#convmdadd_tagtags_decoratorfunc_wrapper)<br />
[DocString2MD()](#docstring2md)<br />
[DocString2MD.import_module()](#docstring2mdimport_module)<br />
[DocString2MD.get_doc()](#docstring2mdget_doc)<br />
[PytFile()](#pytfile)<br />
[PytFile.filename()](#pytfilefilename)<br />
[PytFile.filename()](#pytfilefilename)<br />
[PytFile.exists()](#pytfileexists)<br />
[PytFile.read()](#pytfileread)<br />
[run()](#run)<br />
[ExtractPythonModule()](#extractpythonmodule)<br />
[ExtractPythonModule.module()](#extractpythonmodulemodule)<br />
[ExtractPythonModule.docstring()](#extractpythonmoduledocstring)<br />
[ExtractPythonModule.pkg_main_docstring()](#extractpythonmodulepkg_main_docstring)<br />
[ExtractPythonModule.toc()](#extractpythonmoduletoc)<br />
[ExtractPythonModule.ismodule()](#extractpythonmoduleismodule)<br />
[ExtractPythonModule.read()](#extractpythonmoduleread)<br />

#### MyConst()
```python
classe MyConst():
```

```
params 
```

#### LineType()
```python
classe LineType():
```

```
params 
```

#### PythonObjType()
```python
classe PythonObjType():
```

```
params 
```

#### Tag()
```python
classe Tag():
```

```
params 
```

#### ObjVisitor()
```python
classe ObjVisitor():
```

```
None
```

##### ObjVisitor.get_tree()
```python

def ObjVisitor.get_tree(self, source):
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_Module()
```python

def ObjVisitor.visit_Module(self, node):
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_ClassDef()
```python

def ObjVisitor.visit_ClassDef(self, node):
```
> <br />
> None<br />
> <br />
##### ObjVisitor.visit_FunctionDef()
```python

def ObjVisitor.visit_FunctionDef(self, node):
```
> <br />
> None<br />
> <br />
#### ConvMD()
```python
classe ConvMD(object):
```

```
Prepare MD string
```

##### ConvMD.repl_str()
```python

def ConvMD.repl_str(old_string, new_string):
```
> <br />
> Decorator - search & replace a string by another string<br />
> Example : replace space by a HTML tag.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  old_string (str): string to search<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  new_string (str): new string<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
###### ConvMD.repl_str.tags_decorator()
```python

def ConvMD.repl_str.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
####### ConvMD.repl_str.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.repl_str.tags_decorator.func_wrapper(*args, **kwargs):
```
> <br />
> wrapper <br />
> <br />
##### ConvMD.repl_beg_end()
```python

def ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag):
```
> <br />
> Decorator - replace the beggining and the end<br />
> <br />
> <b>Example:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  All new lines must be provided with a specific tag<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  > 'Line' <br /><br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_regexp (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  begin_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
###### ConvMD.repl_beg_end.tags_decorator()
```python

def ConvMD.repl_beg_end.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
####### ConvMD.repl_beg_end.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.repl_beg_end.tags_decorator.func_wrapper(*args, **kwargs):
```
> <br />
> wrapper <br />
> <br />
##### ConvMD.add_tag()
```python

def ConvMD.add_tag(begin_tag, end_tag):
```
> <br />
> Decorator - add a tag<br />
> <br />
> <b>Example:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ('__', '__') => __ TXT __<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  beg_tag (str)<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  end_tag (str)<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  decorated function<br />
> <br />
###### ConvMD.add_tag.tags_decorator()
```python

def ConvMD.add_tag.tags_decorator(func):
```
> <br />
> decorator <br />
> <br />
####### ConvMD.add_tag.tags_decorator.func_wrapper()
```python
@wraps(func)
def ConvMD.add_tag.tags_decorator.func_wrapper(self, *args):
```
> <br />
> wrapper <br />
> <br />
#### DocString2MD()
```python
classe DocString2MD(object):
```

```
Class DocString2MD : export Google docstring to MD File.

Use:
    >>> doc = DocString2MD("docstring2md")
    >>> doc.import_module()
    True
    >>> result = doc.get_doc()
    >>> result = result.split("\n")
    >>> print(result[0])
    # docstring2md
```

##### DocString2MD.import_module()
```python

def DocString2MD.import_module(self):
```
> <br />
> import all infos<br />
> <br />
##### DocString2MD.get_doc()
```python

def DocString2MD.get_doc(self):
```
> <br />
> Extract the doc<br />
> Returns self.__output or self.__writedoc<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  str: self.__output<br />
> <br />
#### PytFile()
```python
classe PytFile(object):
```

```
>>> data_file = PytFile("lorem")
Traceback (most recent call last):
...
OSError: File not found !
>>> data_file = PytFile(None)
>>> data_file.exists()
False
>>> fstab = PytFile("/etc/fstab")
>>> fstab.filename.stem
'fstab'
>>> fstab
/etc/fstab
>>> # pathlib to run the test everywhere
>>> import pathlib
>>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
>>> license = PytFile(path + "../LICENSE")
>>> license.filename.stem
'LICENSE'
>>> license.exists()
True
>>> #print(license.read())
```

##### PytFile.filename()
```python
@property
def PytFile.filename(self):
```
> <br />
> path to the module<br />
> <br />
##### PytFile.filename()
```python
@setter
def PytFile.filename(self, value):
```
> <br />
> Store the path<br />
> <br />
##### PytFile.exists()
```python

def PytFile.exists(self):
```
> <br />
> file exists<br />
> <br />
##### PytFile.read()
```python

def PytFile.read(self):
```
> <br />
> read the text<br />
> <br />
#### run()
```python

def run():
```
> <br />
> Main function<br />
> <br />
#### ExtractPythonModule()
```python
classe ExtractPythonModule(object):
```

```
Object in order to extract Python functions, classes....

Use:
    >>> mod = ExtractPythonModule("oups...")
    >>> mod.read()
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'oups'
    >>> mod = ExtractPythonModule("json")
    >>> mod.read()
    >>> # print(mod.pkg_main_docstring)
    >>> # print(mod.docstring)
```

##### ExtractPythonModule.module()
```python
@property
def ExtractPythonModule.module(self):
```
> <br />
> None<br />
> <br />
##### ExtractPythonModule.docstring()
```python
@property
def ExtractPythonModule.docstring(self):
```
> <br />
> None<br />
> <br />
##### ExtractPythonModule.pkg_main_docstring()
```python
@property
def ExtractPythonModule.pkg_main_docstring(self):
```
> <br />
> None<br />
> <br />
##### ExtractPythonModule.toc()
```python
@property
def ExtractPythonModule.toc(self):
```
> <br />
> None<br />
> <br />
##### ExtractPythonModule.ismodule()
```python

def ExtractPythonModule.ismodule(self):
```
> <br />
> None<br />
> <br />
##### ExtractPythonModule.read()
```python

def ExtractPythonModule.read(self):
```
> <br />
> None<br />
> <br />

