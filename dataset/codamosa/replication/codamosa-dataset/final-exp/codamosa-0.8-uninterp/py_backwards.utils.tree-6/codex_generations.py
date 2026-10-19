

# Generated at 2022-06-14 03:01:36.306060
# Unit test for function find
def test_find():
    ast_tree = ast.parse('a+1\nb+1')
    ast_tree.body.insert(0, ast.parse('a=2'))
    ast_tree.body.insert(2, ast.parse('c=3'))
    c = find(ast_tree, ast.Assign)
    print(ast.dump(c))
    for ass in c:
        print(ass.value)
test_find()

# Generated at 2022-06-14 03:01:37.376831
# Unit test for function get_parent
def test_get_parent():
    pass


# Generated at 2022-06-14 03:01:38.339504
# Unit test for function find

# Generated at 2022-06-14 03:01:39.419824
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:01:41.146511
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:01:46.809798
# Unit test for function find
def test_find():
    from typed_ast.ast3 import Name, Expr, Load, Num, Module
    node = Module(
        body=[
            Expr(
                value=Num(n=1)
            )
        ]
    )
    res = find(node, Num)
    assert len(list(res)) == 1
    res = find(node, Name)
    assert len(list(res)) == 0
    res = find(node, Expr)
    assert len(list(res)) == 1


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:01:56.676159
# Unit test for function replace_at
def test_replace_at():
    imp_mod = ast.ImportFrom(
        module="__main__",
        names=[
            ast.alias(
                name="type_repr",
                asname=None
            )
        ],
        level=0
    )
    test_node = ast.Module(
        body=[ast.Expr(value=imp_mod)]
    )
    assert(len(test_node.body) == 1)
    replace_at(
        0,
        test_node,
        ast.Import(names=[ast.alias(name="typing.io", asname=None)])
    )
    assert(len(test_node.body) == 1)

# Generated at 2022-06-14 03:02:02.629707
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    parent = ast.Module(body=[])
    parent.body.append(ast.FunctionDef(name='foo', args=ast.arguments(
        args=[ast.Name(id='x', ctx=ast.Param())],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]),
        body=[],
        decorator_list=[],
        returns=None))

    top_parent, index = get_non_exp_parent_and_index(parent, parent.body[0])
    assert top_parent is parent and index == 0
    # assert False, 'test is not implemented'


# Generated at 2022-06-14 03:02:08.398121
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('def foo():\n    a = 2\n    b = 4\n    c = a * b')
    wanted_node = tree.body[0].body[2].value
    closest_parent = get_closest_parent_of(tree, wanted_node, ast.FunctionDef)
    assert(isinstance(closest_parent, ast.FunctionDef))
    assert(closest_parent.name == "foo")

# Generated at 2022-06-14 03:02:11.758203
# Unit test for function find
def test_find():
    tree = ast.parse('a = 5')
    for node in find(tree, ast.Assign):
        assert isinstance(node, ast.Assign)
        assert node.value.n == 5

    for node in find(tree, ast.Name):
        assert isinstance(node, ast.Name)

# Generated at 2022-06-14 03:02:19.643182
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("""if True:
        x = 1
    """)
    assert get_non_exp_parent_and_index(tree, tree.body[0]) == (tree, 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].body[0]) == (tree, 1)

# Generated at 2022-06-14 03:02:25.309290
# Unit test for function find
def test_find():
    tree = ast.parse("""def fn():
    x = 1
    y = 2
    x = 3
    print(x, y)""")

    assert list(find(tree, ast.Assign)) == [
        tree.body[0].body[0],
        tree.body[0].body[1],
        tree.body[0].body[2],
    ]

    assert list(find(tree, ast.Print)) == [tree.body[0].body[3]]

    assert list(find(tree, ast.Assign)) == [
        tree.body[0].body[0],
        tree.body[0].body[1],
        tree.body[0].body[2],
    ]



# Generated at 2022-06-14 03:02:32.205167
# Unit test for function find
def test_find():
    code = "a = 1 + 2"
    tree = ast.parse(code)
    print(find(tree, ast.BinOp))
    print(all(isinstance(item, ast.BinOp) for item in find(tree, ast.BinOp)))

# Generated at 2022-06-14 03:02:41.547280
# Unit test for function find
def test_find():
    assert list(find(ast.parse('a=1\nb=2\nc=6'), ast.Assign)) == \
        [ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())],
                    value=ast.Num(n=1)),
         ast.Assign(targets=[ast.Name(id='b', ctx=ast.Store())],
                    value=ast.Num(n=2)),
         ast.Assign(targets=[ast.Name(id='c', ctx=ast.Store())],
                    value=ast.Num(n=6))]

# Generated at 2022-06-14 03:02:45.720327
# Unit test for function find
def test_find():
    @add_id
    def run():
        pass

    def func(x: int) -> int:
        return x + 1


# Generated at 2022-06-14 03:02:52.130462
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from . import from_source
    tree = from_source('x = 1 + 2')
    node = tree.body[0].value
    print(node, node.left, node.right)
    parent = get_closest_parent_of(tree, node, ast.Module)
    print(parent)
    assert isinstance(parent, ast.Module)

# Generated at 2022-06-14 03:02:52.921593
# Unit test for function find
def test_find():
    pass

# Generated at 2022-06-14 03:02:57.640577
# Unit test for function get_parent
def test_get_parent():
    module = ast.parse('{"hello": "world"}')
    body = module.body[0]
    ctx = body.value.keys[0].ctx
    assert get_parent(module, ctx) is body.value.keys[0]


if __name__ == '__main__':
    test_get_parent()

# Generated at 2022-06-14 03:02:58.622996
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:03:03.818675
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from typed_ast import ast3
    a = ast3.Expr(ast3.Subscript(ast3.Name('a', ast3.Load()),\
    ast3.Index(ast3.Num(1)), ast3.Load()))
    b = ast3.Expr(ast3.Subscript(ast3.Name('b', ast3.Load()),\
    ast3.Index(ast3.Num(2)), ast3.Load()))
    tree = ast3.Module(body=[a, b])
    ret_node, ret_index = get_non_exp_parent_and_index(tree, a)
    assert isinstance(ret_node, ast3.Module), '(Invalid type)'
    assert ret_index == 0, '(Invalid index)'



# Generated at 2022-06-14 03:03:10.689734
# Unit test for function find
def test_find():
    with open('tests/test_source/function_with_block.py', 'r') as f:
        tree = ast.parse(f.read())

    assert len(list(find(tree, ast.FunctionDef))) == 2


if __name__ == "__main__":
    test_find()

# Generated at 2022-06-14 03:03:14.247961
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    start = ast.parse(
'''
for x in range(5):
    print(x)

''')
    print(get_non_exp_parent_and_index(start, start.body[0]))



# Generated at 2022-06-14 03:03:17.122118
# Unit test for function find
def test_find():
    tree = ast.parse('x = 1 if y == 2 else 3')
    for node in find(tree, ast.BinOp):
        if node.op.__class__.__name__ == 'Add':
            print(node.op.__class__.__name__)


# Generated at 2022-06-14 03:03:23.224174
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code_string = """
    from test_code.test_code_package.test_code_module import test_code_function
    """
    tree = ast.parse(code_string)
    node = list(find(tree, ast.ImportFrom))[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert isinstance(parent, ast.Module)
    assert index == 0

# Generated at 2022-06-14 03:03:24.008260
# Unit test for function replace_at
def test_replace_at():
    assert False

# Generated at 2022-06-14 03:03:29.428641
# Unit test for function find
def test_find():
    tree = ast.parse(open('./tests/test_code.py', 'r').read())
    assert isinstance(find(tree, ast.For).__next__(), ast.For)
    assert isinstance(find(tree, ast.Name).__next__(), ast.Name)
    assert isinstance(find(tree, ast.Num).__next__(), ast.Num)
    assert isinstance(find(tree, ast.Add).__next__(), ast.Add)
    assert isinstance(find(tree, ast.Load).__next__(), ast.Load)



# Generated at 2022-06-14 03:03:33.220085
# Unit test for function find
def test_find():
    from kimmo import get_parser
    from . import parse

    parser = get_parser('/tmp/test_find')
    parse(parser, '''
        def test_function(a, b):
            return a + b
    ''')

# Generated at 2022-06-14 03:03:41.002738
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    logger = logging.getLogger(__name__)
    logger.info('test get_closest_parent_of')

    expr_to_print_1 = ast.Name(id='x', ctx=ast.Load())
    expr_to_print_2 = ast.Name(id='y', ctx=ast.Load())
    expr_to_print_3 = ast.Name(id='z', ctx=ast.Load())
    mod = ast.Module(
        body=[
            ast.Expr(value=expr_to_print_1),
            ast.Expr(value=expr_to_print_2),
            ast.Expr(value=expr_to_print_3),
        ]
    )


# Generated at 2022-06-14 03:03:49.314226
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from ..ast_tools import parse_ast

    tree = parse_ast("""
    def a():
        if b:
            c()
            for d in e:
                f()
    """)

    node = get_closest_parent_of(tree, tree.body[0].body[0].body[0],
                                 ast.For)

    parent, index = get_non_exp_parent_and_index(tree, node)

    assert parent.body[0].body == node.body
    assert index == 0
    assert isinstance(parent.body[0], ast.If)
    assert isinstance(parent, ast.FunctionDef)

# Generated at 2022-06-14 03:03:50.286182
# Unit test for function find

# Generated at 2022-06-14 03:03:55.581567
# Unit test for function find
def test_find():
    import astp
    res = [it for it in find(astp, ast.AST)]
    assert len(res) == 3


# Generated at 2022-06-14 03:03:56.430197
# Unit test for function find

# Generated at 2022-06-14 03:04:07.580257
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse(
        'for i in range(5):\n'
        '    print(i\n'
        '    print(list(range(i)))')

    # Get first print statement
    func_def_node = tree.body[0]
    for_loop_node = func_def_node.body[0]
    for_loop_body_statements = for_loop_node.body

    assert len(for_loop_body_statements) == 2
    assert isinstance(for_loop_body_statements[0], ast.Expr)
    assert isinstance(for_loop_body_statements[0].value, ast.Call)
    assert isinstance(for_loop_body_statements[0].value.args[0], ast.Name)
    print_call_node = for_loop

# Generated at 2022-06-14 03:04:11.536011
# Unit test for function find
def test_find():
    # pylint: disable=unused-argument
    import inspect
    tree = ast.parse(inspect.getsource(find))
    nodes_list = []
    for node in find(tree, ast.AST):
        nodes_list.append(node)
    assert len(nodes_list) == 2


# Generated at 2022-06-14 03:04:13.071156
# Unit test for function replace_at
def test_replace_at():
    # TODO: This test is not implemented
    pass

# Generated at 2022-06-14 03:04:21.037651
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astunparse
    with open('input_examples/test_get_non_exp_parent_and_index.py') as f:
        tree = astunparse.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Str):
            text = node.s
            expected_parent = tree.body[0]
            expected_index = 0
            break
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert parent is expected_parent
    assert index == expected_index

# Generated at 2022-06-14 03:04:27.899062
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    a = ast.parse('def f():\n    a = 1 + 2')
    t = a.body[0].body[0].value.left
    p, i = get_non_exp_parent_and_index(a, t)
    assert i == 0
    assert isinstance(p, ast.FunctionDef)

# Generated at 2022-06-14 03:04:34.272655
# Unit test for function find
def test_find():
    from .test_data import tree
    from .nodes import FuncDef

    defs = list(find(tree, FuncDef))

    assert len(defs) == 1

    for node in defs:
        assert isinstance(node.name, ast.Name) and node.name.id == 'keep'



# Generated at 2022-06-14 03:04:35.127567
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:04:41.837896
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import astor

    tree = ast.parse('''
    if 3 < 4:
        func(func2(3))
    elif 4 > 2:
        func(3)
    else:
        print(3)
    ''')
    _build_parents(tree)
    node = tree.body[0].body[0].value
    parent, index = get_non_exp_parent_and_index(tree, node)
    print(astor.to_source(parent))
    print(index)

# Generated at 2022-06-14 03:04:57.896423
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from . import ast_helper  # type: ignore

    corr = ast_helper.get_corr('get_non_exp_parent_and_index')
    for i, code in enumerate(corr['code']):
        tree = ast.parse(code)
        node = ast_helper.get_node(tree, corr['node'][i])
        parent, index = get_non_exp_parent_and_index(tree, node)
        assert isinstance(parent, ast.AST)
        assert isinstance(index, int)
        assert corr['parent'][i] == type(parent).__name__
        assert corr['index'][i] == index


# Generated at 2022-06-14 03:05:00.105767
# Unit test for function find
def test_find():
    _ = find(ast.parse("a = 1"), ast.AST)  # type: ignore
    _ = find(ast.parse("a = 1"), ast.stmt)  # type: ignore



# Generated at 2022-06-14 03:05:09.329447
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class TestClass(object):

        def __init__(self, test_number: int, expected_parent, expected_idx):
            self.__test_number = test_number
            self.__expected_parent = expected_parent
            self.__expected_idx = expected_idx

        def run(self):
            tree = ast.parse(self.__get_source_code())
            parent, index = get_non_exp_parent_and_index(tree,
                                                         self.__get_node(tree))
            self.__compare_node_types(parent, self.__expected_parent)
            assert index == self.__expected_idx, \
                'For test number {} expected index is {}, got {}'.format(
                    self.__test_number,
                    self.__expected_idx, index)

# Generated at 2022-06-14 03:05:14.100816
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("def fn():\n\tpass")
    function = tree.body[0]
    body = function.body[0]

    parent, index = get_non_exp_parent_and_index(tree, body)

    assert parent.body[index] == body

# Generated at 2022-06-14 03:05:20.023775
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    test_tree = ast.parse(
        '''
for i in range(5):
    if i == 3:
        pass
    print(i, end=' ')
    '''
    )
    assert get_non_exp_parent_and_index(test_tree, test_tree.body[0].body[0]) \
        == (test_tree.body[0], 0)

    assert get_non_exp_parent_and_index(test_tree,
                                        test_tree.body[0].body[0].test) \
        == (test_tree.body[0].body[0], 1)

# Generated at 2022-06-14 03:05:21.213197
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:27.037998
# Unit test for function get_parent
def test_get_parent():
    from astor import dump
    from ast import parse
    from tests.helpers import get_ast

    tree = get_ast('def foo(bar, baz):\n    return bar')
    node = find(tree, ast.Return).__next__()

    assert dump(get_parent(tree, node)) == dump(
        get_ast('\n    return bar'))

# Generated at 2022-06-14 03:05:36.189051
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from .test_data import root

    index = 0
    parent = get_parent(root, root.body[0])
    assert root is get_non_exp_parent_and_index(root, root)[0]
    assert index == get_non_exp_parent_and_index(root, root.body[0])[1]
    index = root.body.index(get_parent(root, root.body[0]))
    assert index == get_non_exp_parent_and_index(root, parent.body[0])[1]
    index = root.body.index(parent)
    assert index == get_non_exp_parent_and_index(root, parent)[1]


# Generated at 2022-06-14 03:05:40.776013
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("""
    def f():
        pass

    def g():
        pass
    """)

    class_def = tree.body[1]
    function_def = tree.body[0]

    assert get_closest_parent_of(tree, class_def, ast.FunctionDef) == function_def

# Generated at 2022-06-14 03:05:43.529691
# Unit test for function find
def test_find():
    tree = ast.parse('a = 1 + 2')
    nodes = find(tree, ast.BinOp)
    assert isinstance(next(nodes), ast.BinOp)



# Generated at 2022-06-14 03:06:16.138453
# Unit test for function find
def test_find():
    from typed_ast import parse
    tree = parse("""
    import json
    import os
    import sys

    def main():
        x = 0
        while x < 10:
            print("Hallo")
            x += 1
    """)

    defs = list(find(tree, ast.FunctionDef))
    assert len(defs) == 1
    assert defs[0].name == 'main'

    imports = list(find(tree, ast.ImportFrom))
    assert len(imports) == 3
    assert imports[0].module == 'json'

test_find()

# Generated at 2022-06-14 03:06:28.762953
# Unit test for function find
def test_find():
    from ..examples import example_code
    from ..examples import example_code_all_features
    import astunparse

    tree = ast.parse(example_code)
    ast_print = astunparse.unparse(tree).strip()
    assert ast_print == example_code.strip()

    find_node = list(find(tree, ast.Expr))[0]
    ast_print = astunparse.unparse(find_node).strip()
    assert ast_print == 'print("test")'

    tree = ast.parse(example_code_all_features)
    ast_print = astunparse.unparse(tree).strip()
    assert ast_print == example_code_all_features.strip()

    find_body = list(find(tree, ast.Body))[0]
    ast_print = ast

# Generated at 2022-06-14 03:06:35.637466
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Arrange
    @generate_fn
    @add_method('def m(): pass')
    def cls(): pass

    class _: pass

    m = cls.methods[0]
    tree = m.ast
    _build_parents(tree)

    # Act
    result = get_closest_parent_of(tree, m.ast, type(_))

    # Assert
    assert isinstance(result, type(_))

# Generated at 2022-06-14 03:06:42.718719
# Unit test for function find
def test_find():
    #pylint: disable=W0613
    """
    def test():
        def test():
            def test():
                pass
    """

    f = find
    tree = ast.parse(test_find.__doc__)

    assert len(list(f(tree, ast.FunctionDef))) == 3
    assert len(list(f(tree, ast.Name))) == 3


# Generated at 2022-06-14 03:06:48.920707
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    AST = ast.parse("""
    a = 9
    b = 3
    class Node():
        def __init__(self, a, b):
            self.a = a
            self.b = b
    q = Node(a, b)
    """).body
    assert get_non_exp_parent_and_index(AST, AST[2].body[2].value.args[0]) == \
        (AST[2].body[2].value, 1)

# Generated at 2022-06-14 03:06:53.006950
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('a = 1')
    test = tree.body[0]
    parent = get_parent(tree, test)
    non_exp_parent, index = get_non_exp_parent_and_index(tree, test)
    assert parent == non_exp_parent
    assert index == 0

# Generated at 2022-06-14 03:06:59.892733
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('a = b + 1')
    _build_parents(tree)
    assert get_non_exp_parent_and_index(tree, tree.body[0]) == (tree, 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].value) == (tree, 0)
    assert get_non_exp_parent_and_index(tree, tree.body[0].value.left) == (tree, 0)

# Generated at 2022-06-14 03:07:06.345083
# Unit test for function get_parent
def test_get_parent():
    def foo():
        bar = 42
        bar += 1
        bar = bar
        print(bar)

    foo_func = ast.parse(foo.__doc__).body[0]
    bar_assign = foo_func.body[0]
    assign_value = bar_assign.value
    name_bar = assign_value.left
    parent = get_parent(foo_func, name_bar)
    assert parent == bar_assign

    call_print = foo_func.body[2]
    arg_bar = call_print.args[0]
    parent = get_parent(foo_func, arg_bar)
    assert parent == call_print
    assert arg_bar in parent.args



# Generated at 2022-06-14 03:07:14.326001
# Unit test for function find
def test_find():
    tree = ast.parse(
        """
        def foo(func=None):
            if True:
                print()
            else:
                print()
        """
    )

    check = {"If", "Print", "Print"}
    classes = {"If": 3, "Print": 2, "Else": 1}
    for node in find(tree, ast.If):
        assert node.test.value.id in check
        assert node.test.value.id in classes
        classes[node.test.value.id] -= 1
        if classes[node.test.value.id] == 0:
            check.remove(node.test.value.id)
    assert len(check) == 0

# Generated at 2022-06-14 03:07:24.053888
# Unit test for function replace_at
def test_replace_at():
    # Unit test
    import astor
    tree = ast.parse('def foo():\n    bar = 1\n\nbaz = 2')
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0])
    # Replace function foo with function test
    replace_at(index, parent, ast.parse('def test():\n    pass'))
    f = open('test.py', 'w')
    f.write(astor.to_source(tree))
    f.close()

    assert astor.to_source(tree) == 'def test():\n    pass\n\nbaz = 2\n'

# Generated at 2022-06-14 03:08:09.925772
# Unit test for function get_parent
def test_get_parent():
    import ast as ast_
    from .test_utils import parse_ast


# Generated at 2022-06-14 03:08:16.444289
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    src = '''
if foo:
    bar()
'''

    tree = ast.parse(src)
    node = tree.body[0].body[0]  # node == Call instance
    parent = get_closest_parent_of(tree, node, ast.If)

    assert isinstance(parent, ast.If)



# Generated at 2022-06-14 03:08:17.616620
# Unit test for function get_parent

# Generated at 2022-06-14 03:08:21.996155
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse("a = 5")
    node = get_closest_parent_of(tree, tree.body[0].value, ast.Module)
    assert node.body[0].value.n == 5


# Generated at 2022-06-14 03:08:24.815411
# Unit test for function find
def test_find():
    src = "a.b(foo(), bar()).c"
    tree = ast.parse(src)
    found = [n for n in find(tree, ast.Call)]
    assert found[0].func.attr == 'b'
    assert len(found) == 2
    assert found[1].func.attr == 'b'

# Generated at 2022-06-14 03:08:34.194087
# Unit test for function find
def test_find():
    import typed_ast.ast3 as ast
    a = ast.parse('a = 1')
    i1 = find(a, ast.Assign)
    i2 = find(a, ast.Name)
    n = next(i2)
    assert (n.id == 'a')
    n = next(i1)
    assert (isinstance(n, ast.Assign))
    try:
        next(i1)
        raise AssertionError('This line should not be reached.')
    except StopIteration:
        pass

    import sys
    module = sys.modules[__name__]
    for c in find(a, ast.ClassDef):
        assert (c.name == 'test_find')

# Generated at 2022-06-14 03:08:41.401284
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import ast
    import types
    s = '''
        def foo():
            pass

        def bar():
            pass

        def baz():
            pass

        def qux():
            pass

        def goo():
            pass
        '''
    tree = ast.parse(s)
    f = get_closest_parent_of(tree,
                              tree.body[0].body[0], types.FunctionType)
    assert f.name == "foo"
    f = get_closest_parent_of(tree,
                              tree.body[1].body[0], types.FunctionType)
    assert f.name == "bar"
    f = get_closest_parent_of(tree,
                              tree.body[2].body[0], types.FunctionType)

# Generated at 2022-06-14 03:08:51.825445
# Unit test for function find
def test_find():
    code = "def foo(x):\n  return 3"
    tree = ast.parse(code)

    assert [node.id for node in find(tree, ast.Name)] == ['foo', 'x', 'Return']
    assert [node.value.n for node in find(tree, ast.Num)] == [3]
    assert [node.id for node in find(tree, ast.FunctionDef)] == ['foo']
    assert [node.value.n for node in find(tree, ast.Num)] == [3]
    assert [node.id for node in find(tree, ast.Name)] == ['foo', 'x', 'Return']
    assert [node.func.id for node in find(tree, ast.Call)] == ['foo']

# Generated at 2022-06-14 03:09:00.650704
# Unit test for function find
def test_find():
    import unittest
    import typed_ast.ast3

    class ListCompTester(unittest.TestCase):
        def test_returns_list_comp_node(self):
            given_code = '[n for n in range(1, 10)]'
            ast_tree = typed_ast.ast3.parse(given_code)
            list_comp_nodes = list(find(ast_tree, ast.ListComp))

            self.assertEqual(len(list_comp_nodes), 1)
            self.assertEqual(type(list_comp_nodes[0]), ast.ListComp)

    unittest.main()

# Generated at 2022-06-14 03:09:05.706556
# Unit test for function find