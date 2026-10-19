

# Generated at 2022-06-14 02:27:59.312502
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:09.815355
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class X():
        def func(self):
            super()
    """

    t = ast.parse(code)
    SuperWithoutArgumentsTransformer.run_default(t)

    assert t.body[0].bases == [ast.Name(id="object")]
    assert t.body[0].body[0].args.args[0].arg == "self"
    assert isinstance(t.body[0].body[0].body[0].value.args[0], ast.Name)
    assert isinstance(t.body[0].body[0].body[0].value.args[1], ast.Name)
    assert t.body[0].body[0].body[0].value.args[0].id == "X"

# Generated at 2022-06-14 02:28:22.233345
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.source import source_to_unicode as u
    from ..utils.source import split_lines as sl
    from .base import BaseObjectTransformer
    from .object import ObjectTransformer


# Generated at 2022-06-14 02:28:23.057172
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:28:32.838735
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..testing.utils import build_ast_tree
    from ..utils.helpers import dump_ast
    from ..utils.ast_builder import build


# Generated at 2022-06-14 02:28:40.670395
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ast import parse, dump
    from ..utils.helpers import get_ast_for_code

    ast1 = get_ast_for_code('super()')
    ast2 = SuperWithoutArgumentsTransformer().visit(ast1)
    code = dump(ast2)
    assert code == "Call(func=Name(id='super', ctx=Load()), args=[Name(id='Foo', ctx=Load()), Name(id='func', ctx=Load())], keywords=[], starargs=None, kwargs=None)"

# Generated at 2022-06-14 02:28:41.229597
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:28:53.283904
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast
    from ..bin.transformer import Transformer

    # Test for super in a class
    class Foo:
        def __init__(self, x):
            super().__init__()
    tree = ast.parse(Foo.__init__.__code__)
    t = Transformer([SuperWithoutArgumentsTransformer])
    tree = t.visit(tree)
    expected = ast.parse("def __init__(self, x):\n    super(Foo, self).__init__()\n")
    assert ast.dump(expected) == ast.dump(tree)

    # Test for super in a function
    def f():
        super()
    tree = ast.parse(f.__code__)
    t = Transformer([SuperWithoutArgumentsTransformer])
    tree = t

# Generated at 2022-06-14 02:28:55.457566
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    t = SuperWithoutArgumentsTransformer()

# Generated at 2022-06-14 02:29:05.482499
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    tree = ast.parse("""
        class Spam:
            def __init__(self) -> None:
                super()
                self.eggs = 1
    """)
    SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:29:19.099206
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..parser import parse
    from ..utils.helpers import assert_equal_code


    code = '''
    class A:
        def __init__(self):
            super().__init__()
    '''
    tree = parse(code)
    SuperWithoutArgumentsTransformer(tree).run()
    assert_equal_code(code, tree)

    code = '''
    class A:
        def __init__(self):
            super()
    '''
    tree = parse(code)
    SuperWithoutArgumentsTransformer(tree).run()
    assert_equal_code('super(A, self)', tree.body[0].body[0].value.args[0])

    code = '''
    class A:
        def __init__(self):
            super(A, self)
    '''


# Generated at 2022-06-14 02:29:22.164765
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:23.308957
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:29:28.027558
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    from ..utils import get_closest_parent_of
    

# Generated at 2022-06-14 02:29:29.696783
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import astor
    

# Generated at 2022-06-14 02:29:36.368549
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import get_ast, assert_source_equal  # noqa
    tree = get_ast("super()")
    SuperWithoutArgumentsTransformer(tree).visit()
    assert_source_equal(tree, "super(Cls, self)")
    tree = get_ast("super()")
    SuperWithoutArgumentsTransformer(tree).visit()
    assert_source_equal(tree, "super(Cls, self)")

# Generated at 2022-06-14 02:29:37.705951
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    node = ast.parse('super()')

# Generated at 2022-06-14 02:29:43.492747
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():

    code = """
    class Cls:
        def f_func(self):
            super()
    """

    expected_code = """
    class Cls:
        def f_func(self):
            super(Cls, self)
    """
    
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))

# Generated at 2022-06-14 02:29:53.265625
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .. import compile
    import textwrap

    code = textwrap.dedent('''
    class A(object):
        def f(self):
            return super().f
            ''')
    _, tree = compile(code)
    node = tree.body[0].body[0].body[0].value
    assert isinstance(node, ast.Call)
    assert isinstance(node.func, ast.Attribute)
    assert node.func.attr == 'f'
    assert node.func.value.args == [ast.Name(id='A'), ast.Name(id='self')]



# Generated at 2022-06-14 02:29:57.335053
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    super_without_args_transformer = SuperWithoutArgumentsTransformer()
    node_example = ast.parse('super()')
    super_without_args_transformer.visit(node_example)
    target = ast.parse('super(clsname, self)')
    assert ast.dump(node_example) == ast.dump(target)

# Generated at 2022-06-14 02:30:09.549951
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse('super()').body[0]
    obj = SuperWithoutArgumentsTransformer()
    obj.visit(node)
    node_str = ast.dump(node)
    assert node_str == "Expr(value=Call(func=Name(id='super', ctx=Load()), args=[Name(id='Cls', ctx=Load()), Name(id='self', ctx=Load())], keywords=[], starargs=None, kwargs=None))"

# Generated at 2022-06-14 02:30:16.501160
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .test_helpers import get_ast_for_source_lines

    src = (
        'class A(object):',
        '    def b(self):',
        '        super()'
    )

    target = (
        'class A(object):',
        '    def b(self):',
        '        super(A, self)'
    )

    result = get_ast_for_source_lines(src)
    SuperWithoutArgumentsTransformer(result).visit(result)
    assert result == get_ast_for_source_lines(target)

# Generated at 2022-06-14 02:30:21.974891
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    tree = astor.parse_file('test/fixtures/super_without_arguments.py')
    SuperWithoutArgumentsTransformer().visit(tree)
    compiled = astor.to_source(tree)

    assert(compiled == 'class MyTest:\n    def f(self):\n        super(MyTest, self).__init__(2)\n')

# Generated at 2022-06-14 02:30:27.395348
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast

    before = ast.parse("""
super()
    """)
    expected = ast.parse("""
super(Cls, self)
    """)

    transformer = SuperWithoutArgumentsTransformer(tree=before)
    transformer.register_transformer(func=transformer._replace_super_args)
    transformer.visit(before)
    assert ast.dump(before) == ast.dump(expected)

# Generated at 2022-06-14 02:30:27.972696
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:34.018287
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    code = """
            class Cls(object):
                def foo(self):
                    super()
        """
    expected_output = """
            class Cls(object):
                def foo(self):
                    super(Cls, self)
        """
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.run()
    assert_code_equal(ast.unparse(tree), expected_output)



# Generated at 2022-06-14 02:30:41.438532
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from .utils import make_call
    from ..utils.helpers import get_first_node_of_type

    node = make_call(
        name='super',
        args=[],
        func_name='func',
        func_args=['self'],
        cls_name='Cls',
    )
    expected = make_call(
        name='super',
        args=[
            ast.Name(
                id='Cls',
                ctx=ast.Load(),
            ),
            ast.Name(
                id='self',
                ctx=ast.Load(),
            ),
        ],
    )

    transformer = SuperWithoutArgumentsTransformer()
    new_node = transformer._replace_super_args(node)

    assert new_node.func.id == expected.func.id

# Generated at 2022-06-14 02:30:43.602631
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import run_filter
    from . import FilterSuperWithoutArguments


# Generated at 2022-06-14 02:30:44.344965
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:30:54.901107
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    class Func(ast.AST):
        """Function definition"""
        def __init__(self, name: str, args: List[str] = []) -> None:
            self.name = name
            self.args = [ast.Name(id=arg) for arg in args]
            self.body = []

    class Cls(ast.AST):
        """Class definition"""
        def __init__(self, name: str) -> None:
            self.name = name
            self.body = []


# Generated at 2022-06-14 02:31:00.775843
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:31:02.425968
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_nodes

# Generated at 2022-06-14 02:31:03.870296
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_snippet

# Generated at 2022-06-14 02:31:05.092835
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:31:11.484025
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A():
        def __init__(self):
            super().__init__(3, 4)
        def __new__(cls):
            super().__new__(cls)
        def foo(self):
            super().foo(x=2)
        def bar(cls):
            super().bar()
    """
    transformer = SuperWithoutArgumentsTransformer()
    transformer.visit(ast.parse(code))
    assert transformer.tree_changed()

# Generated at 2022-06-14 02:31:11.984756
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    pass

# Generated at 2022-06-14 02:31:13.690271
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:31:21.087963
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import setup_transformer

    code = """
        class C(object):
            def foo(self):
                super()
    """

    expected_code = """
        class C(object):
            def foo(self):
                super(C, self)
    """

    tree = setup_transformer(SuperWithoutArgumentsTransformer, code, target=(2, 7))
    assert expected_code == tree_to_code(tree, indent='    ', single=True)



# Generated at 2022-06-14 02:31:27.526978
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse(textwrap.dedent('''
    class Test:
        def __init__(self):
            super() # should be super(Test, self)
    '''))
    SuperWithoutArgumentsTransformer().visit(node)
    module = ast.Module(body=node.body)

    assert ast.dump(module) == ast.dump(ast.parse(textwrap.dedent('''
    class Test:
        def __init__(self):
            super(Test, self)
    ''')))


# Generated at 2022-06-14 02:31:39.347194
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .base import UnitTestTransformer
    import textwrap
    source = textwrap.dedent('''\
    class cls(object):
        def method(self):
            super()
            pass
        @classmethod
        def class_method(cls):
            super()
            pass
    ''')
    expected_source = textwrap.dedent('''\
    class cls(object):
        def method(self):
            super(cls, self)
            pass
        @classmethod
        def class_method(cls):
            super(cls, cls)
            pass
    ''')
    UnitTestTransformer(
        SuperWithoutArgumentsTransformer, source, expected_source,
        target=(2, 7)
    )

# Generated at 2022-06-14 02:31:48.928130
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    assert SuperWithoutArgumentsTransformer(None).target == (2, 7)



# Generated at 2022-06-14 02:31:56.973867
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():

    from typed_ast import ast3
    from ...unit import transform
    from ...unit import compare

    # Test this example:
    # class A:
    #   def __init__(self):
    #     super().__init__()
    # this example will be transformed from:
    # class A:
    #   def __init__(self):
    #     super(A, self).__init__()

    tree = ast3.parse('class A:\n  def __init__(self):\n    super().__init__()')

    expected = ast3.parse('class A:\n  def __init__(self):\n    super(A, self).__init__()')

    transform(SuperWithoutArgumentsTransformer, tree, expected)



# Generated at 2022-06-14 02:32:01.516174
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = parse('super()')
    tree = SuperWithoutArgumentsTransformer(None).visit(code)
    assert tree.body[0].value.args[0].id == 'Cls'

# Generated at 2022-06-14 02:32:11.438179
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils import get_ast, compare_asts

    source = """\
        class Cls:
            def __init__(self):
                super()
                super().method()

            def method(self):
                super()
    """
    expected = """\
        class Cls:
            def __init__(self):
                super(Cls, self)
                super(Cls, self).method()

            def method(self):
                super(Cls, self)
    """
    ast1 = get_ast(source)
    ast2 = get_ast(expected)

    nodeTransformer = SuperWithoutArgumentsTransformer(ast1)
    nodeTransformer.visit(ast1)

    assert compare_asts(ast1, ast2)

# Generated at 2022-06-14 02:32:20.984926
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .transpile_test_util import TranspileTestCase

    class Test(TranspileTestCase):
        def test_super_without_arguments(self):
            self.assertCodeExecution("""
                class Cls(object):
                    def meth(self):
                        return super()
                cls = Cls()
                print("{}.__class__.__name__".format(cls))
                print("{}.__class__.__base__.__name__".format(cls))
            """, run_in_function=False)

    return Test


# Generated at 2022-06-14 02:32:21.586826
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:23.498813
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test constructor of SuperWithoutArgumentsTransformer"""
    pass

# Generated at 2022-06-14 02:32:33.422842
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    v = SuperWithoutArgumentsTransformer()
    v.visit(ast.parse("""
    class Foo:
        def __init__(self):
            super()
        
        @staticmethod
        def foo():
            super()
    """))
    assert str(v.tree) == textwrap.dedent("""\
    class Foo:
        def __init__(self):
            super(Foo, self)
        
        @staticmethod
        def foo():
            super(Foo, cls)
    """)

# Generated at 2022-06-14 02:32:34.528589
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:32:36.029763
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:32:52.518091
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
        
        class C:
            def f():
                super()
                
        class D(object):
            def g(self):
                super()
    """
    expected_code = """
        
        class C:
            def f():
                super(C, self)
                
        class D(object):
            def g(self):
                super(D, self)
    """
    module = ast.parse(dedent(code))
    SuperWithoutArgumentsTransformer().visit(module)

    code2 = dedent(expected_code)
    module2 = ast.parse(code2)
    assert equal_trees(module, module2)

# Generated at 2022-06-14 02:32:58.194446
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    src = """
    class A(object):
        def b(self, a):
            super()
    """
    expected = """
    class A(object):
        def b(self, a):
            super(A, self)
    """
    tree = ast.parse(src)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:33:05.570577
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_unicode
    example_code = source_to_unicode("""
                  class Cls:
                      def __init__(self):
                          super()
                  """)
    tree = ast.parse(example_code)
    SuperWithoutArgumentsTransformer().visit(tree)
    assert ast.dump(tree) == source_to_unicode("""
                  class Cls:
                      def __init__(self):
                          super(Cls, self)
                  """)

# Generated at 2022-06-14 02:33:06.189584
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:33:10.221638
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ast import parse

    class TestSuperWithoutArgumentsTransformer(SuperWithoutArgumentsTransformer):
        def _replace_super_args(self, node):
            node.args = [ast.Name(id='cls_name'), ast.Name(id='func_name')]
            

# Generated at 2022-06-14 02:33:13.128919
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils.helpers import code_to_ast, ast_to_code


# Generated at 2022-06-14 02:33:23.120722
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor, typed_astunparse
    from ..node_visitor import NodeTransformer
    code = 'super()'
    tree = ast.parse(code)
    result = astor.to_source(NodeTransformer(SuperWithoutArgumentsTransformer()).visit(tree))
    expected = 'super(__class__, self)'
    assert(result == expected)
    code = 'super().__init__()'
    tree = ast.parse(code)
    result = astor.to_source(NodeTransformer(SuperWithoutArgumentsTransformer()).visit(tree))
    expected = 'super(__class__, self).__init__()'
    assert(result == expected)

# Generated at 2022-06-14 02:33:27.808003
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    class Old:
        class Cls:
            def func(self):
                super()

    class New:
        class Cls:
            def func(self):
                super(Cls, self)



# Generated at 2022-06-14 02:33:35.933863
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .test_helpers import assert_transformation
    from ..utils.helpers import clean_warning_registry

    # pylint: disable=unused-variable, protected-access
    class Test:
        def __init__(self):
            super()

    # Before transformation
    assert_transformation(
        Test.__init__,
        """
        def __init__(self):
            super()
        """
    )
    # After transformation
    assert_transformation(
        Test.__init__,
        """
        def __init__(self):
            super(Test, self)
        """
    )
    clean_warning_registry()

# Generated at 2022-06-14 02:33:43.083233
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # fmt: off
    source = '''
    class A:
        def __init__(self):
            super()
    '''
    expected = '''
    class A:
        def __init__(self):
            super(A, self)
    '''
    # fmt: on

    tree = ast.parse(source)
    transformer = SuperWithoutArgumentsTransformer()
    new_tree = transformer.visit(tree)

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:34:03.258281
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    # Run test case
    transformer = SuperWithoutArgumentsTransformer(None)
    node = ast.parse("super()")
    transformer.generic_visit(node)
    assert node.body[0].value.func.id == "super"
    assert len(node.body[0].value.args) == 2
    assert node.body[0].value.args[0].id == "__class__"
    assert node.body[0].value.args[1].id == "__self__"

    # Run test case
    transformer = SuperWithoutArgumentsTransformer(None)
    node = ast.parse('super()\nsuper()')
    transformer.generic_visit(node)
    assert node.body[0].value.func.id == "super"
    assert len(node.body[0].value.args) == 2

# Generated at 2022-06-14 02:34:14.362807
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """
    Checks if the SuperWithoutArgumentsTransformer class properly detects the super() method call
    and replaces the argument-less call to super() with call to super() with two arguments: class and instance.
    """
    tree = ast.parse("""
    class Bar():
        def __init__(self):
            super()
    """)
    tree = SuperWithoutArgumentsTransformer().visit(tree)

# Generated at 2022-06-14 02:34:20.324273
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    # Simple case
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree, 'module').visit(tree)
    assert tree_to_str(tree) == 'super(Cls, self)'

    # Check that it works inside method
    tree = ast.parse('class A: def f(self): super()')
    SuperWithoutArgumentsTransformer(tree, 'module').visit(tree)
    assert tree_to_str(tree) == 'class A: def f(self): super(A, self)'



# Generated at 2022-06-14 02:34:24.290752
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    """Test if SuperWithoutArgumentsTransformer constructor raises error for invalid string."""
    with pytest.raises(ValueError):
        SuperWithoutArgumentsTransformer("test")


# Unit Test for method visit_Call()

# Generated at 2022-06-14 02:34:29.538313
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = '''
    class A:
        def __init__(self):
            super().__init__()
            
    '''
    tree = ast.parse(code)
    transformer = SuperWithoutArgumentsTransformer(tree)
    new_tree = transformer.visit(tree)
    transformer.assert_no_changes()

# Generated at 2022-06-14 02:34:33.882685
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    node = ast.parse('super()')

    SuperWithoutArgumentsTransformer().visit(node)

    assert ast.dump(node) == 'Call(Name(id="super", ctx=Load()), [Name(id="Cls", ctx=Load()), Name(id="self", ctx=Load())], [], None, None)'

# Generated at 2022-06-14 02:34:38.741002
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    def do_test(code_before, code_after, version):
        tree = ast.parse(code_before)
        SuperWithoutArgumentsTransformer(tree, version).visit(tree)
        assert code_after == astor.to_source(tree)


# Generated at 2022-06-14 02:34:40.422567
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile_restricted
    from ast import parse


# Generated at 2022-06-14 02:34:44.115957
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
  class ExampleTransformer(SuperWithoutArgumentsTransformer):
    target = (2, 7)

    def run(self, source: str) -> str:
      return source
    

# Generated at 2022-06-14 02:34:53.699249
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    import copy
    from typed_ast import ast3 as ast
    from ..utils.tree import get_closest_parent_of
    from .super_without_arguments_transformer import SuperWithoutArgumentsTransformer

    tree = ast.parse('class Foo:\n  def foo(self): super()\n  def bar(cls): super()')
    node = get_closest_parent_of(tree, get_closest_parent_of(tree,tree.body[0].body[0], ast.FunctionDef), ast.ClassDef)
    transformer = SuperWithoutArgumentsTransformer(tree=tree)
    transformer.visit(node)
    expected = ast.parse('class Foo:\n  def foo(self): super(Foo, self)\n  def bar(cls): super(Foo, cls)')

   

# Generated at 2022-06-14 02:35:32.719825
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert astunparse(tree) == 'super(cls, self)'

    tree = ast.parse('super()')
    SuperWithoutArgumentsTransformer(tree).visit(tree)
    assert astunparse(tree) == 'super(cls, self)'


# Generated at 2022-06-14 02:35:33.897719
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:35:43.051108
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from typed_ast.ast3 import parse, dump
    import textwrap

    code = textwrap.dedent(r'''
        class A:
            def f(self, x):
                super()
                super(x)
                super()
        ''')
    expected = textwrap.dedent(r'''
        class A:
            def f(self, x):
                super(A, self)
                super(x)
                super(A, self)
        ''')
    tree_A= parse(code, mode='exec')
    tree_B= parse(expected, mode='exec')
    SuperWithoutArgumentsTransformer().visit(tree_A)
    print(dump(tree_A))
    assert ast3.dump(tree_A, include_attributes=True)

# Generated at 2022-06-14 02:35:43.571338
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    pass

# Generated at 2022-06-14 02:35:51.192108
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class A(object):
        def __init__(self):
            super()

    class B(A, object):
        def __init__(self):
            super()
    """

    # Running the transformer
    result = SuperWithoutArgumentsTransformer().visit(get_ast(code))

    # Checking the result
    expected_code = """
    class A(object):
        def __init__(self):
            super(A, self)

    class B(A, object):
        def __init__(self):
            super(B, self)
    """
    expected_ast = get_ast(expected_code)

    assert ast.dump(result) == ast.dump(expected_ast)



# Generated at 2022-06-14 02:35:53.627858
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..transpile import from_str
    from .super_without_arguments import super_without_arguments


# Generated at 2022-06-14 02:35:57.232079
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    tree = ast.parse('super()')
    transformer = SuperWithoutArgumentsTransformer(tree)
    transformer.visit(tree)
    assert transformer.tree_changed
    assert dump_tree(tree) == 'super(Cls, self)'

# Generated at 2022-06-14 02:36:00.140878
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from unittest.mock import Mock
    from .functions import FunctionTransformer
    from .classes import ClassTransformer
    from .base import BaseNodeTransformer


# Generated at 2022-06-14 02:36:04.332484
# Unit test for method visit_Call of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer_visit_Call():
    from ..utils import run_transformer
    from ..utils import compare_ast
    from .. import parse

    m = parse.parse('''
    class MyClass:
        def my_method(self):
            super()
    ''')
    assert compare_ast(run_transformer(m, SuperWithoutArgumentsTransformer), '''
    class MyClass:
        def my_method(self):
            super(MyClass, self)
    ''')

# Generated at 2022-06-14 02:36:12.330870
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from typed_ast import ast3
    from .test_helpers import compile_func
    class Cls:
        def __init__(self):
            self.a = super()
    func_ast3 = compile_func(Cls.__init__, 'func_name', 'Cls')
    func_ast2 = SuperWithoutArgumentsTransformer().visit(func_ast3)
    assert isinstance(func_ast2, ast3.FunctionDef)
    stmts = func_ast2.body
    assert len(stmts) == 1
    stmt = stmts[0]
    assert isinstance(stmt, ast3.Assign)
    super_call = stmt.value
    assert isinstance(super_call, ast3.Call)

# Generated at 2022-06-14 02:37:23.657970
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor

# Generated at 2022-06-14 02:37:27.274225
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
    class Bases:
        pass
    class A(Bases):
        def __init__(self):
            super()
    """
    expected_code = """
    class Bases:
        pass
    class A(Bases):
        def __init__(self):
            super(A, self)
    """
    tree = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(tree)
    result = compile(tree, filename="", mode="exec")
    exec(result)

# Generated at 2022-06-14 02:37:33.090333
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    with open('./tests/assets/super_without_args.py') as f:
        tree: SRT = ast.parse(f.read())

    SuperWithoutArgumentsTransformer().visit(tree)

    func = tree.body[1]
    assert isinstance(func, ast.FunctionDef)

    cls = tree.body[0]
    assert isinstance(cls, ast.ClassDef)

    func_call = func.body[0].value
    assert isinstance(func_call, ast.Call)

    assert func_call.args[0].id == cls.name
    assert func_call.args[1].id == 'self'

# Generated at 2022-06-14 02:37:34.267091
# Unit test for constructor of class SuperWithoutArgumentsTransformer

# Generated at 2022-06-14 02:37:42.805374
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.test_utils import should_not_change
    from ..utils.test_utils import should_change_regex
    from ..utils.test_utils import run_test_node, run_test_ast

    code = '''
        class A:
            def foo(self):
                super().foo()
    '''
    should_not_change(SuperWithoutArgumentsTransformer, code)

    code = '''
        class A:
            def foo(self):
                super()
    '''
    should_change_regex(SuperWithoutArgumentsTransformer, code, r'super\(A, self\)')

    code = '''
        class A:
            def foo(cls, self):
                super()
            
            def bar(self):
                super()
    '''
    should_change_re

# Generated at 2022-06-14 02:37:43.810935
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    import astor
    from ..tree import AST


# Generated at 2022-06-14 02:37:45.070403
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from ..utils.source import source_to_ast

    # Test for super() in class

# Generated at 2022-06-14 02:37:50.688055
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    code = """
      class S(object):
          def __init__(self):
              super()
              super().__init__()

          def method(self):
              super()
              super().method()
    """
    module = ast.parse(code)
    SuperWithoutArgumentsTransformer().visit(module)
    assert isinstance(module.body[0].body[0].value, ast.Call)
    assert len(module.body[0].body[0].value.args) == 2
    assert module.body[0].body[0].value.args[0].id == 'S'
    assert module.body[0].body[0].value.args[1].id == 'self'
    assert module.body[0].body[1].value.func.value.args[0].id == 'S'
    assert module

# Generated at 2022-06-14 02:37:55.046234
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    x = """
    class Foo:
        def __init__(self):
            super()
    """
    expected = """
    class Foo:
        def __init__(self):
            super(Foo, self)
    """
    # TODO: add test
    return None



# Generated at 2022-06-14 02:38:02.703534
# Unit test for constructor of class SuperWithoutArgumentsTransformer
def test_SuperWithoutArgumentsTransformer():
    from .. import compile
    from typed_ast import ast3
    source = """
    class A:
        def __init__(self):
            super().__init__()
    """
    expected = """
    class A:
        def __init__(self):
            super(A, self).__init__()
    """
    tree = ast3.parse(source)
    assert compile(tree, SuperWithoutArgumentsTransformer) == expected

    source = """
    class A:
        def __init__(self, x):
            super().__init__(x + 1)
    """
    expected = """
    class A:
        def __init__(self, x):
            super(A, self).__init__(x + 1)
    """
    tree = ast3.parse(source)