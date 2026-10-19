

# Generated at 2022-06-14 02:50:25.940435
# Unit test for function extend_tree
def test_extend_tree():
    import astor

    tree = ast.parse("""
        extend([
            1,
            2,
        ])
    """)

    extend_tree(tree, {'[1, 2]': [
        ast.Assign(targets=[ast.Name(id='x')],
                   value=ast.Num(n=1)),
        ast.Assign(targets=[ast.Name(id='x')],
                   value=ast.Num(n=2)),
    ]})

    expected = """
x = 1
x = 2
    """.strip()

    assert expected == astor.to_source(tree).strip()

# Generated at 2022-06-14 02:50:33.864949
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)")
    variable = ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(n=1))
    extend_tree(tree, {'vars': [variable]})
    assert get_source(tree) == 'x = 1'

# Generated at 2022-06-14 02:50:43.068597
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_kwargs = {}
    n = 3
    for i in range(n):
        snippet_kwargs['x' + str(i)] = i

    @snippet
    def square():
        # type: (**snippet_kwargs) -> None
        for i in range(n):
            x = let(snippet_kwargs['x' + str(i)])


if __name__ == '__main__':
    # Unit test for method get_body of class snippet
    test_snippet_get_body()

# Generated at 2022-06-14 02:50:49.464396
# Unit test for function extend_tree
def test_extend_tree():
    source = """
extend(vars)
print(x, y)
    """
    tree = ast.parse(source)
    variables = {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(1)),
                          ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())], value=ast.Num(2))]}
    extend_tree(tree, variables)
    assert get_source(tree) == "x = 1\nx = 2\nprint(x, y)\n"



# Generated at 2022-06-14 02:50:51.773591
# Unit test for function find_variables
def test_find_variables():
    source = """
let(x)
x += 1
y = 1
"""
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'x'}



# Generated at 2022-06-14 02:50:55.455616
# Unit test for function find_variables
def test_find_variables():
    source = """
    let(x)
    let(y)
    """
    tree = ast.parse(source)
    assert set(find_variables(tree)) == set(['x', 'y'])



# Generated at 2022-06-14 02:51:07.252019
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class T:
        @snippet
        def snippet(x: int, y: int) -> None:
            y = x + y
            a = 1

        def snippet_caller(self):
            self.snippet(x=1, y=2)


# Generated at 2022-06-14 02:51:12.747330
# Unit test for function extend_tree
def test_extend_tree():
    snippet_code = '''
        extend(vars)
        x += 1
        y = 1
    '''

    vars_code = '''
        x = 1
        x = 2
    '''

    expected = '''
        x = 1
        x = 2
        x += 1
        y = 1
    '''

    tree = ast.parse(snippet_code)
    variables = {'vars': ast.parse(vars_code).body}
    extend_tree(tree, variables)
    assert get_source(tree) == expected

# Generated at 2022-06-14 02:51:20.959199
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(var)\n')
    variables = {'var': [ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=1)),
                         ast.Assign([ast.Name(id='x', ctx=ast.Store())], ast.Num(n=2))]}
    extend_tree(tree, variables)
    assert get_source(tree) == 'x = 1\nx = 2\n'

# Generated at 2022-06-14 02:51:27.345533
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)')
    vars = [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1)),
        ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=2))
    ]
    extend_tree(tree, {'vars': vars})
    assert ast.dump(tree) == "Module(body=[Extend(vars=[Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id='y', ctx=Store())], value=Num(n=2))])])"

# Generated at 2022-06-14 02:51:31.548226
# Unit test for function extend_tree

# Generated at 2022-06-14 02:51:36.677456
# Unit test for function extend_tree
def test_extend_tree():
    code = """
    let(a)
    x = 1
    y = a
    extend(a)
    """
    tree = ast.parse(code)
    let(x=1, y=2)
    extend(x=3)
    assert get_source(tree) == """
    x = 3
    x = 1
    y = x
    x = 3
    """

# Generated at 2022-06-14 02:51:43.123213
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: int, y: int) -> None:
        let(z)
        let(a)
        a.b = 1
        a.c = 2
        x = 1 + 2
        y = x + z + 10
        print(x, y, a)

    body = test.get_body(x=ast.Name(id='a', ctx=ast.Load()), z=0)
    print(ast.dump(body))

# Generated at 2022-06-14 02:51:52.542394
# Unit test for function extend_tree
def test_extend_tree():

    tree = ast.parse('''
        extend(l)
    ''')

    l = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                     value=ast.Num(n=2))]
    extend_tree(tree, {'l': l})
    assert ast.dump(tree) == '''
    Assign(
        targets=[
            Name(
                id='x',
                ctx=Store(),
            ),
        ],
        value=Num(
            n=2,
        ),
    )'''

# Generated at 2022-06-14 02:52:00.136321
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def foo(x: int, y: int) -> str:
        let(z)
        return str(z)

    snippet_object = snippet(foo)

    # Test case 1
    # source:
    #   def foo(x: int, y:int) -> str:
    #       let(z)
    #       return str(z)

# Generated at 2022-06-14 02:52:07.959050
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    extend(var)
    """)
    tree.body[0].args[0].id = 'var'  # type: ignore

    ast.fix_missing_locations(tree)
    extend_tree(tree, {
        'var': [
            ast.parse("x = 1").body[0],
            ast.parse("y = 1").body[0]
        ]
    })

    assert get_source(tree) == """
    x = 1
    y = 1
    """[1:]



# Generated at 2022-06-14 02:52:15.541345
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def unit_test():
        let(x)
        x += 1
        y = 1

    snippet_instance = snippet(unit_test)
    assert snippet_instance.get_body() == [
        ast.Assign(
            targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
            value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                            op=ast.Add(),
                            right=ast.Num(n=1))
        ), ast.Assign(
            targets=[ast.Name(id='y', ctx=ast.Store())],
            value=ast.Num(n=1),
        )
    ]

# Generated at 2022-06-14 02:52:26.616664
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x):
        for _ in range(y):
            z = x**4
            print(x, z)
    
    tree = snippet(func).get_body(y=3, x=2)

# Generated at 2022-06-14 02:52:33.185237
# Unit test for function extend_tree
def test_extend_tree():
    def snippet(vars: List[ast.Assign]) -> None:
        extend(vars)
        print(x)

    vars = [
        ast.parse('x = 1').body[0],
        ast.parse('x = 2').body[0],
    ]
    tree = snippet.get_body(vars=vars)
    assert ast.dump(tree) == "[Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=1)), Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=2)), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]))]"



# Generated at 2022-06-14 02:52:44.361843
# Unit test for function extend_tree
def test_extend_tree():
    # 1. Statement
    tree = ast.parse('extend(vars); print(x)')
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id='x')],
                                           value=ast.Num(n=1)),
                                ast.Assign(targets=[ast.Name(id='x')],
                                           value=ast.Num(n=2))]})
    assert get_source(tree) == 'x = 1\nx = 2\nprint(x)'

    # 2. Expression
    tree = ast.parse('print(extend(vars) * 5)')

# Generated at 2022-06-14 02:53:00.643398
# Unit test for function extend_tree
def test_extend_tree(): 
    import pprint
    from .helpers import import_common, ast_to_source
    from .tree import find
    ast_common = import_common()
    expr = ast_common.expr
    test_source = '''
    extend(vars)
    print(x, y)
    '''
    tree = ast.parse(test_source)
    vars = [expr('x = 1'), expr('x = 2')]
    extend_tree(tree, {'vars': vars})
    source = ast_to_source(tree)
    expected = '''
    x = 1
    x = 2
    print(x, y)
    '''
    assert(source == expected)

# Generated at 2022-06-14 02:53:05.921280
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""def test():
        extend(vars)
        test()""")
    func = tree.body[0]
    assert func.name == 'test'
    assert isinstance(func, ast.FunctionDef)
    body = func.body
    assert isinstance(body[0], ast.Expr)
    assert isinstance(body[0].value, ast.Call)
    assert isinstance(body[0].value.args[0], ast.Name)
    assert body[0].value.args[0].id == 'vars'
    assert isinstance(body[1], ast.Expr)
    assert isinstance(body[1].value, ast.Call)
    assert isinstance(body[1].value.func, ast.Name)
    assert body[1].value.func.id == 'test'

# Generated at 2022-06-14 02:53:15.608292
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    def fn():
        extend(vars)
        x = 1
        print(x)
    """
    tree = ast.parse(source)
    variables = {'vars': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(n=1)),
                          ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(n=2))]}
    extend_tree(tree, variables)
    assert isinstance(tree.body[0].body[0], ast.Assign)
    assert isinstance(tree.body[0].body[1], ast.Assign)



# Generated at 2022-06-14 02:53:24.722026
# Unit test for function extend_tree

# Generated at 2022-06-14 02:53:32.789965
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
    let(body)
    extend(body)
    """)
    variables = {'body': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(1)),
                          ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                     value=ast.Num(2))]}
    extend_tree(tree, variables)
    assert [node.targets[0].id for node in find(tree, ast.Assign)] == ['x', 'x']
    assert [node.value.n for node in find(tree, ast.Num)] == [1, 2]



# Generated at 2022-06-14 02:53:41.224454
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet() -> None:
        let(x)
        x += 1
        y = 1
        extend(vars)
        let(z)

    code = my_snippet.get_body(x=2, vars=[ast.Assign([ast.Name(id='x')], ast.Num(2))], z=2)

    source = get_source(code)
    assert source == 'x = 2\nx = 2\ny = 1\n_py_backwards_z_0 = 2'



# Generated at 2022-06-14 02:53:52.755075
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_body():
        let(x)
        x += 1
        let(y)
        y = 1
        return x + y

    a = test_body.get_body()
    assert(ast.dump(a) == '[Assign(targets=[Name(_py_backwards_x_0, Store())], value=BinOp(left=Name(_py_backwards_x_0, Load()), op=Add(), right=Constant(1, None))), Assign(targets=[Name(_py_backwards_y_1, Store())], value=Constant(1, None)), Return(value=BinOp(left=Name(_py_backwards_x_0, Load()), op=Add(), right=Name(_py_backwards_y_1, Load())))]')

# Generated at 2022-06-14 02:53:58.378852
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(vars)\n"
                     "print(x + 1, y)")
    vars = ast.parse("\n".join(
        "x = %d" % i for i in range(1, 10)
    ))
    extend_tree(tree, {
        "vars": vars.body
    })
    ext_tree = ast.parse("\n".join(
        "x = %d" % i for i in range(1, 10)
    ) + "\nprint(x + 1, y)")
    assert ast.dump(tree) == ast.dump(ext_tree)

# Generated at 2022-06-14 02:54:09.244022
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _snippet():
        let(x)
        x += 1
        y = 1

    snippet_obj = snippet(_snippet)
    snippet_body = snippet_obj.get_body()
    assert(snippet_body[0].value.op == 'Add')
    assert(snippet_body[0].value.left.id == '_py_backwards_x_0')
    assert(snippet_body[0].value.right.n == 1)
    assert(snippet_body[1].value.n == 1)
    assert(snippet_body[1].targets[0].id == 'y')



# Generated at 2022-06-14 02:54:18.712285
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
let(vars)
extend(vars)
let(vars)
extend(vars)
let(vars)
extend(vars)
""")
    names = find_variables(tree)
    variables = {name: VariablesGenerator.generate(name)
                 for name in names}
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)
    print(ast.dump(tree))


# Generated at 2022-06-14 02:54:32.199310
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def myfunc(x: int, y: int):
        let(x)
        let(y)
        extend(z)
        x += y 
    
    assert myfunc.get_body(x=1, y=2, z=['a = 3']) == \
        [ast.AugAssign(ast.Name('_py_backwards_x_0', ast.Load()), ast.Add(), ast.Num(1)),
         ast.Assign([ast.Name('_py_backwards_y_1', ast.Store())], ast.Num(2)),
         ast.Assign([ast.Name('a', ast.Store())], ast.Num(3))]

# Generated at 2022-06-14 02:54:41.472036
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2

    @snippet
    def snip() -> None:
        let(a)
        let(b)
        b = a + a
    

# Generated at 2022-06-14 02:54:51.032228
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet1_expected_result = """
    def foo(x, y):
        return x + y
    """
    snippet1_expected_ast = ast.parse(snippet1_expected_result)
    snippet1_expected_ast.body.pop()
    snippet1_actual_ast = snippet(lambda x, y: let(x + y)).get_body()
    assert ast.dump(snippet1_actual_ast) == ast.dump(snippet1_expected_ast.body)

    snippet2_expected_result = """
    def foo(x, y):
        return _py_backwards_x_0 + y
    """
    snippet2_expected_ast = ast.parse(snippet2_expected_result)
    snippet2_expected_ast.body.pop()
    snippet2_actual_ast

# Generated at 2022-06-14 02:55:01.429395
# Unit test for function extend_tree
def test_extend_tree():
    # checking that extend_tree extends tree properly
    extended_tree = ast.parse('x += 1\n'
                              'extend(expanded_tree)\n'
                              'y = 1\n')

    variable_tree = ast.parse('x = 1\n'
                              'x = 2\n')

    extend_tree(extended_tree, {'expanded_tree': variable_tree})

    # checking that extend_tree doesn't change unextended trees
    tree = ast.parse('x = 1\n')
    extend_tree(tree, {'expanded_tree': variable_tree})
    assert ast.dump(tree) == ast.dump(ast.parse('x = 1\n'))

    # checking that extend_tree replaces first occurance of extend call

# Generated at 2022-06-14 02:55:13.441135
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def get_body(**kwargs):
        def body():
            extend(kwargs.get('assignments', []))  # type: ignore
            let(kwargs.get('x', None))  # type: ignore
            return x  # type: ignore

        return snippet(body).get_body(**kwargs)  # type: ignore

    body = get_body(x=0)
    assert len(body) == 1
    assert isinstance(body[0], ast.Return)
    assert isinstance(body[0].value, ast.Num)
    assert body[0].value.n == 0

    body = get_body(assignments=[ast.Assign(targets=[ast.Name('x', ast.Store())],
                                            value=ast.Num(2))])

# Generated at 2022-06-14 02:55:20.765180
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_function():
        extend([ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                           value=ast.Num(n=1))])
        extend([ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                           value=ast.Num(n=2))])
        print('x', 'y')

    cls_instance: snippet = snippet(snippet_function)
    cls_instance.get_body()

# Generated at 2022-06-14 02:55:27.801192
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import pytest
    import astor
    import astunparse
    import ast

    def _get_ast(body):
        source = astor.codegen.to_source(body, tabsize=1)
        tree = ast.parse(source)
        return tree.body
    
    def test(tree, **kwargs):
        @snippet
        def f(x: str, y: str, z: str):
            """Function description."""
            let(x)
            extend(x)
            extend(y)
            extend(z)
            y = x + y
            z = z + x
            z = z + y
        ast = f.get_body(**kwargs)
        assert _get_ast(ast) == tree


# Generated at 2022-06-14 02:55:35.937703
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""extend(vars)""")
    replace_at(0, tree.body[0], [ast.Assign([ast.Assign([ast.Name('a', ast.Load())], ast.Num(1))], ast.Num(2))])
    extend_tree(tree, vars)
    assert get_source(tree) == 'a = 2'

# Generated at 2022-06-14 02:55:37.579321
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert 'let' in snippet(None).get_body()



# Generated at 2022-06-14 02:55:42.389168
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snip1(a, b):
        let(c)
        return a + b + c

    def snip2():
        let(x)
        x = 1
        return x

    def snip3():
        let(x, y, z)
        return x, y, z

    def snip4():
        let(y)
        x = 1
        return x, y

    def snip5():
        let(x)
        x = 1
        return x, x

    def snip6():
        let(x, y)
        x = 1
        y = 2
        return x, y

    def snip7():
        let(x, y, z)
        x = 1
        y = x
        z = y
        return x, y, z


# Generated at 2022-06-14 02:56:04.343737
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_source = '''\
left_paren = "("
right_paren = ")"

if isinstance(node, ast.Expr):
    let(body)
    body += right_paren
else:
    let(body)
    body += "," + right_paren
'''
    snippet_ast = ast.parse(snippet_source)
    let_calls = list(find(snippet_ast, ast.Call))
    assert len(let_calls) == 2
    vars_ = {}
    variables = find_variables(snippet_source)
    assert set(variables) == {'body'}
    for var in variables:
        vars_[var] = VariablesGenerator.generate(var)

# Generated at 2022-06-14 02:56:07.669529
# Unit test for function find_variables
def test_find_variables():
    assert list(find_variables(
        ast.parse("""
        let(x)
        let(y)
        """
        )
    )) == ['x', 'y']



# Generated at 2022-06-14 02:56:19.177987
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def _f():
        let(x)
        x = 1
        extend(vars)
        extend(vars2)

    snippet_instance = snippet(_f)
    snippet_instance.get_body()
    snippet_instance.get_body(x=1, vars=[ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Num(n=1))],
        vars2=[ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=2))])

# Generated at 2022-06-14 02:56:24.273760
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_case(fn: Callable[..., None], **kwargs: Any) -> None:
        assert fn.get_body(**kwargs) == ast.parse("def x():\n    x = 1").body

    test_case(snippet(lambda x: x))
    test_case(snippet(lambda x: let(x)), x=1)


# Generated at 2022-06-14 02:56:28.942859
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_fn():
        let(x)
        x += 1
        y = 1

    snippet_obj = snippet(snippet_fn)
    result = snippet_obj.get_body()
    assert type(result) == list
    assert len(result) == 3
    assert isinstance(result[0], ast.Assign)
    assert isinstance(result[1], ast.AugAssign)
    assert isinstance(result[2], ast.Assign)

# Generated at 2022-06-14 02:56:32.771178
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x, y=None):
        let(x)
        extend(y)
        return [x]

    snippet_instance = snippet(test_snippet)
    body = snippet_instance.get_body(x=1, y=[])
    assert len(body) == 1
    assert body[0].value.args[0].s == '1'

# Generated at 2022-06-14 02:56:42.510585
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test snippet replacement."""
    s = snippet(lambda: x)
    assert s.get_body()[0].value.id == '_py_backwards_x_0'  # type: ignore

    s = snippet(lambda: x + 1)
    assert s.get_body()[0].value.left.id == '_py_backwards_x_0'  # type: ignore

    s = snippet(lambda: x(y))
    assert s.get_body()[0].value.func.id == '_py_backwards_x_0'  # type: ignore

    s = snippet(lambda: x[y])
    assert s.get_body()[0].value.value.id == '_py_backwards_x_0'  # type: ignore

    s = snippet(lambda: x.y())

# Generated at 2022-06-14 02:56:48.123943
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Checks that snippet get_body returns expected AST."""
    def test_snippet(a: int,
                     b: Union[ast.Name, str]) -> Union[bool, ast.Name]:
        """Returns AST of snippet with arguments replaced."""
        if let(b) is None:
            b = 0

        return a <= b

    source = get_source(test_snippet)
    tree = ast.parse(source)
    variables = find_variables(tree)
    extend_tree(tree, variables)
    VariablesReplacer.replace(tree, variables)

    for v in variables.values():
        if isinstance(v, ast.Name):
            assert str(v.id).startswith('_py_backsards_')

# Generated at 2022-06-14 02:56:58.203980
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .helpers import is_checked

    def f1(x: int) -> None:
        let(y)
        y = x * x * x + x * x + x + 1
        print(y)

    tree = snippet(f1).get_body(x=2)

    y = tree[0].value.left.id
    assert isinstance(tree[0], ast.Assign)
    assert is_checked(tree[0].value.right,
                      ast.BinOp(ast.Name(y, ast.Load()), ast.Mult(),
                                ast.BinOp(ast.Name(y, ast.Load()), ast.Mult(),
                                          ast.Name(y, ast.Load()))))

# Generated at 2022-06-14 02:57:04.091041
# Unit test for function find_variables
def test_find_variables():
    tree = ast.parse("""
        let(x)
        let(y)
        let(z)
    """)
    assert find_variables(tree) == ['x', 'y', 'z']
    assert get_source(tree) == """
        z
        z
        z
    """



# Generated at 2022-06-14 02:57:25.132976
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet(x: int, y: int) -> None:
        let(x)
        x += 1
        y = 1
        return y
    assert my_snippet.get_body()[0].value.value == 1


# Generated at 2022-06-14 02:57:38.775305
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def func(x: int, y: int):
        let(x)
        x += 1
        z = 1
        z += 1
        z += 1
        return z


# Generated at 2022-06-14 02:57:42.133582
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x, y):
        let(a)
        let(b)
        let(c)
        return (a + b) / c

    snippet(f).get_body(
        a=2,
        b=1,
        c=ast.Name('d', ast.Load()),
    )



# Generated at 2022-06-14 02:57:53.235578
# Unit test for function extend_tree
def test_extend_tree():
    code = ('extend(vars)\n'
            'vars = (1, 2)')
    tree = ast.parse(code)
    extend_tree(tree, {'vars': [ast.Assign(targets=[ast.Name(id='vars')],
                                           value=ast.Num(1)),
                                ast.Assign(targets=[ast.Name(id='vars')],
                                           value=ast.Num(2))]})
    assert code == compile(tree, filename='<ast>', mode='exec').co_code

# Generated at 2022-06-14 02:57:58.423217
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x, y):
        let(a)
        let(b)
        return a, b

    expected = """
    def f(_py_backwards_a_0, _py_backwards_b_0):
        return _py_backwards_a_0, _py_backwards_b_0
    """
    assert expected == ast.dump(snippet(f).get_body())



# Generated at 2022-06-14 02:58:02.623989
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """Test method snippet.get_body."""
    
    @snippet
    def snippet_func():
        let(x)
        x += 1
        y = 1
        
    lines = snippet_func.get_body()
    assert len(lines) == 2
    assert isinstance(lines[0], ast.AugAssign)
    assert isinstance(lines[1], ast.Assign)

# Generated at 2022-06-14 02:58:03.487073
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:58:12.040937
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def s(a: int, b: int = 2) -> int:
        let(x)
        x = a + b
        return x

    assert s.get_body(a=1) == ast.parse('_py_backwards_x_0 = (1 + 2)').body  # type: ignore
    assert s.get_body(a=2, b=3) == ast.parse('_py_backwards_x_1 = (2 + 3)').body  # type: ignore



# Generated at 2022-06-14 02:58:21.988956
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    """
    Checks if get_body of snippet class returns correct AST and does not change the original function
    :return:
    """
    @snippet
    def test_snippet(a):
        let(b)
        let(c)
        a = 2
        b = a
        c = a + b
        return c

    test_body = test_snippet.get_body(b=3, c=5)
    assert get_source(test_snippet._fn) == '''
        def test_snippet(a):
            let(b)
            let(c)
            a = 2
            b = a
            c = a + b
            return c
    '''

# Generated at 2022-06-14 02:58:28.209378
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x, y: x + y).get_body(x=10, y=20) == \
        [ast.Expr(value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0',
                                                ctx=ast.Load()),
                                  op=ast.Add(),
                                  right=ast.Name(id='_py_backwards_y_0',
                                                 ctx=ast.Load())))]

# Generated at 2022-06-14 02:59:11.563746
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f():
        extend(vars)
        print(x, y)
        return let(z)
    
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(n=2))]
    snippet_instance = snippet(f)
    body = snippet_instance.get_body(x='x')

# Generated at 2022-06-14 02:59:17.429477
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet_var = 1
    _py_backwards_snippet_var_0 = 0
    _py_backwards_snippet_var_1 = 0
    _py_backwards_snippet_var_2 = 0

    def _py_backwards_test_snippet_get_body_1():
        let(snippet_var)
        return snippet_var

    assert snippet(_py_backwards_test_snippet_get_body_1).get_body() == \
        _py_backwards_test_snippet_get_body_1().body  # type: ignore
    assert snippet(_py_backwards_test_snippet_get_body_1).get_body(variable=10) == \
        _py_backwards_test_snippet_get_body_1

# Generated at 2022-06-14 02:59:29.131188
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    result = 9
    
    def fn(a: int, b: int) -> int:
        let(x)
        let(y)
        x += a
        y += b
        return x + y


# Generated at 2022-06-14 02:59:39.555813
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    class Class:
        def method(self, x: int) -> None:
            let(a)
            a = x
            method_var = 1
            extend(vars)
            print(a, self.class_var, method_var, b)
            extend(vars_2)
            print(b)

    code = get_source(Class.method)

    obj = Class()
    obj.class_var = 2
    vars = [ast.Assign([ast.Name('a')], ast.Constant(1)),
            ast.Assign([ast.Name('b')], ast.Constant(2))]
    vars_2 = [ast.Assign([ast.Name('b')], ast.Constant(3))]
    snippet_instance = snippet(eval(code))
    code = snippet_instance.get

# Generated at 2022-06-14 02:59:46.633490
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    _x = 10
    sources = [
        """
        def func():
            let(x)
            let(y)
            let(z)
            z = x + y
            print(x, y, z)

        x = 1
        y = 2
        func()
        """,
        """
        extend(x)
        """,
        """
        def func():
            let(x)
            x = 2
        func()
        """
    ]

# Generated at 2022-06-14 03:00:01.514931
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 1
    y = 2
    test1 = snippet(lambda x, y: let(x + y))
    test2 = snippet(lambda x, y: let(x + y) + x + y)
    test3 = snippet(lambda x, y: let(x + y) + x)
    test4 = snippet(lambda x, y: let(x + y) + y)
    test5 = snippet(lambda x, y: let(x + y))
    test6 = snippet(lambda x, y: let(x + y) + y)
    test7 = snippet(lambda x, y: let(x + y) + let(x + 2))
    test8 = snippet(lambda x, y: let(x + y) + x + let(x + 2))

# Generated at 2022-06-14 03:00:10.255918
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test_snippet(x: int, y: List[int]):
        let(x)
        let(y)
        x += 1
        extend(y)

    # body = test_snippet.get_body(x = 3, y = [1, 2])

    tree = ast.parse('''
    def avg(a, b):
        return (a + b) * 0.5
    ''')

    print(ast.dump(tree))
    tree2 = ast.fix_missing_locations(tree)
    print(ast.dump(tree2))


if __name__ == '__main__':
    test_snippet_get_body()