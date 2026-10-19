

# Generated at 2022-06-14 01:54:58.501280
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:55:05.946229
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    root = ast.parse('''class M(metaclass=B): pass''')
    expected = '''class M(_py_backwards_six_with_metaclass(B)): pass'''
    result = codegen.to_source(MetaclassTransformer('2.7').visit(root))
    assert result == expected

# Generated at 2022-06-14 01:55:13.473547
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestCase(unittest.TestCase):
        def test_with_metaclass(self):
            self.assertEqual(
                compile_source(MetaclassTransformer, 'class A(metaclass=B): pass'),
                'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
                'class A(_py_backwards_six_withmetaclass(B)):\n    pass'
            )

        def test_without_metaclass(self):
            self.assertEqual(
                compile_source(MetaclassTransformer, 'class A: pass'),
                'class A:\n    pass'
            )

    unittest.main()

# Generated at 2022-06-14 01:55:23.539780
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .base import BaseNodeTransformerTest
    BaseNodeTransformerTest.run_visitor(MetaclassTransformer,
        """
            class A(metaclass=type):
                pass
            class B(A):
                pass
        """,
        """
            from six import with_metaclass as _py_backwards_six_withmetaclass

            class A(_py_backwards_six_withmetaclass(type, )):
                pass

            class B(_py_backwards_six_withmetaclass(type, )):
                pass
        """
    )

# Generated at 2022-06-14 01:55:26.243478
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import fixture_test_ast

    classdef_test = fixture_test_ast("classdef")
    ModuleTransformer = MetaclassTransformer()

# Generated at 2022-06-14 01:55:31.059911
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_base import get_ast

    tree = get_ast('''
        ''')
    expected = get_ast('''
        ''')
    result = MetaclassTransformer().visit(tree)
    assert result == expected

# Generated at 2022-06-14 01:55:31.511193
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:37.858847
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    code = '''
    class A(metaclass=B):
        pass
    '''
    expected_code = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''
    node = ast.parse(code)

    # When
    new_node = MetaclassTransformer().visit(node)

    # Then
    assert ast.dump(new_node) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 01:55:48.232059
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    from typed_ast import ast3 as ast
    node = ast.ClassDef(name='A',
                        bases=[],
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='B', ctx=ast.Load()))],
                        body=[],
                        decorator_list=[])

    # When
    constructed_object = MetaclassTransformer().visit(node)

    # Then

# Generated at 2022-06-14 01:55:57.800413
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.as_source import as_source
    from ..utils.ast_compare import compare_ast
    from ..utils.snippet import snippet
    import ast

    input_source = snippet(
        """
        
        class A(metaclass=B):
            pass
        
        """
    )
    output_source = snippet(
        """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B, )):
            pass
        
        """
    )
    obj = MetaclassTransformer()
    src_node: ast.Module = ast.parse(input_source)
    trg_node = obj.visit(src_node)

# Generated at 2022-06-14 01:56:09.727689
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer()

    # Visit a ClassDef node with no keywords, to ensure that nothing changes
    classdef_no_kw = ast.ClassDef(name='A',
                                  bases=[ast.Name(id='B', ctx=ast.Load())],
                                  body=[],
                                  keywords=[],
                                  decorator_list=[])
    classdef_no_kw_visited = t.visit(classdef_no_kw)
    assert not t._tree_changed
    assert classdef_no_kw_visited == classdef_no_kw

    # Visit a ClassDef node with invalid keyword arguments (not metaclass), to ensure that nothing changes

# Generated at 2022-06-14 01:56:15.519985
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.syntax import to_source
    from ..utils.tree import parse
    from ..utils.environment import get_environment
    from ..utils.asttools import is_equal

    code = """class A(metaclass=b):\n    pass"""


# Generated at 2022-06-14 01:56:16.688843
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:18.491319
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as py_ast
    import python_modernize.fixes.metaclass as fix


# Generated at 2022-06-14 01:56:27.241805
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .base import BaseTestTransformer
    from .. import patch
    import six

    class TestMetaclassTransformer(BaseTestTransformer):
        transformer = MetaclassTransformer
        method = 'visit_ClassDef'
        expected_code = '''
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        '''
        code = '''
        class A(metaclass=B):
            pass
        '''

    patch([six]).apply()
    TestMetaclassTransformer().test_transformations()

# Generated at 2022-06-14 01:56:37.975694
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    class_def = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[], lineno=1, col_offset=0)
    metaclass = ast.Name(id='A', ctx=ast.Load(), lineno=1, col_offset=0)
    class_def.keywords.append(ast.arg(arg='metaclass', value=metaclass, lineno=1, col_offset=0))
    transformer = MetaclassTransformer()
    new_class_def = transformer.visit(class_def)
    assert str(new_class_def.bases[0].args[0]) == 'A'

# Generated at 2022-06-14 01:56:50.562319
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .. default_visitors import BaseNodeTransformer
    from typed_ast import ast3 as ast
    from . import TreeAssertions
    from . test_six_snippets import test_six_import, test_class_bases
    from ... import utils
    src = 'class A(metaclass=B): pass'
    expected_src = '\n'.join([test_six_import(),
                              test_class_bases(),
                              src])
    root = utils.parse_code_to_ast(src)
    transformer = MetaclassTransformer()
    new_root = transformer.visit(root)
    # The transformer should have changed the tree
    assert transformer.tree_changed

    assert new_root
    assert isinstance(new_root, ast.Module)

# Generated at 2022-06-14 01:57:01.770750
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("""
    class C(object):
        def foo(self):
            print('foo')
    
    class C1(metaclass=C):
        pass
    """)
    # tree before transformation
    c1 = node.body[-1]
    # assert C1's bases are (metaclass=C)
    assert c1.bases[0].keywords[0].arg == "metaclass"

    # transform
    trans = MetaclassTransformer()
    trans.visit(node)

    # now C1's bases should be _py_backwards_six_withmetaclass(C)
    assert c1.bases[0].func.id == "_py_backwards_six_withmetaclass"

# Generated at 2022-06-14 01:57:09.184616
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    class testMetaclassTransformer(MetaclassTransformer):
        def generic_visit(self, node):
            return node
    tree = ast.parse('class A(metaclass=B): pass')
    tree = testMetaclassTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(
        'from six import with_metaclass as _py_backwards_six_withmetaclass;\n'
        'class A(_py_backwards_six_withmetaclass(B)): pass'
    ))

# Generated at 2022-06-14 01:57:18.030362
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import test_transformer
    from ..utils import build_ast

    code = '''
        class A(metaclass=B):
            pass
    '''
    expected_code = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
    '''

    ast_ = build_ast(code)
    transformed = test_transformer(MetaclassTransformer, ast_)
    
    assert transformed == build_ast(expected_code)

# Generated at 2022-06-14 01:57:32.461808
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    imp = ast.ImportFrom(module="six", names=[ast.alias(name="with_metaclass", asname="_py_backwards_six_withmetaclass")], level=0)
    cls = ast.ClassDef(name="A", bases=[class_bases.get_body(metaclass=ast.Name(id="B", ctx=ast.Load()), bases=ast.List(elts=[]))], body=[ast.Pass()], decorator_list=[])
    expected_tree = ast.Module(body=[imp, cls])
    actual_tree = MetaclassTransformer(None).visit_Module(ast.parse("class A(metaclass=B): pass"))
    assert ast.dump(actual_tree, True) == ast.dump(expected_tree, True)

# Generated at 2022-06-14 01:57:35.347603
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_node_equal  # type: ignore
    import ast

# Generated at 2022-06-14 01:57:50.915405
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.mock import mock_module_paths

    with mock_module_paths(), snakeoil.tempdir() as td:
        from ..tests.module_setup import module_setup
        import six

        six.add_move(six.MovedModule('six.moves.zip_longest', 'six.moves.zip', 'zip_longest'))

        class TestMetaclass(type):
            pass

        class TestClass(metaclass=TestMetaclass):
            pass

        module_setup(td, TestClass)

        source = td / 'module_under_test.py'
        transformer = MetaclassTransformer()
        transformer.visit(ast.parse(source.read_text()))
        assert transformer._tree_changed is True


# Generated at 2022-06-14 01:57:56.058951
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():

    expected = """class A(_py_backwards_six_withmetaclass(B)):
    pass
"""
    node = ast.parse("class A(metaclass=B):\n    pass")
    node = MetaclassTransformer().visit(node)
    assert astor.to_source(node) == expected, "Test failed!"

# Generated at 2022-06-14 01:58:01.405518
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    with patch.object(BaseNodeTransformer, 'visit_Module') as generic_visit:
        transformer = MetaclassTransformer()
        node = ast.Module()
        transformer.visit_Module(node)
        generic_visit.assert_called_once_with(transformer, node)
        assert node.body[0] == six_import.get_ast()


# Generated at 2022-06-14 01:58:03.129148
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from six import PY27
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 01:58:04.685619
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.compiler import compiler_for


# Generated at 2022-06-14 01:58:10.428443
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    nodes = ast.parse("class A: pass")
    transformer = MetaclassTransformer()
    transformer.visit(nodes)
    assert str(nodes) == "class A: pass"

    nodes = ast.parse("class A(metaclass=B): pass")
    transformer = MetaclassTransformer()
    transformer.visit(nodes)
    assert str(nodes) == "class A(_py_backwards_six_withmetaclass(B))"

# Generated at 2022-06-14 01:58:17.700613
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = '''
    class A:
        class B:
            class C(metaclass=D):
                pass
        class E(metaclass=F):
            pass
    '''
    expected = '''
    class A:
        class B:
            class C(_py_backwards_six_withmetaclass(D)):
                pass
        class E(_py_backwards_six_withmetaclass(F)):
            pass
    '''
    module = ast.parse(source)
    transformer = MetaclassTransformer()
    transformed = transformer.visit(module)
    assert ast.dump(transformed, include_attributes=True) == expected

# Generated at 2022-06-14 01:58:23.825045
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import astor
    test_node = six_import()
    test_node.body.append(class_bases())
    node = test_node
    mt = MetaclassTransformer()
    mt.visit(node)
    assert mt.has_changed()
    assert mt.get_tree() is node

# Generated at 2022-06-14 01:58:32.714804
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:41.251238
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.inputcase import snippet_to_ast
    from .base import snippet_to_tree_transformer_class
    MetaclassTransformer = snippet_to_tree_transformer_class(MetaclassTransformer)
    class _snippet:
        # language=python
        body = '''
        class A(metaclass=B):
            pass
        '''
    module = snippet_to_ast(_snippet)
    MetaclassTransformer(module).visit(module)
    has_six_import = False
    for child in module.body:
        if isinstance(child, ast.ImportFrom) and child.module == 'six':
            assert child.names[0].name == 'with_metaclass'

# Generated at 2022-06-14 01:58:42.263587
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:58:47.552031
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    mt = MetaclassTransformer()
    test = """
    class A():
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A():
        pass
    """
    mod = ast.parse(test)
    mt.visit(mod)
    assert ast.dump(mod) == expected



# Generated at 2022-06-14 01:58:55.678281
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3
    from .base import BaseNodeTransformer

    import sys

    sys.version_info = (3, 7)  # Set your Python version
    parser = ast3.python_future_compatible_parse('')

    transformer = MetaclassTransformer()
    new_tree = transformer.visit(parser)

    assert transformer._transformed == True

    print(new_tree)
    # print(ast3.dump(new_tree, include_attributes=True))
    # print(transformer._dependencies)

    assert transformer._dependencies == ['six'] # type: ignore

# Generated at 2022-06-14 01:58:57.044587
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    transformer = MetaclassTransformer()
    assert transformer

# Generated at 2022-06-14 01:59:05.538508
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    x = ast.parse("class A(metaclass=B):\n\tpass")
    mt = MetaclassTransformer()
    mt.visit(x)
    assert x.body[0].__class__ == ast.ClassDef
    assert x.body[0].name == 'A'
    assert x.body[0].keywords == []
    assert x.body[0].bases > 0
    assert x.body[0].body[0].__class__ == ast.Pass

# Generated at 2022-06-14 01:59:09.855615
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = "class A(metaclass=B): pass"
    node = ast.parse(code)
    expected_code = "class A(_py_backwards_six_withmetaclass(B)): pass"
    node_expected = ast.parse(expected_code)
    transformer = MetaclassTransformer()
    assert transformer.visit(node) == node_expected

# Generated at 2022-06-14 01:59:23.344676
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    from typed_ast import ast3 as ast

    from . import compile_source

    from ..utils.snippet import snippet

    from ..utils.source import fix_indentation, insert_at


    @snippet
    def source(bases):
        class A(bases):
            pass


    def test_case(bases, expected):
        base_source = fix_indentation(source.get_body(bases=bases))
        tree = compile_source(base_source)
        tree = MetaclassTransformer().visit(tree)  # type: ignore
        expected_tree = compile_source(expected)
        self.assertEqual(expected_tree, tree)


# Generated at 2022-06-14 01:59:33.944033
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    from utils.test_visitor import TestVisitor

    test_visitor = TestVisitor(MetaclassTransformer)

    def check(test):
        test_visitor.reset()
        test_visitor.test(test)

    check("""
        class A(metaclass=B):
            pass
        """
    )

    check("""
        class A(B, metaclass=C):
            pass
        """
    )

    with pytest.raises(AssertionError):
        check("""
            class A(B, metaclass=C, D):
                pass
            """
        )


# Generated at 2022-06-14 01:59:54.125155
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast
    from ..utils.tree import parse

    source = """
        
        class A:
            pass
        class B(metaclass=A):
            pass"""
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A:
            pass
        class B(_py_backwards_six_withmetaclass(A)):
            pass
    """
    for tree in (parse(source), parse(source, mode='eval')):
        tree = MetaclassTransformer().visit(tree)
        assert ast.dump(tree, include_attributes=False) == expected

# Generated at 2022-06-14 02:00:03.982114
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    assert six_import.get_body() == [ast.ImportFrom(module='six', names=[ast.alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0)]
    assert class_bases.get_body(metaclass=ast.Name(id='B'), bases=[ast.Name(id='C')]) == [ast.Call(func=ast.Name(id='_py_backwards_six_withmetaclass', ctx=ast.Load()), args=[ast.Name(id='B'), ast.Name(id='C')], keywords=[])]

if __name__ == '__main__':
    test_MetaclassTransformer()

# Generated at 2022-06-14 02:00:15.472355
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    source = '''
        class MyList(metaclass=ABCMeta):
            pass
        class MyOtherList(metaclass=ABCMeta):
            pass        
    '''
    module = ast.parse(source)
    MetaclassTransformer.run_default(module)

    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class MyList(_py_backwards_six_withmetaclass(ABCMeta)):
            pass
        class MyOtherList(_py_backwards_six_withmetaclass(ABCMeta)):
            pass
        
    '''
    expected_ast = ast.parse(expected)
    ast.fix_missing_locations(expected_ast)
    assert ast.dump(module) == ast.dump(expected_ast)

# Generated at 2022-06-14 02:00:23.972213
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Arrange
    node = ast.parse('class A(metaclass=B):\n    pass')
    expected = ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass""")

    # Act
    actual = MetaclassTransformer().visit(node)

    # Assert
    assert ast.dump(expected) == ast.dump(actual)



# Generated at 2022-06-14 02:00:25.249543
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:36.228047
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import Source

    source = Source("""class Foo(Bar, Baz, metaclass=object): pass""")
    tree = source.parse()

    transformer = MetaclassTransformer()
    new = transformer.visit(tree)

    assert transformer._tree_changed is True

# Generated at 2022-06-14 02:00:43.345866
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = """
    class A(metaclass=M):
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    class A(_py_backwards_six_withmetaclass(M)):
        pass
    """
    result = MetaclassTransformer().visit_ClassDef(ast.parse(source).body[0])
    assert ast.dump(result) == ast.dump(ast.parse(expected).body[1])

# Generated at 2022-06-14 02:00:49.361371
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer

    class DummyTransformer(BaseNodeTransformer):
        def visit_ClassDef(self, node):
            return ast.ClassDef(name="DummyClass")

    node = ast.parse("class A(metaclass=B): pass")
    module = MetaclassTransformer().visit(node)
    module = DummyTransformer().visit(module)
    assert compile(module, "<test>", "exec").co_consts[0] == "DummyClass"

# Generated at 2022-06-14 02:00:56.379592
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import parse
    import ast
    import six

    module = """
    class A(metaclass=B):
        pass
    """
    module = parse(module, mode="exec")
    if six.PY2:
        result = MetaclassTransformer().visit(module)
        assert isinstance(result.body[0], ast.ClassDef)
        assert isinstance(
            result.body[0].bases[0],
            ast.Call)
        assert isinstance(result.body[0].bases[0].func, ast.Name)
        assert result.body[0].bases[0].func.id == "_py_backwards_six_withmetaclass"

# Generated at 2022-06-14 02:00:59.389737
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Create an instance of a parser and parse source
    parser = ast.PyCF_ONLY_AST.Parser()

# Generated at 2022-06-14 02:01:28.325734
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    class DummyTransformer(ast.NodeTransformer):
        pass


# Generated at 2022-06-14 02:01:29.695341
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import six_import, class_bases


# Generated at 2022-06-14 02:01:31.426847
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    MetaclassTransformer().visit(ast.parse('class A(metaclass=B): pass'))

# Generated at 2022-06-14 02:01:36.726857
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    tree = ast.parse(dedent('''\
    class A():
        pass
    '''))
    assert MetaclassTransformer(None).visit(tree) == ast.parse(dedent('''\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A():
        pass
    '''))


# Generated at 2022-06-14 02:01:43.763320
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    src = "class A(metaclass=B):\n    pass"
    tree = ast.parse(src)
    trans = MetaclassTransformer()
    trans.visit(tree)
    assert trans._tree_changed
    assert trans.dependencies == ['six']

    codeoutput = astor.to_source(tree).rstrip()

# Generated at 2022-06-14 02:01:45.053250
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import six


# Generated at 2022-06-14 02:01:56.952338
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    metaclass_transformer = MetaclassTransformer()
    # Create the test node
    simple_module = ast.Module(body=[ast.ClassDef(name="TestClass", 
                                                  bases=[ast.Name(id="object", ctx=ast.Load())], 
                                                  keywords=[ast.keyword(arg="metaclass", value=ast.Name(id="TestMetaClass", ctx=ast.Load()))], 
                                                  body=[ast.Pass()],
                                                  decorator_list=[])])
    # Test if the code is transformed correctly
    assert "from six import with_metaclass as _py_backwards_six_withmetaclass" == astunparse.unparse(metaclass_transformer.visit(simple_module)).split("\n")[0]
    assert astun

# Generated at 2022-06-14 02:02:06.576207
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():

    tree = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    MetaclassTransformer().visit(tree)


# Generated at 2022-06-14 02:02:14.142089
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..base import get_ast

    ast = get_ast("class A(metaclass=B): pass")

    assert [node.__class__.__name__ for node in ast.body] == [
        'ImportFrom',
        'ClassDef']
    assert isinstance(ast.body[1].bases[0], ast.Call)
    assert ast.body[1].bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert not ast.body[1].keywords

# Generated at 2022-06-14 02:02:25.043399
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import astor
    from typing import Any, Dict, Tuple
    from ..unitutil import a2
    from ..unitutil import NodeAssertion, function_name

    ast_tree1 = astor.parse('''
    class A:
        pass
    ''')
    expected_ast1 = astor.parse('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A:
        pass
    ''')
    ast_tree2 = astor.parse('''
    class B:
        pass
    class A:
        pass
    ''')

# Generated at 2022-06-14 02:03:28.713902
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast

# Generated at 2022-06-14 02:03:30.915559
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    MetaclassTransformer.__test__(False)

# Generated at 2022-06-14 02:03:37.076275
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...tests.transpile_testcase import TranspileTestCase
    from ...utils.snippet import snippet
    from ...utils.source import Source
    from ... import utils

    class Test(TranspileTestCase):
        def test_class_with_metaclass(self):
            self.assertCodeExecution("""
                import six
                class Meta(type):
                    pass
                class A(six.with_metaclass(Meta)):
                    pass
                a = A()
                print(a)
                print(type(a))
                print(A.__bases__)
                print(A.__class__.__bases__)
            """)


# Generated at 2022-06-14 02:03:46.093401
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    tree = ast.parse('class A(metaclass=B, c=1):\n  pass')
    tree = MetaclassTransformer.r(tree)
    assert astor.to_source(tree)
    assert astor.to_source(tree) == (
        'from six import with_metaclass as _py_backwards_six_withmetaclass\n\n'
        'class A(_py_backwards_six_withmetaclass(B, *[])):\n    pass'
    )
    tree = ast.parse('class A(b, metaclass=C, c=1):\n  pass')
    tree = MetaclassTransformer.r(tree)

# Generated at 2022-06-14 02:03:54.064160
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import typed_astunparse

    code = '''
    class A(metaclass=B):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''
    module = ast.parse(code)
    module = MetaclassTransformer().visit(module)
    assert typed_astunparse.unparse(module) == expected

# Generated at 2022-06-14 02:03:55.373222
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 02:04:04.037201
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    cls = ast.ClassDef(name='A',
                       bases=[ast.Name(id='object', ctx=ast.Load())],
                       keywords=[ast.arg(arg='metaclass',
                                         value=ast.Name(id='B', ctx=ast.Load()))],
                       body=[],
                       decorator_list=[],
                       )


# Generated at 2022-06-14 02:04:13.538144
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..parser import parse
    from ..utils.ast_helpers import print_tree
    import textwrap
    source = textwrap.dedent("""
            class C(metaclass=type):
                pass
            """)
    tree = parse(source)
    MetaclassTransformer().visit(tree)
    check = textwrap.dedent("""
            from six import with_metaclass as _py_backwards_six_withmetaclass
            class C(_py_backwards_six_withmetaclass(type, )):
                pass
            """)
    assert print_tree(tree) == check

# Generated at 2022-06-14 02:04:22.994899
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse
    m = ast.parse(
        "class C(metaclass=meta, bases=(a, b)):\n"
        "    pass"
    )
    mt = MetaclassTransformer()
    m = mt.visit(m)
    assert astunparse.unparse(m) == (
        "from six import with_metaclass as _py_backwards_six_withmetaclass\n"
        "class C():\n"
        "    _py_backwards_six_withmetaclass(meta, *(a, b,))"
    )

# Generated at 2022-06-14 02:04:26.701787
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    one_import = _get_one_import()
    mt = MetaclassTransformer()
    assert len(mt.visit_Module(one_import).body) == len(six_import.get_body()) + 1
