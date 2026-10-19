

# Generated at 2022-06-14 01:55:12.337375
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    from ..testing_utils import assert_tree, parse

    code = """class A(object):\n    pass"""
    expected = """class A(_py_backwards_six_withmetaclass(object, )):\n    pass"""
    assert_tree(MetaclassTransformer, code, expected)

    code = """class B(A, metaclass=A):\n    pass"""
    expected = """class B(_py_backwards_six_withmetaclass(A, A)):\n    pass"""
    assert_tree(MetaclassTransformer, code, expected)

    code = """class F(A, B, C, D, E, metaclass=A):\n    pass"""

# Generated at 2022-06-14 01:55:22.800197
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.fixtures import make_snippet
    import astor
    node = make_snippet('''
    class A(metaclass=B):
        pass
    ''', parser='python3')
    MetaclassTransformer('2.7').visit(node)
    assert astor.to_source(node) == make_snippet('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B),):
        pass
    ''', parser='python3')

# Generated at 2022-06-14 01:55:28.759493
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from _py_backwards_utils.testing import get_test_cases

    cases = get_test_cases(
        MetaclassTransformer, mode='function',
        dir_path=__path__[0],
        ignore_files=[__file__]
    )

    t = MetaclassTransformer()

    for c in cases:

        tree = c.before
        t.visit(tree)
        after = c.after

        actual = astor.to_source(tree)
        assert actual == after

# Generated at 2022-06-14 01:55:32.635582
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    classdef = ast.parse('class NewClass(metaclass=OldClass):\n pass')
    assert transformer.visit(classdef) == ast.parse(
        'from six import with_metaclass as _py_backwards_six_withmetaclass; '
        'class NewClass(_py_backwards_six_withmetaclass(OldClass)):\n pass')

# Generated at 2022-06-14 01:55:33.470077
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:55:44.190312
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

    class A(object):
        pass

    class B(object):
        pass

    class C(object):
        pass

    class D(object):
        pass

    class E(object):
        pass

    class F(object):
        pass

    class G(object):
        pass

    class H(object):
        pass

    class I(object):
        pass

    class J(object):
        pass

    class K(object):
        pass

    class L(object):
        pass

    class M(object):
        pass

    class N(object):
        pass

    class O(object):
        pass

    class P(object):
        pass

    class Q(object):
        pass

    class R(object):
        pass

    class S(object):
        pass


# Generated at 2022-06-14 01:55:48.125531
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse("class A(metaclass=B): pass")
    tr = MetaclassTransformer()
    tr.visit(node)
    assert tr._tree_changed


# Example for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:54.265964
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.functions import visit_module

    module = ast.parse('class B(metaclass=A):\n    pass')
    MetaclassTransformer(module).visit(module)

    assert visit_module(module) == 'from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass B(_py_backwards_six_withmetaclass(A)):\n    pass'

# Generated at 2022-06-14 01:55:59.610512
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import inspect

    source = inspect.getsource(test_MetaclassTransformer_visit_ClassDef).split('\n')
    source.insert(1, 'from six import with_metaclass')
    tree = ast.parse('\n'.join(source))
    tree = MetaclassTransformer().visit(tree)
    result = compile(tree, '<string>', 'exec')
    exec(result)

# Generated at 2022-06-14 01:56:09.897967
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    from ..utils.source import source_to_module, source_to_ast
    module = source_to_module(textwrap.dedent('''\
    from six import with_metaclass as _py_backwards_six_with_metaclass
    
    
    class A(metaclass=B):
        pass'''))
    tr = MetaclassTransformer()
    tr.visit(module)
    assert __name__ == "__main__"

# Generated at 2022-06-14 01:56:21.470778
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test MetaclassTransformer.visit_ClassDef method
    """
    from ..utils import ast_dump

    src = """class Klass(metaclass=M):
    def method(self):
        pass
"""
    tree = ast.parse(src)
    transformer = MetaclassTransformer()
    tree = transformer.visit(tree)
    tree_str = ast_dump(tree)

# Generated at 2022-06-14 01:56:32.836341
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    six = ast.parse("from six import with_metaclass as _py_backwards_six_withmetaclass")
    sample = ast.parse("class A(metaclass=B): pass")
    expected = ast.Module(body=[
        six.body[0],
        ast.ClassDef(name='A', bases=[
            ast.Call(func=ast.Name(id='_py_backwards_six_withmetaclass', ctx=ast.Load()),
                      args=[ast.Name(id='B', ctx=ast.Load())], keywords=[], starargs=None, kwargs=None)
        ], keywords=[], body=[], decorator_list=[])
    ])
    transformer = MetaclassTransformer()
    assert transformer.visit(sample) == expected

# Generated at 2022-06-14 01:56:39.689749
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import AssignName
    from .base import CompilerTestCase
    
    class TestMetaclassTransformer_visit_ClassDef(CompilerTestCase):
        def test_MetaclassTransformer(self):
            module = ast.parse("""
            class A(metaclass=B):
                pass
            """)
            transformer = MetaclassTransformer()
            transformer.visit(module)
            self.assertEqual(
                transformer.get_snippets(),
                ['six', 'class_bases']
            )
            self.assertEqual(
                transformer.get_classes(),
                ['_py_backwards_six_withmetaclass']
            )

# Generated at 2022-06-14 01:56:41.343254
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:56:42.842972
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast import parse

# Generated at 2022-06-14 01:56:54.481152
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("class A(metaclass=B): pass")
    transform = MetaclassTransformer()
    
    insert_six_import_asserts = ast.Assign(
        targets=[ast.Name(id='insert_six_import_asserts', ctx=ast.Store())], value=ast.List(
            elts=[ast.Tuple(elts=[
                ast.Str(s='from six import with_metaclass as _py_backwards_six_withmetaclass'),
                ast.Tuple(elts=[], ctx=ast.Load())], ctx=ast.Store())]
        ))

# Generated at 2022-06-14 01:57:06.414088
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List, Tuple
    
    
    global _py_backwards_six_withmetaclass, _six_metaclass
    
    # Add type annotations
    _py_backwards_six_withmetaclass: Any = None
    _six_metaclass: Any = None
    
    if _py_backwards_six_withmetaclass is None:
        _py_backwards_six_withmetaclass = _py_backwards_six_withmetaclass(type)
    
    if _six_metaclass is None:
        _six_metaclass = _six_metaclass(type)
    
    class A(metaclass=B):
        pass
    

# Generated at 2022-06-14 01:57:18.651189
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..context import Context
    from ..utils.source import source_to_code
    from ..nodes import ast_parse

    context = Context(target=(2, 7))
    transformer = MetaclassTransformer(context)

    # Test creating an instance of MetaclassTransformer
    code = source_to_code(
        """
        class A(B):
            pass
        """)
    tree = ast_parse(code)
    assert transformer.visit(tree)

    # Test creating an instance of MetaclassTransformer where the class
    # definition doesn't have a metaclass keyword
    code = source_to_code(
        """
        class A(B, metaclass=C):
            pass
        """)
    tree = ast_parse(code)
    assert transformer.visit(tree)

    # Test creating

# Generated at 2022-06-14 01:57:20.143567
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:57:28.751512
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    """Test the method visit_Module of the class MetaclassTransformer."""
    module = ast.parse('''class A(metaclass=metaclass):\n    pass''')
    MetaclassTransformer().visit(module)
    result = ast.fix_missing_locations(ast.parse('''from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(metaclass)):\n    pass\n'''))
    assert module == result

# Generated at 2022-06-14 01:57:37.990271
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    # type: () -> None
    """Class MetaclassTransformer should not change node if there is no keywords
    """
    tree = ast.parse("""class A:
    pass""")
    node_transformer = MetaclassTransformer()
    new_tree = node_transformer.visit(tree)
    assert ast.dump(tree) == ast.dump(new_tree)



# Generated at 2022-06-14 01:57:43.818885
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class MockMetaclassTransformer(MetaclassTransformer):
        def __init__(self, code):
            self.tree = ast.parse(code)
            self._tree_changed = False

    tree = ast.parse(textwrap.dedent("""
        class A(metaclass=int):
            pass
    """))

    expected_tree = ast.parse(textwrap.dedent("""\
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(int)):
            pass"""))

    transformer = MockMetaclassTransformer(textwrap.dedent("""\
        class A(metaclass=int):
            pass"""))
    result = transformer.visit(transformer.tree)
    assert_

# Generated at 2022-06-14 01:57:51.196575
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..testing.utils import get_example_ast
    from ..utils.tree import print_tree

    example_str = \
        """
        class A(metaclass=B):
            pass
        """
    example_ast = get_example_ast(example_str)

    transformer = MetaclassTransformer()
    new_ast = transformer.visit(example_ast)
    assert transformer.tree_changed()

    # print('Example:')
    # print_tree(example_ast)
    # print('Transformed:')
    # print_tree(new_ast)

# Generated at 2022-06-14 01:57:59.888993
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_equal_ignore_ws, transform_and_compile

    code = """
    class A(B, metaclass=C):
        pass
    """

    def test_A():
        assert isinstance(A, C)  # type: ignore

    assert_equal_ignore_ws(transform_and_compile(code, MetaclassTransformer), """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(C, B)):
        pass


    def test_A():
        assert isinstance(A, C)
    """)

# Generated at 2022-06-14 01:58:07.059242
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    element = ast.ClassDef(name='A',
                           bases=[],
                           keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
                           body=[],
                           decorator_list=[],
                           )
    node = ast.Module(body=[element])
    assert six_import.get_body() == MetaclassTransformer.transform(node).body[0]
    assert element == MetaclassTransformer.transform(node).body[1]

# Generated at 2022-06-14 01:58:16.227486
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.testing import assert_type
    from ..utils.testing import assert_tree

    tree = compile("from six import with_metaclass as _py_backwards_six_withmetaclass; class A: pass", '', 'exec')
    assert_type(tree, ast.Module, 1)
    tree = MetaclassTransformer.visit(tree)
    assert_type(tree, ast.Module, 1)
    tree = compile("from six import with_metaclass as _py_backwards_six_withmetaclass; class B(metaclass=A): pass", '', 'exec')
    assert_type(tree, ast.Module, 2)
    tree = MetaclassTransformer.visit(tree)
    assert_type(tree, ast.Module, 3)
    # Ensure the changes have been applied


# Generated at 2022-06-14 01:58:26.526150
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from typing import List

    class A:
        pass

    class B(object):
        pass

    class C:
        pass

    class D:
        pass

    class E(object):
        pass

    class F(object):
        pass

    class G(F, object):
        pass

    def func():
        class A(metaclass=D):
            pass

        class B(object, metaclass=F):
            pass

        class C(G, metaclass=D):
            pass

        class D(object, metaclass=E):
            pass

        class E(object, metaclass=A):
            pass

        class F(E, object, metaclass=B):
            pass

    mod = ast.parse(func.__code__)
   

# Generated at 2022-06-14 01:58:33.368122
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse(dedent('''
        class MyClass(metaclass=MyMetaclass,
                      baz=bar):
            pass
    '''))
    transformer = MetaclassTransformer()
    actual = transformer.visit(node)
    expected = ast.parse(dedent('''
        class MyClass(_py_backwards_six_with_metaclass(MyMetaclass)):
            pass
    '''))
    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 01:58:35.068418
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    actual = compile(parse("""
    class A(metaclass=B):
        pass
    """), "filename", mode="exec")
    exec(actual)

# Generated at 2022-06-14 01:58:46.636629
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer_visit_Module.input_source = (
        "from typing import List\n"
        "class A(metaclass=List[int]):\n"
        "    pass"
    )
    metaclass_transformer_visit_Module.input_tree = ast.parse(metaclass_transformer_visit_Module.input_source)
    metaclass_transformer_visit_Module.expected_tree = ast.parse(
        metaclass_transformer_visit_Module.input_source[:3] +
        six_import.get_source() +
        metaclass_transformer_visit_Module.input_source[3:]
    )
    metaclass_transformer_visit_Module

# Generated at 2022-06-14 01:59:05.638608
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Unit test for method visit_ClassDef of class MetaclassTransformer.
    
    """
    import ast
    import typing

    from typed_ast import ast3 as typed_ast

    from typed_astunparse import ast3unparse

    from pytype_extensions.type_annotations_lining import MetaclassTransformer

    from ..utils.testing import check_equal

    code = "class A(metaclass=B):\n    pass"

# Generated at 2022-06-14 01:59:06.475094
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:07.603470
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    _test_MetaclassTransformer_visit_Module()



# Generated at 2022-06-14 01:59:08.873144
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:59:10.111745
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:59:23.470550
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...testing import assert_tree
    from ...testing.utils import update_context, dump_tree
    from .six import six_import_transformer

    tree = ast.parse('''
        class A(metaclass=B):
            pass
    ''')

    expected = ast.parse(six_import + '''
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    ''')

    result = MetaclassTransformer().visit(tree)
    assert_tree(result, expected)

    # Test with other dependencies.
    update_context(2, 7)
    result = six_import_transformer.visit(result)

# Generated at 2022-06-14 01:59:24.269509
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:59:32.765859
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast

    code = """
        class Foo(metaclass=Bar):
            pass\n
        """
    expected = """
        class Foo(Bar):
            pass\n
        """
    actual = ast.parse(code)
    expected = ast.parse(expected)
    user_stubs = {
        'six': 'def with_metaclass(meta, *bases): pass\n'
    }
    xformer = MetaclassTransformer(user_stubs)
    xformer.visit(actual)
    pytest.helpers.assert_source_equal(expected, actual)

# Generated at 2022-06-14 01:59:41.469768
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.test_utils import transform

    @snippet
    def before():
        class A(metaclass=B):
            pass


# Generated at 2022-06-14 01:59:47.260728
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .fixtures.metaclass import snippet, expected
    import astor

    # we're testing a class, so we must use 3.x syntax
    ast_module = ast.parse(snippet)

    transpiled_module = MetaclassTransformer().visit(ast_module)
    transpiled_code = astor.to_source(transpiled_module)

    assert transpiled_code == expected

# Generated at 2022-06-14 02:00:07.924474
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.test_utils import (assert_conversion, assert_reverts)

    node = ast.ClassDef(name='A', bases=[], keywords=[ast.arg('metaclass', ast.Name('B', ast.Load()))],
                        body=[], decorator_list=[])
    expected = ast.ClassDef(bases=ast.List(elts=[], ctx=ast.Load()),
                            body=[], decorator_list=[],
                            keywords=[],
                            name='A')

# Generated at 2022-06-14 02:00:09.148080
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:19.437812
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    AstNode = pyast.AST
    tester = MetaclassTransformer()
    example1 = pyast.parse(''' class A(metaclass=B):
                                    pass
                             ''')
    example2 = pyast.parse(''' class A(B):
                                    pass
                             ''')
    example3 = pyast.parse(''' class A(metaclass=B, a=1):
                                    pass
                             ''')

# Generated at 2022-06-14 02:00:33.138461
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:44.316989
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    mt = MetaclassTransformer()
    source = textwrap.dedent("""\
        class A(metaclass=B):
            pass
        """)
    code = mt.visit(ast.parse(source))
    result = ast.dump(code)

# Generated at 2022-06-14 02:00:45.763491
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor

# Generated at 2022-06-14 02:00:55.395883
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # setup ast
    node = ast.parse(
        """
        class A(metaclass=B):
            pass
        """
    ).body[0]

    # execute transform
    mt = MetaclassTransformer()
    mt.visit(node)

    # assert transform

# Generated at 2022-06-14 02:01:03.663884
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    expected = ast.Module(body=[
        six_import.get_body(),
        ast.ClassDef(name='A',
                     bases=[
                         class_bases.get_body(
                             metaclass=ast.Name(id='B', ctx=ast.Load()),  # type: ignore
                             bases=ast.List(elts=[], ctx=ast.Load())
                         )
                     ],
                     body=[],
                     decorator_list=[])
    ])
    actual = ast.parse("""
        class A(metaclass=B):
            pass
    """)
    actual = MetaclassTransformer().visit(actual)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 02:01:05.516312
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:01:07.781949
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    assert MetaclassTransformer.__name__ == "MetaclassTransformer"

# Generated at 2022-06-14 02:01:34.324001
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils import run_transformer
    from .. import six

    node = ast.parse(six.import_statement)
    node = run_transformer(MetaclassTransformer, node)

    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.ImportFrom)
    assert node.body[0].module == 'six'



# Generated at 2022-06-14 02:01:35.905052
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.tree import tree_to_str


# Generated at 2022-06-14 02:01:41.634015
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    c = MetaclassTransformer(None)
    metaclass = ast.Name(id='Meta', ctx=ast.Load())
    c = ast.ClassDef(name='C', bases=[], keywords=[],
    body=[], decorator_list=[], lineno=0,
    col_offset=0)
    newast = c.visit(metaclass)
    assert newast == None

# Generated at 2022-06-14 02:01:48.584885
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast

    class A():
        pass

    class B():
        pass

    def gen_ast(m0, m1, b0, b1, **kwargs):
        class0 = ast.ClassDef(name='A',
                              bases=[m0, b0])

        class1 = ast.ClassDef(name='B',
                              bases=[m1, b1])

        module = ast.Module(body=[class0, class1])
        module_body = node_body(module)
        return module_body

    # Test a module with the same class name
    # in multiple nodes

# Generated at 2022-06-14 02:01:59.005542
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():

    # Setup variables !
    root = ast.parse('class A(metaclass=B, c=d): pass', mode = 'exec')
    metaclass_transformer = MetaclassTransformer()

    # Mutate root of the tree
    metaclass_transformer.visit(root)

    # Convert AST tree to string again, check if the string corresponds to our goal
    new_str = astor.to_source(root).strip()

# Generated at 2022-06-14 02:02:10.151836
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """This test corresponds to the following Python code:

    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(metaclass=B):
        pass
    """
    node = ast.parse(inspect.getsource(test_MetaclassTransformer))
    t = MetaclassTransformer()
    t.visit(node)
   #print(astunparse.unparse(node))
    # print(six_import.get_body())
    # print(astunparse.unparse(six_import.get_body()))
    # print(astunparse.unparse(t.visit(node)))
    # six_import.get_body()[0].name == "_py_backwards_six_withmetaclass"
    # node.body[0].value.

# Generated at 2022-06-14 02:02:14.547099
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    assert compile_snippet(
        '''
        class Test(metaclass=type):
            pass
        ''',
        MetaclassTransformer
    ) == '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class Test(_py_backwards_six_withmetaclass(type)):
            pass
        '''

# Generated at 2022-06-14 02:02:20.365355
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astroid
    import six
    src = '''
    class A(metaclass=B):
        pass
    '''
    t = astroid.parse(src)
    mct = MetaclassTransformer()
    mct.visit(t)
    print(t.repr_tree())
    src_expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''
    six.assertCountEqual(src_expected, t.as_string())

# Generated at 2022-06-14 02:02:23.568366
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # type: () -> None
    """
    Test for method visit_ClassDef of class MetaclassTransformer
    """
    transformer = MetaclassTransformer()

# Generated at 2022-06-14 02:02:26.093411
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import ast as pyast
    from ..utils.compiler import compile_snippet
    from ..utils.tree import convert


# Generated at 2022-06-14 02:03:28.396534
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():

    from typed_ast import ast3 as ast

    from .base import CompilerTestCase

    from .compat27 import with_metaclass

    class MetaclassTestCase(CompilerTestCase):
        __metaclass__ = MetaclassTransformer

        def test_metaclass_name(self):
            exec(six_import)

            class A(with_metaclass(type)):
                pass

            self.assertEqual(A.__class__, type)
            self.compile_to_execution_tree(A)

            A = self.compile(A)

            self.assertEqual(A.__class__, type)

        def test_metaclass_name_with_args(self):
            exec(six_import)


# Generated at 2022-06-14 02:03:36.430341
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse("class A(b, c=d, e=f, metaclass=B):\n  pass")
    module.body[0].keywords.append(ast.keyword(arg='c', value=ast.Name(id='d', ctx=ast.Load())))
    module.body[0].keywords.append(ast.keyword(arg='e', value=ast.Name(id='f', ctx=ast.Load())))
    module.body[0].keywords.append(ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load())))

# Generated at 2022-06-14 02:03:43.386813
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    code = "class A(metaclass=type): pass"
    expected = "from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(type))"
    t = MetaclassTransformer()
    assert t.visit(ast.parse(code)).body[0].body[0].bases[0].body[0].value.args[0].id == "_py_backwards_six_withmetaclass"


# Generated at 2022-06-14 02:03:54.792123
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import tree
    from textwrap import dedent
    from typed_ast import AST

    # Test with no keyword arguments
    transformer = MetaclassTransformer()
    node = ast.parse(dedent("""
    class A(object):
        pass
    """)).body[0]
    transformer.visit(node)

# Generated at 2022-06-14 02:03:59.926782
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import parse
    from ..utils.sample_code import sample_code

    module = parse(sample_code['metaclass'])
    mt = MetaclassTransformer()
    mt.visit(module)
    result = mt.result()

    # Use a type-unaware visitor to ensure that the resulting tree is valid
    from typed_ast import ast3, c_ast_transforms
    c_ast_transforms.validate(module)

# Generated at 2022-06-14 02:04:13.141614
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .case_transformer import CaseTransformer
    import textwrap
    import astunparse
    source = textwrap.dedent('''
    class MetaClass(dict): pass

    class BaseClass(metaclass=MetaClass):
        def __init__(self):
            super(BaseClass, self).__init__()

        def function(self):
            print("base class called")
    ''')
    def check(transformer: CaseTransformer, source: str) -> None:
        parsed = ast.parse(source)
        transformer.visit(parsed)
        transformed = astunparse.unparse(parsed)
        parsed = ast.parse(transformed)
        transformer.visit(parsed)
        transformed_twice = astunparse.unparse(parsed)
        assert transformed == transformed

# Generated at 2022-06-14 02:04:21.184957
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = """
        class A(metaclass=B):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """

    transform = MetaclassTransformer()
    result = transform(source)
    assert normalize_code(expected) == normalize_code(result)

# Generated at 2022-06-14 02:04:28.877281
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    @snippet
    def snippet():
        class A(metaclass=B, c=d):
            x: int

    mod = ast.parse(snippet.code())
    transformer = MetaclassTransformer(mod)
    transformer.visit(mod)
    code = _ast3_to_code(mod)

    assert code == 'from six import with_metaclass as _py_backwards_six_withmetaclass\n' \
                   '\n' \
                   '\n' \
                   'class A(_py_backwards_six_withmetaclass(B), c=d):\n' \
                   '    x: int\n'

# Generated at 2022-06-14 02:04:33.955631
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    a = ast.ClassDef(name='A',
                     bases=[],
                     keywords=[ast.arg(arg='metaclass',
                                       value=ast.Name(id='B', ctx=ast.Load()))],
                     body=[],
                     decorator_list=[])
    tree = ast.Module(body=[a])
    MetaclassTransformer().visit(tree)
    assert tree.body == six_import.get_body() + [a]



# Generated at 2022-06-14 02:04:36.888985
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    # Constructor
    t = MetaclassTransformer()
    # Method resolution order test
    assert issubclass(MetaclassTransformer, BaseNodeTransformer)