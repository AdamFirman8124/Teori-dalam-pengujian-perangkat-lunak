

# Generated at 2022-06-14 02:28:07.264665
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseNodeTransformer
    from typed_ast import ast3 as ast
    from .. import tree
    from ..utils.source import source_to_unicode
    from collections import namedtuple

    Source = namedtuple('Source', ['code', 'tree'])

# Generated at 2022-06-14 02:28:14.623114
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A:
            def __init__(self, a):
                super().__init__(a)
        """
    expected_code = """
        class A:
            def __init__(self, a):
                super(A, self).__init__(a)
    """
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert expected_code == astor.to_source(tree)



# Generated at 2022-06-14 02:28:16.794644
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_without_args_transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:28:22.598483
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class SuperTest(object):
        def __init__(self):
            super()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

    new_code = compile(tree, '<test>', 'exec')
    exec(new_code)



# Generated at 2022-06-14 02:28:25.771679
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    tree = ast3.parse('super()')
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    print(ast3.dump(tree))

# Generated at 2022-06-14 02:28:27.562041
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # Given
    from .. import compile as compile
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:28:35.522072
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..tests.fixtures.tree import Call
    from ..tests.fixtures.tree import FunctionDef
    from ..tests.fixtures.tree import ClassDef

    code = '''
super()
'''

    expected_code = '''
super(cls, self)
'''

    class TestSuperWithoutArgumentsTransformer(SuperWithoutArgumentsTransformer):
        def __init__(self):
            self.tree = Call()

    transformer = TestSuperWithoutArgumentsTransformer()
    transformer.generic_visit = lambda x: x
    node = transformer.visit(transformer.tree)

    assert ast.dump(node) == expected_code

# Generated at 2022-06-14 02:28:36.470867
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:46.223804
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    
    class SuperWithoutArgumentsTransformer_(SuperWithoutArgumentsTransformer):
        tree = None
        _tree_changed = False
    transformer = SuperWithoutArgumentsTransformer_()

    def run_test(test_name, code, expected_tree, expected_tree_changed):
        t = ast.parse(code)
        SuperWithoutArgumentsTransformer_.tree = t
        SuperWithoutArgumentsTransformer_._tree_changed = False
        transformer.visit(t)
        if ast.dump(t) != ast.dump(expected_tree):
            print('----- {} failed'.format(test_name))
            print('expected')
            print(ast.dump(expected_tree))
            print('actual')
            print(ast.dump(t))
            assert False

# Generated at 2022-06-14 02:28:49.465191
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        x = super()
    """

    tree = ast.parse(code)  # type: ignore
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree).strip() == """
        x = super(Cls, self)
    """.strip()

# Generated at 2022-06-14 02:29:01.667438
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import inspect
    import textwrap
    from splark.compiler import PreprocessorVisitor

    source = inspect.cleandoc(textwrap.dedent(
        """
        class A(B):
            def __init__(self):
                super()
        """
    ))

    tree = ast.parse(source)
    tree = PreprocessorVisitor().visit(tree)
    tree = SuperWithoutArgumentsTransformer().visit(tree)

    expected = inspect.cleandoc(textwrap.dedent(
        """
        class A(B):
            def __init__(self):
                super(A, self)
        """
    ))
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:29:04.347068
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)

    assert_code(transformer.result(), 'super(NoneType, self)')



# Generated at 2022-06-14 02:29:14.542642
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    program_ast = ast.parse("""
    class A(object):
        def f(self):
            super()
    
    class B(object):
        def f(cls):
            super()
        """)

    expected_program_ast = ast.parse("""
    class A(object):
        def f(self):
            super(A, self)
    
    class B(object):
        def f(cls):
            super(B, cls)
        """)

    t = SuperWithoutArgumentsTransformer()
    new_ast = t.visit(program_ast)
    compare_ast(new_ast, expected_program_ast)

# Generated at 2022-06-14 02:29:17.339220
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast_helper import ast_to_code
    from ..threetofive import ThreeToFive
    import ast
    import sys


# Generated at 2022-06-14 02:29:21.524001
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit tests for the constructor of the class SuperWithoutArgumentsTransformer."""

    # Test the class SuperWithoutArgumentsTransformer
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer()
    assert super_without_arguments_transformer is not None

# Generated at 2022-06-14 02:29:25.754610
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(None)

    assert isinstance(transformer, BaseNodeTransformer)
    assert not transformer.tree_changed
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:29:26.642446
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:27.875060
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:28.565182
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:29.746492
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:36.038144
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:44.935871
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ast_helper import ast_from_code
    from ..utils.helpers import bytecode_equal
    code = '''
        class Parent:
            def __init__(self, x):
                super().__init__()
    '''
    tree = ast_from_code(code)
    expected_code = '''
        class Parent:
            def __init__(self, x):
                super(Parent, self).__init__()
    '''
    tree2 = ast_from_code(expected_code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    bytecode_equal(tree, tree2)



# Generated at 2022-06-14 02:29:45.661066
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:46.402754
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:29:50.563294
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = parse("super()", "<ast>", "exec")
    node = tree.body[0]

    assert node.__class__.__name__ == "Call"
    SuperWithoutArgumentsTransformer(tree).visit(node)



# Generated at 2022-06-14 02:29:59.745409
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typing import cast
    module: ast.Module = parse('super()')
    func: ast.FunctionDef = cast(ast.FunctionDef, module.body[0])
    node: ast.Expr = cast(ast.Expr, func.body[0])
    assert isinstance(node.value, ast.Call)
    node = cast(ast.Call, node.value)
    assert isinstance(node.func, ast.Name)
    assert node.func.id == 'super'
    assert len(node.args) == 0
    assert len(node.keywords) == 0

    transformer = SuperWithoutArgumentsTransformer(None)
    transformer.visit_Call(node)
    assert len(node.args) == 2
    assert isinstance(node.args[0], ast.Name)

# Generated at 2022-06-14 02:30:00.476789
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:30:06.601314
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode as u
    from ..utils.source import source_to_ast as parse
    from ..utils.helpers import is_equal_ast
    code = u('''
    class Cls():
        def __init__(self, val):
            self._val = val

        def somefunc(self):
            pass

        def someotherfunc(self):
            print(super())

    class SubCls(Cls):
        def __init__(self, val):
            super()
            self._val = val

        def somefunc(self):
            super().somefunc()
    ''')

# Generated at 2022-06-14 02:30:10.246738
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = "super()"
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, '', 'exec'))

if __name__ == '__main__':
    test_SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:30:20.345774
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class TestTransformer(BaseNodeTransformer):
        target = (2, 7)

        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                self._replace_super_args(node)
                self._tree_changed = True

            return self.generic_visit(node)  # type: ignore

        def _replace_super_args(self, node: ast.Call) -> None:
            try:
                func = get_closest_parent_of(self._tree, node, ast.FunctionDef)
            except NodeNotFound:
                warn('super() outside of function')
                return


# Generated at 2022-06-14 02:30:34.525573
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    assert isinstance(transformer._replace_super_args, types.MethodType)

    assert len(transformer._replace_super_args.__closure__) == len(transformer.__class__.__dict__['__init__'].__closure__)
    assert all(x is y for x, y in zip(transformer._replace_super_args.__closure__, transformer.__class__.__dict__['__init__'].__closure__))

    assert len(transformer.visit_Call.__closure__) == len(transformer._replace_super_args.__closure__)
    assert all(x is y for x, y in zip(transformer.visit_Call.__closure__, transformer._replace_super_args.__closure__))


transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:30:41.676115
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class A:
        def m(self):
            super()
            super().m()
    '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    mod = compile(tree, '', 'exec')
    ns = {}
    exec(mod, ns)
    assert ns['A'].m.__code__.co_code == b'd\x00S\x00d\x01\x85\x02\x02\x83\x02\x02}\x01\x01\x84\x02\x01\x01'
    assert ns['A'].m.__code__.co_varnames == (
        'self',
        'A',
        'self',
        'A',
    )

# Generated at 2022-06-14 02:30:54.541260
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..utils.testing import get_node_as_string

    obj = Source("super().hello()", path='test.py')
    wrapper = SuperWithoutArgumentsTransformer()
    wrapper.visit(obj.tree)
    new_node = get_node_as_string(wrapper.new_tree)
    expected_node = "super(Calculate, self).hello()"
    assert new_node == expected_node
    wrapper = SuperWithoutArgumentsTransformer()
    source = Source("super().hello()", path='test.py')
    wrapper.visit(source.tree)
    new_node = get_node_as_string(wrapper.new_tree)
    expected_node = "super(Calculate, self).hello()"
    assert new_node == expected_node

# Generated at 2022-06-14 02:31:01.286161
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import textwrap
    import astor

    tree = astor.parse_file(textwrap.dedent("""
        class A(object):
            def m(self):
                super().__init__()
    """))
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    print(astor.to_source(tree))



# Generated at 2022-06-14 02:31:02.178695
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:08.638950
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.dump import dump_python_ast
    from ..utils.tree import parse_ast_tree

    code = '''
    class A(object):
        def __init__(self):
            super().__init__()
    '''
    tree = parse_ast_tree(code)
    target_node = 'super(__class__.__name__, self)'
    SuperWithoutArgumentsTransformer().visit(tree)
    result = dump_python_ast(tree)
    assert target_node in result

# Generated at 2022-06-14 02:31:19.355178
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("""
        class Derived(Base):
            def __init__(self, value):
                super().__init__()
        """)

    transformer = SuperWithoutArgumentsTransformer(tree, None)
    transformer.run()

    method = tree.body[0].body[0]
    expected = """
    class Derived(Base):
        def __init__(self, value):
            super(Derived, self).__init__()
    """
    assert method.body[1].args[0].id == 'self'
    assert method.body[1].args[1].id == 'Derived'
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:31:20.119944
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:31:28.985240
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast as sta
    from ..transformers.ast_transformer import AstTransformer
    from ..transformers.parent_node_transformer import ParentNodeTransformer
    class Foo(AstTransformer):
        transformers = [
            ParentNodeTransformer,
            SuperWithoutArgumentsTransformer,
        ]
    print(Foo.transform(sta('''
        class A:
            def f(self):
                super()
        ''')))
    print(Foo.transform(sta('''
        class A:
            def f(self):
                pass
        ''')))

# Generated at 2022-06-14 02:31:33.520156
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import astunparse

    class ExampleVisitor(ast.NodeVisitor):  # type: ignore
        def visit_Call(self, node):
            print(f'Hi, I\'m visiting a FunctionDef node')

    class ExampleTransformer(ast.NodeTransformer):  # type: ignore
        def visit_Call(self, node):
            return ast.Name(id="Hi")


# Generated at 2022-06-14 02:31:43.292274
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode


# Generated at 2022-06-14 02:31:58.304879
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from nuitka.ast.tree import build_module_tree
    from nuitka.ast.tree import build_tree
    from nuitka.ast.tree import build_tree
    from nuitka.ast.Building import buildStatementsNode
    from .test_transformer_helpers import build_call_node

    content = """
    class MyClass(SuperClass):
        def __init__(self):
            super()
    """

    tree = build_module_tree(content)
    func_def_nodes = tree.getVisitableNodes()
    assert len(func_def_nodes) == 1
    func_def_node0 = func_def_nodes[0]

    node0 = func_def_node0.body[0]
    node1 = func_def_node0.body[1]


# Generated at 2022-06-14 02:32:07.934382
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..parser import Parser
    import os
    from .base import BaseNodeTransformer
    from .base import BaseErrorHandler
    from ..utils.helpers import create_module
    from ..utils.helpers import create_function
    from ..utils.helpers import create_class
    from ..utils.helpers import create_super_call
    from ..utils.helpers import create_import
    from ..utils.helpers import create_assignment
    from ..utils.helpers import create_print

    parser = Parser()

    # Create a module

# Generated at 2022-06-14 02:32:19.495418
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .base import NodeTransformer

    transformer = NodeTransformer(target=(2, 7))

    class NodeTransformerForTest(NodeTransformer):  # type: ignore
        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                self._replace_super_args(node)
                self._tree_changed = True

            return self.generic_visit(node)

    class AST:
        pass

    def compile_tree(x_tree: AST) -> AST:
        pass

    class Tree:
        pass

    tree = Tree()

    setattr(tree, '_tree', tree)

# Generated at 2022-06-14 02:32:29.422576
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Test for method visit_Call of class SuperWithoutArgumentsTransformer"""
    from typed_ast import ast3 as ast
    from ..utils import tree
    from ..compiler.main import _compile
    from ..exceptions import CompilerError
    from ..program import Program
    import logging

    logger = logging.getLogger("SuperWithoutArgumentsTransformer_visit_Call_test")
    logger.setLevel(logging.DEBUG)

    program = Program(logger=logger)

# Generated at 2022-06-14 02:32:40.759106
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    from ast import parse as parse3

    from .base import BaseNodeTransformerTestCase

    class SuperWithoutArgumentsTransformerTestCase(BaseNodeTransformerTestCase):
        transformer_type = SuperWithoutArgumentsTransformer

        def test_super_inside_function(self):
            tree = parse3('''
            class A:
                def __init__(self):
                    super()
            ''')
            self.check_tree('''
            class A:
                def __init__(self):
                    super(A, self)
            ''')

        def test_super_inside_class(self):
            tree = parse3('''
            class A:
                def __init__(self):
                    super()
            ''')

# Generated at 2022-06-14 02:32:51.519119
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A:
        def __init__(self):
            super()
        def func(self, arg1):
            super()
    def func(arg1):
        super()
    super()
    """
    result = """
    class A:
        def __init__(self):
            super(A, self)
        def func(self, arg1):
            super(A, self)
    def func(arg1):
        super(A, self)
    super()
    """
    t = SuperWithoutArgumentsTransformer()
    t.visit(ast.parse(code))
    assert ast.dump(ast.parse(result)) == ast.dump(t.tree)

# Generated at 2022-06-14 02:32:58.563086
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class SUT(SuperWithoutArgumentsTransformer):
        def _get_tree(self) -> ast.Module:
            body = [ast.Expr(value=ast.Call(func=ast.Name(id='super'), args=[], keywords=[]))]
            return ast.Module(body=body)

    sut = SUT()
    name = sut.visit(sut.tree)
    assert isinstance(name, ast.Name)
    assert name.id == 'super'


# Generated at 2022-06-14 02:33:03.477690
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_setup import setup_test_file
    from ..utils import tree

    tree = setup_test_file("""
    class Foo:
        def bar(self):
            super()
    """)

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    code = tree.code


# Generated at 2022-06-14 02:33:04.703940
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing.code_generation import code_gen
    from . import fix_missing_locations, parse


# Generated at 2022-06-14 02:33:21.400694
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:33:25.672174
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    tree = ast.parse('class foo:\n  def __init__(self):\n    super()')
    transformer.visit(tree)
    assert 'super(foo, self)' in astor.to_source(tree)

# Generated at 2022-06-14 02:33:30.398355
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A():
        def __init__(self):
            super()
    """

    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    expected_code = """
    class A():
        def __init__(self):
            super(A, self)
    """

    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))

test_SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:33:36.705368
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class FooBar:
        def __init__(self):
            self.x = 1
    """
    node = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(node)
    new_code = compile(node, '', 'exec')

    globals_ = {}
    exec(new_code, globals_)
    cls = globals_['FooBar']
    cls()

# Generated at 2022-06-14 02:33:44.394070
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # Setup
    tree = ast.parse('''class A:
    def m1(self):
        super()
    def m2(self):
        raise NotImplementedError
''')
    expected_tree = ast.parse('''class A:
    def m1(self):
        super(A, self)
    def m2(self):
        raise NotImplementedError
''')
    transformer = SuperWithoutArgumentsTransformer(tree, {})

    # Run
    transformer.run()

    # Assert
    assert ast.dump(tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:33:46.460142
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:33:55.380580
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:01.126835
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_code = """
    class Base():
        def __init__(self):
            super()
    """
    expected_code = """
    class Base():
        def __init__(self):
            super(Base, self)
    """
    uut = SuperWithoutArgumentsTransformer()
    uut.visit(ast.parse(input_code))
    assert expected_code == astor.to_source(uut.tree)



# Generated at 2022-06-14 02:34:06.387953
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse('super()', '<string>', 'exec')
    SuperWithoutArgumentsTransformer().visit(node)
    expected = ast.parse('super(Cls, cls)', '<string>', 'exec')
    assert ast.dump(node) == ast.dump(expected)



# Generated at 2022-06-14 02:34:12.022467
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Test SuperWithoutArgumentsTransformer.visit_Call."""
    from typed_ast import parse
    from ..utils.context import Context
    node = parse("super()").body[0]
    SuperWithoutArgumentsTransformer(
        tree=None,
        filename=None,
        context=Context()
    ).visit_Call(node)
    assert str(node) == 'super(Cls, self)'

# Generated at 2022-06-14 02:34:49.571838
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    statement = 'class A: def f(a): print(super().__class__)'

    tree = ast.parse(statement)
    transf = SuperWithoutArgumentsTransformer()
    transf.visit(tree)

    assert astor.to_source(tree) == 'class A:\n    def f(a):\n        print(super(A, a).__class__)\n'

# Generated at 2022-06-14 02:34:57.990012
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    generated_code = compile(tree, '', 'exec')
    test_env = {}
    exec(generated_code, test_env)
    assert True

code = '''class Test(object):
    def __init__(self):
        super()
'''
transformed_code = '''class Test(object):
    def __init__(self):
        super(Test, self)
'''


# Generated at 2022-06-14 02:35:03.272708
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    node = tree.body[0].value
    transformer = SuperWithoutArgumentsTransformer({}, tree)
    transformer.visit(node)
    print(astunparse.unparse(tree))

# Generated at 2022-06-14 02:35:10.650514
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer."""
    tree = ast.parse('''class A():
        def __init__(self):
            super(A, self).__init__()
        def pass_():
            pass''')
    tree.body[0].body[0].value.args[0].args[1].id = 'self'

    node = tree.body[0].body[0].value
    assert isinstance(node, ast.Call)
    assert isinstance(node.args[0], ast.Name)
    assert isinstance(node.args[1], ast.Name)
    assert node.args[0].id == 'A'
    assert node.args[1].id == 'self'
    assert node.func.id == 'super'


# Generated at 2022-06-14 02:35:16.072292
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = "super()"
    expected_transform_code = "super(Cls, self)"

    _, new_tree = SuperWithoutArgumentsTransformer.run_it(code, as_tree=True)
    transformed_code = astor.to_source(new_tree)

    assert expected_transform_code == transformed_code


# Generated at 2022-06-14 02:35:22.307920
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
        class Cls:
            def func(self):
                super()
                super()
            
        def func():
            super()
        """

    expected_result = """
        class Cls:
            def func(self):
                super(Cls, self)
                super(Cls, self)
            
        def func():
            super()
        """

    assert_source_transformation(SuperWithoutArgumentsTransformer, source, expected_result)

# Generated at 2022-06-14 02:35:29.018297
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_restricted, restrict
    from ast import parse
    #Restrict to basic python features
    restrict(
        compile_restricted(
            #Example 1. Super without arguments inside class and method
            parse('''
            class C:
                def f(self):
                    a = super()

            '''),
            __name__ + '.test_SuperWithoutArgumentsTransformer_visit_Call'
        ),
        __name__ + '.test_SuperWithoutArgumentsTransformer_visit_Call'
    )

# Generated at 2022-06-14 02:35:33.531333
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
# Python 3 code
super()
"""
    expect = """
# Python 3 code
super(Cls, self)
"""
    tree = ast.parse(source)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert expect == astor.to_source(tree)


# Generated at 2022-06-14 02:35:35.115234
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typing import List


# Generated at 2022-06-14 02:35:43.017616
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import Compiler
    from ..utils.helpers import captured_output
    from ..utils.helpers import ast_to_src
    from pathlib import Path
    import tempfile

    with tempfile.NamedTemporaryFile('r+') as tmpfile:
        content = """
        class Test:
            def __init__(self, x):
                self.x = x
                super().__setattr__('x', self.x)
        """
        tmpfile.write(content)
        tmpfile.flush()
        tmpfile.seek(0)
        
        compiler = Compiler(source_path=tmpfile.name)
        compiler.compile()


# Generated at 2022-06-14 02:37:04.592458
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    s = ast.parse("""
    class Test:
        def test(self):
            super()""")

    t = ast.parse("""
    class Test:
        def test(self):
            super(Test, self)""")

    tt = ast.parse("""
    class Test:
        def test(self):
            super(Test, cls)""")

    u = ast.parse("""
    class Test:
        def test(cls):
            super()""")

    uu = ast.parse("""
    class Test:
        def test(cls):
            super(Test, cls)""")

    #super()
    func = s.body[0].body[0]
    SuperWithoutArgumentsTransformer(s).visit(func)

# Generated at 2022-06-14 02:37:06.764315
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:37:07.284135
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:15.041462
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from ..utils.helpers import get_node_text
    node = ast3.parse("class A(object):\n\tdef __init__(self):\n\t\tsuper()")
    trans = SuperWithoutArgumentsTransformer()
    trans.visit(node)
    node_patch = ast3.parse(trans.get_patch())
    anode = ast3.parse("class A(object):\n\tdef __init__(self):\n\t\tsuper(A, self)")
    assert get_node_text(node_patch) == get_node_text(anode)

# Generated at 2022-06-14 02:37:18.764963
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    a = SuperWithoutArgumentsTransformer(None)

    a._replace_super_args(ast.parse('super()').body[0].value)
    assert ast.dump(ast.parse('super(__class__, self)')) == ast.dump(ast.parse('super(__class__, self)'))

# End of test

# Generated at 2022-06-14 02:37:23.006891
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..common import tokenize
    from ..common import parse
    from ..transform import TreeTransformer
    tt = TreeTransformer()
    tt.register_transformer(SuperWithoutArgumentsTransformer)

# Generated at 2022-06-14 02:37:29.125668
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    example = """
    class C:
        def f(self):
            super()
            
    """
    expected = """
    class C:
        def f(self):
            super(C, self)
            
    """
    tree = ast.parse(example)  # type: ignore
    expected_tree = ast.parse(expected)  # type: ignore
    transformer = SuperWithoutArgumentsTransformer()
    result = transformer.visit(tree)  # type: ignore
    assert result == expected_tree



# Generated at 2022-06-14 02:37:35.257836
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast.ast3 import parse, dump
    from .base import BaseNodeTransformer
    code = "super()"
    tree = parse(code)
    node = tree.body[0].value
    assert(isinstance(node,ast.Call))
    transformer = BaseNodeTransformer()
    transformer.visit(tree)
    dump(tree)
    assert(isinstance(node,ast.Call) )

# Generated at 2022-06-14 02:37:37.460722
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super()"""
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, filename="", mode="exec"))

# Generated at 2022-06-14 02:37:40.916748
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super()"""
    expected = """super(Cls, self)"""
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert expected == codegen.to_source(tree)

