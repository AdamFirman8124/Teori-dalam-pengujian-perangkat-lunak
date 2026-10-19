

# Generated at 2022-06-14 02:17:04.747343
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:17:08.299854
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .base import BaseNodeTransformer
    assert issubclass(StarredUnpackingTransformer, BaseNodeTransformer)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:17:19.494790
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = "[2, *range(10), 1]"
    dst = "[2] + list(range(10)) + [1]"
    assert StarredUnpackingTransformer().visit(ast.parse(src)).body[0].value.s == dst

    src = "[2, *[4, 5, 6], 1]"
    dst = "[2] + list([4, 5, 6]) + [1]"
    assert StarredUnpackingTransformer().visit(ast.parse(src)).body[0].value.s == dst

    src = "[2, *range(10), *range(10), 1]"
    dst = "[2] + list(range(10)) + list(range(10)) + [1]"
    assert StarredUnpackingTransformer().visit(ast.parse(src)).body[0].value.s == dst

    src

# Generated at 2022-06-14 02:17:32.612781
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_helpers import get_node
    from .test_helpers import dump_to_dummy_module
    from .test_helpers import get_source_from_node
    import re

    source = """\
    list(1, *range(2), *range(1))
    foo(42, *range(2), *range(1))
    foo(42, *range(2), *range(1), bah=1, *range(3))
    foo(42, *range(2), *range(1), bah=1, *range(3), sep=',', *range(4))
    foo(42, *range(2), *range(1), *range(3), bah=1, *range(5), a=5)
    """


# Generated at 2022-06-14 02:17:42.529042
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    print("method StarredUnpackingTransformer.visit_Call")
    t = StarredUnpackingTransformer()
    call = ast.Call(func=ast.Name(id='print'),
                    args=[ast.Starred(value=ast.List(elts=[ast.Num(n=1),ast.Num(n=2),ast.Num(n=3)], ctx=ast.Load())),ast.Starred(value=ast.List(elts=[ast.Num(n=4),ast.Num(n=5),ast.Num(n=6)], ctx=ast.Load()))],
                    keywords=[])

# Generated at 2022-06-14 02:17:51.923755
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast as ast3
    from .base import BaseNodeTransformer, transform
    from . import _specs as specs

    class _StarredUnpackingTransformer(BaseNodeTransformer):
        """Compiles:
            [2, *range(10), 1]
            print(*range(1), *range(3))
        To:
            [2] + list(range(10)) + [1]
            print(*(list(range(1)) + list(range(3))))

        """
        target = (3, 4)

        def _has_starred(self, xs: List[ast3.expr]) -> bool:
            for x in xs:
                if isinstance(x, ast3.Starred):
                    return True

            return False


# Generated at 2022-06-14 02:18:02.423608
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from tests.compiler.CompilerTestCase import CompilerTestCase

    class Test(CompilerTestCase):
        __fixture__ = 'compiler'

        def test__visit_Call_with_starred_argument(self):
            node = ast.parse("compile(x, z, os.path.join('a', 'b'), x)", mode='eval')
            sut = StarredUnpackingTransformer()

            result = list(sut.visit(node))

            self.assertEqual(len(result), 1)
            self.assertIsInstance(result[0], ast.Call)
            call = result[0]
            self.assertIsInstance(call.args[0], ast.Name)
            self.assertIsInstance(call.args[1], ast.Name)

# Generated at 2022-06-14 02:18:12.695943
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
        print("0", *range(10), "1")
        print("0", *range(1), *range(3), "1")
    """
    expected = """
        print(*(['0'] + list(range(10)) + ['1']))
        print(*(['0'] + list(range(1)) + list(range(3)) + ['1']))
    """
    result = str(StarredUnpackingTransformer().visit(ast.parse(code)))
    assert result == expected


# Generated at 2022-06-14 02:18:14.229571
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:18:18.587452
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tr = StarredUnpackingTransformer()
    node = ast.parse('[2, *range(10)]', mode='eval').body
    expected = ast.parse('[2] + list(range(10))', mode='eval').body

    result = tr.visit(node)

    assert result == expected


# Generated at 2022-06-14 02:18:29.589811
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class_obj = StarredUnpackingTransformer()
    
    assert_equal(
        class_obj.visit_Call(ast.parse('print(*range(10))').body[0].value),
        ast.parse('print(*(list(range(10))))').body[0].value
    )
    
    assert_equal(
        class_obj.visit_Call(ast.parse('print(range(10))').body[0].value),
        ast.parse('print(range(10))').body[0].value
    )
    

# Generated at 2022-06-14 02:18:34.557653
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    node = astor.parse_expr("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    assert astor.to_source(node) == astor.to_source(astor.parse_expr("[2] + list(range(10)) + [1]"))


# Generated at 2022-06-14 02:18:41.058614
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast.ast3 import parse
    import astpretty

    tree = parse("""
    print(*range(3), *range(3))
    print(*range(3))
    print(1, *[2, *range(3), 4], 5)
    """)
    astpretty.pprint(tree)

    StarredUnpackingTransformer().visit(tree)
    print()

    astpretty.pprint(tree)


# Generated at 2022-06-14 02:18:46.909772
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_data = [
        ('''print(*range(1), *range(3))''', '''print(*(list(range(1)) + list(range(3))))'''),
        ('''x = *range(1), *range(3); print(x)''', '''x = *(list(range(1)) + list(range(3))); print(x)'''),
        ('''y = range(1), range(3); print(y)''', '''y = range(1), range(3); print(y)'''),
        ('''foo(*range(1), *range(3))''', '''foo(*(list(range(1)) + list(range(3))))'''),
    ]
    for test_string, correct_string in test_data:
        t = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:18:49.691152
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    st = StarredUnpackingTransformer()
    assert not st._tree_changed
    assert st._trees == tuple()
    assert st._filename == ""


# Generated at 2022-06-14 02:18:54.085422
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # given
    source = """
    [2, *range(10), 1]
    """
    compiled = """
    [2] + list(range(10)) + [1]
    """
    expected = ast.parse(compiled)

    # when
    tree = ast.parse(source)
    StarredUnpackingTransformer(tree).visit(tree)

    # then
    assert ast.dump(expected) == ast.dump(tree)



# Generated at 2022-06-14 02:19:00.403387
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '''
        [2, *range(10), 1]
    '''
    expected = '''
        [2] + list(range(10)) + [1]
    '''

    tree = ast.parse(source)
    expected_tree = ast.parse(expected)
    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree)
    assert compare_ast(tree, expected_tree)


# Generated at 2022-06-14 02:19:01.698566
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:19:10.007234
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
    print(*range(10), *range(4))
    """
    tree = ast.parse(code)
    tree = StarredUnpackingTransformer.run_on_tree(tree)
    print('%%%%%%%%%%%%%%%%%%%%%%%')
    print(astor.to_source(tree))
    print('%%%%%%%%%%%%%%%%%%%%%%%')

    # old code
    def_old = """
    print(*(list(range(10)) + list(range(4))))
    """
    tree_old = ast.parse(def_old)
    print('%%%%%%%%%%%%%%%%%%%%%%%')
    print(astor.to_source(tree_old))
    print('%%%%%%%%%%%%%%%%%%%%%%%')
    assert astor.to_source(tree) == astor.to_source(tree_old)

# Generated at 2022-06-14 02:19:11.501574
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """Create instance of class StarredUnpackingTransformer."""
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:19:23.091560
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    code = """\
[2, *range(10), 1]
print(*range(1), *range(3))
"""
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:19:33.802557
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from typed_ast import ast3
    from .testutils import round_trip
    from .testutils import assert_equal

    def check(before, after):
        """Assert AST and `before` and `after` are equal"""
        after = ast3.parse(after)
        before = ast3.parse(before)
        transformer = StarredUnpackingTransformer()
        after = transformer.visit(after)
        assert_equal(before, after)
        round_trip(before, StarredUnpackingTransformer)

    check("[2, *range(10), 1]", "[2] + list(range(10)) + [1]")
    check("print(*range(1), *range(3))", "print(*(list(range(1)) + list(range(3))))")

# Generated at 2022-06-14 02:19:44.504033
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node_list_of_args = ast.List(elts=[
        ast.Call(func=ast.Name(id='list'), args=[ast.Name(id='v')], keywords=[]),
        ast.Starred(value=ast.Name(id='v2')),
        ast.Str(s='v3'),
        ast.Starred(value=ast.Name(id='v4'))])

# Generated at 2022-06-14 02:19:50.944808
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = """
        [2, *range(10), 1]
    """
    expected = """
        [2] + list(range(10)) + [1]
    """
    assert expected == run_transformer(StarredUnpackingTransformer, source)


# Generated at 2022-06-14 02:19:54.429230
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    sut = StarredUnpackingTransformer(verbose=True)
    assert sut is not None, "constructor of class StarredUnpackingTransformer"

# Generated at 2022-06-14 02:20:04.164003
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import unittest
    import textwrap
    from typed_ast import ast3 as ast
    from .testutils import assert_node_equal, has_changed
    class Test(unittest.TestCase):
        def _test(self, code: str, expected_code: str):
            node = ast.parse(textwrap.dedent(code))
            transpiled = StarredUnpackingTransformer().visit(node)
            expected_node = ast.parse(textwrap.dedent(expected_code))
            assert_node_equal(transpiled, expected_node)
            self.assertTrue(has_changed(transpiled))
        def test_01(self):
            code = """\
            def foo():
                print(*range(1), *range(3))\
            """

# Generated at 2022-06-14 02:20:12.306269
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("f(*range(0), *range(3))", mode='eval').body
    expected = ast.parse("f(*list(range(0)) + list(range(3)))", mode='eval').body

    transformer = StarredUnpackingTransformer()
    result = transformer.visit(node)

    assert isinstance(result, ast.Call), "Result type is not Call"
    assert result == expected


# Generated at 2022-06-14 02:20:24.071309
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Given
    SOURCE = """
    func('a', 'b', *args, 'c', *args, 'd')
    """
    module = ast.parse(SOURCE)

    # When
    result = module.body[0]
    result = StarredUnpackingTransformer().visit(result)

    # Then

# Generated at 2022-06-14 02:20:36.514019
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_helpers import assert_equal_ast

    expected = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Starred(value=ast.List(elts=[ast.List(elts=[], ctx=ast.Load()), ast.List(elts=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)], ctx=ast.Load())]))],
        keywords=[],
        starargs=None,
        kwargs=None,
    )

# Generated at 2022-06-14 02:20:46.116213
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Create a Python AST for:
    # [2, *range(10), 1]
    ast1 = ast.parse("[2, *range(10), 1]", mode="eval")
    # Create a Python AST for:
    # [2] + list(range(10)) + [1]
    ast2 = ast.parse("[2] + list(range(10)) + [1]", mode="eval")
    t = StarredUnpackingTransformer()
    node = ast.fix_missing_locations(t.visit(ast1))
    assert ast.dump(node) == ast.dump(ast.fix_missing_locations(ast2))


# Generated at 2022-06-14 02:20:55.254933
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[2, *range(10), 1]"
    tree = ast.parse(source)

    expected = "[2] + list(range(10)) + [1]"
    expected_tree = ast.parse(expected)

    assert StarredUnpackingTransformer().visit(tree) == expected_tree


# Generated at 2022-06-14 02:21:03.136283
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(*range(1), *range(3))").body[0]
    assert isinstance(node, ast.Expr)
    node = node.value
    assert isinstance(node, ast.Call)
    assert len(node.args) == 2
    assert isinstance(node.args[0].value, ast.Call)
    assert isinstance(node.args[1].value, ast.Call)

# Generated at 2022-06-14 02:21:08.891100
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .util import ast_compare

    source = """\
    foo(*(bar + baz))
    """
    expected = """\
    foo(*list(bar + baz))
    """

    tree = ast.parse(source)
    transformed = StarredUnpackingTransformer().visit(tree)
    ast_compare(transformed.body[0], expected)



# Generated at 2022-06-14 02:21:21.167070
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from shivyc.compile_ast import compile_ast
    from shivyc.transformer import Transformer
    from shivyc.transformer.test_utils import transform

    # Simple test 1
    source = "[1, *range(10), 2]"
    result = transform(source, StarredUnpackingTransformer)
    assert result == '[1] + list(range(10)) + [2]'

    # Simple test 2
    source = '[*range(10), 1]'
    result = transform(source, StarredUnpackingTransformer)
    assert result == 'list(range(10)) + [1]'

    # Compile list
    source = "[1, *range(10), 2]"
    result = transform(source, Transformer)

# Generated at 2022-06-14 02:21:31.689470
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    program = '''
[2, *range(10), 1]
'''
    expected_program = '''
[2] + list(range(10)) + [1]
'''

    tree = ast.parse(program)
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)

    print(ast.dump(tree))
    assert ast.dump(tree) == expected_program

    expected_tree = ast.parse(expected_program)
    assert ast.dump(tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 02:21:39.684342
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    classTree = ast.parse('''
    def f(x, y, z):
        print(x, y, z)
    ''')
    callTree = ast.parse('f(*range(3))')
    transformer = StarredUnpackingTransformer()
    transformer.transform(callTree)
    exec(compile(callTree, '<string>', 'exec'), {}, {'range': range})
    exec(compile(classTree, '<string>', 'exec'), {}, {'range': range})
    return None

# Generated at 2022-06-14 02:21:40.916258
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:21:53.385867
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from textwrap import dedent

    def _test(src: str, expected: str):
        tree = ast.parse(dedent(src))
        transformer = StarredUnpackingTransformer()
        tree = transformer.visit(tree)
        assert transformer._tree_changed is True
        assert ast.dump(tree) == dedent(expected).strip()

    _test("""
    [1, 2, *range(10), 1, 2, 3]
    """, """
    [1, 2] + list(range(10)) + [1, 2, 3]
    """)


# Generated at 2022-06-14 02:22:03.684729
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    class Dummy(StarredUnpackingTransformer):
        def _has_starred(self, xs):
            return True

        def _split_by_starred(self, xs):
            return [[1], [2], [3], [ast.Starred(value=4)], [5]]

        def _prepare_lists(self, xs):
            return [ast.List(elts=[1]), ast.Call(func=ast.Name(id='list'), args=[4])]

        def _merge_lists(self, xs):
            return ast.Call(func=ast.Name(id='result'), args=[], keywords=[])

        def _to_sum_of_lists(self, xs):
            return ast.Call(func=ast.Name(id='sum_of_lists'), args=[], keywords=[])

# Generated at 2022-06-14 02:22:09.378573
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    b = StarredUnpackingTransformer()
    a = ast.List(elts=[ast.Num(1), ast.Starred(ast.Num(2))])
    b.visit(a)
    print(ast.dump(a))

    y = ast.Call(func=ast.Name("print"), args=[ast.Starred(ast.Num(2))])
    b.visit(y)
    print(ast.dump(y))

# Generated at 2022-06-14 02:22:22.136588
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # *a, b -> [a, b]
    node = ast.Call(func=ast.Name(id='fun'), args=[ast.Starred(value=ast.Name(id='a'), ctx=ast.Load()), ast.Name(id='b')], keywords=[])
    transformer = StarredUnpackingTransformer()
    new_node = transformer.visit(node)
    assert transformer._tree_changed == True
    assert isinstance(new_node, ast.Call)
    assert isinstance(new_node.args[0], ast.Starred)
    assert isinstance(new_node.args[0].value, ast.BinOp)
    assert isinstance(new_node.args[0].value.left, ast.List)

# Generated at 2022-06-14 02:22:31.592773
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # type: () -> None
    with open('tests/data/list_unpacking.py') as fp:
        ast_text = fp.read()
    node = ast.parse(ast_text)
    trans = StarredUnpackingTransformer()
    trans.visit(node)

# Generated at 2022-06-14 02:22:37.288435
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    import ast

    source = 'print(1, *range(1), *range(3))'
    node = ast.parse(source)

    expected = ('print(*(list(range(1)) + list(range(3))))')
    StarredUnpackingTransformer().visit(node)
    #print(astor.to_source(node))
    assert expected == astor.to_source(node)

# Generated at 2022-06-14 02:22:52.835088
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import parse
    from .base import NodeTransformerPassTestCase, transform
    from .nodes import transform_specific_nodes, StarredUnpackingTransformer

    class TestCase(NodeTransformerPassTestCase):
        transformer = StarredUnpackingTransformer()
        transform = transform

    class Test(TestCase):
        def runTest(self):
            src = "print(*range(1), *range(3))"
            dst = "print(*(list(range(1)) + list(range(3))))"
            self.assertEqual(self.transform(src), dst)

    class Test2(TestCase):
        def runTest(self):
            src = "print(1, *range(3), *range(10), 100)"

# Generated at 2022-06-14 02:23:02.880370
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .. import compile_source, NativeCodeGenerator
    unpacker = StarredUnpackingTransformer()
    c = compile_source('print(*range(10), *range(1, 3), *range(2))')
    unpacker.visit(c)
    assert unpacker.tree_changed
    c = NativeCodeGenerator.to_source(c)
    assert c == """\
print(*(list(range(10)) + list(range(1, 3)) + list(range(2))))"""



# Generated at 2022-06-14 02:23:14.656099
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Test the method visit_Call of the class StarredUnpackingTransformer

    test input:
        f(a, *b, c)
        f(a, *hotel, *babel)
    expected output:
        f(*(list(a) + list(b) + list(c)))
        f(*(list(a) + list(hotel) + list(babel)))
    """

    # test input
    _node_call_first = ast.parse(
        """
        f(a, *b, c)
        """
    ).body[0].value
    type(_node_call_first).__name__ == 'Call'

    _node_call_second = ast.parse(
        """
        f(a, *hotel, *babel)
        """
    ).body[0].value


# Generated at 2022-06-14 02:23:27.407602
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source_code = """
    print(*range(1), *range(3))
    print(*range(1), *range(3), end=';')
    """
    expected_code = """\
    print(*(list(range(1)) + list(range(3))))
    print(*(list(range(1)) + list(range(3))), end=';')
    """
    SourceCode = namedtuple('SourceCode', 'code')
    source_code = SourceCode(code=source_code)
    expected_code = SourceCode(code=expected_code)
    actual_code = StarredUnpackingTransformer().transform_code(source_code)
    assert actual_code == expected_code
    print(actual_code.code)



# Generated at 2022-06-14 02:23:37.059465
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import typed_ast.ast3 as ast
    from .transpile_test_case import transpile_TestCase
    import unittest

    class test_StarredUnpackingTransformer_visit_Call(transpile_TestCase):
        def test_1(self):
            tree = ast.parse("""
                print(*range(1), *range(3))
            """)

            node = tree.body[0].value

# Generated at 2022-06-14 02:23:43.459518
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    code = """
True if (1 in {2: 3, 4: 5, 6: 7}
        ) else False
    """
    t = ast.parse(code)
    StarredUnpackingTransformer().visit(t)
    assert astor.to_source(t) == """
True if (1 in _ast_transformer_dummy_2
        ) else False
    """

# Generated at 2022-06-14 02:23:52.411007
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("""
    print(*range(1), *range(3))
    """).body

    trans = StarredUnpackingTransformer()
    trans.visit(node)

    assert ast.dump(node) == "[Call(func=Name(id='print'), args=[Starred(value=BinOp(left=Call(func=Name(id='list'), args=[Call(func=Name(id='range'), args=[Num(n=1)], keywords=[])], keywords=[])), right=Call(func=Name(id='list'), args=[Call(func=Name(id='range'), args=[Num(n=3)], keywords=[])], keywords=[])), op=Add()), keywords=[]]"

# Generated at 2022-06-14 02:24:15.063597
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Test for list with no starred
    unpacked = 'x, y, z'
    code = f'[{unpacked}]'
    expected_code = code
    expected_output = ast.parse(expected_code)
    actual_output = StarredUnpackingTransformer().visit(ast.parse(code))
    assert ast.dump(expected_output) == ast.dump(actual_output)

    # Test for list with starred
    unpacked = 'a, b, *c, d'
    code = f'[{unpacked}]'
    expected_code = f'[a, b] + list(c) + [d]'
    expected_output = ast.parse(expected_code)
    actual_output = StarredUnpackingTransformer().visit(ast.parse(code))
    assert ast.dump(expected_output)

# Generated at 2022-06-14 02:24:24.712715
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    def do_test(input, expected_output):
        node = ast.parse(input)
        transformer = StarredUnpackingTransformer()
        transformed_node = transformer.visit(node)
        assert ast.dump(transformed_node) == expected_output

    do_test('[*range(10)]', 'Module(body=[Expr(value=Call(func=Name(id=list, ctx=Load()), args=[Call(func=Name(id=range, ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[]))])')

# Generated at 2022-06-14 02:24:26.091575
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:24:32.196190
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_code = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    new_tree = transformer.visit(test_code)
    expected_tree = ast.parse("[2] + list(range(10)) + [1]")
    assert ast.dump(new_tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 02:24:35.179934
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    '''Unit test for constructor of class StarredUnpackingTransformer'''
    x = StarredUnpackingTransformer()
    assert(x.__class__.__name__ == "StarredUnpackingTransformer")

# Generated at 2022-06-14 02:24:42.960417
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('foo(1, 2, 3, bar, 4, 5)')
    node = StarredUnpackingTransformer().visit(node)
    expected = ast.parse('foo(*([1, 2, 3] + list(bar) + [4, 5]))')
    assert ast.dump(node, annotate_fields=False) == ast.dump(expected, annotate_fields=False)



# Generated at 2022-06-14 02:24:51.558944
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from astor import unparse
    from .ast_helpers import compile_as_module

    code = '[2, *range(10), 1]'
    ast_module = compile_as_module(code)
    ast.fix_missing_locations(ast_module)

    new_ast_module = StarredUnpackingTransformer().visit(ast_module)
    print(unparse(new_ast_module))
    assert unparse(new_ast_module) == '__globals__ = {}\nlist(range(10)) + [2] + [1]\n'


# Generated at 2022-06-14 02:24:57.269275
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    node = ast.parse('print(5, *range(1), *range(5))')
    t.visit(node)
    assert 'print(*(list(range(1)) + list(range(5))))' == ast.unparse(node)

# Generated at 2022-06-14 02:25:02.286802
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('''print(*range(1), *range(3))''')
    node_transformer = StarredUnpackingTransformer()
    node_transformer.visit(tree)
    assert 'print(*(list(range(1)) + list(range(3))))' == ast.dump(tree)


# Generated at 2022-06-14 02:25:14.126992
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import sys
    import ast
    source = open("test/test_sources/StarredUnpackingTransformer_visit_Call.py", "r").read()
    expected = open("test/test_sources/StarredUnpackingTransformer_visit_Call.expected.py", "r").read()
    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)
    compiled = compile(tree, filename="<ast>", mode="exec")
    namespace = {}
    exec(compiled, namespace)
    assert namespace["result"] == expected


# Generated at 2022-06-14 02:25:40.900600
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    stars = StarredUnpackingTransformer()
    test = ast.parse("[2, *range(10), 1]")
    test_res = ast.parse("[2] + list(range(10)) + [1]")
    result = stars.visit(test)
    assert ast.dump(result) == ast.dump(test_res)


# Generated at 2022-06-14 02:25:44.994295
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '[2, *range(10), 1]'
    check_source(StarredUnpackingTransformer, source, '[2] + list(range(10)) + [1]')


# Generated at 2022-06-14 02:25:55.800915
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Test function (1)
    # Test case (1.1)
    node_List_1 = ast.parse('[2, *range(10), 1]').body[0].value
    # Expected result (1.1)
    expected1 = ast.BinOp(
        left=ast.List(elts=[ast.Num(n=2)]),
        right=ast.BinOp(
            left=ast.Call(
                func=ast.Name(id='list'),
                args=[ast.Name(id='range')],
                keywords=[ast.keyword(arg='start', value=ast.Num(n=10))]),
            right=ast.List(elts=[ast.Num(n=1)]),
            op=ast.Add()),
        op=ast.Add())
    # Test code (1.

# Generated at 2022-06-14 02:26:04.193128
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expected_result = ast.parse("[2, 4, 6, 8, 10] + [12, 14] + [1]")
    input = "[2, *range(2, 12, 2), *range(12, 15), 1]"
    input_tree = ast.parse(input)
    transformed_tree = StarredUnpackingTransformer(input_tree)
    assert ast.dump(expected_result) == ast.dump(transformed_tree.tree)


# Generated at 2022-06-14 02:26:11.246238
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    for i in range(4):
        expr = ast.parse(
            '[2, *range(10), *[1, 2], *range(5), 1]',
            mode='eval').body
        assert isinstance(expr, ast.List)
        StarredUnpackingTransformer().visit(expr)
        calc = compile(ast.Expression(body=expr), '', mode='eval')
        assert eval(calc) == [2] + list(range(10)) + [1, 2] + list(range(5)) + [1]  # type: ignore

# Generated at 2022-06-14 02:26:23.518215
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[
            ast.List(elts=[
                ast.Num(n=1),
                ast.Starred(value=ast.Name(id='range', ctx=ast.Load())),
            ], ctx=ast.Load())
        ],
        keywords=[])

    node = StarredUnpackingTransformer().visit(node)

# Generated at 2022-06-14 02:26:28.810303
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    with open('tests/samples/test_StarredUnpackingTransformer_visit_Call.py') as test_file:
        tree = ast.parse(test_file.read())
        StarredUnpackingTransformer(tree).visit(tree)
        assert codegen.to_source(tree).strip() == """\
print(*(list(range(1)) + list(range(3))))
a = *[1, *range(10), 2]"""


# Generated at 2022-06-14 02:26:37.107581
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse(
        '[2, *range(10), 1]'
    )
    expr = tree.body[0]
    xs = StarredUnpackingTransformer().visit(expr)   # type: ast.List
    assert xs.elts[0].n == 2
    assert xs.elts[1].elts[0].func.id == 'range'
    assert xs.elts[1].elts[0].args[0].n == 10
    assert xs.elts[2].n == 1


# Generated at 2022-06-14 02:26:45.199317
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from .uncurry import UncurryTransformer

    tree = ast.parse("print(*range(1), *range(3))")
    trans = StarredUnpackingTransformer()
    res = trans.visit(tree)
    assert isinstance(res, ast.Module)
    assert len(res.body) == 1
    assert isinstance(res.body[0], ast.Expr)
    assert isinstance(res.body[0].value, ast.Call)
    assert isinstance(res.body[0].value.func, ast.Name)
    assert res.body[0].value.func.id == 'print'
    assert len(res.body[0].value.args) == 1
    assert isinstance(res.body[0].value.args[0], ast.Starred)

# Generated at 2022-06-14 02:26:49.012880
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
  transformer = StarredUnpackingTransformer()
  call_ast = ast.parse('print(*[1, 2, 3])').body[0]
  assert isinstance(transformer.visit(call_ast), ast.Call)
