

# Generated at 2022-06-14 02:50:32.742595
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def fn(a: int, b: int):
        let(x)
        x = a
        return x + b
    
    a, b = 1, 2
    body = fn.get_body(x=a)
    assert body == [ast.Assign([ast.Name('_py_backwards_x_0', ast.Load())], ast.Num(1)), 
                    ast.Return(ast.BinOp(ast.Name('_py_backwards_x_0', ast.Load()), 
                                         ast.Add(), ast.Num(2)))]


# Generated at 2022-06-14 02:50:43.135381
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    source = '''
        def run():
            let(x)
            let(y)
            return x, y
        '''
    tree = ast.parse(source)
    variables = find_variables(tree)
    extend_tree(tree, variables)
    body = VariablesReplacer.replace(tree.body[0].body, variables)
    assert body == [
        ast.Return(value=ast.Tuple(elts=[
            ast.Name(id=variables['x']),
            ast.Name(id=variables['y'])
        ], ctx=ast.Load()))
    ]

# Generated at 2022-06-14 02:50:51.589972
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import typed_ast.ast3 as ast
    from copy import copy
    from .syntax import Equals, Add
    from .models import Comprehension, Function, Class

    body = snippet(lambda x: x + 1).get_body(x=1)
    assert len(body) == 1
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].value, ast.BinOp)
    assert isinstance(body[0].value.left, ast.Name)
    assert isinstance(body[0].value.op, ast.Add)
    assert isinstance(body[0].value.right, ast.Num)
    assert body[0].value.left.id == '_py_backwards_x_0'

# Generated at 2022-06-14 02:51:03.917616
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""for let(v) in [1, 2]:
    print(v)
    extend(let(foo))
    extend(let(bar))
""")
    extend_tree(tree, {'foo': ast.Assign(targets=[ast.Name(id='v', ctx=ast.Store())],
                                         value=ast.Num(n=666)),
                        'bar': ast.Assign(targets=[ast.Name(id='v', ctx=ast.Store())],
                                          value=ast.Num(n=777))})


# Generated at 2022-06-14 02:51:04.888084
# Unit test for function find_variables

# Generated at 2022-06-14 02:51:09.770127
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func2(a: int, b: int, c: int) -> int:
        let(x)
        let(y)
        let(z)
        return a + b + c

    snippet_instance = snippet(func2)
    snippet_instance.get_body()
    snippet_instance.get_body(a = 2, b = 2, c = 2)

# Generated at 2022-06-14 02:51:21.860398
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def my_snippet(x: int, y: int=3) -> None:
        let(x)
        z = 2
        x += y
        z += y
        
    body = my_snippet.get_body(x=5, y=4)
    assert len(body) == 2
    
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[0].targets[0], ast.Name)
    assert body[0].targets[0].id == '_py_backwards_x_0'
    
    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[1].targets[0], ast.Name)
    assert body[1].targets[0].id == 'z'

# Generated at 2022-06-14 02:51:23.908736
# Unit test for function find_variables
def test_find_variables():
    def f():
        let(1)



# Generated at 2022-06-14 02:51:31.828300
# Unit test for function extend_tree
def test_extend_tree():
    source = 'extend(vars) print(x, y)'
    tree = ast.parse(source)
    x = ast.parse('x = 1').body[0]
    y = ast.parse('y = 2').body[0]
    extend_tree(tree, {'vars': [x, y]})
    source = source.replace('vars', 'var')
    source = source.replace('extend', 'let')
    assert source == ast.unparse(tree)



# Generated at 2022-06-14 02:51:42.140822
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('a = 1\n'
                     'b = 2\n'
                     'let(extended)\n'
                     'extend(extended)\n'
                     'print(a, b)')
    extend_tree(tree, {'extended': [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                                               value=ast.Constant(value=1, kind=None)),
                                    ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                                               value=ast.Constant(value=2, kind=None))]})

# Generated at 2022-06-14 02:51:57.947371
# Unit test for function extend_tree
def test_extend_tree():
    var = {'vars': [ast.Assign([ast.Name('x', ast.Store())],
                    ast.Num(1)),
                    ast.Assign([ast.Name('x', ast.Store())],
                    ast.Num(2))]}
    tree = ast.parse('extend(vars)\nprint(x)')
    extend_tree(tree, var)

# Generated at 2022-06-14 02:52:03.632916
# Unit test for function find_variables
def test_find_variables():
    fn_src = '''\
    def f():
        let(x)
        x = x + 1
        let(y)
        y = 2 + 1
        return let(z)
    '''
    tree = ast.parse(fn_src)
    assert list(find_variables(tree)) == ['x', 'y', 'z']



# Generated at 2022-06-14 02:52:07.727878
# Unit test for function find_variables
def test_find_variables():
    result = find_variables(ast.parse('''
        let(x)
        let(y)
        x = y + 20
    '''))
    assert list(result) == ['x', 'y']



# Generated at 2022-06-14 02:52:15.684910
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    TREE = ast.parse(
        "let(x)\n"
        "x = 1\n"
        "y = 2\n"
        "let(z)\n"
        "let(a)\n"
        "a = 1\n"
    )
    EXPECTED_TREE = ast.parse(
        "g0_0 = 1\n"
        "y = 2\n"
        "g0_1 = 1\n"
    )

    from .copy_propagation import copy_propagation

    def func(x: int, y: int, z: int, a: int) -> None:
        let(x)
        x = 1
        y = 2
        let(z)
        let(a)
        a = 1

    tree = copy_propagation(TREE)

# Generated at 2022-06-14 02:52:18.177266
# Unit test for function extend_tree
def test_extend_tree():
    x = let(0)
    y = let(1)
    extend((1, 2))
    assert x == 1 and y == 2

# Generated at 2022-06-14 02:52:19.104761
# Unit test for function extend_tree

# Generated at 2022-06-14 02:52:23.491596
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    import_from_str = 'from math import pi'
    module = (ast.parse(import_from_str)).body[0]  # type: ast.ImportFrom
    replacer = VariablesReplacer({'pi': 'pi'})
    replacer.visit_alias(module.names[0])
    assert module.names[0].name == 'pi'

# Generated at 2022-06-14 02:52:28.400950
# Unit test for method visit_alias of class VariablesReplacer
def test_VariablesReplacer_visit_alias():
    alias_node = ast.alias(name='typing', asname=None)
    variables = {
        'typing': alias_node,
        'typing.List': ['typing.List']
    }
    variables_replacer = VariablesReplacer(variables)
    alias = variables_replacer.visit_alias(alias_node)
    assert alias is alias_node



# Generated at 2022-06-14 02:52:36.359607
# Unit test for function find_variables
def test_find_variables():
    source = """
test = let(test)
test()
test1 = let(test1)
test2 = test1

test3 = let(test3)
test3()
"""
    tree = ast.parse(source)
    assert set(find_variables(tree)) == {'test', 'test1', 'test3'}
    assert get_source(tree) == """
test = test
test()
test1 = test1
test2 = test1

test3 = test3
test3()
"""



# Generated at 2022-06-14 02:52:44.159562
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    c = 3

    @snippet
    def foo():
        let(a)
        a += b
        c += 1


    assert isinstance(foo.get_body(), list)
    assert isinstance(foo.get_body()[0], ast.AugAssign)
    assert foo.get_body()[0].target.id == '_py_backwards_a_0'
    assert foo.get_body()[1].target.id == 'c'


# Generated at 2022-06-14 02:52:56.167877
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def module_fn(x):
        let(x)
        x += 1

    assert snippet(module_fn).get_body() == [
        ast.Assign(targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
                   value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0',
                                                 ctx=ast.Load()),
                                   op=ast.Add(),
                                   right=ast.Num(n=1)))]



# Generated at 2022-06-14 02:53:00.309200
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import astor
    def _my():
        let(x)
        x += 1
        y = 1

    expected = """
        _py_backwards_x_0 += 1
        y = 1
    """
    assert astor.to_source(snippet(_my).get_body()) == expected



# Generated at 2022-06-14 02:53:04.796096
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x, y=1):
        z = x + y
        return z

    snippet_kwargs = {'x': ast.Name(id='str', ctx=ast.Load()),
                      'y': 1}
    tree = snippet(f).get_body(**snippet_kwargs)
    z = tree[0].value.args[0].n  # type: ignore
    assert z == 2

# Generated at 2022-06-14 02:53:15.034504
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2
    @snippet
    def func():
        let(x)
        x = a
        extend(vars)
        print(a, b)

# Generated at 2022-06-14 02:53:22.122816
# Unit test for function extend_tree
def test_extend_tree():

    def sample_fn(vars):
        extend(vars)
        print(x, y)

    ast_assign1 = ast.parse('x = 1')
    ast_assign2 = ast.parse('x = 2')
    ast_assign3 = ast.parse('x = 3')

    tree = ast.parse(get_source(sample_fn))
    extend_tree(tree, {'vars': [ast_assign1, ast_assign2, ast_assign3]})
    assert tree.body[0].body == [ast_assign1.body[0],
                                 ast_assign2.body[0],
                                 ast_assign3.body[0],
                                 ast.parse('print(x, y)').body[0]]

# Generated at 2022-06-14 02:53:27.835140
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('extend(vars)\ny = 1')
    vars = [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(1)),
            ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                       value=ast.Num(2))]
    extend_tree(tree, {'vars': vars})

# Generated at 2022-06-14 02:53:30.536940
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda: let(x) == 'x')().get_body() == [ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Str(s='x'))]

# Generated at 2022-06-14 02:53:36.517531
# Unit test for function extend_tree
def test_extend_tree():
    source = """
    extend(vars)
    print(foo)
    """
    tree = ast.parse(source)
    extend_tree(tree, {
        "vars": [
            ast.Assign(
                targets=[ast.Name(id='foo', ctx=ast.Store())],
                value=ast.Num(n=1)
            ),
            ast.Assign(
                targets=[ast.Name(id='foo', ctx=ast.Store())],
                value=ast.Num(n=2)
            )
        ]
    })
    result = astor.to_source(tree)
    expected = """
    foo = 1
    foo = 2
    print(foo)
    """
    assert result == expected

# Generated at 2022-06-14 02:53:44.442922
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("extend(globals)\nprint(y)")
    vars = [
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=1)
        ),
        ast.Assign(
            targets=[ast.Name(id='x', ctx=ast.Store())],
            value=ast.Num(n=2)
        )
    ]
    extend_tree(tree, {'globals': vars})

    # Assert tree after extending and transforming

# Generated at 2022-06-14 02:53:46.945258
# Unit test for function extend_tree
def test_extend_tree():
    """Test extend_tree function"""
    import astor

# Generated at 2022-06-14 02:54:00.018873
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
let(vars)
extend(vars)
""")  # type: ast.AST
    extend_tree(tree, {'vars': [ast.parse('x = 1').body[0]]})
    assert ast.dump(tree) == 'Module([Assign([Name(x, Store())], Num(1))])'

# Generated at 2022-06-14 02:54:00.486530
# Unit test for function extend_tree

# Generated at 2022-06-14 02:54:06.258087
# Unit test for function extend_tree
def test_extend_tree():
    source = '''
x = 1
extend(z)
y = 2
'''
    tree = ast.parse(source)
    extend_tree(tree, {'z': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                                       value=ast.Num(n=42))]})
    assert get_source(tree) == 'x = 1\nx = 42\ny = 2\n'



# Generated at 2022-06-14 02:54:14.248118
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    # Actual test
    import inspect
    @snippet
    def _snip():
        let(a)
        a += 1
        b = 1
        return a + b

# Generated at 2022-06-14 02:54:22.649540
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def snippet_get_body():
        let(x)
        x += 1
        y = None
        extend(vars)
    tree = snippet_get_body.get_body(
        vars=ast.parse('y = 1').body
    )
    assert '_py_backwards_x_0 += 1' == get_source(tree[0])
    assert 'y = 1' == get_source(tree[1])

# Generated at 2022-06-14 02:54:30.804824
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:54:40.929964
# Unit test for function extend_tree
def test_extend_tree():
    module = ast.parse("""
extend(vars)
print(x)
""")

# Generated at 2022-06-14 02:54:45.603574
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse('''
    x = 1
    extend(s)
    y = x
    ''')
    extend_tree(tree, {
        's': [ast.Assign(targets=[ast.Name(id='x', ctx=ast.Store())],
                              value=ast.Num(n=2))]
    })

    assert tree == ast.parse('''
    x = 1
    x = 2
    y = x
    ''')

# Generated at 2022-06-14 02:54:56.843526
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: let(x)).get_body() == []
    assert snippet(lambda x: let(x)).get_body(x=1) == []

    assert snippet(lambda x: let(x)).get_body(x=ast.Name(id='_py_backwards_x',
                                                         ctx=ast.Load())) == []

    assert snippet(lambda x: let(x) + x).get_body(x=1) == [
        ast.Expr(ast.BinOp(ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                           ast.Add(), ast.Num(1)))
    ]

    # test value

# Generated at 2022-06-14 02:55:03.849574
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    assert snippet(lambda x: let(x) or x).get_body() == [ast.Assign(
        targets=[ast.Name(id='_py_backwards_x_0', ctx=ast.Store())],
        value=ast.Name(id='x', ctx=ast.Load()))]
    assert snippet(lambda x: let(x) or x).get_body(x=ast.Name(id='y', ctx=ast.Load())) == [ast.Assign(
        targets=[ast.Name(id='_py_backwards_y_0', ctx=ast.Store())],
        value=ast.Name(id='y', ctx=ast.Load()))]

# Generated at 2022-06-14 02:55:15.599294
# Unit test for function extend_tree
def test_extend_tree():
    tree = ast.parse("""
extend(vars)
print(x)
""")
    extend_tree(tree, {'x': ast.Module([ast.Assign([ast.Name('x', ast.Store())], ast.Num(1))])})
    assert ast.dump(tree) == "<_ast.Module object at 0x0000022E2EBFC978>\n"



# Generated at 2022-06-14 02:55:24.949847
# Unit test for function extend_tree
def test_extend_tree():
    from .compatibility import Parser
    from .values import Number
    from .operators import Add, Sub

    source = """
    x = 1
    y = 2
    
    extend(vars)
    x = 3
    """

    tree = Parser.parse(source)
    body = tree.body
    var = body[0]
    
    variables = {
        'vars': [var],
    }
    
    extend_tree(tree, variables)
    vars = variables['vars']
    assert isinstance(vars[0].value, Number)
    assert vars[0].value.n == 1
    
    
    source = """
    x = 1
    y = 2
    
    extend(vars)
    x = x + 1
    """
    

# Generated at 2022-06-14 02:55:31.148214
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def func(x):
        let(y)
        y += 1
        z = 1

    snip = snippet(func)
    code = snip.get_body()
    assert len(code) == 2
    assert code[0].value.left.id == '_py_backwards_y_0'
    assert code[1].value.value == 1

# Generated at 2022-06-14 02:55:39.617494
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test_snippet(x: int) -> List[int]:
        let(y)
        z = 1
        return [x, y, z]

    snippet = snippet(test_snippet)
    body = snippet.get_body(x=1, y=2)
    assert len(body) == 3
    assert isinstance(body[0], ast.Assign)
    assert isinstance(body[1], ast.Assign)
    assert isinstance(body[2], ast.Return)
    assert isinstance(body[2].value, ast.List)
    assert len(body[2].value.elts) == 3



# Generated at 2022-06-14 02:55:47.244305
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    x = 5
    y = 10
    @snippet
    def fn():
        let(x)
        let(y)
        x = 1
        x += 1
        y = 1
        return x + y

    body = fn.get_body()
    assert len(body) == 4  # type: ignore
    assert isinstance(body[0], ast.Assign)  # type: ignore
    assert isinstance(body[1], ast.AugAssign)  # type: ignore
    assert isinstance(body[2], ast.Assign)  # type: ignore
    assert isinstance(body[3], ast.Return)  # type: ignore
    ret = body[3]
    assert isinstance(ret.value, ast.BinOp)  # type: ignore

# Generated at 2022-06-14 02:56:01.773223
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def my_snippet():
        a = 1
        b = 2
        let(c)
        extend(d)
        e = a + b + c + d

    snippet_ = snippet(my_snippet)

    tree = snippet_.get_body(c=3, d=4)


# Generated at 2022-06-14 02:56:09.742242
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet_source():
        extend(vars)
        print(x, y)

    x = ast.parse('x = 1').body[0]
    y = ast.parse('y = 2').body[0]
    vars = [x, y]
    ast_snippet = snippet(snippet_source)
    assert len(ast_snippet.get_body(x='x', y='y')) == 4
    assert ast_snippet.get_body(x='x', y='y') == ast.parse('x = 1\nx = 2\nprint(x, y)').body

# Generated at 2022-06-14 02:56:19.837151
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def foo(x: int = 1, y: str = 'y') -> None:
        let(x)
        x += 1
        y = 1

        extend(y)
        print(x, y)

    snippet_body = foo.get_body(x=2)


# Generated at 2022-06-14 02:56:29.797986
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def snippet():
        let(x)
        x += 1
        y = 1

    assert snippet.get_body(x=1, y=1) == [
        ast.AnnAssign(target=ast.Name(id='_py_backwards_x_0', ctx=ast.Store()),
                      annotation=None,
                      value=ast.BinOp(left=ast.Name(id='_py_backwards_x_0', ctx=ast.Load()),
                                      op=ast.Add(),
                                      right=ast.Num(n=1)),
                      simple=1),
        ast.Assign(targets=[ast.Name(id='_py_backwards_y_1', ctx=ast.Store())], value=ast.Num(n=1))
    ]

    def snippet():
        let

# Generated at 2022-06-14 02:56:33.449177
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .deep_ast import pretty_format
    @snippet
    def s(x: int, y: int) -> int:
        let(z)
        return x + y + z

    code = pretty_format(s.get_body(x=1, y=2))


    assert code == 'return 1 + 2 + _py_backwards_z_0'

# Generated at 2022-06-14 02:56:49.297842
# Unit test for function find_variables
def test_find_variables():
    source = "let('x')\nlet(y)\nz = 1"
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['x', 'y']



# Generated at 2022-06-14 02:56:56.069444
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    import random
    import typing
    import ast
    #import pytest
    #from pytest import raises

    def test_number():
        # one_number = snippet(lambda : 1)
        one_number = snippet(lambda: 1)
        assert eval(compile(ast.Module(body=one_number.get_body()),
                            filename='<ast>', mode='exec')) == 1

        @snippet
        def plus_one():
            return x + 1

        for _ in range(10):
            x = random.randint(0, 100)
            assert eval(compile(ast.Module(body=plus_one.get_body(x=x)),
                                filename='<ast>', mode='exec')) == x + 1

        x = 1

# Generated at 2022-06-14 02:57:02.017274
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snippet._GLOBAL_VARIABLES_GENERATOR = VariablesGenerator()

    @snippet
    def fn(x: ast.AST) -> None:
        let(x)
        x += 1

    kwargs = {'x': ast.Name(id='a', ctx=ast.Load())}
    body = fn.get_body(**kwargs)
    assert body == ast.parse('''
x_0 = a
x_0 += 1
    ''').body

    @snippet
    def fn(x: ast.AST) -> None:
        extend(x)
        print(x)

    kwargs = {'x': ast.parse('a = 1\nb = 2\n').body}
    body = fn.get_body(**kwargs)

# Generated at 2022-06-14 02:57:05.961651
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def add(x: int, y: int) -> int:
        let(x)
        return x + y

    ast_body = snippet(add).get_body(y=1)
    assert isinstance(ast_body, list)
    assert ast.dump(ast_body[0]) == "Expr(value=BinOp(left=Name('x', Load()), op=Add(), right=Num(n=1)))"



# Generated at 2022-06-14 02:57:17.450084
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f(x):
        let(y)
        let(z)
        z = x
        y += x
        return z

    snippet_f = snippet(f)
    d = snippet_f.get_body()
    assert len(d) == 4
    assert isinstance(d[1], ast.Assign)
    assert isinstance(d[1].value, ast.Name)
    assert d[1].value.id == 'x'
    assert isinstance(d[2], ast.AugAssign)
    assert isinstance(d[2].value, ast.Name)
    assert d[2].value.id == 'x'
    assert isinstance(d[3], ast.Return)
    assert isinstance(d[3].value, ast.Name)
    assert d[3].value.id == 'x'


# Generated at 2022-06-14 02:57:26.880301
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def x():
        let(x)
        x += 1
        y = (x + 1) / 2


# Generated at 2022-06-14 02:57:32.270184
# Unit test for function find_variables
def test_find_variables():
    source = '''
    foo = lambda x: let(y)
    if let(z) > 1:
        pass'''
    tree = ast.parse(source)
    assert list(find_variables(tree)) == ['y', 'z']



# Generated at 2022-06-14 02:57:44.237859
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def f_0():
        let(x)
        let(y)
        z = x * 2 + y * 2
        return z
    locals()['f_0'] = snippet(f_0)
    locals()['f_0_ref'] = f_0
    def f_1():
        let(x)
        let(y)
        extend(vars)
        return vars
    locals()['f_1'] = snippet(f_1)
    locals()['f_1_ref'] = f_1
    def f_2():
        let(x)
        z = x * 2 + y * 2
        return z
    locals()['f_2'] = snippet(f_2)
    locals()['f_2_ref'] = f_2
    def f_3():
        let(x)


# Generated at 2022-06-14 02:57:54.491908
# Unit test for method get_body of class snippet

# Generated at 2022-06-14 02:58:00.173711
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    snip = snippet(lambda x: print(x))
    assert snip.get_body(x=1)[0].value.args[0].n == 1
    assert snip.get_body(x=ast.Name(id='y'))[0].value.args[0].id == 'y'
    assert snip.get_body(x=ast.Name(id='y'))[0].value.args[0].id == 'y'



# Generated at 2022-06-14 02:58:36.387827
# Unit test for function extend_tree
def test_extend_tree():
    source_code = \
        """
        def x():
            extend(vars)
            y = 3

        """
    tree = ast.parse(source_code)
    vars = ast.parse("x = 1; x = 2").body

    extend_tree(tree, {"vars": vars})
    assert get_source(tree.body[0]) == \
        """def x():
    x = 1
    x = 2
    y = 3

"""

# Generated at 2022-06-14 02:58:42.738322
# Unit test for function extend_tree
def test_extend_tree():
    import astor
    tree = ast.parse('extend(assignments)\n')
    extend_tree(tree, {'assignments': [ast.parse('x = 1\nx = 2').body[0]]})
    assert astor.to_source(tree).strip() == 'x = 1\nx = 2\n'


# Generated at 2022-06-14 02:58:45.323148
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def fn(a, b):
        return a + b

    snippet_instance = snippet(fn)
    snippet_body = snippet_instance.get_body(var=let)
    assert snippet_body[0].value.id == '_py_backwards_var_0'

# Generated at 2022-06-14 02:58:55.203030
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x: int) -> int:
        """Docstring."""
        let(y)
        let(z)
        return x + y + z

    body = test.get_body(y=2, z=3)
    assert len(body) == 1
    assert isinstance(body[0], ast.Return)
    assert len(body[0].value.args) == 3
    assert isinstance(body[0].value.args[0], ast.Name)
    assert body[0].value.args[0].id == 'x'
    assert isinstance(body[0].value.args[1], ast.NameConstant)
    assert body[0].value.args[1].value == 2
    assert isinstance(body[0].value.args[2], ast.NameConstant)


# Generated at 2022-06-14 02:59:05.342339
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    a = 1
    b = 2

    def foo(x: int, y: int) -> int:
        let(x)
        let(y)
        return x + y


    snippet_ = snippet(foo)

# Generated at 2022-06-14 02:59:13.955967
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def test(x, y):
        let(a)
        let(b)
        let(c)

    snippet_body = test.get_body(x=1, y=3,
                                 a=ast.Constant(value=1, kind=None), b=2, c=2)
    assert snippet_body[0].value.id == '_py_backwards_a_0'
    assert snippet_body[1].value.id == '_py_backwards_b_0'
    assert snippet_body[2].value.id == '_py_backwards_c_0'

    @snippet
    def test(x):
        extend(c)


# Generated at 2022-06-14 02:59:22.415234
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    def test():
        let(x)
        y = 1
        x += 1

    snippet = Snippet(test)

# Generated at 2022-06-14 02:59:23.391394
# Unit test for function find_variables

# Generated at 2022-06-14 02:59:28.589359
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    @snippet
    def func(x: int, y: int, z: int) -> None:
        let(a)
        a += 1
        let(c)
        c = 2
        extend(d)
        for i in range(z):
            let(b)
            b = x + y

        return a + b

# Generated at 2022-06-14 02:59:38.977232
# Unit test for method get_body of class snippet
def test_snippet_get_body():
    from .tree import ast2py as ast2py
    from .tree import py2ast as py2ast

    def get_code(func: Callable[..., None]) -> str:
        source = get_source(func)
        source = source.strip()
        source = source.split('\n')
        return '\n'.join(line.strip() for line in source)

    def assert_equal(func: Callable[..., None],
                     compare_func: Callable[..., None]) -> None:
        assert get_code(snippet(func).get_body()) == get_code(compare_func)

    @snippet
    def test_simple():
        let(x)
        x = 1

    @snippet
    def test_simple_compare():
        x = 1

    assert_