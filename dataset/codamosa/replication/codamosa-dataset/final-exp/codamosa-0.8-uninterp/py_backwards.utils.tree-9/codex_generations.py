

# Generated at 2022-06-14 03:01:36.912038
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    module = ast.parse('x = 5\ny = x + 1\n')
    test_node = module.body[1].value
    result = get_closest_parent_of(module, test_node, ast.Module)
    assert result == module

# Generated at 2022-06-14 03:01:40.745825
# Unit test for function find
def test_find():
    body = ast.parse('class Foo():\n\tdef method(self):\n\t\tpass').body
    parent = body[0]
    assert len(list(find(parent, ast.FunctionDef))) == 1

# Generated at 2022-06-14 03:01:47.986667
# Unit test for function get_parent
def test_get_parent():
    '''
    Test get_parent()
    '''
    py_source = '''
        def foo():
            bar()
    '''
    tree = ast.parse(py_source)
    func_def = tree.body[0]
    call = func_def.body[0]

    parent = get_parent(tree, func_def)
    assert parent == tree
    parent = get_parent(tree, call)
    assert parent == func_def

    Python_source = '''
        class Foo:
            def bar(self):
                pass
    '''
    tree = ast.parse(py_source)
    class_def = tree.body[0]
    method_def = class_def.body[0]
    pass_stmt = method_def.body[0]


# Generated at 2022-06-14 03:01:53.936057
# Unit test for function replace_at
def test_replace_at():
    root_node = ast.FunctionDef(name='f1', body=[ast.Pass()], args=ast.arguments(), decorator_list=[])
    insert_node = ast.Try([ast.Pass()])
    replace_at(0, root_node, insert_node)
    assert(isinstance(root_node.body[0], ast.Try))

# Generated at 2022-06-14 03:01:56.650633
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("def foo(): pass")
    assert get_parent(tree, tree.body[0].body[0]) == tree.body[0]



# Generated at 2022-06-14 03:02:01.032876
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("""
        def func():
            # comment
            pass
    """)
    closest_parent = get_closest_parent_of(tree, tree.body[0].body[0],
                                           ast.FunctionDef)
    assert isinstance(closest_parent, ast.FunctionDef)
    assert closest_parent.name == 'func'

# Generated at 2022-06-14 03:02:08.177431
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    lines = ['def func(a, b):',
             '  t = a + b',
             '  return t']
    tree = ast.parse('\n'.join(lines))

    # Find "t" node
    t = get_closest_parent_of(tree,
                              ast.parse('a + b').body[0].value,
                              ast.Name)

    non_exp_parent, index = get_non_exp_parent_and_index(tree, t)

    assert isinstance(non_exp_parent, ast.FunctionDef)
    assert index == 1

# Generated at 2022-06-14 03:02:17.869531
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class Module(ast.AST):
        _fields = ('body',)
        body = []

    class ClassDef(ast.AST):
        _fields = ('body',)
        body = []

    class FunctionDef(ast.AST):
        _fields = ('body',)
        body = []

    class Expr(ast.AST):
        _fields = ('value',)
        value = None

    module = Module()
    klass = ClassDef(name='test')
    func = FunctionDef(name='test')
    expr = Expr()

    module.body.append(klass)  # type: ignore
    klass.body.append(func)    # type: ignore
    func.body.append(expr)     # type: ignore

    _build_parents(module)

    assert get_non_exp_parent_and_

# Generated at 2022-06-14 03:02:22.141482
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """test_get_closest_parent_of."""
    # TODO: implement unit test for function get_closest_parent_of
    assert True

# Generated at 2022-06-14 03:02:33.420674
# Unit test for function replace_at
def test_replace_at():
    from typed_ast import ast3 as ast

    parent = ast.Module(body=[ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int', ctx=ast.Load()), value=ast.Num(n=0), simple=1), ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=0)), ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=0))])
    node = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=0))

# Generated at 2022-06-14 03:02:40.489684
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from .test_utils import test_module
    tree = test_module('a = 0')
    parent_index = get_non_exp_parent_and_index(tree, tree.body[0].value)
    assert parent_index[0].body[0] is tree.body[0]
    assert parent_index[1] == 0

# Generated at 2022-06-14 03:02:49.961199
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    test_code = """
    def foo(a):
        if a:
            return 1
    """

    test_ast = ast.parse(test_code)
    _build_parents(test_ast)

    parent, index = get_non_exp_parent_and_index(test_ast, test_ast.body[0])

    assert parent is test_ast
    assert index == 0

    parent, index = get_non_exp_parent_and_index(test_ast, test_ast.body[0].body[0])
    assert parent is test_ast.body[0]
    assert index == 0

# Generated at 2022-06-14 03:02:53.973033
# Unit test for function get_parent
def test_get_parent():
    assert get_parent(ast.parse('a = 1 + 1'),
                      ast.parse('a = 1 + 1').body[0], True) == ast.parse('a = 1+1')


# Generated at 2022-06-14 03:03:01.885954
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:03:05.965436
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(ast.parse('x = 1 + 2'), ast.parse('2'), ast.Module) == ast.parse('x = 1 + 2')

# Generated at 2022-06-14 03:03:07.227490
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:03:08.144781
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:03:12.605336
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('for i in range(5): pass')
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0])
    assert isinstance(parent, ast.For)
    assert index == 0

# Generated at 2022-06-14 03:03:16.035183
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..parser import parse_ast

    tree = parse_ast(
        '''
        def f(x: int) -> int:
            return x + 1
        '''
    )
    parent = get_closest_parent_of(tree, tree.body[0].body[0].value, ast.FunctionDef)
    assert parent.name == 'f'


# Generated at 2022-06-14 03:03:16.600660
# Unit test for function get_parent

# Generated at 2022-06-14 03:03:24.740000
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astor as p

# Generated at 2022-06-14 03:03:25.978167
# Unit test for function find
def test_find():
    import astor
    from . import parse


# Generated at 2022-06-14 03:03:33.043731
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    test_ast = astor.parse_file(unittest.__file__)
    actual = get_closest_parent_of(test_ast, test_ast.body[0], type(ast.Module))
    assert(isinstance(actual, ast.Module))
    # print(astor.dump_tree(actual))

# Generated at 2022-06-14 03:03:37.250845
# Unit test for function find
def test_find():
    code = 'def func(x): return x + 20'
    tree = ast.parse(code)

    assert all(True for _ in find(tree, ast.Num))

    code = 'def func(x):    return x + 20'
    tree = ast.parse(code)

    assert all(True for _ in find(tree, ast.Name))

# Generated at 2022-06-14 03:03:39.095433
# Unit test for function find
def test_find():
    import ast
    import astrid


# Generated at 2022-06-14 03:03:43.150909
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('''
    def zzz():
        @decorator
        def foo():
            x = 3
            return x + 1

    def bar():
        return 2
    ''')

    non_exp_parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0].body[-1])
    assert isinstance(non_exp_parent, ast.FunctionDef)
    assert index == 2

    non_exp_parent, index = get_non_exp_parent_and_index(tree, tree.body[1].body[-1])
    assert isinstance(non_exp_parent, ast.Module)
    assert index == 1

# Generated at 2022-06-14 03:03:53.120981
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    exp_tree = ast.parse("""
    class Test():
        def foo():
            bar()
    """)
    _, index = get_non_exp_parent_and_index(exp_tree, exp_tree.body[0])
    assert index == 0
    _, index = get_non_exp_parent_and_index(exp_tree, exp_tree.body[0].body[0])
    assert index == 0
    _, index = get_non_exp_parent_and_index(exp_tree, exp_tree.body[0].body[0].body[0])
    assert index == 0
    _, index = get_non_exp_parent_and_index(exp_tree, exp_tree.body[0].body[0].body[0].value)
    assert index == 0

# Generated at 2022-06-14 03:04:00.848723
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    # Test with Module
    tree = ast.parse("""
    a = 2
    """)
    node = tree.body[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert isinstance(parent, ast.Module)
    assert index == 0

    # Test with FunctionDef
    tree = ast.parse("""
    def test():
        a = 2
    """)
    node = tree.body[0]
    parent, index = get_non_exp_parent_and_index(tree, node.body[0])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 0

    # Test with If
    tree = ast.parse("""
    if True:
        a = 2
    """)
    node = tree.body[0]
   

# Generated at 2022-06-14 03:04:12.263411
# Unit test for function get_parent
def test_get_parent():

    class C:
        pass

    class C2:
        pass

    class C3:
        pass

    class C4:
        pass

    c = C()
    c2 = C2()
    c3 = C3()
    c4 = C4()
    c5 = C4()

    c.c2 = c2
    c2.c3 = c3
    c3.c4 = c4
    c3.c5 = c5

    assert get_parent(c, c2) == c
    assert get_parent(c, c3) == c2
    assert get_parent(c, c4) == c3
    assert get_parent(c, c5) == c3

    assert get_parent(c, c2, rebuild=True) == c

# Generated at 2022-06-14 03:04:18.646471
# Unit test for function find
def test_find():
    import astor
    t = ast.parse('def f(): return 1+1')
    func = get_closest_parent_of(t, t.body[0].body[0].value, ast.FunctionDef)
    assert func is t.body[0]
    assert func.lineno == 1
    assert func.name == 'f'
    assert astor.to_source(func) == 'def f(): return 1+1\n'

# Generated at 2022-06-14 03:04:35.624192
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node = ast.Name(id='a', ctx=ast.Store())

    # Should return FunctionDef node
    assert isinstance(get_closest_parent_of(ast.parse('def f():\n    a'), node,
                                            ast.FunctionDef),
                      ast.FunctionDef)

    # Should return ClassDef node
    assert isinstance(get_closest_parent_of(ast.parse('class A:\n    a'), node,
                                            ast.ClassDef),
                      ast.ClassDef)

    # Should return ast.Module node
    assert isinstance(get_closest_parent_of(ast.parse('a'), node,
                                            ast.Module),
                      ast.Module)


# Generated at 2022-06-14 03:04:43.451324
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    data = """
        def fn():
            pass
    """
    tree = ast.parse(data)
    body = tree.body[0].body

    # Test for def node of function fn
    def_node = find(tree, ast.FunctionDef).__next__()
    assert get_non_exp_parent_and_index(tree, def_node) == (tree, 0)

    # Test for pass node of function fn
    pass_node = find(tree, ast.Pass).__next__()
    assert get_non_exp_parent_and_index(tree, pass_node) == (body, 0)

# Generated at 2022-06-14 03:04:56.797967
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class MyNode(ast.AST):
        _fields = ()
    # Generate AST
    v = ast.Name(id='v', ctx=ast.Load())
    v_assign = ast.Assign(targets=[v], value=ast.Num(n=3))
    function_name = 'foo'
    function_name_node = ast.Name(id=function_name, ctx=ast.Load())
    function_body = [v_assign, MyNode()]
    function_def = ast.FunctionDef(name=function_name, args=ast.arguments(
        args=[], vararg=None, kwonlyargs=[], kwarg=None, defaults=[],
        kw_defaults=[]), body=function_body, decorator_list=[],
        returns=None)

# Generated at 2022-06-14 03:04:58.418182
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:05:08.497464
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from ..exceptions import NodeNotFound
    from .test_gen import parse

    code = """
    function = lambda: x
    function()
    """

    tree = parse(code)
    func = tree.body[0].value  # type: ignore
    parent, index = get_non_exp_parent_and_index(tree, func)
    if not isinstance(parent, ast.Module):
        raise AssertionError('Tree root is not a module')
    if index != 0:
        raise AssertionError('Index is not 0')

    func = tree.body[1].value  # type: ignore
    parent, index = get_non_exp_parent_and_index(tree, func)
    if not isinstance(parent, ast.Module):
        raise AssertionError('Tree root is not a module')
   

# Generated at 2022-06-14 03:05:12.520521
# Unit test for function find
def test_find():
    expr = ast.parse('a == 2', mode='eval')
    nodes = find(expr, ast.Compare)

    for node in nodes:
        assert isinstance(node, ast.Compare)



# Generated at 2022-06-14 03:05:17.762786
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse(
        'def a(b):\n'
        '    return b + 2\n'
        'a(2)')

    assert get_non_exp_parent_and_index(tree, tree.body[0].body[0]) == \
        (tree, 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].body) == \
        (tree, 0)



# Generated at 2022-06-14 03:05:19.826341
# Unit test for function find
def test_find():
    from ..utils import parse
    code = '''
    def func():
        pass
    '''
    node = parse(code)
    print(list(find(node, ast.FunctionDef)))

# Generated at 2022-06-14 03:05:23.456931
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    sibling = ast.Expr(ast.Name('x'))
    expr = ast.Expr(ast.Call(ast.Name('f'), [], []))
    parent = ast.Module([sibling, expr])
    assert (get_non_exp_parent_and_index(parent, expr) ==
            (parent, 1))



# Generated at 2022-06-14 03:05:31.611334
# Unit test for function replace_at
def test_replace_at():
    """Test for function replace_at to make sure it works as expected."""
    parent = ast.parse('''
        def fn(func):
            def wrapper(a, b):
                print(1)
            return wrapper
        ''').body[0]

    nodes = ast.parse('''
        def fn(func):
            def wrapper(a, b):
                print(1)
                func(a, b)
                print(2)
            return wrapper
        ''').body[0]

    replace_at(1, parent, nodes)


test_replace_at()

# Generated at 2022-06-14 03:05:47.210044
# Unit test for function replace_at
def test_replace_at():
    """Run test for function replace_at."""
    import textwrap
    import unittest
    from ..nodes import nodes_equal
    from ..to_source import to_source
    from ..visitors.visitor import visit

    class TestReplaceAt(unittest.TestCase):
        def test_add_in_init(self):
            """Test of replacement in function init."""
            code = textwrap.dedent(
                """\
                class Example:
                    def __init__(self, num):
                        self.num = num
                """)
            tree = visit(code)

            # Find node:
            # self.num = num
            num_node = tree.body[0].body[0].body[0]
            # Find function init node
            init_node = tree.body[0].body[0]

# Generated at 2022-06-14 03:05:56.113140
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .test_suite import Tree
    from .test_suite import ASSIGNMENT_SETUP
    from .test_suite import FUNCTION_SETUP

    tree, program = Tree(ASSIGNMENT_SETUP)
    closest_func = get_closest_parent_of(tree, program, ast.FunctionDef)

    assert isinstance(closest_func, ast.FunctionDef)
    assert closest_func.body[0] == program

    tree, program = Tree(FUNCTION_SETUP)
    closest_body = get_closest_parent_of(tree, program, ast.FunctionDef)

    assert isinstance(closest_body, ast.FunctionDef)
    assert closest_body.body[0] == program



# Generated at 2022-06-14 03:05:57.972502
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:06:13.467426
# Unit test for function replace_at
def test_replace_at():
    import unittest
    import astor

    class TestReplaceAt(unittest.TestCase):
        def test_replace_at(self):
            class_tree = ast.parse(
                "class A: pass\nclass B: pass\nprint('OK')")
            a_class = get_closest_parent_of(class_tree, class_tree.body[0].body[0],
                                            ast.ClassDef)
            b_class = get_closest_parent_of(class_tree, class_tree.body[1].body[0],
                                            ast.ClassDef)
            replace_at(0, class_tree, b_class)
            result_tree = ast.parse(
                "class B: pass\nclass A: pass\nprint('OK')")

# Generated at 2022-06-14 03:06:18.882212
# Unit test for function replace_at
def test_replace_at():
    code = 'a = 42'
    tree = ast.parse(code)

    node = tree.body[0].value
    parent = get_non_exp_parent_and_index(tree, node)[0]

    assert node == ast.Num(n=42, lineno=1, col_offset=9)

    root_const_node = ast.Num(n=1337, lineno=1, col_offset=9)
    lvar_node = ast.Name(id='a', ctx=ast.Store(), lineno=1, col_offset=3)
    assign_node = ast.Assign(targets=[lvar_node],
                             value=root_const_node,
                             lineno=1, col_offset=1)


# Generated at 2022-06-14 03:06:24.698039
# Unit test for function find
def test_find():
    example = ast.parse("""
    while True:
        x = 4
    """)

    assert len(list(find(example, ast.While))) == 1
    assert len(list(find(example, ast.Assign))) == 1

# Generated at 2022-06-14 03:06:29.527006
# Unit test for function find
def test_find():
    from tests.ast_compare import compare_mod
    from ..tests.utils import update_source
    from ..common.structure import py_mod

    tree = ast.parse(update_source(py_mod))

    assert compare_mod(tree, find(tree, ast.Module))

# Generated at 2022-06-14 03:06:32.839523
# Unit test for function find
def test_find():
    """Test whether find works."""
    tree = ast.parse('import typing; x: typing.Tuple[int, float]')
    nodes = list(find(tree, ast.Import))
    assert nodes, 'Find should return non-empty list'
    assert isinstance(nodes[0], ast.Import)



# Generated at 2022-06-14 03:06:35.944467
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(ast.parse("for i in range(1):\n pass"),
                                 ast.parse("for i in range(1):\n pass").body[0].body[0],
                                 ast.For)

# Generated at 2022-06-14 03:06:47.600308
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest

    import core.parser as parser
    from core.parser.utils import get_closest_parent_of

    class Test(unittest.TestCase):
        def test_simple(self):
            tree = parser.parse_string('[1, 2, [3, 4]]')
            node = tree.body[0].value.elts[2]

            self.assertIsInstance(
                get_closest_parent_of(tree, node, ast.Module), ast.Module)
            self.assertIsInstance(
                get_closest_parent_of(tree, node, ast.List), ast.List)

        def test_nested(self):
            tree = parser.parse_string('[1, 2, [3, [4, 5], 6]]')

# Generated at 2022-06-14 03:07:22.424473
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    line1 = ast.parse("main()").body[0]
    line2 = ast.parse("main2()").body[0]
    line3 = ast.parse("main3()").body[0]
    setattr(line1, 'body', [line2, line3])
    parent, index = get_non_exp_parent_and_index(line1, line2)
    assert parent.body[index] == line2
    assert parent == line1

# Generated at 2022-06-14 03:07:30.496761
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Unit test for function get_closest_parent_of."""
    code = '''
if 0: pass
elif 0: pass
else: pass
'''
    root = ast.parse(code)
    elif_node = root.body[0].orelse[0]
    assert isinstance(get_closest_parent_of(root, elif_node, ast.If), ast.If)
    assert isinstance(get_closest_parent_of(root, elif_node, ast.FunctionDef),
                      ast.Module)

# Generated at 2022-06-14 03:07:33.708607
# Unit test for function find
def test_find():
    source = 'test = lambda value: value'
    tree = ast.parse(source)
    tree_changed = find(tree, ast.Lambda)
    assert('lambda value: value' in tree_changed)
    assert('test =' not in tree_changed)


# Generated at 2022-06-14 03:07:34.962110
# Unit test for function replace_at

# Generated at 2022-06-14 03:07:39.387019
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astor
    tree = ast.parse("""if a:
                        b = 'test'""")
    node = tree.body[0].body[0]
    parent, index = get_non_exp_parent_and_index(tree, node)

    assert astor.to_source(parent) == "if a:"

# Generated at 2022-06-14 03:07:44.197306
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = """
    def foo():
        '''
        do something
        '''
        if a:
            pass
        elif b:
            1
        else:
            pass
    """
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if(node.__class__ == ast.Expr):
            assert (get_closest_parent_of(tree, node, ast.If)
                    .__class__ == ast.If)

# Generated at 2022-06-14 03:07:47.401037
# Unit test for function find
def test_find():
    code = """
    a = 1 + 2
    b = a + 2
    """

    tree = ast.parse(code)

    for node in find(tree, ast.Assign):
        print(repr(node))

# Generated at 2022-06-14 03:07:49.916386
# Unit test for function find
def test_find():
    tree = ast.parse("[1,2,3,4]")
    assert list(find(tree, ast.List)) == tree.body



# Generated at 2022-06-14 03:07:50.851760
# Unit test for function find

# Generated at 2022-06-14 03:07:59.967068
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class ParentA(ast.AST):
        pass

    class ParentB(ast.AST):
        pass

    class ParentC(ast.AST):
        pass

    class ChildA(ast.AST):
        pass

    class ChildB(ast.AST):
        pass

    tree = ParentA()
    tree.body = [
        ParentB(),
        ParentC(),
        ChildA(),
        ChildB(),
    ]

    parent = get_closest_parent_of(tree, ChildB(), type_=ParentC)

    assert isinstance(parent, ParentC)

# Generated at 2022-06-14 03:10:29.333452
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # test case 1:
    tree = ast.parse("x = 1")
    node = tree.body[0]
    type_ = ast.Module
    result = get_closest_parent_of(tree, node, type_)
    assert(result.body == tree.body)

    # test case 2:
    tree = ast.parse("x = 1")
    node = tree.body[0]
    type_ = ast.FunctionDef
    result = get_closest_parent_of(tree, node, type_)
    assert(result is None)

# Generated at 2022-06-14 03:10:34.960144
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..parser import parse

    tree = parse('def foo():\n    print(1)\n')
    node = list(find(tree, ast.Call))[0]

    assert isinstance(get_closest_parent_of(tree, node, ast.FunctionDef),
                      ast.FunctionDef)
    assert isinstance(get_closest_parent_of(tree, node, ast.Module), ast.Module)



# Generated at 2022-06-14 03:10:37.654052
# Unit test for function find
def test_find():
    # test tree
    tree = ast.parse('d = 5')

    # find all "Name" nodes
    for node in find(tree, ast.Name):
        print(node.id)
    assert False


# Generated at 2022-06-14 03:10:48.984827
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..exceptions import NodeNotFound
    from_ast = ast.parse("f = a.b(c.d, e.f(g.h, i.j), k.l)")
    f_init = get_closest_parent_of(from_ast, from_ast.body[0].value, ast.Call)
    assert f_init.func.attr == 'b'
    with pytest.raises(NodeNotFound):
        get_closest_parent_of(from_ast, from_ast.body[0].value, ast.Attribute)

# Generated at 2022-06-14 03:10:50.671468
# Unit test for function find

# Generated at 2022-06-14 03:10:54.718776
# Unit test for function get_parent
def test_get_parent():
    import astor
    from ..refactor import transform

    code = '''
    def f():
        def g():
            pass
        pass
    '''
    tree = ast.parse(code)

    tree = transform(tree, [('body_for_node', 'name', 'f', 'g')])
    # print(astor.to_source(tree))

    node = get_closest_parent_of(tree, tree.body[0].body[0], ast.FunctionDef)
    assert node.name == 'g'

# Generated at 2022-06-14 03:10:55.881143
# Unit test for function find
def test_find():
    import astor

# Generated at 2022-06-14 03:11:02.916455
# Unit test for function find
def test_find():
    tree = ast.parse("class Test: def a(self): pass")
    for node in find(tree, ast.ClassDef):
        assert isinstance(node, ast.ClassDef)
    for node in find(tree, ast.FunctionDef):
        assert isinstance(node, ast.FunctionDef)

# Generated at 2022-06-14 03:11:10.045356
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    def func(arg1, arg2):
        arg2 = arg2.f1
        arg2.f1 = arg1
    tree = ast.parse(inspect.getsource(func))
    node = tree.body[0].body[1].value.f1
    closest_parent_of_Assign = get_closest_parent_of(tree, node, ast.Assign)
    assert(closest_parent_of_Assign.targets[0].id == 'arg2')

# Generated at 2022-06-14 03:11:26.703949
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    source = ast.parse(
        """
    def foo():
        a = [1, 2]
        b = a[0]
    """
    )
