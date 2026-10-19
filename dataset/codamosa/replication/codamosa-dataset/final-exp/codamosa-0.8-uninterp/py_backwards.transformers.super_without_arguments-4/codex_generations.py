

# Generated at 2022-06-14 02:28:09.773312
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class B:
        def __init__(self):
            super()
        def foo(self):
            super()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:28:11.700385
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:20.738825
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode
    from ..utils.transformer import Transformer

    text = source_to_unicode("""
    class Cls(object):
        def __init__(self):
            super()
    """)
    tree = ast.parse(text)
    transformer = Transformer(tree, SuperWithoutArgumentsTransformer)
    assert source_to_unicode(transformer.tree) == source_to_unicode("""
    class Cls(object):
        def __init__(self):
            super(Cls, self)
    """
    )

# Generated at 2022-06-14 02:28:29.148680
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.Call(
        func=ast.Name(id='super'),
        args=[],
        keywords=[]
    )  # type: ast.AST
    expected = ast.Call(
        func=ast.Name(id='super'),
        args=[
            ast.Name(id='Cls'),
            ast.Name(id='self')
        ],
        keywords=[]
    )  # type: ast.AST

    tree = ast.parse("def some_method(self): super()")
    tree = SuperWithoutArgumentsTransformer(tree).visit(tree)

    got = tree.body[0].body[0]
    assert expected == got

# Generated at 2022-06-14 02:28:35.167382
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import ast as pyast
    ast_tree1 = pyast.parse('''class Foo(Super):
    def foo(self):
        super()''')
    ast_tree2 = pyast.parse('''class Foo(Super):
    def foo(self):
        super()''')

    transformer = SuperWithoutArgumentsTransformer(ast_tree1)
    transformer.visit(ast_tree1)    
    transformer.visit(ast_tree2)
    assert transformer.tree_changed() == True
    assert ast_tree1 == ast_tree2



# Generated at 2022-06-14 02:28:37.722242
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils import parse_ast_tree


# Generated at 2022-06-14 02:28:38.385041
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:42.285228
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast as sta
    from ..utils.source import source_to_code as stc


# Generated at 2022-06-14 02:28:43.574517
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:48.683850
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.codegen import to_source
    from ..utils.helpers import from_code
    module_node = from_code('super()')
    SuperWithoutArgumentsTransformer().visit(module_node)
    assert to_source(module_node) == 'super(Cls, self)'

# Generated at 2022-06-14 02:28:56.329723
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer"""
    code_in = inspect.cleandoc('''\
        class Foo():
            def __init__(self):
                super()''')
    # code_out should be identical to code_in
    code_out = inspect.cleandoc('''\
        class Foo():
            def __init__(self):
                super(Foo, self)''')
    tree_in = ast.parse(code_in)
    tree_out = ast.parse(code_out)
    tree = SuperWithoutArgumentsTransformer().visit(tree_in)
    assert ast.dump(tree, include_attributes=False) == ast.dump(tree_out, include_attributes=False)

# Generated at 2022-06-14 02:28:58.012785
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:07.678138
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode as u
    from .util import round_trip
    from .base import BaseNodeTransformer

    tree = BaseNodeTransformer.parse_tree(u('''
        class A:
            def __init__(self):
                super()
    '''))

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert u(round_trip(tree)) == u('''
        class A:
            def __init__(self):
                super(A, self)
    ''')

# Generated at 2022-06-14 02:29:08.838751
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:09.926147
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:20.749115
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A(object):
            def __init__(self):
                super()
        class B(object):
            def get_a(self):
                super()
    """
    expected_code = """
        class A(object):
            def __init__(self):
                super(A, self)
        class B(object):
            def get_a(self):
                super(B, self)
    """
    # Parse code
    tree = ast.parse(code)  # type: ast.Module

    # Apply transform
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)  # type: ast.Module

    # Compare transformed AST to expected AST
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:29:29.279764
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    if sys.version_info < (3, 7):
        return

    from typed_ast import ast3 as ast

    transformer = SuperWithoutArgumentsTransformer()

    node = ast.Call(func=ast.Name(id='super'), args=[])
    transformer.visit(ast.FunctionDef(args=ast.arguments(args=[ast.arg(arg='self', annotation=None)]),
                                      body=[node],
                                      decorator_list=[],
                                      name='foo',
                                      returns=None))

    assert node.args[0].id == 'Cls', 'failed to replace super() in foo()'
    assert node.args[1].id == 'self', 'failed to replace super() in foo()'

    node = ast.Call(func=ast.Name(id='super'), args=[])
   

# Generated at 2022-06-14 02:29:36.082241
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class A:
            def __init__(self):
                super()

        class B:
            def __init__(cls):
                super()
    '''
    tree = ast.parse(code)

    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)

    exec(compile(new_tree, filename="<ast>", mode="exec"), globals())  # type: ignore

# Generated at 2022-06-14 02:29:37.102158
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:37.707186
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:29:42.865525
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:29:44.297760
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:46.013467
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source

# Generated at 2022-06-14 02:29:52.910812
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Tests use missing class/function definition
    # to prevent wrapping logic
    super_transformer = SuperWithoutArgumentsTransformer()

    class_node = ast.ClassDef(name='Cls', body=[])
    func_node = ast.FunctionDef(name='test_func', args=ast.arguments(args=[ast.Name(id='self', ctx=ast.Param())], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[], decorator_list=[], returns=None)

    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])
    class_node.body = [func_node]
    func_node.body = [node]
    
    super_transformer.visit

# Generated at 2022-06-14 02:30:00.913915
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.test_helpers import run_transformer_test

    class TNode:
        """TNode stands for transformed node"""
        def __init__(self, code: str, expected_code: str):
            self.code = code
            self.expected_code = expected_code


# Generated at 2022-06-14 02:30:04.896235
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    fixture = """
        class A:
            def __init__(self):
                super()

    """
    expected = """
        class A:
            def __init__(self):
                super(A, self)
    """
    tree = ast.parse(fixture)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert astor.to_source(tree) == expected



# Generated at 2022-06-14 02:30:05.698544
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:11.316431
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''class Test:
    def test(self):
        super().test()
'''

    tree = ast.parse(code)
    p = SuperWithoutArgumentsTransformer()
    p.visit(tree)

    code2 ='''class Test:
    def test(self):
        super(Test, self).test()
'''
    tree2 = ast.parse(code2)
    assert compare_ast(tree, tree2)

# Generated at 2022-06-14 02:30:12.582653
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import to_source


# Generated at 2022-06-14 02:30:14.639207
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:19.856124
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:27.992773
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Unit test for constructor of class SuperWithoutArgumentsTransformer
    from ..compiler import PythonCompiler
    from ..base import BaseTransformer
    from ..compilation import CompilationState
    from ..utils.helpers import get_ast
    from ..utils.helpers import set_positions_recursively
    
    code = """class A:
        def __init__(self):
            super().__init__()"""

    tree = get_ast(code)
    set_positions_recursively(tree)
    
    compiler = PythonCompiler(tree, CompilationState())
    module = compiler.compile()

# Generated at 2022-06-14 02:30:34.022826
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Src:
        class Cls:
            def __init__(self):
                super()  #@

    tree = ast.parse(inspect.getsource(Src))
    tree = SuperWithoutArgumentsTransformer(tree, Src).visit(tree)
    assert ast.dump(tree) == parse(
        '''
        class Cls:
            def __init__(self):
                super(Cls, self)
        '''
    )


# Generated at 2022-06-14 02:30:36.544386
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.testing import run_transformer
    result = run_transformer(SuperWithoutArgumentsTransformer, 'test', 'super()')
    assert result == 'super(Cls, self)'

# Generated at 2022-06-14 02:30:45.527895
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.python_ast_utils import py_ast
    from ..utils import helpers
 
    p = """
        class Parent(object):
            pass
        class Child(Parent):
            def __init__(self):
                super()
    """
    tree = py_ast(p)
    tr = SuperWithoutArgumentsTransformer(tree)
    tr.visit(tree)
    actual = helpers.pretty(tree)
    expected = """
        class Parent(object):
            pass
        
        class Child(Parent):
            def __init__(self):
                super(Child, self)
    """
    assert actual == expected

# Generated at 2022-06-14 02:30:47.980461
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile as compile
    assert compile("""
        class A:
            def __init__(self):
                super()
    """)
    
    assert compile("""
        class A:
            def m(self):
                super()
    """).strip() == 'class A:\n    def m(self):\n        super(A, self)'


# Generated at 2022-06-14 02:30:52.130676
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('class Cls: def func(self): super()')

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert str(tree) == "class Cls:\n    def func(self):\n        super(Cls, self)"

# Generated at 2022-06-14 02:30:58.531517
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # TestCase1
    func = "super()"
    expected = "super(__cls__, __self__)"
    node = ast.parse(func)
    SuperWithoutArgumentsTransformer().visit(node)
    result = compile(node, '', 'exec')
    assert(expected == str(result.co_consts[0]))

    # TestCase2

# Generated at 2022-06-14 02:31:07.472436
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.ast_helpers import get_ast
    from ..utils.helpers import compile_func
    from ..utils.gensys import gensys
    from .base import BaseNodeTransformer
    import sys
    import random

    # Sample class
    class Dummy(object):
        def __init__(self):
            self.foo = 'bar'

        def doit(self, a: int, b: int) -> int:
            return a + b + self.foo
    
    class Cls(BaseNodeTransformer):
        def __init__(self, tree: ast.AST):
            self._tree = tree


# Generated at 2022-06-14 02:31:13.217383
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class A:
        def foo(self):
            super()
    '''
    expected_code = '''
    class A:
        def foo(self):
            super(A, self)
    '''

    t = Transpile()
    t.append(SuperWithoutArgumentsTransformer)
    new_code = t.transpile_code(code)

    assert new_code == expected_code

# Generated at 2022-06-14 02:31:29.303598
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class Foo(object):
            def __init__(self):
                super()
    '''
    expected_output = '''
        class Foo(object):
            def __init__(self):
                super(Foo, self)
    '''
    t = SuperWithoutArgumentsTransformer()
    t.visit(ast.parse(code))
    assert expected_output == astor.to_source(t.tree)  # type: ignore

# Generated at 2022-06-14 02:31:33.144869
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''super()'''

    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)

    assert 'super(Cls, self)' in astor.to_source(tree)

# Generated at 2022-06-14 02:31:34.397300
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:35.725289
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:37.000756
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:42.111229
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("super()")
    SuperWithoutArgumentsTransformer().visit(node)
    assert ast.dump(node) == 'Module(body=[Expr(value=Call(func=Name(id=\'super\', ctx=Load()), args=[Name(id=\'Cls\', ctx=Load()), Name(id=\'self\', ctx=Load())], keywords=[], starargs=None, kwargs=None))])'

# Generated at 2022-06-14 02:31:49.757610
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A:
            def f(self):
                super()
        """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    expected_code = """
        class A:
            def f(self):
                super(A, self)
        """
    result_code = astor.to_source(tree).strip()
    assert result_code == expected_code.strip()



# Generated at 2022-06-14 02:32:00.905213
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.ast_helpers import parse_ast_tree
    from ..utils.ast_helpers import format_ast_tree

    code = """
        class Foo:
            def __init__(self):
                super()
    """
    tree = parse_ast_tree(code)
    SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:32:03.158859
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import get_ast
    from ..fixes import FixSuperWithoutArguments


# Generated at 2022-06-14 02:32:11.064166
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Simple test for constructor of class SuperWithoutArgumentsTransformer.
    """
    from typed_ast import ast3 as ast
    from ..utils.source import source_to_unicode
    from . import BaseNodeTransformer
    tree = ast.parse(source_to_unicode('''\
        class A:
            def foo(self):
                super()
        '''))
    assert BaseNodeTransformer.check_tree(tree)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert BaseNodeTransformer.check_tree(tree)

# Generated at 2022-06-14 02:32:29.870332
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import transpile
    from ..utils.helpers import load_ast_tree


# Generated at 2022-06-14 02:32:35.991512
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    before = """
try: True
except: super()
"""
    after = """
try: True
except: super(UnboundLocalError, self)
"""
    # convert the source code
    result = compile_to_ast(before, True)
    # and make sure it's the same
    assert ast.dump(result) == ast.dump(ast.parse(after))

# Generated at 2022-06-14 02:32:43.974732
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import setup_ast, get_ast_diff
    from ..utils.api import compile_source, load_source

    source = """
        class Foo(object):
            def __init__(self, x, y):
                super().__init__()

    """

    expected = """
        class Foo(object):
            def __init__(self, x, y):
                super(Foo, self).__init__()

    """

    tree = setup_ast(source)
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)
    assert transformer.tree_changed is True
    assert not get_ast_diff(tree, new_tree)
    assert compile_source(source, '<test>', 'exec') == compile_source(expected, '<test>', 'exec')



# Generated at 2022-06-14 02:32:45.741055
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()


# Generated at 2022-06-14 02:32:47.461444
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:48.173094
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:32:52.484751
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert 'super(Cls, self)' == astor.to_source(tree)



# Generated at 2022-06-14 02:32:53.089967
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:59.425389
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ...utils.node_utils import node_to_str
    code = 'class A(object):\n    def m(self): super()\n'
    expected_code = 'class A(object):\n    def m(self): super(A, self)\n'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert node_to_str(tree) == expected_code

# Generated at 2022-06-14 02:33:06.790572
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse('class Foo: def __init__(self, x): super()')
    tree2 = ast.parse('class Foo: def __init__(self, x): super(Foo, self)')
    node = tree.body[0].body[1]
    node2 = tree2.body[0].body[1]
    x = SuperWithoutArgumentsTransformer()
    x.visit(tree)
    assert ast.dump(node) == ast.dump(node2)
    assert x._tree_changed

# Generated at 2022-06-14 02:33:30.485634
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test(SuperWithoutArgumentsTransformer):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            return super().visit_Call(node) # type: ignore

    node = ast.parse('super()').body[0]
    Test().visit(node)

    assert isinstance(node.func, ast.Name)

# Generated at 2022-06-14 02:33:31.558126
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:32.088792
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:33.739571
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    q = SuperWithoutArgumentsTransformer(2, 7)
    assert(q.target == (2, 7))

# Generated at 2022-06-14 02:33:34.412287
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:41.405490
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class DummyNode(ast.AST):
        _fields = ['a']

    transformer = SuperWithoutArgumentsTransformer(DummyNode())
    node = ast.Call(func=ast.Name('super', ctx=ast.Load), args=[], keywords=[])
    super_without_args_transformed_node = transformer.visit_Call(node)
    assert super_without_args_transformed_node is node
    assert transformer._tree_changed is False


# Generated at 2022-06-14 02:33:43.389909
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.test_utils import transform, node_equal, node_to_str


# Generated at 2022-06-14 02:33:46.199468
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("""super()""", mode='exec')
    SuperWithoutArgumentsTransformer(node, (2, 7)).visit(node)
    assert "super(Cls, func)" in astunparse.unparse(node)

# Generated at 2022-06-14 02:33:58.894684
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    
    a = ast.parse('super()')
    a_tree = ast.parse('class Test(object): def foo(self): super()')
    a_new = SuperWithoutArgumentsTransformer(a, 2).visit(a)
    a_new_tree = SuperWithoutArgumentsTransformer(a_tree, 2).visit(a_tree)

    assert_equal(type(a_new), ast.Call)
    assert_equal(type(a_new.func), ast.Name)
    assert_equal(a_new.func.id, 'super')
    assert_equal(len(a_new.args), 2)
    assert_equal(type(a_new.args[0]), ast.Name)
    assert_equal(a_new.args[0].id, 'Test')

# Generated at 2022-06-14 02:34:02.349360
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    test_ast = ast.parse('""')
    with pytest.raises(NodeNotFound):
        transformer.visit_Call(test_ast)

# Generated at 2022-06-14 02:34:50.743528
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Testing SuperWithoutArgumentsTransformer"""
    from ..utils.source import source_to_unicode as u


# Generated at 2022-06-14 02:35:03.331831
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import BaseCompilerTest

    class Compiler(BaseCompilerTest):
        def test_method_call(self):
            self.compile(
                '''
                class A:
                    def __init__(self):
                        super()
                ''',
                '''
                class A:
                    def __init__(self):
                        super(A, self)
                '''
            )

        def test_method_call_with_args(self):
            self.compile(
                '''
                class A:
                    def __init__(self, arg):
                        super()
                ''',
                '''
                class A:
                    def __init__(self, arg):
                        super(A, self)
                '''
            )


# Generated at 2022-06-14 02:35:08.579306
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .transformer_util import run_test_ast_transformer

    source = """
s = super()
"""
    expected = """
s = super(Cls, self)
"""

    @run_test_ast_transformer(
        source,
        expected,
        [SuperWithoutArgumentsTransformer],
        "Cls"
    )
    def does_nothing(self):
        pass

# Generated at 2022-06-14 02:35:12.468769
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast


# Generated at 2022-06-14 02:35:16.071750
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import to_code
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer()


# Generated at 2022-06-14 02:35:24.088710
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import print_node
    from .base import BaseNodeTransformer
    from .arguments import ArgumentsTransformer
    from .func import FuncTransformer
    from .classdef import ClassDefTransformer

# Generated at 2022-06-14 02:35:30.485879
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    t = Transpiler()
    t.register_transformer(SuperWithoutArgumentsTransformer)
    t.transpile_code('super()')

    assert t.get_output() == 'super(Cls, self)\n'


# Integration test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:39.886831
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    from ..utils.source import source_to_nodes
    from ..utils.ast import compare_ast

    class Test(unittest.TestCase):
        def test(self):
            source = """
                class A:
                    def __init__(self):
                        super()

                    def m(self):
                        super()
            """

            nodes = tuple(source_to_nodes(source))
            nodes = SuperWithoutArgumentsTransformer(None).visit_sequence(nodes)


# Generated at 2022-06-14 02:35:41.457975
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    obj = SuperWithoutArgumentsTransformer(None, None)
    assert type(obj) == SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:49.482793
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse('super()', '<test>', 'exec')
    SuperWithoutArgumentsTransformer().visit(tree)

    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Call)
    assert isinstance(tree.body[0].value.func, ast.Name)
    assert tree.body[0].value.func.id == 'super'
    assert len(tree.body[0].value.args) == 2
    assert isinstance(tree.body[0].value.args[0], ast.Name)
    assert tree.body[0].value.args[0].id == 'Cls'
    assert isinstance(tree.body[0].value.args[1], ast.Name)


# Generated at 2022-06-14 02:37:27.324159
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
            class Cls:
                def __init__(self, a):
                    super()
                    print(super)
            """

    expected_code = """
        class Cls:
            def __init__(self, a):
                super(Cls, self)
                print(super)
        """

    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)

    print(ast.dump(tree))

    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 02:37:30.725491
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'class A:def f():super()'
    node = ast.parse(code)

    SuperWithoutArgumentsTransformer().visit(node)

    assert node.body[0].body[0].value.args[0].id == 'A'
    assert node.body[0].body[0].value.args[1].id == 'self'

# Generated at 2022-06-14 02:37:31.193973
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:33.832052
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test that the constructor will set the correct values"""
    x = SuperWithoutArgumentsTransformer(None)
    assert x._tree_changed == False

# Unit tests for class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:35.181286
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:40.626025
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    CODE = """class A(object):
        def __init__(self, b):
            super()
            
            self.b = b
            
            def extra(self):
                super()
                
                def extra_extra(self):
                    super() 
    """
    tree = ast.parse(CODE)
    super_ = SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(super_, filename='<ast>', mode='exec'))

    assert A().b == None

# Generated at 2022-06-14 02:37:45.965501
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import assert_source
    from ..utils.source import Source

    source = Source("""
        class MyClass(object):
            def method(self, cls):
                super()
    """)

    tree = source.tree

    # type: ignore
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer(tree)
    tree = super_without_arguments_transformer.visit(tree)

    assert_source(tree, """
        class MyClass(object):
            def method(self, cls):
                super(MyClass, self)
    """)

# Generated at 2022-06-14 02:37:50.288099
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = '''
        class Foo(object):
            def __init__(self, a):
                super()
                
            def bar(self):
                super()
    '''
    expected = '''
        class Foo(object):
            def __init__(self, a):
                super(Foo, self)
                
            def bar(self):
                super(Foo, self)
    '''
    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    assert(expected == transformer.to_source())



# Generated at 2022-06-14 02:37:55.630532
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Cls(object):
            def method(self):
                super()
    """
    transformer = SuperWithoutArgumentsTransformer(code, (2, 7))
    transformer.run()
    assert transformer.tree_changed
    assert transformer.get_new_code() == """
        class Cls(object):
            def method(self):
                super(Cls, self)
    """

# Generated at 2022-06-14 02:37:57.374324
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
