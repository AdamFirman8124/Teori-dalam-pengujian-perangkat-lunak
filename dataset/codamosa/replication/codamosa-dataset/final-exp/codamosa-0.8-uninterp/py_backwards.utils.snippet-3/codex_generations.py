

# Generated at 2022-06-14 02:50:17.195663
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def run(# pylint: disable=unused-variable
            arg: Variable = 'str') -> int:
        let(x)
        if x:
            let(y)
            return y

        return 0

    assert snippet(run).get_body() == [
        ast.If(
            test=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
            body=[ast.Assign(
                targets=[ast.Name(id='_py_backwards_y_0', ctx=ast.Store())],
                value=ast.Name(id='_py_backwards_y_0', ctx=ast.Load()))],
            orelse=[])]



# Generated at 2022-06-14 02:50:27.659428
# Unit test for method visit_ImportFrom of class VariablesReplacer
def test_VariablesReplacer_visit_ImportFrom():
    import ast
    class VariablesReplacer(ast.NodeTransformer):
        """Replaces declared variables with unique names."""
        def __init__(self, variables: Dict[str, Variable]) -> None:
            self._variables = variables
        def _replace_field_or_node(self, node: T, field: str, all_types=False) -> T:
            value = getattr(node, field, None)
            if value in self._variables:
                if isinstance(self._variables[value], str):
                    setattr(node, field, self._variables[value])
                elif all_types or isinstance(self._variables[value], type(node)):
                    node = self._variables[value]  # type: ignore
            return node

# Generated at 2022-06-14 02:50:33.173119
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    alias = ast.alias(name="random", asname="rand")
    import_node = ast.ImportFrom(module="", names=[alias])
    tree = ast.Module(body=[import_node])
    # NOTE: in Python 3.8, the alias name is not rewritten
    variables = {"random": "numpy.random", "rand": "numpy.random"}
    VariablesReplacer.replace(tree, variables)
    assert alias.name == "numpy.random"  # type: ignore
    assert alias.asname == "rand"  # type: ignore


# Generated at 2022-06-14 02:50:39.443848
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def a(x: int) -> int:  # type: ignore
        let(y)
        return y

    tree = a.get_body(y=1)
    assert tree[0].value.n == 1  # type: ignore

# Generated at 2022-06-14 02:50:42.280511
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    assert get_source(snippet(lambda: let(ast.Name('a', ast.Load()))).get_body()) == 'a = 1'


# Generated at 2022-06-14 02:50:44.138586
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
let(x)
x += 1
""")
    assert set(find_variables(tree)) == set(['x'])

# Generated at 2022-06-14 02:50:50.323189
# Unit test for function find_variables
def test_find_variables():
    """
    Find variables should find variables and remove them
    """
    code = """let(x)
x = 1
let(y)
y = 2
let(z)
z = 3
z += 1
let(a)"""
    tree = ast.parse(code)
    names = find_variables(tree)
    assert names == ['x', 'y', 'z', 'a']
    assert get_source(tree) == """x = 1
y = 2
z = 3
z += 1"""



# Generated at 2022-06-14 02:50:54.087469
# Unit test for function find_variables
def test_find_variables():
    fn = snippet(lambda x: let(x))
    source = get_source(fn._fn)
    tree = ast.parse(source)
    assert fn._find_variables(tree) == {'x': VariablesGenerator.generate('x')}



# Generated at 2022-06-14 02:51:00.750147
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import_tree = ast.parse('from my_module import *').body[0]
    import_tree = VariablesReplacer.replace(import_tree, {'my_module': 'new_module'})
    import_tree = ast.fix_missing_locations(import_tree)
    assert get_source(import_tree) == 'from new_module import *'



# Generated at 2022-06-14 02:51:02.702939
# Unit test for method visit_ImportFrom of class VariablesReplacer
def test_VariablesReplacer_visit_ImportFrom():
    tree = ast.parse("from import_test import a, b")
    variables = {"import_test": "import_test_new"}
    VariablesReplacer.replace(tree, variables)
    module = tree.body[0].module
    assert module == "import_test_new"

# Generated at 2022-06-14 02:51:22.512026
# Unit test for function extend_tree
def test_extend_tree():
    import ast
    var_x = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=1))
    var_y = ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                       value=ast.Num(n=2))
    var_x1 = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=3))
    var_y1 = ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                       value=ast.Num(n=4))

# Generated at 2022-06-14 02:51:27.980480
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: let(x))(x=[10]).get_body() == [ast.AugAssign(target=ast.Name(id='_py_backwards_x_0', ctx=ast.Store()), op=ast.Add(), value=ast.Num(n=1))]

# Generated at 2022-06-14 02:51:38.395203
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert [] == snippet(lambda:
                         let(x)).get_body()


# Generated at 2022-06-14 02:51:46.793577
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def add(x: int, y: int) -> int:
        let(a)
        a += 1

        let(b)
        b += 1

        let(c)
        c += 1

        return a + b + c

    tree = snippet(add).get_body(x=1, y=2)
    assert len(tree) == 4
    for i, node in enumerate(tree):
        assert isinstance(node, ast.Assign)
        assert len(node.targets) == 1
        var = node.targets[0]
        assert isinstance(var, ast.Name)
        assert var.id == f'_py_backwards_a_{i}'
        assert isinstance(node.value, ast.Name)
        assert node.value.id == var.id



# Generated at 2022-06-14 02:51:53.121342
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import get_ast_node_source
    from .test_utils import strip

    @snippet
    def test():
        let(x)
        x += 1
        y = 1

    assert strip(get_ast_node_source(test.get_body())) == strip('''\
        _py_backwards_x_0 += 1
        y = 1''')



# Generated at 2022-06-14 02:52:01.377288
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x, y):
        let(x)
        x += 1
        y = 1
        return y
    
    body = foo.get_body(x=1, y=2)
    
    assert len(body) == 2
    assert isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[1], ast.Assign) and isinstance(body[1].value, ast.Num)

# Generated at 2022-06-14 02:52:11.648884
# Unit test for function extend_tree
def test_extend_tree():
    # Source code with
    code = """
    extend(vars)
    print(x, y)
    """

    # Variables, which we want to extend the code with
    vars = [
        ast.Assign(
            [ast.Name(id='x', ctx=ast.Store())],
            ast.Num(n=1)
        ),
        ast.Assign(
            [ast.Name(id='x', ctx=ast.Store())],
            ast.Num(n=2)
        )
    ]

    # Expected result after extend_tree function

# Generated at 2022-06-14 02:52:21.490573
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # test case 1
    def test_snippet_get_body_case_1(a: int, b: int) -> int:
        let(c)
        c = a + b
        d = a + b + c
        return d
    tree = test_snippet_get_body_case_1.get_body(a=1, b=4)

# Generated at 2022-06-14 02:52:27.258634
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo():
        let(x)
        x += 1
        y = 1
        extend(vars)
        x = y  # type: ignore
        y = x  # type: ignore
        print(x, y)

    x = 1
    vars = [
        ast.Assign(
            [ast.Name(id='x', ctx=ast.Store())],
            ast.Num(n=x)
        )
    ]

# Generated at 2022-06-14 02:52:38.897626
# Unit test for function extend_tree
def test_extend_tree():
    x = 1
    vars = [
        ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(1)),
        ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(2)),
        ast.Expr(ast.Call(func=ast.Name(id='print', ctx=ast.Load()),
                          args=[ast.Name(id='x', ctx=ast.Load())], keywords=[])),
    ]

# Generated at 2022-06-14 02:52:57.060517
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def add_one_to(x):
        let(x)
        x += 1
        y = 1

    snippet_obj = snippet(add_one_to)
    body = snippet_obj.get_body(x=1)
    assert body == [ast.Assign([ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                               ast.BinOp(ast.Name(id='_py_backwards_x_0',
                                                  ctx=ast.Load()),
                                         ast.Add(),
                                         ast.Num(1))),
                     ast.Assign([ast.Name(id='y', ctx=ast.Store())],
                               ast.Num(1))]


# Generated at 2022-06-14 02:52:57.867390
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:05.926460
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(variables)
    """)
    variables = {'variables': [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store()),
                                                   ast.Name(id='b', ctx=ast.Store())],
                                        value=ast.Num(n=1))]}

    extend_tree(tree, variables)
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id=\'b\', ctx=Store())], value=Num(n=1))])'

# Generated at 2022-06-14 02:53:12.853070
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    s = snippet
    source = get_source(s)
    tree = ast.parse(source)
    assert_equals(len(tree.body[0].body), 1)
    # Generate class snippet
    assert_equals(type(tree.body[0].body[0]), ast.ClassDef)
    # Generate function get_body
    assert_equals(len(tree.body[0].body[0].body), 1)
    assert_equals(type(tree.body[0].body[0].body[0]), ast.FunctionDef)
    # Generate function _get_variables
    assert_equals(len(tree.body[0].body[0].body[0].body), 1)

# Generated at 2022-06-14 02:53:23.173604
# Unit test for function extend_tree
def test_extend_tree():
    snippet_code = '''
    extend(vars)
    x = 1
    '''
    snippet_ast = ast.parse(snippet_code)
    vars_code = '''
    x = 2
    '''
    vars_ast = ast.parse(vars_code)
    extend_tree(snippet_ast,
                {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(1)),
                          ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(2))]})
    assert snippet_ast is not None
    assert snippet_ast.body[0].value.value == 2  # type:

# Generated at 2022-06-14 02:53:29.946442
# Unit test for function extend_tree
def test_extend_tree():
    code = """
extend(variables)
print(x)
    """

    variables = ast.parse("x = 1; x = 2").body
    tree = ast.parse(code)
    extend_tree(tree, variables)

    assert ast.dump(tree) == "Module([Print(dest=None, values=[Name(id='x', ctx=Load())], nl=True)])"

# Generated at 2022-06-14 02:53:36.585613
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:43.005676
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = let
    y = let
    z = let

    def test():
        x = 1
        y = 2
        z = 3

    var = snippet(test)
    test_body = var.get_body(x='x', y='y')
    assert test_body[0].value.args[0].s == 'x'
    assert test_body[1].value.args[0].s == 'y'
    assert test_body[2].value.args[0].s == 'z'



# Generated at 2022-06-14 02:53:44.536982
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:54.035521
# Unit test for function extend_tree
def test_extend_tree():
    snippet_fn = snippet(lambda x, y: extend(x))
    func_def = snippet_fn.get_body(x=[ast.Assign(
        targets=[ast.Name(id=':', ctx=ast.Store())],
        value=ast.Num(n=1),
        lineno=1,
        col_offset=0
    )])

    assert isinstance(func_def[0], ast.Assign)
    assert isinstance(func_def[0].targets[0], ast.Name)
    assert func_def[0].targets[0].id == ':'
    tree = ast.parse("""
x = 1
x = 2
x = 3
x = 4""")
    extend_tree(tree, {':': func_def[0]})

# Generated at 2022-06-14 02:54:06.819627
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet(x: int, y: int) -> None:
        let(z)
        assert x + y == z

    tree = my_snippet.get_body(x=1, y=2)
    assert len(tree) == 2
    assert isinstance(tree[0], ast.Assert)
    code = compile(ast.Module(body=tree), '', 'exec')
    assert eval(code) is None

# Generated at 2022-06-14 02:54:10.946851
# Unit test for function find_variables
def test_find_variables():
    snippet_source = '''
    let(x)
    x += 1
    '''

    tree = ast.parse(snippet_source)
    names = list(find_variables(tree))

    assert names == ['x']


# Generated at 2022-06-14 02:54:25.982969
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    _ = let
    x = 1
    y = 2
    source = get_source(snippet.get_body)
    assert source == '''
        
        _ = let
        x = 1
        y = 2

    '''
    tree = ast.parse(source)
    names = find_variables(tree)
    variables = {name: VariablesGenerator.generate(name) for name in names}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)

# Generated at 2022-06-14 02:54:32.394162
# Unit test for function extend_tree
def test_extend_tree():
    @snippet
    def func():
        a = 1
        extend(vars)

    vars = ast.parse('a = 2; b = 1;').body
    tree = func.get_body(vars=vars)
    assert len(tree) == 2
    assert isinstance(tree[0], ast.Assign)
    assert ast.dump(tree[0].value) == 'Num(n=1)'
    assert ast.dump(tree[1]) == 'Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=2))'
    assert ast.dump(tree[0]) == 'Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=1))'



# Generated at 2022-06-14 02:54:37.247876
# Unit test for function find_variables
def test_find_variables():
    code = """
    let(x)
    print(x)
    """
    tree = ast.parse(code)
    variables = find_variables(tree)
    assert list(variables) == ['x']



# Generated at 2022-06-14 02:54:47.201476
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
    def test():
        let(x)
        x += 1
        let(y)
        y = y + 1
        let(z)
        z = 2
    """
    tree = ast.parse(source)
    variables = find_variables(tree)
    res = VariablesReplacer.replace(tree, variables)
    expected = """
    def test():
        _py_backwards_x_0 += 1
        _py_backwards_y_1 = _py_backwards_y_1 + 1
        _py_backwards_z_2 = 2
    """
    assert ast.dump(res) == ast.dump(ast.parse(expected))



# Generated at 2022-06-14 02:54:51.413660
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f1():
        let(x)
        x += 1

    def f2():
        extend(nodes)
        print(x)

    assert isinstance(snippet(f1).get_body()[0], ast.Assign)
    assert isinstance(snippet(f2).get_body(), list)

# Generated at 2022-06-14 02:54:56.625681
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    result = snippet(lambda: let(x) or let(y)).get_body(x=[ast.parse('y = 1').body[0], ast.parse('y = 2').body[0]])
    assert len(result) == 1
    assert result[0] == ast.parse('''
x = 1
x = 2''').body[0]

# Generated at 2022-06-14 02:55:01.724416
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a: int, b: int) -> None:
        let(x)
        extend(vars)
        x = 1
        print(x, y)

    tree = ast.parse('x = 2')
    vars = tree.body
    actual = fn.get_body(vars=vars)

    expected = ast.parse('''
x = 1
print(x, y)''').body
    assert actual == expected

# Generated at 2022-06-14 02:55:07.462837
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def method_snippet():
        let(x)
        x += 1
        y = 1

    snippet_obj = snippet(method_snippet)
    assert snippet_obj.get_body() == method_snippet()._body

# Generated at 2022-06-14 02:55:27.102114
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = ast.Name(id='_py_backwards_x_0')
    y = ast.Name(id='y')
    z = ast.Name(id='z')
    
    @snippet
    def test():
        let(x)
        let(y)
        x += 1
        y += 1
        z += 1
        assert x == y


# Generated at 2022-06-14 02:55:42.191492
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_get_body():
        let(a)
        extend_body = let(a)
        a += 1
        let(b)

    assert snippet_get_body.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='a', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='a', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ),
        ast.Assign(
            targets=[ast.Name(id='b', ctx=ast.Store())],
            value=None
        )
    ]

# Generated at 2022-06-14 02:55:48.622499
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        x += 1
        return x

    snippet_instance = snippet(snippet_fn)
    out = snippet_instance.get_body(x=1)

    assert out == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ),
        ast.Return(value=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()))
    ]

# Generated at 2022-06-14 02:55:57.266197
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet1 = snippet(lambda: "hello")
    snippet2 = snippet(lambda: let(x) and x*2 + 2)
    snippet3 = snippet(lambda: let(x) and print(x))
    snippet4 = snippet(lambda: let(sin) and let(x) and sin(x))
    snippet5 = snippet(lambda: let(sin) and let(x) and print(sin(x)))
    snippet6 = snippet(lambda: let(x) and let(y) and let(z) and x*y + z)
    snippet7 = snippet(lambda: extend(x) and x.append(1))
    snippet8 = snippet(lambda: extend(x) and print(x))
    snippet9 = snippet(lambda: extend(x) and extend(y) and extend(z) and print(x, y, z))

   

# Generated at 2022-06-14 02:56:08.349202
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import get_source
    
    
    def my_fn(x: int) -> int:
        let(y)
        extend(x)
        let(z)
        return y + z + 10
    
    
    snippet = snippet(my_fn)
    source = get_source(my_fn)
    body = snippet.get_body(x=[ast.Assign([ast.Name(id='y', ctx=ast.Store())], ast.Num(n=10)),
                                  ast.Assign([ast.Name(id='y', ctx=ast.Store())], ast.Num(n=20))],
                             z=[ast.Assign([ast.Name(id='z', ctx=ast.Store())], ast.Num(n=1))])

# Generated at 2022-06-14 02:56:10.837907
# Unit test for function find_variables

# Generated at 2022-06-14 02:56:23.984231
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    let_var = ast.Name(id='let_var', ctx=ast.Load())
    extend_var = ast.Name(id='extend_var', ctx=ast.Load())

    @snippet
    def my_snippet():
        let(let_var)
        let_var *= 2
        extend(extend_var)
    
    assert my_snippet.get_body(let_var='abc', extend_var=[
        ast.parse('y = 1').body[0],
        ast.parse('y = 2').body[0],
    ]) == [
        ast.parse('y = 1').body[0],
        ast.parse('y = 2').body[0],
        ast.parse('abc *= 2').body[0],
    ]

# Generated at 2022-06-14 02:56:29.373970
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x += 1
    y = 1
    if True:
        a = 5
        let(b)
        c = 1
        d = [1, 2, 3]
        if False:
            let(c)
            print(1)
        else:
            let(c)
            print(2)
        print(3)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'b', 'c']



# Generated at 2022-06-14 02:56:36.012190
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def a():
        let(x)

        def b():
            print(x)

        b()

    s = snippet(a)

# Generated at 2022-06-14 02:56:40.501738
# Unit test for function find_variables
def test_find_variables():
    ast_tree = ast.parse('''
        let(a)
        b = 1
        c = 1
        let(d)
        e = 1
        let(f)
        g = 1
        ''')
    assert list(find_variables(ast_tree)) == ['a', 'd', 'f']


# Generated at 2022-06-14 02:57:16.385771
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(x: int, y: int) -> None:
        let(z)
        q = x + y
        t = x - y
        print(x, y, z, q, t)

    s = snippet(snippet_fn)
    lst = s.get_body(x=1, y=2, z=3)
    assert lst[0].value.left.id == "_py_backwards_q_0"
    assert lst[1].value.left.id == "_py_backwards_t_1"
    assert isinstance(lst[2], ast.Print)
    assert lst[2].dest is None
    assert isinstance(lst[2].values[0].value, ast.Num)
    assert lst[2].values[0].value.n == 1


# Generated at 2022-06-14 02:57:24.998301
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: int) -> None:
        let(x)
        z = x + y + 1
        x = 2
        y = 3

    tree = ast.parse(dedent("""
    def foo():
        _py_backwards_x_0 = 1
        z = _py_backwards_x_0 + y + 1
        y = 3
    """))

    # x = 1
    # y = 2
    # print(x)
    # x = 3
    variables = {'x': [ast.parse('x = 1')],
                 'y': ast.parse('y = 2')}

    variables = snippet(foo)._get_variables(tree, variables)
    extend_tree(tree, variables)

# Generated at 2022-06-14 02:57:35.429817
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)')
    vars_values = [ast.Assign([ast.Name('x', ast.Store())], ast.Num(1)),
                   ast.Assign([ast.Name('y', ast.Store())], ast.Num(2))]
    extend_tree(tree, {'vars': vars_values})
    assert ast.dump(tree) == 'Module([Assign([Name(y, Store())], Num(2)), Assign([Name(x, Store())], Num(1))])'



# Generated at 2022-06-14 02:57:44.304586
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x):
        let(y)
        return x + y

    assert test.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.Num(1)
        ),
        ast.Return(value=ast.BinOp(
            left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
            op=ast.Add(),
            right=ast.Name(id='_py_backwards_y_1', ctx=ast.Load())
        ))
    ]


# Generated at 2022-06-14 02:57:47.135392
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:57:59.693870
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
extend(vars)
print(x, y)
    """)
    extend_tree(tree, {'vars': [
       ast.Assign(
           targets=[ast.Name(id='x', ctx=ast.Store())],
           value=ast.Constant(value=1)
       ),
       ast.Assign(
           targets=[ast.Name(id='x', ctx=ast.Store())],
           value=ast.Constant(value=2)
       ),
    ]})

# Generated at 2022-06-14 02:58:08.421906
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from astunparse import unparse as python_code
    from typing import Dict, List
    from .tree import to_ast

    def add_plus_minus_one(x: int, y: int = None) -> Dict[str, List[int]]:
        let(x + 1)
        assert x == 2
        let(y)
        y_ = list(range(10))
        extend(y_)
        assert len(y_) == 11
        return {'x': [1, 2], 'y': y_}

    snippet_ = snippet(add_plus_minus_one)
    assert snippet_
    body = snippet_.get_body()
    assert body
    assert '_py_backwards_x_0' in python_code(body)
    assert '_py_backwards_y_1' in python

# Generated at 2022-06-14 02:58:12.433681
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(a: int, b: int) -> int:
        let(x)
        return x

    body = test.get_body(a=ast.Num(n=1), b=2)
    assert body == [ast.Return(_py_backwards_x_0)]  # type: ignore



# Generated at 2022-06-14 02:58:16.354655
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 5
    y = 10
    s = snippet(lambda x, y: x + y)
    print(s.get_body(x=x, y=y))
    print(ast.dump(ast.parse(get_source(lambda x, y: x + y))))

# Generated at 2022-06-14 02:58:25.451057
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var = ast.Name(id='var', ctx=ast.Store())
    var1 = ast.Name(id='y', ctx=ast.Store())
    @snippet
    def function():
        let(var)
        var += 1
        y = 1
    result = function.get_body(var=var1)
    assert [ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                       value=ast.Num(1)), ast.AugAssign(target=var1,
                                                        op=ast.Add(),
                                                        value=ast.Num(1))] == result

# Generated at 2022-06-14 02:59:22.256124
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def my_func_to_test(arg1: int, arg2: int) -> int:
        x = 1
        y = 0
        let(x)
        x += 1 + arg1
        y += x * 2

        if x == 3:
            x -= 1
            y -= 1
            return 1
        elif x == 2:
            return 0

    fn_source = get_source(my_func_to_test)
    tree = ast.parse(fn_source)

    tree = ast.parse(fn_source)
    snippet_tree = snippet(my_func_to_test).get_body(x=ast.Name(id='_x', ctx=ast.Store()))
    assert snippet_tree == tree.body[0].body[2:7]

# Generated at 2022-06-14 02:59:31.781478
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_body(x, y):
        let(z)
        x = 1
        y = 2
        z = 3
        return x, y, z

    from . import walker

    res = snippet(snippet_body).get_body(x=5, y='str')
    print([node.__class__.__name__ for node in res])
    walker.pretty_print(res)
    print()

    def test():
        let(x)
        let(y)
        x = 1
        y = 2
        return x, y

    print(get_source(test))
    res = snippet(test).get_body()
    walker.pretty_print(res)



# Generated at 2022-06-14 02:59:34.717191
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x += 1
        y = 1

    snippet_ = snippet(fn)
    code = snippet_.get_body()
    for node in code:
        if isinstance(node, ast.Assign):
            print(node.targets[0].id)

test_snippet_get_body()

# Generated at 2022-06-14 02:59:43.105684
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(arg1, arg2=None):
        let(x)
        let(y)
        let(z)
        x = 3
        x += 4
        y = 4
        y += 5
        z = 5
        z += 6

    snippet_obj = snippet(snippet_fn)
    ast_list = snippet_obj.get_body(x=1, z=2)
    tree = ast.Module(ast_list)
    
    assert get_source(tree) == 'x = 3\nx += 4\n_py_backwards_y_0 = 4\n_py_backwards_y_0 += 5\nz = 5\nz += 6'


# Generated at 2022-06-14 02:59:58.598102
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    source = """
    def test():
    
        extend(vars)
        print(a)
        print(b)
        
        extend(vars2)
        print(c)
        print(d)
        
        print(e)
    """
    tree = ast.parse(source)
    vars = [
        ast.Assign([ast.Name(id='a', ctx=ast.Store())], ast.Num(1)),
    ]
    vars2 = [
        ast.Assign([ast.Name(id='c', ctx=ast.Store())], ast.Num(3)),
    ]
    extend_tree(tree, {
        'vars': vars,
        'vars2': vars2
    })