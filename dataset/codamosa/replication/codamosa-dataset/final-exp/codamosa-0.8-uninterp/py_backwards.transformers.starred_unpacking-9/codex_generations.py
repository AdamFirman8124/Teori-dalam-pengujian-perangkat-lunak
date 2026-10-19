

# Generated at 2022-06-14 02:17:04.322574
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    source = [2, *range(10), 1]
    
    expected_result = [2] + list(range(10)) + [1]

    class DummyTransformer:
        tree_changed = False
        def generic_visit(self, node):
            return node

    node = ast.parse(str(source))
    dst = StarredUnpackingTransformer()
    dst.generic_visit = DummyTransformer.generic_visit
    result = dst.visit(node)
    code = compile(result, '<ast>', 'eval')
    assert eval(code) == expected_result
    # Results
    assert dst.tree_changed



# Generated at 2022-06-14 02:17:16.580602
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
    print(*range(1), *range(3))
    """.strip()

    node = ast.parse(code)
    StarredUnpackingTransformer().visit(node)

# Generated at 2022-06-14 02:17:20.183686
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"
    result = StarredUnpackingTransformer(source).run()
    assert expected == result



# Generated at 2022-06-14 02:17:32.918710
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from ast_tools.transforms.visitor import to_source

    test_cases = [
        (
            '[2, 3, 4]',
            '[2, 3, 4]'
        ),
        (
            '[*range(1), 2, 3]',
            '[2] + list(range(1)) + [3]'
        ),
        (
            '[2, *range(1), 3]',
            '[2] + list(range(1)) + [3]'
        ),
        (
            '[2, 3, *range(1)]',
            '[2, 3] + list(range(1))'
        ),
    ]

    t = StarredUnpackingTransformer()
    for test_case in test_cases:
        src, expected = test_case

# Generated at 2022-06-14 02:17:37.834902
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from astor.code_gen import to_source

    code = """print(*range(1), *range(3))"""

    # without transform
    expected = code

    # with transform
    result = to_source(StarredUnpackingTransformer().visit(ast.parse(code)))

    assert expected == result


# Generated at 2022-06-14 02:17:42.262654
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import ast as stdlib_ast
    import astor
    input_str = "[2, *range(10), 1]"
    tree = stdlib_ast.parse(input_str)
    StarredUnpackingTransformer.run(tree)
    assert astor.to_source(tree) == '[2] + list(range(10)) + [1]'


# Generated at 2022-06-14 02:17:45.133200
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert isinstance(StarredUnpackingTransformer().visit(
        ast.parse('print(x, *y, *z, 1, 2)').body[0].value
    ), ast.Call)


# Generated at 2022-06-14 02:17:49.774465
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("ListAuthors(filter(lambda a: a.book_count > 1, authors), 'id')")
    assert not isinstance(tree.body[0].value.args[0], ast.Call)
    StarredUnpackingTransformer().visit(tree)
    assert isinstance(tree.body[0].value.args[0], ast.Call)

# Generated at 2022-06-14 02:17:55.224243
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("a = [1, 'a', *range(10)]")
    StarredUnpackingTransformer().visit(node)
    assert ast.dump(node) == '''\
a = [1, 'a'] + list(range(10))
'''



# Generated at 2022-06-14 02:18:04.840846
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    sample = """def foo():
            l = [2, *range(10), 1]
            return l
            """
    expected = """def foo():
            l = [2] + list(range(10)) + [1]
            return l
            """
    actual = StarredUnpackingTransformer().visit(ast.parse(sample))
    assert ast.dump(
        ast.parse(expected), DumpFilter(), indent_with=' ') == ast.dump(
        actual, DumpFilter(), indent_with=' ')


# Generated at 2022-06-14 02:18:21.475506
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from py_mini_racer.ast_compiler import Compiler
    from .base import _code_to_ast, _ast_to_code
    from .base import HexastTransformer
    from .base import BaseNodeTransformer

    class DummyTransformer(BaseNodeTransformer):
        def _visit_list_of_args(self, args: Iterable[ast.expr]) -> Iterable[ast.expr]:
            for arg in args:
                yield self.generic_visit(arg)

    class DummyTransformer2(DummyTransformer):
        # noinspection PyUnusedLocal
        def visit_Name(self, node: ast.Name) -> ast.Name:
            return ast.Name(id=node.id, ctx=node.ctx)


# Generated at 2022-06-14 02:18:27.652184
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    input = ast.parse("print(*range(1), *range(3))")
    StarredUnpackingTransformer().visit(input)
    assert "print(*(list(range(1)) + list(range(3))))" == astunparse.unparse(input).rstrip()


# Generated at 2022-06-14 02:18:38.580961
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    func_body = ast.parse("""
        print(1, 2, 3, *range(4), 5, *[6, 7], *range(8), 9)
        print(1, 2, 3, *range(4), 5, *range(6))
    """).body # type: List[ast.stmt]
    expected_ast = ast.parse('''
        print(*(list([1, 2, 3]) + list(range(4)) + list([5]) + list([6, 7]) + list(range(8)) + list([9])))
        print(*(list([1, 2, 3]) + list(range(4)) + list([5]) + list(range(6))))
    ''').body

    result = StarredUnpackingTransformer().visit(func_body)
    assert result == expected_ast



# Generated at 2022-06-14 02:18:46.055051
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
        print(*range(1), *range(3))
    """
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:18:51.378461
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = '[2, *range(10), 1]'
    expected_code = '[2] + list(range(10)) + [1]'
    node = ast.parse(code)

    new_node = StarredUnpackingTransformer().visit(node)

    assert new_node is not None
    assert get_source(new_node) == expected_code


# Generated at 2022-06-14 02:19:02.855928
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .transformer import Compiler

    source = '[2, *range(10), 1]'
    expect = '[2] + list(range(10)) + [1]'

    tree = ast.parse(source)
    compiler = StarredUnpackingTransformer()
    compiler.visit(tree)
    tree = Compiler().visit(tree)

    assert tree.body[0].value.left.op.__class__.__name__ == 'Add'
    assert tree.body[0].value.right.op.__class__.__name__ == 'Add'
    assert tree.body[0].value.func.id == 'list'

    # To test the result, we compile it by the Compiler.
    compiler = Compiler()
    code = compiler.visit(tree)


# Generated at 2022-06-14 02:19:11.031359
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3
    from .base import BaseNodeTransformerTesterMixin, BaseNodeVisitorTesterMixin, BaseNodeTransformer
    StarredUnpackingTransformerTesterMixin = type(
        'StarredUnpackingTransformerTesterMixin',
        (BaseNodeTransformerTesterMixin,),
        {'transformer_class': StarredUnpackingTransformer})
    tester = StarredUnpackingTransformerTesterMixin()
    source = 'print(*range(1), *range(3))'
    expected_tree = ast3.parse(
        'print(*(list(range(1)) + list(range(3))))')
    tester.test(
        expected_tree=expected_tree,
        source=source,
        filename='<test>')
    return


# Generated at 2022-06-14 02:19:17.622835
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
        [2, *range(10), 1]
    """

    expected_code = """
        [2] + list(range(10)) + [1]
    """

    tree = ast.parse(code)
    expected_tree = ast.parse(expected_code)
    StarredUnpackingTransformer(tree).visit(tree)
    assert ast.dump(tree) == ast.dump(expected_tree)


# Generated at 2022-06-14 02:19:24.720581
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    #GIVEN
    code = """foo(1, *[2, 3], 4)"""
    expected_code = """foo(*(list([1]) + list([2, 3]) + list([4])))"""
    #WHEN
    StarredUnpackingTransformer().visit(ast.parse(code))
    #THEN
    assert ast.dump(ast.parse(expected_code)) == ast.dump(ast.parse(code))

# Generated at 2022-06-14 02:19:34.702438
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # (1 + 3) + (2 + 4) => [1, 3] + [2, 4]
    assert ast.dump(
        StarredUnpackingTransformer().visit(
            ast.parse("[1, 3] + [1, 2, 3]", mode='eval')),
        include_attributes=True) == \
        ast.dump(
            ast.BinOp(left=ast.List(elts=[ast.Constant(value=1, kind=None), ast.Constant(value=3, kind=None)]), right=ast.List(elts=[ast.Constant(value=1, kind=None), ast.Constant(value=2, kind=None), ast.Constant(value=3, kind=None)]), op=ast.Add()),
            include_attributes=True)
    # (

# Generated at 2022-06-14 02:19:48.652890
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import sys
    import astunparse
    from .base import BaseNodeTransformerTest

    class Test(BaseNodeTransformerTest):
        def create_transformer(self):
            return StarredUnpackingTransformer()

    code_1 = '''\
        [2, *range(10), 1]
        '''
    res_1 = '''\
        [2] + list(range(10)) + [1]
        '''
    Test.test(code_1, res_1, True)

    code_2 = '''\
        [2, *range(10), 1, *range(2), *list(range(3))]
        '''

# Generated at 2022-06-14 02:19:55.733488
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("""
print(*range(1), *range(3))
    """)
    expected = ast.parse("""
print(*(list(range(1)) + list(range(3))))
    """)
    node = StarredUnpackingTransformer()
    result = node.visit(tree)
    assert result == expected


# Generated at 2022-06-14 02:20:03.074682
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    print('Unit test for method visit_Call of class StarredUnpackingTransformer')
    source = 'print(1, *range(2), 3, *range(10))'
    sample = ast.parse(source)

    StarredUnpackingTransformer().visit(sample)
    assert to_source(sample) == "print(*(list([1]) + list(range(2)) + list([3]) + list(range(10))))"


# Generated at 2022-06-14 02:20:08.632181
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert (StarredUnpackingTransformer().visit(ast.parse('[2, *range(10), 1]')) == ast.parse('[2] + list(range(10)) + [1]'))
    assert (StarredUnpackingTransformer().visit(ast.parse('print(*range(1), *range(3))')) == ast.parse('print(*(list(range(1)) + list(range(3))))'))

# Generated at 2022-06-14 02:20:17.428458
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import round_trip

    source = """\
    print(*range(1), *range(3))
    """
    expected = """\
    print(*(list(range(1)) + list(range(3))))
    """
    ast_tree = round_trip(source)
    transformer = StarredUnpackingTransformer()
    transformer.visit(ast_tree)
    # print(astor.to_source(ast_tree))
    assert expected == astor.to_source(ast_tree).strip()



# Generated at 2022-06-14 02:20:25.577004
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()

    node = ast.parse("print(1, 2)", "<test>")
    expected_node = ast.parse("print(list((1, 2)))", "<test>")
    transformer.visit(node)
    assert transformer._tree_changed
    assert ast.dump(transformer.toplevel, include_attributes=False) == ast.dump(expected_node, include_attributes=False)

    transformer = StarredUnpackingTransformer()
    node = ast.parse("print(*range(1), *range(3))", "<test>")
    expected_node = ast.parse("print(*(list(range(1)) + list(range(3))))", "<test>")
    transformer.visit(node)
    assert transformer._tree_changed

# Generated at 2022-06-14 02:20:37.197002
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Arrange
    input = [ast.List(
            elts=[
                ast.Num(n=2),
                ast.Starred(
                    value=ast.Call(
                        func=ast.Name(id='range'),
                        args=[ast.Num(n=10)],
                        keywords=[]),
                    ctx=ast.Load()),
                ast.Num(n=1)],
            ctx=ast.Load())]

# Generated at 2022-06-14 02:20:48.057844
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    prog_string = "print(*range(1), *range(3))"
    root = ast.parse(prog_string)
    StarredUnpackingTransformer().visit(root)

# Generated at 2022-06-14 02:20:55.322932
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

    source = 'range(10)[*range(1,10)]'
    expected_source = 'range(10)[0:10]'
    tree = ast.parse(source)

    transformer = StarredUnpackingTransformer()
    transformed_tree = transformer.visit(tree)

    assert astor.to_source(transformed_tree) == expected_source
    assert tree is not transformed_tree
    assert transformer._tree_changed == True


# Generated at 2022-06-14 02:21:08.796646
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('f(a, b, *c, d)')
    new_tree = StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:21:22.627722
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base_tests import check
    code = 'print(*range(2), *range(3, 5))'
    tree = ast.parse(code)

    check(StarredUnpackingTransformer, code, tree)

# Generated at 2022-06-14 02:21:33.175718
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(1, *[2, 3], 4, *range(10), 9)')
    trans = StarredUnpackingTransformer()
    trans.visit(node)

# Generated at 2022-06-14 02:21:38.663707
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("""
    print(*range(1), 2, *range(4))
    """)
    expected = """
    print(*(list(range(1)) + [2] + list(range(4))))
    """
    StarredUnpackingTransformer().visit(node)
    assert astor.to_source(node).strip() == expected.strip()


# Generated at 2022-06-14 02:21:50.764248
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    assert ast.dump(t.visit(ast.parse('print(*range(1))').body[0])) == \
        "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Constant(value=1, kind=None)], keywords=[])], keywords=[])], keywords=[]))"

# Generated at 2022-06-14 02:22:00.859911
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3
    from .ast_compare import compare_ast
    from .testing_utils import pretty_source
    from .transformer import Transformer

    src = 'print(*range(1), *range(3))\n'
    expected = pretty_source('print(*(list(range(1)) + list(range(3))),)\n')

    module = ast.parse(src)
    target = Transformer(StarredUnpackingTransformer)
    result = target.visit(module)
    compare_ast(result, expected)

    # Just a fake test to increase coverage
    transformer = StarredUnpackingTransformer()
    assert transformer._has_starred([]) == False
    assert transformer._has_starred([ast3.Starred(value='1')]) == True


# Generated at 2022-06-14 02:22:11.988849
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_base import compile, transform

    source = """
        print(*range(1), *range(5))
        """.strip()

    print_func = transform(compile(source, "", "exec").body[0],
                           StarredUnpackingTransformer)


# Generated at 2022-06-14 02:22:23.501131
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .util import source_to_node

    node = source_to_node("print(*range(1), *range(3))")
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    node = StarredUnpackingTransformer(True).visit(node)
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)

# Generated at 2022-06-14 02:22:28.467094
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from ..compiler import to_source
    source = '[2, *range(10), 1]'
    source_expected = '[2] + list(range(10)) + [1]'
    module = ast.parse(source)
    result = StarredUnpackingTransformer().visit(module)
    assert to_source(result) == source_expected
    source = 'print(*range(1), *range(3))'
    source_expected = 'print(*(list(range(1)) + list(range(3))))'
    module = ast.parse(source)
    result = StarredUnpackingTransformer().visit(module)
    assert to_source(result) == source_expected

# Generated at 2022-06-14 02:22:30.746767
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    tmp = StarredUnpackingTransformer()
    assert tmp


# Generated at 2022-06-14 02:22:40.853558
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # type: () -> None
    lst = ast.parse('[2, *range(10), 1]').body[0].value

    assert isinstance(lst, ast.List)
    assert len(lst.elts) == 3
    assert isinstance(lst.elts[1], ast.Starred)

    transformed = StarredUnpackingTransformer().visit(lst)
    assert isinstance(transformed, ast.Call)

    assert isinstance(transformed.func, ast.Name)
    assert transformed.func.id == 'list'

    assert isinstance(transformed.args[0], ast.BinOp)
    assert isinstance(transformed.args[0].left, ast.BinOp)
    assert isinstance(transformed.args[0].right, ast.List)

# Generated at 2022-06-14 02:23:13.923832
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    t = StarredUnpackingTransformer()
    node = ast.List(elts=[ast.Num(n=2), ast.Starred(value=ast.Call(
        func=ast.Name(id='range'), args=[ast.Num(n=10)], keywords=[]), ctx=ast.Load()), ast.Num(n=1)], ctx=ast.Load())

    result = t.visit(node)

    assert isinstance(result, ast.List)
    assert len(result.elts) == 1
    assert isinstance(result.elts[0], ast.BinOp)
    assert len(result.elts[0].elts) == 3
    assert isinstance(result.elts[0].elts[0], ast.List)

# Generated at 2022-06-14 02:23:22.784058
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import textwrap
    from .test_utils import roundtrip

    source_code = textwrap.dedent('''\
        [2, *range(10), 1]
    ''')

    expected = textwrap.dedent('''\
        [2] + list(range(10)) + [1]
    ''')

    roundtrip(source_code, expected, StarredUnpackingTransformer)


# Generated at 2022-06-14 02:23:31.774796
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from astor.misc import dump
    from .test_misc import compile_node_or_raise

    code = "print(1, *range(2))"
    compiled = compile_node_or_raise(code, StarredUnpackingTransformer, mode="exec")

    result = dump(compiled, include_attributes=True)
    expected = dump(compile(
        "print(*(list([1]) + list(range(2))))",
        filename="",
        mode="exec",
        ), include_attributes=True)

    assert result == expected


# Generated at 2022-06-14 02:23:33.628020
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    s = StarredUnpackingTransformer()
    assert s is not None

# Generated at 2022-06-14 02:23:43.814739
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = '[2, *range(10), 1]'
    module = ast.parse(code, mode='exec')
    code_gen = compile(module, filename='<ast>', mode='exec')

    obj = StarredUnpackingTransformer()
    module = obj.visit(module)
    code_gen2 = compile(module, filename='<ast>', mode='exec')

    ns = {}
    exec(code_gen, ns)
    exec(code_gen2, ns)
    assert ns['__builtins__'] is builtins
    assert ns['_result'] == ns['_result2']



# Generated at 2022-06-14 02:23:45.293701
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().target == (3, 4)


# Generated at 2022-06-14 02:23:52.737654
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    class_transformer = StarredUnpackingTransformer()
    node = ast.parse('print(1, 2, 3, *[4, 5, 6])')
    updated = class_transformer.visit(node)
    print(astor.to_source(updated))
    assert astor.to_source(updated) == '''print(*(list([1, 2, 3]) + list([4, 5, 6])))
'''
    class_transformer.run_code('print(1, 2, 3, *[4, 5, 6])')


# Generated at 2022-06-14 02:23:59.427128
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expected = ast.parse('a = list(range(2)) + [1, [2], list(range(3))] + [1]')
    result = StarredUnpackingTransformer().visit(ast.parse('a = [2, *range(2), 1, [2], *[list(range(3))], 1]'))
    print(result)
    assert ast.dump(expected) == ast.dump(result)


# Generated at 2022-06-14 02:24:08.581291
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code_before = """\
s = 0
s += sum(range(3))
"""
    code_after = """\
s = 0
s += sum(*(list(range(3))))
"""
    with subTest(name='Data before transf'):
        tree_before = ast.parse(code_before)
        assert_code(tree_before, code_before)
    with subTest(name='Unit test for method visit_Call of class CallFormatter'):
        tree_after = StarredUnpackingTransformer().visit(tree_before)
        assert_code(tree_after, code_after)

    # test with tree already changed
    code_before = """\
s = 0
s += sum(*(list(range(3))))
"""
    tree_before = ast.parse(code_before)
    star = Starred

# Generated at 2022-06-14 02:24:15.063617
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse
    source = """a( *b, *c)"""
    tree = typed_ast.ast3.parse(source)
    expected_tree = ast.parse("""a(*(list(b) + list(c)))""")
    StarredUnpackingTransformer().visit(tree)
    assert unparse(tree) == unparse(expected_tree)


# Generated at 2022-06-14 02:25:10.186243
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:25:16.065896
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer()
    code = """
        [2, *range(10), 1]
        print(*range(1), *range(3))
        print(1)
    """
    tree = ast.parse(code)
    trans.visit(tree)
    exec(compile(tree, '', 'exec'))

# Generated at 2022-06-14 02:25:27.972665
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expected = ast.List(
        elts=[
            ast.List(elts=[ast.Num(n=2)]),
            ast.Call(
                func=ast.Name(id='list'),
                args=[
                    ast.Call(
                        func=ast.Name(id='range'),
                        args=[ast.Num(n=10)],
                        keywords=[]
                    )
                ]
            ),
            ast.List(elts=[ast.Num(n=1)])
        ]
    )
    expected = StarredUnpackingTransformer.visit(expected)

# Generated at 2022-06-14 02:25:39.505056
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """
    Test for method visit_Call of StarredUnpackingTransformer
    """
    import ast
    import textwrap
    from ministarlint.transformers.starred_unpacking import StarredUnpackingTransformer
    print("Test for method visit_Call of StarredUnpackingTransformer")
    print("Expected:\nprint(*(list(range(1)) + list(range(3))))")
    print("Measured:")

    node = ast.parse(textwrap.dedent("""\
    print(*range(1), *range(3))
    """))

    transformer = StarredUnpackingTransformer()
    node = transformer.visit(node)
    print(ast.dump(node))
    print("")


# Generated at 2022-06-14 02:25:41.013483
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()


# Generated at 2022-06-14 02:25:49.997334
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from tests.assembler_test_utils import assert_assembler_equivalent

    assert_assembler_equivalent(
        "[2, *range(10), 1]",
        "[2] + list(range(10)) + [1]")

    assert_assembler_equivalent(
        "print(*range(1), *range(3))",
        "print(*(list(range(1)) + list(range(3))))")

    assert_assembler_equivalent(
        "f(*range(1), *range(3))",
        "f(*(list(range(1)) + list(range(3))))")

# Generated at 2022-06-14 02:25:59.069163
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    ast_node = ast.parse('[2, *range(10), 1]').body[0].value
    assert ast_node == ast.List(elts=[ast.Num(n=2), ast.Starred(value=ast.Call(
        func=ast.Name(id='range'),
        args=[ast.Num(n=10)],
        keywords=[])), ast.Num(n=1)])
    node_transformed = StarredUnpackingTransformer().visit(  # type: ignore
        ast_node)

# Generated at 2022-06-14 02:26:10.360036
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import BaseNodeTransformerTest
    from typed_ast import ast3 as ast
    from custom_parser.parser_4 import Python4Parser

    class StarredUnpackingTransformerTest(BaseNodeTransformerTest):
        target = (3, 4)
        transformer = StarredUnpackingTransformer

        def assertTransformedAst(self, src, expected_ast, transformer=None):
            assert src == self.unparse(expected_ast)
            ast_tree = self.parse(src)
            transformed_ast_tree = self.transform(ast_tree)
            assert expected_ast == transformed_ast_tree
            if transformer:
                assert transformer._tree_changed is True

    StarredUnpackingTransformerTest.generate_test_methods(globals())


# Generated at 2022-06-14 02:26:22.506312
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_helpers import assert_equal  # type: ignore
    st = StarredUnpackingTransformer()

    assert_equal(
        st.visit(ast.parse('[2, *range(10), 1]')),
        ('[2] + list(range(10)) + [1]', True))  # type: ignore

    assert_equal(
        st.visit(ast.parse('list([2, *range(10), 1])')),
        ('list([2] + list(range(10)) + [1])', True))  # type: ignore

    assert_equal(
        st.visit(ast.parse('print(*range(1), *range(3))')),
        ('print(*(list(range(1)) + list(range(3))))', True))  # type: ignore

    assert_equal

# Generated at 2022-06-14 02:26:28.636668
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import NodeTestCase
