

# Generated at 2022-06-13 17:44:57.537201
# Unit test for method visit_Subscript of class Resolver
def test_Resolver_visit_Subscript():
    """Test case for method visit_Subscript of class Resolver."""
    _Resolver = Resolver("a", {})
    _assert_equal(
        _Resolver._visit_Subscript(
            Subscript(Name("A", Load()), Tuple(
                [Name("a", Load()), Name("b", Load())], Load()),
                Load())).value,
        "a | b"
    )
    _assert_equal(
        _Resolver._visit_Subscript(
            Subscript(Name("A", Load()), Tuple(
                [Name("a", Load())], Load()),
                Load())).value,
        "a"
    )

# Generated at 2022-06-13 17:45:02.921646
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    p = Parser()

# Generated at 2022-06-13 17:45:12.249804
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    from .doc import parse
    from .resolver import Resolver
    from .reader import Reader
    from .alias import Alias
    from .type_def import TypeDef
    from .typing import Union, cast
    from .config import Config
    from .doc import Doc, parse, Parser
    from .reader import Reader
    from .utils import get_docstring
    from .alias import Alias
    from .resolver import Resolver
    from .typing import cast
    from .type_def import TypeDef
    from .config import Config
    from .annotations import eval_ann
    def func_ann(root, alias, node, *, has_self, cls_method):
        reader = Reader(root)
        alias = Alias(alias)
        alias.close()
        resolver = Resolver(root, alias, '')

# Generated at 2022-06-13 17:45:18.799573
# Unit test for method compile of class Parser
def test_Parser_compile():
    from typing import List
    from mypy_extensions import TypedDict
    from typing_extensions import Literal
    from .walker import ClassDef, Name, Module
    from .types import _Q
    import logging
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    p = Parser()
    p.imp['test'] = set()
    p.alias['test.CONST'] = '2 ** 3'
    p.alias['test.self'] = 'self'
    p.alias['test.Class'] = 'test.Class'
    p.alias['test.Class.attr'] = 'Any'
    p.alias['test.Class.attr2'] = 'test.Class'
    p.alias['test.Class.attr3'] = 'test.Class'


# Generated at 2022-06-13 17:45:25.200910
# Unit test for method is_public of class Parser
def test_Parser_is_public():
    from .utils import PY3, PY36
    from .functions import is_public_family
    from .ast import parse
    from .codegen import CodeGenerator
    # common
    p = Parser()
    m = parse(('import a.b.c', 'a.d.e: f.g'))
    p.feed(m, '')
    assert p.is_public('')
    assert p.is_public('a')
    assert p.is_public('a.b')
    assert p.is_public('a.b.c')
    assert p.is_public('a.d')
    assert not p.is_public('a.d.e')
    assert p.is_public('a.d.e.f')

# Generated at 2022-06-13 17:45:32.007032
# Unit test for method api of class Parser
def test_Parser_api():
    import inspect
    import re
    import sys
    import types

    from pkg_resources import resource_string
    
    import asttokens

    from .utils import get_ast

    def check(src: str, ok: str) -> None:
        """Check documentation."""
        m = ModuleType('_marvin_doc')
        m.__file__ = '<marvin_doc>'
        m.__path__ = []
        m.__package__ = 'marvin_doc'
        exec(src, m.__dict__)
        ast = get_ast(src)
        parser = Parser(m.__file__, ast)
        result = parser.compile()
        result = re.sub(r'\n{3,}', '\n\n', result)

# Generated at 2022-06-13 17:45:42.110412
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():

    P=Parser()
    root=""
    args=["*"]
    has_self=True
    cls_method=True
    def test(args,root,has_self,cls_method):
        args=[arg(arg=arg,annotation=None) for arg in args]
        return list(P.func_ann(root,args,has_self,cls_method))

    assert test(["a","b","c"],"abc",True,False)==["type[Self]","type[A]","type[B]","type[C]"]
    assert test(["*"],"",False,False)==[""]
    assert test(["*","a","b"],"ab",True,True)==["type[Self]","","type[A]","type[B]"]

# Generated at 2022-06-13 17:45:47.128900
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():
    data = 'typing.List[typing.List[int]]'
    doc = Resolver('', {}).visit(parse(data).body[0].value)
    assert unparse(doc) == 'List[List[int]]'



# Generated at 2022-06-13 17:45:56.823927
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    import ast
    import io
    p = Parser()
    class_body = ast.parse(
        '''
        def __init__(self, a, b, *, c=None, d=None):
            """Docstring for __init__."""
            ...

        def __new__(cls, *args, **kwargs):
            """Docstring for __new__."""
            ...

        async def __aenter__(self):
            """Docstring for __aenter__."""
            ...

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            """Docstring for __aexit__."""
            ...
        ''')
    p.class_api('module.A', [], class_body)

# Generated at 2022-06-13 17:46:03.613366
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    assert Resolver("", {}, "").visit_Name(Name("", Load())) == Name("", Load())
    assert Resolver("", {}, "").visit_Name(Name("N", Load())) == Name("N", Load())
    node = Name("N", Load())
    assert Resolver("", {'N': 'A'}, "").visit_Name(node) == Name("A", Load())
    node = Name("N", Load())
    assert Resolver("R", {'R.N': 'A'}, "").visit_Name(node) == Name("A", Load())
    node = Name("N", Load())
    assert Resolver("R", {'R.N': 'A'}, "N").visit_Name(node) == Name("Self", Load())