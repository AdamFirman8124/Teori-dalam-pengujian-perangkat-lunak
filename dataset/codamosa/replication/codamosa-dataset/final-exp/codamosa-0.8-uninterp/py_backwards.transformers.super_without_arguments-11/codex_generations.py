

# Generated at 2022-06-14 02:28:12.454262
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    from .. import parse
    from .. import ast_transforms

    source = '''
        class D(object):
            def __init__(self):
                super()
        
        class C(object):
            def meth(self):
                super()
    '''
    code = compile(source, '<test>', 'exec')
    tree: ast.Module = parse(code)  # type: ignore
    assert ast_transforms.SuperWithoutArgumentsTransformer(2, 7).visit(tree)

    source = '''
        class D(object):
            def __init__(self, a):
                super()
        
        class C(object):
            def meth(self, b):
                super()
    '''
    code = compile(source, '<test>', 'exec')
   

# Generated at 2022-06-14 02:28:22.769295
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    class DummyDefaultTree(ast.NodeVisitor):
        def __init__(self):
            self.generic_visit = lambda node: node

    tree = ast.parse('super()')
    tree.body[0].args[0].id = 'A'
    tree.body[0].value.args[0].id = 'B'
    tree.body[0].value.func.attr = 'C'
    tree.body[0].value.func.value.id = 'D'
    actual = SuperWithoutArgumentsTransformer(DummyDefaultTree(), tree).visit(tree)
    expected = ast.parse('super(A, B)')
    assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 02:28:24.198902
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    from .. import parse


# Generated at 2022-06-14 02:28:27.638653
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    a = ast.parse('super(Cls)')
    b = ast.parse('super(Cls, self)')
    assert SuperWithoutArgumentsTransformer.visit_Call(a, a.body[0].value) == b.body[0].value



# Generated at 2022-06-14 02:28:29.426234
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes

# Generated at 2022-06-14 02:28:38.704858
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Example():
        def __init__(self):
            super()
            super(Cls, self)
            super(Cls, cls)

# Generated at 2022-06-14 02:28:46.574637
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    "Test for SuperWithoutArgumentsTransformer"
    from ..utils import get_ast, compare_ast

    code = "super()"
    tree = get_ast(code)
    expected_code = "super(cls, self)"
    expected_tree = get_ast(expected_code)

    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)

    assert compare_ast(new_tree, expected_tree)

# Generated at 2022-06-14 02:28:50.641969
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .helper import compile_to_untyped_ast

    string = 'super()'
    root = compile_to_untyped_ast(string)
    SuperWithoutArgumentsTransformer.run_default(root)


# Generated at 2022-06-14 02:28:55.490337
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("""class Test:
    def test(self):
        super()""").body[0].body[0]
    result = SuperWithoutArgumentsTransformer().visit(node)
    assert len(result.body[0].args) == 2
    assert isinstance(result.body[0].args[0], ast.Name)
    assert result.body[0].args[0].id == 'Test'
    assert isinstance(result.body[0].args[1], ast.Name)
    assert result.body[0].args[1].id == 'self'

# Generated at 2022-06-14 02:28:56.163593
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:01.203975
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3
    

# Generated at 2022-06-14 02:29:09.733772
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    t = ast.parse("super()")
    visitor = SuperWithoutArgumentsTransformer()
    visitor.visit(t)

    assert "super(Cls, self)" == compile(t, "<string>", "exec").strip()

    t = ast.parse("super()")
    c = ast.ClassDef(name="Cls")
    t.body.insert(0, c)
    visitor = SuperWithoutArgumentsTransformer()
    visitor.visit(t)
    assert "super(Cls, self)" == compile(t, "<string>", "exec").strip()




# Generated at 2022-06-14 02:29:13.186585
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    transformer = SuperWithoutArgumentsTransformer(ast.parse('super()'))
    assert isinstance(transformer.visit(transformer.tree), ast.parse('super(MyClass, self)').body[0])


# Generated at 2022-06-14 02:29:23.487406
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input = """
            class s:
                def __init__(self):
                    super()
            """
    tree = ast.parse(input)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:29:27.066060
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import utils
    from . import SuperWithoutArgumentsTransformer
    # Testing with super()

# Generated at 2022-06-14 02:29:33.942887
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import get_ast
    from . import run_transformer
    from .test_utils import get_test_data

    test_data = get_test_data(__file__, 'SuperWithoutArgumentsTransformer_visit_Call')
    tree = get_ast(test_data[0])
    expected_tree = get_ast(test_data[1])

    transformed = run_transformer(tree, SuperWithoutArgumentsTransformer)
    assert transformed == expected_tree

# Generated at 2022-06-14 02:29:44.935831
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing import assert_transformed_code, transform_test_pattern

    with transform_test_pattern("super()") as results:
        transformer_test = results[0]
        assert_transformed_code(transformer_test, "super(Cls, self)")
        assert transformer_test.transformer.tree_changed is True

    with transform_test_pattern("super", pattern_type="fstring") as results:
        transformer_test = results[0]
        assert_transformed_code(transformer_test, "super(Cls, self)")
        assert transformer_test.transformer.tree_changed is True

    with transform_test_pattern("super", pattern_type="function") as results:
        transformer_test = results[0]

# Generated at 2022-06-14 02:29:47.111192
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    import ast

# Generated at 2022-06-14 02:29:54.889277
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .unparser import Unparser
    from ..utils.helpers import get_ast

    test_string = """
        class D:
            def __init__(self, arg):
                super()
    """
    tree = get_ast(test_string)
    new_tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert Unparser(new_tree) == """
        class D:
            def __init__(self, arg):
                super(D, self)
    """

# Generated at 2022-06-14 02:30:04.691713
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from astor.code_gen import to_source
    from .base import validate_transformer_on_file
    from .helpers import build_visit_call_test

    build_visit_call_test(
        SuperWithoutArgumentsTransformer,
        (r'class A(object): def m(self): super()',
         r'class A(object): def m(self): super(A, self)'),
        (r'class A(object): def m(self): super(a, b)',
         r'class A(object): def m(self): super(a, b)')
    )

# Generated at 2022-06-14 02:30:11.313125
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astunparse
    import sys

    # Given

# Generated at 2022-06-14 02:30:12.891909
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3


# Generated at 2022-06-14 02:30:17.192252
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    assert str(tree) == "super(Cls, cls)"


# Generated at 2022-06-14 02:30:20.112356
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_source
    compile_source("""
    class Parent(object):
        def __init__(self):
            super().foo()
    """, pyversion=(2, 7))

# Generated at 2022-06-14 02:30:26.867007
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test(ast.NodeTransformer):
        ALLOWED_VERSIONS = (2, 7)

        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                self.generic_visit(node)  # type: ignore
                node.args = [ast.Name(id='Cls'), ast.Name(id='self')]
                return node
            return self.generic_visit(node)  # type: ignore


# Generated at 2022-06-14 02:30:30.960115
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def testEquals(code_in, code_out):
        tree = ast.parse(code_in)
        SuperWithoutArgumentsTransformer().visit(tree)
        assert ast.dump(tree) == code_out


# Generated at 2022-06-14 02:30:35.732625
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_str = '''class A(object):
    def test(self):
        super()
        '''
    expect_str = '''class A(object):
    def test(self):
        super(A, self)
        '''
    target_version = (2, 7)
    tester(input_str, expect_str, SuperWithoutArgumentsTransformer, target_version, arg=True)

# Generated at 2022-06-14 02:30:42.520402
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='super'), args=[], keywords=[],
                    starargs=None, kwargs=None)
    t = SuperWithoutArgumentsTransformer()
    t._replace_super_args = lambda _: None
    t.visit_Call(node)
    assert node.args == [ast.Name(id='Cls'), ast.Name(id='self')]

# Generated at 2022-06-14 02:30:54.646505
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from textwrap import dedent
    from typed_ast import ast3 as ast

    from ..utils.tree import walk_down

    tree = ast.parse(dedent("""\
    class A:
        def __init__(self):
            super().__init__()
    """))

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    def find_super(node: ast.AST) -> bool:
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'super'

    super_node = walk_down(tree.body[0], find_super)[0]

    assert super_node.args[0].id == 'A'
    assert super_node.args[1].id == 'self'

# Generated at 2022-06-14 02:31:05.787688
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    s = """super()"""
    t = """super(Cls, self)"""
    t2 = """super(Cls, cls)"""
    t3 = """super(Cls, self)"""
    tree = ast.parse(s)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(t))
    #tree = ast.parse(s)
    transformer = SuperWithoutArgumentsTransformer(ast.parse(s))
    transformer.visit(ast.parse(s))
    assert ast.dump(tree) == ast.dump(ast.parse(t))
    tree = ast.parse(s)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

# Generated at 2022-06-14 02:31:15.730875
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class Foo:
            def __init__(self):
                super()
    '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    compiled = compile(tree, '', 'exec')
    exec(compiled)

# Generated at 2022-06-14 02:31:16.611401
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:31:27.162018
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # AssertionError: Objects are not equal: a = 'class A(object):\n ... ' != b = 'class A(object):\n ... '
    # assert SuperWithoutArgumentsTransformer._from_string("class A(object):\n pass")._to_string() \
    #        == 'class A(object):\n\n    pass\n'

    assert SuperWithoutArgumentsTransformer._from_string("class A(object):\n pass")._to_string() \
           == 'class A(object):\n\n    def __init__(self, *args, **kwargs):\n        super(A, self).__init__(*args, **kwargs)\n\n    pass\n'


# Generated at 2022-06-14 02:31:39.441053
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Test case 1
    test1_input = dedent("""
        class Cls:
            def __init__(self):
                super()
    """)
    test1_expected = dedent("""
        class Cls:
            def __init__(self):
                super(Cls, self)
    """)
    assert test1_expected == SuperWithoutArgumentsTransformer(test1_input, (2, 7)).result()

    # Test case 2
    test2_input = dedent("""
        class Cls:
            def __new__(cls):
                super()
    """)
    test2_expected = dedent("""
        class Cls:
            def __new__(cls):
                super(Cls, cls)
    """)
    assert test2_expected == SuperWithoutArguments

# Generated at 2022-06-14 02:31:49.474861
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = astroid.parse("""
    class A:
        def f(self):
            super()
    """)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed == True
    expected = """
    class A:
        def f(self):
            super(A, self)
    """
    compiled = compile(tree, '', 'exec')
    lines = iter_source_lines(compiled)
    for expected_line, actual_line in zip(expected.split('\n'), lines):
        assert_equal(expected_line.strip(), actual_line.strip())


# Generated at 2022-06-14 02:32:00.823962
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from collections import namedtuple

    def test(func: ast.FunctionDef, cls: ast.ClassDef) -> None:
        node = ast.Call(func=ast.Name(id='super'), args=[], keywords=[])
        visitor = SuperWithoutArgumentsTransformer()
        visitor.visit(node)
        assert node.args[0].id == cls.name

    Call = namedtuple('Call', 'func args keywords')
    FunctionDef = namedtuple('FunctionDef', 'args')
    ClassDef = namedtuple('ClassDef', 'name')
    Name = namedtuple('Name', 'arg')
    Assign = namedtuple('Assign', 'value')


# Generated at 2022-06-14 02:32:10.358579
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A:
            def __init__(self):
                super()
    
        class B:
            def method(self):
                super()
    """

    expected_output = """
        class A:
            def __init__(self):
                super(A, self)

        class B:
            def method(self):
                super(B, self)
    """

    tt = SuperWithoutArgumentsTransformer()
    tree = ast.parse(code)
    new_tree = tt.visit(tree)

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected_output))

# Generated at 2022-06-14 02:32:23.125773
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

    # Node with no super() call.
    node = ast.parse('def a():\n    b()')
    transformer.visit(node)
    assert node == ast.parse('def a():\n    b()')

    # Normal super() call.
    node = ast.parse('def a():\n    super()')
    transformer.visit(node)
    assert node == ast.parse('def a():\n    super(Cls, self)')

    # super() call within a method.
    node = ast.parse('class Foo:\n    def a(self):\n        super()')
    transformer.visit(node)
    assert node == ast.parse('class Foo:\n    def a(self):\n        super(Foo, self)')
    
    #

# Generated at 2022-06-14 02:32:27.887022
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    m = ast.parse('super()')
    m = SuperWithoutArgumentsTransformer().visit(m)
    assert ast.dump(m) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:32:34.471464
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes

    source = '''
        class Cls(object):
            def __init__(self):
                super().__init__()
    '''

    # pylint: disable=unused-variable
    module, = source_to_nodes(source)
    assert not SuperWithoutArgumentsTransformer().visit(module)

# Generated at 2022-06-14 02:32:53.645222
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_to_py3
    
    code = '''
if True:
    class A(object):
        def __init__(self):
            super()
    '''
    tree = compile_to_py3(code, '<test>')
    
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    
    assert 'ast.Call(ast.Name(id=\'super\', ctx=ast.Load()), args=[ast.Name(id=\'A\', ctx=ast.Load()), ast.Name(id=\'self\', ctx=ast.Load())], keywords=[])' in str(tree)

# Generated at 2022-06-14 02:32:55.125001
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:33:01.321507
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import textwrap
    from .utils import transform
    code = textwrap.dedent('''
    class A:
        def __init__(self):
            super()
            super(A)
    ''')
    res = transform(code, 2, 7)
    assert res == textwrap.dedent('''
    class A:
        def __init__(self):
            super(A, self)
            super(A)
    ''')

# Generated at 2022-06-14 02:33:07.093381
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.tree import to_src
    from .simple_transformer import SimpleTransformer

    code = 'super()'
    tree = ast.parse(code)

    transformer = SuperWithoutArgumentsTransformer(tree, SimpleTransformer.NODE_INFO)
    transformer.visit(tree)

    assert to_src(tree) == 'super(Cls, self)'


# Generated at 2022-06-14 02:33:14.053929
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .. import compile_restricted
    from ..parser import get_python_parser
    from ._test_transformers import assert_transform
    import textwrap
    parser = get_python_parser()
    
    # Tests that when a call to super() is made from within a function within a class, the call is transformed into super(cls_name, self) 
    source = source_to_unicode('''
    class A(object):
        def fct(self):
            super()
    ''')
    expected_source = source_to_unicode('''
    class A(object):
        def fct(self):
            super(A, self)
    ''')
    ast_tree = parser.parse(source)

# Generated at 2022-06-14 02:33:26.712890
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    src = """
    class Cls:
        def mthd(self):
            super()
    """
    tree = ast.parse(src)
    SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:33:27.351519
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:37.096987
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    class SuperTransformerTest(SuperWithoutArgumentsTransformer):
        target = (2, 7)

        def visit_Assign(self, node: ast.Assign) -> ast.Assign:
            return self.generic_visit(node)

    class SuperTransformerTest(SuperWithoutArgumentsTransformer):
        target = (3, 8)

        def visit_Assign(self, node: ast.Assign) -> ast.Assign:
            return self.generic_visit(node)

    class A:
        i = 1

    class B(A):
        def __init__(self):
            super()

        def f(self):
            super()

    class C(B):
        def __init__(self):
            super()

        def f(self):
            super()


# Generated at 2022-06-14 02:33:42.993599
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code = \
    """
    class A:
        def __init__(self):
            super()
    """

    expected_output = \
    """
    class A:
        def __init__(self):
            super(A, self)
    """

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree) == expected_output

# Generated at 2022-06-14 02:33:49.835829
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Set up AST
    one = ast.Constant(value=1, kind=None)
    two = ast.Constant(value=2, kind=None)

# Generated at 2022-06-14 02:34:03.597939
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:14.940607
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .helpers import assert_equal_ast, unit_transform
    code1 = 'super()'
    expected1 = ast.Call(
        func=ast.Name(id='super'), args=[
            ast.Name(id='Cls'),
            ast.Name(id='self')], keywords=[]
    )
    assert_equal_ast(unit_transform(code1, SuperWithoutArgumentsTransformer), expected1)

    code2 = 'super(Cls, obj)'
    expected2 = ast.Call(
        func=ast.Name(id='super'), args=[
            ast.Name(id='Cls'),
            ast.Name(id='obj')], keywords=[]
    )

# Generated at 2022-06-14 02:34:15.835902
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:27.191756
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input = """
        class foo(object):
            def __init__(self):
                super().__init__()
            def bar(cls):
                super().bar()
            @classmethod
            def baz(cls):
                super().baz()
        """
    output = """
        class foo(object):
            def __init__(self):
                super(foo, self).__init__()
            def bar(cls):
                super(foo, cls).bar()
            @classmethod
            def baz(cls):
                super(foo, cls).baz()
        """
    utils.assert_convert(input, output)

# Generated at 2022-06-14 02:34:32.501897
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''class X:\n\tdef f(self): super()'''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree) == 'class X:  def f(self): super(X, self)\n'


# Generated at 2022-06-14 02:34:39.300173
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='super'), args=[])
    transformer = SuperWithoutArgumentsTransformer(tree=None, future_features={})
    new_node = transformer.visit_Call(node)
    assert isinstance(new_node, ast.Call)
    assert isinstance(new_node.args[0], ast.Name)
    assert new_node.args[0].id == 'Cls'

# Generated at 2022-06-14 02:34:44.119259
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..transpile import Transpiler
    from ..utils.helpers import as_tuple

    class Test(Transpiler):
        def __init__(self, tree: ast.AST, code: str = None, filename: str = None) -> None:
            super().__init__(tree, code, filename)
            self.modules.append(SuperWithoutArgumentsTransformer)


# Generated at 2022-06-14 02:34:47.993941
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code: str = """
    class Test:
        def f(self):
            super()
    """
    expected: str = """
    class Test:
        def f(self):
            super(Test, self)
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree, annotate_fields=False) == ast.dump(ast.parse(expected), annotate_fields=False)


# Generated at 2022-06-14 02:34:59.889592
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import fix_missing_locations
    import textwrap

    code = textwrap.dedent('''\
        class A:
            def __init__(self):
                super()

        class B(A):
            def __init__(self):
                super()
            
        def foo():
            super()
        ''')

    tree = parse(code)
    transformer = SuperWithoutArgumentsTransformer()

    new_tree = transformer.visit(tree)
    fix_missing_locations(new_tree)

    assert_code_equal(compile(tree, filename="<test>", mode="exec"),
                      compile(new_tree, filename="<test>", mode="exec"))

# Generated at 2022-06-14 02:35:05.213465
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_original = '''
    class  A:
        def __init__(self):
            super()
    '''
    tree = ast.parse(code_original).body[0]
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

    assert code_original != ast.unparse(tree)


# Generated at 2022-06-14 02:35:38.781479
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for SuperWithoutArgumentsTransformer"""
    import astunparse

    code = """
        class SuperWithoutArgumentsTransformer:
            def __init__(self):
                self._tree = None

            def _replace_super_args(self, node):
                super()
    """

    expected_code = """
        class SuperWithoutArgumentsTransformer:
            def __init__(self):
                self._tree = None

            def _replace_super_args(self, node):
                super(SuperWithoutArgumentsTransformer, self)
    """

    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    compiled_code = astunparse.unparse(tree)

    assert compiled_code == expected_code

# Generated at 2022-06-14 02:35:40.060713
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .utils import should_transform_to


# Generated at 2022-06-14 02:35:40.924353
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:41.308401
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:42.130811
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer is not None

# Generated at 2022-06-14 02:35:50.041879
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''\
    def hello(self):
        super().hello()
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    expected = \
        ast.parse('''\
        def hello(self):
            super(Cls, self).hello()
        ''')
    assert ast.dump(tree) == ast.dump(expected)
    
    code = '''\
    def hello():
        super().hello()
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

# Generated at 2022-06-14 02:35:50.855830
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:35:55.923287
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import ast_converter
    code = 'super()'
    tree = ast_converter.parse(code)
    SuperWithoutArgumentsTransformer.run_visitor(tree)
    expected = '(super(Cls, self))'
    result = ast_converter.unparse(tree).strip()
    assert result == expected

# Generated at 2022-06-14 02:36:01.200729
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''a = super()'''
    tree = ast.parse(code)

    expected_output = '''a = super(Cls, self)'''
    expected_tree = ast.parse(expected_output)

    transformer = SuperWithoutArgumentsTransformer(tree)
    tree = transformer.visit(tree)

    assert ast.dump(tree, include_attributes=False) == ast.dump(expected_tree, include_attributes=False)

# Generated at 2022-06-14 02:36:08.099334
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('''
        class Cls:
            def func(self):
                super()
    ''')

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert to_source(tree) == '''
        class Cls:
            def func(self):
                super(Cls, self)
    '''.strip()


# Generated at 2022-06-14 02:37:01.307931
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:06.628655
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    transformer = SuperWithoutArgumentsTransformer()

    class_def = ast.parse('class Test(object): pass').body[0]
    func_def = ast.parse('''
    def __init__(self):
        super()
    ''').body[0]
    call_super = func_def.body[0]

    class_def.body.append(func_def)

    module = ast.Module(body=[class_def])

    transformer.visit(module)
    assert len(call_super.args) == 2  # type: ignore

# Generated at 2022-06-14 02:37:16.008182
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])
    tree = ast.parse('class A: def __init__(self): super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert isinstance(tree.body[0].body[0].body[0].value.args[0], ast.Name)

    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])
    tree = ast.parse('class A: def f(self): super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:37:17.408361
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:28.006306
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Compiles:
        super()

    To:
        super(Cls, self)
        super(Cls, cls)
    """
    # TODO: Fix tests

# Generated at 2022-06-14 02:37:28.751903
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:31.701183
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("super()", mode="eval")
    SuperWithoutArgumentsTransformer().visit(node)
    assert codegen.to_source(node) == "super(<unknown>, self)"

# Generated at 2022-06-14 02:37:33.757689
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    import sys
    import astunparse
    from .transformers import fix_missing_locations


# Generated at 2022-06-14 02:37:41.021625
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class SuperWithoutArgumentsTransformerTest(SuperWithoutArgumentsTransformer):
        def __init__(self, tree: ast.AST):
            super().__init__(tree)
            # Test tree setter
            self._tree = tree

        def _replace_super_args(self, node: ast.Call) -> None:
            super()._replace_super_args(node)
            self._tree_changed = True

        def visit_Call(self, node: ast.Call) -> ast.Call:
            super().visit_Call(node)
            return node


# Generated at 2022-06-14 02:37:46.304471
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    source = '''
    class A(B):
        def __init__(self, x):
            super()
            return x
            
    '''
    expected = '''
    class A(B):
        def __init__(self, x):
            super(A, self)
            return x
            
    '''
    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert expected == astor.to_source(tree).lstrip()
