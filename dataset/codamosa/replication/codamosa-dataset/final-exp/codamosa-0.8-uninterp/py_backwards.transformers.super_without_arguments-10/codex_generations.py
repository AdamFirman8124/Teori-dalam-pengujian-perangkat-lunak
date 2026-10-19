

# Generated at 2022-06-14 02:27:57.276759
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import parse, compare_ast


# Generated at 2022-06-14 02:28:01.150730
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("""super()""")
    tree2 = ast.parse("""super(A, self)""")
    SuperWithoutArgumentsTransformer().visit(tree)

    assert ast.dump(tree) == ast.dump(tree2)

# Generated at 2022-06-14 02:28:10.541494
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest


# Generated at 2022-06-14 02:28:11.895225
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:16.967147
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    transformer = SuperWithoutArgumentsTransformer(None, None)

    node = ast.Call(
        func=ast.Name(id='super'),
        args=[],
        keywords=[]
    )

    node = transformer.visit_Call(node)
    assert isinstance(node, ast.Call)

# Generated at 2022-06-14 02:28:23.938952
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    class TestSuperWithoutArgumentsTransformer(SuperWithoutArgumentsTransformer):
        def visit_FunctionDef(self, node):
            return node

    tree = ast.parse("""
                class TestSuperWithoutArgumentsTransformer:
                    def f(self):
                        super()

                def f():
                    super()

                """)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    print(ast.dump(tree))

# Generated at 2022-06-14 02:28:25.921247
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Test Correctness of class SuperWithoutArgumentsTransformer
    """

# Generated at 2022-06-14 02:28:35.832619
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import unittest
    from ast_helper import parse_to_ast

    class TestVisitor(unittest.TestCase):
        def test_01_response_to_super_without_arguments(self):
            tree = parse_to_ast("""
            class Cls:
                def __init__(self):
                    super().__init__()
            """)
            transformer = SuperWithoutArgumentsTransformer()
            transformer.visit(tree)

# Generated at 2022-06-14 02:28:45.856876
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import cst
    from .base import BaseNodeTransformer
    from .ast_transformer import AstTransformer
    import sys
    class DummySuperWithoutArgumentsTransformer(BaseNodeTransformer):
        target = (2, 7)
        def visit_Call(self, node: ast.Call) -> ast.Call:
            return self.generic_visit(node) # type: ignore
    class DummyAstTransformer(AstTransformer):
        def __init__(self):
            super().__init__()
            self.target = (2, 7)
            self.transformer_classes = [DummySuperWithoutArgumentsTransformer]

# Generated at 2022-06-14 02:28:50.484517
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    def test(tree, expected_tree):
        # type: (ast.AST, ast.AST) -> None
        super_without_arguments_transformer = SuperWithoutArgumentsTransformer()
        trans_tree = super_without_arguments_transformer.visit(tree)
        assert(expected_tree == trans_tree)

    test(ast.parse('super()'), ast.parse('super(__class__, self)'))

# Generated at 2022-06-14 02:28:56.816635
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import parse_ast
    from ..utils.helpers import get_ast


# Generated at 2022-06-14 02:29:03.485124
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    class A(ast.AST):
        pass

    class B(A):
        pass

    class C(B):
        pass

    program = """
    class Bar():
        def baz(self):
            return super()
    """

    tree = ast.parse(program)

    SuperWithoutArgumentsTransformer().visit(tree)


# Generated at 2022-06-14 02:29:14.336474
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import parse_and_visit
    from ..utils.context import Context
    ctx = Context()

    tree = parse_and_visit("""
    class Foo:
        def __init__(self):
            super()
    """, [SuperWithoutArgumentsTransformer])

    assert tree.body[0].body[0].args[1].id == 'self' 

    tree = parse_and_visit("""
    class Foo:
        def __init__(cls):
            super()
    """, [SuperWithoutArgumentsTransformer])

    assert tree.body[0].body[0].args[1].id == 'cls'

# Generated at 2022-06-14 02:29:25.027239
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import sys
    sys.path.append('..')
    from utils.test_visitor import TestVisitor
    from typed_ast import ast3 as ast

    node_arguments = []
    # Initialize the tree to visit
    test_tree = ast.Module([ast.ClassDef(name='Cls',
                                         body=[ast.FunctionDef(name='func',
                                                               body=[ast.Expr(value=ast.Call(func=ast.Name(id='super'), args=node_arguments))])],
                                                               bases=[ast.Name(id='object')])])

    # Initialize the visitor
    test_visitor = TestVisitor.from_visitor(SuperWithoutArgumentsTransformer)

    # Visit the tree
    test_visitor.visit(test_tree)

    # The tree should

# Generated at 2022-06-14 02:29:36.440803
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = "super()"
    tree = ast.parse(code)
    result = SuperWithoutArgumentsTransformer.run_pipeline(code)


# Generated at 2022-06-14 02:29:42.669455
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class A(object):
            def __init__(self):
                super()
    '''
    expected_output = '''
        class A(object):
            def __init__(self):
                super(A, self)
    '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

    assert ast.dump(tree) == ast.dump(ast.parse(expected_output))

# Generated at 2022-06-14 02:29:50.920243
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from astor.code_gen import to_source
    from ..utils.python_deps_resolver import PythonDepsResolver

    tree = ast.parse("class A:\n  def __init__(self):\n    super()")

    t = SuperWithoutArgumentsTransformer(tree, PythonDepsResolver())
    t.visit(tree)

    assert to_source(tree) == "class A:\n  def __init__(self):\n    super(A, self)"

# Generated at 2022-06-14 02:29:53.637903
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='super'), args=[], keywords=[])
    tree = ast.parse('class A: a = 1; def b(c): super()')
    t = SuperWithoutArgumentsTransformer()
    t.visit(tree)
    assert str(node) == str(t._tree)

# Generated at 2022-06-14 02:30:01.195240
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test:
        def f(self):
            return super()

    tree = ast.parse(inspect.getsource(Test))
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    Test = compile(tree, file=__file__, mode='exec')

    test = Test()
    assert test.f() == 'super'

    class Test:
        def f(self):
            def g():
                return super()

            return g()

    tree = ast.parse(inspect.getsource(Test))
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    Test = compile(tree, file=__file__, mode='exec')

    test = Test()
    assert test.f() is None

    class Test:
        def f(self):
            super()


# Generated at 2022-06-14 02:30:09.507567
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.dummy_context import DummyContext
    from ..main import compile_src

    code = 'super()'
    expected_code = 'super(Cls, self)'
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer(DummyContext, tree).visit(tree)
    assert compile_src(tree) == expected_code

    code = 'super(Name, args)'
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer(DummyContext, tree).visit(tree)
    assert compile_src(tree) == code


# Generated at 2022-06-14 02:30:12.544749
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:15.023045
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:25.344253
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import compile_source
    from prettyprinter import pprint

    from .test_base import BaseTest

    class Test(BaseTest):
        target = (2, 7)
        transform = SuperWithoutArgumentsTransformer

        def test_simple(self):
            code = '''\
            class Base(object):
                def __init__(self, arg):
                    super()
            
            class Derived(Base):
                def __init__(self, arg):
                    super()
            '''
            astree = compile_source(code, '<test>', 'exec')

# Generated at 2022-06-14 02:30:35.479384
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode

    source = source_to_unicode('''
        class Foo():
            def __init__(self):
                super().__init__()
    ''')

    node = ast.parse(source)
    SuperWithoutArgumentsTransformer().visit(node)


# Generated at 2022-06-14 02:30:41.459707
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """class A:
        def __init__(self):
            super().__init__()"""

    tree = ast.parse(code)

    new_tree = SuperWithoutArgumentsTransformer().visit(tree)

    transpiled_code = compile(new_tree, '<string>', 'exec')
    eval(transpiled_code)

# Generated at 2022-06-14 02:30:48.576662
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.unparse import unparse_python_version

    tree = ast.parse('class Test(object): def test(self): super()', '', 'exec')
    fixer = SuperWithoutArgumentsTransformer(tree)
    assert fixer.tree_changed
    assert unparse_python_version(tree) == 'class Test(object): def test(self): super(Test, self)'

# Generated at 2022-06-14 02:30:50.463226
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import parse


# Generated at 2022-06-14 02:31:00.516642
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A(object):
        def __init__(self, a):
            super()

    class B(A):
        def __init__(self, b):
            super()

        def ff(self):
            def gg():
                super()
    """
    compile(code, '', 'exec')
    expected_code = """
    class A(object):
        def __init__(self, a):
            super(A, self)

    class B(A):
        def __init__(self, b):
            super(B, self)

        def ff(self):
            def gg():
                super(B, self)
    """
    assert SuperWithoutArgumentsTransformer().visit(parse(code)).dump() == parse(expected_code).dump()

# Generated at 2022-06-14 02:31:02.873041
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast

    class TestNodeTransformer(SuperWithoutArgumentsTransformer):
        pass


# Generated at 2022-06-14 02:31:09.915738
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ..utils import tests
    from .self_without_arguments import SelfWithoutArgumentsTransformer
    sample = tests.get_sample('simple_class.py')

    module = ast.parse(sample)
    transformer = SelfWithoutArgumentsTransformer()
    transformer.visit(module)
    sample = astor.to_source(module)
    module = ast.parse(sample)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(module)
    result = astor.to_source(module)


# Generated at 2022-06-14 02:31:14.295264
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:31:17.530112
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
super(A, self)
super(A, cls)
super()
    """
    expected_ast = ast.parse(source)
    tree = SuperWithoutArgumentsTransformer().visit(ast.parse(source))
    assert ast.dump(tree) == ast.dump(expected_ast)

# Generated at 2022-06-14 02:31:20.154050
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer
    """
    tree = ast.parse("super()")
    SuperWithoutArgumentsTransformer().visit(tree)
    assert(str(tree) == "super(__main__, self)")

# Generated at 2022-06-14 02:31:22.378253
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(None)


# Generated at 2022-06-14 02:31:34.218801
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class SuperWithoutArgumentsTransformer_Tester(SuperWithoutArgumentsTransformer):
        def run(self, tree: ast.AST) -> ast.AST:
            self._tree_changed = False
            self.visit(tree)
            return self._tree_changed

    text_1 = '''
if ''.startswith(''):
    def f():
        super()
'''
    text_2 = '''
if ''.startswith(''):
    def f():
        super(str, 'str', sep='')
'''
    exp_1 = '''
if ''.startswith(''):
    def f():
        super(Cls, self)
'''

# Generated at 2022-06-14 02:31:43.731251
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from .base import BaseNodeTransformer
    from ..utils.nodes import compare_nodes
    from ..transformers.remove_object import ObjectTransformer
    from ..transformers.fstrings import FStringsTransformer
    from ..transformers.remove_metaclass import RemoveMetaclassTransformer

    source = """
    class Foo(object):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    """
    expected_source = """
    class Foo:
        def __init__(self, *args, **kwargs):
            super(Foo, self).__init__(*args, **kwargs)
    """
    trees = source_to_nodes(source)

# Generated at 2022-06-14 02:31:44.462316
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:45.290037
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:46.566529
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:54.578288
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A():
        def __init__(self, a: int):
            pass
    """
    node = ast.parse(code)
    t = SuperWithoutArgumentsTransformer()
    t.visit(node)
    expected = """
    class A():
        def __init__(self, a: int):
            super(A, self)
            pass
    """
    assert astor.to_source(node) == expected
    t.visit(node)
    assert astor.to_source(node) == expected



# Generated at 2022-06-14 02:32:03.485398
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import get_ast, compare_ast
    from ..to_python import compile_ast


# Generated at 2022-06-14 02:32:08.011441
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast
    from ..transforms import TransformError
    from ..transforms.helpers import TransformErrorCollector

    # Test that code stays the same as it is not changed

# Generated at 2022-06-14 02:32:13.881064
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(2)
    tree = ast.parse(dedent('''
        class Test(object):
            def test(self):
                super()
    '''))
    transformer.visit(tree)
    assert transformer.tree_changed

# Generated at 2022-06-14 02:32:20.881243
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:32:29.478780
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('''
        class Parent:
            def __init__(self):
                super()
                super()
    ''')
    node = tree.body[0].body[0]
    super_node = node.body[0]
    assert len(super_node.args) == 0
    assert isinstance(super_node.args[0], ast.Name)
    assert super_node.args[0].id == 'Parent'
    assert isinstance(super_node.args[1], ast.Name)
    assert super_node.args[1].id == 'self'

# Generated at 2022-06-14 02:32:37.201257
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse(
        '''
        class Cls:
            def __init__(self):
                super()
        ''')
    tree_compiled = ast.parse(
        '''
        class Cls:
            def __init__(self):
                super(Cls, self)
        ''')
    trasf = SuperWithoutArgumentsTransformer()
    tree = trasf.visit(tree)
    assert ast.dump(tree) == ast.dump(tree_compiled)

# Generated at 2022-06-14 02:32:44.345137
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('class A:\n  def __init__(self):\n    super()\n')
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)
    assert transformer._tree_changed is True
    assert isinstance(new_tree, ast.AST)
    assert isinstance(new_tree.body[0], ast.ClassDef)
    assert isinstance(new_tree.body[0].body[0], ast.FunctionDef)
    assert isinstance(new_tree.body[0].body[0].body[0], ast.Expr)
    assert isinstance(new_tree.body[0].body[0].body[0].value, ast.Call)

# Generated at 2022-06-14 02:32:54.626353
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseNodeTransformer
    from typed_ast.ast3 import Call, ClassDef, FunctionDef, Name
    from ..exceptions import NotImplementedError
    # Testing for target
    transformer = SuperWithoutArgumentsTransformer()
    assert transformer.target == (2, 7)
    # Testing for visit_Call
    transformer = SuperWithoutArgumentsTransformer()
    tree = Call(Name(id='super'), [])
    new_tree = transformer.visit_Call(tree)
    assert isinstance(new_tree, Call)
    # Testing for visit_Call
    transformer = SuperWithoutArgumentsTransformer()
    tree = Call(Name(id='super'), [])
    tree.args = [ast.Name(id='__class__')]
    new_tree = transformer.visit_Call(tree)

# Generated at 2022-06-14 02:33:01.643780
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .helpers import get_ast
    from ..utils.helpers import compare_trees
    from ..compiler import Compiler
    from ..utils.tree import Tree
    ast_tree = get_ast('super()')
    expected_tree = get_ast('super(Cls, self)')
    tree = Tree(ast_tree)
    compiler = Compiler(tree)
    compiler._compile_class(SuperWithoutArgumentsTransformer())
    assert compare_trees(ast_tree, expected_tree)

# Generated at 2022-06-14 02:33:03.279711
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:33:24.661908
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    sample_code = """
        class B:
            def __init__(self, x, y):
                super().__init__(x, y)
    """
    expected_code = """
        class B:
            def __init__(self, x, y):
                super(B, self).__init__(x, y)
    """
    try:
        nodes = ast.parse(sample_code, mode='exec')
        obj = SuperWithoutArgumentsTransformer().visit(nodes)
        code = compile(obj, "", "exec")
        assert _get_co(code) == _get_co(expected_code)
    except ImportError:
        # in case typed_ast module is not installed
        pass


# Generated at 2022-06-14 02:33:31.483020
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = 'class A: def f(self): super()'
    tree = ast.parse(source)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert(ast.dump(tree) == "Module(body=[ClassDef(name='A', bases=[], keywords=[], body=[FunctionDef(name='f', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='A', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]))], decorator_list=[], returns=None)])])")

# Generated at 2022-06-14 02:33:32.160716
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:42.542406
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.source import source_to_unicode
    from .base import BaseNodeTransformer
    from .decorators import DecoratorTransformer
    from .arguments import ArgumentTransformer

    tree = ast.parse(source_to_unicode("""
        class MySuper(Super):
            @staticmethod
            def monkey(arg) -> None:
                super()
    """), mode="eval")
    for transformer in DecoratorTransformer, ArgumentTransformer:
        transformer(tree).visit(tree)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    call = list(ast.walk(tree))[-2]
    assert isinstance(call, ast.Call)
    assert call.args[0].id == 'MySuper'
    assert call.args

# Generated at 2022-06-14 02:33:43.494280
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:50.004432
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3  # noqa # pylint: disable=unused-import

    class DummyTree:
        pass

    tree = DummyTree()


# Generated at 2022-06-14 02:33:51.408313
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:53.042014
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:54.286846
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Tested in test_transformer.py
    pass

# Generated at 2022-06-14 02:33:55.066755
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:33.489976
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import astunparse

    source = """
    class Spam:
        def __init__(self, who):
            super(Spam, self).__init__()
            super(Spam, self).__init__(who)
            super().__init__()
            super().__init__(who)
            super(who=who)
            super(who=who, me=me).__init__()
    """
    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    result = astunparse.unparse(tree)

# Generated at 2022-06-14 02:34:45.518099
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import unittest
    from . import get_ast

    class TestSuperWithoutArgumentsTransformer(unittest.TestCase):
        def check(self, src: str, expected: str) -> None:
            from ..utils.helpers import as_python
            module = ast.parse(src)
            SuperWithoutArgumentsTransformer(module).visit(module)
            self.assertEqual(as_python(module), expected)

        def test_super(self) -> None:
            code = """
                class Cls(object):
                    def __init__(self):
                        super()
            """
            self.check(code, """
                class Cls(object):
                    def __init__(self):
                        super(Cls, self)
            """)


# Generated at 2022-06-14 02:34:50.278253
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..unittest_tools import assert_compiled_output

    assert_compiled_output(SuperWithoutArgumentsTransformer,
        target_tree=ast.parse(
            '''
        class Cls:
            def method(self):
                super()
            @classmethod
            def class_method(cls):
                super()
        '''
        ),
        expected_tree=ast.parse(
            '''
        class Cls:
            def method(self):
                super(Cls, self)
            @classmethod
            def class_method(cls):
                super(Cls, cls)
        '''
        )
    )

# Generated at 2022-06-14 02:34:57.151292
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code = """
    class A:
        def __init__(self):
            super()
            """
    tree = ast.parse(code)

    # Constructor without no parameters
    x = SuperWithoutArgumentsTransformer()

    # The first time visit should return "True"
    assert x.visit(tree) is True

    # The second time visit should return "False" because there is no change
    assert x.visit(tree) is False

# Generated at 2022-06-14 02:34:59.667056
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer."""

# Generated at 2022-06-14 02:35:11.039865
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_tree
    from ..utils.helpers import pretty_print_ast
    tree = source_to_tree('''
        class A(object):
            def f(self):
                super()
    ''')
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    ast.fix_missing_locations(tree)
    assert pretty_print_ast(tree) == '''
    class A(object):
        def f(self):
            super(A, self)
    '''

# Generated at 2022-06-14 02:35:17.002885
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.test_utils import source_to_nodes, nodes_to_source

    source = """
    class A:
        def __call__(self):
            super()
    """

    pyversion = (2, 7)
    nodes = source_to_nodes(pyversion, source)

    tr = SuperWithoutArgumentsTransformer(pyversion, nodes, {})
    tr.visit(nodes[0])
    result = nodes_to_source(pyversion, nodes[0], False)

    expected = """
    class A:
        def __call__(self):
            super(A, self)
    """
    assert result == expected

# Generated at 2022-06-14 02:35:32.194129
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import Code
    from .base import BaseNodeTransformer
    from .base import NodeTransformer

    tree = ast.parse(Code(
        """
    class A:
        def fn(self):
            super()
    """
    ))  # type: ast.AST

    transpiler = BaseNodeTransformer()
    transpiler.visit(tree)

    assert Code(ast.dump(transpiler.tree)) == Code(
        """
    class A(object):
        def fn(self):
            super(A, self)
    """
    )

    node_transformer = NodeTransformer(tree)
    c = node_transformer.visit(node_transformer.tree.body[0].body[0])


# Generated at 2022-06-14 02:35:33.176219
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:40.278365
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..ssa import build_ssa
    from ..utils.source import source_to_code

    code = """
    class Bar:
        def __init__(self):
            super()
            self._p = 1
    """

    expected_code = """
    class Bar:
        def __init__(self):
            super(Bar, self)
            self._p = 1
    """

    tree = build_ssa(source_to_code(code))
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    assert expected_code == code_gen.to_source(tree)

# Generated at 2022-06-14 02:36:49.320219
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.testing import assert_transformed_ast

# Generated at 2022-06-14 02:36:49.935509
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:36:50.568849
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:51.146166
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:52.310690
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_src


# Generated at 2022-06-14 02:36:59.787094
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    fixture = """
        class A:
            def __init__(self):
                super().__init__()
                super().x()
        """
    tree = ast.parse(fixture)
    transformer = SuperWithoutArgumentsTransformer(tree, ())
    transformer.visit(tree)
    
    expected = """
        class A:
            def __init__(self):
                super(A, self).__init__()
                super(A, self).x()
        """
    expected = ast.parse(expected)
    assert are_ast_equal(tree, expected)

# Generated at 2022-06-14 02:37:07.428967
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree1 = ast.parse('super()')
    tree2 = ast.parse('super(cls, self)')
    tree3 = ast.parse('super()')
    cls1 = ast.parse('class A: pass')
    cls2 = ast.parse('class A: def init(): pass')
    cls3 = ast.parse('class A: def init(self): pass')
    cls4 = ast.parse('class A: def init(cls): pass')
    assert SuperWithoutArgumentsTransformer(None).visit(tree1) == tree2
    assert SuperWithoutArgumentsTransformer(cls1).visit(tree3) is tree3
    assert SuperWithoutArgumentsTransformer(cls2).visit(tree3) is tree3

# Generated at 2022-06-14 02:37:07.951946
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:09.430184
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:37:13.324006
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("class Bar(Foo):\n    def __init__(self):\n        super()")
    TreeRebuilder(tree).run()
    assert dump_python_source(tree) == "class Bar(Foo):\n    def __init__(self):\n        super(Bar, self)"

