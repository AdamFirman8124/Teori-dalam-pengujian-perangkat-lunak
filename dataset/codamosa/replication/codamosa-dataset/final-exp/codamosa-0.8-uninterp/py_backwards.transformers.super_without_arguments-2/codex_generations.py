

# Generated at 2022-06-14 02:28:05.656511
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing.transformer_unit_test import TransformerUnitTest

    code = '''
    class Test(object):
        def test(self):
            super()
    '''
    expected_code = '''
    class Test(object):
        def test(self):
            super(Test, self)
    '''
    tu = TransformerUnitTest(SuperWithoutArgumentsTransformer, code, expected_code)
    tu.run_tests()


# Generated at 2022-06-14 02:28:06.617702
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:07.633965
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    from typed_ast import ast3 as ast
    from astunparse import unparse
    from ..transpile import transpile
    from ..pipeline import Pipeline


# Generated at 2022-06-14 02:28:09.943473
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import test_super_without_arguments_transformer
    return test_super_without_arguments_transformer.test_SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:28:22.343423
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    class TestSuperWithoutArgumentsTransformer(SuperWithoutArgumentsTransformer):
        def generic_visit(self, node: ast.AST) -> ast.AST:
            return node

    tree = ast.parse('super()', mode='exec')
    node_to_test = tree.body[0].value
    t = TestSuperWithoutArgumentsTransformer()
    result = t.visit_Call(node_to_test)
    assert ast.dump(result) == ast.dump(ast.parse('super(Cls, self)', mode='exec').body[0].value)

    tree = ast.parse('def test_super():\n'
                     '  super()', mode='exec')
    node_to_test = tree.body[0].body[0].value
    t = TestSuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:28:32.730588
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..context import Context

    def compile_function(source: str) -> str:
        ast_tree = ast.parse(source)
        Compiler.attach_logging_info(ast_tree)
        context = Context(target_version=SuperWithoutArgumentsTransformer.target)
        SuperWithoutArgumentsTransformer(context).visit(ast_tree)
        return astor.to_source(ast_tree)

    assert compile_function('''
        class A:
            def __init__(self):
                super()
    ''') == '''
        class A:
            def __init__(self):
                super(A, self)
    '''


# Generated at 2022-06-14 02:28:34.158154
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Test method visit_Call of class SuperWithoutArgumentsTransformer."""
    pass

# Generated at 2022-06-14 02:28:38.935715
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # type: () -> None
    """Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
    """
    from ..utils.source import Source
    from .. import compile_string


# Generated at 2022-06-14 02:28:39.635098
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:50.251488
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import parse_ast_tree
    from ..snippets import python_snippets
    from ..utils.ast_helper import get_ast_node_ids

    tree = parse_ast_tree(python_snippets['super_without_arg_with_inherit'])
    node = get_ast_node_ids(tree, 'Call(Name(super), [])')[0]
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    node = get_ast_node_ids(tree, 'Call(Name(super), [Name(Cls), Name(self)])')[0]

# Generated at 2022-06-14 02:28:57.748243
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    class A(object):
        def __init__(self):
            super()
    tree = ast.parse(inspect.getsource(A))
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    code = astor.to_source(tree)
    assert 'super(A, self)' in code


# Generated at 2022-06-14 02:29:00.808997
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ..parser import parse

# Generated at 2022-06-14 02:29:08.805567
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = '''
        class Parent:
            def __init__(self):
                super()
        class Child(Parent):
            def __init__(self):
                super()
    '''
    expected_code = '''
        class Parent:
            def __init__(self):
                super(Parent, self)
        class Child(Parent):
            def __init__(self):
                super(Child, self)
    '''
    SuperWithoutArgumentsTransformer.run_test(code, expected_code)



# Generated at 2022-06-14 02:29:19.704671
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_
    from .test_helpers import assert_compiled
    from ..utils.helpers import repthonify
    from pathlib import Path
    from .base import BaseNodeTransformer

    test_file = Path(BaseNodeTransformer.get_repo_root(), 'tests/samples/super.py')
    with test_file.open('r', encoding='utf-8') as fd:
        c = compile_(fd.read(), '2.py', mode='exec')


# Generated at 2022-06-14 02:29:25.823815
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseStreamingTransformer
    from .. import transform
    from .. import print_ast

    @transform(SuperWithoutArgumentsTransformer)
    def test_function_simple(a, b):
        super()

    # And now a more complex function/class
    @transform(SuperWithoutArgumentsTransformer)
    def test_function_complex(a, b=None):
        class TestClass(object):
            def test_method(self):
                super()
        
        class TestClass2(object):
            x = 1

            @classmethod
            def test_class_method(cls):
                super()
                super()

            def test_method(self):
                super()

        return TestClass, TestClass2

    print_ast.print_ast(test_function_simple)
    print()
    print_

# Generated at 2022-06-14 02:29:33.134327
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from py2ts.compilers.transformers.base import TreeTransformer
    from typed_ast import ast3 as ast
    from ..utils import compile_to_ast

    mod = compile_to_ast("""
        class Parent:
            def __init__(self):
                super().__init__()
    """)  # type: ast.Module

    transformer = TreeTransformer(2, 7)
    transformer.visit(mod)
    assert transformer.result_tree == mod

# Generated at 2022-06-14 02:29:44.116281
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Python code we want to compile to
    code = """
        class Foo:
            def bar(self):
                super()
    """
    # Expected output:
    expected_code = """
        class Foo:
            def bar(self):
                super(Foo, self)
    """
    t = SuperWithoutArgumentsTransformer()
    t.visit(ast.parse(code))
    generated_code = compile(t.root, '', 'exec')
    exec(generated_code)
    assert expected_code.strip() == ast.dump(ast.parse(code.strip())).strip()

# Generated at 2022-06-14 02:29:54.079726
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from ..utils.compiler import compile_nodes
    from .base import BaseNodeTransformer

    code = """
    class A(object):
        def __init__(self):
            super().__init__()
    """

    node = source_to_nodes(code)[0]
    BaseNodeTransformer.reset()
    SuperWithoutArgumentsTransformer().visit(node)  # type: ignore
    assert compile_nodes(node) == """
    class A(object):
        def __init__(self):
            super(A, self).__init__()
    """

# Generated at 2022-06-14 02:29:57.904404
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        def __init__(self):
            super()
    """
    module = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(module)
    transformer.visit(module)

    assert code != module_to_code(module)
    assert len(transformer.errors) == 0


# Generated at 2022-06-14 02:30:09.164316
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .tester import BaseNodeTransformerTester
    from ..utils import dump_ast

    # Test simple super() .
    code = """super()"""
    expect = """super(Cls, self)"""
    tree = ast.parse(code)
    expected_tree = ast.parse(expect)
    result = BaseNodeTransformerTester(SuperWithoutArgumentsTransformer).visit(tree)
    assert dump_ast(result) == dump_ast(expected_tree)

    # Test super() with a class.
    code = """
    class C:
        def a(self, b):
            super()
    """
    expect = """
    class C:
        def a(self, b):
            super(C, self)"""
    tree = ast.parse(code)

# Generated at 2022-06-14 02:30:16.856362
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class_name = "A"
    func_name = "f"

    # Test
    transformer = SuperWithoutArgumentsTransformer(None)

# Generated at 2022-06-14 02:30:26.533463
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:30:29.287897
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import run_transformer
    from ..utils import get_ast
    from .test_helpers import get_func_first_arg_name


# Generated at 2022-06-14 02:30:37.236468
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

    original_tree = list(ast.parse('super()').body)[0]
    assert isinstance(original_tree, ast.Expr)
    assert isinstance(original_tree.value, ast.Call)

    transformed_tree = transformer.visit(original_tree)
    assert isinstance(transformed_tree, ast.Expr)
    assert isinstance(transformed_tree.value, ast.Call)
    assert isinstance(transformed_tree.value.args[0], ast.Name)
    assert isinstance(transformed_tree.value.args[1], ast.Name)


SUPER_WITHOUT_ARGUMENTS_TRANSFORMER = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:30:44.229568
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class A:
            def __init__(self):
                super().__init__()
    '''
    expected_code = '''
        class A:
            def __init__(self):
                super(A, self).__init__()
    '''

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree).strip() == expected_code.strip()



# Generated at 2022-06-14 02:30:46.490515
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test(SuperWithoutArgumentsTransformer):
        pass

# Generated at 2022-06-14 02:30:57.451523
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    class FakeTree(object):
        def __init__(self, parent, node, node_type):
            self.parent = parent
            self.node = node
            self.node_type = node_type
    
    def fake_visit(self, node: ast.Call) -> ast.Call:
        return node

    # Testing super() call outside of function definition
    root = ast.Module([ast.Call(func=ast.Name(id='super'), args=[], keywords=[], starargs=None, kwargs=None)])
    fake_tree = FakeTree(None, None, None)
    transformer = SuperWithoutArgumentsTransformer(fake_tree, '2.7')
    transformer.generic_visit = fake_visit
    transformer.visit(root)
    assert len(transformer._err_msgs) == 1

# Generated at 2022-06-14 02:30:58.174143
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:01.532539
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode
    from ..utils.helpers import dump_tree
    from ..utils.ast_parser import get_parser
    

# Generated at 2022-06-14 02:31:03.165112
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from typed_ast import parse


# Generated at 2022-06-14 02:31:12.421699
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astunparse


# Generated at 2022-06-14 02:31:13.593967
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    from ..utils.test_utils import assert_program_equal


# Generated at 2022-06-14 02:31:14.314916
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:31:22.858935
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typing import cast
    from ..utils.source import source_to_unicode
    from ..utils.helpers import ast_from_str
    from ..utils.tree import get_node_name, check_equal_ast

    code = source_to_unicode('''
        class A(object):
            def __init__(self):
                super()
    ''')

    expected_code = source_to_unicode('''
        class A(object):
            def __init__(self):
                super(A, self)
    ''')

    tree = ast_from_str(code)
    super_call_node = cast(ast.Call, tree.body[0].body[0].value)
    super_name_node = cast(ast.Name, super_call_node.func)
    assert get_

# Generated at 2022-06-14 02:31:34.402524
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Cls(BaseNodeTransformer):
        @staticmethod
        def get_ast_nodes(filename: str, function: str='test_SuperWithoutArgumentsTransformer') -> List[ast.AST]:
            module = ast.parse(inspect.getsource(test_SuperWithoutArgumentsTransformer))
            for node in module.body:
                if isinstance(node, ast.FunctionDef) and function == node.name:
                    return node.body
            raise Exception('Node not found')

    node_list = Cls.get_ast_nodes(__file__)

    for node in node_list:
        if isinstance(node, ast.Expr):
            def test_super():
                super()

            assert_equal(Cls(test_super).tree, node)
            break

# Generated at 2022-06-14 02:31:37.808144
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A:
        def foo():
            pass
    """
    # FIXME: typed_ast is broken and prevents proper testing of this
    # transformer
    pass

# Generated at 2022-06-14 02:31:42.779041
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseNodeTransformerTest
    import textwrap
    class Test(BaseNodeTransformerTest):
        target_tree = ast.parse(textwrap.dedent('''
        class A:
            def __init__(self):
                super()

        class B:
            def __init__(self, a, b):
                super()
        '''))
        transform = SuperWithoutArgumentsTransformer

    t = Test()
    t.test()

# Generated at 2022-06-14 02:31:46.347848
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.helpers import assert_equal_ignore_ws

# Generated at 2022-06-14 02:31:48.927982
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    
    import ast as python_ast
    import astunparse


# Generated at 2022-06-14 02:31:51.467503
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import Source
    from ..utils.validate import validate

# Generated at 2022-06-14 02:32:08.896924
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:11.431440
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer().__class__.__name__ == "SuperWithoutArgumentsTransformer"


# Generated at 2022-06-14 02:32:20.130541
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.helpers import get_ast_node_at
    from ..tests.test_case import BaseTestCase
    from ..visitor.type_inference import TypeInfererVisitor

    class Test(BaseTestCase):
        CODE = '''
        class C:
            def m(self):
                super()
        '''
        AST = get_ast_node_at(Test.CODE, line=3, column=21)
        TRANSFORMER = SuperWithoutArgumentsTransformer()

    asser

# Generated at 2022-06-14 02:32:30.922015
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer.target == (2, 7)

    from .test_helpers import parse

    tree = parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert str(tree) == '(Module (Expr (Call (Name (id super)) [Name (id BaseClass), Name (id self)])))'

    tree = parse('super(instance=obj)')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert str(tree) == '(Module (Expr (Call (Name (id super)) (Keyword (arg instance) (Name (id obj))) [Name (id BaseClass), Name (id self)])))'

    tree = parse('super(arg1, arg2)')
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:32:36.677994
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')

    # Setup
    cls = SuperWithoutArgumentsTransformer()

    # Exercise
    cls.visit(tree)

    # Verify
    assert tree.body[0].value.args[0].id == 'Cls'
    assert tree.body[0].value.args[1].id == 'self'


# Generated at 2022-06-14 02:32:41.933512
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    code = '''
        class Cls:
            def __init__(self):
                super()'''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    expected = '''
        class Cls:
            def __init__(self):
                super(Cls, self)'''
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:32:44.074074
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import parse
    from .. import dump

# Generated at 2022-06-14 02:32:48.957283
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.test_utils import should_transform

    source = '''
    super()
    '''

    expected = '''
    super(Cls, self)
    '''

    should_transform(SuperWithoutArgumentsTransformer, source, expected, __file__)
    
    

# Generated at 2022-06-14 02:33:00.325628
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast, source_to_code
    from ..pgen2 import token
    import ast as ast_module
    class_ = source_to_ast("class A(): def __init__(self): super().__init__()").body[0]
    changed = False
    x = SuperWithoutArgumentsTransformer(None, None, token, ast_module)
    new_node = x.visit(class_)
    assert new_node.body[0].body[0].value.args[0].id == "A"
    assert new_node.body[0].body[0].value.args[1].id == "self"
    assert source_to_code(new_node) == "class A(): def __init__(self): super(A, self).__init__()"

# Generated at 2022-06-14 02:33:05.783751
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    test_input = """
super().foo()
"""
    expected_output = """
super(Cls, self).foo()
"""
    transformer = SuperWithoutArgumentsTransformer()
    tree = parse_ast(test_input)
    transformer.visit(tree)

    expected_tree = parse_ast(expected_output)
    assert_ast_equals(tree, expected_tree)



# Generated at 2022-06-14 02:33:26.414181
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import run_local_tests

    class Dummy(ast.AST):
        _fields = ('foo', 'bar')


# Generated at 2022-06-14 02:33:30.354686
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class C:
            def m(self):
                super()
    """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    expected = """
        class C:
            def m(self):
                super(C, self)
    """

    assert astor.to_source(tree).strip('\n') == expected.strip('\n')

# Generated at 2022-06-14 02:33:41.676946
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class A:
            def __init__(self):
                super()

        class B:
            def method(self):
                super()

        class C:
            @staticmethod
            def static_method(a):
                super()

            @classmethod
            def class_method(cls):
                super()

        class D:
            def __init__(self):
                super([], [])

        class E:
            def __init__(self):
                super(A, [])

        class F:
            def __init__(self):
                super(A, self)

        class G:
            def __init__(self):
                super().__init__()
    '''

# Generated at 2022-06-14 02:33:44.773724
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    module = ast.parse("super()")
    SuperWithoutArgumentsTransformer().visit(module)
    expected = ast.parse("super(Cls, self)")
    assert ast.dump(module) == ast.dump(expected)

# Generated at 2022-06-14 02:33:46.094182
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:53.921734
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(node)
    assert ast.dump(node) == "Expr(value=Call(func=Attribute(value=Name(id='super', ctx=Load()), attr='__init__', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))"

# Generated at 2022-06-14 02:34:02.372114
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from ..utils.helpers import get_ast_node_class
    from ..utils.source import source_to_string
    from .base import BaseNodeTransformer
    from .base import GenericUnsupportedException
    from .base import GenericTransformerError

    node_transformer = SuperWithoutArgumentsTransformer(None)

    # test visit_Call

# Generated at 2022-06-14 02:34:06.500950
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class DummySuperWithoutArgumentsTransformer(SuperWithoutArgumentsTransformer):
        def __init__(self, tree, *args, **kwargs):
            self._tree = tree
            self._tree_changed = False


# Generated at 2022-06-14 02:34:16.742597
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .base import BaseNodeTransformer
    import unittest

    class Test(unittest.TestCase):
        maxDiff = None

        def test(self):
            source = source_to_unicode('''
            class A:
                def __init__(self):
                    super()
            ''')
            expected = source_to_unicode('''
            class A:
                def __init__(self):
                    super(A, self)
            ''')
            tree = ast.parse(source)
            tree = SuperWithoutArgumentsTransformer().visit(tree)
            result = BaseNodeTransformer._reconstruct_source(tree)
            self.assertEqual(result, expected)


# Generated at 2022-06-14 02:34:25.612633
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import astunparse

    code = """
    class C:
        def foo(self):
            super().foo()
    """
    expected_code = """
    class C:
        def foo(self):
            super(C, self).foo()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert(astunparse.unparse(tree) == expected_code) # type: ignore

# Generated at 2022-06-14 02:34:58.411502
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("super()")
    SuperWithoutArgumentsTransformer(node).generic_visit(node)
    assert(astunparse.unparse(node) == "super(Cls, self)")

# Generated at 2022-06-14 02:35:04.984971
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import parse
    module = parse('''class Cls:
        def __init__(self):
            super()
    ''')
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(module)
    assert transformer.is_changed
    assert str(module) == '''class Cls:
        def __init__(self):
            super(Cls, self)
    '''

# Generated at 2022-06-14 02:35:15.557075
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_ast
    from .demo_transformer import DemoTransformer
    transformer = DemoTransformer()
    transformer.add_transformer(SuperWithoutArgumentsTransformer)

    assert source_to_ast(transformer.visit, 'super()').body[0].value == ast.Call(
        func=ast.Attribute(
            value=ast.Name(id='super'),
            attr='__init__',
            ctx=ast.Load()
        ),
        args=[
            ast.Name(id='MyClass'),
            ast.Name(id='self')
        ],
        keywords=[],
        starargs=None,
        kwargs=None
    )

# Generated at 2022-06-14 02:35:25.953149
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    old_code = """
    class Foo:
        def foo(self):
            super()

        def bar(cls):
            super()
    """

    new_code = """
    class Foo:
        def foo(self):
            super(Foo, self)

        def bar(cls):
            super(Foo, cls)
    """

    transformer = SuperWithoutArgumentsTransformer()
    result = transformer.visit(ast.parse(old_code))
    assert_equivalent_code(result, new_code)



# Generated at 2022-06-14 02:35:28.193787
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    code = '''
            class Test():
                def method(self):
                    super()
    '''
    tree = ast.parse(code)

# Generated at 2022-06-14 02:35:29.318764
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astunparse
    import astor

# Generated at 2022-06-14 02:35:32.002039
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import parse

    class DummyTree:
        def __init__(self, tree):
            self._tree = tree


# Generated at 2022-06-14 02:35:32.585403
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:34.721583
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import as_tuple

# Generated at 2022-06-14 02:35:42.035156
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class SuperWithoutArgumentsTransformer_Test():
        def __func__(self):     
            super()

        def __init__(self):
            pass
    
    class_ = SuperWithoutArgumentsTransformer_Test
    tree = parser.ast_parse(inspect.getsource(class_))  # type: ast.AST

    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert (tree.body[0].body[0].value.args[0].id == 'SuperWithoutArgumentsTransformer_Test')
    assert (tree.body[0].body[0].value.args[1].id == 'self')

# Generated at 2022-06-14 02:36:21.650798
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
            class Foo:
                def __init__(self):
                    super()
                    super.__init__() # not affected
            """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    node = tree.body[0].body[0].body[1]
    assert node.func.value.args[0].id == 'Foo'
    assert node.func.value.args[1].id == 'self'

# Generated at 2022-06-14 02:36:24.153727
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.tree import print_tree
    from ..parser.parser import PythonParser
    from ..parser.ast_utils import parse_node


# Generated at 2022-06-14 02:36:34.228324
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    # super() -> super(ClassName, self)
    def test_case1():
        source = '''
        class A:
            def __init__(self):
                super().__init__()
        '''
        expected = '''
        class A:
            def __init__(self):
                super(A, self).__init__()
        '''
        tree = ast.parse(source)
        tree = SuperWithoutArgumentsTransformer(tree).visit(tree)

        assert ast.dump(tree) == expected

    # super() -> super(ClassName, cls)
    def test_case2():
        source = '''
        class A:
            @classmethod
            def create(cls):
                super().create()
        '''

# Generated at 2022-06-14 02:36:38.206999
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    x = ast.parse("super()")
    y = x.body[0]
    z = SuperWithoutArgumentsTransformer().visit(y)
    assert z.args[0].id == "Cls"
    assert z.args[1].id == "self"

# Generated at 2022-06-14 02:36:39.979249
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:47.078833
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Test:
            def __init__(self):
                super()
    """
    module = ast.parse(code)  # type: ignore
    SuperWithoutArgumentsTransformer().visit(module)
    expected_result = """
        class Test:
            def __init__(self):
                super(Test, self)
    """
    result = astunparse.unparse(module).strip()
    assert result == expected_result

# Generated at 2022-06-14 02:36:48.426224
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:49.741974
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer"""

# Generated at 2022-06-14 02:36:57.854236
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[]))])"

# Generated at 2022-06-14 02:36:59.515551
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import cStringIO
    import astor