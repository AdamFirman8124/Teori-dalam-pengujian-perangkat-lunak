

# Generated at 2022-06-13 17:45:24.263775
# Unit test for method compile of class Parser
def test_Parser_compile():
    parser = Parser(["../../aio/__init__.py"], link=True)
    assert isinstance(parser.compile(), str)


# Generated at 2022-06-13 17:45:27.551330
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    """Unit test for method visit_Subscript of class Resolver."""

# Generated at 2022-06-13 17:45:39.086005
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    from typing import Sequence
    from typing import Any
    from typing import Iterator
    from typing import Optional
    class arg: ...
    class expr: ...
    parser = Parser(False, False)
    root = "root"
    args = [arg("a", None), arg("*", None), arg("**b", None), arg("return", None)]
    has_self = False
    cls_method = False
    expect = ["Any", "", "Any", "Any"]
    actual = []
    for i, x in enumerate(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method)):
        actual.append(str(x))
    assert(actual == expect)

# Generated at 2022-06-13 17:45:47.870692
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    from ast_pyx import Module
    from ast import parse
    from unittest import TestCase
    from io import StringIO
    from .markdown import Documentation
    from .logger import logging

    code = """
    class Foo(object, metaclass=abc.ABCMeta):
        """

# Generated at 2022-06-13 17:45:53.620423
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    alias = {
        '__module1__.__module2__.__module3__': 'Alias',
        '__module1__.__module2__': 'Alias.__module3__'
    }
    resolver = Resolver('__module1__.__module2__.__module3__', alias)
    assert resolver.visit_Name(Name('__module2__', Load())) == Name('Alias', Load())

# Generated at 2022-06-13 17:46:01.501309
# Unit test for method compile of class Parser

# Generated at 2022-06-13 17:46:07.100685
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    parser = Parser()
    parser.imp['a.b'] = set()
    parser.imp['a.b.c'] = {'a.b.c.d'}
    parser.root['a.b.c.d'] = 'a.b.c.d'
    assert parser.is_public('a.b.c')
    assert not parser.is_public('a.b.c.d')
    parser.imp['a.b'] = {'a.b.c'}
    assert parser.is_public('a.b.c')
    assert parser.is_public('a.b.c.d')
    parser.imp['a.b.c'] = {'a.b.c.d'}
    assert not parser.is_public('a.b.c')

# Generated at 2022-06-13 17:46:15.229245
# Unit test for method api of class Parser
def test_Parser_api():
    from jedi.api.classes import Script
    from jedi.inference.compiled import get_special_object
    from jedi.inference.gradual.typing import get_generic_type

    p = Parser()
    m = Script('from typing import Union, Generic, TypeVar, Any, List',
               1, len('from typing import Union, Generic'), None).goto_definitions()[0].module_context
    p.class_api('typing', 'typing.Union',
                m.get_subscope_by_name('Union').py__bases__(),
                m.get_subscope_by_name('Union').tree_node.body)

# Generated at 2022-06-13 17:46:24.611302
# Unit test for function table
def test_table():
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == (
        "| a | b |\n"
        "|:---:|:---:|\n"
        "| c | d |\n"
        "| e | f |\n\n"
    )
    assert table('a', 'b', [['c', 'd'], ['e', 'f']], ['g', 'h']) == (
        "| a | b |\n"
        "|:---:|:---:|\n"
        "| c | d |\n"
        "| e | f |\n"
        "| g | h |\n\n"
    )

# Generated at 2022-06-13 17:46:29.964798
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():
    r = Resolver("", dict())
    a = Attribute(Name("typing", Load()), "Optional", Load())
    b = r.visit_Attribute(a)
    assert isinstance(b, Name)
    assert b.id == "Optional"
    a = Attribute(Name("typing", Load()), "Optional", Load())
    b = r.visit_Attribute(a)
    assert isinstance(b, Name)
    assert b.id == "Optional"
    a = Name("Optional", Load())
    b = r.visit_Attribute(a)
    assert isinstance(b, Name)
    assert b.id == "Optional"