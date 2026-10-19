

# Generated at 2022-06-14 01:54:55.518974
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:02.770424
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    class A(ast.NodeTransformer):
        def visit_ClassDef(self, node):
            node.bases = [1, 2, 3]
            return node
    class B(ast.NodeTransformer):
        def visit_ClassDef(self, node):
            node.keywords = []
            return node

    node = six.exec_(_class_metaclass)
    node = A().visit(node)
    node = B().visit(node)
    node = MetaclassTransformer().visit(node)
    assert ast.dump(node) == six.text_type(_class_metaclass_target)


# Generated at 2022-06-14 01:55:12.040146
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from ast import Module
    
    module = Module(body=[
        ast.ClassDef(name='A',
                     bases=[ast.Name(id='B', ctx=ast.Load())],
                     keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='C', ctx=ast.Load()))],
                     body=[],
                     decorator_list=[])
    ])


# Generated at 2022-06-14 01:55:21.000621
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = textwrap.dedent("""
    import six
    class A(metaclass=six.with_metaclass(B)):
        pass
    """)
    expected = textwrap.dedent("""
    class A(_py_backwards_six_with_metaclass(B)):
        pass
    """)

    tree = ast.parse(source)
    tree = MetaclassTransformer().visit(tree)
    result = ast.unparse(tree)

    assert result == expected

# Generated at 2022-06-14 01:55:25.601551
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    test_1 = MetaclassTransformer.run_test(
        source='''
        class A(metaclass=type):
            pass
        ''',
        expected='''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(type, object)):
            pass
        '''
    )

# Generated at 2022-06-14 01:55:30.316237
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = """
        class A(metaclass=B, object=None, extra=1):
            pass
    """
    expected = """
        class A(_py_backwards_six_withmetaclass(B, object, extra)):
            pass
    """
    MetaclassTransformer.test(node, expected)


# Generated at 2022-06-14 01:55:32.177837
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..codegen import to_source
    from .six import to_py3
    
    source = 'class A(metaclass=B): pass'
    assert to_py3(source) == to_source(MetaclassTransformer(compiler_version=3).visit(ast.parse(source)))

# Generated at 2022-06-14 01:55:40.405940
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    node = ast.parse("""
        class A(metaclass=B):
            pass
    """)

    # When
    transformer = MetaclassTransformer(None)
    transformer.visit(node)
    result = ast.dump(node)

    # Then
    expected = """Module(
    body=[FromImport(
        module='six',
        names=[alias(
            name='with_metaclass',
            asname='_py_backwards_six_withmetaclass')],
        level=None)],
    type_ignores=[])"""
    assert result == expected


# Generated at 2022-06-14 01:55:40.997715
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:51.471437
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """class A(metaclass=B): ... -> class A(_py_backwards_six_with_metaclass(B)): ..."""
    from typed_ast import ast3 as ast
    tree = ast.parse('class A(metaclass=B): pass')
    A = tree.body[0]
    assert isinstance(A, ast.ClassDef)
    assert len(A.keywords) == 1
    assert A.keywords[0].arg == 'metaclass'
    assert A.keywords[0].value.id == 'B'
    assert len(A.bases) == 0
    assert len(A.body) == 1
    assert isinstance(A.body[0], ast.Pass)

    new_tree = MetaclassTransformer().visit(tree)

# Generated at 2022-06-14 01:55:56.780028
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()
    m = ast.parse('''class A(metaclass=B):
                        pass''')
    mt.visit(m)
    assert m.body[0].value.bases[0].args[0].id == 'B'

# Generated at 2022-06-14 01:56:08.030979
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import pytest
    from ..converter import Converter
    from ..utils.snippet import snippet

    @snippet
    def test_class():
        class A(B, metaclass=C):
            pass

    @snippet
    def test_expected():
        class A(_py_backwards_six_withmetaclass(C, B)):
            pass

    node = test_class.get_ast(parser='python3')
    assert not isinstance(node, ast.Module)
    expected = ast.Module(body=test_expected.get_body())

    conv = Converter()
    conv.target = (2, 7)

    tr = MetaclassTransformer()
    conv.add_transformer(tr)
    tr.visit(node)

    assert node == expected

# Generated at 2022-06-14 01:56:19.110500
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast27 as ast
    from ..utils.compat import six_import
    from .base import BaseNodeTransformerTestCase
    from .six_import_transformer import SixImportTransformer

    code = \
        """
            class A(metaclass=type):
                pass
            """.split('\n')

    class Test(BaseNodeTransformerTestCase):
        transformer = MetaclassTransformer
        expected_output = \
            """
            class A(_py_backwards_six_withmetaclass(type)):
                pass
            """.split('\n')
        expected_tree = ast.parse("".join(expected_output))

    if six_import.get_body():
        class Test(Test):
            transformer = SixImportTransformer + Test.transformer

# Generated at 2022-06-14 01:56:30.812852
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    expected = ast.Module(
        body=[
            six_import.get_body(),
            ast.ClassDef(
                name='B',
                bases=[
                    ast.Call(func=ast.Name(id='_py_backwards_six_withmetaclass',
                                           ctx=ast.Load()),
                             args=[ast.Name(id='A', ctx=ast.Load())],
                             keywords=[],
                             starargs=None,
                             kwargs=None)
                ],
                keywords=[]
            )
        ]
    )


# Generated at 2022-06-14 01:56:32.146113
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:40.143550
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()
    node = ast.ClassDef(name='B',
                        bases=[ast.Name(id='A', ctx=ast.Load())],
                        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='C', ctx=ast.Load()))],
                        body=[ast.Pass()],
                        decorator_list=[])
    mt.visit(node)
    assert str(node) == "class B(metaclass=C)(_py_backwards_six_withmetaclass(C), A):\n    pass"  # type: ignore

# Generated at 2022-06-14 01:56:50.117458
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = dedent("""\
    class A(B, C, metaclass=D):
        pass
    """)
    expected_result = dedent("""\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    
    class A(_py_backwards_six_withmetaclass(D, B, C)):
        pass
    """)
    node = ast.parse(source)
    transformer = MetaclassTransformer()
    result_node = transformer.visit(node)
    assert ast.dump(result_node) == ast.dump(ast.parse(expected_result))

# Generated at 2022-06-14 01:56:53.866006
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.testing import maketemp_context
    from ..utils import tree
    import os.path
    import shutil


# Generated at 2022-06-14 01:57:02.073129
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformation = MetaclassTransformer()

    source = """
    
    class A(metaclass=B):
        pass
        
    """

    expected = """
    import six
    class A(six.with_metaclass(B)):
        pass
        
    """

    tree = ast.parse(source)
    new_tree = transformation.visit(tree)
    new_source = astunparse.unparse(new_tree)  # type: ignore

    assert new_source == expected



# Generated at 2022-06-14 01:57:08.544431
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module_node = ast.parse("class A(metaclass=B):pass")
    expected_module_node = ast.parse("from six import with_metaclass as _py_backwards_six_withmetaclass;class A(metaclass=B):pass")
    assert isinstance(module_node, ast.Module)
    module_node = MetaclassTransformer().visit(module_node)
    assert ast.dump(module_node) == ast.dump(expected_module_node)



# Generated at 2022-06-14 01:57:21.406352
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    class CustomMeta(type):
        pass

    class A:
        pass


    class B(A, metaclass=CustomMeta):
        pass

    _py_backwards_six_withmetaclass = six_import.get_body()[0].body[0]
    _py_backwards_six_withmetaclass(CustomMeta, A)

    tree = ast.parse(dedent('''
    class A:
        pass


    class B(A, metaclass=CustomMeta):
        pass
    '''))  # type: ignore

    visitor = MetaclassTransformer()
    visitor.visit(tree)

    assert len(tree.body) == 4
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert tree.body

# Generated at 2022-06-14 01:57:30.211372
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .. import transform
    from astmonkey import transformers
    from typed_ast.ast3 import parse
    import textwrap

    testcase = """
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class A(metaclass=B):
            pass
    """

    node = parse(textwrap.dedent(testcase))  # type: ast.Module
    new_node = transformers.ParentNodeTransformer().visit(node)
    transform(new_node, [MetaclassTransformer])
    assert new_node == node


# Generated at 2022-06-14 01:57:31.584219
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:57:41.678658
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.Module(
        body=[ast.ClassDef(
            name="A",
            keywords=[ast.keyword(
                arg='metaclass',
                value=ast.Name(
                    id='B',
                    ctx=ast.Load()
                )
            )],
            bases=[ast.Name(
                id='Parent',
                ctx=ast.Load()
            )],
            body=[ast.Pass()]
        )]
    )

# Generated at 2022-06-14 01:57:44.548374
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source
    from .metaclass import MetaclassTransformer

# Generated at 2022-06-14 01:57:50.453112
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .base import BaseTestTransformer

    class Test(BaseTestTransformer):
        target = MetaclassTransformer.target
        transformer = MetaclassTransformer
        method = 'visit_ClassDef'
        s = "class A(metaclass=B): pass"
        expected_code = (
            "class A(_py_backwards_six_withmetaclass(B)): pass"
        )

    Test().test(debug=False)

# Generated at 2022-06-14 01:57:58.575216
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from textwrap import dedent as d
    from ..utils.fixtures import make_test_tree
    node = make_test_tree({2: 7}, d("""\
        class A(metaclass=B):
            pass
        """))
    assert MetaclassTransformer(node).visit(node) == make_test_tree({2: 6}, d("""\
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """))

# Generated at 2022-06-14 01:58:08.541649
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.conftest import fix_python_path
    from ..utils.fixtures import make_test_module

    # Make a test module
    test_module = make_test_module(fix_python_path(__file__))
    module_node = test_module['module_node']

    # Prepare module node
    node = ast.ClassDef(
        name='B',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='A'))],
        body=[],
        decorator_list=[])
    module_node.body.append(node)

    # Visit module
    transform = MetaclassTransformer()
    module_node = transform.visit(module_node)

    # Confirm results

# Generated at 2022-06-14 01:58:15.274878
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = dedent("""
    class A(metaclass=B):
        pass
    """)
    node = ast.parse(code)
    new_node = MetaclassTransformer().visit(node)

# Generated at 2022-06-14 01:58:25.823054
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast import parse as ast_parse
    from compile import ModuleCodeGenerator
    node = ast_parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer()
    node = transformer.visit(node)
    assert node.body[0].bases[0].value.func.id == '_py_backwards_six_withmetaclass'
    assert node.body[0].bases[0].value.args[0].id == 'B'
    assert node.body[0].keywords == []
    module_code_generator = ModuleCodeGenerator()
    source_text = module_code_generator.visit(node)

# Generated at 2022-06-14 01:58:31.509729
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_transformed_ast, normalize_str


# Generated at 2022-06-14 01:58:40.512705
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Test 1: 
    #	Module
    #	  |-ClassDef
    #	      |-metaclass
    #	          |-Name
    #	              |-id(Keyword)
    #	              |-arg(Keyword)
    ast_tree = ast.parse('''
    class A(metaclass=B):
        pass
    ''')
    transformer = MetaclassTransformer()
    result_ast_tree = transformer.visit(ast_tree)

    expected_ast_tree = ast.parse('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    ''')


# Generated at 2022-06-14 01:58:42.834660
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:58:51.998438
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:58.896641
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ... import compile
    from . import util
    util.assert_src_equal(compile('import six', MetaclassTransformer),
                          'import six')

    util.assert_src_equal(compile('import six\n'
                                  'import this', MetaclassTransformer),
                          'import six\n'
                          'import this\n')


# Generated at 2022-06-14 01:59:08.763659
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    old_code = """
        class A(B, metaclass=C):
            pass
        """
    new_code = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(C, B)):
            pass
        """
    t = MetaclassTransformer()
    old_tree = ast.parse(old_code)
    new_tree = t.visit(old_tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse(new_code))


# Generated at 2022-06-14 01:59:17.379080
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = textwrap.dedent('''
    class A(type):
        pass
    ''')
    from .base import TestTransformer
    from .base import transform_and_compile
    res = transform_and_compile(MetaclassTransformer, source)
    assert res.body[0].value.bases[0].elts[0] == 'A'
    assert res.body[1].value.bases == []



# Generated at 2022-06-14 01:59:23.009186
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse('''
        class A(metaclass=B):
            pass
    ''')
    MetaclassTransformer().visit(module)


# Generated at 2022-06-14 01:59:33.448235
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    class TestMetaclassTransformer(MetaclassTransformer):
        def __init__(self):
            self._tree_changed = False

    for test_source in [
        'class A(metaclass=B): pass',  # noqa: E731
        'class A(b, metaclass=B): pass',  # noqa: E731
        'class A(b, c, d): pass'
    ]:
        tree = ast.parse(test_source)
        transformer = TestMetaclassTransformer()
        tree = transformer.visit(tree)
        assert not transformer._tree_changed

        tree = ast.parse(test_source, type_comments=True)
        transformer = TestMetaclassTransformer()
        tree = transformer.visit(tree)
        assert not transformer._tree_changed

   

# Generated at 2022-06-14 01:59:35.619906
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:44.826970
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # TODO: write tests
    pass

# Generated at 2022-06-14 01:59:50.164100
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = "class Foo(metaclass=type): pass"
    target = "class Foo(_py_backwards_six_withmetaclass(type)): pass"
    node = ast.parse(source)
    MetaclassTransformer().visit(node)
    result = compile(node, "<test>", "exec")
    exec(result)
    assert str(result) == target

# Generated at 2022-06-14 01:59:56.857537
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    ast_fragment_1 = """
        class A(metaclass=B):
            pass
    """
    expected_ast_fragment_1 = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(metaclass=B):
            pass
    """
    ast_fragment_2 = """
        class A(metaclass=B):
            pass
        class C(metaclass=D):
            pass
        """
    expected_ast_fragment_2 = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(metaclass=B):
            pass
        class C(metaclass=D):
            pass
        """

# Generated at 2022-06-14 01:59:58.652292
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.astdump import astdump
    import ast

# Generated at 2022-06-14 02:00:06.122209
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..fixtures.six import six_import
    from ..fixtures.metaclass import simple_class, import_six_and_class
    from ..utils.snippet import snippet


    snippet_obj = snippet(six_import)
    ast_obj = ast.parse(snippet_obj)
    correct_ast_module = ast.parse(import_six_and_class).body[0]
    assert ast_obj.body[0] == correct_ast_module



# Generated at 2022-06-14 02:00:12.407824
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
        class A(metaclass=B):
            pass
    """)
    node = tree.body[0]  # type: ast.ClassDef
    assert not isinstance(node.bases[0], ast.Call)
    MetaclassTransformer.visit_ClassDef(node)
    assert isinstance(node.bases[0], ast.Call)
    assert node.keywords == []

# Generated at 2022-06-14 02:00:14.398232
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:00:17.497658
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A:
        pass
    
    def check(code):
        t = MetaclassTransformer()
        node = ast.parse(code)
        t.visit(node)
        assert t._tree_changed
    

# Generated at 2022-06-14 02:00:24.408830
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class Main():
        def main():
            class A(metaclass=B):
                pass
    res = compile(Main.__module__, Main.main.__module__, 'exec')

# Generated at 2022-06-14 02:00:26.271668
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import assert_transform


# Generated at 2022-06-14 02:00:42.818924
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:44.171269
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:45.716316
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 02:00:55.363038
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import compare_ast
    # Check that this compiles
    compare_ast(compiler.parse('''
        class A(object, metaclass=B):
            pass
        ''', mode='exec'), '''
        class A(object):
            pass
        ''')

    # Check that this compiles
    compare_ast(compiler.parse('''
        class A(metaclass=B):
            pass
        ''', mode='exec'), '''
        class A():
            pass
        ''')

    # Check that this compiles
    compare_ast(compiler.parse('''
        class A(object, metaclass=B):
            pass
        ''', mode='exec'), '''
        class A(object):
            pass
        ''')

    # Check that this compiles


# Generated at 2022-06-14 02:01:05.871115
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    from typed_ast import ast3 as ast

    class Test(unittest.TestCase):
        def setUp(self):
            self.transformer = MetaclassTransformer()

        def test_simple_case(self):
            classdef = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[], lineno=1, col_offset=0)
            ast.copy_location(classdef, ast.ClassDef())
            classdef.keywords.append(ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load())))

# Generated at 2022-06-14 02:01:15.265155
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    @snippet
    def sample_module(metaclass):
        class C(metaclass=metaclass):
            pass

    source = sample_module.get_body(metaclass=ast.Constant(value="Metaclass"))  # type:ignore
    expected = sample_module.get_body(metaclass=ast.Name(id="Metaclass"))  # type:ignore
    for i, j in zip(expected.body[0].bases.elts, MetaclassTransformer().visit(source).body[0].bases.args):
        assert i == j

# Generated at 2022-06-14 02:01:16.234530
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:01:26.373748
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    six_import_transform = [
        {
            "node": "six_import.body[0]",
            "type": "ImportFrom",
            "module": "six",
            "names": [
                {
                    "name": "with_metaclass",
                    "asname": "_py_backwards_six_withmetaclass"
                }
            ]
        }
    ]
        

# Generated at 2022-06-14 02:01:29.258397
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = '''class Test(metaclass=TestMeta):
    pass
'''

# Generated at 2022-06-14 02:01:39.898144
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # ```python
    # class A(metaclass=B, c=d):
    #     pass
    # ```
    #
    # ```python
    # class A(_py_backwards_six_with_metaclass(B, D), c=d):
    #     pass
    # ```
    class_def = ast.ClassDef(name="A",
                             bases=[ast.Name(id="B", ctx=ast.Load())],
                             keywords=[ast.keyword(arg="c", value=ast.Name(id="d", ctx=ast.Load()))],
                             body=[ast.Pass()],
                             decorator_list=[])

    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer.visit(class_def)

    expected

# Generated at 2022-06-14 02:02:21.026120
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.visitor import dump
    from ..transformers.base import BaseNodeTransformer

    class A(object):
        pass

    class B(A, metaclass=A):
        pass

    A_node = ast.parse('A', 'exec').body[0]
    class_def = ast.fix_missing_locations(ast.parse('class B(A, metaclass=A): pass', 'exec').body[0])
    transformer = MetaclassTransformer()

    result = transformer.visit(class_def)
    assert transformer.tree_changed is True

# Generated at 2022-06-14 02:02:27.097312
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("class A(metaclass=B): pass")
    transformer = MetaclassTransformer(tree)  # type: ignore
    new_tree = transformer.visit(tree)


# Generated at 2022-06-14 02:02:33.430577
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from six import with_metaclass

    code = """
    from six import with_metaclass

    class Foo(metaclass=Bar):
        pass

    class Bar(object):
        pass
    """

    tree = ast.parse(code)
    tree = MetaclassTransformer().visit(tree)

    assert astor.to_source(tree) == """
    from six import with_metaclass

    class Foo(_py_backwards_six_withmetaclass(Bar, object)):
        pass


    class Bar(object):
        pass
    """


# Generated at 2022-06-14 02:02:36.622315
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testutils import assert_code_equal, assert_tree_equal
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:02:39.406958
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from typed_ast.test.test_transformer import test_transformer
    from .six import six_import
    from .six import class_bases

# Generated at 2022-06-14 02:02:49.131372
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    visitor = MetaclassTransformer()

    # Replace class definition in body
    class_definition = ast.ClassDef(name="Test",
                                    keywords=[ast.keyword(arg="metaclass",
                                                          value=ast.Name(id="A"))],
                                    bases=[])
    original_ast = ast.Module(body=[class_definition])
    expected_ast = ast.Module(body=[class_bases.get_body(metaclass=ast.Name(id="A"),
                                                         bases=ast.List(elts=[]))])
    result = visitor.visit(original_ast)

    assert result == expected_ast
    assert visitor.deps == {"six"}

# Generated at 2022-06-14 02:02:54.441114
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_equal_code

    node = ast.parse('''
        class A(object, metaclass=type):
            pass
    ''')

    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(type), object):
            pass
    '''
    assert_equal_code(MetaclassTransformer.run(node), expected)



# Generated at 2022-06-14 02:02:57.323184
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("class A(metaclass=B):\n    pass")
    MetaclassTransformer().visit(node)
    assert ast.dump(node) == textwrap.dedent("""\
        class A(_py_backwards_six_with_metaclass(B)):
            pass""")

# Generated at 2022-06-14 02:02:58.078275
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:06.328628
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from textwrap import dedent
    # Test simple case with one metaclass

    # In:
    code = dedent("""
    class A(metaclass=B):
        pass
    """)
    expected_code = dedent("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)
    # Out:
    tree = astor.parse_tree(code)
    six_import._py_backwards_six_withmetaclass.compile_cache = []
    class_bases._py_backwards_six_withmetaclass.compile_cache = []
    node = MetaclassTransformer().visit(tree)

# Generated at 2022-06-14 02:03:45.084614
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = textwrap.dedent('''\
    class A(metaclass=B):
        pass
    ''')
    target = textwrap.dedent('''\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    ''')
    tree = ast.parse(source)
    tree = MetaclassTransformer().visit(tree)
    assert target == unparse(tree)


# Generated at 2022-06-14 02:03:47.818851
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .utils import get_target_ast


# Generated at 2022-06-14 02:03:54.521979
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ... import parse_ast
    tree = parse_ast('class A(metaclass=B): \n'
                     '    pass')
    transformer = MetaclassTransformer(tree)
    transformer.run()
    expected = parse_ast('class A(_py_backwards_six_with_metaclass(B)): \n'
                         '    pass')
    assert transformer._tree_changed
    assert tree == expected

# Generated at 2022-06-14 02:03:59.343511
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..parser import parse

    tree = parse(
        '''
        class A(metaclass=B):
            pass
        '''
    )

    transformer = MetaclassTransformer(tree)
    assert transformer.visit(tree) == parse(
        '''
        import six


        class A(six.with_metaclass(B)):
            pass
        '''
    )

# Generated at 2022-06-14 02:04:05.586732
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    """Test that with_metaclass method is added to snakemake.six module.
    """
    module = ast.parse("""class A(metaclass=B):
        pass""")
    transformer = MetaclassTransformer()
    transformer.visit(module)

    assert any(isinstance(node, ast.ImportFrom) for node in module.body)

# Generated at 2022-06-14 02:04:17.498109
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Pass # type: ignore
    from .base import BaseNodeTransformer
    from .base import BaseTransformedModule
    from .base import TransformedModule
    m = ast.parse('class A(metaclass=B):pass')
    MetaclassTransformer().visit(m)
    assert isinstance(m, ast.Module)
    assert len(m.body) == 2
    assert isinstance(m.body[0], ast.FunctionDef)
    assert m.body[0].name == '_py_backwards_six_withmetaclass'
    assert len(m.body[1].body) == 1
    assert isinstance(m.body[1].body[0], ast.Pass)

# Generated at 2022-06-14 02:04:21.038650
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import astor
    from ast import (
        ClassDef,
        FunctionDef,
        Module
    )
    from astor.code_gen import to_source

# Generated at 2022-06-14 02:04:30.157181
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # This test is auto-generated from a snippet created with py_backwards.
    from py_backwards.transformers import WithMetaclassTransformer
    from typed_ast import ast3 as ast

    code = (
        'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
        '\n'
        '\n'
        'class A(metaclass=B):\n'
        '    pass\n'
        '\n'
    )


# Generated at 2022-06-14 02:04:33.761639
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Example:
    #     class A(metaclass=B):
    #         pass
    #
    # Should be transformed to:
    #     from six import with_metaclass as _py_backwards_six_withmetaclass
    #     class A(_py_backwards_six_withmetaclass(B)):
    #         pass
    def abstract_0(node: ast.Module) -> ast.Module:
        ...

    ast_ = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    subject: ast.Module = abstract_0(ast_.body[0])

    result = MetaclassTransformer(None).visit(subject)

# Generated at 2022-06-14 02:04:40.726610
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import sys
    from typed_ast import ast3 as ast
    from ..codegen import to_source
    from .transformer import Module

    class A(metaclass=type):
        pass

    node = ast.parse(to_source(A))
    debug = {'_py_backwards_six_withmetaclass': sys.modules['six'].with_metaclass}
    for transformer in (MetaclassTransformer, ):
        node = transformer().visit(node)
    node = Module(debug=debug).visit(node)
    module = compile(node, '<string>', 'exec')
    exec(module)