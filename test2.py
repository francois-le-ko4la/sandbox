#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

____                 _        _             ____  __  __ ____
|  _ \  ___   ___ ___| |_ _ __(_)_ __   __ _|___ \|  \/  |  _ \
| | | |/ _ \ / __/ __| __| '__| | '_ \ / _` | __) | |\/| | | | |
| |_| | (_) | (__\__ \ |_| |  | | | | | (_| |/ __/| |  | | |_| |
|____/ \___/ \___|___/\__|_|  |_|_| |_|\__, |_____|_|  |_|____/
                                       |___/

"""
import os
import sys
import inspect
import importlib.util
from functools import wraps
import re

class ConvertMD(object):
    def replace_string(old_string, new_string):
        """
        Decorator - search & replace a string by another string
        Example : replace space by a HTML tag.

        Args:
            old_string (str): string to search
            new_string (str): new string

        Returns:
            decorated function

        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return (func(*args, **kwargs)).replace(old_string, new_string)
            return func_wrapper
        return tags_decorator

    def replace_beginning_and_end(begin_regexp, end_regexp,
                                    begin_tag, end_tag):
        """
        Decorator - replace the beggining and the end

        Example:
            All new lines must be provided with a specific tag
            > 'Line' <br />

        Args:
            begin_regexp (str)
            end_regexp (str)
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(*args, **kwargs):
                """ wrapper """
                return re.sub(
                    begin_regexp+'(.*)'+end_regexp,
                    begin_tag + r'\1' + end_tag,
                    func(*args, **kwargs),
                    flags=re.MULTILINE
                    )
            return func_wrapper
        return tags_decorator

    def md_tag(begin_tag, end_tag):
        """
        Decorator - add a tag

        Example:
            ('__', '__') => __ TXT __

        Args:
            begin_tag (str)
            end_tag (str)

        Returns:
            decorated function
        """
        def tags_decorator(func):
            """ decorator """
            @wraps(func)
            def func_wrapper(self, *args):
                """ wrapper """
                return "{0}{1}{2}".format(
                    begin_tag, func(self, *args), end_tag)
            return func_wrapper
        return tags_decorator


class TitleObj(object):
    def __init__(self, value, level):
        self.value = value
        self.level = level
    def __repr__(self):
        return "{} {}".format("#"*(self.level+2),  self.value)
    def __str__(self):
        return repr(self)

class PythonDefinitionObj(object):
    def __init__(self, value):
        self.value = value

    @ConvertMD.md_tag("\n````python\n", "\n````\n\n")
    def __repr__(self):
        return self.value
    def __str__(self):
        return repr(self)

class DocStringObj(object):
    def __init__(self, value):
        self.value = value

    @ConvertMD.replace_beginning_and_end('^', '$', '> ', '<br />')
    @ConvertMD.replace_beginning_and_end('^', ':$', '<b>', ':</b>')
    @ConvertMD.replace_string('    ', '&nbsp;' * 15 + '  ')
    @ConvertMD.md_tag("\n", "\n")
    def __repr__(self):
        return self.value
    def __str__(self):
        return repr(self)

class MembersObj(object):
    def __init__(self):
        self.__members = dict()
    def __repr__(self):
        return str(self.__members)
    def __str__(self):
        return repr(self)
    def __setitem__(self, index, value):
        self.__members[index]=value
    def __getitem__(self, index):
        return self.__members[index]
    def __len__(self):
        return len(self.__members)
    def sortkeys(self):
        return sorted(self.__members)
    def items(self):
        return self.__members

        
class PythonObj(object):
    def __init__(self, name, full_name, docstring, level):
        self.__title = TitleObj(name, level)
        self.__definition = PythonDefinitionObj(full_name)
        self.__docstring = DocStringObj(docstring)
        self.members = MembersObj()     
    def __repr__(self):
        return "\n\n{}\n{}\n{}".format(self.__title, self.__definition, self.__docstring)
    def __str__(self):
        return repr(self)


class ModuleObj(PythonObj):
    def __init__(self, name, full_name, docstring, level=0):
        PythonObj.__init__(self, name, full_name, docstring, level)
        self.__module_docstring = docstring

    def __repr__(self):
        return "{}\n## Dev docstring\n".format(self.__module_docstring)

    def getallstr(self, member=None):
        if member is None:
            member=self
        output = str(member)
        for idmember in member.members.sortkeys():
            output += self.getallstr(member.members[idmember])
        return output


class ExtractPythonModule(object):
    def __init__(self, module_name):
        sys.path.append(os.getcwd())
        self.__module_name = module_name
        self.__module = None
        self.__module_spec = None
        self.module = None
    
    def __check_module(func):
        """
        Decorator - Checks if module can be imported.
        Updates self.__module_spec in order to import the module.

        Args:
            None

        Retuns:
            bool: The return value. True for success, False otherwise.

        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            """ wrapper """
            try:
                self.__module_spec = importlib.util.find_spec(
                    self.__module_name)
                if self.__module_spec is None:
                    return False
            except Exception as e:
                print("This file is not a module.")
                return False
            return func(self, *args, **kwargs)
        return wrapper

    @__check_module
    def import_module(self):
        """
        Check module
        Import the module via the passed in module specification
        Returns the newly imported module and updates attributes self.__module

        Args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            self.__module = importlib.util.module_from_spec(self.__module_spec)
            self.__module_spec.loader.exec_module(self.__module)
        except Exception as e:
            print("Import error")
            return False
        return True
        
    def extract(self):

        self.module = ModuleObj(self.__module_name, self.__module_name, inspect.getdoc(self.__module))
        self.__extract(self.module, self.__module)
        
        
    def __extract(self, my_pythonobj, inspectmembers, level=0):
        """
        Inspects functions in a moddule.
            doc = inspect.getdoc(member[1])
            classe : "{0}()".format(str(member[0]))
            fonction : "{0}{1}".format((str(member[1]).split(" "))[1],
                                   str(inspect.signature(member[1])))
        Args:
            item (obj): inspect obect
            class_member (bool): False by default / if def in class -> True

        Returns:
            None
        """
        if level >= 2:
            return

            
        level += 1
        for member in inspect.getmembers(inspectmembers):
            if inspect.isclass(member[1]) and member[0] != "__class__":
                name = "{0}()".format(str(member[0]))
                full_name = "class {0}:".format(name)
                docstring = inspect.getdoc(member[1])
                new_pythonobj = PythonObj(name, full_name, docstring, level)
                my_pythonobj.members[name] = new_pythonobj
                self.__extract(new_pythonobj, member[1], level)
            if inspect.isfunction(member[1]):
                name = "{0}{1}".format((str(member[1]).split(" "))[1],
                                   str(inspect.signature(member[1])))
                full_name = "def {0}:".format(name)
                docstring = inspect.getdoc(member[1])
                new_pythonobj = PythonObj(name, full_name, docstring, level)
                my_pythonobj.members[name] = new_pythonobj


class DocString2MD(object):

    """
    Class DocString2MD : export Google docstring to MD File.
    """

    def __init__(self, module_name, export_file=None):
        """Init the class
        This function define default attributs.

        Args:
            module_name (str): /path/to/the/module/
            export_file (str): /path/to/the/doc/file - None by default

        Attributes:
            self.__module_name
            self.__module
            self.__module_spec
            self.__output
            self.__first_member

        Returns:
            obj

        """
        self.__export_file = export_file
        self.__my_module = ExtractPythonModule(module_name)
        self.__output = ""

    def import_module(self):
        self.__my_module.import_module()
        if self.__my_module.import_module():
            self.__output = self.__my_module.extract()

    def get_doc(self):
        """

        Extract the doc
        Returns self.__output or self.__writedoc

        Args:
            None

        Returns:
            str: self.__output
        """

        if self.__exportfile is None:
            return self.__output
        else:
            return self.__writedoc()


    def __writedoc(self):
        """
        Writes the content in the file

        args:
            None

        Returns:
            bool: The return value. True for success, False otherwise.

        """
        try:
            exportfile = open(self.__exportfile, "w")
            try:
                exportfile.write(self.__output)
            finally:
                exportfile.close()
        except IOError:
            print("Unable to create {0} on disk.".format(self.__exportfile))
            return False

        return True

				
test = ExtractPythonModule("docstring2md")
if test.import_module():
    test.extract()
    print(test.module.getallstr())
