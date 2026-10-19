

# Generated at 2022-06-14 02:28:09.595361
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import parse

    # Test simple case
    class_ast = parse('class Foo(object):\n    def __init__(self): super().__init__()')
    transformer = SuperWithoutArgumentsTransformer(class_ast)
    transformer.run()
    print(class_ast)
    assert class_ast.body[0].body[0].body[0].value.args[0].id == 'Foo'
    assert class_ast.body[0].body[0].body[0].value.args[1].id == 'self'

    # Test simple case 2
    class_ast = parse('class Foo(object):\n    @staticmethod\n    def foo(): super().__init__()')
    transformer = SuperWithoutArgumentsTransformer(class_ast)
    transformer.run()

# Generated at 2022-06-14 02:28:13.802184
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    func = ast.parse('super()').body[0]
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(func)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 02:28:20.848415
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Base:
        def __init__(self):
            super().__init__()
        """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

    expected = """
    class Base:
        def __init__(self):
            super(Base, self).__init__()
        """
    expected = ast.parse(expected)
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:28:24.851207
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pyi = """class Test:
    def __init__(self):
        super()
    """
    py = """class Test:
    def __init__(self, self1):
        super(Test, self1)
    """
    assert SuperWithoutArgumentsTransformer.run_on_string(pyi) == py

# Generated at 2022-06-14 02:28:34.976468
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from . import BaseNodeTransformerTest

    class Test(BaseNodeTransformerTest):
        target_transformer = SuperWithoutArgumentsTransformer
        target_version = (2, 7)

        def test_no_change(self):
            node = ast3.parse("""
                class A(object):
                    def __init__(self):
                        super(A, self).__init__()
            """)
            new_node = self.changed(node)
            self.assertNotEqual(new_node, node)

        def test_change(self):
            node = ast3.parse("""
                class A(object):
                    def __init__(self):
                        super().__init__()
            """)
            new_node = self.changed(node)
            self.assertNotE

# Generated at 2022-06-14 02:28:40.928654
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from ..utils.helpers import get_ast_node_string

    source = '''
super()
'''

    cls = SuperWithoutArgumentsTransformer()

    nodes = source_to_nodes(source)
    nodes = cls.transform(nodes)

    assert get_ast_node_string(nodes[0][1]) == 'super(Cls, self)'

# Generated at 2022-06-14 02:28:44.280446
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .. import compile_
    from ..defaults import PYTHON3_VERSION


# Generated at 2022-06-14 02:28:45.981996
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typing import List
    import astor

# Generated at 2022-06-14 02:28:48.683693
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit tests for SuperWithoutArgumentsTransformer
    
    """
    
    # Arrange

# Generated at 2022-06-14 02:28:49.863344
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Not Used test case
    pass

# Generated at 2022-06-14 02:28:58.383119
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import cst_from_code
    from .base import BaseUnparseTest

    tree = cst_from_code("super()")
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    unparse_test = BaseUnparseTest(tree, expected_code="super(Cls, self)")
    unparse_test.run_tests()

# Generated at 2022-06-14 02:29:06.924620
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast

    tree = source_to_ast.parse('''
        class Test(a):
            def __init__(self):
                s = super()
    ''')

    SuperWithoutArgumentsTransformer().visit(tree)

    from ..utils.source import ast_to_source
    src = ast_to_source(tree)
    assert src == """class Test(a):
    def __init__(self):
        s = super(Test, self)"""

# Generated at 2022-06-14 02:29:15.503722
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..utils.helpers import compile_source

    # Test with function
    source = Source("""
        class Foo:
            def bar(self):
                return super()
    """)
    expected = Source("""
        class Foo:
            def bar(self):
                return super(Foo, self)
    """)
    tree = compile_source(source, SuperWithoutArgumentsTransformer)
    assert expected == tree

    # Test with classmethod
    source = Source("""
        class Foo:
            @classmethod
            def bar(cls):
                return super()
    """)
    expected = Source("""
        class Foo:
            @classmethod
            def bar(cls):
                return super(Foo, cls)
    """)

# Generated at 2022-06-14 02:29:26.464580
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # fmt: off
    source = inspect.cleandoc(
        """
        class Cls:
            def test(self):
                super()
        """
    )
    # fmt: on

    expected_result = inspect.cleandoc(
        """
        class Cls:
            def test(self):
                super(Cls, self)
        """
    )

    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)
    assert ast.dump(new_tree) == expected_result

# Generated at 2022-06-14 02:29:33.893202
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer(ast_tree=ast.AST())

    call = ast.Call()
    call.func = ast.Name()
    call.func.id = "super"
    call.args = []
    assert not super_without_arguments_transformer.visit_Call(node=call)
    assert call.args[0].id == "Cls"
    assert call.args[1].id == "self"


# Generated at 2022-06-14 02:29:40.172045
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    stmt = 'class X:\n def f(self):\n  super()'
    expect = 'class X:\n def f(self):\n  super(X, self)'
    tree = ast.parse(stmt)
    t = SuperWithoutArgumentsTransformer()
    t.visit(tree)
    assert t.tree_changed == True
    assert astunparse.unparse(tree) == expect


# Generated at 2022-06-14 02:29:49.290991
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.ast_importer import AstImporter
    from ..utils.helpers import filename_to_modulename
    import sys

    class A(object):
        def __init__(self):
            super()

    source = AstImporter().visit(ast.fix_missing_locations(ast.parse(inspect.getsource(A))))
    tree = SuperWithoutArgumentsTransformer().visit(source)
    sys.modules[filename_to_modulename(__file__)] = tree

    import test_SuperWithoutArgumentsTransformer
    cls = getattr(test_SuperWithoutArgumentsTransformer, 'A')

    instance = cls()

    if not isinstance(instance, object):
        raise TypeError

# Generated at 2022-06-14 02:29:58.986310
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from typed_ast import parse
    from ..utils.tree import get_closest_parent_of
    from ..utils.helpers import warn
    from ..exceptions import NodeNotFound
    from .base import BaseNodeTransformer

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

           

# Generated at 2022-06-14 02:30:09.733365
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.pyversion import PY35

    code = 'super()'
    tree = ast.parse(code)
    tree_copy = copy.deepcopy(tree)

    SuperWithoutArgumentsTransformer().visit(tree)

    expected_code = 'super(Test, self)' if PY35 else 'super(Test, cls)'
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))

    code = 'super(foo)'
    tree = ast.parse(code)
    tree_copy = copy.deepcopy(tree)

    SuperWithoutArgumentsTransformer().visit(tree)

    expected_code = 'super(foo)'
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))


# Generated at 2022-06-14 02:30:19.804833
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_without_args_transformer = SuperWithoutArgumentsTransformer()
    class_def_ast = ast.parse('class A: super()\n').body[0]
    super_without_args_transformer.visit(class_def_ast)

# Generated at 2022-06-14 02:30:27.355690
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTest

    code = """
if True:
    super()
"""
    tree = ast.parse(code)  # type: ignore
    BaseNodeTransformerTest(SuperWithoutArgumentsTransformer, code, tree)

# Generated at 2022-06-14 02:30:36.001941
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == \
        "Module(body=[FunctionDef(name='', args=arguments(args=[arg(arg='C', annotation=None)], " \
        "vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), " \
        "body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='C', ctx=Load()), " \
        "Name(id='C', ctx=Load())], keywords=[]))], " \
        "decorator_list=[], returns=None)])"

# Generated at 2022-06-14 02:30:47.328904
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..unittest_tools import assert_transform
    from typed_ast import ast3 as ast

    tests = [
        (
            """
            class A:
                def func(self):
                    super()
            """,
            """
            class A:
                def func(self):
                    super(A, self)
            """
        ),
        (
            """
            class A:
                def func(self):
                    super()
                @classmethod
                def func2(cls):
                    super()
            """,
            """
            class A:
                def func(self):
                    super(A, self)
                @classmethod
                def func2(cls):
                    super(A, cls)
            """
        ),
    ]

    for code_in, code_out in tests:
        assert_

# Generated at 2022-06-14 02:30:55.904793
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    root_node = source_to_nodes('''
        class C(object):
            def __init__(self):
                super().__init__()
                super.run()
    ''')

    nodes = SuperWithoutArgumentsTransformer(root_node).visit(root_node)
    for node in nodes:
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            assert len(node.args) == 2
            assert isinstance(node.args[0], ast.Name)
            assert isinstance(node.args[1], ast.Name)

# Generated at 2022-06-14 02:31:06.038087
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # super()
    tree = ast.parse(
        '''
super()
'''
    )

    SuperWithoutArgumentsTransformer(tree).run()
    assert ast.dump(tree) == '''
Module(body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))])
'''

    # super(args)
    tree = ast.parse(
        '''
super(args)
'''
    )

    SuperWithoutArgumentsTransformer(tree).run()

# Generated at 2022-06-14 02:31:12.385646
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor

    tree = astor.parse_file(__file__.replace('.py', '.test_SuperWithoutArgumentsTransformer_visit_Call.py'))

    # init transformer
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)

    # compile the tree to test if visit worked properly
    compiled = compile(tree, '', 'exec')

    # check if compiled code is correct
    test = tree_to_str(tree)

# Generated at 2022-06-14 02:31:20.728830
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    'class A:
        def __init__(self):
            super()
        def b(self):
            super()
    '
    """
    input_code = '\n'.join([
        'class A:',
        '    def __init__(self):',
        '        super()',
        '    def b(self):',
        '        super()'
    ])

    expected_code = '\n'.join([
        'class A:',
        '    def __init__(self):',
        '        super(A, self)',
        '    def b(self):',
        '        super(A, self)'
    ])
    expected_as_tree = ast.parse(expected_code)
    actual_as_tree = ast.parse(input_code)


# Generated at 2022-06-14 02:31:30.478309
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Parent():
      def __init__(self):
        super().__init__()
        super()

      def f(self):
        super()
    """
    expected_output = """
    class Parent():
      def __init__(self):
        super(Parent, self).__init__()
        super(Parent, self)

      def f(self):
        super(Parent, self)
    """
    tree = ast.parse(dedent(code))
    transformed_tree = transform_tree(tree, [SuperWithoutArgumentsTransformer])
    assert(to_source(transformed_tree) == dedent(expected_output))

# Generated at 2022-06-14 02:31:37.264767
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import build_ast
    from ..utils.source import source_to_unicode

    source = source_to_unicode("""
        class C:
            def f(self):
                super()

        class D(C):
            def f(cls):
                super()
    """)
    expected_result = source_to_unicode("""
        class C:
            def f(self):
                super(C, self)

        class D(C):
            def f(cls):
                super(D, cls)
    """)
    tree = build_ast(source)
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)
    assert expected_result == ast.dump(tree)
    assert transformer

# Generated at 2022-06-14 02:31:44.717161
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..utils.tree import parse_tree
    from ..utils.helpers import Expectation

    tree = parse_tree('''
        class A:
            def foo(self):
                super().foo()
            def bar(self):
                super()
            def baz(self, arg):
                super().baz()
    ''')

    trans = SuperWithoutArgumentsTransformer(tree)
    trans.run()

    super_names = [attr.args[1].id for attr in tree.body[0].body[0].body if isinstance(attr, ast.Expr)]
    assert super_names == Expectation(['self', 'self', 'arg'])

# Generated at 2022-06-14 02:32:01.390897
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ast_tools.transformers.transformers.super_without_arguments import SuperWithoutArgumentsTransformer
    from ast_tools.utils.helpers import ast_to_source
    
    class_name = 'SomeClass'
    super_call = ast.Call(func=ast.Name(id='super'), args=[], keywords=[], starargs=None, kwargs=None)
    method_name = 'a_method'
    method_body = [super_call]

# Generated at 2022-06-14 02:32:11.590241
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from copy import deepcopy
    from typed_ast import ast3 as ast

    example = {'Call':
                {'args': [],
                 'func': {'id': 'super'},
                 'keywords': [],
                 'starargs': None,
                 'kwargs': None}}

    expected_output = {'Call':
                        {'args': [{'id': 'cls'}, {'id': 'self'}],
                         'func': {'id': 'super'},
                         'keywords': [],
                         'starargs': None,
                         'kwargs': None}}


# Generated at 2022-06-14 02:32:14.464426
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import run_transformer
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:32:25.271288
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..ast_transformer import AstTransformer
    transformer = AstTransformer(version=2.7)
    transformer.append_transformer(SuperWithoutArgumentsTransformer)

    node = ast.parse('super()', mode='eval')
    node = transformer.visit(ast.Expression(body=node))
    assert isinstance(node.body, ast.Call)
    assert node.body.args[1].id == 'self'
    assert 'super' not in transformer._source

    node = ast.parse('super()', mode='eval')
    node = transformer.visit(node)
    assert isinstance(node, ast.Call)
    assert node.args[1].id == 'self'

    transformer.clear()

    node = ast.parse('super(cls)', mode='eval')
    node = transformer.visit

# Generated at 2022-06-14 02:32:32.026109
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
    class A(object):
        def test(self):
            super()
    """

    expected = """
    class A(object):
        def test(self):
            super(A, self)
    """

    tree = ast.parse(source)  # type: ignore
    node = SuperWithoutArgumentsTransformer()
    new_tree = node.visit(tree)

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))  # type: ignore

# Generated at 2022-06-14 02:32:42.282279
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ..transpile import Transpiler

    t = Transpiler()
    t.add_transformer(SuperWithoutArgumentsTransformer)

    # def f():
    #     super()

    source = ast.Module(
        body=[
            ast.FunctionDef(
                name='f',
                args=ast.arguments(
                    args=[],
                    vararg=None,
                    kwonlyargs=[],
                    kwarg=None,
                    defaults=[],
                    kw_defaults=[],
                ),
                body=[
                    ast.Expr(value=ast.Call(
                        func=ast.Name(id='super'),
                        args=[],
                        keywords=[],
                    )),
                ],
                decorator_list=[],
            ),
        ],
    )

# Generated at 2022-06-14 02:32:44.267850
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.helpers import run_python_source


# Generated at 2022-06-14 02:32:45.215433
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:54.434063
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # assert isinstance(SuperWithoutArgumentsTransformer, object)
    assert issubclass(SuperWithoutArgumentsTransformer, BaseNodeTransformer)
    assert issubclass(SuperWithoutArgumentsTransformer, ast.NodeTransformer)
    assert SuperWithoutArgumentsTransformer.__name__ == "SuperWithoutArgumentsTransformer"
    assert SuperWithoutArgumentsTransformer.__module__ == __name__

    # assert isinstance(SuperWithoutArgumentsTransformer().visit, collections.abc.Callable)
    # assert isinstance(SuperWithoutArgumentsTransformer().visit_Call, collections.abc.Callable)
    # assert isinstance(SuperWithoutArgumentsTransformer().generic_visit, collections.abc.Callable)

# Generated at 2022-06-14 02:32:59.931416
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from . import apply_ast

    source = """
    class A(object):
        def m(self):
            super()
    """

    result = """
    class A(object):
        def m(self):
            super(A, self)
    """

    tree = apply_ast(SuperWithoutArgumentsTransformer(), source)
    assert result == tree_to_str(tree)

# Generated at 2022-06-14 02:33:21.085327
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    super_node = ast.Call(func=ast.Name(id='super'), args=[], keywords=[])

    func_def_node = ast.FunctionDef(name='m', args=ast.arguments(args=[ast.arg(arg='self', annotation=None)]), body=[super_node], decorator_list=[], returns=None)
    cls_def_node = ast.ClassDef(name='C', bases=[], keywords=[], body=[func_def_node], decorator_list=[])

    node = ast.Module(body=[cls_def_node])

    transformer = SuperWithoutArgumentsTransformer(node)

    transformer.visit(node)

    # super(Cls, self)
    assert super_node.args == node.body[0].body[0].body[0].args
    assert super_node.args

# Generated at 2022-06-14 02:33:27.008521
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Foo:
            def __init__(self):
                super()
    """
    expected = """
        class Foo:
            def __init__(self):
                super(Foo, self)
    """
    tree = ast.parse(code)
    result = SuperWithoutArgumentsTransformer().visit(tree)
    result_code = parseast(result)
    assert expected == result_code

# Generated at 2022-06-14 02:33:28.095496
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:36.487848
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    node = ast3.parse("super()")
    tree = SuperWithoutArgumentsTransformer().visit(node)
    assert isinstance(tree.body[0].value.args[0], ast3.Name)
    assert tree.body[0].value.args[0].id == 'Cls'
    assert isinstance(tree.body[0].value.args[1], ast3.Name)
    assert tree.body[0].value.args[1].id == 'self'

# Generated at 2022-06-14 02:33:43.808585
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    import inspect
    import sys

    tree = ast.parse(
        inspect.cleandoc('''
        class Cls:
            def __init__(self):
                super()
        '''))
    node_transformer = SuperWithoutArgumentsTransformer()
    node_transformer.visit(tree)
    assert node_transformer._tree_changed
    compile(tree, 'test', 'exec')
    exec(compile(tree, 'test', 'exec'), sys._getframe(1).f_globals)

# Generated at 2022-06-14 02:33:45.254503
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
 

# Generated at 2022-06-14 02:33:54.048564
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from . import compile_function
    source = source_to_unicode(
        # fmt: off
        """
        class A:
            def b(self):
                super()
        """)
        # fmt: on
    transformers = [SuperWithoutArgumentsTransformer]
    _, tree = compile_function(source, transformers)
    assert "super(A, self)" == ast.dump(tree.body[0].body[0].value)



# Generated at 2022-06-14 02:34:00.566196
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse('super()').body[0]
    transformer = SuperWithoutArgumentsTransformer(None)
    transformer.visit_Call(node)
    assert ast.dump(node) == "Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[])"


# Unit test to check class SuperWithoutArgumentsTransformer is in the right module

# Generated at 2022-06-14 02:34:08.986767
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'class A: \n' \
           '    def f(self):\n' \
           '        super()\n'
    expected = 'class A: \n' \
               '    def f(self):\n' \
               '        super(A, self)\n'

    tree = ast.parse(code)
    transformed_tree = SuperWithoutArgumentsTransformer().visit(tree)

    assert ast.dump(transformed_tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:34:17.833592
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest

    class SuperWithoutArgumentsTransformerTest(unittest.TestCase):
        def test_super(self):
            tx = SuperWithoutArgumentsTransformer()
            node = ast.parse('''
                                class A:
                                    def b(self): 
                                        super()
                                ''')
            tx.visit(node)
            self.assertIsInstance(node.body[0].body[0].body[0].value.args[0], ast.Name)
            self.assertEqual(node.body[0].body[0].body[0].value.args[0].id, 'A')
            self.assertIsInstance(node.body[0].body[0].body[0].value.args[1], ast.Name)

# Generated at 2022-06-14 02:34:41.195688
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import format_code
    from astunparse import unparse


# Generated at 2022-06-14 02:34:45.963755
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        super()
        """
    expected_code = """
        super(Cls, self)
        """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    transformed_code = compile(tree, '<test>', 'exec')

    globals_ = {'super': super}
    locals_ = {}
    exec(transformed_code, globals_, locals_)
    assert transformed_code.co_code == expected_code

# Generated at 2022-06-14 02:34:51.583731
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Tests SuperWithoutArgumentsTransformer."""
    from ..utils.test_utils import generate_wrapping_code, generate_source_code_tree, assertSourceEqualsTarget
    source = generate_wrapping_code(
        """
        class MyClass:
            def my_method(self):
                super()
                
        def other_method(self):
            super()
        """,
        version=3
    )
    target = generate_wrapping_code(
        """
        class MyClass:
            def my_method(self):
                super(MyClass, self)

        def other_method(self):
            super()
        """,
        version=3
    )
    tree = generate_source_code_tree(source, version=3)

    SuperWithoutArgumentsTransformer().visit(tree)

   

# Generated at 2022-06-14 02:34:52.722925
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    _ = SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:53.962135
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:08.212092
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def check(before: ast.AST, after: ast.AST, python_version: Tuple[int, int]):
        tree = ast.parse(dedent(before))
        SuperWithoutArgumentsTransformer(tree, python_version).run()

        result = dump(tree)
        expected_result = dump(ast.parse(dedent(after)))
        assert result == expected_result

    before = """
    class Cls:
        def method(self):
            super()
    """

    after = """
    class Cls:
        def method(self):
            super(Cls, self)
    """

    check(before, after, (2, 7))
    check(before, after, (3, 0))
    check(before, after, (3, 7))
    check(before, after, (3, 8))

# Generated at 2022-06-14 02:35:10.705532
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils import compile_source_code

# Generated at 2022-06-14 02:35:11.361803
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:12.980005
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    fname = 'example.py'

# Generated at 2022-06-14 02:35:16.884494
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    assert str(SuperWithoutArgumentsTransformer({'2.7': 2.7}).visit(ast.parse("""
super()
        """))) == '\nsuper(Cls, self)'


# Generated at 2022-06-14 02:35:59.089434
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from testing.compile import assert_in_output
    assert_in_output(
        """
        class A:
            def __init__(self):
                super()
                super().test
        """,
        [
            "super(A, self).__init__()",
            "super(A, self).test"
        ],
        SuperWithoutArgumentsTransformer
    )


# Generated at 2022-06-14 02:36:02.072020
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    code = 'super()'
    tree = compile(code)

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert str(transformer._tree) == "super(<unknown>, <unknown>)"

# Generated at 2022-06-14 02:36:08.584167
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def test_super(self):
        super()

    tree = ast.parse(inspect.getsource(test_super))
    SuperWithoutArgumentsTransformer(tree).run()

    code_out = compile(tree, '', 'exec')
    exec(code_out)
    cls = locals()['TestSuperWithoutArgumentsTransformer']
    cls_instance = cls()
    cls_instance.test_super()

# Generated at 2022-06-14 02:36:09.490150
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:36:17.923757
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer"""
    # pylint: disable=protected-access
    current_node = ast.parse("""super()""").body[0]
    assert isinstance(current_node, ast.Expr)
    node = current_node.value
    assert isinstance(node, ast.Call)
    assert isinstance(node.func, ast.Name)
    assert not node.args
    assert SuperWithoutArgumentsTransformer._replace_super_args.__code__.co_argcount == 2

# Generated at 2022-06-14 02:36:19.668833
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..context import Context
    import sys

# Generated at 2022-06-14 02:36:29.016878
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .. import dump, compile_string

    def test_basic(case, template, ast3_dump=dump):
        src = template.format(case)
        expected_src = template.format(ast3_dump(ast.parse(src)))

        # Test transformer on code
        module = compile_string(src, '<test>', 'exec')
        tree = ast.parse(src)
        transformer = SuperWithoutArgumentsTransformer(tree)
        transformer.visit(tree)
        assert tree is not None
        assert dump(tree) == ast3_dump(ast.parse(expected_src))

        # Test compile of transformed code
        module = compile_string(dump(tree), '<test>', 'exec')

        # Test eval of transformed code
        ns = {}

# Generated at 2022-06-14 02:36:32.472496
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.tree_builder import build_ast_tree


# Generated at 2022-06-14 02:36:40.625156
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("""
    class Cls:
        def __init__(self):
            super().__init__()
    """)

    tr = SuperWithoutArgumentsTransformer(tree)
    tr.run()

    assert astunparse(tree).replace(" ", "").replace("\n", "") == \
        "classCls:def__init__(self):super(Cls,self).__init__()"

# Generated at 2022-06-14 02:36:51.021136
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = 'class A: def f(self): super()'
    
    new_code = 'class A: def f(self): super(A, self)'
    tree = ast.parse(code)
    node = tree.body[0].body[0].body[0]
    assert str(node) == 'super()'
    
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    node = tree.body[0].body[0].body[0]
    assert str(node) == 'super(A, self)'
    assert str(tree) == astor.to_source(ast.parse(new_code))