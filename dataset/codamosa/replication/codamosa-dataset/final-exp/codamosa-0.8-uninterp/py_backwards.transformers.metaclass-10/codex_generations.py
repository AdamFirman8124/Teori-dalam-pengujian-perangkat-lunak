

# Generated at 2022-06-14 01:55:04.437127
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.visitor import RecursiveVisitor
    from ..utils.io import StringIO

    class FindMethod(RecursiveVisitor):

        def __init__(self, *args, **kwargs):
            super(FindMethod, self).__init__(*args, **kwargs)
            self.class_def = None

        def visit_ClassDef(self, node: ast.ClassDef):
            if node.keywords:
                if node.keywords[0].arg == 'metaclass':
                    self.class_def = node
                    self.stop()

    module = ast.parse(StringIO('class A(metaclass=B): pass').read())
    transformer = MetaclassTransformer()
    transformer.visit(module)

    assert transformer._tree_changed

# Generated at 2022-06-14 01:55:06.716276
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer(target_version=(3,))

# Generated at 2022-06-14 01:55:14.707887
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    
    transformer = MetaclassTransformer()
    module = ast.Module(
        body=[
            ast.ClassDef(
                name='A',
                bases=[
                    ast.Name(
                        id='B',
                        ctx=ast.Load()
                    )
                ],
                keywords=[
                    ast.keyword(
                        arg='metaclass',
                        value=ast.Name(
                            id='C',
                            ctx=ast.Load()
                        )
                    )
                ],
                body=[],
                decorator_list=[],
                lineno=1,
                col_offset=0
            )
        ]
    )

# Generated at 2022-06-14 01:55:23.419767
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    expected = ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """, mode='exec')
    module = MetaclassTransformer().visit(module)
    assert module == expected
    assert module is not expected



# Generated at 2022-06-14 01:55:31.414141
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class Test(object):
        def assert_ast(self, node: ast.AST, expected: str) -> None:
            self.assertEqual(ast.dump(node), expected)

        def test_metaclass(self):
            source = '''
            class A(metaclass=B):
                pass
            '''
            module = ast.parse(source)
            transformer = MetaclassTransformer()
            module = transformer.visit(module)
            self.assertTrue(transformer._tree_changed)
            expected = '''
            from six import with_metaclass as _py_backwards_six_withmetaclass
            class A(_py_backwards_six_withmetaclass(B)):
                pass
            '''
            self.assert_ast(module, expected)


# Generated at 2022-06-14 01:55:40.134902
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as _ast

    class F(_ast.NodeTransformer):
        def generic_visit(self, node):
            print("generic_visit", type(node).__name__)
            return super().generic_visit(node)

    from .test_utils import def_context

    class MetaclassTransformer(MetaclassTransformer):
        def __init__(self, *args, **kwargs):
            self._tree_changed = kwargs.pop('tree_changed', False)
            super().__init__(*args, **kwargs)
            self._f = F()

        def visit_Str(self, node):
            return self._f.visit(node)

        def visit_Name(self, node):
            return self._f.visit(node)


# Generated at 2022-06-14 01:55:49.805089
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..testing import assert_source
    from .test_end2end import _TestTransformer

    class _MetaclassTransformer(_TestTransformer, MetaclassTransformer):
        pass

    source = '''
    class A(metaclass=int):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(int)):
        pass
    '''

    tree = ast.parse(source)
    new_tree = _MetaclassTransformer().visit(tree)
    assert_source(new_tree, expected)


# Generated at 2022-06-14 01:55:55.444322
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from .utils import roundtrip
    from .six_import import fix_six_import

    class C(metaclass=int):
        pass

    code = ast.dump(ast3.parse(roundtrip(C)))
    code = fix_six_import(code)
    assert code == "class C(_py_backwards_six_withmetaclass(int)):\n    pass"



# Generated at 2022-06-14 01:56:00.535758
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
        class A(metaclass=B):
            pass
    """)
    target = ast.parse("""
        class A(_py_backwards_six_with_metaclass(B)):
            pass
    """)
    MetaclassTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(target)

# Generated at 2022-06-14 01:56:10.599997
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Simple case
    assert MetaclassTransformer.run_on_node(
        ast.parse('class A(B): pass')
    ) == ast.parse(
        'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
        '\n'
        'class A(_py_backwards_six_withmetaclass(B)):\n'
        '    pass\n'
    )

    # Multiple bases

# Generated at 2022-06-14 01:56:23.208614
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import run_local_tests

    class_def = ast.parse("class A(metaclass=B):\n    pass").body[0]
    result = MetaclassTransformer().visit(class_def)

    assert isinstance(result, ast.ClassDef)
    assert result.keywords == []
    assert result.bases[0].func.id == "_py_backwards_six_withmetaclass"
    assert result.bases[0].args[0].id == "B"
    assert len(result.bases[0].args) == 2

    run_local_tests()

# Generated at 2022-06-14 01:56:32.973750
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class_def = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[
            ast.Pass()
        ]
    )
    
    import_six = six_import.get_body()[0]
    class_bases_assign = class_bases.get_body()
    class_def.bases = [class_bases_assign]

    module = ast.Module(body=[class_def])
    result = MetaclassTransformer().visit_Module(module)
    assert result.body == [import_six, class_def]

# Generated at 2022-06-14 01:56:33.450349
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:37.287544
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    import six
    import sys
    import builtins
    m = ast.parse("class A(metaclass=B): pass")
    x = MetaclassTransformer()
    x.visit(m)
    d = ast.Interactive(body=[m])
    code = compile(d, "", "exec")
    globs = globals().copy()
    globs.update(locals())
    globs.update(sys.modules)
    globs.update(locals())
    globs.update(globals())
    globs["six"] = six
    exec(code, globs)
    assert 'A' in globs
    assert 'B' in globs
    a = globs["A"]

# Generated at 2022-06-14 01:56:44.366435
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import astor
    from ...utils.test_utils import MockNode
    parser = ast.parse("class A(metaclass=B, other=1): pass")
    mock = MockNode(parser.body[0])
    visitor = MetaclassTransformer()
    visitor.visit(mock)
    assert astor.to_source(mock) == "class A(_py_backwards_six_withmetaclass(B))"

# Generated at 2022-06-14 01:56:57.030071
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..transformers import TransformerSequence

    class A(metaclass=object):
        pass

    actual_ast = ast.parse(dedent('''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(object)):
            pass
    '''))

    seq = TransformerSequence([MetaclassTransformer])
    transform = seq.visit(ast.parse(dedent('''
        class A(metaclass=object):
            pass
    ''')))

    assert ast.dump(transform) == ast.dump(actual_ast)

    # Unit test with multiple bases

# Generated at 2022-06-14 01:57:07.986730
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .base import BaseTestTransformer
    from .six import SixTransformer
    from .generic_function_dispatch import GenericFunctionDispatchTransformer

    tree = BaseTestTransformer.get_parsed('''
        class Foo(metaclass=Bar, arg='x'):
            pass
    ''', package='six')  # type: ignore

    class FakeTransformer(MetaclassTransformer):
        # type: () -> None
        last_visited = None

        def generic_visit(self, node):
            self.last_visited = node
            return node

    transformed = FakeTransformer().visit(tree)  # type: ignore
    assert transformed is tree

    fake_transformer = FakeTransformer()  # type: ignore
    class_def = tree.body[0]  # type: ast.ClassDef


# Generated at 2022-06-14 01:57:19.236243
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing.utils import transform, assert_transform, string
    m = """
    class A(B, metaclass=C):
        pass
    """
    assert_transform(
        transform(MetaclassTransformer, m),
        m,
    )
    assert_transform(
        transform(MetaclassTransformer, m),
        """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(C,*(B,))):
            pass
        """,
    )
    m = """
    class A(metaclass=B):
        def m(self):
            with D():
                pass
    """

# Generated at 2022-06-14 01:57:24.049258
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    metaclass_transformer = MetaclassTransformer()
    node = ast.parse('class A(B, metaclass=C): pass')
    metaclass_transformer.visit(node)

    assert node.body[0].bases[0].args[0].value.id == 'metaclass'

# Generated at 2022-06-14 01:57:34.278656
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TransformedClassDef:
        pass

    class UntransformedClassDef:
        pass

    node = ast.ClassDef(name="TransformedClassDef",
                        bases=[ast.Name(id="object", ctx=ast.Load())],
                        keywords=[ast.keyword(arg="metaclass",
                                              value=ast.Name(id="A", ctx=ast.Load()))],
                        body=[],
                        decorator_list=[])

    dummy_node = ast.ClassDef(name="UntransformedClassDef",
                              bases=[ast.Name(id="object", ctx=ast.Load())],
                              keywords=[],
                              body=[],
                              decorator_list=[])

    module = ast.Module(body=[node, dummy_node])


# Generated at 2022-06-14 01:57:42.980072
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    input = """
    class TestClass(metaclass=cls, TestClass1, TestClass2):
        pass
    """
    expect = """
    class TestClass(_py_backwards_six_with_metaclass(cls, TestClass1, TestClass2)):
        pass
    """
    node = ast.parse(input)
    MetaclassTransformer().visit(node)
    result = ast.dump(node)
    assert result == expect

# Generated at 2022-06-14 01:57:49.374063
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
        class A(metaclass=B):
            pass
        """
    expected_code = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """

    transformed_code = MetaclassTransformer.run_to_string(code)
    assert transformed_code == expected_code



# Generated at 2022-06-14 01:57:50.109860
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast

# Generated at 2022-06-14 01:57:58.830282
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import astor
    from py_backwards.transformers.metaclass import MetaclassTransformer
    source = """
        class A(metaclass=B):
            pass
        """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """
    tree = ast.parse(source)
    MetaclassTransformer().visit(tree)
    result = astor.to_source(tree)
    assert result == expected

# Generated at 2022-06-14 01:58:02.274584
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import dump
    tree = MetaclassTransformer().visit(ast.parse(
        'class A(metaclass=B): pass'
    ))

# Generated at 2022-06-14 01:58:11.759548
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class DummyVisitor(ast.NodeVisitor):
        def visit_List(self, node):
            return [self.visit(el) for el in node.elts]

        def visit_Name(self, node):
            assert isinstance(node.id, str)
            return node.id

    def visit(node):
        return DummyVisitor().visit(node)

    assert visit(class_bases.get_body(metaclass=ast.Name(id='B'),
                                      bases=[ast.Name(id='A')])) == ['_py_backwards_six_withmetaclass','B','A']
    assert visit(six_import.get_body()) == ['from six import with_metaclass as _py_backwards_six_withmetaclass']

    class DummyClass:
        pass

# Generated at 2022-06-14 01:58:12.877696
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..visitor import to_source


# Generated at 2022-06-14 01:58:21.953249
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    test_class_def = ast.parse('class MyClass(metaclass=abc.ABCMeta): pass').body[0]
    mt = MetaclassTransformer()
    mt.visit(test_class_def)
    assert mt._tree_changed
    assert (repr(test_class_def.bases) == 
            "Call(func=Name(id='_py_backwards_six_with_metaclass', ctx=Load()), args=[Name(id='abc', ctx=Load()), '.', Name(id='ABCMeta', ctx=Load())], keywords=[])")

# Generated at 2022-06-14 01:58:27.793553
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
    class A():
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A():
        pass
    """
    tree = ast.parse(code)
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    assert transformer.unparse() == expected



# Generated at 2022-06-14 01:58:36.980626
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    if sys.version_info < (3, 5):
        return

    metaclass = ast.Name(id='B', ctx=ast.Load())
    bases = [ast.Name(id='C', ctx=ast.Load()), ast.Name(id='D', ctx=ast.Load())]
    node = ast.ClassDef(name='A', bases=bases, keywords=[ast.arg(arg='metaclass', value=metaclass)])
    transformer = MetaclassTransformer()
    res = transformer.visit(node)
    assert transformer._tree_changed
    assert transformer._code_changed

    assert res.bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert res.bases[0].args[0] == metaclass


# Generated at 2022-06-14 01:58:46.158568
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:47.196759
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:53.194908
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import build_ast_tree
    transformer = MetaclassTransformer()
    code = """class Test(metaclass=test.test):
    pass"""
    tree = build_ast_tree(code, __name__)
    assert transformer.visit(tree) is True

# Generated at 2022-06-14 01:58:53.962286
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:07.663880
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class M(type): pass
    class A: pass

    assert ast.dump(MetaclassTransformer().visit(ast.parse('class B(metaclass=M): pass'))) == \
        ast.dump(ast.parse('from six import with_metaclass as _py_backwards_six_withmetaclass\n'
                           'class B(_py_backwards_six_withmetaclass(M)): pass'))

# Generated at 2022-06-14 01:59:14.290648
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import python_modernize
    import ast
    from ast import ClassDef, Name, Load, Pass, Module
    
    class DummyNodeTransformer(python_modernize.BaseNodeTransformer):
        def visit_Name(s, n):
            return n
    
    class Meta(type):
        pass
    
    class A:
        pass
    
    class C(A, metaclass=Meta):
        pass
    
    class Abstract(C):
        pass
    

# Generated at 2022-06-14 01:59:15.710571
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:23.727877
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test import transform_test_impl

    source = '''
        class A(metaclass=B):
            pass
    '''

    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    '''

    transform_test_impl(source, expected, MetaclassTransformer)

# Generated at 2022-06-14 01:59:31.823430
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    expected = class_bases.get_body(metaclass=ast.Name(id='B', ctx=ast.Load()),  # type: ignore
                                    bases=ast.List(elts=[]))
    node = ast.ClassDef(name='A', bases=[], keywords=[ast.arg(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
                        body=[ast.Pass()], decorator_list=[], lineno=1, col_offset=0)
    node = MetaclassTransformer().visit(node)
    assert node.bases == expected.args

# Generated at 2022-06-14 01:59:46.539735
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """It should transform:
        class A(metaclass=A):
            pass
    To:
        class A(_py_backwards_six_withmetaclass(A, *A)):
            pass

    """
    node = ast.ClassDef(name="A",
                        bases=[ast.Name("A", ast.Load())],
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name("A", ast.Load()))],
                        body=[ast.Pass()],
                        decorator_list=[])

    transformer = MetaclassTransformer()
    new_class = transformer.visit(node)  # type: ignore

    assert transformer.tree_changed
    assert new_class.bases[0].func.id == '_py_backwards_six_withmetaclass'
   

# Generated at 2022-06-14 02:00:11.091975
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
            class A(metaclass=B):
                pass
            """
    tree = ast.parse(code)
    expected = """
            from six import with_metaclass as _py_backwards_six_withmetaclass


            class A(_py_backwards_six_withmetaclass(B)):
                pass
            """
    tree = MetaclassTransformer().visit(tree)
    real = ast.dump(tree)
    assert real == expected

# Generated at 2022-06-14 02:00:20.351933
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    import textwrap
    from ..utils.snippet import snippet
    
    @snippet 
    def expected_body():
        class A(_py_backwards_six_withmetaclass(int)):
            pass

    @snippet
    def input_body():
        class A(metaclass=int):
            pass
    
    expected = expected_body.get_ast_tree()
    expected = expected.body[0]
    expected = ast.fix_missing_locations(ast.copy_location(expected, input_body.find_body()[0]))
    
    result = MetaclassTransformer(2, 7).visit(input_body.get_ast_tree())
    result = result.body[0]
    
    assert result == expected

# Generated at 2022-06-14 02:00:21.169416
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:27.048091
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import transform_and_compare

    @transform_and_compare
    def a():
        class A(metaclass=B):
            pass

    @transform_and_compare
    def a():
        class A(B, C, metaclass=D):
            pass

# Generated at 2022-06-14 02:00:37.518147
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from os.path import join
    from ..utils.parse import parse_module
    from ..utils.compile import (compile_source,
                                 typed_ast_to_original,
                                 compare_source)
    from .transform import transform
    from .base import get_workdir

    dir_path = get_workdir("test_visit_ClassDef")
    test_file = join(dir_path, "test_visit_ClassDef.py")
    with open(test_file, "w") as f:
        f.write("""class A(metaclass=B): pass""")

    expected_file = join(dir_path, "test_visit_ClassDef_expected.py")

# Generated at 2022-06-14 02:00:40.467726
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    ast_, mod = six_import.get_ast()
    ast_, six_withmetaclass = class_bases.get_ast()


# Generated at 2022-06-14 02:00:49.591485
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTester
    from .six import SixTransformer

    class_def = ast.ClassDef(name='A',
                             bases=[ast.Name(id='object', ctx=ast.Load())],
                             keywords=[ast.keyword(arg='metaclass',
                                                   value=ast.Name(id='B', ctx=ast.Load()))],
                             body=[],
                             decorator_list=[])


# Generated at 2022-06-14 02:00:50.765833
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(metaclass=type):
        pass



# Generated at 2022-06-14 02:01:01.495822
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    
    snippet = ast.parse("class A(metaclass=B): pass")
    
    # Expected AST
    ast_expected = ast.ClassDef(
        name='A',
        bases=[ast.Call(func=ast.Name(id='_py_backwards_six_withmetaclass'),
                        args=ast.List(elts=[
                            ast.Name(id='B'), ast.Tuple(elts=[])],
                                      ctx=ast.Load()), keywords=[], starargs=None,
                        kwargs=None)],
        body=[],
        decorator_list=[],
        keywords=[]
    )
    # Actual AST
    ast_actual = MetaclassTransformer(2, 7).visit(snippet)
    
    # assert

# Generated at 2022-06-14 02:01:09.637277
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer_visit_ClassDef_test
    from ..utils.tree import ast_to_str

    class TestClassTransformer(BaseNodeTransformer_visit_ClassDef_test, MetaclassTransformer):
        pass

    tests = [
        ('class A(metaclass=B): pass', 'class A(_py_backwards_six_withmetaclass(B))')
    ]

    for test in tests:
        tree = ast.parse(test[0])
        expected_tree = ast.parse(test[1])

        transformer = TestClassTransformer()
        actual_tree = transformer.visit(tree)
        assert ast_to_str(expected_tree) == ast_to_str(actual_tree)

# Generated at 2022-06-14 02:01:24.872531
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.test_utils import transform


# Generated at 2022-06-14 02:01:32.921495
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(object):
        pass
    class B(metaclass=type):
        pass
    class C(object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, object, metaclass=type):
        pass

    node = parse(inspect.getsource(A))
    MetaclassTransformer().visit(node)

# Generated at 2022-06-14 02:01:34.162102
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:01:35.588029
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor  # type: ignore


# Generated at 2022-06-14 02:01:44.392298
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse("class Foo(metaclass=Bar): pass")
    module_new = MetaclassTransformer().visit(module)
    assert 'from six import with_metaclass as _py_backwards_six_withmetaclass' in module_new.body[0].value.s
    assert isinstance(module_new.body[1].body[0].bases[0], ast.Call)
    assert module_new.body[1].body[0].bases[0].func.id == '_py_backwards_six_withmetaclass'


# Generated at 2022-06-14 02:01:49.746361
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    code = "class A(metaclass=B): pass"

    tree = ast.parse(code)
    print(astor.to_source(tree).strip())

    MetaclassTransformer().walk(tree)

    print(astor.to_source(tree).strip())

# Generated at 2022-06-14 02:02:00.207361
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..types import FunctionDef, Module, ClassDef, Load, Str, Attribute, Name

    node = Module(body=[
        FunctionDef(name='f', args=None, body=[
            ClassDef(name='A', bases=[Name(id='object', ctx=Load())], keywords=[],
                     body=[], decorator_list=[])
        ])
    ])
    expected = Module(body=[
        FunctionDef(name='f', args=None, body=[
            ClassDef(name='A', bases=[Name(id='_py_backwards_six_withmetaclass', ctx=Load())(
                args=[Name(id='object', ctx=Load())], keywords=[], starargs=None, kwargs=None
            )], keywords=[], body=[], decorator_list=[])
        ])
    ])

    assert Met

# Generated at 2022-06-14 02:02:09.197550
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ...tests.fixtures import make_test_module
    from ...tests.utils import round_trip

    module = '''\
        class A(metaclass=B):
            pass
        '''
    expected = '''\
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(with_metaclass(B)):
            pass
        '''
    module_node = make_test_module(module)
    result_node = MetaclassTransformer().visit(module_node)
    assert expected == round_trip(result_node)

# Generated at 2022-06-14 02:02:18.776773
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class Test(unittest.TestCase):
        def test_1(self):
            src = """
            class A(): pass
            """
            expected = """
            class A(): pass
            """
            _src = ast.parse(src)
            _expected = ast.parse(expected)
            # _src and _expected are identical
            self.assertEqual(_src, _expected)
            # convert _src
            m = MetaclassTransformer()
            new_src = m.visit(_src)
            # new_src and _expected are identical
            self.assertEqual(new_src, _expected)
            # the tree did not change during transform
            self.assertFalse(m._tree_changed)


# Generated at 2022-06-14 02:02:25.475422
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    source = """
        class A(metaclass=B):
            pass
        """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """
    tree = ast.parse(source)
    fixed_tree = MetaclassTransformer().visit(tree)
    assert ast.dump(fixed_tree) == expected

# Generated at 2022-06-14 02:03:05.511981
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.source import Source
    from ..utils.validate import validate_transformation

    source = Source("""
    class A(metaclass=B):
        pass
    """)

    expected_source = Source("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)

    tree = source.tree
    expected_tree = expected_source.tree

    transformer = MetaclassTransformer()
    assert transformer.tree_changed is False
    tree = transformer.visit(tree)
    assert transformer.tree_changed is True
    assert validate_transformation(tree, expected_tree)

# Generated at 2022-06-14 02:03:12.340107
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testing import check_not_changed
    from ..utils.testing import check_transformation
    from ..utils.testing import check_unchanged
    from ..utils.testing import transform

    from ..transforms.metaclass import MetaclassTransformer

    check_not_changed(MetaclassTransformer, 'pass')

    # §§class A:
    #     def x():
    #         pass
    # $$class A(x=1):
    #     pass

# Generated at 2022-06-14 02:03:13.717249
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 02:03:15.807442
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
  mt = MetaclassTransformer()

# Generated at 2022-06-14 02:03:26.341124
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """
    Args:
    Returns:
    Raises:
    """
    import typed_ast.ast3 as ast
    from ..utils.ast_factory import factory
    from ..transpiler.context import Context

    class MockMetaclassTransformer(MetaclassTransformer):
        def __init__(self):
            super().__init__(ctx=Context(), source=None)
            self._tree_changed = False

    class A(metaclass=object):
        pass


# Generated at 2022-06-14 02:03:28.356149
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..converter import Converter
    from ..utils.source import source_to_ast, ast_to_source


# Generated at 2022-06-14 02:03:36.218356
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    class TestMetaclass(unittest2.TestCase):
        def test_class_bases(self):
            node = ast.parse("class A(metaclass=bases): pass")
            transformer = MetaclassTransformer(2, 7)
            transformed = transformer.visit(node)

            self.assertIsInstance(transformed.body[0], ast.FunctionDef)
            self.assertIsInstance(transformed.body[1], ast.ClassDef)

            class_def = transformed.body[1]
            self.assertEqual(class_def.bases[0].func.id, '_py_backwards_six_withmetaclass')
            self.assertEqual(class_def.bases[0].args[0].id, 'bases')

# Generated at 2022-06-14 02:03:45.764071
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typing import Any
    from ..visitor import Visitor
    from ..utils.six import IS_PYTHON2
    import six
    import astroid  # type: ignore

    if not IS_PYTHON2:
        from ..processor import Processor  # type: ignore
        from ..transformers.metaclass import MetaclassTransformer

        class DummyProcessor(Processor):
            def __init__(self) -> None:
                self.register_transformer(MetaclassTransformer)

        dummy_processor = DummyProcessor()

    class FindAssign(Visitor):
        """Util to find the assignment in the AST of a class that uses the
        six.with_metaclass.

        """

        def __init__(self) -> None:
            self.bases = None  # type: Any



# Generated at 2022-06-14 02:03:47.170781
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:03:50.985649
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.source import source_to_ast as sta
    from ..utils.source import source_to_module as stm
    from ..utils.source import ast_to_source as ats
