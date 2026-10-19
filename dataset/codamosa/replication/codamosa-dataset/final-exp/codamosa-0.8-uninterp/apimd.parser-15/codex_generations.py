

# Generated at 2022-06-13 17:45:40.838819
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    assert code(unparse(Resolver("root", {}).visit_Subscript(Subscript(Name("List", Load()), Tuple(elts=[Name("int", Load())]), Load())))) == "`List[int]`"
    assert code(unparse(Resolver("root", {}).visit_Subscript(Subscript(Name("Dict", Load()), Tuple(elts=[Name("int", Load()), Name("int", Load())]), Load())))) == "`Dict[int, int]`"
    assert code(unparse(Resolver("root", {}).visit_Subscript(Subscript(Name("List", Load()), Tuple(elts=[Name("int", Load())]), Load())))) == "`List[int]`"

# Generated at 2022-06-13 17:45:47.784961
# Unit test for function walk_body
def test_walk_body():
    assert list(walk_body([
        Assign([], Expr(Constant(1))),
        If([], [], []),
        Try([], [], [], []),
    ])) == [
        Assign([], Expr(Constant(1))),
        If([], [], []),
        Try([], [], [], []),
    ]



# Generated at 2022-06-13 17:45:49.653064
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():

    from .parser import Parser
    from .parser import _g
import nptyping


# Generated at 2022-06-13 17:45:58.835686
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    """Test method visit_Name of class Resolver"""
    from .collection import _Mapping
    from .simulation import _Iterable
    from .simulation import _Iterator
    # noqa: E501, E261(line too long)

# Generated at 2022-06-13 17:46:05.082851
# Unit test for function doctest
def test_doctest():
    assert doctest(">>> # Hello world!") == "```python\n>>> # Hello world!\n```"
    assert doctest(
        """>>> # Hello world!
>>> print("hello")
hello
"""
    ) == """```python
>>> # Hello world!
>>> print("hello")
hello
```"""
    assert doctest(
        """# Hello world!
>>> print("hello")
hello"""
    ) == """# Hello world!
```python
>>> print("hello")
hello
```"""
    assert doctest(
        """# Hello world!
>>> # Hello world!
>>> print("hello")
hello"""
    ) == """# Hello world!
```python
>>> # Hello world!
>>> print("hello")
hello
```"""

# Generated at 2022-06-13 17:46:13.819117
# Unit test for function is_public_family
def test_is_public_family():
    assert not is_public_family('abc._def')
    assert not is_public_family('abc._def._ghi.jkl')
    assert is_public_family('abc._Def._ghi.jkl')
    assert is_public_family('abc.def')
    assert is_public_family('abc.def.ghi.jkl')
    assert not is_public_family('abc.__def.__ghi.__jkl')
    assert is_public_family('abc.__Def.ghi.__jkl')
    assert not is_public_family('abc.__Def.ghi.__jkl.__mno')
test_is_public_family()
del test_is_public_family



# Generated at 2022-06-13 17:46:24.675428
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    parser = Parser()
    parser.doc = {"a": 1, "a.b": 1, "a.c": 1, "a.b.c": 1}
    parser.root = {
        "a": "a", "a.b": "a", "a.c": "a", "a.b.c": "a.b"
    }
    parser.imp = {
        "a": set(["a.c"])
    }
    tests = (
        ("a", True), ("a.b", True), ("a.c", True), ("a.b.c", True), ("a.d", False),
        ("a.a", False), ("a.b.c.d", False)
    )
    for test in tests:
        assert parser.is_public(test[0]) == test[1]

# Generated at 2022-06-13 17:46:30.911010
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    _p = Parser(['foo', 'bar'], 'root')
    assert _p.alias == {'root': 'root'}
    assert _p.root == {'root': 'root'}
    assert _p.imp == {'root': {'root'}}
    assert _p.level == {'root': 0}
    assert not _p.is_public('root.err')
    assert _p.is_public('root')
    assert _p.is_public('root.foo')
    assert not _p.is_public('root.foo.err')
    assert _p.is_public('root.bar')
    _p = Parser([], 'root')
    assert not _p.is_public('root.err')
    assert _p.is_public('root')
    assert _p.is_

# Generated at 2022-06-13 17:46:42.141943
# Unit test for function const_type
def test_const_type():
    from sys import version_info
    from ast import parse
    from .pep585 import PEP585
    from .utils import const_type

    # Case from PEP 585
    assert const_type(parse('b""').body[0].value) == "bytes"
    assert const_type(parse('u""').body[0].value) == "str"
    assert const_type(parse('f""').body[0].value) == "str"
    assert const_type(parse('r""').body[0].value) == "str"

    # Case from PEP 584
    assert const_type(parse('typing.Any').body[0].value.func) == "Any"

# Generated at 2022-06-13 17:46:51.521209
# Unit test for method visit_Constant of class Resolver
def test_Resolver_visit_Constant():
    from ast import Expr
    from .__data__.parser import annotations, aliases
    resolver = Resolver('pyslvs', {
        'pyslvs.misc': 'misc',
    })
    assert type(resolver) == Resolver
    resolver.visit(Expr(Name('pyslvs', Load()))) == Name('pyslvs', Load())
    resolver.visit(annotations) == Attribute(Name('typing', Load()), 'Dict', Load())
    resolver.visit(aliases[0][1]) == Attribute(Name('pyslvs', Load()), 'Point', Load())
    resolver.visit(aliases[1][1]) == Tuple(
        [Attribute(Name('typing', Load()), 'Sequence', Load())],
        Load())
#