

# Generated at 2022-06-14 01:55:08.960132
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # The following correct Python code:
    # 
    #     class A(metaclass=B):
    #         pass
    # 
    # Should be compiled to:
    # 
    #     class A(_py_backwards_six_withmetaclass(B)):
    #         pass
    # 
    # When the method ``visit_ClassDef`` of class ``MetaclassTransformer``
    # is called.
    from .test_env import test_env

    code = """class A(metaclass=B):
    pass
    """

# Generated at 2022-06-14 01:55:21.846102
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_transformed_ast_is

    classdef_with_metaclass = ast.parse(
        '''
        class A(metaclass=B, x=3):
            pass
        '''
    ).body[0]

    classdef_without_metaclass = ast.parse(
        '''
        class A(x=3):
            pass
        '''
    ).body[0]
    
    classdef_without_args = ast.parse(
        '''
        class A():
            pass
        '''
    ).body[0]
    
    expected_classdef = ast.parse(
        '''
        class A(_py_backwards_six_with_metaclass(B)):
            pass
        '''
    ).body[0]

   

# Generated at 2022-06-14 01:55:30.958796
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from ..utils.tree import get_body
    from ..utils.source import generate_source

    node = ast.parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer()
    node = transformer.visit(node)
    print(generate_source(node))
    assert generate_source(get_body(node, 0)) == six_import.get_source()
    node = get_body(node, 1)
    assert node.bases == class_bases.get_body(metaclass=ast.Name('B'),
                                              bases=ast.List(elts=[]))
    assert node.keywords == []



# Generated at 2022-06-14 01:55:39.571736
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse
    from .base import BaseTest
    from .six import six_import_all_test, six_import_all

    source = '''
    class A(B):
        pass
    class C(D, E):
        pass
    class F(G, metaclass=H):
        pass
    class I(J, K, L, M, N):
        pass
    class O(metaclass=P):
        pass
    class Q(metaclass=R, S):
        pass
    class T(U, V, metaclass=W):
        pass
    class X(Y, metaclass=Z):
        pass
    class C(metaclass=D, E):
        pass
    '''


# Generated at 2022-06-14 01:55:47.972025
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    old_class = 'class A(metaclass=B):\n    pass'
    new_class = transformer.visit(ast.parse(old_class))
    assert transformer.was_changed()
    assert new_class.body[0].name == 'A'
    assert new_class.body[0].bases.elts[0].func.id == '_py_backwards_six_withmetaclass'
    assert new_class.body[0].bases.elts[0].args[0].id == 'B'
    assert new_class.body[0].keywords == []

# Generated at 2022-06-14 01:55:54.501795
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():

    # Given
    source = 'class A(B): pass'
    expected = 'from six import with_metaclass as _py_backwards_six_withmetaclass;class A(B): pass'

    # When
    result = compile(source, '', 'exec', ast.PyCF_ONLY_AST, True)
    transformed = MetaclassTransformer().visit(result)
    transformed = compile(transformed, '', 'exec', 0, True)

    # Then
    assert expected == transformed


# Generated at 2022-06-14 01:55:55.709772
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer()

# Generated at 2022-06-14 01:56:01.566188
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    prog = 'class A(metaclass=B):\n    pass'
    node = ast.parse(prog, mode='exec')
    trans = MetaclassTransformer(lambda x: x)
    ret = trans.visit(node)
    assert ret.body[0].bases[0].args[0].value.id == 'B'
    assert prog == trans.get_module().get_source()

# Generated at 2022-06-14 01:56:10.788757
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    # type: str -> ast.Module
    parse = ast.parse

    # type: ast.Module -> str
    unparse = astor.to_source

    code = textwrap.dedent("""
        class A(metaclass=B):
            pass
    """)

    res = textwrap.dedent("""
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class A(_py_backwards_six_with_metaclass(B)):
            pass
    """)

    module = parse(code)
    metaclass_transformer = MetaclassTransformer()
    metaclass_transformer.visit(module)
    assert unparse(module) == res

# Generated at 2022-06-14 01:56:12.826048
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from ast import parse

# Generated at 2022-06-14 01:56:23.898564
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ast_tools.transformers.compatibility.metaclass import MetaclassTransformer
    from utils.source import source as s
    result = MetaclassTransformer(input_string='''
    class A(object):
        pass
    class B(metaclass=C):
        pass
    class C(D):
        __metaclass__ = E
        def __metaclass__(self):
            pass
    class D(object, metaclass=F):
        pass
    class E(object):
        pass
    class F(object):
        pass
    class G(object, metaclass=F, metaclass=F):
        pass
    ''').visit(ast.parse('', mode='eval'))
    nodes = list(ce)
   

# Generated at 2022-06-14 01:56:33.365225
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Fake code
    code = """\
    class A(metaclass=D):
        pass
    class B(metaclass=C, E):
        pass
    """
    # Comparison code
    compare = """\
    class A:
        pass
    class B(E):
        pass
    """
    # Parse fake code
    tree = ast.parse(code)
    # Transform tree
    transformer = MetaclassTransformer()
    tree = transformer.visit(tree)
    # Parse comparison code
    compare_tree = ast.parse(compare)
    # Assert trees are equivalent
    assert ast.dump(tree) == ast.dump(compare_tree)



# Generated at 2022-06-14 01:56:36.142393
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import unittest
    import tempfile
    import sys
    import os
    import astor
    from ..utils.tests import TestTransformer
    

# Generated at 2022-06-14 01:56:40.372325
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = dedent('''\
    class A():
        pass
    ''')

    ret_code = dedent('''\
    class A(object):
        pass
    ''')

    return (MetaclassTransformer,
            code,
            ret_code)


# Generated at 2022-06-14 01:56:49.918860
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_parsed

    code = '''
        class A(metaclass=B):
            pass
    '''
    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
    '''
    expected = expected.strip()

    with_padding = MetaclassTransformer(code)
    actual = with_padding.get_new_code().strip()
    assert_parsed(expected, actual)

# Generated at 2022-06-14 01:57:01.735718
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    from .test_common import compile_from_text, generate_from_text
    from astroid import parse

    text = 'class A(metaclass=B):\n pass'
    expected = 'class A(_py_backwards_six_withmetaclass(B, object)):\n pass'
    node = parse(text)
    transformer = MetaclassTransformer()

    # When
    actual_code = transformer.visit(node)
    actual_node = parse(actual_code)
    actual = generate_from_text(compile_from_text(actual_node))

    # Then
    assert actual == expected, f'Expected:\n{expected}\nGot:\n{actual}'

# Generated at 2022-06-14 01:57:10.639988
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from dataclasses import dataclass
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import ClassDef, Name
    from .base import BaseNodeTransformerTester

    # 1. Test ClassDef of a class that inherits from a base class that
    # does not require a metaclass.
    input_source = """
        class Base:
            pass
        
        class A(Base, metaclass=B):
            pass
        """

# Generated at 2022-06-14 01:57:16.398442
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_source


    class C(metaclass=ABCMeta):
        pass

    node = ast.parse(C.__qualname__)
    module = MetaclassTransformer().visit(node)

    source = six_import + class_bases.snippet + C.__qualname__

    assert_source(module, source)

# Generated at 2022-06-14 01:57:22.784522
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.tree import print_tree, load_tree

    class A(metaclass=B):
        pass

    tree = ast.parse(A.__code__.co_consts[0])
    trans = MetaclassTransformer()
    tree = trans.visit(tree)
    assert trans._tree_changed

    assert print_tree(tree.body[0]) == """class A(B):
    pass"""

    class A(B):
        pass

    tree = ast.parse(A.__code__.co_consts[0])
    trans = MetaclassTransformer()
    tree = trans.visit(tree)
    assert trans._tree_changed


# Generated at 2022-06-14 01:57:33.549071
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
        class A:
            pass

        class B(metaclass=C):
            pass

        class D(A, B):
            pass

        class E(metaclass=F):
            pass

        class G(A, E):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(object):
            pass

        class B(_py_backwards_six_withmetaclass(C)):
            pass

        class D(A, B):
            pass

        class E(_py_backwards_six_withmetaclass(F)):
            pass

        class G(A, E):
            pass
    """
    mt = MetaclassTransformer()

# Generated at 2022-06-14 01:57:40.415184
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ...codetree import CodeTree
    from astor import dump
    from ast import parse


# Generated at 2022-06-14 01:57:46.847687
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .. import run_transformer
    module = run_transformer(MetaclassTransformer, 'class A(B, C, metaclass=D): pass')
    assert module.body[0].bases[0].value.func.id == '_py_backwards_six_withmetaclass'

# Generated at 2022-06-14 01:57:47.895377
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:57:52.239420
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # type: () -> None
    """
    Class test_MetaclassTransformer_visit_Module
    """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    from .base import BaseNodeTransformer

# Generated at 2022-06-14 01:58:01.643299
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """
    Check for compilation of class with metaclass to six.withmetaclass
    """
    from ..utils.symbols import SymbolTable
    from ..utils.tree import parse
    from .six import Six
    from .common import Common
    from .builtins import Builtins

    source = """
    class A(metaclass=B):
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """
    root = parse(source)
    symboltable = SymbolTable()

    six = Six()
    common = Common()
    builtins = Builtins()
    six.apply(root, symboltable)

# Generated at 2022-06-14 01:58:11.271988
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import sys
    import textwrap
    import unittest
    import typed_astunparse
    import astunparse

    code = textwrap.dedent('''
        class A(metaclass=B):
            pass
    ''')

    # Get a module's abstract syntax tree
    tree = ast.parse(code)

    # Compile source code and check for errors
    transformer = MetaclassTransformer(sys.version_info)
    transformer.visit(tree)
    assert transformer.changed
    assert 'six' in transformer.modules
    assert textwrap.dedent('''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
    ''') == typed_astunparse

# Generated at 2022-06-14 01:58:18.306944
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    """Tests code generation of the class MetaclassTransformer.
    """
    # Arrange
    import ast

    module_node = ast.parse('class A(metaclass=B): pass')
    # Act
    transformer = MetaclassTransformer()
    new_ast = transformer.visit(module_node)
    result = get_code(new_ast)
    expected = dedent('''
    from six import with_metaclass as _py_backwards_six_withmetaclass

    _py_backwards_six_withmetaclass(B, )
    class A(, ):
        pass
    ''').strip()
    # Assert
    assert result == expected

# Generated at 2022-06-14 01:58:28.388851
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import inspect

    import untrusted
    from untrusted.compat import ast as ast3

    source = '''
        class A(object):
            __slots__ = ()
            def f(self):
                pass
    '''

    tree = ast3.parse(source)
    transformer = MetaclassTransformer()
    r = transformer.visit(tree)
    code = compile(r, '<fragment>', 'exec')
    env = {}
    exec(code, env)
    code = inspect.getsource(env['A'])
    assert code == '\n' \
                    '    class A(_py_backwards_six_withmetaclass(object)):\n' \
                    '        __slots__ = ()\n' \
                    '        def f(self):\n' \
                   

# Generated at 2022-06-14 01:58:29.389270
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:58:29.968841
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 01:58:37.274043
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    from .common import clean_transformed_source


# Generated at 2022-06-14 01:58:44.297431
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.source import source
    from .. import run
    from .test_utils import assert_transformed

    # verify six_import
    assert_transformed(
        run(source(six_import)),
        source(six_import)
    )

    # verify class_bases
    assert_transformed(
        run(source(class_bases)),
        source(class_bases)
    )

    # verify MetaclassTransformer.visit_Module
    src = '''
        class A(object, metaclass=B):
            pass
    '''
    expected = '''
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class A(_py_backwards_six_with_metaclass(B)):
            pass
    '''
   

# Generated at 2022-06-14 01:58:52.909081
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.test_utils import assert_equal_code
    from typed_ast import ast3 as ast
    from .six_transformer import SixTransformer

    tree = ast.parse(six_import.get_original_code())
    transformer = SixTransformer()
    new_tree = transformer.visit(tree)
    assert (transformer.tree_changed
            == 'six' in [im.module for im in new_tree.body
                         if isinstance(im, ast.Import)])

    tree = ast.parse(class_bases.get_original_code())
    transformer = MetaclassTransformer()
    new_tree = transformer.visit(tree)

# Generated at 2022-06-14 01:59:05.010124
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_converter import py_ast_to_typed_ast_Module

    def compare_asts(a: ast.AST, b: ast.AST):
        assert ast.dump(a) == ast.dump(b)
    
    # Checking a module without classes
    module = py_ast_to_typed_ast_Module("")
    copied_module = copy.deepcopy(module)

    MetaclassTransformer().visit(module)
    compare_asts(copied_module, module)

    # Checking module with class without metaclass

# Generated at 2022-06-14 01:59:14.812035
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse("""
        class A(metaclass=B):
            pass
    """)

    module = MetaclassTransformer().visit(module)

    assert ast.dump(module) == \
"""
Module(body=[
    ImportFrom(module='six', names=[alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0), ClassDef(name='A', bases=[
        Call(func=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), args=[
            Name(id='B', ctx=Load())], keywords=[])], body=[], decorator_list=[])])
"""

# Generated at 2022-06-14 01:59:26.118400
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # These two test cases are not required by the current implementation
    # and just serve as documentation/examples
    assert MetaclassTransformer().visit(ast.parse('''
        class A:
            pass
    ''')) == ast.parse('''
        class A:
            pass
    ''')

    assert MetaclassTransformer().visit(ast.parse('''
        class A(metaclass=B):
            pass
    ''')) == ast.parse('''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    ''')

# Generated at 2022-06-14 01:59:31.179839
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast27
    from ..utils.testing import assert_same_ast
    from ..transformer import Context
    from .six import SixTransformer

    example = """class A(metaclass=B):
    pass"""

# Generated at 2022-06-14 01:59:39.478053
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    source = """class A(metaclass=B): pass"""
    expected_meta = """from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)): pass\n"""
    result = MetaclassTransformer().transform_source(source)
    assert result == expected_meta

# Generated at 2022-06-14 01:59:42.817034
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from . import test_Transformer_visit_Module
    test_Transformer_visit_Module(MetaclassTransformer)


# Generated at 2022-06-14 01:59:45.704786
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = """class A():pass"""

# Generated at 2022-06-14 02:00:04.336256
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('class A(metaclass=B):\n    pass')
    transformer = MetaclassTransformer()
    module = transformer.visit(module)
    expected = ast.parse('''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B))
            pass
    ''')
    assert ast.dump(module) == ast.dump(expected)



# Generated at 2022-06-14 02:00:15.836331
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    from .base import transform
    from ..utils.snippet import snippet
    from ..utils.dump import dump
    from ..utils.tree import copy_clean

    @snippet
    def code():
        class A(metaclass=B):
            pass

    # Show output of code snippet
    tree = ast.parse(code.get_source())
    print('Input:\n\n', code.get_source())
    print('\nDump:\n\n', dump(tree))

    # Show output of transformation
    tree2 = copy_clean(tree, None)
    transform(tree2, 2.7, MetaclassTransformer(language_level=2.7))
    print('\nTransformed:\n\n', astor.to_source(tree2))


test_MetaclassTransformer

# Generated at 2022-06-14 02:00:17.691908
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import assert_transform


# Generated at 2022-06-14 02:00:27.048846
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..parser import parse
    from .pep8 import PEP8Transformer
    from .whitespace import WhitespaceTransformer

    source = '''
    class A(metaclass=B):
        pass
    '''

    tree = parse(source)
    PEP8Transformer(tree).visit()
    MetaclassTransformer(tree).visit()
    WhitespaceTransformer(tree).visit()
    assert compile(tree, '<test>', 'exec')


# Generated at 2022-06-14 02:00:34.592895
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    m = ast.parse("""
        class A(metaclass=B):
            pass
    """)

    expected = ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass
    
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """)

    r = MetaclassTransformer().visit(m)
    assert ast.dump(r) == ast.dump(expected)

# Generated at 2022-06-14 02:00:49.113660
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import ast as pyast
    from .base import BaseNodeTransformerTest
    from .fixtures import comment_block, six_import_block, import_block


    source = '''
    class A(metaclass=B): pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)): pass
    '''
    tree = pyast.parse(source)
    tree = MetaclassTransformer().visit(tree)
    assert(BaseNodeTransformerTest.compare(tree, expected, {
        'comment_block': comment_block,
        'six_import_block': six_import_block,
        'import_block': import_block,
    }))

# Generated at 2022-06-14 02:00:52.113725
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse(
        'class A: pass')
    node = MetaclassTransformer().visit(node)
    assert str(node) == (six_import + '\nclass A: pass')



# Generated at 2022-06-14 02:00:52.703288
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:58.924889
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import compare_ast, parse
    from ..context import Context
    source = '''class Base(metaclass=abc.ABCMeta): pass'''
    ctx = Context()
    tree = parse(source, ctx)
    result = MetaclassTransformer(ctx).visit(tree)

# Generated at 2022-06-14 02:01:07.995970
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..transpiler import Transpiler
    from ..transpiler import Py2Transpiler
    from ..transpiler import Py3Transpiler
    from ..transpiler import Py33Transpiler
    from ..default_settings import settings
    from .base import BaseTranspilerTest

    class TestMetaclassTransformer(BaseTranspilerTest):
        settings = settings
        module = MetaclassTransformer

    class TestTranspiler(Transpiler):
        settings = settings
        module = MetaclassTransformer
        dependencies = []

    class TestPy2Transpiler(Py2Transpiler, TestTranspiler):
        pass

    class TestPy3Transpiler(Py3Transpiler, TestTranspiler):
        pass


# Generated at 2022-06-14 02:01:32.988703
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:01:33.496422
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    transformer = MetaclassTransformer()

# Generated at 2022-06-14 02:01:36.621422
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from py_backwards.transformers.visitors import fix_missing_locations
    from py_backwards.tests.visitors.test_helper import expect_same_code


# Generated at 2022-06-14 02:01:47.591674
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .base import BaseTestTransformer
    from ..utils.source import source

    class Test(BaseTestTransformer):
        transformer = MetaclassTransformer
        filename = __file__

        def test_metaclass_attribute(self):
            self.assertTransform(
                before="""
                class A(metaclass=some_metaclass):
                    pass
                """,
                after="""
                from six import with_metaclass as _py_backwards_six_withmetaclass
                
                class A(
                    _py_backwards_six_withmetaclass(some_metaclass),
                ):
                    pass
                """
            )


# Generated at 2022-06-14 02:01:54.611735
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    testcase = """class Foo(metaclass=FooMeta): pass"""
    expected = """class Foo(_py_backwards_six_withmetaclass(FooMeta)): pass"""
    res = MetaclassTransformer().visit(ast.parse(testcase))
    assert astor.to_source(res).strip() == expected
    r2 = get_ast(expected)
    assert res.body[0] == r2.body[0]



# Generated at 2022-06-14 02:02:00.586809
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent
    t = MetaclassTransformer()
    node = ast.parse(dedent('''
    class Foo(object, metaclass=abc.ABCMeta):
        pass
    '''))
    t.visit(node)
    assert t._tree_changed
    original_code = dedent('''
    class Foo(_py_backwards_six_withmetaclass(abc.ABCMeta), object):
        pass
    ''')
    assert astor.to_source(node) == original_code

# Generated at 2022-06-14 02:02:11.357800
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing.utils import assert_python_code_equals_ast
    from typed_ast import ast3 as ast
    from .six_import import SixImportTransformer

# Generated at 2022-06-14 02:02:12.378089
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:02:21.812600
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    # Given
    mt = MetaclassTransformer()

# Generated at 2022-06-14 02:02:28.620943
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    src = """
        class A(metaclass=a):
            pass
        """
    expected_result = """
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(a)):
            pass
        """
    node = ast.parse(src)
    mt = MetaclassTransformer()
    mt.visit(node)
    result = ast.dump(node)
    assert result == expected_result

# Generated at 2022-06-14 02:03:32.517274
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import sys
    from ..utils.source import source_to_ast

    import_level = 0 if sys.version_info < (3, ) else 1
    # This test fails from python 3.5 onwards due to the importlib.util
    # module
    if sys.version_info > (3, 4):
        import_level += 1

    node = source_to_ast("""
    class A(metaclass=B):
        pass
    """)
    transpiled_node = source_to_ast("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)

    assert MetaclassTransformer()(node) == transpiled_node.body[import_level:]

# Generated at 2022-06-14 02:03:36.915975
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(metaclass=type):\n pass')
    transform = MetaclassTransformer()
    transformed = transform.visit(node)
    assert transformed is not None
    assert str(transformed) == 'class A(_py_backwards_six_withmetaclass(type))'

# Generated at 2022-06-14 02:03:37.538160
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:43.973873
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse('''class A: pass'''))
    assert mt._tree_changed == False

    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse('''class A(B): pass'''))
    assert mt._tree_changed == False

    mt = MetaclassTransformer()
    mt.visit_Module(ast.parse('''class A(metaclass=B): pass'''))
    assert mt._tree_changed == True

# Generated at 2022-06-14 02:03:55.239883
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .._py_transformer import PyTransformer
    from .test_utils import source_to_code, parse
    from ..utils.tree import node_to_str

    source = '''
        class A(metaclass=B):
            pass
        class C:
            pass
    '''
    code = source_to_code(source)
    imports = {
        'six': six_import.get_body()
    }
    expected_code = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        class C:
            pass
    '''

# Generated at 2022-06-14 02:04:03.920479
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from . import get_node
    from . import run_visitor


# Generated at 2022-06-14 02:04:16.008462
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    source = '''
    class A(): pass
    '''
    tree = pyast.parse(source)
    assert tree == pyast.parse(source)
    tree = MetaclassTransformer().visit(tree)
    assert tree == pyast.parse(source)

    source = '''
    class A(metaclass=B): pass
    '''
    tree = pyast.parse(source)
    tree_expected = pyast.parse("""
    class A(_py_backwards_six_withmetaclass(B)): pass
    """)
    tree = MetaclassTransformer().visit(tree)
    assert tree == tree_expected

# Generated at 2022-06-14 02:04:26.790113
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import sys
    import textwrap
    import unittest
    from ..utils.six_util import six

    class MetaclassTransformer_test(unittest.TestCase):
        """MetaclassTransformer class unit test"""

        def test_py27(self):
            if six.PY2:
                source = """
                class Test(object):
                    def __init__(self):
                        super(Test, self).__init__()
                """
                expected = """
                from six import with_metaclass as _py_backwards_six_withmetaclass

                class Test(_py_backwards_six_withmetaclass(object, object)):
                    def __init__(self):
                        super(Test, self).__init__()
                """
                self._helper(source, expected)


# Generated at 2022-06-14 02:04:27.280783
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    pass

# Generated at 2022-06-14 02:04:30.482788
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    def check(s: str, s_expected: str):
        node = ast.parse(s)
        node = MetaclassTransformer().visit(node)
        assert astunparse.unparse(node) == s_expected
