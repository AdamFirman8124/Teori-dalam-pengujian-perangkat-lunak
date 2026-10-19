

# Generated at 2022-06-14 03:01:41.934789
# Unit test for function find
def test_find():
    # Setup fixture
    tree = ast.parse('def f(x): 1 + x')
    # Exercise + verify
    assert len(list(find(tree, int))) == 2
    assert len(list(find(tree, ast.Name))) == 3
    assert len(list(find(tree, ast.Add))) == 1
    assert len(list(find(tree, ast.FunctionDef))) == 1
    assert len(list(find(tree, ast.Module))) == 1
    assert len(list(find(tree, ast.Call))) == 0

# Generated at 2022-06-14 03:01:46.806977
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    fn_node = ast.parse("""def fn():
    a = 3
    b = 4""")
    fn_parent, fn_index = get_non_exp_parent_and_index(fn_node, fn_node.body[0].body[0])

    assert(isinstance(fn_parent, ast.Module))
    assert(fn_index == 0)



# Generated at 2022-06-14 03:01:50.984023
# Unit test for function get_parent
def test_get_parent():
    class Tk(ast.AST): pass
    class T(ast.AST): pass

    tk = Tk()
    t = T()
    tk.a = t

    assert get_parent(tk, t) == tk


# Generated at 2022-06-14 03:01:58.804750
# Unit test for function find
def test_find():
    val = ast.parse('''
        def f(x):
            return x * 2
    ''')  # type: ast.AST

    defs = list(find(val, ast.FunctionDef))
    assert len(defs) == 1
    assert defs[0].name == 'f'



# Generated at 2022-06-14 03:02:05.745016
# Unit test for function find
def test_find():
    # type: () -> None
    import unittest2 as unittest

    class FindTest(unittest.TestCase):
        def test_find(self):
            # type: () -> None
            tree = ast.parse("""\
            from a import b
            from c.d import e
            """)
            mods = list(find(tree, ast.ImportFrom))
            self.assertEqual(len(mods), 2)

    unittest.main(module=__name__, buffer=True)


if __name__ == "__main__":
    test_find()

# Generated at 2022-06-14 03:02:07.205524
# Unit test for function get_parent
def test_get_parent():
    import astor

# Generated at 2022-06-14 03:02:15.105212
# Unit test for function insert_at
def test_insert_at():
    parent = ast.Module([
        ast.Assign([ast.Name(id='a', ctx=ast.Store())], ast.Num(n=2)),
        ast.Assign([ast.Name(id='b', ctx=ast.Store())], ast.Num(n=3))
    ])

    insert_at(0, parent, ast.Assign([ast.Name(id='x', ctx=ast.Store())],
                         ast.Num(n=1)))


# Generated at 2022-06-14 03:02:20.385795
# Unit test for function insert_at
def test_insert_at():
    tree = ast.parse("print(1)")
    insert_at(0, tree, ast.Expr(value=ast.Num(1)))
    assert len(tree.body) == 2
    assert tree.body[0].value.n == 1  # type: ignore
    assert tree.body[1].value.n == 1  # type: ignore


# Generated at 2022-06-14 03:02:26.001669
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .gen import generate_function
    from .printer import print_ast
    from .fuzzer import Fuzzer

    # Test for a function
    tree = generate_function(
        'func_test', ['a'],
        [ast.With(
            context_expr=ast.Constant(value=None),
            optional_vars=None,
            body=[
                ast.Expr(
                    value=ast.Constant(
                        value=Fuzzer(
                            allow_none=True,
                            allow_int=True,
                            allow_float=True,
                            allow_bool=True,
                            allow_str=True,
                            allow_bytes=True,
                        ).generate()
                    ),
                ),
            ],
        )],
    )
    # Disallow tuple and list,

# Generated at 2022-06-14 03:02:39.203787
# Unit test for function get_parent
def test_get_parent():
    code = """
    def testfn(x):
        if x > 3:
            pass
    """
    module = ast.parse(code)
    _build_parents(module)
    assert isinstance(get_parent(module, module.body[0]), ast.Module)
    assert isinstance(get_parent(module, module.body[0].body[0]), ast.FunctionDef)
    assert isinstance(get_parent(module, module.body[0].body[0].body[0]), ast.If)
    assert isinstance(get_parent(module, module.body[0].body[0].body[0].body[0]), ast.If)

# Generated at 2022-06-14 03:02:56.629159
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class Node(ast.AST):
        def __init__(self, body):
            self.body = body

    import astor

    try:
        get_non_exp_parent_and_index(
            ast.Module([]),
            Node([
                ast.Expr(ast.Index(ast.Name('abc', ast.Load()), ast.Constant(1))),
                ast.Expr(ast.Index(ast.Name('abc', ast.Load()), ast.Constant(2))),
                ast.Expr(ast.Index(ast.Name('abc', ast.Load()), ast.Constant(3))),
            ])
        )
    except TypeError:
        print('Expected TypeError')
    except Exception:
        print('Wrong exception')
        import traceback
        traceback.print_exc()

# Generated at 2022-06-14 03:03:06.144182
# Unit test for function find
def test_find():
    class DummyNode(ast.AST):
        _fields = ()
    class DummyNode2(DummyNode):
        _fields = ()
    class DummyNode3(DummyNode2):
        pass

    node = DummyNode()
    node2 = DummyNode2()
    node3 = DummyNode3()

    node._parent_node = node2
    node2._parent_node = node3

    results = list(find(node3, DummyNode))
    assert results == [node, node2, node3]

# Generated at 2022-06-14 03:03:07.390464
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:03:12.183638
# Unit test for function get_parent
def test_get_parent():
    parent_node = ast.Module([ast.Import(names=[ast.alias(name='foo',
                                              asname='bar')])])
    child_node = parent_node.body[0]
    _build_parents(parent_node)

    assert get_parent(parent_node, child_node) == parent_node



# Generated at 2022-06-14 03:03:17.876282
# Unit test for function get_parent
def test_get_parent():
    class1 = ast.ClassDef(name='Foo',
                          body=[
                              ast.FunctionDef(name='on_enter',
                                              body=[ast.Pass()]),
                          ])

    class2 = ast.ClassDef(name='Bar', body=[class1])

    assert get_parent(ast.Module(body=[class2]), class2) == class2
    assert get_parent(ast.Module(body=[class2]), class1) == class2
    assert get_parent(ast.Module(body=[class2]), class1.body[0]) == class1

# Generated at 2022-06-14 03:03:23.449161
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Unit test for function get_closest_parent_of."""
    a = ast.parse('def f():\n  if True:\n    a = 3\n  else:\n    b = 3',
                  mode='eval')
    node = a.body[0].body[0].test
    parent = get_closest_parent_of(a, node, ast.If)
    assert isinstance(parent, ast.If)



# Generated at 2022-06-14 03:03:30.538042
# Unit test for function find
def test_find():
    import unittest
    import astor

    class TestFind(unittest.TestCase):

        def test_find(self):
            src = '''
                    def hi():
                        pass
                    '''
            tree = ast.parse(src)
            func_def = find(tree, ast.FunctionDef).__next__()
            self.assertEqual(func_def, find(tree, ast.FunctionDef).__next__())

        def test_find_func_def(self):
            src = '''
                    def hi():
                        pass
                    '''
            tree = ast.parse(src)
            func_def = ast.parse('def hi(): pass').body[0]

# Generated at 2022-06-14 03:03:35.699007
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = """
    def func(a, b):
        return a + b
    """

    tree = ast.parse(code)  # type: ignore
    Add = ast.add

    non_exp_parent, index = get_non_exp_parent_and_index(tree, Add.left)

    assert non_exp_parent.__class__.__name__ == 'FunctionDef'
    assert index == 0

# Generated at 2022-06-14 03:03:39.165777
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = """
        def foo():
            pass
    """
    tree = ast.parse(code)
    func = tree.body[0]
    parent, index = get_non_exp_parent_and_index(tree, func)
    assert (parent, index) == (tree, 0)



# Generated at 2022-06-14 03:03:44.806176
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import typed_ast.ast3 as ast
    code = "class A(B, C): pass"
    node = ast.parse(code).body[0]

    # Should return ClassDef for any node
    for subnode in ast.walk(node):
        result = get_closest_parent_of(node, subnode, ast.ClassDef)
        assert isinstance(result, ast.ClassDef)



# Generated at 2022-06-14 03:03:59.893445
# Unit test for function get_parent
def test_get_parent():
    class DummyNode(ast.AST):
        pass

    class DummyExp(ast.Expression):
        pass

    class DummyStmt(ast.Statement):
        pass

    tree = DummyExp()
    node = DummyNode()
    stmt = DummyStmt()

    tree.body = node
    node.body = stmt

    assert get_parent(tree, node) == tree
    assert get_parent(tree, stmt) == node

# Generated at 2022-06-14 03:04:11.457831
# Unit test for function replace_at
def test_replace_at():
    import unittest

    class TestReplaceAt(unittest.TestCase):
        def test_replace_at(self):
            from ..parser import parse

            tree = parse('''
            def f():
                pass
            ''')

            # editing the tree to be:
            # def f():
            #     pass
            # def g():
            #     pass

            def_stmt: ast.FunctionDef = next(find(tree, ast.FunctionDef))
            parent_stmt, index = get_non_exp_parent_and_index(tree, def_stmt)

# Generated at 2022-06-14 03:04:19.014109
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse('a = 1; b = 2; c = 3; d = 4;')
    assign_node = tree.body[3]
    parent, index = get_non_exp_parent_and_index(tree, assign_node)

    assert assign_node == parent.body[index]
    assign_node_2 = ast.parse('e = 5;').body[0]
    replace_at(index, parent, assign_node_2)
    assert assign_node_2 == parent.body[index]

# Generated at 2022-06-14 03:04:31.658227
# Unit test for function replace_at
def test_replace_at():
    class A:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class B:
        def __init__(self, b, c):
            self.b = b
            self.c = c

    class C:
        def __init__(self, d):
            self.d = d

    a = A(1, 2)
    b = B('b', 4)
    c = C('c')

    a.b = b
    b.c = c

    replace_at(0, b, a)
    print(c.d)

# Generated at 2022-06-14 03:04:34.594136
# Unit test for function find
def test_find():
    assert list(find(ast.parse('(1+1)'), ast.BinOp)) == [ast.parse('(1+1)').body[0].value.left]


# Generated at 2022-06-14 03:04:40.414788
# Unit test for function find
def test_find():
    from typed_ast import ast3
    test = ast3.parse("a = b")
    result = list(find(test, ast3.Name))
    assert len(result) == 2
    assert isinstance(result[0], ast3.Name)
    assert isinstance(result[1], ast3.Name)

# Generated at 2022-06-14 03:04:44.975367
# Unit test for function find
def test_find():
    node = ast.parse("def f():\n  pass")
    f = get_closest_parent_of(node, node.body[0].body[0], ast.FunctionDef)
    assert f.name == "f"
    assert f.lineno == 1
    assert f.col_offset == 4
    assert f.body is not None
    assert f.args is not None
    assert f.decorator_list is not None
    assert f.body[0] is node.body[0].body[0]

# Generated at 2022-06-14 03:04:50.621789
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(
        ast.parse('1'), ast.parse('1'), ast.Module).body[0] == 1
    assert get_closest_parent_of(
        ast.parse('1'), ast.parse('1+2'), ast.Module).body[0].value.left == 1



# Generated at 2022-06-14 03:04:55.045571
# Unit test for function find
def test_find():
    """Test function find."""
    tree = ast.parse(
        '''
        def testme(a):
            return a + 2 + a
        ''')
    assert [node.name for node in find(tree, ast.Name)] == ['testme', 'a', 'a']
    assert [node.name for node in find(tree, ast.Add)] == ['+', '+']

# Generated at 2022-06-14 03:04:59.520547
# Unit test for function find
def test_find():
    if __name__ == '__main__':
        from .test_tree_builder import test_func_one

        tree = test_func_one()
        assert len(list(find(tree, ast.FunctionDef))) == 1
        assert len(list(find(tree, ast.While))) == 1



# Generated at 2022-06-14 03:05:17.546843
# Unit test for function find
def test_find():
    module = ast.parse('''
        def foo(a, b):
            pass
    ''')

    f = module.body[0]  # type: ignore

    assert list(find(module, ast.Module)) == [module]
    assert list(find(module, ast.FunctionDef)) == [f]
    assert list(find(module, ast.arguments)) == [f.args]
    assert list(find(module, ast.Name)) == [f.name]


# Generated at 2022-06-14 03:05:20.098578
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.parse('a + b').body[0].value

    parent, index = get_non_exp_parent_and_index(ast.parse('a + b'), node)

    assert index == 0
    assert isinstance(parent, ast.Module)

# Generated at 2022-06-14 03:05:22.917344
# Unit test for function get_parent
def test_get_parent():
    """Test get_parent function."""
    assert get_parent(ast.parse('a.b.c.d'), ast.parse('a.b.c.d').body[0]) == \
           ast.parse('a.b.c.d')

# Generated at 2022-06-14 03:05:24.715544
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:05:26.184667
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:30.352561
# Unit test for function get_parent
def test_get_parent():
    node = ast.parse('if False: print(5)')
    node = list(node.body)[0]
    
    assert get_parent(ast.parse('1 + 2'), node)
    assert isinstance(get_parent(ast.parse('1 + 2'), node), ast.Module)
    

# Generated at 2022-06-14 03:05:40.739342
# Unit test for function replace_at
def test_replace_at():
    '''
    >>> import typed_ast.ast3 as ast
    >>> from ast_transformer.ast_tools import replace_at
    >>> '''

# Generated at 2022-06-14 03:05:44.307989
# Unit test for function find
def test_find():
    tree = ast.parse("""
    print('Hello World!')
    print(1)
    print(2)
    """)

    print = find(tree, ast.Print).__next__()
    asserts = find(tree, ast.Assert).__next__()  # type: ignore

# Generated at 2022-06-14 03:05:48.043112
# Unit test for function find
def test_find():
    find_test = ast.parse('import find_test\n'
                          'import find_test2\n'
                          'from find_test3 import find_test4')

    assert list(find(find_test, ast.Import)) == find_test.body[:2]
    assert list(find(find_test, ast.ImportFrom)) == [find_test.body[2]]

# Generated at 2022-06-14 03:05:57.337259
# Unit test for function replace_at
def test_replace_at():
    # Note: in this function, we use only body of statements,
    # and this makes the test a little bit dirty
    tree = ast.parse("""
for i in range(10):
    a = 0
    while True:
        a += 1
    a += 1
    """)
    parser_stmts = tree.body
    while_node = parser_stmts[0].body[1]
    if_node = ast.If(test=ast.Name(id="a", ctx=ast.Load()), body=[], orelse=[])
    replace_at(1, parser_stmts[0], if_node)
    assgn_node = ast.Assign(targets=[ast.Name(id="b", ctx=ast.Store())],
                            value=ast.Num(n=1))


# Generated at 2022-06-14 03:06:16.577284
# Unit test for function get_parent
def test_get_parent():
    # Arrange
    tree = ast.parse("""
        for i in range(10):
            for i in [0, 1]:
                print('i=', i)""")

    # Act
    res = get_parent(tree, tree.body[0])

    # Assert
    assert isinstance(res, ast.Module)
    assert res == _parents[tree.body[0]]



# Generated at 2022-06-14 03:06:21.410483
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    node = ast.parse('a + b')
    tree = ast.parse('a + b')
    # parent = node
    # index = 0
    assert get_non_exp_parent_and_index(tree, node) == (tree, 0)

# Generated at 2022-06-14 03:06:31.017214
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("def foo(x):\n    pass")
    f = tree.body[0]
    assert f == get_non_exp_parent_and_index(tree, f)[0]
    assert 0 == get_non_exp_parent_and_index(tree, f)[1]
    assert f == get_non_exp_parent_and_index(tree, f.args)[0]
    assert 0 == get_non_exp_parent_and_index(tree, f.args)[1]
    assert f.body == get_non_exp_parent_and_index(tree, f.body[0])[0]
    assert 0 == get_non_exp_parent_and_index(tree, f.body[0])[1]

# Generated at 2022-06-14 03:06:39.679309
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    parent = ast.For(target=ast.Name(id='x'),
                     iter=ast.Call(func=ast.Name(id='range'),
                                   args=(ast.Num(n=10),),
                                   keywords=[]),
                     body=[
                         ast.If(test=ast.Compare(left=ast.Name(id='x'),
                                                 ops=[ast.Eq()],
                                                 comparators=[ast.Num(n=10)]),
                                body=[ast.Expr(value=ast.Str(s='x == 10')),
                                      ast.Expr(value=ast.Num(n=1))])],
                     orelse=[])
    assert get_non_exp_parent_and_index(parent, parent.body[0].body[0]) == (
        parent.body[0], 0)

# Generated at 2022-06-14 03:06:44.081211
# Unit test for function find
def test_find():
    source = """
    def foo(arg):
        print("{}")
        if arg:
            pass
        return None
    """
    tree = ast.parse(source)
    assert len(list(find(tree, ast.Name))) == 3



# Generated at 2022-06-14 03:06:53.980021
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse(
        """from a import f,g
a = f(g(9))
"""
    )
    _build_parents(tree)
    for node in tree.body:
        parent = get_parent(tree, node)
        assert parent == tree
    for node in tree.body[0].body:
        parent = get_parent(tree, node)
        assert parent == tree.body[0]
    for node in tree.body[1].targets:
        parent = get_parent(tree, node)
        assert parent == tree.body[1]
    for node in tree.body[1].value.args:
        parent = get_parent(tree, node)
        assert parent == tree.body[1].value

# Generated at 2022-06-14 03:06:59.702463
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from .test_parser import to_expr
    test_expr = to_expr("""
        def f(x, y):
            return x + y
    """)
    func = test_expr.body[0]
    expr = func.body[0]
    assert get_non_exp_parent_and_index(test_expr, expr) == (func, 0)

# Generated at 2022-06-14 03:07:06.925720
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    from ..parser import nim as nim_ast_gen

    test_code = """
    proc testFunc() =
        var x = 4
        var y = 3
        var z = 5

        if a == 1:
            while b == 1:
                a = c
                var bool = false
        else:
            1
    """
    test_ast = nim_ast_gen.parse_string(test_code)

    assert get_closest_parent_of(test_ast, test_ast.body[0].body[1], ast.Module) == test_ast
    assert get_closest_parent_of(test_ast, test_ast.body[0].body[3], ast.Module) == test_ast

# Generated at 2022-06-14 03:07:15.187892
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    source_code = """
    def func(a, b):
        a + b
    """
    tree = ast.parse(source_code)

    closest_function_def_parent = get_closest_parent_of(tree, tree.body[0].body[0], ast.FunctionDef)
    assert astor.to_source(closest_function_def_parent) == (
        "def func(a, b):\n"
        "    a + b"
    )

    closest_module_parent = get_closest_parent_of(tree, tree.body[0].body[0], ast.Module)

# Generated at 2022-06-14 03:07:22.527993
# Unit test for function replace_at
def test_replace_at():
    """test_replace_at() -> None

    Test of function replace_at.
    """

    from typed_ast.ast3 import (Expr, FunctionDef, Module, Load, Num,
                                Assign, Name, Tuple, Dict, Attribute)
    from ...utils import print_ast
    from ...exceptions import TransformError

    code = "def f(a, b): pass"

    mod = Module([FunctionDef("f", [FunctionDef.arg("b", None),
                                     FunctionDef.arg("a", None, [])],
                              [Expr(Tuple([Load(), Name("b", Load())],
                                         Load()))],
                              [], None, None)])

    print_ast(mod)
    print()

    mod_body = mod.body

    # Test if exception is raised if nothing to remove