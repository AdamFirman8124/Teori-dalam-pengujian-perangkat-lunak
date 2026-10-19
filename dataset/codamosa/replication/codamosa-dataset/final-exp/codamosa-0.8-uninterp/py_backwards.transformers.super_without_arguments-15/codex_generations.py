

# Generated at 2022-06-14 02:27:53.638343
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:27:54.770270
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:03.789127
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'

    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    exec(compile(tree, filename='<ast>', mode='exec'))



# Generated at 2022-06-14 02:28:14.366485
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTest
    from .super_without_arguments import SuperWithoutArgumentsTransformer
    from textwrap import dedent
    
    class Test(BaseNodeTransformerTest):
        target_class = SuperWithoutArgumentsTransformer

        def test_super_without_arguments(self):
            code = dedent('''
                class SuperTest(object):
                    def __init__(self):
                        super().__init__()
            ''')
            tree = ast.parse(code)
            mod = self._transform_tree(tree)
            self.assertIsInstance(mod, ast.Module)
            cls = mod.body[0]
            self.assertIsInstance(cls, ast.ClassDef)

# Generated at 2022-06-14 02:28:16.967518
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
super()
"""
    assert SuperWithoutArgumentsTransformer(code).result == """super(Cls, self)"""

# Generated at 2022-06-14 02:28:17.903703
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:18.537924
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:24.545379
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert transformer.tree_changed
    expected_tree = ast.parse('super(__class__, __first_arg__)')
    assert ast.dump(tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:28:26.656668
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Testing the constructor"""
    obj = SuperWithoutArgumentsTransformer()
    assert obj.target == (2,7), "The constructor not working fine"


# Generated at 2022-06-14 02:28:35.309950
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..analyses.signature_change_checker import SignatureChangeChecker
    from .annotate_with_original_code import AnnotateWithOriginalCode
    from .base import BaseNodeTransformer
    from .customize_for_meta_class import CustomizeForMetaClass
    from .fix_missing_locations import FixMissingLocations
    from .remove_empty_functions import RemoveEmptyFunctions
    from .remove_staticmethods import RemoveStaticMethods
    from .transform_with_future_division import TransformWithFutureDivision
    from .type_style_checker import TypeStyleChecker
    from ..utils.tree import node_lineno

    # The class definition of the class to be tested

# Generated at 2022-06-14 02:28:39.143578
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:28:47.458635
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Test:
            def __init__(self):
                super()
        """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformed_tree = transformer.visit(tree)
    expected_code = """
        class Test:
            def __init__(self):
                super(Test, self)
        """
    assert ast.dump(transformed_tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:28:56.096619
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.unparse import Unparser
    from ..utils.helpers import ast_from_code
    from ..utils.tree import get_node_of_class
    from ..exceptions import NodeNotFound

    tree = ast_from_code('super()')

    trans = SuperWithoutArgumentsTransformer(tree)
    trans.visit(tree)
    assert Unparser(tree) == 'super(Cls, self)'

    # Test with super() inside method
    tree = ast_from_code('''
    class Cls:
        def method(self):
            super()
    ''')
    trans = SuperWithoutArgumentsTransformer(tree)
    trans.visit(tree)

    cls = get_node_of_class(tree, ast.ClassDef)

# Generated at 2022-06-14 02:28:58.635099
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.tree import ast_parse
    from ..utils.helpers import dump_ast

# Generated at 2022-06-14 02:29:00.564624
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:06.822935
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A():
        def __init__(self):
            return super()
    """
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree, include_attributes=False) == "'''\nclass A():\n    def __init__(self):\n        return super(A, self)\n'''"

# Generated at 2022-06-14 02:29:15.447096
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.visitor import NODE_SWAPPER
    from ..utils.helpers import compile_source
    from ..exceptions import NodeNotFound

    class Foo(object):
        pass

    class Example(object):
        def __init__(self):
            pass

        def __new__(cls, *args, **kwargs):
            return object.__new__(cls)

        def foo(self):
            return super().foo()

    class Broken(object):
        def __init__(self, *args, **kwargs):
            super()

    class AlsoBroken(object):
        def __init__(self, *args, **kwargs):
            pass

        @classmethod
        def foo(cls):
            super()


# Generated at 2022-06-14 02:29:25.857730
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.helpers import get_ast_node_at_or_raise
    from ..utils.ast_builder import build_ast

    code = """
    class Foo:
        def bar(self):
            super()
    """
    node = get_ast_node_at_or_raise(build_ast(code),
                                    line_number=3,
                                    column_offset=9)

    assert isinstance(node, ast.Call)

    transformer = SuperWithoutArgumentsTransformer(build_ast(code))
    transformed = transformer.visit(node)

    assert isinstance(transformed, ast.Call)
    assert isinstance(transformed.func, ast.Name)
    assert transformed.func.id == 'super'
    assert isinstance(transformed.args[0], ast.Name)
    assert transformed.args

# Generated at 2022-06-14 02:29:27.275273
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:32.511178
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    from ..utils.codegen import to_source
    code = 'super()'
    tree = compile(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    res_code = to_source(tree)
    assert 'super(C, self)' in res_code


# Generated at 2022-06-14 02:29:42.020546
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    node = ast3.parse('super()')
    node = SuperWithoutArgumentsTransformer().visit(node)
    assert ast3.dump(node) == "Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[])"

# Generated at 2022-06-14 02:29:48.772150
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import parse
    from ..utils.source import Source
    source = Source("""
        class C:
            def __init__(self):
                super()
                super().__init__()
        """)
    tree = parse(source.read())
    compiler = SuperWithoutArgumentsTransformer()
    compiler.visit(tree)
    assert compile(tree, '<>', 'exec')

# Generated at 2022-06-14 02:29:58.704999
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse(
        """
        class SomeClass(object):
            def some_method(self):
                super().method()
        """,
        mode='exec'
    )

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    cls = tree.body[0]
    func = cls.body[0]
    node = func.body[0].value

    if not isinstance(node, ast.Call):
        raise Exception("Node not Call")

    if not isinstance(node.func, ast.Call):
        raise Exception("Func not Call")

    if not isinstance(node.func.func, ast.Name):
        raise Exception("Func not Name")

    if node.func.func.id != 'super':
        raise Exception("Func not super")


# Generated at 2022-06-14 02:30:09.685768
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    program_ast = ast.parse("super()")
    program_node = program_ast.body[0]

    cls_node = ast.ClassDef(name='Cls', body=[])
    tree = ast.Module(body=[cls_node, program_node])

    func_node = ast.FunctionDef(name='foo', args=ast.arguments(args=[ast.Name(id='self')]))
    cls_node.body.append(func_node)
    func_node.body = [program_node]

    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert isinstance(program_node.args[0], ast.Name)
    assert program_node.args[0].id == 'Cls'

# Generated at 2022-06-14 02:30:10.670728
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile

# Generated at 2022-06-14 02:30:11.685366
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:12.315681
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:17.337887
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    program = 'super()'
    expected = 'super(Cls, self)'
    tree = ast.parse(program)
    SuperWithoutArgumentsTransformer(tree, None).visit(tree)  
    assert astor.to_source(tree) == expected
    

# Generated at 2022-06-14 02:30:22.703481
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class TestNodeTransformer(BaseNodeTransformer):
        def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
            return node

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
            return node

        def visit_Call(self, node: ast.Call) -> ast.Call:
            return node


# Generated at 2022-06-14 02:30:27.612968
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """Tests whether the following code in Python 2.7 is properly transformed to Python 3:
        super()
    """
    code = 'super()'
    # Code in Python 2.7
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    # Code in Python 3
    expected_output = 'super(Cls, self)'
    actual_output = astor.to_source(tree)
    assert expected_output == actual_output

# Generated at 2022-06-14 02:30:37.711808
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    import inspect

    class CodeGenerator(ast.NodeVisitor):
        def __init__(self):
            self.code = []

        def generic_visit(self, node):
            """
            if isinstance(node, ast.FunctionDef):
                print(astor.to_source(node))
            """
            for child in ast.iter_child_nodes(node):
                self.visit(child)

    code = inspect.getsource(SuperWithoutArgumentsTransformer)
    module = ast.parse(code)

    cg = CodeGenerator()
    cg.visit(module)

    assert cg.code != []

# Generated at 2022-06-14 02:30:48.373965
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:30:55.561052
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    #test1
    input1 = '''
super()
'''
    expected_output1 = '''
super(Cls, self)
'''
    tree1 = ast.parse(input1)  # type: ignore
    SuperWithoutArgumentsTransformer().visit(tree1)
    output1 = compile(tree1, filename='<ast>', mode='exec')
    assert(expected_output1 == output1.co_consts[2])

    #test2

# Generated at 2022-06-14 02:31:05.450538
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert ast.dump(tree, include_attributes=False) == \
           'Module(body=[Expr(value=Call(func=Name(id="super", ctx=Load()), ' \
           'args=[Name(id="Cls", ctx=Load()), Name(id="cls", ctx=Load())], ' \
           'keywords=[], starargs=None, kwargs=None))])'

    tree = ast.parse('class Cls:\n'
                     '    def func(self):\n'
                     '        super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:31:09.897814
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import get_ast
    with open('tests/fixtures/optimizers/super_without_arguments.py') as f:
        node = get_ast(f.read())

    SuperWithoutArgumentsTransformer(node).visit(node)

    # print(astunparse.unparse(node))

# Generated at 2022-06-14 02:31:15.974159
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    transformer = SuperWithoutArgumentsTransformer(ast3.parse("super()"), {})
    transformer.visit(transformer.tree)
    assert transformer.tree.body[0].value.args[0].id == 'Cls'
    assert transformer.tree.body[0].value.args[1].id == 'self'

# Generated at 2022-06-14 02:31:25.170090
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    tree = ast.parse('class MyClass: def mymethod(self): super()')
    transformer.visit(tree)
    assert 'super(MyClass, self)' in str(tree)
    assert 'super(MyClass, cls)' not in str(tree)

    tree = ast.parse('class MyClass: def mymethod(self): super("arg")')
    transformer.visit(tree)
    assert 'super("arg")' in str(tree)
    assert 'super(MyClass, self)' not in str(tree)

    tree = ast.parse('class MyClass: @classmethod\n def mymethod(cls): super()')
    transformer.visit(tree)
    assert 'super(MyClass, cls)' in str(tree)

# Generated at 2022-06-14 02:31:27.264444
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import tree
    from .. import test_utils


# Generated at 2022-06-14 02:31:29.474335
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_node


# Generated at 2022-06-14 02:31:38.988816
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():   # type: ignore
    from ..testing.provide_tree import provide_tree

    for version in (2, 7):
        tree = provide_tree(version=version, tree_name='super_no_arg')
        expected = provide_tree(version=version, tree_name='super_no_arg_expected')
        transformer = SuperWithoutArgumentsTransformer(tree, 'super_no_arg')
        assert transformer._tree == tree, 'Unexpected tree after initialization'
        transformer.run()
        assert transformer._tree != tree, 'Tree must change during transformation'
        assert transformer._tree == expected, 'Unexpected tree after transformation'

# Generated at 2022-06-14 02:31:55.764071
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    super_ = ast.Name(id='super')

    call = ast.Call(func=super_, args=[])
    assert SuperWithoutArgumentsTransformer.get_transformed_ast(call).body[0].value.func.id == 'super'

    class ClsDef(ast.AST):
        _fields = ('name', )

    class ClsBody(ast.AST):
        _fields = ('body', )

    class Cls(ast.AST):
        _fields = ('class_node', 'body_node')

    class FuncDef(ast.AST):
        _fields = ('args', )

    class Arguments(ast.AST):
        _fields = ('args',)

    class Arg(ast.AST):
        _fields = ('arg', )


# Generated at 2022-06-14 02:32:05.177705
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    import sys
    import os.path

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    from test_nodes import super_without_arguments_test

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(super_without_arguments_test))

    runner = unittest.TextTestRunner(verbosity = 3)
    result = runner.run(suite)

# Generated at 2022-06-14 02:32:12.166806
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast, source_to_code
    from ..utils.tree import tree_to_str

    code = """
    class Cls(object):
        def __init__(self):
            super()
            self._a = 0
    """

    expected_code = """
    class Cls(object):
        def __init__(self):
            super(Cls, self)
            self._a = 0
    """

    tree = source_to_ast(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    result_code = source_to_code(tree)
    assert result_code == code



# Generated at 2022-06-14 02:32:15.078333
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ast import parse
    from .util import run_visitor_class


# Generated at 2022-06-14 02:32:18.350013
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_without_arguments = 'super()'
    tree = ast.parse(super_without_arguments)

# Generated at 2022-06-14 02:32:23.891205
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''super()'''
    expected_code = '''super(Cls, self)'''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert expected_code == astunparse.unparse(tree)

# Generated at 2022-06-14 02:32:24.474438
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:32:25.401825
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:34.803844
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..test.test_utils import transform_test_with_target, assert_same_ast_structure

    def super_call_no_args(a):
        super()

    def super_call_with_args(a):
        super(object, a)

    def super_call_with_args_and_keyword(a):
        super(a)

    transform_test_with_target(SuperWithoutArgumentsTransformer, super_call_no_args, assert_same_ast_structure)
    transform_test_with_target(SuperWithoutArgumentsTransformer, super_call_with_args, assert_same_ast_structure)
    transform_test_with_target(SuperWithoutArgumentsTransformer, super_call_with_args_and_keyword, assert_same_ast_structure)

# Generated at 2022-06-14 02:32:43.557433
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    code = """
    class Test:
        def func(self):
            super()
    """

    expected_code = """
    class Test:
        def func(self):
            super(Test, self)
    """
    tree = ast.parse(code)
    SubSuperWithoutArgumentsTransformer().generic_visit(tree)
    assert astor.to_source(tree) == expected_code

    code = """
    class Test:
        def func(self):
            sub_tree = super()
    """

    expected_code = """
    class Test:
        def func(self):
            sub_tree = super(Test, self)
    """
    tree = ast.parse(code)
    SubSuperWithoutArgumentsTransformer().generic_visit(tree)

# Generated at 2022-06-14 02:33:07.211556
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test that SuperWithoutArgumentsTransformer transforms super() call to super() call with class and self"""
    from .test_pipeline import create_pipeline_from_unittest
    class_ast = create_pipeline_from_unittest(1, 
        """\
        class TestSuperWithoutArguments(object):
            def test_super_not_in_class(self):
                super()
            def test_super_in_class(self):
                super()
        """,
        [SuperWithoutArgumentsTransformer])
    print(ast.dump(class_ast))

    # Test that super() call in not in class stays the same
    assert len(class_ast.body) == 1
    assert len(class_ast.body[0].body) == 2

# Generated at 2022-06-14 02:33:09.894799
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Verify that the SuperWithoutArgumentsTransformer class constructs a SuperWithoutArgumentsTransformer object"""
    assert isinstance(SuperWithoutArgumentsTransformer(), SuperWithoutArgumentsTransformer)

# Unit tests for visit_Call

# Generated at 2022-06-14 02:33:11.806868
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:33:22.873420
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    # Replacement of super()
    source = """
mylist = list()
super(mylist)
    """
    tree = ast.parse(source)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert ast.dump(tree) == '''Module(body=[Assign(targets=[Name(id='mylist', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[], keywords=[])), Call(func=Name(id='super', ctx=Load()), args=[Name(id='mylist', ctx=Load())], keywords=[])])'''

    # Replacement of super() within function body

# Generated at 2022-06-14 02:33:29.366223
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(None, None)
    node = ast.Call()
    node.func = ast.Name(id='super')
    node.args = []
    transformer._replace_super_args(node)
    assert len(node.args) == 2
    assert type(node.args[0]) is ast.Name
    assert node.args[0].id == 'Cls'
    assert type(node.args[1]) is ast.Name
    assert node.args[1].id == 'self'

# Generated at 2022-06-14 02:33:32.046153
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    module_ast = ast.parse("super()")
    SuperWithoutArgumentsTransformer().visit(module_ast)
    assert(str(module_ast) == "super(Cls, self)")

# Generated at 2022-06-14 02:33:34.910311
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast import parse
    from ..utils.fake_context import FakeContext
    from ..utils.helpers import get_ast_node_name


# Generated at 2022-06-14 02:33:42.793902
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..ast_transformer import tree_to_code
    from ..ast_transformer import get_ast

    code = """
    class SuperArgumentless():
        def __init__(self):
            super()
    """
    node = get_ast(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(node)
    assert tree_to_code(node).strip() == """
    class SuperArgumentless():
        def __init__(self):
            super(SuperArgumentless, self)
    """.strip()

# Generated at 2022-06-14 02:33:49.749227
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test(ast.NodeTransformer):

        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                node.args = [ast.Name(id='Cls'), ast.Name(id='self')]
            return node

    code = 'class A: def __init__(self): super().a()'
    tree = ast.parse(code)
    tree = tree.body[0]
    transformer = SuperWithoutArgumentsTransformer(tree, None)
    transformer.visit(tree)
    transformer = Test()
    tree = transformer.visit(tree)

    assert isinstance(tree.body[0], ast.FunctionDef)

# Generated at 2022-06-14 02:33:51.618437
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode

# Generated at 2022-06-14 02:34:27.398113
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import parse
    from .base import BaseNodeTransformer

    source = """class Base(object):
        def __init__(self):
            super().__init__()
    """
    expected = """
        class Base(object):
            def __init__(self):
                super(Base, self).__init__()
    """
    tree = parse(source)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert expected == astor.to_source(tree)

# Generated at 2022-06-14 02:34:34.844553
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import ast
    import typed_ast.ast3 as typed_ast

    # Check that a Call with a super() is transformed in the expected way
    call_node = ast.parse("super()").body[0]
    class_node = ast.ClassDef()
    function_node = ast.FunctionDef()
    function_node.args = ast.arguments()
    function_node.args.args = [typed_ast.arg(arg="self", annotation=None)]
    super_transformer = SuperWithoutArgumentsTransformer([], "")
    super_transformer.visit(call_node)
    assert isinstance(call_node, typed_ast.Call) # type: ignore
    assert call_node.args[0].id == class_node.name

# Generated at 2022-06-14 02:34:43.657420
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Test(SuperWithoutArgumentsTransformer):
        def visit_Call(self, node: ast.Call) -> None:
            pass

    node = ast.Call(
        func=ast.Name(id='super', ctx=ast.Load()),
        args=[
        ],
        keywords=[
        ],
    )

    transformer = Test()
    transformer.visit_Call(node)

    assert len(node.args) == 2
    assert isinstance(node.args[0], ast.Name)
    assert node.args[0].id == 'cls'

# Generated at 2022-06-14 02:34:53.290901
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
            class foo:
                def __init__(self, bar):
                    super()
                    super()
    """

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:34:58.315694
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """super(A, b)"""
    # tree = ast.parse(code)
    # compiler = SuperWithoutArgumentsTransformer()
    # compiler.visit_tree(tree)
    # target = """super(A, b)"""
    # assert compile(tree, '', 'exec') == compile(target, '', 'exec')

# Generated at 2022-06-14 02:35:02.422023
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import Source
    from .. import refactor
    from ..utils.helpers import version
    from ..utils.helpers import version_info


# Generated at 2022-06-14 02:35:03.844842
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:12.584514
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_in = dedent("""\
    class A:
        def __init__(self, a):
            super().__init__()
                
    """)

    tree = ast.parse(code_in)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

    code_out = dedent("""\
    class A:
        def __init__(self, a):
            super(A, self).__init__()
                
    """)

    assert parse_ast(code_in) == parse_ast(code_out), 'SuperWithoutArgumentsTransformer produces wrong output'

# Generated at 2022-06-14 02:35:23.104995
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .test_utils import assertAstEqual, assertAstNotEqual
    from .test_utils import parse_and_transform

    transform = SuperWithoutArgumentsTransformer().visit
    parse = lambda code: ast.parse(code, mode='eval')

    assertAstEqual(
        parse('super()'),
        parse_and_transform('super(Cls, self)', transform),
    )
    assertAstEqual(
        parse('super(Cls, self)'),
        parse_and_transform('super(Cls, self)', transform),
    )
    assertAstEqual(
        parse('super(Cls, cls)'),
        parse_and_transform('super(Cls, cls)', transform),
    )

# Generated at 2022-06-14 02:35:34.775683
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    input_source = """
        class A:
            def m1(self):
                return super()
            def m2(self, a):
                return a + super()
        
        class B(A):
            def m3(self):
                return super()
        """

    expected_output = """
        class A:
            def m1(self):
                return super(A, self)
            def m2(self, a):
                return a + super(A, self)
        
        class B(A):
            def m3(self):
                return super(B, self)
        """

    from .. import transform

    actual_output = transform(input_source, [SuperWithoutArgumentsTransformer])

    assert actual_output == expected_output

# Generated at 2022-06-14 02:36:42.349471
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:54.193734
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse('''
        class C():
            def __init__(self):
                super().__init__()
    ''').body[0].body[0]

    SuperWithoutArgumentsTransformer().visit(node)
    assert isinstance(node.body[0], ast.Expr)
    assert isinstance(node.body[0].value, ast.Call)
    assert isinstance(node.body[0].value.func, ast.Name)
    assert node.body[0].value.func.id == 'super'
    assert len(node.body[0].value.args) == 2
    assert isinstance(node.body[0].value.args[0], ast.Name)
    assert node.body[0].value.args[0].id == 'C'

# Generated at 2022-06-14 02:36:54.800348
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:59.916370
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    def foo():
        super()
    
    class A:
        def __init__():
            super()
        '''

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert code.replace('super()', 'super(A, self)') == compile(tree, '', mode='exec').strip()

# Generated at 2022-06-14 02:37:06.327280
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class MyClass:
        def __init__(self, max_numbers=5):
            super()
            pass

        def do_something(self, data):
            super()
            pass
    """
    expected_code = """
    class MyClass:
        def __init__(self, max_numbers=5):
            super(MyClass, self)
            pass

        def do_something(self, data):
            super(MyClass, self)
            pass
    """
    assert expected_code == compile_to_fixed(code, SuperWithoutArgumentsTransformer)

# Generated at 2022-06-14 02:37:11.614001
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Tests `SuperWithoutArgumentsTransformer`.
    """
    tree = ast.parse('class A():\n    def __init__(self):\n        super()\n'
                     'class B():\n    def __init__(self):\n        super()')
    transformer = SuperWithoutArgumentsTransformer(tree=tree)
    transformer.run()
    assert 'super' not in astor.to_source(tree)

# Generated at 2022-06-14 02:37:20.124908
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode as u
    from ast import parse as ast_parse
    from typed_ast import ast3 as ast

    super_node = ast.Call()
    super_node.func = ast.Name(id='super', ctx=ast.Load())

    with_args_node = ast.Call()
    with_args_node.func = ast.Name(id='super', ctx=ast.Load())
    with_args_node.args = [ast.Str(s='args')]

    nested_args_node = ast.Call()
    nested_args_node.func = ast.Name(id='super', ctx=ast.Load())
    nested_args_node.args = [super_node]

    class_node = ast.ClassDef()

# Generated at 2022-06-14 02:37:22.472360
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:23.595462
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:31.680321
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Some:
            def __init__(self, a, b):
                super()

        class Other:
            def __init__(self, a, b, c):
                super(Other)

        class New:
            def __init__(self, a, b):
                super()

            def __new__(cls, a, b):
                super(cls, None)
    """