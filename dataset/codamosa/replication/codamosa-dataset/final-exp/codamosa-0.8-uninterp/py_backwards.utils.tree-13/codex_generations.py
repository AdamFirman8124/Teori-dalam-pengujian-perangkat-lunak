

# Generated at 2022-06-14 03:01:45.314371
# Unit test for function get_parent
def test_get_parent():
    import unittest
    from typed_ast import ast3 as ast

    class TestGetParent(unittest.TestCase):
        def test_get_parent_returns_expected_node(self):
            with self.subTest('parent of name'):
                mod = ast.Module(body=[ast.FunctionDef(name='foo', body=[
                    ast.Return(value=ast.Name(id='foo', ctx=ast.Load())),
                ])])
                parent = get_parent(mod, mod.body[0].body[0].value)
                self.assertIs(mod.body[0].body[0], parent)


# Generated at 2022-06-14 03:01:52.022093
# Unit test for function find
def test_find():
    # Tests find with a single node of a type
    class TestNode(ast.AST):
        _fields = ("test_field",)
    parent = ast.Module([TestNode(test_field="test")])
    found_nodes = list(find(parent, TestNode))
    assert len(found_nodes) == 1
    assert found_nodes[0].test_field == "test"

    # Tests find with multiple nodes of a type
    class TestNode(ast.AST):
        _fields = ("test_field",)
    parent = ast.Module([TestNode(test_field="test")] * 3)
    found_nodes = list(find(parent, TestNode))
    assert len(found_nodes) == 3
    assert found_nodes[0].test_field == "test"
    assert found_n

# Generated at 2022-06-14 03:02:04.056764
# Unit test for function get_parent
def test_get_parent():
    # test for function get_parent
    a = ast.Name(id="a", ctx=ast.Load())
    b = ast.Name(id="b", ctx=ast.Load())
    c = ast.Name(id="c", ctx=ast.Load())
    d = ast.Name(id="d", ctx=ast.Load())
    e = ast.Name(id="e", ctx=ast.Load())
    f = ast.Name(id="f", ctx=ast.Load())
    f.value = ast.Call(func=d, args=[e], keywords=[])
    f.value.func.value = c
    f.value.func.value.value = b
    c.value = ast.Call(func=f, args=[a], keywords=[])
    c.value.func.value = f

# Generated at 2022-06-14 03:02:13.012487
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import ast

    class Empty(ast.AST):

        def __init__(self, *args, **kwargs):
            pass

        def __iter__(self):
            return iter([])

    class Exp(ast.AST):

        def __init__(self, *args, **kwargs):
            pass

        def __iter__(self):
            return iter([])

    class Block:

        def __init__(self, body, *args):
            self.body = body

    parent = Block([Exp(), Exp(), Exp(), Exp(), Exp(), Exp(), Exp()])

    assert(get_non_exp_parent_and_index(parent, parent)
           == (parent, 0))
    assert(get_non_exp_parent_and_index(parent, parent.body[0])
           == (parent, 0))

# Generated at 2022-06-14 03:02:16.197048
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast, parse
    tree = parse('a = 1')
    assert find(tree,ast.Assign) 
    assert find(tree,str) == []

# Generated at 2022-06-14 03:02:25.066889
# Unit test for function get_parent
def test_get_parent():
    import astunparse
    from .environment.environment import Environment
    import textwrap
    code = textwrap.dedent('''\
    def example():
        a = 5
        b = 6

        return a + b
    ''')
    tree = ast.parse(code)
    _build_parents(tree)
    env = Environment()
    environment.add_function(tree, "example", env)
    # Unit test for function get_parent

# Generated at 2022-06-14 03:02:39.991838
# Unit test for function replace_at
def test_replace_at():
    root = ast.parse("""
        a = 1
        b = 2
    """)

    mod = root.body
    replace_at(0, mod, ast.parse("""
        a = 1
        c = 2
    """))

# Generated at 2022-06-14 03:02:41.848762
# Unit test for function get_parent

# Generated at 2022-06-14 03:02:53.134609
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse("""
        def foo():
            return 1
        # comment
        def bar():
            return 2
    """)
    foo = tree.body[0]
    bar = tree.body[1]
    comment = tree.body[2]  # type: ignore
    assert comment.s == '# comment'

    replace_at(0, tree, comment)

    assert tree.body[0].s == '# comment'
    assert isinstance(tree.body[1], ast.FunctionDef)
    assert tree.body[1].name == foo.name

    replace_at(1, tree, foo)

    assert isinstance(tree.body[1], ast.FunctionDef)
    assert tree.body[1].name == bar.name

# Generated at 2022-06-14 03:02:56.629377
# Unit test for function find
def test_find():
    tree = ast.parse('foo(1, 2)')
    res = find(tree, ast.Call)

    assert 'Call' in [type(n).__name__ for n in res]



# Generated at 2022-06-14 03:03:12.548599
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Unit test for function get_closest_parent_of.
    """
    source = """module A.B
    import A.B.C
    import B.C
    if a == 1:
        return 2"""
    tree = ast.parse(source)
    node = find(tree, ast.Import).__next__()
    parent = get_closest_parent_of(tree, node, ast.Module)
    assert parent.name.__str__() == """A.B"""
    node = find(tree, ast.Module).__next__()
    parent = get_closest_parent_of(tree, node, ast.Module)
    assert parent is node
    node = find(tree, ast.If).__next__()

# Generated at 2022-06-14 03:03:17.769782
# Unit test for function get_parent
def test_get_parent():
    """Unit test for function get_parent"""
    ast_obj = ast.parse('a = b.c if true else 0')
    if_else_node = get_parent(ast_obj, ast_obj.body[0].value)
    leaves = leaf_nodes(ast_obj)

    assert if_else_node == leaves[1]



# Generated at 2022-06-14 03:03:18.523810
# Unit test for function get_parent
def test_get_parent():
    import astor


# Generated at 2022-06-14 03:03:20.292525
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class_tree = ast.parse('def foo():\n    def bar():\n        pass')
    expected = class_tree.body[0].body[0]
    assert get_closest_parent_of(class_tree, expected, ast.FunctionDef)\
        == class_tree.body[0]

# Generated at 2022-06-14 03:03:23.413261
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('while True: 1\n2')
    node = tree.body[0].body[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert parent == tree.body[0] and index == 0

# Generated at 2022-06-14 03:03:25.942874
# Unit test for function find
def test_find():
    code = """
    def foo():
        pass
    """
    tree = ast.parse(code)
    assert len(list(find(tree, ast.FunctionDef))) == 1
    assert len(list(find(tree, ast.arguments))) == 1


# Generated at 2022-06-14 03:03:27.104338
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('foo')
    get_parent(tree, tree.body[0].value)



# Generated at 2022-06-14 03:03:31.860137
# Unit test for function find
def test_find():
    tree = ast.parse("""if True:
                        a = 1
                        print(a)
                    """)
    for node in find(tree, ast.Name):
        print(node)

# Generated at 2022-06-14 03:03:36.574033
# Unit test for function find
def test_find():
    tree = ast.parse('import abc\nabc.abstractclassmethod')

    assert(list(find(tree, ast.Import)) == [tree.body[0]])
    assert(list(find(tree, ast.Name)) == [tree.body[1].value.func,
                                          tree.body[1].value.func.value.attr])



# Generated at 2022-06-14 03:03:42.178169
# Unit test for function replace_at
def test_replace_at():
    def f():
        pass

    tree = ast.parse(f)
    print(ast.dump(tree))
    f_expr = tree.body[0]
    print(replace_at(0, tree, ast.parse("def g(): pass")))
    print(ast.dump(tree))


if __name__ == '__main__':
    test_replace_at()

# Generated at 2022-06-14 03:03:48.599192
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest.mock as mock
    import typed_ast.ast3 as ast
    from types import FunctionType

    import mutpy

    def test_function():
        return 3

    tree = ast.parse(FunctionType.__code__)

    mutpy.utils.get_closest_parent_of(tree, tree.body[0], ast.FunctionDef)

    mock.call(tree.body[0])



# Generated at 2022-06-14 03:03:55.745351
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node = ast.parse('''
    def a():
        b()
    if a():
        print(123)
    ''')
    if_stmt = get_closest_parent_of(node, node.body[1].body[0], ast.If)
    assert isinstance(if_stmt, ast.If)
    assert isinstance(get_closest_parent_of(node, node.body[0], ast.If), ast.FunctionDef)
    assert isinstance(get_closest_parent_of(node, node.body[1], ast.If), ast.Module)

# Generated at 2022-06-14 03:03:59.692481
# Unit test for function get_parent
def test_get_parent():
    class TestNode(ast.AST):
        _fields = ()
    code = '''
    def foo():
        pass
    '''
    tree = ast.parse(code)
    node = TestNode()
    assert get_parent(tree, node) == tree

# Generated at 2022-06-14 03:04:11.244599
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest

    # TODO: Generate a tree, where functions has a body,
    # TODO: and test it
    class TestNode(ast.AST):
        _fields = ['body']

    class TestTree(ast.AST):
        _fields = ['node', 'body']

    class TestModule(ast.AST):
        _fields = ['body']

    node = TestTree(TestNode())
    body = [
        node,
        TestNode(),
        TestTree(node),
        node,
        TestNode(),
        node,
    ]

    tree = TestModule([
        TestTree(body=body),
        node,
    ])

    node = find(tree, TestTree).__next__()
    assert node is get_closest_parent_of(tree, node, TestModule)

# Generated at 2022-06-14 03:04:15.470938
# Unit test for function find
def test_find():
    # test with returned type
    ret = find(ast.parse('a = "a"; b = "b"'), ast.Assign)
    assert isinstance(ret, list)
    assert isinstance(ret[0], ast.Assign)

# Generated at 2022-06-14 03:04:19.292988
# Unit test for function find
def test_find():
    test_tree = ast.parse("""
    def foo():
        pass
    """).body[0]
    pass_count = 0

    for pass_node in find(test_tree, ast.Pass):
        pass_count += 1

    assert pass_count == 1

# Generated at 2022-06-14 03:04:23.273650
# Unit test for function find
def test_find():
    a = ast.parse("a = 3")
    nodes = list(find(a, ast.Assign))
    assert nodes[0].value.n == 3



# Generated at 2022-06-14 03:04:30.266153
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse('f()')
    fbody = tree.body
    x = ast.Name('x')
    replace_at(0, fbody, x)
    assert ast.dump(tree) == '<_ast.Module object at 0x7fe89a8f14e0>'

# Generated at 2022-06-14 03:04:35.822049
# Unit test for function get_parent
def test_get_parent():
    import unittest
    import astunparse
    unittest.main(modulename='astgen.modifiers_ast.test_get_parent', exit=False)


if __name__ == '__main__':
    my_ast = ast.parse("""def func():\n  return 1""")
    my_return = my_ast.body[0].body[0]
    assert astunparse.unparse(get_parent(my_ast, my_return)) == 'def func():\n  return 1'

# Generated at 2022-06-14 03:04:43.815387
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("foo()")
    assert isinstance(get_closest_parent_of(tree, tree.body[0], ast.FunctionDef), ast.FunctionDef)
    assert isinstance(get_closest_parent_of(tree, tree.body[0], ast.Module), ast.Module)
    assert isinstance(get_closest_parent_of(tree, tree.body[0].value, ast.FunctionDef), ast.FunctionDef)
    assert isinstance(get_closest_parent_of(tree, tree.body[0].value, ast.Module), ast.Module)


# Generated at 2022-06-14 03:04:55.476081
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('''
    a = 1
    b = 2
    def c():
        d = 3
        e()
        f = 5''')
    n = ast.parse('f = 5')
    output = get_non_exp_parent_and_index(tree, n.body[0])
    assert output[0].body[2] == n.body[0]
    assert output[1] == 2



# Generated at 2022-06-14 03:05:03.387235
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from . import parse_ast

    tree = parse_ast('''
    def random_func(a: int) -> bool:
        if a == 1:
            print('A')
            return True
        else:
            print('B')
            return False
    ''')

    assert isinstance(get_closest_parent_of(tree, tree.body[0].body[0].body[1],
                      ast.FunctionDef), ast.FunctionDef)
    assert isinstance(get_closest_parent_of(tree, tree.body[0].body[0],
                      ast.FunctionDef), ast.FunctionDef)
    assert isinstance(get_closest_parent_of(tree, tree.body[0],
                      ast.Module), ast.Module)

# Generated at 2022-06-14 03:05:07.742269
# Unit test for function find
def test_find():
    import astor
    ast1 = ast.parse('def func(): pass')
    assert list(find(ast1, ast.FunctionDef))
    

if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:05:12.460452
# Unit test for function insert_at
def test_insert_at():
    parent = ast.Module()
    insert_at(0, parent, ast.Expr(ast.Num(1)))
    assert parent.body[0] == ast.Expr(ast.Num(1))
    ast.fix_missing_locations(parent)



# Generated at 2022-06-14 03:05:14.934666
# Unit test for function find
def test_find():
    def f1():
        pass

    func = find(ast.parse(f1.__code__), ast.FunctionDef)
    print(func)

# Generated at 2022-06-14 03:05:18.442310
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert ast.parse('[print("test1")]').body[0].body[0] == get_non_exp_parent_and_index(ast.parse('[print("test1")]'), ast.parse('[print("test1")]').body[0].body[0])[0].body[0]



# Generated at 2022-06-14 03:05:23.537885
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest

    class TestFindParentOf(unittest.TestCase):
        def test_simple_function(self):
            tree = ast.parse('''
            def simple_function(arg):
                pass
            ''')
            node = ast.parse('pass').body[0]
            parent = get_closest_parent_of(tree, node, ast.FunctionDef)
            self.assertEqual(parent.name, 'simple_function')

    unittest.main()

# Generated at 2022-06-14 03:05:32.656214
# Unit test for function find
def test_find():
    tree = ast.parse("""
if True:\n
    print('hello')""")

    print(tree)
    print(list(find(tree, ast.Name)))
    assert list(find(tree, ast.Name)) == [ast.Name('True', ast.Load())]
    assert list(find(tree, ast.Expr)) == [ast.Expr(ast.Call(ast.Name('print',
                                                                     ast.Load()),
                                                           [ast.Str('hello')], [])),
                                          ast.Name('True', ast.Load())]


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:05:33.253349
# Unit test for function find

# Generated at 2022-06-14 03:05:37.906173
# Unit test for function find
def test_find():
    import astor
    source = '''def foo():
        x = 4

        def bar():
            x = 5
            if x:
                return x
    '''

    tree = ast.parse(source)

    for item in find(tree, ast.FunctionDef):
        print(astor.dump_tree(item))


# Generated at 2022-06-14 03:05:43.126489
# Unit test for function replace_at
def test_replace_at():
    pass

# Generated at 2022-06-14 03:05:47.957737
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    source = """
    foo = 'foo'
    foo.replace('f', 'b')
    """
    tree = ast.parse(source)
    foo = find(tree, ast.Name).__next__()
    assert isinstance(get_closest_parent_of(tree, foo, ast.Assign), ast.Assign)
    assert isinstance(get_closest_parent_of(tree, foo, ast.Attribute),
                      ast.Attribute)

test_get_closest_parent_of()

# Generated at 2022-06-14 03:05:51.160170
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    tree = ast.parse('x=42;y=4')

    for node in find(tree, ast.Assign):
        assert isinstance(node.value, ast.Num)

# Generated at 2022-06-14 03:05:59.112431
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    import astunparse
    import statistics
    import sys

    from . import ast_utils

    # Setup main args
    main_args = sys.argv
    if len(main_args) < 4:
        print("Usage: python3 {} <repair.py> <script> <output>"
              .format(main_args[0]))
        exit(1)

    # Setup script args
    script_args = sys.argv[2].split(" ")
    if len(script_args) < 4:
        print("Usage: python3 {} <repair.py> <script> <output>"
              .format(main_args[0]))
        exit(1)

    repair_file = script_args[0]
    script = script_args[1]
    output = script_args[2]
   

# Generated at 2022-06-14 03:06:14.466510
# Unit test for function find
def test_find():
    source = '''
from sys import platform
if platform == "win32":
    # True for Windows/Cygwin
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    # UNIX
    import tty
    import termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
'''
    tree = ast.parse(source)

    # Test by module

# Generated at 2022-06-14 03:06:21.983085
# Unit test for function find
def test_find():
    tree = ast.parse("""
        def f():
            pass
    """)

    # Test simple search of function
    assert (next(iter(find(tree, ast.FunctionDef)))) == tree.body[0]

    # Test search of Name from inside function
    # TODO: add in test node of inner function
    assert (next(iter(find(tree, ast.Name)))) == tree.body[0].body[0].value

# Generated at 2022-06-14 03:06:30.667020
# Unit test for function find
def test_find():
    string = """
if True:
    if False:
        print('')
    else:
        while True:
            pass
        else:
            pass
    finally:
        print('')
else:
    pass"""

    tree = ast.parse(string)
    ifs = list(find(tree, ast.If))

    assert ifs[0].test.value.id == 'True'
    assert ifs[1].test.value.id == 'False'
    assert ifs[2].test.value.id == 'True'
    assert ifs[3].test.value.id == 'False'



# Generated at 2022-06-14 03:06:36.654048
# Unit test for function find
def test_find():
    exp = ast.parse('a=5').body[0]  # type Assign
    a = find(exp, ast.Name)
    b = find(exp, ast.Assign)

    assert list(a) == [exp.targets[0]]
    assert list(b) == [exp]

# Generated at 2022-06-14 03:06:48.144359
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    '''
    test for function get_closest_parent_of
    :return: None
    '''
    # The test node
    arg_name = ast.Num(n=2)

    # The test tree

# Generated at 2022-06-14 03:06:57.196237
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    cls = ast.ClassDef()
    cls.body = [
        ast.FunctionDef(),
        ast.FunctionDef(),
        ast.FunctionDef(),
    ]

    # If it is the same function, return it
    assert cls.body[0] == get_closest_parent_of(cls, cls.body[0], ast.FunctionDef)

    # If it is it's parent, return it
    assert cls == get_closest_parent_of(cls, cls.body[0], ast.ClassDef)

    # If it is the closest parent, return it
    assert cls.body[0] == get_closest_parent_of(cls, cls.body[0].body[0], ast.FunctionDef)

    # If it is not in the tree, raise NodeNotFound

# Generated at 2022-06-14 03:07:13.927952
# Unit test for function find
def test_find():
    assert [x.value for x in find(ast.parse('a = 1 + 2'), ast.Name)] == ['a']

    code = '''
        def frobnicate(num):
            return num * 2 + 1

        print(frobnicate(1))
        print(frobnicate(2))
        print(frobnicate(3))
        '''

    tree = ast.parse(code)

    assert [x.id for x in find(tree, ast.Name)] == ['frobnicate', 'num', 'num',
                                                    'frobnicate', 'num', 'num',
                                                    'frobnicate', 'num']

# Generated at 2022-06-14 03:07:25.201491
# Unit test for function get_parent
def test_get_parent():
    import sys
    import os

    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    from typedpyco.parser import parse_source, get_tree
    from typedpyco import Visitor

    source = '''
    def f():
        1 + 2 + 3
    '''

    tree = get_tree(source)

    class GetParentVisitor(Visitor):
        def visit_BinOp(self, node):
            assert get_parent(tree, node) == get_parent(tree, node)
            assert get_parent(tree, node) == node.left.parent

    GetParentVisitor().visit(tree)

# Generated at 2022-06-14 03:07:25.876085
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:07:29.805127
# Unit test for function find
def test_find():
    tree = ast.parse("""
a = 1
b = a + 2
c = b * 3
""")
    finds = list(find(tree, ast.Assign))
    assert len(finds) == 3



# Generated at 2022-06-14 03:07:34.889235
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Test get_closest_parent_of function."""
    tree = ast.parse('bar = [1, 2, 3, 4, 5]')
    node = find(tree, ast.Num).__next__()

    assert isinstance(get_closest_parent_of(tree, node, ast.ListComp),
                      ast.ListComp)
    assert isinstance(get_closest_parent_of(tree, node, ast.Module),
                      ast.Module)

# Generated at 2022-06-14 03:07:39.350531
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    parent = ast.parse('if a: b()')
    func = parent.body[0].body[0]

    assert isinstance(func, ast.Expr)
    assert isinstance(get_closest_parent_of(parent, func, ast.If), ast.If)

# Generated at 2022-06-14 03:07:45.458000
# Unit test for function replace_at
def test_replace_at():
    node_to_replace = ast.FunctionDef(
        'test',
        ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[],
                      kwarg=None, defaults=[]),
        body=[
            ast.Expr(
                ast.Call(func=ast.Name(id='print', ctx=ast.Load()),
                         args=[ast.Str(s='Hello World')],
                         keywords=[], starargs=None, kwargs=None)
            )
        ],
        decorator_list=[],
        returns=None
    )

    node_tree = ast.Module(body=[node_to_replace])


# Generated at 2022-06-14 03:07:56.593801
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class A: pass

    class B: pass

    class C: pass

    class D: pass

    class E: pass

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    tree = [a, b, c, d, e]
    _parents[a] = tree
    _parents[b] = tree
    _parents[c] = tree
    _parents[d] = tree
    _parents[e] = tree

    assert get_closest_parent_of(tree, b, A) == a
    assert get_closest_parent_of(tree, b, C) == c
    assert get_closest_parent_of(tree, b, D) == d

# Generated at 2022-06-14 03:08:03.616795
# Unit test for function get_parent
def test_get_parent():
    ctx = ast.parse('a = 4 + 5\n')
    _build_parents(ctx)
    assert(get_parent(ctx, ctx.body[0]).__class__ == ast.Module)
    assert(get_parent(ctx, ctx.body[0].value).__class__ == ast.Assign)
    assert(get_parent(ctx, ctx.body[0].value.left).__class__ == ast.Assign)
    assert(get_parent(ctx, ctx.body[0].value.right).__class__ == ast.Assign)


# Generated at 2022-06-14 03:08:12.987197
# Unit test for function find
def test_find():
    code = 'foo(1+2, 3+4)'
    tree = ast.parse(code)
    exp_nodes = list(find(tree, ast.Expr))
    assert len(exp_nodes) == 2
    assert code[exp_nodes[0].col_offset:exp_nodes[0].col_offset+7] == '1+2, 3'
    assert code[exp_nodes[1].col_offset:exp_nodes[1].col_offset+3] == '3+4'


# Generated at 2022-06-14 03:08:31.274006
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """ Unit test for function get_non_exp_parent_and_index """

    exp_parent = ast.FunctionDef(name="TestFun", body=[ast.Expr(value=ast.Call(func=ast.Name(id="TestFun2"), args=[], keywords=[]))], decorator_list=[], returns=None)
    exp_parent2 = ast.Module(body=[exp_parent])
    _build_parents(exp_parent2)
    node = ast.Call(func=ast.Name(id="TestFun2"), args=[], keywords=[])
    assert get_non_exp_parent_and_index(exp_parent2, node)[0] == exp_parent
    assert get_non_exp_parent_and_index(exp_parent2, node)[1] == 0

# Generated at 2022-06-14 03:08:32.878763
# Unit test for function find
def test_find():
    import unittest as ut
    from ..parser import py2ast, ast2py


# Generated at 2022-06-14 03:08:36.602015
# Unit test for function find
def test_find():
    tree = ast.parse("""
        def foo():
            if True:
                return
                a = 0
                pass
            else:
                b = 1
    """)
    nodes = find(tree, ast.FunctionDef)
    assert isinstance(next(nodes), ast.FunctionDef)



# Generated at 2022-06-14 03:08:40.442741
# Unit test for function get_parent
def test_get_parent():
    # TODO: skip this test
    import sys
    if sys.version_info < (3, 6):
        return
    import astor

    node = astor.to_source(ast.parse('def foo():\n\tpass')).strip()
    node = astor.parse_file(node)
    parent = get_parent(node, node)
    assert parent == node.body[0]

# Generated at 2022-06-14 03:08:43.614324
# Unit test for function find
def test_find():
    tree = ast.parse('def foo(): a = 2; b = 2')
    assert find(tree, ast.FunctionDef)
    assert find(tree, ast.Assign)
    assert find(tree, ast.Name)

# Generated at 2022-06-14 03:08:52.747252
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse(
        """
        x = 1
        y = 2
        if x == 1:
            x += 1
        else:
            y += 1
    """
    )
    non_exp_parent, index = get_non_exp_parent_and_index(
        tree, tree.body[0].value)
    assert isinstance(non_exp_parent, ast.Module)
    assert index == 0
    non_exp_parent, index = get_non_exp_parent_and_index(
        tree, tree.body[1].value)
    assert isinstance(non_exp_parent, ast.Module)
    assert index == 1
    non_exp_parent, index = get_non_exp_parent_and_index(
        tree, tree.body[2].body[0])

# Generated at 2022-06-14 03:08:56.738896
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    parent = ast.parse('a = 1\nfunc(a)').body[1]
    node = parent.args[0]
    n, i = get_non_exp_parent_and_index(parent, node)
    assert(n == parent)
    assert(i == 0)

# Generated at 2022-06-14 03:09:02.985138
# Unit test for function find
def test_find():
    tree = ast.parse("def foo(a, b, c=4, *args, **kwargs):\n"
                     "    pass")
    assert len(list(find(tree, ast.FunctionDef))) == 1  # type: ignore
    assert len(list(find(tree, ast.arguments))) == 1  # type: ignore


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:09:04.292836
# Unit test for function find

# Generated at 2022-06-14 03:09:12.641633
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .faux_nodes import ModuleNode
    from .faux_nodes import FunctionNode
    from .faux_nodes import AssignNode

    module = ModuleNode(body=[
        FunctionNode(body=[
            AssignNode(value="1 + 1")
        ])
    ])

    # find the FuncDef node
    funcdef = get_closest_parent_of(module, module.body[0][0], ast.FunctionDef)
    assert isinstance(funcdef, ast.FunctionDef)

    # find Assign node
    assign = get_closest_parent_of(module, module.body[0][0], ast.Assign)
    assert isinstance(assign, ast.Assign)

    # find Name node