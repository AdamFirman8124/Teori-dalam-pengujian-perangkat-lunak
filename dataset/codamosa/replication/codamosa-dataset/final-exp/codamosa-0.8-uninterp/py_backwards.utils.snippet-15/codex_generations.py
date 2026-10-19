

# Generated at 2022-06-14 02:50:52.061176
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    tree = ast.parse('from a.b.c import x')
    variables = {'a.b.c': 'd.e'}
    VariablesReplacer.replace(tree, variables)
    assert ast.dump(tree) == "ImportFrom(module='d.e', names=[alias(name='x', asname=None)], level=0)"



# Generated at 2022-06-14 02:50:57.209669
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import numpy as np
    x = np.array(1)
    def test() -> snippet:
        let(x)
        x += 1

    body = test().get_body(x=2)

    expect = ast.parse("x += 1").body
    assert body == expect  # type: ignore



# Generated at 2022-06-14 02:51:08.280293
# Unit test for function extend_tree
def test_extend_tree():
    def extend_example():
        @extend
        def code():  # pylint: disable=no-name-in-module
            let(x)
            let(y)
            yield [
                ast.Assign(
                    targets=[ast.Name(id=x, ctx=ast.Store())],
                    value=ast.Num(n=1)),  # type: ignore
                ast.Assign(
                    targets=[ast.Name(id=y, ctx=ast.Store())],
                    value=ast.Num(n=2))
            ]  # type: ignore

        extend(code())
        z = x + y

    source = get_source(extend_example)
    tree = ast.parse(source)
    extend_tree(tree, {'x': 0, 'y': 0})
    assert VariablesRepl

# Generated at 2022-06-14 02:51:12.413882
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse('''
        foo = 0
        let(foo)
        x = foo + 1
        let(x)
        bar = foo + 2
    ''')
    names = find_variables(tree)
    assert names == ['foo', 'x']



# Generated at 2022-06-14 02:51:24.023584
# Unit test for function find_variables
def test_find_variables():
    import inspect
    import ast


# Generated at 2022-06-14 02:51:35.249208
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import ast
    import sys
    import typing
    import unittest

    class Test (unittest.TestCase):
        def test(self):
            self.alias_node = ast.parse("from .foo.bar import baz as spam").body[0]
            class VariablesReplacer_visit_alias(ast.NodeTransformer):
                def visit_alias(self, node):
                    return node
            self.assertEqual(ast.dump(VariablesReplacer.replace(self.alias_node,
                {"baz": "kot", "spam": "pies"})), """\
ImportFrom(
    module='...foo.bar',
    names=[alias(name='kot', asname='pies')],
    level=0)""")

    unittest.main()

# Generated at 2022-06-14 02:51:38.938843
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse(
        """let(x)
x = 5
y = let(y)
y += x
"""
    )
    variables = set(find_variables(tree))
    assert variables == set(['x', 'y'])


# Generated at 2022-06-14 02:51:40.261095
# Unit test for function extend_tree

# Generated at 2022-06-14 02:51:45.668856
# Unit test for function find_variables
def test_find_variables():
    source = """
    a = 0
    let(b)
    let(c)
    let(d)
    """
    tree = ast.parse(source)
    names = find_variables(tree)
    assert names == ['b', 'c', 'd']

# Generated at 2022-06-14 02:51:48.699281
# Unit test for function extend_tree
def test_extend_tree():
    x = ast.Name('x', ast.Store())
    y = ast.Name('y', ast.Store())

# Generated at 2022-06-14 02:52:04.760969
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet1(x, y):
        let(x)
        extend(y)
    assert snippet1.get_body(x=3, y=ast.parse('x = 1')) == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.Num(n=3)
        ),
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]

# Generated at 2022-06-14 02:52:10.755430
# Unit test for function extend_tree
def test_extend_tree():
    # definition
    x = 1
    extend_vars = [ast.Assign(targets=[ast.Name(id="x", ctx=ast.Store())],
                   value=ast.Num(1)),
                   ast.Assign(targets=[ast.Name(id="x", ctx=ast.Store())],
                   value=ast.Num(2))]
    # test
    extend(extend_vars)
    assert x == 2

# Generated at 2022-06-14 02:52:18.688925
# Unit test for function extend_tree
def test_extend_tree():
    x = ast.parse('x = 1').body[0]
    y = ast.parse('y = 2').body[0]
    assign = ast.Assign(targets=[ast.Name(id='z', ctx=ast.Store())],
                        value=ast.Num(n=3))

    tree = ast.parse('''
let(vars)
extend(vars)
''')

    extend_tree(tree, {'vars': [x, y, assign]})
    assert ast.dump(tree) == 'Module(body=[])'  # extend modifies tree directly

# Generated at 2022-06-14 02:52:27.164319
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet():
        let(x)
        x += 1
        y = 1

    body = snippet.get_body()
    assert body[0].value.id == '_py_backwards_x_0'
    assert body[1].value.n == 1
    # Test variable from module ast (Name)
    assert '_py_backwards_ast_Name_0' in (n.id for n in body)
    # Test variable from module ast.parse (Call)
    assert '_py_backwards_ast_parse_0' in (n.id for n in body)



# Generated at 2022-06-14 02:52:36.549212
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(x)\nprint(1)")
    extend_tree(tree, {'x': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                       value=ast.Num(n=3))]})  # type: ignore
    assert ast.dump(tree) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Num(n=3)), Print(dest=None, values=[Num(n=1)], nl=True)])'  # type: ignore

# Generated at 2022-06-14 02:52:43.672102
# Unit test for function extend_tree
def test_extend_tree():
    source1 = """
a = 5
extend(vars)
b = 3
        """

    source2 = """
x = 6
y = 7
        """

    tree = ast.parse(source1)

    vars = ast.parse(source2).body
    extend_tree(tree, {'vars': vars})

    assert(get_source(tree) == 'a = 5\nx = 6\ny = 7\nb = 3')


# Generated at 2022-06-14 02:52:51.446610
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_body(a: int, b: int, c: int) -> int:
        let(x)
        let(y)
        let(z)
        x = a
        y = b
        z = c
        return x + y + z

    snippet_fn = snippet(snippet_body)
    body = snippet_fn.get_body(a=1, b=2, c=3)

# Generated at 2022-06-14 02:52:59.949617
# Unit test for function extend_tree
def test_extend_tree():
    source = """
        let(body)
        extend(body)
    """
    tree = ast.parse(source)
    body = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=ast.Num(n=1),
                        type_comment=None),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                        value=ast.Num(n=2),
                        type_comment=None)]
    extend_tree(tree, {'body': body})
    assert get_source(tree) == """
        pass
    """



# Generated at 2022-06-14 02:53:00.622575
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:06.295044
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
extend(snippet.get_body(a=10))
a = 1 + 2
extend(snippet.get_body(a=11))
b = 3
    """)
    extend_tree(tree, {'snippet': snippet(test_extend_tree)})
    tree_after = ast.parse("a = 10\na = 11\na = 1 + 2\nb = 3")
    assert ast.dump(tree_after) == ast.dump(tree)

# Generated at 2022-06-14 02:53:14.235482
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def my_snippet():
        let(x)
        x += 2

    snippet_ = snippet(my_snippet)
    body = snippet_.get_body()
    assert len(body) == 2
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.AugAssign)
    assert body[0].targets[0].id == '_py_backwards_x_0'
    assert body[0].value.n == 1
    assert body[1].value.n == 2

# Generated at 2022-06-14 02:53:22.485259
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Dummy:
        def method(self) -> None:
            let(self)
            self.a = 1
            self.b = 2
            self.c = 3
    
    snippet_body = snippet(Dummy.method).get_body(self=Dummy())
    extract_let(snippet_body)
    assert snippet_body[0].value.elts[0].s == 'a'
    assert snippet_body[1].value.elts[0].s == 'b'
    assert snippet_body[2].value.elts[0].s == 'c'
    assert len(snippet_body) == 3

# Generated at 2022-06-14 02:53:31.898610
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_code():
        let(x)
        x = x + 1
        y = 1
        return y

    assert snippet_code.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0')],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0'),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ),
        ast.Assign(
            targets=[ast.Name(id='y')],
            value=ast.Num(n=1)
        )
    ]


# Generated at 2022-06-14 02:53:42.984524
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def hello():
        print("Hello!")
    # print(hello.get_body())
    # for n in hello.get_body():
    #     print(n.__class__.__name__)
    # print(hello.get_body()[0].body[0].__class__.__name__)
    # print(hello.get_body()[0].body[0].value)
    # assert hello.get_body()[0].body[0].value.s == 'Hello!'
    assert len(hello.get_body()) == 1
    assert hello.get_body()[0].__class__.__name__ == 'Expr'
    assert hello.get_body()[0].value.__class__.__name__ == 'Str'

# Generated at 2022-06-14 02:53:52.947236
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import inspect
    import dis
    import types
    import ast
    # create snippet object
    def some_function(a, b):
        let(body)
    _f = snippet(some_function)
    # ast tree of some_function
    tree: ast.Module = ast.parse(inspect.getsource(some_function))
    assert tree == ast.parse('''def some_function(a, b):
    let(body)''')
    # bytecode of some_function
    bytecode = dis.Bytecode(inspect.getclosurevars(some_function).code)
    # body of some_function
    assert _f.get_body() == [ast.parse(str(bytecode[0])).body[0]]
    # body of some_function with one arg

# Generated at 2022-06-14 02:53:53.576256
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:57.459055
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x: int) -> int:
        return x + 1

    snippet_body = snippet(f).get_body()

# Generated at 2022-06-14 02:54:05.339193
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def example(x: int) -> int:
        let(y)
        let(z)
        y = 1
        z = 2
        x += y
        return x + z

    s = snippet(example)

    assert s.get_body(y=1) == \
        ast.parse('y = 1\nz = 2\nx += y\nreturn x + z')\
        .body[0].body

    assert s.get_body(y=1, z=2) == \
        ast.parse('y = 1\nz = 2\nx += y\nreturn x + z')\
        .body[0].body

# Generated at 2022-06-14 02:54:11.762441
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    e = 3
    x_value = 20 # Changing this will change x_value in the snippet

    @snippet
    def my_snippet(z: int) -> None:
        let(x)
        let(y)
        let(e)

        z += 1
        x = x_value
        y += z
        e += y
        print(x, y, z, e)

    # Expecting the snippet to end up like this if we pass z = 1:
    # _py_backwards_x_0 = x_value
    # _py_backwards_y_1 += _py_backwards_z_2
    # _py_backwards_e_3 += _py_backwards_y_1
    # print(_py_backwards_x_0,

# Generated at 2022-06-14 02:54:20.063237
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_foo():
        var = 1
        let(var)
        var += 1
        y = 1
        assert var == 2
        assert y == 1

    body = snippet(snippet_foo).get_body()
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[2], ast.Assert)

# Generated at 2022-06-14 02:54:30.110552
# Unit test for function find_variables
def test_find_variables():
    source = '''
    let(y)
    x = 1
    let(x)
    import os
    let(i)
    '''
    assert find_variables(ast.parse(source)) == ['y', 'x', 'i']

# Generated at 2022-06-14 02:54:40.691346
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Snippet:
        def __init__(self, var1: int, var2: str) -> None:
            self.var1 = var1
            self.var2 = var2

        @snippet
        def get_function1(self):
            let(x)
            let(y)
            x = randint(1, 100)
            y = x + 10
            return x, y

        @snippet
        def get_function2(self):
            let(x)
            x = randint(1, 100)
            y = x + 10
            return x, y

    snippet_obj = Snippet(1, '2')


# Generated at 2022-06-14 02:54:51.060465
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class TestClass:
        def test_method(self):
            def func():
                let(x)
                let(y)
                x += x
                extend(vars)
                let(z)
                print(x, y, z)
                return x

            return func

    test_obj = TestClass()
    func = test_obj.test_method()

    snippet_kwargs = {'x': 1, 'vars': [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=2)),
                                       ast.Assign([ast.Name(id='z', ctx=ast.Store())], ast.Num(n=-1))]}
    snippet_body = snippet(func).get_body(**snippet_kwargs)

    # body length

# Generated at 2022-06-14 02:55:01.478514
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    let(x)
    x += 1
    y = 1

    s = snippet(lambda: None)
    body = s.get_body(x=2)
    result = ast.parse('\n'.join(get_source(node) for node in body)).body

# Generated at 2022-06-14 02:55:13.440808
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Tests method snippet.get_body()."""

    class TestSnippet(snippet):
        @staticmethod
        def test(arg1: int, arg2: int):
            """Test function"""

            var: int = arg1 + arg2

            let(var)

            var += 1
            print(x)


# Generated at 2022-06-14 02:55:23.648487
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = """
        def foo():
            let(x)
            x = 1
            y = 2
            return x + y
    """
    tree = ast.parse(source)
    snippet_kwargs = {'x': ast.Num(n=1)}
    variables = {'x': VariablesGenerator.generate('x')}

# Generated at 2022-06-14 02:55:25.633711
# Unit test for function extend_tree

# Generated at 2022-06-14 02:55:37.973395
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class A:
        pass

    a = A()
    a.x = 5

    class B:
        pass

    b = B()
    b.y = 10

    class C:
        pass

    c = C()
    c.z = 20

    class D:
        pass

    d = D()

    @snippet
    def main(a: A, b: B) -> C:
        let(c)
        # let(d)
        c.z = a.x + b.y
        # d.x = c.z + 100
        return c

    body1 = main.get_body(a=a, b=b)  # c is declared
    assert len(body1) == 2

    body2 = main.get_body(a=a, b=b, c=c)
   

# Generated at 2022-06-14 02:55:46.274297
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = let(10)
    y = let(5)
    z = extend(5)
    
    def f(x: Any, y: Any, z: Any) -> None:
        x += 1
        y += x
        z += 1
        a = let(z)
        b = extend(z)
        print(a, b)

    result = snippet(f).get_body(x=x, y=y, z=z)

# Generated at 2022-06-14 02:55:55.676374
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)")
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id = 'x', ctx = ast.Store())], value = ast.Num(n = 1)), ast.Assign(targets=[ast.Name(id = 'x', ctx = ast.Store())], value = ast.Num(n = 2))]})
    assert get_source(tree) == "x = 1\nx = 2"

# Generated at 2022-06-14 02:56:18.310167
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet(x: int, y: int) -> int:
        let(x)
        x += 1
        y = 1
        return x + y


# Generated at 2022-06-14 02:56:28.667836
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x: int, y: int = 5) -> None:
        let(x)
        x += 1
        y += x
        print(x, y)

    s = snippet(test_snippet)
    test_tree = ast.parse("let(x); x += 1; y += x; print(x, y)")

    body_tree = ast.parse("_py_backwards_x_0 += 1; y += _py_backwards_x_0; print(_py_backwards_x_0, y)")

# Generated at 2022-06-14 02:56:35.494308
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: None).get_body() == []
    assert snippet(lambda: let(1)).get_body() == []
    assert snippet(lambda: x).get_body() == [ast.parse('x').body[0]]
    assert snippet(lambda: let(x)).get_body() == [ast.parse('_py_backwards_x_0').body[0]]
    assert snippet(lambda: let(x) + x).get_body() == [ast.parse('_py_backwards_x_0 + _py_backwards_x_0').body[0]]
    assert snippet(lambda: let(x) + y).get_body() == [ast.parse('_py_backwards_x_0 + y').body[0]]

# Generated at 2022-06-14 02:56:44.728610
# Unit test for function extend_tree
def test_extend_tree():
    from .tree import ast_to_source

    def test_simple_case():
        tree = ast.parse("""
            extend(vars)
            assert True
        """)
        
        extend_tree(tree, {'vars': [
            ast.Assign([ast.Name(
               id='x', ctx=ast.Store())], ast.Num(n=1)) 
        ]})

        assert ast_to_source(tree).strip() == "x = 1\nassert True"

    def test_with_multiple():
        tree = ast.parse("""
            extend(vars)
            assert True
        """)
        

# Generated at 2022-06-14 02:56:45.452105
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # TODO: implement unit test
    assert 1 == 1

# Generated at 2022-06-14 02:56:54.339620
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars); print(x, y)')
    vars = ast.Module([ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                  ast.Num(n=1)),
                       ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                                  ast.Num(n=2))])
    extend_tree(tree, {'vars': vars})
    expected = ast.parse('x = 1; x = 2; print(x, y)')
    assert ast.dump(expected) == ast.dump(tree)

# Generated at 2022-06-14 02:56:59.828111
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn(a, b):
        let(c)
        d = a + b + c
        e = c
        extend(f)
        return d + e

    snippet_fn.a = 1
    snippet_fn.b = 2
    snippet_fn.c = 3
    snippet_fn.f = [ast.Assign(target=[ast.Name(id='c')], value=ast.Num(n=4))]

# Generated at 2022-06-14 02:57:06.590125
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_let(x:int)->int:
        let(x)
        x += 1
        y = 1
        return x + y
    
#     print(test_let(1))

    test_snippet = snippet(test_let)
    print(test_snippet.get_body(x=1))
    a = test_snippet.get_body(x=1)
    print(ast.dump(a[0]))
    print(ast.dump(a[1]))
    
#     x += 1
#     print(ast.dump(a[1]))
#     x += 1
#     x += 1


# Generated at 2022-06-14 02:57:18.045788
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor  # type: ignore
    from .reverse import reverse_identifiers, reverse_functions, reverse_classes

    def fn(x: int) -> int:
        let(y)
        y = 1
        if x:
            let(z)
            z = 2
        return y + z  # noqa

    @snippet
    def snippet_with_let():
        let(x)
        x += 1
        y = 1

    @snippet
    def snippet_with_extend(x: int):
        extend(x)
        y = 2
        return y + x

    assert astor.to_source(snippet_with_let.get_body()) == '_py_backwards_x_0 += 1\n' \
                                                           'y = 1\n'


# Generated at 2022-06-14 02:57:21.698686
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test():
        let(x)
        x += 1
        y = 1
    assert len(test.get_body()) == 2
    assert test.get_body()[0].value.op == ast.Add



# Generated at 2022-06-14 02:57:50.876009
# Unit test for function find_variables
def test_find_variables():
    source = """
        def f():
            let(i)
            let(j)
            return i + j
    """

    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'i', 'j'}



# Generated at 2022-06-14 02:57:54.327360
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func():
        let(x)
        x = 1
        y = 2

    expected = ast.parse("""x = 1
                            y = 2""").body

    assert snippet(func).get_body() == expected

# Generated at 2022-06-14 02:57:57.625022
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        let(x)
        x += 1
        let(y)
        print(x, y)
    """)
    assert list(find_variables(tree)) == ['x', 'y']



# Generated at 2022-06-14 02:57:58.569405
# Unit test for function find_variables

# Generated at 2022-06-14 02:58:07.394077
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _get_body(x: int, y: int) -> List[ast.AST]:
        let(x)
        x += 1
        y = 1
        return x, y

    snippet = snippet(_get_body)

# Generated at 2022-06-14 02:58:12.433570
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int, y: int):
        let(x)
        x += y
        y = 1
        print(y)
        for i in range(x):
            z = 1
            z += x
        return x

    assert foo.get_body(x=1, y=1) == foo.get_body(x=2, y=1)

# Generated at 2022-06-14 02:58:23.914378
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """
    Unit test for get_body of snippet
    """

    def test_function():
        # print('this is test function')
        let(var1)
        extend(var2)
        let(var3)

    var1 = 2
    var2 = ast.parse('x = 1\nx = 2', mode='exec')
    var3 = ast.parse('x = True', mode='exec')

    test_snippet = snippet(test_function)
    body = test_snippet.get_body(var1=var1, var2=var2, var3=var3)

    assert(len(body) == 2)
    body = body[0].body
    assert(len(body) == 2)
    assert(isinstance(body[0], ast.Assign))

# Generated at 2022-06-14 02:58:29.613921
# Unit test for function extend_tree
def test_extend_tree():
    vars = ast.parse("x = 1\nx = 2")
    input_parse = ast.parse("extend(vars)\nprint(x, y)")
    extend_tree(input_parse, {'vars': vars})
    assert ast.dump(input_parse) == ast.dump(vars) + "\nprint(x, y)"

# Generated at 2022-06-14 02:58:38.768486
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """
    >>> @snippet
    ... def f(x: int):
    ...    let(y)
    ...    y += 1
    >>> f.get_body(x=1)
    [<_ast.Assign at 0x10c3583c8>, <_ast.Expr at 0x10c358470>]
    """
    pass

# Generated at 2022-06-14 02:58:46.885568
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    def snippet():
        let(x)
        let(y)

    assert astor.to_source(snippet.get_body()) == """
    _py_backwards_x_0
    _py_backwards_y_0
    """.strip()

    def snippet():
        let(a)
        x = ast.Name("y", ast.Load())
        y = ast.Name("a", ast.Load())

    assert astor.to_source(snippet.get_body()) == """
    _py_backwards_a_0
    x = y
    y = _py_backwards_a_0
    """.strip()

    def snippet(x, y):
        let(a)
        x = y + 1
        y = a + 2

    assert astor.to

# Generated at 2022-06-14 02:59:42.642284
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    snippet_kwargs = {"var": ast.parse("x=1").body[0].value}

# Generated at 2022-06-14 02:59:58.166180
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x: int, y: int) -> None:
        let(z)
        let(a)
        let(b)
        a = 1
        b = 2
        extend(c)
        c = x + y

    snippet_body = fn.get_body(x='x', y='y', c=[ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                          value=ast.Num(1)),
                                                  ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                                          value=ast.Num(2))])

# Generated at 2022-06-14 03:00:08.488630
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet():
        let(x_val)
        y = x_val + 1
        z = 2 * y

    # Unit test snippet with parametr x_val
    variables = {'x_val': 1}
    ast_body = test_snippet.get_body(**variables)

    result = ast.dump(ast_body)

# Generated at 2022-06-14 03:00:18.245652
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn():
        let(x)
        x += 1
        y = 1
    _snippet = snippet(fn)
    assert _snippet.get_body() == [
        ast.Assign([ast.Name('_py_backwards_x_0', ast.Store())], ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()), ast.Add(), ast.Num(1))),
        ast.Assign([ast.Name('y', ast.Store())], ast.Num(1))
    ]



# Generated at 2022-06-14 03:00:20.781767
# Unit test for function find_variables
def test_find_variables():
    source = """let(a)
let(b)
a + b
"""
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['a', 'b']



# Generated at 2022-06-14 03:00:29.279038
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_with_let(y: int = let(1)) -> int:
        return y

    def snippet_without_let() -> int:
        return 1

    def snippet_with_let_and_extend(x: int = let(1), vars: List[ast.AST] = extend([])) -> int:
        return x

    def snippet_with_extend_only(vars: List[ast.AST] = extend([])) -> int:
        return 1

    # Check correctness with let
    snippet_with_let_tree = snippet(snippet_with_let).get_body()
    assert snippet_with_let_tree == [ast.Return(value=ast.Name(id='_py_backwards_y_0', ctx=ast.Load()))]

    # Check correctness without let
    snippet

# Generated at 2022-06-14 03:00:36.868538
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        let(x)
        x += 1
        y = 1
        
    assert snippet(f).get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Load())],
            value=ast.BinOp(
                left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                op=ast.Add(),
                right=ast.Num(n=1)
            )
        ),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1)
        )
    ]

# Generated at 2022-06-14 03:00:42.652408
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    FOO_VAL = 42
    def foo() -> None:
        let(x)
        x += FOO_VAL
    snippet_body = snippet(foo).get_body()
    assert len(snippet_body) == 1
    assert isinstance(snippet_body[0], ast.Assign)
    assert snippet_body[0].value.op == ast.Add()
    assert snippet_body[0].value.left.id == '_py_backwards_x_0'
    assert snippet_body[0].value.right.n == FOO_VAL


# Generated at 2022-06-14 03:00:53.320183
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(x: int) -> int:
        let(y)
        let(z)
        return x * y * z

    expected = """
let(z)
_py_backwards_y_0 = 5
_py_backwards_x_0 = 4
return _py_backwards_x_0 * _py_backwards_y_0 * z
"""
    result = ast.dump(fn.get_body(y=5, z=4))
    assert result == expected