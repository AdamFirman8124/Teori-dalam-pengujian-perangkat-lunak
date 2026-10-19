

# Generated at 2022-06-14 01:55:11.965855
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from typing import List
    from ..tests.utils import snippet_to_ast, dump_ast
    tree = snippet_to_ast("""
    class A(metaclass=B, object=C):
        pass
    """)
    transformer = MetaclassTransformer()
    dump_ast(tree)
    transformer.visit(tree)
    dump_ast(tree)
    assert tree.body[0].value == class_bases.get_body(metaclass=ast.Name(id='B'),
                                                      bases=ast.List(elts=[ast.Name(id='C')]))

# Generated at 2022-06-14 01:55:19.452369
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    _test = """
        class Foo(metaclass=Bar):
            pass
        """
    _result = """
        class Foo(_py_backwards_six_with_metaclass(Bar)):
            pass
        """
    _transformer = MetaclassTransformer()
    _transformer.visit(ast.parse(_test))
    assert _transformer.result == ast.parse(_result)

# Generated at 2022-06-14 01:55:20.198244
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:26.899305
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testutils.compile import compile_function

    def run_test(source):
        tree = ast.parse(source)
        tree = MetaclassTransformer().visit(tree)
        return compile_function(tree)

    # given
    test_cases = [
        """
        class A:
            pass
        """,
        """
        class A(metaclass=B):
            pass
        """
    ]

    # expect
    results = [
        """
        class A:
            pass
        """,
        """
        class A(_py_backwards_six_with_metaclass(B)):
            pass
        """
    ]

    for case, result in zip(test_cases, results):
        assert result == run_test(case)



# Generated at 2022-06-14 01:55:33.184391
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    import ast
    code = 'class A(metaclass=B, c=2, d=3):\n    pass'
    module = ast.parse(code)
    MetaclassTransformer().visit(module)
    assert 'import six' in astor.to_source(module)

    assert 'def _py_backwards_six_withmetaclass(metaclass, *bases):\n    return metaclass(\'tempclassname\', bases, {})' in astor.to_source(module)

    assert 'class A(_py_backwards_six_withmetaclass(B), c=2, d=3):\n    pass' in astor.to_source(module)

# Generated at 2022-06-14 01:55:36.976298
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .util import source_to_node

    src = """class A(metaclass=B):
        pass
    """


# Generated at 2022-06-14 01:55:41.993615
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = 'class A(metaclass=B): pass'
    visitor = MetaclassTransformer(2, 7)
    node = ast.parse(code)
    visitor.visit(node)
    expected = ['class A(_py_backwards_six_withmetaclass(B)): pass']
    assert to_source(node) == expected

# Generated at 2022-06-14 01:55:47.169175
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse
    with_metaclass_code = """class A(metaclass=B):
    pass"""
    actual_code = astunparse.unparse(MetaclassTransformer._test_model(with_metaclass_code))

# Generated at 2022-06-14 01:55:50.666221
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:55.710336
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    source = """class A(metaclass=B, c=Foo):
            pass
        """
    expected = """class A(_py_backwards_six_withmetaclass(B, Foo)):
            pass
        """

    tree = ast.parse(source)
    MetaclassTransformer().visit(tree)

    assert str(tree) == expected

# Generated at 2022-06-14 01:56:01.887439
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    code = """class X(metaclass=type): pass"""
    module = ast.parse(code)
    MetaclassTransformer().visit(module)
    assert six_import.get_body() in module.body  # type: ignore
    assert class_bases.get_body() in module.body  # type: ignore

# Generated at 2022-06-14 01:56:05.180703
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    t = MetaclassTransformer()
    imports = """import sys
from typing import Callable
from six import with_metaclass
"""

# Generated at 2022-06-14 01:56:09.588278
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    ret = MetaclassTransformer().visit_Module(ast.parse('class C(metaclass=B): pass'))
    assert isinstance(ret, ast.Module)
    assert isinstance(ret.body[0], ast.ImportFrom)
    assert isinstance(ret.body[1], ast.ClassDef)


# Generated at 2022-06-14 01:56:15.978965
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Setup
    node = ast.parse("class A(metaclass=B): pass")
    # Exercise
    MetaclassTransformer(node).visit(node)
    # Verify
    expected = six_import() + ast.parse("class A(_py_backwards_six_withmetaclass(B)): pass")
    assert ast.dump(expected) == ast.dump(node)


# Generated at 2022-06-14 01:56:16.587749
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:56:24.553944
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from py_backwards.transformers import MetaclassTransformer
    import typed_ast.ast3 as ast
    from py_backwards.utils.ast_builder import build_ast
    source = """
        import six.moves as six

        with six.with_metaclass(type):
            pass
        """

    transformer = MetaclassTransformer()
    tree = build_ast(source)
    transformer.visit(tree)
    assert transformer.transformed
    assert str(tree) == """
    import six.moves as six
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    
    
    with type():
        pass
    
    """

# Generated at 2022-06-14 01:56:28.042729
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = """class A(metaclass=B):\n    pass"""

# Generated at 2022-06-14 01:56:39.119950
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    class_def = ast.ClassDef(name="A",
                             bases=[ast.Name(id="m", ctx=ast.Load())],
                             keywords=[ast.keyword(arg="metaclass", value=ast.Name(id="B", ctx=ast.Load()))],
                             body=[], decorator_list=[], lineno=0, col_offset=0)


# Generated at 2022-06-14 01:56:42.450313
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    transpiler = MetaclassTransformer(target=(3, 6))
    transpiler.visit_Module(ast.parse("class A(metaclass=B): pass", mode='exec'))

# Generated at 2022-06-14 01:56:54.208333
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.dummy import DummyFile, DummyNode
    import_six = DummyNode(six_import.get_ast())
    metaclass = DummyNode(test=1)
    bases = DummyNode(test=2)
    with_metaclass = DummyNode(test=3)
    class_def = DummyNode(test=4, bases=[bases], keywords=[DummyNode(value=metaclass)])
    tree = DummyNode(
        body=[import_six, class_def],
        type_ignores=[bases, class_def]
    )
    f = DummyFile(tree)
    MetaclassTransformer().visit(f)
    assert tree.body[1] is class_def, 'class_def is in the correct spot'
    assert class_def.b

# Generated at 2022-06-14 01:56:59.911735
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    ast.parse("""
    class A(metaclass=B):
        pass
    """)
    MetaclassTransformer().visit(ast.parse("""
    class A(metaclass=B):
        pass
    """))

# Generated at 2022-06-14 01:57:07.182593
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    transformer = MetaclassTransformer()

    class Base(metaclass=six.with_metaclass(six.with_metaclass(object))): # type: ignore
        pass

    class A: pass

    code = transformer.to_source(Base)
    assert code == "class Base(_py_backwards_six_withmetaclass(_py_backwards_six_withmetaclass(object))): pass" # type: ignore

    code = transformer.to_source(A)
    assert code == "class A: pass"

# Generated at 2022-06-14 01:57:16.355907
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    """Compiles:
        class A(metaclass=B):
            pass
    To:
        class A(_py_backwards_six_with_metaclass(B))
    
    """
    m = ast.parse("""class A(metaclass=B):
        pass
    """)
    node = MetaclassTransformer().visit_Module(m)

# Generated at 2022-06-14 01:57:25.443244
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestMetaclassTransformer_visit_ClassDef(unittest.TestCase):
        def test_class_has_metaclass(self):
            node = ast.parse('''
            class A(metaclass=B):
                pass
            ''')
            metaclass_transformer = MetaclassTransformer()
            metaclass_transformer.visit(node)
            self.assertEqual(node.body[0].bases[0].args[0].id, '_py_backwards_six_withmetaclass')

        def test_class_no_metaclass(self):
            node = ast.parse('''
            class A(B):
                pass
            ''')
            metaclass_transformer = MetaclassTransformer()
            metaclass_transformer.vis

# Generated at 2022-06-14 01:57:35.262320
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .base import BaseTestTransformer
    
    class Test(BaseTestTransformer):
        Transformer = MetaclassTransformer

        def test_no_keyword(self):
            code = """
                class A:
                    pass
            """
            tree = ast.parse(code)
            tree = self.transform.visit(tree)
            self.assertSameTree(code, tree)
        
        def test_keyword(self):
            code = """
                class A(metaclass=B, c=d):
                    pass
            """
            expected = """
                from six import with_metaclass as _py_backwards_six_withmetaclass

                class A(_py_backwards_six_withmetaclass(B, c=d)):
                    pass
            """

# Generated at 2022-06-14 01:57:50.873024
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    node = ast.parse('class foo(metaclass=bar): pass').body[0]
    node2 = ast.parse('class foo(object, metaclass=bar): pass').body[0]
    node3 = ast.parse('class foo(bar, metaclass=baz): pass').body[0]
    node4 = ast.parse('class foo(bar, baz, metaclass=bing): pass').body[0]
    node5 = ast.parse('class foo(bar, baz, quux, metaclass=bing): pass').body[0]
    node6 = ast.parse('''class foo(bar, baz, quux, metaclass=bing):
        def __init__(self):
            pass
    ''').body[0]

# Generated at 2022-06-14 01:57:55.700738
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..run import quick_transform

    source = """class A(metaclass=B):
                     pass"""
    result = quick_transform(MetaclassTransformer, source)

# Generated at 2022-06-14 01:58:01.358009
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse("""
        class Foo(metaclass=Bar):
            pass
    """)
    transformer = MetaclassTransformer()
    node2 = transformer.visit(node)
    assert transformer.tree_changed == True

    node2_str = ast.unparse(node2)

# Generated at 2022-06-14 01:58:03.980019
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import ast as _ast
    exec(compile(ast.parse(MetaclassTransformer.__doc__), filename='<string>', mode='exec'))


# Generated at 2022-06-14 01:58:12.624292
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    transformer = MetaclassTransformer()

    node = ast.parse("""
        class A(metaclass=B):
            pass
        """)
    node = transformer.visit(node)  # type: ignore

# Generated at 2022-06-14 01:58:19.667838
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    cls_def = ast.parse('class A(B, metaclass=C):\n    pass')
    expected = """class A(_py_backwards_six_withmetaclass(C))\n    pass"""
    assert MetaclassTransformer().run(cls_def) == expected

# Generated at 2022-06-14 01:58:21.941679
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .fixtures import method_test


# Generated at 2022-06-14 01:58:30.488170
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = '''
        class Foo(metaclass=Bar):
            pass

        class Foo(Object, metaclass=Bar):
            pass
    '''
    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class Foo(_py_backwards_six_withmetaclass(Bar)):
            pass

        class Foo(_py_backwards_six_withmetaclass(Bar), Object):
            pass
    '''
    node = ast.parse(source)
    MetaclassTransformer().visit(node)
    assert ast.dump(node) == expected

# Generated at 2022-06-14 01:58:39.722155
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..introspect import get_names
    from .. import parse
    import six

    # Test for constructor of class MetaclassTransformer
    code = '''
    class A(metaclass=B, **d):
        pass
    '''

    f = six.exec_(code)
    tree = parse(code)
    node = tree.body[0]
    assert node.keywords[0].value.id == 'B', 'Input tree is not valid'
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    tree = transformer.get_tree()
    node = tree.body[0]
    assert get_names(node.bases[0]) == '_py_backwards_six_with_metaclass(B)', 'Output tree is not valid'

# Generated at 2022-06-14 01:58:49.129952
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse(textwrap.dedent('''\
    class A(metaclass=int):
        pass

    class B(object, metaclass=int):
        pass
    '''))

    module = MetaclassTransformer.run_pipeline(module)
    six = module.body[0]
    class_a: ast.ClassDef = module.body[1]
    class_b: ast.ClassDef = module.body[2]

    # Check if the from ... import ... is properly inserted
    assert isinstance(six, ast.ImportFrom)
    assert six.module == 'six'
    assert six.names[0].name == 'with_metaclass'
    assert six.names[0].asname == '_py_backwards_six_withmetaclass'

    # Check if the

# Generated at 2022-06-14 01:58:53.702365
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..test_utils import make_test, _remove_tree_nodes
    make_test(MetaclassTransformer, "class A(metaclass=type): pass", """
        import six

        class A(_py_backwards_six_withmetaclass(type)):
            pass
    """)

# Generated at 2022-06-14 01:59:07.405060
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from astor.code_gen import to_source
    from six import assertCountEqual

    p = ast.parse(
        '''
        class A(metaclass=B):
            pass
        ''')
    node = p.body[0]
    assert node.keywords == [ast.keyword(arg="metaclass", value=ast.Name(id="B", ctx=ast.Load()))]
    assert node.bases == []

    p = MetaclassTransformer().visit(p)

    assert node.keywords == []

# Generated at 2022-06-14 01:59:11.483825
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = "class A(object, metaclass=B): pass"
    expected = "from six import with_metaclass as _py_backwards_six_withmetaclass\n"
    expected += "class A(_py_backwards_six_withmetaclass(B, *[object]))"
    node = ast.parse(source)
    MetaclassTransformer(node).visit(node)
    assert ast.dump(node) == expected

# Generated at 2022-06-14 01:59:12.658818
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:59:16.291302
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .test_transformer_visitors import source_to_node


# Generated at 2022-06-14 01:59:25.758627
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ...typed_astunparse import dump
    from ..utils.examples import module_1
    from ..utils.visitor import ExampleTransformation

    tree = ExampleTransformation(MetaclassTransformer, example=module_1).tree


# Generated at 2022-06-14 01:59:30.430687
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .syntax_snippets import metaclass_snippets
    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer.visit(metaclass_snippets.get_tree())
# End unit test

# Generated at 2022-06-14 01:59:42.431297
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.source import source2ast

    code = """
    class A(metaclass=B):
        pass
    """
    expected_code = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """
    actual_tree = source2ast(code)
    expected_tree = source2ast(expected_code)
    transformer = MetaclassTransformer()
    assert transformer.visit(actual_tree) == expected_tree

# Generated at 2022-06-14 01:59:49.099227
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    from typing import cast
    from ..utils.tree import parse
    from ..utils.source import source
    from ..utils.transform import transform

    x = transform(MetaclassTransformer, parse(source("""
        class A(metaclass=B, x=y):
            pass
        """)))
    assert source(x) == """
        from six import with_metaclass as _py_backwards_six_withmetaclass;
        class A(_py_backwards_six_withmetaclass(B, *(x=y))):
            pass
        """
    if True:
        # test that no AST nodes were modified
        nodes = []

# Generated at 2022-06-14 01:59:56.614687
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # Arrange
    module = ast.parse('class A(B): pass')

    # Act
    module = MetaclassTransformer().visit(module)

    # Assert
    assert ast.dump(module) == '''\
Module(body=[
    ImportFrom(module='six', names=[
        alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')
    ], level=0),
    ClassDef(name='A', bases=[], keywords=[], body=[
        Pass()
    ])
])'''


# Generated at 2022-06-14 02:00:04.721742
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse("class A(metaclass=B): pass")
    MetaclassTransformer().visit(module)

    assert module.body[0].names[0].name == "six"
    assert module.body[0].names[0].asname == "six"
    assert module.body[0].names[1].name == "with_metaclass"
    assert module.body[0].names[1].asname == "_py_backwards_six_withmetaclass"
    assert isinstance(module.body[1], ast.FunctionDef)



# Generated at 2022-06-14 02:00:10.616085
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """Test constructor for class MetaclassTransformer"""
    target = (2, 7)
    dependencies = ['six']
    c = MetaclassTransformer(target, dependencies)
    assert c.target == target
    assert c.dependencies == dependencies

if __name__ == "__main__":
    c = MetaclassTransformer((2, 7), ['six'])

# Generated at 2022-06-14 02:00:19.658247
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    metaclass_one = ast.Name(id='one', ctx=ast.Load())
    class_one = ast.ClassDef(name='One', bases=[metaclass_one],
                             keywords=[ast.keyword(arg='metaclass', value=metaclass_one)], body=[])
    expected_class_one = ast.ClassDef(name='One',
                                      bases=[class_bases.get_body(metaclass=metaclass_one,  # type: ignore
                                                                  bases=ast.List(elts=[metaclass_one]))], body=[])
    assert_equals_ast(MetaclassTransformer().visit(class_one), expected_class_one)



# Generated at 2022-06-14 02:00:32.381446
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typing import List
    from ..utils import check_source

    class MetaclassTransformerTest(MetaclassTransformer):
        """A class that uses the MetaclassTransformer to test it"""
        def visit_Assign(self, node: ast.Assign) -> List[ast.AST]:
            new_target = ast.Name(id='new_target', ctx=ast.Store())
            node.targets.append(new_target)
            return node,

    check_source(MetaclassTransformerTest, '''
        class A(metaclass=B):
            pass
        ''')

    check_source(MetaclassTransformerTest, '''
        class B(metaclass=C):
            pass
        ''')

# Generated at 2022-06-14 02:00:34.984714
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:00:53.379341
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import ast

    def test(code: str, *, expected: ast.Module) -> None:
        # Arrange
        from . import six_import

        transformer = MetaclassTransformer()
        code_ast = ast.parse(code)

        # Act
        actual = transformer.visit_Module(code_ast)

        # Assert
        assert actual == expected


# Generated at 2022-06-14 02:00:59.245158
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    class_name = "_py_backwards_six_with_metaclass"
    node = ast.Module(body=[ast.ClassDef(name="A",
                                         bases=[ast.Name(id="B", ctx=ast.Load())],
                                         keywords=[ast.keyword(arg="metaclass",
                                                               value=ast.Name(id=class_name, ctx=ast.Load()))])])
    mt = MetaclassTransformer()
    mt.visit(node)
    assert eval(compile(node, "", "exec"))

# Generated at 2022-06-14 02:01:14.077982
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.testing import ast_compare
    from ..metaclass import MetaclassTransformer
    from ..utils.snippet import snippet
    from ..utils.tree import tree_from_source as tfs

    @snippet
    def before():
        class A(metaclass=B):
            pass

    @snippet
    def expected():
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass

    node = MetaclassTransformer.run(tfs(before.get_ast()))
    assert ast_compare(expected.get_ast(), node)

# Generated at 2022-06-14 02:01:25.395755
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(metaclass=int, object): pass')
    node = MetaclassTransformer().visit(node)
    node = ast.fix_missing_locations(node)

# Generated at 2022-06-14 02:01:35.687842
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast

    node = ast.Module(body=[ast.ClassDef(name='A',
                                         bases=[],
                                         keywords=[ast.keyword(arg='metaclass',
                                                                value=ast.Num(n=3))],
                                         body=[],
                                         decorator_list=[])])

    expected = ast.Module(body=[six_import.get_body()[0],
                                ast.ClassDef(bases=[class_bases.get_body(metaclass=ast.Num(n=3), bases=ast.List(elts=[])).body[0]],
                                             body=[],
                                             decorator_list=[],
                                             keywords=[],
                                             name='A')])

    transformer = MetaclassTransformer()

# Generated at 2022-06-14 02:01:44.495581
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Tests ``MetaclassTransformer.visit_ClassDef`` method
    using the following pattern:

    .. code-block:: python

        class A(metaclass=B):
            pass

    """
    ast_ = ast.parse(textwrap.dedent("""
    class A(metaclass=B):
        pass

    """), mode='exec')  # type: ignore

    new_ast = MetaclassTransformer(ast_).visit(ast_)  # type: ignore
    assert compile(new_ast, '', mode='exec')  # type: ignore



# Generated at 2022-06-14 02:01:56.469049
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from .nodes import Nodes

    class M(BaseNodeTransformer):
        def visit_ClassDef(self, node):
            print('Bases:', node.bases)
            # node.bases = [<ast3.Name object at 0x7f8d6c2d3710>]

            node.bases = ast.List(
                elts=[
                    ast.Name(id='B', ctx=ast.Load()),
                    ast.Name(id='C', ctx=ast.Load()),
                ]
            )

            print('Bases:', node.bases)
            # node.bases = <ast3.List object at 0x7f8d6c2d3898>

            return node

    node

# Generated at 2022-06-14 02:02:05.961602
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import sys
    from ..utils.source import source_to_code

    source = source_to_code('''
        class A(metaclass=B):
            pass
        ''')

    expected_source = source_to_code('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    ''')

    node = ast.parse(source)
    transformer = MetaclassTransformer(sys.version_info)
    transformer.visit(node)

    assert ast.dump(node) == ast.dump(ast.parse(expected_source))

# Generated at 2022-06-14 02:02:16.582505
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.fixtures import ast_from_snippet
    from ..utils.tree import assert_tree_equality

    # Unit test for method visit_ClassDef of class MetaclassTransformer
    def test_MetaclassTransformer_visit_ClassDef():
        from ..utils.fixtures import ast_from_snippet
        from ..utils.tree import assert_tree_equality

        # Simple example
        source = 'class A(metaclass=B): pass'
        expected = 'from six import with_metaclass as _py_backwards_six_with_metaclass\n' \
                   'class A(_py_backwards_six_with_metaclass(B)): pass'
        assert_tree_equality(expected, MetaclassTransformer, source)

        # Intermediate example

# Generated at 2022-06-14 02:02:25.743770
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3
    from . import Py2to3TreeTest

    class Test(Py2to3TreeTest):
        from . import my_method

        transform = MetaclassTransformer

        def test_classdef(self):
            before = ast.parse(
                """class Foo(metaclass=type): pass"""
            )
            after = ast.parse(
                """
                from six import with_metaclass as _py_backwards_six_withmetaclass

                class Foo(_py_backwards_six_withmetaclass(type)):
                    pass
                """
            )
            self.assertTransformEquals(before, after)


# Generated at 2022-06-14 02:02:49.509108
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    import inspect
    import six

    class Config(object):
        pass

    class Python2_with_MetaClass_Transformer(MetaclassTransformer):
        target = (2, 7)
        dependencies = ['six']

    class Python3_with_MetaClass_Transformer(MetaclassTransformer):
        target = (3,)
        dependencies = ['six']

    class Python2_with_MetaClass_Transformer_without_six(MetaclassTransformer):
        target = (2, 7)
        dependencies = []

    class Python3_with_MetaClass_Transformer_without_six(MetaclassTransformer):
        target = (3,)
        dependencies = []

    class Python3_without_MetaClass_Transformer(MetaclassTransformer):
        target = (3,)

# Generated at 2022-06-14 02:02:50.395143
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor

# Generated at 2022-06-14 02:02:57.867146
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import numpy as np
    import ast as ast
    node = ast.parse(
        '''class A(metaclass=np.ndarray):
            pass
            '''
    )
    MetaclassTransformer().visit(node)
    assert ast.dump(node) == "Module(body=[\n    ClassDef(name='A', bases=[Call(func=Attribute(value=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), attr='get_body', ctx=Load()), args=[Name(id='np', ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], keywords=[])], body=[Pass()], decorator_list=[])\n    ])"

# Generated at 2022-06-14 02:03:06.258046
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    class MockNode(ast.AST):
        body = []

    class MockClass(ast.AST):
        pass

    import astunparse

    # test constructors of class MetaclassTransformer
    transformer = MetaclassTransformer(MockNode, MockClass)
    assert isinstance(transformer, BaseNodeTransformer)

    # test visit_ClassDef method of class MetaclassTransformer
    test_node = ast.parse("class A(metaclass=B):\n    pass")
    test_transformer = MetaclassTransformer(test_node, None)
    test_transformer.visit(test_node)

# Generated at 2022-06-14 02:03:08.803421
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import ast
    test_MetaclassTransformer1 = MetaclassTransformer()

# Generated at 2022-06-14 02:03:14.865303
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import os
    import sys
    import astor
    import pytest

    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir)))

    from pybackwards.transformers.metaclass import MetaclassTransformer


# Generated at 2022-06-14 02:03:28.815987
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    from textwrap import dedent

    code = dedent('''
        def test():
            class A(metaclass=type, g=1):
                pass
    ''')

    code2 = dedent('''
        def test():
            from six import with_metaclass as _py_backwards_six_withmetaclass
            class A(_py_backwards_six_withmetaclass(type, metaclass=type, g=1)):
                pass
    ''')

    tree = ast.parse(code)
    converter = MetaclassTransformer()
    new_tree = converter.visit(tree)
    assert astor.to_source(new_tree) == code2

# Generated at 2022-06-14 02:03:36.662277
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from asttokens import ASTTokens

    metaclass_transform = MetaclassTransformer()
    source = '''
    class A(metaclass=B):
        pass
    '''
    tokens = ASTTokens(source, parse=True)
    tree = tokens.tree

    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 1
    assert isinstance(tree.body[0], ast.ClassDef)
    assert tree.body[0].name == 'A'
    assert isinstance(tree.body[0].bases[0], ast.Call)

    metaclass_transform.visit(tree)
    output = tokens.get_text()

    assert isinstance(tree, ast.Module)
    assert six_import.get_text() in output
    assert class_bases.get

# Generated at 2022-06-14 02:03:43.023036
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse(textwrap.dedent('''
    class A(metaclass=B, *args):
        pass
    '''))
    expected = ast.parse(textwrap.dedent('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B, *args)):
        pass
    '''))
    assert expected == MetaclassTransformer().visit(module)

# Generated at 2022-06-14 02:03:45.936788
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .. import compile
    import unittest


# Generated at 2022-06-14 02:04:18.812895
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():

    import textwrap

    test = textwrap.dedent(r"""
    import datetime
    class A(metaclass=datetime.date):
        pass
    """)

    expected = textwrap.dedent(r"""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    import datetime
    class A(_py_backwards_six_withmetaclass(datetime.date)):
        pass
    """).strip()

    result = MetaclassTransformer().transform_source(test)[0]
    assert result == expected

# Generated at 2022-06-14 02:04:19.863069
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:04:25.170899
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(metaclass=int):
        pass
    result = MetaclassTransformer().visit(ast.parse(source=inspect.getsource(A)))
    assert result == ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(int, object)):
        pass
    """)

# Generated at 2022-06-14 02:04:33.768542
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import copy
    import unittest
    import typed_ast.ast3 as ast
    import typed_astunparse

    class ClassDefTransformerTests(unittest.TestCase):

        def assert_code_equal(self, expected, node, mode='exec'):
            self.assertEqual(expected, typed_astunparse.unparse(node, mode=mode).strip())

        def test_visit_class_def(self):
            tree = ast.parse('class A(metaclass=B):\n    pass')
            expected = ast.parse('''
                class A(_py_backwards_six_withmetaclass(B)):
                    pass''')
            node = MetaclassTransformer().visit(tree)
            self.assert_code_equal(expected, node)

    unittest.main

# Generated at 2022-06-14 02:04:37.299783
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    _input = """
    class A(metaclass=B):
        pass
    """
    transformer = MetaclassTransformer()
    tree = ast.parse(_input)
    transformer.visit(tree)
    assert transformer._tree_changed

# Generated at 2022-06-14 02:04:47.630521
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    import six
    from ..utils.fake_six import fake_six_with_metaclass
    from ..pygram import python_symbols as syms

    class class_visitor(ast.NodeVisitor):
        def visit_ClassDef(self, node):
            self.assertEqual(len(node.keywords), 0)
            self.assertIsInstance(node.bases[0], ast.Call)
            func = node.bases[0].func
            self.assertIsInstance(func, ast.Attribute)
            self.assertIsInstance(func.value, ast.Name)
            self.assertIsInstance(func.value.ctx, ast.Load)
            self.assertEqual(func.value.id, 'six')

# Generated at 2022-06-14 02:04:58.611601
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testing import make_name, make_arguments, make_alias, make_keyword, make_literal
    from ..utils.tree import make_module
    from typed_ast import ast3
    
    import_ = ast3.Import([make_alias('six', 'six')])
    a_name = make_name('A')
    b_name = make_name('B')
    arguments = make_arguments()
    class_ = ast3.ClassDef(a_name, [], arguments, [], [], [make_literal(1)])
    arguments.kwonlyargs = [make_arg(make_name('metaclass'), b_name)]
    arguments.kw_defaults = [make_literal(2)]
    arguments.kwarg = make_name('kw')
    arguments.vararg = make

# Generated at 2022-06-14 02:05:03.984213
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ... import refactor

    source = '''class A(metaclass=B):
    pass'''