# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _MyString
else:
    import _MyString

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class MyString(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _MyString.MyString_swiginit(self, _MyString.new_MyString(*args))
    __swig_destroy__ = _MyString.delete_MyString

    def __add__(self, *args):
        return _MyString.MyString___add__(self, *args)

    def __iadd__(self, *args):
        return _MyString.MyString___iadd__(self, *args)

    def __gt__(self, other):
        return _MyString.MyString___gt__(self, other)

    def __lt__(self, other):
        return _MyString.MyString___lt__(self, other)

    def __ge__(self, other):
        return _MyString.MyString___ge__(self, other)

    def __le__(self, other):
        return _MyString.MyString___le__(self, other)

    def __ne__(self, other):
        return _MyString.MyString___ne__(self, other)

    def __eq__(self, other):
        return _MyString.MyString___eq__(self, other)

    def c_str(self):
        return _MyString.MyString_c_str(self)

    def data(self):
        return _MyString.MyString_data(self)

    def size(self):
        return _MyString.MyString_size(self)

    def length(self):
        return _MyString.MyString_length(self)

    def capacity(self):
        return _MyString.MyString_capacity(self)

    def empty(self):
        return _MyString.MyString_empty(self)

    def shrink_to_fit(self):
        return _MyString.MyString_shrink_to_fit(self)

    def clear(self):
        return _MyString.MyString_clear(self)

    def insert(self, *args):
        return _MyString.MyString_insert(self, *args)

    def erase(self, index, count):
        return _MyString.MyString_erase(self, index, count)

    def replace(self, *args):
        return _MyString.MyString_replace(self, *args)

    def substr(self, *args):
        return _MyString.MyString_substr(self, *args)

    def append(self, *args):
        return _MyString.MyString_append(self, *args)

    def find(self, *args):
        return _MyString.MyString_find(self, *args)

# Register MyString in _MyString:
_MyString.MyString_swigregister(MyString)



