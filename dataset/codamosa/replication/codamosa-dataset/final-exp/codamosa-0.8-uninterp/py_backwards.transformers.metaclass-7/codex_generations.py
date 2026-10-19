

# Generated at 2022-06-14 01:55:06.382910
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    input = 'class A(metaclass=B): pass'
    expected = 'class A(_py_backwards_six_withmetaclass(B)): pass'
    t = MetaclassTransformer.from_string(input)
    assert t.output == expected



# Generated at 2022-06-14 01:55:14.533271
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    (a, b, c) = (
        ast.Name(id="a"),
        ast.Name(id="b"),
        ast.Name(id="c"),
    )
    expected = ast.ClassDef(
        name="A",
        bases=[
            ast.Call(
                func=ast.Name(id="_py_backwards_six_with_metaclass"),
                args=[ast.Name(id="a"), ast.Name(id="b"), ast.Name(id="c")],
                keywords=[],
                starargs=None,
                kwargs=None,
            )
        ],
        keywords=[],
        body=[],
        decorator_list=[],
    )

# Generated at 2022-06-14 01:55:25.601910
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    transformer = MetaclassTransformer(None)
    module = ast.Module([])  # type: ast.Module
    classdef = ast.ClassDef(name="A",
                            keywords=[ast.keyword(arg="metaclass",
                                                  value=ast.Name(id="B",
                                                                 ctx=ast.Load()))],
                            bases=[],
                            body=[],
                            decorator_list=[])  # type: ast.ClassDef
    module.body = [classdef]  # type: ignore

    module = transformer.visit(module)

    assert transformer._tree_changed is True
    assert len(classdef.bases) == 1

# Generated at 2022-06-14 01:55:31.323263
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import io
    import unittest

    from six import assertRegex
    from ast_tools.passes.six import MetaclassTransformer

    class TestMetaclassTransformer(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None


# Generated at 2022-06-14 01:55:37.859870
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_visitor import TestVisitor
    s = '''
    class Bar(metaclass=abc.ABCMeta):
        pass
    '''
    node = TestVisitor.parse(s, mode='exec')
    MetaclassTransformer(node, None).visit_Module(node)
    assert TestVisitor.compile(node) == \
    '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class Bar(_py_backwards_six_withmetaclass(abc.ABCMeta)):
        pass
    '''

# Generated at 2022-06-14 01:55:42.531736
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    from ..utils.source import source_to_ast

    class DummyLogger:
        def debug(self, *args, **kwargs):
            pass

    t = MetaclassTransformer(sys.version_info, DummyLogger())


# Generated at 2022-06-14 01:55:43.141947
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:53.474687
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test that when the following code:
        class A(metaclass=B):
            pass
    Is changed to:
        class A(_py_backwards_six_with_metaclass(B))
    """
    tree = ast.parse('class A(metaclass=B): pass')
    MetaclassTransformer().visit(tree)
    result = ast.dump(tree)

# Generated at 2022-06-14 01:56:00.030175
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # type: () -> None
    source = '''
    class X(metaclass=type):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class X(_py_backwards_six_withmetaclass(type, )):
        pass
    '''
    transformed = MetaclassTransformer().visit(ast.parse(source))
    assert ast.dump(transformed, annotate_fields=False) == expected

# Generated at 2022-06-14 01:56:09.067376
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import Dict, List
    import six
    import astor

    class UnitTestTransformer(MetaclassTransformer):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._tree_changed = False

        @property
        def tree_changed(self):
            return self._tree_changed

    @six.add_metaclass(UnitTestTransformer)
    class A(object):
        pass

    assert UnitTestTransformer.tree_changed is True


# Generated at 2022-06-14 01:56:19.319625
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ... import parse
    from ... import dump
    from .modifiers import BaseModifier
    module = parse("class A(metaclass=B): pass")
    modifier = BaseModifier(MetaclassTransformer())
    modifier.visit(module)
    # print(dump(module))
    assert dump(module) == (
        'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
        'class A(_py_backwards_six_withmetaclass(B)):\n'
        '    pass'
    )

# Generated at 2022-06-14 01:56:19.946073
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    pass

# Generated at 2022-06-14 01:56:31.645413
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Test to see if MetaclassTransformer correctly transforms a class
    # definition with a metaclass to a class using six's
    # with_metaclass function.
    from ast import parse
    from .util import round_trip

    source = """
            class A(metaclass=B):
                pass
            """
    expected_source = """
            from six import with_metaclass as _py_backwards_six_withmetaclass
            
            class A(_py_backwards_six_withmetaclass(B)):
                pass
            """
    result = round_trip(source, MetaclassTransformer)

    # Test that the MetaclassTransformer has correctly imported the
    # six module and has transformed the class definition.
    assert expected_source == result[0].strip()

# Generated at 2022-06-14 01:56:41.030561
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from ..utils.test_utils import transform, compare_module_ast, round_trip
    from ..utils.compat import builtins, six

    new_module = '''
    import six

    class C(metaclass=six.with_metaclass(M, N)):
        pass

    class D(A, B, metaclass=six.with_metaclass(M, N)):
        pass
    '''

    compare_module_ast(
        new_module,
        transform(ast3.parse(new_module), MetaclassTransformer)
    )

    compare_module_ast(
        new_module,
        transform(
            round_trip(new_module),
            MetaclassTransformer
        )
    )


# Generated at 2022-06-14 01:56:53.131445
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils import loader
    
    module = loader.load_code('''
    import six
    class A(metaclass=six.with_metaclass):
        pass
    ''')
    transformer = MetaclassTransformer()
    module = transformer.visit(module)

# Generated at 2022-06-14 01:57:05.220764
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    node = ast.ClassDef(name='A', bases=[ast.Name(id='B', ctx=ast.Load())], keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='C', ctx=ast.Load()))], body=[], decorator_list=[])
    node = MetaclassTransformer(node).visit_ClassDef(node)
    assert isinstance(node, ast.ClassDef)
    assert node.bases
    assert len(node.bases) == 1
    assert isinstance(node.bases[0], ast.Call)
    assert isinstance(node.bases[0].func, ast.Name)
    assert node.bases[0].func.id == '_py_backwards_six_withmetaclass'


# Generated at 2022-06-14 01:57:09.297342
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    assert MetaclassTransformer().visit(ast.parse(textwrap.dedent('''\
    class A(metaclass=B):
        pass'''))) == ast.parse(textwrap.dedent('''\
    class A(_py_backwards_six_withmetaclass(B)):
        pass'''))

# Generated at 2022-06-14 01:57:11.445063
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:57:20.953970
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    import textwrap
    from ..utils.fixtures import context_module
    from ..visitor import ContextSensitiveTransformer
    from ..utils.inspect import source_inspect

    tree = ast.parse(textwrap.dedent("""
        class A(metaclass=B):
            pass
    """), mode='exec')

    compiler = ContextSensitiveTransformer(tree)
    compiler.add_transformers(MetaclassTransformer)
    with context_module(compiler.module) as context:
        compiled_code = compiler.compile()
        print(compiled_code)
        source_inspect(compiled_code)
        context['A']()

# Generated at 2022-06-14 01:57:22.746842
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A():
        pass

    class B(metaclass=A):
        pass


# Generated at 2022-06-14 01:57:32.089492
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    src = """
    class A(metaclass=B):
        pass
    """
    expected_result = """
    class A(_py_backwards_six_with_metaclass(B))
        pass
    """

    transformed_node = MetaclassTransformer().visit(ast.parse(src))
    assert astor.to_source(transformed_node).strip() == expected_result.strip()

# Generated at 2022-06-14 01:57:38.807408
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import ast_from_snippet, ast_equals_snippet, ast_equals_node
    from .extract_metaclasses import ExtractMetaclassesTransformer
    from .extract_dependencies import ExtractDependenciesTransformer
    from ..utils.tree import print_ast

    transformer = MetaclassTransformer()

# Generated at 2022-06-14 01:57:43.220734
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...testing import assert_text_snippet
    assert_text_snippet(MetaclassTransformer.visit_ClassDef,
        """
        class A(metaclass=B):
            pass
        """,
        """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """,
    )

# Generated at 2022-06-14 01:57:52.561086
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from six import add_metaclass
    import sys
    import astor
    import textwrap

    src = textwrap.dedent("""
    class A:
        pass
    """)
    tree = ast.parse(src)

    cls = tree.body[0]

    cls.keywords = [ast.keyword(arg="metaclass", value=ast.Name(id="type", ctx=ast.Load()))]

    transformer = MetaclassTransformer()
    transformer.visit(tree)

    as_str = astor.to_source(tree)

    assert as_str == "class A(_py_backwards_six_withmetaclass(type)):\n    pass"



# Generated at 2022-06-14 01:58:02.231734
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .generic import GenericTransformer

    code = "class SomeClass(metaclass=ABCMeta):\n    pass"
    tree = ast.parse(code)

    # visit_ClassDef should be called twice
    mt = MetaclassTransformer()
    mt.visit_Module(tree)
    assert mt.visit_ClassDef.call_count == 1

    # test case 2
    code = "class SomeClass(metaclass=ABCMeta, other=1):\n    pass"
    tree = ast.parse(code)

    mt = MetaclassTransformer()
    mt.visit_Module(tree)
    assert mt.visit_ClassDef.call_count == 1

    # test case 3
    code = "class SomeClass(metaclass=ABCMeta, other=1):\n    pass"
    tree

# Generated at 2022-06-14 01:58:11.760797
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import context
    c = context('', target_version=(2, 7))
    c.check('class A(metaclass=B): pass', 'from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(B)):\n    pass\n')
    c.check('class A(object, metaclass=B): pass', 'from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(B), object):\n    pass\n')

# Generated at 2022-06-14 01:58:19.602921
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import typing
    import six
    import re
    from astor.code_gen import to_source

    tree = ast.parse('''
        import typing
        class A(metaclass=typing.GenericMeta):
            pass
        class B(A, metaclass=typing.GenericMeta):
            pass
    ''')

    m = MetaclassTransformer()
    m.visit(tree)


# Generated at 2022-06-14 01:58:22.615681
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.transformer import print_tree
    from ..utils.transformer import to_source
    from ..utils.transform import LocalsDict
    from .six import make_six_transformer
    from .six import make_name_transformer


# Generated at 2022-06-14 01:58:24.614193
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..unittest_tools import assert_compiled_output


# Generated at 2022-06-14 01:58:31.276935
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import test_utils
    from six import with_metaclass as _py_backwards_six_withmetaclass
    input_code = """
    class A(metaclass=B):
        pass"""
    expected_code = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass"""
    test_utils.compare(MetaclassTransformer, input_code, expected_code)

# Generated at 2022-06-14 01:58:43.969274
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse('''class A(metaclass = B, *args): pass''')
    s = MetaclassTransformer()
    s.visit(tree)

# Generated at 2022-06-14 01:58:51.018322
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    s = 'class A:pass'
    tree = ast.parse(s)
    m = MetaclassTransformer()
    tree2 = m.visit(tree)
    assert ast.dump(tree2)==ast.dump(tree)

    s = 'class A(metaclass=B):pass'
    tree = ast.parse(s)
    m = MetaclassTransformer()
    tree2 = m.visit(tree)
    expected_tree = ast.parse('class A(_py_backwards_six_withmetaclass(B)):pass')
    assert ast.dump(tree2)==ast.dump(expected_tree)

# Generated at 2022-06-14 01:58:55.377892
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    src = """
        class A(metaclass=B):
            pass
        """
    assert MetaclassTransformer(src).result == """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B, )):
            pass
        """

# Generated at 2022-06-14 01:59:02.630495
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import roundtrip

    snippet = 'class A(metaclass=B):\n    pass'
    result = 'from six import with_metaclass as _py_backwards_six_withmetaclass\n' \
             'class A(_py_backwards_six_withmetaclass(B)):\n    pass'
    assert roundtrip(snippet, MetaclassTransformer) == result

# Generated at 2022-06-14 01:59:04.420300
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typing
    import astor


# Generated at 2022-06-14 01:59:06.297552
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 01:59:08.592331
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import round_trip
    from ..utils.utils import get_ast_body
    from .visitor import Python2to3Parser

# Generated at 2022-06-14 01:59:17.250176
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node_contents = """
        class A(metaclass=B):
            pass
        """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """
    node = ast.parse(node_contents)
    MetaclassTransformer.run_test(node_contents, node, expected)

# Generated at 2022-06-14 01:59:22.989009
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # type: () -> None
    class BaseTransformerTest(TransformerTest):
        transformer = MetaclassTransformer
        target = (2, 7)
        goal = 2

    BaseTransformerTest.test_node(
        """
        class A(object, metaclass=B, foo=bar):
            pass
        """
    )



# Generated at 2022-06-14 01:59:31.424621
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import asttokens, ast
    from py_backwards.transformers.metaclass import MetaclassTransformer

    code = """\
    class A(metaclass=B):
        pass
    """
    expected_source = six_import.get_code() + """\
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """
    tree = asttokens.ASTTokens(code, parse=True).tree
    transformer = MetaclassTransformer(tree)
    source = transformer.visit(tree).tokens.get_text()
    assert source == expected_source

# Generated at 2022-06-14 01:59:54.869271
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import run_transform
    class TestClass(object):
        def __init__(self):
            pass
        def __call__(self):
            pass
        def __new__(self):
            pass
        def __metaclass__(self):
            pass
    import six
    with_metaclass = six.with_metaclass

    # test with keyword (2.7)
    # test class instance
    test = TestClass()
    expected = TestClass
    actual = run_transform(test, MetaclassTransformer)
    print(actual)
    assert expected == actual
    # test class instance with attribute
    test = TestClass
    expected = TestClass
    actual = run_transform(test, MetaclassTransformer)
    print(actual)
    assert expected == actual
    # test class with __met

# Generated at 2022-06-14 01:59:55.985585
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:06.509102
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source
    from . import fix_missing_locations
    from .base import BaseNodeTransformerTest

    class Test(BaseNodeTransformerTest):
        transformer = MetaclassTransformer

        def test_metaclass(self):
            node = ast.parse(source("""
                class A(metaclass=B): pass
            """))
            new_node = self.transform(node)
            self.assertEqual(source(new_node), source("""
                from six import with_metaclass as _py_backwards_six_withmetaclass
                class A(_py_backwards_six_withmetaclass(B)): pass
            """))

        def test_normal_class(self):
            node = ast.parse(source("""
                class A(B): pass
            """))

# Generated at 2022-06-14 02:00:08.823182
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...codegen.ast import ast_parse


# Generated at 2022-06-14 02:00:12.679802
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(metaclass=type):
        pass

    tree = ast.parse(inspect.getsource(A))
    MetaclassTransformer().visit(tree)
    eval(compile(tree, '<test>', mode='exec'))



# Generated at 2022-06-14 02:00:21.168872
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from .basetest import BaseNodeTest, compile_function_with_call
    
    class Test(BaseNodeTest):
        target = MetaclassTransformer
        transform = MetaclassTransformer.visit_ClassDef

        cases = [
            (
                """
                class A(a):
                    pass
                """,
                """
                class A(a):
                    pass
                """
            ),
            (
                """
                class A(metaclass=A):
                    pass
                """,
                """
                class A(_py_backwards_six_withmetaclass(A, *[])):
                    pass
                """,
            ),
        ]
    
    compile_function_with_call(MockTarget, (ast3, ), {'six': six})
    Test

# Generated at 2022-06-14 02:00:34.460967
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import copy
    import six

    class B(type):
        pass

    class A(metaclass=B):
        pass

    initial_tree = ast.parse(dedent('''
        from six import with_metaclass
        class B():
            pass
        class A(metaclass=B):
            pass
    ''').strip())

    expected_tree = copy.deepcopy(initial_tree)
    expected_bases = expected_tree.body[-1].bases
    expected_bases.elts = [
        ast.Name(id='with_metaclass', ctx=ast.Load())
    ]
    expected_bases.elts.append(ast.Name(id='B', ctx=ast.Load()))


# Generated at 2022-06-14 02:00:38.997479
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source
    from .. import compile

    source = source('')
    to_compile = '''
        class A(metaclass=B):
            pass
    '''

    module = compile(source + to_compile,
                     MetaclassTransformer)
    result = source.get_value()

    # module is a list of strings, where each string is a line in the source code
    assert result[-21:] == '''
        class A(_py_backwards_six_withmetaclass(B)):
            pass
'''



# Generated at 2022-06-14 02:00:49.676072
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # A 'module' node representing:
    #  class Base(metaclass=abc.ABCMeta):
    #      pass
    module = ast.Module(
        body=[
            ast.ClassDef(
                name='Base',
                bases=[
                    ast.Attribute(
                        attr='ABCMeta',
                        value=ast.Name(id='abc', ctx=ast.Load()),
                        ctx=ast.Load()
                    )
                ],
                keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='ABCMeta', ctx=ast.Load()))],
                body=[ast.Pass()],
            )
        ]
    )

    MetaclassTransformer.run_on(module)


# Generated at 2022-06-14 02:00:54.325326
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = """
    class A(metaclass=B):
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, )):
        pass
    """
    _test_transformer(MetaclassTransformer, source, expected)

# Generated at 2022-06-14 02:01:32.498129
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.tester import run_node_visitor
    from ..utils.fixtures import ClassDef, keyword, load_code_snippet
    from ..utils.tree_compare import tree_equal
    metaclass = keyword('metaclass', value='six')
    classdef  = ClassDef('Foo', keywords=[metaclass])
    expected  = load_code_snippet('six.with_metaclass')
    assert tree_equal(expected,
                      run_node_visitor(metaclass, MetaclassTransformer))
    assert tree_equal(expected,
                      run_node_visitor(classdef, MetaclassTransformer))

# Generated at 2022-06-14 02:01:33.484481
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:01:44.898005
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import ClassDef, Assign, Mod, Module, Compare, Num, Name, Eq, Load, BinOp, Add, Str, \
        Call, Attribute, AugAssign, Subscript, Sub, Store, Tuple, List, NameConstant, Ellipsis, Index, ListComp, \
        GeneratorExp, SetComp, DictComp, Set, Dict, Starred, Expr, Parser, parse, dump, AST
    ast_module = parse('''class A(metaclass=B):pass''')
    print(dump(ast_module))
    # Using `ast.NodeTransformer` causes unexpected behavior - `visit` methods are called twice.
    # To mitigate that we use `BaseNodeTransformer` instead.
    metaclass_transformer = MetaclassTransformer()
    transformed_ast_

# Generated at 2022-06-14 02:01:56.355421
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import asserts
    from ..utils.source import source2ast


    assert_tree_changed = asserts.assert_tree_changed(MetaclassTransformer)
    assert_tree_unchanged = asserts.assert_tree_unchanged(MetaclassTransformer)

    # should handle class with keywords
    assert_tree_changed(
        'class A(metaclass=B): pass',
        """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """
    )
    # should handle class without keywords
    assert_tree_unchanged(
        'class A(object): pass'
    )



# Generated at 2022-06-14 02:01:57.146659
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:06.694284
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class _TestMetaclassTransformer_visit_ClassDef(unittest.TestCase):
        def _do_test(self, code, expected):
            node = ast.parse(code)
            transformer = MetaclassTransformer()
            transformed_node = transformer.visit(node)
            expected_node = ast.parse(expected)
            self.assertEqual(ast.dump(transformed_node), ast.dump(expected_node))

        def test_01(self):
            # with metaclass on class definition
            code = "class A(metaclass=B): pass"
            expected = "from six import with_metaclass as _py_backwards_six_withmetaclass; class A(_py_backwards_six_withmetaclass(B)): pass"

# Generated at 2022-06-14 02:02:16.836415
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import parse
    from . import six_import, class_bases
    from .base import BaseNodeTransformer
    from .six_import_transformer import SixImportTransformer
    from .six_with_metaclass_transformer import SixWithMetaclassTransformer

    # __enter__ method of class contextlib.contextmanager
    input = """
    class A(metaclass=B):
        pass
    """
    expected = """
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """
    et = MetaclassTransformer()
    result = et.visit(parse(input))
    assert(expected == astunparse.unparse(result))

# Generated at 2022-06-14 02:02:23.775075
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Create AST tree
    tree = ast.parse("""
    class A(B):
        pass

    class B(C):
        __metaclass__ = D
    """) # type: ast.Module
    # Create MetaclassTransformer
    transformer = MetaclassTransformer()
    # Transform AST tree
    ast.fix_missing_locations(transformer.visit(tree))
    # Test case

# Generated at 2022-06-14 02:02:30.507184
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()
    mt.visit(ast.parse("""
    class A(metaclass=Test):
        pass
    """))
    assert mt._tree_changed == True
    expected_node = ast.parse("""
    class A(_py_backwards_six_with_metaclass(Test)):
        pass
    """)
    assert ast.dump(mt._tree, include_attributes=False) == \
        ast.dump(expected_node, include_attributes=False)



# Generated at 2022-06-14 02:02:31.912672
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .. import compile

# Generated at 2022-06-14 02:03:51.816560
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse('import six; class A(metaclass=B): pass')
    MetaclassTransformer().visit(module)
    module = ast.parse('import six; class A(metaclass=B): pass')
    class A(metaclass=B): pass
    import six
    """
        assert ast.dump(module) == ast.dump(metaclass_module)
    """

# Generated at 2022-06-14 02:04:02.545347
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
  from .base import BaseTestTransformer
  from astunparse import unparse
  class TestMetaclassTransformer(BaseTestTransformer):
    transformer = MetaclassTransformer
  tmt = TestMetaclassTransformer()

  for klass_tuple in tmt.iter_test_templates('ClassDef'):
    with TestMetaclassTransformer.subTest(klass_tuple=klass_tuple):
      klass = klass_tuple[0]()
      # print('======= Transforming:')
      # print(unparse(klass.ast_tree).rstrip())
      new_ast = tmt.transform(klass.ast_tree)
      # print('======= To:')
      # print(unparse(new_ast).rstrip())
      # print('======= Expected:')

# Generated at 2022-06-14 02:04:10.689612
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse('''
        class Foo(bases, metaclass=A):
            pass
    ''')
    _tree_changed = False
    new_tree = MetaclassTransformer().visit(tree)
    assert_equal(
        ast.dump(new_tree.body[0]),
        ast.dump(ast.parse('''
            class Foo(_py_backwards_six_withmetaclass(A, *bases)):
                pass
        ''').body[0])
    )

# Generated at 2022-06-14 02:04:17.370083
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source

    source = source('''
    class A(metaclass=B):
        pass
    ''')
    assert MetaclassTransformer().visit(source) == source('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    
    class A(_py_backwards_six_withmetaclass(B, )):
        pass
    ''')

# Generated at 2022-06-14 02:04:27.770729
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from six import PY2, PY3
    from ..six_extra import get_ast_args
    from typing import cast

    def transform(code: str, six_import: str='') -> str:
        module = ast.parse(code)
        if six_import:
            module.body.insert(0, ast.parse(six_import).body[0])

        MetaclassTransformer(target=(2, 7)).visit(module)
        return cast(str, ast.unparse(module))


# Generated at 2022-06-14 02:04:29.677493
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor  # type: ignore
    from .utils import evaluate_transformation, evaluate_source


# Generated at 2022-06-14 02:04:34.683383
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    _source = """
    class A(metaclass=B):
        pass
    """
    _expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass


    class A(_py_backwards_six_withmetaclass(B,
    )):
        pass
    """
    from ..utils.test_helpers import normalize_ast, run_test
    run_test(_source, _expected, MetaclassTransformer)

# Generated at 2022-06-14 02:04:42.528317
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from _ast import ClassDef, CopyFrom, Expr, Name, Load, Arg, List

    # class A(metaclass=B): pass
    classdef_cls = ClassDef(name="A", bases=[Expr(value=Name(id="B", ctx=Load()))], keywords=[CopyFrom(arg="metaclass", value=Name(id="B", ctx=Load()))], body=[], decorator_list=[], lineno=0, col_offset=0)
    classdef_exp = ClassDef(name="A", bases=[Expr(value=_py_backwards_six_withmetaclass(Name(id="B", ctx=Load()), *[]))], keywords=[], body=[], decorator_list=[], lineno=0, col_offset=0)

   

# Generated at 2022-06-14 02:04:48.365436
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast

    node = ast.ClassDef(name='A',
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='B',
                                                             ctx=ast.Load()))],
                        body=[],
                        decorator_list=[],
                        bases=[])

    ret = MetaclassTransformer().visit_ClassDef(node)
    assert ret.bases[0].args[0].value.id == 'B'

# Generated at 2022-06-14 02:04:53.602794
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    assert (compile(ast.parse("""
        class A(metaclass=B):
            pass
    """), filename="test", mode="exec") ==
            compile(ast.parse("""
        class A(_py_backwards_six_with_metaclass(B)):
            pass
    """), filename="test", mode="exec"))