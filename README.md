# docstring2md
## Description:

This package Export Google DocString to Markdown from Python module.

The following files comprise the `docstring2md` package:
* `LICENSE`: The license file. `docstring2md` is released under the terms of
the GNU General Public License (GPL), version 3.
* `README.md`: This readme file.
* `Makefile`: Generic management tasks.
* `setup.py`: Package and distribution management.
* `setup.cfg`: The setuptools setup file.

The package contents itself are in the `docstring2md` directory:
* `__init__.py` Initialization file for the Python package.
* `docstring2md/docstring2md.py`: The code of interest.

The script is in the `bin` directory:
* `export_docstring2md.py`: The script to run

## Setup:
```shell
git clone https://github.com/francois-le-ko4la/docstring2md.git
cd config-from-json
make install
```

## Test:

This module has been tested and validated on Ubuntu.
```shell
make test
```

## Use:

Use the script:
```shell
$ export_docstring2md.py -h
usage: export_docstring2md.py [-h] [-v] -i INPUT [-o FILE] [-t FILE] [-r FILE]

This script is provided by docstring2md package.
It exports google docstrings from python module to a Markdown file in order to
generate README.

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

Enjoy...
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
- [ ] Write Doc/stringdoc
- [X] Run PEP8 validation
- [ ] Clean & last check
- [ ] Release

## Note:
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## Dev notes
[ConvMD()](#92dd76e2526bcd318d24dd06abc492ddd9aa060a)
[ConvMD.add_tag(begin_tag, end_tag)](#a340e0fb29090ceda39c781d0287b409a6d506b2)
[ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag)](#dd0d60e32851a831bb2a9357ccf94a0aa0775ac9)
[ConvMD.repl_str(old_string, new_string)](#93e1829c90b94cb63174a733726fc9158da243b1)
[DocString2MD()](#1a1bc9270ef9889e3e1ff955ad391cd75f9ceb3e)
[@Property: module_name](#efca858446dedd94f56d684293129b4b92e514db)
[DocString2MD.__init__(self, module_name, export_file=None, runtime_file=None, requirements_file=None, uml_file=None)](#49efdc7fb225b82ba060ca1b356aad67e5a0c1e2)
[DocString2MD.__writedoc(self)](#4ecf66e6c1632fbe76c05e842b961fc9b7434836)
[DocString2MD.get_doc(self)](#8b167cfe759596ebe08fe184e4143d650b9948ea)
[DocString2MD.import_module(self)](#ab424550d18ae8bae0a1ce66f4d41e8ac19750a9)
[DocStringObj()](#8daf5988f2974abc7e6394d3c745d44ba43fd5c7)
[@Property: value](#6f76a1931dcc00e9d3c07f0346c22a49bb507bc8)
[DocStringObj.__init__(self, value)](#87af9694b9afa3eaf10e3cb6657f153ee4209b3c)
[DocStringObj.__repr__(self)](#ac39c86c895b381c7620540f1b29b571cd8d58e0)
[DocStringObj.__str__(self)](#b9282981f37b00239f3eff16d9da3412466c00ff)
[ExtractPythonModule()](#2498540c5ed9310facae548d4ba9cd71b162470d)
[ExtractPythonModule.__check_module(func)](#c215001384acf81c10359befa3395fa69ce35a55)
[ExtractPythonModule.__extract(self, my_pythonobj, inspectmembers, level=0, decorator=None)](#359967e59a746508900585f22f68bc1a99fa3f08)
[ExtractPythonModule.__extractdecorator(self, member)](#c50284af2411ebfdec40bcd172207e4b340f2023)
[ExtractPythonModule.__extractproperties(self, my_pythonobj, inspectmembers, level, decorator, cls_name)](#27b22c82207664254f720cc931426a77bf3b1bf5)
[ExtractPythonModule.__findinline(self, line, search_item)](#c5f653d758516a2dd23a12d8a4efef8324d9b062)
[ExtractPythonModule.__init__(self, module_name)](#aec9f32e063906787c5906d4fb3b7a3ad54d9dd0)
[ExtractPythonModule.__linetype(self, line)](#0305ba5a01d7af75a39a63a952e6532d836d0830)
[ExtractPythonModule.extract(self)](#a7312d4fccc4e5885ad9dbe26bda903340444366)
[ExtractPythonModule.import_module(self)](#08f40447cb4474fe9b892c10ad6b4c88ee0e341f)
[LineType()](#d65fbaed25ebe482588b51e3000c5d65f7f0b6a9)
[MembersObj()](#393a95ae46f991e26e9ef12082af0ceeec81c025)
[MembersObj.__getitem__(self, index)](#5bb035ab7a37d6fb4ac0d63feb7ae1f0a91947a8)
[MembersObj.__init__(self)](#f8edcec0fb8181a28713b55f08a59a4881bbb9a7)
[MembersObj.__len__(self)](#21079dc8d29c6d783d26b1d2426a62f5a1af0c0b)
[MembersObj.__repr__(self)](#8a055d95e4aac47645e9e5e966536ce1f1a7c3d5)
[MembersObj.__setitem__(self, index, value)](#bc654d0b0ccbd43dbc3e3ef5731d9dfd4ab4b98a)
[MembersObj.__str__(self)](#d1491d742bd8ce5f9f09df77cfc00f9809f51ba2)
[MembersObj.items(self)](#4bbbf05855d621ad0fcedef8da6c57ffd4a0396e)
[MembersObj.sortkeys(self)](#dd169b053302842c9d4e56e149472595afde1411)
[ModuleObj()](#ad7e199936a9f0900d22f9146d9c6122e07bad8f)
[ModuleObj.__init__(self, name, full_name, docstring, level=0)](#2d22ce06ca9358b7c3edffc10f0bdee205d1911c)
[ModuleObj.__repr__(self)](#8b175a86b227b43e4afc2c119f380c060ce264b3)
[ModuleObj.__str__(self)](#1c7845109b61b62b699dd9f1423f808d757410a8)
[ModuleObj.getallstr(self, member=None)](#7fbcc4146a8608bdfecd6c87e4a940598c913196)
[ModuleObj.gettoc(self, member=None)](#18e852be5041c36903e5fd149222a046dd707ff6)
[PythonObj.getlink(self)](#689ea8cf936d2e124206fa9cb72dc92c8c24595c)
[MyConst()](#e291187727c46a2a7059bc2ccf1382ddbbad7a35)
[PythonDefinitionObj()](#f8db111c5a1f08313ce3428f1d33236b5e45e5aa)
[@Property: value](#6f76a1931dcc00e9d3c07f0346c22a49bb507bc8)
[PythonDefinitionObj.__init__(self, value)](#f92b4947fd1e614b2dcab47aa233379b58ccdefe)
[PythonDefinitionObj.__repr__(self)](#bbf1d86197e458205810c7b3ee145de586016b66)
[PythonDefinitionObj.__str__(self)](#d178bfa378031ea38a69d09ccb07288e60c4796f)
[PythonObj()](#780f202252b8da2c8bc85f829e382aedbac554de)
[PythonObj.__init__(self, name, full_name, docstring, level)](#32fa5e8d0fc098c6b016d2b3f8456f79f9d19edd)
[PythonObj.__repr__(self)](#42878b1f331162ae5974baefb33db40a796468d9)
[PythonObj.__str__(self)](#d073303de05e300512174a05689ceeafb8aae5df)
[PythonObj.getlink(self)](#689ea8cf936d2e124206fa9cb72dc92c8c24595c)
[ReadFile()](#99b7f0b4d121c98a3c7fd7ceb688997305523603)
[@Property: filename](#4419219f9e4f4d1f83af7a9364d51e4c51a9cccf)
[ReadFile.__init__(self, filename)](#c8e5cccc0708cd0536dd47de06263f45c8e2ecb2)
[ReadFile.__repr__(self)](#32b969e1552a6e1cab80c5f07855d7400c34646c)
[ReadFile.__str__(self)](#8a8aa432137a04f8144a93d22b9c61b774a3a2e1)
[ReadFile.get(self)](#e5f2319ad83767af70e8fed672c4f7680b176f18)
[ReadFile.isdefined(self)](#55921ecc8e7838c202ccc204e430a0932d1edd66)
[Tag()](#fcd5f72200e4464c35485721a8a2b0e13174c384)
[TitleObj()](#980cf4e5d783b767ca441cbf071099d0f16f4d1a)
[@Property: level](#011984f79f02e5c60873b19559bc142571679ea2)
[@Property: title](#8d95c4c692e61b9ab4b1f02ac0758af0b1b9bc45)
[TitleObj.__init__(self, title, level)](#21f2d461732e11dbfdaa658a6b6d5cc61c999328)
[TitleObj.__repr__(self)](#610a9fe9960395f8ac80cb52ffc9b35d384c5502)
[TitleObj.__str__(self)](#208f8142eb3011693506258da1362ee3b2d81c7b)
[TitleObj.getanchor(self)](#3ae67beddf00ea4d0c3dd55d0a6e32b0807ffe00)
[wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))](#4ab498195731ad085c678a9e05353f0d72327513)

### <a id="92dd76e2526bcd318d24dd06abc492ddd9aa060a"></a> ConvMD()

```python
class ConvMD(object):
```

> <br />
> Prepare MD string<br />
> <br />
#### <a id="a340e0fb29090ceda39c781d0287b409a6d506b2"></a> ConvMD.add_tag(begin_tag, end_tag)

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
#### <a id="dd0d60e32851a831bb2a9357ccf94a0aa0775ac9"></a> ConvMD.repl_beg_end(begin_regexp, end_regexp, begin_tag, end_tag)

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
#### <a id="93e1829c90b94cb63174a733726fc9158da243b1"></a> ConvMD.repl_str(old_string, new_string)

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
### <a id="1a1bc9270ef9889e3e1ff955ad391cd75f9ceb3e"></a> DocString2MD()

```python
class DocString2MD(object):
```

> <br />
> Class DocString2MD : export Google docstring to MD File.<br />
> <br />
#### <a id="efca858446dedd94f56d684293129b4b92e514db"></a> @Property: module_name

```python
@property
def DocString2MD.module_name(self):
@module_name.setter
def DocString2MD.module_name(self, module_name):

```

> <br />
> @Property<br />
> <br />
#### <a id="49efdc7fb225b82ba060ca1b356aad67e5a0c1e2"></a> DocString2MD.__init__(self, module_name, export_file=None, runtime_file=None, requirements_file=None, uml_file=None)

```python
def DocString2MD.__init__(self, module_name, export_file=None, runtime_file=None, requirements_file=None, uml_file=None):
```

> <br />
> Init the class<br />
> This function define default attributs.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  module_name (str): /path/to/the/module/<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  export_file (str): /path/to/the/doc/file - None by default<br />
> <br />
> <b>Attributes:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__export_file (str): /path/to/the/doc/file - None by default<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__my_module<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  self.__output<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  obj<br />
> <br />
#### <a id="4ecf66e6c1632fbe76c05e842b961fc9b7434836"></a> DocString2MD.__writedoc(self)

```python
def DocString2MD.__writedoc(self):
```

> <br />
> Writes the content in the file<br />
> <br />
> <b>args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />
#### <a id="8b167cfe759596ebe08fe184e4143d650b9948ea"></a> DocString2MD.get_doc(self)

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
#### <a id="ab424550d18ae8bae0a1ce66f4d41e8ac19750a9"></a> DocString2MD.import_module(self)

```python
def DocString2MD.import_module(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="8daf5988f2974abc7e6394d3c745d44ba43fd5c7"></a> DocStringObj()

```python
class DocStringObj(object):
```

> <br />
> String to store and prepare the docstring.<br />
> This object will become an attribute.<br />
> <br />
#### <a id="6f76a1931dcc00e9d3c07f0346c22a49bb507bc8"></a> @Property: value

```python
@property
def DocStringObj.value(self):
@value.setter
def DocStringObj.value(self, value):

```

> <br />
> @Property<br />
> <br />
#### <a id="87af9694b9afa3eaf10e3cb6657f153ee4209b3c"></a> DocStringObj.__init__(self, value)

```python
def DocStringObj.__init__(self, value):
```

> <br />
> Store the docstring<br />
> <br />
#### <a id="ac39c86c895b381c7620540f1b29b571cd8d58e0"></a> DocStringObj.__repr__(self)

```python
@ConvMD.repl_beg_end(Tag.beg_str, Tag.end_str, Tag.quote, Tag.html_cr)
@ConvMD.repl_beg_end(Tag.beg_str, Tag.end_strh, Tag.beg_b, Tag.end_bh)
@ConvMD.repl_str(Tag.tab, Tag.html_tab)
@ConvMD.add_tag(Tag.cr, Tag.cr)
def DocStringObj.__repr__(self):
```

> <br />
> Provide the new docstring with MD tags.<br />
> <br />
#### <a id="b9282981f37b00239f3eff16d9da3412466c00ff"></a> DocStringObj.__str__(self)

```python
def DocStringObj.__str__(self):
```

> <br />
> Call repr<br />
> <br />
### <a id="2498540c5ed9310facae548d4ba9cd71b162470d"></a> ExtractPythonModule()

```python
class ExtractPythonModule(object):
```

> <br />
> Object in order to extract Python functions, classes....<br />
> <br />
#### <a id="c215001384acf81c10359befa3395fa69ce35a55"></a> ExtractPythonModule.__check_module(func)

```python
def ExtractPythonModule.__check_module(func):
```

> <br />
> Decorator - Checks if module can be imported.<br />
> Updates self.__module_spec in order to import the module.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Retuns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />
#### <a id="359967e59a746508900585f22f68bc1a99fa3f08"></a> ExtractPythonModule.__extract(self, my_pythonobj, inspectmembers, level=0, decorator=None)

```python
def ExtractPythonModule.__extract(self, my_pythonobj, inspectmembers, level=0, decorator=None):
```

> <br />
> Inspects classes & functions in a moddule.<br />
> Store information in a PythonObj object.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  inspectmembers (obj): inspect obect<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  my_pythonobj (PythonObj): object to define a Python member<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### <a id="c50284af2411ebfdec40bcd172207e4b340f2023"></a> ExtractPythonModule.__extractdecorator(self, member)

```python
def ExtractPythonModule.__extractdecorator(self, member):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="27b22c82207664254f720cc931426a77bf3b1bf5"></a> ExtractPythonModule.__extractproperties(self, my_pythonobj, inspectmembers, level, decorator, cls_name)

```python
def ExtractPythonModule.__extractproperties(self, my_pythonobj, inspectmembers, level, decorator, cls_name):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="c5f653d758516a2dd23a12d8a4efef8324d9b062"></a> ExtractPythonModule.__findinline(self, line, search_item)

```python
def ExtractPythonModule.__findinline(self, line, search_item):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="aec9f32e063906787c5906d4fb3b7a3ad54d9dd0"></a> ExtractPythonModule.__init__(self, module_name)

```python
def ExtractPythonModule.__init__(self, module_name):
```

> <br />
> Init<br />
> <br />
#### <a id="0305ba5a01d7af75a39a63a952e6532d836d0830"></a> ExtractPythonModule.__linetype(self, line)

```python
def ExtractPythonModule.__linetype(self, line):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="a7312d4fccc4e5885ad9dbe26bda903340444366"></a> ExtractPythonModule.extract(self)

```python
def ExtractPythonModule.extract(self):
```

> <br />
> Defines module object and extracts all members.<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
#### <a id="08f40447cb4474fe9b892c10ad6b4c88ee0e341f"></a> ExtractPythonModule.import_module(self)

```python
@__check_module
def ExtractPythonModule.import_module(self):
```

> <br />
> Check module<br />
> Import the module via the passed in module specification<br />
> Returns the newly imported module and updates attributes self.__module<br />
> <br />
> <b>Args:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  None<br />
> <br />
> <b>Returns:</b><br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  bool: The return value. True for success, False otherwise.<br />
> <br />
### <a id="d65fbaed25ebe482588b51e3000c5d65f7f0b6a9"></a> LineType()

```python
class LineType:
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="393a95ae46f991e26e9ef12082af0ceeec81c025"></a> MembersObj()

```python
class MembersObj(object):
```

> <br />
> Dict() to store a python object's members.<br />
> This object will become an attribute.<br />
> <br />
#### <a id="5bb035ab7a37d6fb4ac0d63feb7ae1f0a91947a8"></a> MembersObj.__getitem__(self, index)

```python
def MembersObj.__getitem__(self, index):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="f8edcec0fb8181a28713b55f08a59a4881bbb9a7"></a> MembersObj.__init__(self)

```python
def MembersObj.__init__(self):
```

> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### <a id="21079dc8d29c6d783d26b1d2426a62f5a1af0c0b"></a> MembersObj.__len__(self)

```python
def MembersObj.__len__(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="8a055d95e4aac47645e9e5e966536ce1f1a7c3d5"></a> MembersObj.__repr__(self)

```python
def MembersObj.__repr__(self):
```

> <br />
> Return repr(self).<br />
> <br />
#### <a id="bc654d0b0ccbd43dbc3e3ef5731d9dfd4ab4b98a"></a> MembersObj.__setitem__(self, index, value)

```python
def MembersObj.__setitem__(self, index, value):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="d1491d742bd8ce5f9f09df77cfc00f9809f51ba2"></a> MembersObj.__str__(self)

```python
def MembersObj.__str__(self):
```

> <br />
> Return str(self).<br />
> <br />
#### <a id="4bbbf05855d621ad0fcedef8da6c57ffd4a0396e"></a> MembersObj.items(self)

```python
def MembersObj.items(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="dd169b053302842c9d4e56e149472595afde1411"></a> MembersObj.sortkeys(self)

```python
def MembersObj.sortkeys(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="ad7e199936a9f0900d22f9146d9c6122e07bad8f"></a> ModuleObj()

```python
class ModuleObj(PythonObj):
```

> <br />
> Class in order to register module informations<br />
> __str__ is used to export with MD format.<br />
> <br />
#### <a id="2d22ce06ca9358b7c3edffc10f0bdee205d1911c"></a> ModuleObj.__init__(self, name, full_name, docstring, level=0)

```python
def ModuleObj.__init__(self, name, full_name, docstring, level=0):
```

> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### <a id="8b175a86b227b43e4afc2c119f380c060ce264b3"></a> ModuleObj.__repr__(self)

```python
def ModuleObj.__repr__(self):
```

> <br />
> Return repr(self).<br />
> <br />
#### <a id="1c7845109b61b62b699dd9f1423f808d757410a8"></a> ModuleObj.__str__(self)

```python
def ModuleObj.__str__(self):
```

> <br />
> Return str(self).<br />
> <br />
#### <a id="7fbcc4146a8608bdfecd6c87e4a940598c913196"></a> ModuleObj.getallstr(self, member=None)

```python
def ModuleObj.getallstr(self, member=None):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="18e852be5041c36903e5fd149222a046dd707ff6"></a> ModuleObj.gettoc(self, member=None)

```python
def ModuleObj.gettoc(self, member=None):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="689ea8cf936d2e124206fa9cb72dc92c8c24595c"></a> PythonObj.getlink(self)

```python
def PythonObj.getlink(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="e291187727c46a2a7059bc2ccf1382ddbbad7a35"></a> MyConst()

```python
class MyConst:
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="f8db111c5a1f08313ce3428f1d33236b5e45e5aa"></a> PythonDefinitionObj()

```python
class PythonDefinitionObj(object):
```

> <br />
> <b>String so store and prepare the object definition:</b><br />
> Example : def function_name(*args)<br />
> This object will become an attribute.<br />
> <br />
#### <a id="6f76a1931dcc00e9d3c07f0346c22a49bb507bc8"></a> @Property: value

```python
@property
def PythonDefinitionObj.value(self):
@value.setter
def PythonDefinitionObj.value(self, value):

```

> <br />
> @Property<br />
> <br />
#### <a id="f92b4947fd1e614b2dcab47aa233379b58ccdefe"></a> PythonDefinitionObj.__init__(self, value)

```python
def PythonDefinitionObj.__init__(self, value):
```

> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### <a id="bbf1d86197e458205810c7b3ee145de586016b66"></a> PythonDefinitionObj.__repr__(self)

```python
@ConvMD.add_tag(Tag.beg_py, Tag.end_py)
def PythonDefinitionObj.__repr__(self):
```

> <br />
> Provide the definition string with MD tags.<br />
> <br />
#### <a id="d178bfa378031ea38a69d09ccb07288e60c4796f"></a> PythonDefinitionObj.__str__(self)

```python
def PythonDefinitionObj.__str__(self):
```

> <br />
> Call repr<br />
> <br />
### <a id="780f202252b8da2c8bc85f829e382aedbac554de"></a> PythonObj()

```python
class PythonObj(object):
```

> <br />
> Class in order to register object informations<br />
> __str__ is used to export with MD format.<br />
> <br />
#### <a id="32fa5e8d0fc098c6b016d2b3f8456f79f9d19edd"></a> PythonObj.__init__(self, name, full_name, docstring, level)

```python
def PythonObj.__init__(self, name, full_name, docstring, level):
```

> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### <a id="42878b1f331162ae5974baefb33db40a796468d9"></a> PythonObj.__repr__(self)

```python
def PythonObj.__repr__(self):
```

> <br />
> Return repr(self).<br />
> <br />
#### <a id="d073303de05e300512174a05689ceeafb8aae5df"></a> PythonObj.__str__(self)

```python
def PythonObj.__str__(self):
```

> <br />
> Return str(self).<br />
> <br />
#### <a id="689ea8cf936d2e124206fa9cb72dc92c8c24595c"></a> PythonObj.getlink(self)

```python
def PythonObj.getlink(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="99b7f0b4d121c98a3c7fd7ceb688997305523603"></a> ReadFile()

```python
class ReadFile(object):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
#### <a id="4419219f9e4f4d1f83af7a9364d51e4c51a9cccf"></a> @Property: filename

```python
@property
def ReadFile.filename(self):
@filename.setter
def ReadFile.filename(self, filename):

```

> <br />
> @Property<br />
> <br />
#### <a id="c8e5cccc0708cd0536dd47de06263f45c8e2ecb2"></a> ReadFile.__init__(self, filename)

```python
def ReadFile.__init__(self, filename):
```

> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
#### <a id="32b969e1552a6e1cab80c5f07855d7400c34646c"></a> ReadFile.__repr__(self)

```python
def ReadFile.__repr__(self):
```

> <br />
> Return repr(self).<br />
> <br />
#### <a id="8a8aa432137a04f8144a93d22b9c61b774a3a2e1"></a> ReadFile.__str__(self)

```python
def ReadFile.__str__(self):
```

> <br />
> Return str(self).<br />
> <br />
#### <a id="e5f2319ad83767af70e8fed672c4f7680b176f18"></a> ReadFile.get(self)

```python
def ReadFile.get(self):
```

> <br />
> open & read the file<br />
> Returns the content<br />
> <br />
#### <a id="55921ecc8e7838c202ccc204e430a0932d1edd66"></a> ReadFile.isdefined(self)

```python
def ReadFile.isdefined(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="fcd5f72200e4464c35485721a8a2b0e13174c384"></a> Tag()

```python
class Tag:
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="980cf4e5d783b767ca441cbf071099d0f16f4d1a"></a> TitleObj()

```python
class TitleObj(object):
```

> <br />
> String to store and prepare MD title<br />
> This object will become an attribute.<br />
> <br />
#### <a id="011984f79f02e5c60873b19559bc142571679ea2"></a> @Property: level

```python
@property
def TitleObj.level(self):
@level.setter
def TitleObj.level(self, level):

```

> <br />
> @Property<br />
> <br />
#### <a id="8d95c4c692e61b9ab4b1f02ac0758af0b1b9bc45"></a> @Property: title

```python
@property
def TitleObj.title(self):
@title.setter
def TitleObj.title(self, title):

```

> <br />
> @Property<br />
> <br />
#### <a id="21f2d461732e11dbfdaa658a6b6d5cc61c999328"></a> TitleObj.__init__(self, title, level)

```python
def TitleObj.__init__(self, title, level):
```

> <br />
> Init => store the sting in value and level (H1/H2/H3/...)<br />
> <br />
#### <a id="610a9fe9960395f8ac80cb52ffc9b35d384c5502"></a> TitleObj.__repr__(self)

```python
def TitleObj.__repr__(self):
```

> <br />
> Provide the MD string according to the level<br />
> <br />
#### <a id="208f8142eb3011693506258da1362ee3b2d81c7b"></a> TitleObj.__str__(self)

```python
def TitleObj.__str__(self):
```

> <br />
> Return str(self).<br />
> <br />
#### <a id="3ae67beddf00ea4d0c3dd55d0a6e32b0807ffe00"></a> TitleObj.getanchor(self)

```python
def TitleObj.getanchor(self):
```

> <br />
> <b>- docstring empty -</b><br />
> <br />
### <a id="4ab498195731ad085c678a9e05353f0d72327513"></a> wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))

```python
def wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',)):
```

> <br />
> Decorator factory to apply update_wrapper() to a wrapper function<br />
> <br />
> Returns a decorator that invokes update_wrapper() with the decorated<br />
> function as the wrapper argument and the arguments to wraps() as the<br />
> remaining arguments. Default arguments are as for update_wrapper().<br />
> This is a convenience function to simplify applying partial() to<br />
> update_wrapper().<br />
> <br />
--- 0.058852434158325195 seconds ---
