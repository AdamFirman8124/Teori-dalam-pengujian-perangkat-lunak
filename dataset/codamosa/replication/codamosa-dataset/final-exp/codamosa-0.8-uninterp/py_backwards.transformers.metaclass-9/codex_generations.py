

# Generated at 2022-06-14 01:55:13.064951
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Declare an object of class MetaclassTransformer
    sut = MetaclassTransformer()
    # Create an AST with a class with a metaclass and a body of class and function definitions
    tree1 = ast.parse('''  
        class A(metaclass=type):
            def __init__(self):
                pass
            class B:
                pass
            def C():
                pass
    ''')
    # Create an AST with a class with a metaclass and a body of class and function definitions
    tree2 = ast.parse('''  
        class A(metaclass=type):
            class B:
                pass
            def __init__(self):
                pass
    ''')
    # Create an AST with a class with a metaclass and a body of class and function definitions

# Generated at 2022-06-14 01:55:21.620531
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    source = "class A(metaclass=B):\n  pass"
    expected = "class A(_py_backwards_six_withmetaclass(B))"
    tree = ast.parse(source)
    MetaclassTransformer._tree_changed = False
    MetaclassTransformer().visit(tree)
    assert MetaclassTransformer._tree_changed == True
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 01:55:27.380264
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():  # noqa
    class BaseTest:  # noqa
        pass

    class Test(BaseTest):
        pass

    class TestWithMeta(BaseTest, metaclass=type):
        pass

    transformer = MetaclassTransformer()

    # Nothing should happen, transformer should do nothing.
    @transformer.visit_ClassDef
    class TestNoMeta(BaseTest):
        pass

    assert TestNoMeta.__bases__ == (BaseTest,)

    # The transformer should add the six import at the top of the file.
    @transformer.visit_ClassDef
    class TestWithMeta(BaseTest):
        pass

    assert TestWithMeta.__bases__ == type, TestWithMeta.__bases__
    assert TestWithMeta.__bases__[0](BaseTest) is TestWithMeta



# Generated at 2022-06-14 01:55:34.191266
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import ClassDef
    from typed_ast.ast3 import Name
    from typed_ast.ast3 import Attribute
    

# Generated at 2022-06-14 01:55:36.394682
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    import typed_ast.ast3 as typedast


# Generated at 2022-06-14 01:55:38.286509
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import _transform
    import ast


# Generated at 2022-06-14 01:55:48.284555
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from six import with_metaclass as _py_backwards_six_with_metaclass
    snippet = """
    import jedi
    class A(metaclass=type):
        pass
    """
    node = ast.parse(snippet, 'snippet')
    # Fake import for Jedi
    node.body[0] = ast.Import(names=[ast.alias(name='jedi', asname=None)])
    exp = """
    import jedi
    class A(_py_backwards_six_with_metaclass(type))
        pass
    """
    node = MetaclassTransformer().visit(node)
    assert ast.dump(node, include_attributes=False) == exp

# Generated at 2022-06-14 01:55:50.662054
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import make_local_verifier
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:55:51.482930
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:59.681476
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class MetaclassTransformerSubclass(MetaclassTransformer):
        pass

    tree = ast.parse('class Foo(metaclass=type):\n    pass')

    cls = MetaclassTransformerSubclass()
    cls.visit(tree)
    assert cls._tree_changed == True
    assert tree.body[0].keywords == []
    assert type(tree.body[0].bases[0]) == ast.Call
    assert tree.body[0].bases[0].func.id == '_py_backwards_six_withmetaclass'

    tree = ast.parse('class Foo():\n    pass')

    cls = MetaclassTransformerSubclass()
    cls.visit(tree)
    assert cls._tree_changed == False

# Generated at 2022-06-14 01:56:04.418778
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List
    from .utils import round_trip
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:56:13.332551
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()

    classdef_without_metaclass = ast.ClassDef(name='A',
                                              bases=[],
                                              keywords=[],
                                              body=[],
                                              decorator_list=[])
    classdef_without_metaclass = mt.visit(classdef_without_metaclass)

    assert classdef_without_metaclass.keywords == []
    assert classdef_without_metaclass.bases == []


# Generated at 2022-06-14 01:56:23.132479
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    module = ast.Module(body=[ast.ClassDef(name='A',
                                           bases=[ast.Name(id='metaclass',
                                                           ctx=ast.Load())],
                                           keywords=[ast.keyword(arg='metaclass',
                                                                 value=ast.Name(id='B',
                                                                                ctx=ast.Load()))],
                                           body=[],
                                           decorator_list=[])])

    module.body[0].bases = class_bases.get_body(metaclass=metaclass,  # type: ignore
                                                bases=ast.List(elts=module.body[0].bases))
    module.body[0].keywords = []

    module = MetaclassTransformer

# Generated at 2022-06-14 01:56:26.711796
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Initialization
    source = ('\n'
           'class A(metaclass=B):\n'
           '    pass\n'
           '')
    expected = ('\n'
                'from six import with_metaclass as _py_backwards_six_withmetaclass\n'
                'class A(_py_backwards_six_withmetaclass(B)):\n'
                '    pass\n'
                '')

    # Run
    result = MetaclassTransformer().visit(ast.parse(source))
    result_string = ast.dump(result)

    # Verify
    assert result_string == expected




# Generated at 2022-06-14 01:56:30.431377
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    import ast as py_ast

    from ..translate import translate

    from .test_utils import assert_equal_source

    class C(type):
        pass


# Generated at 2022-06-14 01:56:40.296811
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    module = ast.parse("""
        class A(metaclass=B, baz=qux):
            pass

        class B(metaclass=C):
            pass
    """)
    transformer = MetaclassTransformer()
    result = transformer.visit(module)

    expected_result = ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, *[])):
        pass

    class B(_py_backwards_six_withmetaclass(C, *[])):
        pass
    """)

    assert astor.to_source(result) == astor.to_source(expected_result)

# Generated at 2022-06-14 01:56:52.491995
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer(2, 7)

    some_metaclass = ast.Name(id='SomeMetaclass')

    classdef_node = ast.ClassDef(name='A',
                                 bases=[],
                                 keywords=[ast.keyword(arg='metaclass',
                                                       value=some_metaclass)],
                                 body=[])

    classdef_node = t.visit(classdef_node)
    assert type(classdef_node.bases[0]) is ast.Call
    kwargs_dict = ast.Call(func=ast.Name(id='dict'),
                           args=[],
                           keywords=[ast.keyword(arg='metaclass',
                                                 value=some_metaclass)],
                           starargs=None,
                           kwargs=None)

# Generated at 2022-06-14 01:56:53.819900
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    

# Generated at 2022-06-14 01:57:05.725181
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import copy
    import sys
    import unittest
    from ..utils.ast_compare import assert_asts_equivalent
    from ..utils.test_transformer import SingleTestTransformerBase as TestTransformerBase

    name = 'test_MetaclassTransformer_visit_ClassDef'
    module_a = ast.parse(
        '''
        class A(B, metaclass=C):
            pass
        ''')

    module_b = ast.parse(
        '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(C, B)):
            pass
        ''')


# Generated at 2022-06-14 01:57:10.252819
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    from typing import List

    from py_backwards.transformers.metaclass import MetaclassTransformer

    test_tree = ast.parse('''
        from typing import Any, AnyStr, Union
        
        class A(metaclass=B):
            pass
    ''')
    expected_output = ast.parse('''
        from typing import Any, AnyStr, Union
        from six import with_metaclass as _py_backwards_six_withmetaclass
        
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    ''')

    transformer = MetaclassTransformer(target=(3, 0))
    dummy_list = transformer.visit(test_tree)
    assert isinstance(dummy_list, ast.Module)


# Generated at 2022-06-14 01:57:17.396477
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:57:22.792654
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import round_trip
    source = """
        class A(metaclass=B):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B, *[])):
            pass
    """
    round_trip(source, MetaclassTransformer, expected)


# Generated at 2022-06-14 01:57:24.900776
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:57:34.890879
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from .py2to3 import MetaclassTransformer
    from .six import SixTransformer
    from ..utils.snippet import snippet
    import typing
    import unittest

    class MockMetaclass(type):
        pass

    class OriginalClass(object):
        class Meta:
            pass

        class Attributes:
            pass

    class NewClass(object):
        class Meta(MockMetaclass):
            pass

        class Attributes:
            pass

    code1 = """
    class A(object):
        pass
    """
    code2 = """
    class A(_py_backwards_six_with_metaclass(Metaclass)):
        pass
    """

# Generated at 2022-06-14 01:57:49.471412
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    transformer.target = (2, 7)
    transformer.dependencies = ['six']

    # Given
    class A(metaclass=B):
        def test(self):
            pass
    node = ast.parse(inspect.getsource(A))
    transformer.visit(node)

    # When
    source = inspect.getsource(node)

    # Then
    assert source == "from six import with_metaclass as _py_backwards_six_withmetaclass\n"\
                     "class A(_py_backwards_six_withmetaclass(B)):\n"\
                     "    def test(self):\n"\
                     "        pass\n"

# Generated at 2022-06-14 01:57:59.555278
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import maketest
    from ..six import six_import

    test = maketest(MetaclassTransformer)
    test('''class A(object): pass''', '''class A(_py_backwards_six_with_metaclass(object)): pass''',
         imports=six_import)
    test('''class A(int): pass''', '''class A(_py_backwards_six_with_metaclass(int)): pass''',
         imports=six_import)
    test('''class A(object, int): pass''', '''class A(_py_backwards_six_with_metaclass(int, object)): pass''',
         imports=six_import)

# Generated at 2022-06-14 01:58:02.318529
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = '''class A(B): pass'''

# Generated at 2022-06-14 01:58:11.759773
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.snapshot import snapshot
    from ..utils.parse import parse_ast
    from ..utils.compatibility import unicode
    import astor
    insert_at.snapshot = snapshot("insert_at")
    six_import.snapshot = snapshot("six_import")
    class_bases.snapshot = snapshot("class_bases")

    class_def = parse_ast("""\
        class A(metaclass=B):
            pass
    """, mode="exec")
    symtable = {}
    transformer = MetaclassTransformer(symtable)
    transformer.visit(class_def)
    string = astor.to_source(class_def)
    assert unicode('class A(_py_backwards_six_withmetaclass(B))') in string

# Generated at 2022-06-14 01:58:19.603995
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from .jinja import get_template
    
    class_ = get_template("""
    class A(metaclass=B):
        pass
    """)
    class_ = class_()
    
    expected_output = get_template("""
    
    
    
    
    
    
    
    
    
    
    class A(_py_backwards_six_with_metaclass(B))
        pass
    
    
    
    
    
    
    """)
    expected_output = expected_output()
    expected_output = expected_output.strip()
    
    tree = ast.parse(class_)
    tree = MetaclassTransformer().visit(tree)
    output = astor.to_source(tree)
    output = output.strip()
    assert output

# Generated at 2022-06-14 01:58:21.486475
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:58:37.559563
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import check_visitor
    from ..utils.tree import dump
    from ..utils.codegen import module_to_str
    from ..utils.ast import build_ast

    class DummyMeta(object):
        pass

    class A(metaclass=DummyMeta):
        pass

    visitor = MetaclassTransformer()
    tree = build_ast(locals())
    node = visitor.visit(tree)
    # Check that the tree was modified properly
    eval(module_to_str(node))  # type: ignore
    # Check whether the visitor returns nodes in the correct order
    assert check_visitor(visitor, tree, module_to_str(node))

# Generated at 2022-06-14 01:58:40.410659
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 01:58:46.106934
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import TransformTestCase as T
    import logging
    import sys
    
    class A(T):
        transformer = MetaclassTransformer
        target = sys.version_info[:2]
        module = None
        dependencies = ['six']
        logging_level = logging.DEBUG
        method = 'visit_ClassDef'
    
    A.run_tests()

# Generated at 2022-06-14 01:58:56.548778
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import parse
    from ..utils.symbols import SymbolTableVisitor

    symbol_table_visitor = SymbolTableVisitor()

    class_def = parse("""
        class Meta:
            pass

        class A(metaclass=Meta):
            pass
    """).body[1]

    assert class_def.keywords
    assert str(class_def.keywords[0].value) == 'Meta'

    expected_keywords = []

# Generated at 2022-06-14 01:59:05.136644
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import astunparse

    class_node = ast.parse(
        """
        class A(metaclass=B):
            pass
        """
    )
    class_node_mod = MetaclassTransformer().visit(class_node)
    assert astunparse.unparse(class_node_mod) == """
    import six as _py_backwards_six
    class A(_py_backwards_six.with_metaclass(B)):
        pass
    """

# Generated at 2022-06-14 01:59:12.644522
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    from ..utils.snippet import snippet
    from ..utils.code_gen import to_source
    from ..utils.tree import parse_module
    from ..utils.compat import StringIO
    from ..utils.compat import is_python2, is_python3_4
    from ..utils.compat import is_python3_5, is_python3_6
    from ..utils.compat import is_python3_7
    from ..utils.compat import is_python3_8, is_python3_9

    source = textwrap.dedent("""\
    class A(metaclass=B):
        pass
    """)

# Generated at 2022-06-14 01:59:24.773753
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestClass(unittest.TestCase):
        def test_transformation_no_keywords(self):
            input_source = "class A(object): pass"
            expected_output_source = "class A(object): pass"
            input_ast = ast.parse(input_source)
            expected_output_ast = ast.parse(expected_output_source)
            instance = MetaclassTransformer()
            result = instance.visit(input_ast)
            self.assertEqual(result, expected_output_ast)

        def test_transformation(self):
            input_source = "class A(object, metaclass=B): pass"

# Generated at 2022-06-14 01:59:25.832442
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:59:36.175962
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from typed_ast import parse
    from ..utils.ast_factory import ast_factory
    from ..utils.run_transformer import run_transformer

    s = 'class A(metaclass=B): pass'
    _ast = ast_factory(s)
    assert isinstance(_ast, ast3.ClassDef)
    assert _ast.keywords[0].arg == 'metaclass'
    assert len(_ast.bases) == 0
    _ast = run_transformer(MetaclassTransformer, *_ast)
    assert isinstance(_ast, ast3.ClassDef)
    assert len(_ast.bases) == 1
    assert _ast.bases[0].func.id == '_py_backwards_six_withmetaclass'

# Generated at 2022-06-14 01:59:37.029789
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:01.597736
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    input = '''
    class A(metaclass=B):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(metaclass=B)):
        pass
    '''
    node = ast.parse(input)
    # When
    MetaclassTransformer().visit(node)
    # Then
    actual = ast.dump(node, annotate_fields=False, include_attributes=False)
    assert actual == expected

# Generated at 2022-06-14 02:00:05.691807
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    # derived from https://github.com/python/cpython/blob/2.7/Lib/test/test_metaclass.py#L58

# Generated at 2022-06-14 02:00:16.829544
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    node = ast.ClassDef(
        name="Foo",
        bases=[ast.Name(id="Bar")],
        keywords=[ast.keyword(arg="metaclass", value=ast.Name(id="Baz"))],
        body=[],
        decorator_list=[],
        lineno=0,
        col_offset=0
    )
    node = MetaclassTransformer().visit(node)

# Generated at 2022-06-14 02:00:29.584931
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    from unittest import TestCase
    from inspect import cleandoc
    import pytest
    from ..utils.ast import dump
    from ..utils.codewave import CodeWave
    from ..transformers.metaclass import MetaclassTransformer

    class TestMetaclassTransformer_visit_ClassDef(TestCase):
        def test_should_transform_class_definition_with_metaclass_keyword(self):
            code = cleandoc('''
                class Foo(metaclass=Bar):
                    pass
            ''')

            tree = ast.parse(code)
            wave = CodeWave(tree)
            transformer = MetaclassTransformer(wave)
            tree = wave.apply()


# Generated at 2022-06-14 02:00:40.565537
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List
    from ..utils.source import source
    with source(six_import) as (lines, filename):
        lines = '\n'.join(lines)

    class_def = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    node = class_def.body[0]
    metaclass = node.keywords[0].value

    assert node.keywords
    assert node.keywords[0].arg == 'metaclass'

    trans = MetaclassTransformer()
    result = trans.visit_ClassDef(node)  # type: ignore

    assert isinstance(result, ast.ClassDef)
    assert not result.keywords
    assert isinstance(result.bases[0], ast.Call)

# Generated at 2022-06-14 02:00:41.783160
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from six import with_metaclass as _py_backwards_six_withmetaclass

# Generated at 2022-06-14 02:00:48.001704
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List
    node: ast.ClassDef = ast.parse("""
        class A(metaclass=B):
            pass
        """).body[0]  # type: List[ast.ClassDef]
    expected_node = ast.parse("""
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """).body[0]
    MetaclassTransformer().visit(node)
    assert ast.dump(node) == ast.dump(expected_node)

# Generated at 2022-06-14 02:00:53.034766
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .six_transpile import SixTranspile
    from .six_transpile import TreeCopyVisitor
    import textwrap
    source = textwrap.dedent('''
    ''')
    tree = ast.parse(source)
    MetaclassTransformer(tree).transpile()
    print(SixTranspile().transpile(tree))

# Generated at 2022-06-14 02:01:03.691991
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # a class with a metaclass
    source = """
    class A(object, metaclass=B):
        pass
    """
    target = """
    class A(_py_backwards_six_withmetaclass(B, object)):
        pass
    """
    node = ast.parse(source)
    transformer = MetaclassTransformer()
    updated_node = transformer.visit(node)
    updated_source = astunparse.unparse(updated_node)
    assert target == updated_source

    # a class with a metaclass and a base class
    source = """
    class A(B, metaclass=C):
        pass
    """
    target = """
    class A(_py_backwards_six_withmetaclass(C, B)):
        pass
    """

# Generated at 2022-06-14 02:01:14.009724
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...utils.test_utils import transform, is_code_equivalent
    snippet_code = '''
        class A(metaclass=B):
            pass
        '''
    target_code = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        '''
    transform(MetaclassTransformer, snippet_code, target_code)

# Generated at 2022-06-14 02:01:52.127979
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(metaclass=B): pass', mode='exec')
    node = MetaclassTransformer().visit(node)


# Generated at 2022-06-14 02:01:54.564887
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .util import source_to_ast, source_to_target_ast


# Generated at 2022-06-14 02:01:55.873930
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 02:02:02.158956
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse('''
        class Foo(metaclass=Bar, object):
            pass
        class Foo2:
            pass
    ''')
    MetaclassTransformer().visit(tree)

    expected = ast.parse('''
        class Foo(_py_backwards_six_withmetaclass(Bar, object)):
            pass
        class Foo2:
            pass
    ''')
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:02:15.073660
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test for method visit_ClassDef of class MetaclassTransformer"""
    from typed_ast import ast3 as ast

    class A(ast.NodeTransformer):
        def __init__(self, tree=None):
            self.tree = tree

        def generic_visit(self, node):
            return node

    src = """
        class Foo(metaclass=int):
            pass
    """

    exp = """
    class Foo(_py_backwards_six_withmetaclass(int, *[])):
        pass
    """
    tree = ast.parse(src)
    res = A(tree).visit(tree)

    assert ast_to_str(res, imports=(six_import,)) == exp

# Generated at 2022-06-14 02:02:22.587894
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # MetaclassTransformer.visit_ClassDef(node: ast.ClassDef) -> ast.ClassDef
    from six import with_metaclass as _py_backwards_six_withmetaclass
    from typed_ast import ast3 as ast

    node = ast.ClassDef(
        name='A',
        bases=[],
        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))],
        body=[],
        decorator_list=[]
    )

    result = MetaclassTransformer().visit(node)

    assert result == _py_backwards_six_withmetaclass(B, )

# Generated at 2022-06-14 02:02:24.088279
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Checks if visit_ClassDef correctly transforms python3 code to python2 compatible code"""


# Generated at 2022-06-14 02:02:28.800382
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse(
        """
        from six import with_metaclass
        class A(metaclass=int): pass
        """
    )
    t = MetaclassTransformer()
    assert t.run(node)

    assert isinstance(node.body[1].bases[0], ast.Call)


# Generated at 2022-06-14 02:02:33.102984
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import assert_transforms, assert_source

    assert_transforms(MetaclassTransformer, """
    class A(metaclass=B):
        pass
    """, """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)

# Generated at 2022-06-14 02:02:37.470817
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    x = """
    class foo(metaclass=bar):
        pass
    """
    node = ast.parse(x)
    MetaclassTransformer().visit(node)
    code = compile(node, "<test>", "exec")
    exec(code)

# Generated at 2022-06-14 02:04:04.698069
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..builder import build
    my_code = '''
    from six import with_metaclass as _py_backwards_six_with_metaclass

    class MyClass(metaclass=MyMetaclass):
        pass
    '''
    my_expected = '''
    from six import with_metaclass as _py_backwards_six_with_metaclass

    class MyClass(_py_backwards_six_with_metaclass(MyMetaclass)):
        pass
    '''
    my_tree = build(my_code, 2, 7)
    my_transformer = MetaclassTransformer()
    my_transformer.walk(my_tree)
    assert my_expected == my_transformer.compile()



# Generated at 2022-06-14 02:04:12.241304
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source_to_code
    from .utils import assert_transform

    source = """
    class Foo(metaclass=type):
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class Foo(_py_backwards_six_withmetaclass(type, object)):
        pass
    """
    assert_transform(MetaclassTransformer, source, expected)

# Generated at 2022-06-14 02:04:22.714548
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3
    from ...utils.testing import assert_code_equal

    code_in = '''
        class A(metaclass=B):
            pass
    '''

    meta_code_out = '''
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    '''

    meta_ast_in = ast3.parse(code_in)
    transformer = MetaclassTransformer()
    meta_ast_out = transformer.visit(meta_ast_in)
    meta_code_out = ast3.unparse(meta_ast_out)

    ast_meta_out = ast3.parse(meta_code_out)
    meta_ast_out = transformer.visit(ast_meta_out)

# Generated at 2022-06-14 02:04:29.516020
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .six import six_import, class_bases
    import ast
    import sys

    main_module = ast.parse('''class A(metaclass=str):
    def __init__(self, *args):
        self.value = args
''')

    target = MetaclassTransformer(main_module, sys.modules[__name__])
    target.visit(main_module)

    assert six_import in main_module.body
    assert class_bases in main_module.body[1].bases[0].elts

# Generated at 2022-06-14 02:04:33.515044
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..transformer_utils import transform
    
    from typed_ast import ast3
    
    six_import = """
from six import with_metaclass as _py_backwards_six_withmetaclass
"""
    class_bases = """
_py_backwards_six_withmetaclass(metaclass, *bases)
"""


# Generated at 2022-06-14 02:04:40.795207
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ...test_utils import make_test_case
    from .example_visitor import ExampleVisitor
    from .example_transformer import ExampleTransformer

    test_cases = []
    for (expected, input) in [
        (six_import.get_ast() + class_bases.get_ast(),
         class_bases.get_ast()),
    ]:
        test_cases.append(make_test_case(
            input=input,
            expected=expected,
            transform=ExampleTransformer([
                MetaclassTransformer,
            ], ExampleVisitor),
            testid='{}-{}'.format(expected, input),
        ))

    return test_cases

# Generated at 2022-06-14 02:04:43.188890
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    from py_backwards.transformers.six import MetaclassTransformer


# Generated at 2022-06-14 02:04:51.734823
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_python import ast3 as ast
    from typed_ast import ast3 as typed_ast
    from typed_ast import convert
    import sys

    global_namespace = {'__name__': '__main__', '__file__': 'test.py'}

    class_def = ast.parse("""class A(metaclass=int):
        pass""").body[0]
    class_def: ast.ClassDef

    visitor = MetaclassTransformer(sys.version_info, global_namespace)
    visitor.visit(class_def)
    assert visitor._tree_changed

    typed_ast_node = convert(class_def)
    typed_ast_node: typed_ast.ClassDef

    assert type(typed_ast_node.keywords) == list
    assert not typed_ast_node.key

# Generated at 2022-06-14 02:04:57.287034
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import six

    with patch('six.with_metaclass') as w:
        w.return_value = 'return succesful'
        with patch('astunparse.unparse') as u:
            u.return_value = 'new class'
            six.assertRaises = lambda e, v, t=Exception: e(v)
            code = MetaclassTransformer().visit_ClassDef(ast.ClassDef(name='A',
                                                                      args=ast.arguments(),
                                                                      keywords=[ast.keyword(arg='metaclass',
                                                                                            value=ast.Num(n=5))],
                                                                      bases=[]))

# Generated at 2022-06-14 02:05:02.617697
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class ClassDef():
        def __init__(self) -> None:
            self.bases = []
            self.keywords = []

    test_cases = {
        ClassDef.__init__: False,
        ClassDef: True
    }  # type: Dict[ast.AST, bool]

    transformer = MetaclassTransformer()

    for test_case, expected in test_cases.items():
        assert MetaclassTransformer.visit_ClassDef(transformer,
                                                   test_case) == expected