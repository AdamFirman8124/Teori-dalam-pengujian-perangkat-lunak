

# Generated at 2022-06-14 02:50:29.077281
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(abc)\nx = 123\nprint(x)")
    ast1 = ast.parse("extend(abc)\nprint(x)")
    ast2 = ast.parse("x = 123")
    extend_tree(tree, {'abc': ast1})
    extend_tree(tree, {'abc': ast2})
    assert tree == ast.parse("x = 123\nprint(x)")


# Generated at 2022-06-14 02:50:30.780889
# Unit test for function extend_tree

# Generated at 2022-06-14 02:50:37.786736
# Unit test for method visit_ImportFrom of class VariablesReplacer
def test_VariablesReplacer_visit_ImportFrom():
    class T(ast.NodeTransformer):
        def __init__(self, variables):
            self.variables = variables
        def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
            node.module = self._replace_module(node.module)
            return self.generic_visit(node)
        def _replace_module(self, module: str) -> str:
            def _replace(name):
                if name in self.variables:
                    return self.variables[name].id
                return name
            return '.'.join(_replace(part) for part in module.split('.'))
    import ast as ast3
    tree = ast3.parse("import tensorflow.keras")
    variables = {'tensorflow' : ast3.Name('tf', ast3.Load())}

# Generated at 2022-06-14 02:50:46.886214
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _fn():
        let(x)
        let(y)
        extend(vars)

    source = get_source(_fn)
    tree = ast.parse(source)
    names = find_variables(tree)
    variables = {name: VariablesGenerator.generate(name) for name in names}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    expected = ['_py_backwards_x_0', 'print(_py_backwards_x_0, _py_backwards_y_1)']
    actual = [
        get_source(stmt)
        for stmt in tree.body[0].body
    ]
    assert expected == actual


if __name__ == '__main__':
    test_snippet_get_body()

# Generated at 2022-06-14 02:50:53.368932
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(vars)
    print(x, y)
    """)
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=2))]
    extend_tree(tree, {'vars': vars})
    expected = ast.parse("""
    x = 1
    x = 2
    print(x, y)
    """)
    assert ast.dump(tree) == ast.dump(expected)



# Generated at 2022-06-14 02:51:00.316407
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    source = """from test import a as b"""
    tree = ast.parse(source)  #type: ignore
    tree = VariablesReplacer.replace(tree, {'test': 'ok'})
    assert ast.dump(tree) == 'Module(body=[ImportFrom(module=\'ok\', names=[alias(name=\'a\', asname=\'b\')], level=0)])'

# Generated at 2022-06-14 02:51:02.896908
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("let(x); foo(x)")
    variables = list(find_variables(tree))
    assert variables == ["x"]

# Generated at 2022-06-14 02:51:12.628298
# Unit test for function extend_tree
def test_extend_tree():
    py_code = """
    def foo(x):
        extend(snippet_vars)

        def bar():
            return x**2
        return bar()
    """
    snippet_vars = [ast.parse("x = x + 1").body[0]]
    tree = ast.parse(py_code)
    extend_tree(tree, {"snippet_vars": snippet_vars})

# Generated at 2022-06-14 02:51:21.729868
# Unit test for function extend_tree
def test_extend_tree():
    tree1 = ast.parse('extend(vars)\n')
    tree2 = ast.parse('a = 1\n')
    extend_tree(tree1, {'vars': tree2.body})
    assert ast.dump(tree1) == '<_ast.Module object at 0x0>'
    assert ast.dump(tree2) == 'Module(body=[Assign(targets=[Name(id="a", ctx=Store())],\n' \
                              '              value=Num(n=1))])'


# Generated at 2022-06-14 02:51:33.811830
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import unittest
    import _py_backwards._helpers as helpers
    from typing import List

    def test_fn(x: int, y: int):
        let(x)
        x += 1
        y = 1


# Generated at 2022-06-14 02:51:55.172094
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""a = 1
let(vars)
extend(vars)""")
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                                          value=ast.Num(n=2))],
                        'a': '_py_backwards_a_0'})
    assert ''.join(ast.dump(tree, False).split()) == 'a=2', \
        'a should be set to 2 and not 1'



# Generated at 2022-06-14 02:52:01.655619
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
        let(x)
        let(a)
        let(b)
        let(c)
        let(d)
        let(e)
    ''')
    assert list(find_variables(tree)) == ['x', 'a', 'b', 'c', 'd', 'e']


# Generated at 2022-06-14 02:52:08.603811
# Unit test for function find_variables
def test_find_variables():
    # Code tree
    code_tree = ast.parse(
        '''\
    def foo():
        let(x)
        x += 1
        y = 1
        extend(vars)
        print(x, y)
    '''
    )

    # Expected result
    result = find_variables(code_tree)
    expected_result = {'x', 'y', 'vars'}

    # Compare results with expected results
    assert result == expected_result

# Generated at 2022-06-14 02:52:20.192116
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    test_snippet = snippet(lambda x, y=1: let(y))
    assert ast.dump(test_snippet.get_body()) == 'FunctionDef(name=\'_py_backwards_fn_1\', ' \
                                                'args=arguments(args=[arg(_py_backwards_x_0, None)], ' \
                                                'vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), ' \
                                                'body=[Assign(targets=[Name(_py_backwards_y_0, Store())], ' \
                                                'value=Num(n=1))], decorator_list=[], returns=None)'

# Generated at 2022-06-14 02:52:28.512571
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import ast
    import textwrap
    snippet_fn = textwrap.dedent('''
        def snippet_code(a, b):
            return a + b
    ''')
    b = ast.parse(snippet_fn)
    snippet_fn = b.body[0]
    print(snippet_fn)

    declared_variables = {
        'a': ast.Name(id='c', ctx=ast.Load()),
        'b': ast.Name(id='d', ctx=ast.Load())
    }

    print(snippet(snippet_fn).get_body(**declared_variables))

# Generated at 2022-06-14 02:52:38.794307
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _test():
        let(x)
        x += 1
        y = 1

    assert snippet(_test).get_body() == [
        ast.Assign(
            targets=[ast.Name(
                id='_py_backwards_x_0',
                ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(
                    id='_py_backwards_x_0',
                    ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1))),
        ast.Assign(
            targets=[ast.Name(
                id='y',
                ctx=ast.Store())],
            value=ast.Num(n=1))
    ]


# Generated at 2022-06-14 02:52:40.615083
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:52:47.630530
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    a = 1
    b = 2
    c = 3

    @snippet
    def test_func() -> None:
        let(a)
        a = 1
        let(b)
        b = 2
        extend(c)

    body = test_func.get_body(a=1, b=2, c=ast.parse('c = 3').body)


# Generated at 2022-06-14 02:52:58.543405
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    i = 1
    def f():
        a = 3
        let(a)
        a += 1
        b = 2
        return a, b
    s = snippet(f)
    assert s.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='a', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='a', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1))),
        ast.Assign(
            targets=[ast.Name(id='b', ctx=ast.Store())],
            value=ast.Num(n=2))]

# Generated at 2022-06-14 02:53:07.700480
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
a = 1
let(x)
extend(x)
b = 1
""")
    variables = {'x': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                  value=ast.Num(n=0))]}
    extend_tree(tree, variables)
    print(ast.dump(tree))

# Generated at 2022-06-14 02:53:21.531349
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # pylint: disable=no-member
    import operator
    import pytest
    from .helpers import compare_source_code

    def _test_fn():
        let(a)
        let(b)
        x = a + b

    snippet_obj = snippet(_test_fn)
    fn_body = snippet_obj.get_body(
        a=ast.parse("1 * 2").body[0].value,
        b=ast.parse("4 * 7").body[0].value
    )
    assert len(fn_body) == 3
    assert len(fn_body[0].body) == 2
    compare_source_code("1 * 2", fn_body[0].body[0].value)
    compare_source_code("4 * 7", fn_body[0].body[1].value)
   

# Generated at 2022-06-14 02:53:26.408190
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import make_assign
    from .tree import find_nodes

    class U:
        pass
    # Assignments
    assignments = [
        make_assign('x', 1),
        make_assign('y', 2)
    ]
    # Expected assignments
    expected_assignments = U()
    expected_assignments.body = [
        make_assign('_py_backwards_var_0', 2),
        make_assign('_py_backwards_var_1', 1)
    ]
    # Code

# Generated at 2022-06-14 02:53:32.725373
# Unit test for function find_variables
def test_find_variables():
    source = """
        def foo():
            let(x)
            let(y)
            return x + y
    """
    tree = ast.parse(source)
    variables = find_variables(tree)
    assert set(variables) == set(['x', 'y'])



# Generated at 2022-06-14 02:53:41.516674
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test for method get_body of snippet class."""

    @snippet
    def my_snippet(x: int) -> None:
        let(x)
        x += 1
        y = 1

    body = my_snippet.get_body(x=5)

    assert len(body) == 2
    assert isinstance(body[0], ast.AugAssign)
    assert get_source(body[0].value) == '5'
    assert isinstance(body[1], ast.Assign)
    assert get_source(body[1].value) == '1'



# Generated at 2022-06-14 02:53:52.326741
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x += 1
        y = 1

    assert snippet(fn).get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1),
            ),
        ),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1),
        ),
    ]



# Generated at 2022-06-14 02:53:56.646178
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    tmp = snippet(lambda x: x + 1)
    body = tmp.get_body()
    assert body[0].value.left.id == '_py_backwards_x_0'



# Generated at 2022-06-14 02:54:00.907366
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test() -> None:
        let(3)

    snippet1 = snippet(test)
    print(snippet1.get_body())



# Generated at 2022-06-14 02:54:07.232707
# Unit test for function extend_tree
def test_extend_tree():
    # Given
    tree = ast.parse("""extend(x)""")
    variables = {'x': [ast.parse("""y = 1""").body[0]]}

    # When
    extend_tree(tree, variables)

    # Then
    assert str(tree) == "y = 1"



# Generated at 2022-06-14 02:54:14.308546
# Unit test for function find_variables
def test_find_variables():
    from .compiler import compile_snippet
    from .helpers import map

    def test(x):
        let(y)
        return y

    assert map(test, range(3)) == [0] * 3

    def test2(x):
        let(y)
        let(z)
        return y + z

    assert map(test2, range(3)) == [0] * 3

    def test3(x):
        let(y)
        extend(y)
        return 0

    assert map(test3, range(3)) == [0] * 3

    def test4(x):
        extend(y)
        let(y)
        return 0

    assert map(test4, range(3)) == [0] * 3

    def test5(x):
        let(y)

# Generated at 2022-06-14 02:54:27.891404
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    # Expected result

# Generated at 2022-06-14 02:54:36.844362
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test snippet._get_body method."""

    @snippet
    def f():
        let(x)
        x += 1

    assert f.get_body() == [
        ast.AugAssign(ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                      ast.Add(), ast.Num(n=1)),
    ]

# Generated at 2022-06-14 02:54:47.812438
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func():
        let(x)
        let(y)
        x += 1
        y = 1
        pass

    snip = snippet(func)
    assert snip.get_body() == [
        ast.Assign([ast.Name(id='_py_backwards_x_0', ctx=ast.Store())], ast.BinOp(ast.Name(id='_py_backwards_x_0', ctx=ast.Load()), ast.Add(), ast.Num(n=1)), lineno=4, col_offset=4),
        ast.Assign([ast.Name(id='_py_backwards_y_1', ctx=ast.Store())], ast.Num(n=1), lineno=5, col_offset=4)]

# Generated at 2022-06-14 02:54:57.591213
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 'x'
    y = 'y'
    @snippet
    def my_snippet(x: int, y: int) -> int:
        let(x)
        let(y)
        x += 1
        y = 1
        return y

# Generated at 2022-06-14 02:55:00.971189
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # pylint: disable=missing-docstring
    @snippet
    def fn(x: int, y: int) -> int:
        let(a)
        let(b)
        return a * b * x * y


# Generated at 2022-06-14 02:55:02.592426
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import os
    os.system('pytest -v -s tests/test_snippet.py')

# Generated at 2022-06-14 02:55:03.578088
# Unit test for function extend_tree

# Generated at 2022-06-14 02:55:15.109702
# Unit test for function extend_tree
def test_extend_tree():
    import ast as src_ast

    def function():
        x = 1
        y = 2
        extend(vars)
        print(x, y)

    source = get_source(function)
    tree = ast.parse(source)
    variables = {'vars': [src_ast.parse('x = 3').body[0]]}  # type: ignore
    extend_tree(tree, variables)

# Generated at 2022-06-14 02:55:24.603799
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # GIVEN
    foo = snippet(lambda x, y: let(x) + let(y))
    # WHEN
    body = foo.get_body(x=3, y=4)
    # THEN

# Generated at 2022-06-14 02:55:36.919848
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def a():
        let(x)
        x += 1
        y = 1

    assert a.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0',
                              ctx=ast.Store())],
            value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0',
                                          ctx=ast.Load()),
                            op=ast.Add(),
                            right=ast.Num(n=1))
        ),
        ast.Assign(
            targets=[ast.Name(id='y',
                              ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]

# Generated at 2022-06-14 02:55:45.571954
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: ast.Name, z: ast.name, a) -> None:
        let(a)
        a += 1
        z += 1
        y = 1


# Generated at 2022-06-14 02:56:06.874128
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    s = snippet(lambda: [let(x) for x in [1, 2]]) 
    body = s.get_body()
    assert len(body) == 2
    for i in range(2):
        assert body[i].__class__ is ast.Assign
        assert body[i].targets[0].__class__ is ast.Name
        assert body[i].targets[0].id == f'_py_backwards_x_{i}'

# Generated at 2022-06-14 02:56:21.853053
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    vars = {'x': 1, 'y': 2}
    actual = snippet(lambda x, y: let(x), lambda w: extend(w)) \
        .get_body(x=vars, y=4, w='c')

# Generated at 2022-06-14 02:56:26.640072
# Unit test for function find_variables
def test_find_variables():
    source = '''
let(x)
let(y)
some_func(x, y)
'''
    tree = ast.parse(source)
    assert len(list(find_variables(tree))) == 2
    assert list(find_variables(tree)) == ['x', 'y']

# Generated at 2022-06-14 02:56:34.700897
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor

    def test():
        let(1)
        let(2)
        extend(4)
        print(a, b)

    result = {'body': [ast.Expr(value=ast.List(elts=[ast.Num(n=1), ast.Num(n=2),
                                                    ast.Num(n=4), ast.Name(id='a'),
                                                    ast.Name(id='b')],
                                              ctx=ast.Load())),
                      ast.Print(dest=None, values=[ast.Name(id='a'),
                                                   ast.Name(id='b')], nl=True)]}

    assert astor.to_source(snippet(test).get_body()) == astor.to_source(result)


# Generated at 2022-06-14 02:56:44.096350
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    var_global = 10
    var_local = 20
    expected = (var_global, var_local)
    @snippet
    def _snippet_func(var_global: int, var_local: int) -> None:
        let(var_global)
        let(var_local)
        var_global = var_global
        var_local = var_local
        # some more code
        
    snippet_body = _snippet_func.get_body(**{'var_global': var_global, 'var_local': var_local})
    assert snippet_body[0].value.lineno == 0
    assert snippet_body[1].value.lineno == 1
    assert snippet_body[0].value.col_offset == 0
    assert snippet_body[1].value.col_offset == 0


# Generated at 2022-06-14 02:56:54.504259
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import walk

    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.nodes = []

        def visit(self, node: ast.AST) -> None:
            self.nodes.append(node)
            super().visit(node)

    @snippet
    def fn() -> None:
        let(x)
        x += 1

    visitor = Visitor()
    walk(fn.get_body(), visitor)

    assert visitor.nodes[0].__class__.__name__ == "Assign"
    assert visitor.nodes[-1].__class__.__name__ == "Name"
    assert visitor.nodes[-1].id == '_py_backwards_x_0'


# Unit tests for method replace of class VariablesRepl

# Generated at 2022-06-14 02:56:59.826494
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x: int, y: int=1) -> int:
        let(z)
        extend(vars)
        return x + y + z

    snippet_ = snippet(func)

# Generated at 2022-06-14 02:57:09.196732
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    body_list = []
    x = 0
    y = 0
    for _ in range(10):
        let(x)
        let(y)
        x += 1
        y += 1
        body_list.append(x)
        body_list.append(y)
    body_list.append(x + y)
    assert len(body_list) == 22

    body_snippet = snippet(test_snippet_get_body).get_body()
    assert len(body_snippet) == 11
    for index, snippet_node in enumerate(body_snippet[:-1]):
        node_list = body_list[2*index: 2*index + 2]
        # node_list = [current x, next x]
        # node_list = [current y, next y]
       

# Generated at 2022-06-14 02:57:14.524261
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    @snippet
    def g(x, y):
        let(c)
        c += a
        c += b
        return x, c
    body = g.get_body(x=ast.Name(id="y", ctx=ast.Load()))
    assert(True)

# Generated at 2022-06-14 02:57:24.790242
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""class X:\n    a = 1\n    let(b) = a\n    extend(expr)\n    c = 1\n""")
    extend_tree(tree,
                {'expr': [ast.Assign(
                    targets=[ast.Name(id='b', ctx=ast.Store())],
                    value=ast.Num(n=10)),
                          ast.Assign(
                              targets=[ast.Name(id='b', ctx=ast.Store())],
                              value=ast.Num(n=0))]}
                )

# Generated at 2022-06-14 02:57:58.527267
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    @snippet
    def snippet_method(a, c=3):
        let(b)
        return a + b * c

    snippet.get_body()
    snippet.get_body(b=5)
    snippet.get_body(c=7)



# Generated at 2022-06-14 02:58:07.395545
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: None).get_body() == []

    def a():
        pass

    def b():
        pass

    assert snippet(lambda: let(a)).get_body() == [ast.Assign([ast.Name('a', ast.Store())], ast.Str('a'))]
    assert snippet(lambda: let(a)).get_body() == [ast.Assign([ast.Name('_py_backwards_a_0', ast.Store())], ast.Str('a'))]
    assert snippet(lambda: let(a)).get_body() == [ast.Assign([ast.Name('_py_backwards_a_1', ast.Store())], ast.Str('a'))]


# Generated at 2022-06-14 02:58:08.177205
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:58:15.277074
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    @snippet
    def f():
        let(x)
        x += 1

# Generated at 2022-06-14 02:58:26.750158
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: int, y: int) -> int:
        let(z)
        z = x + y
        z += 1
        y = 1
        return z

    res = ast.dump(ast.Module(body=test.get_body()))

# Generated at 2022-06-14 02:58:31.106853
# Unit test for function find_variables
def test_find_variables():
    source = '''
    let(x)
    let(y)
    x += 1
    y += 1
    '''
    tree = ast.parse(source)
    variables = list(find_variables(tree))
    assert variables == ['x', 'y']


# Generated at 2022-06-14 02:58:44.386579
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def to_list(l, *args: int):
        let(tmp)
        tmp += l
        return tmp

    assert to_list.get_body(l=[1, 2], tmp=ast.Name(id='l')) == [
        ast.AugAssign(
            target=ast.Name(id='_py_backwards_tmp_0', ctx=ast.Store()),
            op=ast.Add(),
            value=ast.List(
                elts=[ast.Num(n=1), ast.Num(n=2)],
                ctx=ast.Load()),
            ),
        ast.Return(value=ast.Name(id='_py_backwards_tmp_0', ctx=ast.Load()))
    ]

# Generated at 2022-06-14 02:58:49.550097
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test():
        a = 1
        b = 2
        s = let(a + b)
        return s
    snippet = snippet(test)
    result = snippet.get_body()
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], ast.Return)
    assert isinstance(result[0].value, ast.BinOp)
    assert isinstance(result[0].value.op, ast.Add)
    assert isinstance(result[0].value.left, ast.Num)
    assert isinstance(result[0].value.right, ast.Name)


if __name__ == '__main__':
    test_snippet_get_body()

# Generated at 2022-06-14 02:58:52.218586
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(x)\nx\n')
    name = list(find_variables(tree))
    assert name[0] == 'x'



# Generated at 2022-06-14 02:59:02.490595
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_function() -> None:
        let(x)
        let(y)
        x = x + 1
        return x

    expected = [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1),
            ),
        ),
        ast.Return(value=ast.Name(id='_py_backwards_x_0', ctx=ast.Load())),
    ]
    assert snippet_function.get_body() == expected

# Generated at 2022-06-14 02:59:40.743605
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet():
        x = let(1)
        print(x)

    assert snippet.get_body() == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                                            value=ast.Num(n=1)),
                                   ast.Expr(value=ast.Call(
                                       func=ast.Name(id='print', ctx=ast.Load()),
                                       keywords=[], args=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())]))]

# Generated at 2022-06-14 02:59:46.087088
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1

    @snippet
    def my_snippet(x):
        let(x)
        x += 1

    assert my_snippet.get_body(x=x) == [ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                                                   value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                                                   op=ast.Add(),
                                                                   right=ast.Num(n=1)))]

# Generated at 2022-06-14 02:59:56.860924
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
    def f(x):
        def _(): let(y)
            _let_z = y + 1
        _()
    """
    tree = ast.parse(source)
    generator = VariablesGenerator()
    variables = {name: generator.generate(name)
                 for name in find_variables(tree)}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    assert(tree.body[0].body == snippet(f).get_body())


# Generated at 2022-06-14 02:59:57.417728
# Unit test for function extend_tree

# Generated at 2022-06-14 03:00:07.989318
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: None)().get_body() == []
    
    assert snippet(lambda x: None)(x=1).get_body() == []

    assert snippet(lambda x=1: None)().get_body() == []

    assert snippet(lambda x: x + 1)(x=1).get_body() == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())], 
                   value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                   op=ast.Add(),
                                   right=ast.Num(n=1)))]


# Generated at 2022-06-14 03:00:15.072377
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import pytest
    from .helpers import get_source, ast_ex

    with pytest.raises(AssertionError):
        ast_ex.test_get_source()

    x = 'x'

    @snippet
    def fn():
        let(x)
        
    code = fn.get_body(x='1')
    assert get_source(code) == "x = '1'\n"

    @snippet
    def fn():
        let(x)
        x += 1
        
    code = fn.get_body(x='1')
    assert get_source(code) == "x = '1'\nx += 1\n"

    @snippet
    def fn():
        let(x)
        let(y)
        x += 1
        y += 2
