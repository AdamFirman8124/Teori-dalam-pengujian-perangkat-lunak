

# Generated at 2022-06-14 02:50:46.017985
# Unit test for function find_variables
def test_find_variables():
    # pylint: disable=unused-argument,redefined-outer-name
    @snippet
    def snippet_function(one, two):
        """
        let(x)
        let(y)
        assert x + y == 3
        """

    assert sorted(snippet_function.get_variables()) == ['x', 'y']



# Generated at 2022-06-14 02:50:55.352270
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Test for case
    # let(x)
    # x += 1
    # y = 1
    source = """def test(x):
    let(x)
    x += 1
    y = 1"""
    expected_body = ast.parse("""{
    _py_backwards_x_0 += 1
    y = 1""").body  # type: ignore
    tree = ast.parse(source)
    variables = {}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert tree.body[0].body == expected_body

    # Test for case
    # extend(vars)
    # x = 1
    # x = 2
    # print(x, y)

# Generated at 2022-06-14 02:51:00.104543
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""let(x)
                        x = 1
                        let(foo)
                        def bar():
                            foo = bar
                        """)

    assert list(find_variables(tree)) == ['x', 'foo']



# Generated at 2022-06-14 02:51:05.951379
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import sys

    import_module = ast.parse("import random").body[0]  # type: ignore
    alias = import_module.names[0]  # type: ignore

    assert alias.name == 'random'

    replacer = VariablesReplacer(
        {'random': 'sys'}
    )

    replacer.visit_alias(alias)

    assert alias.name == 'sys'



# Generated at 2022-06-14 02:51:09.656551
# Unit test for function find_variables
def test_find_variables():
    @snippet
    def test():
        let(x)
        x = 1

    assert test.get_body() == [ast.Assign(targets=[ast.Name(id=VariablesGenerator.generate('x'))],
                                         value=ast.Num(n=1))]



# Generated at 2022-06-14 02:51:13.209131
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
    let(x)
    y = 1
    let(z)
    ''')  # type: ignore
    assert sorted(find_variables(tree)) == ['x', 'z']  # type: ignore



# Generated at 2022-06-14 02:51:24.589573
# Unit test for function extend_tree
def test_extend_tree():
    def fn():
        a = 0
        extend(a)
        print(a)

    tree = ast.parse(get_source(fn))


# Generated at 2022-06-14 02:51:36.061382
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        let(y)
        x += 1
        y = 1
        if x == 1:
            extend(a)
        else:
            extend(b)
        let(z)

    sn = snippet(fn)
    body = sn.get_body(x='_py_backwards_x_0', y='_py_backwards_y_1',
                       a=ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],  # type: ignore
                                    value=ast.Constant(1, kind=None)),
                       b=ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],  # type: ignore
                                    value=ast.Constant(2, kind=None)))
   

# Generated at 2022-06-14 02:51:42.907044
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(vars)
    print(x, y)
    """)
    vars_tree = ast.parse("""
    x = 1
    x = 2
    """)
    extend_tree(tree, {'vars': vars_tree.body})
    assert ast.dump(tree) == ast.dump(ast.parse("""
    x = 1
    x = 2
    print(x, y)
    """))


# Generated at 2022-06-14 02:51:55.245124
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    var = "t_1"
    tree = ast.parse("import test.test_helper as t")
    tree2 = ast.parse("import test.test_helper")
    tree3 = ast.parse("import test.test_helper as lol")
    var_dict = { "t": var }
    VariablesReplacer.replace(tree, var_dict)
    VariablesReplacer.replace(tree2, var_dict)
    VariablesReplacer.replace(tree3, var_dict)
    assert ast.dump(tree).replace(' ', '').replace("\n", '') == "Module(body=[ImportFrom(level=0,module=test.test_helper,names=[alias(asname={},name={})])])".format(var, var)

# Generated at 2022-06-14 02:52:07.520966
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(var)")
    extend_tree(tree, {'var': ast.parse("x = 1")})
    extend_tree(tree, {'var': ast.parse("x = 2")})
    assert str(tree) == 'x = 1\nx = 2'


test_extend_tree()

# Generated at 2022-06-14 02:52:10.441071
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
        if True:
            let(a)
            print(a)
    ''')
    vars = [v for v in find_variables(tree)]
    assert vars == ['a']



# Generated at 2022-06-14 02:52:21.029665
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    def test_function(x: int, y: int) -> int:
        let(x)
        x += 1
        y = 1
        return x + y

    snippet_ = snippet(test_function)
    ast_body = snippet_.get_body(x=1, y=2)
    assert ast_body[0].value.id == '_py_backwards_x_0'
    assert ast_body[1].value.id == '_py_backwards_x_0'
    assert ast_body[2].value.id == '_py_backwards_y_1'
    assert ast_body[3].value.left.id == '_py_backwards_y_1'
    assert ast_body[4].value.right.id == '_py_backwards_x_0'


# Generated at 2022-06-14 02:52:30.631580
# Unit test for function find_variables

# Generated at 2022-06-14 02:52:34.614905
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def example1(x: int) -> None:
        let(x)
        x += 1
    expect1 = ast.parse("x += 1").body
    actual1 = snippet(example1).get_body(x=1)
    assert actual1 == expect1



# Generated at 2022-06-14 02:52:45.345715
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    value = 'foo'
    arg = 1

    @snippet
    def test_snippet(x: str, y: int) -> None:
        let(value)
        print(value, y)
        x += ' bar'
        p = value, x

    body = test_snippet.get_body(x=arg, y=2)
    assert isinstance(body, list)
    assert len(body) == 3
    assert isinstance(body[0], ast.Expr)
    assert body[0].lineno == 1
    assert isinstance(body[1], ast.Assign)
    assert body[1].lineno == 2
    assert isinstance(body[1].value, ast.Str)
    assert body[1].value.s == value

# Generated at 2022-06-14 02:52:52.619266
# Unit test for function extend_tree
def test_extend_tree():
    t = ast.parse("""
from test import extend
a = 1
extend(a)
""")
    extend_tree(t, {'a': [
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Constant(value=1, kind=None)),
        ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Constant(value=2, kind=None))
    ]})

# Generated at 2022-06-14 02:52:55.620524
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        let(x)
        x += 1
        let(y)
        z = x + y
    """)
    assert list(find_variables(tree)) == ['x', 'y']



# Generated at 2022-06-14 02:53:03.202695
# Unit test for function extend_tree
def test_extend_tree():
    def fn():
        x = 2
        y = 1

    source = get_source(lambda: extend(fn()))
    tree = ast.parse(source)
    result = extend_tree(tree, {'fn': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                         value=ast.Num(n=1))]})
    assert result is None
    assert tree.body[0].value.lineno == 1
    assert tree.body[0].value.col_offset == 0
    assert tree.body[0].value.value.lineno == 1
    assert tree.body[0].value.value.col_offset == 8

# Generated at 2022-06-14 02:53:13.711078
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = ast.Name(id='a', ctx=ast.Load())
    b = ast.Name(id='b', ctx=ast.Load())
    text = 'c = 1 + 2 + 3'
    body = ast.parse(text).body  # type: ignore

    @snippet
    def test_snippet(x, y):
        let(a)
        let(b)
        extend(body)

    body = test_snippet.get_body(x=a, y=b)
    assert get_source(body) == text


if __name__ == '__main__':
    def test():
        @snippet
        def test_snippet(a, b):
            let(a)
            b += 1


# Generated at 2022-06-14 02:53:25.714333
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def _snippet(a: int, b: Union[int, str]) -> Union[int, str]:
        let(c)
        c += a + b
        return c
    body = _snippet.get_body(a=1, b='abc')

# Generated at 2022-06-14 02:53:31.054100
# Unit test for function find_variables
def test_find_variables():
    def fn():
        let(x)
        x += 1
        y = 1
    source = get_source(fn)
    tree = ast.parse(source)
    assert find_variables(tree) == ['x']

# Generated at 2022-06-14 02:53:39.689730
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def mys():
        let(x)
        x = 1
        y = 2
        t = x + y
        return t


# Generated at 2022-06-14 02:53:49.766287
# Unit test for function find_variables
def test_find_variables():
    # Test simple case
    @snippet
    def f():
        let(x)
        let(y)

    assert set(find_variables(f)) == {'x', 'y'}

    # Test simple case with multiple lets
    @snippet
    def g():
        let(x)
        let(y)
        let(z)

    assert set(find_variables(g)) == {'x', 'y', 'z'}

    # Test let with extend
    @snippet
    def h():
        let(x)
        extend(vars)

    assert set(find_variables(h)) == {'x'}
    assert set(find_variables(h)) == set(find_variables(vars))

    # Test multiple lets with extend

# Generated at 2022-06-14 02:53:57.787033
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("let(x)")
    assert find_variables(tree) == ['x']

    tree = ast.parse("let(x)\nlet(y)")
    assert find_variables(tree) == ['x', 'y']

    tree = ast.parse("let(x)\n1 + x")
    assert find_variables(tree) == ['x']



# Generated at 2022-06-14 02:54:06.668864
# Unit test for function extend_tree
def test_extend_tree():
    test_import_ast = ast.parse(
        'from test_module import function_1, function_2')
    test_import_from_extend_ast = ast.parse(
        'extend(test_from)')  # type: ignore

    test_from_ast = ast.parse('''
from test_from import test_from
from test_module import function_2
from test_module import function_1
''')
    extend_tree(test_from_ast, {'test_from': test_import_from_extend_ast.body[0].value})
    assert test_import_from_extend_ast.body[0].value == test_from_ast.body[0].value

    test_import_from_extend_ast = ast.parse(
        'extend(test_from)') 

# Generated at 2022-06-14 02:54:14.289615
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(**extras) -> None:
        extend(extras)
        x = 1
        x += 1
        x += 1
        y = let(2)
        x += 1
    
    snippet_obj = snippet(snippet_fn)
    snippet_code = snippet_obj.get_body()
    source = get_source(snippet_fn)
    tree = ast.parse(source)
    expected_snippet_code = tree.body[0].body
    
    exp_code_len = len(expected_snippet_code)
    code_len = len(snippet_code)
    assert exp_code_len == code_len
    

# Generated at 2022-06-14 02:54:27.856562
# Unit test for function find_variables
def test_find_variables():
    source = """
      x = let(x)
      y = 1
      let(z)
      x = let(a)
    """
    tree = ast.parse(source)
    variables = {name: VariablesGenerator.generate(name)
                 for name in find_variables(tree)}
    VariablesReplacer.replace(tree, variables)

# Generated at 2022-06-14 02:54:38.361635
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x += 1
    x = 1
    x
    let(y)
    y = 1
    x + y
    """
    tree = ast.parse(source)
    variables = set(find_variables(tree))
    assert variables == set(['x', 'y'])
    code = compile(tree, '', 'exec')
    ns = {}
    exec(code, ns, ns)
    assert ns['_py_backwards_x_0'] == 1
    assert ns['_py_backwards_y_0'] == 1
    assert ns['_py_backwards_res_0'] == ns['_py_backwards_x_0'] + ns['_py_backwards_y_0']



# Generated at 2022-06-14 02:54:44.213298
# Unit test for function find_variables
def test_find_variables():
    snippet = ast.parse('''
    def func():
        let(a)
        let(b)
        let(c)
        return None
    ''')
    assert {name for name, _ in find_variables(snippet)} == {'a', 'b', 'c'}



# Generated at 2022-06-14 02:54:57.163100
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import typed_astunparse # type: ignore

    @snippet
    def fn():
        let(x)
        x += 1
        y = 1
        extend(vars)
        print(x, y, z)

    vars = ast.parse('x = 1; x = 2; z = 1')
    body = fn.get_body(x=1, vars=vars, z=3)
    res = typed_astunparse.unparse(body)
    assert res == ['x = 1; x = 2; z = 1', 'x_0 += 1', 'y = 1', 'print(x_0, y, z)']

# Generated at 2022-06-14 02:55:06.316320
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x):
        let(y)
        extend(vars)
        assert x == y
        return x + y

    assert snippet(fn).get_body() == ast.parse(' assert x == _py_backwards_y_0\n return x + _py_backwards_y_0').body  # type: ignore
    assert snippet(fn).get_body(y=123) == ast.parse(' assert x == 123\n return x + 123').body  # type: ignore
    assert snippet(fn).get_body(y=ast.Name('y')) == ast.parse(' assert x == y\n return x + y').body  # type: ignore
    snip = snippet(fn)
    assert snip.get_body(vars=ast.parse('x = 1; x = 2').body) == ast.parse

# Generated at 2022-06-14 02:55:10.438235
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(y)
        return y

    snippet = snippet(fn)
    snippet.get_body()
    assert snippet.get_body() == [ast.Return(value=ast.Name(id='__py_backwards_y_0',
                                                          ctx=ast.Load()))]



# Generated at 2022-06-14 02:55:17.706836
# Unit test for function extend_tree
def test_extend_tree():
    code = """
        extend(vars)
        print(x, y)
    """
    tree = ast.parse(code)
    vars = [ast.parse("x = 1").body[0], ast.parse("x = 2").body[0]]
    extend_tree(tree, {'vars': vars})
    a1 = ast.parse("x = 1")
    a2 = ast.parse("x = 2")
    assert tree.body == a1.body + a2.body + ast.parse(code).body[1:]
    assert len(tree.body) == 3

# Generated at 2022-06-14 02:55:22.881611
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        body = snippet(f).get_body()
        assert body == [ast.Assign([ast.Name(id='_py_backwards_a_0', ctx=ast.Store())],  # type: ignore
                                   ast.Name(id='a', ctx=ast.Load()))]  # type: ignore
        let(a)
    
    f()

# Generated at 2022-06-14 02:55:35.059620
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x):
        let(y)
        extend(z)
        x += 1
        y += 1
        x += y
        return x

    x = ast.Name('x', ast.Load())
    y = ast.Name('y', ast.Store())
    z = [ast.Assign([x], ast.Num(1)), ast.Assign([y], ast.Num(1))]

    body = snippet(fn).get_body(x=x, y=y, z=z)
    assert len(body) == 5
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[1], ast.AugAssign)
    assert isinstance(body[2], ast.Num)
    assert isinstance(body[3], ast.Assign)

# Generated at 2022-06-14 02:55:44.130832
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def x() -> None:
        let(x)
        x += 1

    source = get_source(x)
    tree = ast.parse(source)
    snippet_ = snippet(x)
    snippet_kwarg = {}
    variables = snippet_._get_variables(tree, snippet_kwarg)

    assert variables == {'x': VariablesGenerator.generate('x')}

    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    source = source.split('\n')
    source.pop(0)
    source = '\n'.join(source)
    tree = ast.parse(source)
    assert snippet_.get_body() == tree.body



# Generated at 2022-06-14 02:55:48.678592
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def __test():
        let(x)
        x.do()
    
    import inspect
    from . import Snippet
    
    snippet = Snippet(__test)
    snippet.get_body()
    import astunparse
    print(astunparse.dump(snippet.get_body()))


__all__ = ['snippet', 'let']

# Generated at 2022-06-14 02:55:57.296810
# Unit test for function find_variables
def test_find_variables():
    # Test for variable not declared and for variable declared
    def example_snippet_1():
        x = 1
        let(x)

    assert list(find_variables(ast.parse(get_source(example_snippet_1)))) == ['x']

    # Test for variable with function name
    def example_snippet_2():
        x = 1
        let(x)

    assert list(find_variables(ast.parse(get_source(example_snippet_2)))) == ['x']

    # Test for variable with underscore name
    def example_snippet_3():
        x = 1
        let(_x)

    assert list(find_variables(ast.parse(get_source(example_snippet_3)))) == ['_x']

    # Test for two vars

# Generated at 2022-06-14 02:56:08.349757
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2

    def fn():
        return let(a) + let(b)


# Generated at 2022-06-14 02:56:20.926556
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int) -> int:
        let(y)
        y += 1
        z = 1
        return x + y + z

    tree = snippet(fn).get_body(y=3)
    assert isinstance(tree, list)
    assert isinstance(tree[0], ast.AugAssign)
    assert isinstance(tree[1], ast.Assign)
    assert isinstance(tree[0].target, ast.Name)
    assert isinstance(tree[1].targets[0], ast.Name)

# Generated at 2022-06-14 02:56:28.371765
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a=3) -> None:
        let(x)
        x += a

        let(y)
        y = a

        extend(vars)
        print(x, y)

    def my_fn(a=3) -> None:
        x = a
        y = a
        print(x, y)

    expected_ast = ast.parse(get_source(my_fn)).body
    assert expected_ast == fn.get_body(vars=ast.parse(get_source(my_fn)).body)

# Generated at 2022-06-14 02:56:32.504116
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def upper():
        x = 1
        y = 2
        let(x)
        x = x + 2
        z = y
        return z

    assert get_body == [{'_py_backwards_x_0': 1}, {'y': 2}, {'_py_backwards_x_0': 3}, {'z': 2}]



# Generated at 2022-06-14 02:56:42.309638
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x, y):
        let(x)
        let(y)
        z = '.'.join(x)
        z += y
        return z
    
    snippet_instance = snippet(f)

    body = snippet_instance.get_body(x=['a', 'b'],
                                     y='c')

# Generated at 2022-06-14 02:56:47.995285
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .assert_ast import assert_ast

    @snippet
    def foo(a, b):
        let(x)
        let(y)
        x = a + b
        y = x - b
        return x

    code = foo.get_body(a=1, b=2)

# Generated at 2022-06-14 02:56:52.920268
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: x + 1).get_body() == ast.parse(
        """\
x = 1
x + 1
""").body[0].body

# Generated at 2022-06-14 02:56:57.933430
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from typing import List
    test_snippet = snippet(lambda x, y, z: let(z) + z)
    result = test_snippet.get_body(
        x = 1,
        y = 2,
        z = 3
    )
    assert(result[0].value.left.id == '_py_backwards_z_0')
    assert(result[0].value.right.n == 3)
    assert(result[1].value.id == '_py_backwards_z_0')

# Generated at 2022-06-14 02:57:03.857951
# Unit test for function find_variables
def test_find_variables():
    code = """
        let(x)
        x += 1
        let(y)
    """
    tree = ast.parse(code)
    names = find_variables(tree)
    assert names == {'x', 'y'}



# Generated at 2022-06-14 02:57:16.042294
# Unit test for function extend_tree
def test_extend_tree():
    from .helpers import make_tree

    vars = [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(n=1)),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=2))]
    tree = make_tree('''
        extend(vars)
    ''')

    extend_tree(tree, {'vars': vars})
    assert len(tree.body[0].body) == 2
    assert len(tree.body[0].body[0].targets) == 1
    assert tree.body[0].body[0].targets[0].id == 'x'

# Generated at 2022-06-14 02:57:19.606076
# Unit test for function find_variables
def test_find_variables():
    find_variables.clear()
    source = '''
if True:
    let(a)
    a += 1
    let(y)
    y = 1
'''
    tree = ast.parse(source)
    assert eager(find_variables(tree)) == ['a', 'y']



# Generated at 2022-06-14 02:57:31.689185
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x += 1
    let(y)
    # y -= 1
    """

    tree = ast.parse(source)
    variables = set(find_variables(tree))
    assert variables == {'x', 'y'}



# Generated at 2022-06-14 02:57:43.715826
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def none():
        let(1)
        print(x)

    assert snippet(none).get_body()[0].value.s == '_py_backwards_x_0'

    def with_args():
        let(1)
        print(x, y)

    assert snippet(with_args).get_body(y=2)[0].value.elts[1].n == 2

    def extend_args():
        extend(vars)
        print(x)

    assert (snippet(extend_args).get_body(vars='x = 1')[0].value.s
            == '_py_backwards_x_0')


# Generated at 2022-06-14 02:57:57.651593
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x, y)
        for i in range(x):
            yield y
        let(z)

    # test
    snippet_obj = snippet(snippet_fn)
    snippet_body = snippet_obj.get_body(x=10, y=20)

# Generated at 2022-06-14 02:58:01.589951
# Unit test for function extend_tree
def test_extend_tree():
    a = ast.parse('x = 1').body[0]
    b = ast.parse('x = 2').body[0]
    tree = ast.parse('extend(vars)')
    extend_tree(tree, {'vars': [a, b]})
    assert str(tree) == '[x = 1, x = 2]'

# Generated at 2022-06-14 02:58:07.643870
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(a: int, b: int) -> int:
        let(a)
        let(b)
        return a + b

    ast_body = foo.get_body()
    assert isinstance(ast_body, list)
    assert isinstance(ast_body[0], ast.Return)
    assert ast_body[0].value.left.id == '_py_backwards_a_0'
    assert ast_body[0].value.comparators[0].id == '_py_backwards_b_1'



# Generated at 2022-06-14 02:58:14.242425
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Unit test for method get_body of class snippet."""
    @snippet
    def fn(x: int) -> int:
        let(x)
        x += 1
        return x

    assert len(fn.get_body()) == 3
    assert isinstance(fn.get_body()[1], ast.Assign)  # type: ignore
    assert isinstance(fn.get_body()[1].value, ast.BinOp)  # type: ignore
    assert isinstance(fn.get_body()[1].value.right, ast.Num)  # type: ignore
    assert fn.get_body()[1].value.right.n == 1  # type: ignore

# Generated at 2022-06-14 02:58:25.899401
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # test 1: simple example
    @snippet
    def test1(x: int, y: int) -> None:
        let(x)
        x += y
        z = 1
        y = 2

    tree = test1.get_body(x=1, y=2)

# Generated at 2022-06-14 02:58:33.694743
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var2 = 3
    @snippet
    def test_fn(var1: int = 1, var2: int = 2):
        let(var1)
        let(var2)
        y = 1
        return y


# Generated at 2022-06-14 02:58:41.587516
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(a)
    let(b)
    
    def foo():
        f = a * b
        print(f)
    
    foo()
    """
    tree = ast.parse(source)
    variables = sorted(find_variables(tree))
    assert variables == ['a', 'b']

# Generated at 2022-06-14 02:58:46.085810
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)')
    var1 = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=1))

# Generated at 2022-06-14 02:59:00.981515
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x=1):
        let(foo)
        foo += 1
        f(foo)

    snippet = globals()['snippet'](f)
    assert snippet.get_body()[0].name == '_py_backwards_foo_0'

# Generated at 2022-06-14 02:59:07.755618
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: x + 1).get_body() == [
        ast.Assign([ast.Name(id="_py_backwards_x_0", ctx=ast.Store())],
                   ast.BinOp(left=ast.Name(id="_py_backwards_x_0", ctx=ast.Load()),
                             op=ast.Add(),
                             right=ast.Num(n=1)))
    ]



# Generated at 2022-06-14 02:59:09.426739
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tests.test_snippet import test_snippet_get_body
    test_snippet_get_body()

# Generated at 2022-06-14 02:59:14.939388
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        let(x)
        x += 1
        y = 1
        extend(vars)
        print(x, y)

    variables = {'x': ast.Name('x', ast.Load()), 'y': ast.Name('y', ast.Load()),
                 'vars': ast.Name('vars', ast.Load())}

    expected_tree = ast.parse('x = 1; x = 2; print(x, y)').body

    snippet = Snippet(f)
    result_tree = snippet.get_body(**variables)

    assert result_tree == expected_tree

# Generated at 2022-06-14 02:59:22.030248
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    global a
    global b
    a = b = None

    @snippet
    def snippet():
        let(a)
        let(b)
        extend(vars)
        a = 1
        a += 1
        return a + b

    vars = [ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                        value=ast.Num(n=2))]

    tree = snippet.get_body(vars=vars)
    exec(compile(ast.Module(body=tree), filename='<unknown>',
                 mode='exec'))
    assert a == 2
    assert b == 2

# Generated at 2022-06-14 02:59:33.084160
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x: int) -> int:
        let(y)
        y = x + 1
        return y
    # fn.get_body(x=2) gives [[Assign(targets=[Name(id='_py_backwards_y_0', ctx=Store())], value=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Num(n=1)))], [Return(value=Name(id='_py_backwards_y_0', ctx=Load()))]]
    # assert fn.get_body(x=2) == [[Assign(targets=[Name(id='_py_backwards_y_0', ctx=Store())], value=BinOp(left=Name(id='x', ctx=Load()), op

# Generated at 2022-06-14 02:59:36.369924
# Unit test for function find_variables
def test_find_variables():
    def func():
        let(x)
        x = 1
        y = 2

    source = get_source(func)
    tree = ast.parse(source)
    result = list(find_variables(tree))

    assert result == ['x']

# Generated at 2022-06-14 02:59:44.955375
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _test_fn(x: int, y: int) -> None:
        let(x)
        x += 1
        y = 1
        let(z)
        z += 1
        extend(x)
        w = 2
        let(v)
        v += 1
        extend(g)

    _tree = ast.parse(get_source(_test_fn))

# Generated at 2022-06-14 02:59:59.336229
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    _x = 1
    _y = 2

    @snippet
    def test():
        extend(locals())
        let(x)
        x += 1
        _y = 1
        let(y)
        return x

    # This is AST of snippet.
    result = test.get_body()

    assert result[0].value.func.value.id == '_py_backwards_x_0'
    assert result[1].value.op == 'Add'
    assert result[1].value.left.id == '_py_backwards_x_0'
    assert result[1].value.right.n == 1
    assert result[2].value.id == '_py_backwards_y_0'

# Generated at 2022-06-14 03:00:09.288920
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test():
        let(B)
        let(A)

    assert test.get_body() == [
        ast.Assign(
            targets=[
                ast.Name(id='B', ctx=ast.Store()),
                ast.Name(id='A', ctx=ast.Store()),
            ],
            value=None),
    ]

    assert test.get_body(B='_py_backwards_B_0') == [
        ast.Assign(
            targets=[
                ast.Name(id='_py_backwards_B_0', ctx=ast.Store()),
                ast.Name(id='A', ctx=ast.Store()),
            ],
            value=None),
    ]



# Generated at 2022-06-14 03:00:34.984656
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def method(x: ast.Name, y: int, z: str) -> None:
        let(x)
        x += y
        print(z)

    body = method.get_body(x=ast.Name(id='_a_name'), y=5, z='some_string')
    assert body[0].value.s == 'some_string'
    assert body[1].value.left.id == '_a_name'

# Generated at 2022-06-14 03:00:48.646908
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(x: int, y: int):
        let(z)
        return x, y, z

    assert snippet(fn).get_body(x=1, y=2) == [
        ast.Assign(
            [ast.Name(id='z', ctx=ast.Store())],
            ast.Name(id='_py_backwards_z_0', ctx=ast.Load())),
        ast.Return(
            value=[ast.Name(id='x', ctx=ast.Load()),
                   ast.Name(id='y', ctx=ast.Load()),
                   ast.Name(id='z', ctx=ast.Load())])
    ]