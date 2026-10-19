

# Generated at 2022-06-14 02:50:39.129262
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(x)")
    variables = {'x': [ast.parse('x = 1'),
                       ast.parse('x = 2')]}
    extend_tree(tree, variables)
    assert str(tree) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=2))])'
    

if __name__ == '__main__':
    test_extend_tree()

# Generated at 2022-06-14 02:50:43.771476
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""extend(vars)
x = 1
x = 2""")
    vars = ast.parse("""x = 1
x = 2""")
    extend_tree(tree, {'vars': vars})
    assert ast.dump(vars) == ast.dump(tree)


# Unit tests for function VariablesReplacer.replace

# Generated at 2022-06-14 02:50:50.489685
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
extend(vars)
""")
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=1)),
                                ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=2))]})
    assert ast.dump(tree) == ast.dump(ast.parse("""
x = 1
x = 2
"""))



# Generated at 2022-06-14 02:50:52.291389
# Unit test for function extend_tree

# Generated at 2022-06-14 02:51:04.620003
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
extend(x)
extend(y)
extend(z)
    """)
    extend_tree(tree, {'z': [
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                   value=ast.Num(n=1)),
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                   value=ast.Num(n=2)),
    ]})
    assert ast.dump(tree) == 'Module([Assign(targets=[Name(id=\'x\', ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id=\'x\', ctx=Store())], value=Num(n=2))])'



# Generated at 2022-06-14 02:51:12.539485
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def x():
        let(1)
        extend([ast.Expr(ast.Call(func=ast.Name(id='print', ctx=ast.Load()),
                                  args=[ast.Name(id='x', ctx=ast.Load())], keywords=[]))])

    body = snippet(x).get_body()
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].value, ast.Num)
    assert body[0].value.n == 1
    assert isinstance(body[1], ast.Expr)
    assert isinstance(body[1].value, ast.Call)
    assert isinstance(body[1].value.func, ast.Name)



# Generated at 2022-06-14 02:51:24.123975
# Unit test for function find_variables
def test_find_variables():
    class Test:
        @snippet
        def fn1(x: float, y: float) -> float:
            let(z)
            return x + y

        @snippet
        def fn2(x: float, y: float) -> float:
            let(z)
            return x + y

        @snippet
        def fn3(x: float, y: float) -> float:
            def fn(a: float, b: float) -> float:
                return a + b
            return fn(x, y)

    expected_fn1 = ['z']
    expected_fn2 = ['z']
    expected_fn3 = []

    assert Test.fn1.get_variables() == expected_fn1
    assert Test.fn2.get_variables() == expected_fn2
    assert Test.fn3

# Generated at 2022-06-14 02:51:27.355484
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .test_snippet import snippet_get_body_test
    snippet_get_body_test()



# Generated at 2022-06-14 02:51:29.696929
# Unit test for function extend_tree
def test_extend_tree():
    from .helpers import compile_and_run
    from .assertions import run_snippet_test


# Generated at 2022-06-14 02:51:34.752772
# Unit test for function extend_tree
def test_extend_tree():
    import textwrap
    from .tree import to_source

    tree = ast.parse(textwrap.dedent(
        """
            def f():
                extend(vars)
                print(x, y)
        """
    ))

    vars = ast.parse(textwrap.dedent(
        """
            x = 1
            x = 2
        """
    )).body

    extend_tree(tree, {'vars': vars})

    assert to_source(tree).strip() == textwrap.dedent(
        """
            def f():
                x = 1
                x = 2
                print(x, y)
        """
    ).strip()

# Generated at 2022-06-14 02:51:45.356108
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x = 2
    let(y)
    """
    tree = ast.parse(source)
    # results in {x: '_py_backwards_x', y: '_py_backwards_y'}
    variables = dict(find_variables(tree))
    assert variables == {'x': '_py_backwards_x', 'y': '_py_backwards_y'}
    assert len(variables) == 2



# Generated at 2022-06-14 02:51:56.439396
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_get_body():
        let(x)
        x += 1
        y = 1

    tree = snippet(snippet_get_body).get_body()

    assert isinstance(tree, list)
    assert len(tree) == 2

    assert isinstance(tree[0], ast.AugAssign)
    assert isinstance(tree[0].target, ast.Name)
    assert tree[0].target.id == '_py_backwards_x_0'
    assert isinstance(tree[0].op, ast.Add)
    assert isinstance(tree[0].value, ast.Num)
    assert tree[0].value.n == 1

    assert isinstance(tree[1], ast.Assign)
    assert isinstance(tree[1].targets[0], ast.Name)

# Generated at 2022-06-14 02:52:01.293962
# Unit test for function find_variables
def test_find_variables():
    # Test for empty function
    tree = ast.parse('def f(): pass')
    variables = list(find_variables(tree))
    assert [] == variables

    # Test for simple case

# Generated at 2022-06-14 02:52:08.645566
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("def f():\n"
                     "    extend(snippet)\n"
                     "    print(x)")

    code = ast.parse("x = 1\n"
                     "print(x)").body

    extend_tree(tree, {'snippet': code})
    assert ast.dump(tree) == ast.dump(ast.parse("def f():\n"
                                                "    x = 1\n"
                                                "    print(x)"))

# Generated at 2022-06-14 02:52:19.051089
# Unit test for function find_variables
def test_find_variables():
    # no variables
    source = '''
    def f(x):
        return x + 1
    x = 1
    '''
    assert find_variables(source) == []

    # one variable
    source = '''
    def f(x):
        let(y)
        return x + y
    x = 1
    '''
    assert find_variables(source) == ['y']

    # more variables
    source = '''
    def f(x):
        let(y)
        let(z)
        return x + y + z
    x = 1
    '''
    assert find_variables(source) == ['y', 'z']



# Generated at 2022-06-14 02:52:25.725832
# Unit test for function find_variables
def test_find_variables():
    assert list(find_variables(ast.parse('''
    let(x)
    a = 1

    let(y)
    b = 2

    let(z)
    let(w)
    c = 3
    four = 4


    let(u)
    def func():
        let(t)
        return t
    '''))) == ['x', 'y', 'z', 'u', 't']


# Generated at 2022-06-14 02:52:32.720072
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        y = x
        _ = x + y

    assert snippet(fn).get_body(x=1) == [
        ast.Assign([ast.Name('y', ast.Store(),
                             lineno=2, col_offset=4)],
                   ast.Num(1, lineno=2, col_offset=8)),
        ast.Assign([ast.Name('_', ast.Store(),
                             lineno=3, col_offset=4)],
                   ast.BinOp(ast.Num(1, lineno=3, col_offset=8),
                             ast.Add(),
                             ast.Name('y', ast.Load(),
                                      lineno=3, col_offset=11),
                             lineno=3, col_offset=8))]

# Generated at 2022-06-14 02:52:37.122916
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_test():
        let(x)
        x += 1
        y = 1

    assert snippet_test.get_body() == ast.parse('#!/usr/bin/env python3\n_py_backwards_x_0 += 1\ny = 1\n').body

# Generated at 2022-06-14 02:52:46.139221
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int, y: int) -> int:
        let(x)
        x += 1
        y = 1
        return x + y

    snippet = snippet(fn)
    snippet_var = ast.Name(id='snippet_var', ctx=ast.Load())
    let(snippet_var)

# Generated at 2022-06-14 02:52:52.987748
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(*args, **kwargs):
        let(1)
        let(2)
        extend(3)
        return 1


# Generated at 2022-06-14 02:53:02.840260
# Unit test for function find_variables
def test_find_variables():
    from py_backwards.variables import find_variables
    test_code = '''
    let(x)
    let(y)
    let(z)
    x * y * z
    '''
    source = ast.parse(test_code)
    assert list(find_variables(source)) == ['x', 'y', 'z']

# Generated at 2022-06-14 02:53:09.137182
# Unit test for function find_variables
def test_find_variables():
    snippet_args = dict(
        let(x=5),
        let(y='some string'),
        let(z=(x, y)),
        let(c='Hahahahahahahahahahahahahahahah'),
        let(d=(x, y, z, c))
    )
    assert find_variables(snippet(snippet1).get_body(**snippet_args)) == [
        'x', 'y', 'z', 'c'
    ]



# Generated at 2022-06-14 02:53:14.076348
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2

    @snippet
    def snippet_fn():
        let(x)
        x += 1
        y = 1

    expected = ast.Module(
        body=[
            ast.Expr(value=ast.BinOp(
                left=ast.Name(id=VariablesGenerator.current_var, ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1))),
            ast.Assign(
                targets=[ast.Name(id='y', ctx=ast.Store())],
                value=ast.Num(n=1))])

    assert snippet_fn.get_body() == expected.body


# Unit tests for let function

# Generated at 2022-06-14 02:53:19.577868
# Unit test for function find_variables
def test_find_variables():
    source = '''
    def foo(a):
        let(b)
        let(c)
        return a + b + c
    '''

    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'b', 'c'}

# Generated at 2022-06-14 02:53:26.368168
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_method():
        a, b = 0, 1
        let(a)
        a += 1
        let(b)
        b += 2

    snippet_obj = snippet(test_method)
    assert len(snippet_obj.get_body()) == 4
    assert isinstance(snippet_obj.get_body()[0], ast.Assign)
    assert isinstance(snippet_obj.get_body()[1], ast.AugAssign)
    assert isinstance(snippet_obj.get_body()[2], ast.Assign)
    assert isinstance(snippet_obj.get_body()[3], ast.AugAssign)

# Generated at 2022-06-14 02:53:35.996774
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # NOT a snippet and it is normal function
    def test_function(a, b):
        return a + b

    # snippet and it is not a normal function
    @snippet
    def test_snippet(a, b):
        return a + b

    assert test_function.__defaults__ is not None
    assert test_snippet.get_body().__defaults__ is not None

    assert test_function.__code__.co_varnames is None
    assert test_snippet.get_body().__code__.co_varnames is None

    assert test_function.__code__.co_filename is not None
    assert test_snippet.get_body().__code__.co_filename is not None

    assert test_function.__code__.co_code is not None

# Generated at 2022-06-14 02:53:40.988777
# Unit test for function find_variables
def test_find_variables():
    assert set(find_variables(
        ast.parse("""
a = 1
b = 2
let(c)
c = 1
""")
    )) == {'c'}

    assert set(find_variables(
        ast.parse("""
a = 1
b = 2
""")
    )) == set()

# Generated at 2022-06-14 02:53:49.055460
# Unit test for function find_variables
def test_find_variables():
    s = snippet(lambda x: let(x) + x)
    assert s._get_variables(s.get_body(), {}) == {'x': '_py_backwards_x_0'}  # type: ignore
    s = snippet(lambda x, y: let(x) + x + let(y) + y)
    assert s._get_variables(s.get_body(), {}) == {'x': '_py_backwards_x_0',  # type: ignore
                                                   'y': '_py_backwards_y_1'}  # type: ignore

# Generated at 2022-06-14 02:53:51.540425
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']


# Generated at 2022-06-14 02:54:00.949977
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(a=2); let(b=3); a+b')
    variables = {'a': 'a_0', 'b': 'b_0'}
    assert find_variables(tree) == ['a', 'b']
    extend_tree(tree, variables)
    assert ast.dump(tree) == 'Module(body=[Expr(value=BinOp(left=Name(id="a_0", ctx=Load()), op=Add(), right=Name(id="b_0", ctx=Load())))])'

# Generated at 2022-06-14 02:54:15.011542
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test(x, y):
        let(z)
        if x > y + z:
            return True
        else:
            return False

    snippet_obj = snippet(test)
    body = snippet_obj.get_body(x=1, y=2)

# Generated at 2022-06-14 02:54:24.520877
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import inspect

    with open('/Users/mxm/Documents/py-backwards/tests/test_snippet_get_body/test.txt', 'r') as f:
        tree = ast.parse(f.read())
    fn = tree.body[0].body[0].value.args[0].func
    source = inspect.getsource(fn)
    snippet_obj = snippet(fn)
    result = snippet_obj.get_body()
    assert source == inspect.getsource(result)



# Generated at 2022-06-14 02:54:32.180333
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    # Test case 1: no return
    def test_case_1(a, b):
        let(c)
        let(d)
        e = 1
        c = (a + b) * e

    snippet_1 = snippet(test_case_1)
    assert snippet_1.get_body(c=2, d=3) == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_c_0', ctx=ast.Store())], value=ast.BinOp(
            left=ast.BinOp(left=ast.Name(id='a', ctx=ast.Load()), op=ast.Add(), right=ast.Name(id='b', ctx=ast.Load())), op=ast.Mult(), right=ast.Num(n=1))),
    ]

# Generated at 2022-06-14 02:54:41.471706
# Unit test for function extend_tree
def test_extend_tree():
    def test_case(before: str, after: str) -> None:
        tree = ast.parse(before)
        extend_tree(tree, {})
        assert ast.dump(tree) == after

    test_case('extend({1: 2})', '2')
    test_case('extend({1: 2, 3: 4})', '4')
    test_case('def foo():\n    extend({"1": 2})', 'def foo():\n    pass')
    test_case('def foo():\n    "1"\n    extend({"1": 2})', 'def foo():\n    "1"\n    pass')

# Generated at 2022-06-14 02:54:46.340037
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int, y: int) -> None:
        let(z1)
        let(z2)
        z1 += x
        y += z2

    snippet = snippet(fn)
    body = snippet.get_body()
    assert len(body) == 2
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[1], ast.AugAssign)

# Generated at 2022-06-14 02:54:55.427810
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f():
        let(x)
        x += 1
        y = 1
        extend(v)
    
    # These values are used for testing snippet_kwargs
    k = ast.Name(id = "k")
    l = ast.Name(id = "l")
    m = ast.Name(id = "m")
    snippet_kwargs = {
        "x": k,
        "y": l,
        "v": m
    }
    
    # This is the correct result

# Generated at 2022-06-14 02:55:03.530351
# Unit test for function extend_tree
def test_extend_tree():
    def assert_tree_equals(actual: ast.AST, expected: ast.AST):
        assert ast.dump(actual) == ast.dump(expected)

    # assert_tree_equals(
    #     extend_tree(ast.parse('x = 1'), {'vars': ast.parse('x = 2')}),  # type: ignore
    #     ast.parse('x = 2; x = 1')  # type: ignore
    # )
    # assert_tree_equals(
    #     extend_tree([ast.parse('x = 1')], {'vars': [ast.parse('x = 2')]}),  # type: ignore
    #     ast.parse('x = 2; x = 1')  # type: ignore
    # )
    # assert_tree_equals(
    #     extend_tree(

# Generated at 2022-06-14 02:55:15.069612
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_function(x: int, a: int) -> None:
        let(y)
        let(z)
        y = x + y
        z = y * a
        x += 1

        extend(vars)
    tree = test_function.get_body(x=123, y=100, z=100, a=10, vars="""
x = 1
x = 2
""")

# Generated at 2022-06-14 02:55:24.569680
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    (x, y) = 0, 3

    def snippet_fn() -> None:
        let(x)
        let(y)
        y += 1
        z = 2
        extend(z)

    body = snippet(snippet_fn).get_body(x=x, y=1)

# Generated at 2022-06-14 02:55:36.877572
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Test snippet without any declares and extends.
    def test_fn():
        a = 1
        b = 2
        c = a + b
        return c

    tree = snippet(test_fn).get_body()

# Generated at 2022-06-14 02:55:55.701707
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int):
        """Docstring."""
        let(x)
        x += 1

    body = foo.get_body(x=10)
    assert isinstance(body, list)
    assert body[0].value.target.id == '_py_backwards_x_0'
    assert body[1].value.value.n == 11
    assert body[2].value.s == 'Docstring.'



# Generated at 2022-06-14 02:56:02.206825
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('a\nextend(params)\nb')
    extend_tree(tree, {'params': [ast.parse('c = 1\nd = 2')]})
    assert ''.join(ast.dump(node) for node in tree.body) == 'a\n\nc = 1\n\nd = 2\n\nb'

# Generated at 2022-06-14 02:56:12.333741
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x: int) -> int:
        let(y)
        return y + x
    
    snippet_ = snippet(f)
    variables = {
        'y': 42
    }
    ast_body = snippet_.get_body(x=2, y=42)
    assert ast_body[0].value.args[0].id == '_py_backwards_y_0'
    assert ast_body[0].value.args[1].n == 2
    assert ast_body[1].value.args[0].n == 42
    assert ast_body[1].value.args[1].n == 2
    assert isinstance(ast_body[2].value, ast.Num)
    assert ast_body[2].value.n == 44


# Generated at 2022-06-14 02:56:21.611616
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet1(a: int) -> None:
        let(b)
        b = a + 1
        print(a, b)

    @snippet
    def snippet2(a: int) -> None:
        let(b)
        b = a + 1
        print(a, b)

    assert snippet1.__name__ == 'snippet1'
    assert snippet2.__name__ == 'snippet2'

    assert snippet1.get_body(b=ast.Name(id='c', ctx=ast.Store())) == snippet2.get_body(
        b=ast.Name(id='c', ctx=ast.Store()))


# Generated at 2022-06-14 02:56:29.005009
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''def test(x):
        let(a)
        a = x * 2
        y = 1 + a
    '''
    tree = ast.parse(source)
    snippet = tree.body[0]
    variables = {'a': ast.Name(id='z')}
    variables = VariablesReplacer.replace(variables, variables)
    print(variables)
    body = snippet.body
    extend_tree(tree, variables)
    print(get_source(tree))
    assert get_source(body) == 'a = x * 2\ny = 1 + a'

# Generated at 2022-06-14 02:56:33.060104
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        extend(assignments)

        let(a)
        a += 1
        let(b)
        b += 1

    # Class snippet returns str
    result = snippet(f).get_body()
    check_result = ast.parse(
        "__py_backwards_a_0 += 1\n__py_backwards_b_0 += 1\n").body
    assert result == check_result

# Generated at 2022-06-14 02:56:42.751379
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet1():
        let(x)
        x += 2
        y = 2

    def snippet2():
        let(x)
        x = y
        let(y)
        y = 2

    def snippet3():
        let(x)
        x = y
        return None

    def snippet4():
        let(x)
        x(2)

    def snippet5():
        let(x)
        extend(vars)
        x = 1
        x = 2
        x = 3
        print(x)

    body1 = ast.parse('''_py_backwards_x_0 += 2
y = 2''').body[0].body

# Generated at 2022-06-14 02:56:48.281674
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: int = 1) -> int:
        let(a)
        a += x
        y += 1
        return a + y

    tree = foo.get_body()

# Generated at 2022-06-14 02:56:58.229521
# Unit test for function extend_tree
def test_extend_tree():
    fn = snippet(
        lambda x: extend(vars)
    )

# Generated at 2022-06-14 02:57:07.198433
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import find, get_non_exp_parent_and_index
    from .helpers import get_source
    from .helpers import VariablesGenerator
    x = 3
    def _test_snippet_get_body():
        let(x)
        y = x + 1
        extend(vars)
        print(y)
    tree = ast.parse(_test_snippet_get_body.__code__)
    snippet_kwargs = {}
    for node in find(tree, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == 'let':
            snippet_kwargs[node.args[0].id] = node.args[0]
    variables = snippet()._get_variables(tree, snippet_kwargs)

# Generated at 2022-06-14 02:57:41.250097
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: Union[int, str]) -> None:
        let(x)
        y = x
        print(y)

    assert test.get_body() == test.get_body(1)
    assert test.get_body() == test.get_body(x='1')



# Generated at 2022-06-14 02:57:52.302128
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:57:55.335329
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _f():
        let(print)
        return print

    snip = snippet(_f)
    expected_body = ast.parse('return print').body
    assert snip.get_body() == expected_body

# Generated at 2022-06-14 02:57:58.988473
# Unit test for function find_variables
def test_find_variables():
    assert eager(find_variables)(
        tree=ast.parse(
            """
            def func():
                let(a)
                let(b)
                let(c)
                print(a)
            """)) == ['a', 'b', 'c']



# Generated at 2022-06-14 02:58:06.325957
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        let(y)
        extend(vars)
        
    from py_backwards.transforms.import_replace import ImportReplace
    
    ast_ = snippet(snippet_fn).get_body(x='x', y='y', vars=[ast.Assign(targets=[ast.Name(id=x, ctx=ast.Store())],
                                           value=ast.Num(n=1))])
    tree = ast.Module(body=ast_)
    ImportReplace.replace(tree)
    assert get_source(tree) == 'x = 1'

# Generated at 2022-06-14 02:58:08.552159
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    print(snippet(test_get_body).get_body())
    assert snippet(test_get_body).get_body() == snippet(test_get_body_test_expected).get_body()



# Generated at 2022-06-14 02:58:12.685879
# Unit test for function find_variables
def test_find_variables():
    import astor

    source = """
    let(x)
    x += 1
    y = 1
    """
    tree = ast.parse(source)
    assert find_variables(tree) == ['x']
    assert astor.to_source(tree) == "x += 1\ny = 1\n"



# Generated at 2022-06-14 02:58:17.672485
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    let(a)
    let(b)
    print(a, b)
    """)

    result = set(find_variables(tree))
    expected = {"a", "b"}
    assert result == expected



# Generated at 2022-06-14 02:58:21.220498
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x: int) -> None:
        pass

    def func2() -> None:
        pass

    s = snippet(func)
    with pytest.raises(AssertionError):
        s.get_body(x=1)

# Generated at 2022-06-14 02:58:30.099141
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def get_body(x, y, **kwargs) -> List[ast.AST]:
        return snippet(foo).get_body(x=x, y=y, **kwargs)

    assert get_body(ast.Name('a', ast.Load()), ast.Name('b', ast.Load())) == [
        ast.Assign([ast.Name('a', ast.Store())], ast.Num(1)), ast.Assign([ast.Name('b', ast.Store())], ast.Num(2)),
        ast.Assign([ast.Name('a', ast.Store())], ast.Num(3)), ast.Assign([ast.Name('b', ast.Store())], ast.Num(4))]


# Generated at 2022-06-14 02:59:30.762105
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def body(x):
        let(x)
        x += 1
        y = 1

    snippet_ = snippet(body)

    result = snippet_.get_body(x = 10)

    assert len(result) == 2, 'fail snippet get body'

# Generated at 2022-06-14 02:59:41.047883
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(a, b):
        let(a)
        a += 1
        b += 1
        return a, b

# Generated at 2022-06-14 02:59:47.325908
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .annotations import T, Int, Float

    @snippet
    def add_one(x: T) -> T:
        let(y)
        y = 1
        return x + y

    # annotation need to be specified explicitly
    assert ast.dump(add_one.get_body(x=Float(10))) == 'Return(value=Add(left=Name(id="x", ctx=Load()), right=Name(id="y", ctx=Load())))'

    # annotation can be inferred automatically
    assert ast.dump(add_one.get_body(x=10)) == 'Return(value=Add(left=Name(id="x", ctx=Load()), right=Name(id="y", ctx=Load())))'


# Generated at 2022-06-14 02:59:55.733734
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # type: () -> None
    from .tree import dump, replace_at
    from .types import expression, statements
    from .. import tree

    x, y = ast.Name(id='x', ctx=ast.Load()), ast.Name(id='y', ctx=ast.Load())
    x_visible = ast.Name(id='x_visible', ctx=ast.Load())

    @snippet
    def snippet_func(arg: expression) -> statements:
        let(x)
        x += 1
        y = 1


# Generated at 2022-06-14 03:00:06.583528
# Unit test for function extend_tree
def test_extend_tree():
    ast_tree = ast.parse('''
    def f():
        let(x)
        x = 1
        y = 2
        extend(z)
        let(a)
        a = x
        b = y
    ''')
    extend_tree(ast_tree, {'x': ast.Name(id='x'), 'y': ast.Name(id='y')})

# Generated at 2022-06-14 03:00:14.342510
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # snippet._get_variables()
    snippet._get_variables(ast.parse('let(x)'),
                           {}) == {'x': '_py_backwards_x_0'}

    snippet._get_variables(ast.parse('let(x)\nlet(y)'),
                           {}) == {'x': '_py_backwards_x_0',
                                   'y': '_py_backwards_y_1'}

    snippet._get_variables(ast.parse('let(x)\nlet(y)').body[0],
                           {}) == {'x': '_py_backwards_x_0',
                                   'y': '_py_backwards_y_1'}


# Generated at 2022-06-14 03:00:20.294958
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import compare_trees
    @snippet
    def test():
        let(x)
        let(y)
        y = x - 1
    source = get_source(test)
    tree = ast.parse(source)
    variables = test._get_variables(tree, {})
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert compare_trees(test.get_body(), tree.body[0].body)

# Generated at 2022-06-14 03:00:29.075445
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    for counter in [0, 1, 2]:
        @snippet
        def get_body(may_be_mutated: int) -> None:
            let(counter)
            let(may_be_mutated)
            counter += 1
            may_be_mutated += 1

        assert get_body.get_body(may_be_mutated=1) == [
            ast.AugAssign(ast.Name('_py_backwards_counter_0', ast.Store()),
                          ast.Add(),
                          ast.Num(1)),
            ast.AugAssign(ast.Name('may_be_mutated', ast.Store()),
                          ast.Add(),
                          ast.Num(1))
        ]