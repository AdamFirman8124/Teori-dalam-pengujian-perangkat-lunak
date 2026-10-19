

# Generated at 2022-06-14 03:01:34.084360
# Unit test for function find
def test_find():
    def func_to_test():
        a = 0
        return b
        b = 4

    mod = ast.parse(func_to_test.__doc__)
    assert len(list(find(mod, ast.Assign))) == 0
    assert len(list(find(mod, ast.Name))) == 2

# Generated at 2022-06-14 03:01:40.292910
# Unit test for function find
def test_find():
    # tree = ast.parse("def foo():\n    var = None")
    # tree = ast.parse("for i in range(10):\n    if i > 5:\n        i = 5")
    tree = ast.parse("def foo():\n    var = None")
    if_node = find(tree, ast.AST)
    print(if_node)

# Generated at 2022-06-14 03:01:41.268028
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:01:44.893724
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Given
    tree = ast.parse("""\
if a:
    b()
else:
    c()
""")
    # When
    result = get_closest_parent_of(tree, tree.body[0].body[0], ast.If)
    # Then
    assert result == tree.body[0]

# Generated at 2022-06-14 03:01:51.818110
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("""
    for x in y:
        for z in w:
            1+1
            x = 1
        x = 1
    """)
    parents = [
        (ast.For, ast.FunctionDef, ast.Module),
        (ast.For, ast.FunctionDef, ast.Module),
        (ast.For, ast.FunctionDef, ast.Module),
        (ast.For, ast.FunctionDef, ast.Module),
        (ast.For, ast.FunctionDef, ast.Module)
    ]
    indices = [0, 1, 0, 1, 1]

# Generated at 2022-06-14 03:02:02.432114
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    parent = ast.parse("def foo(a, b): ''' docstring '''\n\treturn a * b\n")
    func = parent.body[0]
    arguments = func.args
    arg_a = arguments.args[0]
    arg_b = arguments.args[1]
    assert (type(get_closest_parent_of(parent, arg_a, ast.FunctionDef)) ==
            ast.FunctionDef)
    assert (type(get_closest_parent_of(parent, arg_b, ast.FunctionDef)) ==
            ast.FunctionDef)
    assert (type(get_closest_parent_of(parent, arg_a, ast.Return)) ==
            ast.FunctionDef)

# Generated at 2022-06-14 03:02:11.866306
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert get_non_exp_parent_and_index(
        ast.parse(
            """
            def foo():
                a = b
                c = d
                e = f
            """,
            "file.py"
        ),
        ast.parse(
            """
            a = b
            """,
            "file.py"
        ).body[0]
    ) == (
        ast.parse(
            """
            def foo():
                a = b
                c = d
                e = f
            """,
            "file.py"
        ).body[0],
        0
    )


# Generated at 2022-06-14 03:02:13.771631
# Unit test for function find
def test_find():
    statement = ast.parse(
        '''
        def main():
            pass
        '''
    )

    assert len(list(find(statement, ast.FunctionDef)))

# Generated at 2022-06-14 03:02:23.152269
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:33.850379
# Unit test for function find
def test_find():
    from .test_base import create_test_tree
    from ..ast_utils import get_node
    tree = create_test_tree()

    print('Modules:')
    print(find(tree, ast.Module))

    print('FunctionDefs:')
    print(find(tree, ast.FunctionDef))

    print('Call:')
    print(find(tree, ast.Call))

    print('Assigns:')
    print(find(tree, ast.Assign))

    print('Name:')
    print(find(tree, ast.Name))

    print('Str:')
    print(find(tree, ast.Str))

    print('Print:')
    print(find(tree, ast.Print))

    print('Expr:')
    print(find(tree, ast.Expr))


# Generated at 2022-06-14 03:02:42.035768
# Unit test for function insert_at
def test_insert_at():
    root = ast.parse('\n'
                     'def test():\n'
                     '    return 0\n')
    target_node = root.body[0]  # type: ignore
    assert isinstance(target_node, ast.FunctionDef)

    target_node_body = target_node.body[0]
    assert isinstance(target_node_body, ast.Return)

    insert_at(0, target_node, ast.Assign(
        targets=[ast.Name(id='a', ctx=ast.Store())],
        value=ast.Num(n=0)))
    insert_at(1, target_node, ast.Assign(
        targets=[ast.Name(id='b', ctx=ast.Store())],
        value=ast.Num(n=0)))

# Generated at 2022-06-14 03:02:42.749633
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pass



# Generated at 2022-06-14 03:02:44.215717
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:56.467261
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("""
    def cookie(n, k):
        for j in range(k):
            for i in range(n-j-1):
                if a[i] > a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
    """)
    _build_parents(tree)
    assert get_parent(tree, tree.body[0].body[0].body[0]) == tree.body[0].body[0]
    assert get_parent(tree, tree.body[0].body[0].body[0].body[0]) == \
        tree.body[0].body[0].body[0]

# Generated at 2022-06-14 03:03:06.973799
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class_ = ast.ClassDef(
        name='A',
        body=[
            ast.FunctionDef(
                name='func1',
                body=[
                    ast.Pass(),
                    ast.Pass(),
                ],
            ),
            ast.FunctionDef(
                name='func2',
                body=[
                    ast.Pass(),
                    ast.Pass(),
                ],
            )
        ],
    )
    parent, index = get_non_exp_parent_and_index(class_, class_.body[0].body[0])
    assert(parent is class_)
    assert(index is 0)

# Generated at 2022-06-14 03:03:14.525459
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = """
            def foo():
                pass

            class bar():
                pass
            """
    tree = ast.parse(code)
    # We should visit nodes in reverse order, otherwise index is incorrect
    test_nodes = list(reversed(list(ast.walk(tree))))

    for index, node in enumerate(test_nodes):
        parent, _ = get_non_exp_parent_and_index(tree, node)
        assert parent == tree.body[index]  # type: ignore

# Generated at 2022-06-14 03:03:19.644140
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import typed_ast.ast3 as ast
    from . import get_non_exp_parent_and_index

    # Example from documentation
    a = ast.parse('some.function()')
    t, i = get_non_exp_parent_and_index(a, a.body[0].value)
    assert isinstance(t, ast.Module)
    assert i == 0
    assert isinstance(t.body[i], ast.Expr)

    # Example from documentation
    a = ast.parse('if something: x = 1')
    t, i = get_non_exp_parent_and_index(a, a.body[0].body[0])
    assert isinstance(t, ast.If)
    assert i == 0
    assert isinstance(t.body[i], ast.Assign)

    # Example from

# Generated at 2022-06-14 03:03:21.077451
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:03:27.991919
# Unit test for function find
def test_find():
    src = '''
    class A:
        def __init__(self, a):
            self.a = a
            return None
    '''

    tree = ast.parse(src)

    def_ = list(find(tree, ast.FunctionDef))[0]
    assert '__init__' == def_.name

    last_statement = ast.Return()
    last_statement.value = ast.Name(id='None')

    replace_at(2, def_, last_statement)

    assert last_statement is def_.body[2]  # type: ignore

    parent = get_parent(tree, last_statement)
    assert def_ is parent

    parent, index = get_non_exp_parent_and_index(tree, last_statement)
    assert def_ is parent
    assert def_.body[index] is last

# Generated at 2022-06-14 03:03:36.115243
# Unit test for function insert_at
def test_insert_at():
    def _(tree):
        pass

    tree = ast.parse(_.__code__).body[0]
    parent = get_closest_parent_of(tree, tree.body[0], ast.Module)

    insert_at(0, parent, ast.Expr(value=ast.Num(n=0)))
    with open('../test_files/test_insert_at.py', 'w') as fp:
        ast.fix_missing_locations(tree)
        fp.write(ast.unparse(tree))



# Generated at 2022-06-14 03:03:45.017180
# Unit test for function get_parent
def test_get_parent():
    ast3 = ast.parse('''
        def foo(a, b):
            return a + b
        ''')
    for node in ast.walk(ast3):
        _parents[node] = None
    _build_parents(ast3)
    assert _parents[ast3.body[0].body[0]].name == 'foo'


# Generated at 2022-06-14 03:03:49.130288
# Unit test for function get_parent
def test_get_parent():
    m = ast.parse(
        """
        class A(object):
            def meth(self, a, b):
                return a + b
        """
    )
    f = m.body[0].body[0]
    r = f.body[0]
    a = r.value.left

    _build_parents(m)

    assert get_parent(m, a) == r
    assert get_parent(m, r) == f
    assert get_parent(m, f) == m.body[0]
    assert get_parent(m, m.body[0]) == m



# Generated at 2022-06-14 03:03:54.550996
# Unit test for function find
def test_find():
    from . import nodes
    ast_ = nodes.for_loop(nodes.integer(1), nodes.integer(2),
                          [nodes.integer(3), nodes.integer(4)])
    found = list(find(ast_, ast.Num))
    assert len(found) == 3
    assert found[0].n == 3
    assert found[1].n == 4
    assert found[2].n == 2



# Generated at 2022-06-14 03:04:04.429318
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """Testing get_non_exp_parent_and_index function."""
    tree = ast.parse("""
        def func(x):
            def func_inner():
                return x
            return func_inner()
        print func(2)
    """)
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 0
    parent, index = \
        get_non_exp_parent_and_index(tree, tree.body[0].body[0].body[0])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 0
    assert len(parent.body) == 2

# Generated at 2022-06-14 03:04:10.183389
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import typed_astunparse
    import json

    test_node = ast.parse('1 + 1').body[0].value
    assert json.loads(typed_astunparse.dump(get_closest_parent_of(
        ast.parse('{1 + 1}'), test_node, ast.With
    ))) == json.loads('{1 + 1}')

# Generated at 2022-06-14 03:04:16.289041
# Unit test for function find
def test_find():  # type: ignore
    import inspect
    import sys
    print(
        "ast_tools.py::test_find is a functional test: "
        "it executes a function and compares some output.\n"
        "The function to be executed will be passed to exec().")
    print("Function body:\n" + inspect.getsource(test_find))
    print("Executing function to compare output...")
    orig_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    exec(inspect.getsource(test_find))
    sys.stdout = orig_stdout
    print("Done.")

# Generated at 2022-06-14 03:04:20.072946
# Unit test for function find
def test_find():
    node = ast.parse('print("Hello")')
    assert isinstance(list(find(node, ast.Expr))[0], ast.Expr)



# Generated at 2022-06-14 03:04:33.851575
# Unit test for function find
def test_find():
    tree = ast.parse('def foo():\n    def bar():\n        3\nbar()\nfoo()')
    # TODO: What is the correct type of tree?
    msg = 'assert each is of type _ast.FunctionDef'
    funcs = list(find(tree, ast.FunctionDef))  # type: ignore
    assert len(funcs) == 2
    assert all(isinstance(each, ast.FunctionDef) for each in funcs), msg
    assert funcs[0].name == 'foo'
    assert funcs[1].name == 'bar'
    assert funcs[0].body[0] == funcs[1]



# Generated at 2022-06-14 03:04:37.683951
# Unit test for function get_parent
def test_get_parent():
    import astor

    tree = ast.parse("""foo = 1 + 2""")
    expected = ast.parse("""foo = 1 + 2""").body[0]
    assert get_parent(tree, tree) == expected



# Generated at 2022-06-14 03:04:45.175968
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('def f():\n    pass\n    pass\n')
    node = tree.body[0].body[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert(isinstance(parent, ast.FunctionDef))
    assert(index == 0)


# Generated at 2022-06-14 03:04:58.795317
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    # pylint: disable=too-many-locals
    # pylint: disable=protected-access
    import _ast as ast2


# Generated at 2022-06-14 03:05:08.535545
# Unit test for function get_parent
def test_get_parent():
    # Test ast tree
    node_5 = ast.Expr(ast.Name(id='a'))
    node_4 = ast.Str('thing')
    node_3 = ast.Str('stuff')
    node_2 = ast.BinOp(left=node_4, op=ast.Sub(), right=node_5)
    node_1 = ast.BinOp(left=node_2, op=ast.Sub(), right=node_3)
    root = ast.Module(body=[node_1])

    assert get_parent(root, node_1) == root
    assert get_parent(root, node_2) == node_1
    assert get_parent(root, node_3) == node_1
    assert get_parent(root, node_4) == node_2

# Generated at 2022-06-14 03:05:16.094896
# Unit test for function get_parent
def test_get_parent():
    n = ast.Name(id='x', ctx=ast.Load())
    s = ast.Subscript(value=n, slice=ast.Index(value=ast.Constant(value=0)),
                      ctx=ast.Load())  # type: ast.AST
    g = ast.Global(names=['x'])  # type: ast.AST

    module = ast.Module(body=[ast.Assign(targets=[n], value=g), s])
    assert get_parent(module, n) == module.body[0]



# Generated at 2022-06-14 03:05:18.024473
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert ast.parse('a') == get_non_exp_parent_and_index(ast.parse('a'), ast.parse('a').body[0])[0]

# Generated at 2022-06-14 03:05:18.568347
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pass

# Generated at 2022-06-14 03:05:19.690181
# Unit test for function find

# Generated at 2022-06-14 03:05:25.530620
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from . import from_code
    from . import dump

    tree = from_code("x = (lambda x: x**2)(4)")
    pprint.pprint(tree)

    ###########################################################################
    print("\n### Searching for an argument to a lambda ###")

    def find_name(node):
        if isinstance(node, ast.Name):
            return node

    lambda_ = get_closest_parent_of(tree, find_name(tree), ast.Lambda)
    print("Lambda: \n" + dump.dump(lambda_))

    ###########################################################################
    print("\n### Searching for an argument to a Assign ###")

    def find_assign(node):
        if isinstance(node, ast.Assign):
            return node

    assign = get_

# Generated at 2022-06-14 03:05:27.695040
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """Unit test for function get_non_exp_parent_and_index."""

# Generated at 2022-06-14 03:05:33.204468
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    def func(a):
        b = 1
        c = 2
        if True:
            b = 2
        d = 3
        return b

    tree = ast.parse(func.__doc__)
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[1])  # b = 1
    print(ast.dump(parent))
    print(index)

# Generated at 2022-06-14 03:05:41.049978
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    for tree in [ast.parse(
        """def foo():
            return {'a': 0}['a']
        """
    ), ast.parse(
        """for x in y:
            z
        """
    )]:
        index = 1
        if isinstance(tree.body[0], ast.FunctionDef):  # type: ignore
            index = 0
        node = tree.body[index].body[0]
        parent, i = get_non_exp_parent_and_index(tree, node)
        assert parent == tree.body[index]
        assert i == 0


# Generated at 2022-06-14 03:05:56.111415
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    parent = ast.Module([
        ast.Expr(value=ast.BinOp(
            left=ast.Constant(value='abc'),
            op=ast.Plus(),
            right=ast.Constant(value='def'))),
        ast.Expr(value=ast.BinOp(
            left=ast.Constant(value='qwe'),
            op=ast.Plus(),
            right=ast.Constant(value='rty')))
    ])

    result = get_non_exp_parent_and_index(parent, parent.body[0].value)

    assert result == (parent, 0)



# Generated at 2022-06-14 03:06:01.643115
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    # Test case with simple assignment
    test_ast = ast.parse('a = 1')
    test_node = test_ast.body[0].value
    expected_parent = test_ast.body[0]
    assert get_non_exp_parent_and_index(test_ast, test_node) == (expected_parent, 0)

    # Test case with assign to a function parameter
    test_ast = ast.parse('def f(a):\n    b = a')
    test_node = test_ast.body[0].body[0].value
    expected_parent = test_ast.body[0].body[0]
    assert get_non_exp_parent_and_index(test_ast, test_node) == (expected_parent, 0)

    # Test case where a function expression is passed as an argument
    test

# Generated at 2022-06-14 03:06:03.162043
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:06:14.174287
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.parse("""
    def func(arg1, arg2):
        def inner_func(inner_arg):
            return inner_arg
        
        var1 = inner_func(arg1)
        var2 = inner_func(arg2)
        return var1 + var2 + 1
    """)

    parent, index = get_non_exp_parent_and_index(node, node.body[0].body[0].body[0])
    assert isinstance(parent, ast.FunctionDef) and index == 0
    assert parent.body[index] is node.body[0]

    parent, index = get_non_exp_parent_and_index(node, node.body[0].body[1].value)
    assert isinstance(parent, ast.FunctionDef) and index == 1

# Generated at 2022-06-14 03:06:21.853998
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node1 = ast.Name("node1")
    node2 = ast.Name("node2")
    node3 = ast.Name("node3")
    node4 = ast.Name("node4")
    node5 = ast.Name("node5")

    tree = ast.Module([
        ast.Expr(node1),
        ast.Expr(ast.List([
            ast.Expr(node2),
            node5
        ], ctx=ast.Load())),
        ast.Expr(ast.Tuple([
            ast.Expr(node3),
            node4
        ], ctx=ast.Load()))
    ])

    assert get_non_exp_parent_and_index(tree, node1) ==\
        (tree.body, 0)


# Generated at 2022-06-14 03:06:23.006745
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:06:33.251706
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree_src = '''
node = False
if node: #comments
    print 'xx'

node = True
if node:
    node = 'this is node'
    print node
    #comments

node = 'node'
print node

node = True
i = 1
while node:
    node = i > 0
    print i

for node in range(0, 10):
    if node > 3:
        break
    i = node
    print 'output: %s' % node

    def test_function():
        node = 'test func'
        return node

    node = test_function()
    print node
    '''
    tree = ast.parse(tree_src)
    get_parent(tree, tree.body[4])

# Generated at 2022-06-14 03:06:45.033970
# Unit test for function replace_at
def test_replace_at():
    # Create function
    function_def = ast.FunctionDef(name='decorated_function', args=ast.arguments(
        args=[],
        kwonlyargs=[],
        vararg=None,
        kwarg=None,
        defaults=[],
        kw_defaults=[]
    ), body=[], decorator_list=[], returns=None)

    # Create call and add it to function body
    function_call = ast.Expr(value=ast.Call(func=ast.Name(id='print'), args=[
        ast.Str(s='This is a test')], keywords=[]))

    function_def.body.append(function_call)  # type: ignore

    # Replace function call with two calls

# Generated at 2022-06-14 03:06:48.573732
# Unit test for function find
def test_find():
    tree = ast.parse('def foo(a, b):\n  return (a + b)')
    nodes = find(tree, ast.FunctionDef)
    assert [node.name for node in nodes] == ['foo']

# Generated at 2022-06-14 03:06:53.347780
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    def foo():
        """
        foo doc
        """
        return 0

    tree = ast.parse(foo.__code__.co_code)
    target = tree.body[0].body[0]
    parent, index = get_non_exp_parent_and_index(tree, target)
    assert parent is tree.body[0]
    assert index == 0

# Generated at 2022-06-14 03:07:06.179407
# Unit test for function find
def test_find():
    """
    Test function find
    :return:
    """
    prg = """
    if x:
        print(x)
    """
    tree = ast.parse(prg)
    parents = dict()  # type: dict[ast.AST, ast.AST]

    for node in list(ast.walk(tree)):
        for child in list(ast.iter_child_nodes(node)):
            parents[child] = node

    assert len([node for node in ast.walk(tree) if isinstance(node, ast.Print)]) == 1
    assert len(find(tree, ast.Print)) == 1



# Generated at 2022-06-14 03:07:12.719281
# Unit test for function find
def test_find():
    """Test find function."""
    s = ast.parse("class X: pass")
    try:
        assert list(find(s, ast.ClassDef)) == [s.body[0]]
        assert list(find(s, ast.Name)) == [
            s.body[0].name,
            *s.body[0].body[0].args.args
        ]
    except:
        print("test_find failed!")
        raise


# Generated at 2022-06-14 03:07:22.095065
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    import ast
    code = """
if 5:
    if 7:
        abc = 10
    else:
        abc = 1
else:
    abc = 0
    """
    tree = ast.parse(code)
    test_node = get_closest_parent_of(tree, tree.body[0], ast.AST)
    if astor.to_source(test_node).strip() != 'if 5:':
        raise AssertionError("Error: get_closest_parent_of")


# Generated at 2022-06-14 03:07:28.871260
# Unit test for function find
def test_find():
    code = '''
    class A():
        pass

    class B():
        pass

    class C():
        pass
    '''

    tree = ast.parse(code)
    classes = list(find(tree, ast.ClassDef))
    assert len(classes) == 3
    assert classes[0].name == 'A'
    assert classes[1].name == 'B'
    assert classes[2].name == 'C'



# Generated at 2022-06-14 03:07:34.997599
# Unit test for function find
def test_find():
    global tree
    # test node in tree
    for node in tree.body:
        assert len([n for n in find(tree, ast.FunctionDef) if n is node]) == 1
    # test node not in tree
    node = ast.FunctionDef(name='test', args=ast.arguments(args=[], vararg=None,
                                                           kwarg=None,
                                                           defaults=[]),
                           body=[], decorator_list=[])
    assert len([n for n in find(tree, ast.FunctionDef) if n is node]) == 0


# Generated at 2022-06-14 03:07:38.403529
# Unit test for function find
def test_find():
    # Testing the current program
    tree = ast.parse(open(__file__).read())
    assert len(list(find(tree, ast.AST))) == len(list(ast.walk(tree)))

# Generated at 2022-06-14 03:07:40.354044
# Unit test for function get_parent
def test_get_parent():
    assert get_parent(ast.parse("def foo():\n    pass"), ast.parse("pass")) == ast.parse("def foo():\n    pass")



# Generated at 2022-06-14 03:07:42.751374
# Unit test for function find
def test_find():
    test_fnc = \
        """
        def f():
            pass
        """

    tree = ast.parse(test_fnc)

    assert len(list(find(tree, ast.FunctionDef))) == 1



# Generated at 2022-06-14 03:07:48.721540
# Unit test for function get_parent
def test_get_parent():
    """Test for get_parent."""
    tree = ast.parse(dedent('''
    def f(x, y, z):
        a = 1
        b = a + y
        c = a + b
        return c
    '''))
    assert get_parent(tree, tree.body[0].body[1].value) == tree.body[0]


# Generated at 2022-06-14 03:07:56.914269
# Unit test for function find
def test_find():
    class A(ast.AST):
        _fields = ()  # type: List[str]

    class B(ast.AST):
        _fields = ()  # type: List[str]

    a = A()
    b1 = B()
    b2 = B()

    assert list(find(a, A)) == [a]

    a.a = b1
    b1.b = b2
    a.b1 = b1

    assert list(find(a, A)) == [a]
    assert list(find(a, B)) == [b1, b2]

# Generated at 2022-06-14 03:08:06.545574
# Unit test for function find
def test_find():
    assert len(list(find(tree('1+1'), ast.BinOp))) == 1
    assert len(list(find(tree('1+1'), ast.Call))) == 0


# Generated at 2022-06-14 03:08:14.015375
# Unit test for function find
def test_find():
    assert sum(1 for _ in find(ast.parse('a = ("b", "c")'), ast.Tuple)) == 1
    assert sum(1 for _ in find(ast.parse('a = ("b", "c")'), ast.Expr)) == 1
    assert sum(1 for _ in find(ast.parse('a = ("b", "c")'), ast.Attribute)) == 2
    assert sum(1 for _ in find(ast.parse('a = ("b", "c")'), ast.Name)) == 3

# Generated at 2022-06-14 03:08:21.509258
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest
    import typed_ast.ast3 as t

    class Test(unittest.TestCase):

        def test_get_closest_parent_of(self):
            global p
            p = t.parse("""if d:
                if b:
                    if c:
                        pass
            """).body[0]
            test_node = p.body.body[0].body.body[0]
            result = get_closest_parent_of(p, test_node, t.If)
            self.assertEqual(result, p.body.body[0])

    test = Test()
    test.test_get_closest_parent_of()



# Generated at 2022-06-14 03:08:37.199375
# Unit test for function find
def test_find():
    class _:
        def __init__(self, n):
            self.n = n
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

        def __iter__(self):
            return iter(self.children)

    a = _(1)
    b = _(2)
    c = _(3)
    d = _(4)
    e = _(5)
    f = _(6)

    a.add_child(b)
    a.add_child(c)
    b.add_child(d)
    c.add_child(e)
    d.add_child(f)

    res = list(find(a, type(_)))
    assert len(res) == 6
    assert res[0].n == 1


# Generated at 2022-06-14 03:08:41.842233
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    ast_tree = ast.parse("""
    def add(a, b):
        return a + b
    """)
    expected_result = (ast_tree.body[0], 0)
    result = get_non_exp_parent_and_index(ast_tree, ast_tree.body[0].body[0])
    assert result == expected_result

# Generated at 2022-06-14 03:08:47.783394
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..exceptions import NodeNotFound
    from typed_ast import ast3 as ast
    from ..transforms.type_annotate import annotate_type_comments
    from ..utils.tools import parse_module, dump_module, ast_cache


# Generated at 2022-06-14 03:08:51.215864
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    print("Running", test_get_closest_parent_of.__name__)
    pytest = importlib.import_module("pytest")
    pytest.main()



# Generated at 2022-06-14 03:08:58.037540
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import tests.test_data.ast_dump as ast_dump

    closest_parent = get_closest_parent_of(ast_dump.t, ast_dump.a1, ast.Module)

    assert(closest_parent is ast_dump.m)

# Generated at 2022-06-14 03:09:05.185580
# Unit test for function find
def test_find():
    import astor

    source = '''
    def foo():
        a = 1
        b = 2
        return a + b
    '''
    tree = ast.parse(source)
    nodes = list(find(tree, ast.Store))
    assert len(nodes) == 2
    assert astor.to_source(nodes[0]) == 'a = 1\n'
    assert astor.to_source(nodes[1]) == 'b = 2\n'

# Generated at 2022-06-14 03:09:09.992110
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """
    test_get_closest_parent_of is a unit test function.
    """
    tree = ast.parse(
        '''
        def foo():
            pass
        '''
    )
    node = find(tree, ast.FunctionDef).__next__()
    parent = get_closest_parent_of(tree, node, ast.Module)

    assert isinstance(parent, ast.Module)



# Generated at 2022-06-14 03:09:22.652171
# Unit test for function find
def test_find():
    find_test = ast.parse('''
        def test():
            print(1)
            print(2)
    ''')
    list(find(find_test, ast.Print))

# Generated at 2022-06-14 03:09:31.035388
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import typed_ast.ast3 as ast

    tree = ast.parse('[a, b, c]')
    node = tree.body[0].value

    assert isinstance(node, ast.List)

    # Expected: ast.Expr
    assert isinstance(get_closest_parent_of(tree, node, ast.Expr), ast.Expr)

    assert isinstance(node, ast.List)

    # Expected: ast.Module
    assert isinstance(get_closest_parent_of(tree, node, ast.Module), ast.Module)

# Generated at 2022-06-14 03:09:39.102144
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Parent
    assert get_closest_parent_of(ast.parse(
        """
        def foo():
            print(42)
        """), ast.parse(
        """
        print(42)
        """).body[0], ast.FunctionDef) == ast.parse(
        """
        def foo():
            print(42)
        """).body[0]

    # Parent's parent
    assert get_closest_parent_of(ast.parse(
        """
        def foo():
            print(42)
        """), ast.parse(
        """
        print(42)
        """).body[0], ast.Module) == ast.parse(
        """
        def foo():
            print(42)
        """)

    # Grandparent

# Generated at 2022-06-14 03:09:49.254059
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from astor import to_source
    from astpretty import pformat

    source = """\
    def main():
        if a():
            if a():
                print('yeah')
        # comment

        return True
    """

    tree = ast.parse(source)
    node = list(find(tree, ast.If))[1]
    parent = get_closest_parent_of(tree, node, ast.ClassDef)
    assert parent is None, pformat(parent)

    func = get_closest_parent_of(tree, node, ast.FunctionDef)
    assert to_source(func) == "def main():\n    if a():\n        if a():\n            print('yeah')\n    # comment\n\n    return True"


# Generated at 2022-06-14 03:09:52.278211
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("def hello():\n    print('Hello, world!')")
    tree_node = tree.body[0].body[0]
    parent_found = get_parent(tree, tree_node)

    assert tree.body[0] == parent_found


# Generated at 2022-06-14 03:09:53.178329
# Unit test for function get_parent
def test_get_parent():
    import unittest
    import astunparse


# Generated at 2022-06-14 03:09:58.119091
# Unit test for function find
def test_find():
    import astor
    tree = ast.parse('1 + 2\ndef foo():\n    return 3')
    nodes = list(find(tree, ast.Name))
    nodes_str = [astor.to_source(node).strip() for node in nodes]
    assert nodes_str == ['1', '2', 'foo', 'return']



# Generated at 2022-06-14 03:10:07.038318
# Unit test for function find
def test_find():
    import unittest.mock as mock

    loc = mock.Mock(line=1, col=1)
    lineno = mock.Mock(lineno=1)

# Generated at 2022-06-14 03:10:16.501046
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    string_with_parenthesis = "((a + b) // 10)"
    test_tree = ast.parse(string_with_parenthesis)
    node = test_tree.body[0].value.left.left
    assert(isinstance(node, ast.Name))
    assert(node.id == "a")
    test_type = ast.BinOp
    test_closest_parent = get_closest_parent_of(test_tree, node, test_type)
    assert(isinstance(test_closest_parent, test_type))
    assert(test_closest_parent.op.__class__.__name__ == "Add")
    string_without_parenthesis = string_with_parenthesis[1:-1]
    test_tree = ast.parse(string_without_parenthesis)
   

# Generated at 2022-06-14 03:10:27.984006
# Unit test for function find
def test_find():
    import astor
    prog = astor.parse_file("tests/test.py")
    _build_parents(prog)
    test_prog = astor.parse_file("tests/tests.py")
    funcs = find(test_prog, ast.FunctionDef)
    test_names = [func.name for func in funcs]
    assert "test_simple" in test_names
    assert "test_attribute" in test_names
    assert "test_name_constant" in test_names
    assert "test_add" in test_names
    assert "test_tuple" in test_names

# Generated at 2022-06-14 03:10:42.664825
# Unit test for function find
def test_find():
    from ... import parse
    from ... import generate
    from typing import Tuple, Union

    tree = parse('''
    def foo(a: int, b: int) -> int:
        return a + b
    ''') # type: Union[ast.AST, Tuple[ast.AST, ...]]

    for node in find(tree, ast.FunctionDef):
        assert node.name == 'foo'
        break



# Generated at 2022-06-14 03:10:48.482273
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    ast_ = ast.parse('def foo(a):\n    bar(a)')
    assert isinstance(get_closest_parent_of(ast_, ast_.body[0].body[0].args[0],
                                            ast.FunctionDef),
                      ast.FunctionDef)

# Generated at 2022-06-14 03:11:06.603711
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import typed_astunparse

    code = """
    def fun():
        x = 5
        if x > 3:
            if x > 4:
                return x
    """

    node = find(ast.parse(code), ast.Compare).__next__()
    for i in range(3):
        node = get_parent(ast.parse(code), node)

    assert node == get_closest_parent_of(ast.parse(code), node, ast.FunctionDef)
    assert node == typed_astunparse.unparse(ast.parse(code)).split('\n')[2]



# Generated at 2022-06-14 03:11:08.432529
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor

# Generated at 2022-06-14 03:11:26.704690
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse("""
    def test(a,b,c,d):
        a()
        b()
        c()
        d()
        return a
    """)

    func = tree.body[0]
    (new_node_1, new_node_2) = [ast.parse("""
    def new_func(a, b):
        return a
    """).body[0]] * 2

    replace_at(0, func, new_node_1)
    replace_at(1, func, new_node_2)
