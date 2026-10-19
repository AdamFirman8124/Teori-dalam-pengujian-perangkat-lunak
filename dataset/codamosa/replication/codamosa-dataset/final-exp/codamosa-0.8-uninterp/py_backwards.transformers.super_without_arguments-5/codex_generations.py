

# Generated at 2022-06-14 02:28:02.199784
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super()"""
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, '', 'exec'))

# Generated at 2022-06-14 02:28:13.053636
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test for super() class for specific args of arguments
    """
    from ..utils.source import source_to_ast

    class TestClass(SuperWithoutArgumentsTransformer):
        def __init__(self):
            self.test_function(source_to_ast('super()'))
            self.test_function(source_to_ast('super()'), 'test', 'cls')

        def test_function(self, value: ast.AST, func: str = 'function', cls: str = 'class') -> None:
            self._tree = value
            self.visit(value)
            answer = ast.parse(f'super({cls}, {func})')
            if hasattr(self, '_tree'):
                assert ast.dump(self._tree) == ast.dump(answer)

# Generated at 2022-06-14 02:28:20.131132
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():

    code = """
        class A:
            def m1(self):
                super()
    """
    expected_code = """
        class A:
            def m1(self):
                super(A, self)
    """
    tree = ast.parse(dedent(code))
    SuperWithoutArgumentsTransformer(tree).run()
    assert astor.to_source(tree) == dedent(expected_code)



# Generated at 2022-06-14 02:28:22.043277
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:32.465741
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # super()
    node = ast.parse("super()")
    node = SuperWithoutArgumentsTransformer().visit(node)
    assert isinstance(node.body[0].value, ast.Call)
    assert isinstance(node.body[0].value.func, ast.Name)
    assert node.body[0].value.func.id == 'super'
    assert len(node.body[0].value.args) == 2
    assert isinstance(node.body[0].value.args[0], ast.Name)
    assert node.body[0].value.args[0].id == 'Cls'
    assert isinstance(node.body[0].value.args[1], ast.Name)
    assert node.body[0].value.args[1].id == 'cls'

    # super().__init__(

# Generated at 2022-06-14 02:28:40.619788
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .example_code import SUPER_WITHOUT_ARGUMENTS_TRANSPILED_METHOD
    tree = ast.parse(SUPER_WITHOUT_ARGUMENTS_TRANSPILED_METHOD)
    node = tree.body[1]
    expected_result = ast.parse(SUPER_WITHOUT_ARGUMENTS_TRANSPILED_METHOD)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(node)
    assert expected_result.body[1] == node

# Generated at 2022-06-14 02:28:52.882215
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    class D(ast.NodeTransformer):
        pass

    class C(D):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            # pylint: disable=E0102
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                self._replace_super_args(node)
                self._tree_changed = True

            return self.generic_visit(node)  # type: ignore

# Generated at 2022-06-14 02:28:53.357660
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:55.557701
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:05.555314
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    node1 = ast.parse("super()")
    node2 = ast.parse("super(1)")
    node3 = ast.parse("super(self)")
    node4 = ast.parse("super(cls)")
    node5 = ast.parse("super(other)")
    node6 = ast.parse("super(first, second)")
    node7 = ast.parse("''' first comment '''\nsuper()\n''' second comment '''\n")
    node8 = ast.parse("''' first comment '''\nsuper(1)\n''' second comment '''\n")
    node9 = ast.parse("''' first comment '''\nsuper()\n''' second comment '''\n")

# Generated at 2022-06-14 02:29:10.590087
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..common import make_function_def
    from ..exceptions import NotCompilableError

# Generated at 2022-06-14 02:29:21.428071
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    #given
    from typed_ast import ast3
    from ..compat import NamedExpr

    tree = ast3.parse('super()')
    tree.body[0] = NamedExpr(id='foo', value=tree.body[0].value)
    node = tree.body[0].value
    # def foo (): super()
    assert isinstance(node, ast3.Call)
    assert isinstance(node.func, ast3.Name)
    assert node.func.id == 'super'
    assert isinstance(node.args, list)
    assert len(node.args) == 0

    #when
    x = SuperWithoutArgumentsTransformer(tree, 'dummy.py')
    x.visit_Call(node)

    #then
    assert len(node.args) == 2

# Generated at 2022-06-14 02:29:26.181637
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    result = SuperWithoutArgumentsTransformer().visit(tree)

    assert result.body[0].value.args[0].id == 'Cls', 'super() should be replaced with super(Cls)'

# Generated at 2022-06-14 02:29:31.231376
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
                class Foo:
                    def __init__(self):
                        super()
                '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, filename="", mode="exec"))

test_SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:29:35.538200
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    tree = ast.parse('class A: def f(self): super()')
    tree2 = ast.parse('class A: def f(self): super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert tree != tree2

# Generated at 2022-06-14 02:29:45.979584
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    import textwrap

    code = textwrap.dedent("""
    class C(object):
        def __init__(self):
            super().__init__()
        def method(self):
            pass
    class Cls:
        def __init__(self):
            super().__init__()
        def method(self):
            pass
    """)

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().generic_visit(tree)
    invoke_super_methods = get_invoke_super_methods(tree)
    for node in invoke_super_methods:
        assert isinstance(node, ast.Call), f'Found {type(node)}'

# Generated at 2022-06-14 02:29:57.080510
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('class A: def foo(self): super()')
    transformer = SuperWithoutArgumentsTransformer(tree)
    new_tree = transformer.visit(tree)

# Generated at 2022-06-14 02:30:03.034440
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Tests that SuperWithoutArgumentsTransformer successfully compiles 
    `super()` to `super(cls, self)` and `super(self)` to `super(self)`
    """
    # Checks that target is a tuple
    assert isinstance(SuperWithoutArgumentsTransformer.target, tuple)

    code_dict = {
        'super()' : "super(cls, self)",
        'super(self)' : "super(self)"
    }

    for code, expected in code_dict.items():
        # Checks that code can be compiled
        assert compile(code, '', 'exec')

        # Checks that the NodeTransformer produces the expected code
        tree = ast.parse(code)
        node_transformer = SuperWithoutArgumentsTransformer(tree)
        assert node_transformer.result() == expected

# Generated at 2022-06-14 02:30:07.891953
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    inp = 'super()'
    expected_out = 'super(Cls, self)'
    tree = ast.parse(inp)
    transformer.visit(tree)
    assert (expected_out == astor.to_source(tree))

# Generated at 2022-06-14 02:30:14.134105
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = inspect.cleandoc('''
    class Test(object):
        def __init__(self):
            super().__init__()
    ''')
    expected = inspect.cleandoc('''
    class Test(object):
        def __init__(self):
            super(Test, self).__init__()
    ''')
    module = ast.parse(source)
    SuperWithoutArgumentsTransformer(module).visit(module)
    assert astor.to_source(module) == expected

# Generated at 2022-06-14 02:30:26.755484
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ast import parse
    from pickle import dumps, loads
    from copy import deepcopy

    from neuralpy.utils import alias_function
    from neuralpy.utils import CustomArgumentParser
    from neuralpy.transpilers.base import BaseTranspiler

    alias_function('Function', 'function')

    def compile_code(code: str) -> ast.Module:
        return loads(dumps(parse(code.strip())))

    sut = SuperWithoutArgumentsTransformer()

    class DummyTranspiler(BaseTranspiler):
        def __init__(self, tree: ast.AST, target: str) -> None:
            super().__init__(tree, CustomArgumentParser(), target)

        def visit_body(self, nodes: List[ast.AST]) -> List[ast.AST]:
            return nodes


# Generated at 2022-06-14 02:30:36.441688
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.testing import assert_equivalent_node
    from .node_test_factory import create_name_node, create_keyword_node, create_call_node, create_module

    def create_super_call():
        return create_call_node('super')

    def create_super_without_args_mod(with_call: bool = True):
        node = create_module([
            ast.Assign([create_name_node('arg')], create_name_node('arg')),
            ast.Assign([create_name_node('cls')], create_name_node('cls')),
        ])

        kwarg = create_keyword_node(arg='cls')

# Generated at 2022-06-14 02:30:38.078630
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:48.872012
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from refactorlib.parse import parse
    from refactorlib.refactor import get_transformer_classes
    from refactorlib.fix import print_diff

    source = dedent("""
        class C:
            def f(self):
                super()
            
        class D(object):
            def f(self):
                super()
            
        class E:
            def f(self):
                super()
            @classmethod
            def f2(cls):
                super()

    """)
    tree = parse(source)

    transformers = get_transformer_classes()
    for TransformerClass in transformers:
        transformer = TransformerClass()
        tree = transformer.visit(tree)
        if transformer.tree_changed:
            print(transformer)


# Generated at 2022-06-14 02:30:56.449493
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    node = ast.parse('super()').body[0]
    transformer = SuperWithoutArgumentsTransformer(node)
    node = transformer.visit(node)
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    args = node.value.args
    assert len(args) == 2
    assert isinstance(args[0], ast.Name)
    assert args[0].id == 'Cls'
    assert isinstance(args[1], ast.Name)
    assert args[1].id == 'self'
    assert transformer._tree_changed

# Generated at 2022-06-14 02:31:03.188325
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Testing constructor of class SuperWithoutArgumentsTransformer.
    """
    import sys
    from io import StringIO
    from .helpers import get_ast

    # Getting AST.
    ast = get_ast("super()")
    captcha_solver = SuperWithoutArgumentsTransformer(ast, sys.version_info)
    output = StringIO()
    captcha_solver.generic_visit(captcha_solver._tree)
    assert captcha_solver._tree is not None



# Generated at 2022-06-14 02:31:07.271435
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    expected = "super(Cls, self)"
    result = astor.to_source(tree)
    assert result == expected



# Generated at 2022-06-14 02:31:16.747994
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def test_func():
        super()
    def test():
        class Test:
            def test_method(self):
                super()
    source = inspect.getsource(test)
    tree = ast.parse(source)
    cls = get_class(tree, SuperWithoutArgumentsTransformer)
    assert cls is not None
    assert len(cls.body) == 1
    func = get_func(cls.body, 'test_method')
    assert func is not None
    assert len(func.body) == 1
    expr = func.body[0]
    assert isinstance(expr, ast.Expr)
    assert isinstance(expr.value, ast.Call)
    assert isinstance(expr.value.func, ast.Name)
    assert expr.value.func.id == 'super'
    assert len

# Generated at 2022-06-14 02:31:23.974453
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("super()")
    super_trans = SuperWithoutArgumentsTransformer(tree)
    super_trans.visit()
    assert ast.dump(tree) == 'Module(body=[Expr(value=Call(func=Name(id=\'super\', ctx=Load()), args=[Name(id=\'Cls\', ctx=Load()), Name(id=\'self\', ctx=Load())], keywords=[]))])'
    return "test passed"

# Generated at 2022-06-14 02:31:24.557448
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import compile_source

# Generated at 2022-06-14 02:31:32.335152
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """something = super()"""
    expected_code = """something = super(C, self)"""
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert astor.to_source(tree).strip() == expected_code

# Generated at 2022-06-14 02:31:39.143759
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == "Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))"

# Generated at 2022-06-14 02:31:51.358275
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import ast as pyast
    from typing import List
    from typed_ast import ast3

    # для assert'ов
    # pylint:disable=unidiomatic-typecheck

    # для дебажинга
    # pylint:disable=redefined-outer-name

    def _build_tree(code):
        return pyast.parse(code, '<unknown>', 'exec').body[0]

    def _build_module(body):
        return pyast.Module(
            body=body
        )


# Generated at 2022-06-14 02:31:52.146726
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:55.589602
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..tests.utils import transform_and_compile
    class A(object):
        def __init__(self):
            super().__init__()
    @transform_and_compile
    class B(object):
        def __init__(self):
            super().__init__()
    assert A().__class__ == B().__class__

# Generated at 2022-06-14 02:31:59.027803
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_base import BaseTestTransformer
    from ..utils.helpers import generate_code_obj


# Generated at 2022-06-14 02:32:08.976996
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer, transform
    import os
    import sys

    class TestTransformer(BaseNodeTransformer):
        target = (2, 7)

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                node.args = [ast.Name(id='Cls'), ast.Name(id='self')]
                self._tree_changed = True
            return self.generic_visit(node)  # type: ignore


# Generated at 2022-06-14 02:32:12.106620
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.source import assign_fields
    from .base import BaseNodeTransformer
    from .stub_node import StubNodeTransformer

    class Test(BaseNodeTransformer):
        def visit_Call(self, node):
            self._tree_changed = True
            return node


# Generated at 2022-06-14 02:32:13.870791
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:15.100574
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor

# Generated at 2022-06-14 02:32:29.827536
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import cst_to_ast

    cst = "super()"
    ast_ = cst_to_ast(cst, target_versions={'3.6'})

    # Calling `visit_Call` manually
    transformer = SuperWithoutArgumentsTransformer(target_versions={'3.6'})
    result = transformer.visit_Call(ast_.body[0].value)

    assert isinstance(result, ast.Call)
    assert isinstance(result.func, ast.Name)
    assert result.func.id == 'super'
    assert len(result.args) == 2
    assert isinstance(result.args[0], ast.Name)
    assert result.args[0].id == 'Cls'
    assert isinstance(result.args[1], ast.Name)

# Generated at 2022-06-14 02:32:41.224666
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Initialize the transformer
    transformer = SuperWithoutArgumentsTransformer()
    # Read the test file at the location tests/fixtures/files/super_without_arguments.py
    file_path = os.path.dirname(os.path.abspath(__file__))
    test_file = open(file_path + "/../../fixtures/files/super_without_arguments.py")
    # Construct an AST tree
    old_tree = ast.parse(test_file.read())
    # Pass the AST tree to the transformer for parsing
    new_tree = transformer.visit(old_tree)
    # Generate the code from the modified AST tree
    codeobj = compile(new_tree, '', 'exec')
    # Execute the code
    exec(codeobj)
    # Assert that the string "SuperTransform

# Generated at 2022-06-14 02:32:48.611072
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = textwrap.dedent("""
    class TestClass:
        def __init__(self):
            super()
    """)
    node = ast.parse(code)
    SuperWithoutArgumentsTransformer(node).visit(node)
    assert isinstance(node.body[0].body[0].value.args[0], ast.Name)
    assert node.body[0].body[0].value.args[0].id == 'TestClass'

# Generated at 2022-06-14 02:32:49.992397
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:56.753133
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    node = tree.body[0]
    SuperWithoutArgumentsTransformer(tree).visit(node)
    assert ast.dump(tree) == "Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))\n"



# Generated at 2022-06-14 02:33:07.213956
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.fake_tree import FakeTree

    # Apply a class method definition
    class_def = ast.ClassDef(name='Cls', body=[
        ast.FunctionDef(name='meth', args=ast.arguments(args=[ast.arg(arg='self')], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[
            ast.Expr(value=ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])),
            ast.Return(value=ast.Num(n=1))
        ])
    ])
    fake_tree = FakeTree(node=class_def)

# Generated at 2022-06-14 02:33:12.142660
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    test_input = "class Foo():\n    def __init__(self):\n        super()\n"
    expected_output = "class Foo():\n    def __init__(self):\n        super(Foo, self)\n"
    module = ast.parse(test_input)
    SuperWithoutArgumentsTransformer().visit(module)
    result = astor.to_source(module).strip()
    assert result == expected_output

# Generated at 2022-06-14 02:33:23.569961
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import CompileError, NodeTransformer
    from astmonkey import transformers
    from typed_ast import ast3

    code = '\n'.join([
        'class Foo():',
        '    def __init__(self):',
        '        super()',
        ''
    ])

    stmt = ast.parse(code).body[0]
    cls = stmt.body[0]
    node = cls.body[0]

    transformer = NodeTransformer()
    transformer.register(SuperWithoutArgumentsTransformer)
    transformed = transformer.visit(stmt)
    transformed_cls = transformed.body[0]
    transformed_node = transformed_cls.body[0]

    assert isinstance(transformed_node.args[0], ast3.Name)

# Generated at 2022-06-14 02:33:25.715927
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:30.526550
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    before = """class A:
    def __init__(self):
        super()"""
    after = """class A:
    def __init__(self):
        super(A, self)"""
    t = SuperWithoutArgumentsTransformer().visit(ast.parse(before))
    assert ast.dump(t) == ast.dump(ast.parse(after))

# Generated at 2022-06-14 02:33:44.485023
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # Arrange
    from ..utils.testing import assert_transform
    from ..utils.helpers import parse_python_snippet_into_ast

    snippet = """
        class Foo:
            def __init__(self):
                super()
    """
    expected_snippet = """
        class Foo:
            def __init__(self):
                super(Foo, self)
    """
    transformer = SuperWithoutArgumentsTransformer(parse_python_snippet_into_ast(snippet))

    # Act
    assert_transform(transformer, snippet, expected_snippet)

# Generated at 2022-06-14 02:33:51.211675
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .tests.fixtures.super_without_arguments.input import input_code
    from .tests.fixtures.super_without_arguments.output import output_code
    t = SuperWithoutArgumentsTransformer()
    new_tree = t.visit(input_code)
    assert output_code == ast.dump(new_tree, AnnotateTreeLines())

# Generated at 2022-06-14 02:33:52.354587
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..parser import parse


# Generated at 2022-06-14 02:33:57.350074
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class foo(object):
        def __init__(self):
            super()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert 'super(foo, self)' in astor.to_source(tree)

# Generated at 2022-06-14 02:33:58.788309
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:03.602017
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .test_helpers import get_comparison_ast
    from .test_helpers import roundtrip_unparse_compare
    from ..targets.python_target import PythonTarget
    from ..utils.helpers import get_top_level_classes_and_functions

# Generated at 2022-06-14 02:34:11.678953
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code = """
    class Base:
        def test(self):
            pass
            
    class Sub(Base):
        def test(self):
            super()
    """

    expected_output = """
    class Base:
        def test(self):
            pass
            
    class Sub(Base):
        def test(self):
            super(Base, self)
    """

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert_code(expected_output, tree)



# Generated at 2022-06-14 02:34:12.648431
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import ast

# Generated at 2022-06-14 02:34:21.475214
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_restricted as compile
    from ..utils.helpers import as_tuple
    from .helpers import get_func_ast, get_cls_ast

    def f(self):
        return super()

    f_ast = get_func_ast(f)
    SuperWithoutArgumentsTransformer(f_ast).visit(f_ast)

    func_ast = as_tuple(f_ast.body[0])

# Generated at 2022-06-14 02:34:25.507896
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import unittest
    import ast as pyast
    from unittest.mock import Mock
    from ast_helper import assert_ast_equal, parse
    mock_tree = Mock()

    class UnderTest(SuperWithoutArgumentsTransformer):
        _tree = mock_tree


# Generated at 2022-06-14 02:34:41.506364
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:34:44.625625
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = "super()"
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).run()
    assert str(tree) == "super(Cls, self)"

# Generated at 2022-06-14 02:34:48.741587
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    class TestTransformer(SuperWithoutArgumentsTransformer):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            self._replace_super_args(node)
            return node


# Generated at 2022-06-14 02:34:56.409643
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''class A:
        def __init__(self):
            super()'''

    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)

    assert transformer.tree_changed()

    expected = ast.parse('''class A:
        def __init__(self):
            super(A, self)''')

    assert ast.dump(tree) == ast.dump(expected)


# Generated at 2022-06-14 02:34:57.828893
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:00.514999
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import typed_astunparse
    from .test_BaseNodeTransformer import BaseNodeFactory


# Generated at 2022-06-14 02:35:02.190650
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:10.210133
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Foo:
        def bar(self):
            super()
            
        class FooBar:
            def bar(self):
                super()
    """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed is True
    assert code_gen.to_source(tree).strip() == code.strip()
    # assert code_gen.to_source(tree).strip() == """
    # class Foo:
    #     def bar(self):
    #         super(Foo, self)
    #
    #     class FooBar:
    #         def bar(self):
    #             super(FooBar, self)
    # """.strip()

# Generated at 2022-06-14 02:35:13.138172
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor


# Generated at 2022-06-14 02:35:23.465760
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode as u
    from ..utils.source import source_to_ast as parse

    # class A:
    #     def foo():
    #         super()

    src = u('''
    class A:
        def foo():
            super()
    ''')
    tc = SuperWithoutArgumentsTransformer(parse(src))
    tc.visit(tc.tree)
    assert tc.tree_changed is True

# Generated at 2022-06-14 02:35:58.331261
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import parse, ast3
    from ..utils.tree import dump
    import sys

    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:36:01.459781
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import setup_ast_node_transformer
    from ..utils.testing import assert_transformed_code_equals
    from ..utils.tree import get_code_from_ast

    setup_ast_node_transformer()


# Generated at 2022-06-14 02:36:03.493039
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:04.100028
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:10.410485
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import find_all, build_ast_tree
    code = """
        class A:
            def __init__(self, name):
                self.name = name
                super()
    """
    tree = build_ast_tree(code, (2, 7))
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    expected = """
        class A:
            def __init__(self, name):
                self.name = name
                super(A, self)
    """
    assert expected == code

# Generated at 2022-06-14 02:36:11.987246
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transpiler = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:36:19.517030
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Sample(object):
        def __init__(self):
            super()
    """
    expected_output = """
    class Sample(object):
        def __init__(self):
            super(Sample, self)
    """
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree) == expected_output
    assert tree is not None


# Generated at 2022-06-14 02:36:25.528473
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_str = """
    class Test:
        def __init__(self):
            super()
    """
    code_ast = ast.parse(code_str)
    SuperWithoutArgumentsTransformer().visit(code_ast)


# Generated at 2022-06-14 02:36:30.047689
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse(dedent('''
        class A:
            def __init__(self):
                super()
    '''))
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast_to_str(tree) == dedent('''
        class A:
            def __init__(self):
                super(A, self)
    ''').strip()

# Generated at 2022-06-14 02:36:34.247491
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astunparse
    import sys
    if sys.version_info[:2] != (2, 7):
        raise RuntimeError(
            "SuperWithoutArgumentsTransformer is only tested for Python 2.7, you are running {}.{}.".format(
                sys.version_info[0], sys.version_info[1]))

# Generated at 2022-06-14 02:37:55.005903
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..utils.helpers import as_tuple


# Generated at 2022-06-14 02:37:56.657046
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass


# Generated at 2022-06-14 02:38:02.648508
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from pymodernize import fixer_util
    from ..transformers import CastVarsTransformer

    code = '''
    class A:
        def __init__(self):
            super()
            def f():
                return super()
    '''
    tree = fixer_util.parse_print(code)

    transformer = SuperWithoutArgumentsTransformer(CastVarsTransformer())
    new = transformer.visit(tree)
