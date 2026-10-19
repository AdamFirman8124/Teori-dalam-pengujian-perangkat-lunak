

# Generated at 2022-06-14 03:01:33.101265
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    pass

# Generated at 2022-06-14 03:01:38.673941
# Unit test for function find
def test_find():
    node = ast.parse('a = some()\nprint(a)')

    for param in find(node, ast.Expr):
        pass
    else:
        raise AssertionError('Found no nodes')



# Generated at 2022-06-14 03:01:43.105515
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("""
foo()
""")
    non_exp_parent, index = get_non_exp_parent_and_index(tree, tree.body[0])
    assert index == 0
    assert isinstance(non_exp_parent, ast.Module)
    assert non_exp_parent.body[index] == tree.body[0]


# Generated at 2022-06-14 03:01:47.986208
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('1 + 1')
    assert get_non_exp_parent_and_index(tree, tree.body[0].value) == \
           (tree.body[0], 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].value.left) == \
           (tree.body[0].value, 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].value.right) == \
           (tree.body[0].value, 1)

# Generated at 2022-06-14 03:01:51.745528
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = astor.parse_file("fixtures/get_non_exp_parent_and_index.py")
    func_def = list(find(tree, ast.FunctionDef))[0]
    for i, node in enumerate(func_def.body):
        assert get_non_exp_parent_and_index(tree, node) == (func_def, i)

# Generated at 2022-06-14 03:02:02.410333
# Unit test for function replace_at
def test_replace_at():
    import astunparse
    import inspect
    import pdb
    import re

    # Define ast to sample
    sample_ast = ast.parse("""
    def sample():
        if True:
            x = 1

    pdb.set_trace()

    """, mode='exec')

    # Find the first call
    call = sample_ast.body[1].value

    # Define replacement for call
    replacement = ast.parse("""
    if True:
        print("foo")
    print("bar")
    """, mode='exec')

    # Find the first function node
    function = sample_ast.body[0]

    # Find pdb call inside function
    for child in function.body:
        if isinstance(child, ast.Expr) and isinstance(child.value, ast.Call):
            pdb_

# Generated at 2022-06-14 03:02:11.865890
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest

    class TestCase(unittest.TestCase):
        def test(self):
            from ..context import find_context
            from ..ctx_analysis import analyze
            from .utils import str_ast
            from .gen import gen_block
            from astor.code_gen import to_source

            tree = ast.parse('[x for x in iterable]')
            context = find_context(tree, (2, 0))
            gen_block(tree, context)
            assert to_source(tree) == '[x for x in iterable if x]'

            tree = ast.parse('a[b]')
            context = find_context(tree, (0, 2))
            gen_block(tree, context)
            assert to_source(tree) == 'None'


# Generated at 2022-06-14 03:02:12.799467
# Unit test for function replace_at

# Generated at 2022-06-14 03:02:21.068324
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    def test():
        a = 1 + 1
        b = a + 2

    module = ast.parse(inspect.getsource(test))
    _build_parents(module)
    a = module.body[0].body[0].value
    parent, index = get_non_exp_parent_and_index(module, a)
    assert parent is module.body[0]
    assert index == 0

    b = module.body[0].body[1].value
    parent, index = get_non_exp_parent_and_index(module, b)
    assert parent is module.body[0]
    assert index == 1

# Generated at 2022-06-14 03:02:26.307163
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node1 = ast.If (
        test = ast.Name(id = 'a'),
        body = [ast.BoolOp(op = ast.And(), values = [ast.Name(id = 'b'), ast.Name(id = 'c')])],
        orelse = [ast.BoolOp(op = ast.And(), values = [ast.Name(id = 'd'), ast.Name(id = 'e')])]
    )
    node2 = ast.And()
    node3 = ast.Name(id = 'a')
    node4 = ast.Name(id = 'd')

    assert(get_closest_parent_of(node1, node2, ast.BoolOp) == node1.body[0])

# Generated at 2022-06-14 03:02:31.790546
# Unit test for function find
def test_find():
    comp = ast.parse('x = 1 + 2')
    num2 = find(comp, ast.Num).__next__().n
    assert num2 == 2



# Generated at 2022-06-14 03:02:42.749175
# Unit test for function find
def test_find():
    import astor

    class ModuleVisitor(ast.NodeVisitor):
        def visit_Expr(self, node):
            print("Found expression:", astor.to_source(node))

    class ExprTransformer(ast.NodeTransformer):
        def visit_Expr(self, node):
            return ast.parse("result = 'OK'").body[0].value

    code = "1 + 1\n"
    tree = ast.parse(code)
    visitor = ModuleVisitor()
    visitor.visit(tree)

    transformer = ExprTransformer()
    new_tree = transformer.visit(tree)
    print("Transformed code:")
    print(astor.to_source(new_tree))



# Generated at 2022-06-14 03:02:46.837979
# Unit test for function find
def test_find():
    tree = ast.parse('#do something\n1 + 1\n[1,2,3]')
    print(find(tree, ast.Lambda))

# Generated at 2022-06-14 03:02:58.732497
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    def nested_function(arg: int) -> int:
        return arg + 1

    tree = ast.parse(inspect.getsource(nested_function))

    closestCallParent = get_closest_parent_of(tree, tree.body[0].body[0],
                                              ast.Call)
    assert isinstance(closestCallParent, ast.Call)

    closestMethodParent = get_closest_parent_of(tree, tree.body[0].body[0],
                                                ast.FunctionDef)
    assert isinstance(closestMethodParent, ast.FunctionDef)

    closestModuleParent = get_closest_parent_of(tree, tree.body[0].body[0],
                                                ast.Module)
    assert isinstance(closestModuleParent, ast.Module)



# Generated at 2022-06-14 03:03:01.605770
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse(
        '''
        def test():
            assert True
        test()
        '''
    )
    test_node = tree.body[0].body[0].value.left
    assert isinstance(get_closest_parent_of(tree, test_node, ast.FunctionDef),
                      ast.FunctionDef)

# Generated at 2022-06-14 03:03:07.206433
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    class TestParent(ast.AST):
        _fields = ('body',)
    test_node = ast.Assign()
    test_parent = TestParent(body=[test_node])
    assert(get_closest_parent_of(test_parent, test_node, TestParent) == test_parent)

# Generated at 2022-06-14 03:03:07.859744
# Unit test for function insert_at
def test_insert_at():
    pass

# Generated at 2022-06-14 03:03:10.859001
# Unit test for function find
def test_find():
    for node in find(ast.parse('''
        def foo(x):
            return x
    '''), ast.FunctionDef):
        print(node)



# Generated at 2022-06-14 03:03:15.245375
# Unit test for function find
def test_find():
    node_type = ast.Call
    tree = ast.parse('call_func(1, 2)')

    node = next(find(tree, node_type))
    assert isinstance(node, node_type)

    assert next(find(ast.parse('call_func(1, 2)'), node_type)).func.id == 'call_func'


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:03:22.046772
# Unit test for function find
def test_find():
    import unittest

    class TestFind(unittest.TestCase):
        def test_empty_list(self):
            tree = ast.parse('1')
            self.assertEqual(list(find(tree, ast.List)), [])

        def test_find_list(self):
            tree = ast.parse('[1, 2, 3]')
            self.assertTrue(isinstance(find(tree, ast.List).__next__(),
                                       ast.List))

    unittest.main()


# Generated at 2022-06-14 03:03:37.516494
# Unit test for function replace_at
def test_replace_at():
    module = ast.parse("""
x = 1
y = 2
z = 3
""")
    assign = module.body[1]
    new_assign = ast.Assign([ast.Name(id='a', ctx=ast.Store())],
                            ast.Num(n=1))
    assert module.body[1] == assign
    replace_at(1, module, new_assign)
    assert new_assign == module.body[1]

# Generated at 2022-06-14 03:03:41.971424
# Unit test for function find
def test_find():
    source = '''
        a = 1
        b = 2
    '''
    tree = ast.parse(source)
    list(find(tree, ast.Assign))
    assert len(list(find(tree, ast.Assign))) == 2


# Generated at 2022-06-14 03:03:50.236486
# Unit test for function replace_at
def test_replace_at():
    module = ast.parse("""
    def foo():
        def bar():
            def baz():
                pass
                pass
            pass

        pass
        pass
    """)

    # Find the node to replace
    node_to_replace = find(module, ast.FunctionDef).next()
    body = node_to_replace.body

    # Replace the node with two pass statements
    replace_at(0, node_to_replace, [ast.Pass(), ast.Pass()])

    assert len(body) == 2
    assert isinstance(body[0], ast.Pass)
    assert isinstance(body[1], ast.Pass)

# Generated at 2022-06-14 03:03:52.266439
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..migrations import RemoveLinesMigration


# Generated at 2022-06-14 03:03:59.967857
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .utils import create_ast_module
    
    module_ast = create_ast_module("""
        def function(a,b,c):
            a = 1
            b = 2
            c = 3
            return a + b + c
    
        def second_function():
            d = 4
            return d
    """)
    
    body_of_function = get_closest_parent_of(module_ast, module_ast.body[0].body[0], ast.FunctionDef)
    
    assert body_of_function is module_ast.body[0]
    assert isinstance(body_of_function, ast.FunctionDef)

# Generated at 2022-06-14 03:04:03.682403
# Unit test for function get_parent
def test_get_parent():
    """
    >>> module = ast.parse('a + b + 5')
    >>> get_parent(module, module.body[0].value.left) == module
    True
    """
    pass

# Generated at 2022-06-14 03:04:13.874689
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Function with a normal body
    fun = ast.FunctionDef(name='fun', args=ast.arguments(
        posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[],
        kwarg=None, defaults=[]), body=[ast.Expr(value=ast.NameConstant(value=None)),
                                        ast.Expr(value=ast.NameConstant(value=None)),
                                        ast.Expr(value=ast.NameConstant(value=None))],
                            decorator_list=[], returns=None)
    # Module with the function
    mod = ast.Module(body=[fun])
    # Strategy tree

# Generated at 2022-06-14 03:04:15.225591
# Unit test for function get_parent
def test_get_parent():
    parent_node = ast.parse('\nfoo()')
    child_node = ast.parse('foo')
    _build_parents(parent_node)
    assert (get_parent(parent_node, child_node) == parent_node)

# Generated at 2022-06-14 03:04:17.753751
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    global _parents

    _parents = WeakKeyDictionary()
    tree = ast.parse('3 + 4 + 5', mode='eval')

    assert isinstance(get_closest_parent_of(tree, tree.body, ast.Expression),
                      ast.Expression)

# Generated at 2022-06-14 03:04:24.332338
# Unit test for function replace_at
def test_replace_at():
    def fn(x):
        while True:
            yield x

    tree = ast.parse('def fn(x):\n    while True:\n        yield x',
                     '<test file>', 'exec')
    parent = tree.body[0]
    parent = parent.body[0]
    child = parent.body[0]

    parent = get_parent(tree, child)
    assert parent is not None

    replace_at(0, parent, tree.body[0].body[0].body)



# Generated at 2022-06-14 03:04:39.101487
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    test_tree = ast.parse('''
if True:
    def bar():
        pass
    def foo():
        pass
    def baz():
        pass
    def spam():
        pass
''')
    spam = test_tree.body[0].body[3]
    spam_func_def = get_closest_parent_of(test_tree, spam, ast.FunctionDef)
    assert spam_func_def.name == 'spam'
    assert spam_func_def.body[0].value.s == 'pass'



# Generated at 2022-06-14 03:04:46.273662
# Unit test for function find
def test_find():
    from ..examples import import_as_example
    from ..transforms.importtransformers import CommaImportTransformer

    example_tree = import_as_example()

    for node in CommaImportTransformer().find_candidates(example_tree):
        print(node)

    assert 1 == 2


# Generated at 2022-06-14 03:04:53.649614
# Unit test for function find
def test_find():
    """Test for find."""
    code = 'a + b'
    tree = ast.parse(code)
    add_nodes = list(find(tree, ast.Add))
    assert len(add_nodes) == 1
    assert code == ast.dump(add_nodes[0])

# Generated at 2022-06-14 03:05:03.977645
# Unit test for function find
def test_find():
    node_to_find = ast.Name(id='foo', ctx=ast.Load())
    some_node = ast.Expr(value=node_to_find)

    tree = ast.parse('''
    def foo():
        bar = 10
        baz = "qwerty"
        print(bar, baz)
    ''')

    assert list(find(tree, ast.Name)) == [ast.Name(id='foo', ctx=ast.Load()),
                                          ast.Name(id='bar', ctx=ast.Store()),
                                          ast.Name(id='baz', ctx=ast.Store()),
                                          ast.Name(id='print', ctx=ast.Load())]


# Generated at 2022-06-14 03:05:10.764701
# Unit test for function find
def test_find():
    import subprocess
    ast_module = ast.parse(open(__file__).read())
    ast_tree = ast_module.body[0]
    if list(find(ast_tree, ast.FunctionDef)) != [ast_tree]:
        subprocess.call(['nosetests', '--with-coverage', '--cover-erase',
                         '--cover-package=unitizer', __file__])
        print("Ran 1 test in 0.000s")
        print("\nOK")
        exit(0)
    else:
        subprocess.call(['nosetests', '--with-coverage', '--cover-erase',
                         '--cover-package=unitizer', __file__])
        exit(1)

# Generated at 2022-06-14 03:05:16.925795
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..rewriter import Rewriter
    from .examples import simple_ast_modules

    for mod in simple_ast_modules:
        for stmt in find(mod, ast.Expr):
            r = Rewriter(mod)
            r.replace(stmt, ast.Name(id='asd', ctx=ast.Load()))


if __name__ == '__main__':
    test_get_closest_parent_of()

# Generated at 2022-06-14 03:05:19.587813
# Unit test for function find
def test_find():
    src = '''
    a = 1
    b = 2

    def foo():
        pass
    '''

    tree = ast.parse(src)
    result = find(tree, ast.stmt)
    assert len(list(result)) == 4



# Generated at 2022-06-14 03:05:22.852533
# Unit test for function get_parent
def test_get_parent():
    name = ast.Name(id='foo', ctx=ast.Store())
    node = ast.Assign(targets=[name], value=ast.Num(n=42))
    assert(get_parent(node, name) is node)



# Generated at 2022-06-14 03:05:28.251580
# Unit test for function find
def test_find():
    tree = ast.parse('a + b')
    assert list(find(tree, ast.Name)) == [ast.Name(id='a', ctx=ast.Load()), ast.Name(id='b', ctx=ast.Load())]
    assert list(find(tree, ast.Num)) == []


# Generated at 2022-06-14 03:05:33.833839
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .base import convert
    code = '''
(1, 2)
'''
    tree = ast.parse(code)
    _build_parents(tree)
    try:
        node = tree.body[0].value
        parent = get_closest_parent_of(tree, node, ast.Expr)
        assert parent == tree.body[0]
    except NodeNotFound:
        assert False

# Generated at 2022-06-14 03:06:10.312237
# Unit test for function find
def test_find():
    pass



# Generated at 2022-06-14 03:06:19.876170
# Unit test for function find
def test_find():
    class N(ast.AST):
        pass

    class T(ast.AST):
        pass

    class K(ast.AST):
        pass

    class E(ast.AST):
        pass

    class R(ast.AST):
        pass

    class A(ast.AST):
        pass

    class S(ast.AST):
        pass


# Generated at 2022-06-14 03:06:24.946500
# Unit test for function find
def test_find():
    tree = ast.parse("class Test:\n x = 1")
    res = {n.name for n in find(tree, ast.Name)}
    assert res == {'Test'}


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:06:33.960209
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..printers import print_ast
    import ast
    import astor

    print_ast(ast.parse('''
    def f(a, b, c):
        if a == b:
            c = a + b
        else:
            c = a - b
        d = c + 4
        return d
    '''))


# Generated at 2022-06-14 03:06:39.238492
# Unit test for function get_parent
def test_get_parent():
    source = """
    a = 1
    """
    tree = ast.parse(source)
    _build_parents(tree)
    print(get_parent(tree, tree.body[0]))

if __name__ == "__main__":
    test_get_parent()

# Generated at 2022-06-14 03:06:47.915371
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node_ast = ast.parse('''
    def test():
        x = 1
    def test1():
        if x == 1:
            y = 2
            x = 3
    ''')
    node = find(node_ast, ast.Name).__next__()
    assert get_closest_parent_of(node_ast, node, ast.FunctionDef).name == 'test'
    assert get_closest_parent_of(node_ast, node, ast.Module).body[1].body[1].value.right.n==3

# Generated at 2022-06-14 03:06:57.061850
# Unit test for function find
def test_find():
    class Test(ast.AST):
        _fields = ('name', 'args')
        _attributes = ('arg', 'kwarg')

    class Test2(Test):
        pass

    class Test3(ast.AST):
        pass

    class Test4(ast.AST):
        pass

    class Test5(Test4):
        pass

    test = Test(name='test', args=[Test4()])
    test2 = Test2(name='test2', args=[Test4()])
    test.arg = Test2(name='test', args=[Test2(name='dir')])
    test.kwarg = Test()

    tree = Test3(Test3(body=[test, Test3(body=[test2])]), Test3(Test3(Test3())))

    found = list(find(tree, Test))

# Generated at 2022-06-14 03:07:05.144358
# Unit test for function find
def test_find():
    tree = ast.parse(
        "def Foo():\n"
        "    print 'Foo'\n"
        "    print 'Foo2'\n"
        "    def Bar():\n"
        "        print 'Bar'\n"
        "        print 'Bar2'\n"
        "        def Baz():\n"
        "            print 'Baz'\n"
        "            print 'Baz2'\n"
        "            def Qaz():\n"
        "                print 'Qaz'\n"
        "                print 'Qaz2'\n"
        "                print 'Qaz3'\n"
    )

    _build_parents(tree)

    functions = find(tree, ast.FunctionDef)
    assert len(functions) == 4


# Generated at 2022-06-14 03:07:14.365788
# Unit test for function get_parent
def test_get_parent():
    # Check if parent could be found.
    fi = ast.parse("if x:\n\tprint(x)")
    assert isinstance(get_parent(fi, fi.body[0]), ast.Module)
    assert isinstance(get_parent(fi, fi.body[0].test), ast.If)
    assert isinstance(get_parent(fi, fi.body[0].test.left), ast.Compare)
    assert isinstance(get_parent(fi, fi.body[0].test.left.left), ast.Name)

    # Check if parent could not be found.
    assert isinstance(get_parent(fi, fi), ast.Module), "Root of AST is the parent"

# Generated at 2022-06-14 03:07:17.600954
# Unit test for function find
def test_find():
    class Test:
        pass
    t = Test()
    t.x = 1
    t.y = 2
    find(t, int)


# Generated at 2022-06-14 03:08:00.482012
# Unit test for function get_parent
def test_get_parent():
    T = ast.body[0].body[0].body[0]
    assert get_parent(ast.Module, T) == ast.body[0].body[0]
    assert get_parent(ast.Module, ast.Module) is None


# Generated at 2022-06-14 03:08:07.161668
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node_1 = ast.Lambda(arguments=ast.arguments(args=[ast.Name(id='x', ctx=ast.Load()),
                                                       ast.Name(id='m', ctx=ast.Load())],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kwarg=None,
                                                defaults=[],
                                                kw_defaults=[]),
                        body=ast.Assign(targets=[ast.Name(id='y', ctx=ast.Store())],
                                        value=ast.Name(id='x', ctx=ast.Load())))

# Generated at 2022-06-14 03:08:13.707967
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import ast
    import astor
    ast_tree = ast.parse("""for i in range(3):
    print(i)""")
    print('\ninput:\n\n', astor.dump(ast_tree))
    node = get_closest_parent_of(ast_tree, ast_tree.body[0].body[0], ast.For)
    assert node.iter.func.id == 'range'


# Generated at 2022-06-14 03:08:17.894750
# Unit test for function find
def test_find():
    tree = ast.parse("""
if True:
    x = 5
    if True:
        y = 6
""")
    assert list(find(tree, ast.If)) == [tree.body[0], tree.body[0].body[1]]

# Generated at 2022-06-14 03:08:18.782846
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:08:23.074976
# Unit test for function find
def test_find():
    node = ast.parse('a = 1\n')
    objects = list(find(node, ast.Name))
    assert len(objects) == 1
    assert objects[0].id == 'a'


# Generated at 2022-06-14 03:08:25.681455
# Unit test for function find
def test_find():
    find(ast.parse('a = 1\na = 2').body[0], ast.Assign)



# Generated at 2022-06-14 03:08:40.474862
# Unit test for function get_parent
def test_get_parent():

    node1a = ast.Compare(
        left=ast.Num(n=1),
        ops=[ast.Gt()],
        comparators=[ast.Num(n=2)],
    )
    node1b = ast.Compare(
        left=node1a,
        ops=[ast.Eq()],
        comparators=[ast.Num(n=2)],
    )

    node2a = ast.BinOp(
        left=ast.Num(n=1),
        op=ast.Add(),
        right=ast.Num(n=2)
    )
    node2b = ast.BinOp(
        left=node2a,
        op=ast.Sub(),
        right=ast.Num(n=1),
    )


# Generated at 2022-06-14 03:08:46.212907
# Unit test for function find
def test_find():
    class F:
        b = "hello"

    class E:
        c = F()

    class D:
        d = E()

    class C:
        e = D()

    class B:
        f = C()

    class A:
        g = B()

    res = find(A.g, str)
    assert next(res) == 'hello'

# Generated at 2022-06-14 03:08:53.549921
# Unit test for function get_parent
def test_get_parent():
    import astor
    from ..exceptions import NodeNotFound

    code = """def bar(x):
        x*x
        return str(x)
        
    class bla(object):
        pass
    """
    tree = ast.parse(code)
    print('Tree:')
    print(astor.dump_tree(tree))

    child = tree.body[0]
    print('\nChild:')
    print(astor.dump_tree(child))

    parent = get_parent(tree, child)
    print('\nParent:')
    print(astor.dump_tree(parent))

    print('\nTry to get non existing parent:')
    try:
        get_parent(tree, parent)
    except NodeNotFound as e:
        print(e)

