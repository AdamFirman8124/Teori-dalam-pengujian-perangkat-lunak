

# Generated at 2022-06-14 03:01:41.438720
# Unit test for function find
def test_find():
    t = ast.parse('if a == 1:\n    a = 1\nelse:\n    a = 2')
    assert list(find(t, ast.If)) == [t.body[0]]
    assert list(find(t, ast.Compare)) == [t.body[0].test]
    assert list(find(t, ast.Assign)) == [t.body[0].body[0]] + \
        [t.body[1].body[0]]

# Generated at 2022-06-14 03:01:48.639475
# Unit test for function get_parent
def test_get_parent():
    # Arrange
    node1 = ast.Num(n=1)
    node2 = ast.Num(n=2)
    node3 = ast.Num(n=3)
    node4 = ast.Num(n=4)
    node5 = ast.Num(n=5)
    node6 = ast.Num(n=6)
    node7 = ast.Num(n=7)
    node8 = ast.Num(n=8)
    node4.n = node5
    node3.n = node4
    node2.n = node3
    node1.s = node2
    node1.n = node1.s
    node1.s = node6
  
    # Act
    get_parent(node1, node1)
    get_parent(node1, node2)
    get_parent

# Generated at 2022-06-14 03:01:54.629473
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse("""
        if a:
            print('a')
    """)

    def_stmt = get_closest_parent_of(tree, tree.body[0].body[0], ast.FunctionDef)
    assert def_stmt == None

if __name__ == "__main__":
    test_replace_at()

# Generated at 2022-06-14 03:01:55.123978
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    pass



# Generated at 2022-06-14 03:02:01.538734
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Unit test for function get_closest_parent_of."""
    from ast import parse
    from .generate import generate_code
    # Test for getting parents of FunctionDef node
    tree = parse('''
        a = 1
        def func(x=None):
            return x
    ''')
    node = tree.body[1]

    parent = get_parent(tree, node)
    assert generate_code(parent) == '''
        a = 1
        def func(x=None):
            return x
    '''

    parent = get_closest_parent_of(tree, node, ast.Module)
    assert generate_code(parent) == '''
        a = 1
        def func(x=None):
            return x
    '''

    parent = get_closest_parent_

# Generated at 2022-06-14 03:02:09.688108
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class_name = "Test"
    function_name = "test"
    class_node = ast.ClassDef(name=class_name, body=[], decorator_list=[])
    function_node = ast.FunctionDef(name=function_name, body=[],
                                    decorator_list=[])
    parent_node = class_node.body
    parent_node.append(function_node)

    result = get_non_exp_parent_and_index(class_node, function_node)

# Generated at 2022-06-14 03:02:13.305828
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    example_tree = ast.parse('test', mode='eval')
    node_1 = example_tree.body
    parent_1, index_1 = get_non_exp_parent_and_index(
        example_tree, node_1)
    assert parent_1 == example_tree
    assert index_1 == 0



# Generated at 2022-06-14 03:02:22.546216
# Unit test for function replace_at
def test_replace_at():
    t = ast.parse('a = 1\n'
                  'b = 2\n'
                  'c = 3')
    b = t.body[1]
    replace_at(1, t, ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
               value=ast.Name(id='y', ctx=ast.Load())))
    assert isinstance(t.body[2], ast.Assign)
    assert isinstance(t.body[2].value, ast.Name)
    assert t.body[2].value.id == 'y'
    assert isinstance(t.body[3], ast.Assign)

    replace_at(1, t, b)
    assert t.body[2] == b

# Generated at 2022-06-14 03:02:23.749365
# Unit test for function find

# Generated at 2022-06-14 03:02:24.423894
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:29.972490
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.Import([ast.alias("a", None)])
    parent = ast.Module([node])
    answer = node, 0
    assert get_non_exp_parent_and_index(parent, node) == answer

# Generated at 2022-06-14 03:02:34.017121
# Unit test for function find
def test_find():
    code = "i = 2 + 3"
    tree = ast.parse(code)
    _build_parents(tree)

    assert len(list(find(tree, ast.Expression))) == 1
    assert len(list(find(tree, ast.BinOp))) == 1



# Generated at 2022-06-14 03:02:43.460162
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = ast.parse("""
    def foo(a):
        b = a + 5
        return b
    """)

    # 'a + 5' is an expression
    # 'b = a + 5' is not
    parent_and_index = get_non_exp_parent_and_index(code, code.body[0].body[0].value)

    # The parent of 'b = a + 5' should be the
    # function body (a list) of 'foo'
    assert isinstance(parent_and_index[0], ast.FunctionDef) # type: ignore

    # The parent's index of 'b = a + 5' should be 0
    assert parent_and_index[1] == 0


# Unit tests for function find

# Generated at 2022-06-14 03:02:49.709403
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('def foo():\n  pass\n  pass')
    assert isinstance(get_closest_parent_of(tree, tree.body[0].body[0],
                                            ast.FunctionDef), ast.FunctionDef)


# pylint: disable=unused-argument

# Generated at 2022-06-14 03:02:55.847713
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    exp = ast.parse('1 + 1', mode='eval').body
    add = exp.op
    num1 = exp.left

    assert get_non_exp_parent_and_index(exp, num1) == (exp, 0)
    assert get_non_exp_parent_and_index(exp, add) == (exp, 1)

# Generated at 2022-06-14 03:03:09.510536
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    t = ast.parse("""
a = 1
b = 2
l = [1, 2, 3]
for i in l:
    print("Hello")
    print("World")
c = 3
    """)
    body = t.body
    print("Assignment a's parent:", get_closest_parent_of(t, body[0], ast.FunctionDef))
    print("Assignment b's parent:", get_closest_parent_of(t, body[1], ast.FunctionDef))
    print("Assignment l's parent:", get_closest_parent_of(t, body[2], ast.FunctionDef))
    print("for-loop i's parent:", get_closest_parent_of(t, body[3], ast.FunctionDef))

# Generated at 2022-06-14 03:03:16.191149
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    print(get_non_exp_parent_and_index(
        ast.parse("""a.b.c(
    1,
    d=2,
    *[1, 2, 3],
    e=4,
    **{1: 2, 3: 4}
)""", '<string>', mode='exec'),
        ast.parse("""d=2""", '<string>', mode='exec').body[0]
    ))


# Generated at 2022-06-14 03:03:17.084058
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:03:23.313290
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest
    import astor

    class TestGetClosestParentOf(unittest.TestCase):
        def test_get_closest_parent_of(self):
            tree = astor.parse_file('tests/fixtures/functions/foobar.py')
            node = tree.body[0]
            parrent = get_closest_parent_of(tree, node, ast.Module)
            assert isinstance(parrent, ast.Module)

    unittest.main()



# Generated at 2022-06-14 03:03:29.583179
# Unit test for function find
def test_find(): # type: ignore
    import unittest
    import astor

    class FindTest(unittest.TestCase):
        def test_basic(self):
            code = '''
x = 1
y = x + 1
                '''
            tree = ast.parse(code)  # type: ignore
            y = find(tree, ast.Name).next()
            x = find(tree, ast.Name).next()

            self.assertEqual(x.id, 'x')
            self.assertEqual(y.id, 'y')

    unittest.main()

if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:03:34.409108
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    test_ast = ast.parse('a = 1')
    parent = get_non_exp_parent_and_index(test_ast, test_ast.body[0].value)[0]
    assert parent.body[0].value.lineno == test_ast.body[0].value.lineno

# Generated at 2022-06-14 03:03:39.200549
# Unit test for function find
def test_find():
    program = ast.parse('a = 1\nx = a + 1\n')
    for name_node in find(program, ast.Name):
        name_node.id = "d"  # type: ignore
    assert ast.dump(program) == ast.dump(ast.parse('d = 1\nd = d + 1\n'))


# Generated at 2022-06-14 03:03:42.124569
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse(
        '''import antlr4\n'''
    )
    node = tree.body[0]
    res = get_closest_parent_of(tree, node, ast.AST)
    assert(res == tree)



# Generated at 2022-06-14 03:03:45.767144
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('a = 1')
    exp = tree.body[0].value
    parent, index = get_non_exp_parent_and_index(tree, exp)
    assert index == 0 and isinstance(parent, ast.Module)

# Generated at 2022-06-14 03:03:51.031453
# Unit test for function get_parent
def test_get_parent():
    source = ast.parse('if True: a = 1')
    if_stmt = source.body[0]  # type: ignore
    stmt = if_stmt.body[0]  # type: ignore
    ass = stmt.value  # type: ignore
    parent_for_ass = get_parent(source, ass)

    assert parent_for_ass is stmt


# Generated at 2022-06-14 03:03:51.603521
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pass

# Generated at 2022-06-14 03:03:52.565320
# Unit test for function get_parent

# Generated at 2022-06-14 03:04:01.096820
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("""
        def Test():
            a = (
                Test2(
                    Test3(
                        Test3(
                            Test3()
                        )
                    )
                )
            )
        """)

    assert get_closest_parent_of(tree, tree.body[0].body[0], ast.FunctionDef) == tree.body[0]
    assert get_closest_parent_of(tree, tree.body[0].body[0], ast.Module) == tree

    # Should raise because there is no parent
    try:
        get_closest_parent_of(tree, tree, ast.FunctionDef)
        assert False
    except:
        pass

# Generated at 2022-06-14 03:04:09.321090
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('x = 1 + 2')
    tree_children = ast.iter_child_nodes(tree)
    tree_child_one = next(tree_children)
    tree_child_one_children = ast.iter_child_nodes(tree_child_one)
    tree_child_one_child = next(tree_child_one_children)
    assert(get_parent(tree, tree_child_one_child) == tree_child_one)


# Generated at 2022-06-14 03:04:09.949345
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:04:32.304960
# Unit test for function find
def test_find():
    ast_ = ast.parse('1')
    mod = ast_.body[0]
    assert len(list(find(ast_, ast.Module))) == 1
    assert len(list(find(ast_, ast.Expr))) == 1
    assert len(list(find(ast_, ast.Num))) == 1

    # Replace module with Expr
    replace_at(0, mod, mod.body[0])
    assert len(list(find(ast_, ast.Module))) == 0
    assert len(list(find(ast_, ast.Expr))) == 1
    assert len(list(find(ast_, ast.Num))) == 1

# Generated at 2022-06-14 03:04:42.688103
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import parser
    import astunparse

    node = parser.parse("""
    def test_func():
        a = 1
        b = 2
        c = 3
    """, mode='exec')

    # Test that closest parent module is returned
    parent = get_closest_parent_of(node, node.body[0], ast.Module)
    assert astunparse.unparse(parent) == astunparse.unparse(node)

    # Test that closest parent funcdef is returned
    parent = get_closest_parent_of(node, node.body[0].body[0], ast.FunctionDef)
    assert astunparse.unparse(parent) == astunparse.unparse(
        node.body[0])

    # Test closest parent with no matching parent and assert that it raises
    # IndexError

# Generated at 2022-06-14 03:04:43.160448
# Unit test for function find
def test_find():
    pass

# Generated at 2022-06-14 03:04:56.003079
# Unit test for function find
def test_find():
    from .example_program import program as tree
    tree.vs_file_revision = 1
    tree.vs_file_id = 1
    tree.vs_dependencies = []
    tree.vs_dependency_edges = []
    import vs_ast.generators as gen
    tree = gen.generate_tree('def my_func(a):\n    print(a)')
    tree.vs_file_revision = 1
    tree.vs_file_id = 1
    tree.vs_dependencies = []
    tree.vs_dependency_edges = []
    for node in find(tree, ast.Assign):
        node.targets[0].id = 'nop'

# Generated at 2022-06-14 03:05:04.318281
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():

    # prepare AST Tree
    from typed_ast import ast3
    from . import transpile_ast

    tree = transpile_ast("""def foo():
                                bar = None
                                while bar < 5:
                                    bar = bar + 2
                                return bar""")
    tree = ast3.fix_missing_locations(tree)

    # try to get closest node of type FunctionDef
    node = get_closest_parent_of(tree, tree.body[0].body[0], ast3.FunctionDef)
    assert node.name == "foo"

    # try to get closest node of type While
    node = get_closest_parent_of(tree, tree.body[0].body[0], ast3.While)
    assert node.test.left.id == "bar" and node.test.ops

# Generated at 2022-06-14 03:05:06.515860
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:05:08.903857
# Unit test for function find
def test_find():
    prog = ast.parse('for i in range(10): print(i)')

    for stmnt in find(prog, ast.For):
        assert isinstance(stmnt, ast.For)



# Generated at 2022-06-14 03:05:17.124483
# Unit test for function get_parent
def test_get_parent():
    # build the tree for the test
    root = ast.Module()

    expr = ast.Expression()
    call = ast.Call()

    expr.body = call

    parent = ast.FunctionDef()
    parent.body = [expr]
    parent.name = 'test_func'

    root.body = [parent]

    # test the tree
    _build_parents(root)

    assert get_parent(root, expr) == call
    assert get_parent(root, call) == expr
    assert get_parent(root, parent) == root
    assert get_parent(root, root) == None

# Generated at 2022-06-14 03:05:17.862537
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:05:22.336032
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('\n'.join([
        'def test():',
        '    if True:',
        '        pass',
        '    if True:',
        '        pass',
        '    pass'
    ]))

    first_if = find(tree, ast.If).__next__()
    _, index = get_non_exp_parent_and_index(tree, first_if)
    assert index == 1

    second_if = find(tree, ast.If).__next__()
    _, index = get_non_exp_parent_and_index(tree, second_if)
    assert index == 3

# Generated at 2022-06-14 03:05:58.492882
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class A(ast.AST): pass
    class B(ast.AST): pass
    class C(ast.AST): pass

    node = B()
    a = A()
    c = C()
    a.child = node
    node.child = c

    assert get_closest_parent_of(node, node.child, A) == a

# Generated at 2022-06-14 03:06:02.136095
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index(): # pragma: no cover
    exp = ast.Expr(value=ast.Num(n=1))
    parent, index = get_non_exp_parent_and_index(exp, exp)
    assert isinstance(parent, ast.Module)
    assert index == 0

# Generated at 2022-06-14 03:06:03.574621
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:06:16.741286
# Unit test for function get_parent
def test_get_parent():
    """Unit test for function get_parent."""
    import astor
    from datetime import datetime
    from random import random
    from unittest import TestCase

    start_time = datetime.now()
    times = 0

    class TestGetParent(TestCase):
        """Test get parent function."""

        def test_get_parent(self):
            """Test get parent function."""
            for _ in range(1000):
                times += 1
                tree = ast.parse(astor.to_source(random))
                test_node = get_parent(tree, tree.body[0])
                self.assertEqual(test_node, tree)

    TestGetParent().test_get_parent()
    print('{} {}'.format(datetime.now() - start_time, times))

# Generated at 2022-06-14 03:06:29.381647
# Unit test for function get_parent
def test_get_parent():

    node1 = ast.parse("""{'x': x}""").body[0].value
    node2 = ast.parse("""{'x': x}""").body[0].value.key
    node3 = ast.parse("""{'x': x}""").body[0].value.value
    node4 = ast.parse("""{'x': x}""").body[0].value.keys()[0]
    node5 = ast.parse("""{'x': x}""").body[0].value.items()[0]
    node6 = ast.parse("""{'x': x}""").body[0].value.items()[0][0]
    node7 = ast.parse("""{'x': x}""").body[0].value.items()[0][1]


# Generated at 2022-06-14 03:06:32.736165
# Unit test for function find
def test_find():
    def func():
        pass

    _, tree = ast.parse(func)
    assert list(find(tree, ast.FunctionDef)) == [tree.body[0]]


# Generated at 2022-06-14 03:06:33.587469
# Unit test for function find

# Generated at 2022-06-14 03:06:34.546038
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    p = ast.parse('x = 1')
    0

# Generated at 2022-06-14 03:06:35.633681
# Unit test for function find
def test_find():
    import astor

# Generated at 2022-06-14 03:06:42.309717
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(ast.parse('1'), ast.parse('1').body[0].value, ast.Module) == ast.parse('1')
    assert get_closest_parent_of(ast.parse('[]'), ast.parse('[]').body[0].value, ast.Expr) == ast.parse('[]').body[0]

# Generated at 2022-06-14 03:07:49.845166
# Unit test for function get_parent
def test_get_parent():
    class A(ast.AST):
        pass

    class B(ast.AST):
        pass

    class C(ast.AST):
        pass

    class D(ast.AST):
        pass

    node_a = A()
    node_b = B()
    node_c = C()
    node_d = D()
    node_a.body = [node_b]  # type: ignore
    node_b.body = [node_c, node_d]  # type: ignore

    assert get_parent(node_a, node_a) == None
    assert get_parent(node_a, node_b) == node_a
    assert get_parent(node_a, node_c) == node_b
    assert get_parent(node_a, node_d) == node_b

# Generated at 2022-06-14 03:07:53.318899
# Unit test for function find
def test_find():
    a = ast.parse('class A: pass')
    b = find(a, ast.ClassDef)
    assert next(b) is a.body[0]



# Generated at 2022-06-14 03:07:57.562553
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    with open('tests/data/test.py') as f:
        tree = ast.parse(f.read())
    func = get_closest_parent_of(tree, tree.body[2].body[1].body[1],
                                 ast.FunctionDef)
    assert func.name == 'test'



# Generated at 2022-06-14 03:08:02.443897
# Unit test for function get_parent
def test_get_parent():
    sample_code = "a = 0\nb = 1\n"
    tree = ast.parse(sample_code)
    print("original code:\n", sample_code)
    for node in ast.walk(tree):
        print("\nparent of:\n", node, " is\n", get_parent(tree, node), "\n")


# Generated at 2022-06-14 03:08:15.239192
# Unit test for function get_parent
def test_get_parent():
    root_node = ast.FunctionDef(
        name='example',
        args=ast.arguments(
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[]
                ),
        body=[
            ast.Pass(),
            ast.Pass()
        ],
        decorator_list=[],
        returns=None
    )
    assert(get_parent(root_node, root_node) is None)
    assert(get_parent(root_node, root_node.body[0]) == root_node)
    assert(get_parent(root_node, root_node.body[1]) == root_node)
    assert(get_parent(root_node, root_node.name) is None)

# Generated at 2022-06-14 03:08:26.164127
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('''\
function outer() {
    function inner() {
        console.log('inner');
    }

    for(var i = 0; i < 10; i++) {
        inner();
    }
}

function myFunction() {
    function inner() {
        console.log('inner');
    }

    function inner2() {
        inner();
    }

    inner2();
}
    ''')

    inner = tree.body[1].body[1].orelse[0]  # type: ignore
    closest_parent_of = get_closest_parent_of(tree, inner, ast.For)
    assert get_parent(tree, closest_parent_of) == tree.body[1]  # type: ignore


# TODO(davit): rewrite tests with doct

# Generated at 2022-06-14 03:08:31.064691
# Unit test for function find
def test_find():  # pylint: disable=missing-docstring
    tree = ast.parse('x = 1 + 2 + 3')
    assert len(list(find(tree, ast.Add))) == 2



# Generated at 2022-06-14 03:08:37.517117
# Unit test for function find
def test_find():
    import astor

    def f() -> None:
        a = 1
        b = 2
        a = a + b
        print(a)
        print(b)

    root = ast.parse(f.__code__)
    assert len(list(find(root, ast.Name))) == 6



# Generated at 2022-06-14 03:08:43.955743
# Unit test for function find
def test_find():
    node = ast.parse(
        'def f():\n'
        '    return lambda: 0'
    )

    functions = list(find(node, ast.FunctionDef))
    lambdas = list(find(node, ast.Lambda))

    assert len(functions) == 1
    assert functions[0].name == 'f'

    assert len(lambdas) == 1
    assert isinstance(lambdas[0].body, ast.Num)

# Generated at 2022-06-14 03:08:45.511582
# Unit test for function get_parent