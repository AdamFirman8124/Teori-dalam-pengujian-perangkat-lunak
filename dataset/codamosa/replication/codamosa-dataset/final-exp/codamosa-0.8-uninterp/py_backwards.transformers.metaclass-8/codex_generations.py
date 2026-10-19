

# Generated at 2022-06-14 01:55:09.381604
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    class_def = ast.ClassDef(name='A',
                             bases=[],
                             keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
                             body=[],
                             decorator_list=[],
                             lineno=1,
                             col_offset=0,
                             end_lineno=3,
                             end_col_offset=0)
    module = ast.Module(body=[class_def])
    transformer = MetaclassTransformer()
    transformer.visit(module)
    assert module.body[0].lineno == 1

# Generated at 2022-06-14 01:55:10.632233
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:23.535564
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import textwrap
    from typed_astunparse import unparse
    from ..visitor import Visitor

    # Define a list of code snippets that are expected to be identical
    # after running the transformation on them.

# Generated at 2022-06-14 01:55:26.255528
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    r'''
    class A(metaclass=B):
        pass
    '''

# Generated at 2022-06-14 01:55:29.649938
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    node = ast.parse("foo = 1\n\nclass Bar(metaclass=type): pass")
    ref = "foo = 1\n\nclass Bar(_py_backwards_six_withmetaclass(type)): pass"
    assert transformer.visit(node) == ast.parse(ref)

# Generated at 2022-06-14 01:55:30.451076
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:35.967056
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # error: statement has no effect

    class t: pass
    class A(t): x=None # type: ignore
    assert A.__metaclass__ == type(A)
    assert A.x is None

    # normal case

    source = 'class A(metaclass=B): pass'
    expected = 'class A(_py_backwards_six_withmetaclass(B))'

    node = ast.parse(source)
    node = MetaclassTransformer().visit(node)
    actual = ast.unparse(node).strip()

    assert actual == expected

    # with bases

    source = 'class A(B, metaclass=C): pass'
    expected = 'class A(_py_backwards_six_withmetaclass(C), B)'

    node = ast.parse(source)
    node

# Generated at 2022-06-14 01:55:46.443029
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.visitor import ASTVisitor
    from .. import transforms
    from typing import List, Tuple
    from typed_ast.ast3 import ClassDef, Assign, Store, Name, Str, Load, FunctionDef, Mod
    import six
    import builtins

    class NodesCollector(ASTVisitor):
        def __init__(self):
            self.collected_nodes: List[Tuple[int, ast.AST]] = []

        def generic_visit(self, node):
            self.collected_nodes.append((0, node))
            return super().generic_visit(node)

        def visit_Assign(self, node):
            self.collected_nodes.append((1, node))
            return super().generic_visit(node)


# Generated at 2022-06-14 01:55:56.533451
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...fake import FakeNode, FakeTree
    from ...fake import get_fake_context
    from ..utils.node import dump_node_tree
    tree = FakeTree()
    parent = FakeNode(children=[tree])
    context = get_fake_context()
    visitor = MetaclassTransformer(context, parent)
    source = 'class A(metaclass=B): pass'
    node = ast.parse(source)
    tree.node = node
    node = visitor.visit_ClassDef(node.body[0])
    assert dump_node_tree(node) == '''\
ClassDef(name='A',
         bases=List(elts=[],
                    ctx=Load()),
         keywords=[],
         body=[Pass()],
         decorator_list=[])'''

# Generated at 2022-06-14 01:55:59.161578
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.example import example_ast_tree
    from ..utils.compare import compare_ast


# Generated at 2022-06-14 01:56:07.944800
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .. import compile_snippet

    input_ = snippet('''
    class A(metaclass=B):
        pass
    ''')
    expected_ = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B))
    '''

# Generated at 2022-06-14 01:56:19.109082
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    from typing import Any, List

    from .base import BaseNodeTransformer
    
    class FlaggingTransformer(BaseNodeTransformer):
        _tree_changed: bool = False

    @snippet
    def klass():
        class A(object):
            pass

    @snippet
    def klass2():
        class A(_py_backwards_six_withmetaclass(object)):
            pass

    tree = parse(klass)
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 1, len(tree.body)
    klass = tree.body[0]
    assert isinstance(klass, ast.ClassDef)

    transformer = MetaclassTransformer()
    metaclass = ast.Name(id='object', ctx=ast.Load())

# Generated at 2022-06-14 01:56:22.379955
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .test_base import compile_snippet, snippet_test


# Generated at 2022-06-14 01:56:33.266792
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()
    classdef = ast.ClassDef(name="A",  # type: ignore
                            bases=[],  # type: ignore
                            keywords=[ast.keyword(arg="metaclass",  # type: ignore
                                                  value=ast.Name("baz"))],  # type: ignore
                            body=[],  # type: ignore
                            decorator_list=[])  # type: ignore

    classdef = mt.visit_ClassDef(classdef)
    assert mt.tree_changed
    assert isinstance(classdef.bases[0], ast.Call)
    assert isinstance(classdef.bases[0].func, ast.Name)
    assert classdef.bases[0].func.id == "_py_backwards_six_withmetaclass"


# Unit test

# Generated at 2022-06-14 01:56:37.440885
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing_utils import compile_source
    from six import add_metaclass  # noqa
    from six.moves import reload_module

    reload_module(six)
    reload_module(typing)

    source = '''
    from six import add_metaclass

    @add_metaclass(type)
    class A:
        pass
    '''
    assert compile_source(source, MetaclassTransformer)

# Generated at 2022-06-14 01:56:44.646505
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer()
    module = transformer.visit(module)
    assert str(module) == 'from six import with_metaclass as _py_backwards_six_withmetaclass\n\n\nclass A(_py_backwards_six_withmetaclass(B)):\n    pass\n'


# Generated at 2022-06-14 01:56:51.029682
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # type: () -> None
    expected_output = ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A():
            pass
    """)
    output = MetaclassTransformer.run_pipeline(ast.parse("class A():pass"))
    assert ast.dump(expected_output) == ast.dump(output)


# Generated at 2022-06-14 01:56:55.989802
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import test_ast_node

    obj = MetaclassTransformer()
    ret = obj.visit_ClassDef(ast.parse('class A(metaclass=B): pass').body[0])

# Generated at 2022-06-14 01:57:03.328835
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    assert_equal(
        MetaclassTransformer().visit(ast.parse("""
        class A(metaclass=B, b=b):
            pass
        """)),
        ast.parse("""
        from six.imports import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B), b=b):
            pass
        """),
    )


# Generated at 2022-06-14 01:57:04.375963
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:57:16.466276
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    snippet2 = '''
    class A(metaclass=B):
        pass
    '''
    node = ast.parse(snippet2)
    ast.copy_location(node, ast.parse(snippet)())
    trans = MetaclassTransformer()
    assert not trans._tree_changed
    trans.visit(node)
    assert trans._tree_changed # pylint: disable=protected-access


# Generated at 2022-06-14 01:57:19.235989
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse(six_import)
    node_ = insert_at(0, node, six_import.get_body())
    assert node_.body == node.body
    assert node is not node_



# Generated at 2022-06-14 01:57:30.843311
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.messages import msg_metaclass_transformer
    from ..utils.test import TestCase, test_all_versions, test_module_versions

    class WithMetaclass(TestCase):
        def _test(self, source, expected):
            self.assertEqual(MetaclassTransformer().visit(ast.parse(source)), expected)

        def test_metaclass(self):
            self._test('''class A(metaclass=B):
            pass''', '''class A(_py_backwards_six_withmetaclass(B)):
            pass''')

        def test_no_metaclass(self):
            self._test('class A: pass', 'class A: pass')

    test_all_versions(WithMetaclass)


# Generated at 2022-06-14 01:57:40.075006
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_BaseNodeTransformer import Source
    from ..utils.source import separator
    from ..utils.tree import ast_to_source


# Generated at 2022-06-14 01:57:47.694309
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
        class A(object):
            pass
    """
    node = ast.parse(code)
    node = MetaclassTransformer().visit(node)

    assert ast.dump(node) == _dedent("""
        from six import with_metaclass as _py_backwards_six_withmetaclass


        class A(_py_backwards_six_withmetaclass(object)):
            pass
    """)

# Generated at 2022-06-14 01:57:57.913395
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('class A(metaclass=B): pass')
    node = MetaclassTransformer().visit(module)
    assert node.body == [
        six_import.get_body()[0],
        ast.ClassDef(name='A',
                     bases=[ast.Call(func=ast.Name(id='_py_backwards_six_withmetaclass',
                                                   ctx=ast.Load()),
                                     args=[ast.Name(id='B', ctx=ast.Load()),
                                           ast.Name(id='object', ctx=ast.Load())],
                                     keywords=[],
                                     starargs=None,
                                     kwargs=None)],
                     keywords=[],
                     body=[],
                     decorator_list=[])
    ]

# Generated at 2022-06-14 01:57:58.830319
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:58:08.090172
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.fake import get_fake
    from .remove_decorators import RemoveDecoratorsTransformer

    fake = get_fake(
        '''
        from six import with_metaclass

        class A(metaclass=B):  #@
            pass
        '''
    )

    node = ast.parse(fake.code, mode="exec")

    class T(RemoveDecoratorsTransformer):
        pass

    node = T.run(node)
    node = MetaclassTransformer.run(node)
    code = compile(node, "<string>", mode="exec", )
    exec(code)

    assert A == with_metaclass(B, object)


# Generated at 2022-06-14 01:58:10.164726
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..environ import Environ
    from ..parser import Parser
    from ..transformer.six_metaclass import MetaclassTransformer
    environ = Environ()
    parser = Parser()
    transformer = MetaclassTransformer()


# Generated at 2022-06-14 01:58:11.496547
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:58:27.838462
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    m = ast.parse("""
    class A(metaclass=B):
        pass
""")
    trans = MetaclassTransformer()

    node = trans.visit(m)

# Generated at 2022-06-14 01:58:36.125298
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    transformer = MetaclassTransformer()
    module = ast.parse("""
    class Class1(metaclass=type):
        pass
    """)
    module = transformer.visit(module)
    assert transformer.dependencies == ['six']
    assert transformer._tree_changed
    assert transformer.changes == 1
    assert transformer.dependencies == ['six']
    assert transformer.target == (2, 7)
    assert ast.dump(module) == "Module(body=[ClassDef(name='Class1', bases=ClassBases(metaclass=Name(id='type', ctx=Load()), bases=[]), keywords=[], body=[Pass()], decorator_list=[])])"

# Generated at 2022-06-14 01:58:47.748695
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import make_local_transformer_test
    test = make_local_transformer_test(MetaclassTransformer)
    # Example 1
    test('''
        class A(metaclass=B):
            pass
        ''',
        '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        
        ''')
    # Example 2

# Generated at 2022-06-14 01:58:48.424643
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:58.195818
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = \
    """
    class A(metaclass=B):
        pass
    """
    expected = \
    """
    class A(_py_backwards_six_withmetaclass(B, object)):
        pass
    """
    node = ast.parse(source).body[0]
    transformed = MetaclassTransformer().visit(node)
    assert ast.dump(transformed) == expected

    source = \
    """
    class A(B, metaclass=C):
        pass
    """
    expected = \
    """
    class A(_py_backwards_six_withmetaclass(C, B)):
        pass
    """
    node = ast.parse(source).body[0]
    transformed = MetaclassTransformer().visit(node)
    assert ast.dump

# Generated at 2022-06-14 01:59:09.889790
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.ctx import dump_and_load
    from ..utils.tree import tree_to_str
    from .base import BaseNodeTransformer

    source = '''
        class A(object):
            pass
        class B(abc.ABCMeta):
            pass
    '''

    tree: ast.AST = ast.parse(source)
    MetaclassTransformer(tree).visit(tree)


# Generated at 2022-06-14 01:59:23.343106
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import typing

    # Define test node
    class TestNode(object):
        def __init__(self, value):
            self.value = value

    # Define new node for comparison
    class NewNode(object):
        def __init__(self, value):
            self.value = value
            self.bases = [ast.Name(id='_py_backwards_six_withmetaclass', ctx=ast.Load()),ast.Attribute(attr='B', value=ast.Name(id='metaclass', ctx=ast.Load()), ctx=ast.Load())]
            self.keywords = []

    # Initialise transformer
    transformer = MetaclassTransformer()
    transformer._tree_changed = True
    # Set up test node

# Generated at 2022-06-14 01:59:30.134122
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    import astor
    tree = ast.parse("""
        class A(metaclass=B):
            pass
        """)

    expectation = """
        class A(_py_backwards_six_with_metaclass(B)):
            pass
    """
    transformer = MetaclassTransformer(sys.version_info)
    transformer.visit(tree)
    assert astor.to_source(tree) == expectation

# Generated at 2022-06-14 01:59:37.869409
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("""
        def f(x):
            return x
    """)
    transformer = MetaclassTransformer(node)
    result = transformer.visit(node)
    result = ast.Module(body=[
        six_import.get_body()[0],
        result.body[0]
    ])
    assert ast.dump(result, include_attributes=False) == ast.dump(ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass
    
        def f(x):
            return x
    """), include_attributes=False)

# Generated at 2022-06-14 01:59:44.635886
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    node_ClassDef = ast3.ClassDef(
        name='TestClass',
        bases=[
            ast3.Name(id='TestBaseClass', ctx=ast3.Load())
        ],
        keywords=[
            ast3.keyword(arg='metaclass', value=ast3.Name(id='TestMetaClass', ctx=ast3.Load()))
        ],
        body=[
            ast3.Expr(value=ast3.Str(s='Unit test ClassDef.'))
        ]
    )
    node_Module = ast3.Module(body=[node_ClassDef])
    transformer = MetaclassTransformer()
    result_Module = transformer.visit(node_Module)

    TestClass = getattr(result_Module, 'TestClass')
    TestMetaClass = getattr

# Generated at 2022-06-14 02:00:15.701291
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_visitor import run_visitor_test
    run_visitor_test(MetaclassTransformer,
                     'class A(metaclass=B):\n    pass',
                     'class A(_py_backwards_six_withmetaclass(B)):\n    pass')
    run_visitor_test(MetaclassTransformer,
                     'class A(B):\n    pass',
                     'class A(B):\n    pass')
    run_visitor_test(MetaclassTransformer,
                     'class A(B, metaclass=C):\n    pass',
                     'class A(_py_backwards_six_withmetaclass(C), B):\n    pass')

# Generated at 2022-06-14 02:00:20.061641
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from nuitka.PythonVersions import python_version
    from nuitka.ast.nodes.ClassNodes import ExpressionClassBody
    from nuitka.ast.nodes.FunctionNodes import ExpressionFunctionBody


# Generated at 2022-06-14 02:00:33.763823
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Unit test for method visit_ClassDef of class MetaclassTransformer."""

    # from six import with_metaclass as _py_backwards_six_withmetaclass
    # class A:
    #     pass
    import astor
    node = ast.parse(astor.to_source(six_import.get_body()) + 'class A: pass')

    # from six import with_metaclass as _py_backwards_six_withmetaclass
    # class A(object, metaclass=ABCMeta):
    #     pass
    module = ast.parse('class A(object, metaclass=ABCMeta): pass')
    metaclass = module.body[0].keywords[0].value

# Generated at 2022-06-14 02:00:34.873850
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:36.359816
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:00:38.874945
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # type: () -> None

    import six
    import ast
    import astunparse


# Generated at 2022-06-14 02:00:47.314182
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(metaclass=B):
            pass
        """)  # noqa: E501
    xformer = MetaclassTransformer()
    xformer.visit(tree)
    assert str(tree) == str(ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B, *[])):
            pass
        """))  # noqa: E501

# Generated at 2022-06-14 02:00:53.834633
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import parse
    from .test_BaseNodeTransformer import BaseNodeTransformerTest

    source = '''class A(metaclass=B, x=3):
                   pass'''
    tree = parse(source)
    node = tree.body[0]
    transformer = MetaclassTransformer()
    node = transformer.visit(node)
    assert BaseNodeTransformerTest.compare(node,
                                           'class A(_py_backwards_six_withmetaclass(B), '
                                           'x=3): pass')

# Generated at 2022-06-14 02:01:03.100298
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class_def = ast.parse('class A(metaclass=B, object=C):pass').body[0]
    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer.visit(class_def)

    assert ast.dump(class_def.bases[0]) == ast.dump(six_import.get_body()[0])
    assert ast.dump(class_def.bases[1]) == ast.dump(class_bases.get_body(ast.Name(id='B', ctx=ast.Load()),
                                                                           ast.List(elts=[ast.Name(id='object', ctx=ast.Load())])))
    assert len(class_def.keywords) == 0

# Generated at 2022-06-14 02:01:15.329379
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    m = ast.parse(
        'class A(metaclass=B): pass\n'
        'class D(C, metaclass=E): pass\n'
    )
    mt = MetaclassTransformer()
    mt.visit(m)
    expected = ast.parse(
        'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
        'class A(_py_backwards_six_withmetaclass(B)): pass\n'
        'class D(_py_backwards_six_withmetaclass(E), C): pass\n'
    )
    assert ast.dump(m) == ast.dump(expected)

# Generated at 2022-06-14 02:02:06.498708
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    from typed_ast import ast3 as ast
    from ..utils.tree import dump
    from .base import BaseNodeTransformer
    from .metaclass import MetaclassTransformer

    class Test(unittest.TestCase):
        def test_metaclass(self):
            t = MetaclassTransformer()

            class C(metaclass=int):
                pass

            c = ast.ClassDef(name='C',
                             bases=[],
                             keywords=[ast.keyword(arg='metaclass', value=ast.Num(n=1))],
                             body=[],
                             decorator_list=[])
            c = t.visit(c)

# Generated at 2022-06-14 02:02:17.269570
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Setup
    node = ast.ClassDef(name='A',
                        bases=[],
                        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
                        body=[],
                        decorator_list=[])

    expected = ast.ClassDef(name='A',
                            bases=[],
                            keywords=[],
                            body=[],
                            decorator_list=[],
                            )

    expected.bases.extend(class_bases.get_body(metaclass=ast.Name(id='B', ctx=ast.Load()),
                                               bases=ast.List(elts=[])))
    visitor = MetaclassTransformer()
    visitor.visit(node)


# Generated at 2022-06-14 02:02:25.849075
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent
    from ..utils.source import source_to_ast as to_ast

    source = dedent("""
    class A(metaclass=B):
        pass
    """).strip()
    ast_node = to_ast(source)
    transformed = MetaclassTransformer().visit(ast_node)  # type: ignore

    expected_source = dedent("""
    class A(_py_backwards_six_with_metaclass(B)):
        pass
    """).strip()
    expected_ast_node = to_ast(expected_source)
    assert transformed == expected_ast_node

# Generated at 2022-06-14 02:02:32.508963
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .helper import ast_parse
    source = 'class A(metaclass=B, x=y):\n    pass'
    expected = 'from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B, *[])):\n    pass'
    node = ast_parse(source)
    m = MetaclassTransformer()
    node = m.visit(node)
    result = astunparse.unparse(node)
    assert result == expected

# Generated at 2022-06-14 02:02:39.407969
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import ast
    import typing as t

    class A(six.with_metaclass(str)):
        pass

    class B(six.with_metaclass(str), object):
        pass

    class C(str, six.with_metaclass(str)):
        pass

    @MetaclassTransformer.test_on(A)
    @MetaclassTransformer.test_on(B)
    @MetaclassTransformer.test_on(C)
    def test():
        pass

# Generated at 2022-06-14 02:02:42.875101
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_transformer import parse_to_ast

    syntax = '''class A(metaclass=B): pass'''

# Generated at 2022-06-14 02:02:51.682003
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node1 = ast.parse('class A(metaclass=B):\n    pass')
    node2 = MetaclassTransformer().visit(node1)
    assert ast.dump(node2) == \
        "Module(body=[ImportFrom(module='six', names=[alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0), ClassDef(name='A', bases=[Call(func=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), args=[Name(id='B', ctx=Load())], keywords=[], starargs=None, kwargs=None)], keywords=[], body=[], decorator_list=[])])"

# Generated at 2022-06-14 02:02:53.184397
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.transform import single_pass_transform


# Generated at 2022-06-14 02:02:55.442109
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
        class Foo:
            pass
    """)
    tree = MetaclassTransformer().visit(tree)
    assert MetaclassTransformer._tree_changed



# Generated at 2022-06-14 02:03:04.690495
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import assert_equal_ast

    snippet_before = '''
    from typing import Union

    class A(Union, metaclass=type):
        pass
    '''
    snippet_after = '''
    from typing import Union
    from six import with_metaclass as _py_backwards_six_with_metaclass

    class A(_py_backwards_six_with_metaclass(type), *[Union, ]):
        pass
    '''
    ast_before = ast.parse(snippet_before)
    ast_after = ast.parse(snippet_after)
    transformer = MetaclassTransformer()
    transformer.visit(ast_before)
    assert_equal_ast(ast_before, ast_after)

# Generated at 2022-06-14 02:04:48.082703
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    six_import_ = six_import.get_body()
    class_bases_ = class_bases.get_body(metaclass=ast.Name(id='A', ctx=ast.Load()), bases=[])

    def test_case(before: str, after: str):
        module_node = ast.parse(before)
        mt = MetaclassTransformer()
        mt.visit(module_node)
        assert module_node_to_str(module_node) == after


# Generated at 2022-06-14 02:04:49.825547
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import astor

# Generated at 2022-06-14 02:04:53.421463
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.compiler import compile_snippet
    from .remove_unnecessary_passes import RemoveUnnecessaryPassesTransformer

# Generated at 2022-06-14 02:04:55.359836
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import astor

# Generated at 2022-06-14 02:05:04.098216
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """
    Test that the MetaclassTransformer.visit_ClassDef method performs the expected
    transformation.
    """
    test_transformer = MetaclassTransformer()
    assert test_transformer.tree_changed() == False

    test_classdef = ast.parse('class A(metaclass=B):\n    pass').body[0]
    test_classdef.keywords[0].value = ast.Name(id='C')

    expected_classdef = ast.parse('class A(_py_backwards_six_withmetaclass(C)):\n    pass').body[0]
    expected_classdef.bases = ast.List(elts=[ast.Name(id='C')], ctx=ast.Load())

    actual_classdef = test_transformer.visit(test_classdef)
