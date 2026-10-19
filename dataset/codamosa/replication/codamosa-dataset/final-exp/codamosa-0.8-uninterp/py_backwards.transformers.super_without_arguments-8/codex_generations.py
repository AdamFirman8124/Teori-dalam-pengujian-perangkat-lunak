

# Generated at 2022-06-14 02:27:55.230977
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:27:56.888615
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:27:59.581430
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:04.445211
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # type: () -> None
    from typed_ast import ast3 as ast

    class Cls(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call) -> None:
            ...

    node = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(node)

    Cls().visit(node)

# Generated at 2022-06-14 02:28:06.617477
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import get_ast
    import astunparse

# Generated at 2022-06-14 02:28:09.181066
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    from . import ClassAndFunctionVisitor

    class In:
        pass


# Generated at 2022-06-14 02:28:18.572408
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import assert_equal_source


# Generated at 2022-06-14 02:28:23.719802
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    transformer = SuperWithoutArgumentsTransformer()
    source = '''\
super()'''

    tree = transformer.visit(ast.parse(source))
    assert source == '\n'.join([node.raw for node in ast.iter_fields(tree)])



# Generated at 2022-06-14 02:28:26.141817
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code_1 = """
super()
    """.strip()
    expected_code_1 = """
super(Cls, self)
    """.strip()

# Generated at 2022-06-14 02:28:27.176304
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:33.579428
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("super()")
    super_wo_args_transformer = SuperWithoutArgumentsTransformer(tree)
    super_wo_args_transformer.visit(tree)
    assert len(tree.body[0].body[0].body[0].args.args) == 2

# Generated at 2022-06-14 02:28:44.739210
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .base import BaseNodeTransformer

    class TestTransformer(BaseNodeTransformer):
        target = (2, 7)

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and not len(node.args):
                try:
                    func = get_closest_parent_of(self._tree, node, ast.FunctionDef)
                except NodeNotFound:
                    warn('super() outside of function')
                    return
                try:
                    cls = get_closest_parent_of(self._tree, node, ast.ClassDef)
                except NodeNotFound:
                    warn('super() outside of class')
                    return

# Generated at 2022-06-14 02:28:45.856321
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:49.051464
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse('super()')
    SuperWithoutArgumentsTransformer().visit(node)
    assert 'super(Cls, self)' in ast.dump(node)

# Generated at 2022-06-14 02:28:56.680284
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_code_object, source_to_ast
    from ..utils.helpers import assert_code_eq

    s = """
        class Cls:
            def method(self):
                super()
            @classmethod
            def class_method(cls):
                super()
        """

    ast_tree = source_to_ast(s)
    c = source_to_code_object(s)
    result = ast.dump(SuperWithoutArgumentsTransformer(ast_tree).visit(ast_tree))

# Generated at 2022-06-14 02:29:06.217038
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse(
        '''
    class C(super):
        def __init__(self):
            super()
    '''
    )
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(node)

    assert transformer._tree_changed,\
        'Tree should be changed'

    assert isinstance(node.body[0].bases[0], ast.Call),\
        'super() should be replaced with super(cls, self)'

    assert isinstance(node.body[0].body[0].value.args[0], ast.Name) and\
           isinstance(node.body[0].body[0].value.args[1], ast.Name),\
        'super() should be replaced with super(cls, self)'


# Generated at 2022-06-14 02:29:10.996278
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    source = """
        class Cls:
            def __init__(self):
                super()
    """
    expected = """
        class Cls:
            def __init__(self):
                super(Cls, self)
    """
    SuperWithoutArgumentsTransformer.verify(source, expected)

# Generated at 2022-06-14 02:29:15.168151
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    :Example:
        class Foo:
            def __init__(self):
                super().__init__()
    :Result:
        class Foo:
            def __init__(self):
                super(Foo, self).__init__()
    """

# Generated at 2022-06-14 02:29:25.661213
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import ast as python_ast
    from typed_ast import ast3 as typed_ast
    from typed_ast import convert

    class Visitor(object):
        def __init__(self):
            self.output = None

        def visit_Call(self, node):
            if isinstance(node.func, typed_ast.Name) and node.func.id == 'super' and not len(node.args):
                node.args = [typed_ast.Name(id='Cls'), typed_ast.Name(id="self")]
                self.output = convert(node)
                return self.output

            return self.generic_visit(node) # type: ignore


# Generated at 2022-06-14 02:29:36.965047
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .context import Context
    source = 'super()'
    root_node = ast.parse(source)
    root_node = SuperWithoutArgumentsTransformer(Context()).visit(root_node)

# Generated at 2022-06-14 02:29:43.262875
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast

    class DummyTransformer(BaseNodeTransformer):
        def generic_visit(self, node: ast.AST) -> ast.AST:
            return node


# Generated at 2022-06-14 02:29:51.040775
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    input_code = '''
    class Test():
        def __init__(self):
            super()
    '''
    expected_output = '''
    class Test():
        def __init__(self):
            super(Test, self)
    '''
    tree = ast.parse(input_code)
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(tree)
    assert expected_output == astunparse.unparse(tree).strip()

# Generated at 2022-06-14 02:29:53.487420
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class A(object):
            def __init__(self):
                super()
    """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

    assert code != astor.to_source(tree)


# Generated at 2022-06-14 02:29:57.759904
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..unit_test import assert_transform
    
    assert_transform(
        SuperWithoutArgumentsTransformer,
        'super()',
        'super(Foo, foo)'
    )

    assert_transform(
        SuperWithoutArgumentsTransformer,
        'super().bar()',
        'super(Foo, foo).bar()'
    )



# Generated at 2022-06-14 02:29:58.851159
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:03.458650
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Foo(object):
        def __init__(self):
            self.a = super()
            
        def foo(self):
            self.b = super()
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    exec(compile(tree, '', 'exec'))

# Generated at 2022-06-14 02:30:06.705605
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.helpers import tree_from_src
    from ..utils.ast import dump_tree


# Generated at 2022-06-14 02:30:16.343392
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = 'class A:\n    def __init__(self):\n        super()'

# Generated at 2022-06-14 02:30:25.507452
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import setup_fixtures

    source = """
        class Foo(Bar):
            def __init__(self):
                super()

            def test(self, baz):
                super()
    """
    expected_source = """
        class Foo(Bar):
            def __init__(self):
                super(Foo, self)

            def test(self, baz):
                super(Foo, self)
    """
    tree = setup_fixtures(source, expected_source)
    transformer = SuperWithoutArgumentsTransformer()

    tree = transformer.visit(tree)

    assert transformer.tree_changed is True
    assert source != expected_source
    assert ast.dump(tree) == ast.dump(expected_source)

# Generated at 2022-06-14 02:30:35.241315
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    """unit test for visit_Call method of class SuperWithoutArgumentsTransformer"""
    from ..utils.test_utils import is_equal_trees
    from ..utils.test_utils import get_test_cases_for_function
    from ..utils.test_utils import get_code_for_node
    from ast import parse

    test_cases = get_test_cases_for_function(__file__, "SuperWithoutArgumentsTransformer_visit_Call")

    for test_case in test_cases:
        src1, src2 = test_case["in"]

        tree1 = parse(src1)
        tree2 = parse(src2)

        transformer = SuperWithoutArgumentsTransformer()
        transformer.visit(tree1)


# Generated at 2022-06-14 02:30:44.375541
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse("super()")
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == "Expr(value=Call(func=Attribute(value=Name(id='super', ctx=Load()), attr='__new__', ctx=Load()), args=[Name(id='int', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]))"

# Generated at 2022-06-14 02:30:55.870957
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        class Foo(object):
            def __init__(self):
                super()


        class Bar(object):
            def __init__(self):
                pass
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

# Generated at 2022-06-14 02:31:02.095626
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Test
    s = 'class A(B):\n    def __init__(self):\n        super()\n'

    # Run
    tree = ast.parse(s)
    tree = SuperWithoutArgumentsTransformer().visit(tree)
    compiled = compile(tree, '', 'exec')

    # Assert
    assert 'super(A, self)' in str(compiled)



# Generated at 2022-06-14 02:31:11.642410
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    code = '''
    class Parent(object):
        def __init__(self):
            super()
        
        def some(self):
            def inner():
                super()
    '''

    expected_res = '''
    class Parent(object):
        def __init__(self):
            super(Parent, self)
        
        def some(self):
            def inner():
                super(Parent, self)
    '''

    tree = ast.parse(code)
    t = SuperWithoutArgumentsTransformer(tree)
    t.visit(tree)
    result = compile(tree, filename='<ast>', mode='exec')
    
    result_code = str(result.co_consts[0])
    assert result_code == expected_res

# Generated at 2022-06-14 02:31:16.567136
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    my_code = '''class MyClass:
    def my_method(self):
        print(super())
'''
    module, _ = compile(my_code, SuperWithoutArgumentsTransformer)
    expected = '''class MyClass:
    def my_method(self):
        print(super(MyClass, self))
'''
    assert str(module) == expected

# Generated at 2022-06-14 02:31:23.486492
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    node = ast.parse('''
        def f():
            super()
        ''')
    SuperWithoutArgumentsTransformer().visit(node)
    expected = ast.parse('''
        def f():
            super(__builtin__, self)
        ''')
    assert astor.to_source(node).strip() == astor.to_source(expected).strip()


# Generated at 2022-06-14 02:31:35.666283
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    ast_tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(ast_tree)

    assert transformer._tree_changed is True
    assert ast.dump(ast_tree) == "Module(body=[FunctionDef(name='<module>', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[]))], decorator_list=[], returns=None, type_comment=None)])"


# Generated at 2022-06-14 02:31:42.214452
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode_str, source_to_ast

    source = source_to_unicode_str('super()')
    tree = source_to_ast(source)

    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)

    expected_source = source_to_unicode_str('super(Cls, self)')
    expected_tree = source_to_ast(expected_source)

    assert transformer._tree_changed is True
    assert expected_tree == tree

# Generated at 2022-06-14 02:31:44.124613
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:31:55.157839
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .helpers import get_node

    # test with super and args
    node = get_node("""
        class A(object):
            def x(self):
                super(A, self)
    """)
    code = compile(node, '<string>', mode='exec')
    assert check_code(code)

    # test with super and args
    node = get_node("""
        class A(object):
            def x(self):
                super(B, self)
    """)
    code = compile(node, '<string>', mode='exec')
    assert check_code(code)

    # test without args
    node = get_node("""
        class A(object):
            def x(self):
                super()
    """)

# Generated at 2022-06-14 02:32:03.264509
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:09.187320
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .example import example_super_without_arguments
    from ..utils import compile_source

    # Test the original example
    tree = compile_source(example_super_without_arguments, __name__, True)
    assert 'super(A, self)' in ast.dump(tree)

    assert 'super(B, cls)' in ast.dump(tree)

# Generated at 2022-06-14 02:32:10.154806
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor, typed_ast.ast3
    #TODO: refactor it to use property

# Generated at 2022-06-14 02:32:11.103346
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:16.302354
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class C(object):
        def f(self):
            super()
    """
    tree = ast.parse(code)  # type: ignore
    SuperWithoutArgumentsTransformer().visit(tree)
    print(format(tree, 'concise'))

# Generated at 2022-06-14 02:32:17.524647
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:27.640748
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    from .legacy_transformers import LegacySuperWithoutArgumentsTransformer
    from .helper import get_ast, check_ast

    source = """
    class Foo:
        def bar(self):
            super()
    """

    tree = get_ast(source)
    check = check_ast(tree)
    check.name = 'Foo'
    check.type = 'ClassDef'
    check.body().name = 'bar'
    check.body().type = 'FunctionDef'
    check.body().body().name = 'super'
    check.body().body().value().args[0].id = 'Foo'
    check.body().body().value().args[1].id = 'self'

    check.run()

    # Also test with legacy class
    tree = get_ast(source)
    check = check_

# Generated at 2022-06-14 02:32:37.704349
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from textwrap import dedent

    tree = astor.parse_file(dedent('''
    class Foo:
        def __init__(self):
            super()

        @property
        def bar(self):
            super()
    '''))

    trans = SuperWithoutArgumentsTransformer()
    trans.visit(tree)

    assert astor.to_source(tree).strip() == dedent('''
    class Foo:
        def __init__(self):
            super(Foo, self)

        @property
        def bar(self):
            super(Foo, self)
    ''').strip()

# Generated at 2022-06-14 02:32:45.167036
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from ..utils.tree import get_ast

    source = source_to_unicode("""
        class A:
            def __init__(self):
                super().__init__()
    """)

    tree = get_ast(source)
    SuperWithoutArgumentsTransformer(tree).visit(tree)

    source2 = source_to_unicode("""
        class A:
            def __init__(self):
                super(A, self).__init__()
    """)

    assert source2 == astor.to_source(tree)

# Generated at 2022-06-14 02:32:53.878951
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = dedent('''
    class Cls:
        def __new__(cls):
            super()
        def __init__(self):
            super()
    ''')
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    add_before_each_return_stmt(tree, transformer.target)
    assert code_equal(tree, '''
    class Cls:
        def __new__(cls):
            super(Cls, cls)
        def __init__(self):
            super(Cls, self)
    ''')

# Generated at 2022-06-14 02:33:12.831086
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')

    class Cls(ast.NodeVisitor):

        def __init__(self, node):
            self.node = node

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            self.node.args = [ast.Name(id='Cls'), ast.Name(id='cls')]

    instance = Cls(tree.body[0].value)
    instance.visit(tree)

    assert tree == ast.parse('super(Cls, cls)')

# Generated at 2022-06-14 02:33:16.827716
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    module = ast.parse(
        """
super()
        """
    )
    result = SuperWithoutArgumentsTransformer(module).visit(module)

# Generated at 2022-06-14 02:33:28.372484
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class ModuleLineNumbering(ast.NodeVisitor):
        def __init__(self, tree):
            self.lineno = 0
            ast.NodeVisitor.__init__(self)
            self.visit(tree)

        def visit_Module(self, node):
            self.generic_visit(node)
            del node.body[-1].value.args

        def visit(self, node):
            try:
                node.lineno = self.lineno
            except AttributeError:
                pass
            ast.NodeVisitor.visit(self, node)

        def generic_visit(self, node):
            for field, value in ast.iter_fields(node):
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, ast.AST):
                            self

# Generated at 2022-06-14 02:33:31.393965
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    transformer = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:33:41.745082
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from astor.code_gen import to_source
    from . import ExampleCode
    from .base import BaseNodeTransformer

    class_with_super = '''
    class Foo(object):
        def __init__(self):
            super()'''
    ast_node = ast.parse(class_with_super, mode='exec')
    foo = SuperWithoutArgumentsTransformer()
    foo.visit(ast_node)
    assert to_source(ast_node) == '''
    class Foo(object):
        def __init__(self):
            super(Foo, self)'''

    class_with_super = '''
    class Foo(object):
        def bar(self):
            super()'''
    ast_node = ast.parse(class_with_super, mode='exec')
    foo = Super

# Generated at 2022-06-14 02:33:45.792820
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import inspect
    import astor.codegen
    import ast2json

    node = ast.parse(inspect.getsource(test_SuperWithoutArgumentsTransformer))
    node = SuperWithoutArgumentsTransformer().visit(node)

    print(astor.to_source(node))
    print(ast2json.dump(node))

# Generated at 2022-06-14 02:33:58.473661
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import unittest

    class TestSuperWithoutArgumentsTransformer(unittest.TestCase):
        def test_super(self):
            from typed_ast import ast3 as ast

            module = """
            class D(object):
                def __init__(self):
                   super().__init__() 
                def test(self):
                   super().test()
                @classmethod
                def testc(cls):
                   super().testc()
                @staticmethod
                def tests():
                   super().tests()
            """
            module_ast = parse(module)
            SuperWithoutArgumentsTransformer(module_ast).visit(module_ast)
            compiled_module_ast = parse(compile(module_ast, '', 'exec'))
            cls = compiled_module_ast.body[0]

# Generated at 2022-06-14 02:33:59.921205
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:08.683810
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from .test_transformer import Source

    src = Source(source_to_unicode("""
    class SuperTest:
        def __init__(self):
            super()
        def test(self):
            super()
    """))
    t = SuperWithoutArgumentsTransformer()
    t.visit(src.tree)
    assert src.unicode_repr() == """
    class SuperTest:
        def __init__(self):
            super(SuperTest, self)
        def test(self):
            super(SuperTest, self)
    """

# Generated at 2022-06-14 02:34:14.046203
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer().visit(ast.parse("super()")) == ast.parse("super(Cls, self)")
    assert SuperWithoutArgumentsTransformer().visit(ast.parse("super(self, cls)")) == ast.parse("super(self, cls)")

# Unit test from the doc string of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:29.481718
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import os
    import astor

# Generated at 2022-06-14 02:34:34.696313
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from .base import BaseNodeTransformer, CONST_NODE
    import textwrap
    
    code = textwrap.dedent('''
    class A:
      def __init__(self):
        super()
    ''')
    
    tree = ast3.parse(code)
    visitor = BaseNodeTransformer()
    visitor.visit(tree)
    assert CONST_NODE in visitor.get_changed_nodes()

# Generated at 2022-06-14 02:34:36.137293
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:34:37.897339
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    SuperWithoutArgumentsTransformer(None, None).visit(None)

# Generated at 2022-06-14 02:34:38.571301
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert True

# Generated at 2022-06-14 02:34:44.670904
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Vistor(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call) -> ast.Call:
            if isinstance(node.func, ast.Name) and node.func.id == 'super' and len(node.args) == 1:
                raise AssertionError('super() not replaced')

    tree = ast.parse("""
        class Foo:
            def __init__(self):
                super()
    """)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    Vistor().visit(tree)

# Generated at 2022-06-14 02:34:47.331337
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pytest.test_numpy()
    pytest.test_scipy()
    pytest.test_sympy()
    pytest.test_tensorflow()
    pytest.test_pandas()
    pytest.test_sklearn()
    pytest.test_skimage()

# Generated at 2022-06-14 02:34:52.364845
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformerTestCase, transform, warning

    class Test(BaseNodeTransformerTestCase):
        target = SuperWithoutArgumentsTransformer


# Generated at 2022-06-14 02:35:04.581100
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from .test_BaseNodeTransformer import BaseNodeTransformerTest
    from ..utils.helpers import get_ast_of_code, get_python_source

    tester = BaseNodeTransformerTest(SuperWithoutArgumentsTransformer)

    test_code_1 = """
    class A:
        def f(self):
            super()
    """
    ast_1 = get_ast_of_code(test_code_1)
    tester.test(ast_1, test_code_1)

    test_code_2 = """
    class A:
        def f():
            super()
    """
    ast_2 = get_ast_of_code(test_code_2)
    tester.test(ast_2, test_code_2)

    test_code

# Generated at 2022-06-14 02:35:08.133390
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import typed_ast.ast3 as ast

    code = 'super()'
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:35:49.627422
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class_def = ast.FunctionDef(
        name='Foo',
        args=ast.arguments(
            args=[ast.Name(id='self')],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[
            ast.Call(
                func=ast.Attribute(
                    value=ast.Name(
                        id='super'
                    ),
                    attr='bar',
                    ctx=ast.Load()
                ),
                args=[],
                keywords=[],
                starargs=None,
                kwargs=None
            )
        ],
        decorator_list=[],
        returns=None
    )

# Generated at 2022-06-14 02:36:00.166451
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import parse
    from .. import print_tree
    from .ast_converter import ASTConverter
    from .class_renamer import ClassRenamer
    from .copy_cleaner import CopyCleaner
    from .dead_code_eliminator import DeadCodeEliminator
    from .function_definitions import FunctionDefinitions
    from .stdout_writer import StdoutWriter
    from .variables_assignments import VariablesAssignments

    code = "class A(B):\n    def foo(self):\n        super()"
    tree = parse(code)
    converter = ASTConverter()
    converter.visit(tree)
    tree = converter.tree
    class_renamer = ClassRenamer(tree)
    class_renamer.visit(tree)
    tree = class_renamer

# Generated at 2022-06-14 02:36:01.940007
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Unit test for constructor of class SuperWithoutArgumentsTransformer"""
    from typed_ast import ast3
    import astor

# Generated at 2022-06-14 02:36:11.439855
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .helpers import get_ast
    import typed_ast.ast3 as ast
    from .base import BaseNodeTransformer

    tree = get_ast(
        """
        class A:
            def __init__(self):
                super()
        """
    )

    Transformer = SuperWithoutArgumentsTransformer.get_transformer()

    # Create an instance of the transformer.
    transformer = Transformer(tree)

    # Visit and replace nodes that match the predicate.
    transformer.visit(tree)

    # Ensure the expected changes were made.
    assert isinstance(tree, ast.Module)
    assert isinstance(tree.body[0], ast.ClassDef)
    assert isinstance(tree.body[0].body[0], ast.FunctionDef)

# Generated at 2022-06-14 02:36:18.206769
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    b = SuperWithoutArgumentsTransformer()
    class Cls:
        def __init__(self):
            super()

    code = inspect.getsource(Cls)
    module = ast.parse(code)
    b.visit(module)
    assert 'super' in code
    assert b._tree_changed

    exec(compile(module, filename="<ast>", mode="exec"))  # pylint: disable=exec-used

# Generated at 2022-06-14 02:36:19.514714
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:36:22.113671
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = """super()"""
    tree = ast.parse(node)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    expected = ast.parse("super(Cls, self)")
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:36:29.972907
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Cls:
        def __init__(self):
            super()
    """
    tree = ast.parse(code)  # type: ignore
    compiler = SuperWithoutArgumentsTransformer()
    compiler.visit(tree)
    
    Cls = tree.body[0]  # type: ignore
    assert Cls.name == 'Cls'
    func = Cls.body[0]  # type: ignore
    assert func.name == '__init__'
    super_call = func.body[0]  # type: ignore
    assert (super_call.args[0].id, super_call.args[1].id) == ('Cls', 'self')

# Generated at 2022-06-14 02:36:33.675468
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Test case for the constructor of SuperWithoutArgumentsTransformer.
    """
    node = ast.Call(func=ast.Name(id='super', ctx=ast.Load()),
                    args=[], keywords=[])
    transformer = SuperWithoutArgumentsTransformer(node)

    assert transformer is not None

# Generated at 2022-06-14 02:36:34.774270
# Unit test for constructor of class SuperWithoutArgumentsTransformer