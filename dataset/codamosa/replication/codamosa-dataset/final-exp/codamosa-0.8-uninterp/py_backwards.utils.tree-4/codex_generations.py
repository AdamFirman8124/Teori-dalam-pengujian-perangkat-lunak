

# Generated at 2022-06-14 03:01:43.217740
# Unit test for function replace_at
def test_replace_at():
    def func():
        a = 1 + 2
        b = 2 + 3
        print('ok')

    tree = ast.parse(func.__code__.co_consts[0])
    b_parent, b_index = get_non_exp_parent_and_index(tree,
                                                     tree.body[1].value)

    replace_at(b_index, b_parent, [ast.parse('z = 2 + 3')])

    b_parent, b_index = get_non_exp_parent_and_index(tree,
                                                     tree.body[1].value)

    replace_at(b_index, b_parent, [ast.parse('z = 2 * 3')])


# Generated at 2022-06-14 03:01:46.229845
# Unit test for function get_parent
def test_get_parent():
    import astor
    from . import simplecode

    _build_parents(simplecode.tree)
    parent = get_parent(simplecode.tree, simplecode.simple_assign)
    assert astor.to_source(parent) == dedent('''
        if False:
            print(42)
        ''')



# Generated at 2022-06-14 03:01:48.162521
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor

# Generated at 2022-06-14 03:01:51.762534
# Unit test for function find
def test_find():
    exp = ast.parse('a.b(c)').body[0].value

    assert len(list(find(exp, ast.Attribute))) == 1
    assert len(list(find(exp, ast.Call))) == 1

# Generated at 2022-06-14 03:02:00.282838
# Unit test for function replace_at
def test_replace_at():
    parent = ast.parse('if True: x = 5')
    replace_at(0, parent, [ast.parse('if True: x = 7').body[0]])
    assert ast.dump(parent) == "Module(body=[If(test=Name(id='True', ctx=Load()), " \
                             "body=[Assign(targets=[Name(id='x', ctx=Store())], " \
                             "value=Num(n=7))], orelse=[])])"

    parent = ast.parse('if True: x = 5')
    replace_at(0, parent, ast.parse('if True: x = 7').body)

# Generated at 2022-06-14 03:02:05.390455
# Unit test for function find
def test_find():
    node = ast.parse('''
    while True:
        pass
    ''')

    assert len(list(find(node, ast.While))) == 1

# Generated at 2022-06-14 03:02:14.167055
# Unit test for function find
def test_find():
    src = """
x = 1
if x > 5:
    y = 2
elif x > 6:
    y = 3
else:
    y = 4
    """
    tree = ast.parse(src)
    assert list(find(tree, ast.If)) == [tree.body[1]]
    assert list(find(tree, ast.Name)) == [tree.body[0].targets[0]]
    assert list(find(tree, ast.Num)) == [tree.body[0].value, tree.body[1],
                                         tree.body[1].body[0].value,
                                         tree.body[1].orelse[0].value,
                                         tree.body[1].orelse[1].value,
                                         tree.body[1].orelse[2].value]


# Generated at 2022-06-14 03:02:18.185213
# Unit test for function find
def test_find():
    tree = ast.parse("""
    def foo():
        return 0
    """)
    assert len(list(find(tree, ast.FunctionDef))) == 1
    assert len(list(find(tree, ast.Return))) == 1


# Generated at 2022-06-14 03:02:22.777433
# Unit test for function insert_at
def test_insert_at():
    tree = ast.parse("a = [1, 2, 3]")
    node = find(tree, ast.Name).__next__()
    l = [ast.Num(n=4)]
    insert_at(2, tree.body[0], l)
    assert tree.body[0].value.elts[2].n == 4
    assert tree.body[0].value.elts[3].n == 3


# Generated at 2022-06-14 03:02:29.106508
# Unit test for function find
def test_find():
    exp = '5 + 5'
    tree = ast.parse(exp)
    result = (exp for exp in find(tree, ast.Expression))
    assert next(result)
    with pytest.raises(StopIteration):
        next(result)



# Generated at 2022-06-14 03:02:40.142739
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    with open('example.py', 'r') as file:
        code = file.read()
    ast_tree = ast.parse(code)
    try:
        node = ast_tree.body[1].body[0].body[0]
        func_node = get_closest_parent_of(ast_tree, node, ast.FunctionDef)
        assert func_node.name == 'avg'
    except IndexError:
        print('Index Error!')




# Generated at 2022-06-14 03:02:44.475899
# Unit test for function find
def test_find():
    import astor
    import python_minifier.ast_compare as ast_compare

    print('Testing find() function')

# Generated at 2022-06-14 03:02:57.380734
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:59.777061
# Unit test for function find
def test_find():
    code = """
while True:
    pass
"""
    tree = ast.parse(code)
    while_ = next(find(tree, ast.While))

    assert isinstance(while_, ast.While)

# Generated at 2022-06-14 03:03:02.100674
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    pytest.skip()
    # TODO: add unit test
    # know_test = """
    #     def test(a):
    #         def test1():
    #             test2()
    # """.strip()



# Generated at 2022-06-14 03:03:03.421290
# Unit test for function find
def test_find():
    import astor

# Generated at 2022-06-14 03:03:07.083623
# Unit test for function find
def test_find():
    import pprint
    from .samples import tree_sample
    pprint.pprint(list(find(tree_sample, ast.FunctionDef)))



# Generated at 2022-06-14 03:03:10.537924
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('a=b;a')

    test_node = get_parent(tree, tree.body[0])
    assert get_non_exp_parent_and_index(tree, test_node) == (tree.body[0], 0)

# Generated at 2022-06-14 03:03:18.452159
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():

    def test_func(a, b):
        if a:
            print(b)

    tree = ast.parse(
        inspect.getsource(test_func),
        filename='<ast>',
    )

    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0])
    assert isinstance(parent, ast.If)
    assert index == 0

    parent = get_parent(tree, parent)
    assert isinstance(parent, ast.Module)

    # Non-exp
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[1])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 1

    # Raises

# Generated at 2022-06-14 03:03:28.539995
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    module_ast = ast.parse('def func(a, b):\n  a = a + 5')
    func_node = find(module_ast, ast.FunctionDef).__next__()
    assert get_non_exp_parent_and_index(module_ast, func_node) == (
        module_ast, 0)

    module_ast = ast.parse('insert_at(index, parent, [nodes])')
    func_node = find(module_ast, ast.FunctionDef).__next__()
    assert get_non_exp_parent_and_index(module_ast, func_node) == (
        module_ast, 0)
    assert type(get_non_exp_parent_and_index(module_ast, func_node)[0]) == ast.Module

# Generated at 2022-06-14 03:04:55.750373
# Unit test for function find
def test_find():
    from ..exceptions import InvalidUnitTest

    from .minify import minify
    from .extract import extract

    dec = minify(
        """
        def test_function_2(a, b):
            c = a + b
            print(c)
        """,
        with_types=True,
    )

    function = extract(dec, 'test_function_2')
    assert len([node for node in find(function, ast.Name)]) == 3


# Generated at 2022-06-14 03:05:03.826561
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node_a = ast.Expr(value=ast.Name(id='a'))
    node_b = ast.Expr(value=ast.Name(id='b'))
    node_c = ast.Expr(value=ast.Name(id='c'))

    node_body = ast.Expr(value=ast.Tuple(elts=[
        node_a,
        node_b,
        node_c,
    ]))

    node_my_func = ast.FunctionDef(name='my_func', body=[node_body])

    node_mod = ast.Module(body=[node_my_func])

    node_d = ast.Expr(value=ast.Name(id='d'))


# Generated at 2022-06-14 03:05:16.073399
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from typed_ast import ast3 as ast
    from ..manipulation import get_non_exp_parent_and_index
    assert get_non_exp_parent_and_index(ast.parse("""import random
random.choice(['I', 'like', 'python'])"""), ast.Name(id='random', ctx=ast.Load())) == (ast.parse("""import random
random.choice(['I', 'like', 'python'])""").body[0], 0)
    assert get_non_exp_parent_and_index(ast.parse("""random.choice(['I', 'like', 'python'])"""), ast.Name(id='random', ctx=ast.Load())) == (ast.parse("""random.choice(['I', 'like', 'python'])""").body[0].value, 0)

# Generated at 2022-06-14 03:05:17.766725
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:21.927714
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """Test get_non_exp_parent_and_index()."""
    source = '''
    def __init__(self):
        super().__init__()
        self.a = 5
        self.b = 6
    '''

    node = ast.parse(source, filename='<unknown>', mode='exec').body[0]
    parent, index = get_non_exp_parent_and_index(node, node.body[-1])

    assert index == 2
    assert parent == node

# Generated at 2022-06-14 03:05:23.333882
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:05:25.353076
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('x + y + z')
    assert get_non_exp_parent_and_index(tree ,tree.body[0].value.right) \
        == (tree.body[0], 1)

# Generated at 2022-06-14 03:05:26.879906
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:05:35.137979
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Pragma used to silence mypy warning about non-standard string formatting
    # behavior. This is only a test and we don't care about such problems.
    # https://github.com/python/mypy/issues/4185
    ast_source = '''
    # type: ignore
    def f():
        pass
    '''
    tree = ast.parse(ast_source)
    function = tree.body[0]
    parent = get_closest_parent_of(tree, function, ast.Module)

    assert isinstance(parent, ast.Module)

# Generated at 2022-06-14 03:05:38.832281
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('def f():\n  pass')
    assert get_parent(tree, tree.body[0].body[0]) == tree.body[0]


# Generated at 2022-06-14 03:06:49.914810
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:06:57.554194
# Unit test for function find
def test_find():
    example = ast.parse('''
    def some_function(x):
        if x == 1:
            return x <= 2 and x >= 1
        return x < 2 and x > 1
    ''')
    result = None
    for node in ast.walk(example):
        if isinstance(node, ast.FunctionDef):
            result = node

    assert result is not None



# Generated at 2022-06-14 03:06:59.959123
# Unit test for function find
def test_find():
    src = '''
    import os
    import sys

    import random
    import math
    '''

    tree = ast.parse(src)
    imports = list(find(tree, ast.Import))
    assert len(imports) == 4

# Generated at 2022-06-14 03:07:06.604832
# Unit test for function get_parent
def test_get_parent():
    program = """
        for u in range(0, 3):
            for v in range(0, 3):
                for w in range(0, 3):
                    for x in range(0, 3):
                        for y in range(0, 3):
                            for z in range(0, 3):
                                a = range(0, 3)
    """
    tree = ast.parse(program)
    _build_parents(tree)
    try:
        assert (type(_parents[tree.body[0].body[0].body[1].body[0].body[1].
                      body[0].body[0]])) == ast.For
    except:
        assert False



# Generated at 2022-06-14 03:07:14.973230
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    from .tree_utils import find
    from pprint import pprint
    import sys

    try:
        # with open("../test/test.py") as f:
        with open("../test/test1.py") as f:
            # tree = ast.parse(f.read(), filename="<ast>")
            tree = ast.parse(f.read())
    except FileNotFoundError as e:
        print(e.args)
        sys.exit(0)

    for i in tree.body:
        pprint(i)
        for j in find(i, ast.Assign):
            pprint(j)
            print('')



# Generated at 2022-06-14 03:07:19.662161
# Unit test for function get_parent
def test_get_parent():
    code = 'def foo():\n    pass\n'
    tree = ast.parse(code)
    node = tree.body[0]

    assert get_parent(tree, node) == tree
    assert get_parent(tree, node.body[0]) == node

# Generated at 2022-06-14 03:07:21.760190
# Unit test for function find
def test_find():
    import astor

# Generated at 2022-06-14 03:07:30.324593
# Unit test for function get_parent
def test_get_parent():
    import astor
    global_ast = ast.parse("""def a():\n    def b():\n        pass\n        pass""")
    _build_parents(global_ast)
    node_1 = global_ast.body[0]
    node_2 = node_1.body[0]
    node_3 = node_2.body[0]
    assert node_1 == get_parent(global_ast, node_2)
    assert node_2 == get_parent(global_ast, node_3)

# Generated at 2022-06-14 03:07:34.879412
# Unit test for function find
def test_find():
    assert list(find(ast.parse("""
    def foo(a, b):
        pass
    """), ast.Name)) == [ast.Name(id='foo', ctx=ast.Load())]



# Generated at 2022-06-14 03:07:43.741192
# Unit test for function get_parent
def test_get_parent():
    sys.path.append("..")
    import test.basic_test_file
    import inspect
    import astunparse
    test_file = inspect.getsource(test.basic_test_file)
    test_tree = ast.parse(test_file)
    lines_file = test_file.split("\n")
    print("\n")

    for node in ast.walk(test_tree):
        for child in ast.iter_child_nodes(node):
            print("Parent for: " + astunparse.unparse(child) + "\n")
            print("Found: " + astunparse.unparse(get_parent(test_tree, child)) + "\n")

# Generated at 2022-06-14 03:09:52.453629
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    s = '''
    if True:
        if True:
            a = ()
    '''

    tree = ast.parse(s)
    a_assign = tree.body[0].body[0].body[0]
    print(get_closest_parent_of(tree, a_assign, ast.If))

# Generated at 2022-06-14 03:09:57.269025
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Minimum expected ast with different types just to make sure the functions
    # works as expected
    ast_tree_code = """
    def func(a, b):
        if True:
            while True:
                return a + b

    class A:
        def __init__(self):
            pass
    """
    ast_tree = ast.parse(ast_tree_code)

    test_nodes = [
        ast_tree.body[1].body[0].body[0].body[0].value,
        ast_tree.body[1].body[1],
        ast_tree.body[2].body[0]
    ]

# Generated at 2022-06-14 03:10:02.255396
# Unit test for function find
def test_find():
    tree = ast.parse('''
        def a():
            if True:
                return 1

        class b:
            def a(self):
                c = 1
                return c
                ''')

    assert len(list(find(tree, ast.FunctionDef))) == 2
    assert len(list(find(tree, ast.ClassDef))) == 1



# Generated at 2022-06-14 03:10:12.709846
# Unit test for function find
def test_find():
    import astor
    source = '''
    def example():
        def hello():
            pass
        hello()
    '''
    tree = ast.parse(source)
    functions = find(tree, ast.FunctionDef)
    assert any(astor.to_source(func).strip() == 'def hello():\n    pass' for func in functions)
    assert any(astor.to_source(func).strip() == 'def example():\n    def hello():\n        pass\n    hello()' for func in functions)

# Generated at 2022-06-14 03:10:31.429182
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Test for get_closest_parent_of."""
    from .utils import parse_ast
    block = parse_ast("""
    if x:
        if y:
            
            a = 1
            b = 2
            c = 1 + 2
            if z:
                d = 4
                e = 5
    """)
    # get_closest_parent_of(block, block.body[0], ast.If)
    assert get_closest_parent_of(block, block.body[0], ast.If) == block.body[0]
    assert get_closest_parent_of(block, block.body[0].body[0], ast.If) == block.body[0].body[0]

# Generated at 2022-06-14 03:10:42.250899
# Unit test for function get_parent
def test_get_parent():
    import astor
    from ast import parse
    from ..utils import rename_unbound_local_variables
    test_code = '''
    def add(a, b):
        if a == 5:
            print(a + 5)
        else:
            print(b)
        return a + b
    '''
    tree = rename_unbound_local_variables(parse(test_code))
    # Test if FunctionDef
    assert astor.to_source(
        astor.dump_tree(tree)) == astor.to_source(
            astor.dump_tree(get_parent(tree, tree.body[0])))

    # Test If

# Generated at 2022-06-14 03:10:48.177962
# Unit test for function find
def test_find():  # noqa
    tree = ast.parse('x = 6 + 7')
    assert find(tree, ast.Assign)
    assert list(find(tree, ast.Assign))[0].value.n == 7



# Generated at 2022-06-14 03:11:07.097515
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Create tree
    parent = ast.Module(body=[ast.FunctionDef(name='func', args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Return(value=ast.Name(id='1', ctx=ast.Load())), ast.Return(value=ast.Name(id='2', ctx=ast.Load()))], decorator_list=[], returns=None)])
    node = ast.Return(value=ast.Name(id='1', ctx=ast.Load()))

    assert get_closest_parent_of(parent, node, ast.Module) == parent



# Generated at 2022-06-14 03:11:18.482795
# Unit test for function get_parent
def test_get_parent():
    def get_parents(node: ast.AST) -> List[ast.AST]:
        parents = []

        while node is not None:
            parents.append(node)
            node = get_parent(code, node, rebuild=True)

        return parents

    code = ast.parse('while True: pass')
    expected = [
        code,
        code.body[0],
        code.body[0].body[0],
    ]

    for i, node in enumerate(expected):
        assert get_parents(node)[::-1] == expected[:i + 1]



# Generated at 2022-06-14 03:11:31.589288
# Unit test for function find
def test_find():
    # AST Object for comarison
    class_ = ast.ClassDef(name='Test',
                          body=[ast.Pass()],
                          decorator_list=[],
                          keywords=[],
                          lineno=10,
                          col_offset=0)

    # AST Object for comarison
    function = ast.FunctionDef(name='test',
                               args=ast.arguments(args=[],
                                                  vararg=None,
                                                  kwonlyargs=[],
                                                  kw_defaults=[],
                                                  kwarg=None,
                                                  defaults=[]),
                               body=[ast.Pass()],
                               decorator_list=[],
                               returns=None,
                               lineno=11,
                               col_offset=0)

    # AST Object for comarison