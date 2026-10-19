

# Generated at 2022-06-14 02:27:57.500875
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:08.373827
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Test(object):
            def test(self):
                super()
    """
    tree = ast.parse(code)
    tree = SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:28:09.320858
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:18.875220
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A:
            def __init__(self):
                super()
    """
    root = ast.parse(code)
    SuperWithoutArgumentsTransformer(root).run()
    assert isinstance(root.body[0].body[0].value, ast.Call)
    assert root.body[0].body[0].value.func.id == 'super'

    code = """
        class A:
            def __init__(self):
                super(A, self)
    """
    root = ast.parse(code)
    SuperWithoutArgumentsTransformer(root).run()
    assert isinstance(root.body[0].body[0].value, ast.Call)
    assert root.body[0].body[0].value.func.id == 'super'


# Generated at 2022-06-14 02:28:27.759977
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3
    tree = ast3.parse("""a = super()""")
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert ast3.dump(tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='cls', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:28:36.704472
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    sys.modules['ast'] = ast
    s = 'super()'
    t = ast.parse(s)
    t = SuperWithoutArgumentsTransformer().visit(t)
    assert ast.dump(t) == "Module(body=[FunctionDef(name='test', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]))], decorator_list=[], returns=None)])"

# Generated at 2022-06-14 02:28:39.203075
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..helpers import Compiler
    from ..utils.testing import get_code
    from ..utils.parsing.parser import PythonParser

# Generated at 2022-06-14 02:28:43.012896
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..bundled.six import print_
    from .. import compile_source
    module_name = 'test_super_transformer'

# Generated at 2022-06-14 02:28:47.276974
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.helpers import get_ast_from_source
    from ..utils.asserts import assert_code_equal

# Generated at 2022-06-14 02:28:54.319763
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..builder import build_ast
    from ..utils.helpers import clone

    tree = build_ast("super();")
    trans = SuperWithoutArgumentsTransformer()
    new_tree = trans.visit(clone(tree))

    assert str(new_tree) == "super(Cls, self);"

    tree = build_ast("super();")
    trans = SuperWithoutArgumentsTransformer()
    new_tree = trans.visit(clone(tree))

    assert str(new_tree) == "super(Cls, self);"

# Generated at 2022-06-14 02:29:08.286229
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer(): # noqa: WPS433
    """Test for constructor of class SuperWithoutArgumentsTransformer."""
    from .. import transformations  # noqa: WPS433
    from .. import ast_parser  # noqa: WPS433

    tree = ast_parser.parse('a = super().__str__()')
    transformations.transform(tree, SuperWithoutArgumentsTransformer)
    assert str(tree) == 'a = super(Cls, self).__str__()'

    tree = ast_parser.parse('a = super()')
    transformations.transform(tree, SuperWithoutArgumentsTransformer)
    assert str(tree) == 'a = super(Cls, self)'

# Generated at 2022-06-14 02:29:16.204784
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..typed_python_transforms import _CLASS_BINDING_NAME
    
    class Cls(object):
        def __init__(self) -> None:
            super().__init__()
    src = Source(Cls)
    
    class Cls2(object):
        @classmethod
        def f(cls) -> None:
            super().f()
    src2 = Source(Cls2)
    SuperWithoutArgumentsTransformer(src2).transform()
    assert "super({}, self)".format(_CLASS_BINDING_NAME) in str(src2)
    assert "super({}, cls)".format(_CLASS_BINDING_NAME) in str(src2)
    
    SuperWithoutArgumentsTransformer(src).transform()

# Generated at 2022-06-14 02:29:30.928999
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Foo(ast.NodeTransformer):
        """blah"""
        def _replace_super_args(self, node):
            node.args = [ast.arguments(args=[ast.arg(arg='Cls', annotation=None)], vararg=None, kwonlyargs=[],
                                       kw_defaults=[], kwarg=None, defaults=None)]

    class Bar(Foo, SuperWithoutArgumentsTransformer):
        """blah"""

    foo = Foo()
    bar = Bar()

    inp = 'def foo(): super()'
    expected = 'def foo(): super(Cls)'
    out = astunparse.unparse(bar.visit(ast.parse(inp)))
    assert out == expected

    # Test SuperWithoutArgumentsTransformer not hijacking Foo's visit_Call()
    inp

# Generated at 2022-06-14 02:29:41.602752
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class C(object):
        def __init__(self):
            super()
            """

    from typed_ast import ast3 as ast

    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    module = compile(tree, '<string>', 'exec')
    ns = {}
    exec(module, ns)
    assert ns['C'].__init__.__code__.co_argcount == 2

    code2 = """
    class C(object):
        def __init__(self):
            super()

        def f(self):
            super()
            """
    tree2 = ast.parse(code2)
    SuperWithoutArgumentsTransformer().visit(tree2)
    module2 = compile(tree2, '<string>', 'exec')


# Generated at 2022-06-14 02:29:42.398937
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:29:49.188507
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    tree = astor.parse_file('tests/fixtures/super_without_arguments.py')
    super_without_arguments_transformer = SuperWithoutArgumentsTransformer()
    super_without_arguments_transformer.visit(tree)
    assert len(super_without_arguments_transformer.warnings)==1
    assert astor.to_source(tree)=="""\
"""

# Generated at 2022-06-14 02:29:49.898045
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:52.599551
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_tree
    from ..utils.compare import compare_ast


# Generated at 2022-06-14 02:30:00.715985
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    class DummyNode(ast.AST):
        _fields = ('arg')

    tree = ast.Module(
        body=[
            ast.ClassDef(
                name='Cls',
                body=[
                    ast.FunctionDef(
                        name='func',
                        args=ast.arguments(args=[ast.arg(arg='self')]),
                        body=[
                            ast.Expr(value=ast.Call(func=ast.Name(id='super'), args=[], keywords=[])),
                            ast.Return(value=ast.Name(id='self'))
                        ]
                    )
                ]
            )
        ]
    )

    DummyNode(arg=ast.Call(func=ast.Name(id='super'), args=[], keywords=[]))

    extracted = tree.body

# Generated at 2022-06-14 02:30:02.481642
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer(): 
    import astor

# Generated at 2022-06-14 02:30:07.079940
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:16.696416
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    def f(self):
        super()
    """

    tree = ast.parse(code)
    node = tree.body[0].body[0]
    tree = SuperWithoutArgumentsTransformer().visit(tree)

    assert isinstance(tree.body[0].body[0], ast.Expr)
    assert isinstance(tree.body[0].body[0].value, ast.Call)

    args = tree.body[0].body[0].value.args

    assert isinstance(args[0], ast.Name)
    assert args[0].id == 'Cls'
    assert astor.to_source(args[0]) == 'Cls'

    assert isinstance(args[1], ast.Name)
    assert args[1].id == 'self'
    assert astor.to_source

# Generated at 2022-06-14 02:30:18.054819
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_restricted

# Generated at 2022-06-14 02:30:19.687436
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:30:21.250215
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Test cases
    assert SuperWithoutArgumentsTransformer()


# Generated at 2022-06-14 02:30:23.458267
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. ... import ast
    # testing for replacement of super() with super(Cls, self)


# Generated at 2022-06-14 02:30:31.342767
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import typed_ast.ast3 as ast
    from ..utils.testing import assert_equal_source
    transformer = SuperWithoutArgumentsTransformer(None)
    assert_equal_source(transformer.visit(ast.parse('class C:\n    def m(self):\n        super()')),
                        'class C:\n    def m(self):\n        super(C, self)')
    assert_equal_source(transformer.visit(ast.parse('class C:\n    def m(cls):\n        super()')),
                        'class C:\n    def m(cls):\n        super(C, cls)')

# Generated at 2022-06-14 02:30:34.142292
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast import parse
    from typed_ast import ast3
    from ..utils.tree_compare import assert_tree_equal
    from ..utils.helpers import string_to_ast


# Generated at 2022-06-14 02:30:40.677350
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .. import register_transformers, transform_file
    from ..transformers.super_without_arguments import SuperWithoutArgumentsTransformer
    from .test_utils import assert_equal_source

    register_transformers({
        'super_without_arguments': SuperWithoutArgumentsTransformer,
    })

    assert_equal_source(
        transform_file(
            'tests/fixtures/super_without_arguments.py',
            apply_transforms=['super_without_arguments']),
        source_to_unicode(
            'tests/fixtures/super_without_arguments.py.expected'))

# Generated at 2022-06-14 02:30:43.649209
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes
    from ..utils.helpers import get_ast_of_node_type


# Generated at 2022-06-14 02:30:52.639390
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:00.512799
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .. import compile_isolated
    from typed_ast import ast3 as ast

    source_1 = source_to_unicode('''
    class A(object):
        def __init__(self):
            super()
    ''')
    expected_1 = source_to_unicode('''
    class A(object):
        def __init__(self):
            super(A, self)
    ''')
    module_1 = compile_isolated(source_1, "test_data_1", 'exec')
    assert isinstance(module_1, ast.Module)

    source_2 = source_to_unicode('''
    class A(object):
        def __init__(cls):
            super()
    ''')
   

# Generated at 2022-06-14 02:31:01.426756
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:03.528179
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    transform = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:31:04.831189
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_isolated

# Generated at 2022-06-14 02:31:10.204174
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    code = """
    class Class():
        def method(self):
            super()
    """
    expected = """
    class Class():
        def method(self):
            super(Class, self)
    """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert expected == astor.to_source(tree)

# Generated at 2022-06-14 02:31:15.729997
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = """class A():
    def __init__(self):
        super()"""
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()

    assert transformer.was_changed
    assert 'super(A, self)' in pretty_code(tree)


# Generated at 2022-06-14 02:31:26.471985
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    cls = ast.ClassDef(
        name='Cls',
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[])

    func = ast.FunctionDef(
        name='func',
        args=ast.arguments(args=[ast.arg(arg='self', annotation=None)],
                           vararg=None,
                           kwonlyargs=[],
                           kw_defaults=[],
                           kwarg=None,
                           defaults=[]),
        body=[ast.Expr(value=ast.Call(func=ast.Name(id='super'), args=[], keywords=[]))],
        decorator_list=[])

    cls.body.append(func)

    tree = ast.Module(body=[cls])

# Generated at 2022-06-14 02:31:27.490114
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:31:39.624724
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode as u
    from .base import BaseNodeTransformerTest
    from .. import register_transformer

    register_transformer(SuperWithoutArgumentsTransformer)

    class Test(BaseNodeTransformerTest):
        target_version = (2, 7)
        transformers = (SuperWithoutArgumentsTransformer,)
        tree = ast.parse(u('''
        class Cls:
            def method():
                super()
            """
        '''))

        expectations = {
            # no expectations
        }

    test = Test()
    result = test.results[0]

    assert len(result) == 1
    # noinspection PyUnresolvedReferences
    assert isinstance(result[0], ast.Call)
    # noinspection PyUnresolvedReferences

# Generated at 2022-06-14 02:32:00.817662
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:10.495690
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class C(B):
        def __init__(self):
            super()
    """

    tr = SuperWithoutArgumentsTransformer()
    tr.visit(ast.parse(code))

    code_expected = """
    class C(B):
        def __init__(self):
            super(C, self)
    """

    assert ast.dump(ast.parse(code_expected), annotate_fields=False) == ast.dump(tr.tree, annotate_fields=False)


# Generated at 2022-06-14 02:32:20.292268
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import Compiler
    code = '''
        class Cls(object):
            def method(self):
                super()
    '''
    tree = ast.parse(code)
    module = ast.Module(body=[])
    module.body.append(tree)
    Compiler(SuperWithoutArgumentsTransformer).visit(module)
    comp_code = compile(module, '<string>', 'exec')
    res = {}
    exec(comp_code, res)
    assert res['Cls'].__dict__['method'].__code__.co_argcount == 2

# Generated at 2022-06-14 02:32:27.043300
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    test = '''
    class A:
        super()
    '''
    tree = ast.parse(test)
    node = tree.body[0].body[0].value
    assert node.args == []
    SuperWithoutArgumentsTransformer().visit(node)
    assert node.args[0].id == 'A'
    assert node.args[1].id == 'self'

# Generated at 2022-06-14 02:32:28.970265
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:36.770017
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    module = ast.parse('super()')
    
    # Check if module is valid
    assert(isinstance(module, ast.Module))

    # Check if the module have a body
    assert(isinstance(module.body, list))

    # Check if the module body have an elements
    assert(isinstance(module.body[0], ast.Expr))

    # Check if the module body is an expression
    assert(isinstance(module.body[0].value, ast.Call))

    # Check if the module contain super()
    assert(isinstance(module.body[0].value.func, ast.Name))
    assert(module.body[0].value.func.id == 'super')

    # Check if the module body is an expression
    assert(isinstance(module.body[0].value.args, list))

    # Check

# Generated at 2022-06-14 02:32:37.807284
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:43.745464
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    def my_function():
        super()
        
    class A:
        def __init__(self):
            super()
    '''
    expected_code = '''
    def my_function():
        super(A, self)
        
    class A:
        def __init__(self):
            super(A, self)
    '''
    module = ast.parse(code)  # type: ignore
    SuperWithoutArgumentsTransformer(module).visit(module)
    assert (ast.dump(module, annotate_fields=False) == expected_code)

# Generated at 2022-06-14 02:32:50.179142
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code = 'class Cls(object):\n    def func(self):\n        super().func()'
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)

    assert str(tree) == '\n'.join([
        'class Cls(object):',
        '    def func(self):',
        '        super(Cls, self).func()',
    ])

# Generated at 2022-06-14 02:32:51.106518
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:33:30.701848
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    # Assert that the code is changed
    assert ast.dump(tree) != ast.dump(ast.parse(code))

# Generated at 2022-06-14 02:33:42.024905
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def test():
        class A:
            def __init__(self):
                super().__init__()
    expected = """
    class A:
        def __init__(self):
            super(A, self).__init__()
    """
    test = ast.parse(textwrap.dedent(test.__doc__))
    transformer = SuperWithoutArgumentsTransformer(test)
    transformer.visit(test)
    actual = ast.fix_missing_locations(test).body[0]
    diff = list(difflib.ndiff(expected.splitlines(), ast.dump(actual).splitlines()))
    assert not diff, "ast is different from expected:\n{}".format("\n".join(diff))


# Generated at 2022-06-14 02:33:49.423921
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typing import List

    cls = ast.ClassDef(name='Foo', bases=[], keywords=[], body=[
        ast.FunctionDef(name='bar', args=ast.arguments(args=[ast.arg(arg='self',annotation=None)], defaults=[], vararg=None,kwonlyargs=[],kw_defaults=[], kwarg=None), decorator_list=[], returns=None, body=[
            ast.Expr(value=ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[]))
        ])
    ], decorator_list=[])

    tree = ast.Module(body=[cls])

# Generated at 2022-06-14 02:33:58.140747
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from ..utils.ast_helpers import parse_ast

    source = """
        class A:
            def foo(self):
                super()
    """

    tree = parse_ast(source)

    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)

    expected = ast3.parse("""
        class A:
            def foo(self):
                super(A, self)
    """)

    assert ast3.dump(tree) == ast3.dump(expected)

# Generated at 2022-06-14 02:34:03.386513
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .. import _compat

    source = source_to_unicode(
        """
        class Test:

            def method(self):
                super()
            """
    )
    tree = ast.parse(source)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    expected_source = source_to_unicode(
        """
        class Test:

            def method(self):
                super(Test, self)
            """
    )
    expected_tree = ast.parse(expected_source)
    _compat.assertEqual(ast.dump(tree, annotate_fields=False, include_attributes=False),
                        ast.dump(expected_tree, annotate_fields=False, include_attributes=False))

# Generated at 2022-06-14 02:34:11.021262
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('''
    class Foo:
        def bar(self):
            super()
    ''')
    ast.fix_missing_locations(tree)
    transformer = SuperWithoutArgumentsTransformer()
    tree = transformer.visit(tree)
    expected = '''
    class Foo:
        def bar(self):
            super(Foo, self)
    '''
    transformer.generic_visit(tree)
    assert astunparse.unparse(tree).strip() == expected.strip()

# Generated at 2022-06-14 02:34:17.637474
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ..transformers.base import Transformer
    from ..utils.helpers import transform

    class TestTransformer(Transformer):
        def _setup(self):
            self._tree_changed = False
            self._tree = ast.parse(self.code)
            self._transformed_tree = ast.parse(self.code)
            self._transformer = SuperWithoutArgumentsTransformer(self._tree, self._transformed_tree, self._tree_changed)


# Generated at 2022-06-14 02:34:24.668050
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.helpers import assert_conversion

    code = '''class X:\n    @staticmethod\n    def m():\n        super()'''
    assert_conversion(SuperWithoutArgumentsTransformer, code, code.replace('super()', 'super(X, self)'))

# Generated at 2022-06-14 02:34:28.061587
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(ast.parse("super()", mode='exec'))
    assert str(transformer.tree) == "super(__module__, self)"


# Generated at 2022-06-14 02:34:35.839795
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    from ..utils import dump_ast

    module = ast.parse('super()')
    node = module.body[0]

    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'super'
    assert not node.value.args

    class Cls(SuperWithoutArgumentsTransformer):
        pass

    Cls().visit(module)
    assert dump_ast(module) == '[Expr(value=Call(func=Name(id=str, ctx=Load()), args=[Str(s=\'Test\')], keywords=[], starargs=None, kwargs=None))]'

# Generated at 2022-06-14 02:36:10.020764
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    
    transformer = SuperWithoutArgumentsTransformer(ast.parse('super()'))
    transformer.visit(transformer._tree)
    expected = 'super(Cls, self)'
    tree = ast.dump(transformer._tree)
    assert tree == expected

# Generated at 2022-06-14 02:36:19.196721
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # type: () -> None
    from .. import compile_ast
    import ast

    code = '''
    class Foo:
        def __init__(self):
            super()

        @staticmethod
        def static():
            super()

        @classmethod
        def classm(cls):
            super()
    '''
    tree = compile_ast(code, __name__)
    func_names = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
    assert func_names == ['__init__', 'static', 'classm', '<lambda>']

# Generated at 2022-06-14 02:36:20.356266
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast import parse

# Generated at 2022-06-14 02:36:21.329453
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:28.096216
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from util import to_source

    code = to_source(
        ast.parse('''
        class A:
            def __init__(self):
                super()
        ''')
    )

    tree = ast.parse(code)
    node = tree.body[0]
    SuperWithoutArgumentsTransformer(tree, code).visit(node)
    assert to_source(tree) == to_source(
        ast.parse('''
        class A:
            def __init__(self):
                super(A, self)
        ''')
    )

# Generated at 2022-06-14 02:36:29.859340
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import ast, typing
    from ..utils.build_tree import build_ast_tree


# Generated at 2022-06-14 02:36:30.394369
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:37.003148
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import Source
    from ..visitors import SkipNode
    tree = ast.parse('def foo(arg): super()')
    transformer = SuperWithoutArgumentsTransformer(tree, Source('<test>', 'class Cls: def foo(arg): super()'))
    visitor = transformer.visitor()
    node = tree.body[0].body[0]
    assert isinstance(visitor.visit(node), SkipNode)

    tree = ast.parse('class Cls: def foo(arg): super()')
    transformer = SuperWithoutArgumentsTransformer(tree, Source('<test>', 'class Cls: def foo(arg): super()'))
    visitor = transformer.visitor()
    node = tree.body[0].body[0]
    assert isinstance(visitor.visit(node), SkipNode)

# Generated at 2022-06-14 02:36:38.264785
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:51.021092
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from copy import deepcopy
    from .utils import TransformTestCase
    
    class Test(TransformTestCase):
        target_version = (2, 7)  # for assertWarns
        transformer = SuperWithoutArgumentsTransformer
        
        def test_super_in_function(self):
            # super() outside of class
            tree = ast.parse("""
            def foo(self):
                super()
            """)

            self.check(tree, tree)

        def test_super_outside_function(self):
            # super() outside of function
            tree = ast.parse("""
            class Foo(object):
                super()
            """)

            self.check(tree, tree)
