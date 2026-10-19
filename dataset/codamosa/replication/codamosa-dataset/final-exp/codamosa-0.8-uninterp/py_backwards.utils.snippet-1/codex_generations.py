

# Generated at 2022-06-14 02:50:21.179568
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(a)
    print(a)
    let(a)
    print(a)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['a'] * 2
    source = """
    print(1)
    let(a)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['a']
    source = """
    let(a)
    print(a)
    let(a)
    """
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['a'] * 2
    source = """
    let(a)
    let(a)
    """
    tree = ast.parse(source)

# Generated at 2022-06-14 02:50:29.053026
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    from .helpers import ast_to_str
    from .template import Template
    from .helpers import assert_code_equals
    import_node = ast.parse('from .a import b').body[0]  # type: ignore
    var_names_dict = {'b': 'c'}

    assert ast_to_str(import_node) == 'from .a import b'
    replacer = VariablesReplacer(var_names_dict)
    replacer.visit_alias(import_node.names[0])  # type: ignore
    assert ast_to_str(import_node) == 'from .a import c'



# Generated at 2022-06-14 02:50:43.233694
# Unit test for function extend_tree
def test_extend_tree():
    one = ast.Num(1)
    two = ast.Num(2)
    test_tree = ast.parse("x = extend(vars); y = 2; print(x, y);").body
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=one),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=two)]
    extend_tree(test_tree, {'vars': vars})
    # Check that x is overwritten by the last declaration
    assert test_tree[1].target.id == 'x'
    assert test_tree[1].value.n == 2

    # Check that print function works with last assigned value of x
    assert test_tree

# Generated at 2022-06-14 02:50:51.665011
# Unit test for function find_variables
def test_find_variables():
    assert list(find_variables(ast.parse('let(x)'))) == ['x']
    assert list(find_variables(ast.parse('a; let(x); b'))) == ['x']
    assert list(find_variables(ast.parse('if let(x): a; else: b'))) == ['x']
    assert list(find_variables(ast.parse('\n'.join([
        'def f():',
        '    let(x)',
        '    return x',
    ])))) == ['x']
    assert list(find_variables(ast.parse('def f(): let(x); return x'))) == ['x']
    assert list(find_variables(ast.parse('let(x); let(x)'))) == ['x', 'x']

# Generated at 2022-06-14 02:50:55.404666
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    x = 1
    let(y)
    y = x
    """

    root = ast.parse(source)
    assert find_variables(root) == ['x', 'y']

# Generated at 2022-06-14 02:51:03.815022
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    extend(a)
    import sys
    import os
    print(1)
    """
    tree = ast.parse(source)
    extend_tree(tree, {'a': [ast.Import(names=[ast.alias(name='sys', asname=None)]),
                             ast.Import(names=[ast.alias(name='os', asname=None)])]})
    assert get_source(tree) == """
    import sys
    import os
    print(1)
    """

# Generated at 2022-06-14 02:51:09.815963
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    alias = ast.alias(name='collections.abc', asname='abc')
    gen = VariablesGenerator()
    replacer = VariablesReplacer({'collections.abc': gen.generate('someting')})
    new_alias = replacer.visit_alias(alias)
    assert new_alias.name == gen.generate('someting')
    assert new_alias.asname == 'abc'
    assert new_alias.asname != new_alias.name


# Generated at 2022-06-14 02:51:21.902218
# Unit test for function extend_tree
def test_extend_tree():

    tree = ast.parse("""
    a = 1
    b = 1
    c = let(a)
    extend(a)
    print(a)
    """)

    tree.body[0].value = 2
    tree.body.insert(1, ast.parse("a = 2").body[0])

    extend_tree(tree, {
        'a': tree.body
    })


# Generated at 2022-06-14 02:51:22.675232
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    pass

# Generated at 2022-06-14 02:51:27.155737
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""let(x);x + let(y);let(z);""")
    assert set(find_variables(tree)) == {'x', 'y', 'z'}



# Generated at 2022-06-14 02:51:35.300108
# Unit test for method get_body of class snippet
def test_snippet_get_body():
  from .tree import compare_ast
  snippet_ = snippet(lambda x: let(x))

# Generated at 2022-06-14 02:51:39.306445
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("let(x)\nx = 1\ny = 1")
    extend_tree(tree, {
        'x': ast.parse("x = 1\nx = 2").body
    })
    assert(get_source(tree) == "x = 1\nx = 2\ny = 1")

# Generated at 2022-06-14 02:51:47.215785
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(snip: snippet, *, arg1: ast.Name, arg2: ast.Name, arg3: ast.Name):
        let(arg1)
        let(arg2)
        let(arg3)
        arg3.id += '_increased'
        arg2.id += '_increased'
        print(arg1, arg2, arg3)

    snippet_func_body = snippet(test_snippet).get_body(
        arg1=ast.Name(id='x', ctx=ast.Load()),
        arg2=ast.Name(id='y', ctx=ast.Load()),
        arg3=ast.Name(id='z', ctx=ast.Load())
    )

# Generated at 2022-06-14 02:51:54.236077
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('a = 1\nb = 2\nc = 3\nextend(d)\nprint(a, b, c)')
    result = ast.parse('a = 1\na = 2\nb = 2\nc = 3\na = 3\nprint(a, b, c)')
    extend_tree(tree, {'d': result.body[2:]})
    assert ast.dump(tree) == ast.dump(result)



# Generated at 2022-06-14 02:52:01.078274
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def let_var():
        let(x)
        print("result:", x)

    def let_args(x):
        let(x)
        print("result:", x)

    def extend_var():
        extend(vars)
        print("result:", x)

    def let_and_extend_var():
        let(y)
        extend(vars)
        print("result:", x + y)

    def let_and_extend_var_mixed_args():
        z = 1
        let(y)
        extend(vars)
        print("result:", x + y + z)

    def let_and_extend_var_class_method():
        let(y)
        extend(vars)
        print("result:", x.val + y.val)


# Generated at 2022-06-14 02:52:03.496902
# Unit test for function extend_tree

# Generated at 2022-06-14 02:52:13.104861
# Unit test for function extend_tree
def test_extend_tree():
    source = '''
        a = let(a)
        b = let(b)
        c = 3
        extend(d)
        e = 5
        f = 6
    '''
    tree = ast.parse(source)
    extend_tree(tree, {'a': 'A', 'b': 'B', 'd': [ast.Assign(targets=[ast.Name('C')], value=ast.Num(4)), ast.Assign(targets=[ast.Name('D')], value=ast.Num(5))]})

# Generated at 2022-06-14 02:52:16.221585
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_func():
        let(A)
        let(B)
        B = 1
        return A
    s = snippet(snippet_func).get_body()
    assert isinstance(s, list)
    assert len(s) == 2


# Generated at 2022-06-14 02:52:26.311824
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test get_body method of class snippet.
    """

    @snippet
    def test_snippet():
        let(x)
        x += 1
        y = 1

    x = ast.parse('x = 1').body[0]  # type: ignore
    y = ast.parse('y = 2').body[0]  # type: ignore
    z = ast.parse('z = 3').body[0]  # type: ignore
    assert(get_source(test_snippet.get_body(x=x, y=y, z=z)) ==
           'x = 1\nx += 1\n_.__add__ = _._add\n_.__add__ = _add\ny = 1')

# Generated at 2022-06-14 02:52:32.818829
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    @snippet
    def foo(x: int) -> int:
        let(y)
        y += x
        return y

    body = foo.get_body(x=1, y=1)
    assert isinstance(body, list)
    assert len(body) == 2
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[1], ast.Return)
    assert isinstance(body[0].value, ast.Name)
    assert body[0].value.id == "y"
    assert isinstance(body[1].value, ast.Name)
    assert body[1].value.id == "y"
    assert isinstance(body[0].target, ast.Name)
    assert body[0].target.id == "y"

# Generated at 2022-06-14 02:52:46.356498
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def example():
        let(a)
        a = 9
        let(c)
        c = 555
        c = a
        print(c)

    snippet_ = snippet(example)

# Generated at 2022-06-14 02:52:55.106227
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = x + 2

    @snippet
    def func(x: Variable, y: Variable) -> None:
        let(x)
        let(y)

        print(x)
        print(y)

    assert func.get_body(x=x, y=y) == [
        ast.Expr(ast.Call(ast.Name('print', ast.Load()), [ast.Name('x', ast.Load())], [])),
        ast.Expr(ast.Call(ast.Name('print', ast.Load()), [ast.Name('y', ast.Load())], []))]


# Generated at 2022-06-14 02:53:01.871190
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
    let(x)
    x += 1
    y = 1

    def func():
        let(x)
        x += 1
        y += 2
    ''')

    assert list(find_variables(tree)) == ['x', 'x']

    tree = ast.parse('''
    let()
    x += 1
    y = 1

    def func():
        let(x)
        x += 1
        y += 2
    ''')

    assert list(find_variables(tree)) == ['x']

# Generated at 2022-06-14 02:53:13.214803
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test(a, b, c):
        let(a)
        a += 1
        b += 2
        let(c)
        c += 3
        return a + b + c

    s = snippet(test)
    body = s.get_body(a=1, b=[], c=3)

# Generated at 2022-06-14 02:53:23.599577
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)\nz = 3")
    vars = ast.parse("x = 1\ny = 2")
    assert len(tree.body) == 2
    assert len(vars.body) == 2
    extend_tree(tree, {"vars": vars})
    assert len(tree.body) == 3
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[1], ast.Assign)
    assert isinstance(tree.body[2], ast.Assign)
    assert tree.body[0].targets[0].id == "x"
    assert tree.body[1].targets[0].id == "y"
    assert tree.body[2].targets[0].id == "z"

# Generated at 2022-06-14 02:53:33.152189
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x: int) -> int:
        let(y)
        y += 1
        return y, x

    snippet = snippet(f)

    body = snippet.get_body(y=[ast.AnnAssign(
        target=ast.Name(id='y', ctx=ast.Store()),
        annotation=None,
        value=ast.Num(n=4),
        simple=1)])


# Generated at 2022-06-14 02:53:43.086554
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import ast_to_source, assert_equals
    from .tree import find, is_subnode
    from .finders import find_unassigned
    from .transformers import AssignFinder

    def fn():
        let(x)
        x += 1
        y = 1

    s = snippet(fn)
    body = s.get_body()
    assert len(body) == 2
    assert isinstance(body[0], ast.AugAssign)
    assert isinstance(body[1], ast.Assign)
    assert len(body[1].targets) == 1
    assert isinstance(body[1].targets[0], ast.Name)
    assert body[1].targets[0].id == 'y'

    def fn():
        let(x)
        x += 1

# Generated at 2022-06-14 02:53:52.810736
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = [1, 2]
    c = ast.Name('c')

    @snippet
    def fn(a: int = a, b: List[int] = b, c: ast.Name = c):
        let(a)
        let(b)
        let(c)
        extend(c)
        pass

    a = 2
    b = [3, 4]
    vars = [ast.Assign(targets=[ast.Name('b')], value=ast.List(elts=[ast.Num(4), ast.Num(5)], ctx=ast.Load()))]
    fn_body = fn.get_body(a=a, b=b, c=vars)
    assert fn_body == [ast.Pass()]

# Generated at 2022-06-14 02:54:08.337326
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    c = 3
    d = 4

    @snippet
    def test(x: int = 3, y: int = 4) -> int:
        let(a)
        let(b)
        let(c)
        let(d)
        x += a
        b += y
        c += x
        d += b
        import os
        import math
        import sys as yy
        yy.version
        os.name
        math.pi
        import subprocess as s  # type: ignore
        s.call
        print(math.pi)
        print(os.path)
        from os import path as p
        p.join
        p.exists
        from player import Player
        from utils.dirs import get_dir


# Generated at 2022-06-14 02:54:12.615092
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''let(a)
a += 1
''')

    assert list(find_variables(tree)) == ['a']



# Generated at 2022-06-14 02:54:28.394097
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test get_body method of snippet class.

    Notes
    -----
    It is better to test this method in a separate file,
    but it is not necessary yet.
    """
    def my_function(x: int, y: int) -> int:
        let(z)
        z += 1
        return z

    snippet_fn = snippet(my_function)

# Generated at 2022-06-14 02:54:36.837199
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 3
    @snippet
    def test_fn():
        let(x)
        x += 1
        y = 1
    tree = test_fn.get_body()
    assert ast.dump(tree) == '[Assign(targets=[Name(_py_backwards_x_0, Store())], value=BinOp(left=Name(_py_backwards_x_0, Load()), op=Add(), right=Num(1))), Assign(targets=[Name(y, Store())], value=Num(1))]'

# Generated at 2022-06-14 02:54:47.774921
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def f(x):
        let(y)
        let(z)
        y = x
        extend(z)
        return y, z

    assert f.get_body(
        x=ast.Name(id='unkown_vars_0'),
        y=ast.BinOp(ast.Name(id='unkown_vars_0'), ast.Add(), ast.Num(1)),
        z=[ast.Assign([ast.Name(id='y')], ast.Num(1))],
    ) == [
        ast.Assign([ast.Name(id='y')], ast.Name(id='unkown_vars_0')),
        ast.Assign([ast.Name(id='y')], ast.Num(1))
    ]

# Generated at 2022-06-14 02:54:52.792574
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_with_let():
        let(x)
        x += 1
        y = 1

    assert snippet(snippet_with_let).get_body()[1].value.right.n == 1
    assert snippet(snippet_with_let).get_body()[2].value.n == 1



# Generated at 2022-06-14 02:55:02.973781
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import pytest

    def test_snippet() -> None:
        x = 1
        let(x)
        x += 1
        y = 1
        extend(vars)

    def test_snippet_1() -> None:
        x = 1
        extend(vars)
        x += 1
        y = 1
        let(y)

    def test_snippet_2() -> None:
        x = 1
        let(x)
        extend(vars)
        x += 1
        y = 1
        let(y)

    def test_snippet_3() -> None:
        x = 1
        let(x)
        extend(vars)
        x += 1
        y = 1

    def test_snippet_4() -> None:
        x = 1

# Generated at 2022-06-14 02:55:03.911292
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:55:13.766895
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from random import randint
    from .base import to_text
    from .helpers import VariablesGenerator
    vars = {'a': randint(0, 10), 'b': randint(0, 10), 'c': randint(0, 10)}
    s = snippet(lambda x, y, z: x + y + z)
    body = s.get_body(**vars)
    print(to_text(body))
    assert(VariablesGenerator.generate('x') in to_text(body))
    assert(VariablesGenerator.generate('y') in to_text(body))
    assert(VariablesGenerator.generate('z') in to_text(body))

# Generated at 2022-06-14 02:55:23.869278
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a: int) -> int:
        let(b)
        let(c)
        return a + b + c

# Generated at 2022-06-14 02:55:27.396712
# Unit test for function find_variables
def test_find_variables():
    assert list(find_variables(ast.parse("""
      let(x)
      let(y)
      let(z)
    """))) == ['x', 'y', 'z']



# Generated at 2022-06-14 02:55:42.573408
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # pylint: disable=pointless-statement, used-before-assignment
    @snippet
    def s(x, y, z):
        let(w)
        let(v)

        x = 12
        y = 13
        z = 14

        extend(w)
        extend(v)

    tree = s.get_body(x=1, y=2, z=3, w=[x + y, x + z], v=[x - y, x - z])

    assert isinstance(tree, list)
    assert tree[0].value.left.id == '_py_backwards_x_0'
    assert tree[0].value.right.n == 12
    assert tree[1].value.left.id == '_py_backwards_y_0'
    assert tree[1].value.right

# Generated at 2022-06-14 02:55:52.416370
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Unit test for method get_body of class snippet."""
    @snippet
    def get_code() -> ast.AST:
        let(x)
        y = x
        x += 1
        return ast.parse('x + y + 1').body[0].value

    result = get_code.get_body(x=1)
    assert result[0].targets[0].id == '_py_backwards_x_0'
    assert result[1].targets[0].id == 'y'
    assert result[1].value.id == '_py_backwards_x_0'
    assert result[2].value.left.id == '_py_backwards_x_0'
    assert result[2].value.op.__class__.__name__ == 'Add'

# Generated at 2022-06-14 02:55:59.408625
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test that get_body method of class snippet works correctly."""

    def foo() -> ast.AST:
        let(x)
        y = 1
        z = 2, 3
        extend(lst)
        return x + y


# Generated at 2022-06-14 02:56:10.534613
# Unit test for function extend_tree
def test_extend_tree():
    def foo():
        let(x)
        let(y)
        extend(xs)
        print(x, y)
    x = ast.parse("x = 1; x = 2; x = 3;").body
    tree = snippet(foo).get_body(xs=x)
    assert len(tree) == 4
    assert isinstance(tree[0], ast.Expr)
    assert isinstance(tree[0].value, ast.Str)
    assert tree[0].value.s == '1'
    assert isinstance(tree[1], ast.Expr)
    assert isinstance(tree[1].value, ast.Str)
    assert tree[1].value.s == '2'
    assert isinstance(tree[2], ast.Expr)
    assert isinstance(tree[2].value, ast.Str)


# Generated at 2022-06-14 02:56:19.456881
# Unit test for method get_body of class snippet
def test_snippet_get_body():  # noqa: D103
    @snippet
    def some_snippet(x: int, y: int) -> int:
        let(z)
        z = x + y
        return z

    assert some_snippet.get_body(x=1, y=2) == [
        ast.Assign(
            targets=[
                ast.Name(id='z', ctx=ast.Store())
            ],
            value=ast.BinOp(
                left=ast.Num(n=1),
                op=ast.Add(),
                right=ast.Num(n=2)
            )
        ),
        ast.Return(value=ast.Name(id='z', ctx=ast.Load()))
    ]

# Generated at 2022-06-14 02:56:29.773600
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a: int, b: int) -> None:
        let(c)
        let(d)
        c = a + b
        d = a * b

# Generated at 2022-06-14 02:56:36.234394
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: print(x)).get_body() == [ast.Print(values=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())], nl=True, dest=None)]
    assert snippet(lambda x: print(x)).get_body(x=1) == [ast.Print(values=[ast.Name(id='x', ctx=ast.Load())], nl=True, dest=None)]

# Generated at 2022-06-14 02:56:43.041983
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def example():
        let(x)
        x += 1

    result = example.get_body()
    expected_source = '_py_backwards_x_0 += 1'
    expected = ast.parse(expected_source).body[0]
    assert result[0] == expected


# Generated at 2022-06-14 02:56:47.410935
# Unit test for function extend_tree
def test_extend_tree():
    code = """
        def test_func():
            x = 1
            extend(vars)
            print(x)

        test_func()
    """

    tree = ast.parse(code)
    extend_tree(tree, {'vars': [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(1),
    )],
    })
    assert get_source(tree) == """
        def test_func():
            x = 1
            x = 1
            print(x)

        test_func()
    """

# Generated at 2022-06-14 02:56:57.921791
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: int, y: int) -> None:
        let(vars)
        let(n)
        let(b)
        b = x + y
        n = 1
        print(b, n)

    vars = [
        ast.parse('''x = 4''').body[0],
        ast.parse('''y = 1''').body[0],
    ]
    body = test.get_body(vars=vars)


# Generated at 2022-06-14 02:57:03.333963
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('let(x); x + 1')
    assert next(find_variables(tree)) == 'x'
    assert len(list(find_variables(tree))) == 0



# Generated at 2022-06-14 02:57:24.207878
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    from .rewriter import global_rewriter as rewriter

    @snippet
    def my_snippet(x, y):
        let(y)
        let(x)
        x += 1
        y += x

    @rewriter
    def foo(x):
        my_snippet(1, 2)

    @rewriter
    def bar(x):
        my_snippet(4, 7)

    foo(1)
    bar(1)
    foo(1)

    get_source(foo)
    get_source(bar)

    assert foo.func_body[0].body == my_snippet.get_body(x=1, y=2)
    assert bar.func_body[0].body == my_snippet.get_body(x=4, y=7)


# Generated at 2022-06-14 02:57:38.163312
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x)
        let(y)
        x += 1
        y = 1

    assert test_snippet.get_body({'x': 2, 'y': 123}) == [
        ast.Assign([ast.Name('_py_backwards_x_0', ast.Store())],
                   ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()),
                             ast.Add(),
                             ast.Num(1))),
        ast.Assign([ast.Name('_py_backwards_y_0', ast.Store())],
                   ast.Num(1))]
    x = 1

# Generated at 2022-06-14 02:57:49.498878
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 0
    y = 0
    @snippet
    def fn(u: int):
        let(u)
        let(x)
        let(y)
        x = x + u
        return y
    
    u = 1
    y = 2
    

# Generated at 2022-06-14 02:57:59.633789
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippets = {"snippet": snippet}
    with open("demo/examples/example2.py") as file:
        exec(file.read(), snippets)
    snippet = snippets["snippet"]

    code = snippet.get_body(a=1)

# Generated at 2022-06-14 02:58:04.579088
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_func(x: int, y: int):
        let(x)
        x += 1
        print(x, y)
    snippet = snippet(test_func)
    body = snippet.get_body(x=1, y=1)
    assert get_source(body) == """x = 1
x = 2
print(x, y)
"""

# Generated at 2022-06-14 02:58:13.401184
# Unit test for function find_variables
def test_find_variables():
    body = ast.parse("let(x)").body

    assert [i for i in find_variables(body)] == ['x']

    body = ast.parse("let(x); let(y)").body
    assert [i for i in find_variables(body)] == ['x', 'y']

    body = ast.parse("def hello():\n    let(x)").body
    assert [i for i in find_variables(body)] == ['x']

    body = ast.parse("def hello():\n    let(x); let(y)").body
    assert [i for i in find_variables(body)] == ['x', 'y']



# Generated at 2022-06-14 02:58:21.075368
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    source = """\
    extend(vars)
    print(x)"""
    tree = ast.parse(source)
    vars_ = [
        ast.parse("x = 1").body[0],
        ast.parse("x = 2").body[0],
    ]
    extend_tree(tree, {"vars": vars_})
    assert astor.to_source(tree) == "x = 1\nx = 2\nprint(x)\n"

# Generated at 2022-06-14 02:58:27.617965
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x):
        let(x)
        x += 1
        y = 1
        return x + y
    expected = ast.parse("""x += 1
y = 1
return x + y""").body
    assert list(fn.get_body(x=ast.Str('1'))) == expected

# Generated at 2022-06-14 02:58:31.460565
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
    def foo():
        let(x)
        x = 1
        let(y)
        y = 2
        return x + y
    """
    tree = ast.parse(source)
    func = tree.body[0]
    assert snippet(foo).get_body() == func.body

# Generated at 2022-06-14 02:58:44.753413
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: str) -> None:
        let(y)
        let(z)
        print(x)
        print(y)
        print(z)

    result = test.get_body(x='hello', y=None)
    assert isinstance(result, list)
    assert len(result) == 4

    expected = ['hello', '_py_backwards_y_0', '_py_backwards_z_0']
    for i, node in enumerate(result):
        assert isinstance(node, ast.Expr)
        assert isinstance(node.value, ast.Call)
        assert isinstance(node.value.func, ast.Name)
        assert node.value.func.id == 'print'

# Generated at 2022-06-14 02:59:35.745766
# Unit test for method get_body of class snippet
def test_snippet_get_body():

    def fn():
        let(x)
        let(y)
        x += 1
        y = 1
        extend(vars)
        print(x, y)
        extend(vars1)
        print(x, y)
        let(x)
        x = 1
        z = x + 1
        print(z)

    class Class:
        let(x)
        x = 1
        let(y)
        y = 2
        extend(vars)
        print(x, y)
        extend(vars1)

    var = ast.parse('x = 1').body[0]
    var1 = ast.parse('x = 2').body[0]
    var2 = ast.parse('x = 3').body[0]
    var3 = ast.parse('y = 2').body[0]


# Generated at 2022-06-14 02:59:44.548703
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 'x'
    y = 1

    @snippet
    def fn():
        let(x)
        x += y
        x += y
        x += y
        x += y

    body = fn.get_body(x=x, y=y)

    x_node = ast.parse('_py_backwards_x_0').body[0].value
    y_node = ast.parse('1').body[0].value

# Generated at 2022-06-14 03:00:00.517563
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import pytest
    from .helpers import compare_asts
    var = VariablesGenerator.generate('foo')

    @snippet
    def example():
        let(foo)

        foo = 1
        foo += 5
        extend(foo)

        let(bar)
        bar = foo
    
    asts = example.get_body(foo=var)
    assert len(asts) == 4

# Generated at 2022-06-14 03:00:10.255962
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet(x, y):
        let(x)
        x += 1
        y = 1

    assert test_snippet.get_body(x=1) == [ast.Assign([ast.Name('_py_backwards_x_0', ast.Store())], ast.Num(1)),
                                          ast.Assign([ast.Name('y', ast.Store())], ast.Num(1))]
    assert test_snippet.get_body(y=1, x=0) == [ast.Assign([ast.Name('_py_backwards_x_1', ast.Store())], ast.Num(0)),
                                               ast.Assign([ast.Name('y', ast.Store())], ast.Num(1))]
