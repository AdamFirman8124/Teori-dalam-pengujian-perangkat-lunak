

# Generated at 2022-06-14 02:51:04.564490
# Unit test for function extend_tree
def test_extend_tree():
    src = """
let(x)

let(y)

extend(vars)

print(x, y)
"""

    tree = ast.parse(src)
    extend_tree(tree, {'vars': [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(1)),
                                ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                            ast.Num(2))]})


# Generated at 2022-06-14 02:51:06.725938
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # type: () -> None
    assert snippet(lambda: 1).get_body() == [ast.parse("1").body[0]]



# Generated at 2022-06-14 02:51:13.875274
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def function():
        let(a)
        a = 20
        b = 20
        extend(a)
        return a + b

    snippet_ = snippet(function)
    snippet_kwargs = {}
    result = snippet_.get_body(**snippet_kwargs)
    # assert result == ast.Module(body=[ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
    # value=ast.Num(n=20)), ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=ast.Num(n=20)),
    # ast.Return(value=ast.BinOp(left=ast.Name(id='a', ctx=ast.Load()), op=ast.Add(),
    # right=ast.Name

# Generated at 2022-06-14 02:51:23.780933
# Unit test for function extend_tree
def test_extend_tree():
    code1 = extend(vars)
    x = 1
    y = 2
    code2 = print(x, y)

    tree = ast.parse(code1 + code2)
    extend_tree(tree, {'vars': [ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                           ast.Num(n=1)),
                                ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                           ast.Num(n=2))]})
    assert get_source(tree) == 'x = 1\nx = 2\nprint(x, y)\n'

# Generated at 2022-06-14 02:51:35.398817
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Verifies that AST is transformed to replace the variables declared inside the snippet."""
    @snippet
    def my_snippet(x: int, y: int) -> int:
        let(a)
        a = x + y
        return a
    assert(my_snippet.get_body(x=ast.Num(n=1), y=ast.Num(n=2)) ==
           [ast.Assign([ast.Name(id='_py_backwards_a_0', ctx=ast.Store())], ast.BinOp(op=ast.Add(), left=ast.Num(n=1), right=ast.Num(n=2))),
            ast.Return(value=ast.Name(id='_py_backwards_a_0', ctx=ast.Load()))])


# Generated at 2022-06-14 02:51:42.907004
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(a)
    extend(b)
    c = 1
    """)

    extend_tree(tree, {
        'a': [
            ast.parse("a = 1").body[0],
            ast.parse("a = 2").body[0],
        ],
        'b': ast.parse("b = 1").body[0],
    })

    assert ast.dump(tree) == ast.dump(ast.parse("""
    a = 1
    a = 2
    b = 1
    c = 1
    """))

# Generated at 2022-06-14 02:51:55.261173
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .test_helpers import assert_all_nodes

    @snippet
    def test():
        let(x)
        y = 1
        x += 1
        return x

    body = test.get_body()

    assert len(body) == 2

# Generated at 2022-06-14 02:52:01.754777
# Unit test for function find_variables
def test_find_variables():

    def find_variables_test():
        let(x)
        let(y)
        let(z)
        print(x, y, z)

    tree = ast.parse(get_source(find_variables_test))
    assert [name for name in find_variables(tree)] == ['x', 'y', 'z']



# Generated at 2022-06-14 02:52:09.693390
# Unit test for function extend_tree
def test_extend_tree():
    def test():
        x = 1
        extend(vars)
        print(x)
    
    tree = ast.parse(get_source(test)).body[0]
    extend_tree(tree, {"vars": [ast.Assign(targets=[ast.Name(id="x")], value=ast.Num(1)), ast.Assign(targets=[ast.Name(id="x")], value=ast.Num(2))]})
    assert get_source(tree) == """x = 1
x = 2
print(x)"""


# Generated at 2022-06-14 02:52:20.898505
# Unit test for function extend_tree
def test_extend_tree():
    example_tree = ast.parse("""\
        extend(x)
        z = 1
        """)

    example_vars = {'x': [ast.Assign(targets=[ast.Name(id='x',
                                                      ctx=ast.Store())],
                                     value=ast.Num(n=1)),
                           ast.Assign(targets=[ast.Name(id='x',
                                                      ctx=ast.Store())],
                                     value=ast.Num(n=2))]}

    extend_tree(example_tree, example_vars)

# Generated at 2022-06-14 02:52:26.379979
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: x).get_body() is not None

# Generated at 2022-06-14 02:52:30.000939
# Unit test for function find_variables
def test_find_variables():
    # Declaring only 1 variable
    assert list(find_variables(ast.parse('x = let(x)'))) == ['x']
    # Declaring multiple variables
    assert list(find_variables(ast.parse('x = let(x)\nx = let(y)'))) == ['x', 'y']


# Generated at 2022-06-14 02:52:37.027202
# Unit test for function extend_tree
def test_extend_tree():
    source = "extend(vars)"
    tree = ast.parse(source)
    extend_tree(tree, {'vars': [ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                           ast.Num(1)),
                                ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                           ast.Num(2))]})
    assert get_source(tree) == 'x = 1\nx = 2'

# Generated at 2022-06-14 02:52:44.721119
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('a = extend(x)\n')
    x = ast.copy_location(ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                                     value=ast.Num(n=42)),
                         tree)
    extend_tree(tree, {'x': x})
    assert ast.dump(tree) == "Module(body=[Assign(targets=[Name(id='b', ctx=Store())], value=Num(n=42))])"



# Generated at 2022-06-14 02:52:55.714981
# Unit test for function extend_tree
def test_extend_tree():
    # We need to add our "let"/"extend" functions to global dictionary
    ast.fix_missing_locations(ast.Module(body=[ast.Expr(value=ast.Call(
        func=ast.Name(id='let', ctx=ast.Load()),
        args=[ast.Name(id='var', ctx=ast.Load())],
        keywords=[]))], type_ignores=[]))

    ast.fix_missing_locations(ast.Module(body=[ast.Expr(value=ast.Call(
        func=ast.Name(id='extend', ctx=ast.Load()),
        args=[ast.Name(id='var', ctx=ast.Load())],
        keywords=[]))], type_ignores=[]))

    # Create snippet


# Generated at 2022-06-14 02:53:04.938840
# Unit test for function extend_tree
def test_extend_tree():  # pragma: no cover
    # Example 1
    tree = ast.parse("""extend(vars)
print(x, y)
print(z)""")
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=ast.Num(n=2))]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:53:15.118256
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('print(let(x)); x = 1; extend(vars); extend(vars2)')
    variables = {'x': '_py_backwards_x_0',
                 'vars': [ast.AnnAssign(target=ast.Name(id='x', ctx=ast.Store()), value=ast.Num(1)),
                          ast.AnnAssign(target=ast.Name(id='x', ctx=ast.Store()), value=ast.Num(2))],
                 'vars2': [ast.AnnAssign(target=ast.Name(id='y', ctx=ast.Store()), value=ast.Num(10))]}

    extend_tree(tree, variables)


# Generated at 2022-06-14 02:53:22.581459
# Unit test for function extend_tree
def test_extend_tree():
    program = ast.parse("""
let(x)
let(y)
extend(vars)
print(x, y)
""", mode='exec')
    vars = ast.parse("""
x = 1
x = 2
""", mode='eval')

    extend_tree(program, {'vars': vars})

# Generated at 2022-06-14 02:53:32.733517
# Unit test for function find_variables

# Generated at 2022-06-14 02:53:43.041491
# Unit test for function extend_tree
def test_extend_tree():
    source = "extend(x); extend(y)"
    tree = ast.parse(source)
    x = [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(n=1)),
         ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(n=2))]
    y = [ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=ast.Num(n=1)),
         ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=ast.Num(n=2))]
    extend_tree(tree, {'x': x, 'y': y})


# Generated at 2022-06-14 02:53:54.611982
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def s(x: int, y: int) -> None:
        let(z)
        let(w)
        z += 1
        w = y
        print(z, w)


# Generated at 2022-06-14 02:53:58.786357
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test():
        let(x)
        x += 1
        y = 1

    s = snippet(test)
    assert str(s.get_body(x='test')[0]) == '_py_backwards_x_0 += 1'



# Generated at 2022-06-14 02:54:07.333970
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = ast.parse("x + 1").body[0]
    y = ast.parse("y + 1").body[0]
    @snippet
    def f(a):
        let(x)
        let(y)
        x += 1
        y += 1
    assert f.get_body(x=1, y='_') == [x, y]
    assert f.get_body(x=1, y='_') == [x, y]
    assert f.get_body(x=1, y=2) == [ast.parse("1 + 1").body[0],
                                    ast.parse("2 + 1").body[0]]

# Generated at 2022-06-14 02:54:09.460381
# Unit test for function extend_tree

# Generated at 2022-06-14 02:54:22.713303
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = ast.Name(id='x', ctx=ast.Load())
    snippet_ = snippet(lambda x: x + 1)
    body = snippet_.get_body(x=x)  # type: ignore
    assert body == ast.parse(
        """x = x + 1""").body  # type: ignore

    snippet_ = snippet(lambda: let(x) + 1)
    body = snippet_.get_body(x=x)  # type: ignore
    assert body == ast.parse(
        """x = x + 1""").body  # type: ignore

    snippet_ = snippet(lambda: x + let(y))
    body = snippet_.get_body(x=x)  # type: ignore

# Generated at 2022-06-14 02:54:30.826129
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """A unit test for method get_body of class snippet."""

    @snippet
    def fn(x: int, y: int) -> None:
        let(z)
        z = x + y
        x += 1
        y = 1
        extend(vars)
        print(x, y)

    tree = fn.get_body(vars=[ast.Assign([ast.Name('x', ast.Store())],
                                        ast.Num(1)),
                            ast.Assign([ast.Name('x', ast.Store())],
                                        ast.Num(2))],
                       x=2,
                       y=3)

    assert len(tree) == 1

# Generated at 2022-06-14 02:54:40.928569
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('import os\nos.path.join(x, x)')
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name('x')], value=ast.Num(1)),
                                ast.Assign(targets=[ast.Name('x')], value=ast.Num(2))]})

# Generated at 2022-06-14 02:54:50.557706
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo():
        let(x)
        x += 1
        y = 1
        
    assert foo.get_body() == [ast.Assign(
        targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
        value=ast.BinOp(
            left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
            op=ast.Add(),
            right=ast.Num(n=1)
        )
    ), ast.Assign(
        targets=[ast.Name(id='y', ctx=ast.Store())],
        value=ast.Num(n=1)
    )]

# Generated at 2022-06-14 02:55:00.893416
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: int, y: int) -> int:
        let(x)
        extend(vars)
        y = 5
        return x + y


# Generated at 2022-06-14 02:55:07.712717
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor

    @snippet
    def test_snippet() -> None:
        let(x)
        x += 1
        y = 1
        let(z)
        extend(vars)

    vars = [
        ast.AnnAssign(
            target=ast.Name(id='myvar', ctx=ast.Store()),
            annotation=None,
            value=ast.Num(n=42),
            simple=True,
        )
    ]

    body = test_snippet.get_body(x=1, y=2, vars=vars)
    print(astor.to_source(body))

# Generated at 2022-06-14 02:55:14.683913
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # let(x)
    # let(y)
    # return x + y
    # Will end up like:
    # _py_backwards_x_0 + _py_backwards_y_0

    @snippet
    def fn_1(x, y):
        let(x)
        let(y)
        return x + y

    # extend(vars)
    # x = 1
    # y = 2
    # return x + y
    # Will end up like:
    # x = 1
    # y = 2
    # x + y
    def fn_2(vars):
        extend(vars)
        x = 1
        y = 2
        return x + y

    # extend(vars)
    # x = 1
    # y = 2
    # return x + y


# Generated at 2022-06-14 02:55:24.305126
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

    @snippet
    def test(arg: int) -> None:
        let(arg)
        arg += 1
        print(arg, x)
        print(arg)


# Generated at 2022-06-14 02:55:36.659364
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Foo:
        @snippet
        def foo(self, x, y):
            let(z)
            let(a)
            a.b += c
            extend(d)
            def bar(x):
                return x + y
            bar(x)

    foo_obj = Foo()
    foo_body = foo_obj.foo.get_body(a=1, b=2, c=[3, 4], x=5,
                                    y=['_py_backwards_x_0', 8], d={'z': 9})
    assert isinstance(foo_body, list)
    assert isinstance(foo_body[0], ast.Assign)
    assert isinstance(foo_body[0].targets[0], ast.Name)

# Generated at 2022-06-14 02:55:43.312643
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import inspect

    a = 1
    b = 2
    s = snippet(inspect.currentframe().f_code)
    body = s.get_body()
    assert body == ast.parse('''\
_py_backwards_a_0 += 2
_py_backwards_b_0 -= 2
''').body

    # Check for let
    body = s.get_body(x=a)
    assert body == ast.parse('''\
_py_backwards_b_0 -= 2
_py_backwards_x_0 += 2
''').body

# Generated at 2022-06-14 02:55:51.795071
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def add_one() -> None:
        let(x)
        x = x + 1

    body = snippet(add_one).get_body(x=1)
    assert body == [
        ast.Assign(
            targets=[ast.Name(id=VariablesGenerator.generate('x'), ctx=ast.Store())],
            value=ast.BinOp(left=ast.Name(id=VariablesGenerator.generate('x'), ctx=ast.Load()),
                            op=ast.Add(),
                            right=ast.Constant(1, kind=None))
        )
    ]



# Generated at 2022-06-14 02:55:58.821449
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_func(x: int):
        let(y)
        return y + 1
    assert snippet(test_func).get_body() == [
        ast.Assign(
            targets=[
                ast.Name(id='_py_backwards_y_0', ctx=ast.Store())
            ],
            value=ast.Name(id='_py_backwards_x_0', ctx=ast.Load())
        ),
        ast.Return(
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_y_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        )
    ]



# Generated at 2022-06-14 02:56:09.662772
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astunparse
    import inspect

    line = inspect.currentframe().f_lineno

    @snippet
    def fn(x: int, y: int):
        let(x)
        let(y)

        assert x == y
        x = y + 1

    snippet_kwargs = {'x': ast.Name(id='x', ctx=ast.Store(),
                                   lineno=line + 2, col_offset=4),
                      'y': ast.Name(id='y', ctx=ast.Store(),
                                    lineno=line + 3, col_offset=4)}
    expected = ast.parse("""
    assert x == y
    _py_backwards_x_0 = y + 1
    """).body

    body = fn.get_body(**snippet_kwargs)
   

# Generated at 2022-06-14 02:56:19.764081
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: let(1)).get_body() == [ast.Assign(targets=[ast.Name('_py_backwards_1', ast.Store())], value=ast.Num(n=1, lineno=1, col_offset=4))]
    assert snippet(lambda: let(a)).get_body() == [ast.Assign(targets=[ast.Name('_py_backwards_a', ast.Store())], value=ast.Name(id='a', ctx=ast.Load(), lineno=1, col_offset=4))]

# Generated at 2022-06-14 02:56:29.796884
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_func():
        let(x)
        x = 1
        y = 2
        extend(z)

    snippet_obj = snippet(snippet_func)

    assert len(snippet_obj.get_body()) == 2
    assert snippet_obj.get_body()[0].body[0].value.n == 1
    assert snippet_obj.get_body()[1].value.n == 2
    assert snippet_obj.get_body()[0].value.id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:56:32.148006
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_test(x: int) -> None:
        let(x)
        print(x)
        
    # snippet_test._fn(1)



# Generated at 2022-06-14 02:56:45.329715
# Unit test for function extend_tree
def test_extend_tree():
    class A(ast.AST): pass
    class B(ast.AST): pass
    class C(ast.AST): pass

    tree = ast.parse('''
    extend(one)
    extend(two)
    extend(three)
    ''')

    extend_tree(tree, {
        'one': [A(), A(), A()],
        'two': [B(), B()],
        'three': [C(), C(), C(), C()],
    })

    actual = [type(child) for child in tree.body]

    assert actual == [A, A, A, B, B, C, C, C, C]

# Generated at 2022-06-14 02:56:48.542033
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_body = snippet(lambda x: let(3)).get_body()
    assert snippet_body == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                                       value=ast.Num(n=3))]



# Generated at 2022-06-14 02:56:51.698507
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 0
    let(x)
    x += 1
    y = 1
    return x + y



# Generated at 2022-06-14 02:56:57.689632
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: print(1)).get_body() == [ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Num(n=1)], keywords=[]))]
    assert snippet(lambda x: let(x)).get_body() == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())], value=ast.Name(id='x', ctx=ast.Load()))]

# Generated at 2022-06-14 02:57:05.644935
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    code = """
        for i in range(4):
            let(var)
            var += 1
            print(var)
    """
    expected = """
        for i in range(4):
            _py_backwards_var_0 += 1
            print(_py_backwards_var_0)
    """
    tree = ast.parse(code)
    snippet(lambda: None).get_body()
    units = ast.parse(expected).body
    assert snippet(lambda: None).get_body() == units
    

# Generated at 2022-06-14 02:57:07.812469
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    print(snippet(lambda x, y: x + y).get_body(x=7))



# Generated at 2022-06-14 02:57:18.854798
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x, y=42):
        return x + y

    s = snippet(fn)
    body = s.get_body()
    assert isinstance(body[0], ast.Return)
    assert isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[0].value.left, ast.NameConstant)
    assert isinstance(body[0].value.op, ast.Add)

    body = s.get_body(x=1)
    assert isinstance(body[0], ast.Return)
    assert isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[0].value.left, ast.Num)
    assert isinstance(body[0].value.op, ast.Add)


# Generated at 2022-06-14 02:57:25.821465
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_args = {'x': [6, 7, 8]}
    snip = snippet('''
        let(x)
        for x2 in x:
            x += 1
            print(x)
        ''')
    body = snip.get_body(x=snippet_args['x'])
    assert isinstance(body, list)
    assert len(body) == 2
    assert isinstance(body[0], ast.For)
    assert isinstance(body[0].target.id, str)
    assert isinstance(body[1], ast.Print)
    assert isinstance(body[1].values[0].value, ast.Name)
    assert body[1].values[0].value.id == body[0].target.id

# Generated at 2022-06-14 02:57:39.429985
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x = x + 1
        return x + 1

    sn = snippet(fn)
    body = sn.get_body()
    import_node = body[0]

    assert isinstance(import_node, ast.Assign)
    assert isinstance(import_node.targets[0], ast.Name)
    assert import_node.targets[0].id == 'x'
    assert isinstance(import_node.value, ast.BinOp)

    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[1].targets[0], ast.Name)
    assert body[1].targets[0].id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:57:44.792924
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    vars = [
        ast.AnnAssign(target=ast.Name(id='x'), value=ast.Num(n=1), annotation=None, simple=1),
        ast.AnnAssign(target=ast.Name(id='y'), value=ast.Num(n=2), annotation=None, simple=1),
    ]

    def test_snippet():
        extend(vars)
        let(x)
        x += 1
        y = 1
        z = 1
        for x in range(10):
            print(x)

    snippet_obj = snippet(test_snippet)

    result = snippet_obj.get_body()
    assert isinstance(result, list)
    assert len(result) == 7


# Generated at 2022-06-14 02:57:58.738344
# Unit test for function find_variables
def test_find_variables():
    source = """
        let(foo)
        let(bar)
        foobar
    """
    tree = ast.parse(source)
    assert {'foo', 'bar'} == set(find_variables(tree))



# Generated at 2022-06-14 02:58:07.538136
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo():
        let(x)
        x += 1
        y = 1
        extend(vars)

    s = snippet(foo)
    x = 5
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=2))]
    body = s.get_body(vars=vars, x=ast.Name(id='x', ctx=ast.Load()))
    assert len(body) == 3
    # In body, x should be replaced by generated name

# Generated at 2022-06-14 02:58:11.324462
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet3():
        extend(x)
        return 3

    x: List[ast.AST] = [ast.parse(
        """x = 1
        x = 2
        """).body
    ]

    tree = snippet(snippet3).get_body()

    assert len(tree) == 2

# Generated at 2022-06-14 02:58:21.599961
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x)
        x += 1

    assert test_snippet.get_body() == ([
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.Name(id='x', ctx=ast.Load()),
        ),
        ast.AugAssign(
            target=ast.Name(id='x', ctx=ast.AugStore()),
            op=ast.Add(),
            value=ast.Num(n=1),
        ),
    ])


# Generated at 2022-06-14 02:58:30.394582
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test get_body method."""
    import inspect

    def _run_test(fn, *args, **kwargs):
        _snippet = snippet(fn)
        fn_ast = _snippet.get_body(*args, **kwargs)
        target_ast = ast.parse(inspect.getsource(fn)).body[0].body
        assert ast.dump(fn_ast, include_attributes=True) == ast.dump(target_ast, include_attributes=True)
    
    def fn(x, y):
        let(z)
        z = y + x
        return z
    
    _run_test(fn, 2, 5)
    
    def fn1(x):
        let(y)
        y = x
        return y
    

# Generated at 2022-06-14 02:58:44.399374
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    z = 3

    def _func() -> None:
        # type: ignore
        let(x)  # type: ignore
        x += 1
        y += 2
        extend(z)  # type: ignore
        let(x)
        x += 1

    source = '''
    x = 1
    y = 2
    x = 2
    '''
    parsed = ast.parse(source)
    snippet_ = snippet(_func)
    result = snippet_.get_body(x=3)

# Generated at 2022-06-14 02:58:49.236699
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo():
        let(x)
        x += 1
        y = 1
    
    snippet_ = snippet(foo)
    body = snippet_.get_body()
    assert body == [
        ast.AugAssign(
            target=ast.Name(id='_py_backwards_x_0', ctx=ast.Store()),
            op=ast.Add(),
            value=ast.Num(n=1)
        ),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]  # type: ignore



# Generated at 2022-06-14 02:58:55.354209
# Unit test for function extend_tree
def test_extend_tree():
    import pytest
    from .helpers import to_ast

    code = 'extend(x)\nprint(x)'
    tree = ast.parse(code)
    extend_tree(tree, {'x': to_ast('x = 1\ny = 1')})
    assert get_source(tree) == 'x = 1\ny = 1\nprint(x)'



# Generated at 2022-06-14 02:59:02.557932
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
    def foo():
        let(a) = bar()
        let(b) = bar()
        return a, b
    """
    tree = ast.parse(source)
    variables = {'a': 1, 'b': 2}
    extend_tree(tree, variables)
    new_tree = VariablesReplacer.replace(tree, variables)
    assert new_tree.body[0].body[0].value.value == 1
    assert new_tree.body[0].body[1].value.value == 2

# Generated at 2022-06-14 02:59:04.883959
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("let(x);x = 1")
    assert list(find_variables(tree)) == ['x']



# Generated at 2022-06-14 02:59:31.179874
# Unit test for function find_variables
def test_find_variables():
    source = inspect.getsource(let) + inspect.getsource(extend)
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert variables == ['_py_backwards_var_0', '_py_backwards_var_1']



# Generated at 2022-06-14 02:59:36.417591
# Unit test for function extend_tree
def test_extend_tree():
    assert ast.dump(extend_tree(ast.parse("extend(x)"), {"x": [ast.Assign(targets=[ast.Name(id="a", ctx=ast.Store())],
                              value=ast.Num(n=1))]})).strip() == ast.dump(ast.parse("a = 1")).strip()


# Generated at 2022-06-14 02:59:44.033277
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:59:54.553838
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_with_vars(a, b):
        let(x)
        x += 1
        extend(y)
        x += 2
        y += 1
        return x + y

    snippet_fn = snippet(snippet_with_vars)
    body = snippet_fn.get_body(
        x=ast.Name(id='_py_backwards_x_0', ctx=ast.Store()),
        y=[
            ast.Assign(targets=[
                ast.Name(id='y', ctx=ast.Store())],
                       value=ast.Num(n=10))
        ]
    )
    y_line = ast.parse("y += 1").body[0]
    x_line = ast.parse("_py_backwards_x_0 += 2").body[0]


# Generated at 2022-06-14 03:00:02.213857
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(vars)
    print(x)
    """)

    variables = {
        'vars': [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Constant(value=1)),
                 ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Constant(value=2))]
    }

    extend_tree(tree, variables)
    assert get_source(tree) == 'x = 1\nx = 2\nprint(x)\n'

# Generated at 2022-06-14 03:00:09.459502
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_func(x, y="1"):
        let(x)
        z = y + '3'
        return z

    def test_func1(y):
        let(x)
        z = y + '3'
        return z

    tree = test_func.get_body(y="abc", x=ast.Name('def','def'))
    assert(get_source(test_func1) == ast.get_source(ast.Module(body=tree)))



# Generated at 2022-06-14 03:00:21.031447
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""extend(vars)
v = 1
print(v)
""")
    vars = [ast.parse("""x = 1
x = 2
""")]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 03:00:28.915867
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def function():
        let(x)
        let(y)
        extend(vars)
        z = 100
        z += z
        z -= z
        print(x, y, z)

    vars = ast.parse("x = 1; y = 2").body
    assert snippet(function).get_body(vars=vars) == ast.parse("x = 1; y = 2; _py_backwards_z_0 = 100; _py_backwards_z_0 += _py_backwards_z_0; _py_backwards_z_0 -= _py_backwards_z_0; print(_py_backwards_x_0, _py_backwards_y_0, _py_backwards_z_0)").body

# Generated at 2022-06-14 03:00:31.162013
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    s = snippet(lambda x: let(a) + a + extend(a) + a)
    assert isinstance(s.get_body(), list)

# Generated at 2022-06-14 03:00:39.097779
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .compat import abstract_tree

    var_x = ast.Name(id='_py_backwards_x_0', ctx=ast.Store())
    var_y = ast.Name(id='_py_backwards_y_1', ctx=ast.Store())