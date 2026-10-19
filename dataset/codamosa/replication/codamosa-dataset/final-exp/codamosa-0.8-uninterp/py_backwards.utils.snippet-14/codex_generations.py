

# Generated at 2022-06-14 02:50:43.760573
# Unit test for function find_variables

# Generated at 2022-06-14 02:50:51.397626
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x: List[int]) -> int:
        let(y)
        y += 1
        return y

    test_snippet.__annotations__['return'] = int

    # test_snippet.__annotations__['x'] = List[int]  # type: ignore

    ast_body = snippet(test_snippet).get_body(x=[0, 0])
    result = compile(ast.Module(ast_body), '<string>', 'exec')
    globals_dict = locals()
    exec(result, globals_dict, locals_dict=locals())
    assert locals()['_py_backwards_y_0'] == 1



# Generated at 2022-06-14 02:50:59.947632
# Unit test for function find_variables
def test_find_variables():
    source = """
        x = 1
        let(y)
        let(z)
        print(z)
        """
    tree = ast.parse(source)
    variables = list(find_variables(tree))
    assert variables == ['y', 'z']
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id=x, ctx=Store())], value=Num(n=1)), Print(dest=None, values=[Name(id=z, ctx=Load())])])'



# Generated at 2022-06-14 02:51:09.974141
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import numpy as np

    x = np.array([0, 1])
    y = np.array([1, 2])
    z = np.array([2, 3])

    @snippet
    def snippet_example():
        let(x)
        let(y)
        x += y

    expected = [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Name(id='_py_backwards_y_1', ctx=ast.Load()),
            ),
        ),
    ]
    assert snippet

# Generated at 2022-06-14 02:51:22.070854
# Unit test for function find_variables
def test_find_variables():
    import unittest

    class TestLet(unittest.TestCase):
        def test_multiple_lets(self) -> None:
            source = '''
let(x)
x += 1
let(y)
y -= 2
z = x + y
'''
            tree = ast.parse(source)
            names = list(find_variables(tree))
            self.assertEqual(['x', 'y'], names)

        def test_multiple_variable_names(self) -> None:
            source = '''
let(a)
a += 1
let(b)
b -= 2
c = a + b
'''
            tree = ast.parse(source)
            names = list(find_variables(tree))
            self.assertEqual(['a', 'b'], names)


# Generated at 2022-06-14 02:51:30.871693
# Unit test for function find_variables
def test_find_variables():
    variables_list = [
        let(x)
        for x in [
            1, 2, 3
        ]
    ]

    variables_dict = {
        let(key): let(value)
        for key, value in {
            'foo': 'bar',
            'asdf': 'fdsa',
        }
    }

    tree = ast.parse('x = let(x)\nprint(y)')
    variables = find_variables(tree)
    assert set(variables) == {'x', 'y'}



# Generated at 2022-06-14 02:51:41.263269
# Unit test for function find_variables
def test_find_variables():
    # pylint: disable=expression-not-assigned
    assert set(find_variables('x')) == set(['x'])
    assert set(find_variables('let(a) a')) == set(['a'])
    assert set(find_variables('a;let(a);b')) == set(['a'])
    assert set(find_variables('a;let(b);let(a);a')) == set(['a', 'b'])
    assert set(find_variables('let(b);let(a);a')) == set(['a', 'b'])
    assert set(find_variables('let(b);let(a);let(b)')) == set(['a', 'b'])

# Generated at 2022-06-14 02:51:47.793083
# Unit test for function extend_tree
def test_extend_tree():
    vars = [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(n=1),
        type_comment=None),
            ast.Assign(
                targets=[ast.Name(id='x', ctx=ast.Store())],
                value=ast.Num(n=2),
                type_comment=None)]
    tree = ast.parse('extend(vars)\nprint(x)')
    extend_tree(tree, {'vars': vars})
    test = ast.parse('x = 1\nx = 2\nprint(x)')

    def assert_equals(n1, n2):
        assert isinstance(n1, n2.__class__)

# Generated at 2022-06-14 02:51:57.718474
# Unit test for function extend_tree
def test_extend_tree():
    def snippet():
        let(x)
        extend(vars)

    source = get_source(snippet)
    tree = ast.parse(source)
    vars = [ast.parse('x = 1').body[0], ast.parse('x = 2').body[0]]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:51:59.036313
# Unit test for function find_variables
def test_find_variables():
    source = 'let(x) x = 1'
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x']

# Generated at 2022-06-14 02:52:15.117706
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 0
    b = 0

    @snippet
    def s():
        a += 1
        let(b)
        b += a
        return a + b

    tree = s.get_body()
    assert len(tree) == 4
    assert isinstance(tree[2], ast.Assign)
    assert isinstance(tree[2].targets[0], ast.Name)
    assert tree[2].targets[0].id == 'b'  # type: ignore
    assert isinstance(tree[3], ast.Return)
    assert tree[3].value.left.id == 'a'  # type: ignore
    assert tree[3].value.right.id == 'b'  # type: ignore


# Generated at 2022-06-14 02:52:23.042965
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

# Generated at 2022-06-14 02:52:24.015484
# Unit test for function extend_tree

# Generated at 2022-06-14 02:52:31.864004
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _test(fn, expected):
        actual = snippet(fn).get_body()
        assert actual == expected

    def fn():
        let(x)
        x += 1
        y = 1

    expected = [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.BinOp(op=ast.Add(),
                        left=ast.Name(id='x', ctx=ast.Load()),
                        right=ast.Num(n=1)),
        type_comment=None),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1),
            type_comment=None)]
    _test(fn, expected)


# Generated at 2022-06-14 02:52:37.617295
# Unit test for function extend_tree
def test_extend_tree():
    my_dict = {'p': ast.parse("x = 'test'").body[0],
               'q': ast.parse("x = 'test2'").body[0]}
    parse_tree = ast.parse("extend(p)\nextend(q)")
    extend_tree(parse_tree, my_dict)
    assert parse_tree.body == my_dict.values()



# Generated at 2022-06-14 02:52:38.574311
# Unit test for function extend_tree

# Generated at 2022-06-14 02:52:48.507340
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse(dedent(
        """
        extend(vars)
        def f():
            x = 2
        """
    ))
    vars = [ast.Assign([ast.Name('x', ast.Store())], ast.Num(1))]
    extend_tree(tree, {'vars': vars})
    assert len(tree.body) == 3
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[1], ast.Assign)
    assert isinstance(tree.body[2], ast.FunctionDef)
    assert tree.body[0].targets[0].id == 'x'
    assert tree.body[0].value.n == 1
    assert tree.body[1].targets[0].id == 'x'
   

# Generated at 2022-06-14 02:52:53.796253
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    let(x)
    let(y)
    for i in range(x):
        x -= 1
    for j in range(y):
        y -= 1
    """)

    assert set(find_variables(tree)) == {'x', 'y'}

# Generated at 2022-06-14 02:52:54.403817
# Unit test for function extend_tree

# Generated at 2022-06-14 02:52:59.782655
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def method(x: int) -> int:
        extend(x + 1)
        return let(x + 1)

    assert snippet(method).get_body(x=1) == ast.parse(
        '_py_backwards_x_0 = 1\n_py_backwards_x_0 = 2\nreturn _py_backwards_x_0 + 1').body  # type: ignore



# Generated at 2022-06-14 02:53:11.453750
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def s():
        let(x)
        x += 1

    assert s.get_body() == [  # type: ignore
        ast.Assign(  # type: ignore
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],  # type: ignore
            value=ast.BinOp(  # type: ignore
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),  # type: ignore
                op=ast.Add(),  # type: ignore
                right=ast.Num(n=1)))]  # type: ignore

    @snippet
    def s():
        let(x)
        z = x


# Generated at 2022-06-14 02:53:21.611563
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snp(x: int, y: int = 2) -> int:
        let(z)
        return x + y + z


# Generated at 2022-06-14 02:53:25.543557
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 5
    y = 4

    @snippet
    def f(**kwargs):
        let(x)
        x += 1
        z = y + x
        print(z)

    tree_body = f.get_body()

    assert tree_body
    assert len(tree_body) == 2
    assert tree_body[1].value.left.value.id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:53:35.661413
# Unit test for function extend_tree
def test_extend_tree():
    vars = ast.Module(body=[
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Constant(value=1),
        ),
    ])
    tree = ast.Module(body=[
        ast.Expr(value=ast.Call(
            func=ast.Name(id='extend', ctx=ast.Load()),
            args=[ast.Name(id='_py_unittest_0', ctx=ast.Load())],
            keywords=[],
        )),
        ast.Print(dest=None, values=[ast.Name(id='x', ctx=ast.Load())], nl=True),
    ])
    extend_tree(tree, {'_py_unittest_0': vars})
    result = ast

# Generated at 2022-06-14 02:53:43.791832
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x: int, y: int) -> int:
        let(z)
        return x + y + z

    from .transform import run, Transform

    class MyTransformer(Transform):
        inputs = (snippet.get_body(x=ast.Name(id='c1'), y=ast.Name(id='c2')),)
        outputs = (ast.Name(id='c3', ctx=ast.Load()),)

    code = run(MyTransformer)

    def test_snippet_with_run(x, y):
        let(z)
        return code(x, y, z)

    assert test_snippet_with_run(1, 2) == 1 + 2 + 3

# Generated at 2022-06-14 02:53:51.402926
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""extend(x)
                        print(x)""")

    x = ast.parse("""x = 1
                     x = 2""")

    extend_tree(tree, {'x': x})

    assert ast.dump(tree) == """Module(body=[x = 1,
 x = 2,
 Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]))])"""


# Generated at 2022-06-14 02:54:06.949716
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .testing import run_assert
    def test(a, b, c):
        let(d)
        a = b + c
        d = 3
        return a + d
    snippet_ = snippet(test)

# Generated at 2022-06-14 02:54:13.416491
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x):
        let(x)
        x += 1
        y = 1
        extend(vars)

    assert test.get_body().__repr__() == '[Assign(targets=[Name(id=py_backwards_x_0_0, ctx=Store())], value=BinOp(left=Name(id=py_backwards_x_0_0, ctx=Load()), op=Add(), right=Num(n=1))), Assign(targets=[Name(id=y, ctx=Store())], value=Num(n=1))]'

# Generated at 2022-06-14 02:54:24.772057
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    print("Snippet get body:")
    def inner_func(x: int, y: int):
        let(a)
        let(b)
        let(c)
        extend(vars1)
        extend(vars2)
        extend(vars3)
        c += 1
        return a, c, x, y

    # imports, variables, assignments

# Generated at 2022-06-14 02:54:31.430686
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet(x, y):
        let(x)
        x += 1
        let(y)
        y -= 1


# Generated at 2022-06-14 02:54:41.929337
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test snippet.get_body method."""

    @snippet
    def fn(a: int, b: int, c: int) -> int:
        let(x)
        let(y)
        let(z)
        x = a
        z = x + 2
        y = z
        return x

    body = fn.get_body(a=1, b=3, c=3)
    assert isinstance(body, list)
    assert len(body) == 3

    x_assign = body[0]
    assert isinstance(x_assign, ast.Assign)
    assert len(x_assign.targets) == 1
    assert x_assign.targets[0].id == '_py_backwards_x_0'

    y_assign = body[1]


# Generated at 2022-06-14 02:54:51.218178
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: let(x)).get_body(x=1) == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]

    # Multiple assignments

# Generated at 2022-06-14 02:54:53.409457
# Unit test for function extend_tree
def test_extend_tree():
    assert eval(get_source(extend_tree).replace('extend_tree', 'test_extend_tree')) == 'ok'



# Generated at 2022-06-14 02:55:03.504523
# Unit test for function extend_tree
def test_extend_tree():
    source_1 = '''
    a = 1
    b = 2
    extend(vars)
    c = 3
    d = 4
    '''
    tree_1 = ast.parse(source_1)
    extend_tree(tree_1, {'vars': [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                                             value=ast.Num(n=12))]})
    assert astor.to_source(tree_1) == '''
    a = 12
    b = 2
    c = 3
    d = 4
    '''

    source_2 = '''
    a = 1
    b = 2
    extend(vars)
    extend(vars_2)
    c = 3
    d = 4
    '''


# Generated at 2022-06-14 02:55:14.199989
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    counter: int = 0
    text = 'blabla'

    @snippet
    def test_function(x: int, y: float, z: float = 2.3, name: str = text) -> None:
        let(counter)
        counter += 1

    body = test_function.get_body()
    assert body == [ast.Assign(
        targets=[ast.Name(id='_py_backwards_counter_0',
                          ctx=ast.Store())],
        value=ast.BinOp(
            left=ast.Name(id='_py_backwards_counter_0',
                          ctx=ast.Load()),
            op=ast.Add(),
            right=ast.Num(n=1)))
    ]



# Generated at 2022-06-14 02:55:24.261697
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_f():
        let(x)
        x += 1
        y = 1
        extend(vars1)
        extend(vars2)

    snippet_obj = snippet(test_f)
    ast_objects = snippet_obj.get_body()

    assert len(ast_objects) == 4
    assert ast_objects[0].__class__.__name__ == 'AugAssign'
    assert ast_objects[1].__class__.__name__ == 'Assign'
    assert ast_objects[2].__class__.__name__ == 'Assign'
    assert ast_objects[3].__class__.__name__ == 'Assign'
    assert isinstance(ast_objects[0].target, ast.Name)

# Generated at 2022-06-14 02:55:30.516750
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = get_source(test_snippet_get_body)
    tree = ast.parse(source)
    snippet_kwargs = find_variables(tree)
    #assert snippet_kwargs == {'x': ast.Num(1)}
    assert snippet_kwargs == {'x': ast.NameConstant(value=1)}


# Generated at 2022-06-14 02:55:38.445526
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def function():
        x = let(1)
        x += x + 1
        y = 2
    source = get_source(function)
    tree = ast.parse(source)
    variables = find_variables(tree)
    extend_tree(tree, variables)
    variables = {name: VariablesGenerator.generate(name)
                 for name in variables}
    result_body = VariablesReplacer.replace(tree.body[0], variables).body
    assert function.get_body() == result_body

# Generated at 2022-06-14 02:55:42.848439
# Unit test for function extend_tree
def test_extend_tree():
    source = '''
        extend(snippet)
        assert 1 == 2
    '''
    tree = ast.parse(source)
    variables = {'snippet': ast.parse('let(x)')}
    extend_tree(tree, variables)
    assert tree.body[0].body[0].value.args[0].id == 'x'

# Generated at 2022-06-14 02:55:45.141752
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet():
        let(x)
        x += 1

    tree = test_snippet.get_body()
    assert len(tree) == 1



# Generated at 2022-06-14 02:55:54.531130
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_fn(a: int, b: int) -> int:
        let(x)
        z = x + 1
        return z
    snippet_object = snippet(test_fn)
    snippet_body = snippet_object.get_body(x=2)
    assert snippet_body[0].targets[0].id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:56:03.117485
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo_snippet(x: int, y: str = '1'):
        let(x)
        extend(_vars)
        print(x, y)

    _vars = [
        ast.Assign(
            [ast.Name('x', ast.Store())],
            ast.Num(1),
        ),
        ast.Assign(
            [ast.Name('x', ast.Store())],
            ast.Num(2),
        ),
    ]

    body = foo_snippet.get_body(x=100, y='2', _vars=_vars)

    assert len(body) == 4

    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].targets[0], ast.Name)
    assert body

# Generated at 2022-06-14 02:56:11.385393
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    if a:
        extend(a)
        pass
    """
    tree = ast.parse(source)
    assignments = [
        ast.Assign(
            [ast.Name('x', ast.Store())],
            ast.Num(10)
        ),
        ast.Assign(
            [ast.Name('y', ast.Store())],
            ast.Num(20)
        )
    ]
    extend_tree(tree, {'a': assignments})
    assert get_source(tree) == '\nif a:\n    x = 10\n    y = 20\n    pass'

# Generated at 2022-06-14 02:56:24.320553
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f():
        let(foo)
        let(bar)
        spam = 'egg'
        ham = 'egg'
        foo += 10
        y = foo
        return (foo, y)

    tree = f.get_body()
    assert get_source(tree) == '''\
_py_backwards_foo_0 += 10
y = _py_backwards_foo_0
return (_py_backwards_foo_0, y)
'''

    tree = f.get_body(bar=42, spam='ham')
    assert get_source(tree) == '''\
_py_backwards_foo_1 += 10
y = _py_backwards_foo_1
return (_py_backwards_foo_1, y)
'''



# Generated at 2022-06-14 02:56:33.244305
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 0
    b = ''
    c = False
    

# Generated at 2022-06-14 02:56:40.502428
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    global x
    global y
    x = 1
    y = x + 1
    print(x, y)

    tree = snippet(test_snippet_get_body).get_body()
    assert len(tree) == 3
    assert isinstance(tree[0], ast.Assign)
    assert isinstance(tree[1], ast.Assign)
    assert isinstance(tree[2], ast.Expr)
    assert tree[0].value.n == 1  # type: ignore
    assert tree[1].value.n == 2  # type: ignore



# Generated at 2022-06-14 02:56:49.717852
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_test(x: int, y: int, z: int) -> None:
        let(x)
        x += 1
        y = 1
        extend(z)

    tree = snippet(snippet_test).get_body(x=ast.Name(id='_x'),
                                          y=ast.Name(id='_y'),
                                          z=[ast.Assign([ast.Name(id='_x',
                                                                  ctx=ast.Store())],
                                                        ast.Num(n=1)),
                                              ast.Assign([ast.Name(id='_x',
                                                                  ctx=ast.Store())],
                                                        ast.Num(n=2))])

# Generated at 2022-06-14 02:56:54.071030
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(a); let(b); let(c)')
    assert set(find_variables(tree)) == {'a', 'b', 'c'}



# Generated at 2022-06-14 02:56:58.307212
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet = '''
x = 1
x + 1
'''
    result = '''
py_backwards_x_0 = 1
py_backwards_x_0 + 1
'''
    ast1 = ast.parse(snippet)
    ast2 = ast.parse(result)
    s = snippet(lambda x: None)  # type: ignore
    assert s.get_body(x=ast1.body[0].value) == ast2.body[0:2]
    


# Generated at 2022-06-14 02:57:07.220170
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    class A:
        def __init__(self, x):
            self.x = x
    a = A(5)
    def method(x, y):
        return x + y

# Generated at 2022-06-14 02:57:25.991538
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def sn(x):
        let(y)
        extend(y)
    assert isinstance(sn.get_body(x=1, y=[ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())], value=ast.Num(n=1),)]), list)

# Generated at 2022-06-14 02:57:36.520891
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_method(x: int, y: int) -> int:
        let(x)
        x += y
        return x

    assert snippet(snippet_method).get_body(y=1) == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                   value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                   op=ast.Add(),
                                   right=ast.Num(n=1)))
               ]

# Generated at 2022-06-14 02:57:43.437746
# Unit test for function find_variables
def test_find_variables():
    assert(['x', 'y'] ==
           find_variables(ast.parse("""let(x)
let(y)""")))
    assert(['x'] ==
           find_variables(ast.parse("""let(x)
x = 1""")))
    assert(['y', 'z'] ==
           find_variables(ast.parse("""let(y)
let(z)
y = 1""")))
    assert([] ==
           find_variables(ast.parse("""let(y)
let(z)
y = 1
z = 2""")))



# Generated at 2022-06-14 02:57:52.199678
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    let = lambda x: None
    extend = lambda x: None

    @snippet
    def my_snippet():
        let(x)
        x += 1

    tree = my_snippet.get_body()
    assert isinstance(tree, list)
    assert len(tree) == 1
    assert isinstance(tree[0], ast.AugAssign)
    assert isinstance(tree[0].value, ast.Num)
    assert tree[0].value.n == 1

# Generated at 2022-06-14 02:58:01.611140
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def with_let_and_extend(x, y):
        let(x)
        x += 1
        y = 1
        extend(vars)

    def without_let_and_extend(x, y):
        x += 1
        y = 1
        extend(vars)

    vars = [ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                       ast.Num(n=1)),
            ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                       ast.Num(n=2))]

    snippet_with_let_and_extend = snippet(with_let_and_extend)
    snippet_without_let_and_extend = snippet(without_let_and_extend)

    body_with_let_and

# Generated at 2022-06-14 02:58:13.589965
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Unit test for method get_body of class snippet"""

    import ast

    # Test with extend
    @snippet
    def a(x: int):
        extend(vars)
        print(x)
    vars = ast.parse('y = 1').body
    a.get_body(vars=vars)
    # Output: [Assign(targets=[Name(id='y', ctx=Store())], value=Num(n=1)),
    # Print(dest=None, values=[Name(id='x', ctx=Load())], nl=True)]

    # Test with let
    @snippet
    def b(y: bool):
        let(x)
        x += 1
        print(x, y)
    b.get_body(y=True)
    # Output: [Ass

# Generated at 2022-06-14 02:58:25.225915
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    let_x = ast.Name(id='_py_backwards_x_0', ctx=ast.Load())
    let_y = ast.Name(id='_py_backwards_y_1', ctx=ast.Load())

    @snippet
    def f(**snippet_kwargs):
        """
        let(x)
        x += 1
        y = 1
        """

    body = f.get_body(x=let_x, y=let_y)


# Generated at 2022-06-14 02:58:32.713069
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(a: int, b: int) -> int:
        let(x)
        return x + a + b

    snippet_fn = snippet(fn)
    tree = ast.parse("print(1 + 1)")
    variables = {
        "a": tree.body[0].value,
        "x": ast.Str("Ok")
    }
    body = snippet_fn.get_body(**variables)
    assert len(body) == 1, "fn body should have one expression"
    assert body[0].value.s == "Ok", "fn body should have 'Ok' as expression value"

# Generated at 2022-06-14 02:58:45.106313
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    if __name__ == '__main__':
        @snippet
        def test_function(x: str, **kwargs: str) -> None:
            """This function is example of snippet usage.
            
            x should be string and keyword arguments should be string too.
            """
            y = 'abc'
            let(z)
            x += y + z
            return x

        @snippet
        def test_function2(x: str, y: ast.AST, **kwargs: str) -> None:
            """This function is example of snippet usage.
            
            x should be string and keyword arguments should be string too.
            """
            extend(y)
            return x

        tree = test_function.get_body(x='abc', z=1, **{'kwargs': 1})

# Generated at 2022-06-14 02:58:45.664505
# Unit test for function find_variables

# Generated at 2022-06-14 02:59:09.828971
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_test():
        let(x)
        y = 1
        x += 1
        return x, y
    assert snippet(snippet_test).get_body() == snippet_test.__code__.co_consts[1]

# Generated at 2022-06-14 02:59:16.477232
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
let(x)
let(y)

if y:
    x += 1
    let(z)
    for i in range(10):
        z = i

print(x, y, z)''')

    variables = {var: VariablesGenerator.generate(var) for var in ['x', 'y', 'z']}
    VariablesReplacer.replace(tree, variables)
    assert get_source(tree) == '''\
if _py_backwards_y_0:
    _py_backwards_x_0 += 1
    for i in range(10):
        _py_backwards_z_0 = i

print(_py_backwards_x_0, _py_backwards_y_0, _py_backwards_z_0)'''

# Generated at 2022-06-14 02:59:24.426175
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(x):
        let(y)
        extend(z)
        return y
    t = snippet(foo)
    res = t.get_body(y="Hello", z=ast.copy_location(ast.Name("World", ast.Load()), y))
    assert isinstance(res, list)
    assert len(res) == 1
    assert isinstance(res[0], ast.Return)
    assert isinstance(res[0].value, ast.Name)
    assert res[0].value.id == "World"

# Generated at 2022-06-14 02:59:29.506012
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var = ast.Name('foo')
    def main():
        let(var)
        var.id = 'aaa'

    snippet = Snippet(main)
    body = snippet.get_body()
    assert body == [
        ['_py_backwards_foo_0.id', '=', 'aaa'],
    ]

# Generated at 2022-06-14 02:59:39.939531
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import source
    import inspect

    def func():
        x = "initial"
        y = 1
        let(x)
        x = "modified"
        z = y + 1
        x = "dont replace"
        extend(x)

    snippets = snippet(func)
    x = ast.parse(source(lambda: 'x = "modified x"')).body[0]

    assert 'dont replace' not in source(lambda: snippets.get_body(x=x))
    assert 'modified x' in source(lambda: snippets.get_body(x=x))
    assert 'x' in source(lambda: snippets.get_body())
    assert 'y' in source(lambda: snippets.get_body())
    assert 'z' in source(lambda: snippets.get_body())
    assert '+= 1'

# Generated at 2022-06-14 02:59:43.284033
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        let(x)
        let(y)
        x = 1
        y = 2
    """)
    result = find_variables(tree)
    assert set(result) == {'x', 'y'}



# Generated at 2022-06-14 02:59:58.819769
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    real_y = 0

    @snippet
    def test(x, y):
        let(x)
        x += 1
        extend(y)
        return x

    x = ast.Name(id="x")
    let(x)
    x += 1
    y = ast.Assign(targets=[ast.Name(id="real_y", ctx=ast.Store())], value=ast.Constant(value=1))
    extend(y)

# Generated at 2022-06-14 03:00:07.246786
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('''
let(vars)
extend(vars)
''')
    variables = {
        'vars': [
            ast.Assign(targets=[ast.Name('x', ast.Store())], value=ast.Num(1)),
            ast.Assign(targets=[ast.Name('x', ast.Store())], value=ast.Num(2))
        ],
    }
    extend_tree(tree, variables)
    assert ast.dump(tree) == ast.dump(ast.parse('''
x = 1
x = 2
'''))

# Generated at 2022-06-14 03:00:12.348487
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from py_backwards.transformers import remove_absolute_import
    from .transformers import remove_from_import
    from .helpers import ast_to_source
    for transformer in [remove_absolute_import, remove_from_import]:
        ast3 = transformer.snippets[0].get_body()
        ast_eq = lambda x, y: ast_to_source(x) == ast_to_source(y)
        assert ast_eq(ast3, transformer.ast3)

# Generated at 2022-06-14 03:00:20.977676
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_get_body(x: int, y: int) -> ast.AST:
        """ This is docstring.
        Let's test it.
        """
        let(x)
        x += 1
        y = 1
        return x

    expected = '''
x = 1
x = 2
x += 1
y = 1
return x
'''
    tree = ast.parse(expected)
    assert test_get_body.get_body(x=1, y=2) == tree.body  # type: ignore
    assert len(test_get_body.get_body(x=1, y=2)) == 4

