

# Generated at 2022-06-13 17:43:54.035270
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    p = Parser()
    class_doc = "_name_\n\n*Full name:* `_full_name_`\nBases: ()\nMembers:\n\
 | name | Type | \n|-|-|\n| `a` | `int` | \n| `b` | `int` | \n"
    assert p.class_api('__main__', '_name_', [], [
        Assign(targets=[Name(id='a', ctx=Store())],
               value=Constant(value=1, kind=None)),
        Assign(targets=[Name(id='b', ctx=Store())],
               value=Constant(value=1, kind=None))]) == class_doc

# Generated at 2022-06-13 17:43:54.926147
# Unit test for method api of class Parser

# Generated at 2022-06-13 17:44:01.167397
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    root = 'mod.submod'
    name = 'class'
    node = ClassDef(
        name='class',
        bases=[],
        keywords=[],
        body=[Assign(
            targets=[Name(id='name')],
            value=Constant(value='hello')
        )],
        decorator_list=[],
        type_comment=None
    )
    parser = Parser()
    parser.imp[root] = set()
    parser.level[root] = 0
    parser.level[name] = 1
    parser.root[name] = root
    parser.class_api(root, 'mod.submod.class', [], node.body)

# Generated at 2022-06-13 17:44:11.040529
# Unit test for method globals of class Parser
def test_Parser_globals():
    from doctyp import Parser, _I, _G
    from doctyp.util import resolve
    from doctyp.parser import Module
    from doctyp.ast import parse
    # Test case 1
    p = Parser()
    root = "test"
    node = parse(
        """
        name = 1
        """,
    )
    p.globals(root, node)
    assert p.alias == {"test.name": "1"}
    # Test case 2
    p = Parser()
    root = "test"
    node = parse(
        """
        a: int = 1
        """,
    )
    p.globals(root, node)
    assert p.alias == {"test.a": "1"}
    # Test case 3
    p = Parser()
    root = "test"


# Generated at 2022-06-13 17:44:18.067688
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    def assert_equal(fn: str, code: str, alias: dict[str, str],
                     self_ty: str = "", root: str = "tests.test_dataclass") \
            -> None:
        fncode = unparse(parse(code).body[0])
        r = Resolver(root, alias, self_ty)
        c = r.visit(parse(fncode).body[0])
        if not isinstance(c, Expr):
            assert fncode == unparse(c)
        else:
            assert fncode == unparse(c.value)

    assert_equal("Self -> int", "str", {}, "Self")
    assert_equal("Dict", "typing.Dict[str, int]", {})

# Generated at 2022-06-13 17:44:23.506069
# Unit test for method api of class Parser
def test_Parser_api():
    return None
import builtins
from importlib import import_module
from typing import (
    Any,
    Sequence,
)
from textwrap import dedent
from types import ModuleType
from typing_extensions import Final
from numpydoc.__main__ import Session, Autodoc, Option, Options
from numpydoc.docscrape import getdoc, get_doc_object
from numpydoc.linker import Linker
from numpydoc.docscrape_sphinx import _parse_doc_string
from numpydoc.utils import docstring_head
from numpydoc.numpydoc import NumpyDocString
from pytest import fixture
from .utils import TempDir
from .utils import attr, arg
from .utils import code, table
from .utils import doctest
from .utils import esc_underscore


# Generated at 2022-06-13 17:44:26.427262
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    from .ast import ast
    p = Parser()
    for a in ast("def f(x, y, z=1, *args, a, b=2, **kwargs) -> int: ...").body[0].args.args:
        assert p.func_ann("f", [a]) == [
            "str", "str", "int", "type[Iterable[str]]", "str", "int", "str"]

# Generated at 2022-06-13 17:44:31.625205
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    from .utils import code_to_ast
    from .types import Doc, Arg
    from .svg import uri_md5, display_svg
    from .ontology import Ontology, OntologyNode
    from .ontology.classes import V

    def gen_doc(doc: str, *, alias: dict[str, str], root: str = 'pyslvs',
                self_ty: str = "") -> Arg:
        e = code_to_ast(doc)
        e = Resolver(root, alias, self_ty).visit(e.body[0])
        return eval(unparse(e), {"V": V})

    class O:
        pass


# Generated at 2022-06-13 17:44:36.574891
# Unit test for method imports of class Parser
def test_Parser_imports():
    root = 'some.project'
    node = Import([alias('aaa.bbb.ccc', 'aaa')])
    parser = Parser()
    parser.imports(root, node)
    assert parser.alias == {
        _m(root, 'aaa'): 'aaa.bbb.ccc',
    }
    node = ImportFrom(module='aaa', names=[alias('bbb', 'ccc')], level=1)
    parser.imports(root, node)
    assert parser.alias == {
        _m(root, 'aaa'): 'aaa.bbb.ccc',
        _m(root, 'ccc'): _m(parent(root), 'aaa', 'bbb'),
    }

# Generated at 2022-06-13 17:44:39.301502
# Unit test for method globals of class Parser
def test_Parser_globals():
    from . import test_Parser
    from . import test_generic_visit

    parser = test_Parser()
    test_generic_visit(parser, parser.globals)

# Generated at 2022-06-13 17:46:04.214059
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    class Test(Parser):
        alias = {}
        imp = {'': {''}}
        root = {'': ''}
        const = {}
        docstring = {}
        def __init__(self, **kwargs):
            self.doc = kwargs
            super().__init__()

# Generated at 2022-06-13 17:46:10.039936
# Unit test for function table
def test_table():
    # pylint: disable=eval-used
    assert eval(table('a', 'b', [['c', 'd'], ['e', 'f']])).startswith('| a | b |\n|:---:|:---:|\n| c | d |\n| e | f |')



# Generated at 2022-06-13 17:46:14.623756
# Unit test for method compile of class Parser
def test_Parser_compile():
    f = """# Multi-line docstring
    def func(): pass
    """
    p = Parser()
    p.add_from_file(f, 'test_pdoc.py')
    assert p.compile() == '**Table of contents:**\n\n    + [test_pdoc.func]()\n\n### func()\n\n*Full name:* `test_pdoc.func`\n\n\nMulti-line docstring\n\n\n'


# Generated at 2022-06-13 17:46:22.559528
# Unit test for function const_type
def test_const_type():
    assert const_type(parse(f'{1!r}').body[0].value) == "int"
    assert const_type(parse(f'{1!r}').body[0].value) == "int"
    assert const_type(parse(f'{1!r}').body[0].value) == "int"
    assert const_type(parse(f'{1!r}').body[0].value) == "int"
    assert const_type(parse(f'{1!r}').body[0].value) == "int"



# Generated at 2022-06-13 17:46:29.292697
# Unit test for function doctest
def test_doctest():
    assert doctest("""\
    >>> a = 5
    >>> b = 3
    """) == """\
```python
>>> a = 5
>>> b = 3
```"""
    assert doctest("""\
    >>> a = 5
    >>> b = 3
    >>> c = 5
    >>> d = 3
    """) == """\
    >>> a = 5
    >>> b = 3
    ```
    >>> c = 5
    >>> d = 3
    ```"""
    assert doctest("""\
    >>> a = 5
    b = 3
    """) == """\
    >>> a = 5
    b = 3
    """

# Generated at 2022-06-13 17:46:36.800362
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    node_Union = Subscript(Name('Union', Load()), Tuple([
        Name('a', Load()),
        Name('b', Load()),
    ], Load()), Load())
    node_Optional = Subscript(Name('Optional', Load()), Tuple([
        Name('a', Load()),
    ], Load()), Load())
    node_List = Subscript(Name('List', Load()), Tuple([
        Name('a', Load()),
    ], Load()), Load())
    node_Deque = Subscript(Name('Deque', Load()), Tuple([
        Name('a', Load()),
    ], Load()), Load())

# Generated at 2022-06-13 17:46:42.403712
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    parser = Parser("")
    parser.imp = {"": {}}
    parser.root = {"": ""}
    parser.alias = {"": ""}
    parser.const = {"": ""}
    parser.level ={"": 0}
    parser.doc = {"": ""}
    parser.docstring = {"": ""}
    parser.b_level = 0
    parser.link = False
    parser.toc = False
    parser.is_public("")



# Generated at 2022-06-13 17:46:46.879745
# Unit test for function is_public_family
def test_is_public_family():
    assert is_public_family('abc')
    assert is_public_family('abc.Abc')
    assert not is_public_family('abc._Abc')
    assert not is_public_family('abc.__Abc')
    assert not is_public_family('abc.__abcd__')



# Generated at 2022-06-13 17:46:55.656695
# Unit test for method api of class Parser
def test_Parser_api():
    def run(d):
        p = Parser(Naming.UPPER_CASE)
        p.api('root', parse(d))
        return p.compile()
    def check(d: str, *, output: str) -> None:
        assert run(d) == output
    # Function
    check('''
        def foo(a, b, *, c=d) -> e:
            pass
    ''', output='''
        ### foo()
        *Full name:* `root.foo`

        Type | Default
        --- | ---
        Self | 
        * | 
        args... | 
        **kwargs | 
        return | e

        ```python
        pass
        ```
    ''')
    # Function with different kind of args
    # TODO: Add more examples


# Generated at 2022-06-13 17:46:58.843049
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():
    root = '__main__'
    alias = {}
    self_ty = ''
    node = Attribute(value=Name(id='typing', ctx=Load()), attr='Union', ctx=Load())
    assert Resolver(root, alias, self_ty).visit_Attribute(node) == Name(id='Union', ctx=Load())

# Generated at 2022-06-13 17:48:28.113145
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    p = Parser(link=False)
    p.imp['a'] = {'a.a', 'a.b', 'a.c.c', 'a.c.d', 'a.c.e'}
    p.doc['a'] = ""
    p.doc['a.b'] = ""
    p.doc['a.c.c'] = ""
    p.doc['a.c.d'] = ""
    p.doc['a.c.e'] = ""
    assert not p.is_public('a.b.b')
    p.doc['a.b.b'] = ""
    assert p.is_public('a.b.b')
    
test_Parser_is_public()

# Generated at 2022-06-13 17:48:32.800011
# Unit test for function walk_body
def test_walk_body():
    a = """
    import b
    if True:
        import c
    """
    a = unparse(parse(a))
    b = """
    import b
    import c
    """
    assert code(b) == code(unparse(walk_body(parse(a).body)))



# Generated at 2022-06-13 17:48:35.590787
# Unit test for function table
def test_table():
    """Unit test for function table."""
    assert table('a', 'b', [['c', 'd'], ['e', 'f']]) == (
        '| a | b |\n'
        '|:---:|:---:|\n'
        '| c | d |\n'
        '| e | f |\n\n'
    )

# Generated at 2022-06-13 17:48:45.324410
# Unit test for method func_api of class Parser
def test_Parser_func_api():
    p = Parser(['.'])
    fdef = FunctionDef(
        name='f',
        args=arguments(
            args=[arg('x', None), arg('y', None)],
            vararg=arg('zs', None),
            kwonlyargs=[arg('kw1', None), arg('kw2', None)],
            kwarg=arg('kw', None),
            defaults=[None, Num(1), None, Num(2)],
        ),
        decorator_list=[],
        returns=None,
    )
    p.func_api('', '', fdef.args, fdef.returns, has_self=False, cls_method=False)

# Generated at 2022-06-13 17:48:54.209725
# Unit test for method globals of class Parser
def test_Parser_globals():
    f = io.StringIO()
    h = logging.StreamHandler(f)
    logger.addHandler(h)

# Generated at 2022-06-13 17:49:01.043904
# Unit test for method compile of class Parser
def test_Parser_compile():
    p = Parser(link=False)
    for expr, target in _test_get_docstring_table:
        node = parse1(expr)
        p.imports('', node)
        p.globals('', node)
    for expr in _test_get_docstring_api:
        node = parse1(expr)
        p.api('', node)
    assert p.compile() == _test_get_docstring_target

# Docstring for function test_Parser_compile
test_Parser_compile.__doc__ = f"\n{_test_get_docstring_table}\n{_test_get_docstring_api}\n{_test_get_docstring_target}"


# Generated at 2022-06-13 17:49:10.277168
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    from .structure import Node
    r: Resolver = Resolver('', {
        'typing.Union': 'typing.Union',
        'typing.Optional': 'typing.Optional',
        'typing.Tuple': 'typing.Tuple',
    })
    e = r.visit(parse('[typing.Union[1, 2]]').body[0].value.elts[0])
    e2 = BinOp(Constant(1), BitOr(), Constant(2))
    assert e == e2, f"{unparse(e)} != {unparse(e2)}"
    e = r.visit(parse('[typing.Optional[1]]').body[0].value.elts[0])
    e2 = BinOp(Constant(1), BitOr(), Constant(None))
    assert e