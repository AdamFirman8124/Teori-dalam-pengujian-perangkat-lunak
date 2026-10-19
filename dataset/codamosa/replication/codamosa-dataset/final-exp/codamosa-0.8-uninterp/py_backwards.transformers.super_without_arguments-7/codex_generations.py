

# Generated at 2022-06-14 02:28:02.045644
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class MyCompiler(Compiler):
        def extend_ast_transforms(self, transforms: Sequence[Type[BaseNodeTransformer]]) -> Sequence[Type[BaseNodeTransformer]]:
            return transforms + [SuperWithoutArgumentsTransformer]

    tree = ast.parse('super()')
    MyCompiler(tree=tree)

# Generated at 2022-06-14 02:28:12.979353
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode, source_to_ast, source_to_ast_node
    import ast
    src = source_to_unicode("""
    class A(object):
        def __init__(self):
            super()
    """)
    tree = source_to_ast(src)
    SuperWithoutArgumentsTransformer().visit(tree)
    node = source_to_ast_node(tree, ast.ClassDef)
    assert node.body[0].name == '__init__'
    assert node.body[0].args.args[0].arg == 'self'
    assert node.body[0].body[0].value.args[0].id == 'A'
    assert node.body[0].body[0].value.args[1].id == 'self'

# Generated at 2022-06-14 02:28:13.857339
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:18.354315
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_to_python
    tree = compile_to_python("""
        class C:
            def f(self):
                super().foo()
    """)
    assert tree == compile_to_python("""
        class C:
            def f(self):
                super(C, self).foo()
    """)

# Generated at 2022-06-14 02:28:19.926375
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:28:28.953838
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import ast
    import typed_astunparse
    input_code = "super()"
    expected_code = "super(cls, self)"
    parsed = ast.parse(input_code)
    class_node = ast.ClassDef(name="cls", body=[ast.FunctionDef(name="f0", body=[parsed], args=ast.arguments(args=[ast.arg(arg="self", annotation=None)]))], bases=[])
    SuperWithoutArgumentsTransformer().visit(class_node)
    actual_code = typed_astunparse.unparse(class_node)
    assert expected_code == actual_code

# Generated at 2022-06-14 02:28:38.300229
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import typed_ast.ast3 as ast
    from ..tree_transformer import TreeTransformer
    tree_transformer = TreeTransformer()
    tree_transformer.register_transformer(SuperWithoutArgumentsTransformer())

    code = '''class Test:
        def method(self):
            super()
    '''
    test_tree = ast.parse(code)
    tree_transformer.visit(test_tree)

# Generated at 2022-06-14 02:28:41.120849
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import parse
    from .. import compile


# Generated at 2022-06-14 02:28:42.350900
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:47.033113
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    module_ast = create_ast('super()')
    tree = ast.parse(module_ast)

    SuperWithoutArgumentsTransformer().visit(tree)

    assert ast.dump(tree) == create_ast('super(Cls, self)')



# Generated at 2022-06-14 02:28:51.751453
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:59.363987
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = \
        """
        class A(object):
            def __init__(self):
                super()
        """

    expected_code = \
        """
        class A(object):
            def __init__(self):
                super(A, self)
        """

    tree = ast.parse(dedent(code))
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    transformed_code = unparse(tree).strip()
    assert expected_code == transformed_code



# Generated at 2022-06-14 02:29:02.236433
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    from util.ast_test import assert_source_equal

# Generated at 2022-06-14 02:29:05.198180
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert compile(tree, '', 'exec')

# Generated at 2022-06-14 02:29:11.200192
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node1 = ast.parse('super()').body[0]
    tree = ast.parse('class Foo:\n  def __init__(self, x):\n    super()')
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert node1 == tree.body[0].body[0].args[0]



# Generated at 2022-06-14 02:29:11.839612
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:12.836150
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:15.026295
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_transformers_base import run_test_tree_transformers
    from .. import tree


# Generated at 2022-06-14 02:29:17.044800
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast import parse
    from ..utils.test_utils import assert_text_transformation

# Generated at 2022-06-14 02:29:26.966219
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from lib2to3.pgen2 import token
    from lib2to3.pytree import Leaf

    my_node = ast.Call()
    my_node.func = ast.Name(id='super', ctx=ast.Load())
    my_name = ast.Name(id='cls', ctx=ast.Load())
    my_node.args = [ Leaf(token.NAME, 'cls') ]
    my_tree = ast.parse('foo')
    my_tree.body.append(my_node)

    my_visitor = SuperWithoutArgumentsTransformer(None, None, my_tree)

    result = my_visitor.visit_Call(my_node)

    assert result.func.id == "super"
    assert result.args[0].id == "cls"

# Generated at 2022-06-14 02:29:39.130496
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')

    node = tree.body[0].value

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

    class_def = ast.ClassDef(name='Cls')
    function_def = ast.FunctionDef(name='func', args=ast.arguments(args=[ast.arg(arg='self')]))

    transformer._append_node(node, class_def)
    transformer._append_node(node, function_def)

    assert type(node.func) is ast.Name
    assert node.args[0].id == 'Cls'
    assert node.args[1].id == 'self'

    x = 1

# Generated at 2022-06-14 02:29:41.073748
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.source import Source


# Generated at 2022-06-14 02:29:53.841239
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typing import List, TYPE_CHECKING

    if TYPE_CHECKING:
        from typed_ast import ast3 as ast
        from .base import BaseNodeTransformerTestCase

    class MyTestCase(BaseNodeTransformerTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.transformer = SuperWithoutArgumentsTransformer()

        def test_basic(self) -> None:
            tree = ast.parse('''
            class A:
                def __init__(a):
                    super()
                    pass
            ''')
            expected = ast.parse('''
            class A:
                def __init__(a):
                    super(A, a)
                    pass
            ''')

            self.check(tree, expected)


# Generated at 2022-06-14 02:30:02.669726
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import compile
    from ..utils.helpers import compare_source
    from ..node_utils import get_ast

    source = """
        class A:
            def __init__(self):
                super()
                super()
                super()
                
        class B(A):
            def __init__(self):
                super()
                super()
                super()
                
        class C(B):
            def __init__(self):
                super()
                super()
                super()
                
    """
    expected_tree = get_ast(compile(source, '<test>', 'exec'))
    actual_tree = get_ast(compile(source, '<test>', 'exec',
                                  [SuperWithoutArgumentsTransformer]))

# Generated at 2022-06-14 02:30:13.592804
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import from_string, to_string
    from .base import BaseNodeTransformer
    from ..transforms import SuperWithoutArgumentsTransformer
    source = '''
    class A:
        def a(self):
            super()

    class B(A):
        def b(self):
            super()

    class C(B):
        def c(self):
            super()

    class D(B):
        def d(self):
            super()
    '''
    tree = from_string(source)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

# Generated at 2022-06-14 02:30:16.523166
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

# Generated at 2022-06-14 02:30:24.746039
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.codegen import to_source
    from . import transform
    from . import GenericTransformer

    code = """
    class A(object):
        def f(self, bar=None):
            super().f()
    """
    expected_code = """
    class A(object):
        def f(self, bar=None):
            super(A, self).f()
    """
    tree = ast.parse(textwrap.dedent(code))
    transformer = SuperWithoutArgumentsTransformer(tree, GenericTransformer)
    transformer.visit(tree)
    source = to_source(tree)
    assert expected_code == source
    transform(code) == expected_code

# Generated at 2022-06-14 02:30:29.177001
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # example class
    code = '''
    class C:
        def __init__(self):
            super().__init__()
    '''
    # compiling source code
    tree = ast.parse(code)
    # transformers
    t1 = SuperWithoutArgumentsTransformer()
    # checking tree to match transformer
    print(t1('__init__', tree))
    assert t1('__init__', tree) is True
    # check if all nodes visited
    assert t1.nodes_visited == 9
    # check if all nodes visited
    assert t1.nodes_replaced == 1

# Generated at 2022-06-14 02:30:29.778866
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:31.223900
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ... import ast_parse, transform


# Generated at 2022-06-14 02:30:45.966156
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import assert_conversion
    from ..utils.constants import GLOBAL_VARS

    tests = [
        # (Single line test)
        ('super()', 'super(Cls, self)'),
        ('super()', 'super(Cls, cls)'),
        ('super()', 'super(cls, self)'),
        ('super()', 'super(cls, cls)'),
        ('super()', 'super(cls, foo)'),
    ]

    for t in tests:
        assert_conversion(
            SuperWithoutArgumentsTransformer,
            t[0],
            t[1],
            {
                name: ast.Name(id=name, ctx=ast.Load()) for name in GLOBAL_VARS
            },
        )

# Generated at 2022-06-14 02:30:46.705267
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:47.909452
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:51.811159
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode_node

    source = """
        class Foo(object):
            def bar(self):
                super(Foo, self).__init__()
        """

# Generated at 2022-06-14 02:30:53.542604
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .base import BaseNodeTransformer

# Generated at 2022-06-14 02:31:02.866183
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Given
    from typed_ast import ast3 as ast
    from ..utils import parse

    class TestTransformer(SuperWithoutArgumentsTransformer):
        def __init__(self, tree: ast.AST) -> None:
            self._tree = tree

    # When
    class Foo(object):
        def bar(self):
            super()

    tree = parse(Foo.bar.__code__)
    TestTransformer(tree).visit(tree)
    code_object = compile(tree, '<string>', 'exec')
    exec(code_object)
    f = Foo()
    f.bar()

# Generated at 2022-06-14 02:31:03.614568
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:04.516070
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:14.609783
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast, source_to_code

    # Test with function outside class
    source = '''
        super()
    '''
    expected = '''
        super()
    '''
    tree = source_to_ast(source)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert source_to_code(tree) == expected

    # Test with invalid self
    source = '''
        def test():
            super()
    '''
    expected = '''
        def test():
            super()
    '''
    tree = source_to_ast(source)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert source_to_code(tree) == expected

    # Test with valid self

# Generated at 2022-06-14 02:31:23.132268
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class A:
        def __init__(self):
            super().__init__()
            super().method()
        
        def method(self):
            super().__init__()
            super().method()
    '''
    correct_code = '''
    class A:
        def __init__(self):
            super(A, self).__init__()
            super(A, self).method()
        
        def method(self):
            super(A, self).__init__()
            super(A, self).method()
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse(correct_code))




# Generated at 2022-06-14 02:31:34.803063
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Given
    code = 'super()'
    tree = ast.parse(code)

    # When
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    compiled_code = compile(tree, '', 'exec')

    # Then
    exec(compiled_code)

# Generated at 2022-06-14 02:31:44.137276
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    from typed_ast import ast3 as ast
    from .test_base import BaseNodeTestCase
    from .test_helpers import test_node, test_node_exact, extract_node

    class DummyNode(ast.AST):
        _fields = ('dummy',)

    class Test(BaseNodeTestCase):
        target_version = (3, 7)

        def test_name_node_on_super_call(self):
            source = '''
            class Cls:
                def __init__(self):
                    super()
            '''
            expected = '''
            class Cls:
                def __init__(self):
                    super(Cls, self)
            '''
            tree = extract_node(source)

# Generated at 2022-06-14 02:31:55.157117
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseTestTransformer
    from .base import get_ast_tree
    import textwrap
    class TestTransformer(BaseTestTransformer):
        def assertEqual(self, first, second):
            super().assertEqual(textwrap.dedent(first).strip(), textwrap.dedent(second).strip())

    code = '''
        class MyClass(object):
            def my_method(self):
                pass
    '''
    expected = '''
        class MyClass(object):
            def my_method(self):
                super(MyClass, self)
                super(MyClass, self)
                super()
                super()

        def outside_class():
            super()
    '''
    tree = get_ast_tree(textwrap.dedent(code), SuperWithoutArgumentsTransformer)
   

# Generated at 2022-06-14 02:32:03.432152
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='__class__', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"


# Generated at 2022-06-14 02:32:12.141590
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super()"""
    module = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer(module).visit(module)
    assert(ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])")

# Generated at 2022-06-14 02:32:16.816223
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..compiler import compile_code
    code = compile_code("""
    class Dummy(object):
        def func(self):
            super()
    """)


# Generated at 2022-06-14 02:32:24.723431
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Note: Unit test is not strictly required due to small size of the code and ease of manual testing.
    code = """
    class A:
        def __init__(self):
            super()
    """
    expected_output = """
    class A:
        def __init__(self):
            super(A, self)
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    output = astor.to_source(tree)
    assert output == expected_output

# Generated at 2022-06-14 02:32:33.836670
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor, typed_ast.ast3
    source = """\
    class Foo:
        def bar(self):
            pass
        
    class Bar(Foo):
        def bar(self):
            super()
    """
    expected = """\
    class Foo:
        def bar(self):
            pass
        
    class Bar(Foo):
        def bar(self):
            super(Bar, self)
    """
    tree = typed_ast.ast3.parse(source)
    TransformerClass = SuperWithoutArgumentsTransformer
    transformer = TransformerClass()
    new_tree = transformer.visit(tree)
    result = astor.to_source(new_tree)
    assert(result == expected)

# Generated at 2022-06-14 02:32:43.045010
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ...tests.transformer_test_cases import (
        BaseTransformerTestCase,
        assertAstEqual
    )

    class Test(BaseTransformerTestCase):
        @property
        def transformer(self) -> BaseNodeTransformer:
            return SuperWithoutArgumentsTransformer

        def test_super_in_func_and_class(self):
            input = '''
            class A(object):
                def method(self):
                    super()
            '''
            expected = '''
            class A(object):
                def method(self):
                    super(A, self)
            '''
            assertAstEqual(self, input, expected)

        def test_super_outside_of_func_and_class(self):
            input = '''
            super()
            '''

# Generated at 2022-06-14 02:32:48.809139
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_from = "super()"
    code_to = "super(Cls, cls)"

    module_ast = ast.parse(code_from)
    SuperWithoutArgumentsTransformer().visit(module_ast)
    code_result = astor.to_source(module_ast)
    assert code_to == code_result

# Generated at 2022-06-14 02:33:04.996350
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    obj = SuperWithoutArgumentsTransformer(str(code), tree)
    obj.run()
    assert str(tree) == 'super(Cls, self)'

# Generated at 2022-06-14 02:33:13.150879
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    ref_node_1 = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])

    trans_node_1 = SuperWithoutArgumentsTransformer(ast.parse('class C:\n super()')).run()
    trans_node_1 = get_closest_parent_of(trans_node_1, ref_node_1, ast.FunctionDef)

    assert isinstance(trans_node_1.body[0], ast.Call)
    assert isinstance(trans_node_1.body[0].func, ast.Name)
    assert trans_node_1.body[0].func.id == 'super'

    assert len(trans_node_1.body[0].args) == 2

# Generated at 2022-06-14 02:33:23.121467
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    tree = ast.parse('class a: pass')
    transformer.visit(tree)

    tree = ast.parse('\n'.join([
        'class Foo:',
        '    def __init__(self):',
        '        super()',
        '        pass',
    ]))
    transformer.visit(tree)

    source = '\n'.join([
        'class Foo:',
        '    def __init__(self):',
        '        super()',
        '        pass',
    ])
    compiled_source = '\n'.join([
        'class Foo:',
        '    def __init__(self):',
        '        super(Foo, self)\n'
        '        pass',
    ])
    tree = ast.parse(source)


# Generated at 2022-06-14 02:33:29.607248
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    import astor

    class TestVisitor(unittest.TestCase):
        def test_constructor(self):
            transformer = SuperWithoutArgumentsTransformer(None)
            self.assertEqual(transformer._tree, None)
            self.assertEqual(transformer._tree_changed, False)

    unittest.main()



# Generated at 2022-06-14 02:33:30.878105
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast

# Generated at 2022-06-14 02:33:31.987131
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:38.242277
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    code = 'class Test: def __init__(self): super()'
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    assert transformer._tree_changed
    actual = compile(tree, '<string>', 'exec').code
    expected = 'class Test:\n    def __init__(self):\n        super(Test, self)\n'
    assert actual == expected

# Generated at 2022-06-14 02:33:38.923791
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:46.880841
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test that all super without arguments are transformed
    """
    from .. import setup_ast_parser, transform
    setup_ast_parser()

    code = """
    class Parent():
        def m(self):
            pass
    
    class Child(Parent):
        def m(self):
            super()
    """
    expected = """
    class Parent():
        def m(self):
            pass
    
    class Child(Parent):
        def m(self):
            super(Parent, self)
    """

    tree = ast.parse(code)
    transform(tree, [SuperWithoutArgumentsTransformer])
    actual = compile(tree, filename="<test>", mode='exec').strip()
    assert actual == expected

# Generated at 2022-06-14 02:33:48.708335
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:30.689785
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..codegen import to_source
    from .transformers.base import BaseTreeTransformer
    from .transformers.remove_decorator_locally_imported import RemoveDecoratorLocallyImportedTransformer
    from .transformers.remove_parenthesis_for_one_line_function import RemoveParenthesisForOneLineFunctionTransformer
    from .transformers.replace_nonlocal_with_global import ReplaceNonlocalWithGlobalTransformer
    from .transformers.replace_print_with_function import ReplacePrintWithFunctionTransformer
    from .transformers.replace_raise_with_assertion_errors import ReplaceRaiseWithAssertionErrorsTransformer
    from .transformers.replace_single_if_abbreviation import ReplaceSingleIfAbbreviationTransformer
    from .transformers.replace_single_for_abbreviation import ReplaceSingleForAb

# Generated at 2022-06-14 02:34:37.034190
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # test for super()
    node = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(node)
    assert ast.dump(node) == 'Expr(value=Call(func=Attribute(value=Super(type=Name(id="A", ctx=Load()), type_args=[]), attr="__init__", ctx=Load()), args=[Name(id="A", ctx=Load()), Name(id="self", ctx=Load())], keywords=[], starargs=None, kwargs=None))'

    # test for another func()
    node = ast.parse('func()')
    SuperWithoutArgumentsTransformer().visit(node)

# Generated at 2022-06-14 02:34:37.730026
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:38.852832
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:40.543413
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:48.039930
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..utils.helpers import ast_to_source
    from .. import compile_ast

    source = Source("""
    class A:
        def __init__(self):
            super().__init__()
    """)

    ast_tree = compile_ast(source)
    assert ast_to_source(ast_tree) == """
    class A:
        def __init__(self):
            super(A, self).__init__()
    """.strip()

# Generated at 2022-06-14 02:34:54.126283
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import assert_equal_ast
    source = 'super()'
    expected = 'super(Cls, self)'
    tree = ast.parse(source)
    tree = SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert_equal_ast(tree, expected)

# Generated at 2022-06-14 02:34:55.061202
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:57.989957
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    tree = compile("super()")
    assert tree == ast.parse("super(__name__, self)")

# Generated at 2022-06-14 02:35:05.638976
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''class A(object):
        def __init__(self):
            super()
            return
        '''
    expected_code = """class A(object):
    def __init__(self):
        super(A, self)
        return
    """
    result = SuperWithoutArgumentsTransformer().visit(ast.parse(code))
    assert astor.to_source(result) == expected_code

# Generated at 2022-06-14 02:36:27.763212
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    t = SuperWithoutArgumentsTransformer()

    # Without arguments before
    c1 = ast.parse("""\
        class Foo:
            def bar(self):
                super()
    """)
    t.visit(c1)
    assert ast.dump(c1) == ast.parse("""\
        class Foo:
            def bar(self):
                super(Foo, self)
    """).body[0].body[0].body[0]

    # With arguments before
    c2 = ast.parse("""\
        class Foo:
            def bar(self):
                super(Foo)
    """)
    t.visit(c2)

# Generated at 2022-06-14 02:36:28.939400
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:36:33.607471
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from nala.utils.testing import snapshot_ast
    from nala.transformers.super_without_args import SuperWithoutArgumentsTransformer
    code = 'super()'
    tree = ast.parse(code)
    target = SuperWithoutArgumentsTransformer(tree=tree)
    target.transform()
    snapshot_ast(astor.to_source(tree))

# Generated at 2022-06-14 02:36:37.500591
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ast_helper import parse
    import copy

    # Before changing

# Generated at 2022-06-14 02:36:38.757904
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:41.557942
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
    class Foo:
        def __init__(self):
            super()
    """

# Generated at 2022-06-14 02:36:53.727586
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse(
    """
    class Foo:
      def __init__(self):
        super()
    """
    )
    SuperWithoutArgumentsTransformer(node, 2.7).visit(node)
    assert type(node.body[0]) == ast.ClassDef
    assert type(node.body[0].body[0]) == ast.FunctionDef
    assert type(node.body[0].body[0].body[0]) == ast.Expr
    assert type(node.body[0].body[0].body[0].value) == ast.Call
    assert type(node.body[0].body[0].body[0].value.func) == ast.Name
    assert node.body[0].body[0].body[0].value.func.id == 'super'

# Generated at 2022-06-14 02:37:03.792042
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test that the transformer properly fixes the following code:
        super()
    """
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(
        ast.parse(
            '''class A(B):
               def a(self):
                   c = super()''',
            mode='exec'
        )
    )
    assert transformer._tree_changed


# Generated at 2022-06-14 02:37:04.261718
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:12.713236
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import transform, assert_equal_ast, dedent
    code = dedent('''
    class A:
        def __init__(self):
            super()

    class B:
        def __init__(self):
            super().__init__()
    ''')
    correct_code = dedent('''
    class A:
        def __init__(self):
            super(A, self)

    class B:
        def __init__(self):
            super(B, self).__init__()
    ''')
    assert_equal_ast(transform(SuperWithoutArgumentsTransformer, code), correct_code)