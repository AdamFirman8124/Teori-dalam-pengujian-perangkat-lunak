

# Generated at 2022-06-14 02:28:03.512365
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from untokenize import untokenize
    from utils.compat import StringIO


# Generated at 2022-06-14 02:28:04.800004
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor


# Generated at 2022-06-14 02:28:14.719849
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class Cls:
        def __init__(self):
            super().__init__(x)

        # noqa: WPS231
        def method(self):
            super().meth()
    '''
    tree = ast.parse(code)
    t = SuperWithoutArgumentsTransformer(tree)
    t.run()

# Generated at 2022-06-14 02:28:20.390581
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_tree
    from ..utils.compare import expect

    # This should not be tested
    expect(SuperWithoutArgumentsTransformer._replace_super_args).to.raise_an_error()


# Generated at 2022-06-14 02:28:31.168114
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast.ast3 import parse
    from typed_ast import ast3 as ast
    node = parse('super()')
    tree = SuperWithoutArgumentsTransformer().visit(node)

    func = node.body[0]
    cls = node.body[1]

    assert isinstance(tree, ast.Module)
    assert isinstance(tree.body[0], ast.ClassDef)
    assert isinstance(tree.body[0].body[0], ast.FunctionDef)
    assert isinstance(tree.body[0].body[0].body[0], ast.Expr)
    assert isinstance(tree.body[0].body[0].body[0].value, ast.Call)

    assert isinstance(tree.body[0].body[0].body[0].value.args[0], ast.Name)


# Generated at 2022-06-14 02:28:31.926496
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:37.279539
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """class C:
        def __init__(self):
            super()
    """
    expected = """class C:
    def __init__(self):
        super(C, self)

"""
    tree = ast.parse(code)
    assert ast.dump(SuperWithoutArgumentsTransformer().visit(tree)) == expected

# Generated at 2022-06-14 02:28:50.466533
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Create an instance of SuperWithoutArgumentsTransformer
    transformer = SuperWithoutArgumentsTransformer()

    # Get the ast from the file test_SuperWithoutArgumentsTransformer_before.py
    file_path = os.path.join(os.path.dirname(__file__), 'test_SuperWithoutArgumentsTransformer_before.py')
    with open(file_path, 'r') as f:
        file_content = f.read()
    tree = ast.parse(file_content)

    # Apply the transformation to the tree
    transformer.visit(tree)

    # Get the expected result from the file test_SuperWithoutArgumentsTransformer_after.py
    file_path = os.path.join(os.path.dirname(__file__), 'test_SuperWithoutArgumentsTransformer_after.py')

# Generated at 2022-06-14 02:28:53.252725
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # When
    node = ast.parse('super()')
    node = SuperWithoutArgumentsTransformer().visit(node)

    # Then
    assert 'super(cls, self)' in astor.to_source(node)

# Generated at 2022-06-14 02:28:58.985117
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Unit test for method visit_Call of class SuperWithoutArgumentsTransformer"""

    import sys
    sys.setrecursionlimit(100000)

    # Example of code used as input

# Generated at 2022-06-14 02:29:03.250986
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import _ast as ast


# Generated at 2022-06-14 02:29:13.788637
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    code = 'super()'

    tree = ast.parse(code)
    node = tree.body[0]

    trans = SuperWithoutArgumentsTransformer()
    new_node = trans.visit(node)

    assert isinstance(new_node, ast.Expr)
    assert isinstance(new_node.value, ast.Call)
    args = new_node.value.args
    assert isinstance(args[0], ast.Name)
    assert args[0].id == 'Cls'
    assert isinstance(args[1], ast.Name)
    assert args[1].id == 'self'



# Generated at 2022-06-14 02:29:14.839480
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:17.292530
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Unit test for method visit_Call of class SuperWithoutArgumentsTransformer."""

    import astor


# Generated at 2022-06-14 02:29:27.162921
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    ast_tree_1 = ast.parse('super()')
    ast_tree_2 = ast.parse('super(self)')
    ast_tree_3 = ast.parse('super().foo()')
    ast_tree_4 = ast.parse('super(self).foo()')
    ast_tree_5 = ast.parse('self.super()')
    ast_tree_6 = ast.parse('self.super(self)')
    ast_tree_7 = ast.parse('cls.super()')
    ast_tree_8 = ast.parse('cls.super(cls)')

    SuperWithoutArgumentsTransformer(ast_tree_1).visit(ast_tree_1)
    assert str(ast_tree_1) == "super(Cls, self)"


# Generated at 2022-06-14 02:29:28.398383
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:34.656493
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.mock_tree import mock_tree
    from ..utils.mock_tree import parse

    # SyntaxError: super() outside of class
    tree = mock_tree(parse("super()"))
    SuperWithoutArgumentsTransformer().visit(tree)
    assert tree == mock_tree(parse("super()"))

    # SyntaxError: super() outside of function

# Generated at 2022-06-14 02:29:45.205085
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing import assert_code_equal
    from ..utils.helpers import compile_func, str_ast
    from ..utils.tree import findall_in_tree

    funcs = [
        'super()',
        'super(NewClass)',
    ]

    for f in funcs:
        tree = compile_func(f, 'exec')
        # print(str_ast(tree))
        super_nodes = findall_in_tree(tree, ast.Name, lambda n: n.id == 'super')
        assert len(super_nodes) == 1
        # print(str_ast(super_nodes[0]))

        SuperWithoutArgumentsTransformer().visit(tree)
        # print(str_ast(tree))
        assert_code_equal(f, str_ast(tree))

# Generated at 2022-06-14 02:29:47.763131
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert 'super(__main__.A, self)' == astor.to_source(tree).strip()

# Generated at 2022-06-14 02:29:57.728993
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    src = """
        class A:
            def f(self):
                super(B, self)

            def g(self):
                super()
    """

    expected_src = """
        class A:
            def f(self):
                super(B, self)

            def g(self):
                super(B, self)
    """

    tree = ast.parse(src)

    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert ast.dump(tree) == expected_src

    src = """
        class A:
            def f(self):
                super()

            def g(self):
                print(super())
    """

    tree = ast.parse(src)

    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert ast.dump

# Generated at 2022-06-14 02:30:07.443055
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class MyClass:
            def my_func(self):
                super()
    """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)

    expected_code = """
        class MyClass:
            def my_func(self):
                super(MyClass, self)
    """

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:30:14.093702
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .utils import should_transform

    tree = should_transform("""super()""", SuperWithoutArgumentsTransformer)

    assert tree.body[0].value.func.id == 'super'
    assert isinstance(tree.body[0].value.args[0], ast.Name)
    assert tree.body[0].value.args[0].id == 'Cls'
    assert isinstance(tree.body[0].value.args[1], ast.Name)
    assert tree.body[0].value.args[1].id == 'x'

# Generated at 2022-06-14 02:30:14.780934
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:22.161645
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.codegen import to_source

    # Test 001
    tree = ast.parse("super(B,C)")
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    code = to_source(tree)
    assert code == "super(B,C)"

    # Test 002
    tree = ast.parse("super()")
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    code = to_source(tree)
    assert code == "super(C,self)"

# Generated at 2022-06-14 02:30:28.060885
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..transpile import Transpiler

    code = dedent("""
        class C:
            def __init__(self, x):
                super().__init__(x + 2)
    """)

    expected_code = dedent("""
        class C:
            def __init__(self, x):
                super(C, self).__init__(x + 2)
    """)

    transpiler = Transpiler()
    transpiler.register(SuperWithoutArgumentsTransformer)
    actual_code = transpiler.transpile_code(code)
    assert expected_code == actual_code

# Generated at 2022-06-14 02:30:28.708399
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:32.958570
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''super()'''
    expected_code = '''super(Cls, self)'''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    tree = transformer.visit(tree)
    assert ast.dump(tree) == expected_code


# Generated at 2022-06-14 02:30:40.823459
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast
    #`super` test
    x = '''
    class Foo(object):
       def __init__(self, first, second):
           super()
    '''
    tree = source_to_ast(x)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:30:46.819261
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
            class A:
                def __init__(self):
                    super()
            """
    expected = """
            class A:
                def __init__(self):
                    super(A, self)
            """
    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)
    assert expected == astor.to_source(tree)


# Generated at 2022-06-14 02:30:50.343048
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    code_after = compile(tree, '', 'exec')
    eval(code_after)

# Generated at 2022-06-14 02:30:59.960972
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer"""
    code = """
d = super()
"""
    errors_list = ['super() outside of function', 'super() outside of class']
    tree = ast.parse(code)
    node_instance = SuperWithoutArgumentsTransformer(tree)
    if node_instance.error_flag:
        print("Constructor test of class SuperWithoutArgumentsTransformer to check if super() is inside of function and also inside of class failed")
    assert not node_instance.error_flag
    for error in errors_list:
        assert error not in node_instance.error_list


# Generated at 2022-06-14 02:31:00.581238
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:08.470773
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from ..utils.codegen import to_source
    
    
    # When super() is used without arguments, this transformer will compile it to super(cls, self) or super(cls, cls) depending on the context
    # this unit test will find the parent(ClassDef) and func(FunctionDef) of the super() Call and add the first argument of func to the Call
    # Example:
    class x:
        def test(self):
            super()
    
    
    
    source = to_source(x)
    tree = ast3.parse(source)
    
    
   
    SuperWithoutArgumentsTransformer().visit(tree)
    from ..utils.codegen import to_source
    from .. import compile_and_run
    
    
    
    
    

# Generated at 2022-06-14 02:31:12.893187
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    with open('./tests/fixtures/transforms/super.py') as fp:
        tree = ast.parse(fp.read())
    transformer.visit(tree)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 02:31:13.606692
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:16.976570
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert transformer._tree_changed
    assert dump_ast(tree) == dump_ast(ast.parse('super(Cls, self)'))


# Generated at 2022-06-14 02:31:26.760474
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    global_var = ast.Global()
    assert global_var.names == []
    super_global_var = ast.Global()
    super_global_var.names.append('super')
    assert super_global_var.names == ['super']
    argument1 = ast.Name()
    argument2 = ast.Name()
    args = ast.arguments()
    args.args.append(argument1)
    args.args.append(argument2)
    function = ast.FunctionDef()
    function.name = 'function'
    function.args = args
    assert function.name == 'function'
    assert function.args == args
    assert function.args.args[0] == argument1
    assert function.args.args[1] == argument2
    class_def = ast.ClassDef()

# Generated at 2022-06-14 02:31:39.143910
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..tests.fixtures.typed_asts import CLASS_WITH_SUPER

    def _run(node, *args):
        transformer = SuperWithoutArgumentsTransformer(*args)
        return transformer.visit(node)

    # test to replace super() with super(Cls, self) when it is inside of method
    class_with_super = CLASS_WITH_SUPER.value

    _run(class_with_super)
    assert len(class_with_super.body[1].body[0].body[0].value.args) == 2

    # test to replace super() with super(Cls, self) when it is inside of method
    class_with_super = CLASS_WITH_SUPER.value

    _run(class_with_super)

# Generated at 2022-06-14 02:31:49.532827
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import typed_ast.ast3 as typed_ast

    module_str = "super()"
    module_ast = typed_ast.parse(module_str)
    module_ast.body[0] = SuperWithoutArgumentsTransformer().visit(module_ast.body[0])
    assert typed_ast.dump(module_ast) == "Expr(value=Call(func=Name(id='super', ctx=Load()), " \
                                         "args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], " \
                                         "keywords=[], starargs=None, kwargs=None))"



# Generated at 2022-06-14 02:31:53.314322
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    t = SuperWithoutArgumentsTransformer()
    for n in [2, 7]:
        t.target = (n, n)

# Generated at 2022-06-14 02:32:01.106818
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor


# Generated at 2022-06-14 02:32:08.432183
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('assert super() is None')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree, include_attributes=True) == \
        'Module(body=[Assert(test=Call(func=Attribute(value=Name(id="super", ctx=Load()), attr="isnull", ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None), msg=None)])'

# Generated at 2022-06-14 02:32:14.453350
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing.test_base import NodeTestCase

    class TestCase(NodeTestCase):
        target = (2, 7)
        transformer = SuperWithoutArgumentsTransformer

        def test_class(self):
            tree = ast.parse("""
                class Test:
                    def __init__(self):
                        super()
            """)

            self.compare(tree, """
                class Test:
                    def __init__(self):
                        super(Test, self)
            """)

        def test_nested_class(self):
            tree = ast.parse("""
                class Test:
                    class Nested:
                        def __init__(self):
                            super()
            """)


# Generated at 2022-06-14 02:32:21.775793
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
if True:
    class A(object):
        def f(self):
            super()
            return None
    '''

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

    fixed_code = '''
if True:
    class A(object):
        def f(self):
            super(A, self)
            return None
    '''

    assert astor.to_source(tree) == fixed_code

# Generated at 2022-06-14 02:32:32.686808
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import sys
    import io
    import unittest
    from typed_ast import ast3 as ast

    class SuperWithoutArgumentsTransformerTest(unittest.TestCase):
        def test_simple(self):
            class Test(SuperWithoutArgumentsTransformer):
                def visit_Name(self, node):
                    return node
            node = ast.parse('super()')
            Test().visit(node)

# Generated at 2022-06-14 02:32:41.906940
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from textwrap import dedent
    from ..utils.source_code import SourceCode

    s = dedent('''
        class A:
            def __init__(self):
                super()
    ''')
    tree = ast.parse(s)

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert isinstance(transformer._tree, ast.Module)
    assert transformer._tree_changed is True

    s2 = dedent('''
        class A:
            def __init__(self):
                super(A, self)
    ''')
    tree2 = ast.parse(s2)
    assert SourceCode(tree2).code == SourceCode(transformer._tree).code

# Generated at 2022-06-14 02:32:49.485960
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import ast as pyast

    tree = pyast.parse("super()")
    tree = SuperWithoutArgumentsTransformer().visit(tree)

    assert pyast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='C', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"


# Generated at 2022-06-14 02:32:52.876885
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_code
    from ..utils.helpers import bytecode_compare
    from ..utils.tree import tree_to_str

# Generated at 2022-06-14 02:32:56.903389
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
            class A():
                def __init__(self):
                    super()
            """
    module_node = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(module_node)
    assert transformer._tree_changed == True

# Generated at 2022-06-14 02:32:57.975230
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:22.862960
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import ast
    
    # Default case
    tree = ast.parse('''
        class test():
            def test(self):
                super()
                super(test, self)
    ''')
    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()))
    node.lineno = tree.body[0].body[0].body[0].lineno
    node.col_offset = tree.body[0].body[0].body[0].col_offset
    tree.body[0].body[0].body[0] = node
    
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    
    # test ctx

# Generated at 2022-06-14 02:33:23.924610
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:35.019087
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(ast.parse('super()', mode='exec'))
    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Call)
    assert isinstance(tree.body[0].value.func, ast.Name)
    assert tree.body[0].value.func.id == 'super'
    assert len(tree.body[0].value.args) == 2
    assert isinstance(tree.body[0].value.args[0], ast.Name)
    assert isinstance(tree.body[0].value.args[1], ast.Name)
    assert tree.body[0].value.args[0].id == 'Cls'

# Generated at 2022-06-14 02:33:45.094225
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_code = """
        class SuperWithoutArgumentsTransformer:
            def __init__(self):
                super()
                super(SuperWithoutArgumentsTransformer).__init__()
        """
    expected_output = """
        class SuperWithoutArgumentsTransformer:
            def __init__(self):
                super(SuperWithoutArgumentsTransformer, self)
                super(SuperWithoutArgumentsTransformer, self).__init__()
        """
    tree = ast.parse(input_code)
    transformer = SuperWithoutArgumentsTransformer()
    transformed_tree = transformer.visit(tree)
    try:
        transformed_code = astor.to_source(transformed_tree)
    except AttributeError:
        transformed_code = astor.to_source(ast.Module(body=transformed_tree.body))
   

# Generated at 2022-06-14 02:33:49.839702
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class A:
        def m(self):
            super()
    '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, filename="", mode="exec"))

# Generated at 2022-06-14 02:34:00.927311
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    sut = SuperWithoutArgumentsTransformer()

    tree = ast.parse('class Test(object): def Test(self): super()')
    sut.visit(tree)

    assert isinstance(tree.body[0].body[0].body[0], ast.Expr)
    assert isinstance(tree.body[0].body[0].body[0].value, ast.Call)
    assert isinstance(tree.body[0].body[0].body[0].value.func, ast.Name)
    assert tree.body[0].body[0].body[0].value.func.id == "super"

    assert len(tree.body[0].body[0].body[0].value.args) == 2

# Generated at 2022-06-14 02:34:02.375964
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:02.918487
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:08.918384
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..testing_utils import assert_code_equal
    from .utils import transform, load_example_snippet

    tree = load_example_snippet('super-without-arguments')
    expected_tree = load_example_snippet('super-without-arguments', 'expected')
    transform(tree, SuperWithoutArgumentsTransformer)
    assert_code_equal(tree, expected_tree)

# Generated at 2022-06-14 02:34:09.921937
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:41.342271
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """ Unit test for constructor of class SuperWithoutArgumentsTransformer.
    """

# Generated at 2022-06-14 02:34:42.047477
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:47.241255
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer(): 
    from ..utils.example_code import example_code
    from ..utils.helpers import get_ast

    tree = get_ast(example_code, (2, 7))
    transformed_tree = SuperWithoutArgumentsTransformer().visit(tree)

    assert "super(Cls, self)" in example_code
    assert "super(Cls, cls)" in example_code

    code_after_transformation = str(transformed_tree)

    assert "super(Cls, self)" in code_after_transformation
    assert "super(Cls, cls)" in code_after_transformation

# Generated at 2022-06-14 02:34:59.587454
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # No arguments
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert len(tree.body[0].value.args) == 2
    node = tree.body[0].value.args[0]
    assert isinstance(node, ast.Name)
    assert node.id == 'Cls'
    node = tree.body[0].value.args[1]
    assert isinstance(node, ast.Name)
    assert node.id == 'self'

    # Position argument
    tree = ast.parse('super(4)')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert len(tree.body[0].value.args) == 2
    node = tree.body[0].value.args[0]

# Generated at 2022-06-14 02:35:03.897417
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.context import Context
    from ..utils.source import source_to_unicode
    from ..transformers.super import SuperWithoutArgumentsTransformer


# Generated at 2022-06-14 02:35:04.768408
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor


# Generated at 2022-06-14 02:35:06.959308
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import typed_ast.ast3 as ast
    from typed_ast import ast3


# Generated at 2022-06-14 02:35:07.646911
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:19.704290
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("class A: def __init__(self): super()")
    SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:35:22.870279
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import ast
    from typed_ast import ast27
    from ..utils.helpers import str_node


# Generated at 2022-06-14 02:36:30.227809
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:36:30.835633
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:33.214735
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.source import source_to_tree, tree_to_source


# Generated at 2022-06-14 02:36:44.046045
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode
    from ..utils.ast_converter import ast_to_source

    from typed_ast import ast3

    src = 'class A: def meth(self): super()'
    node = ast3.parse(src)
    tw = SuperWithoutArgumentsTransformer()
    node = tw.visit(node)
    src2 = ast_to_source(node)
    src_expected = 'class A: def meth(self): super(A, self)'
    assert source_to_unicode(src2) == source_to_unicode(src_expected)


# Generated at 2022-06-14 02:36:46.018792
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test class SuperWithoutArgumentsTransformer
    """

# Generated at 2022-06-14 02:36:52.489815
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Foo:
            def bar(self):
                super()
    """
    expected_code = """
        class Foo:
            def bar(self):
                super(Foo, self)
    """
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))



# Generated at 2022-06-14 02:37:01.261293
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ...pipeline import compile

    assert compile('super()', target=(3,0)).strip() ==\
        'super(__main__.Test, self)'
    assert compile('super()', target=(2,7)).strip() ==\
        'super(__main__.Test, self)'

    assert compile('super()', target=(2,7),
                   additional_transformers=[SuperWithoutArgumentsTransformer]).strip() ==\
        'super(__main__.Test, self)'
    assert compile('super()', target=(3,0),
                   additional_transformers=[SuperWithoutArgumentsTransformer]).strip() ==\
        'super(__main__.Test, self)'


# Generated at 2022-06-14 02:37:07.969914
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    source = source_to_unicode("""
        class A(object):
            pass

        class B(A):
            def __init__(self):
                super()

        class C(B):
            def __init__(self):
                super().__init__()

        class D(A):
            def __init__(self, x):
                super()
    """)

    from ..utils.ast_builder import build_ast
    module = build_ast(source)

    from .base import NodeTransformer
    transformer = NodeTransformer()
    results = transformer.visit(module)

    from ..utils.source import source_to_unicode

# Generated at 2022-06-14 02:37:12.801783
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    tree = ast.parse("""
    class Cls:
        def __init__(self):
            super()
    """)
    AST_tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(AST_tree) == 'class Cls:\n\n    def __init__(self):\n        super(Cls, self)\n'

# Generated at 2022-06-14 02:37:20.958110
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from .helpers import get_node_of_type
    node = ast3.parse("super()")
    root = node.body[0].value
    cls = ast3.ClassDef(name='Foo', bases=[], body=[], decorator_list=[])
    func = ast3.FunctionDef(name='__init__', args=ast3.arguments(args=[ast3.Name(id='self', ctx=ast3.Param())],
                                                                 vararg=None, kwonlyargs=[], kw_defaults=[],
                                                                 kwarg=None, defaults=[]), body=[ast3.Expr(value=root), ], decorator_list=[])
    cls.body.append(func)