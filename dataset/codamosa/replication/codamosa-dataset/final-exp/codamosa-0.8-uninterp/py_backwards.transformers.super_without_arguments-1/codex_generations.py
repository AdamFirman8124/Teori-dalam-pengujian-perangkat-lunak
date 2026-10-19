

# Generated at 2022-06-14 02:28:08.354167
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class TestNodeTransformer(BaseNodeTransformer):
        pass

    code = """
    class Cls(object):
        def test(self):
             super()
        @staticmethod
        def test_static():
            super()
        @classmethod
        def test_class(cls):
            super()
    """
    tree = ast.parse(code)
    node_transformer = SuperWithoutArgumentsTransformer(tree, TestNodeTransformer())
    node_transformer.visit(tree)
    output = astor.to_source(tree)

# Generated at 2022-06-14 02:28:09.321660
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:11.745572
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:12.722053
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:14.226476
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:23.211368
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile_src
    from .helpers import assert_node
    from typed_ast import ast3 as ast

    src = """
    class Base(object):
        def __init__(self):
            super()

    class Derived(Base):
        def __init__(self):
            super()
    """

    tree = compile_src(src, __name__, 'exec')
    correct = compile_src(src, __name__, 'exec', target=(2, 6))

    sut = SuperWithoutArgumentsTransformer(tree)
    assert_node(sut.visit(tree), correct)



# Generated at 2022-06-14 02:28:24.271738
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:24.928448
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:28:34.769851
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class SuperWithoutArgumentsTransformerTest(unittest.TestCase):
        def test_SuperWithoutArgumentsTransformer(self):
            with open(os.path.join(os.path.dirname(__file__), 'SuperWithoutArgumentsTransformer_1.in')) as file:
                source = file.read()
            with open(os.path.join(os.path.dirname(__file__), 'SuperWithoutArgumentsTransformer_1.out')) as file:
                expected_output = file.read()
            tree = ast.parse(source)
            SuperWithoutArgumentsTransformer().visit(tree)
            output = astunparse.unparse(tree)
            self.assertEqual(output, expected_output)


# Generated at 2022-06-14 02:28:45.440189
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])
    func = ast.FunctionDef(name='foo', args=ast.arguments(args=[ast.arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[super_node], decorator_list=[])
    cls = ast.ClassDef(name='bar', bases=[ast.Name(id='object', ctx=ast.Load())], keywords=[], body=[func], decorator_list=[])
    tree = ast.Module(body=[cls])
    SuperWithoutArgumentsTransformer(tree).run()

# Generated at 2022-06-14 02:28:55.800827
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.helpers import get_ast_node

    tree = get_ast_node("""
        class C(object):
            def assert_true(self):
                super()
        """)
    t = SuperWithoutArgumentsTransformer()
    t.visit(tree)
    assert tree.body[0].body[0].value.func.args[0].id == 'C'
    assert tree.body[0].body[0].value.func.args[1].id == 'self'

    for i in range(2):
        tree = get_ast_node("""
            class C(object):
                def __init__(self, arg): super()
            """)
        t = SuperWithoutArgumentsTransformer()
        t.visit(tree)

# Generated at 2022-06-14 02:28:56.929664
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:10.108663
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    module = ast.parse('super()')
    node = get_func_body(module)[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'super'

    transformer = SuperWithoutArgumentsTransformer(ast.parse('super()'))
    node = transformer.visit(node)
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'super'
    assert len(node.value.args) == 2
    assert isinstance(node.value.args[0], ast.Name)

# Generated at 2022-06-14 02:29:10.756293
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:12.133196
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import roundtrip

# Generated at 2022-06-14 02:29:23.078666
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:35.337128
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode as u
    from ..utils import ast_from_str

    source = u("""
    class A(object):
        def __init__(self):
            super().__init__()
    """)

    tree = ast_from_str(source)
    trans = SuperWithoutArgumentsTransformer(tree)
    tree = trans.visit(tree)


# Generated at 2022-06-14 02:29:36.414454
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:46.757024
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .compile import compile_str
    from .unwrap_lambda import UnwrapLambdaTransformer
    from .staticmethods import StaticMethodTransformer
    from ..tree import Module
    module = Module(body=[])

# Generated at 2022-06-14 02:29:57.549685
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # Case 1: super() outside of function
    tree = ast.parse('super()')
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    assert(ast.dump(tree) == 'Module(body=[Expr(value=Call(func=Name(id=\'super\', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))])')


    # Case 2: super() outside of class
    tree = ast.parse('def f(): super()')
    tree = SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:30:05.214559
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import transform
    from .. import utils


# Generated at 2022-06-14 02:30:06.375839
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:10.764072
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = """super()"""
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    result = ast.fix_missing_locations(tree)
    assert astor.to_source(result) == """super(Cls, self)"""


# Generated at 2022-06-14 02:30:20.815749
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node_dumps_equal_pairs = [
        # The following node will not be transformed
        (
            ast.Call(func=ast.Name(id='super'), args=[ast.Name(id='A')], keywords=[]),
            ast.Call(func=ast.Name(id='super'), args=[ast.Name(id='A')], keywords=[])
        ),

        # The following node will be transformed
        (
            ast.Call(func=ast.Name(id='super'), args=[], keywords=[]),
            ast.Call(func=ast.Name(id='super'), args=[ast.Name(id='Cls'), ast.Name(id='self')], keywords=[])
        ),
    ]


# Generated at 2022-06-14 02:30:21.768090
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:23.125636
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(2, 7)

# Generated at 2022-06-14 02:30:24.981083
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    import _ast
    ast.dump = _ast.dump


# Generated at 2022-06-14 02:30:26.152951
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:26.962427
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:35.887150
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    from ..utils.testing import assert_transformed_code_equals
    code = 'super()'
    tree = ast.parse(code)
    expected_tree = ast.parse('super(Cls, self)')

    transformer = SuperWithoutArgumentsTransformer(tree=tree)

    transformer._replace_super_args = MagicMock(return_value=None)
    transformer._tree_changed = False

    actual_tree = transformer.visit_Call(tree.body[0].value)

    assert transformer._replace_super_args.called
    assert transformer._tree_changed

    assert_transformed_code_equals(astor.to_source(actual_tree), astor.to_source(expected_tree))

# Generated at 2022-06-14 02:30:43.158952
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:44.342187
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:45.673035
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:53.319885
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    tree = ast.parse("super()")
    tree_changed = transformer.visit(tree)
    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"
    assert tree_changed == True

# Generated at 2022-06-14 02:31:04.833644
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from . import BaseNodeTransformer

    class SuperWithoutArgumentsTransformer(BaseNodeTransformer):
        """Compiles:
            super()
        To:
            super(Cls, self)
            super(Cls, cls)
                
        """
        target = (2, 7)
        
        def _replace_super_args(self, node: ast.Call) -> None:
            try:
                func = get_closest_parent_of(self._tree, node, ast.FunctionDef)
            except NodeNotFound:
                warn('super() outside of function')
                return
            

# Generated at 2022-06-14 02:31:08.943754
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    program = Program.from_source('''
        class MyClass:
            def __init__(self, x):
                super()
                print(x)
        ''')
    SuperWithoutArgumentsTransformer(program).transform()

# Generated at 2022-06-14 02:31:21.147696
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..testing import assert_source

    def test_super(cls):
        super()

    def test_no_super():
        print()

    def test_super_with_args(cls):
        super(cls, cls)


# Generated at 2022-06-14 02:31:22.312449
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:22.860135
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:31:30.618283
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import inspect
    import dis
    import astor

    module_ast = ast.parse(inspect.getsource(SuperWithoutArgumentsTransformer))

    compiler = SuperWithoutArgumentsTransformer(module_ast)
    new_ast = compiler.visit(module_ast)
    codeobj1 = compile(new_ast, '', 'exec')
    codeobj2 = compile(module_ast, '', 'exec')

    print(dis.dis(codeobj1))
    print(astor.dump_tree(new_ast))

# Generated at 2022-06-14 02:31:38.099143
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:39.225172
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:40.682753
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # TODO: figure out how to test this code
    pass

# Generated at 2022-06-14 02:31:42.000502
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:54.095428
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code1 = '''
    def get_id():
        return super():
    '''

    code2 = '''
    class A:
        def __init__(self):
            return super():
    '''

    code3 = '''
    class A:
        def __init__(self):
            return super():
    class B(A):
        def __init__(self):
            return super():
    '''

    t1 = ast.parse(code1)
    assert ''.join(ast.get_source(t1)) == 'def get_id():\n    return super()\n'

    t2 = SuperWithoutArgumentsTransformer(2, 7, t1).run()

# Generated at 2022-06-14 02:31:55.145277
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:32:02.973247
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse(
            "super()",
            mode='eval'
    )
    transformer = SuperWithoutArgumentsTransformer(node)
    node = transformer.visit(node)
    assert ast.dump(node) == "Module(body=Call(func=Super(args=[], keywords=[]), args=[Name(id='Foo'), Name(id='self')], keywords=[], starargs=None, kwargs=None))"

# Generated at 2022-06-14 02:32:03.661897
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:11.099932
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3
    from .helpers import assert_source_equal

    code = """
            class Foo(super):
                def bar(self):
                    super()
            """
    _ast = ast.parse(code)

    transformer = SuperWithoutArgumentsTransformer()
    result = transformer.visit(_ast)
    assert transformer._tree_changed is True
    assert_source_equal(result, """
            class Foo(super):
                def bar(self):
                    super(Foo, self)
            """)

# Generated at 2022-06-14 02:32:19.782465
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='super'), args=[], keywords=[], starargs=None, kwargs=None)
    transformer = SuperWithoutArgumentsTransformer(ast.parse('func()'), 'str')
    transformer._replace_super_args = lambda node: None
    transformer.visit_Call(node)
    assert len(node.args) == 2
    assert isinstance(node.args[0], ast.Name)
    assert isinstance(node.args[1], ast.Name)

# Generated at 2022-06-14 02:32:35.205439
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = ''' 
    class A:
        def __init__(self):
            super()
    '''
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    exec(compile(tree, "<ast>", "exec"), locals(), globals())
    assert locals()['A'].__init__.__code__.co_code == b's\x00d\x01|l\x00d\x00\x84\x00\x83\x00\x01\x00d\x00S\x00'

# Generated at 2022-06-14 02:32:46.286655
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
# Input 0
    in0_node0 = ast.Call()
    in0_node0.func = ast.Name(id='super')
# Output 0
    out0_node0 = ast.Call()
    out0_node0.func = ast.Name(id='super')
    out0_node0.args = [ast.Name(id='Cls'), ast.Name(id='a')]
# Output 1
    out1 = None
# Call function

# Generated at 2022-06-14 02:32:47.565445
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:48.209503
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:53.798332
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse("""
    class Spam:
        def __init__(self):
            super()
    """)

    transformer = SuperWithoutArgumentsTransformer(tree=node)
    transformer.run()
    assert str(node) == "class Spam:\n    def __init__(self):\n        super(Spam, self)"

# Generated at 2022-06-14 02:33:00.080992
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = """
    class Cls:
        def __init__(self):
            super()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).run()
    expected_code = """
    class Cls:
        def __init__(self):
            super(Cls, self)
    """
    assert astor.to_source(tree) == expected_code



# Generated at 2022-06-14 02:33:00.702444
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:03.064230
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from astunparse import unparse
    from .transformers import ClassDefTransformer, FunctionDefTransformer
    import ast


# Generated at 2022-06-14 02:33:11.812974
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode

    from .. import setup_type_inference_context

    from .function_transformer import FunctionTransformer
    from .class_transformer import ClassTransformer

    source = (
        u'class Foo:\n'
        u'    def func(self, a, b, c):\n'
        u'        super()\n'
    )
    tree = ast.parse(source_to_unicode(source))
    context = setup_type_inference_context()
    tree = context.run_pipeline(tree, FunctionTransformer, ClassTransformer, SuperWithoutArgumentsTransformer)
    assert type(tree.body[0].body[0].body[0]) is ast.Call

# Generated at 2022-06-14 02:33:12.505087
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:47.549057
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..testing_utils import make_simple_func
    from ..utils.tree import ast_to_str
    from ..utils.helpers import get_first_ast_node

    code = """\
    class Cls(object):
        def f(self):
            super()
            
    """
    expected_code = """\
    class Cls(object):
        def f(self):
            super(Cls, self)
            
    """
    tree = ast.parse(code)
    node = get_first_ast_node(tree, ast.Name, id='super')
    transformer = SuperWithoutArgumentsTransformer(tree=tree)
    transformer.visit(node)
    assert ast_to_str(tree) == expected_code



# Generated at 2022-06-14 02:33:50.895038
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .fake_ast import f

    assert SuperWithoutArgumentsTransformer(f.ClassDef1, {}).visit(f.Call1) == f.Call2

# Generated at 2022-06-14 02:33:53.115453
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer(tree=node)
    transformer.run()
    assert str(node) == 'super(Cls, self)'

# Generated at 2022-06-14 02:33:53.831268
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:58.894713
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test that super() calls are transformed to calls which
    contain the class name and self.

    """
    c = SuperWithoutArgumentsTransformer()
    tree = ast.parse('super()')
    c.visit(tree)

    assert(len(tree.body[0].value.args) == 2)

# Generated at 2022-06-14 02:33:59.381185
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:01.021958
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:02.375926
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import tree


# Generated at 2022-06-14 02:34:13.400488
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer(ast.parse("""class A:
    def __init__(self):
        super()"""))

    assert transformer.tree_changed is True

    # Expected: super(A, self)
    tree = transformer.new_tree
    assert isinstance(tree, ast.Module)
    assert isinstance(tree.body[0], ast.ClassDef)

    cls = tree.body[0]
    assert cls.name == 'A'
    assert len(cls.body) == 1
    assert isinstance(cls.body[0], ast.FunctionDef)

    func = cls.body[0]
    assert func.name == '__init__'
    assert len(func.body) == 1
    assert isinstance(func.body[0], ast.Expr)

# Generated at 2022-06-14 02:34:22.191477
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .bases import NodeTransformerTestCase

    class Test(NodeTransformerTestCase):
        target_node = ast.Call
        transformer = SuperWithoutArgumentsTransformer

        def create_target_node(self):
            return ast.Call(ast.Name(id='super', ctx=ast.Load()), [], [])

        def create_valid_node(self):
            return ast.Call(ast.Call(ast.Name(id='super', ctx=ast.Load()),
                                     [],
                                     []),
                            [],
                            [])


# Generated at 2022-06-14 02:35:31.060386
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = '''
        class Chicken:
            def abc(x):
                super()
            def abc(a, b):
                super()
            def __init__(self):
                super()
    '''
    expected = '''
        class Chicken:
            def abc(x):
                super(Chicken, x)
            def abc(a, b):
                super(Chicken, a)
            def __init__(self):
                super(Chicken, self)
    '''
    tree = ast.parse(source)
    t = SuperWithoutArgumentsTransformer(tree)
    t.run()
    assert str(tree) == expected


# Generated at 2022-06-14 02:35:35.330265
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class TestTransformer(BaseNodeTransformer):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name):
                if node.func.id == 'super':
                    return ast.Str('100')
            return node


# Generated at 2022-06-14 02:35:44.511463
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = textwrap.dedent('''
        class A:
            def f1(self):
                super()

            def f2(self):
                super.a()

            @staticmethod
            def f3(self):
                super()


        class B(A):
            def f4(self):
                super()

            @staticmethod
            def f5(self):
                super()

        class C:
            def f6(self):
                super()

        class D(A):
            def f7(self):
                super().__init__()

        class F:
            def f8(self):
                super().__init__()
    ''')

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)


# Generated at 2022-06-14 02:35:49.544341
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
        class A:
            def __init__(self):
                super()
    '''
    module = ast.parse(code)
    cls = module.body[0]
    func = cls.body[0]
    super_call = func.body[0]
    assert isinstance(super_call, ast.Expr)
    assert isinstance(super_call.value, ast.Call)

# Generated at 2022-06-14 02:36:00.141520
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    module_node = ast.parse("""
    class X:
        def __init__(self):
            super()
    """)  # type: ast.Module

    t = SuperWithoutArgumentsTransformer()
    new_ast = t.visit(module_node)

    assert isinstance(new_ast.body[0], ast.ClassDef)
    cls_node = new_ast.body[0]  # type: ast.ClassDef
    assert isinstance(cls_node.body[0], ast.FunctionDef)
    func_node = cls_node.body[0]  # type: ast.FunctionDef
    assert isinstance(func_node.body[0], ast.Expr)
    expr_node = func_node.body[0]  # type: ast.Expr

# Generated at 2022-06-14 02:36:02.446889
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    module = ast.parse("super()", mode="exec")
    transformer = SuperWithoutArgumentsTransformer(module)
    transformer.visit(module)
    assert len(module.body[0].value.args) == 2

# Generated at 2022-06-14 02:36:11.692146
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import assert_transformation, transform

    assert_transformation(SuperWithoutArgumentsTransformer, """
        super()
    """, """
        super(Cls, self)
    """)

    assert_transformation(SuperWithoutArgumentsTransformer, """
        class Foo:
            def __new__(cls):
                super()

            def __init__(self):
                super()
    """, """
        class Foo:
            def __new__(cls):
                super(Foo, cls)

            def __init__(self):
                super(Foo, self)
    """)


# Generated at 2022-06-14 02:36:23.094688
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('''
    class Spam():
        def __init__(self):
            super()
    class Eggs():
        def __init__(cls):
            super()

    ''')

    tree = SuperWithoutArgumentsTransformer().visit(tree)  # type: ignore
    constructor1 = tree.body[0].body[0]
    assert len(constructor1.body) == 1
    assert isinstance(constructor1.body[0], ast.Call)
    assert isinstance(constructor1.body[0].args[0], ast.Name)
    assert constructor1.body[0].args[0].id == "Spam"
    assert isinstance(constructor1.body[0].args[1], ast.Name)

# Generated at 2022-06-14 02:36:33.363077
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    superWithoutArgumentsTransformer = SuperWithoutArgumentsTransformer()
    tree = ast.parse("""class Example:
        def __init__(self):
            super()""")
    superWithoutArgumentsTransformer.visit(tree)

# Generated at 2022-06-14 02:36:46.703269
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest
    import ast as pyast
    from ..utils.tree import compile_tree, tree_to_code

    def compile_code(code: str) -> str:
        tree = compile_tree(pyast.parse(code), SuperWithoutArgumentsTransformer)
        return tree_to_code(tree)

    class TestSuperWithoutArgumentsTransformer(unittest.TestCase):

        def test_super_in_function(self) -> None:
            code = '''
            class Cls:
                def __init__(self):
                    super()
            '''
            new_code = '''
            class Cls:
                def __init__(self):
                    super(Cls, self)
            '''
            self.assertEqual(compile_code(code), compile_code(new_code))

