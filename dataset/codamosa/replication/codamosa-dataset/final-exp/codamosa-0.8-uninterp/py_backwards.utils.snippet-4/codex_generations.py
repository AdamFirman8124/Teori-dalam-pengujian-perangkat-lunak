

# Generated at 2022-06-14 02:50:42.225027
# Unit test for function extend_tree
def test_extend_tree():
    extend_tree(ast.parse('extend(x)'), {'x': [ast.parse('x=1'), ast.parse('x=2')]}) \
        .body[0].body == [ast.parse('x=1').body[0], ast.parse('x=2').body[0]]

# Generated at 2022-06-14 02:50:50.822927
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    class Foo:
        pass
    extend(vars)
    """)

    vars = [
        ast.Assign([ast.Name(id='first_var', ctx=ast.Store())],
                   ast.Num(n=1)),
        ast.Assign([ast.Name(id='second_var', ctx=ast.Store())],
                   ast.Num(n=2)),
    ]

    extend_tree(tree, {
        'vars': vars
    })


# Generated at 2022-06-14 02:50:57.310145
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    def func():
        extend(vars)
        a = 1
        b = 2
        print(a, b)
    """
    tree = ast.parse(source)
    extend_tree(tree, {'vars': [ast.parse('x = 1').body[0],
                                ast.parse('y = 2').body[0]]})
    source = ast.fix_missing_locations(tree)
    assert source.body[0].body[0].value.args[0].elts[0].value.id == 'x'
    assert source.body[0].body[0].value.args[0].elts[1].value.id == 'y'



# Generated at 2022-06-14 02:51:04.663769
# Unit test for function extend_tree
def test_extend_tree():
    code_base = """
        x = 1
        y = 2
    """
    code_extend = """
        t = x + y
        x += t
    """

    tree_base = ast.parse(code_base)
    tree_extend = ast.parse(code_extend)

    extend_tree(tree_base, {'vars': tree_extend})

    assert astor.to_source(tree_base) == code_base + code_extend

# Generated at 2022-06-14 02:51:12.780899
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet():
        let(x)
        extend(y)

    tree = snippet.get_body(x=1, y=[ast.parse('x = 1').body[0], ast.parse('x = 2').body[0]])
    assert tree == [
        ast.Assign(targets=[
            ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.Num(n=1)),
        ast.Assign(targets=[
            ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1)),
        ast.Assign(targets=[
            ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=2))
    ]

# Generated at 2022-06-14 02:51:13.691025
# Unit test for function find_variables

# Generated at 2022-06-14 02:51:22.070227
# Unit test for function find_variables
def test_find_variables():
    code = '''
        let(x)
        let(y)
        
        def foo(q):
            pass
            
        def bar():
            let(r)
            pass
        
        class B:
            let(sd)
            pass
    '''

    tree = ast.parse(code)
    names = find_variables(tree)
    assert list(names) == ['x', 'y', 'q', 'r']

    # import IPython; IPython.embed()

# Generated at 2022-06-14 02:51:30.881906
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars); x = 1')
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id='x')], value=ast.Num(1))]})
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1))])'

# Generated at 2022-06-14 02:51:36.250681
# Unit test for function extend_tree
def test_extend_tree():  # noqa
    import astor

    a_assign = ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                          value=ast.Num(n=1))
    b_assign = ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                          value=ast.Num(n=2))


# Generated at 2022-06-14 02:51:45.424698
# Unit test for function extend_tree
def test_extend_tree():
    tree_obj = ast.parse("""
for x in range(10):
    extend(vars)
    x += 1
    y = 1
""")
    tree = tree_obj.body[0]
    vars_ = [
        ast.Assign(
            targets=[ast.Name(id="x", ctx=ast.Store())],
            value=ast.Num(n=1)
        ),
        ast.Assign(
            targets=[ast.Name(id="x", ctx=ast.Store())],
            value=ast.Num(n=2)
        )
    ]
    expected_tree = ast.parse("""
for x in range(10):
    x = 1
    x = 2
    x += 1
    y = 1
""")

# Generated at 2022-06-14 02:51:54.287888
# Unit test for function find_variables
def test_find_variables():
    source = """\
x = 1
y = 2
let(a)
a = 1 + 1
let(b)
"""
    tree = ast.parse(source)

    assert sorted(find_variables(tree)) == ['a', 'b']



# Generated at 2022-06-14 02:51:58.068665
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""let(x)
    x += 1""")
    assert next(find_variables(tree)) == 'x'

# Generated at 2022-06-14 02:52:05.562788
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn() -> None:
        let(x)
        let(y)
        x += 1
        print(y)

    snippet_get_body = snippet(fn)
    source = snippet_get_body.get_body()
    assert source[0].targets[0].id == "_py_backwards_x_0"
    assert source[1].value.func.id == "print"
    assert source[1].value.args[0].id == "_py_backwards_y_1"



# Generated at 2022-06-14 02:52:13.784529
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        x += 1
        y = 1

    snippet_instance = snippet(snippet_fn)
    expected_body = [
        ast.Assign(
            targets=[
                ast.Name(id='_py_backwards_x_0', ctx=ast.Store())
            ],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ),
        ast.Assign(
            targets=[
                ast.Name(id='y', ctx=ast.Store())
            ],
            value=ast.Num(n=1)
        )
    ]
    assert snippet

# Generated at 2022-06-14 02:52:24.357446
# Unit test for function find_variables
def test_find_variables():
    a = snippet(lambda: let(x))
    assert list(find_variables(a.get_body())) == ['x']

    a = snippet(lambda: let(x) + let(y))
    assert set(find_variables(a.get_body())) == {'x', 'y'}

    b = snippet(lambda: let(x) + 2)
    assert set(find_variables(b.get_body())) == {'x'}

    a = snippet(lambda: let(x) + let(y))
    assert set(find_variables(a.get_body())) == {'x', 'y'}

    a = snippet(lambda: let(x) + let(y) + let(z) + let(w))

# Generated at 2022-06-14 02:52:32.071238
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test snippet.get_body."""
    def fn():
        """Snippet for testing."""
        let(x)
        x += 1
        y = 1
        extend(vars)
        print(x, y)

    snippet_inst = snippet(fn)
    vars_ast = ast.parse('x = 1\nx = 2')
    body = snippet_inst.get_body(x=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()), vars=vars_ast)
    expected = ast.parse('_py_backwards_x_0 = 1\n_py_backwards_x_0 = 2\n_py_backwards_x_0 += 1\ny = 1\nprint(_py_backwards_x_0, y)')
   

# Generated at 2022-06-14 02:52:33.641552
# Unit test for function find_variables

# Generated at 2022-06-14 02:52:38.239215
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
a = let(x)
b = let(y)
c = let(x)
d = x
e = y
f = let(y)
g = y
""")
    assert set(find_variables(tree)) == {'x', 'y'}



# Generated at 2022-06-14 02:52:45.299437
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    #test if __init__ works correctly
    #test to see if get_body works on empty function
    def empty_fn():
        pass
    empty_snippet = snippet(empty_fn)
    assert empty_snippet.get_body() == []
    #test to see if get_body works on function with code
    def some_fn():
        x = 1
        y = 2
    some_snippet = snippet(some_fn)
    body = some_snippet.get_body()
    assert body[0].value.n == 1
    assert body[1].value.n == 2

# Generated at 2022-06-14 02:52:48.902788
# Unit test for function find_variables
def test_find_variables():
    source = '''
        def fn(x):
            let(a)
            a = 2
    '''
    tree = ast.parse(source)
    var = find_variables(tree)
    assert 'a' in var
    # Test that let was removed from body
    assert find(tree, ast.Call) == []



# Generated at 2022-06-14 02:53:01.013158
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f(x: int, y: int) -> None:
        let(x)
        while x < y:
            x += 1
            print(x)

    assert f.get_body(x=5, y=10) == ast.parse('''
    while _py_backwards_x_0 < y:
        _py_backwards_x_0 += 1
        print(_py_backwards_x_0)
    ''').body

# Generated at 2022-06-14 02:53:12.143577
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x += 1
        y = 1
        z = x + y
        extend(vars)
        print(x, y)
    
    var = ast.parse("x = 1\nx = 2")
    tree = snippet(fn).get_body(vars=var, x="_py_backwards_x_0")
    assert len(tree) == 4
    assert str(tree[0]) == 'x = 1'
    assert str(tree[1]) == 'x = 2'
    assert str(tree[2]) == "_py_backwards_x_0 += 1"
    assert str(tree[3]) == "print(_py_backwards_x_0, 1)"

# Generated at 2022-06-14 02:53:22.126189
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet(x, y):
        let(x)
        x += 1
        y = 1

    # Check types
    result = snippet.get_body()
    assert isinstance(result, list)
    assert isinstance(result[0], ast.Assign)
    assert isinstance(result[1], ast.Assign)

    # Check values
    result = snippet.get_body(x=ast.Name(id='_x', ctx=ast.Load()), y=ast.Num(n=2))

# Generated at 2022-06-14 02:53:31.029992
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x):
        let(y)
        let(z)
        y = 1
        z = 2
        assert x == 3
        assert y == 1
        assert z == 2

    fn_snippet = snippet(fn)
    body = fn_snippet.get_body(x=3)
    source = ast.unparse(body)
    expected = """
_py_backwards_y_0 = 1
_py_backwards_z_0 = 2
assert 3 == x
assert 1 == _py_backwards_y_0
assert 2 == _py_backwards_z_0
"""
    assert source == expected

# Generated at 2022-06-14 02:53:34.846010
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(a)
    extend(b)
    """)
    variables = {'a': ast.parse('x=1').body[0],
                 'b': ast.parse('x=2').body[0]}
    extend_tree(tree, variables)
    assert(get_source(tree) == "...\nx = 1\nx = 2")



# Generated at 2022-06-14 02:53:41.753426
# Unit test for function find_variables
def test_find_variables():
    assert set(find_variables(ast.parse("""
        def foo(x):
            let(y)
            z = 1
            assert z >= y
    """))) == {'y'}

    assert set(find_variables(ast.parse("""
        def bar(x, let=let):
            let(y)
            z = 1
            assert z >= y
    """))) == {'y'}



# Generated at 2022-06-14 02:53:46.958639
# Unit test for function find_variables
def test_find_variables():
    code = '''
let(a)
let(b)
a = 1
'''
    tree = ast.parse(code)
    vars = set(find_variables(tree))
    assert vars == {'a', 'b'}
    assert code == ast.dump(tree)



# Generated at 2022-06-14 02:53:55.070890
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        y = x
        for i in range(y):
            extend(vars)
    snippet_fn()

    src = "let(x)\nx += 1\ny = 1"
    tree = ast.parse(src)
    variables = {'x': ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                 'y': 1,
                 'vars': ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())], value=1)}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)

# Generated at 2022-06-14 02:54:05.312567
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class A(snippet):
        def __init__(self, fn: Callable[..., None]) -> None:
            snippet.__init__(self, fn)

    def f(x, y) -> int:
        let(x)
        x = x + y
        y = z
        return x + y + z

    a = A(f)
    source = get_source(f)
    tree = ast.parse(source)
    variables = a._get_variables(tree, {'x': 10})
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert len(tree.body[0].body) == 5
    assert isinstance(tree.body[0].body[0], ast.Assign)

# Generated at 2022-06-14 02:54:09.710991
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)\nprint(x, y)")
    extend_tree(tree, {'vars': ast.parse("x=1\nx=2").body})
    assert tree.body[0].body == ast.parse("x=1\nx=2\nprint(x, y)").body


# Unit tests for class snippet

# Generated at 2022-06-14 02:54:27.919155
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test() -> None:
        let(x)
        x += 1
        y = 1

    body = test.get_body()
    assert body == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                   value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                   op=ast.Add(),
                                   right=ast.Num(n=1))),
        ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                   value=ast.Num(n=1))]

# Generated at 2022-06-14 02:54:38.718733
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Trivial case
    def trivial():
        var = [1, 2, 3]
        var.append(3)
        return var

    assert snippet(trivial).get_body() == ast.parse(get_source(trivial)).body

    # Using let
    def using_let():
        let(x)
        x = 1
        return x + 2

    assert snippet(using_let).get_body() == [ast.Assign([ast.Name('_py_backwards_x_0', ast.Store())],
                                                         ast.Num(1)),
                                             ast.Return(ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()),
                                                                  ast.Add(),
                                                                  ast.Num(2)))]

    # Using extend


# Generated at 2022-06-14 02:54:49.196487
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Test snippet body - test body of snippet
    def test_snippet_body(x: int) -> None:
        x = let(x)
        x += 1
        return x

    # Test snippet full source - source of snippet
    def test_snippet_full_source(x: int) -> None:
        x = let(x)
        x += 1
        return x

    test_snippet_full_source_ast = ast.parse(get_source(test_snippet_full_source))

    # Test snippet body ast - ast of snippet body
    test_snippet_body_ast = test_snippet_body(1)

    # Convert body of snippet to string for compare

# Generated at 2022-06-14 02:54:51.766927
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_with_let():
        let(x)
        print(x)

    body = snippet(snippet_with_let).get_body()
    print(body)



# Generated at 2022-06-14 02:54:56.796991
# Unit test for function find_variables
def test_find_variables():
    code = """
        let(x)
        let(y)
        x * 2
        y = 1
        print(foo)
    """
    tree = ast.parse(code)
    vars = find_variables(tree)
    assert isinstance(vars, dict)
    assert vars == {'x', 'y'}

# Generated at 2022-06-14 02:55:01.017815
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int):
        let(y)
        y = 1
        x += 2

    snippet_object = snippet(fn)
    snippet_object._get_variables(ast.parse(get_source(fn)), {})


# This is a unit test for method replace of class VariablesReplacer.
# It points out if name is undefined in variable.

# Generated at 2022-06-14 02:55:03.635459
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:55:15.150092
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(a: ast.AST, b: ast.AST, c: ast.AST) -> None:
        let(a)
        let(b)
        let(c)
        print(a)
        print(b)
        print(c)

    source = get_source(test_snippet)
    tree = ast.parse(source)
    variables = find_variables(tree)
    extend_tree(tree, variables)
    test_snippet_body = tree.body[0].body

    assert len(test_snippet_body) == 6
    assert isinstance(test_snippet_body[0], ast.Expr)
    assert isinstance(test_snippet_body[0].value, ast.Call)
    assert test_snippet_body[0].value

# Generated at 2022-06-14 02:55:22.232654
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: int) -> None:
        let(a)
        let(b)
        return a + b

    tree: ast.AST = foo.get_body(a=1, b=3)
    assert ast.dump(tree) == 'Return(value=BinOp(left=Name(id=_py_backwards_a_0, ctx=Load()), op=Add(), right=Name(id=_py_backwards_b_0, ctx=Load())))'



# Generated at 2022-06-14 02:55:34.281824
# Unit test for function extend_tree
def test_extend_tree():
    source = '''
        extend(vars)
        print(x, y)
    '''
    tree = ast.parse(source)
    assignments = ast.Module(body=[
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                   value=ast.Num(n=1)),
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                   value=ast.Num(n=2)),
    ])
    extend_tree(tree, {'vars': assignments})

# Generated at 2022-06-14 02:55:47.344285
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse(textwrap.dedent(
        """
        def function(a, b):
            extend(vars)
            if ok:
                c = 3
        """))
    variables = {
        'vars': [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                            value=ast.Num(n=1)),
                 ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                            value=ast.Num(n=2))]
    }
    extend_tree(tree, variables)
    expected = textwrap.dedent(
        """
        def function(a, b):
            a = 1
            b = 2
            if ok:
                c = 3
        """
    )


# Generated at 2022-06-14 02:56:01.846405
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x) -> None:
        let(y)
        print(x, y)

    body = foo.get_body(x=ast.Name(id='a', ctx=ast.Load()))

# Generated at 2022-06-14 02:56:12.332316
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('x = 1; extend(vars); print(x, y)')
    vars = ast.parse('x = 1; x = 2')
    extend_tree(tree, {'vars': vars})
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1)), Print(dest=None, values=[Name(id="x", ctx=Load()), Name(id="y", ctx=Load())], nl=True), Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=2))])'



# Generated at 2022-06-14 02:56:21.646817
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet1(x: int, fn: Callable[[int], int]) -> int:
        let(fn)
        return fn(x) + 1  # type: ignore

    def snippet2() -> int:
        x = 1

        def fn(y):
            return y + x

        let(fn)
        return fn(1)

    snippets = [snippet1, snippet2]
    for snippet in snippets:
        for new_fn_name in [None, 'new_fn_name']:
            new_fn_name1 = 'new_fn_name1'
            snippet_body = snippet(harness1.snippet(new_fn_name)).get_body()

# Generated at 2022-06-14 02:56:26.329083
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        a = b
        c = let(d)
        e = let(f)
        g = f + h
    """)
    assert list(find_variables(tree)) == ['d', 'f']



# Generated at 2022-06-14 02:56:34.851762
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import parse_body_as

    @snippet
    def snippet_fn(x: int) -> None:
        let(y)
        y += 1
        assert x == y
        let(z)
        z = 2
        assert z == 2

    @snippet
    def snippet_fn_extend(x: int) -> None:
        extend(z)
        assert z == 1

    @snippet
    def snippet_fn_extend_with_call(x: int) -> None:
        extend(z)
        assert z(x) == 1


# Generated at 2022-06-14 02:56:40.127168
# Unit test for function extend_tree
def test_extend_tree():
    def fn(x, y):
        a = 1
        b = 2
        extend(a)
        extend(b)
        print(x, y)

    body = snippet(fn).get_body(x=1, y=2)
    assert get_source(ast.Module(body).body) == '''
    a = 1
    b = 2
    print(x, y)
    '''

# Generated at 2022-06-14 02:56:46.893084
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    a = 3
    b = 4

    @snippet
    def test(z):
        let(x)
        let(y)
        let(a)
        let(b)
        extend(z)

    tree = test.get_body(z=[ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                       value=ast.Num(n=1)),
                            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                       value=ast.Num(n=2))])

    tree = ast.Module(body=tree)


# Generated at 2022-06-14 02:56:55.054212
# Unit test for function find_variables
def test_find_variables():
    # Find single variable
    code = 'let(x)'
    tree = ast.parse(code)
    assert find_variables(tree) == ['x']

    # Find multiple variables
    code = 'let(x)\nlet(y)'
    tree = ast.parse(code)
    assert find_variables(tree) == ['x', 'y']

    # Find inside function
    code = "def f():\n    let(x)"
    tree = ast.parse(code)
    assert find_variables(tree) == ['x']

    # Find inside class
    code = "class A:\n    let(x)"
    tree = ast.parse(code)
    assert find_variables(tree) == ['x']

    # Return empty list when no variables
    code = "x = 1"
    tree = ast.parse

# Generated at 2022-06-14 02:56:58.307623
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def add(x, y):
        let(z)
        z = x + y
        return z
    
    x = ast.parse('x = 1').body[0]
    z = ast.parse('z = 1').body[0]
    y = ast.Name(id='y', ctx=ast.Load())
    
    assert add.get_body(x=x, y=y) == [z]


# Generated at 2022-06-14 02:57:20.101392
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x, y):
        let(z)
        let(t)
        z = x + y
        t = x * y
        return z * t

    snippet_ = snippet(fn)
    x = ast.Name(id='x', ctx=ast.Load())
    y = ast.Name(id='y', ctx=ast.Load())
    my_body = snippet_.get_body(z=7, t=ast.Num(n=10))

# Generated at 2022-06-14 02:57:26.777897
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_to_test(a: int, b: int, c: Any) -> None:
        let(a)
        x = 10
        let(b)
        y = x
        extend(c)
        print(a, b, y)

    snippet_instance = snippet(snippet_to_test)
    body = snippet_instance.get_body(
        a='_py_backwards_a_0',
        b=ast.parse('_py_backwards_b_0').body[0],
        c=ast.parse('_py_backwards_c_0').body[0]
    )

# Generated at 2022-06-14 02:57:40.257779
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(a: int) -> int:
        let(x)
        let(y)
        x = 1
        y = 2
        res = x + y
        return res


# Generated at 2022-06-14 02:57:51.016888
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class A:
        def __getitem__(self, key: int) -> int:
            return key

    a = A()
    x = 0
    for i in range(1, 100):
        if i < 50:
            j = 4
        else:
            j = 3

        x += a[j]

    x += a[1]

    @snippet
    def test():
        x = 0
        for i in range(1, 100):
            if i < 50:
                j = let(4)
            else:
                j = let(3)

            let(x)
            x += a[j]

            let(i)
            if i == let(10):
                extend(let(['let(print)', 'print(1)']))


# Generated at 2022-06-14 02:57:53.280648
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import inspect
    from py_backwards import snippet

    factor = 10

# Generated at 2022-06-14 02:58:02.264261
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_add_behavior():
        x = 1

        # x += 1
        # x += 2
        let(x)
        x += 1
        x += 2
        y = 1



# Generated at 2022-06-14 02:58:13.948897
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2

    @snippet
    def foo(a, b, c=3, **kwargs):
        let(x)
        let(y)
        extend(kwargs)
        return x + y + a + b + c


# Generated at 2022-06-14 02:58:22.105424
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def get_body(x: int) -> ast.AST:
        let(x)
        x += 1
        y = 1
        return ast.parse(f'{x} + {y}').body[0]

    snippet = snippet(get_body)
    body = snippet.get_body(x=0)
    assert body[0].value.left.id == '_py_backwards_x_0'
    assert body[0].value.right.n == 1
    assert body[1].value.n == 1

# Generated at 2022-06-14 02:58:23.913600
# Unit test for function find_variables
def test_find_variables():
    assert find_variables(ast.parse('let(x)')) == ['x']



# Generated at 2022-06-14 02:58:33.602611
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_fn():
        let(1)
        let(2)
        a = 3
        let(f"{a}")
    

# Generated at 2022-06-14 02:58:55.744513
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def add_one(x: int) -> int:
        """Add 1 to variable x."""
        let(x)
        x += 1
        return x

    body = snippet(add_one).get_body()

    assert len(body) == 3

    x = ast.Name(id='_py_backwards_x_0', ctx=ast.Load())
    node = ast.AugAssign(op=ast.Add(), target=x, value=ast.Num(1))

    assert body[0].lineno == body[1].lineno
    assert body[0] == node

    node = ast.Return(value=x)  # type: ignore

    assert body[2].lineno == body[1].lineno
    assert body[2] == node


# Generated at 2022-06-14 02:59:03.923041
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def inc(x: int) -> int:
        let(y)
        y += 1
        return x + y

    body = inc.get_body(x=3)
    assert ast.dump(body) == '''
[Assign
  targets=[Name(id='_py_backwards_y_0', ctx=Store())],
  value=BinOp(left=Name(id='_py_backwards_y_0', ctx=Load()), op=Add(), right=Num(n=1))],
[Return(value=BinOp(left=Num(n=3), op=Add(), right=Name(id='_py_backwards_y_0', ctx=Load())))]
'''

# Generated at 2022-06-14 02:59:08.004759
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    let(x)
    let(y)
    y = x[1]
    print(y)
    """)
    assert list(find_variables(tree)) == ['x', 'y']


# Generated at 2022-06-14 02:59:15.192046
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f(x: int) -> None:
        let(y)
        y += 1
        y -= 1
        z = y

    body = f.get_body(y=1)
    assert len(body) == 2
    assert isinstance(body, list)
    assert type(body[0]) == ast.Assign
    assert body[0].targets == [ast.Name(id='_py_backwards_y_0')]
    assing_value = body[0].value
    assert type(assing_value) == ast.BinOp
    assert type(assing_value.left) == ast.Name
    assert assing_value.left.id == '_py_backwards_y_0'
    assert type(assing_value.op) == ast.Add

# Generated at 2022-06-14 02:59:23.238608
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_fn(x: float, y: float) -> None:
        let(z)
        z = x + y

    body = test_fn.get_body(x=1.0, y=1.0)
    assert len(body) == 1

    addition = body[0]
    assert isinstance(addition, ast.Assign)
    assert len(addition.targets) == 1

    target = addition.targets[0]
    assert isinstance(target, ast.Name)
    assert target.id == '_py_backwards_z_0'

    binop: ast.BinOp = addition.value
    assert isinstance(binop, ast.BinOp)
    assert isinstance(binop.left, ast.Num)

# Generated at 2022-06-14 02:59:30.294921
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x)  # x = _py_backwards_x_0
        let(y)  # y = _py_backwards_y_0
        let(z)  # z = _py_backwards_z_0
        y += 1  
        z += y
        z += y
        a = x + y
        b = x + z
        c = x + z
 
    print(*test_snippet.get_body())

# Generated at 2022-06-14 02:59:39.890828
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from textwrap import dedent
    from typing import Dict, List
    from typed_ast import ast3 as ast
    from .helpers import VariablesGenerator

    def snippet():
        let(x)
        x += 1
        y = 1

    source = get_source(snippet)
    tree = ast.parse(source)

    names = ['x', 'y']
    variables = {name: VariablesGenerator.generate(name)
                 for name in names}
                
    VariablesReplacer.replace(tree, variables)
    expected = '\n'.join((
        '{x} += 1',
        'y = 1'
    ))
    assert dedent(expected) == ast.unparse(tree)

# Generated at 2022-06-14 02:59:44.981841
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int) -> int:
        let(y)
        y += 1
        let(z)
        z.append(1)
        return y

    s = snippet(fn)
    body = s.get_body(y=1, z=[])
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].value, ast.Call)
    assert isinstance(body[1], ast.Return)



# Generated at 2022-06-14 02:59:57.618382
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 0
    class SnippetClass:
        @snippet
        def snippet_function(self, x):
            let(x)
            x += 1
            y = 1
    snippet_obj = SnippetClass()
    body = snippet_obj.snippet_function.get_body(x=x)
    assert body[0].value.id == '_py_backwards_x_0'
    assert body[0].targets[0].id == '_py_backwards_x_0'
    assert body[1].value.id == 'y'
    assert body[1].targets[0].id == 'y'

# Generated at 2022-06-14 03:00:03.350907
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f(a: int, b: int) -> int:
        let(x)
        return a + x

    tree = f.get_body(a=42, x=b)
    assert ast.dump(tree) == '''
[Expr(value=BinOp(left=Num(n=42), op=Add(), right=Name(id='b', ctx=Load())))]
'''