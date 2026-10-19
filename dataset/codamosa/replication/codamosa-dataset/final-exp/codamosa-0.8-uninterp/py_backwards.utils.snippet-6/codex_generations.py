

# Generated at 2022-06-14 02:50:17.405001
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    extend(vars)
    """
    tree = ast.parse(source)
    vars = [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1),
        ),
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=2),
        ),
    ]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:50:18.802344
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:50:28.486837
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_test(x, y=2, *args):
        let(x)
        x += 1
        y = 1
        extend(args)
    body = snippet(snippet_test).get_body(
        x=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
        args=[
            ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())],
                       value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())],
                       value=ast.Num(n=2)),
        ]
    )

# Generated at 2022-06-14 02:50:31.916762
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def body():
        let(x)
        x += 1
        y = 1

    assert body.get_body() == [
        ast.parse('_py_backwards_x_0 += 1').body[0],
        ast.parse('y = 1').body[0],
    ]



# Generated at 2022-06-14 02:50:44.410481
# Unit test for function extend_tree

# Generated at 2022-06-14 02:50:52.433424
# Unit test for function find_variables
def test_find_variables():
    # import from
    tree = ast.parse("from test import x\n")
    assert list(find_variables(tree)) == ['x']
    tree = ast.parse("from test import (x, y, z)\n")
    assert list(find_variables(tree)) == ['x', 'y', 'z']
    tree = ast.parse("from test import x as z\n")
    assert list(find_variables(tree)) == ['x']
    tree = ast.parse("from test import x, y as z\n")
    assert list(find_variables(tree)) == ['x', 'y']
    tree = ast.parse("from test import (x, y as z)\n")
    assert list(find_variables(tree)) == ['x', 'y']

    # import

# Generated at 2022-06-14 02:51:02.636297
# Unit test for function find_variables
def test_find_variables():
    assert find_variables(ast.Call(ast.Name('let', None),
                                   [ast.Name('x', None)],
                                   [])) == ['x']
    assert find_variables(ast.Expr(ast.Call(ast.Name('let', None),
                                            [ast.Name('x', None)],
                                            []))) == ['x']
    assert find_variables(ast.Call(ast.Call(ast.Name('let', None),
                                            [ast.Name('x', None)],
                                            []),
                                   [ast.Num(0)],
                                   [])) == ['x']

# Generated at 2022-06-14 02:51:07.748658
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
        extend(vars)
        print(x, y)
    """)
    vars = ast.parse("""
        x = 1
        x = 2
    """)
    extend_tree(tree, {'vars': vars})
    assert tree.body == vars.body + [ast.parse("print(x, y)").body[0]]



# Generated at 2022-06-14 02:51:10.286033
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)
    """
    tree = ast.parse(source)
    assert find_variables(tree) == ['x', 'y']



# Generated at 2022-06-14 02:51:22.354337
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 0
    y = let(0)
    @snippet
    def f():
        extend(ast.parse('x = 1'))
        extend(ast.parse('x = 2'))
        print(x, y)

# Generated at 2022-06-14 02:51:38.194985
# Unit test for function find_variables
def test_find_variables():
    source = """
        def f(x):
            let(y)
            let(z)
            return x + y + z
    """
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'y', 'z'}



# Generated at 2022-06-14 02:51:46.643791
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    c = let(a)
    d = let(b)
    e = extend(d)

    def f():
        a = 1
        c
        d
        e
        b

    f()


# Generated at 2022-06-14 02:51:51.491489
# Unit test for function find_variables
def test_find_variables():
    source = '''
        let(vars)
        extend(vars)
        x = 1
        y = 2
        vars
    '''
    tree = ast.parse(source)
    assert find_variables(tree) == ['vars']



# Generated at 2022-06-14 02:52:02.714447
# Unit test for function extend_tree
def test_extend_tree():
    test_tree = ast.parse(
        """
var1 = 1
var2 = 2
extend(vars)
"""
    )
    tree_body = test_tree.body

    vars = [
        ast.Assign(
            targets=[ast.Name(id='var1', ctx=ast.Store())],
            value=ast.Num(n=1)
        ),
        ast.Assign(
            targets=[ast.Name(id='var2', ctx=ast.Store())],
            value=ast.Num(n=2)
        )
    ]

    extend_tree(test_tree, {'vars': vars})

    assert tree_body[0].value.n == 1
    assert tree_body[1].value.n == 2



# Generated at 2022-06-14 02:52:08.582826
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

    class Test(snippet):
        def get_body(self, **kwargs):
            return kwargs["var"]

    test = Test(lambda a, b, c: let(a) or let(b) or let(c))
    assert test.get_body(var=x) == 1

# Generated at 2022-06-14 02:52:18.741816
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_fn(_x: int, _y: int, _z: int, _a: int, _b: int) -> float:
        x = let(_x)
        y = let(_y)
        z = let(_z)

        a = let(_a)
        b = let(_b)

        return .001 + .002 + .003
    snippet_ = snippet(test_fn)
    body = snippet_.get_body(
        _x=1,
        _y=2,
        _z=3,
        _a=4,
        _b=5
    )
    assert len(body) == 7

# Generated at 2022-06-14 02:52:23.443200
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    let(x)
    let(y)
    x + y""")

    assert set(find_variables(tree)) == {'x', 'y'}
    assert str(tree) == """
    x + y""".lstrip()



# Generated at 2022-06-14 02:52:31.517768
# Unit test for function find_variables
def test_find_variables():
    assert not list(find_variables(ast.parse('x = 1')))
    assert ['x'] == list(find_variables(ast.parse('let(x = 1)')))
    assert ['x', 'y'] == list(find_variables(ast.parse('''
        let(x = 1)
        let(y = [1, 2])
        ''')))
    assert ['x', 'y'] == list(find_variables(ast.parse('''
        let(x = 1)
        let(y = 1)
        x += 1
        ''')))
    assert ['x', 'y'] == list(find_variables(ast.parse('''
        let(x = 1)
        let(y = 1)
        x += 1
        let(x = 2)
        ''')))




# Generated at 2022-06-14 02:52:43.108173
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x, y):
        let(x)
        x += x * 2 + y * 2
        return x

    # Get AST body of foo
    body = foo.get_body(x=1, y=2)
    # Check if body is correct

# Generated at 2022-06-14 02:52:49.117683
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''
    def f(a, b):
        let(c)
        let(d)
    
    def g(x):
        let(y)
    '''

    tree = ast.parse(source)

    assert snippet(f).get_body(c=1, d=2) == tree.body[0].body[1:]



# Generated at 2022-06-14 02:53:01.958376
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse(
        "extend(vars)\n"
        "print(x, y)")

    vars = ast.parse("x = 1\nx = 2").body
    extend_tree(tree, {'vars': vars})

    assert get_source(tree) == "x = 1\nx = 2\nprint(x, y)\n"

# Generated at 2022-06-14 02:53:13.257847
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class A:
        a = 123
    def f():
        let(A)
        f = A()
        f.a = 1
        x = A.a
        return x


# Generated at 2022-06-14 02:53:18.852253
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse(
        '''
        def foo():
            let(x)
            x = 3
        ''')
    assert list(find_variables(tree)) == ['x']



# Generated at 2022-06-14 02:53:25.483187
# Unit test for function extend_tree
def test_extend_tree():
    body = [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1),
            type_comment=None),
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=2),
            type_comment=None),
        ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[ast.Name(id='x', ctx=ast.Load()), ast.Name(id='y', ctx=ast.Load())],
                keywords=[],
                starargs=None,
                kwargs=None)
        )
    ]

# Generated at 2022-06-14 02:53:33.281413
# Unit test for function find_variables
def test_find_variables():
    source = 'let(x)\n'
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x']

    source = '''let(x)
let(y)
'''
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']

    source = '''let(x)
let(y)
'''
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']

    source = '''let(x)
let(x)
'''
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'x_1']

    source = '''let(x)
let(x)
'''
   

# Generated at 2022-06-14 02:53:43.113110
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:53.051157
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import logger  # type: ignore
    from .helpers import code  # type: ignore
    
    logger.setLevel(logger.ERROR)
    code_1 = code('x')
    snippet_1 = snippet(code_1)
    body_1 = snippet_1.get_body()
    assert(str(body_1[0].value) == '_py_backwards_x_0')
    code_2 = code('x', 'y')
    snippet_2 = snippet(code_2)
    body_2 = snippet_2.get_body()
    assert(str(body_2[1].value) == '_py_backwards_y_0')
    code_3 = code('x', 'y', 'z')
    snippet_3 = snippet(code_3)
    body_3

# Generated at 2022-06-14 02:53:57.488035
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    s = snippet(lambda: 1)
    body = s.get_body()
    assert body == [ast.Return(value=ast.Num(1))]



# Generated at 2022-06-14 02:54:01.044049
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fun():
        x = 1
        y = 2
        let(x)
        x += 1

    snippet_ = snippet(fun)
    body = snippet_.get_body()
    assert body == [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='x', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        )
    ]



# Generated at 2022-06-14 02:54:09.021681
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    from .tree import find
    from .utils import get_source
    from .snippet import set_compare

    class tests(unittest.TestCase):
        def test_extend_tree(self):
            @snippet
            def test_snippet():
                extend(assignments)
                x = 1
                x = 2
                print(x, y)

            assignments = ast.parse(
                """x = 1; x = 2; y = 3; y = 4; y = 5; y = 6; y = 7; y = 8""").body
            extend_tree(ast.parse(get_source(test_snippet)), {'assignments': assignments})

# Generated at 2022-06-14 02:54:28.655552
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = ast.Name(id='_py_backwards_x_0', ctx=ast.Load())
    b = ast.Name(id='y', ctx=ast.Load())
    c = ast.Num(n=1)
    d = ast.Assign(targets=[a], value=c)
    e = ast.Assign(targets=[b], value=c)
    f = ast.Expr(value=b)
    g = ast.Module(body=[d, e, f])

# Generated at 2022-06-14 02:54:29.412376
# Unit test for function extend_tree

# Generated at 2022-06-14 02:54:38.649493
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Arrange
    source = get_source(test_snippet_get_body)

    # Act
    tree = ast.parse(source)
    variables = snippet._get_variables(tree, {'x': ast.Name('y'), 'z': 1})
    let_tree = find(tree, ast.Call)
    new_body = snippet.get_body(tree.body, **variables)

    # Assert
    assert len(new_body) == 2
    assert all('_' in var.id for var in find(new_body, ast.Name))



# Generated at 2022-06-14 02:54:43.573658
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var = ast.Name('x', ast.Load())
    assert snippet(lambda: let(x)).get_body(x=var) == snippet(lambda: _py_backwards_x_0).get_body()

# Generated at 2022-06-14 02:54:52.358989
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x: ast.Name) -> None:
        let(x)
        x += 1

    result = snippet(test_snippet).get_body(x=ast.Name(id='x'))
    expected = [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.BinOp(
            left=ast.Name(id='x', ctx=ast.Load()),
            op=ast.Add(),
            right=ast.Num(n=1)
        )
    )]
    assert result == expected



# Generated at 2022-06-14 02:55:01.334852
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('vars = extend(vars)')
    extensions = {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                 value=ast.Num(n=1)),
                                  ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                 value=ast.Num(n=2))]}
    extend_tree(tree, extensions)
    expected = ast.parse('x = 1\nx = 2\nvars = extend(vars)')
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 02:55:10.524019
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x):
        extend(vars)
        return (x + y) * 2

    assert foo.get_body(x=2, y=[ast.Num(n=1)])[0] == ast.BinOp(
            left=ast.BinOp(
                left=ast.Num(n=2),
                op=ast.Add(),
                right=y),
            op=ast.Mult(),
            right=ast.Num(n=2),
        )



# Generated at 2022-06-14 02:55:20.808634
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Covers the following cases:
    # 1. get body of function that is defined as usual
    # 2. check that variables that were let were replaced with unique names
    # 3. check that variables that were extend were placed in correct places
    # 4. check that variables that were let were not replaced in extend nodes
    @snippet
    def my_fn(n: int) -> None:
        let(x)
        let(y)
        x += 1
        print(y)
        let(z)
        extend(vars)
        print(x, y, z)

    vars = ast.parse('x = 1\nx = 2\nx += 3\n').body
    body = my_fn.get_body(vars=vars)

# Generated at 2022-06-14 02:55:27.801499
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class C:
        @snippet
        def f(x: int) -> ast.AST:
            let(a)
            let(b)
            extend(a)
            extend(b)
            return list(a) + [ast.Name(id='b', ctx=ast.Store())]

    body = C.f.get_body(a=[ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                            value=ast.Constant(value=1, kind=None))],
                        b=ast.Expr(value=ast.Constant(value=2, kind=None)))


# Generated at 2022-06-14 02:55:39.822525
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Arrange
    def my_func(x1, x2):
        let(x1)
        let(x2)
        extend(x3)
        y = x1 + x2
        return y
    x1 = ast.Name(id='x1', ctx=ast.Load())
    x2 = ast.Name(id='x2', ctx=ast.Load())
    x3 = []
    for x in range(1, 3):
        x3.append(ast.Assign(targets=[x1], value=ast.Num(x), ctx=ast.Load()))
    my_snippet = snippet(my_func)
    # Act
    body = my_snippet.get_body(x1=x1, x2=x2, x3=x3)
    # Ass

# Generated at 2022-06-14 02:55:53.803228
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        let(y)
        x += 1
        y = 1
        extend(vars)
    snippet_fn = snippet(fn)
    assert snippet_fn.get_body(x=42, y=None, vars=[_py_backwards_x_0, x]) == \
           [ast.Assign([_py_backwards_x_0], ast.Num(42)), ast.Assign([y], ast.Num(1)),
            ast.Assign([_py_backwards_x_0], ast.BinOp(_py_backwards_x_0, ast.Add(), ast.Num(1)))]



# Generated at 2022-06-14 02:55:58.741470
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def my_snippet(a, b):
        let(x)
        x = a + b
        let(y)
        y = a * b
        return x + y
    snippet_body = snippet(my_snippet).get_body()
    assert snippet_body[0].value.left.id == '_py_backwards_x_0'
    assert snippet_body[1].value.left.id == '_py_backwards_y_1'
    assert snippet_body[2].value.left.id == '_py_backwards_y_1'

# Generated at 2022-06-14 02:56:09.582213
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    x = 1
    y = 1


    def fn():
        let(x)
        x += 1
        y = 1


    x = 1
    y = 2


    def fn1():
        extend(vars)
        print(x, y)

    vars = [
        ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=1)),
        ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=2))
    ]
    res = snippet(fn1).get_body(vars=vars)
    a = astor.to_source(res).strip()
    assert a == 'x = 1\nx = 2\nprint(x, y)'
    res

# Generated at 2022-06-14 02:56:13.009874
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func() -> None:
        let(x)
        x += 1
        y = 1
    
    assert snippet(func).get_body() == ast.parse('_py_backwards_x_0 += 1; y = 1;').body

# Generated at 2022-06-14 02:56:22.223333
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # type: () -> None
    @snippet
    def snippet1(a: Any, b: Any, c: Any) -> None:
        let(y)
        let(x)
        x += a
        y = b + 1
        c += y
        z = x + y

    test_1 = snippet1.get_body(  # type: ignore
        a=2, b=3, c=1
    )

    assert len(test_1) == 6
    assert isinstance(test_1[0], ast.Assign)
    assert isinstance(test_1[1], ast.Assign)
    assert isinstance(test_1[2], ast.AugAssign)
    assert isinstance(test_1[3], ast.Assign)

# Generated at 2022-06-14 02:56:30.287807
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: x).get_body() == ast.parse('').body
    assert snippet(lambda: let(x)).get_body() == ast.parse('').body
    assert snippet(lambda: x).get_body() == ast.parse('x').body
    assert snippet(lambda: let(x) + let(y)).get_body() == ast.parse('_py_backwards_x_0 + _py_backwards_y_1').body
    assert snippet(lambda: let(x) + y).get_body() == ast.parse('_py_backwards_x_0 + y').body
    assert snippet(lambda: let(x) + let(y) + 1).get_body() == ast.parse('_py_backwards_x_0 + _py_backwards_y_1 + 1').body


# Generated at 2022-06-14 02:56:32.469562
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(x)\nx += 1\ny = 1')
    assert list(find_variables(tree)) == ['x']
    assert ast.dump(tree) == ''



# Generated at 2022-06-14 02:56:38.462299
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippets_dir = os.path.dirname(__file__)
    expected_source = open(os.path.join(snippets_dir, 'snippets/expected.py'), 'r').read()
    actual_tree = snippet(lambda x, y, z: None).get_body(
        x=1, y=2, z=3,
    )
    actual_source = get_source(actual_tree)

    assert expected_source == actual_source

# Generated at 2022-06-14 02:56:46.715668
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_a(a):
        let(b)
        return b + a

    nodes = snippet(snippet_a).get_body()
    assert len(nodes) == 1
    assert isinstance(nodes[0], ast.Return)
    assert isinstance(nodes[0].value, ast.BinOp)
    assert isinstance(nodes[0].value.op, ast.Add)
    assert isinstance(nodes[0].value.left, ast.Name)
    assert nodes[0].value.left.id == '_py_backwards_b_0'
    assert isinstance(nodes[0].value.right, ast.Name)
    assert nodes[0].value.right.id == 'a'



# Generated at 2022-06-14 02:56:54.951760
# Unit test for function find_variables
def test_find_variables():
    """Tests if it correctly processes functions with different types of arguments."""
    def test1(x, y):
        let(x)
        let(y)
        pass
    
    def test2(x, y):
        let(x)
        pass
    
    def test3(x: int, y: int):
        let(x)
        let(y)
        pass
    
    def test4(x: int = 1, y: int = 2):
        let(x)
        let(y)
        pass
    
    def test5(x, y: int = 2):
        let(x)
        let(y)
        pass
    
    def test6(*, x, y):
        let(x)
        let(y)
        pass
    

# Generated at 2022-06-14 02:57:02.606847
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(x):
        y = let(2)
        y += x
        return y

    s = snippet(snippet_fn)
    body = s.get_body()
    assert len(body) == 2

# Generated at 2022-06-14 02:57:03.419389
# Unit test for function extend_tree

# Generated at 2022-06-14 02:57:12.172744
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    extend(x)
    x = 1
    """
    tree = ast.parse(source)
    extend_tree(tree, {'x': [ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                        ast.Num(n=1)), ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                                                  ast.Num(n=2))]})
    assert get_source(tree) == 'x = 1;x = 2;'

# Generated at 2022-06-14 02:57:16.582478
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def first():
        let(x)
        x += 1
        y = 1
    
    snippet_ = snippet(first)
    assert snippet_.get_body() == ast.parse("_py_backwards_x_0 += 1\ny = 1").body



# Generated at 2022-06-14 02:57:26.220431
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import ast
    import asttokens

    code = '''
    def let(var):
        None
        
    def extend(var):
        None
        
    def make_assignment(var, value):
        var = value
        
    def add_one(var):
        let(var)
        var += 1
        
    def make_assignment_and_add_one(var, value):
        extend(vars)
        make_assignment(var, value)
        add_one(var)
        
    x = 1
    vars = make_assignment_and_add_one(x, 2)
    '''
    tokens = asttokens.ASTTokens(code, parse=True)
    tree = tokens.tree
    to_process = find(tree, ast.FunctionDef)
    functions

# Generated at 2022-06-14 02:57:35.616307
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn():
        let(x)
        x += 1

    assert fn.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1))),
    ]



# Generated at 2022-06-14 02:57:42.991590
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    @snippet
    def test_snippet():
        let(x)
        x += 1
        y = 1

    result = test_snippet.get_body()
    assert len(result) == 2
    assert result[0].value.left.id == '_py_backwards_x_0'
    assert isinstance(result[1].targets[0], ast.Name)
    assert result[1].targets[0].id == 'y'
    assert result[1].value.n == 1

# Generated at 2022-06-14 02:57:48.850248
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def testfn(x: int) -> int:
        return x + 1

    body = snippet(testfn).get_body(x=1)
    assert 'return _py_backwards_x_0 + 1' in get_source(body)



# Generated at 2022-06-14 02:57:55.463797
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(a: int) -> List[ast.AST]:
        let(x)
        y = x
        return func.__code__.co_code
    v = snippet(func)
    body = v.get_body(x=1)
    assert body[0].value.args[0].n == 1
    assert body[1].value.value.id == "_py_backwards_x_0"

# Generated at 2022-06-14 02:57:59.668244
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert ast.dump(snippet(test_let_ex1).get_body()) == \
        ast.dump(ast.parse(
            'x = x + 1\n'
            'y = 1').body)



# Generated at 2022-06-14 02:58:14.023452
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f():
        let(x)
        x += 1
        y = 1
        extend(vars)

    def get_vars():
        let(x)
        x = 1
        let(y)
        y = 2

    # TODO: fix the shit below:
    vars = f.get_body(vars=ast.parse(get_source(get_vars)).body)
    assert get_source(f.get_body) == ('x = 1\n'
                                      'x = 2\n'
                                      'y = 1\n')

if __name__ == '__main__':
    test_snippet_get_body()

# Generated at 2022-06-14 02:58:21.816928
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x, y):
        let(x)
        let(y)
        a = x + y

    assert snippet(test_snippet).get_body(x=1, y=2) == \
        [ast.Expr(ast.BinOp(  # type: ignore
            ast.Name(id='_py_backwards_x_0', ctx=ast.Store()),
            ast.Add(),
            ast.Num(n=2)))]

# Generated at 2022-06-14 02:58:23.666220
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: 0).get_body() == [ast.Expr(value=ast.Num(n=0))]

# Generated at 2022-06-14 02:58:31.857385
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        x += 1

        def fn():
            return 1

        extend(fn)
        return fn

    body = snippet(snippet_fn).get_body()

# Generated at 2022-06-14 02:58:44.874277
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_fn(a, b):
        a.thing()
        b.other_thing()

    body = snippet_fn.get_body(
        a=ast.Name(id='a', ctx=ast.Load()),
        b=ast.Name(id='b', ctx=ast.Load())
    )

# Generated at 2022-06-14 02:58:55.095740
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func():
        let(x)
        x += 1
        y = 1
        extend(vars)


# Generated at 2022-06-14 02:58:59.822338
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = get_source(test_snippet_get_body)
    tree = ast.parse(source)
    body = tree.body[0].body
    assert body[0].value.args[0].id == "sys"
    assert body[1].value.value.args[0].id == "sys"
    assert body[2].value.elts[0].id == "sys"
    assert body[3].value.id == "sys"
    assert body[4].value.elts[0].id == "sys"
    assert body[5].value.func.id == "sys"



# Generated at 2022-06-14 02:59:04.883911
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int, y: str) -> None:
        let(z)
        z = y
        print(x, z)

    expected_source = 'x = 1\nz = 2\nprint(x, z)\n'
    assert snippet(fn).get_body(x=1, y=2) == ast.parse(expected_source).body

# Generated at 2022-06-14 02:59:13.553751
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .testing_helpers import print_ast
    from .testing_helpers import assert_ast_equal

    @snippet
    def simple_snippet(x: int, y: int, z: float = 0) -> None:
        let(x)
        x += 1

    @snippet
    def extend_snippet(var: str) -> None:
        extend(var)

    ast_y = ast.parse("y = 1").body[0]
    ast_z = ast.parse("z = 1").body[0]

    ast_x_plus_1 = simple_snippet.get_body(x=ast_y)[0]
    ast_x_plus_2 = simple_snippet.get_body(x=ast_y)[0]
    ast_x_plus_3 = simple

# Generated at 2022-06-14 02:59:21.454872
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet():
        let(x)
        let(y)
        x += 1
        y = 1
        z = 2
        z += 1
        
    assert my_snippet.get_body()[0].targets[0].id == '_py_backwards_x_0'
    assert my_snippet.get_body(x=1)[0].targets[0].n == 1
    assert my_snippet.get_body(x=1)[1].value.value == 1
    assert my_snippet.get_body(x=1)[2].value.n == 2

# Generated at 2022-06-14 02:59:30.329526
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def get_imports(modules: let):
        import os
        import sys
        import platform

        extend(modules)

    modules: List[ast.AST] = []
    body = get_imports.get_body(modules=modules)
    assert isinstance(body, list)
    assert len(body) == 3
    assert isinstance(body[2], ast.ImportFrom)

# Generated at 2022-06-14 02:59:34.985994
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_ = snippet(lambda x, y: let(x) + let(y))
    body = snippet_.get_body(x=1, y=2)
    assert len(body) == 2
    assert len(body[0].targets) == 1
    assert len(body[1].targets) == 1
    assert isinstance(body[0].targets[0], ast.Name)
    assert isinstance(body[1].targets[0], ast.Name)
    assert body[0].targets[0].id != body[1].targets[0].id



# Generated at 2022-06-14 02:59:44.098519
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # setup
    x = ast.Name(id='x', ctx=ast.Load())
    y = ast.Name(id='y', ctx=ast.Load())
    x_1 = ast.Name(id='x_1', ctx=ast.Load())
    y_1 = ast.Name(id='y_1', ctx=ast.Load())
    z = ast.Name(id='z', ctx=ast.Load())

    variables = {
        'x': x,
        'y': y,
        'x_1': x_1,
        'y_1': y_1,
        'z': z,
        'assign': ast.Assign,
        'Add': ast.Add,
    }

    @snippet
    def example():
        let(x)

# Generated at 2022-06-14 02:59:59.705934
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(x: int) -> str:
        let(y)
        y = x
        y = y + 1
        extend(z)
        return y

    snippet_foo = snippet(foo).get_body(
        z=[ast.Assign([ast.Name('y', ast.Store())], ast.Num(1))]
    )