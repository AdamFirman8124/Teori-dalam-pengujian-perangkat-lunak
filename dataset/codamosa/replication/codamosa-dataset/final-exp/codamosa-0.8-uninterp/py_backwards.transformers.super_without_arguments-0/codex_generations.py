

# Generated at 2022-06-14 02:28:00.937545
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:04.559519
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import textwrap
    from ..utils.helpers import get_ast
    tree = get_ast(textwrap.dedent("""
        class A:
            def a(self):
                super()
        """))
    new_tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert 'super(A, self)' in str(new_tree)

# Generated at 2022-06-14 02:28:12.368560
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Call, Name, FunctionDef, ClassDef, Load, arguments
    from ..utils.test_utils import get_test_nodes, get_test_nodes_string, assert_source_equal

    for test in get_test_nodes('super.py'):
        tree = test.tree
        transformer = SuperWithoutArgumentsTransformer(tree)
        transformer.visit(tree)

        assert_source_equal(get_test_nodes_string(test.name, 'super.py'), tree)

# Generated at 2022-06-14 02:28:15.736906
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import cst_to_ast


# Generated at 2022-06-14 02:28:17.240593
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:18.874673
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import compile_source
    from .. import settings

# Generated at 2022-06-14 02:28:24.538955
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    class Foo(object):
        def __init__(self):
            super()
    """

    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    exec(compile(tree, filename="<ast>", mode="exec"))



# Generated at 2022-06-14 02:28:28.336441
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = "super()"
    expected = "super(Cls, self)"
    node = ast.parse(source, mode="exec").body[0]
    tree = SuperWithoutArgumentsTransformer(node)
    
    assert tree.body.s() == expected

# Generated at 2022-06-14 02:28:29.331287
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:38.596591
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_restricted
    from itertools import permutations

    prefixes = ['super(Cls, self)', 'super(Cls, cls)']
    for prefix in permutations(prefixes):
        src = 'class Cls(object):\n    def fn(self):\n        {0}\n        {1}'.format(*prefix)
        assert compile_restricted(src, 'exec')

    for prefix in permutations(prefixes):
        src = '\n    def fn(self):\n        {0}\n        {1}'.format(*prefix)
        assert compile_restricted(src, 'exec')
        # assert compile_restricted(src, 'eval')


# Generated at 2022-06-14 02:28:42.452982
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:53.913009
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast.ast3 import parse

    tree = parse(
        """class Test:\n\tdef a(self):\n\t\tsuper()"""
    )
    SuperWithoutArgumentsTransformer(tree).visit(tree)

    def assert_super_args(node: ast.Call) -> None:
        assert len(node.args) == 2
        assert isinstance(node.args[0], ast.Name)
        assert node.args[0].id == 'Test'
        assert isinstance(node.args[1], ast.Name)
        assert node.args[1].id == 'self'

    assert_super_args(tree.body[0].body[1].value)


# Generated at 2022-06-14 02:29:03.254271
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
super()
'''
    module = ast.parse(code)
    classdef_node = module.body[0]
    func_node = module.body[0]

    tree_changed = False

    def assert_tree_changed():
        nonlocal tree_changed
        tree_changed = True
    
    SuperWithoutArgumentsTransformer(tree_changed=assert_tree_changed).visit(module)

    assert tree_changed

    expected_code = '''\
super(Cls, self)
'''

    generated_code = astor.to_source(module)

    assert generated_code == expected_code

# Generated at 2022-06-14 02:29:11.349628
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_code = """
        class Test:
            def __init__(self):
                super()
    """
    expected_code = """
        class Test:
            def __init__(self):
                super(Test, self)
    """
    tree = ast.parse(input_code)
    SuperWithoutArgumentsTransformer().visit(tree)
    generated_code = astor.to_source(tree).strip()
    assert generated_code == expected_code

# Generated at 2022-06-14 02:29:22.165530
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.test_utils import assert_program_equal

    source = '''super()'''
    expected = '''super(Cls, self)'''

    tree = ast.parse(source)
    call_node = tree.body[0].value
    func_node = get_closest_parent_of(tree, call_node, ast.FunctionDef)
    cls_node = get_closest_parent_of(tree, call_node, ast.ClassDef)
    call_node.args = [ast.Name(id=cls_node.name), ast.Name(id=func_node.args.args[0].arg)]

    tree = SuperWithoutArgumentsTransformer().visit(ast.parse(source))
    assert_program_equal(tree, expected)


# Generated at 2022-06-14 02:29:31.659587
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    code = '''class A:
    def f(self):
        super()
    @classmethod
    def g(cls):
        super()
'''
    node = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer()
    tree.visit(node)
    assert astor.to_source(node) == '''class A:
    def f(self):
        super(A, self)
    @classmethod
    def g(cls):
        super(A, cls)
'''

# Generated at 2022-06-14 02:29:33.349019
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    from ..utils.ast_builder import build_ast

# Generated at 2022-06-14 02:29:40.482245
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ast import parse
    from ..utils.helpers import dump_ast
    transformer = SuperWithoutArgumentsTransformer(parse('super()').body[0])
    transformer.visit(transformer.tree)
    assert dump_ast(transformer.tree) == 'Expr(value=Call(func=Name(id=super, ctx=Load()), args=[Name(id=C, ctx=Load()), Name(id=self, ctx=Load())], keywords=[], starargs=None, kwargs=None))'

# Generated at 2022-06-14 02:29:48.532853
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTestCase

    class Test(BaseNodeTransformerTestCase):
        def create_node(self) -> ast.Call:
            return ast.Call(func=ast.Name(id='super'), args=[])

        def create_transformer(self, tree: ast.AST) -> SuperWithoutArgumentsTransformer:
            return SuperWithoutArgumentsTransformer(tree)

    Test().run(globals())



# Generated at 2022-06-14 02:29:58.537805
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import typed_ast.ast3 as ast
    from ..utils.testing.code_gen import generate_code
    from ..utils.testing.source import transform_and_compare_source

    class TestAst(ast.AST):

        _fields = ('name', 'value')

        def __init__(self, name, value):
            self.name = name
            self.value = value

    def TestTransform(node):
        transformer = SuperWithoutArgumentsTransformer()
        return transformer.visit(node)


# Generated at 2022-06-14 02:30:10.511395
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    src = '''
            class A:
                def __init__(self):
                    super()
        '''

    src = transformer.visit(ast.parse(src))
    assert transformer._tree_changed is True

# Generated at 2022-06-14 02:30:13.531782
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..pgen2.token import LEXER, Token
    from ..pgen2 import driver
    from ..utils.source import Source
    from ..utils.tree import build_ast
    from .remove_decorator import RemoveDecorator
    from ..front_base.tokenizer import detect_encoding, tokenize_encoding


# Generated at 2022-06-14 02:30:16.111793
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ..utils.helpers import ast_to_source


# Generated at 2022-06-14 02:30:17.865505
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..exceptions import ParserSyntaxError
    from .. import refactor


# Generated at 2022-06-14 02:30:24.096844
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astunparse
    from textwrap import dedent

    code = dedent('''
    class A:
        def __init__(self):
            super()
    ''')
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astunparse.unparse(tree) == dedent('''
    class A:
        def __init__(self):
            super(A, self)
    ''')

# Generated at 2022-06-14 02:30:24.973552
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:32.456209
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    from ..utils.helpers import get_test_data_path
    from ..utils.tree import parse_file_to_ast

    for version in (2, 7):
        tree = parse_file_to_ast(get_test_data_path(f'SuperWithoutArguments/program.py'),
                                 ignore_future=True, target_versions={version})

        transformer = SuperWithoutArgumentsTransformer(
            tree=tree,
            target_versions={version}
        )

        result_tree = transformer.generic_visit(tree)

        assert result_tree is not None
        assert transformer.tree_changed is True

# Generated at 2022-06-14 02:30:38.003389
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A(object):
            def __init__(self):
                super().__init__()
    """

    expected_code = """
        class A(object):
            def __init__(self):
                super(A, self).__init__()
    """

    t = SuperWithoutArgumentsTransformer()
    t.visit(ast.parse(code))
    assert expected_code == astunparse.unparse(t.tree)

# Generated at 2022-06-14 02:30:42.802754
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import setup_2to3

    class DummyCls():
        def __init__(self):
            pass

        def m1(self):
            super()

    result = setup_2to3('from typing import List\n' + inspect.getsource(DummyCls), 'super')
    print(result)

# Generated at 2022-06-14 02:30:43.549150
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:53.585948
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .test_helpers import parse_to_ast, print_ast

    class DemoVisitor(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                print(f'Found super()!')
                return node


# Generated at 2022-06-14 02:31:01.924976
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from ..utils.helpers import compare_node

    result = source_to_nodes('''
    class A(object):
        def fun(self):
            super()
    ''')

    expect = source_to_nodes('''
    class A(object):
        def fun(self):
            super(A, self)
    ''')

    compare_node(SuperWithoutArgumentsTransformer.run_it(result), expect)

# Generated at 2022-06-14 02:31:04.274397
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from .utils import parse

    class Dummy(ast3.NodeTransformer):
        pass


# Generated at 2022-06-14 02:31:14.410905
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = inspect.cleandoc('''
    class Test:
        def test(self):
            super()
    ''')
    tree = ast.parse(code)
    new_tree = SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:31:15.583098
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import get_ast


# Generated at 2022-06-14 02:31:16.373995
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile

# Generated at 2022-06-14 02:31:19.063325
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typing import Optional
    import astunparse
    from itertools import chain


# Generated at 2022-06-14 02:31:23.185758
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.source import source_to_unicode
    from .syntax_error_transformer import SyntaxErrorTransformer

# Generated at 2022-06-14 02:31:30.616880
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.test_utils import transform_and_compare
    from ..common import COMMENT

    code = '''
    class Foo(object):
        # {0}
        def foo(self):
            super()
    '''.format(COMMENT)

    expected = '''
    class Foo(object):
        def foo(self):
            super(Foo, self)
    '''

    tree = transform_and_compare(SuperWithoutArgumentsTransformer, code, expected)

# Generated at 2022-06-14 02:31:41.559571
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    import unittest
    import sys

    class SuperWithoutArgumentsTransformer_test(unittest.TestCase):
        def test_error_handling(self):
            print('running test_error_handling')
            from astor.code_gen import to_source
            from .. import compile_func

            source = """
            def hello():
                super()
            """
            tree = compile_func(source)
            print(tree)
            self.assertEqual(to_source(tree).strip(), 'super(Hello, hello)')
            print('passed test_error_handling')

        def test_basic(self):
            print('running test_super')
            from astor.code_gen import to_source
            from .. import compile_func


# Generated at 2022-06-14 02:31:56.404875
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    test_tree = ast.parse("""class A:
        def __init__(self):
            super()""")
    expected_tree = ast.parse("""class A:
        def __init__(self):
            super(A, self)""")

    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(test_tree)
    assert astor.to_source(test_tree) == astor.to_source(expected_tree)

# Generated at 2022-06-14 02:32:09.342047
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
        class A(object):
            def m1(self):
                super()
            def m2(self, a):
                super(A, self)
            def m3(self, a, b, c=None, *args, **kwargs):
                super()
                
        class B(A):
            def __init__(self):
                super().__init__()
                
        def func():
            super()
    """

# Generated at 2022-06-14 02:32:12.869040
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer(None, None)._replace_super_args(
        ast.Call(func=ast.Name(id='super'), args=[], keywords=[])) is None

    assert SuperWithoutArgumentsTransformer(None, None)._replace_super_args(
        ast.Call(func=ast.Name(id='super'),
                 args=[ast.Name(id='cls')],
                 keywords=[])) is None

# Generated at 2022-06-14 02:32:14.927339
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:16.126108
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:22.824255
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super()"""
    import sys
    import os.path
    sys.path.append(os.path.realpath('.'))
    from typed_ast import ast3
    from typed_ast.transforms import super
    tree = ast3.parse(code)
    tree2 = super.SuperWithoutArgumentsTransformer().visit(tree)
    assert(ast3.dump(tree2) == 'super(Cls, cls)')

# Generated at 2022-06-14 02:32:24.156000
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:33.893119
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A:
        def __init__(self):
            super()
        def f(self):
            super()
    class B:
        def __init__(cls):
            super()
        def f(cls):
            super()
    """
    expected_code = """
    class A:
        def __init__(self):
            super(A, self)
        def f(self):
            super(A, self)
    class B:
        def __init__(cls):
            super(B, cls)
        def f(cls):
            super(B, cls)
    """
    tree = ast.parse(code)

    SuperWithoutArgumentsTransformer().visit(tree)

    assert astor.to_source(tree).strip() == expected_code

# Generated at 2022-06-14 02:32:36.729428
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class B:
          def m(self) -> int:
            return super()
        """
    compile(ast.parse(code), '<test>', 'exec')

# Generated at 2022-06-14 02:32:43.255526
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import assert_node_transformed
    code = """
        import abc

        class MyABC(metaclass=abc.ABCMeta):
            @abc.abstractmethod
            def do_something(self, value):
                super()
                pass
    """
    expected = """
        import abc

        class MyABC(metaclass=abc.ABCMeta):
            @abc.abstractmethod
            def do_something(self, value):
                super(MyABC, self)
                pass
    """
    assert_node_transformed(SuperWithoutArgumentsTransformer, code, expected)

# Generated at 2022-06-14 02:32:55.882353
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:02.971336
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class Foo:
            def bar(self):
                super()
    '''

    module = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(module)
    assert isinstance(tree, ast.Module)

    cls = tree.body[0]
    assert isinstance(cls, ast.ClassDef)

    func = cls.body[0]
    assert isinstance(func, ast.FunctionDef)

    call = func.body[0]
    assert isinstance(call, ast.Expr)
    assert isinstance(call.value, ast.Call)

    assert isinstance(call.value.args[0], ast.Name)
    assert call.value.args[0].id == 'Foo'


# Generated at 2022-06-14 02:33:11.743150
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_tree

    tree = source_to_tree('''
        class A(object):
            def __init__(self):
                super().__init__()
        
        class B(A):
            def __init__(self):
                super().__init__()
        
        class D(A):
            def __init__(self):
                super().__init__()
            def f(self):
                super().__init__()
    ''')

    x = SuperWithoutArgumentsTransformer()
    x.visit(tree)


# Generated at 2022-06-14 02:33:23.398969
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super().__init__()'


# Generated at 2022-06-14 02:33:26.042161
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:29.347836
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """class Cls:
            def foo(self):
                super()
            """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert isinstance(ast.dump(tree), str)

# Generated at 2022-06-14 02:33:29.922207
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:33:35.063088
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from . import test_utils
    from . import test_utils as tu

    func = test_utils.build_function(
        name='bar',
        code='''        super()
        '''
    )

    cls = test_utils.build_class(name='Foo', childs=[func])

    source = tu.code_gen([cls])

# Generated at 2022-06-14 02:33:45.093818
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """class Cls():
    def __init__(self):
        super()
        super()

    def __str__(self):
        super()
        super()"""
    expected_code = """class Cls():
    def __init__(self):
        super(Cls, self)
        super(Cls, self)

    def __str__(self):
        super(Cls, self)
        super(Cls, self)"""
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    compiled = compile(tree, "<test>", 'exec')
    actual_code = ''.join(line for line in compiled.co_consts[0] if isinstance(line, str))
    assert actual_code == expected_code


# Generated at 2022-06-14 02:33:50.305540
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import typed_ast.ast3 as ast
    from .. import TranspileResult
    from ..transformer_factory import transformer_factory
    from ..transformer import BaseTransformer

    tf = transformer_factory([SuperWithoutArgumentsTransformer])

# Generated at 2022-06-14 02:34:18.148966
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_tree

    tree = source_to_tree('''class A:
        def __init__(self):
            super()
''')

    node = tree.body[0].body[0].body[0]
    
    assert node.args == []

    trans = SuperWithoutArgumentsTransformer(tree)
    trans.run()

    assert len(node.args) == 2
    assert node.args[0].id == 'A' or node.args[1].id == 'A'

# Generated at 2022-06-14 02:34:21.048017
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer.name() == 'SuperWithoutArgumentsTransformer'

# Generated at 2022-06-14 02:34:32.882832
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def check(tree: ast.AST, exp_tree: ast.AST) -> None:
        """Checks that the transformer compiles the tree as expected."""
        SuperWithoutArgumentsTransformer(None).visit(tree)  # type: ignore
        assert ast.dump(tree) == ast.dump(exp_tree)

    code = """
        class X(object):
            def method1(self):
                super()

            def method2(cls):
                super()
    """
    exp_code = """
        class X(object):
            def method1(self):
                super(X, self)

            def method2(cls):
                super(X, cls)
    """
    tree = ast.parse(code)
    exp_tree = ast.parse(exp_code)

# Generated at 2022-06-14 02:34:35.035030
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .context import Context


# Generated at 2022-06-14 02:34:35.679940
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:41.686713
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
  from ..utils.source import source_to_ast

  tree = source_to_ast.parse('''
    class MyClass:
      def my_method(self):
        my_var = super().my_other_method()
  ''')

  res = SuperWithoutArgumentsTransformer(tree).result()
  assert b'MyClass' in ast.dump(res)

# Generated at 2022-06-14 02:34:42.406586
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:47.664986
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Given
    code = "super()"
    expected_code = "super(Cls, self)"
    tree = ast.parse(code)

    # When
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)
    # Then
    assert ast.dump(tree, include_attributes=True) == expected_code

# Generated at 2022-06-14 02:34:53.792457
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
for i in x:
    super()
    """
    expected_code = """
for i in x:
    super(__tau_9176__, self)
    """
    result_code = SuperWithoutArgumentsTransformer(code).result()
    print(result_code)
    assert result_code == expected_code

# Generated at 2022-06-14 02:35:08.002778
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes

    module = ast.parse('super()')
    node = module.body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'super'

    SuperWithoutArgumentsTransformer().visit(module)

    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'super'
    assert isinstance(node.value.args[0], ast.Name)
    assert node.value.args[0].id == 'Cls'

# Generated at 2022-06-14 02:36:07.799394
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse('super()')
    tr = SuperWithoutArgumentsTransformer()
    node = tr.visit(node)
    assert ast.dump(node) == 'Super(Name(id="Cls", ctx=Load()), Name(id="self", ctx=Load()))'

# Generated at 2022-06-14 02:36:17.091636
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Arrange
    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[], starargs=None, kwargs=None)
    transformed_tree = SuperWithoutArgumentsTransformer().visit(node)

    # Assert
    assert ast.dump(transformed_tree) == '(Call(func=Name(id=\'super\', ctx=Load()), args=[Name(id=\'Cls\', ctx=Load()), Name(id=\'self\', ctx=Load())], keywords=[], starargs=None, kwargs=None))'

# Generated at 2022-06-14 02:36:27.293032
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer._get_source_code(
        'super()', 2, 7) == 'super(Cls, self)'
    assert SuperWithoutArgumentsTransformer._get_source_code(
        'super(test, x, y)', 2, 7) == 'super(test, x, y)'
    assert SuperWithoutArgumentsTransformer._get_source_code(
        'super(test)', 2, 7) == 'super(test)'
    assert SuperWithoutArgumentsTransformer._get_source_code(
        'super(test, x, y)', 3, 6) == 'super(test, x, y)'
    assert SuperWithoutArgumentsTransformer._get_source_code(
        'super(test, x, y)', 3, 7) == 'super(test, x, y)'
    assert SuperWithout

# Generated at 2022-06-14 02:36:31.785187
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class A:
        def func(self):
            super()
        def meth(self):
            super()
            
    class B(A):
        def func(self):
            super()

    class C:
        def meth(self):
            super()

    assert SuperWithoutArgumentsTransformer(A).run() == A
    assert SuperWithoutArgumentsTransformer(B).run() == B
    assert SuperWithoutArgumentsTransformer(C).run() == C

# Generated at 2022-06-14 02:36:33.026485
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import tree, module


# Generated at 2022-06-14 02:36:39.860957
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
$a = super()
        '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert isinstance(tree.body[0].value.args[0], ast.Name)
    assert isinstance(tree.body[0].value.args[1], ast.Name)

# Generated at 2022-06-14 02:36:52.538210
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = textwrap.dedent("""
    class D(A, B):
        def foo(self):
            super()
    """)
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:37:02.864398
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import compare_source
    from .base import BaseNodeTransformer
    from .scope import ConditionalScopeTransformer
    from .super import SuperWithoutArgumentsTransformer

    source = '''class MyClass(object):
    def my_func(self):
        super()
        super()
    def my_func(self):
        super()
        super()'''

    expected = '''class MyClass(object):
    def my_func(self):
        super(MyClass, self)
        super(MyClass, self)
    def my_func(self):
        super(MyClass, self)
        super(MyClass, self)'''

    tree = ast.parse(source)
    scope_transf = ConditionalScopeTransformer(source)
    scope_transf.visit(tree)
   

# Generated at 2022-06-14 02:37:03.410705
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:13.083154
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    t = SuperWithoutArgumentsTransformer({'super()'})
    tree = ast.parse('super()')
    t.visit(tree)
    assert len(tree.body[0].value.args) == 2
    assert tree.body[0].value.args[0].id == "Cls"
    assert tree.body[0].value.args[1].id == "self"

    t = SuperWithoutArgumentsTransformer({'super.__init__()'})
    tree = ast.parse('super.__init__()')
    t.visit(tree)
    assert len(tree.body[0].value.func.value.args) == 2
    assert tree.body[0].value.func.value.args[0].id == "Cls"
    assert tree.body[0].value.func.value.args