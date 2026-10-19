

# Generated at 2022-06-14 02:17:11.660797
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert _parse_and_transform('[2, *range(10), 1]') == '[2] + list(range(10)) + [1]'


# Generated at 2022-06-14 02:17:21.446655
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import textwrap
    from ..transformer import TreeTransformer
    from ..utils import dump
    from ..parsing import parse_string

    tt = TreeTransformer()
    tt.register(StarredUnpackingTransformer)


# Generated at 2022-06-14 02:17:29.707166
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def caller(a, b, c):
        print(a,b,c)

    code = """caller(0,*[2, 3], 1)"""
    expected = """caller(*(([0] + list([2, 3])) + [1]))"""

    nodes = ast.parse(code)
    t = StarredUnpackingTransformer()
    res = t.visit(nodes)
    actual = str(res)[:-1]  # skip last linefeed

    assert actual == expected


# Generated at 2022-06-14 02:17:35.857497
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3
    import astor
    code = '[2, *range(10), 1]'
    tree = astor.parse_file(io.StringIO(code))
    visitor = StarredUnpackingTransformer()
    visitor.visit(tree)
    assert isinstance(tree.body[0], ast3.Expr)
    assert isinstance(tree.body[0].value, ast3.BinOp)
    assert isinstance(tree.body[0].value.right, ast3.Call)


# Generated at 2022-06-14 02:17:44.689095
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    class DummyNodeTransformer(StarredUnpackingTransformer):
        def visit_List(self, node: ast.List) -> ast.List:
            node = super(DummyNodeTransformer, self).visit_List(node)

            return node

    # Test with 1 Starred appearance
    dummy = DummyNodeTransformer()
    node = ast.List(
        elts=[
            ast.Num(n=2),
            ast.Starred(value=ast.Name(id='range', ctx=ast.Load())),
            ast.Num(n=1)
        ]
    )
    assert str(dummy.visit(node)) == '[2] + list(range(0)) + [1]'

    # Test with more than 1 Starred appearance

# Generated at 2022-06-14 02:17:55.877072
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from python_transformer.typed_ast_converter import parse_ast
    from .instance_mocker import InstanceMocker
    from python_transformer.typed_ast_extension import get_all_nodes

    source = '[2, *range(10), 1, *[1]]'
    expected = '([2] + list(range(10)) + [1] + list([1]))'

    result = StarredUnpackingTransformer(source).transform()
    assert expected == result

    # Check: all nodes were visited (ie. this method is complete)
    exp_node = parse_ast(expected)
    node = parse_ast(result)

# Generated at 2022-06-14 02:18:01.356276
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List."""
    in_val = """
# in
[2, *range(10), 1]
"""
    out_val = """
# out
[2] + list(range(10)) + [1]
"""

    st = StarredUnpackingTransformer()
    tree = ast.parse(in_val)
    st.visit(tree)
    code = compile(tree, filename="<string>", mode="exec")
    ns = {}
    eval(code, ns)
    out_tree = ast.parse(out_val)
    assert_equal_ast(ns['x'], out_tree)


# Generated at 2022-06-14 02:18:07.826016
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    print("test_StarredUnpackingTransformer_visit_Call")
    source = """
a = 2
b = 3
print(a, b, *range(10))
    """
    tests = [
        (ast.parse(source), """
a = 2
b = 3
print(*(list([a, b]) + list(range(10))))
        """)
    ]
    for input, expected in tests:
        output = StarredUnpackingTransformer().visit(input)
        assert output == ast.parse(expected)


# Generated at 2022-06-14 02:18:14.483984
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astunparse

    tree = ast.parse('''
        print(*range(2, 3), *range(4, 6), *range(7, 12))
    ''')

    trans = StarredUnpackingTransformer()
    new_ast = trans.visit(tree)

    assert astunparse.unparse(new_ast) == '''
        print(*(list(range(2, 3)) + list(range(4, 6)) + list(range(7, 12))))
    '''



# Generated at 2022-06-14 02:18:23.247926
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast.ast3 import parse
    import astor
    tree = parse("""print(1, *range(1), 2, *range(1), *range(10), 1, end=' ')""")

    StarredUnpackingTransformer().visit(tree)

    code = astor.to_source(tree)
    import sys
    exec(code, sys._getframe(1).f_globals, sys._getframe(1).f_locals)
    assert code == """print(*(list([1]) + list(range(1)) + list([2]) + list(range(1)) + list(range(10)) + list([1])), end=' ')"""


# Generated at 2022-06-14 02:18:29.969163
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:18:40.845047
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert not StarredUnpackingTransformer._has_starred([])
    assert not StarredUnpackingTransformer._has_starred([ast.Name('a')])
    assert StarredUnpackingTransformer._has_starred([ast.Starred(ast.Name('a'))])

    assert StarredUnpackingTransformer()._split_by_starred([ast.Name('a'),
                                                             ast.Starred(ast.Name('b')),
                                                             ast.Name('c'),
                                                             ast.Name('d')]) == [
        [ast.Name('a')],
        ast.Starred(ast.Name('b')),
        [ast.Name('c'), ast.Name('d')]]


# Generated at 2022-06-14 02:18:42.425181
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer(None).target == (3, 4)

# Generated at 2022-06-14 02:18:51.489125
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:18:55.405351
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = "[2, *range(10), 1]"
    expected_code = "[2] + list(range(10)) + [1]"
    tree = compile(code, '<string>', 'exec', ast.PyCF_ONLY_AST)
    expected_tree = compile(expected_code, '<string>', 'exec', ast.PyCF_ONLY_AST)
    StarredUnpackingTransformer().visit(tree)
    assert compare_ast(tree, expected_tree)


# Generated at 2022-06-14 02:19:01.766666
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*range(1), *range(3))')
    expected = ast.parse('print(*(list(range(1)) + list(range(3))))')
    result = StarredUnpackingTransformer().visit(tree)
    assert ast.dump(expected) == ast.dump(result)
    assert ast.dump(expected) == ast.dump(tree)


# Generated at 2022-06-14 02:19:09.633643
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List(elts=[
        ast.Num(n=2),
        ast.Starred(value=ast.Call(
            func=ast.Name(id='range'),
            args=[ast.Num(n=10)],
            keywords=[])),
        ast.Num(n=1)])
    StarredUnpackingTransformer.run(node)
    expected = ast.Module(body=ast.Expr(value=ast.BinOp(left=ast.List(elts=[ast.Num(n=2)]), right=ast.Call(
        func=ast.Name(id='list'),
        args=[ast.Call(
            func=ast.Name(id='range'),
            args=[ast.Num(n=10)],
            keywords=[])],
        keywords=[]), op=ast.Add())))

# Generated at 2022-06-14 02:19:18.088974
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    raw_tree = ast.parse("""
        [2, *range(10), 1]
    """)
    tree = StarredUnpackingTransformer().visit(raw_tree)
    expected = ast.parse("""
        [2] + list(range(10)) + [1]
    """)
    assert ast_equal(tree, expected)

    raw_tree = ast.parse("""
        [2, *range(10)]
    """)
    tree = StarredUnpackingTransformer().visit(raw_tree)
    expected = ast.parse("""
        [2] + list(range(10))
    """)
    assert ast_equal(tree, expected)

    raw_tree = ast.parse("""
        [*range(10), 1]
    """)
    tree = StarredUnpackingTransformer().vis

# Generated at 2022-06-14 02:19:30.739802
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    c = StarredUnpackingTransformer()
    node = ast.parse('[2, *range(10), 1]')
    node = c.visit(node)
    assert ast.dump(node) == 'Expr(value=BinOp(left=BinOp(left=List(elts=[Num(n=2)], ctx=Load()), right=Call(func=Name(id="list", ctx=Load()), args=[Call(func=Name(id="range", ctx=Load()), args=[Num(n=10)], keywords=[], starargs=None, kwargs=None)], keywords=[], starargs=None, kwargs=None), op=Add()), right=List(elts=[Num(n=1)], ctx=Load()), op=Add()))'  # noqa


# Unit

# Generated at 2022-06-14 02:19:35.739858
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Test StarredUnpackingTransformer.visit_Call"""

    # Assert utility function assert_that, see pylint: disable=unused-import
    from auto_everything.base import assert_that

    source = 'print(*range(1), *range(3))'
    tree = ast.parse(source, mode='exec')
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)

    expected = 'print(*(list(range(1)) + list(range(3))))'
    assert_that(ast.dump(tree)).is_equal_to(expected)

# Generated at 2022-06-14 02:19:48.506373
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[2, *range(10), 1]", mode="eval")
    expected = ast.parse("[2] + list(range(10)) + [1]", mode="eval")
    actual = StarredUnpackingTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)

    node = ast.parse("[2, *range(10), 1, *range(10)]", mode="eval")
    expected = ast.parse("[2] + list(range(10)) + [1] + list(range(10))", mode="eval")
    actual = StarredUnpackingTransformer().visit(node)
    assert ast.dump(expected) == ast.dump(actual)


# Generated at 2022-06-14 02:20:01.282940
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test.transformer_testing import expect
    from .test.transformer_testing import generate_call_node_by
    from .test.transformer_testing import generate_list_node_by

    # without arguments
    expect(StarredUnpackingTransformer, 'print()', 'print()')

    # outer call
    expect(StarredUnpackingTransformer,
    'print(1, *[2, 3], 4)',
    'print(*(list([2, 3]) + [4]))')

    # inner call
    expect(StarredUnpackingTransformer,
    'print(1, *[2, 3])',
    'print(*(list([2, 3])))')

    # multi-level

# Generated at 2022-06-14 02:20:07.539522
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class_visitCall = StarredUnpackingTransformer()
    ast_test_call = ast.parse('foo(a, *b, *c, d)')
    ast_result = class_visitCall.visit(ast_test_call)
    exec(compile(ast_result, filename="", mode="exec"))
    assert foo(*(list(b) + list(c))) == foo(*(list(b) + list(c)))

# Generated at 2022-06-14 02:20:14.365644
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """print(*range(4), *range(5), *range(6))"""
    expected_code = """print(*(list(range(4)) + list(range(5)) + list(range(6))))"""
    tree = ast.parse(code)
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)
    generated_code = ast.unparse(tree)
    assert generated_code == expected_code


# Generated at 2022-06-14 02:20:24.874523
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    node = ast.Call(func=ast.Name(id='print'),
            args=[ast.Starred(value=ast.Call(func=ast.Name(id='range'),
                                             args=[ast.Num(n=1)],
                                             keywords=[]),
                              ctx=ast.Load())],
            keywords=[])
    node = StarredUnpackingTransformer.run(node)
    assert node == ast.Call(func=ast.Name(id='print'),
            args=[ast.Starred(value=ast.List(elts=[ast.Call(func=ast.Name(id='range'),
                                             args=[ast.Num(n=1)],
                                             keywords=[])]), ctx=ast.Load())],
            keywords=[])


# Generated at 2022-06-14 02:20:30.788169
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    test = ast.parse('print(*(range(1)), *(range(3)))').body[0]
    correct = ast.parse('print(*list(range(1)) + list(range(3)))').body[0]
    assert transformer.visit(test) == correct


# Generated at 2022-06-14 02:20:39.125149
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def test_case(src, expected_src):
        expected_src = assert_import_visitor.visit_source(expected_src)
        src = assert_import_visitor.visit_source(src)
        assert isinstance(src, ast.Module)
        actual_src = StarredUnpackingTransformer().visit(copy.deepcopy(src))
        assert isinstance(actual_src, ast.Module)
        actual_src = StarredUnpackingTransformer().visit(actual_src)
        assert isinstance(actual_src, ast.Module)
        dump = ast.dump(ast.fix_missing_locations(actual_src))
        expected_src_dump = ast.dump(ast.fix_missing_locations(expected_src))
        print('--- expected:')
        print(expected_src_dump)

# Generated at 2022-06-14 02:20:43.873168
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    input_source = '[2, *range(10), 1]'
    output_source = '[2] + list(range(10)) + [1]'

    test_node = ast.parse(input_source).body[0]
    StarredUnpackingTransformer.run_test(test_node, output_source)


# Generated at 2022-06-14 02:20:49.839893
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import BaseTestTransformer
    from .test_data import test_unpacking_starred_data
    class TestStarredUnpackingTransformer(BaseTestTransformer):
        transform = StarredUnpackingTransformer().visit_List
    TestStarredUnpackingTransformer.test(test_unpacking_starred_data.TEST_CASES, test_unpacking_starred_data.TYPE_CASES)


# Generated at 2022-06-14 02:20:58.373870
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():

    # Create Node
    func = ast.Name(id='print')
    args = [ast.Name(id='*range(1)'), ast.Name(id='*range(3)')]
    node = ast.Call(
            func=func,
            args=args
    )

    # Initialize Transformer
    transformer = StarredUnpackingTransformer()

    # Visit node
    node = transformer.visit(node)

    # Check result
    assert node.args[0].value.left.func.id == 'range'
    assert node.args[0].value.right.func.id == 'range'
    assert node.args[0].value.left.keywords == []
    assert node.args[0].value.right.keywords == []
    assert node.args[0].value.left.args[0].n

# Generated at 2022-06-14 02:21:20.640711
# Unit test for constructor of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:21:28.874337
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:21:40.140342
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(2, *a, b, *c, 3, *d)")
    StarredUnpackingTransformer().visit(node)

# Generated at 2022-06-14 02:21:48.395806
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """__init__()"""
    node = ast.parse(
        """print(*range(1), *range(3))"""
    ).body[0]
    expected = ast.parse(
        """print(*(list(range(1)) + list(range(3))))"""
    ).body[0]
    print(expected)
    transformer = StarredUnpackingTransformer(None)
    actual = transformer.visit(node)
    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 02:21:53.435092
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    t = StarredUnpackingTransformer()
    assert ast.dump(t.visit(ast.parse("[2, *range(10), 1, *[1, 2]][0]"))) == ast.dump(ast.parse("list(range(10)) + [1, 2][0]"))


# Generated at 2022-06-14 02:22:00.060936
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import typed_astunparse
    import astunparse

    code = "[2, *range(10), 1]"
    expected_code = "[2] + list(range(10)) + [1]"

    tree = ast.parse(code)
    expected_tree = ast.parse(expected_code)

    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)

    assert typed_astunparse.unparse(tree) == astunparse.unparse(expected_tree)



# Generated at 2022-06-14 02:22:02.047832
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer() is not None


# Generated at 2022-06-14 02:22:06.552082
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import astpretty
    from .base import NodeTransformerTestCase
    from .transformers import LoopTransformer, FunctionTransformer
    tester = NodeTransformerTestCase()
    tester.test_ast(LoopTransformer())
    tester.test_ast(FunctionTransformer())
    tester.test_ast(StarredUnpackingTransformer())

# Generated at 2022-06-14 02:22:17.040600
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():

    try:
        if (sys.version_info >= (3, 5)):
            raise Exception
    except:
        print("SKIP")
        return

    node = ast.parse("a = [1, *b, 2]")
    node = ast.fix_missing_locations(node)
    trans = StarredUnpackingTransformer()
    trans.visit(node)
    #print(ast.dump(node))

# Generated at 2022-06-14 02:22:18.406915
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:22:36.704873
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    List_ = ast.parse(r'[1, *[1, 2], 3]').body[0].value
    StarredUnpackingTransformer().visit(List_)
    assert ast.dump(List_) == (
        "List(elts=[Num(n=1), Name(id='list', ctx=Load()), Starred(value=List(elts=[Num(n=1), Num(n=2)])), "
        "Num(n=3)], ctx=Load())"
    )

    List_ = ast.parse(r'[1, *(1, 2), 3]').body[0].value
    StarredUnpackingTransformer().visit(List_)

# Generated at 2022-06-14 02:22:45.838536
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    e = [[2, *range(10), 1]]
    assert StarredUnpackingTransformer().visit_List(ast.parse(repr(e)).body[0].value).body == [
        '_0 = [2, 1]',
        '_1 = list(range(10))',
        '_0 = (_0 + _1)',
        '_0',
    ]


# Generated at 2022-06-14 02:22:54.759345
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '''
print([1, 2, *range(3), *range(4, 6)])
'''
    expected = '''
print(([1, 2] + list(range(3)) + list(range(4, 6))))
'''
    node = ast.parse(source)
    transformed = StarredUnpackingTransformer().visit(node)
    actual = ast.unparse(transformed)
    assert actual == expected

    source = '''
print([2])
'''
    expected = '''
print([2])
'''
    node = ast.parse(source)
    transformed = StarredUnpackingTransformer().visit(node)
    actual = ast.unparse(transformed)
    assert actual == expected



# Generated at 2022-06-14 02:23:03.813500
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    class Foo:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    class Bar:
        def __init__(self, foo):
            self.foo = foo

    class Baz:
        def __init__(self, foo):
            self.foo = foo

    x = Foo(1, 2, 3)
    y = Bar(x)
    z = Baz(y)

    l = [1, 2, 3, *[4, 5, 6], 7, *[8, 9, 10]]
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    l = [1, 2, 3, *(1, 2, 3), 4, *(1, 2, 3)]


# Generated at 2022-06-14 02:23:13.848270
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from . import TestCase
    from .util import parse
    import astor

    class Test(TestCase):

        def setUp(self):
            self.transformer = StarredUnpackingTransformer()

        def test_ok_empty_list(self):
            tree = parse("[]")
            self.transformer.visit(tree)
            self.assertEqual("[]", astor.to_source(tree))

        def test_ok_no_starred_list(self):
            tree = parse("[1, 2, 3]")
            self.transformer.visit(tree)
            self.assertEqual("[1, 2, 3]", astor.to_source(tree))

        def test_ok_empty_starred_list(self):
            tree = parse("[*[]]")
            self.trans

# Generated at 2022-06-14 02:23:24.329595
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_code = '''[2, *range(10), 1]'''
    expected_code = '''[2] + list(range(10)) + [1]'''
    code_tree = ast.parse(test_code)  # type: ignore
    tree_transformer = StarredUnpackingTransformer()
    new_tree = tree_transformer.visit(code_tree)  # type: ignore
    generated_code = ast.unparse(new_tree)
    assert generated_code == expected_code



# Generated at 2022-06-14 02:23:29.728897
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = "[4, *range(1), 10]"
    expected = "4 + list(range(1)) + [10]"
    assert expected == compile_snippet(src, StarredUnpackingTransformer)


# Generated at 2022-06-14 02:23:38.448664
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse(dedent('''
        [2, *range(10), 1]
        '''))
    node = StarredUnpackingTransformer().visit(node)

# Generated at 2022-06-14 02:23:50.128996
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert compile(
        '[2, *range(10), 1]', '', 'eval', ast.PyCF_ONLY_AST).body[0] == ast.List(
        elts=[ast.Num(n=2), ast.Starred(value=ast.Call(
            func=ast.Name(id='range'),
            args=[ast.Num(n=10)],
            keywords=[])), ast.Num(n=1)],
        ctx=ast.Load())

    # Second case will have `left` and `right` nodes with **many** fields,
    # that's why we just compare bytecode.

# Generated at 2022-06-14 02:23:57.195759
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    test = ast.parse('''
a = [2, *range(10), 1]
    ''')

    c = StarredUnpackingTransformer()
    c.run(test)

    expected = ast.parse('''
a = [2] + list(range(10)) + [1]
    ''')

    assert ast.dump(test) == ast.dump(expected)


# Generated at 2022-06-14 02:24:10.238289
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer([])
    tree = ast.parse("[2, *range(10), 1]")
    expected_tree = ast.parse("[2] + list(range(10)) + [1]")
    new_tree = transformer.visit(tree)
    assert ast.dump(expected_tree) == ast.dump(new_tree)


# Generated at 2022-06-14 02:24:16.393903
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_text = '[2, *range(10), 1]'
    ast_tree = ast.parse(test_text)
    expected_text = '[2] + list(range(10)) + [1]'
    expected_tree = ast.parse(expected_text)
    StarredUnpackingTransformer(debug=False).visit(ast_tree)
    assert ast_tree == expected_tree


# Generated at 2022-06-14 02:24:21.008173
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tr = StarredUnpackingTransformer()
    node = ast.parse("[2, *range(10), 1]")
    actual = tr.visit(node)
    expected = ast.parse("([2] + list(range(10)) + [1])")
    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 02:24:25.045862
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import LazyScript
    script = LazyScript("[2, *range(10), 1]")
    node = StarredUnpackingTransformer().visit(script.ast)
    assert isinstance(node, ast.Module)
    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.Expr)
    assert isinstance(node.body[0].value, ast.BinOp)
    assert isinstance(node.body[0].value.left, ast.BinOp)
    assert isinstance(node.body[0].value.left.right, ast.Call)
    assert isinstance(node.body[0].value.right, ast.List)
    assert len(node.body[0].value.right.elts) == 1



# Generated at 2022-06-14 02:24:29.641029
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import BaseNodeTransformerTestCase

    class TestCase(BaseNodeTransformerTestCase):
        transformer = StarredUnpackingTransformer
        code = '[1, *range(2), 3]'
        expected = '[1] + list(range(2)) + [3]'

    return TestCase


# Generated at 2022-06-14 02:24:34.687306
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    input_text = '[2, *range(10), 1]'
    expected_text = '[2] + list(range(10)) + [1]'
    compiler = StarredUnpackingTransformer()
    result = compiler.visit_List(ast.parse(input_text).body[0].value)
    output_text = ast.unparse(result).strip()
    assert expected_text == output_text

# Generated at 2022-06-14 02:24:40.781495
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3 as ast
    import astunparse

    module = ast.parse("[2, *range(10), 1]")
    module = StarredUnpackingTransformer().visit(module)
    assert astunparse.unparse(module) == "[2] + list(range(10)) + [1]\n"


# Generated at 2022-06-14 02:24:51.448819
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer"""
    from ..util import parse_to_ast, unparse
    from .binop_to_function_call import BinOpToFunctionCallTransformer
    from ..ctx import Ctx
    from .type_comment import TypeCommentTransformer

    node = parse_to_ast("""
    [2, *range(10), 1, 1, 2, 3, 4] + [1, 1, 2, 3, 4, 5]
    """)
    result = StarredUnpackingTransformer(Ctx()).visit(node)
    assert unparse(result) == """
    ([2] + list(range(10)) + [1, 1, 2, 3, 4]) + list([1, 1, 2, 3, 4, 5])
    """

    # Ideally type comments

# Generated at 2022-06-14 02:25:04.129707
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[2, *range(10), 1]"
    root = ast.parse(source)
    tr = StarredUnpackingTransformer()
    tr.visit(root)
    assert tr._tree_changed

# Generated at 2022-06-14 02:25:10.466085
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_helpers import assert_equal_ast
    from .test_helpers import assert_tree_changed, assert_tree_not_changed

    # only one Starred
    tree = ast.parse('[1, *range(2), 3]')
    expected = ast.parse('[1] + list(range(2)) + [3]')
    transformer = StarredUnpackingTransformer()
    assert_tree_changed(transformer, tree)
    assert_equal_ast(transformer.visit(tree), expected)

    # two Starred
    tree = ast.parse('[1, *range(2), 3, *range(4)]')
    expected = ast.parse('[1] + list(range(2)) + [3] + list(range(4))')
    transformer = StarredUnpackingTransformer()
   

# Generated at 2022-06-14 02:25:24.757827
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    uut = StarredUnpackingTransformer()
    text = '[1, *range(10), 2]'
    ast_module, tree_changed = uut.transform_tree(text)
    assert tree_changed
    ast_module_expected = ast.parse(
        '_sum([1], list(range(10)), [2])')
    assert ast.dump(
        ast_module_expected) == ast.dump(ast_module), "Wrong result!"


# Generated at 2022-06-14 02:25:33.256702
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    expected = ast.parse(
        'x = [2] + list(range(10)) + [1]\n'
        'print(*(list(range(1)) + list(range(3))))\n')

    code = ast.parse('x = [2, *range(10), 1]\nprint(*range(1), *range(3))\n')
    StarredUnpackingTransformer().visit(code)

    assert ast.dump(code) == ast.dump(expected)

# Generated at 2022-06-14 02:25:43.996534
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # test 1
    print("test StarredUnpackingTransformer_visit_Call 1")
    input_code = "print(*range(1), *range(2))"
    expected_code = "print(*(list(range(1)) + list(range(2))))"
    tree = ast.parse(input_code)
    StarredUnpackingTransformer().visit(tree)
    result_code = astor.to_source(tree).strip()
    assert result_code == expected_code

    # test 2
    print("test StarredUnpackingTransformer_visit_Call 2")
    input_code = "print(print(*range(1), *range(2)), 1)"
    expected_code = "print(print(*(list(range(1)) + list(range(2)))), 1)"

# Generated at 2022-06-14 02:25:55.008184
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[
            ast.Name(id='None'),
            ast.Starred(
                value=ast.List(elts=[
                    ast.Name(id='x'),
                    ast.Name(id='y')
                ])
            )
        ],
        keywords=[]
    )


# Generated at 2022-06-14 02:25:55.882156
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    pass

# Generated at 2022-06-14 02:26:00.202766
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    compile = StarredUnpackingTransformer().visit_List
    assert compile(ast.parse('[2, *range(10), 1]', mode='eval').body) == ast.parse('[2] + list(range(10)) + [1]', mode='eval').body
    assert compile(ast.parse('[2, 1]', mode='eval').body) == ast.parse('[2, 1]', mode='eval').body


# Generated at 2022-06-14 02:26:10.417169
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[2, *range(10), 1]').body[0].value
    result = StarredUnpackingTransformer().visit(node)
    assert ast.dump(result, include_attributes=False) == \
        'BinOp(left=List(elts=[Num(n=2)], ctx=Load()), ' \
        'right=BinOp(left=Call(func=Name(id=\'list\', ctx=Load()), ' \
        'args=[Call(func=Name(id=\'range\', ctx=Load()), args=[Num(n=10)], ' \
        'keywords=[])], keywords=[]), ' \
        'right=List(elts=[Num(n=1)], ctx=Load()), op=Add()), op=Add())'


# Generated at 2022-06-14 02:26:22.559247
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(*range(1), *range(3))')
    assert isinstance(node, ast.Module)
    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.Expr)
    call = node.body[0].value

    assert isinstance(call, ast.Call)
    assert call.args == [
        ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load()),
        ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load())]
    assert call.func == ast.Name(id='print', ctx=ast.Load())


# Generated at 2022-06-14 02:26:26.125784
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_tools import assert_transformed_ast

    ast_ = ast.parse('[2, *range(10), 1]')

    class_ = StarredUnpackingTransformer
    func_ = class_.visit_List
    assert_transformed_ast(ast_, class_, func_)



# Generated at 2022-06-14 02:26:38.180516
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    list_ = ast.parse('[2, *range(10), 1]').body[0].value
    assert isinstance(list_, ast.List)
    assert len(list_.elts) == 3

    new_list = StarredUnpackingTransformer().visit(list_)
    assert isinstance(new_list, ast.Call)

    assert isinstance(new_list.func, ast.Name)
    assert new_list.func.id == 'list'
    assert len(new_list.args) == 1
    assert len(new_list.keywords) == 0

    assert isinstance(new_list.args[0], ast.BinOp)
    assert isinstance(new_list.args[0].op, ast.Add)
    assert isinstance(new_list.args[0].left, ast.List)

# Generated at 2022-06-14 02:26:55.862723
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
for i in range(4):
    print(*range(i), end='*\n')
"""
    target = """
for i in range(4):
    print(*(list(range(i))), end='*\n')
"""
    result = next(compile_source(source, StarredUnpackingTransformer, 3)).strip()
    assert result == target.strip()


# Generated at 2022-06-14 02:27:00.116272
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .base import BaseNodeTransformer
    from .get_code import get_code
    from .uncompyle import uncompyle

    class NodeTransformer(BaseNodeTransformer):
        pass

    tree = NodeTransformer(ast.parse(get_code('example.py'))).tree

    tree = StarredUnpackingTransformer(tree).tree

    assert "print(*(list(range(1)) + list(range(3))))" in uncompyle(tree)