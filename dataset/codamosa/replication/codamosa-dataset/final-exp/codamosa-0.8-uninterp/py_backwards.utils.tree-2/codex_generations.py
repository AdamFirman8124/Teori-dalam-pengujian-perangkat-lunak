

# Generated at 2022-06-14 03:01:39.924144
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('a = 1')
    test = tree.body[0]
    parent = get_non_exp_parent_and_index(tree, test)
    assert parent[0] == tree
    assert parent[1] == 0

assert __name__ != "__main__", test_get_non_exp_parent_and_index()

# Generated at 2022-06-14 03:01:42.858601
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert get_non_exp_parent_and_index(
        ast.parse('a = 1 if a > 2 else 5'),
        ast.parse('a > 2').body[0]) == (ast.parse('a = 1 if a > 2 else 5'), 1)

# Generated at 2022-06-14 03:01:49.586145
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from . import ast2py
    print(get_closest_parent_of(ast2py('(1, (2,), 3, 4), 5'), ast2py('(2,)'), ast.Tuple))
    return get_closest_parent_of(ast2py('(1, (2,), 3, 4), 5'), ast2py('(2,)'), ast.Tuple)

# Generated at 2022-06-14 03:01:50.822967
# Unit test for function get_parent

# Generated at 2022-06-14 03:01:54.826588
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .visitor import walk
    from .parser import parse_code


# Generated at 2022-06-14 03:01:59.627411
# Unit test for function find
def test_find():
    with open('../test/test.py', 'r') as f:
        tree = ast.parse(f.read())

    results = find(tree, ast.Name)
    assert len(list(results)) == 4

# Generated at 2022-06-14 03:02:00.980017
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pass



# Generated at 2022-06-14 03:02:03.497709
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    mod = ast.parse('(1 + 2) * 3')
    assert get_non_exp_parent_and_index(mod, mod.body[0].value) == (mod, 0)



# Generated at 2022-06-14 03:02:18.004633
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor

# Generated at 2022-06-14 03:02:18.768583
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:02:27.400610
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('a(1) + b(2)')
    assert isinstance(get_closest_parent_of(tree, tree.body[0].value.args[0],
                                            ast.Expression), ast.Expression)
    assert isinstance(get_closest_parent_of(tree, tree.body[0].value.args[0],
                                            ast.Module), ast.Module)

# Generated at 2022-06-14 03:02:36.204143
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import typed_ast.ast3 as ast

    func_def = ast.FunctionDef(name='some_function',
                               decorator_list=[],
                               args=ast.arguments(
                                   args=[],
                                   vararg=None,
                                   kwonlyargs=[],
                                   kw_defaults=[],
                                   kwarg=None,
                                   defaults=[]
                               ),
                               body=[
                                   ast.Pass()
                               ],
                               returns=None,
                               type_comment=None)

    parent, index = get_non_exp_parent_and_index(func_def, func_def.body[0])
    assert parent == func_def
    assert index == 0


# Generated at 2022-06-14 03:02:45.315960
# Unit test for function replace_at
def test_replace_at():
    import copy
    tree = ast.parse("3 + 2")
    tree_copy = copy.deepcopy(tree)
    parent = get_parent(tree, tree.body[0])
    assert(parent)
    assert(len(parent.body) == 1)
    replace_at(0, parent, ["4"])
    parent = get_parent(tree, tree.body[0])
    assert(len(parent.body) == 1)
    replace_at(0, parent, ["4", "4"])
    parent = get_parent(tree, tree.body[0])
    assert(len(parent.body) == 2)
    replace_at(1, parent, ["1"])
    parent = get_parent(tree, tree.body[1])
    assert(len(parent.body) == 2)

# Generated at 2022-06-14 03:02:48.496405
# Unit test for function find
def test_find():
    assert len(list(find(ast.parse('from distutils.core import setup'),
                         ast.Import))) == 1



# Generated at 2022-06-14 03:02:56.437510
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = '''
        a = 1
        b = 2

        def func():
            return a + b
    '''

    module = ast.parse(code)
    node = module.body[2].body[0].body[0]

    assert get_closest_parent_of(module, node, ast.Module) == module
    assert get_closest_parent_of(module, node, ast.FunctionDef) == \
        module.body[2]



# Generated at 2022-06-14 03:03:09.451203
# Unit test for function find
def test_find():
    import ast
    import astunparse
    tree = ast.parse("""def test():\n    if True:\n        True\n    return 10""")
    print(astunparse.unparse(tree))
    nodes = list(find(tree, ast.Return))
    assert len(nodes) == 1
    assert nodes[0].value.n == 10
    nodes = list(find(tree, ast.Load))
    assert len(nodes) == 3
    assert [x.id for x in nodes] == ['True', 'True', 'Return']
    print(astunparse.unparse(nodes[0]))
    print(astunparse.unparse(nodes[1]))
    print(astunparse.unparse(nodes[2]))

# Generated at 2022-06-14 03:03:10.618167
# Unit test for function find
def test_find():
    # TODO: add test
    pass

# Generated at 2022-06-14 03:03:16.772482
# Unit test for function find
def test_find():
    from .builders import build_simple

    simple = build_simple()
    assert list(find(simple, ast.Name)) == find(simple, 'Name') == \
           [ast.Name(id='c', ctx=ast.Load()), ast.Name(id='a', ctx=ast.Load()),
            ast.Name(id='b', ctx=ast.Load())]
    assert list(find(simple, ast.Load)) == find(simple, 'Load') == [ast.Load(),
                                                                    ast.Load(),
                                                                    ast.Load()]



# Generated at 2022-06-14 03:03:18.128425
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astor  # type: ignore
    import astunparse  # type: ignore


# Generated at 2022-06-14 03:03:24.078135
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("def func():\n i = 0\n print(i)")
    func = tree.body[0]
    assert get_parent(tree, func) is tree
    assert get_parent(func, func.body[0]) is func
    assert get_parent(func, func.body[0].value) is func.body[0]



# Generated at 2022-06-14 03:03:38.830275
# Unit test for function find
def test_find():
    def find_helper(type_: Type[T], tree: ast.AST, count: int) -> None:
        """Checks that type_ is count in tree."""
        results = find(tree, type_)
        results = [r for r in results]
        assert len(results) == count

    tree = ast.parse("x = 0")

    find_helper(ast.Name, tree, 1)
    find_helper(ast.Load, tree, 1)
    find_helper(ast.Assign, tree, 1)
    find_helper(ast.Store, tree, 1)

    tree = ast.parse("def f(): pass")
    find_helper(ast.FunctionDef, tree, 1)
    find_helper(ast.Name, tree, 2)

# Generated at 2022-06-14 03:03:42.479692
# Unit test for function find
def test_find():
    assert len([t for t in find(ast.parse("def f(): pass"), ast.FunctionDef)]) == 1
    assert len([t for t in find(ast.parse("def f(): pass"), ast.Call)]) == 0


# Generated at 2022-06-14 03:03:52.566115
# Unit test for function find
def test_find():
    # Test function for testing function find
    import unittest
    import sys
    import astor

    class TestFind(unittest.TestCase):

        def test_find(self):
            # Test case 1
            code = '''
                a = 0
                b = a
                a = 1
                '''
            tree = ast.parse(code)
            nodes = [node for node in find(tree, ast.Assign)]
            result = astor.to_source(nodes[0])
            expected = 'a = 0'
            assert result == expected

            # Test case 2
            code = '''
                def f():
                    a = 1
                    return a
                '''
            tree = ast.parse(code)
            nodes = [node for node in find(tree, ast.Assign)]
            result = astor

# Generated at 2022-06-14 03:04:00.780960
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = '''def foo():
                  a = 1
                  b = 2
                  c = 3
                  d = 4
                  e = 5
                  return a + b
              '''
    tree = ast.parse(code)

    # Find 'a' node
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == 'a':
            break

    # Assert that node is found
    assert node, 'Node not found'

    # Assert that closest FunctionDef is found
    assert isinstance(get_closest_parent_of(tree, node, ast.FunctionDef),
                      ast.FunctionDef), \
        'Not a function definition'

# Generated at 2022-06-14 03:04:08.095770
# Unit test for function find
def test_find():
    import astor
    tree = ast.parse('''
    def a():
        if True:
            pass
        while True:
            pass
    ''')
    assert len(list(find(tree, ast.If))) == 1
    assert len(list(find(tree, ast.While))) == 1
    assert len(list(find(tree, ast.FunctionDef))) == 1
    t = astor.dump_tree(tree)
    print(t)

# Generated at 2022-06-14 03:04:18.800898
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import inspect
    import unittest

    class TestCase(unittest.TestCase):
        def test_get_closest_parent_of(self):
            def test_func():
                a = True
                if a:
                    b = True
                    if b:
                        c = True
                        if c:
                            d = True
                        else:
                            e = True
                    else:
                        f = True
                        if f:
                            g = True
                        else:
                            h = True
                else:
                    i = True
                    if i:
                        j = True

            tree = ast.parse(inspect.getsource(test_func))

# Generated at 2022-06-14 03:04:30.185202
# Unit test for function find
def test_find():
    import astor
    def function(a, b):
        """function docstring"""
        c = 4
        print(a + b + d)
        return c * a * b * d
    tree = ast.parse(function.__doc__)
    # ast.fix_missing_locations(tree)
    print(astor.dump_tree(tree))
    for node in find(tree, ast.FunctionDef):
        print(node)
    for node in find(tree, ast.Return):
        print(node)



# Generated at 2022-06-14 03:04:31.740369
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:04:33.426434
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:04:35.622753
# Unit test for function find
def test_find():
    tree = ast.parse('def foo():\n\tpass')
    for node in find(tree, ast.FunctionDef):
        assert node.name == 'foo'



# Generated at 2022-06-14 03:04:51.451019
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.parse("def foo():\n    return 1")
    print (get_non_exp_parent_and_index(node, node.body[0].body[0]))


# Generated at 2022-06-14 03:04:53.322653
# Unit test for function find
def test_find():
    tree = ast.parse('1+1')
    assert len(list(find(tree, ast.Num))) == 2



# Generated at 2022-06-14 03:05:03.602164
# Unit test for function get_parent
def test_get_parent():
    class Node:
        def __init__(self, parent, label):
            self.parent = parent
            self.label = label

        def accept(self, visitor):
            return visitor.visit(self)

    class ParentNode:
        def __init__(self, children):
            self.children = children

        def accept(self, visitor):
            return visitor.visit(self)

    class Visitor:
        def visit(self, node):
            return node

    class NodeVisitor(Visitor):
        def visit(self, node):
            _parents[node] = node.parent
            return node

    class ParentNodeVisitor(Visitor):
        def visit(self, node):
            for child in node.children:
                child.accept(self)
            return node


# Generated at 2022-06-14 03:05:06.442039
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:12.247100
# Unit test for function find
def test_find():
    source = \
'''
if 1:
    for x in y:
        if 1:
            for x in y:
                pass
'''
    tree = ast.parse(source)
    assert list(find(tree, ast.For)) == \
        [tree.body[0].body[0].body[0].body[0], tree.body[0].body[0].body[0]]

# Generated at 2022-06-14 03:05:13.249580
# Unit test for function find
def test_find():
    pass



# Generated at 2022-06-14 03:05:14.418988
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:19.339688
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Setup
    from typed_ast import ast3 as ast
    from manuscript.tools.tree_manipulation.tree_manipulation import get_closest_parent_of
    tree = ast.parse("""x = 1
if x == 1:
    x = 2
else:
    x = 3
    """)
    child = tree.body[0].value
    # Test
    parent = get_closest_parent_of(tree, child, ast.FunctionDef)
    # Verify
    assert parent is tree



# Generated at 2022-06-14 03:05:24.795923
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    node = ast.parse("""
    if x:
        a = func()
        b = 1
    """)

    assert isinstance(get_closest_parent_of(node, node.body[0].body[1],
                                            ast.FunctionDef),
                      ast.FunctionDef)
    assert isinstance(get_closest_parent_of(node, node.body[0].body[1],
                                            ast.If),
                      ast.If)
    assert isinstance(get_closest_parent_of(node, node.body[0].body[1],
                                            ast.IfExp),
                      ast.If)

# Generated at 2022-06-14 03:05:35.018100
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from string import Template

    src = Template(
        """
        class A:
            def b(self):
                test(
                    FunctionDef(arguments=[arg(arg='a', annotation=None)],
                                body=[Expr(value=assert_node)]
                    ),
                    FunctionDef(arguments=[arg(arg='a', annotation=None)],
                                body=[Expr(value=assert_node)]
                    )
                )
        """
    ).substitute({
        'assert_node': ast.Name(id='assert_node', ctx=ast.Load())
    })

    tree = ast.parse(src)
    assert_node = get_closest_parent_of(tree, tree.body[0].body[0].body[0].value,
                                        ast.Name)
    call_parent,

# Generated at 2022-06-14 03:06:13.925240
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('print(1)')
    body = tree.body[0]
    exp = body.value
    name = exp.func
    parent = get_parent(tree, name)

    assert parent is body

# Generated at 2022-06-14 03:06:20.629420
# Unit test for function find
def test_find():
    result = find(ast.parse(
        'def add(a, b):\n    return a + b\n\nprint(add(2, 3))'), ast.Name)
    assert list(result) == [ast.Name(id='a', ctx=ast.Store()),
                            ast.Name(id='b', ctx=ast.Store()),
                            ast.Name(id='a', ctx=ast.Load()),
                            ast.Name(id='b', ctx=ast.Load()),
                            ast.Name(id='add', ctx=ast.Load()),
                            ast.Name(id='print', ctx=ast.Load())]

# Generated at 2022-06-14 03:06:27.359621
# Unit test for function find
def test_find():
    test_ast = ast.parse("""
    def foo(bar):
        return [1, 2, 3]
        if bar:
            pass
        if bar:
            pass
    """)
    assert len(list(find(test_ast, ast.If))) == 2
    assert len(list(find(test_ast, ast.FunctionDef))) == 1

# Generated at 2022-06-14 03:06:36.894556
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = 'if True: print(5)'
    tree = ast.parse(code)
    node = ast.Name('node', ast.Load())
    print_node = ast.Print(node)
    if_node = ast.If(ast.NameConstant(True), print_node, None)
    module_node = ast.Module(body=[if_node])

    assert if_node is get_closest_parent_of(module_node, node, ast.If)
    assert module_node is get_closest_parent_of(module_node, node, ast.Module)
    assert print_node is get_closest_parent_of(module_node, node, ast.Print)


# Generated at 2022-06-14 03:06:41.207788
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..exceptions import NodeNotFound
    from ..ast.builder import build_ast
    from ..ast.find import find
    from ..ast.checks import is_func, is_for_loop

    import astor


# Generated at 2022-06-14 03:06:45.505772
# Unit test for function find
def test_find():
    source = '''
            def func():
                pass
            '''

    tree = ast.parse(source)
    func_defs = list(find(tree, type(tree.body[0])))
    assert len(func_defs) == 1


# Generated at 2022-06-14 03:06:49.273060
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('x = lambda: lambda: 1\n')
    func = tree.body[0].value.body
    func_2 = func[0].body
    assert get_closest_parent_of(tree, func_2, ast.FunctionDef) == func

# Generated at 2022-06-14 03:06:52.320210
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class Foo:
        pass

    class Bar(Foo):
        pass

    bar = Bar()
    assert get_closest_parent_of(bar, bar, Foo) is bar



# Generated at 2022-06-14 03:07:00.247291
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Test function get_closest_parent_of()."""
    # parent
    def func_parent():
        # child
        pass

    func_def_parent = ast.parse(str(func_parent))
    node_parent = get_closest_parent_of(
        func_def_parent, func_def_parent.body[0].body[0], ast.FunctionDef)

    assert isinstance(node_parent, ast.FunctionDef)
    assert node_parent.name == 'func_parent'



# Generated at 2022-06-14 03:07:04.768022
# Unit test for function find
def test_find():
    assert len(list(find(ast.parse('''
    class a:
        def b():
            pass

        def c():
            pass
    '''), ast.FunctionDef))) == 2

    assert len(list(find(ast.parse('''
    class a:
        def b():
            pass

        def c():
            pass

    class d:
        def e():
            pass
    '''), ast.FunctionDef))) == 3



# Generated at 2022-06-14 03:09:48.627786
# Unit test for function get_parent
def test_get_parent():
    import unittest
    from astroid import MANAGER, builder

    # Define a test class
    class TestGetParent(unittest.TestCase):

        def setUp(self):
            self.code = '''
            def a():
                pass
            '''

        def test_get_parent(self):
            astroid = builder.parse(self.code)
            MANAGER.astroid_cache.clear()
            func = astroid.body[0]
            for node in ast.walk(func):
                assert get_parent(astroid, node) != astroid

    # Run the tests
    unittest.main()

# Generated at 2022-06-14 03:09:52.006342
# Unit test for function find
def test_find():
    tree = ast.parse('def foo():\n  return 1')
    nodes = find(tree, ast.Return)

    # there is only one return
    assert len(list(nodes)) == 1

    # node is of type ast.Return
    node = list(nodes)[0]
    assert isinstance(node, ast.Return)

# Generated at 2022-06-14 03:09:52.461847
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pass

# Generated at 2022-06-14 03:09:53.773337
# Unit test for function find
def test_find():
    tree = ast.parse('a + 1')

    for node in find(tree, ast.Add):
        print(node)



# Generated at 2022-06-14 03:10:03.358809
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    from textwrap import dedent

    code = dedent("""
    for i in range(4):
        pass
    """)

    tree = ast.parse(code)

    for_nodes = list(find(tree, ast.For))
    assert len(for_nodes) == 1
    assert isinstance(for_nodes[0], ast.For)

    pass_nodes = list(find(tree, ast.Pass))
    assert len(pass_nodes) == 1
    assert isinstance(pass_nodes[0], ast.Pass)

    name_nodes = list(find(tree, ast.Name))
    assert len(name_nodes) == 2
    assert isinstance(name_nodes[0], ast.Name)

# Generated at 2022-06-14 03:10:07.829382
# Unit test for function find
def test_find():
    node = ast.parse("def test():\n"
                     "    pass\n")

    for n in find(node, ast.FunctionDef):
        assert n.name == 'test'

# Generated at 2022-06-14 03:10:14.367800
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    module = ast.parse('''if True:
        def g():
            pass
    else:
        def g():
            pass
    ''')

    fdef = module.body[0].body[0]
    fdef_parent, index = get_non_exp_parent_and_index(module, fdef)

    assert fdef_parent == module.body[0]
    assert index == 0
    assert fdef_parent.body[index] == fdef

# Generated at 2022-06-14 03:10:19.168938
# Unit test for function get_parent
def test_get_parent():
    code = '''
    def test_fun():
        return x # Return statement
    '''
    tree = ast.parse(code)
    # get parent of x, should be load
    assert isinstance(get_parent(tree, tree.body[0].body[0].value), ast.Load)

    # In same example, get parent of return
    assert isinstance(get_parent(tree, tree.body[0].body[0]), ast.Return)

    # In same example, get parent of function def
    assert isinstance(get_parent(tree, tree.body[0]), ast.FunctionDef)

    # get parent of return, should raise NodeNotFound
    with pytest.raises(NodeNotFound):
        get_parent(tree, tree.body[0].body[0].value.id)



# Generated at 2022-06-14 03:10:31.427990
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # type: () -> None
    import unittest

    class GetClosestParentOfTestCase(unittest.TestCase):
        def setUp(self):
            AST = ast.parse('def foo():\n    bar = 3').body[0]
            _build_parents(AST)

        def tearDown(self):
            _parents.clear()

        def test_exception(self):
            with self.assertRaises(NodeNotFound):
                get_closest_parent_of(ast.parse('foo'), ast.parse('bar'),
                                      ast.Module)

        def test_get_closest_parent_of(self):
            AST = ast.parse('def foo():\n    bar = 3').body[0]
            node = AST.body[0]

# Generated at 2022-06-14 03:10:35.941895
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    from .ast_utils import find
    from .types import GetattrExpr

    tree = ast.parse('import a.b\na.b')

    for node in find(tree, GetattrExpr):
        assert isinstance(node, GetattrExpr)

if __name__ == '__main__':
    test_find()