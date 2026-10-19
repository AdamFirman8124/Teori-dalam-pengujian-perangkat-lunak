

# Generated at 2022-06-14 01:55:10.110399
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    
    class_snippet = snippet('''
                class A(metaclass=B):
                    pass
                ''')
    class_node = class_snippet.get_ast()
    
    import_snippet = snippet('''
                from six import with_metaclass as _py_backwards_six_withmetaclass
                ''')
    
    classmet_snippet = snippet('''
                _py_backwards_six_withmetaclass(metaclass=metaclass, *bases)
                ''')

    mct = MetaclassTransformer(__name__)

    mct.visit(class_node)
    
    assert mct._tree_changed

    assert import_snippet.get_ast()

# Generated at 2022-06-14 01:55:23.419375
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import IO
    from ..utils import compile_source
    from .six import SixModuleTransformer


# Generated at 2022-06-14 01:55:31.413931
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    six_import_stmts = six_import.get_ast().body
    class_bases_expr = class_bases.get_ast()

    # When
    module = ast.parse("class A(metaclass=B):\n    pass")
    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer.visit(module)
    module_body = module.body

    # Then
    assert len(module_body) == 3
    assert [isinstance(stmt, ast.Expr) for stmt in module_body[:2]]
    assert module_body[0].value.args == class_bases_expr.args
    assert module_body[0].value.keywords[0].arg == 'metaclass'
    assert module_body[0].value

# Generated at 2022-06-14 01:55:38.143692
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import sys
    module = ast.Module([
        ast.ClassDef(
            name='MyClass',
            bases=[ast.Name(id='object', ctx=ast.Load())],
            keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='ABC', ctx=ast.Load()))],
            body=[],
            decorator_list=[]
        )
    ])
    print(ast.dump(module), file=sys.stderr)
    MetaclassTransformer().visit(module)
    print(ast.dump(module), file=sys.stderr)

# Generated at 2022-06-14 01:55:48.553777
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    import six
    from textwrap import dedent
    from typed_ast import ast3

    from typed_astunparse import unparse
    
    from .testutil import canonicalize_source

    class TestCase(unittest.TestCase):
        def test_basic(self):
            source = dedent("""
            class A(metaclass=B):
                pass
            """)
            module = ast3.parse(source)
            MetaclassTransformer().visit(module)
            self.assertEqual(canonicalize_source(source, True),
                             canonicalize_source(unparse(module), True))

    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestCase))
    unittest.Text

# Generated at 2022-06-14 01:55:56.819017
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    body = ast.parse("""class A(metaclass=B):\n    pass""").body
    transformer = MetaclassTransformer([])
    transformer.visit(body[0])
    assert transformer._tree_changed is True
    assert ast.dump(body[0]) == "ClassDef(name='A', bases=[Call(func=Attribute(value=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), attr='withmetaclass', ctx=Load()), args=[Name(id='B', ctx=Load())], keywords=[])], body=[], decorator_list=[])"

# Generated at 2022-06-14 01:56:08.073860
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..snippets import as_str
    from ..utils import parse
    from .six import SixTransformer, six_import_str
    from .unittest_transformer import UnitTestTransformer
    from .unpacking_transformer import UnpackingTransformer
    
    result = parse(as_str(test_MetaclassTransformer_visit_Module))
    result = MetaclassTransformer(UnitTestTransformer()).visit(result)
    result = SixTransformer(UnpackingTransformer()).visit(result)
    result = parse(as_str(result))
    expected = six_import_str + as_str(test_MetaclassTransformer_visit_Module)
    expected = parse(expected)
    
    assert result == expected
#
# Code snippet to test MetaclassTransformer.visit_Module

# Generated at 2022-06-14 01:56:14.241577
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import cst
    class_def = cst.parse_statement("class A(metaclass=B): pass")
    transformer = MetaclassTransformer()
    new_class_def = transformer.visit(class_def)
    assert cst.unparse_code(new_class_def) == "class A(six.with_metaclass(B, object)): pass"



# Generated at 2022-06-14 01:56:16.286841
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    mt = MetaclassTransformer()


# Generated at 2022-06-14 01:56:24.985113
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    transformer = MetaclassTransformer()
    mod = ast.parse("class A(metaclass=type): pass")
    # Successfully imported six
    assert transformer.dependencies_loaded
    transformer.visit(mod)
    assert transformer.dependencies_loaded
    assert transformer.dependencies['six']
    # Transformer has changed the module
    assert transformer._tree_changed
    # Metaclass import has been inserted
    assert len(mod.body) == 2
    assert isinstance(mod.body[0], ast.ImportFrom)
    assert mod.body[0].module == 'six'
    assert mod.body[0].names[0].name == 'with_metaclass'
    assert mod.body[0].names[0].asname == '_py_backwards_six_withmetaclass'
    # Class has been

# Generated at 2022-06-14 01:56:38.691680
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import ClassDef, arguments

    class A(metaclass=type):
        pass

    node = ast.parse(A.__qualname__ + ': pass')
    node.body[0] = MetaclassTransformer().visit(node.body[0])  # type: ignore


# Generated at 2022-06-14 01:56:48.289852
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    code = 'class A(metaclass=B):\n    pass'
    expected = 'from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B))'
    node = ast.parse(code, "example.py")
    transformer = MetaclassTransformer()
    result = transformer.visit(node)
    result_code = compile(result, "example.py", "exec")
    exec(result_code)
    assert transformer._tree_changed is True
    assert expected == result_code.co_consts[2].expandtabs()

# Generated at 2022-06-14 01:57:01.181978
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast


    class FakeSix():
        with_metaclass = "with_metaclass"


    # import six
    # class F(six.with_metaclass(metaclass=object, *bases):
    #     pass

# Generated at 2022-06-14 01:57:10.206217
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # class A: ...
    #
    # should not be changed
    assert MetaclassTransformer().visit(
        ast.parse("""
        class A:
            pass
        """)).dump() == "Module(body=[ClassDef(name='A', bases=[], keywords=[], body=[Pass()], decorator_list=[])])"
    
    # class A(metaclass=B): ...
    #
    # should be changed to
    #
    # class A(_py_backwards_six_with_metaclass(B)): ...

# Generated at 2022-06-14 01:57:10.674531
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:57:11.810229
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:57:19.086722
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    meta_transformer = MetaclassTransformer(2, 7)
    class_ast = ast.parse("class A(object, metaclass=B, kw=value): pass")
    class_module = ast.Module(body=[class_ast])
    new_module = meta_transformer.visit(class_module)
    print(ast.dump(new_module))
    assert ast.dump(new_module) == snippet.dump(six_import) + snippet.dump(class_ast)


# Generated at 2022-06-14 01:57:25.632126
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.source import source_to_code as stc

    snippet = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
    
        import numpy as np
        class A(metaclass=np.object):
            pass
    """
    expected = """
        import numpy as np
        class A(_py_backwards_six_withmetaclass(np.object))
    """
    code = stc(snippet)
    MetaclassTransformer().visit(code)

    assert expected == code_to_source(code)

# Generated at 2022-06-14 01:57:35.406822
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    ast_tree = ast.parse("""
    class A(metaclass=B):
        pass

    class A(metaclass=B, **kwargs):
        pass

    class A(B, metaclass=C):
        pass

    class A(B, C, metaclass=D):
        pass

    class A(B, C, D, metaclass=E):
        pass
    """)
    MetaclassTransformer().visit(ast_tree)


# Generated at 2022-06-14 01:57:38.225049
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor

# Generated at 2022-06-14 01:57:44.934860
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """Test that constructor sets all attributes correctly."""
    t = MetaclassTransformer(None)
    assert t.dependencies == ["six"]
    assert t.target == (2, 7)

# Generated at 2022-06-14 01:57:46.915099
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from ..utils.tree import ast_from_string

# Generated at 2022-06-14 01:57:52.008990
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast

    class_def = ast.ClassDef(name="A",
                             bases=[],
                             keywords=[],
                             body=[],
                             decorator_list=[],
                             lineno=0,
                             col_offset=0)

    node = ast.Module(body=[class_def])
    node = MetaclassTransformer().visit(node)

    assert len(node.body) == 2

# Generated at 2022-06-14 01:57:57.828040
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse("""
    class X(y):
        pass
    """)
    expected_module = ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class X(_py_backwards_six_withmetaclass(y)):
        pass 
    """)
    assert MetaclassTransformer.apply_to(module) == expected_module


# Generated at 2022-06-14 01:58:07.769390
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.fake import FakeFile
    import sys
    import six

    if six.PY2:
        if sys.version_info[1] == 7:
            sys.argv = ['py_backwards', '--target', '2.7', '--from', '3.0']

    # set up fake files
    fake_files = {}
    fake_files['/fake_file.py'] = FakeFile(
        content='from six import with_metaclass as _py_backwards_six_withmetaclass\n'
                'class A:\n'
                '    class B(metaclass=MyMeta):\n'
                '        pass\n')

    from py_backwards.transformers.base import TransformerProvider
    from py_backwards.utils.files import SourceFileLoader

    sys.modules

# Generated at 2022-06-14 01:58:10.559827
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    input = "class A()"
    expected_output = "class A()"
    node = ast.parse(input)
    transformer = MetaclassTransformer(target=(2, 7))
    transformed_node = transformer.visit(node)
    output = ast.dump(transformed_node)
    print('in :', input)
    print('out:', output)
    assert output == expected_output


# Generated at 2022-06-14 01:58:12.233271
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .base import BaseNodeTransformerTest
    BaseNodeTransformerTest(MetaclassTransformer)

# Generated at 2022-06-14 01:58:15.071839
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .utils import assert_ast_tree

# Generated at 2022-06-14 01:58:22.479553
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    import unittest
    
    class TestMetaclassTransformerVisitClassDef(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None

        def test_basic(self):
            actual = MetaclassTransformer.run_yapf(dedent(r'''class A(metaclass=B,):
                pass'''))

# Generated at 2022-06-14 01:58:26.362912
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('class A(metaclass=B): pass')
    visitor = MetaclassTransformer()
    result = visitor.visit(module)
    assert 'from six import with_metaclass' in ast.dump(result)

# Generated at 2022-06-14 01:58:40.774764
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..parser import Parser
    from ..compiler import compile_source

    tree = Parser().parse('''
    class A(metaclass=B):
        pass
    ''')

    assert compile_source(tree, compiler=MetaclassTransformer) == '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(
        _py_backwards_six_withmetaclass(B)
    ):
        pass
    '''

    tree = Parser().parse('''
    class A(B):
        pass
    ''')

    assert compile_source(tree, compiler=MetaclassTransformer) == '''
    class A(
        B
    ):
        pass
    '''

# Generated at 2022-06-14 01:58:42.690720
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .. import compile
    from ..utils.test_utils import assert_code_equal

# Generated at 2022-06-14 01:58:48.437197
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    code = "class A(metaclass=B):\n    pass"
    expected = "from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)):\n    pass"
    node = ast.parse(code)
    MetaclassTransformer().visit(node)
    actual = astor.to_source(node).strip()
    assert actual == expected

# Generated at 2022-06-14 01:58:58.201373
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from . import TestTransformer
    from ..utils.tree import print_tree
    from ..utils.source import source
    from ..utils.visitor import traverse

    class_def = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[])
    class_def.keywords = [ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))]

    tree = TestTransformer(MetaclassTransformer, target=(2, 7), dependencies={'six'}).transform(class_def)
    print(print_tree(tree))

    # Output of this test should be:
    # ClassDef(
    #     name='A',
    #     bases=[
    #         Call(
    #             func=Name(
    #                 id

# Generated at 2022-06-14 01:59:09.975201
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.tree import assert_tree
    tree = ast.parse('class A(metaclass=B): pass')
    MetaclassTransformer.apply(tree)

# Generated at 2022-06-14 01:59:18.466389
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
    module = ast.parse(source)
    transformer = MetaclassTransformer()
    new_module = transformer.visit(module)
    assert ast.dump(new_module) == expected

# Generated at 2022-06-14 01:59:24.221459
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.Module(body=[])
    trans = MetaclassTransformer()
    trans.visit(node)
    assert len(node.body) == len(six_import.get_body())
    assert node.body == six_import.get_body()


# Generated at 2022-06-14 01:59:27.551702
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    tests = loader.loadTestsFromTestCase(TestMetaclassTransformerVisitModule)
    suite.addTests(tests)
    return suite


# Generated at 2022-06-14 01:59:32.115398
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = snippet.compile_ast('''
        class A(metaclass=B):
            pass
    ''')

    module = MetaclassTransformer().visit(module)
    assert module.body == six_import.get_body() + [module.body[0]]



# Generated at 2022-06-14 01:59:40.985250
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import make_mock_node
    from typed_ast import ast3 as ast
    from typing import List

    class MockClass(object):
        _fields = ('name', 'bases', 'keywords', 'body', 'decorator_list', 'starargs', 'kwargs')  # type: List[str]

    class MockKeyword(object):
        _fields = ('arg', 'value')  

    class MockString(object):
        _fields = ('s',)

    class MockName(object):
        _fields = ('id',)

    class MockAttribute(MockName):
        _fields = ('value', 'attr')

    # Case 1: Simple case

# Generated at 2022-06-14 02:00:04.765001
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = "class C(object, metaclass=A): pass"
    trans = MetaclassTransformer()
    node = ast.parse(source)
    trans.visit(node)
    result = ast.dump(node)
    expected = (
        "Module(body=[\n"
        "  ImportFrom(module='six', names=[alias(name='with_metaclass', "
        "asname='_py_backwards_six_withmetaclass')], level=0),\n"
        "  ClassDef(name='C', bases=[_py_backwards_six_withmetaclass(A)], "
        "keywords=[], body=[], decorator_list=[])\n"
        "])"
    )
    assert result == expected, f"\n{result}\n{expected}"



# Generated at 2022-06-14 02:00:16.106115
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    def check(src, expected):
        check_transformation(MetaclassTransformer, src, expected)
    check("""
        class A:
            pass
    """, """
        class A:
            pass
    """)
    check("""
        class A(metaclass=B):
                pass
    """, """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
                pass
    """)

# Generated at 2022-06-14 02:00:24.240080
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """ asdd"""
    source = 'class A(B, C, metaclass=D):\n    pass'
    expected = 'from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(D, B, C)):\n    pass'
    tree = ast.parse(source)
    MetaclassTransformer().visit(tree)
    assert ast.dump(tree) == expected



# Generated at 2022-06-14 02:00:35.012581
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast

    import sys
    import os
    import pathlib
    root = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
    sys.path.append('.')
    sys.path.append(str(root.parent.parent))

    from pybackwards.transformers import MetaclassTransformer

    mt = MetaclassTransformer()

    METACLASS = ast.Name(id='metaclass', ctx=ast.Load())
    MODULE = ast.Module(body=[
        ast.ClassDef(name='A',
                     keywords=[ast.keyword(arg='metaclass', value=METACLASS)],
                     body=[],
                     decorator_list=[])
    ])
    mt.visit(MODULE)

# Generated at 2022-06-14 02:00:36.823484
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer(target=(2, 7), dependencies=['six'])

# Generated at 2022-06-14 02:00:45.985077
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
  from .context import Context
  from ..utils.source import source
  from ..utils.compat import bytes_type

  class_def = "class A(metaclass=B):\n    pass"
  expected = "from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(_py_backwards_six_withmetaclass(B)):\n    pass"
  c = Context()

  # Ensure that the class is picklable, which is important for the script to work
  assert isinstance(bytes_type(pickle.dumps(MetaclassTransformer(c))), bytes_type)

  source = source(class_def)
  node = ast.parse(source)  # type: ignore
  node = MetaclassTransformer(c).visit(node)



# Generated at 2022-06-14 02:00:54.720823
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from astor.code_gen import to_source
    from ..utils import ast_from_source
    from ..utils.python_2_3 import parse_2_to_3

    source = 'class A(metaclass=B): pass'
    expected = 'from six import with_metaclass as _py_backwards_six_withmetaclass\n' \
               'class A(_py_backwards_six_withmetaclass(B)): pass'
    tree = parse_2_to_3(ast_from_source(source))
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    actual = to_source(transformer.visit(tree))
    assert expected == actual

# Generated at 2022-06-14 02:01:01.450670
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    code = 'class A(metaclass=B):\n pass  \n'
    tree = ast.parse(code)
    tree = MetaclassTransformer().visit(tree)
    assert astor.to_source(tree).strip() == 'from six import with_metaclass as _py_backwards_six_withmetaclass  \nclass A(_py_backwards_six_withmetaclass(B)):  \n    pass  '

# Generated at 2022-06-14 02:01:09.605143
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    module = ast.parse(
        """
        class A(metaclass=B):
            pass
        """
    )
    transformer = MetaclassTransformer()
    new_module = transformer.visit(module)

# Generated at 2022-06-14 02:01:17.385789
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.compiler import compile_snippet, tap, transform
    transformer = MetaclassTransformer()
    
    T = type

    assert compile_snippet('''
    class A(metaclass=type):
        pass
    ''') == transform(
        '''
        class A(metaclass=type):
            pass
        ''', transformer)
    assert compile_snippet('''
    class A(metaclass=type, name='1'):
        pass
    ''') == transform(
        '''
        class A(metaclass=type, name='1'):
            pass
        ''', transformer)


# Generated at 2022-06-14 02:01:49.091552
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    code = """
    class A(metaclass=B):
        pass
    """  # type: str
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass


    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """  # type: str
    source = ast.parse(code)
    assert MetaclassTransformer.run_visitor(source) == expected


# Generated at 2022-06-14 02:01:58.222340
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
        class A(metaclass=B):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B, )):
            pass
    """
    tree = ast.parse(code)
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:02:06.768293
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    input_source = """
        class A(metaclass=B):
            pass
    """
    actual_source = astor.to_source(MetaclassTransformer.run_pipeline(input_source))
    expected_source = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    _py_backwards_six_withmetaclass(B, *[])
    
    
    class A(_py_backwards_six_withmetaclass(B, *[])):
        pass
    """
    assert actual_source == expected_source



# Generated at 2022-06-14 02:02:15.770208
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse("class A(metaclass=B): pass"))
    # check the tree was modified
    assert mt._tree_changed

    class A:
        pass
    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse("class A(metaclass=B): pass"))
    # check the tree was modified
    assert mt._tree_changed

    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse("class A(B): pass"))
    # check the tree was not modified
    assert mt._tree_changed == False

# Generated at 2022-06-14 02:02:21.921776
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse('''
    class A(metaclass=B):
        pass
    ''')
    node = MetaclassTransformer().visit(node)
    assert ast.dump(node, annotate_fields=True) == \
        "Module(body=[ImportFrom(module='six', names=[alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0), ClassDef(name='A', bases=[Call(func=Attribute(value=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), attr='__call__', ctx=Load()), args=[Name(id='B', ctx=Load())], keywords=[])], body=[], decorator_list=[])])"

# Generated at 2022-06-14 02:02:28.018001
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    result_expected = ast.parse("""
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(Base):
        pass
    """
    )

    result = ast.parse("""
    class A(Base):
        pass
    """)
    tree = MetaclassTransformer().visit(result)
    assert ast.dump(tree) == ast.dump(result_expected)


# Generated at 2022-06-14 02:02:35.410804
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import DummyNode
    class Tree:
        def __init__(self):
            self.metaclass = DummyNode(6)
            self.keywords = [DummyNode(keyword=DummyNode(value=DummyNode(self.metaclass),
                                                         arg=DummyNode(8)))]
            self.bases = [DummyNode(12)]
        def __eq__(self, other):
            return self.bases == other.bases
            return self.keywords == other.keywords
    class Node:
        def __init__(self):
            self.body = [Tree()]
    class ClassDef:
        def __init__(self):
            self.bases = Tree().bases
            self.keywords = Tree().keywords

# Generated at 2022-06-14 02:02:42.170574
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from .common_tests import assert_equal_source

    # Given
    from ..utils import dump_ast
    from .common_tests import metaclass_example
    ast_tree = metaclass_example.get_ast()
    transformer = MetaclassTransformer()
    expected_tree = metaclass_example.get_metaclass_ast()

    # When
    ast_tree = transformer.visit(ast_tree)

    # Then
    assert_equal_source(astor.to_source(ast_tree), astor.to_source(expected_tree))

# Generated at 2022-06-14 02:02:51.762657
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer((2, 7), ["six"])

    res = transformer.visit(module)

    assert transformer.dependencies == ['six']
    assert transformer.target == (2, 7)
    assert isinstance(res, ast.Module)
    assert isinstance(res.body[0], ast.FunctionDef)
    assert res.body[0].name == '_py_backwards_six_with_metaclass'
    assert isinstance(res.body[1], ast.ClassDef)
    assert res.body[1].name == 'A'
    assert isinstance(res.body[1].bases[0], ast.Call)

# Generated at 2022-06-14 02:02:55.004322
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_transformed

    input = "class A(metaclass=B): pass"
    output = "from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)): pass"

    tr = MetaclassTransformer()
    assert_transformed(tr, input, output)


# Generated at 2022-06-14 02:04:03.593387
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class MetaclassTransformerTest(unittest.TestCase):
        def setUp(self):
            self._tree_changed = False
            self.transformer = MetaclassTransformer(self._tree_changed)

        def tearDown(self):
            pass

        def test_class_with_metaclass(self):
            code = dedent("""\
                class A(metaclass=B):
                    pass
            """)
            node = ast.parse(code)
            node = self.transformer.visit(node)
            expected_code = dedent("""\
                from six import with_metaclass as _py_backwards_six_withmetaclass
                class A(_py_backwards_six_withmetaclass(B)):
                    pass
            """)
            self.maxDiff = None


# Generated at 2022-06-14 02:04:05.430831
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import ast as _ast


# Generated at 2022-06-14 02:04:06.216165
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:04:07.903144
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import astor


# Generated at 2022-06-14 02:04:16.559420
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """\
        class A(metaclass=B, c=6):
            pass
        """

    node = ast.parse(dedent(code))
    MetaclassTransformer().visit(node)
    assert to_source(node) == dedent("""\
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwords_six_withmetaclass(B, *(c=6))):
            pass
        """)

# Generated at 2022-06-14 02:04:23.363287
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    # The expected output is a string. It is the transformed string of the input
    result = MetaclassTransformer().visit(r'''class A(metaclass=B): pass''')
    assert (result ==
            "from six import with_metaclass as _py_backwards_six_withmetaclass\n"
            "class A(_py_backwards_six_withmetaclass(B,*[])): pass")

# Generated at 2022-06-14 02:04:32.574383
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    n = ast.ClassDef(bases=[],
                     body=[],
                     decorator_list=[],
                     keywords=[ast.keyword(arg='metaclass',
                                           value=ast.Name(id='B', ctx=ast.Load()))],
                     name='A')

# Generated at 2022-06-14 02:04:34.075407
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    MetaclassTransformer.dependencies = []

# Generated at 2022-06-14 02:04:39.477216
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import six
    import ast

    tree = ast.parse('''class A(B):
    pass''')

    assert six not in tree.body[0].names

    m  = MetaclassTransformer()
    n = m.visit(tree)

    assert six in n.body[0].names


# Generated at 2022-06-14 02:04:40.102605
# Unit test for method visit_ClassDef of class MetaclassTransformer