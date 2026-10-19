

# Generated at 2022-06-13 17:45:25.764538
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    from typing import List

    @dataclass
    class A:
        x: List[int]

    root = 'test_Resolver_visit_Name'
    alias = {
        'test_Resolver_visit_Name': '',
        'test_Resolver_visit_Name.A': '',
        'test_Resolver_visit_Name.A.x': 'List[int]'
    }
    self_ty = 'A'
    node = Name("x", Load())
    assert Resolver(root, alias, self_ty).visit_Name(node) == Name("List", Load())



# Generated at 2022-06-13 17:45:32.266837
# Unit test for method visit_Subscript of class Resolver

# Generated at 2022-06-13 17:45:35.349620
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    assert code(unparse(Resolver('typing', {}, self_ty='Self')
                        .visit_Name(Name('Self', Load())))) == 'Self'


# Generated at 2022-06-13 17:45:42.173237
# Unit test for function walk_body
def test_walk_body():
    body = [stmt(body=[
        If(test=Name(id='a', ctx=Load()), body=[
            Try(body=[
                Assign(targets=[Name(id='a', ctx=Store())],
                       value=Call(func=Name(id='b', ctx=Load()),
                                  args=[], keywords=[]))
            ], handlers=[], orelse=[], finalbody=[]),
        ], orelse=[])
    ], orelse=[])]
    assert list(walk_body(body)) == body



# Generated at 2022-06-13 17:45:52.348523
# Unit test for method visit_Constant of class Resolver
def test_Resolver_visit_Constant():
    test = Resolver(root='', alias={})
    assert test.visit(Constant('abc')) == Constant('abc')
    node = cast(Expr, parse('abc').body[0])
    assert test.visit(node.value) == Name('abc', Load())
    node = cast(Expr, parse('a.b.c').body[0])
    assert test.visit(node.value) == Attribute(Name('a', Load()), 'b', Load())
    node = cast(Expr, parse('a.b.c[0]').body[0])
    assert test.visit(node.value) == Subscript(Attribute(Name('a', Load()), 'b', Load()),
                                               Constant(0), Load())



# Generated at 2022-06-13 17:46:01.033399
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    "Tests for method func_ann of class Parser"
    # For node:
    # def x(a: str, b: str, *args: tuple[str], c=1, d=2, **kwargs: dict[str, str]):
    #     ...
    args = [
        arg('a', parse_type('str')),
        arg('b', parse_type('str')),
        arg('args', parse_type('tuple[str]')),
        arg('c', None),
        arg('d', None),
        arg('kwargs', parse_type('dict[str, str]')),
    ]
    p = Parser() 
    p.alias['A'] = 'A'
    p.alias['B'] = 'B'
    p.alias['C'] = 'C'

# Generated at 2022-06-13 17:46:03.635379
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    source = '''
import json
json.dumps()
json.loads()
'''
    doc_string = unparse(parse(source, filename='complex.py'))
    assert doc_string == '''import json

json.dumps()

json.loads()

'''


# Generated at 2022-06-13 17:46:11.604939
# Unit test for method visit_Attribute of class Resolver
def test_Resolver_visit_Attribute():
    from pyslvs.typing import Path
    assert Resolver('test', {}).visit_Attribute(
        Attribute(Name('typing', Load()), 'Path', Load())
    ).__dict__['attr'] == 'Path'
    assert Resolver('test', {}).visit_Attribute(
        Attribute(Name('self', Load()), 'item', Load())
    ).__dict__['attr'] == 'item'



# Generated at 2022-06-13 17:46:16.009688
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    tree = parse('1 + 2')
    #print(tree)
    resolver = Resolver(root='', alias={}, self_ty='')
    #print(unparse(resolver.visit(tree)))
    assert unparse(resolver.visit(tree)) == '1 + 2'


# Generated at 2022-06-13 17:46:17.646061
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    @dataclass
    class T:
        t: Optional[str]

# Generated at 2022-06-13 17:47:57.171700
# Unit test for method load_docstring of class Parser
def test_Parser_load_docstring():
    from pybag.core import docstr

    class A:
        a = 1

    class B:
        """b"""

    class C:
        """c"""
        b = B()

    class D:
        e, f = 1, 2

    p = Parser()
    p.doc = {'A.a': '{}\n', 'B.b': '{}\n', 'C.b': '{}\n',
             'D.e': '{}\n', 'D.f': '{}\n'}
    p.load_docstring('', docstr)
    assert p.docstring['docstr.__doc__'] == '\n'
    p.load_docstring('', A)
    assert p.docstring['A.a'] == ''
    p.load_docstring('', B)
   

# Generated at 2022-06-13 17:48:05.377820
# Unit test for method func_ann of class Parser
def test_Parser_func_ann():
    """pdoc.Parser.func_ann:"""
    p = Parser(None)
    assert list(p.func_ann('', [], has_self=False, cls_method=False)) == []

    assert list(p.func_ann(
        '', [arg('', None)], has_self=False, cls_method=False)) == ['ANY']

    assert list(p.func_ann(
        '', [arg('', None)], has_self=True, cls_method=False)) == ['Self']

    assert list(p.func_ann(
        '', [arg('', None)], has_self=True, cls_method=True)) == ['type[Self]']


# Generated at 2022-06-13 17:48:15.392820
# Unit test for function walk_body
def test_walk_body():
    """Test for walk_body"""

# Generated at 2022-06-13 17:48:23.216516
# Unit test for method api of class Parser
def test_Parser_api():
    """ test method api of class Parser """
    from .parser import load_parser
    from .parser import find_parser
    from .parser import parser_mapping
    from .parser import TOKEN_NAME
    from .parser import run_parser

    from .util import ModuleType
    from .util import get_docstring
    from .util import gettext
    from .util import FormatError

    from .type import ClassType
    from .type import AnyType
    from .type import TupleType
    from .type import SequenceType
    from .type import UnionType
    from .type import CallableType
    from .type import OptionalType
    from .type import TypeVarType
    from .type import SyntheticTypeAlias
    from .type import UnboundType
    from .type import TypeList
    from .type import TypeDict


# Generated at 2022-06-13 17:48:30.314336
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    root = 'group'
    alias = {'group': 'Construct', 'group.Construct': 'group'}
    self_ty = 'T'
    resolver = Resolver(root, alias, self_ty)

    def check(name, expect):
        name = Name(name, Load())
        assert code(unparse(resolver.visit(name))) == expect

    check('group', 'Construct')
    check('Construct', 'group.Construct')
    check('T', 'Self')



# Generated at 2022-06-13 17:48:38.144147
# Unit test for function walk_body
def test_walk_body():
    t = parse(
        'def foo() -> None:\n'
        '    if True:\n'
        '        try:\n'
        '            if True:\n'
        '                a = 1\n'
        '            else:\n'
        '                a = 2\n'
        '        except Exception:\n'
        '            b = 1\n'
        '        else:\n'
        '            b = 2\n'
        '        finally:\n'
        '            c = 1\n'
        '    else:\n'
        '        d = 1\n'
        '    e = 1\n').body[0]

# Generated at 2022-06-13 17:48:47.679452
# Unit test for method visit_Name of class Resolver
def test_Resolver_visit_Name():
    resolver = Resolver("my_typing", {"my_typing": "typing"})
    n = cast(Name, parse("A").body[0].value)
    assert resolver.visit_Name(n).id == "A"
    n = cast(Name, parse("B[int]").body[0].value)
    assert resolver.visit_Name(n).value.id == "int"
    n = cast(Name, parse("C[A]").body[0].value)
    assert resolver.visit_Name(n).value.id == "A"
    n = cast(Name, parse("D['a']").body[0].value)
    assert resolver.visit_Name(n).value.value == "a"

# Generated at 2022-06-13 17:48:55.732226
# Unit test for method class_api of class Parser
def test_Parser_class_api():
    def api(root: str, name: str, bases: list[expr], body: list[stmt]) -> str:
        p = Parser(root, link=False)
        p.class_api(root, name, bases, body)
        return p.doc[name]
    assert api('abc', 'abc.A', [], []) == table("Members", "Type", items=())
    assert api('abc', 'abc.A', [Name(id='B', ctx=Load())], []) == (
        table("Bases", items=("code(B)",)) +
        table("Members", "Type", items=(("code(__init__)", "type[None]"),)))

# Generated at 2022-06-13 17:49:02.960976
# Unit test for method api of class Parser
def test_Parser_api():
    string = '''
        # Comment
        def hello_world():
            """Hello world."""

        @test
        async def async_hello_world():
            """Async hello world."""

        class MyClass:
            """Test class."""
            def hello(self, a: int) -> None:
                pass

            @classmethod
            def class_hello(cls, a: int) -> int:
                pass

            @staticmethod
            def static_hello(a: int) -> int:
                pass
    '''