

# Generated at 2022-06-14 03:01:42.820544
# Unit test for function insert_at
def test_insert_at():
    """Test for insert_at function."""
    class Node(ast.AST):
        _fields = ('body',)
        body = []

    parent = Node()
    node = ast.Expr(value=ast.Str(s='Hello!'))
    nodes = ast.Expr(value=ast.Str(s='World!'))

    insert_at(0, parent, node)
    assert parent.body[0] == node

    insert_at(0, parent, nodes)
    assert parent.body[0] == nodes and parent.body[1] == node



# Generated at 2022-06-14 03:01:44.114673
# Unit test for function find
def test_find():
    """Test function find."""

# Generated at 2022-06-14 03:01:49.767286
# Unit test for function find
def test_find():  # noqa
    import astor
    from pytypeutils import types as t

    tree = ast.parse('from foo import bar.baz')
    import_node = tree.body[0]
    assert list(find(tree, ast.ImportFrom)) == [import_node]

    tree = ast.parse('from foo import bar.baz')
    import_node = tree.body[0]
    assert list(find(tree, (ast.ImportFrom, ast.Import))) == [import_node]

    tree = ast.parse('from foo import bar.baz')
    import_node = tree.body[0]
    assert list(find(tree, (ast.ImportFrom,))) == [import_node]



# Generated at 2022-06-14 03:01:55.776742
# Unit test for function find
def test_find():
    import astor
    from .test_utils import parse
    node = astor.to_source(ast.parse('a = 5'))
    tree = parse(node)
    x = find(tree, ast.Assign)
    x = find(tree, ast.Assign)
    x = find(tree, ast.Assign)
    assert x is not None



# Generated at 2022-06-14 03:02:01.214097
# Unit test for function find
def test_find():
    body = ast.parse('[(1, 2, 3), (1, 2)]').body
    parent = body[0]
    tuples = find(parent, ast.Tuple)
    tuples = list(tuples)
    test_tuples = [parent.value, parent.value.elements[2]]
    assert tuples == test_tuples, 'Invalid find result'



# Generated at 2022-06-14 03:02:07.069642
# Unit test for function insert_at
def test_insert_at():
    class Module(ast.AST):
        body = []

    class Name(ast.AST):
        id = ''

    class Expr(ast.AST):
        value = None

    class Attribute(ast.AST):
        attr = ''

    class Str(ast.AST):
        s = ''

    module = Module()
    print_name = Name(id='print')
    module.body.append(Expr(value=print_name))
    module.body.append(Expr(value=Str(s='hello')))

    insert_at(0, module, Attribute(value=print_name, attr='out'))

    assert 'out' == module.body[0].value.attr


# Generated at 2022-06-14 03:02:11.143318
# Unit test for function get_parent
def test_get_parent():
    class P(ast.AST):
        _fields = ('left', 'op', 'right')

    class N(ast.AST):
        _fields = ('n', )

    p = P(left=N(n=None), op=None, right=None)
    assert get_parent(p, p.left.n) == p.left



# Generated at 2022-06-14 03:02:15.964414
# Unit test for function insert_at
def test_insert_at():
    global_node = ast.parse(textwrap.dedent('''
    def main():
        pass
    '''), '', 'exec')
    function_def_node = global_node.body[0]
    function_call_node = ast.parse('print("hi")', '', 'eval').body

    insert_at(0, function_def_node, function_call_node)

    assert global_node == ast.parse(textwrap.dedent('''
    def main():
        print("hi")
        pass
    '''), '', 'exec')



# Generated at 2022-06-14 03:02:23.994665
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import numpy as np
    from ..auxiliary import ast_to_code

    # array[0]
    tree = ast.parse(ast_to_code(np.zeros(1)[0]))
    node = tree.body[0].value.elts[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    node2 = parent.body[index]
    assert node == node2

    # array[0][0]
    tree = ast.parse(ast_to_code(np.zeros(1)[0][0]))
    node = tree.body[0].value.elts[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    node2 = parent.body[index]
    assert node == node2



# Generated at 2022-06-14 03:02:31.673202
# Unit test for function find
def test_find():
    from ..utils import parse

    parsed = parse('''
x = "Killer"
y = "Wabbit"
''')
    found = list(find(parsed, ast.Store))
    assert len(found) == 2

    found = list(find(parsed[1], ast.Store))
    assert len(found) == 1

    found = list(find(parsed, ast.Str))
    assert len(found) == 2


# Generated at 2022-06-14 03:02:41.460336
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest
    import typed_ast.ast3 as ast

    tree = ast.parse("""
    def a():
        print("hi")
        if str == 'hello':
            print("no")
        else:
            print("lol")
    """)
    a_node = tree.body[0].body[1]
    assert get_closest_parent_of(tree, a_node, ast.FunctionDef) == tree.body[0]



# Generated at 2022-06-14 03:02:55.975228
# Unit test for function find
def test_find():
    from .test_utils import build_test_tree
    from .imp_finder import find_imports
    from .func_finder import find_functions
    from .class_finder import find_classes

    tree = build_test_tree()

    imports = find(tree, ast.Import)
    assert len(list(imports)) == 4
    assert len(list(find_imports(tree))) == 4

    imports = find(tree, ast.ImportFrom)
    assert len(list(imports)) == 1
    imports = find_imports(tree)
    assert len(list(imports)) == 4

    classes = find(tree, ast.ClassDef)
    assert len(list(classes)) == 1
    classes = find_classes(tree)
    assert len(list(classes)) == 1


# Generated at 2022-06-14 03:03:09.635865
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert isinstance(get_closest_parent_of(ast.parse("def f(): pass"),
                      ast.parse("def f(): pass").body[0].body[0], ast.FunctionDef), ast.FunctionDef)
    # Test neighbour
    assert isinstance(get_closest_parent_of(ast.parse("def f(): pass"),
                      ast.parse("def f(): pass").body[0], ast.Module), ast.Module)
    # Test neighbour with two levels of nesting
    assert isinstance(get_closest_parent_of(ast.parse("def f(): pass"),
                      ast.parse("def f(): pass").body[0], ast.ClassDef), ast.ClassDef)
    # Test up in tree

# Generated at 2022-06-14 03:03:13.767127
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    parent = ast.AST()
    node = ast.AST()
    _parents[node] = parent
    assert get_closest_parent_of(ast.AST(), node, ast.AST) is parent

# Generated at 2022-06-14 03:03:23.739721
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    parent = ast.Module(body=[
        ast.Expr(value=ast.Num(n=1)),
        ast.Expr(value=ast.Num(n=2)),
        ast.Expr(value=ast.Num(n=3))
    ])
    node = ast.Expr(value=ast.Num(n=2))

    expected = ast.Module(body=[
        ast.Expr(value=ast.Num(n=1)),
        ast.Expr(value=ast.Num(n=3)),
        ast.Expr(value=ast.Num(n=2))
    ])

    parent, index = get_non_exp_parent_and_index(parent, node)
    parent.body.pop(index)  # type: ignore
    insert_at(0, parent, node)

    assert parent

# Generated at 2022-06-14 03:03:29.930600
# Unit test for function replace_at
def test_replace_at():
    """Test the function replace_at."""
    node1 = ast.parse('def test(x):\n'
                      '    y = x + 1\n'
                      '    return y')
    node2 = ast.parse('def test(x):\n'
                      '    y = x + 1\n'
                      '    return y')
    node1.body[0].body[1].value = node2  # type: ignore
    _build_parents(node1)

    parent = get_closest_parent_of(node1, node2, ast.FunctionDef)
    replace_at(0, parent, node1)

    assert parent.body == []

# Generated at 2022-06-14 03:03:37.945615
# Unit test for function insert_at
def test_insert_at():
    print('---------- Test ----------')
    test_ast = ast.parse("""a = 5 + 2;
b = 5 + 2;
c = 5 + 2;
d = 5 + 2;""")
    ast.fix_missing_locations(test_ast)
    print(astor.to_source(test_ast))
    to_insert_ast = ast.parse("d = 5 + 2;")
    ast.fix_missing_locations(to_insert_ast)
    insert_at(1, test_ast, to_insert_ast)
    print(astor.to_source(test_ast))
    print('---------- Test ----------')


# Generated at 2022-06-14 03:03:41.908718
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import ast
    module = ast.parse('def test(): assert True')
    assert isinstance(get_closest_parent_of(module, module.body[0].body[0],
                                            ast.FunctionDef), ast.FunctionDef)

# Generated at 2022-06-14 03:03:43.443876
# Unit test for function find

# Generated at 2022-06-14 03:03:53.389964
# Unit test for function find
def test_find():
    import astor
    code = 'class A: pass\nclass B: pass\n'
    my_module = astor.parse_file(code)
    assert len(find(my_module,ast.ClassDef)) == 2
    assert len(find(my_module,ast.FunctionDef)) == 0

    from ..utils.ast_utils import find, get_parent
    from ..utils.ast_utils import get_non_exp_parent_and_index
    from ..utils.ast_utils import get_closest_parent_of, insert_at, replace_at

    code = 'class X: pass\n class Y: pass\n'
    my_module = astor.parse_file(code)
    assert len(find(my_module,ast.ClassDef)) == 2

# Generated at 2022-06-14 03:04:07.332774
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():

    source = '''
if is_done:
    if not is_done:
        if is_done:
            pass
    else:
        pass
else:
    pass
    '''  # noqa: E501

    tree = ast.parse(source)
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0])
    assert isinstance(parent, ast.Module)
    assert index == 0

    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[1])
    assert isinstance(parent, ast.If)
    assert index == 1

    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0].body[1])

# Generated at 2022-06-14 03:04:09.017678
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:04:16.321723
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree_1 = ast.parse('def foo():\n    pass').body[0]
    parent, index = get_non_exp_parent_and_index(tree_1, tree_1.body[0])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 0
    assert parent.body[0] == tree_1.body[0]

    tree_2 = ast.parse('def foo():\n    if True:\n        pass').body[0]
    parent, index = get_non_exp_parent_and_index(tree_2, tree_2.body[1])
    assert isinstance(parent, ast.FunctionDef)
    assert index == 1
    assert parent.body[1] == tree_2.body[1]

# Generated at 2022-06-14 03:04:25.289486
# Unit test for function get_parent
def test_get_parent():
    code = 'for i in range(10):\n    a = i + 1'

    tree = ast.parse(code)
    _build_parents(tree)

    def test_parent(parent: ast.AST, node: ast.AST) -> None:
        assert get_parent(tree, node) == parent

    for_node = tree.body[0]
    assert for_node.iter.lineno == 1
    assert for_node.body[0].lineno == 2
    test_parent(for_node, for_node.body[0])
    test_parent(tree, for_node)
    test_parent(for_node, for_node.iter)
    test_parent(for_node, for_node.target)



# Generated at 2022-06-14 03:04:30.348582
# Unit test for function get_parent
def test_get_parent():
    root = ast.Module([ast.FunctionDef('func', ast.arguments(), [], [], '')])
    func = root.body[0]

    assert get_parent(root, func) is root

# Generated at 2022-06-14 03:04:34.190781
# Unit test for function find
def test_find():  # pragma: no cover
    tree = ast.parse('x = 17')
    assert list(find(tree, ast.Module))
    assert list(find(tree, ast.Name))



# Generated at 2022-06-14 03:04:34.967856
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:04:40.845461
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("def f():\n"
                     "    while True:\n"
                     "        print(True)\n")

    print(tree)
    print(get_closest_parent_of(tree, tree.body[0].body[0].body[0], ast.While))



# Generated at 2022-06-14 03:04:51.865314
# Unit test for function find
def test_find():
    a = ast.parse('a = 1')
    b = ast.parse('b = 2')
    c = ast.parse('c = 3')
    d = ast.parse('d = 4')

    x = ast.List([a, b])
    y = ast.List([c, d])

    z = ast.List([x, y])

    l = list(find(z, ast.Assign))
    assert l == [a, b, c, d]

# Generated at 2022-06-14 03:04:55.666267
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .test_ast import test_ast
    parent = get_closest_parent_of(test_ast, test_ast.body[0].body[4].body[5], ast.FunctionDef)
    assert parent.name == 'test_func'

# Generated at 2022-06-14 03:05:05.818771
# Unit test for function replace_at
def test_replace_at():
    class ClassDef(ast.AST):
        body = []

    class Module(ast.AST):
        body = []

    child = ast.Name(id='name')
    parent = ClassDef()
    grandparent = Module()
    grandparent.body.append(parent)  # type: ignore
    parent.body.append(child)  # type: ignore

    replace_at(0, grandparent, ast.Name(id='other'))

    assert grandparent.body[0].body[0].id == 'other'



# Generated at 2022-06-14 03:05:09.201462
# Unit test for function find
def test_find():
    code = """
    def fn(x):
        x = True
        x = False
        x = True
        x = False
    """
    tree = ast.parse(code)
    nodes = find(tree, ast.FunctionDef)
    for node in nodes:
        print(node)


# Generated at 2022-06-14 03:05:15.875270
# Unit test for function find
def test_find():
    node = ast.Module([
        ast.FunctionDef(
            name='foo', args=ast.arguments(args=[ast.Name()], vararg=None,
                                           kwarg=None, defaults=[],
                                           kwonlyargs=[], kw_defaults=[]),
            body=[ast.Pass()], decorator_list=[], returns=None)
    ])

    assert len(list(find(node, ast.FunctionDef))) == 1

# Generated at 2022-06-14 03:05:17.336185
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astunparse

# Generated at 2022-06-14 03:05:20.928054
# Unit test for function find
def test_find():
    file_path = '/home/p4kl0nc4t/Projects/GitHub/ast_parser/test/test_data/' \
            'if_condition.py'
    root = ast.parse(open(file_path).read())
    node = get_closest_parent_of(root, find(
        root, ast.Assign)[0], ast.If)
    assert isinstance(node, ast.If)

# Generated at 2022-06-14 03:05:22.269274
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astunparse
    import astor


# Generated at 2022-06-14 03:05:25.945596
# Unit test for function find
def test_find():
    from pprint import pprint
    from .examples import program_1
    pprint(list(find(program_1, ast.Call)))



# Generated at 2022-06-14 03:05:28.064450
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('simple_string')
    assert get_parent(tree, tree.body[0].value) == tree.body[0]



# Generated at 2022-06-14 03:05:36.826475
# Unit test for function replace_at
def test_replace_at():
    from typed_ast import ast3 as ast
    from ..utils.parser import parse_string
    from ..utils.printing import print_value

    tree = parse_string('a = 5')
    assign = tree.body[0]
    name = assign.targets[0]
    parent = get_parent(tree, name)
    index = parent.body.index(assign)  # type: ignore
    replace_at(index, parent, ast.Assign(
        targets=[ast.Name(id='b', ctx=ast.Store())],
        value=ast.Num(n=5)
    ))

    print_value(tree)
    assert False



# Generated at 2022-06-14 03:05:46.291260
# Unit test for function find
def test_find():
    from typed_ast import ast3  # type: ignore
    s = "def f():\n    def f():\n        x = 5\n        x\n    x = 6\n    x"
    root = ast3.parse(s)

    names = list(find(root, ast3.Name))
    assert names == [ast3.Name(id='x', ctx=ast3.Load()),
                     ast3.Name(id='x', ctx=ast3.Store()),
                     ast3.Name(id='f', ctx=ast3.Load())]

    loads = list(find(root, ast3.Load))
    assert loads == [ast3.Load(), ast3.Load()]

    args = list(find(root, ast3.arguments))

# Generated at 2022-06-14 03:05:55.969198
# Unit test for function find
def test_find():
    example = """
    def func():
        lst = [1,2,3]
        lst.append(4)
        b = 2
        return b
    """

    tree = ast.parse(example)
    assert len(list(find(tree, ast.Name))) == 4
    assert len(list(find(tree, ast.List))) == 1
    assert len(list(find(tree, ast.Num))) == 3
    assert len(list(find(tree, ast.If))) == 0
    assert len(list(find(tree, ast.FunctionDef))) == 1

# Generated at 2022-06-14 03:06:04.734106
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('test = []')
    assert get_parent(tree, tree.body[0].value) == tree.body[0]
    tree = ast.parse('test = get_parent(tree.body[0].value)')
    assert get_parent(tree, tree.body[0].value.args[0]) == tree.body[0].value
    assert get_parent(tree, tree.body[0].value.args[0].value) == tree.body[0]

# Generated at 2022-06-14 03:06:17.078654
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:06:27.005349
# Unit test for function replace_at
def test_replace_at():
    _ast = ast.parse(r'''
        def outer():
            def test():
                print(42)
    ''')
    outer_def = _ast.body[0]
    test_def = outer_def.body[0]
    replace_at(0, outer_def, ast.parse(r'''
        def asdf():
            pass
    '''))
    assert(len(outer_def.body) == 2)
    assert(outer_def.body[1] == test_def)

# Generated at 2022-06-14 03:06:34.622799
# Unit test for function find
def test_find():
    class Test(ast.AST):
        _fields = ['foo', 'bar']

    import astor

    t = Test(foo='foo', bar='bar', lineno=1, col_offset=1)
    t2 = Test(foo='foo', bar='bar', lineno=2, col_offset=1)
    t3 = Test(foo='foo', bar='bar', lineno=3, col_offset=1)

    t1_1 = Test(foo='foo', bar='bar', lineno=1, col_offset=1)
    t1_2 = Test(foo='foo', bar='bar', lineno=1, col_offset=2)
    t1_3 = Test(foo='foo', bar='bar', lineno=1, col_offset=3)

    t1_1.foo = t1_2


# Generated at 2022-06-14 03:06:46.439167
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import unittest
    from typed_ast import ast3 as ast

    class TestNonExpParentAndIndex(unittest.TestCase):

        def test_with_class_parent(self):
            source = """
            class TestClass:
                def test_method(self):
                    pass
            """
            tree = ast.parse(source)
            method = tree.body[0].body[0]
            exp = method.body[0]
            self.assertEqual((method, 0), get_non_exp_parent_and_index(tree, exp))

        def test_with_def_parent(self):
            source = """
            def test_method():
                pass
            """
            tree = ast.parse(source)
            method = tree.body[0]
            exp = method.body[0]

# Generated at 2022-06-14 03:06:50.971533
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("""
    def test():
        for i in range(10):
            i = 1
            pass
    """)
    node = tree.body[0].body[0].body[0]
    assert isinstance(get_closest_parent_of(tree, node, ast.For), ast.For)
    assert isinstance(get_closest_parent_of(tree, node, ast.FunctionDef), ast.FunctionDef)

# Generated at 2022-06-14 03:06:57.178211
# Unit test for function replace_at
def test_replace_at():
    root = ast.parse('a = 3')
    replace_at(0, root, ast.parse('b = 4').body)  # type: ignore
    assert ast.dump(root) == "Module(body=[Assign(targets=[Name(id='b', ctx=Store())], value=Num(n=4))])"


# Generated at 2022-06-14 03:07:03.050738
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("a = 100 + 200").body[0]

    # Exp node
    node = tree.value
    assert get_non_exp_parent_and_index(tree, node) == (tree, 0)

    # BinOp node
    node = node.left
    assert get_non_exp_parent_and_index(tree, node) == (tree, 0)

    # Num node
    node = node.n
    assert get_non_exp_parent_and_index(tree, node) == (tree, 0)

# Generated at 2022-06-14 03:07:09.052557
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = "class SomeClass(SomeOtherClass):\n"\
           "    def fun1(self, fun2_arg):\n"\
           "        fun2(fun2_arg)\n"\
           "        for i in range(10):\n"\
           "            fun3(i)"

    tree = ast.parse(tree)
    class_node = tree.body[0]
    fun1_node = class_node.body[0]

    non_exp_parent, index = get_non_exp_parent_and_index(
        tree, fun1_node)
    assert isinstance(non_exp_parent, ast.ClassDef)
    assert index == 0

    for_node = fun1_node.body[1]
    non_exp_parent, index = get_non_exp_parent_and

# Generated at 2022-06-14 03:07:18.231166
# Unit test for function get_parent
def test_get_parent():
    test_tree = ast.parse('def f():\n return 3 + 4')
    expected_tree = '<_ast.Module object at 0x7f9ed9a59d68>'
    parent = get_parent(test_tree, test_tree.body[0])
    assert expected_tree == str(parent)


# Generated at 2022-06-14 03:07:19.279410
# Unit test for function find

# Generated at 2022-06-14 03:07:23.091387
# Unit test for function find
def test_find():
    expr = '''
    x = 1 + 5
    if x == 5:
        y = 3
    '''

    tree = ast.parse(expr)
    print(tree)


# Generated at 2022-06-14 03:07:31.739414
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from .testing import test_ast

    assert isinstance(get_closest_parent_of(test_ast, test_ast.body[2].body[6],
                                            ast.FunctionDef),
                      ast.FunctionDef)
    assert isinstance(get_closest_parent_of(test_ast, test_ast.body[2].body[6],
                                            ast.ClassDef),
                      ast.ClassDef)
    assert isinstance(get_closest_parent_of(test_ast, test_ast.body[2].body[6],
                                            ast.Module),
                      ast.Module)



# Generated at 2022-06-14 03:07:39.528446
# Unit test for function get_parent
def test_get_parent():
    foo = ast.parse("def foo(): pass", mode='exec')
    parent = get_parent(foo, foo.body[0])
    assert isinstance(parent, ast.Module)
    parent = get_parent(foo, foo.body[0].body[0])
    assert isinstance(parent, ast.FunctionDef)
    parent = get_parent(foo, foo.body[0].body[0].value)
    assert isinstance(parent, ast.Pass)

# Generated at 2022-06-14 03:07:42.224663
# Unit test for function find
def test_find():
    code = """
    def f():
        pass
    """
    tree = ast.parse(code)
    assert (list(find(tree, ast.FunctionDef)) ==
            [tree.body[0].body[0].value.func.value.func])


# Generated at 2022-06-14 03:07:46.127224
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    tree = ast.parse('''
    def my_func(arg1, arg2):
        if arg1 and arg2:
            return 0
        return 1
    ''')
    func_def = list(find(tree, ast.FunctionDef))[0]
    body = list(find(tree, ast.Return))[0]
    expected = astor.to_source(func_def)
    actual = astor.to_source(get_closest_parent_of(tree, body, ast.FunctionDef))

    assert expected == actual

# Generated at 2022-06-14 03:07:50.946691
# Unit test for function find
def test_find():
    import unittest

    from typed_ast import ast3 as ast
    from .parse import parse_file

    class Test(unittest.TestCase):
        def test_find(self):
            def test(code):
                tree = parse_file(code)
                self.assertEqual(list(find(tree, ast.FunctionDef)),
                                 [tree.body[0]])

                self.assertEqual(list(find(tree, ast.Name)),
                                 [tree.body[0].args.args[0],
                                  tree.body[0].body[0].value.func,
                                  tree.body[0].body[0].value.args[0]])

            test('def func(name): print(name)')

    unittest.main()

# Generated at 2022-06-14 03:07:59.535001
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            tree = ast.parse('def foo():\n  def bar():\n    pass\n')
            node = tree.body[0].body[0].body[0]
            closest = get_closest_parent_of(tree, node, ast.FunctionDef)
            self.assertEquals(closest.name, 'bar')

    unittest.main()


# Generated at 2022-06-14 03:08:03.750038
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import ast
    import astor
    from ..parser import parse

    code = 'name = get_user_name(user)'
    tree = parse(code)

    node = list(find(tree, ast.Name))[0]
    result = get_closest_parent_of(tree, node, ast.Call)
    assert astor.to_source(result) == 'get_user_name(user)'

# Generated at 2022-06-14 03:08:14.743099
# Unit test for function get_parent
def test_get_parent():
    """Check if function get_parent returns the correct parent"""
    global _parents
    for node in _parents:
        parent = get_parent(tree, node)
        assert parent == _parents[node]


# Generated at 2022-06-14 03:08:18.481175
# Unit test for function find
def test_find():
    code = ast.parse("def a():\n    def b(): pass\n\n    def c(): pass\n")
    assert len(list(find(code, ast.FunctionDef))) == 2

# Generated at 2022-06-14 03:08:26.085150
# Unit test for function find
def test_find():
    import astor
    code_str = "foo = 'bar'"
    node = ast.parse(code_str).body[0]
    parent = get_parent(ast.parse(code_str), node)
    non_exp_parent, index = get_non_exp_parent_and_index(ast.parse(code_str), node)
    nodes = ast.Str('test')
    insert_at(index, non_exp_parent, nodes)

    assert(astor.to_source(node) == "foo = 'test'")

# Generated at 2022-06-14 03:08:33.496850
# Unit test for function find
def test_find():
    tree = ast.parse("""def f(x):\n    print(x + 2)\nprint(5)""")

    assert len(list(find(tree, ast.Module))) == 1
    assert len(list(find(tree, ast.Expression))) == 2
    assert len(list(find(tree, ast.Call))) == 2



# Generated at 2022-06-14 03:08:35.583117
# Unit test for function find
def test_find():
    import astunparse
    import io
    import sys


# Generated at 2022-06-14 03:08:42.310886
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    from ..ast_transformer import transform

    code = """
        def foo(a):
            b = a + 1
            c = a + 2
    """

    tree = ast.parse(code)
    tree = transform(tree)
    node = tree.body[0].body[0].targets[0]
    parent = get_closest_parent_of(tree, node, ast.FunctionDef)

    assert parent.name == 'foo'

# Generated at 2022-06-14 03:08:46.862849
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(ast.parse('def z():\n  x=2\n'), ast.Num(2), ast.FunctionDef) == ast.parse('def z():\n  pass').body[0]

# Generated at 2022-06-14 03:08:48.352367
# Unit test for function find
def test_find():
    # TODO: add docstrings
    pass



# Generated at 2022-06-14 03:08:49.322952
# Unit test for function find

# Generated at 2022-06-14 03:09:01.875670
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Loop through all files in the test folder
    for file in Path(__file__).parent.parent.parent / 'tests' / 'inputs':
        # Parse the file into AST
        with file.open() as f:
            tree = ast.parse(f.read())

        # Find all the class definitions
        for node in find(tree, ast.ClassDef):
            # Find the closest parent of type function
            for child in node.body:
                assert isinstance(get_closest_parent_of(tree, child,
                                                        ast.FunctionDef),
                                  ast.FunctionDef)

        # Find all the function definitions

# Generated at 2022-06-14 03:09:12.569416
# Unit test for function find
def test_find():
    class TestType:
        pass

    class TestType2:
        pass

    test_list = [TestType(), TestType(), TestType2(), TestType(),
                 TestType2()]

    # Make sure find returns correct nodes
    assert list(find(test_list, TestType)) == test_list[0:4:2]
    assert list(find(test_list, TestType2)) == test_list[2::2]

# Generated at 2022-06-14 03:09:17.237526
# Unit test for function find
def test_find():
    import typed_astunparse
    from astor.code_gen import to_source
    import ast
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            result = typed_astunparse.unparse(find(
                ast.parse(to_source(find)), ast.Lambda)[0])
            self.assertEquals(result,
                              "lambda args: return_statement")

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-14 03:09:22.630482
# Unit test for function find
def test_find():
    global _parents
    expr = ast.parse('1+2\nx').body[0]
    _parents = {}
    assert list(find(expr, ast.BinOp)) == [expr.value]
    assert list(find(expr, ast.Name)) == [expr.value.left, expr.value.right]



# Generated at 2022-06-14 03:09:27.761491
# Unit test for function find
def test_find():
    tree = ast.parse("""
        def a():
            pass

        def b():
            pass
        """)
    assert len(list(find(tree, ast.FunctionDef))) == 2
    assert len(list(find(tree, ast.Name))) == 2

# Generated at 2022-06-14 03:09:32.544509
# Unit test for function find
def test_find():
    tree = ast.parse('if True:\n    print("Hello world")')
    nodes = [node for node in find(tree, ast.If)]
    assert len(nodes) == 1
    assert isinstance(nodes[0], ast.If)

# Generated at 2022-06-14 03:09:33.903541
# Unit test for function get_parent

# Generated at 2022-06-14 03:09:44.707160
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Test get_closest_parent_of."""
    node = ast.Expr(value=ast.Name(id='a'))
    tree = ast.Module(body=[
        ast.Expr(value=ast.BinOp(left=ast.Num(n=1), right=node, op=ast.Add())),
    ])

    assert get_closest_parent_of(tree, node, ast.Module) == tree
    assert isinstance(get_closest_parent_of(tree, node, ast.BinOp), ast.BinOp)



# Generated at 2022-06-14 03:09:53.060357
# Unit test for function find
def test_find():
    import unittest

    class TestFind(unittest.TestCase):
        def test_find(self):
            tree = ast.parse('import a.b.c\nimport os')
            self.assertEqual(len(list(find(tree, ast.Module))), 1)
            self.assertEqual(len(list(find(tree, ast.ImportFrom))), 2)
            self.assertEqual(len(list(find(tree, ast.Import))), 2)
            self.assertEqual(len(list(find(tree, ast.Name))), 3)
            self.assertEqual(len(list(find(tree, ast.alias))), 3)
            self.assertEqual(len(list(find(tree, ast.NameConstant))), 0)

    unittest.main()


# Generated at 2022-06-14 03:10:02.765439
# Unit test for function find
def test_find():
    # import astor
    # import astpretty
    from ..utils import Loader
    from ..traversal import transform
    from ..transforms.decorators import decorate_all, decorate_func

    filename = 'testdata/decorator.py'

    #root = Loader.load_ast_from_file(filename)
    #print(astor.to_source(root, indent_with=' '*4))
    #astpretty.pprint(root)

    root = Loader.load_source(filename)
    #print(root)

    tree = Loader.ast_from_source(root)
    tree = decorate_all(tree)
    tree = decorate_func(tree)
    transform(tree)
    # print(astor.to_source(tree, indent_with=' '*4))


# Generated at 2022-06-14 03:10:08.757316
# Unit test for function find
def test_find():
    """Test for function find."""
    tree = ast.parse('foo = 1')
    nodes = list(find(tree, ast.Name))
    assert nodes[0].id == 'foo'
    assert len(nodes) == 1



# Generated at 2022-06-14 03:10:30.793442
# Unit test for function find
def test_find():
    import astor
    # 1. find_all_function_defs_in_tree
    python_module = "def name(args): pass"

    tree = ast.parse(python_module)
    func_def = list(find(tree, ast.FunctionDef))[0]
    assert func_def.name == "name"

    # 2. find all instances of a class


# Generated at 2022-06-14 03:10:38.976241
# Unit test for function get_parent

# Generated at 2022-06-14 03:10:49.178856
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    parsed = ast.parse("""
        def fun():
            if True:
                a = 1
                b = 2
                for c in [1, 2, 3]:
                    pass
    """)
    for_loop = parsed.body[0].body[1]
    assert isinstance(get_closest_parent_of(parsed, for_loop, ast.FunctionDef),
                      ast.FunctionDef)
    assert isinstance(get_closest_parent_of(parsed, for_loop, ast.If), ast.If)



# Generated at 2022-06-14 03:10:52.388381
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    x = ast.Name('x', ast.Store())
    funcdef = ast.FunctionDef('foo', ast.arguments(args=[ast.Name('x', ast.Param())]),
                              [ast.Expr(x)], [], None, None)
    tree = ast.Module([funcdef])
    assert get_closest_parent_of(tree, x, ast.FunctionDef) == funcdef

# Generated at 2022-06-14 03:10:55.973242
# Unit test for function find
def test_find():
    # pylint: disable=invalid-name
    test_ast = ast.parse(
        '''def inner():
            pass

        def test():
            inner()
            pass
        ''')
    test_ast.body[1].body[0].name = 'inner2'
    assert len(list(find(test_ast, ast.Call))) == 2
    assert len(list(find(test_ast, ast.FunctionDef))) == 2
    assert len(list(find(test_ast, ast.Name))) == 2



# Generated at 2022-06-14 03:11:04.237554
# Unit test for function find
def test_find():
    class T(ast.AST):
        pass

    class T1(ast.AST):
        pass

    class T2(ast.AST):
        pass

    root = T1()
    child = T()
    child1 = T2()

    root.body = [child, child1]

    assert list(find(root, type_=T)) == [child]



# Generated at 2022-06-14 03:11:13.625061
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    pyast = ast.parse("""
        a = [[1, 2], [3, 4]]
        b = a[2][2]
    """)

    assert(type(get_closest_parent_of(pyast, pyast.body[1].value, ast.list)) is ast.list)
    assert(type(get_closest_parent_of(pyast, pyast.body[1].value, ast.Subscript)) is ast.Subscript)
    assert(type(get_closest_parent_of(pyast, pyast.body[1].value, ast.FunctionDef)) is ast.Module)

# Generated at 2022-06-14 03:11:23.843666
# Unit test for function find
def test_find():
    # type: (...) -> None
    """Test function find."""
    import astor
    a = ast.parse('''
    class A:
        def f(self):
            pass
    def g():
        pass
    ''')

    for name in find(a, ast.Name):
        if name.id == 'A':
            print(astor.dump_tree(get_parent(a, name)))
            print(astor.dump_tree(name))

if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:11:30.506245
# Unit test for function find
def test_find():
    test_tree = ast.parse("def foo():\n    bar('baz')").body
    assert test_tree == list(find(test_tree, ast.FunctionDef))
    assert 'baz' == find(test_tree, ast.Str).__next__().s
    assert 'foo' == find(test_tree, ast.Name).__next__().id
