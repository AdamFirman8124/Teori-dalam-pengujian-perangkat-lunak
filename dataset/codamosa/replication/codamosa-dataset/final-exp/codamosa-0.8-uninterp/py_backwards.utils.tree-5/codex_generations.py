

# Generated at 2022-06-14 03:01:34.988128
# Unit test for function get_parent
def test_get_parent():
  tree = ast.parse("import os")
  sys_node = next(iter(find(tree, ast.Import)))
  os_node = sys_node.names[0]
  assert os_node.name == "os"

  assert get_parent(tree, os_node) == sys_node

# Generated at 2022-06-14 03:01:41.564125
# Unit test for function find
def test_find():
    from . import string_to_ast
    import ast as std_ast
    n = string_to_ast.parse("""
    def b():
        pass
    class A:
        def a(self):
            pass
    #comment
    """)
    result = [
        t.__class__.__name__
        for t in find(n, std_ast.FunctionDef)
    ]
    assert result == ["FunctionDef", "FunctionDef"]



# Generated at 2022-06-14 03:01:46.697149
# Unit test for function get_parent
def test_get_parent():
    def foo():
        a = 1 + 1
    assert get_parent(foo, ast.parse(foo.__code__).body[0].body[0].value) == \
        ast.parse(foo.__code__).body[0]
    assert get_parent(foo, ast.parse(foo.__code__).body[0]) == \
        ast.parse(foo.__code__)



# Generated at 2022-06-14 03:01:55.419736
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('def f():\n    a = b\n')

    non_exp_parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0])
    assert isinstance(non_exp_parent, ast.FunctionDef)
    assert index == 0

    non_exp_parent, index = get_non_exp_parent_and_index(tree, tree.body[0])
    assert isinstance(non_exp_parent, ast.Module)
    assert index == 0



# Generated at 2022-06-14 03:02:06.884585
# Unit test for function replace_at
def test_replace_at():
    from . import load_ast
    import ast
    import unittest

    class ReplaceTest(unittest.TestCase):
        def get_parent_body(self, code: str) -> Tuple[ast.AST, ast.AST, ast.AST]:
            tree = load_ast(code)
            defn = find(tree, ast.FunctionDef).__next__()
            body = defn.body
            return tree, defn, body

        def test_py(self):
            code = '''
            def foo():
                bar = 1
                baz = 2
                foo = 3
            '''
            tree, defn, body = self.get_parent_body(code)
            body_before, body_after = body[:2], body[2:]
            replace_at(2, defn, body_before)

# Generated at 2022-06-14 03:02:11.627257
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    source = '''
    def func():
        import os
        import sys
    '''
    tree = ast.parse(source)
    imp_node = tree.body[0].body[0]
    parent_node, index = get_non_exp_parent_and_index(tree, imp_node)
    assert(parent_node.body[index] == imp_node)


# Generated at 2022-06-14 03:02:15.866230
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():  # lgtm[py/unused-local-variable]
    source = """
    def foo():
        if True:
            x = 1
            while True:
                x = 2
        x = 3
    """
    tree = ast.parse(source)
    node = tree.body[0].body[1].body[0]
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert isinstance(parent, ast.While)
    assert index == 0



# Generated at 2022-06-14 03:02:23.152312
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    com_node = ast.Body()
    com_node_2= ast.Body()

    node1 = ast.FunctionDef(name='A', # type: ignore
                            body=[ast.Return(com_node)])
    node2 = ast.FunctionDef(name='B', # type: ignore
                            body=[node1, com_node_2])
    node3 = ast.Module(body=[node2])

    assert get_closest_parent_of(node3, com_node, ast.FunctionDef).name == 'A'
    assert get_closest_parent_of(node3, com_node_2, ast.FunctionDef).name == 'B'


# Generated at 2022-06-14 03:02:27.149688
# Unit test for function replace_at
def test_replace_at():
    f = ast.parse("""
    a = 1
    """)
    parent = f.body[1]
    a = ast.BoolOp()
    replace_at(0, parent, a)
    assert parent.body[0] == a

# Generated at 2022-06-14 03:02:32.212414
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from typed_ast.ast3 import parse
    code = """
            def fun(a, b):
                c = a + b
    """
    tree = parse(code)
    node = tree.body[0].body[0]
    get_non_exp_parent_and_index(tree, node)

# Generated at 2022-06-14 03:02:41.322503
# Unit test for function find
def test_find():
    """Test is find function works correct."""
    tree = ast.parse('''
        def foo(x, y):
            return x + y

        def bar():
            return foo(1, '')
    ''')
    nodes = list(find(tree, ast.FunctionDef))
    assert len(nodes) == 2
    assert nodes[0].name == 'foo'
    assert nodes[1].name == 'bar'

# Generated at 2022-06-14 03:02:44.366317
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    """Test get_non_exp_parent_and_index function."""
    import astunparse

# Generated at 2022-06-14 03:02:47.090425
# Unit test for function find
def test_find():
    assert len(list(find(ast.parse('a = 1 + 2'), ast.BinOp))) == 1

# Generated at 2022-06-14 03:02:55.500963
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    t = ast.parse('a + b + (c + d) + 2')
    add_expr = t.body[0].value.left
    add_expr.right = ast.parse('c + d').body[0].value
    expected_closest_parent = add_expr.right
    closest_parent = get_closest_parent_of(t, add_expr.right, ast.BinOp)
    assert expected_closest_parent == closest_parent


# Generated at 2022-06-14 03:02:58.696712
# Unit test for function get_parent
def test_get_parent():
    """Function get_parent test."""
    assert get_parent(ast.parse('def f():pass'), ast.parse('pass')).name == 'f'
    assert get_parent(ast.parse('def f():pass'), ast.parse('pass')).name == 'f'



# Generated at 2022-06-14 03:03:11.640711
# Unit test for function find
def test_find():
    # Setup
    input_ast = ast.parse("""
        [
            x
            for y in z
            if y < 5
        ]

        if x < 5:
            print(1)
        else:
            print(2)

        while x < 5:
            print(1)

        def f():
            pass
    """)

    # Exercise
    found_compares = list(find(input_ast, ast.Compare))
    found_ifs = list(find(input_ast, ast.If))
    found_while = list(find(input_ast, ast.While))
    found_functions = list(find(input_ast, ast.FunctionDef))
    found_names = [n.id for n in list(find(input_ast, ast.Name))]

    # Verify

# Generated at 2022-06-14 03:03:15.650228
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    code = textwrap.dedent("""\
    def foo():
        a = 1
        print(a)
    """)

    tree = ast.parse(code)
    parent, index = get_non_exp_parent_and_index(tree, tree.body[0].body[0])
    assert isinstance(parent, ast.Module)
    assert index == 1

# Generated at 2022-06-14 03:03:20.563186
# Unit test for function find
def test_find():
    tree = ast.parse('print("Hello world!")')

    assert tuple(find(tree, ast.Expr)) == (tree.body[0],)
    assert tuple(find(tree, ast.Str)) == (tree.body[0].value,)
    assert tuple(find(tree, ast.Call)) == (tree.body[0].value,)



# Generated at 2022-06-14 03:03:24.144601
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse("[1, 2]")
    assert tree.body[0].value.elts[0].n == 1
    replace_at(0, tree.body[0].value, ast.parse("[3]").body[0].value)
    assert tree.body[0].value.elts[0].n == 3



# Generated at 2022-06-14 03:03:26.736581
# Unit test for function find
def test_find():
    tree = ast.parse("y = lambda x: x + 1")
    for node in find(tree, ast.Lambda):
        assert node.args.args[0].arg == 'x'



# Generated at 2022-06-14 03:03:32.390507
# Unit test for function find
def test_find():
    node = ast.parse("""
x = 1
""")
    nodes = node.body
    assert len(list(find(node, ast.Assign))) == 1

# Generated at 2022-06-14 03:03:36.069860
# Unit test for function find
def test_find():
    assert (list(find(ast.parse("assert isinstance(obj, list)"), ast.Name)) ==
            list(map(lambda x: ast.Name(id=x, ctx=ast.Load()),
                     ['isinstance', 'list'])))



# Generated at 2022-06-14 03:03:41.047733
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    expr = ast.parse("func(b,\nc,d)")
    expr_parent = get_non_exp_parent_and_index(expr, expr.body[0].value)
    assert(expr_parent[1] == 0)
    assert(expr_parent[0].body[0].value.func.id == "func")

# Generated at 2022-06-14 03:03:51.321801
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from .._ast_tools import ast_from_string
    ast_raw = '''
    def a():
        def b():
            x = 1
    '''

    tree = ast_from_string(ast_raw)
    node = find(tree, ast.Name)

    try:
        get_non_exp_parent_and_index(tree, node)
    except NodeNotFound:
        raise AssertionError("Node without body in parent chain not "
                             "accepted.")

    no_parents_tree = ast.parse(ast_raw)
    try:
        get_non_exp_parent_and_index(no_parents_tree, node)
    except NodeNotFound:
        pass
    else:
        raise AssertionError("Node without body in parent chain not "
                             "accepted.")

# Generated at 2022-06-14 03:03:59.605697
# Unit test for function get_parent
def test_get_parent():
    import astor

# Generated at 2022-06-14 03:04:02.385086
# Unit test for function find
def test_find():
    from .helpers import create_test_class

    c = create_test_class()
    for node in find(c, ast.FunctionDef):
        assert True


# Generated at 2022-06-14 03:04:04.749983
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import inspect
    import sys

    # case 1

# Generated at 2022-06-14 03:04:09.696949
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('foo(bar(baz))')

    baz = tree.body[0].value.args[0]  # type: ast.Call
    assert get_non_exp_parent_and_index(tree, baz) == (
        tree.body[0].value, 0)

# Generated at 2022-06-14 03:04:16.440815
# Unit test for function replace_at
def test_replace_at():
    import ast
    import sys
    import textwrap
    code = textwrap.dedent('''
    def hello():
        return 1
    ''')
    tree = ast.parse(code)
    fun_def = tree.body[0]
    return_stmt = fun_def.body[0]
    sys.path.append('.')
    expr = ast.parse('10').body[0]
    replace_at(0, fun_def, expr)
    if ast.dump(tree) == ast.dump(ast.parse(textwrap.dedent('''
    def hello():
        10
    '''))):
        print('Test passed!')
    else:
        print('Test failed!')

# Generated at 2022-06-14 03:04:21.130256
# Unit test for function replace_at
def test_replace_at():
    import unittest
    import typed_ast.ast3 as ast

    class TestASTReplaceAt(unittest.TestCase):
        def test_replace_at(self):
            module = ast.parse('a = 1')
            module = ast.Module([ast.FunctionDef('f', ast.arguments([]),
                                                 [ast.Assign([ast.Name('a', ast.Store())], ast.Num(1))],
                                                 [])])
            #                  Module
            #              /         \
            #         FunctionDef    Assign
            #          /      \         |
            #     Name 'a'   Num 1     Name 'a'
            replace_at(0, module.body[0].body[0], ast.Str('a'))
            #                  Module
            #              /         \
            #        

# Generated at 2022-06-14 03:04:34.245660
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from ..node_utils import str_node
    imp = ast.Import([ast.alias("datetime", None)])
    ass = ast.Assign(targets=[ast.Name("a", ast.Store())],
                     value=ast.Num(1))
    func = ast.FunctionDef("func", ast.arguments([]), [imp, ass], [], None)
    mod = ast.Module([func])
    get_closest_parent_of(mod, imp, ast.FunctionDef) == func

# Generated at 2022-06-14 03:04:35.126249
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:04:36.074245
# Unit test for function replace_at

# Generated at 2022-06-14 03:04:44.952787
# Unit test for function replace_at
def test_replace_at():
    # test_empty_tree
    tree = ast.parse("")
    with pytest.raises(NodeNotFound):
        replace_at(0, tree, ast.parse("a = 1").body[0])

    # test_empty_body
    tree = ast.parse("a = 1")
    with pytest.raises(NodeNotFound):
        replace_at(0, tree, ast.parse("a = 1").body[0])

    # test_valid
    tree = ast.parse("a = 1; b = 1; c = 1; d = 1; e = 1")
    node = ast.parse("a = 1").body[0]
    target_index = 3
    replace_at(target_index, tree, node)
    assert tree.body[target_index] == node



# Generated at 2022-06-14 03:04:57.305091
# Unit test for function find
def test_find():
    import json
    import ezast as ast
    from .ez_ast import ezast_parse
    from ..utils.ez_object_parser import is_same_ast
    from .node_walker import get_nodes

    find_examples = [
        '''
            l = [1, 2, 3]
        '''
    ]


    for example in find_examples:
        tree = ast.parse(example)
        ez_tree = ezast_parse(example)
        listComp = get_nodes(ez_tree, ast.ListComp)[0]
        result_ez_tree = find(tree, ast.ListComp)[0]
        result_tree = ast.parse(json.dumps(ast.dump(result_ez_tree), sort_keys=True))

# Generated at 2022-06-14 03:05:02.788686
# Unit test for function find
def test_find():
    tree = ast.parse(
        '''
        def f1(a, b):
            print(a)
            return a
        def f2(a, b):
            print(b)
            return b
        ''')
    functions = [f for f in find(tree, ast.FunctionDef)]
    assert len(functions) == 2

# Generated at 2022-06-14 03:05:03.834587
# Unit test for function get_parent

# Generated at 2022-06-14 03:05:07.585126
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = 'func_foo(arg_bar)'
    node = ast.parse(code).body[0].value
    func_def = get_closest_parent_of(ast.parse(code), node, ast.FunctionDef)
    assert func_def.name == 'foo'

# Generated at 2022-06-14 03:05:12.753712
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    module = ast.parse('class A:\n    def __init__(self, a):\n        self.a = a')
    target_node = module.body[0].body[0].body[0]
    assert target_node == get_closest_parent_of(module, target_node, ast.ClassDef)

# Generated at 2022-06-14 03:05:17.687415
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    with open("tests/fixtures/test_ast.py") as f:
        tree = ast.parse(f.read())

    # Find the ClassDef node first.
    class_def_node = find(tree, ast.ClassDef).__next__()
    closest_parent = get_closest_parent_of(tree, class_def_node, ast.Module)

    assert isinstance(closest_parent, ast.Module)

# Generated at 2022-06-14 03:05:29.996442
# Unit test for function find
def test_find():
    tree = ast.parse("""
    def func():
        pass
    """)

    assert len(list(find(tree, ast.FunctionDef))) == 1
    assert len(list(find(tree, ast.Return))) == 0


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:05:36.380053
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = '''
    def foo(x):
        return None

    def bar(y):
        return None
    '''

    find_code = '''
    def foo(x):
        return y

    def bar(y):
        return None
    '''

    search_code = '''
        return y
    '''

    tree = ast.parse(code)
    find_tree = ast.parse(find_code)
    search_tree = ast.parse(search_code)

    result = get_closest_parent_of(tree, search_tree.body[0], ast.ClassDef)

    assert result is None

    result = get_closest_parent_of(find_tree, search_tree.body[0], ast.FunctionDef)

    assert result.name == 'foo'

# Generated at 2022-06-14 03:05:37.358389
# Unit test for function find
def test_find():
    import astor

# Generated at 2022-06-14 03:05:46.760921
# Unit test for function find
def test_find():
    source = """
    def foo():
        pass
    """
    # rebuild parents tree
    parsed_tree = ast.parse(source)
    _build_parents(parsed_tree)

    # find all ast.FunctionDef nodes (nodes with class ast.FunctionDef)
    func_nodes = find(parsed_tree, ast.FunctionDef)

    def_node = None

    # check if we got ast.FunctionDef node
    for func_node in func_nodes:
        def_node = func_node


# Generated at 2022-06-14 03:05:49.954379
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("""
func(a, b, c)
""")

    func = get_closest_parent_of(tree, tree.body[0].value, ast.FunctionDef)
    assert func.name == 'func'

# Generated at 2022-06-14 03:05:56.521124
# Unit test for function get_parent
def test_get_parent():
    import os
    import astor

    module_path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(module_path, '..', '..', 'tests', 'fuzzy', 'test.py')
    with open(file) as f:
        tree = astor.parse(f.read())
    _build_parents(tree)
    assert get_parent(tree, tree.body[0]) == tree
    assert get_parent(tree, tree.body[0].body[0]) == tree.body[0]

# Generated at 2022-06-14 03:06:00.763313
# Unit test for function find
def test_find():
    tree = ast.parse("""if True:
    var = 5""")
    assert list(find(tree, ast.Name)) == [ast.Name(id='True', ctx=ast.Load())]


# Generated at 2022-06-14 03:06:15.834682
# Unit test for function find
def test_find():
    import astor
    from ..visitor.ExpressionVisitor import ExpressionVisitor
    from ..visitor.StatementVisitor import StatementVisitor
    from ..visitor.FunctionDefVisitor import FunctionDefVisitor
    from ..common import get_ast_tree
    stmt_visitor = StatementVisitor()
    exp_visitor = ExpressionVisitor()
    funcdef_visitor = FunctionDefVisitor()
    test_ast = get_ast_tree(__file__)
    test_ast.visit(stmt_visitor)
    test_ast.visit(exp_visitor)
    test_ast.visit(funcdef_visitor)

    gen_exprs = find(test_ast, ast.GeneratorExp)
    num_gen_exprs = len(list(gen_exprs))
    assert num_gen

# Generated at 2022-06-14 03:06:22.028053
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    code = '''
        def foo():
            pass
    '''
    tree = ast.parse(code)
    func_def = get_closest_parent_of(tree, tree.body[0].body[0], ast.FunctionDef)
    assert func_def == tree.body[0]  # type: ignore




# Generated at 2022-06-14 03:06:26.745752
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Test different cases
    node = ast.parse('a + b').body[0].value.left

    assert (
        isinstance(
            get_closest_parent_of(
                ast.parse('a + b'), node, ast.AST), ast.AST))
    assert (isinstance(
        get_closest_parent_of(
            ast.parse('a + b'), node, ast.BinOp), ast.BinOp))
    assert (isinstance(
        get_closest_parent_of(
            ast.parse('a + b'), node, ast.Expr), ast.Expr))

    # Test invalid node
    node = ast.parse('a').body[0].value


# Generated at 2022-06-14 03:06:54.196742
# Unit test for function find
def test_find():
    example_module = ast.parse('a = 1')
    nodes = find(example_module, ast.Assign)
    for node in nodes:
        assert node is example_module.body[0]

# Generated at 2022-06-14 03:07:00.558186
# Unit test for function find
def test_find():
    t = ast.parse(
        'def func():\n'
        '    a = 1\n'
        '    b = 1\n'
        '    return a\n'
    )
    r = list(find(t, ast.Name))
    assert r[0].id == 'func'
    assert r[1].id == 'a'
    assert r[2].id == 'b'
    assert r[3].id == 'a'

# Generated at 2022-06-14 03:07:02.333364
# Unit test for function find
def test_find():
    root = ast.parse("a = b = 1")
    assert len(list(find(root, ast.Name))) == 2



# Generated at 2022-06-14 03:07:03.085010
# Unit test for function find
def test_find():
    pass
    # ...



# Generated at 2022-06-14 03:07:08.924925
# Unit test for function find
def test_find():
    t = ast.parse(
        'def f():\n'
        '    pass\n'
        '\n'
        'def g():\n'
        '    pass\n'
    )

    funcs = [x for x in find(t, ast.FunctionDef)]
    assert len(funcs) == 2
    assert funcs[0].name == 'f'
    assert funcs[1].name == 'g'



# Generated at 2022-06-14 03:07:13.820322
# Unit test for function find
def test_find():
    test_ast = ast.parse('import random\nclass Foo: pass')
    assert set(find(test_ast, ast.Import)) == {test_ast.body[0]}
    assert set(find(test_ast, ast.ClassDef)) == {test_ast.body[1]}
    assert set(find(test_ast, ast.ImportFrom)) == set()
    assert set(find(test_ast, ast.FunctionDef)) == set()



# Generated at 2022-06-14 03:07:15.470546
# Unit test for function get_parent

# Generated at 2022-06-14 03:07:22.988830
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('if True: if True: print(1) else: print(2)')

    # True is a child of If node
    node = tree.body[0].body[0].body[0].value

    # Assert that the closest node of If type
    # is the If node, where True is its child
    assert isinstance(get_closest_parent_of(tree, node, ast.If), ast.If)



# Generated at 2022-06-14 03:07:32.004898
# Unit test for function find
def test_find():
    from pprint import pprint
    import sys
    import os
    import unittest

    sys.path.insert(0, os.getcwd())
    from src.parserfunctions.parserfunctions import ParserFunctions

    ParserClass = ParserFunctions(2)
    tree = ParserClass.parse_file("./tests/test_programs/redundant_assignment.py")

    for node in find(tree, ast.Assign):
        print(node.target)
        print(node)

    def test_instance():
        self.assertTrue(True)


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:07:39.190131
# Unit test for function find
def test_find():
    from ..pyfiles import SourceFile
    from .transforms import Assign
    from .visitor import Visitor
    from ..utils import is_true

    class TestNode(ast.AST):
        _fields = ('test',)
        _attributes = ('test',)
        test = 2

    class TestVisitor(Visitor):
        def visit_Assign(self, node: Assign) -> None:
            super().visit_Assign(node)

        def generic_visit(self, node: ast.AST) -> None:
            super().generic_visit(node)

    tree = ast.parse('\n'.join((
        'a = 1',
        'def b():',
        '    a = 2',
        '    c = 3',
        'c = 4'
    )))

# Generated at 2022-06-14 03:09:39.015132
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    program_a = ast.Module((
        ast.Assign((
            ast.Name('a', ast.Store())),
            ast.BinOp(
                ast.Num(1),
                ast.Add(),
                ast.BinOp(
                    ast.Num(2),
                    ast.Add(),
                    ast.Num(3)
                )
            )
        )
    ))
    assert type(get_closest_parent_of(program_a,
        program_a.body[0].value, ast.expr)) is ast.BinOp
    assert type(get_closest_parent_of(program_a,
        program_a.body[0].value, ast.Module)) is ast.Module

# Generated at 2022-06-14 03:09:46.596862
# Unit test for function get_parent
def test_get_parent():
    import unittest
    import astor
    from .fake_ast import test_ast_str

    class TestCase(unittest.TestCase):
        def test(self):
            tree = astor.parse_file(test_ast_str)  # type: ignore
            first_call_arg = get_parent(
                tree, tree.body[0].body[0].body[0].body[1].body[0])
            self.assertIsInstance(first_call_arg, ast.Call)

    TestCase().test()

# Generated at 2022-06-14 03:09:49.115034
# Unit test for function find
def test_find():
    for type_ in [ast.Assign, ast.Expr]:
        for node in find(ast.parse("x = 5 + 6"), type_):
            assert isinstance(node, type_)


# Generated at 2022-06-14 03:09:51.309621
# Unit test for function find
def test_find():
    module = ast.parse('class A:\n    def __init__(self):\n        pass')
    exp = find(module, ast.FunctionDef)
    assert next(exp).name == '__init__'

# Generated at 2022-06-14 03:09:54.684778
# Unit test for function find
def test_find():
    import astor

    tree = astor.parse_file('add_1.py')
    fun = find(tree, ast.FunctionDef)
    assert fun is not None

    num = find(tree, ast.Num)
    assert num is not None

    call = find(tree, ast.Call)
    assert call is not None

    arg = find(tree, ast.arg)
    assert arg is not None


# Generated at 2022-06-14 03:10:02.160818
# Unit test for function find

# Generated at 2022-06-14 03:10:13.537903
# Unit test for function find
def test_find():
    """Test for function find."""
    code = """def x():
        if __debug__:
            print('hello')
            y = 2
            z = 2
        return 2
    """
    tree = ast.parse(code)
    if_node = find(tree, ast.If).__next__()

    # Before
    print(ast.dump(tree))

    insert_at(0, if_node, ast.parse('b = 3').body[0])
    replace_at(2, if_node, ast.parse('b = 3').body[0])

    # After
    print(ast.dump(tree))

if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:10:16.361608
# Unit test for function get_parent
def test_get_parent():
    root = ast.parse('''class Test(object):\n''')
    _build_parents(root)
    assert isinstance(get_parent(root, [x for x in _parents if isinstance(x, ast.ClassDef)][0]), ast.Module)



# Generated at 2022-06-14 03:10:20.337024
# Unit test for function replace_at
def test_replace_at():
    import astor

    class Test:
        def test_func(self):
            a = [1, 2, 3]
            return a

    test_class = Test()
    test_ast = ast.parse(inspect.getsource(test_class.test_func))
    replace_at(1, test_ast, ast.Pass())
    print(astor.to_source(test_ast))

# Generated at 2022-06-14 03:10:22.665637
# Unit test for function get_parent
def test_get_parent():
    assert len(_parents) == 0
