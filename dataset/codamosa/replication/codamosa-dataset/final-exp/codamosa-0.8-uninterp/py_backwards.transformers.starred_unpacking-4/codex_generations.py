

# Generated at 2022-06-14 02:17:12.745251
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import set_source_code
    from . import parse
    from . import unparse

    source_code = 'list("abc")'
    expected_code = 'list(*("abc",))'

    tree = parse(source_code, version=(3, 8))
    set_source_code(tree, source_code)
    StarredUnpackingTransformer().visit(tree)
    assert unparse(tree) == expected_code


# Generated at 2022-06-14 02:17:21.928730
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    x = [ast.Num(1)]
    y = [ast.Num(2), ast.Starred(value=ast.Tuple(elts=[ast.Num(3)]))]
    z = [ast.Num(4), ast.Starred(value=ast.List(elts=[ast.Num(5)])),
         ast.Starred(value=ast.Set(elts=[ast.Num(6)])), ast.Num(7)]
    node = ast.List(elts=x + y + z)

# Generated at 2022-06-14 02:17:33.566185
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from . import CythonTransformTestCase
    from . import _make_call_ast

    class TestCase(CythonTransformTestCase):
        transform = StarredUnpackingTransformer

        def test_list_with_starred(self):
            x = ast.List(elts=[ast.Starred(value=ast.Name(id="a"), ctx=ast.Load())])
            y = self.transform(x)
            z = ast.Call(
                func=ast.Name(id="list"),
                args=[ast.Name(id="a")],
                keywords=[],
            )
            self.assertEqual(y, z)


# Generated at 2022-06-14 02:17:42.263349
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = \
        """
a = [2, *range(4), 3]
        """

    result = \
        """
a = [2] + list(range(4)) + [3]
        """

    tr = StarredUnpackingTransformer()
    tree = ast.parse(src)
    assert tr.visit(tree).body[0].value.right.left.func.id == 'range'
    assert tr.visit(tree).body[0].value.right.right.elts[0].n == 3
    result = ast.fix_missing_locations(tr.visit(tree))
    assert ast.dump(result) == ast.dump(ast.parse(result))


# Generated at 2022-06-14 02:17:50.853020
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse
    from .base import BaseNodeTransformerTestCase
    
    class TestCase(BaseNodeTransformerTestCase):
        transformer = StarredUnpackingTransformer
        code = "abc(3, *foo, *bar)"
        tree = ast.parse(code)
        
        def test_transformed(self):
            unstared = self.transform()
            expected = ast.parse("""
from typing import List
abc(*(((List[int]([3]) + List[int](foo)) + List[int](bar))))
            """)
            self.assertEqual(unparse(expected), unparse(unstared))
    
    
    TestCase.verify()
    

# Generated at 2022-06-14 02:18:01.568132
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import roundtrip_uncompyle
    source = "[2, *range(10), 1]"
    source_compiled = compile(source, '<string>', 'exec')
    source_transformed = roundtrip_uncompyle(source_compiled, StarredUnpackingTransformer)
    source_transformed = "\n".join(source_transformed.split("\n")[1:])  # drop the first line
    tree_transformed = ast.parse(source_transformed, 'exec')
    tree_reference = ast.parse('[2] + list(range(10)) + [1]', 'exec')
    assert ast.dump(tree_transformed) == ast.dump(tree_reference)



# Generated at 2022-06-14 02:18:10.812340
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tr = StarredUnpackingTransformer()
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Num(n=1)], keywords=[])), ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Num(n=3)], keywords=[]))],
        keywords=[])
    result = ast.Call(func=ast.Name(id='print'), args=[ast.Starred(value=ast.Call(func=ast.Name(id='list'), args=[ast.Call(func=ast.Name(id='range'), args=[ast.Num(n=1)], keywords=[])], keywords=[]))], keywords=[])
    assert tr.visit

# Generated at 2022-06-14 02:18:12.355774
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer([]) == []
    

# Generated at 2022-06-14 02:18:22.925892
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # example 1
    node = ast.parse(
        "print(*range(1), *range(3))"
    ).body[0].value

    output = StarredUnpackingTransformer().visit(node)

    assert output == ast.parse(
        "print(*(list(range(1)) + list(range(3))))"
    ).body[0].value

    # example 2
    node = ast.parse(
        "print( *range(1), *range(3))"
    ).body[0].value

    output = StarredUnpackingTransformer().visit(node)

    assert output == ast.parse(
        "print(*(list(range(1)) + list(range(3))))"
    ).body[0].value

    # example 3

# Generated at 2022-06-14 02:18:28.502773
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    code = """
        [2, *range(10), 1]
        print(*range(1), *range(3))
    """
    translated_code = """
        [2] + list(range(10)) + [1]
        print(*(list(range(1)) + list(range(3))))
    """
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == translated_code

# Generated at 2022-06-14 02:18:44.123311
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    t = StarredUnpackingTransformer()
    i = [2, *range(10), 1]
    o = t._to_sum_of_lists(i)
    print(o)

    assert isinstance(o, ast.BinOp)

    assert isinstance(o.left, ast.List)
    assert o.left.elts[0].n == 2
    assert len(o.left.elts) == 1

    assert isinstance(o.left, ast.List)
    assert o.left.elts[0].n == 2
    assert len(o.left.elts) == 1

    assert isinstance(o.op, ast.Add)

    assert isinstance(o.right, ast.BinOp)
    assert isinstance(o.right.left, ast.Call)

# Generated at 2022-06-14 02:18:49.287344
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Test for visit_Call method of class StarredUnpackingTransformer"""
    from .base import TestCompilerBase
    source = """print(*range(1), *range(2), *range(3))"""
    StarredUnpackingTransformer.test(source, TestCompilerBase)


# Generated at 2022-06-14 02:18:53.732743
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_fixtures import ListTestCase as TestCase
    from .test_fixtures import compile_back

    for test_case in TestCase:
        compiled = compile_back(test_case.node, StarredUnpackingTransformer)
        assert compiled == test_case.expected


# Generated at 2022-06-14 02:18:56.304443
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('a(*range(3), *range(10), *range(5))')
    print(StarredUnpackingTransformer().visit(node))

# Generated at 2022-06-14 02:19:06.700520
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .visitors import CodePrinter
    from .ast_helpers import get_ast

    before = """
print(*range(1), *range(3))
print(*range(10))
"""
    after = """
print(*(list(range(1)) + list(range(3))))
print(*(list(range(1)) + list(range(3)) + list(range(10))))
"""

    transformer = StarredUnpackingTransformer()
    after_ast = CodePrinter().visit(get_ast(after))
    actual_code = CodePrinter().visit(transformer.visit(get_ast(before)))

    assert after_ast == actual_code, """
Expected:

%s

Got:

%s
""" % (after_ast, actual_code)



# Generated at 2022-06-14 02:19:18.285663
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    before = ast.Call(
        func=ast.Name(id='f'),
        args=[
            ast.Num(n=2),
            ast.Starred(
                value=ast.List(
                    elts=[
                        ast.Num(n=3),
                        ast.Num(n=4),
                    ],
                    ctx=ast.Load())),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[
                        ast.Num(n=3)],
                    keywords=[]))],
        keywords=[])


# Generated at 2022-06-14 02:19:30.950804
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(*[1, 2], *(3, 4), 'x', 5)", filename='<test>', mode='eval').body

# Generated at 2022-06-14 02:19:37.161982
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    source = ast.parse("[1_, *range(1_, 10_), 2_]")
    tree = transformer.visit(source)
    assert transformer.is_tree_changed()

    expected = ast.parse("[1_] + list(range(1_, 10_)) + [2_]")
    assert ast.dump(tree) == ast.dump(expected)



# Generated at 2022-06-14 02:19:46.403192
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from ast import parse
    from .unparser import to_source
    from .unparse import Unparser
    result = Unparser(StarredUnpackingTransformer()).visit(parse('''
[2, *range(10), 1]
print(*range(1), *range(3))
    '''))
    assert result == "[2] + list(range(10)) + [1]\nprint(*(list(range(1)) + list(range(3))))"

# Generated at 2022-06-14 02:19:50.554453
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer()
    trans.generic_visit(ast.parse(textwrap.dedent("""
        """)))



# Generated at 2022-06-14 02:20:06.322773
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # test with single argument
    node = ast.parse('print(*range(1))')
    star_unpack_transformer = StarredUnpackingTransformer()
    star_unpack_transformer.visit(node)
    assert star_unpack_transformer._tree_changed == True
    assert ast.dump(node) == "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=1)], keywords=[])], keywords=[])], keywords=[]))])"

    # test many arguments

# Generated at 2022-06-14 02:20:19.223724
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # test case 1
    expression =  ast.Call(
                    func=ast.Name(id='print'),
                    args=[ast.Starred(value=ast.Call(
                        func=ast.Name(id='range'),
                        args=[ast.Num(n=1)],
                        keywords=[]),
                    ctx=ast.Load()),
                    ast.Starred(value=ast.Call(
                        func=ast.Name(id='range'),
                        args=[ast.Num(n=3)],
                        keywords=[]),
                    ctx=ast.Load())],
                    keywords=[])


# Generated at 2022-06-14 02:20:22.681794
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import ast, astor
    node = ast.parse("[2, *range(10), 1]")
    expected_result = "[2] + list(range(10)) + [1]"
    actual_result = StarredUnpackingTransformer().visit(node)
    assert astor.to_source(actual_result) == expected_result



# Generated at 2022-06-14 02:20:32.799162
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    input_ast = ast.parse(textwrap.dedent("""
        print(*range(1), *range(3))
    """)[1:])

    expected_ast = ast.parse(textwrap.dedent("""
        print(*(list(range(1)) + list(range(3))))
    """)[1:])
    expected_changed = True

    t = StarredUnpackingTransformer()
    result = t.visit(input_ast)
    assert result == expected_ast
    assert t._tree_changed == expected_changed



# Generated at 2022-06-14 02:20:39.045582
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[2, *range(10), 1]')
    x = StarredUnpackingTransformer().visit(node)
    print(x.body[0].value)
    print(ast.dump(x.body[0].value, include_attributes=True))


# Generated at 2022-06-14 02:20:49.588698
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast

    node = ast.Call(
        func=ast.Name(id='print'),
        args=[
            ast.Num(n=1),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=10)],
                    keywords=[]
                )
            ),
            ast.Name(id='a'),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=1)],
                    keywords=[]
                )
            )
        ],
        keywords=[]
    )


# Generated at 2022-06-14 02:20:58.026614
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert star_list([]).elts == []
    assert star_list([1]).elts == [1]
    assert star_list([1, *range(3)]).elts == [1, *range(3)]
    assert ast.dump(star_list([1, *range(3)])) == 'List([Num(n=1), Starred(value=Name(id="range", ctx=Load()), ctx=Load()), Num(n=3)], ctx=Load())'

# Generated at 2022-06-14 02:21:07.268756
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast as pyast
    import typed_astunparse
    import inspect

    code = ("print(1, *range(10), *range(20))")

    py_ast = pyast.parse(code)
    typed_ast = typed_ast.ast3.parse(code)
    expected = typed_astunparse.unparse(StarredUnpackingTransformer().visit(typed_ast))
    actual = inspect.getsource(StarredUnpackingTransformer.visit_Call)
    
    assert expected == actual


# Generated at 2022-06-14 02:21:18.844759
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    tree = ast.parse("[*range(4), *range(5), 1]")
    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == "Module(body=[Expr(value=BinOp(left=BinOp(left=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=4)], keywords=[])], keywords=[]), op=Add(), right=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=5)], keywords=[])], keywords=[])), op=Add(), right=List(elts=[Num(n=1)]))])]"

# Generated at 2022-06-14 02:21:28.767251
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    example1 = ast.parse("[2, *range(10), 1]")
    example2 = ast.parse("[2, *range(10), 1]")
    example3 = ast.parse("[2, *range(10), 1]")
    example4 = ast.parse("[2, *range(10), 1]")
    example5 = ast.parse("[2, *range(10), 1]")
    expected1 = ast.parse("[2] + list(range(10)) + [1]")
    expected2 = ast.parse("[2] + list(range(10)) + [1]")
    expected3 = ast.parse("[2] + list(range(10)) + [1]")

# Generated at 2022-06-14 02:21:46.701888
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('foo(2, *range(10), 1)').body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert node.value.args == [ast.Num(2), ast.Starred(ast.Call(ast.Name('range', ast.Load()), [ast.Num(10)], [])), ast.Num(1)]

    assert isinstance(StarredUnpackingTransformer().visit(node), ast.Expr)

# Generated at 2022-06-14 02:21:57.578431
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
        print(*range(1), *range(3))
    """
    node = ast.parse(code)
    node = StarredUnpackingTransformer().visit(node)

# Generated at 2022-06-14 02:22:07.577379
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tests = [
        # initial code, result code
        [
            """
            print(1, 2, 3, 4)
            """,
            """
            print(1, 2, 3, 4)
            """
        ],
        [
            """
            print(1, *[2, 3], 4)
            """,
            """
            print(*list([1]) + list([2, 3]) + list([4]))
            """
        ],
        [
            """
            print(1, 2, *range(4), 5, *range(4), 5, 6)
            """,
            """
            print(*list([1, 2]) + list(range(4)) + list([5, *range(4), 5, 6]))
            """
        ],
    ]

    for code, expected in tests:
        print

# Generated at 2022-06-14 02:22:19.348111
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    x = ast.parse('[2, *range(10), 1]', 'test')
    assert x.body[0].value.elts[1].value.func.id == 'range'

    transformed = StarredUnpackingTransformer().visit(x)
    assert isinstance(transformed.body[0].value.elts[1], ast.BinOp)
    assert transformed.body[0].value.elts[1].op.__class__.__name__ == 'Add'
    assert transformed.body[0].value.elts[1].left.func.id == 'list'
    assert transformed.body[0].value.elts[1].left.args[0].value.func.id == 'range'


# Generated at 2022-06-14 02:22:24.926410
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from astunparse import unparse
    src = '[2, *range(10), 1]'
    expected = "([2] + list(range(10)) + [1])"
    tree = ast.parse(src)
    tr = StarredUnpackingTransformer()
    tr.visit(tree)
    assert tr.tree_changed
    assert unparse(tree) == expected

# Generated at 2022-06-14 02:22:37.041636
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import ast
    import unittest

    from . import Compiler

    class Test(unittest.TestCase):
        def setUp(self):
            self.compiler = Compiler(transformer=StarredUnpackingTransformer)

        def test_without_starred(self):
            lst = ast.List(elts=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)])
            result = self.compiler.compile_ast(lst)
            self.assertEqual(result, '1, 2, 3')


# Generated at 2022-06-14 02:22:43.502480
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    st = ast.parse('print(*range(1), *range(3))')
    result = StarredUnpackingTransformer()(st)
    assert 'print(*list(range(1)) + list(range(3)))' in astor.to_source(result)


# Generated at 2022-06-14 02:22:52.835021
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    input_code = [
        "[2, *range(10), 1]",
        "[2, *range(10), 1, *range(5)]"]
    expected_code = [
        "[2] + list(range(10)) + [1]",
        "[2] + list(range(10)) + [1] + list(range(5))"]
    result = [StarredUnpackingTransformer.run(code) for code in input_code]
    assert result == expected_code


# Generated at 2022-06-14 02:23:01.337749
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse('''
for x in [1, 2, 3, *[4, 5], 6, 7]:
    for y in [4, 5, 6, *[7, 8]]:
        pass
    ''')
    usual_tree = ast.parse('''
for x in [1, 2, 3] + [4, 5] + [6, 7]:
    for y in [4, 5, 6]+[7, 8]:
        pass
    ''')

    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(usual_tree)


# Generated at 2022-06-14 02:23:07.241390
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Test for method visit_List of class StarredUnpackingTransformer."""
    # noinspection PyUnresolvedReferences
    from py_mini_racer import py_mini_racer  # type: ignore

    #  def test_visit_List(self):
    #      xs = [ast.Starred(value=ast.Name(id='x'), ctx=ast.Load())]
    #      result = self._to_sum_of_lists(xs)
    #      assert ast.dump(result) == 'Call(func=Name(id=\'list\', ctx=Load()), \
    #                    args=[Name(id=\'x\', ctx=Load())], keywords=[])'


# Generated at 2022-06-14 02:23:22.021078
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    root = ast.parse(code)
    expected = ast.parse("[2] + list(range(10)) + [1]")
    assert StarredUnpackingTransformer().visit(root) == expected


# Generated at 2022-06-14 02:23:32.994021
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    t = StarredUnpackingTransformer(None, None, None)
    assert t._split_by_starred([]) == [[]]
    assert t._split_by_starred([ast.Starred(value=ast.Name(id='a'))]) == [
            [], ast.Starred(value=ast.Name(id='a')), []]
    assert t._split_by_starred([ast.Name(id='a'), ast.Starred(value=ast.Name(id='b')), ast.Name(id='c')]) == [
            [ast.Name(id='a')], ast.Starred(value=ast.Name(id='b')), [ast.Name(id='c')]]

# Generated at 2022-06-14 02:23:40.765114
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = 'print(*range(1), *range(3))'

    # Prepare AST
    mod = ast.parse(src)
    node = mod.body[0]  # type: ast.Call

    # Test method
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)

    # Test result
    assert str(node) == 'print(*(list(range(1)) + list(range(3))))'


# Generated at 2022-06-14 02:23:52.070311
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(3), 3]"
    module = ast.parse(code)
    StarredUnpackingTransformer().visit(module)

# Generated at 2022-06-14 02:24:03.246006
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    def assert_converts(src: str, expected: str, version: Version = None) -> None:
        node = ast.parse(src)
        StarredUnpackingTransformer(version=version).visit(node)
        actual = ast.dump(node)
        assert actual == expected


# Generated at 2022-06-14 02:24:11.354379
# Unit test for constructor of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:24:21.731731
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import sys
    import astor
    node_list = ast.parse("list([2, *range(10), 1])")
    node_call = ast.parse("print(*range(1), *range(3))")
    node_list_expected = ast.parse("list([2] + list(range(10)) + [1])")
    node_call_expected = ast.parse("print(*(list(range(1)) + list(range(3))))")

    StarredUnpackingTransformer().visit(node_list)
    assert astor.to_source(node_list) == astor.to_source(node_list_expected)
    StarredUnpackingTransformer().visit(node_call)
    assert astor.to_source(node_call) == astor.to_source(node_call_expected)



# Generated at 2022-06-14 02:24:23.203279
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    a = StarredUnpackingTransformer()
    print(a)

# Generated at 2022-06-14 02:24:31.147397
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer.run('''print(*range(1), *range(3))''') == '''print(*(list(range(1)) + list(range(3))))'''
    assert StarredUnpackingTransformer.run('''print(*range(1))''') == '''print(*(list(range(1))))'''
    assert StarredUnpackingTransformer.run('''print(*[1, 2, 3])''') == '''print(*(list([1, 2, 3])))'''

# Generated at 2022-06-14 02:24:37.537965
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    module = _get_ast_from_code("[2, *range(10), 1]")
    StarredUnpackingTransformer().visit(module)
    assert _get_code_from_ast(module) == "[2] + list(range(10)) + [1]"


# Generated at 2022-06-14 02:24:52.616157
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import inspect
    from astunparse import unparse

    source = inspect.getsource(test_StarredUnpackingTransformer_visit_Call)
    tree = compile(source, __file__, 'exec', flags=0, dont_inherit=True)
    tree = StarredUnpackingTransformer().visit(tree)
    print(unparse(tree))

# Generated at 2022-06-14 02:25:05.287830
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast as pyast
    node = pyast.Call(
        func=pyast.Name(id='print'),
        args=[
            pyast.Starred(value=pyast.Name(id='range'), ctx=pyast.Load()),
            pyast.Starred(value=pyast.Name(id='range'), ctx=pyast.Load())
        ],
        keywords=[]
    )

# Generated at 2022-06-14 02:25:08.355909
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    t = StarredUnpackingTransformer(
        """
        [2, *range(1), 1]
    """)

    assert_equal(t.result, """
        ([2] + list(range(1)) + [1])
    """)



# Generated at 2022-06-14 02:25:14.122915
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_transformer import run_test_transform
    code = '[2, *range(5), 1]'
    expected = '[2] + list(range(5)) + [1]'
    run_test_transform(StarredUnpackingTransformer, code, expected, 3)


# Generated at 2022-06-14 02:25:19.350843
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    expr = astor.parse_expr("[1, *[2, *[3, *[4, *[5]]]], 6]")
    result = StarredUnpackingTransformer().visit(expr)
    assert astor.to_source(result) == "[1, 2, 3, 4, 5, 6]"


# Generated at 2022-06-14 02:25:29.732832
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from ast_compat import parse
    from ast_compat import literal_eval
    from .base import BaseNodeTransformer


# Generated at 2022-06-14 02:25:36.081303
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    transformer = StarredUnpackingTransformer()

    tree_in = ast.parse('[2, *range(10), 1]')
    tree_out = ast.parse('[2] + list(range(10)) + [1]')

    assert astor.to_source(transformer.visit(tree_in)) == astor.to_source(tree_out)



# Generated at 2022-06-14 02:25:39.104705
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = """
print(*range(1), *range(3))
    """
    expected = """
print(*(list(range(1)) + list(range(3))))
    """
    tree = ast.parse(src)
    StarredUnpackingTransformer().visit(tree)
    actual = astor.to_source(tree)
    assert actual == expected


# Generated at 2022-06-14 02:25:46.764625
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Given:
    tree = ast.parse("print(*args, *args)")

    # When:
    StarredUnpackingTransformer().visit(tree)

    # Then:
    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=BinOp(left=Call(func=Name(id='list', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]), op=Add(), right=Call(func=Name(id='list', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[])))], keywords=[]))])"



# Generated at 2022-06-14 02:26:01.650635
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from astor.code_gen import to_source
    from .base import BaseNodeTransformer
    from typed_ast import ast3 as ast
    from .target import TargetTranspiler

    class DummyTranspiler(TargetTranspiler):
        def visit_List(self, node: ast.List) -> ast.List:
            node = super().visit_List(node)

        def visit_Call(self, node: ast.Call) -> ast.Call:
            node = super().visit_Call(node)
            node.args.append(ast.Constant(value=123))
            return self.generic_visit(node)

    transpilers = [StarredUnpackingTransformer, DummyTranspiler]
    transpiler = BaseNodeTransformer.chain(transpilers)


# Generated at 2022-06-14 02:26:26.807313
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer."""
    from .. import run_on_single_file

# Generated at 2022-06-14 02:26:38.265541
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Test function for method visit_Call of class StarredUnpackingTransformer
    """
    from typed_ast import ast3 as ast
    from src.core.compiler import Compiler
    f_expr = """
    print(*range(1))
    print(*range(1), *range(3))
    print(1, *range(1), 2, *range(3), 3)
    """
    f_compiler = Compiler(target=3)
    f_tree = f_compiler.process_source(f_expr, mode='eval')
    f_transformer_name = 'src.core.compiler.transformer.StarredUnpackingTransformer'
    f_transformer = f_compiler._transformer_cls_by_name[f_transformer_name]()


# Generated at 2022-06-14 02:26:42.483337
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse(
        "print(*range(1), *range(3))"
    ).body[0]
    StarredUnpackingTransformer().visit(node)
    target = ast.parse(
        "print(*(list(range(1)) + list(range(3))))"
    ).body[0]
    assert ast.dump(target) == ast.dump(node)



# Generated at 2022-06-14 02:26:50.750000
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from plyer.compat import IS_PY35
    tree = ast.parse("[2, *range(10), 1]")
    StarredUnpackingTransformer().visit(tree)
    if IS_PY35:
        exec(compile(tree, filename="<ast>", mode="exec"))
    assert eval(compile(tree, filename="<ast>", mode="eval")) == [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]



# Generated at 2022-06-14 02:26:56.098085
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*[1, *[2]], 3, *range(4), *range(4), sep=' ')")
    StarredUnpackingTransformer().visit(tree)
    compiled = compile(tree, filename="<ast>", mode="eval")
    assert eval(compiled) == "1 2 3 0 1 2 3 "


# Generated at 2022-06-14 02:26:59.519570
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = "print(*range(1), *range(3))"
    expected_code = "print(*(list(range(1)) + list(range(3))))"
    node = ast.parse(code)
    node = StarredUnpackingTransformer().visit(node)
    assert ast.dump(node) == expected_code
