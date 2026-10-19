

# Generated at 2022-06-14 02:27:59.047295
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast


# Generated at 2022-06-14 02:28:09.644587
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode

    source = source_to_unicode("""
    class A(object):
        def f(self):
            super()

    class B(A):
        def g(self):
            super()
        
        @classmethod
        def h(cls):
            super()
    """)
    tree = ast.parse(source)  # type: ignore
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)  # type: ignore


# Generated at 2022-06-14 02:28:12.874195
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_src, print_tree

# Generated at 2022-06-14 02:28:13.902075
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:18.962875
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A:
        def __init__(self):
            super().__init__()
    """

    module: ast.Module = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer.run(module)
    assert isinstance(tree, ast.Module)
    code2 = compile(tree, '<string>', 'exec')
    exec(code2)


# Generated at 2022-06-14 02:28:30.850353
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3

    code = """
    class C:
        def f(self):
            super()
    """
    tree = ast3.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert transformer.is_changed()

# Generated at 2022-06-14 02:28:41.188497
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import Compiler
    from ..run_py import run_py_code
    from ..utils.helpers import get_first_node_name
    from textwrap import dedent

    source = dedent("""
    class A(object):
        def __init__(self):
            super()
    """)

    tree = Compiler(source, {}, target=SuperWithoutArgumentsTransformer.target)._tree

    # Cases:
    # 1. super() inside class A, inside constructor
    expected_result = "super(A, self)"

    node = tree.body[0].body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)

# Generated at 2022-06-14 02:28:42.054246
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:43.180295
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:44.557830
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:55.465039
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..compiler import compile
    from ..utils import python_version

    code = """
            class A:
                def __init__(self, x):
                    super()
            """
    c = compile(code, python_version(2, 7))
    assert 'super(A, self)' in str(c)

    code = """
            def test():
              def __init__(x):
                  super()
            """
    try:
        c = compile(code, python_version(2, 7))
        assert False
    except NodeNotFound:
        assert True

    code = """
            super()
            """
    try:
        c = compile(code, python_version(2, 7))
        assert False
    except NodeNotFound:
        assert True

# Generated at 2022-06-14 02:29:01.533624
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_isolated
    snippet = '''
        class Test:
            def __init__(self):
                super()
    '''
    expected = '''
        class Test:
            def __init__(self):
                super(Test, self)
    '''
    assert compile_isolated(snippet, 'main', 'exec') == expected


# Generated at 2022-06-14 02:29:08.577265
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import typed_ast.ast3 as ast

    code = """
        class Some(object):
            def do_something(self):
                super()
        
        class Some(object):
            def do_something(something):
                super()
        
        class Some(object):
            def do_something(something):
                super().do_something()
        
        def do_something(self):
            super()
        
        def do_something(something):
            super()
    """

# Generated at 2022-06-14 02:29:17.095977
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    t = ast.parse('super()')
    assert ast.dump(t) == "Expr(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))"
    SuperWithoutArgumentsTransformer(2, 7).visit(t)
    assert ast.dump(t) == "Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))"

# Generated at 2022-06-14 02:29:20.500910
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer.apply_on(
        'class Test:def __init__(self):super()') == 'class Test:def __init__(self):super(Test, self)'

# Generated at 2022-06-14 02:29:26.241226
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """class C:
    def __init__(self):
        super()
        """

    node = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(node)

    expected_code = """class C:
    def __init__(self):
        super(C, self)
        """

    expected_node = ast.parse(expected_code)

    assert ast.dump(node) == ast.dump(expected_node)



# Generated at 2022-06-14 02:29:37.301592
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:29:47.197654
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import parse, compare_ast

    from . import Transformer, SuperWithoutArgumentsTransformer

    source = """
        class Cls(object):
            def method(self):
                super()

            @classmethod
            def clsmethod(cls):
                super()

        """
    expected = """
        class Cls(object):
            def method(self):
                super(Cls, self)

            @classmethod
            def clsmethod(cls):
                super(Cls, cls)

        """

    tree = parse(source)
    transformer = Transformer(2, 7)
    transformer.add_transformer(SuperWithoutArgumentsTransformer)
    new_tree = transformer.transform(tree)

    compare_ast(new_tree, expected)

# Generated at 2022-06-14 02:29:57.794400
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree_before = ast.parse(textwrap.dedent('''\
        class A:
            def __init__(self):
                super()
    '''))

    tree_after = ast.parse(textwrap.dedent('''\
        class A:
            def __init__(self):
                super(A, self)
    '''))

    transformer = SuperWithoutArgumentsTransformer()
    tree_transformed = transformer.visit(tree_before)
    assert ast.dump(tree_transformed, include_attributes=False) == ast.dump(tree_after, include_attributes=False)

    tree_before = ast.parse(textwrap.dedent('''\
        class A:
            def f(self):
                super()
    '''))


# Generated at 2022-06-14 02:29:59.087551
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astunparse

# Generated at 2022-06-14 02:30:14.349810
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = parse(
        'class X:\n'
        '    def method(self):\n'
        '        super()\n'
        'class Y:\n'
        '    def method(self):\n'
        '        super()\n'
        'class Z:\n'
        '    def method(self):\n'
        '        super(X, self)\n'
    )

    optimizer = SuperWithoutArgumentsTransformer(tree)
    optimizer.optimize()

    source = tree_to_source(tree)

# Generated at 2022-06-14 02:30:23.986786
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # type: () -> None
    import shutil
    from ..utils.helpers import node_to_tuple, mock_tree

    # setup
    transformer = SuperWithoutArgumentsTransformer()
    tree = mock_tree()
    args = None

# Generated at 2022-06-14 02:30:25.219922
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:30:30.134484
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = ast.parse('super()')
    tree = SuperWithoutArgumentsTransformer().visit(code)
    assert tree == ast.parse('super(Cls, self)')

    code = ast.parse('super')
    with pytest.raises(AssertionError):
        SuperWithoutArgumentsTransformer().visit(code)


# Generated at 2022-06-14 02:30:37.972563
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from python_minifier.utils.helpers import assert_equal_node
    
    # given
    class MyVisitor(SuperWithoutArgumentsTransformer):
        def __init__(self):
            self.assert_count = 0
        def visit_Expr(self, node):
            assert_equal_node(
                node, ast.Expr(value=ast.Call(func=ast.Name(id='super', ctx=ast.Load()), 
                                 args=[ast.Name(id='MainClass', ctx=ast.Load()), 
                                 ast.Name(id='self', ctx=ast.Load())], keywords=[], starargs=None, kwargs=None))
            )
            self.assert_count += 1

# Generated at 2022-06-14 02:30:39.949614
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:50.549751
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .util import parse, roundtrip
    from typing import List

    class Test(ast.AST):
        _fields = ('value', 'test', 'body', 'orelse')
        _attributes = ('lineno', 'col_offset', 'end_lineno', 'end_col_offset')

        def __init__(self, value: Any, test: Any, body: List[ast.stmt], orelse: List[ast.stmt]) -> None:
            self.value = value
            self.test = test
            self.body = body
            self.orelse = orelse

    class TestCall(ast.AST):
        _fields = ('func', 'args', 'keywords', 'starargs', 'kwargs')

# Generated at 2022-06-14 02:30:51.759550
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor


# Generated at 2022-06-14 02:30:52.722807
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:00.535223
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import textwrap
    from .transformers import ClassDefTransformer
    from ..utils.helpers import TreeInstance,  ParseError
    from ..utils.tree import get_trees
    from astunparse import unparse
    from typing import List

    with open('test_super_without_arguments.py', 'r') as fread:
        test_file_contents = fread.read()

    # Make sure our transformer handles other transformers in code
    transformer_class_in_code = textwrap.dedent('''
    class Test1(Parent):
        def __init__(self):
            super().__init__()
    ''')

    # Make sure that our transformer will fail if it can't find a class for the super()

# Generated at 2022-06-14 02:31:11.252868
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_to_ast
    source = 'class D(object): def d(self): super()'
    ast_tree = compile_to_ast(source, target=(2, 7))
    tree = SuperWithoutArgumentsTransformer().walk(ast_tree)
    source = 'class D(object): def d(self): super(D, self)'
    tree_new = compile_to_ast(source, target=(2, 7))
    assert ast.dump(tree_new) == ast.dump(tree)

# Generated at 2022-06-14 02:31:11.835445
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:20.223414
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_node
    from ..utils.helpers import get_ast_node_name
    from ..utils.tree import node_to_str

    source = '''
    class Foo(object):
        
        def __init__(self):
            super().__init__()

        def bar(self):
            super().hello()
   
    '''

    node = source_to_node(source)
    transformer = SuperWithoutArgumentsTransformer()
    node = transformer.visit(node)

    assert isinstance(node.body[0].body[0].value.args[0], ast.Name)
    assert get_ast_node_name(node.body[0].body[0].value.args[0]) == 'Foo'

# Generated at 2022-06-14 02:31:31.062991
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..parser import parse

    code = "super()"
    tree = parse(code)

    node = tree.body[0].value
    assert isinstance(node, ast.Call)
    assert isinstance(node.func, ast.Name)
    assert node.func.id == 'super'
    assert len(node.args) == 0

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(node)
    assert isinstance(node.args[0], ast.Name)
    assert node.args[0].id == 'Cls'
    assert isinstance(node.args[1], ast.Name)
    assert node.args[1].id == 'self'
    assert transformer.tree_changed is True

# Generated at 2022-06-14 02:31:32.169526
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile

# Generated at 2022-06-14 02:31:38.505002
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import parse
    (tree, _) = parse(r"""
    def foo(self):
        super()
        """
    )
    fixer = SuperWithoutArgumentsTransformer(tree)
    fixed = fixer.visit(tree)
    assert fixed.body[0].body[0].value.args[0].id == 'Test'


# Generated at 2022-06-14 02:31:46.567809
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_
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
    tree = compile_(code, '<test>', 'exec')
    node = tree.body[0].body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert len(node.value.args) == 2
    assert node.value.func.id == 'super'
    assert isinstance(node.value.args[0], ast.Name)
    assert node.value.args[0].id == 'A'
    assert isinstance

# Generated at 2022-06-14 02:31:55.843273
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast.ast3 import parse
    from . import NodeTransformerTestMixin

    class Test(NodeTransformerTestMixin):

        TRANSFORMER = SuperWithoutArgumentsTransformer

        def test_func_inside_class(self):
            code = "class Test:\n    def test(self):\n        super()"
            tree = parse(code)
            self.check_transformer(tree, code)
            self.check_transformer(tree, code)

        def test_func_outside_class(self):
            code = "def test():\n    super()"
            tree = parse(code)
            self.check_transformer(tree, code)
            self.check_transformer(tree, code)

    Test.run_tests()

# Generated at 2022-06-14 02:32:02.852541
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import get_ast
    from ..samples import SUPER_NO_ARGS

    tree = SUPER_NO_ARGS
    SuperWithoutArgumentsTransformer().visit(tree)
    assert get_ast(tree) == get_ast(SUPER_NO_ARGS_FIXED)



# Generated at 2022-06-14 02:32:08.269340
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_isolated
    node = ast.parse('super()')
    node = SuperWithoutArgumentsTransformer(target_versions={(2, 7)}).visit(node)
    assert compile_isolated(node, '<Test>', 'exec') == 'class Cls:\n    def f(self):\n        super(Cls, self)'

# Generated at 2022-06-14 02:32:19.634366
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..unittest_tools import transform_from_func
    from typed_ast import ast3


# Generated at 2022-06-14 02:32:23.843816
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree) == 'super(Cls, self)\n'

# Generated at 2022-06-14 02:32:33.688229
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from .base import BaseNodeTransformer

    class SuperWithoutArgumentsTransformer(BaseNodeTransformer):
        """Compiles:
            super()
        To:
            super(Cls, self)
            super(Cls, cls)
                
        """
        target = (2, 7)

        def _replace_super_args(self, node):
            try:
                func = get_closest_parent_of(self._tree, node, ast3.FunctionDef)
            except NodeNotFound:
                warn('super() outside of function')
                return

            try:
                cls = get_closest_parent_of(self._tree, node, ast3.ClassDef)
            except NodeNotFound:
                warn('super() outside of class')
                return


# Generated at 2022-06-14 02:32:34.813364
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:40.001883
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source_code_to_ast import source_to_ast
    source = "def foo():\n    super()"
    tree = source_to_ast(source)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    expected = "def foo():\n    super(Cls, self)"
    assert str(tree) == expected

# Generated at 2022-06-14 02:32:40.751386
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:52.482919
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import _ast
    code = '''
    class A(super()):
        def __init__(self):
            super().__init__()
            class B(super()):
                def __init__(self):
                    super().__init__()
    '''

    expected = '''
    class A(super(A, cls)):
        def __init__(self):
            super(A, self).__init__()
            class B(super(B, cls)):
                def __init__(self):
                    super(B, self).__init__()
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

    assert expected == _ast.dump(tree)



# Generated at 2022-06-14 02:33:03.425971
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_code = """
x = super()
"""
    expected_code = """
x = super(Cls, self)
"""
    transformer = SuperWithoutArgumentsTransformer(input_code, 2, 7)
    transformer.visit(transformer.module)
    assert transformer.stats() == (1, 0)
    assert transformer.module.body[0].value.args[0].id == 'Cls'
    assert transformer.module.body[0].value.args[1].id == 'self'
    transformer.module.body[0].value.args = []
    transformer.visit(transformer.module)
    assert transformer.stats() == (1, 0)
    assert transformer.module.body[0].value.args[0].id == 'Cls'

# Generated at 2022-06-14 02:33:10.701512
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .visitors import ExampleVisitor

    monkey_ast = ast.parse("class A(object):\n    def __init__(self):\n        super()")
    monkey_ast = SuperWithoutArgumentsTransformer().visit(monkey_ast)

    print("Unit test for SuperWithoutArgumentsTransformer")
    print("<-")
    print("->")
    print(ExampleVisitor().visit(monkey_ast))

    assert ExampleVisitor().visit(monkey_ast) == "class A(object):\n    def __init__(self):\n        super(A, self)"

# Generated at 2022-06-14 02:33:11.864557
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import transform


# Generated at 2022-06-14 02:33:35.200064
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import require
    from ..tests.utils import transform
    code = 'class X():\n    def f():\n        super()'
    tree = require.Python(code).tree
    SuperWithoutArgumentsTransformer(tree).run()
    assert transform.to_source(tree) == 'class X():\n    def f():\n        super(X, self)'

# Generated at 2022-06-14 02:33:39.398560
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'class Cls: def f(self): super()'
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert 'super(Cls, self)' in code_gen.to_source(tree)

# Generated at 2022-06-14 02:33:47.524708
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_str = """
        class Test():
            def __init__(self):
                super().__init__()

        class Test2(Test):
            def __init__(self):
                super().__init__()
    """
    ast_tree = ast.parse(code_str)
    SuperWithoutArgumentsTransformer().visit(ast_tree)
    code_out = compile(ast_tree, '<str>', 'exec')
    expected_code = """
        class Test():
            def __init__(self):
                super(Test, self).__init__()

        class Test2(Test):
            def __init__(self):
                super(Test2, self).__init__()
    """
    expected_ast_tree = ast.parse(expected_code)
    assert ast.dump(ast_tree)

# Generated at 2022-06-14 02:33:59.982284
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3

    t = SuperWithoutArgumentsTransformer()
    t._tree = ast3.parse('class C:\n def f(self):\n  super()\n')
    t.visit(t._tree)

# Generated at 2022-06-14 02:34:12.358052
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_str

    from typing import Any, Type

    def check_super_args(cls: Type[Any], code: str, expt_result) -> None:
        node = ast.parse(code)
        cls().visit(node)
        assert expt_result == source_to_str(node)

    code_1= \
"""
super()
"""
    expt_result_1 = \
"""
super(, cls)
"""

    code_2 = \
"""
    def __init__(self):
        super()
"""
    expt_result_2 = \
"""
    def __init__(self):
        super(, self)
"""

    class_name = 'Cls'


# Generated at 2022-06-14 02:34:13.985068
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:14.530829
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:34:17.182406
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_utils import StringStream
    import typed_astunparse
    from ..transformer import Transformer
    from ..utils.tree import get_first_leaf
    from ..visitor import Visitor
    from .helpers import assert_code_equal
    

# Generated at 2022-06-14 02:34:30.744209
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    s = """
                class Cls(object):
                    def __init__(self):
                        super()
                        super(Cls, cls)
                    def func(self):
                        super()
                        super(Cls, cls)
                    @classmethod
                    def __func(cls):
                        super()
                        super(Cls, cls)
                """
    t = """
                class Cls(object):
                    def __init__(self):
                        super(Cls, self)
                        super(Cls, cls)
                    def func(self):
                        super(Cls, self)
                        super(Cls, cls)
                    @classmethod
                    def __func(cls):
                        super(Cls, cls)
                        super(Cls, cls)
                """

# Generated at 2022-06-14 02:34:37.054807
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse('super()')
    t = SuperWithoutArgumentsTransformer()
    t.visit(tree)
    assert isinstance(tree.body[0].value.args[0], ast.Name)
    assert tree.body[0].value.args[0].id == 'Cls'
    assert isinstance(tree.body[0].value.args[1], ast.Name)
    assert tree.body[0].value.args[1].id == 'self'

    tree = ast.parse('class A: super()')
    t = SuperWithoutArgumentsTransformer()
    t.visit(tree)
    assert isinstance(tree.body[0].body[0].value.args[0], ast.Name)

# Generated at 2022-06-14 02:35:17.478902
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:32.139829
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.testing import assert_node

    cls_node = ast.ClassDef(
        name='Foo',
        bases=[],
        body=[
            ast.FunctionDef(
                name='bar',
                args=ast.arguments(
                    args=[
                        ast.arg(arg='self', annotation=None)
                    ],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[],
                ),
                body=[
                    ast.Pass(),
                ],
                decorator_list=[],
                returns=None,
            )
        ],
        decorator_list=[],
    )


# Generated at 2022-06-14 02:35:37.294084
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    from ..backend import PythonCodeBackend

    code = '''
        class A(object):
            def __init__(self):
                super().__init__()
    '''
    tree = compile(code, __name__, backend=PythonCodeBackend)
    assert str(tree) == "class A(object):\n    def __init__(self):\n        super(A, self).__init__()"

# Generated at 2022-06-14 02:35:46.145542
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile

    super_call = 'super().__init__'
    super_out = compile(super_call, '<test>', to_ast=True, mode='eval')
    assert isinstance(super_out, ast.Call), 'super without arguments fails'
    assert len(super_out.args) == 2, 'super without arguments fails'

    tree = compile('''
        class Test(object):
            def method(self):
                return super()
    ''', to_ast=True)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert len(tree.body[0].body[0].body[0].value.args) == 2, 'super without arguments fails'


# Generated at 2022-06-14 02:35:51.802323
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''class Test:
        def __init__(self):
            super()
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    assert isinstance(tree.body[0].body[0].body[0].args[0], ast.Name)
    assert tree.body[0].body[0].body[0].args[0].id == 'Test'
    assert isinstance(tree.body[0].body[0].body[0].args[1], ast.Name)
    assert tree.body[0].body[0].body[0].args[1].id == 'self'

# Generated at 2022-06-14 02:35:57.045519
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A:
            def fn(self):
                super()
        """.strip()

    expected = """
        class A:
            def fn(self):
                super(A, self)
        """.strip()

    assert (SuperWithoutArgumentsTransformer(parse(code)).result == parse(expected)).strip()

# Generated at 2022-06-14 02:36:01.309333
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    test_str = "super()"
    expected_str = "super(ClassName, __this)"
    tree = ast.parse(test_str)
    SuperWithoutArgumentsTransformer(tree, ClassName="ClassName").visit(tree)
    assert astor.to_source(tree).rstrip() == expected_str


# Generated at 2022-06-14 02:36:08.737791
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():  # type: () -> None
    from typed_ast import ast3 as ast
    from .. import print_module

    module_ast = ast.parse('class Test(object):\n    def function(self):\n        super()\n')
    SuperWithoutArgumentsTransformer(module_ast).visit(module_ast)
    assert print_module(module_ast) == 'class Test(object):\n    def function(self):\n        super(Test, self)\n\n'

# Generated at 2022-06-14 02:36:19.143516
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Testing constructor of class SuperWithoutArgumentsTransformer
    """
    node_target = ast.parse('''
        class MySuperClass(MyBaseClass):
            def f(self):
                super(MySuperClass, self)
    ''')

    node_expected = ast.parse('''
        class MySuperClass(MyBaseClass):
            def f(self):
                super(MyBaseClass, self)
    ''')

    tr = SuperWithoutArgumentsTransformer()
    tr.visit(node_target)
    expected = ast.fix_missing_locations(node_expected)

    assert ast.dump(node_target) == ast.dump(expected)



# Generated at 2022-06-14 02:36:23.726722
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # arrange
    code = """
    class Cls:
        def func(self):
            return super()
    """
    expected = """
    class Cls:
        def func(self):
            return super(Cls, self)
    """
    # act
    actual = fixer.transform(code)

    # assert
    assert actual == expected

# Generated at 2022-06-14 02:37:00.885630
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:01.807504
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:06.450805
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import get_ast
    node = get_ast("""
        class A:
            def test(self):
                super()
    """)
    SuperWithoutArgumentsTransformer().visit(node)
    assert(isinstance(node.body[0].body[0].body[0].value.args[0], ast.Name))
    assert(isinstance(node.body[0].body[0].body[0].value.args[1], ast.Name))

# Generated at 2022-06-14 02:37:10.931709
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import typed_ast.ast3 as ast

    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == "Call(Name(id='super', ctx=Load()), [Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], [], None, None)"

# Generated at 2022-06-14 02:37:11.581797
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:37:13.437100
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    from .. import tree

    # Initialization

# Generated at 2022-06-14 02:37:21.484640
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast.ast3 import parse, Assign, ClassDef, FunctionDef, Name, Attribute, Pass
    from .base import BaseNodeTransformer

    tree = parse('class Blah(object):\n    def __init__(self, test):\n        b = super()\n        self.test = test \n\n    def foo(self):\n        b = super()')
    
    transformer = BaseNodeTransformer()
    transformer = SuperWithoutArgumentsTransformer(tree, transformer)
    transformer.visit(tree)
    assert(isinstance(tree.body[0].body[0].body[0].value, Assign))
    assert(isinstance(tree.body[0].body[0].body[0].value.value, Call))

# Generated at 2022-06-14 02:37:22.475044
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert True

# Generated at 2022-06-14 02:37:28.976869
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import os
    import inspect
    import astor
    from rich.console import Console

    # Add parent directory to sys path to import transformer module
    current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)

    from ..transformers.super_without_arguments import SuperWithoutArgumentsTransformer

    console = Console()


# Generated at 2022-06-14 02:37:38.369238
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import as_tuple
    from ..node_utils import as_ast3
    from .base import NodeTransformer
    from .super_without_arguments import SuperWithoutArgumentsTransformer

    for version in (2, 7):
        transformer = NodeTransformer(version)
        assert transformer.__class__ == NodeTransformer
        transformer.add_transformer(SuperWithoutArgumentsTransformer)

        # # Transformer: SuperWithoutArgumentsTransformer
        test_ast = as_ast3("""
            class C:
                def f(self):
                    super()
        """)
        transformer.visit(test_ast)
        expected_ast = as_ast3("""
            class C:
                def f(self):
                    super(C, self)
        """)
        assert as_tuple(test_ast)