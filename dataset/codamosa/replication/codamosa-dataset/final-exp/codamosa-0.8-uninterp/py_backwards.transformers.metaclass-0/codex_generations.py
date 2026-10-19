

# Generated at 2022-06-14 01:55:01.704692
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    meta_transformer = MetaclassTransformer()
    source_code = "class A(metaclass=B): pass"
    source_ast = ast.parse(source_code)
    result_ast = meta_transformer.visit(source_ast)
    assert str(result_ast) == "from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(B, )):\n    pass\n"

# Generated at 2022-06-14 01:55:07.786629
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    # we use astor instead of typed_ast's ast.dump, because it will not dump
    # type annotations
    tree = ast.parse("""class A(metaclass=B):
    pass""")
    tree = MetaclassTransformer.run_pipeline(tree)
    print(astor.to_source(tree))

# Generated at 2022-06-14 01:55:20.790688
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from six import with_metaclass
    from ..utils.source import source_to_ast as to_ast
    from ..utils.source import ast_to_source as to_source

    # python3 class with no metaclass
    py3_class = to_ast('''class C(object): pass''')
    py3_class_transformed = to_ast('''class C(_py_backwards_six_withmetaclass(object, *[])): pass''')
    mt = MetaclassTransformer()
    mt.visit(py3_class)
    assert py3_class == py3_class_transformed

    # python3 class with metaclass specified
    # todo: python3 provides a way to do this without using six

# Generated at 2022-06-14 01:55:30.568996
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('import six')
    module.body.insert(0, ast.FunctionDef(name='foo',
                                          body=[ast.Pass()],
                                          args=ast.arguments(args=[],
                                                             vararg=None,
                                                             kwarg=None,
                                                             kwonlyargs=[],
                                                             kw_defaults=[],
                                                             defaults=[])))

    node_transformer = MetaclassTransformer()
    node_transformer.visit(module)
    assert node_transformer._tree_changed is True

    result = ast.dump(node_transformer.visit(module))

# Generated at 2022-06-14 01:55:34.549555
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    snippet_test_1 = snippet("""
    class A(metaclass=B):
        pass
    """)
    
    actual = snippet_test_1.get_tree(MetaclassTransformer)

    expected = snippet("""
    from six import with_metaclass as _py_backwards_six_with_metaclass

    class A(_py_backwards_six_with_metaclass(B)):
        pass
    """)

    assert actual == expected.get_tree()



# Generated at 2022-06-14 01:55:35.507420
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:46.356410
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..transpile import Transpiler
    import typed_ast.ast3 as ast
    data1 = ast.parse(
        """
        import typing as t
        import six
        class A(object):
            pass
        """)

    data2 = ast.parse(
        """
        import typing as t
        import six
        class A(t.Generic[t.Any], six.with_metaclass(object)):
            pass
        """)

    data3 = ast.parse(
        """
        import typing as t
        import six
        class A(metaclass=object):
            pass
        """)

    data4 = ast.parse(
        """
        import typing as t
        import six
        class A(object, metaclass=object):
            pass
        """)


# Generated at 2022-06-14 01:55:56.533304
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_transformer_utils import parse
    from .test_transformer_utils import compare

    exp = "from six import with_metaclass as _py_backwards_six_withmetaclass\n" \
          "class A(_py_backwards_six_withmetaclass(B, C)):\n" \
          "    pass\n"

    node = parse("class A(metaclass=B, C): pass")
    node = MetaclassTransformer(node).visit(node)
    compare(node, exp)

    exp = "from six import with_metaclass as _py_backwards_six_withmetaclass\n" \
          "class A(_py_backwards_six_withmetaclass(B, C)):\n" \
          "    pass\n"

   

# Generated at 2022-06-14 01:55:58.808570
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast27
    from .test_unparser import Unparser


# Generated at 2022-06-14 01:56:09.299368
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    snippet_g = snippet.get_body
    import_g = six_import.get_body
    class_g = class_bases.get_body
    module = ast.parse(snippet_g("""
    class MyClass(metaclass=MyMeta):
        pass"""))
    output = ast.parse(snippet_g("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class MyClass(_py_backwards_six_withmetaclass(MyMeta)):
        pass"""))
    m = MetaclassTransformer()
    assert m.visit(module) == output
    m = MetaclassTransformer()
    m.visit(output)
    assert not m.tree_changed()


# Generated at 2022-06-14 01:56:21.359601
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from pathlib import Path
    import ast
    from unittest import TestCase

    from typed_ast import ast3 as typed_ast
    from typed_ast.ast3 import Module, ClassDef, Name, Tuple, AST, List, Keyword
    from type_inference_programs.src.utils import ast_compare
    from type_inference_programs.src.compiler.six import six_import
    from type_inference_programs.src.compiler.six import class_bases
    from type_inference_programs.src.compiler.python_version import MetaclassTransformer


    @snippet
    def class_a():
        class A(metaclass=B):
            pass



# Generated at 2022-06-14 01:56:30.774033
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    raw_source = """
        class A(object):
            pass
        class B(metaclass=A):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(object):
            pass


        class B(_py_backwards_six_withmetaclass(A)):
            pass
    """
    tree: ast.AST = ast.parse(raw_source)
    transformer = MetaclassTransformer()
    tree = transformer.visit(tree)
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 01:56:35.841649
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..all import AllTransformer
    import unittest
    
    class TestCase(unittest.TestCase):

        def test_without_metaclass(self):
            for version in [(2, 7), (2, 8)]:
                with self.subTest(version=version):
                    transformer = AllTransformer(transpile_version=version)
                    klass = ast.ClassDef(
                        name="A",
                        bases=[],
                        body=[],
                        keywords=[],
                        starargs=None,
                        kwargs=None,
                        decorator_list=[],
                    )

                    self.assertIs(
                        transformer.visit(klass),
                        klass,
                    )


# Generated at 2022-06-14 01:56:36.856056
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:42.228785
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import sys

    import six
    from six.moves import builtins

    from py_backwards.transformers.metaclass import \
        MetaclassTransformer  # NOQA

    # The transformer will insert the snippet at the start of the module
    snippet_body = six_import.get_body()
    test_body = [ast.ClassDef(name='TestClass',
                              bases=[ast.Str(s=six.text_type('TestBase'))],
                              keywords=[ast.Keyword(arg='metaclass',
                                                    value=ast.Name(
                                                        id='TestMetaClass',
                                                        ctx=ast.Load()))],
                              body=[],
                              decorator_list=[])]



# Generated at 2022-06-14 01:56:54.054069
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testing import assert_node_transformed

    assert_node_transformed(MetaclassTransformer,
                            """
                            class A:
                                pass
                            """,
                            """
                            class A:
                                pass
                            """)
    assert_node_transformed(MetaclassTransformer,
                            """
                            class A(metaclass=B):
                                pass
                            """,
                            """
                            from six import with_metaclass as _py_backwards_six_withmetaclass
                            class A(_py_backwards_six_withmetaclass(B)):
                                pass
                            """)

# Generated at 2022-06-14 01:57:06.120474
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    import os
    from sys import path as sys_path  # type: ignore
    from os import path as os_path
    import six
    import ast as pyast
    from ..utils.parser import get_parser
    from ..utils.source import source_to_unicode
    from ..utils.compiler import compile_snippet
    from ..utils.future import annotations

    parser = get_parser(target=MetaclassTransformer.target)
    MetaclassTransformer._tree_changed = False

    source = source_to_unicode('''
    class A(metaclass=B):
        pass
    ''')
    code = compile_snippet(source, parser=parser)
    tree = parser.parse(source)
    transformer = MetaclassTransformer()
    new_tree = transformer.vis

# Generated at 2022-06-14 01:57:18.211749
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Arrange
    module = ast.parse('class A(metaclass=B, c=d):\n  pass')
    transformer = MetaclassTransformer()

    # Act
    transformed = transformer.visit(module)  # type: ignore
    print('VISITED: {}'.format(ast.dump(transformed, annotate_fields=False)))
    string_result = ast.unparse(transformed)

    # Assert
    transformer.exit()
    assert transformer.dependencies == ['six']
    assert transformer.tree_changed
    assert string_result == 'from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B, c=d)):\n  pass'

# Generated at 2022-06-14 01:57:24.586208
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import NodeTransformerTestCase
    from .utils import parse, compare_nodes

    class Test(NodeTransformerTestCase):
        transformer = MetaclassTransformer
        target = '2.7'
        dependencies = ['six']

        def test_normal(self):
            """Test that MetaclassTransformer doesn't change anything in normal
            code.
            
            """

# Generated at 2022-06-14 01:57:30.697947
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    src = """class A(metaclass=B, c=1):
                pass"""
    tree = ast.parse(src)
    MetaclassTransformer().visit(tree)
    expected = """_py_backwards_six_withmetaclass(metaclass=B, c=1)
        pass"""
    actual = astor.to_source(tree)
    assert expected == actual

# Generated at 2022-06-14 01:57:47.541810
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source

    for version in [(2, 7), (2, 8)]:
        s = source(version, '''
            class A(metaclass = B):
                pass
        ''')
        node = ast.parse(s)

        mt = MetaclassTransformer()
        cnode = mt.visit(node)

        assert len(cnode.body[0].bases[0].elts) == 1
        assert cnode.body[0].bases[0].elts[0].id == 'B'
        assert cnode.body[0].bases[0].elts[0].ctx == ast.Load


# Generated at 2022-06-14 01:57:57.786115
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Create a simple ast
    mod = ast.Module(body=[ast.ClassDef(name='A', bases=[], 
                                        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='MyMeta', 
                                        ctx=ast.Load()))], body=[ast.Pass()], decorator_list=[])])
    # Create expected ast
    expected_mod = ast.Module(body=[six_import.get_body(), 
                                    ast.ClassDef(name='A', bases=class_bases.get_body(
                                        metaclass=ast.Name(id='MyMeta', 
                                                           ctx=ast.Load()), bases=ast.List(elts=[])), 
                                        keywords=[], body=[ast.Pass()], decorator_list=[])])
    # Create

# Generated at 2022-06-14 01:58:04.362845
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source
    from . import run_transformer

    code = source('''
    class A(metaclass=B):
        pass
    ''')
    result = run_transformer(MetaclassTransformer, code)
    assert result == source('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    ''')

# Generated at 2022-06-14 01:58:10.497927
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    visitor = MetaclassTransformer()

    node = ast.ClassDef(
        name="Foo",
        bases=[],
        body=[],
        keywords=[
            ast.keyword(arg="metaclass",
                        value=ast.Name(id="FooMeta"))
        ],
        decorator_list=[],
        lineno=1,
        col_offset=0,
    )

    ret = visitor.visit_ClassDef(node)

    expected_bases = class_bases.get_body(metaclass=ast.Name(id="FooMeta"),
                                          bases=ast.List(elts=[]))


# Generated at 2022-06-14 01:58:11.537354
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:58:19.455359
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test that a class with a metaclass is changed to use _py_backwards_six_withmetaclass."""
    module = six_import.get_ast('from enum import Enum')
    assert module.body[0].name == '_py_backwards_six_withmetaclass'

    metaclass = ast.Name(id='Enum', ctx=ast.Load())
    bases = [ast.Name(id='object', ctx=ast.Load())]
    expected = class_bases.get_ast(metaclass=metaclass, bases=bases)

# Generated at 2022-06-14 01:58:27.083064
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse(textwrap.dedent("""
    class A(metaclass=B):
        pass
    """), mode='exec')
    node1 = MetaclassTransformer().visit(node)
    expected_node = ast.parse(textwrap.dedent("""
    _py_backwards_six_withmetaclass(B, *[])
    class A(_py_backwards_six_withmetaclass(B, *[])):
        pass
    """), mode='eval')
    assert node1.body[0].value.value == expected_node.body[0].value

# Generated at 2022-06-14 01:58:31.788323
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """This tests the method visit_ClassDef of class MetaclassTransformer"""
    module = ast.parse('class A(b, c=d, metaclass=C):\n    pass')
    MetaclassTransformer().visit(module)

# Generated at 2022-06-14 01:58:38.736436
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = dedent("""\
        class A(metaclass=B, **kw):
            pass
    """)
    expected_code = dedent("""\
        class A(_py_backwards_six_withmetaclass(B, **kw)):
            pass
    """)
    expected_ast = ast.parse(expected_code)
    actual_ast = MetaclassTransformer().visit(ast.parse(code))
    assert compare_ast(actual_ast, expected_ast)
    assert MetaclassTransformer().tree_changed()



# Generated at 2022-06-14 01:58:44.742965
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    
    text = ("class A(metaclass=B): pass")
    node = ast.parse(text=text)
    mct = MetaclassTransformer()
    mct.visit(node)
    assert text_type(node) == ("class A(_py_backwards_six_withmetaclass(B)): pass")

# Generated at 2022-06-14 01:59:04.357375
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .fake_ast import make_fake_ast
    import ast

    class_def = ast.ClassDef(name='A',
                             bases=[],
                             keywords=[ast.keyword(arg='metaclass',
                                                    value=ast.Str(s='B'))],
                             body=[],
                             decorator_list=[])
    module = make_fake_ast(ast.Module(body=[class_def]))
    MetaclassTransformer().visit_Module(module)
    assert str(module) == "from six import with_metaclass as _py_backwards_six_withmetaclass\n" + \
                          "class A(_py_backwards_six_withmetaclass(B))\n"

# Generated at 2022-06-14 01:59:11.719803
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import ClassDef, Expr, Load, Name, List, Str, keyword

    class_def = ClassDef(name='A',
                         bases=[Expr(value=Name(id='B', ctx=Load()))],
                         keywords=[keyword(arg='metaclass',
                                           value=Expr(value=Name(id='C', ctx=Load())))],
                         body=[])

# Generated at 2022-06-14 01:59:20.443505
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Test for issue #123 (https://github.com/serge-sans-paille/python-future/issues/123)
    source = """
    from functools import reduce
    from .six import with_metaclass

    class LazyIterator(with_metaclass(type, Iterator)):
        ...
    """
    tree = ast.parse(source)
    new_tree = MetaclassTransformer().visit(tree)
    assert compile(new_tree, '<test>', 'exec')

# Generated at 2022-06-14 01:59:28.546045
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast

    node = ast.ClassDef(name='A',
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='B'))],
                        bases=[ast.Name(id='X')],
                        body=[])

    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)

    assert isinstance(new_node, ast.ClassDef)
    assert new_node.bases == class_bases.get_body(metaclass=ast.Name(id='B'),  # type: ignore
                                                  bases=ast.List(elts=[ast.Name(id='X')]))
    assert len(new_node.keywords) == 0

# Generated at 2022-06-14 01:59:38.565809
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...utils.testing import run_transform_test
    from ...utils.node import ast_from_str

    source = ast_from_str("""
    class A(object, metaclass=B, foo=bar):
        pass
    class B:
        pass
    """)

    # transformed = ast_from_str("""
    # class A(_py_backwards_six_withmetaclass(B, object), foo=bar):
    #     pass
    # class B:
    #     pass
    # """)
    # assert transformed == MetaclassTransformer().visit_Module(source)

    class_def = source.body[0]
    assert class_def.keywords[0].arg == 'metaclass'


# Generated at 2022-06-14 01:59:43.982790
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
  from typed_ast import ast3 as ast
  import astor
  from six_with_metaclass_transformer import MetaclassTransformer, class_bases, six_import
  import astor.codegen
  transformer = MetaclassTransformer()
  node = ast.parse("""class A(metaclass=B): pass""")
  result = transformer.visit(node)
  expected_output = ast.parse("""
  from six import with_metaclass as _py_backwards_six_withmetaclass
  class A(_py_backwards_six_withmetaclass(B)): pass
  """)
  assert astor.to_source(result) == astor.to_source(expected_output)

# Generated at 2022-06-14 01:59:54.298109
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Unit test for method visit_ClassDef of class MetaclassTransformer
    """
    # Given
    module = ast.parse(dedent('''\
        class A(metaclass=type):
            pass

        class B():
            pass
    '''))
    metaclass_transformer = MetaclassTransformer()

    # When
    metaclass_transformer.visit(module)

    # Then
    print(ast.dump(module))

# Generated at 2022-06-14 02:00:05.447066
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    a = ast.Module([ast.ClassDef(name='A',
                                 bases=[ast.Name(id='m', ctx=ast.Load())],
                                 keywords=[ast.keyword(arg='metaclass',
                                                       value=ast.Name(id='B',
                                                                      ctx=ast.Load()))],
                                 body=[ast.Pass()],
                                 decorator_list=[])])

# Generated at 2022-06-14 02:00:13.068806
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    node = ast.parse("class A(metaclass=int): pass")
    trans = MetaclassTransformer()
    trans.visit(node)
    assert trans._tree_changed == True
    assert astor.to_source(node) == "from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(int)):\n    pass\n"



# Generated at 2022-06-14 02:00:14.460548
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:35.044398
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast import Assign, ClassDef, Expr, Load, Name, Num, Store, parse
    from astunparse import unparse
    node = parse("class A(metaclass=B):\n    pass")
    expected = parse("from six import with_metaclass as _py_backwards_six_with_metaclass\nclass A(_py_backwards_six_with_metaclass(B)):\n    pass")
    transformer = MetaclassTransformer()
    result = transformer.visit(node)
    assert result == expected

# Generated at 2022-06-14 02:00:45.505602
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import make_unexpected_visit_test
    from .test_utils import round_trip

    code = '''
    class T(metaclass=abc.ABCMeta):
        pass
    '''
    expected_code = '''
    import six
    class T(six.with_metaclass(abc.ABCMeta)):
        pass
    '''
    mt = MetaclassTransformer(code, (3, 6))
    mt.visit(ast.parse(code))
    assert round_trip(mt.root) == round_trip(expected_code)
    assert mt.root.body[0] is mt.six_import

    mt = MetaclassTransformer(code, (2, 7))
    mt.visit(ast.parse(code))

# Generated at 2022-06-14 02:00:51.134215
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("class A(metaclass=B): pass")
    expected = ast.parse("from six import with_metaclass\nclass A(with_metaclass(B)): pass")
    transformer = MetaclassTransformer()
    transformer.visit(node)
    assert ast.dump(node) == ast.dump(expected)



# Generated at 2022-06-14 02:01:01.867189
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class Base: pass
    class Meta(type): pass

    def test(bases, expected_bases):
        node = ast.ClassDef(name='A',
                            bases=bases,
                            keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='Meta', ctx=ast.Load()))],
                            body=[ast.Pass()],
                            decorator_list=[])
        result = MetaclassTransformer().visit_ClassDef(node)

        print(ast.dump(result))
        assert ast.dump(result) == ast.dump(ast.ClassDef(name='A',
                                                         bases=expected_bases,
                                                         keywords=[],
                                                         body=[ast.Pass()],
                                                         decorator_list=[]))


# Generated at 2022-06-14 02:01:15.672676
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from .fixer_util import tokenize_module, parse_module, round_trip
    from .six_import import fix_six_import
    from .six_metaclass import fix_six_metaclass

    src = """
    class A(metaclass=B):
        pass
    """
    tree = parse_module(src)
    _, new_tree = fix_six_metaclass(tree, 'six')
    fixed_src = round_trip(new_tree)
    fixed_src = round_trip(parse_module(fixed_src))
    fixed_src = fix_six_import(fixed_src)
    module = parse_module(fixed_src)
    #print(fixed_src)
    assert isinstance(module, ast3.Module)

# Generated at 2022-06-14 02:01:24.728655
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testutils import assert_in_out
    assert_in_out(fixtures='test_MetaclassTransformer_visit_ClassDef',
                  transformer=MetaclassTransformer,
                  code_before="""
    class A(metaclass=B, baz='baz'):
        pass

    class C(D):
        pass
    """,
                  code_after="""
    # doctest: +SKIP
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, *[])):
        pass

    class C(D):
        pass
    """,
                  )

# Generated at 2022-06-14 02:01:26.456360
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..visitor import StrictTestVisitor
    from .. import transforms


# Generated at 2022-06-14 02:01:28.183291
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3
    transformer = MetaclassTransformer()

# Generated at 2022-06-14 02:01:37.802586
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .. import test_transformer
    node = test_transformer.parse(r'''
    class A(metaclass = B):
        pass
    ''')
    node = MetaclassTransformer().visit(node)

    assert list(ast.walk(node)) == [
        ast.Module,
        ast.ImportFrom,
        ast.FunctionDef,
        ast.arguments,
        ast.arg,
        ast.arg,
        ast.Return,
        ast.ClassDef,
        ast.arguments,
        ast.arg,
        ast.arg,
        ast.List,
        ast.Call,
        ast.Name,
        ast.Name,
        ast.Name,
    ]
    return node

# Generated at 2022-06-14 02:01:46.760444
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    before = """\
    class A(object, metaclass=B):
        pass
    """
    
    after = """\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B, object)):
        pass
    """
    tr = MetaclassTransformer()
    tree = ast.parse(before)
    tree = tr.visit(tree)
    assert_equal_codes(ast.unparse(tree), after)
    assert_equal_codes(ast.unparse(tr.restore_tree(tree)), before)

# Generated at 2022-06-14 02:02:17.313411
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:22.825839
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast import parse
    from ..utils.test import generate_visit_test

    generate_visit_test(MetaclassTransformer, parse('''
        class A(metaclass=B):
            pass
    '''), parse('''
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    '''))

# Generated at 2022-06-14 02:02:32.251110
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Tests the visit_ClassDef method of class MetaclassTransformer
    # Given
    class TestAST(ast.AST):
        _fields = ('name', 'methods')

    class TestModule(ast.Module):
        _fields = ('body',)

    class TestClassDef(ast.ClassDef):
        _fields = ('name', 'bases', 'keywords', 'body')

    # When
    transformer = MetaclassTransformer()
    snippet = '''
    class Node(metaclass=TestAST):
        def __init__(self, name):
            self.name = name
    '''
    tree = ast.parse(snippet)
    transformer.visit(tree)

    # Then
    class_def = tree.body[0]
    assert class_def.__class__ == TestClassDef
   

# Generated at 2022-06-14 02:02:32.963044
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:02:39.755603
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    tree = ast.parse("""class A(metaclass=B):\n    pass""")

    node = transformer.visit(tree.body[0])
    assert transformer._tree_changed
    assert transformer._imports_changed
    assert isinstance(node, ast.ClassDef)
    assert isinstance(node.bases[0], ast.Call)
    assert node.bases[0].func.id == "_py_backwards_six_withmetaclass"

# Generated at 2022-06-14 02:02:41.575637
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:50.908079
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    
    import sys
    if sys.version_info[:2] == (3, 6):
        # Using python 3.6
        node = ast.parse(dedent('''
            class A(metaclass=B):
                pass
        '''))
        expected = ast.parse(dedent('''
            from six import with_metaclass as _py_backwards_six_withmetaclass
            
            class A(_py_backwards_six_withmetaclass(B)):
                pass
        '''))
        assert ast.dump(transformer.visit(node)) == ast.dump(expected)

# Generated at 2022-06-14 02:02:58.212607
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import make_test, get_test_results
    tests = [
        make_test("""
        class A(metaclass=B):
            pass
        """, """
        class A(_py_backwards_six_withmetaclass(B))
            pass
        """, false_positive=True),

        make_test("""
        class A(metaclass=B, C):
            pass
        """, """
        class A(_py_backwards_six_withmetaclass(B, C)
            pass
        """, false_positive=True),

        make_test("""
        class A():
            pass
        """, """
        class A():
            pass
        """),
    ]

    return get_test_results(MetaclassTransformer, tests)



# Generated at 2022-06-14 02:02:58.755465
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:06.154053
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from ..utils.tree import print_node
    from ..compat import parse
    from ..utils.source import dedent

    source = dedent("""
    class A(metaclass=B):
        pass
    """)
    tree = parse(source)
    tree = MetaclassTransformer().visit(tree)  # type: ignore
    assert print_node(tree) == dedent("""
    from six import with_metaclass as _py_backwards_six_withmetaclass


    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)

# Generated at 2022-06-14 02:04:23.706985
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class_def = "class A(metaclass=B):\n    pass"
    expected = "from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(B))"
    assert MetaclassTransformer().visit(ast.parse(class_def)).body[1].body[0] == ast.parse(expected).body[0].body[0]



# Generated at 2022-06-14 02:04:32.423848
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast_transformer

    # Simple test

    class TestTransformer(ast_transformer.BaseNodeTransformer):
        def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
            self.generic_visit(node)
            return node

    code = "class A(B, metaclass=C):\n    pass"
    tree = ast.parse(code)
    transformer = TestTransformer()
    transformer.visit(tree)
    result = ast.dump(tree)

# Generated at 2022-06-14 02:04:33.804295
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test the visit_ClassDef method of MetaclassTransformer class."""
    pass


# Generated at 2022-06-14 02:04:42.363598
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    import sys
    from typed_ast import ast3 as ast

    from ..utils.ast_importer import AstImporter

    class TestMetaclassTransformer_visit_ClassDef(unittest.TestCase):
        def setUp(self):
            self.ast_importer = AstImporter(sys.version_info)

        def test_should_insert_import_statement_if_missing(self):
            obj = MetaclassTransformer(sys.version_info)
            script = ("class A(): pass\n"
                      "if __name__ == '__main__': A()\n")
            module = self.ast_importer.import_(script)

            obj.visit(module)


# Generated at 2022-06-14 02:04:47.256513
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(metaclass=type):
        pass

    mt = MetaclassTransformer()
    tree = mt.run(ast.parse(inspect.getsource(A)))
    # TODO: Assert about the imports

# Generated at 2022-06-14 02:05:01.879619
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.testing import assert_trees_equal
    from typed_ast import ast3 as ast

    transformer = MetaclassTransformer()

    node = ast.ClassDef(
        name="A",
        bases=[],
        keywords=[ast.keyword(arg="metaclass", value=ast.Name(id="B", ctx=ast.Load()))],
        body=[],
        decorator_list=[])
    node = transformer.visit(node)

    expected = ast.ClassDef(
        name="A",
        bases=[class_bases(metaclass=ast.Name(id="B", ctx=ast.Load()),
                           bases=ast.List(elts=[]))],
        keywords=[],
        body=[],
        decorator_list=[])