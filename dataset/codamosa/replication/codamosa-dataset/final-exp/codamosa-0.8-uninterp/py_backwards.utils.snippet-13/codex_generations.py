

# Generated at 2022-06-14 02:50:20.598351
# Unit test for method visit_ImportFrom of class VariablesReplacer
def test_VariablesReplacer_visit_ImportFrom():
    import os
    import tempfile
    import subprocess
    import sys
    import os.path

    temp_dir = tempfile.gettempdir()
    sys.path.append(temp_dir)
    temp_file = os.path.join(temp_dir, 'import.py')
    a_name = 'import_test'

    with open(temp_file, 'w+') as f:
        f.write("def get_a(): return 'hello'\n")

    fn = snippet(lambda: 0)

    tree = ast.parse("from import import get_a")
    variables = {
        'import': VariablesGenerator.generate(),
        'import_test': a_name
    }

    VariablesReplacer.replace(tree, variables)


# Generated at 2022-06-14 02:50:27.433785
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    node = ast.alias('a', 'b')
    variables = {'a': 'a_new', 'b': 'b_new'}
    new_node = VariablesReplacer.replace(node, variables)
    assert new_node.name == 'a_new'
    assert new_node.asname == 'b_new'

# Generated at 2022-06-14 02:50:36.563546
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    def my_import(a, b):
        import a as b
    tree = ast.parse(my_import.__code__.co_code)
    var = VariablesGenerator.generate('b')
    variables = {'b': var}
    tree = VariablesReplacer.replace(tree, variables)
    assert tree.body[0].body[0].names[0].asname == var

# Generated at 2022-06-14 02:50:42.030594
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)
    let(z)
    """
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'x', 'y', 'z'}


# Unit tests for class VariablesReplacer

# Generated at 2022-06-14 02:50:47.863584
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse(
        """
        extend(vars)
        print(x, y)
    """
    )
    variables = dict(vars=[ast.Assign(targets=[ast.Name(id=name, ctx=ast.Store())],
                                      value=ast.Num(n=n))
                           for n, name in zip(range(1, 3), ['x', 'y'])])

    extend_tree(tree, variables)

    assert compare_ast(tree,
                       """
                       x = 1
                       x = 2
                       print(x, y)
                       """)

# Generated at 2022-06-14 02:50:54.047952
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('1')
    extend_tree(tree, {'1': ast.parse('x = 1\ny = 2')})
    assert ast.dump(tree) == ast.dump(ast.parse('x = 1\ny = 2'))
    tree = ast.parse('1')
    extend_tree(tree, {'1': ast.parse('x = 1')})
    assert ast.dump(tree) == ast.dump(ast.parse('x = 1'))
    tree = ast.parse('x = 1\n1')
    extend_tree(tree, {'1': ast.parse('x = 1\ny = 2')})
    assert ast.dump(tree) == ast.dump(ast.parse('x = 1\nx = 1\ny = 2'))

# Generated at 2022-06-14 02:51:00.693052
# Unit test for function find_variables
def test_find_variables():
    source = '''\
    def test():
        let(a)
        let(b)
        return a'''

    tree = ast.parse(source)
    variables = find_variables(tree)

    assert list(variables) == ['a', 'b']
    assert tree == ast.parse('''\
    def test():
        return a''')



# Generated at 2022-06-14 02:51:06.872296
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    tree = ast.parse("from Stuff import foo, bar")
    replacer = VariablesReplacer({'Stuff': 'NewStuff'})
    replacer.visit(tree)
    print(ast.dump(tree))
    assert(ast.dump(tree) == "ImportFrom(module='NewStuff', names=[alias(name='foo', asname=None), alias(name='bar', asname=None)], level=0)")

# Generated at 2022-06-14 02:51:10.580602
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    expected_source = "y = 1"
    expected_ast = ast.parse(expected_source)

    @snippet
    def test_snippet():
        let(x)
        y = 1
    assert test_snippet.get_body() == expected_ast.body

# Generated at 2022-06-14 02:51:14.136358
# Unit test for function find_variables
def test_find_variables():
    @snippet
    def fn():
        let(x)
        x = 1

    assert fn.get_body() == [ast.Assign([ast.Name(id='_py_backwards_x_0')], ast.Num(1))]



# Generated at 2022-06-14 02:51:20.910621
# Unit test for function find_variables
def test_find_variables():
    """Unit tests for function find_variables."""
    assert list(find_variables(ast.parse('let(x)'))) == ['x']
    assert list(find_variables(ast.parse('let(x); let(y)'))) == ['x', 'y']
    assert list(find_variables(ast.parse('let(x); y'))) == ['x']



# Generated at 2022-06-14 02:51:27.345513
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    let(x)
    let(y)
    x = 1
    y = 2
    print(x, y)
    """)
    assert find_variables(tree) == ['x', 'y']
    tree = ast.parse("""
    let(x)
    let(y)
    x = 1
    y = 2
    print(x, y)
    """)
    assert find_variables(tree) == ['x', 'y']
    assert tree.body[1].body[1].targets[0].id == 'x'
    assert tree.body[2].body[1].targets[0].id == 'y'
    # Test that there is no ongoing mutation
    tree_copy = copy.deepcopy(tree)
    assert tree == tree_copy



# Generated at 2022-06-14 02:51:32.496466
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(x)\n')
    variables = {'x': [ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())], value=ast.Num(n=1))]}
    extend_tree(tree, variables)
    assert ast.dump(tree) == ast.dump(ast.parse('x = 1\n'))

# Generated at 2022-06-14 02:51:35.709158
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x: int, y: int) -> int:
        let(z)
        return z

# Generated at 2022-06-14 02:51:45.057261
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(a):
        let(x)
        let(y)
        extend(x)
        x = a
        y = x


# Generated at 2022-06-14 02:51:52.453747
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(x); extend(y);')
    variables = {'x': [ast.parse('a = b')], 'y': [ast.parse('a = b')]}

    extend_tree(tree, variables)

    assert get_source(tree) == 'a = b\na = b\n'

# Generated at 2022-06-14 02:52:00.652333
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x = 1
    let(y)
    x = let(y)
    """
    tree = ast.parse(source)
    result = list(find_variables(tree))
    assert len(result) == 2
    assert (result[0] in ['x', 'y'])
    assert (result[1] in ['x', 'y'])



# Generated at 2022-06-14 02:52:08.295000
# Unit test for function find_variables
def test_find_variables():
    source = """
    if True:
        a = 'a'
        let(b)
        b = a
        c = 'c'
        let(d)
        let(d)
        let(e)
    """
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert variables == ['b', 'd', 'e']



# Generated at 2022-06-14 02:52:19.619698
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)

    def func(x, y):
        let(z)
        let(t)
        return let(x)
    """
    tree = ast.parse(source)
    variables = set(find_variables(tree))
    assert variables == {'x', 'y', 'z', 't'}

# Generated at 2022-06-14 02:52:29.496366
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def get_body():
        let(x)
        x += 1
        y = 1
    
    s = snippet(get_body)
    body = s.get_body()
    assert [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ), ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ] == body


# Generated at 2022-06-14 02:52:45.423252
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = let(1)
    y = let(2)
    z = let(3)

    class C:
        def f(self):
            def g(x, y, z):
                return x + y + z  # type: ignore

            return g(x, y, z)

    source = get_source(C)
    tree = ast.parse(source)
    snippet_kwargs = {'x': x, 'y': y, 'z': z}
    variables = find_variables(tree)
    variables.update(snippet_kwargs)
    for key, val in variables.items():
        if isinstance(val, ast.Name):
            variables[key] = val.id
    variables = {name: VariablesGenerator.generate(name)
                 for name in variables}
    extend_tree

# Generated at 2022-06-14 02:52:47.553304
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    s = snippet(lambda x: x + 1)
    b = s.get_body()
    assert len(b) == 1 and isinstance(b[0], ast.Return)

# Generated at 2022-06-14 02:52:51.230441
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert str(snippet(lambda: let(1)).get_body()) == '_py_backwards_x_0\n'


# Example for method let:

# Generated at 2022-06-14 02:53:00.977799
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x: int, y: int = 5) -> None:
        x += 1
        let(z)
        z += 1
        print(x)
        if x < y:
            print(x, y)
        print(x)
        print(y)
        print(z)

    # snippet_kwargs = {
    #     'x': (x + 4),
    #     'y': (y + 2)
    # }
    snippet_kwargs = {
        'x': ast.BinOp(left=ast.Name(id='x'), op=ast.Add(), right=ast.Num(4)),
        'y': ast.BinOp(left=ast.Name(id='y'), op=ast.Add(), right=ast.Num(2))
    }

# Generated at 2022-06-14 02:53:13.080351
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_fn(x: int, y: str,
                a: List[int] = [1, 2, 3],
                b: Dict[int, str] = {1: 'one', 2: 'two'},
                c: Callable[[int], int] = lambda x: x + 1) -> int:
        let(x)
        x += 1
        y = 'a'
        a.append(x)
        extend(b)
        extend(c)
        return a, b, c

    snippet_ = snippet(test_fn)
    a, b, c = snippet_.get_body()

# Generated at 2022-06-14 02:53:23.430075
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    v = VariablesGenerator.generate('v')
    i = VariablesGenerator.generate('i')

    def snippet_f():
        let(v)
        i = 0

        for _ in range(5):
            extend(v)
            i += 1

        print(v, i)

    body = snippet(snippet_f).get_body()
    assert len(body) == 10
    for i in range(5):
        assert body[i].__class__.__name__ == 'Assign'
        assert body[i].value.__class__.__name__ == 'Num'
        assert body[i].value.n == i
        assert body[i].targets[0].__class__.__name__ == 'Name'
        assert body[i].targets[0].id == v



# Generated at 2022-06-14 02:53:31.930704
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Arrange
    @snippet
    def s() -> None:
        let(x)
        x += 1
        y = 1
        return x, y

    # Act
    body = s.get_body(x=1, y=2)

    # Assert
    assert ast.dump(body) == '''[
    AugAssign(target=Name(id='_py_backwards_x_0', ctx=Load()), op=Add(), value=Num(n=1)),
    Assign(targets=[Name(id='y', ctx=Store())], value=Num(n=1))
]'''



# Generated at 2022-06-14 02:53:35.437412
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func():
        let(x)
        let(y)
        x = x + 1
        y = x + 1
        return

    s = snippet(func)
    body = s.get_body()
    assert len(body) == 3
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[2], ast.Return)
    return

# Generated at 2022-06-14 02:53:44.022688
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def var_func():
        return None

    @snippet
    def test_snippet_fn(x: int, y: int, z: ast.AST, w: ast.Name, v: str) -> None:
        """Test snippet."""
        let(w)
        let(2)
        # noinspection PyUnresolvedReferences
        let(var_func())
        let(v)
        w.id = 'a'
        x += 1
        let(y)
        extend(z)


# Generated at 2022-06-14 02:53:53.580542
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: let(x)).get_body() == []
    assert snippet(lambda x: let(x) + 1).get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)))]
    assert snippet(lambda x: [let(x)]).get_body() == []

# Generated at 2022-06-14 02:54:03.727841
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fast_fib(n: int) -> int:
        let(n_minus_one)
        let(n_minus_two)
        extend(vars)
        n_minus_one = n - 1
        n_minus_two = n - 2
        if n_minus_one == 0:
            return 1
        if n_minus_two == 0:
            return 1
        return fast_fib(n_minus_one) + fast_fib(n_minus_two)


# Generated at 2022-06-14 02:54:09.407995
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    wrapper_source = '''
    snippet_code = snippet(lambda x: print(x))
    snippet_body = snippet_code.get_body(x=1)
    '''
    tree = ast.parse(wrapper_source)
    variables = {'x': ast.Num(1, lineno=1, col_offset=16)}
    VariablesReplacer.replace(tree, variables)
    expected = '''
    snippet_code = snippet(lambda x: print(x))
    snippet_body = snippet_code.get_body(x=1)
    '''
    assert(expected == ast.unparse(tree))

# Generated at 2022-06-14 02:54:17.636226
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x):
        let(y)
        return x

    tree = ast.parse('''if True:
        pass''')
    tree.body = foo.get_body(x=tree)

    assert ast.dump(tree) == '''Module(body=[If(test=NameConstant(value=True), body=[Pass()], orelse=[])])'''

# Generated at 2022-06-14 02:54:29.136622
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(x: int) -> None:
        x += 1
        let(y)
        y = 2
        extend(vars)
        print(x, y)

    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=2))]

    obj = snippet(foo)
    body = obj.get_body(vars=vars, y=ast.Name(id='foo', ctx=ast.Load()))
    assert len(body) == 4
    print(ast.dump(body))


# Generated at 2022-06-14 02:54:39.978978
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
        def foo():
            let(x)
            let(y)
            x += 1
            y = 1
            return x + y
    """

    tree = ast.parse(source, mode='exec')

    let_x = tree.body[0].body[1].args[0].id  # type: ignore
    let_y = tree.body[0].body[2].args[0].id  # type: ignore

    assert let_x == 'x'
    assert let_y == 'y'

    def foo():
        let(x)
        let(y)
        x += 1
        y = 1
        return x + y

    snippet_fn = snippet(foo)

    assert snippet_fn.get_body() == tree.body[0].body[1:]

    assert snippet_fn.get

# Generated at 2022-06-14 02:54:44.814164
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)
    x = 1
    y = 2
    """
    assert ['x', 'y'] == list(find_variables(ast.parse(source)))



# Generated at 2022-06-14 02:54:54.897629
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a, b):
        let(x)
        x = x + 1
        y = x

    tree = ast.parse(get_source(fn))
    assert tree.body[0].body[0].value.left.id == 'x'
    assert tree.body[0].body[1].value.args[0].id == 'x'

    body = fn.get_body(x=1, y=2)
    assert body[0].value.left.id == '_py_backwards_x_0'
    assert body[0].value.right.value == 1
    assert body[1].value.args[0].id == '_py_backwards_x_0'



# Generated at 2022-06-14 02:55:04.684676
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''let(x)
let(y)
y = 1
x = 2
print(x, y)'''
    tree = ast.parse(source)
    variables = {
        'x': VariablesGenerator.generate('x'),
        'y': VariablesGenerator.generate('y'),
    }
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)

# Generated at 2022-06-14 02:55:15.383360
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: let(x)).get_body() == []
    assert snippet(lambda: let(x)).get_body(x='x') == [ast.parse('x')]
    assert snippet(lambda: let(x + y)).get_body(x=1, y=1) == [ast.parse('1+1')]

    assert snippet(lambda: let(x + y)).get_body(x='x', y='y') == [ast.parse('x+y')]
    assert snippet(lambda: let([1, 2, 3])).get_body() == []
    assert snippet(lambda: let([1, 2, 3])).get_body(x=[1, 2, 3]) == [ast.parse('[1, 2, 3]')]

    assert snippet(lambda: let(x) + let(y)).get_

# Generated at 2022-06-14 02:55:16.026932
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:55:36.303867
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

    @snippet
    def f():
        let(x)
        x += 1

    body = f.get_body()
    assert body == [ast.AugAssign(target=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                  op=ast.Add(),
                                  value=ast.Num(n=1)), ]


# Public testing api:


# Generated at 2022-06-14 02:55:47.180803
# Unit test for function extend_tree

# Generated at 2022-06-14 02:56:01.700021
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x, y):
        let(x)
        x += 1
        y.name = 'a'
        return y


# Generated at 2022-06-14 02:56:11.934927
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_let(x: str, y: str, z: int) -> None:
        let(x)
        let(y)
        let(z)
        x += '1'
        y = '1'
    result = test_let.get_body(x='1', y='2', z=3)
    expected = [ast.Expr(ast.BinOp(ast.Name(_py_backwards_x_0),  # type: ignore
                                   ast.Add(), 
                                   ast.Str('1'))), 
                ast.Assign([ast.Name(_py_backwards_y_1, ast.Store())], 
                           [ast.Str('1')])]
    assert result == expected



# Generated at 2022-06-14 02:56:20.671418
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = let(1)
    b = let(2)
    c = let(3)
    d = extend((print, a, b, c))

    @snippet
    def f(a, b, c) -> None:
        d

    assert f.get_body() == [ast.Print(dest=None, values=[ast.Name(id='_py_backwards_a_0', ctx=ast.Load()),
                                                          ast.Name(id='_py_backwards_b_0', ctx=ast.Load()),
                                                          ast.Name(id='_py_backwards_c_0', ctx=ast.Load())],
                                      nl=True, lineno=8, col_offset=4)]

# Generated at 2022-06-14 02:56:26.399920
# Unit test for function extend_tree
def test_extend_tree():
    result = ast.parse("a = 6")
    extend_tree(result, {"a": [ast.parse("a = 1\na = 2").body[0]]})
    assert ast.dump(result) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=1)])"



# Generated at 2022-06-14 02:56:34.304964
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def example(x: int, y: int) -> None:
        """Function example

        Args:
            x: x
            y: y
        """
        let(z)
        a = x + y
        b = x + y + z

        extend(vars)

        return a + b

    vars = ast.parse(
        "x = 1\n"
        "y = 2\n"
        "z = 3\n"
    ).body

    output = example.get_body(vars=vars)


# Generated at 2022-06-14 02:56:40.766147
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def func():
        let(x)
        x += 1
        return x

    body = func.get_body(x=1)
    assert body == [
        ast.AugAssign(
            target=ast.Name(id='x', ctx=ast.Load()),
            op=ast.Add(),
            value=ast.Num(n=1)),
        ast.Return(value=ast.Name(id='x', ctx=ast.Load()))
    ]



# Generated at 2022-06-14 02:56:46.988173
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(var1: str) -> None:
        let(var1)
        var2 = var1 + '1'
        extend(var2)
        let(var3)
        var3 = 0
        print(var1, var2, var3)

    body = foo.get_body()
    assert len(body) == 3
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.Print)
    assert isinstance(body[2], ast.Assign)



# Generated at 2022-06-14 02:56:55.078967
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import zope.interface as zi
    import zope.component as zc

    def test() -> None:
        let(a)
        let(b)
        let(c)
        a = 1
        b = 2
        c = 3

    snip = snippet(test)
    body = snip.get_body()
    assert body == [ast.Assign([ast.Name('_py_backwards_a_0', ast.Store())],
                               ast.Num(1)),
                    ast.Assign([ast.Name('_py_backwards_b_0', ast.Store())],
                               ast.Num(2)),
                    ast.Assign([ast.Name('_py_backwards_c_0', ast.Store())],
                               ast.Num(3))]


# Generated at 2022-06-14 02:57:30.528377
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """The method snippet.get_body should return AST of snippet
    and replace variables with unique names.
    """
    def fn(x, y, z=None, *args, **kwargs):
        let(x)
        let(y)
        let(z)
        let(args)
        let(kwargs)
        extend(kwargs)

    snippet_ = snippet(fn)

    body = snippet_.get_body(x=1, y=2, z=3, kwargs={'x': 10, 'y': 20})
    assert len(body) == 3
    assert isinstance(body[0], ast.Expr)
    assert isinstance(body[1], ast.Assign)
    assert body[1].targets[0].id == '_py_backwards_kwargs_0'


# Generated at 2022-06-14 02:57:41.424394
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert get_source(snippet(lambda x: x + 1).get_body(x=1))  ==\
           '_py_backwards_x_0 + 1'

    assert get_source(snippet(lambda x, y=let(1): x + y).get_body()) ==\
           '_py_backwards_x_0 + _py_backwards_y_1'

    assert get_source(snippet(lambda x, y=let([1, 2]): x + y[1]).get_body()) ==\
           '_py_backwards_x_0 + _py_backwards_y_1[1]'

    assert get_source(snippet(lambda x=let(1): x).get_body()) ==\
           '_py_backwards_x_0'

    assert get

# Generated at 2022-06-14 02:57:52.456290
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_kwargs = {
        'x': VariablesGenerator.generate('x'),
        'y': VariablesGenerator.generate('y')
    }

    @snippet
    def code():
        extend(vars)
        print(x, y)

    vars = [
        ast.Assign(targets=[ast.Name(id=n, ctx=ast.Store())], value=ast.Num(n=i))
        for i, n in enumerate(['x', 'y'])
    ]

# Generated at 2022-06-14 02:57:53.160739
# Unit test for function extend_tree

# Generated at 2022-06-14 02:58:00.336815
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astunparse
    s = snippet(lambda: let(x) or x)
    expected = ast.parse("""x = 1
x = 2
""")
    assert astunparse.unparse(s.get_body({'x': [ast.Assign(targets=[ast.Name('x', ast.Store())],
                                                        value=ast.Num(1)),
                                                ast.Assign(targets=[ast.Name('x', ast.Store())],
                                                           value=ast.Num(2))]
                                         })) == astunparse.unparse(expected)

# Generated at 2022-06-14 02:58:05.188140
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def say_hello(name: str):
        let(x)
        x += 1
        y = 1
        print(name)

    expected = """
    _py_backwards_x_0 += 1
    y = 1
    print(name)
    """

    assert ast.dump(say_hello.get_body()) == expected

# Generated at 2022-06-14 02:58:10.817695
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_func(x: int, y: int) -> int:
        let(x)
        x += 1
        y = 1
        return y
    assert snippet(test_func).get_body() == ast.parse("""
_py_backwards_x_0 += 1
y = 1
    """).body  # type: ignore

# Generated at 2022-06-14 02:58:16.366261
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('\n'
        'def f(x):\n'
        '    extend(vars)\n'
    )
    vars = ast.parse('x = 1; x = 2').body
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:58:23.171622
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def code_snippet(x: int, y: int) -> None:
        let(x)
        let(y)
        x += 1
        y += 2

    @snippet
    def f(x: int, y: int) -> List[ast.AST]:
        let(x)
        let(y)

# Generated at 2022-06-14 02:58:25.929155
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    snippet_result = snippet(lambda x: 100 * x).get_body(let(x))
    assert snippet_result == [ast.Expr(ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()),
                                                 ast.Mult(),
                                                 ast.Num(100)))]


# Generated at 2022-06-14 02:59:16.248198
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(a):
        let(x)
        extend(y)
        let(z)
        return a + 1
    snippet_obj = snippet(f)
    body = snippet_obj.get_body(x=2, y=[ast.parse("a = 1"),ast.parse("b = 2")])
    assert body[0].value.value == 2
    assert body[1].value.value == 1
    assert body[2].value.value == 1


# Generated at 2022-06-14 02:59:18.932246
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    target = ast.parse('print(1)').body[0]
    test_body = snippet(lambda x: let(x)).get_body(x=target)
    assert test_body == target.body


# Generated at 2022-06-14 02:59:30.988943
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = snippet(lambda x: let(x))
    b = snippet(lambda x: let(x))
    c = snippet(lambda x: let(x))
    d = snippet(lambda x: let(x))

    def f1(x):
        let(x)
        let(x)
        x += 1
        x += 1
        return x

    def f2(x):
        let(x)
        x += 1
        return x

    def f3(x, y, z):
        let(x)
        let(y)
        let(z)
        z += 1
        return z
    body_f1 = a.get_body()
    body_f2 = b.get_body()
    body_f3 = c.get_body()
    body_f3_with_kwargs = d

# Generated at 2022-06-14 02:59:41.245277
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def inner(x: int) -> int:
        let(y)
        extend(a)
        return y + x


# Generated at 2022-06-14 02:59:47.104995
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)')
    body = ast.parse('x = 1').body[0]
    ext_body = ast.parse('x = 2').body[0]
    vars = {'vars': body}
    body.body = [ext_body]
    extend_tree(tree, vars)
    assert tree.body[0].body == [body, ext_body]

# Generated at 2022-06-14 02:59:57.318216
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _snippet(x, y):
        let(x)
        x += 1
        y = 1
        return y

    snippet_instance = snippet(_snippet)
    snippet_kwargs = {'x': 1, 'y': 1}
    actual_body = snippet_instance.get_body(**snippet_kwargs)
    expected_body = _snippet.__code__.co_code

    assert ast.dump(actual_body) == ast.dump(expected_body)

# Generated at 2022-06-14 03:00:06.669573
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # pylint: disable=R0201, W0613, C0103
    def foo(a, b, c=1):
        let(x)
        x += 1
        y = 1
        extend(vars)

    tree = snippet(foo).get_body()
    code = compile(tree, '<test>', 'exec')
    locals_ = {}
    exec(code, {}, locals_)  # type: ignore
    assert '_py_backwards_x_0' in locals_
    assert locals_['_py_backwards_x_0'] == 2
    assert 'y' in locals_
    assert locals_['y'] == 1