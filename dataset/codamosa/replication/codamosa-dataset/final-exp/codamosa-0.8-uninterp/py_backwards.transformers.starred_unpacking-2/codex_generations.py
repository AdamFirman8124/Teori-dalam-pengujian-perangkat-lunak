

# Generated at 2022-06-14 02:17:06.571590
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_code = """
import numpy as np

x1 = np.array([1,2,3,4])
y1 = lambda x: np.mean(x)

x2 = np.array([1,2,3,4])
y2 = lambda x: np.mean(x)
    """
    t = StarredUnpackingTransformer()
    t.visit(ast.parse(test_code))
    assert t._tree_changed == True


# Generated at 2022-06-14 02:17:16.198996
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(*range(1))', mode='eval').body
    StarredUnpackingTransformer().visit(node)
    assert_equals(
        ast.dump(node),
        "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=List(elts=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Constant(value=1, kind=None)], keywords=[])], keywords=[])]))], keywords=[]))")
 

# Generated at 2022-06-14 02:17:28.709142
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    visitor = StarredUnpackingTransformer()
    # Test without starred
    test_code = "print(1, 2, 3)"
    ast_obj = ast.parse(test_code)
    expected_result = "print(1, 2, 3)"
    actual_result = astor.to_source(visitor.visit(ast_obj)).strip()
    assert(expected_result == actual_result)

    # Test with a single starred
    test_code = "print(1, *range(3), 2)"
    ast_obj = ast.parse(test_code)
    expected_result = "print(*(list(range(3))), 2)"
    actual_result = astor.to_source(visitor.visit(ast_obj)).strip()
    assert(expected_result == actual_result)

    # Test with two

# Generated at 2022-06-14 02:17:37.740195
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Tests StarredUnpackingTransformer.visit_Call()"""
    assert astor.to_source(StarredUnpackingTransformer().visit(ast.parse("print(1, 2, 3, 4)"))) == "print(*(list([1, 2, 3, 4]) + list([])))"
    assert astor.to_source(StarredUnpackingTransformer().visit(ast.parse("print(1, 2, 3, 4, 5, 6)"))) == "print(*(list([1, 2, 3, 4]) + list([5, 6])))"

# Generated at 2022-06-14 02:17:48.827980
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    node = ast.Call(
        func=ast.Name(id="print"),
        args=[ast.Starred(value=ast.Name(id="range")),
              ast.Starred(value=ast.Name(id="range"))],
        keywords=[])
    result = transformer.visit(node).body
    assert isinstance(result, list)
    node = result[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == "print"
    assert isinstance(node.value.args, list)
    assert len(node.value.args) == 1
    node = node.value.args[0]

# Generated at 2022-06-14 02:18:01.087051
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()


# Generated at 2022-06-14 02:18:11.357778
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # create an empty StarredUnpackingTransformer object
    a = StarredUnpackingTransformer()

    # compile a simple list for testing purpose
    test_list = ast.parse("[2, *range(2), 3, *range(2), 4]").body[0].value.elts

    # test_list should not contain Starred nodes
    a.visit(test_list)
    assert not a._has_starred(test_list)

    # compile a list with Starred node for testing purpose
    test_list_2 = ast.parse("[2, *range(2), 3, *range(3), 4]").body[0].value.elts

    # test_list_2 should contain Starred nodes
    a.visit(test_list_2)

# Generated at 2022-06-14 02:18:22.136106
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
    print(*[2, *range(10), 1])
    some_function(1, *[2, *range(10), 1], *[5, *range(10), 15], key="value")
    """
    expected_result = """
    print(*(list([2]) + list(range(10)) + list([1])))
    some_function(1, *(list([2]) + list(range(10)) + list([1])), *(list([5]) + list(range(10)) + list([15])), key="value")
    """
    ast_tree = ast.parse(source)
    result_ast_tree = ast.parse(expected_result)

    visitor = StarredUnpackingTransformer()
    visitor.visit(ast_tree)


# Generated at 2022-06-14 02:18:30.757696
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from compiler.transformer.starred_unpacking import StarredUnpackingTransformer
    from compiler.transformer.base import BaseNodeTransformer
    from typed_ast import ast3 as ast

    source = """
        print(*range(1), *range(3))
        """
    node = ast.parse(source)
    assert isinstance(node, ast.Module)
    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.Expr)
    assert isinstance(node.body[0].value, ast.Call)
    assert isinstance(node.body[0].value.func, ast.Name)
    assert node.body[0].value.func.id == 'print'

    assert not isinstance(node.body[0].value.args[0], ast.Starred)  # is not

# Generated at 2022-06-14 02:18:41.710538
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tr = StarredUnpackingTransformer()

    node = ast.parse(
        "print(*range(1), *range(3))").body[0].value

# Generated at 2022-06-14 02:18:56.926711
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Initial ast
    line1 = ast.parse('print(*range(0))')
    line2 = ast.parse('print(*range(1))')
    line3 = ast.parse('print(*range(2), *range(3))')

    # Expected ast
    line1_expected = ast.parse('print(*(list(range(0))))')
    line2_expected = ast.parse('print(*(list(range(1))),)')
    line3_expected = ast.parse('print(*(list(range(2)) + list(range(3))),)')

    # Test all lines
    for line, expected in [[line1, line1_expected], [line2, line2_expected], [line3, line3_expected]]:
        print()
        print('Initial ast')
        print(ast.dump(line))

# Generated at 2022-06-14 02:19:07.133317
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # 'print(*range(1), *range(3))' should be replaced by 'print(*(list(range(1)) + list(range(3))))'
    tree = ast.parse('print(*range(1), *range(3))')
    StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:19:14.982289
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import BaseNodeTransformerTest
    from .base import GenericNodeTransformerTestMixin
    
    expected_node = ast.parse('print(*(list(range(1))+list(range(3))))')
    node = ast.parse('print(*range(1), *range(3))')
    state = BaseNodeTransformerTest(StarredUnpackingTransformer.target)
    
    assert StarredUnpackingTransformer(state).visit(node) == expected_node


# Generated at 2022-06-14 02:19:25.066070
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class Test:
        def __add__(self, b):
            return b
        def __radd__(self, b):
            return b
        def __iter__(self):
            yield 1
            yield 2
            yield 3

    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Starred(
            value=ast.Call(
                func=ast.Name(id='tuple'),
                args=[ast.List(elts=[ast.Name(id='a'), Test()], ctx=ast.Load())]))],
        keywords=[])


# Generated at 2022-06-14 02:19:32.259240
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import unittest

    class TestStarredUnpackingTransformer(unittest.TestCase):
        def test_visit_List(self):
            visitor = StarredUnpackingTransformer()
            print()
            print(visitor.visit(ast.parse('[2, *range(10), 1]').body[0].value))

        def test_visit_Call(self):
            visitor = StarredUnpackingTransformer()
            print()
            print(visitor.visit(ast.parse('print(*range(1), *range(3))').body[0]))

    unittest.main()

# Generated at 2022-06-14 02:19:40.934031
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    a = ast.parse("[2, *range(10), 1]")
    StarredUnpackingTransformer(a).visit(a)
    assert ast.dump(a) == 'Module(body=[Expr(value=BinOp(left=BinOp(left=List(elts=[Num(n=2)]), right=Call(func=Name(id="list", ctx=Load()), args=[Call(func=Name(id="range", ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[]), op=Add()), right=List(elts=[Num(n=1)]), op=Add()))])'


# Generated at 2022-06-14 02:19:41.978886
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()


# Generated at 2022-06-14 02:19:49.917894
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse(
        """
        foo(1, *keys, *values)
        """
    )
    assert isinstance(node, ast.Module)
    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.Expr)
    
    expr = node.body[0].value
    assert isinstance(expr, ast.Call)
    
    args = expr.args
    assert isinstance(args[0], ast.Num)
    assert args[0].n == 1
    assert isinstance(args[1], ast.Starred)
    assert isinstance(args[1].value, ast.Name)
    assert args[1].value.id == 'keys'
    assert isinstance(args[2], ast.Starred)

# Generated at 2022-06-14 02:20:02.160431
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = 'a = [2, *range(10), 1]'
    expected = 'a = [2] + list(range(10)) + [1]'
    module_node = node_factory.extract_node(source)
    StarredUnpackingTransformer(module_node, raise_if_changed=True)
    actual = ast.unparse(module_node)
    assert actual == expected

    # merge next to elems
    source = 'a = [*range(10), *range(10)]'
    expected = 'a = list(range(10)) + list(range(10))'
    module_node = node_factory.extract_node(source)
    StarredUnpackingTransformer(module_node, raise_if_changed=True)
    actual = ast.unparse(module_node)

# Generated at 2022-06-14 02:20:11.719086
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def assert_from_to(from_: str, to_: str):
        tree = ast.parse(from_)
        StarredUnpackingTransformer().visit(tree)
        assert codegen.to_source(tree) == to_

    assert_from_to('foo(0)', 'foo(0)')
    assert_from_to('foo(x=1)', 'foo(x=1)')
    assert_from_to('foo(0, x=1)', 'foo(*(list([0]) + list(range(1))))')
    assert_from_to('foo(0, *range(1), **dict(x=1))', 'foo(*(list([0]) + list(range(1))), **dict(x=1))')

# Generated at 2022-06-14 02:20:24.608352
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def check(node: ast.AST, expected: ast.AST):
        tree = ast.parse(node)
        transformer = StarredUnpackingTransformer(tree)
        transformer.visit()
        assert transformer._tree_changed
        tree = ast.dump(tree)
        expected = ast.dump(expected)
        assert tree == expected, (
            f'\nReal tree:\n'
            f'```\n'
            f'{tree}\n'
            f'```\n'
            f'\nExpected tree:\n'
            f'```\n'
            f'{expected}\n'
            f'```\n'
        )

    check('print(*range(1), *range(3))', 'print(*(list(range(1)) + list(range(3))))')
    check

# Generated at 2022-06-14 02:20:25.785629
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:20:37.334770
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    _source_code = """
    print(*range(1), *range(3))

    fun(*range(1), *range(3))
    """
    _expected = """
    print(*(list(range(1)) + list(range(3))))

    fun(*(list(range(1)) + list(range(3))))
    """

    _tree = ast.parse(_source_code)
    _transformer = StarredUnpackingTransformer()
    _new_tree = _transformer.visit(_tree)
    _compiled = compile(
        _new_tree, "<test>", "exec"
    )
    _test_locals = {}
    exec(_compiled, globals(), _test_locals)
    assert ast.dump(_new_tree) == ast.dump(ast.parse(_expected))

# Unit

# Generated at 2022-06-14 02:20:48.137469
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_var = StarredUnpackingTransformer()
    test_var._has_starred = Lambda(lambda xs: BoolOp(op=Or(), values=[IsInstance(inst=Starred(), obj=x) for x in xs]))
    test_var._split_by_starred = Lambda(lambda xs: [
        [x] if _ else Starred()
        for _, x in zip([IsInstance(inst=Starred(), obj=x) for x in xs], xs)
    ])
    test_var.visit = Lambda(lambda node: node)

# Generated at 2022-06-14 02:20:57.552406
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
    print(*range(1), *range(3))
    """
    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:21:07.102874
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .tree_utils import compile_ast_tree
    from .base import BaseNodeTransformerTestCase

    class TestVisitor(BaseNodeTransformerTestCase):
        transformer = StarredUnpackingTransformer
        method = 'visit_Call'

        # fmt: off

# Generated at 2022-06-14 02:21:14.438203
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    ast_node = ast.parse("""
func(1, 2, 3, 4)
func(1, *range(4))
func(1, *[2, 3])
func(*[1, 2], *range(3))
func(*[1, 2], *range(3), *[7, 9, 8], *[7, 8])
""", mode='eval')
    transformer = StarredUnpackingTransformer()
    transformer.visit(ast_node)
    # print(ast.dump(ast_node, include_attributes=True, indent=2))


# Generated at 2022-06-14 02:21:15.080534
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:21:24.797808
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:21:32.331576
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(1))")
    node = tree.body[0]
    transformer = StarredUnpackingTransformer()
    transformer.visit_Call(node)

    assert node.args == [ast.Starred(value=ast.Call(
        func=ast.Name(id='list'),
        args=[ast.Call(
            func=ast.Name(id='range'),
            args=[ast.Num(n=1)],
            keywords=[])],
        keywords=[]))]



# Generated at 2022-06-14 02:21:38.341755
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
    func(1, *[2, 3], *[4, 5])
    """
    expected = """
    func(*(list([2, 3]) + list([4, 5])))
    """
    assert expected == compile_and_transform(source, [StarredUnpackingTransformer])


# Generated at 2022-06-14 02:21:46.925088
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():

    node = ast.Call(
            func=ast.Name(id='print'),
            args=[
                ast.Starred(value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=1)],
                    keywords=[])),
                ast.Starred(value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=3)],
                    keywords=[]))],
            keywords=[])

    result = StarredUnpackingTransformer().visit(node)


# Generated at 2022-06-14 02:21:57.708982
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .parser import parse_ast
    from .debug_visitor import DebugVisitor


# Generated at 2022-06-14 02:22:04.018223
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """print(*range(1), *range(3))"""
    node = ast.parse(code, mode='eval')
    trans = StarredUnpackingTransformer()
    result = trans.visit(node)
    expected = ast.parse("print(*(list(range(1)) + list(range(3))))", mode='eval')
    assert ast.dump(result, annotate_fields=False) == ast.dump(expected, annotate_fields=False)



# Generated at 2022-06-14 02:22:09.838870
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast

    class StarredUnpackingTransformer(BaseNodeTransformer):
        """Compiles:
            [2, *range(10), 1]
            print(*range(1), *range(3))
        To:
            [2] + list(range(10)) + [1]
            print(*(list(range(1)) + list(range(3))))
            
        """
        target = (3, 4)

        def _has_starred(self, xs: List[ast.expr]) -> bool:
            for x in xs:
                if isinstance(x, ast.Starred):
                    return True

            return False

        def _split_by_starred(self, xs: Iterable[ast.expr]) -> List[Splitted]:
            """Split `xs` to separate list by Starred."""
           

# Generated at 2022-06-14 02:22:15.606855
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer().visit(S.Call([S.Num(2), '*', S.Call(['range', 10]), 1])) == S.Call([S.Num(2), '+', S.Call(['list', S.Call(['range', 10])]), '+', S.List([1])])


# Generated at 2022-06-14 02:22:23.553879
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .unparse_ast import Unparser

    class Transformed(ast.NodeTransformer):
        def visit_Call(self, node):
            return node

    tree = ast.parse("""
    print(*range(1), *range(3))
    """)

    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree)

    unparse = Unparser()
    unparse.visit(tree)

    assert unparse.result == 'print(*(list(range(1)) + list(range(3))))'


# Generated at 2022-06-14 02:22:30.271183
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse
    from ..transformers.unparser import Unparser

    source = 'print(*range(3), *range(4), 5)'
    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)

    unparser = Unparser(tree)
    unparser.preamble.insert(0, 'from typing import List')
    expected = 'from typing import List\n\nprint(*((list(range(3)) + list(range(4))) + [5]))\n'
    assert unparse(tree) == expected



# Generated at 2022-06-14 02:22:38.935550
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from nuitka import (
        SyntaxErrors,
        Options,
        TreeXML
    )
    from nuitka.tree.Building import buildNode

    code = 'print(*range(1), *range(3))'
    module, source_ref = SyntaxErrors.compileErrors(code)  # type: ignore # noqa

    print(TreeXML.toXMLString(buildNode(module, source_ref)))
    options = Options.getDefaultOptions()
    options.shallow = True
    options.optimize = False
    options.debug_level = 0
    options.filename = ''
    options.recurse_none = True
    options.recurse_all = True
    options.recurse_builtins = True
    options.inline_call_treshold = 2
    options.inline_range_

# Generated at 2022-06-14 02:22:53.266774
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = """
x = []
x[0] = 2
print(*range(10), 2)
print(1, *range(10))
print(*range(10), *range(10))
print(*range(10), *range(10), *range(10))
"""
    expected = """
x = []
x[0] = 2
print(*(list(range(10)) + [2]))
print(*(list(range(10)) + [1]))
print(*(list(range(10)) + list(range(10))))
print(*(list(range(10)) + list(range(10)) + list(range(10))))
"""
    from typed_ast import parse
    from typed_ast.ast3 import parse as ast_parse
    mod = parse(src, '<test>', 'exec')

# Generated at 2022-06-14 02:23:03.889530
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node1 = ast.Call(func=ast.Name(id='print'), args=[ast.Num(n=2), ast.Num(n=4), ast.Num(n=5), ast.Starred(value=ast.Name(id='lst'))], keywords=[])
    node2 = ast.Call(func=ast.Name(id='print'), args=[ast.Num(n=2), ast.Num(n=4), ast.Num(n=5), ast.Starred(value=ast.Call(func=ast.Name(id='lst'), args=[], keywords=[]))], keywords=[])
    node3 = ast.Call(func=ast.Name(id='print'), args=[ast.Num(n=2), ast.Num(n=4), ast.Num(n=5)], keywords=[])

# Generated at 2022-06-14 02:23:13.874878
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import sys
    import unittest
    from typed_ast import ast3 as ast

    class Test(unittest.TestCase):
        def test_starred_call_tuple(self):
            ast_expected = ast.parse('print(*(list(range(1)) + list(range(3))))')
            ast_source = ast.parse('print(*range(1), *range(3))')
            ast_transformed = StarredUnpackingTransformer().visit(ast_source)
            self.assertEqual(ast_expected, ast_transformed)

        def test_starred_call_iterable(self):
            ast_expected = ast.parse('print(*(list(range(1)) + list(range(3))))')
            ast_source = ast.parse('print(*range(1), *range(3))')


# Generated at 2022-06-14 02:23:27.912347
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    from .util import Call
    from . import compile_to_ast
    from . import sanity_check

    # test 1
    node = Call(
        target=ast.Name(id='print', ctx=ast.Load()),
        args=[ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), ctx=ast.Load())],
        keywords=[])
    node = compile_to_ast(node)
    StarredUnpackingTransformer().visit(node)
    sanity_check(node)

# Generated at 2022-06-14 02:23:37.604644
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert (
        repr(StarredUnpackingTransformer().visit(
            ast.parse('unpack(*args)')
        )) == repr(
            ast.parse('unpack(*(list(args)))')
        )
    )

    assert (
        repr(StarredUnpackingTransformer().visit(
            ast.parse('unpack(1, *args)')
        )) == repr(
            ast.parse('unpack(1, *(list(args)))')
        )
    )

    assert (
        repr(StarredUnpackingTransformer().visit(
            ast.parse('unpack(*args, a=1)')
        )) == repr(
            ast.parse('unpack(*(list(args)), a=1)')
        )
    )


# Generated at 2022-06-14 02:23:44.301173
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from astor.code_gen import to_source
    from astor.code_gen import unparse
    import astor
    node=astor.parse_file("tests/resources/starred_unpacking_transformer/code.py")
    node = StarredUnpackingTransformer().visit(node)
    assert unparse(node).strip() == to_source(node).strip()

# Generated at 2022-06-14 02:23:53.198310
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast.ast3 import Call
    node = Call(func=Name(id='print'), args=[Starred(value=Name(id='range'), ctx=Load()), Starred(value=Name(id='range'), ctx=Load())], keywords=[])
    m = StarredUnpackingTransformer()
    new = m.visit(node)

    assert new == Call(func=Name(id='print'), args=[Starred(value=BinOp(left=Call(func=Name(id='list'), args=[Name(id='range')], keywords=[]), right=Call(func=Name(id='list'), args=[Name(id='range')], keywords=[]), op=Add()))], keywords=[])

# Generated at 2022-06-14 02:24:03.272601
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Test input
    input_code = """
print(*args)
    """
    # Expected result
    expected_code = """
print(*(list(args)))
    """
    tree = ast.parse(input_code)
    print(ast.dump(tree, include_attributes=False))
    transformer = StarredUnpackingTransformer()
    tree = transformer.visit(tree)
    print(ast.dump(tree, include_attributes=False))
    assert transformer._tree_changed
    out = compile(tree, "test_StarredUnpackingTransformer_visit_Call", "exec")
    ns = {}
    exec(out, ns)
    assert ns["__code__"] == expected_code
    print("OK")


# Generated at 2022-06-14 02:24:07.549694
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import BaseNodeTransformerTestCase

    class TestCase(BaseNodeTransformerTestCase):
        transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:24:19.343295
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import compile_function
    from .base import TestCase

    class Test(TestCase):
        def test_simple(self):
            print_ = compile_function(ast.parse('print()', mode='exec'),
                                      transformers=(StarredUnpackingTransformer,))

            self.assertTrue(print_ is not None)

        def test_starred_unpacking(self):
            print_ = compile_function(ast.parse('print(*range(10), *range(5))', mode='exec'),
                                      transformers=(StarredUnpackingTransformer,))

            self.assertTrue(print_ is not None)

            print_(1, 2)


# Generated at 2022-06-14 02:24:24.137468
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
print(1, *range(3), 2, *range(3))
"""
    expected = """
print(*(list(range(1)) + list(range(2))))
"""
    from .fixer_base import run_fixer_test
    tree = run_fixer_test(StarredUnpackingTransformer, source, expected)
    assert tree == expected


# Generated at 2022-06-14 02:24:39.426952
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typing import Optional
    from typed_ast import ast3
    from .as_source import as_source

    StarredUnpackingTransformer = StarredUnpackingTransformer()

    def function(a: ast3.expr, *b: ast3.expr, **c: ast3.expr) -> Optional[ast3.Call]:
        return ast3.Call(func = ast3.Name(id = 'function'), args = [1, *range(10), 2, 3], keywords = [])

    result = StarredUnpackingTransformer.visit(function)

# Generated at 2022-06-14 02:24:50.875961
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    import astunparse
    from .base import NodeTransformerTestCase
    from .test_inline_lambda import InlineLambdaTransformerTestCase

    class StarredUnpackingTransformerTestCase(InlineLambdaTransformerTestCase):
        def setUp(self):
            self.transformer_class = StarredUnpackingTransformer

    # [2, *range(10), 1]
    code = """
[2, *range(10), 1]
"""  # noqa
    expected_code = """
[2] + list(range(10)) + [1]
"""  # noqa

# Generated at 2022-06-14 02:25:03.495637
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import (parse, ast3, fix_missing_locations)
    import unittest

    class TestVisitor(unittest.TestCase):
        def setUp(self):
            self.transformer = StarredUnpackingTransformer()

        def test_no_starred(self):
            node = parse('print(1, 2, 3)').body[0]
            self.transformer.visit(node)
            fixed_node = fix_missing_locations(node)
            self.assertEqual(node, fixed_node)

        def test_call_with_starred(self):
            node = parse('print(1, *range(2), 3)').body[0]

# Generated at 2022-06-14 02:25:10.290244
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from ast_unparse import unparse_ast

    parser = ast.PyCF_ONLY_AST
    source = 'func(not_starred, *a, arg, *b, end_arg, not_starred2)'
    module = ast.parse(source, filename='<none>', mode='eval',
                       pyversion=(3, 7),
                       # parser == PyCF_ONLY_AST
                       )

    assert unparse_ast.unparse_ast(ast.Module(body=[module])) == f'(0, {source})\n'
    assert unparse_ast.unparse_ast(module) == f'(0, {source})\n'

    StarredUnpackingTransformer.run_options(module, 'ast3')


# Generated at 2022-06-14 02:25:22.321028
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Remove when done
    import sys
    import os.path
    from .tools import show_tree
    from .tools import assert_tree

    filename = os.path.dirname(__file__) + os.path.sep + "code" + os.path.sep + "starred_unpacking.py"
    if filename not in sys.argv:
        pyfile = open(filename)
        sys.argv.append(filename)
        try:
            exec(compile(pyfile.read(), filename, 'exec'))
        finally:
            sys.argv.pop()
            pyfile.close()
    else:
        rev_index = len(sys.argv) - sys.argv[::-1].index(filename) - 1
        filename = sys.argv[rev_index]
        pyfile

# Generated at 2022-06-14 02:25:27.784369
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = 'from typing import List; print(*[1, 2, 3], *[4, 5])'
    expected = "from typing import List; print(1, 2, 3, 4, 5)"
    ast_node = ast.parse(src)
    actual = StarredUnpackingTransformer().visit(ast_node)
    actual = astor.to_source(actual)
    assert actual == expected


# Generated at 2022-06-14 02:25:38.241631
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_utils import round_trip
    from typed_ast import ast3 as ast
    input = ast.parse("""
print(1, *range(10), *range(1), 2)
    """)
    expected = ast.parse("""
print(*(list([1]) + list(range(10)) + list(range(1)) + [2]))
    """)
    actual = round_trip(input, StarredUnpackingTransformer)
    assert ast.dump(expected, annotate_fields=False, include_attributes=False) == ast.dump(actual, annotate_fields=False, include_attributes=False)

# Generated at 2022-06-14 02:25:40.736013
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    target = """print(1, 2, 3, *range(4))"""
    expected = """print(*([1, 2, 3] + list(range(4))))"""
    result = compile_and_transform(target, StarredUnpackingTransformer)
    assert result == expected


# Generated at 2022-06-14 02:25:52.147246
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    stmt = ast.parse("""
test()
test(2, *range(10), 1)  # Nothing happens
print(*range(1), *range(3))
    """).body[1]

    # test(2, *range(10), 1)  # Nothing happens
    assert isinstance(stmt, ast.Expr)
    assert isinstance(stmt.value, ast.Call)
    assert stmt.value.args[0].n == 2
    assert isinstance(stmt.value.args[1], ast.Starred)
    assert stmt.value.args[2].n == 1

    # Before
    assert isinstance(ast.dump(stmt), str)

# Generated at 2022-06-14 02:26:00.638525
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # print(*range(1), *range(3))
    # print(*(list(range(1)) + list(range(3))))
    call = ast.Call(func=ast.Name(id='print'), args=[ast.Starred(value=ast.Name(id='range'), ctx=None), ast.Num(1),
                                                      ast.Starred(value=ast.Name(id='range'), ctx=None), ast.Num(3)],
                    keywords=[])

# Generated at 2022-06-14 02:26:15.811580
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast as ast_def
    from .. import compile_source
    source = "print(*(list(range(1)) + list(range(3))))"
    result = compile_source(source, 3, 4,
                            transforms=[StarredUnpackingTransformer()])

# Generated at 2022-06-14 02:26:25.818200
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    x = StarredUnpackingTransformer()

    # [2, *range(10), 1]
    code = ast.parse("[2, *range(10), 1]").body[0].value
    tree = ast.parse("list([2]) + list(range(10)) + [1]")
    assert ast.dump(x.visit(code)) == ast.dump(tree)

    # print(*range(1), *range(3))
    code = ast.parse("print(*range(1), *range(3))").body[0]
    tree = ast.parse("print(*(list(range(1)) + list(range(3))))")
    assert ast.dump(x.visit(code)) == ast.dump(tree)


# Generated at 2022-06-14 02:26:38.135247
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer."""
    import argparse
    import astor

    parser = argparse.ArgumentParser(
        description='Test StarredUnpackingTransformer_visit_Call.')
    parser.add_argument(
        '--input-file', type=str, default='',
        help='Specify the file from which to read input. If omitted, read from stdin.')
    parser.add_argument(
        '--output-file', type=str, default='',
        help='Specify the file to which to write output. If omitted, write to stdout.')
    args = parser.parse_args()
    in_file = args.input_file
    out_file = args.output_file

    node = astor.parse_file(in_file)
   

# Generated at 2022-06-14 02:26:42.416947
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    StarredUnpackingTransformer().visit_Call(
        ast.Call(
            func=ast.Name(id='print'),
            args=[
                ast.Starred(value=ast.Name(id='arg1')),
                ast.Starred(value=ast.Name(id='arg2'))
            ],
            keywords=[]
        )
    )

# Generated at 2022-06-14 02:26:49.062948
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

    code = """
        print(*range(1), *range(3))
    """

    tree = ast.parse(code)
    expected = """
        print(*(list(range(1)) + list(range(3))))
    """

    transformer = StarredUnpackingTransformer()
    assert astor.to_source(transformer.visit(tree)) == expected

# Generated at 2022-06-14 02:26:54.835594
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse
    import ast as pyast
    u = StarredUnpackingTransformer()
    t = pyast.parse('''
from typing import List
print(*range(10))
print(*[1, 2], 3, *[4])
''')
    print(u.visit(t))
    print(unparse(u.visit(t)).rstrip())
