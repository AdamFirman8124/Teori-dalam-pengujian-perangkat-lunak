

# Generated at 2022-06-14 01:55:11.021064
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_helpers import parse
    # Original
    src = """
    class A(metaclass=B):
        pass
    """

    # Expected
    trg = """
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """

    node = parse(src)
    MetaclassTransformer().visit(node)
    result = compile(node, '<string>', 'exec')

    ns = {}
    exec(result, ns)
    assert ns['A'].__bases__ == (B,)

# Generated at 2022-06-14 01:55:11.772696
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:15.118767
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:55:22.303626
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.transform_test_support import transform_test_support
    from typed_ast import ast3 as ast
    code = 'class A(metaclass=B): pass'
    tree = ast.parse(code)
    transformer = MetaclassTransformer()
    transformer.visit(tree)

# Generated at 2022-06-14 01:55:25.531596
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import typing

    class TestMetaclassTransformer(MetaclassTransformer):
        def visit_ClassDef(self, node: ast.ClassDef) -> typing.Any:
            return super(TestMetaclassTransformer, self).visit_ClassDef(node)


# Generated at 2022-06-14 01:55:32.567714
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    transformer = MetaclassTransformer(tree)
    new_tree = transformer.visit(tree)
    assert transformer._tree_changed
    assert new_tree == ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)


# Generated at 2022-06-14 01:55:33.428926
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:34.726358
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:36.644288
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..tests.utils import round_trip

# Generated at 2022-06-14 01:55:37.367952
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:42.882665
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """class A(metaclass=B):
        pass"""


# Generated at 2022-06-14 01:55:48.799673
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    ast_ = ast.parse('class A(metaclass=B):\n    pass')
    ast_.body[0] = MetaclassTransformer().visit(ast_.body[0])
    assert ast.dump(ast_) == 'Module(_body=[ClassDef(name=\'A\', bases=[_py_backwards_six_withmetaclass(B, )], body=[Pass()], decorator_list=[])])'

# Generated at 2022-06-14 01:55:56.453927
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    from ..fixer_util import tokenize_module, untokenize, PrintVisitor

    code = textwrap.dedent('''
    class Foo(metaclass=Bar):
        pass
    ''')
    tree = tokenize_module(code)
    visitor = MetaclassTransformer()
    new = visitor.visit(tree)
    assert untokenize(new) == textwrap.dedent('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class Foo(_py_backwards_six_withmetaclass(Bar)):
        pass
    ''')

# Generated at 2022-06-14 01:55:57.295770
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:59.294343
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tr = MetaclassTransformer()

# Generated at 2022-06-14 01:56:04.785861
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    node = ast.parse("""
        class A(metaclass=B):
            pass
    """)
    transformer.visit(node)
    assert ast.dump(node) == ast.dump("""
        import six
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """)

# Generated at 2022-06-14 01:56:12.689093
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    from typed_ast import ast3
    from typing import List, Dict, Tuple

    # Test for the code:
    # class A(metaclass=B):
    #   pass
    tree = ast3.parse("class A(metaclass=B):\n    pass")
    old_bases = tree.body[0].bases
    assert isinstance(old_bases, list) and len(old_bases) == 1
    assert isinstance(old_bases[0], ast3.Name) and old_bases[0].id == 'B'

    transformer = MetaclassTransformer(sys.modules[__name__].__dict__)
    transformer.update(tree)
    new_bases = tree.body[0].bases

# Generated at 2022-06-14 01:56:15.762062
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse("class A(metaclass=B): pass")
    MetaclassTransformer().visit(module)
    module = ast.intervene(module, fixups=['six'])

# Generated at 2022-06-14 01:56:22.673126
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(B): pass')
    assert MetaclassTransformer(None).visit(node) == 'class A(_py_backwards_six_withmetaclass(B)):\n    pass'

    node = ast.parse('class A(metaclass=B): pass')
    assert MetaclassTransformer(None).visit(node) == 'class A(_py_backwards_six_withmetaclass(B)):\n    pass'

# Generated at 2022-06-14 01:56:29.196681
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..transpile import Transpiler
    from .utils import compare_nodes

    module = ast.parse("""
        class A(metaclass=B):
            pass
    """)
    transpiler = Transpiler()
    result = transpiler.transpile_module(module)
    compare_nodes(result, """
        import six
        class A(six.with_metaclass(B)):
            pass
    """)

# Generated at 2022-06-14 01:56:34.118992
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(object):
        pass

    class B(metaclass=A):
        pass

    assert isinstance(B, A)



# Generated at 2022-06-14 01:56:37.441179
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .statement import PrintTransformer
    from .imports import RemoveAllTransformer
    from .base import TransformerVisitor

    source = """class A(metaclass=object):
    def __init__():
        pass"""

# Generated at 2022-06-14 01:56:40.297421
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    six_import_ast = [ast.parse(six_import.to_source())]


# Generated at 2022-06-14 01:56:44.423089
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.test_utils import compare_source
    comparator = compare_source(MetaclassTransformer)
    comparator.test('''
    class A(metaclass=B):
        pass
    ''')

# Generated at 2022-06-14 01:56:45.186415
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:56:46.364321
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:48.019449
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:57:00.996155
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import typed_ast.ast3 as ast

    node = ast.parse("class A(metaclass=B): pass")
    transformer = MetaclassTransformer()
    node = transformer.visit(node)
    assert not transformer._tree_changed

    node = ast.parse("class A(metaclass=B): pass")
    transformer = MetaclassTransformer(target=(2, 7))
    node = transformer.visit(node)
    assert transformer._tree_changed

    node = ast.parse("class A(metaclass=B): pass")
    transformer = MetaclassTransformer(target=(2, 7))
    node = transformer.visit(node)
    assert transformer._tree_changed


# Generated at 2022-06-14 01:57:10.092233
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    metaclass_transformer = MetaclassTransformer()
    tree = ast.parse('class A(metaclass=B, c=C): pass')
    tree = metaclass_transformer.visit(tree)
    assert(metaclass_transformer.tree_changed)

# Generated at 2022-06-14 01:57:19.795731
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    nodes = ast.parse('class A(object): pass')
    transformer = MetaclassTransformer()
    transformed = transformer.visit(nodes)
    result = ast.dump(transformed)

# Generated at 2022-06-14 01:57:28.484804
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """ Tests the constructor of the class MetaclassTransformer. """

    instance = MetaclassTransformer()
    assert isinstance(instance, BaseNodeTransformer)
    assert len(instance.dependencies) == 1
    assert instance.dependencies[0] == 'six'
    assert instance.target == (2, 7)


# Generated at 2022-06-14 01:57:30.324446
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    t = MetaclassTransformer()
    t._tree_changed = False

# Generated at 2022-06-14 01:57:39.664043
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..uparser import parse
    from ..utils.compare_source import compare_source
    from ..utils.tree import tree_to_str

    source = """
    class A(metaclass=B):
        pass
    """
    tree = parse(source)

    transformer = MetaclassTransformer()
    transformer.visit(tree)

    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass"""

    assert compare_source(tree_to_str(tree), expected)



# Generated at 2022-06-14 01:57:42.438684
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.source import source
    from ..utils.unparse import Unparser


# Generated at 2022-06-14 01:57:49.368735
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .util import source_to_node
    source = '''
    class A(metaclass=type):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    class A(_py_backwards_six_withmetaclass(type)):
        pass
    '''
    actual = source_to_node(source, MetaclassTransformer)
    assert str(actual) == expected


# Generated at 2022-06-14 01:57:51.281581
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import compile_source


# Generated at 2022-06-14 01:58:01.855571
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    code = """
    class A(metaclass=B):
        pass
    """
    result = ast.parse(code)
    target = ast.parse(code)
    node = target.body[0]
    mt = MetaclassTransformer(2, 7)
    mt.visit(result)
    assert "from six import with_metaclass as _py_backwards_six_withmetaclass" in result.body[0].value.s
    assert result.body[1].bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert len(result.body[1].bases[0].args) == 2
    assert result.body[1].bases[0].args[0] == node.keywords[0].value
    assert result.body[1].b

# Generated at 2022-06-14 01:58:11.421916
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils import get_node
    from ..sixutils import SixTransformer
    original_code = '''
        class A(metaclass=B):
            pass
        class C(B, metaclass=D):
            pass
        class E(B, C, metaclass=D):
            pass
    '''
    expected_code = '''
        class A(_py_backwards_six_with_metaclass(B)):
            pass
        class C(_py_backwards_six_with_metaclass(D)):
            pass
        class E(_py_backwards_six_with_metaclass(D)):
            pass
    '''
    node = get_node(original_code, 2, 7)
    transformer = SixTransformer(node, [], [MetaclassTransformer])
   

# Generated at 2022-06-14 01:58:16.156493
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    source = """
        class A(metaclass=B):
            def __init__(self):
                pass
    """
    tree = ast.parse(source)
    tree = MetaclassTransformer().visit(tree)
    print(astor.to_source(tree))
    assert MetaclassTransformer().visit(tree) is not None

# Generated at 2022-06-14 01:58:21.485021
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .test_utils import make_dummy_code
    from .test_utils import make_dummy_source_tree

    code = make_dummy_code('')
    tree = MetaclassTransformer().visit(code)

    assert MetaclassTransformer().visit(code) is code
    assert make_dummy_source_tree(code) is tree

# Generated at 2022-06-14 01:58:30.488542
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    import python_backwards.tests.utils as test_utils

# Generated at 2022-06-14 01:58:32.659945
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:58:33.929364
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    print(MetaclassTransformer)

# Generated at 2022-06-14 01:58:38.513874
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    expected = [ast.ImportFrom(module='six', names=[ast.alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0)]
    expected.extend(six_import.get_body())
    actual = MetaclassTransformer().visit_Module(six_import.get_tree())
    assert expected == actual.body


# Generated at 2022-06-14 01:58:42.414719
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    class Dummy(ast.NodeTransformer):
        def visit_Name(self, node):
            return ast.Str(s=node.id)


# Generated at 2022-06-14 01:58:45.283693
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import six

    assert not hasattr(six, 'with_metaclass')

    class A(with_metaclass(type)):
        pass

    assert isinstance(A, type)

# Generated at 2022-06-14 01:58:45.961806
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:58:56.429564
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    t = MetaclassTransformer()
    s = 'class A(metaclass=B):\n    pass'
    tree = ast.parse(s)
    t.visit(tree)
    assert six.PY2
    assert t._tree_changed

# Generated at 2022-06-14 01:59:05.008393
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    module = ast.parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer()
    node = transformer.visit(module)
    assert transformer._tree_changed
    assert transformer.dependencies == ['six']
    assert transformer.target == (2, 7)
    assert str(node) == "from six import with_metaclass as _py_backwards_six_withmetaclass; class A(_py_backwards_six_withmetaclass(B))"

# Generated at 2022-06-14 01:59:06.173410
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    x = MetaclassTransformer()
    x.run()

# Generated at 2022-06-14 01:59:26.086285
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    tree = snippet.extract_ast("""
    class A(metaclass=B):
        pass
    """)

    transformer = MetaclassTransformer()
    expected = snippet.extract_ast("""
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, object)):
        pass
    """)

    assert transformer.visit(tree) == expected



# Generated at 2022-06-14 01:59:29.090107
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:59:34.676909
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = "class A(B, metaclass=C)"
    node = ast.parse(code)
    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)
    expected = "class A(_py_backwards_six_withmetaclass(C, *[B]))"
    assert astor.to_source(new_node).strip() == expected


# Generated at 2022-06-14 01:59:46.365026
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from ..utils.tree import as_str
    from ..utils import assert_equal_ast, to_ast

    code = '''
    class A(metaclass=B):
        pass
    '''

    tree = MetaclassTransformer.transform(code, from_version='2.7')

    assert_equal_ast(
        tree,
        to_ast("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """))

# Generated at 2022-06-14 01:59:56.530828
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent
    from typed_ast import ast27
    from typed_ast.test import test_visitor

    # Test for a good case
    class Test_MetaclassTransformer_visit_ClassDef_metaclass(test_visitor.TestVisitor):
        __test__ = True
        transformer = MetaclassTransformer()
        expected_source = dedent('''\
            def func():
                class A(_py_backwards_six_withmetaclass(metaclass)):
                    pass
        ''')
        expected_node = ast27.parse(expected_source)
        source = dedent('''\
            def func():
                class A(metaclass=metaclass):
                    pass
        ''')
        node = ast27.parse(source)


# Generated at 2022-06-14 02:00:06.923857
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test the method MetaclassTransformer.visit_ClassDef
    """
    # set up test data
    from astor.code_gen import to_source
    from ..utils.snippet import snippet
    from ..utils.ast_utils import compare_ast

    @snippet
    def before():
        class A(metaclass=B):
            pass

    @snippet
    def after():
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class A(_py_backwards_six_with_metaclass(B)):
            pass

    expected_source = to_source(after.get_ast())
    expected_node = after.get_ast()

    # exercise the SUT
    transformer = MetaclassTransformer()
    actual_node = transformer

# Generated at 2022-06-14 02:00:10.131348
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..parser import parse
    from ..compiler import compile
    from ..utils.testing import assert_code_equal


# Generated at 2022-06-14 02:00:11.842596
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:00:17.765214
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.util import load_example_snippet
    from ..utils.util import unparse
    tree = load_example_snippet('metaclass_transformer_example.py')
    transformer = MetaclassTransformer()
    tree = transformer.visit(tree)
    expected = load_example_snippet('metaclass_transformer_example_expected.py')
    assert unparse(tree) == unparse(expected)


# Generated at 2022-06-14 02:00:22.524978
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    expected = ast.parse('from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(metaclassA, superclassA)):\n    pass')

# Generated at 2022-06-14 02:00:49.113415
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .test_utils import get_test_nodes

# Generated at 2022-06-14 02:00:55.741364
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    transformer = MetaclassTransformer()
    module = ast.parse(textwrap.dedent("""
    class A(metaclass=type):
        pass
    """))
    transformer.visit(module)
    lines = "\n".join(astunparse.unparse(node).split("\n")[1:] for node in module.body).split("\n")
    assert lines == [
        "from six import with_metaclass as _py_backwards_six_withmetaclass",
        "class A(_py_backwards_six_withmetaclass(type, )):",
        "    pass",
    ]

# Generated at 2022-06-14 02:01:05.871730
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import parse
    from ..utils.syntax import convert_to_syntax_node
    from ..utils.tree import tree_equals
    from . import TestTransformer

    module = parse("class A(metaclass=B): pass")
    TestTransformer.mock_dependency(module, "six")
    MetaclassTransformer.run_toplevel(module)

    expected = parse("from six import with_metaclass as _py_backwards_six_withmetaclass\n"
                     "class A(_py_backwards_six_withmetaclass(B)): pass")
    assert tree_equals(module, expected)
    assert convert_to_syntax_node(module) == convert_to_syntax_node(expected)

# Generated at 2022-06-14 02:01:14.521209
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import from_source, MetaclassTransformerTester
    tree = from_source('''
    class A(metaclass=B):
        pass''')
    transformer = MetaclassTransformerTester(tree, target=(2, 7))
    transformer.run()
    assert transformer._tree_changed
    assert transformer.new_tree.body[0].body[0].bases[0].func.id == '_py_backwards_six_withmetaclass'

# Generated at 2022-06-14 02:01:20.628438
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    for ver in (2, 7), (3, ):
        if sys.version_info[:2] == ver:
            continue
        source = '''class A(metaclass=B):
            pass'''
        src_ast = parse(source)


# Generated at 2022-06-14 02:01:22.405433
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    metaclass_transformer =  MetaclassTransformer()
    assert metaclass_transformer is not None

# Generated at 2022-06-14 02:01:31.217044
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast

    for version in ('2.6', '2.7'):
        class MetaclassTransformerTester(MetaclassTransformer):
            target = version

        tree = ast.parse('class SingleMetaclass(metaclass=G): pass')
        transformed = MetaclassTransformerTester().visit(tree)
        expected = ast.parse('from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass SingleMetaclass(_py_backwards_six_withmetaclass(G))')
        assert ast.dump(transformed) == ast.dump(expected)

        tree = ast.parse('class MultipleMetaclass(metaclass=G, base1, base2): pass')
        transformed = MetaclassTransformerTester().vis

# Generated at 2022-06-14 02:01:36.931961
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    import ast
    import typed_astunparse as aup

    class TestVisitClassDef(unittest.TestCase):
        def test_visit_ClassDef(self):

            from ..transpilers.metaclass import MetaclassTransformer
            transformer = MetaclassTransformer()

            code = (
                """
                class A():
                    pass
                """)

            parsed = ast.parse(code)
            transformer.visit(parsed)
            expected = (
                """
                from six import with_metaclass as _py_backwards_six_withmetaclass

                class A():
                    pass
                """)
            self.assertEqual(aup.unparse(parsed), expected)



# Generated at 2022-06-14 02:01:42.840196
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.test_utils import run_transformer
    module = run_transformer(MetaclassTransformer, """
        class A(metaclass=B):
            pass
    """)
    assert module.as_string() == """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """

# Generated at 2022-06-14 02:01:46.993091
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    mt = MetaclassTransformer()
    assert 'six' in mt.dependencies
    assert mt.target == (2, 7)
    assert isinstance(mt.visit_Module, types.MethodType)
    assert isinstance(mt.visit_ClassDef, types.MethodType)

# Generated at 2022-06-14 02:02:42.826206
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:52.226173
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import make_local_name_scope
    from .test_utils import make_TestCase_subclass_node
    from ..backports.typing import Tuple

    test_nodes = make_TestCase_subclass_node()
    metaclass_kw = ast.keyword(arg="metaclass", value=ast.Name(id="SetMeta", ctx=ast.Load()))
    metaclass_kw.lineno = 1
    metaclass_kw.col_offset = 4
    test_nodes.keywords.append(metaclass_kw)

    transformed_node = MetaclassTransformer(make_local_name_scope()).visit(test_nodes)

# Generated at 2022-06-14 02:02:53.105359
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:02:56.980346
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..test_util import load_test_data
    from ..visitor import Py2PyCompiler

    metadata, input, expected_output = load_test_data(__file__, 'visit_ClassDef')
    compiler = Py2PyCompiler(code=input, metadata=metadata)
    node = compiler.parse()
    compiler.visit(node)
    out = compiler.format()
    assert out == expected_output

# Generated at 2022-06-14 02:03:05.676495
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:08.757533
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from six import with_metaclass
    from typed_ast import ast3
    from typed_ast.ast3 import ClassDef, Name, Str, parse
    from .base import TransformTestCase


# Generated at 2022-06-14 02:03:18.564954
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    six_import_snippet = six_import.get_body()
    assert isinstance(six_import_snippet, ast.Module)

    old_tree = ast.parse("""
        class A(metaclass=B):
            pass
        """)

    expected_tree = ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """)
    MetaclassTransformer().visit(old_tree)
    assert ast.dump(old_tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:03:28.078787
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # type: ()->None
    from compile_py_backwards.visitors.base import BaseNodeTransformer
    from compile_py_backwards.visitors.six_withmeta import MetaclassTransformer
    from compile_py_backwards.utils.source_code import source_code_from_file

    from typed_ast import ast3 as ast
    from six import with_metaclass

    test_source = """\
    import email

    class A(with_metaclass(email.message.Message)):
        pass
    """

    ast_module = ast.parse(test_source)

    t = MetaclassTransformer()
    t.visit(ast_module)

    src = source_code_from_file(ast_module)
    print(src)
    #assert(False)



# Generated at 2022-06-14 02:03:34.272855
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """Test the MetaclassTransformer for Python 3.4+
    """
    from ...test.test_pgen2 import MetaclassTransformerTestCase
    from ...test.test_pgen2 import MetaclassTransformerTestSuite

    class ClassDefTestCase(MetaclassTransformerTestCase):
        pass

    class TestSuite(MetaclassTransformerTestSuite):
        test_case_class = ClassDefTestCase

    suite = TestSuite()
    suite.run_tests()

# Generated at 2022-06-14 02:03:44.434343
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from copy import copy

    class A(MetaclassTransformer):
        def __init__(self):
            self.tree_changed = False

        def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
            if not node.keywords:
                return node
            metaclass = node.keywords[0].value
            node.bases = class_bases.get_body(metaclass=metaclass,  # type: ignore
                                              bases=ast.List(elts=node.bases))
            node.keywords = []
            self.tree_changed = True
            return node

    t = A()