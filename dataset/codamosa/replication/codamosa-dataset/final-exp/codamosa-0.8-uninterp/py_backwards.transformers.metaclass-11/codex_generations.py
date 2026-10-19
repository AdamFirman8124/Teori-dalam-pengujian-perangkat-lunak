

# Generated at 2022-06-14 01:55:08.585217
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import astor
    from .base import BaseNodeTransformerTest
    ast_ = MetaclassTransformer.visit_Module(
        ast.parse('''class A(): pass'''),
        BaseNodeTransformerTest()
    )
    out = astor.to_source(ast_)
    lines = [
        '_py_backwards_six_withmetaclass = with_metaclass',
        'class A():', '    pass'
    ]
    assert out == '\n'.join(lines)


# Generated at 2022-06-14 01:55:11.389469
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .utils import run_transformer_suite
    from .utils import get_node
    from .utils import get_ast


# Generated at 2022-06-14 01:55:24.383708
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet
    from ..transformers.base import BaseNodeTransformer
    from ..transformers.metaclass import MetaclassTransformer

    @snippet
    def target():
        class A(metaclass=B):
            pass

    base_transformer = BaseNodeTransformer()
    copy_tree = base_transformer.visit(target.get_ast())
    assert type(copy_tree) == ast.Module
    assert len(copy_tree.body) == 1

    assert type(copy_tree.body[0]) == ast.ClassDef
    node = copy_tree.body[0]
    assert node.name == 'A'
    assert len(node.keywords) == 1

# Generated at 2022-06-14 01:55:29.727368
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..fixtures.code_examples import py27, py37

    module = py27_example
    assert isinstance(module, ast.Module)

    transformer = MetaclassTransformer()
    result = transformer.visit(module)
    assert transformer._tree_changed == False

    module = py37_example
    assert isinstance(module, ast.Module)

    transformer = MetaclassTransformer()
    result = transformer.visit(module)
    assert transformer._tree_changed == True


# Generated at 2022-06-14 01:55:34.535227
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    
    code = 'class A(metaclass=B): pass'

# Generated at 2022-06-14 01:55:37.754850
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    origin = """class A(metaclass=B): pass"""

# Generated at 2022-06-14 01:55:44.390927
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse
    import six

    class A(object):
        pass

    class B(type(A)):
        pass

    @six.add_metaclass(B)
    class A(object):
        pass

    node = ast.parse(inspect.getsource(A))
    node = MetaclassTransformer().visit(node)
    source = astunparse.unparse(node)
    print(source)
    exec(source)

    assert type(A) is B

# Generated at 2022-06-14 01:55:54.644810
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import Optional
    from typed_ast import ast3 as ast
    from .six_temporary_import import SixTemporaryImportTransformer
    from .six_constants import SixConstantTransformer
    from .six_calls_transformer import SixCallsTransformer
    from .six_metaclass_transformer import MetaclassTransformer
    from .six_exceptions_transformer import SixExceptionsTransformer

    from .six_temporary_import import test_SixTemporaryImportTransformer_visit_Module
    from .six_constants import test_SixConstantTransformer_visit_Module, test_SixConstantTransformer_visit_Methods
    from .six_calls_transformer import test_SixCallsTransformer_visit_Module
    from .six_metaclass_transformer import test_Metaclass

# Generated at 2022-06-14 01:56:04.935140
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    from ast import parse, dump

    src = """
    class A(metaclass=B):
        pass
    """
    tree = parse(src)
    transformer = MetaclassTransformer()
    new_tree = transformer.visit(tree)
    print(dump(new_tree))
    code = compile(new_tree, '<string>', 'exec')
    glob = {}
    six_import.get_body(glob)
    locals = {}
    exec(code, glob, locals)
    assert locals['A'].__bases__ == (six_import.get_body()[0].value,)
    assert locals['A'].__metaclass__ == pyast.Name(id='B', ctx=pyast.Load())

# Generated at 2022-06-14 01:56:07.355356
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.test_utils import stringify_ast_tree, assert_ast_trees_equal

# Generated at 2022-06-14 01:56:20.454920
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """
    Before:
        class A(metaclass=B): pass
    
    After:
        class A(_py_backwards_six_withmetaclass(B)): pass

    """
    import astor
    from six import with_metaclass
    from astmonkey.transformers import CodeTransformer
    from astmonkey import visitors
    from astmonkey.code_gen import to_source
    cls = CodeTransformer(MetaclassTransformer).transform_code('class A(metaclass=B): pass')
    assert cls == 'class A(_py_backwards_six_withmetaclass(B)): pass'
    tree = ast.parse(cls)
    tree2 = visitors.NodeTransformer().visit(tree)

# Generated at 2022-06-14 01:56:22.254648
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast import parse, dump

# Generated at 2022-06-14 01:56:22.939457
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    pass

# Generated at 2022-06-14 01:56:31.936730
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .test_base import BaseNodeTransformerTest
    from ..utils.source import source

    class Test(BaseNodeTransformerTest):
        target = MetaclassTransformer
        target_version = (2, 7)
        transformer = MetaclassTransformer
        transform_source = source(*six_import.get_source())
        before = source("""
        x = 1
        """)
        after = source("""
        from six import with_metaclass as _py_backwards_six_withmetaclass
        x = 1
        """)

    Test().test()



# Generated at 2022-06-14 01:56:34.631028
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.unparser import Unparser

    script = 'class A(metaclass=MyMetaclass): pass'
    expected = six_import.get_script() + class_bases.get_script() + script

    module = ast.parse(script)
    transformer = MetaclassTransformer()
    transformer.visit(module)
    assert transformer.tree_changed
    assert module
    assert Unparser(module) == expected



# Generated at 2022-06-14 01:56:38.421072
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node_input = ast.parse("class A(): pass")
    node_expected = ast.parse("""
                        from six import with_metaclass as _py_backwards_six_withmetaclass
                        class A(): pass
                    """)
    node_output = MetaclassTransformer().visit(node_input)
    assert ast.dump(node_output) == ast.dump(node_expected)


# Generated at 2022-06-14 01:56:39.981413
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .test_env import test_env

# Generated at 2022-06-14 01:56:44.961881
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    class UnittestMetaclassTransformer(MetaclassTransformer):
        def visit_Module(self, node: ast.Module) -> ast.Module:
            self._code = node.body[0].body[0].value.value.id
            return ast.Module()


# Generated at 2022-06-14 01:56:57.735751
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from nuitka.ast.nodes.ClassDef import (
        ClassDef,
        ClassDefType,
    )
    from nuitka.ast.nodes.FunctionDef import FunctionDef
    from nuitka.ast.nodes.Import import Import
    from nuitka.ast.nodes.Name import Name
    from nuitka.ast.nodes.PassStatement import PassStatement
    from nuitka.ast.nodes.ImportFrom import ImportFrom
    from nuitka.ast.nodes.Module import Module
    from nuitka.ast.nodes.Statement import Statement

    six_import_ = ImportFrom(module="six", names=[("with_metaclass", "with_metaclass")], level=0)

# Generated at 2022-06-14 01:57:08.427998
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .base import BaseNodeTest
    from .base import BaseUnaryOpTest
    from .base import BaseNameTest

    class Test(BaseNodeTest, BaseUnaryOpTest, BaseNameTest):
        target = 2, 7
        transformer = MetaclassTransformer

        @property
        def ast(self) -> ast.AST:
            return ast.Module(body=[
                ast.ClassDef(
                    name='A',
                    bases=[],
                    body=[],
                    keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B'))]
                )
            ])


# Generated at 2022-06-14 01:57:14.975659
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor


# Generated at 2022-06-14 01:57:24.906459
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    #
    #   class A(metaclass=B, object):
    #       pass
    #
    node = ast.ClassDef(name='A', bases=[], keywords=[],
                        body=[ast.Pass()], decorator_list=[], lineno=1, col_offset=1)
    node.keywords.append(ast.keyword(
        arg='metaclass', value=ast.Name(id='B', ctx=ast.Load(), lineno=1, col_offset=15)))
    node.bases.append(ast.Name(id='object', ctx=ast.Load(), lineno=1, col_offset=13))
    #
    #   class A(_py_backwards_six_with_metaclass(B, object))
    #       pass
    #

# Generated at 2022-06-14 01:57:31.758233
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(metaclass=B):\n  pass')
    MetaclassTransformer(node).visit(node)
    assert ast.dump(node) == "from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)):\n  pass"

test_MetaclassTransformer_visit_ClassDef()


# Generated at 2022-06-14 01:57:37.990537
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..codegen import SourceGenerator
    node = ast.parse("""
    class A(metaclass=B):
        pass
    """)

    result = SourceGenerator().visit(MetaclassTransformer().visit(node))

# Generated at 2022-06-14 01:57:49.392192
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ast_tools.tests.tester import assert_convert

    assert_convert('''
        class A(Foo, Bar):
            pass
        ''', '''
        class A(_py_backwards_six_withmetaclass(Foo, Bar)):
            pass
        ''')

    assert_convert('''
        class A(metaclass=Foo, Baz):
            pass
        ''', '''
        class A(_py_backwards_six_withmetaclass(Foo, Baz)):
            pass
        ''')

# Generated at 2022-06-14 01:58:00.149598
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source_to_ast as sta
    from ..utils.source import source
    from ..utils.compare import compare_ast
    from ..utils.unparse import Unparser

    src1 = """
    class A(metaclass=B): pass
    """

    src2 = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)): pass
    """

    src3 = """
    class A(object): pass
    """

    ast1 = sta(source(src1))
    ast2 = sta(source(src2))
    ast3 = sta(source(src3))

    # Uncomment to generate new test cases
    # with open('tests/fixtures/Met

# Generated at 2022-06-14 01:58:01.042228
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:02.856627
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor, six

# Generated at 2022-06-14 01:58:09.525593
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..six import parse as six_parse

    input = """\
    class A(metaclass=B): pass
    """
    expected = """\
    from six import with_metaclass as _py_backwards_six_with_metaclass

    class A(_py_backwards_six_with_metaclass(B)):
        pass
    """
    node = six_parse(input)
    MetaclassTransformer().visit(node)
    output = six_parse(expected)
    compare_ast(node, output)

# Generated at 2022-06-14 01:58:11.174793
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer()

# Generated at 2022-06-14 01:58:21.537374
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..ast_manipulation import fix_missing_locations, ast_to_src

    src = b"""class A(object): pass"""
    module = ast.parse(src)
    module = MetaclassTransformer().visit(module)
    module = fix_missing_locations(module)
    src_fixed = ast_to_src(module)

# Generated at 2022-06-14 01:58:28.495091
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..testing.visitor import assert_source

    source = """
    class A(metaclass=B, **args):
        pass
    """

    expected = """
    class A(_py_backwards_six_with_metaclass(B), **args):
        pass
    """

    m = MetaclassTransformer()
    assert_source(expected, m.visit(ast.parse(source)))


# Generated at 2022-06-14 01:58:30.263867
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .. import compile

# Generated at 2022-06-14 01:58:39.580814
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils import get_ast

    body = [
        ast.ClassDef(name='A',
                     bases=[ast.Name(id='B', ctx=ast.Load()),
                            ast.Name(id='C', ctx=ast.Load())],
                     body=[],
                     keywords=[ast.keyword(
                         arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))]),
        ast.Expr(value=ast.Call(func=ast.Name(id='A', ctx=ast.Load()),
                                args=[], keywords=[]))
    ]
    node = ast.Module(body=body)
    transformed = MetaclassTransformer('__main__').visit(node)

    print(ast.dump(transformed))


# Generated at 2022-06-14 01:58:43.922545
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = '''class A(metaclass=C): pass'''
    node = MetaclassTransformer().run(code)
    assert node.body[1].bases[0].elts[0].id == '_py_backwards_six_withmetaclass'

# Generated at 2022-06-14 01:58:47.004727
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import sys
    if sys.version_info[:2] < (3, 6):
        raise AssertionError("Unit test should be run on Python 3.6 or higher.")

    import astroid

# Generated at 2022-06-14 01:58:48.161702
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from . import case


# Generated at 2022-06-14 01:58:50.405928
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:59.247477
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():

    source = """
    class A:
        def __init__(self):
            self.x = 5
            
    class B(object):
        def __init__(self):
            self.x = 5
            
    class C(object, metaclass=type):
        def __init__(self):
            self.x = 5
            
    class D(metaclass=type):
        def __init__(self):
            self.x = 5
    """


# Generated at 2022-06-14 01:59:10.473552
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.source import source
    from ..utils.ast_to_source import ast_to_source
    from ..utils.snippet import snippet

    @snippet
    def class_def(metaclass):
        class A(metaclass=metaclass):
            pass

    tree = ast.parse(source(class_def.get_source(metaclass=None)))
    expected_tree = ast.parse(source(
        six_import.get_source() + class_def.get_source(metaclass='metaclass')))
    trans = MetaclassTransformer(tree=tree)
    trans.visit(tree)
    assert trans._tree_changed
    assert ast_to_source(tree) == ast_to_source(expected_tree)

# Generated at 2022-06-14 01:59:21.599899
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.fake import FakeFile
    from ..utils.run_visitor import run_visitor
    from ..utils.simple_ast import ast_from_code


# Generated at 2022-06-14 01:59:24.837178
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    f = ast.parse('class A(metaclass=B): pass')
    assert_code_equal(f, 'class A(_py_backwards_six_withmetaclass(B)): pass')


# Generated at 2022-06-14 01:59:35.171694
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    snippet1 = six_import.get_body()
    snippet2 = class_bases.get_body(metaclass=ast.Name(id='foo'), bases=ast.List(elts=[]))
    expect = ast.Module(
        body=[snippet1,
              ast.ClassDef(name='A',
                           bases=[snippet2],
                           keywords=[],
                           body=[],
                           decorator_list=[])
              ])

    node = ast.Module(
        body=[ast.ClassDef(name='A',
                           bases=[],
                           keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='foo'))],
                           body=[],
                           decorator_list=[])
              ])

    transformer = MetaclassTransformer()
    actual = transformer

# Generated at 2022-06-14 01:59:47.552733
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = compile("""
    class A(metaclass=B):
        pass
""", filename='', mode='exec')
    transformer = MetaclassTransformer(target_version=(3, 0))
    module = transformer.visit(module)  # type: ignore
    assert type(module) == ast.Module
    assert type(module.body[0]) == ast.ImportFrom
    assert module.body[0].names[0].name == '_py_backwards_six_withmetaclass'
    assert type(module.body[1]) == ast.FunctionDef
    assert module.body[1].name == '_py_backwards_six_withmetaclass'
    assert module.body[2].name == 'A'
    assert type(module.body[2]) == ast.ClassDef

# Generated at 2022-06-14 01:59:51.584003
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..testing import assert_transform

    assert_transform(MetaclassTransformer, MetaclassTransformer.__doc__,
        'import six # 1\n\n',
        explicit_dependencies=['six']
    )



# Generated at 2022-06-14 01:59:59.108713
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import textwrap
    from ..utils import assert_equal_ast

    node = ast.parse(textwrap.dedent('''
    class A(metaclass=B):
        pass
    '''))
    expected = ast.parse(textwrap.dedent('''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''))
    MetaclassTransformer.run_on_tree(node)
    assert_equal_ast(node, expected)

# Generated at 2022-06-14 02:00:05.446111
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import py_backwards
    from .test_utils import wrap_to_test
    metaclass = MetaclassTransformer()
    @wrap_to_test
    def test():
        class A(metaclass=type):
            a = 1
    result = py_backwards.transform(test, [metaclass])
    assert 'class A(_py_backwards_six_with_metaclass(type))' in result

# Generated at 2022-06-14 02:00:16.706371
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent
    from ..compiler import compile_snippet
    from ..utils.tree import parse
    from ..utils.test_utils import transform_and_compare_texts

    snippet_before = dedent("""
        class A(metaclass=B):
            pass
        """)
    expected_snippet_after = dedent("""
        class A(_py_backwards_six_withmetaclass(B)):
            pass
        """)

    snippet_after = compile_snippet(snippet_before,
                                    modules=[MetaclassTransformer])

    node_before = parse(snippet_before)
    node_after = parse(snippet_after)

    MetaclassTransformer(node_before).visit(node_before)  # type: ignore

   

# Generated at 2022-06-14 02:00:21.895847
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .py2to3 import Python2to3
    from .. import ConversionContext
    from typing import List

    src: str = """class A(metaclass=B):
        pass"""

# Generated at 2022-06-14 02:00:31.372115
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""
        class A(metaclass=B):
            pass""")
    tree = MetaclassTransformer().visit(tree)

    correct_ast = """
        from six import with_metaclass as _py_backwards_six_withmetaclass 
        
        class A(_py_backwards_six_withmetaclass(B)) :
            pass"""
    assert ast.dump(ast.Module(body=[ast.parse(correct_ast).body[0]])) == ast.dump(tree)

# Generated at 2022-06-14 02:00:50.739919
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    expected_output = six_import.get_ast()
    module = ast.Module(body=[])
    MetaclassTransformer().visit_Module(module)
    assert expected_output.body == module.body, 'method visit_Module() of class MetaclassTransformer is broken'



# Generated at 2022-06-14 02:00:55.859267
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast.ast3 import parse
    tree = parse('class A(object): pass')
    node = tree.body[0]
    cls = MetaclassTransformer()
    cls.visit(tree)
    assert isinstance(tree.body[1], ast.FunctionDef)
    assert isinstance(node.bases[0], ast.Call)



# Generated at 2022-06-14 02:01:06.234766
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast

    class A(metaclass=type):
        pass

    class B(metaclass=type, stuff=1):
        pass

    class C:
        pass

    class D(B, C):
        pass

    inputs = [
        ast.parse(inspect.getsource(A)),
        ast.parse(inspect.getsource(B)),
        ast.parse(inspect.getsource(C)),
        ast.parse(inspect.getsource(D)),
    ]


# Generated at 2022-06-14 02:01:07.886504
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    MetaclassTransformer()

# Generated at 2022-06-14 02:01:12.839988
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast.ast3 import parse
    from .base import BaseNodeTransformer
    from .six import SixModuleTransformer
    from .op2func import Op2FuncTransformer

# Generated at 2022-06-14 02:01:23.474420
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.tree import get_node
    import sys
    import six

    module_name = '__metaclass_test__'
    src = 'class A(metaclass=type):\n    pass'
    node = ast.parse(src, module_name)
    MetaclassTransformer().visit(node)
    sys.modules[module_name] = node
    del sys.modules[module_name]
    assert get_node(node, ast.Name, id='_py_backwards_six_withmetaclass')

    class B(six.with_metaclass(type)):
        pass

    assert isinstance(B, type)


# Generated at 2022-06-14 02:01:24.830789
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import assert_transform, transform


# Generated at 2022-06-14 02:01:28.839069
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    module = ast.parse('''
    class A(metaclass=B):
        pass
    ''')

    MetaclassTransformer().visit(module)
    assert to_source(module) == six_import.get_source() + '''
    class A(metaclass=B):
        pass
    '''

# Generated at 2022-06-14 02:01:39.385788
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import astor
    # test snippet
    node = ast.parse("""
        class A(metaclass=object):
            pass
    """)
    result = MetaclassTransformer().visit(node)
    assert astor.to_source(result).strip() == """
    import six

    class A(six.with_metaclass(object)):
        pass
    """.strip()

    # test snippet
    node = ast.parse("""
        class A(object, metaclass=object):
            pass
    """)
    result = MetaclassTransformer().visit(node)
    assert astor.to_source(result).strip() == """
    import six

    class A(six.with_metaclass(object, object)):
        pass
    """.strip()

# Generated at 2022-06-14 02:01:47.561222
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class SUT(unittest.TestCase):
        def setUp(self) -> None:
            self.t = MetaclassTransformer()
            self.node = ast.parse('class C(object, metaclass=A): pass')

        def test_creates_six_import(self):
            self.t.visit(self.node)
            actual = ast.dump(self.node.body[0], include_attributes=True)
            expected = six_import.get_ast().body[0]
            self.assertEqual(actual, expected)

        def test_uses_six_import(self):
            self.t.visit(self.node)
            actual = ast.dump(self.node.body[1], include_attributes=True)

# Generated at 2022-06-14 02:02:20.952191
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    # ******************************************************************************
    # class A(metaclass=B):
    #     pass
    # ******************************************************************************
    source = 'class A(metaclass=B): pass'

# Generated at 2022-06-14 02:02:22.409345
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import typed_ast.ast3 as ast


# Generated at 2022-06-14 02:02:24.872768
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():

    source = """class Test(object): pass"""


# Generated at 2022-06-14 02:02:31.111580
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    source = ast_parse('''class A(metaclass=B):
        pass
        ''')
    expected = ast_parse('''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
    ''')
    result = MetaclassTransformer().visit(source)
    assert_equal(result, expected)

# Generated at 2022-06-14 02:02:41.248902
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import build
    from ..utils.compile_to_ast import compile_to_ast

    class MetaclassTransformer_visit_ClassDef_TestCase(unittest.TestCase):
        @property
        def ClassDef_class_with_metaclass_stmt(self):
            return """
            class A(metaclass=B):
                pass
            """

        @property
        def ClassDef_class_with_metaclass_ast(self):
            return build(self.ClassDef_class_with_metaclass_stmt)

        def test_ClassDef_class_with_metaclass_stmt(self):
            t = MetaclassTransformer()

# Generated at 2022-06-14 02:02:50.717074
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer()
    node = ast.ClassDef(name='Foo',
                        bases=[ast.Name(id='object', ctx=ast.Load())],
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='A', ctx=ast.Load()))])
    r = t.visit(node)

# Generated at 2022-06-14 02:02:51.280786
# Unit test for constructor of class MetaclassTransformer

# Generated at 2022-06-14 02:02:58.411513
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from textwrap import dedent
    from typed_ast import ast3 as ast
    class_def = ast.parse(dedent('''\
        class Tuple(metaclass=abc.ABCMeta): ...'''))
    node = class_def.body[0]
    assert isinstance(node, ast.ClassDef)
    assert len(node.keywords) == 1 and node.keywords[0].arg == 'metaclass'
    assert len(node.bases) == 1 and isinstance(node.bases[0], ast.Name) and node.bases[0].id == 'abc.ABCMeta'
    tree_changed, module_changed = MetaclassTransformer().visit(class_def)
    assert tree_changed and module_changed

# Generated at 2022-06-14 02:03:04.658034
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import sys
    if sys.version_info[:2] == (2, 7):
        node = ast.parse('class A(metaclass=B): pass')
        t = MetaclassTransformer()
        t.visit(node)
        #print(ast.dump(node))
        #assert ast.dump(node) == "Module(body=[ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[], lineno=1, col_offset=0)])"

# Generated at 2022-06-14 02:03:11.328981
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..tools import assert_node_equal, transform

    src = "class A(metaclass=B):\n    pass"
    expected = ("from six import with_metaclass as _py_backwards_six_withmetaclass\n\n"
                "class A(_py_backwards_six_withmetaclass(B)):\n    pass")
    actual = transform(src, [MetaclassTransformer])
    assert_node_equal(expected, actual)

# Generated at 2022-06-14 02:04:27.534450
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    class_ = ast.parse('class A(metaclass=B): pass').body[0]
    transformer = MetaclassTransformer()
    assert transformer.visit(class_).bases[0].args[0].id == '_py_backwards_six_withmetaclass'

# Generated at 2022-06-14 02:04:36.672488
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.python_source import SOURCE_2_7, SOURCE_3_6
    from ..utils import transform_and_compare

    from typed_ast import ast3 as ast

    with open(__file__) as f: this_file = f.read()

    class A(object):
        pass

    class B(metaclass=A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    class E(C):
        pass

    module = ast.parse(this_file)
    new_module = MetaclassTransformer().visit(module)

    # No change needed
    assert transform_and_compare(this_file, module, new_module, SOURCE_3_6)

    # Transform

# Generated at 2022-06-14 02:04:45.004351
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():

    code = """
    class A(metaclass=B):
        pass
    """

    tree = ast.parse(code)
    MetaclassTransformer().visit(tree)
    assert ast.dump([tree]) == '[Module(body=[From(module=\'six\', names=[alias(name=\'with_metaclass\', asname=\'_py_backwards_six_withmetaclass\')], level=0), ClassDef(name=\'A\', bases=_py_backwards_six_withmetaclass(B), keywords=[], body=[], decorator_list=[])])'



# Generated at 2022-06-14 02:04:48.470981
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    x = ast.parse(six_import.get_source(), '-', 'exec')
    y = MetaclassTransformer().visit(x)
    assert(ast.dump(x) == ast.dump(y))

# Generated at 2022-06-14 02:04:49.868675
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:05:00.164341
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from typed_ast import ast3 as ast
    from .. import Py2to3Tree
    import unittest

    tree = Py2to3Tree('class A(metaclass=B): pass')
    MetaclassTransformer().visit(tree.ast)
    new_locals = tree.new_locals
    new_body = tree.new_body

    expected_locals = {'_py_backwards_six_withmetaclass': '_py_backwards_six_withmetaclass'}