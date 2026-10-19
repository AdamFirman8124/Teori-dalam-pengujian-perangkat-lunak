

# Generated at 2022-06-14 02:50:29.281655
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:50:43.334244
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .types import Array

    @snippet
    def snippet_fn(a: Array, b: Array) -> Array:
        z = let(a + b)
        print('hola')
        c = let(z + [1, 2, 3])
        return c

    body = snippet_fn.get_body(a=[1, 1], b=[2, 2])

# Generated at 2022-06-14 02:50:51.083015
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse(
        """extend(vars_)""")
    variables = {'vars_': [ast.parse(
        """extend(vars__)"""), ast.parse(
        """x = 100"""), ast.parse(
        """x = 200""")]}
    extend_tree(tree, variables)
    assert ast.dump(tree, include_attributes=True) == ast.dump(
        ast.Module(
            body=[
                ast.Assign(
                    targets=[
                        ast.Name(
                            id='x',
                            ctx=ast.Store())],
                    value=ast.Num(
                        n=100))
            ]), include_attributes=True)

# Generated at 2022-06-14 02:50:53.005231
# Unit test for function extend_tree

# Generated at 2022-06-14 02:51:05.179330
# Unit test for function extend_tree
def test_extend_tree():
    def car():
        let(x)
        extend(vars)

    car_source = get_source(car)
    tree = ast.parse(car_source)

# Generated at 2022-06-14 02:51:13.015665
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    from unittest import mock
    from .helpers import equal_to, indent
    from .instructions import insert

    variables = {'x': 0, 'y': 1}
    variables_gen = VariablesGenerator.get_default()
    co_body = None
    ast = mock.Mock()

    def test_function_body():
        pass


# Generated at 2022-06-14 02:51:24.441432
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from typed_ast import ast3 as ast

    @snippet
    def foo(x: int, y: int):
        let(x)
        extend(lambda: (let(y), y))
        x += 1
        y -= 1

    body = foo.get_body(x=4, y=3)
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[0].target, ast.Name)
    assert body[0].target.id == '_py_backwards_x_0'
    assert isinstance(body[0].op, ast.Add)

    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[1].targets[0], ast.Name)
    assert body[1].targets[0].id == 'y'

# Generated at 2022-06-14 02:51:28.810661
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(x); x = 1')
    assert list(find_variables(tree)) == ['x']
    assert tree == ast.parse('x = 1')



# Generated at 2022-06-14 02:51:31.454553
# Unit test for function find_variables
def test_find_variables():
    assert find_variables(ast.parse("let(x) let(y) let(z)")).tolist() == ['x', 'y', 'z']


# Generated at 2022-06-14 02:51:41.473797
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import sys
    my_alias = ast.alias(name='my_alias', asname=None)
    import_node = ast.ImportFrom(module='test', names=[my_alias],
                                 level=0)
    if sys.version_info[1] >= 8:
        # Python 3.8.{1..3} crashes on visit_alias
        inst = VariablesReplacer(dict())
        inst.visit_ImportFrom(import_node)
    else:
        # type: ignore
        import_node = VariablesReplacer.replace(import_node, dict())
    assert isinstance(import_node, ast.ImportFrom)
    assert import_node.names[0].name == 'my_alias'
    assert import_node.names[0].asname is None

# Generated at 2022-06-14 02:52:00.361661
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import math
    val = 1

    @snippet
    def run(p):
        let(x)
        x += val
        y = x + 3
        y += p
        print(y)
        extend(vars)
        vars.append(x + math.pi)
        x += math.pi
        print(y)

    res = run.get_body(x=2, p=2, vars=[])
    assert len(res) == 6



# Generated at 2022-06-14 02:52:10.792620
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''
    def foo():
        let(x)
        x += 1
        y = 1
    '''
    tree = ast.parse(source)
    find_variables(tree)
    for stmt in find(tree, ast.Call):
        assert isinstance(stmt, ast.Call)
        if isinstance(stmt.func, ast.Name) and stmt.func.id == 'let':
            parent, index = get_non_exp_parent_and_index(tree, stmt)
            parent.body.pop(index)  # type: ignore

    assert tree.body[0].body[0].value.id != tree.body[0].body[1].value.id

# Generated at 2022-06-14 02:52:16.413038
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    tree = ast.parse('''
if True:
    let(x)
    x += 1
    print(x)
''')
    variables = {'x': ast.Name(id='_py_backwards_x_0', ctx=ast.Load())}
    TreeReplacer.replace(tree, variables)

    assert tree.body[0].body[0].value.id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:52:21.457695
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    tree = ast.parse("import a from 'foo'")
    variables = {'a': 'b'}
    VariablesReplacer.replace(tree, variables)
    assert isinstance(tree.body[0].body[0].names[0], ast.alias) and tree.body[0].body[0].names[0].name == 'b'

# Generated at 2022-06-14 02:52:24.322635
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_kwargs = dict()

    snippet_kwargs['x'] = "a"
    snippet_kwargs['y'] = "b"

    value = snippet(lambda: 1).get_body(**snippet_kwargs)
    print(value)

    signature = get_source(lambda: 1)
    print(signature)

    test_value = ast.parse(signature).body[0].body
    print(test_value)

    if value == test_value:
        assert True
    else:
        assert False

test_snippet_get_body()

# Generated at 2022-06-14 02:52:30.241024
# Unit test for function extend_tree
def test_extend_tree():
    """Test function extend_tree."""
    tree = ast.parse("""
x = 0
y = 1
extend(variables)
print(x, y)
""")
    variables = {'variables': [ast.parse("""
x = 1
x = 2
""").body]}
    extend_tree(tree, variables)
    assert ast.dump(tree) == ast.dump(ast.parse("""
x = 0
y = 1
x = 1
x = 2
print(x, y)
"""))


# Generated at 2022-06-14 02:52:37.223126
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import ast
    import astor
    import py_backwards
    from astor import codegen
    from py_backwards.transformers.variables import VariablesReplacer
    replacer = VariablesReplacer({'bytecode': 'bc'})
    node = ast.alias(name='bytecode', asname=None)
    replacer.visit_alias(node)
    assert 'bytecode' not in astor.to_source(node).replace(" ", "").replace("\n", "")

# Generated at 2022-06-14 02:52:44.239713
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    var_a = VariablesGenerator.generate('a')
    var_b = VariablesGenerator.generate('b')
    variables = {
        'a': var_a,
        'b': var_b
    }
    tree = ast.parse("from a import b as c")
    replacer = VariablesReplacer(variables)
    replacer.visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse("from " + var_a + " import " + var_b + " as c"))

# Generated at 2022-06-14 02:52:52.417235
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    alias = ast.alias(
        name='F',
        asname='newname'  # type: ignore
    )
    with_variable = ast.ImportFrom(
        module='names',
        names=[alias],
        level=0
    )
    variables = {
        'F': 'newname'
    }
    tree = VariablesReplacer.replace(with_variable, variables)
    assert len(tree.names) == 1
    assert tree.names[0].name == 'newname'


# Generated at 2022-06-14 02:53:00.268719
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    test_input = [
        ast.Import(
            body=[ast.alias(
                name='sys.path',
                asname='path'
            )]
        )
    ]
    variables = {
        'sys': '_sys'
    }
    expected_output = [
        ast.Import(
            body=[ast.alias(
                name='_sys.path',
                asname='path'
            )]
        )
    ]
    result = VariablesReplacer.replace(test_input, variables)
    # The object comparison is required in order to have proper error messages of unit test
    assert result == expected_output, "test failed"

# Generated at 2022-06-14 02:53:10.907995
# Unit test for function find_variables
def test_find_variables():
    source = get_source(find_variables)
    tree = ast.parse(source)
    VariablesReplacer.replace(tree, {})
    assert source == ast.unparse(tree)



# Generated at 2022-06-14 02:53:21.143443
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_func(x, y):
        let(x)
        extend(y)
        x += 1
        y = 1
        return x + y


# Generated at 2022-06-14 02:53:30.866799
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_fn():
        x = 0
        let(x)
        y = 0
        let(y)
        z = x + y
        return z

    snippet_instance = snippet(test_fn)
    body = snippet_instance.get_body()

    expected_ast_body = ast.parse('_py_backwards_x_0 = 0\n_py_backwards_y_0 = 0\nz = _py_backwards_x_0 + _py_backwards_y_0\nreturn z').body

    assert ast.dump(expected_ast_body, annotate_fields=False) == ast.dump(body, annotate_fields=False)


# Generated at 2022-06-14 02:53:39.455360
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_code = """
let(x)
y = 1
"""
    tree = ast.parse(snippet_code)
    variables = {'x': ast.Name(id='_py_backwards_x_0', ctx=ast.Store())}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert tree.body[0].body == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                   value=ast.Name(id='x', ctx=ast.Load())),
        ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
        value=ast.Num(n=1))
    ]

# Generated at 2022-06-14 02:53:44.598919
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test0():
        let(x)
        x += 1
        y = 1
        z.a.b = 3
    s = snippet(test0)
    tree = s.get_body()
    assert str(tree[0]) == '_py_backwards_x_0 += 1'
    assert str(tree[1]) == 'y = 1'
    assert str(tree[2]) == 'z.a.b = 3'



# Generated at 2022-06-14 02:53:53.497828
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""let(vars)
x = 1
x = 2
print(x, y)""")
    variables = {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Constant(value=1, kind=None)),
                           ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                      value=ast.Constant(value=2, kind=None))]}
    extend_tree(tree, variables)
    assert ast.dump(tree) == ast.dump(ast.parse("""x = 1
x = 2
print(x, y)"""))



# Generated at 2022-06-14 02:54:05.104070
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test(x: int, y: int) -> None:
        let(a)
        let(b)
        let(c)
        a = 1
        b = a + x
        c = 2 * b
        y = c
    snip = snippet(test)
    variables = {'x': ast.Num(n=3)}

# Generated at 2022-06-14 02:54:10.311620
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def var_func():
        let(x)
        x += 1
        y = 3
        extend(vars)
        return x + y + z
    assert snippet(var_func).get_body(x=1, y=2, z=3, vars=ast.parse("x = 1; x = 2").body) == ast.parse("_py_backwards_x_0 += 1; y = 3; x = 1; x = 2; return _py_backwards_x_0 + y + z").body

# Generated at 2022-06-14 02:54:20.575397
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def body():
        let(x)
        x += 1
        y = 1
        extend(vars)
        print(x, y)

    vars = [
        ast.FunctionDef(body=[
            ast.Expr(value=ast.Call(func=ast.Name(id='x', ctx=ast.Load()),
                                    args=[ast.Num(n=1)],
                                    keywords=[], starargs=None, kwargs=None))
        ])]


# Generated at 2022-06-14 02:54:30.047167
# Unit test for function find_variables
def test_find_variables():
    source = '\n'.join([
        "let(x)",
        "x = 'bla'",
        "let(y)",
        "let(z)",
        "z = 1",
        "y = 1"
    ])

    tree = ast.parse(source)
    assert sorted(find_variables(tree)) == ['x', 'y', 'z']

# Generated at 2022-06-14 02:54:56.732413
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x)
        y = x + 1
        z = 2

    # Check that `let` was correctly removed
    assert len(test_snippet.get_body()) == 2

    # Check that `x` was correctly renamed
    assert isinstance(test_snippet.get_body()[0].targets[0], ast.Name)
    assert test_snippet.get_body()[0].targets[0].id.startswith('_py_backwards_x_')

    # Check that `x` was correctly used as value
    assert isinstance(test_snippet.get_body()[0].value, ast.Name)
    assert test_snippet.get_body()[0].value.id == test_snipp

# Generated at 2022-06-14 02:55:03.984062
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    expected_source = """let(x)
    x += 1
    y = 1"""

    expected_ast = ast.parse(expected_source)

    @snippet
    def fn():
        let(x)
        x += 1
        y = 1

    snippet_ast = fn.get_body()
    assert snippet_ast == expected_ast.body[0].body
    assert repr(snippet_ast[0]) == repr(expected_ast.body[0].body[0])
    assert repr(snippet_ast[1]) == repr(expected_ast.body[0].body[1])



# Generated at 2022-06-14 02:55:15.232675
# Unit test for function find_variables
def test_find_variables():
    # Simple case:
    src = """
let(x)
x += 1
x += 1
    """
    tree = ast.parse(src)
    variables = find_variables(tree)
    assert next(variables) == 'x'

    # Nested case:
    src = """
for i in range(10):
    let(x)
    print(x)
    x += 1
    """
    tree = ast.parse(src)
    variables = find_variables(tree)
    assert next(variables) == 'x'

    # Duplicate case:
    src = """
let(x)
x += 1
x += 2
let(x)
x += 5
    """
    tree = ast.parse(src)
    variables = list(find_variables(tree))

# Generated at 2022-06-14 02:55:24.669573
# Unit test for function extend_tree
def test_extend_tree():
    """Test for function extend_tree."""
    tree = ast.parse('''
if True:
    if False:
        print('111')
    extend(vars)
    print('222')
''')
    new_statements = ast.parse('''
x = 1
x = 2
x = 3
''').body
    extend_tree(tree, {'vars': new_statements})

    parent, index = get_non_exp_parent_and_index(tree, tree.body[0])
    assert isinstance(parent, ast.Module)
    assert isinstance(parent, ast.Module)

    while index + 1 < len(parent.body):
        parent.body.pop(index + 1)


# Generated at 2022-06-14 02:55:36.962979
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo() -> None:
        let(x)
        let(y)
        x += 1
    foo()

    assert snippet(foo).get_body() == [
        ast.Assign([ast.Name(_py_backwards_x_0, ast.Store())],
                   ast.BinOp(ast.Name(_py_backwards_x_0, ast.Load()), ast.Add(), ast.Num(1)))
    ]


# Generated at 2022-06-14 02:55:40.919685
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 3
    y = 4

    def f():
        let(x)
        x += 1
        y = 1

    f1 = snippet(f)
    body = f1.get_body()

    assert body[0].value.value.n == 4
    assert body[1].value.value.n == 1

# Generated at 2022-06-14 02:55:47.819953
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)\n')
    vars_ = [
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.Num(n=1)),
        ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())], value=ast.Num(n=2)),
        ast.Assign(targets=[ast.Name(id='c', ctx=ast.Store())], value=ast.Num(n=3)),
    ]
    extend_tree(tree, {'vars': vars_})

# Generated at 2022-06-14 02:55:51.989472
# Unit test for function find_variables
def test_find_variables():
    """Tests if find_variables finds all variables and replace
    let calls with empty calls.
    """
    source = """
    let(x)
    let(y)
    print(x, y)
    """
    tree = ast.parse(source)
    # The next line finds variables, replaces let calls with empty calls
    # and returns list of variables names
    variables = list(find_variables(tree))
    expected = {'x', 'y'}
    assert expected == set(variables)

    expected = """
    print(x, y)
    """
    # The next line checks that let calls are replaced
    # with empty calls
    assert ast.dump(tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:55:59.144630
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snip(x, y):
        let(x)
        x += y
        extend(b)

    # snippet_kwargs = {'x': ast.Name(id='test', ctx=ast.Store()),
    #                   'b': ast.Assign(targets=[ast.Name(id='test', ctx=ast.Store())], value=ast.Num(n='123'))}


# Generated at 2022-06-14 02:56:10.352567
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Test let expression (unique variable)
    @snippet
    def test_snippet():
        let(x)
        x += 1

    assert len(test_snippet.get_body()) == 2
    assert test_snippet.get_body()[0].targets[0].id == '_py_backwards_x_0'
    assert test_snippet.get_body()[1].value.left.id == '_py_backwards_x_0'

    # Test extend and let expression (unique variable)
    @snippet
    def test_snippet():
        let(x)
        extend(vars)
        x += 1

    assert len(test_snippet.get_body()) == 3
    assert test_snippet.get_body()[0].t

# Generated at 2022-06-14 02:56:46.043479
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    global x, y
    x, y = 1, 10
    @eager
    def snippet_test(x) -> ast.AST:
        let(x)
        x += 1
        y = 1
        print(x, y)
        return x


# Generated at 2022-06-14 02:56:53.338089
# Unit test for function extend_tree
def test_extend_tree():
    input_vars = ast.parse("""
    x = 1
    y = 2
    """).body
    snippet_vars = ast.parse("""
    extend(vars)
    print(x, y)
    """).body
    extend_tree(snippet_vars, {"vars": input_vars})

    assert snippet_vars[0].value.id == "vars"
    assert snippet_vars[0].value.args[0].value.elts[0].id == "x"
    assert snippet_vars[0].value.args[0].value.elts[0].value.n == 1

# Generated at 2022-06-14 02:56:56.493961
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Setup
    @snippet
    def my_snippet():
        let(x)
        x += 1
        y = 1

    # Exercise
    body = my_snippet.get_body()

    # Verify
    assert len(body) == 2
    assert body[0].value.left.id == '_py_backwards_x_0'
    assert body[1].targets[0].id == 'y'

# Generated at 2022-06-14 02:57:02.184750
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_cool_code():
        let(x)
        x = x + 1
        y = 1
        z = [1, 2, 3]
        z[0] = x
        extend(vars)
        extend(z)


# Generated at 2022-06-14 02:57:05.780075
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_args = {'x': 'x_1', 'y': [ast.Return()]}
    snippet_var = snippet(test_snippet_get_body)
    body = snippet_var.get_body(**snippet_args)
    assert len(body) == 2
    assert isinstance(body[0].value, ast.Name)
    assert isinstance(body[1], ast.Return)

# Generated at 2022-06-14 02:57:11.052138
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        let(x)
        x += 1
        y = 1
    
    snippet_code = """
x += 1
y = 1"""
    
    snippet_instance = snippet(f)
    snippet_body = snippet_instance.get_body()
    assert ast.dump(snippet_body) == snippet_code



# Generated at 2022-06-14 02:57:16.282131
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_function():
        let(x)
        y = x + 1
        x = y
    snippet_obj = snippet(test_function)
    snippet_obj.get_body(x=3)
    #import sys
    #sys.stderr.write('method get_body for class snippet passed\n')

# Generated at 2022-06-14 02:57:19.922357
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = "a"
    b = "b"
    s = snippet(get_body())
    assert ast.dump(s.get_body()) == ast.dump(ast.parse('_py_backwards_x_1 += 1; y = 1;'))

# Generated at 2022-06-14 02:57:25.436657
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astunparse
    import pytest

    @snippet
    def test(x):
        let(x)
        x += 1
        y = 1

        return y

    body = test.get_body(x=1)
    assert astunparse.unparse(body) == 'y = 1'

    with pytest.raises(AssertionError) as e:
        body = test.get_body(y=1)
    assert str(e.value) == "Let 'x' before usage"



# Generated at 2022-06-14 02:57:29.813775
# Unit test for function find_variables
def test_find_variables():
    source = '''
    let(x)
    var = not x
    '''
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x']


# Generated at 2022-06-14 02:58:30.214491
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _get_body(source, vars=None):
        tree = ast.parse(source)
        tree.body.append(ast.Expr(ast.Num(42)))
        variables = vars or {}
        extend_tree(tree, variables)
        return snippet(lambda: None).get_body(**variables)

    assert _get_body('let(y)') == []
    assert _get_body('let(y)\ny = 17') == [ast.Assign([ast.Name('y', ast.Store())], ast.Num(17))]
    assert _get_body('let(x)\nx = None') == [ast.Assign([ast.Name('x', ast.Store())], ast.Name('None'))]

# Generated at 2022-06-14 02:58:44.323187
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    z = 3
    array = [1, 2, 3]
    @snippet
    def foo(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
        let(a)
        let(b)
        let(c)
        let(d)
        let(e)
        let(f)
        let(g)
        let(h)
        let(i)
        let(j)
        let(k)
        let(l)
        let(m)
        let(n)
        let(o)
        let(p)
        let(q)
        let(r)
        let

# Generated at 2022-06-14 02:58:55.787223
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # code of snippet
    @snippet
    def snippet_name(n: int):
        for _ in range(n):
            let(item)
            item = item + 2
            extend(to_return)

    # get AST for snippet
    body = snippet_name.get_body(
        n=3,
        item=1,
        to_return=[
            ast.Assign(
                targets=[ast.Name(id='result', ctx=ast.Store())],
                value=ast.Name(id='_py_backwards_item_0')
            )
        ]
    )


# Generated at 2022-06-14 02:58:58.859377
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
let(x)
let(y)
x += 1
y += 2
print(x, y)
""")
    variables = find_variables(tree)
    assert variables == ['x', 'y']

    assert ast.dump(tree) == """
<_ast.Module object at 0x1068a3160>
"""



# Generated at 2022-06-14 02:59:09.190010
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)\nprint(x, y)")
    x = ast.Name(id='x', ctx=ast.Store())
    y = ast.Name(id='y', ctx=ast.Store())
    vars = {"vars": [ast.Assign(targets=[x], value=ast.Num(1)),
                     ast.Assign(targets=[y], value=ast.Num(2))]}
    extend_tree(tree, vars)
    assert get_source(tree) == 'x = 1\nx = 2\nprint(x, y)\n'


# Unit tests for function find_variables

# Generated at 2022-06-14 02:59:16.013732
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import pytest
    from .test_helpers import compare_body
    from .type_annotations import make_type_annotations

    @snippet
    def my_snippet(x: int, y: int) -> None:
        let(z)
        let(w)
        w += 1
        z += 2
        y += x
        return w, y, z

    # type annotations

# Generated at 2022-06-14 02:59:23.570666
# Unit test for function find_variables
def test_find_variables():
    assert list(find_variables(("""
        let(x)
        print(x)
    """, {'x': 'a'}))) == ['x']
    assert list(find_variables(("""
        let(x)
    """, {'x': 'a'}))) == ['x']
    assert list(find_variables(("""
        print(x)
    """, {'x': 'a'}))) == []
    assert list(find_variables(("""
        let(x)
        let(y)
        print(x)
    """, {'x': 'a'}))) == ['x', 'y']

# Generated at 2022-06-14 02:59:29.460627
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def my_snippet():
        let(x)

    sn = snippet(my_snippet)
    assert sn.get_body() == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                                        value=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()))]

# Generated at 2022-06-14 02:59:31.780962
# Unit test for function find_variables
def test_find_variables():
    source = let(1), 'x'
    assert source == find_variables(ast.parse('''let(1), 'x' '''))

# Generated at 2022-06-14 02:59:41.891661
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import Compare
    from .helpers import get_source, ast_to_src

    sample = '''
let(x)
    x += 1
y = 1
'''

    var = snippet(lambda: None)
    body = var.get_body()

    assert body[0].value.left.id == '_py_backwards_x_0'
    assert body[1].value.id == '_py_backwards_y_1'

    assert ast_to_src(body, source=sample) == sample

    sample = '''let(x)
let(y)
x += 1
y += 2
z = 3
'''

    var = snippet(lambda: None)
    body = var.get_body()
