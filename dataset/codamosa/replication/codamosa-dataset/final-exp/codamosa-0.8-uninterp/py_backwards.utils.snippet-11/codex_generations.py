

# Generated at 2022-06-14 02:50:52.698706
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''
        def test():
            x, y = let(3), 4
            x += 1
            y += let(2)
            return (y, x)
    '''
    tree = ast.parse(source)
    test_snippet = snippet(test)
    tree.body[0].body = test_snippet.get_body()

# Generated at 2022-06-14 02:50:58.416315
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    code = """
x = 1
extend(vars)
    """
    tree = ast.parse(code)
    extend_tree(tree, {'vars': ast.parse("x = 2").body[0].value})
    assert astor.to_source(tree) == """x = 1
x = 2"""

# Generated at 2022-06-14 02:51:02.685592
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        let(x)
        let(y)
        x = x + 1
    """)
    assert set(find_variables(tree)) == {'x', 'y'}



# Generated at 2022-06-14 02:51:03.363032
# Unit test for function extend_tree

# Generated at 2022-06-14 02:51:06.317212
# Unit test for function find_variables
def test_find_variables():
    ast_tree = ast.parse("""
        let(x)
        x += 1
        let(y)
        y = 1
    """)
    assert len(list(find_variables(ast_tree))) == 2

# Generated at 2022-06-14 02:51:09.329564
# Unit test for function extend_tree
def test_extend_tree():
    body = ast.parse('''x = 1
extend(arg)
y = 2''').body
    assert body == extend_tree(body, {'arg': [ast.parse('x = 2').body[0]]})



# Generated at 2022-06-14 02:51:13.605353
# Unit test for function extend_tree
def test_extend_tree():
    ex = ast.parse('let(a)')
    ex2 = ast.parse('a = 1')

    tree = ast.parse('let(a) + extend(a)')
    extend_tree(tree, {'a': ex2})

    expected = 'a = 1\n1'
    got = ast.dump(tree)

    assert expected == got

# Generated at 2022-06-14 02:51:23.852065
# Unit test for function extend_tree
def test_extend_tree():
    source = """
        extend(vars)
        print(x, y)
    """
    tree = ast.parse(source)
    extend_tree(tree, {"vars": [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(n=1),
    ), ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(n=2),
    )
    ]})
    assert get_source(tree) == """
        x = 1
        x = 2
        print(x, y)
        """.strip()

# Generated at 2022-06-14 02:51:31.055063
# Unit test for function extend_tree
def test_extend_tree():
    vars = ast.parse('''
x = 1
x = 2''')
    tree = ast.parse('''
extend(vars)
print(x)''')
    extend_tree(tree.body[0], {'vars': vars})
    assert ast.dump(tree) == ast.dump(ast.parse('''
x = 1
x = 2
print(x)'''))

# Generated at 2022-06-14 02:51:41.409859
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('''import a
let(d)
let(e)
extend(d)
extend(e)
print(c)
print(b)
''')

    d = ast.Assign(targets=[ast.Name(id='d')], value=ast.Num(n=1))
    e = ast.Assign(targets=[ast.Name(id='e')], value=ast.Num(n=1))

    extend_tree(tree, {'d': d, 'e': e})

# Generated at 2022-06-14 02:51:49.054040
# Unit test for function find_variables
def test_find_variables():
    source = "let(x); x = 1; y = 2"
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'x'}



# Generated at 2022-06-14 02:51:52.585746
# Unit test for function find_variables
def test_find_variables():
    source = '''
y = let(x) + let(y)
'''
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert variables == ['x', 'y']



# Generated at 2022-06-14 02:52:00.137457
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_f():
        return let(1)  # type: ignore

    assert snippet(snippet_f).get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_var_0', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]

    def snippet_func():
        i = let(1)  # type: ignore
        i += 1
        j = let(2)  # type: ignore
        return i, j


# Generated at 2022-06-14 02:52:10.645539
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: None).get_body(x=ast.Name(id="var", ctx=ast.Load())) == []

    @snippet
    def test(x):
        let(x)
        y = 1
        # return x
        print(x.n)


# Generated at 2022-06-14 02:52:21.071216
# Unit test for function find_variables
def test_find_variables():
    snippet1 = "let(x)\nl = [x]"
    snippet2 = "let(x)\nlet(y)\nl = [x, y]"
    snippet3 = "let(x)\nlet(y)\nlet(z)\nl = [x, y, z, 1, 2, 3]"
    snippet4 = "let(x)\nlet(y)\nlet(z)\nl = [x, 1, y, 2, z, 3]"
    snippet5 = "let(x)\nlet(y)\nlet(z)\nl = [x, 1, y, 2, z, x, y, z, 3]"
    snippet6 = "let(x)\nx = x + 1"
    snippet7 = "let(x)\ny = x\nx = x + 1"

# Generated at 2022-06-14 02:52:30.631048
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet1():
        x = 1
        let(x)
        y = 2
        return x + y

    assert snippet(snippet1).get_body() == \
        ast.parse('_py_backwards_x_0 = 1; y = 2; return _py_backwards_x_0 + y').body[0].body

    def snippet2():
        x = 1
        let(x)
        y = 2
        let(y)
        z = 3
        return x + y + z


# Generated at 2022-06-14 02:52:36.459896
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

    @snippet
    def test(x: int) -> int:
        let(x)
        x += 1
        y = 1
        
        return x + y

    body = test.get_body(x=x)
    assert body[1].value.left.id == 'x'
    assert body[1].value.right.n == 1



# Generated at 2022-06-14 02:52:38.569142
# Unit test for function find_variables
def test_find_variables():
    assert find_variables('''
        let(x)
        let(y)
    ''') == ('x', 'y')



# Generated at 2022-06-14 02:52:47.049154
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
        def my_f(a):
            let(x)
            x = 1
            y = 2
            z = 3
    """
    fn = ast.parse(source)
    res1 = snippet(fn).get_body()
    assert len(res1) == 4
    assert isinstance(res1[0], ast.Assign)
    assert ast.dump(res1[0]) == "Assign(targets=[Name(_py_backwards_x_0, Store())], value=Num(1))"
    assert isinstance(res1[1], ast.Assign)
    assert ast.dump(res1[1]) == "Assign(targets=[Name(y, Store())], value=Num(2))"
    assert isinstance(res1[2], ast.Assign)
    assert ast

# Generated at 2022-06-14 02:52:54.789211
# Unit test for function find_variables
def test_find_variables():
    assert find_variables(ast.parse('let(1)')) == []
    assert find_variables(ast.parse('let(x)')) == ['x']
    assert find_variables(ast.parse('[let(x) for x in []]')) == ['x']
    assert find_variables(ast.parse('let(y)\nx')) == ['y']
    assert find_variables(ast.parse('let(y)\n[x, let(x)]')) == ['x', 'y']



# Generated at 2022-06-14 02:53:01.859207
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from astunparse import unparse
    @snippet
    def test(x: int) -> None:
        x += 1
        y = 1
    body = test.get_body(x=2)
    assert unparse(body) == 'x += 1\ny = 1'



# Generated at 2022-06-14 02:53:13.171132
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_for_get_body_test(x: int, y: int) -> None:
        let(z)
        z = x + y
        return z
    body = snippet_for_get_body_test.get_body(x=42, y=1)
    assert len(body) == 1
    assert isinstance(body[0], ast.Return)
    assert isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[0].value.left, ast.Name)
    assert body[0].value.left.id == '_py_backwards_z_0'
    assert isinstance(body[0].value.right, ast.Num)
    assert body[0].value.right.n == 43


# Generated at 2022-06-14 02:53:19.576697
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(a: int, b: int = 2) -> int:
        let(x)
        x += 10
        y = x + a + b
        return y

    print(foo(2, b=3))
    print(snippet(foo).get_body(a=1))

# Generated at 2022-06-14 02:53:23.029271
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    method_get_body = snippet(lambda: None).get_body
    assert method_get_body.__doc__

# Generated at 2022-06-14 02:53:33.029072
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet(a: int, b: float):
        let(a)
        a += 1
        a = b
        extend(c)
        return a - b
    c = [ast.Assign(targets=[ast.Name(id='a')], value=ast.Num(n=1)), ast.Assign(targets=[ast.Name(id='a')], 
                                                                                value=ast.Num(n=2))]

# Generated at 2022-06-14 02:53:42.089565
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    variables = {"x": ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=1)),
                 "y": ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())], value=ast.Num(n=2))}
    tree = ast.parse(
        """extend(x)
        extend(y)
        print(x, y)"""
    )
    extend_tree(tree, variables)
    assert astor.to_source(tree) == """x = 1
y = 2
print(x, y)"""



# Generated at 2022-06-14 02:53:47.287368
# Unit test for function find_variables
def test_find_variables():
    def foo():
        # Forward declaration
        let(a)
        let(b)
        return a + 3 + b

    tree = ast.parse(get_source(foo))
    variables = find_variables(tree)
    assert variables == ['a', 'b']
    assert not tree.body[0].body



# Generated at 2022-06-14 02:53:49.134878
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def b():
        let(x)
        x = 1
        y = 2
        return x, y

    snippet(b).get_body()

# Generated at 2022-06-14 02:53:50.179219
# Unit test for function extend_tree

# Generated at 2022-06-14 02:54:05.337080
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    x = 12

    @snippet
    def body_with_variables():
        let(x)
        x = x
        x = 1
        let(y)
        y = y
        y = 2


# Generated at 2022-06-14 02:54:14.677296
# Unit test for function find_variables
def test_find_variables():
    import ast
    code = """
let(x)
let(y)
x+=1
y+=1
let(foo)
foo()
    """
    tree = ast.parse(code)
    assert set(find_variables(tree)) == set(('x', 'y', 'foo'))

# Generated at 2022-06-14 02:54:21.098555
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vals)\ndot()")
    extend_tree(tree, {"vals": [ast.parse("x = 1").body[0], ast.parse("x = 2").body[0]]})
    assert get_source(tree) == "x = 1\nx = 2\ndot()"

# Generated at 2022-06-14 02:54:29.084600
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def unique_variables(x):
        x += 1
        y = 1
    snippet_body = snippet(unique_variables).get_body()
    assert snippet_body == [ast.Assign([ast.Name('__py_backwards_x_0', ast.Store())],
                                       ast.BinOp(ast.Name('__py_backwards_x_0', ast.Load()),
                                                 ast.Add(),
                                                 ast.Num(1))),
                            ast.Assign([ast.Name('y', ast.Store())],
                                       ast.Num(1))]


# Generated at 2022-06-14 02:54:39.948713
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import get_source
    from .wrappers import source, source_module, source_module_with_imports, source_stmt, source_expr
    
    def foo():
        x = 1
        let(y)
        y += x
        extend(z)
        x += y
        y += x + y
        let(z)
        x += 1
        return x + y + z
                
    assert source(foo) == """
        def foo():
            x = 1
            let(y)
            y += x
            extend(z)
            x += y
            y += x + y
            let(z)
            x += 1
            return x + y + z
    """.strip()


# Generated at 2022-06-14 02:54:50.672222
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(x); y; x.z; x(); let(z); let(x);')
    assert list(find_variables(tree)) == ['x', 'z']
    assert ast.dump(tree) == 'Module(body=[Expr(value=Call(func=Name(id=\'x\', ctx=Load()), args=[], keywords=[])), Expr(value=Name(id=\'y\', ctx=Load())), Expr(value=Attribute(value=Name(id=\'x\', ctx=Load()), attr=\'z\', ctx=Load())), Expr(value=Call(func=Name(id=\'x\', ctx=Load()), args=[], keywords=[]))])'



# Generated at 2022-06-14 02:55:00.609741
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Given
    @snippet
    def snippet_fn():
        let(x)
        y = 42
        return y + x
    x = 2

    # When
    body = snippet_fn.get_body(x=x)

    # Then
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].value, ast.Num)
    assert body[0].value.n == 42
    assert isinstance(body[1], ast.Return)
    assert isinstance(body[1].value, ast.BinOp)
    assert isinstance(body[1].value.right, ast.Name)
    assert isinstance(body[1].value.right.ctx, ast.Load)

# Generated at 2022-06-14 02:55:08.797118
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 5
    y = 6
    s = snippet(lambda : 3)

    class C:
        def __init__(self, z):
            self.z = z


# Generated at 2022-06-14 02:55:17.249936
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(a: ast.AST, b: str) -> None:
        def test_let(a: ast.AST, b: str) -> None:
            a = let(a)
            b = let(b)
        test_let(a, b)

    body = snippet(test_snippet).get_body(a=1, b='A')
    assert body == [ast.Assign([ast.Name('_py_backwards_a_0', None)], ast.Num(1)),
                    ast.Assign([ast.Name('_py_backwards_b_1', None)], ast.Str('"A"'))]



# Generated at 2022-06-14 02:55:26.001396
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: x + 1).get_body() == [ast.Expr(ast.BinOp(
        ast.Name('x', ctx=ast.Load()), ast.Add(), ast.Num(1)))]

    assert snippet(lambda *args: args).get_body(args=['x']) == [ast.Expr(ast.Tuple(
        [ast.Name('_py_backwards_x_0', ctx=ast.Load())], ctx=ast.Load()))]

    assert snippet(lambda **kw: kw).get_body(kw={'x': ['y']}) == [ast.Expr(ast.Dict(
        [ast.Str('x')], [ast.List([ast.Str('y')], ctx=ast.Load())]))]


# Generated at 2022-06-14 02:55:38.317612
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('''
    def a():
        extend(vars)
        print(x)
    ''')
    variables = {
        'vars': ast.parse('''
        x = 1
        x = 2
        ''').body
    }
    extend_tree(tree, variables)

# Generated at 2022-06-14 02:55:51.105209
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    _py_backwards_x_0 = 4
    y = 1

    def func():
        let(_py_backwards_x_0)
        _py_backwards_x_0 += 1
        y = 1

    snip = snippet(func)
    snip.get_body()

    assert _py_backwards_x_0 == 5
    assert y == 1


# Generated at 2022-06-14 02:56:03.288501
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_func():

        def add(x, y):
            return x + y

        let(add)
        print(add(1, 2))
        print(add(2, 3))

    snippet_from_test = snippet(test_func)
    x = ast.parse('x = 1').body[0]
    y = ast.parse('y = 2').body[0]
    print_x_y = ast.parse('print(x, y)').body[0]
    expected_code = [x, y, print_x_y]

    code = snippet_from_test.get_body(y=y)
    print(code)
    assert code == expected_code

# Generated at 2022-06-14 02:56:13.481146
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    c = 3

    @snippet
    def snippet_func(x: int, y: int, z: int) -> None:
        let(c)

        d = 4
        e = 5
        f = 6
        d = 8

        extend(b)

    vars = {
        'x': a,
        'y': b,
        'z': let(c),
    }
    body = snippet_func.get_body(**vars)
    assert len(body) == 3
    assert body[1].value.elts[0].n == 1
    assert body[1].value.elts[1].n == 2
    assert body[2].value.elts[0].n == 1
    assert body[2].value.elts[1].n == 2

# Generated at 2022-06-14 02:56:22.482640
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x, y):
        let(z)
        z += 1
        extend(y)
        z = 1
        return z

    snippet_ = snippet(func)
    body = snippet_.get_body(z=None, y=[ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                                                 value=ast.Num(n=0)),
                                     ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                value=ast.Num(n=1))])

# Generated at 2022-06-14 02:56:29.565257
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x: List[int]) -> List[int]:
        x += [1]
        let(res)
        res = x
        return res

    assert fn.get_body() == \
        [ast.Assign([ast.Name('_py_backwards_res_0', ast.Store())],
                    ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()),
                              ast.Add(),
                              ast.List([ast.Num(1)], ast.Load()))),
         ast.Return(ast.Name('_py_backwards_res_0', ast.Load()))]



# Generated at 2022-06-14 02:56:30.117904
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:56:35.603033
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def s(x: int) -> None:
        let(y=1)
        let(z=y + 1)
        z += z + x

    assert s.get_body(x=5) == [
        ast.Assign([ast.Name(id='_py_backwards_z_0', ctx=ast.Store())],
                   ast.BinOp(ast.Name(id='_py_backwards_z_0', ctx=ast.Load()),
                             ast.Add(),
                             ast.BinOp(ast.Num(n=1), ast.Add(), ast.Num(n=5)))),
    ]


# Generated at 2022-06-14 02:56:39.799976
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .test_helpers import capture_output
    expected = ['2\n', '2\n']
    actual = []

    @snippet
    def snippet(x: int = 0):
        let(x)
        print(x)
        x = x + 1
        return x

    with capture_output() as (out, _):
        code = snippet.get_body()
        exec(compile(ast.Module(body=code), filename="<ast>", mode="exec"))
    actual.append(out.getvalue())

    with capture_output() as (out, _):
        code = snippet.get_body()
        exec(compile(ast.Module(body=code), filename="<ast>", mode="exec"))
    actual.append(out.getvalue())

    assert actual == expected


# Generated at 2022-06-14 02:56:49.143907
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def function(x: int) -> int:
        let(y)
        y += 1
        return y + x

    snippet_kwargs = {'x': 1}
    body = snippet(function).get_body(**snippet_kwargs)

# Generated at 2022-06-14 02:56:58.487976
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def t(x: int, y: float) -> int:
        let(x)
        x += 1
        return x

    snippet_inst = snippet(t)  # type: ignore
    variables = {'x': ast.Num(1), 'y': ast.Num(1.0)}

# Generated at 2022-06-14 02:57:19.238476
# Unit test for function extend_tree
def test_extend_tree():
    def replace(value, target_value, index):
        if value == target_value:
            return index
        return 0

    tree = ast.parse("extend(x)")
    extend_tree(tree, {'x': ast.parse('x=1')})
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1))])'
    tree = ast.parse("extend(x)")
    extend_tree(tree, {'x': ast.parse('x=1, y=2')})

# Generated at 2022-06-14 02:57:25.750252
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 'x'
    y = 'y'
    original = snippet(lambda x=x, y=y: let(x) + y)
    result = snippet(lambda x=x, y=y: let(x) + y).get_body()
    assert result == [ast.Assign(targets=[ast.Name(id=x, ctx=ast.Store())],
                                 value=ast.BinOp(left=ast.Name(id=x, ctx=ast.Load()),
                                                 op=ast.Add(),
                                                 right=ast.Name(id=y, ctx=ast.Load())))], "The result should be the same"

# Generated at 2022-06-14 02:57:33.704335
# Unit test for function find_variables
def test_find_variables():
    source = """
    def a():
        let(x)
        x += 1
        let(y)
        y -= 1

    def b():
        let(z)
        z += 1
    """

    tree = ast.parse(source)
    names = find_variables(tree)
    assert list(names) == ['x', 'y', 'z']


# Unit tests for function VariablesReplacer.replace

# Generated at 2022-06-14 02:57:45.221967
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    x = ast.Name(id='x')
    snippet_kwargs = dict()
    snippet_kwargs['x'] = x
    exps = ast.Expr(value=ast.BinOp(left=ast.Name(id='x'), op=ast.Add(), right=ast.Num(n=1)))
    snippet_kwargs['y'] = exps

    @snippet
    def test_snippet():
        let(x)
        y
        let(y)

    fn = test_snippet()
    assert fn.get_body(**snippet_kwargs) == [ast.Expr(value=ast.BinOp(left=ast.Name(id='x'), op=ast.Add(), right=ast.Num(n=1)))]

# Generated at 2022-06-14 02:57:55.786636
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = None
    y = None
    z = None

    # Basic test
    @snippet
    def snippet1():
        let(x)
        x += 1
        y = 1

    assert snippet1.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='x', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1),
            ),
        ),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1))
    ]

    # Test with multiple declarations

# Generated at 2022-06-14 02:58:00.492321
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x, y):
        let(y)
        y += 1
        return y
    
    expected = """x = 1
x = 2
print(x, y)"""
    actual = ast.dump(fn.get_body(vars=[ast.parse("x = 1\nx = 2")]))
    assert expected == actual

# Generated at 2022-06-14 02:58:09.019694
# Unit test for function extend_tree

# Generated at 2022-06-14 02:58:12.687884
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    obj = snippet(lambda: None)
    stub = obj.get_body()
    assert stub == [ast.Expr(value=ast.Name(id='None', ctx=ast.Load()))]
    #[Expr(value=Name(id='None', ctx=Load()))]



# Generated at 2022-06-14 02:58:21.764147
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x += 1

    snippet_ = snippet(fn)
    body = snippet_.get_body()
    assert len(body) == 1
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[0].target, ast.Name)
    assert body[0].target.id == '_py_backwards_x_0'
    assert isinstance(body[0].op, ast.Add)
    assert isinstance(body[0].value, ast.Num)
    assert body[0].value.n == 1



# Generated at 2022-06-14 02:58:30.504329
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_snippet(a: Any, b: Any) -> None:
        let(a)
        let(b)
        extend(b)
        a += 1

    snippet_snippet = snippet(snippet_snippet)
    body = snippet_snippet.get_body(a=ast.Name(id='a',
                                               ctx=ast.Load()),
                                    b=[ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                  value=ast.Constant(value=1)),
                                       ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                  value=ast.Constant(value=2))])


# Generated at 2022-06-14 02:58:48.297302
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    ob = {
        "a": 10,
        "b": 2
    }
    import math
    # Create snippet of code
    @snippet
    def code(x: int, y: int, ob: dict, z: str) -> int:
        """
        body of code
        :param x:
        :param y:
        :param ob:
        :return:
        """
        let(ob)
        let(a)
        let(b)
        let(math.sqrt)
        extend(x)
        extend(y)
        res = ob["a"] * ob["b"]
        res = math.sqrt(res)
        res1 = ob["a"] * ob["b"]
        res2 = ob["a"] * ob["b"]
        return

# Generated at 2022-06-14 02:58:57.157834
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import to_source
    from .test_tree import TEST_SNIPPET_GET_BODY

    @snippet
    def s(x: ast.Name, y: ast.Name):
        let(x)
        let(y)
        x += 1
        y = (2, 3)
        for i in y:
            x += i

    body = s.get_body(x=ast.Name(id='x'), y=ast.Name(id='y'))

    assert to_source(body) == TEST_SNIPPET_GET_BODY

# Generated at 2022-06-14 02:59:03.357182
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _fn(x: int) -> int:
        let(x)
        x += 1
        return x
    snippet = snippet(_fn)
    snippet_kwargs = {'x': 4}
    assert snippet.get_body(**snippet_kwargs) == [
            ast.Assign([ast.Name('_py_backwards_x_0', ast.Store())],
                        ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()), ast.Add(),
                                  ast.Num(1)))
    ]

# Generated at 2022-06-14 02:59:12.739415
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import parse, unparsed

    @snippet
    def my_snippet(x: int, y: List[int]) -> None:
        let(x)
        x += 1
        let(y)
        y.append(1)

    body = my_snippet.get_body(x=10, y=[])
    parsed = unparsed(body)
    assert parsed == '_py_backwards_x_0 += 1; _py_backwards_y_0.append(1)'

    body = my_snippet.get_body(x=parse('x + y'), y=[])
    parsed = unparsed(body)
    assert parsed == '_py_backwards_x_0 = x + y; _py_backwards_y_0.append(1)'

# Generated at 2022-06-14 02:59:21.605128
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x, y):
        let(x)
        let(y)
        x += 1
        y += 1


# Generated at 2022-06-14 02:59:30.343690
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func():
        let(x)
        let(y)
        x += 1

    snippet_obj = snippet(func)
    out = snippet_obj.get_body(x=1, y=1)
    assert out == [ast.Assign(
        targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
        value=ast.BinOp(
            op=ast.Add(),
            left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
            right=ast.Num(n=1)
        )
    )]

# Generated at 2022-06-14 02:59:37.379585
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    def func(x: int) -> int:
        return x * 2
    y = 3
    from .helpers import get_source
    source = get_source(func)
    # TODO: We should use decorator @snippet
    tree = ast.parse(source)
    variables = {"x": x}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)

# Generated at 2022-06-14 02:59:41.582894
# Unit test for function find_variables
def test_find_variables():
    TREE = ast.parse("""
        let(x)
        let(y)
        let(z)
        extend(x)
        extend(y)
    """)
    assert sorted(find_variables(TREE)) == ['x', 'y', 'z']



# Generated at 2022-06-14 02:59:51.926176
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_test_func(x: int, y: int) -> None:
        let(x)
        x += 1
        y = 1

    body = snippet_test_func.get_body(x=2, y=2)
    assert isinstance(body, list)
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].targets[0], ast.Name)
    assert body[0].targets[0].id == '_py_backwards_x_0'
    assert body[0].targets[0].ctx == ast.Store()
    assert isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[0].value.op, ast.Add)


# Generated at 2022-06-14 03:00:03.971110
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snip(x, y):
        let(x)
        x += 1
        y += 1
        extend(vars)
        return x + y

    vars = [ast.Assign(targets=[ast.Name(id='x')], value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x')], value=ast.Num(n=2)),
            ast.Assign(targets=[ast.Name(id='y')], value=ast.Num(n=3))]

# Generated at 2022-06-14 03:00:13.770702
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helper_objects import _expression, _statement, _assert, _equal
    from .test import _equal as _test_equal
    from py_backwards import snippet
    my_test_snippet = snippet(test_snippet_get_body)
    _expression_of_snippet = my_test_snippet.get_body(a=2)
    _test_equal(len(_expression_of_snippet),1)
    _test_equal(type(_expression_of_snippet[0]),type(_statement(None)))

# Generated at 2022-06-14 03:00:21.938866
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var_x = ast.Name(id='x', ctx=ast.Load())
    var_y = ast.Name(id='y', ctx=ast.Load())
    var_z = ast.Name(id='z', ctx=ast.Load())

    @snippet
    def fn():
        let(var_x)
        let(var_y)

        var_x += 1
        var_y += 2
        
        extend(vars)
        print(var_x, var_y)


# Generated at 2022-06-14 03:00:25.141031
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def x():
        let(a)
        return a

    snippet_x = snippet(x)
    snippet_x.get_body(a=1)

# Generated at 2022-06-14 03:00:34.273908
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: int) -> None:
        let(x)
        let(y)
        print(x, y)
        x += 1

    body = foo.get_body(x=1, y=2)
    assert isinstance(body[0], ast.Print)
    assert isinstance(body[0].values[0], ast.Name)
    assert body[0].values[0].id == 'x'
    assert body[1].target.id == '_py_backwards_x_0'



# Generated at 2022-06-14 03:00:41.146000
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    vars = 'vars'
    x = ast.Name('x', ast.Store())
    y = ast.Name('y', ast.Store())
    tree = ast.Assign(targets=[x, y], value=ast.Constant(1))
    snippet_kwargs = {vars: tree}