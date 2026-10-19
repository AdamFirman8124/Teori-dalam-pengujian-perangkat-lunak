

# Generated at 2022-06-14 02:51:02.636685
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x, y, z):
        let(x)
        x += 42
        assert z != 0
        y.append(x)

    with VariablesGenerator(['x', 'y', 'z']):
        body = fn.get_body(x=1, y=[], z=42)
        assert len(body) == 3
        assert body[0].value.left.id == '_py_backwards_x_0'
        assert isinstance(body[0].value, ast.AugAssign)
        assert isinstance(body[1], ast.Assert)
        assert isinstance(body[2], ast.Expr)

# Generated at 2022-06-14 02:51:07.866013
# Unit test for function extend_tree
def test_extend_tree():
    code = '''
    extend(vars)
    print(x, y)
    '''
    tree = ast.parse(code)
    vars = ast.parse('x = 1\nx = 2')
    extend_tree(tree, {'vars': vars})
    assert ast.dump(vars) == ast.dump(tree.body[:2])



# Generated at 2022-06-14 02:51:17.318653
# Unit test for function extend_tree
def test_extend_tree():
    fn = snippet(lambda: extend('a'))
    source = get_source(fn._fn)
    tree = ast.parse(source)
    variables = fn._get_variables(tree, {'a': [ast.Assign([ast.Name('x', ast.Store())], ast.Num(1)),
                                               ast.Assign([ast.Name('x', ast.Store())], ast.Num(2))]})
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert get_source(tree) == 'x = 1\nx = 2\n'



# Generated at 2022-06-14 02:51:24.255727
# Unit test for function extend_tree
def test_extend_tree():
    x = ast.parse('x = 1', mode='exec')
    y = ast.parse('y = 2', mode='exec')
    tree = ast.parse(extend.__doc__, mode='exec')
    extend_tree(tree, {'vars': [x, y]})
    tree_body = tree.body
    assert isinstance(tree_body[0], ast.Assign)
    assert isinstance(tree_body[1], ast.Assign)
    assert isinstance(tree_body[2], ast.Expr)

# Generated at 2022-06-14 02:51:29.064090
# Unit test for function find_variables
def test_find_variables():
    source = '''
        let(a)

        def foo():
            let(b)
            return b
    '''
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'a', 'b'}

# Generated at 2022-06-14 02:51:36.945843
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    extend(vars)
    
    print(x)
    """
    tree = ast.parse(source)
    assign1 = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                         value=ast.Num(n=1))
    assign2 = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                         value=ast.Num(n=2))
    extend_tree(tree, {'vars': [assign1, assign2]})
    code = compile(tree, '', 'exec')
    ns: Dict[str, Any] = {}
    exec(code, ns)
    assert ns['x'] == 2

# Generated at 2022-06-14 02:51:43.775067
# Unit test for function extend_tree
def test_extend_tree():
    mod = ast.parse('a = 1\nb = 2').body
    tree = ast.parse('extend(mod)')
    extend_tree(tree, {'mod': mod})
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=1)), Assign(targets=[Na' \
                             'me(id=\'b\', ctx=Store())], value=Num(n=2))])'



# Generated at 2022-06-14 02:51:48.555745
# Unit test for function find_variables
def test_find_variables():
    nodes = ast.parse('''
    let(x)
    let(y)
    let(z)
    ''').body
    assert(set(find_variables(nodes)) == {'x', 'y', 'z'})

# Generated at 2022-06-14 02:51:59.766507
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("let(a)\nextend(b)").body[0]
    tree.body.append(ast.parse("c = 1").body[0])

    variables = {'a': '_var', 'b': ast.parse("a = 1").body}
    extend_tree(tree, variables)

    expected_tree = ast.parse("a = 1\nc = 1\n_var = a").body
    assert tree.body == expected_tree


# Generated at 2022-06-14 02:52:04.109754
# Unit test for function find_variables
def test_find_variables():
    source = r"""
    let(x)
    print(x + 1)
    extend(y)
    let(z)
    """
    tree = ast.parse(source)
    variables = list(find_variables(tree))
    assert variables == ['x', 'y', 'z']


# Generated at 2022-06-14 02:52:14.541241
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = None
    y = None

    @snippet
    def f():
        let(x)
        x = 1
        y = 1
        return x + y

    assert len(f.get_body()) == 2
    expected_body = [ast.Assign([ast.Name(id='_py_backwards_x_0', ctx=ast.Store())], ast.Num(n=1)),
                     ast.Assign([ast.Name(id='y', ctx=ast.Store())], ast.Num(n=1))]
    assert f.get_body() == expected_body



# Generated at 2022-06-14 02:52:19.747370
# Unit test for function find_variables
def test_find_variables():
    source = """
        a
        let(x)
        1
        let(y)
        let(z)
    """

    tree = ast.parse(source)
    expected = find_variables(tree)
    print(expected)
    assert 'x' in expected
    assert 'y' in expected
    assert 'z' in expected



# Generated at 2022-06-14 02:52:22.889486
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('x = let(y); let(z)')
    assert list(find_variables(tree)) == ['y', 'z']



# Generated at 2022-06-14 02:52:27.198391
# Unit test for function find_variables
def test_find_variables():
    source = '''
let(x)
x += 1
y = 1
let(z)
'''
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert set(variables) == set(['x', 'z']), (set(variables), set(['x', 'z']))



# Generated at 2022-06-14 02:52:31.451472
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
let(x)
let(y)
let(z)
z = 1
''')

    assert find_variables(tree) == ['x', 'y', 'z']

# Generated at 2022-06-14 02:52:35.782335
# Unit test for function find_variables
def test_find_variables():
    source = """
        def a():
            let(x)
            let(y)
            print("end of function")
    """
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert variables == ['x', 'y']



# Generated at 2022-06-14 02:52:39.039080
# Unit test for function find_variables
def test_find_variables():
    source = """
var1 = let(1)
var2 = let(2)
    """
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'var1', 'var2'}



# Generated at 2022-06-14 02:52:48.252241
# Unit test for function find_variables
def test_find_variables():
    data = "let(x); let(y); x=2; y=3"
    tree = ast.parse(data)
    assert list(find_variables(tree)) == ['x', 'y']
    assert ast.dump(tree, annotate_fields=False) == \
        "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], " \
        "value=Name(id='y', ctx=Load())), Assign(targets=[Name(id='x', " \
        "ctx=Store())], value=Num(n=2)), Assign(targets=[Name(id='y', " \
        "ctx=Store())], value=Num(n=3))])"

# Generated at 2022-06-14 02:52:53.591355
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
    def func(x):
        let(a)
        let(b)
        x = 34
        let(c)
        let(d)
    """)
    assert find_variables(tree) == ['a', 'b', 'c', 'd']

# Generated at 2022-06-14 02:53:00.385087
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo():
        let(x)
        x += 1

    assert foo.get_body() == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                                        value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                                        op=ast.Add(),
                                                        right=ast.Num(n=1)))]



# Generated at 2022-06-14 02:53:11.429405
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet(a: int, b: int, c: int) -> int:
        return let(a) + let(b) * let(c)

    body = test_snippet.get_body(a=1, b=2, c=3)
    assert len(body) == 1
    assert isinstance(body[0], ast.BinOp)

    assert isinstance(body[0].left, ast.Num)
    assert body[0].left.n == 1

    assert isinstance(body[0].right, ast.BinOp)
    assert isinstance(body[0].right.left, ast.Num)
    assert body[0].right.left.n == 2

    assert isinstance(body[0].right.right, ast.Num)

# Generated at 2022-06-14 02:53:15.370357
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Test for method get_body deriving from class snippet
    def f():
        x = 10
        y = 20
        sum = x + y

    s = snippet(f)
    body = s.get_body()
    assert [x.lineno for x in body] == [3, 4]



# Generated at 2022-06-14 02:53:22.623624
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _test_snippet():
        let(x)
        x += 1
        y = 1
    assert snippet(_test_snippet).get_body() == [
        ast.Assign([ast.Name('_py_backwards_x_0', ast.Load())], ast.BinOp(ast.Name(
            '_py_backwards_x_0', ast.Load()), ast.Add(), ast.Num(1))),
        ast.Assign([ast.Name('y', ast.Store())], ast.Num(1)),
    ]


# Generated at 2022-06-14 02:53:32.736164
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test():
        a = 1
        b = 2
        let(x)
        x += 1
        y = 1
        extend(z)
        print(x, y, z)

# Generated at 2022-06-14 02:53:35.636674
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    tree = snippet(lambda: let(x) + x).get_body()
    assert isinstance(tree[0], ast.Assign)

# Generated at 2022-06-14 02:53:44.128805
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: let(x)).get_body(x=[ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                          value=ast.Num(n=1))]) == [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                                                         value=ast.Num(n=1))]

# Generated at 2022-06-14 02:53:53.960398
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Dummy(ast.AST):
        _fields = ()  # type: ignore

    # Check that snippet with let calls are replaced with unique variables
    @snippet
    def _(a: int, b: float) -> None:
        let(a)
        let(b)
        print(a + b)

    parent = ast.Module(body=[_(1, 2)])


# Generated at 2022-06-14 02:54:01.476575
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    code = '''
if __name__ == '__main__':
    a = 15
    let(a)
    extend(a)
    print("a =", a)
    '''
    snippet_func = snippet(lambda a: None)
    snippet_func.get_body(a=ast.parse(code).body[0].body[1])
    assert snippet_func.get_body(a=ast.parse(code).body[0].body[1]) == ast.parse(code).body[0].body[1:]

# Generated at 2022-06-14 02:54:08.254492
# Unit test for function extend_tree
def test_extend_tree():
    from .helpers import unparse

    tree = ast.parse("""
    extend([assign(a, 1), assign(b, 2)])
    """)
    extend_tree(tree, {'assign': ast.Assign})
    

# Generated at 2022-06-14 02:54:10.508283
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from py_backwards.transformers.tests.test_inline_locals import InlineLocalsTestCase

    InlineLocalsTestCase('test_get_body_with_few_let_statements')

# Generated at 2022-06-14 02:54:19.304302
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x)
        x += 1
        y = 1
        
    body = test_snippet.get_body()

    assert get_source(body[0]) == '_py_backwards_x_0 += 1'
    assert get_source(body[1]) == 'y = 1'

# Generated at 2022-06-14 02:54:28.711964
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(x: int, y: int) -> int:
        let(z)
        z = x + y
        return z

    snippet_ = snippet(foo)
    assert snippet_get_body(x=4, y=5) == [
        Assign(
            targets=[Name(id='_py_backwards_z_0', ctx=Store())],
            value=BinOp(
                left=Name(id='x', ctx=Load()),
                op=Add(),
                right=Name(id='y', ctx=Load()),
            ),
        ),
        Return(value=Name(id='z', ctx=Load())),
    ]

# Generated at 2022-06-14 02:54:39.592837
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test(x: int) -> None:
        let(y)
        let(z)
        if x == y:
            y += 1
        else:
            y += 2
        return z
    snp = snippet(test)
    body = snp.get_body(y=7, z=[ast.Pass()])

# Generated at 2022-06-14 02:54:50.896087
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class A:
        def __init__(self, x):
            self.x = x

    class B:
        def __init__(self, y):
            self.y = y

    @snippet
    def add_and_inc(a, b):
        let(x)
        x = a + b
        x += 1
        let(y)
        y = B(x)
        let(a)
        extend(y.y)
        a = A(2)
        return y


# Generated at 2022-06-14 02:55:01.287713
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_fn():
        let(x)  # noqa
        x = 1
        y = 0
        let(z)  # noqa
        return x + y + z

    body = test_fn.get_body(x=2, z=3)

# Generated at 2022-06-14 02:55:03.863635
# Unit test for function find_variables
def test_find_variables():
    """Tests find_variables function."""
    tree = ast.parse('let(x); let(y);')
    assert list(find_variables(tree)) == ['x', 'y']



# Generated at 2022-06-14 02:55:15.231867
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn():
        let(x)
        x += 1
        y = 1
    assert [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                       value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                       op=ast.Add(),
                                       right=ast.Num(n=1))),
            ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                       value=ast.Num(n=1))
            ] == fn.get_body()

    @snippet
    def fn():
        let(x)
        x += 1

# Generated at 2022-06-14 02:55:24.669556
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Unit test snippet."""
    import astor
    from ast import Expr, Assign, Module, Tuple, Name, Attribute, BinOp, Load, Add

    def _get(body=None, **args):
        return snippet(lambda: body).get_body(**args)

    assert astor.to_source(_get(x = 1, y = 2)) == '''
    y = 2
    x = 1
    '''

    assert astor.to_source(_get(let(x), x = 1, y = 2)) == '''
    y = 2
    _py_backwards_x_0 = 1
    '''

    assert astor.to_source(_get(x = 1, y = 2, body = let(x))) == '''
    y = 2
    x = 1
    '''

   

# Generated at 2022-06-14 02:55:28.357421
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse(
        """
        let(x)
        x = 2
        y = 1
        """
    )
    assert set(find_variables(tree)) == {'x'}



# Generated at 2022-06-14 02:55:43.571360
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x, y, z: let(x)).get_body()[0].id == '_py_backwards_x_0'
    print(snippet(lambda x, y, z: let(x)).get_body())
    x = ast.Name('x', ast.Store())
    assert snippet(lambda x, y, z: let(x) or let(y)).get_body()[0].id == '_py_backwards_x_0'
    assert snippet(lambda x, y, z: let(x) or let(y)).get_body()[1].id == '_py_backwards_y_0'
    assert snippet(lambda x, y, z: let(x) or let(y)).get_body()[2] is None

# Generated at 2022-06-14 02:55:49.917686
# Unit test for function find_variables
def test_find_variables():
    exec('x = let(1)\nx += let(2)\nprint(let(3))')


# Unit tests for function VariablesReplacer

# Generated at 2022-06-14 02:55:52.647140
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("let(x)")
    variables = find_variables(tree)
    assert len(variables) == 1
    assert next(variables) == 'x'



# Generated at 2022-06-14 02:55:58.093720
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Assert equal bodies of snippets
    s1 = snippet(lambda: None)
    s2 = snippet(lambda: None)
    assert s1.get_body() == s2.get_body()

    s1 = snippet(lambda x: None)
    s2 = snippet(lambda: None)
    assert s1.get_body() != s2.get_body()

    s1 = snippet(lambda x: None)
    s2 = snippet(lambda y: None)
    assert s1.get_body() != s2.get_body()



# Generated at 2022-06-14 02:56:08.727532
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def get_one():
        let(x)
        x += 1
        y = 1

    assert get_one.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1),
            )
        ),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1),
        ),
    ]

# Generated at 2022-06-14 02:56:15.031056
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet(a: ast.Name, b: ast.Name, c: str) -> None:
        let(a)
        let(b)
        x = a + b
        y = c
        print(y)


# Generated at 2022-06-14 02:56:23.012684
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test():
        let(x)
        let(y)
        x += 1
        y += 1
        return x+y


# Generated at 2022-06-14 02:56:27.283851
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(x: int, y: int) -> None:
        let(z)
        w = 0
        print(w + x + y + z)

    snippet_instance = snippet(snippet_fn)
    snippet_instance.get_body(w=0, x=1, y=2)

# Generated at 2022-06-14 02:56:35.597859
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    z = 3
    @snippet
    def test_fn():
        let(x)
        let(y)
        let(z)
        x += 2
        y += 1
        print(x, y, z)
    body = test_fn.get_body()
    assert isinstance(body, list)
    assert len(body) == 4
    assert body[0].value.targets[0].id == '_py_backwards_x_0'
    assert body[1].value.targets[0].id == '_py_backwards_y_0'
    assert body[2].value.targets[0].id == '_py_backwards_z_0'

# Generated at 2022-06-14 02:56:44.808626
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Simple
    @snippet
    def get_body_test(x: int, y: int, z: int):
        x += 1
        y = y + 2
        let(z)
        z += 3
        return x, y, z

    assert get_body_test.get_body(x=1, y=1, z=1) == [
        ast.parse('x += 1').body[0],
        ast.parse('y = y + 2').body[0],
        ast.parse('z += 3').body[0]]

    # Complex
    @snippet
    def get_body_test_extend(x: int, y: int, z: int, vars: ast.AST):
        extend(vars)
        x += 1
        y = y + 2
        let(z)


# Generated at 2022-06-14 02:56:54.969144
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Foo:
        @snippet
        def test(self):
            let(x)
            let(self.y)
            let(Foo.z)
            x = 1
            self.y = 3
            Foo.z = 5

    # SMELL: We assume that self, self.y, Foo.z are valid names

# Generated at 2022-06-14 02:57:12.221681
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('''
    extend(vars)
    y = 2.5
    ''')
    vars = ast.parse('''
x = 1
x = 3
    ''').body
    extend_tree(tree, {'vars': vars})
    assert(ast.dump(tree) == ast.dump('''
    x = 1
    x = 3
    y = 2.5
    '''))



# Generated at 2022-06-14 02:57:14.886374
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    tree = snippet(
        lambda: let(x))(
        x=1).get_body()

    assert tree[0].value.right.n == 1

# Generated at 2022-06-14 02:57:25.020594
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""extend(vars)
                        x = 1
                        y = 2""")
    vars = [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=1)),
            ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=2))]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:57:37.842298
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x']

    source = """
    let(x)
    let(y)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']

    source = """
    let(x)
    extend(y)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']

    source = """
    def f():
        pass
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == []



# Generated at 2022-06-14 02:57:39.718795
# Unit test for function find_variables

# Generated at 2022-06-14 02:57:46.839328
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x: int) -> None:
        let(y)
        y = x + 1

    assert fn.get_body(x=1) == [
        ast.Assign(targets=[ast.Name(
            id='_py_backwards_y_0', ctx=ast.Store())],
            value=ast.BinOp(left=ast.Num(n=1),
                            op=ast.Add(),
                            right=ast.Num(n=1)))
    ]



# Generated at 2022-06-14 02:57:58.119044
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x, y):
        let(x)
        x += 1
        y = 1
    assert len(foo.get_body()) == 2
    assert len(foo.get_body(y=2)) == 1
    assert isinstance(foo.get_body(y=2)[0], ast.Assign)
    @snippet
    def foo(x, y):
        extend(x)
        return (x, y)
    assert len(foo.get_body()) == 2
    assert isinstance(foo.get_body()[0], ast.Assign)
    assert isinstance(foo.get_body()[1], ast.Return)

# Generated at 2022-06-14 02:58:04.817010
# Unit test for function extend_tree
def test_extend_tree():
    def x():
        extend(vars)
        print(x, y)

    vars = [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=1)),
        ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=2))]

    # We check only body

# Generated at 2022-06-14 02:58:14.333332
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    x = 1
    y = 2
    z = 3
    
    def fn():
        let(x)
        let(y)
        print(x, y, z)
        extend(x)
        extend(y)
        
    snippet_obj = snippet(fn)
    x_assign = ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1))
    y_assign = ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=2))
    body = snippet_obj.get_body(
            x = [x_assign],
            y = [y_assign]
            )

# Generated at 2022-06-14 02:58:25.986435
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x, y: 42).get_body() == []
    assert snippet(lambda x: x + 1).get_body(x=1) == [
        ast.Expr(ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()), ast.Add(), ast.Constant(1, None)))]
    assert snippet(lambda x: x + 1).get_body(x=ast.Name('x', ast.Load())) == [
        ast.Expr(ast.BinOp(ast.Name('x', ast.Load()), ast.Add(), ast.Constant(1, None)))]

    node = snippet(lambda x: x + 1).get_body(x=ast.Name('x', ast.Load()))[0]

# Generated at 2022-06-14 02:58:57.889027
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from _py_backwards.utils import flatten
    @snippet
    def test(x, y):
        let(a)
        return a + 1

    snippets = test.get_body(x=1, y=2)
    assert len(snippets) == 1
    assert flatten("__py_backwards_a_0 = x\nreturn a_0 + 1") == flatten(snippets)

    snippets = test.get_body(x=1, y=2)
    assert len(snippets) == 1
    assert flatten("__py_backwards_a_0 = x\nreturn a_0 + 1") == flatten(snippets)

    snippets = test.get_body(x=1, y=2)
    assert len(snippets) == 1
    assert flatten

# Generated at 2022-06-14 02:59:03.571314
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = let(1)
    assert snippet(lambda: x + 1).get_body() == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())], value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()), op=ast.Add(), right=ast.Num(n=1)))]

# Generated at 2022-06-14 02:59:07.827466
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
let(x)

x = 1
y = 2
""")
    expected = {'x'}
    variables = find_variables(tree)
    assert variables == expected



# Generated at 2022-06-14 02:59:15.051442
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from py_backwards.transformers.base import GenericTransformer

    def func_1(x: int, y: int) -> int:
        let(z)
        return x + y + z

    def func_2(x: int, y: int) -> int:
        let(z)
        return x + y + z

    def expected(x: int, y: int) -> int:
        return x + y + _py_backwards_z_0

    snip = snippet(func_1)
    assert ast.dump(snip.get_body()) == ast.dump(ast.parse(
        get_source(expected)).body[0].body)

    trans = GenericTransformer()
    assert ast.dump(trans.apply(func_2).body) == ast.dump(
        trans.apply(expected).body)

# Generated at 2022-06-14 02:59:23.122760
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Helper function for running get_body()
    def get_body(*args, **kwargs):
        return snippet(snippet_function).get_body(*args, **kwargs)

    # Left side of tests
    example_return = ast.parse('return x + y').body[0]
    array_assign = ast.parse('x[0] = 1').body[0]
    x_1 = ast.parse('x = 1').body[0]
    y_2 = ast.parse('y = 2').body[0]
    z_1 = ast.parse('z = 1').body[0]
    # Right side of test

# Generated at 2022-06-14 02:59:34.173831
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 42
    snippet_kwargs = {'x': 1, 'y': 2}

    @snippet
    def test_snippet(x: int, y: int):
        let(x)
        x += y
        y = 2 + y
        extend(z)
        print(x, y)

    test_case = snippet_kwargs, 1 + 2, 2 + 2


# Generated at 2022-06-14 02:59:35.232901
# Unit test for function find_variables

# Generated at 2022-06-14 02:59:41.547029
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    obj = {'a': 2, 'b': 3}

    def _test(obj):
        obj.a += 1
        return obj.b

    source = get_source(_test)
    tree = ast.parse(source)
    fn = snippet(_test)
    body = fn.get_body(obj=obj)
    assert source == get_source(_test)
    ast.fix_missing_locations(tree)
    print(ast.dump(tree.body[0]))
    assert tree.body == body

# Generated at 2022-06-14 02:59:47.236102
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x, y):
        let(x)
        x += 1
        y = 1

    tester = snippet(test_snippet)
    assert tester.get_body(x='_x', y='_y') == [
        ast.Assign(targets=[ast.Name(id='_x', ctx=ast.Store())],
                   value=ast.BinOp(left=ast.Name(id='_x', ctx=ast.Load()), op=ast.Add(),
                                   right=ast.Num(n=1))),
        ast.Assign(targets=[ast.Name(id='_y', ctx=ast.Store())], value=ast.Num(n=1))
    ]

# Generated at 2022-06-14 02:59:52.250517
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""x = 1
    extend(y)
    extend(z)""")  # type: ignore
    extend_tree(tree, {'y': [ast.parse("x = 2")],
                        'z': ast.parse("print(x)")})  # type: ignore
    assert get_source(tree) == """x = 1
x = 2
print(x)""".strip()

# Generated at 2022-06-14 03:00:35.740337
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 5

    @snippet
    def fn(y):
        let(x)
        x += 1
        return x + y

    assert len(fn.get_body()) == 3

# Generated at 2022-06-14 03:00:40.723117
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_with_variables(x: int, y: int):
        let(x)
        x += 1
        y += 2
        return x, y

    tree = snippet(snippet_with_variables).get_body()
    assert len(tree) == 3
    assert isinstance(tree[0], ast.AugAssign)
    assert isinstance(tree[1], ast.Assign)
    assert isinstance(tree[2], ast.Return)