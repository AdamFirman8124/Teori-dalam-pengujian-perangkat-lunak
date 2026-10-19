

# Generated at 2022-06-14 02:17:12.745431
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse(
        'print(*range(1), *range(3))')
    expected_tree = ast.parse(
        'print(*(list(range(1)) + list(range(3))))')
    transformer = StarredUnpackingTransformer()
    out_tree = transformer.visit(tree)

    assert astor.to_source(out_tree) == astor.to_source(expected_tree)



# Generated at 2022-06-14 02:17:20.273428
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    node = ast.parse("print(*range(1), *range(3))").body[0]
    node = ast.copy_location(transformer.visit(node), node)

    expected = ast.parse("print(*list(range(1))+list(range(3)))")
    expected = ast.copy_location(expected.body[0], node)

    assert ast.dump(expected, annotate_fields=False) == ast.dump(node, annotate_fields=False)



# Generated at 2022-06-14 02:17:25.275703
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test import run_test_transform

    code = 'a = (1,); print(*a)'
    expected = 'a = (1,); print(a[0])'

    run_test_transform(StarredUnpackingTransformer, code, expected)

# Generated at 2022-06-14 02:17:31.414693
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import sys
    import typed_astunparse
    import astunparse

    code = "[2, *range(10), 1]"
    expected = astunparse.unparse(ast.parse(code)).strip()

    module = ast.parse(code)
    StarredUnpackingTransformer().visit(module)
    result = typed_astunparse.unparse(module).strip()

    assert result == expected
    print('Tested {}: {}'.format(StarredUnpackingTransformer.__name__, code))


# Generated at 2022-06-14 02:17:41.174512
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Test for method visit_List of class StarredUnpackingTransformer."""
    from .unparse import Unparser
    from .source import get_source
    from .dump import dump_ast

    source = '[2, *range(10), 1, *range(4)]'

    tree = ast.parse(source)
    dump_ast(tree)
    
    StarredUnpackingTransformer().visit(tree)
    dump_ast(tree)

    assert Unparser(tree) == 'list([2]) + list(range(10)) + [1] + list(range(4))'
    assert get_source(tree) == 'list([2]) + list(range(10)) + [1] + list(range(4))'


# Generated at 2022-06-14 02:17:50.537512
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List(elts=[ast.Num(n=2),
                         ast.Starred(value=ast.Call(func=ast.Name(id='range'),
                                                    args=[ast.Num(n=10)],
                                                    keywords=[])),
                         ast.Num(n=1)])
    transformer = StarredUnpackingTransformer()
    result = transformer.visit_List(node)

# Generated at 2022-06-14 02:18:02.031275
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_tools import make_call_test
    test_func = make_call_test(StarredUnpackingTransformer)
    test_func("print(3)", "print(3)")
    test_func("print(3, *range(1), *range(3))", "print(*(list(range(1)) + list(range(3))) + [3])")
    test_func("print(3, *range(1), *range(3), sep=' ')", "print(*(list(range(1)) + list(range(3))) + [3], sep=' ')")
    test_func("print(3, *range(1), *range(3), 5)", "print(*(list(range(1)) + list(range(3)) + [3, 5]))")

# Generated at 2022-06-14 02:18:14.338127
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3), ast.Num(n=4), ast.Starred(ast.Name(id='test'))],
        keywords=[])


# Generated at 2022-06-14 02:18:17.492159
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expect = [2, 3, 4]
    actual = StarredUnpackingTransformer.run('[2, *[3], *[], 4]')
    assert expect == actual
    

# Generated at 2022-06-14 02:18:32.714350
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class StarredUnpackingTransformerTest(StarredUnpackingTransformer):
        pass

    tree = ast.parse('''
    print(1, *range(3), 2)
    print(*range(3))
    print()
    ''')

    StarredUnpackingTransformerTest().visit(tree)


# Generated at 2022-06-14 02:18:47.611702
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
        #arrange
        code  = "print(*range(1), *range(3))"
        root = compile_code(code, mode="exec")
        #act
        StarredUnpackingTransformer().visit(root)
        #assert
        new_code = astor.to_source(root)
        assert new_code == "print(*(list(range(1)) + list(range(3))))\n"

        code  = "[2, *range(10), 1]"
        root = compile_code(code, mode="exec")
        #act
        StarredUnpackingTransformer().visit(root)
        #assert
        new_code = astor.to_source(root)
        assert new_code == "[2] + list(range(10)) + [1]\n"

# Generated at 2022-06-14 02:18:49.541580
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()
    """StarredUnpackingTransformer()"""

# Generated at 2022-06-14 02:18:52.191577
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()
    print(transformer)

if __name__ == "__main__":
    test_StarredUnpackingTransformer()

# Generated at 2022-06-14 02:19:03.595534
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import roundtrip_unparse_cmp

    def do_test(source: str) -> None:
        roundtrip_unparse_cmp(
            StarredUnpackingTransformer, source,
            source.replace('[*', '[')
        )

    do_test('[*[1, 2]]')
    do_test('[*[1, 2], 3, 4]')
    do_test('[1, 2, *[3, 4]]')
    do_test('[1, 2, *[3, 4], 5, 6]')
    do_test('[*[1, 2], 3, 4, *[5, 6]]')
    do_test('[1, 2, *[3, 4], *[5, 6], 7, 8]')


# Generated at 2022-06-14 02:19:10.215957
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    st = """print(1, 2, *range(3), 3, *range(1, 5), 4)"""

    tr = StarredUnpackingTransformer()
    tr.visit(ast.parse(st))
    assert tr._tree_changed
    assert str(tr.root) == 'print(*(list(range(3)) + list(range(1, 5))))'

# Generated at 2022-06-14 02:19:18.090667
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer."""
    def run(code: str) -> str:
        """Run `code` through the transformer."""
        tree = ast.parse(code)
        StarredUnpackingTransformer().visit(tree)
        return compile(tree, '', 'exec')

    assert run('print(*range(1), *range(3))') == compile(
        'print(*(list(range(1)) + list(range(3))))',
        '', 'exec')


# Generated at 2022-06-14 02:19:29.838820
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert eval(
        """
        from typed_ast.ast3 import parse
        from typed_ast.transforms import StarredUnpackingTransformer

        node = parse("[2, *range(10), 1]")
        transformer = StarredUnpackingTransformer()
        node = transformer.visit(node)
        node = node.body[0].value.elts
        """) == [ast.Num(n=2),
                 ast.Call(
                     func=ast.Name(id='list'),
                     args=[ast.Call(
                         func=ast.Name(id='range'),
                         args=[ast.Num(n=10)],
                         keywords=[])],
                     keywords=[]),
                 ast.Num(n=1)]



# Generated at 2022-06-14 02:19:30.702183
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:19:41.485362
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Test that StarredUnpackingTransformer.visit_List:
    # 1. preserves other List nodes
    # 2. converts List nodes with Starred to sum of lists
    utils.assert_source_equal(
        StarredUnpackingTransformer().visit(ast.parse("[2, 3]")),
        ast.parse("[2, 3]"))
    utils.assert_source_equal(
        StarredUnpackingTransformer().visit(ast.parse("[2, *range(10), *range(3)]")),
        ast.parse("[2] + list(range(10)) + list(range(3))"))
    # 3. converts List nodes with Starred to sum of lists, even if there are arguments

# Generated at 2022-06-14 02:19:42.563301
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    print(StarredUnpackingTransformer())

# Generated at 2022-06-14 02:19:52.688393
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test = """
        print(1, *range(3), 6)
    """
    expected = """
        print(*(list([1]) + list(range(3)) + list([6])))
    """
    assert expected == StarredUnpackingTransformer().visit(ast.parse(test))



# Generated at 2022-06-14 02:19:59.664388
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from compile2 import compile2
    from textwrap import dedent
    a = dedent('''\
        def f():
            print(1, 2, *range(3))
            ''')
    b = dedent('''\
        def f():
            print(*(list([1]) + list([2]) + list(range(3))))
            ''')
    assert compile2(a) == b



# Generated at 2022-06-14 02:20:03.009040
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    input = """
    print(*range(10), *range(20))
    """

    output = """
    print(*(list(range(10)) + list(range(20))))
    """

    assert transform(input) == output



# Generated at 2022-06-14 02:20:10.970148
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # WHEN
    tr = StarredUnpackingTransformer()
    arg = ast.parse('[1, 2, 3]').body[0].value
    node = ast.Call(func=ast.Name(id='print'), args=[arg], keywords=[], starargs=None, kwargs=None)

    # THEN
    assert tr.visit(node) == ast.Call(func=ast.Name(id='print'), args=[ast.Starred(value=ast.List(elts=[ast.Num(n=1), ast.Num(n=2), ast.Num(n=3)]))], keywords=[], starargs=None, kwargs=None)

# Generated at 2022-06-14 02:20:20.253403
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    from . import BaseNodeTransformerTest
    from typed_ast import ast3 as ast

    class Test(BaseNodeTransformerTest):
        TRANSFORMER = StarredUnpackingTransformer
        EXAMPLE = """
            [2, *range(10), 1]
        """


# Generated at 2022-06-14 02:20:32.853844
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    filename = 'dummy'

    # Given
    code = """
list(range(5))
    """
    # When
    ast_tree = ast.parse(code, filename=filename)
    StarredUnpackingTransformer().visit(ast_tree)
    # Then
    expected = ast.parse(code, filename=filename)
    assert ast.dump(ast_tree) == ast.dump(expected)

    # Given
    code = """
list(range(5), 2, *(1, 2, 3))
    """

    # When
    ast_tree = ast.parse(code, filename=filename)
    StarredUnpackingTransformer().visit(ast_tree)
    # Then

# Generated at 2022-06-14 02:20:33.928011
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer()

# Generated at 2022-06-14 02:20:42.016606
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = 'a = [1, *range(5), *[5, 6], *range(11, 17), 2][1:]'
    node = ast.parse(tree)

    expected = 'a = (list(range(5)) + [5, 6] + list(range(11, 17)) + [2])[1:]'
    expected = ast.parse(expected)

    node = StarredUnpackingTransformer().visit(node)
    assert ast.dump(node) == ast.dump(expected)



# Generated at 2022-06-14 02:20:45.566199
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    st = ast.parse("[2, *range(10), 1]\nprint(*range(1), *range(3))")
    t = StarredUnpackingTransformer()
    t.visit(st)
    print(ast.dump(st))

# Generated at 2022-06-14 02:20:56.442198
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List(elts=[
        ast.Constant(value=1, kind=None),
        ast.Starred(value=ast.Name(id='r', ctx=ast.Load())),
        ast.Constant(value=2, kind=None),
        ast.Starred(value=ast.Name(id='m', ctx=ast.Load())),
        ast.Constant(value=3, kind=None)
        ], ctx=ast.Load())

# Generated at 2022-06-14 02:21:05.039825
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    assert StarredUnpackingTransformer().visit(code) == '([2] + list(range(10)) + [1])'



# Generated at 2022-06-14 02:21:10.175774
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class DummyTransformer(BaseNodeTransformer):
        target = ()
        def visit_List(self, node):
            return node
    t = StarredUnpackingTransformer()
    assert(str(t.visit(DummyTransformer().visit(ast.parse('print(*range(1), *range(3))'))))
           == 'print(*(list(range(1)) + list(range(3))))')



# Generated at 2022-06-14 02:21:21.755291
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    tree = ast.parse("""[2, *range(10), 1]
    print(*range(1), *range(3))
    """)
    res = StarredUnpackingTransformer().visit(tree)
    assert res.body[0].value.left.elts[0].n == 2
    assert res.body[0].value.right.elts[0].n == 1
    assert res.body[0].value.left.elts[1].args[0].n == 10
    assert res.body[1].value.args[0].value.left.args[0].n == 1
    assert res.body[1].value.args[0].value.right.args[0].n == 3

# Generated at 2022-06-14 02:21:26.001638
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .transforms import TestTransforms
    TestTransforms(StarredUnpackingTransformer).test_file('call_with_star.py')

# Generated at 2022-06-14 02:21:30.824104
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    node = ast.parse('[2, *range(10), 1]')
    expected = '[2] + list(range(10)) + [1]'
    result_node = transformer.visit(node)
    assert astor.to_source(result_node) == expected


# Generated at 2022-06-14 02:21:41.731827
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = ast.parse("""
print(*range(5), 1, 2, 3, *range(1))
""")
    expected_code = ast.parse("""
print(*((list(range(5)) + [1]) + [2] + [3] + list(range(1))))
"""
                            )
    expected_code_2 = ast.parse("""
print(*((list(range(5)) + [1]) + list([2] + [3] + list(range(1)))))
"""
                            )
    StarredUnpackingTransformer().visit(code)

# Generated at 2022-06-14 02:21:47.752283
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    unpack = StarredUnpackingTransformer()
    assert unpack.visit(ast.parse('print(*range(1), *range(5))').body[0]) == \
           ast.parse('print(*(list(range(1)) + list(range(5))))').body[0]


# Generated at 2022-06-14 02:21:55.517726
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_source = '''[2, *range(10), 1]'''
    expected_result = '''[2] + list(range(10)) + [1]'''
    assert apply_transform(StarredUnpackingTransformer, test_source) == expected_result

    test_source = '''[*range(10), *range(10), 1]'''
    expected_result = '''list(range(10)) + list(range(10)) + [1]'''
    assert apply_transform(StarredUnpackingTransformer, test_source) == expected_result


# Generated at 2022-06-14 02:22:06.006565
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    test_list1 = ('[2, *range(10), 1]', 'list(range(10))', 'list')
    test_list2 = ('[2, *range(10), 1]', 'list(range(10))', 'list', 'add')
    test_list3 = ('[2, *range(10), 1]', '{}<-Tuple[Union[List[expr], Starred]]', '{}<-List[expr]', '{}<-expr', '{}<-Call', '{}<-Name', '{}<-str', 'list', 'add')
    test_list4 = list(range(20))
    tuple_list = ()
    print('test_StarredUnpackingTransformer')
    if 'list' in test_list1:
        print('true')

# Generated at 2022-06-14 02:22:09.475028
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    result = StarredUnpackingTransformer.run(
        """print(*range(1), *range(3))""")
    assert result.strip() == """print(*(list(range(1)) + list(range(3))))"""


# Generated at 2022-06-14 02:22:23.834590
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    simple = ast.List(elts=[
        ast.Num(n=2),
        ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Num(n=10)], keywords=[])),
        ast.Num(n=1)
    ])
    expected = ast.List(elts=[
        ast.Num(n=2),
        ast.BinOp(left=ast.List(elts=[]), right=ast.List(elts=[ast.Num(n=9)]), op=ast.Add()),
        ast.Num(n=1)
    ])

    assert StarredUnpackingTransformer().visit(simple) == expected


# Generated at 2022-06-14 02:22:36.554950
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class Dict(dict):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    tree_dict = Dict(
        body=[
            Dict(
                func=Dict(
                    args=[
                        Dict(
                            func=Dict(
                                id='list'
                            ),
                            args=[
                                Dict(
                                    n=2,
                                    s='2',
                                ),
                            ]
                        ),
                    ],
                    keywords=[],
                ),
                lineno=1,
                col_offset=0,
            ),
        ],
        col_offset=0,
        lineno=1,
        type_ignores=[],
    )
    StarredUnpackingTransformer(tree_dict).visit(tree_dict)

# Generated at 2022-06-14 02:22:52.618030
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import inspect
    from ast import parse
    from .common import unit_test, compile_for_lldb

    def test_it(src, expected):
        source_code = inspect.getsource(src)
        source_ast = parse(source_code)
        source_ast_modified = StarredUnpackingTransformer().visit(source_ast)

        compile_for_lldb(source_ast_modified, 'tmp.py')
        exec(compile(source_ast_modified, filename="<ast>", mode="exec"), {})

    @unit_test
    def test_normal():
        def normal():
            return [1, 2, 3]
        test_it(normal, [1, 2, 3])


# Generated at 2022-06-14 02:23:02.639658
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from textwrap import dedent


# Generated at 2022-06-14 02:23:10.662061
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = """
        [2, *range(10), 1]
    """
    source_ast = ast.parse(source)
    expected = """
        list([2]) + list(range(10)) + list([1])
    """
    expected_ast = ast.parse(expected)

    transformer = StarredUnpackingTransformer()
    result_ast = transformer.visit(source_ast)
    assert ast.dump(result_ast) == ast.dump(expected_ast)



# Generated at 2022-06-14 02:23:16.416977
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test_list = [ast.Name(id="print", ctx=ast.Load()), ast.Starred(value=ast.Name(id="y", ctx=ast.Load()), ctx=ast.Load())]
    test_list2 = [ast.Name(id="print", ctx=ast.Load()), ast.Starred(value=ast.Name(id="y", ctx=ast.Load()), ctx=ast.Load()), ast.Name(id="print", ctx=ast.Load()), ast.Starred(value=ast.Name(id="y", ctx=ast.Load()), ctx=ast.Load())]
    
    testTree = ast.Call(func=ast.Name(id='print'), args=test_list, keywords=[])
    testTree2 = testTree

# Generated at 2022-06-14 02:23:29.239093
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected_ast = ast.parse('''
    def foo(a, *b, c, **d):
        pass
    foo(1, *range(2), 3, *range(4), *range(5), **{'abc': 123})
    ''')
    StarredUnpackingTransformer(expected_ast).visit(expected_ast)


# Generated at 2022-06-14 02:23:33.179667
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    call = ast.parse('print(*range(1), *range(3))').body[0]
    call = transformer.visit(call)
    code = compile(ast.Expression(call), '', 'eval')
    assert eval(code) == None

# Generated at 2022-06-14 02:23:44.634302
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    a = StarredUnpackingTransformer()
    assert ast.dump(a.visit(ast.parse('[2, *range(10), 1]'))) == ast.dump(ast.parse('[2] + list(range(10)) + [1]'))
    assert ast.dump(a.visit(ast.parse('[2,*range(10),1]'))) == ast.dump(ast.parse('[2] + list(range(10)) + [1]'))
    assert ast.dump(a.visit(ast.parse('[2, *range(10),  1]'))) == ast.dump(ast.parse('[2] + list(range(10)) + [1]'))



# Generated at 2022-06-14 02:23:46.671347
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:23:53.179655
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

# Generated at 2022-06-14 02:24:03.575169
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    code_str = """
a = [*range(1, 5)]
b = [*range(3), 3]
c = [*range(3, 0, -1), 5, *range (1, 5)]
d = [*range(1, 2)]
e = [*range(2)]
f = [*range(1, 2)]
g = [*range(2), 3]
    """
    expected_result = """
a = list(range(1, 5))
b = list(range(3)) + [3]
c = list(range(3, 0, -1)) + [5] + list(range(1, 5))
d = list(range(1, 2))
e = list(range(2))
f = list(range(1, 2))
g = list(range(2)) + [3]
"""


# Generated at 2022-06-14 02:24:17.901912
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from .ast_helpers import dump, ast_equals
    from .base import BaseNodeTransformer
    from .starred_unpacking import StarredUnpackingTransformer
    from .pass_manager import PassManager
    from . import example_module

    node = ast.parse("print(*x, *y, *z)")
    pm = PassManager("test:test_StarredUnpackingTransformer_visit_Call")
    pm.add_pass(StarredUnpackingTransformer)
    new_node = pm.run(node)


# Generated at 2022-06-14 02:24:26.591794
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    example1 = ast.parse("[2, *range(10), 1]")
    result1 = StarredUnpackingTransformer().visit(example1)
    assert ast.dump(result1) == "Module(body=[Expr(value=BinOp(left=BinOp(left=List(elts=[Num(n=2)], ctx=Load()), right=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='range', ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[]), op=Add()), right=List(elts=[Num(n=1)], ctx=Load()), op=Add()))])"
    example2 = ast.parse("print(*range(1), *range(3), 4)")
    result

# Generated at 2022-06-14 02:24:37.199321
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_transformer_class import compile_transform
    from .test_transformer_class import get_ast_from_py
    import textwrap

    code = """
        print(*[1], *[2], *[3, 4], *[5, 6, 7], *[8, 9, 10, 11])
    """
    # print the transformed AST if needed
    # get_ast_from_py(code)

    expected = """
        list([1]) + list([2]) + list([3, 4]) + list([5, 6, 7]) + list([8, 9, 10, 11])
    """

    code_compiled = compile_transform(code, StarredUnpackingTransformer)
    assert code_compiled.strip() == textwrap.dedent(expected).strip()


# Generated at 2022-06-14 02:24:49.771830
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='print'),
                    args=[ast.Starred(value=ast.List(elts=[
                        ast.Call(func=ast.Name(id='range'),
                                 args=[ast.Num(n=1)],
                                 keywords=[]),
                        ast.Starred(value=ast.List(elts=[
                            ast.Call(func=ast.Name(id='range'),
                                     args=[ast.Num(n=3)],
                                     keywords=[])],
                                   ctx=ast.Load()))
                    ], ctx=ast.Load()))],
                    keywords=[])


# Generated at 2022-06-14 02:24:57.277009
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class DummyNode:
        pass

    dummy_node = DummyNode()
    node = ast.Call(
        func=dummy_node,
        args=[
            ast.Name(id='a'),
            ast.Starred(ast.Name(id='b'), ast.Load()),
        ],
        keywords=[],
        starargs=None,
        kwargs=None,
    )
    result = StarredUnpackingTransformer().visit(node)
    assert isinstance(result, ast.Call)
    assert result.func is dummy_node
    assert isinstance(result.args[0], ast.Starred)
    assert isinstance(result.args[0].value, ast.BinOp)



# Generated at 2022-06-14 02:25:07.469713
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .base import BaseNodeTransformer

    from typed_ast import ast3 as ast

    tree = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer(tree)
    assert transformer._has_starred([ast.Starred(ast.Name("a"), ast.Load()), ast.Name("b", ast.Load())])
    assert transformer._has_starred([ast.Name("b", ast.Load())]) is False
    assert transformer._has_starred([ast.Starred(ast.Name("a"), ast.Load())])

# Generated at 2022-06-14 02:25:15.012991
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Test if `StarredUnpackingTransformer` conversion of list is equal to target."""
    node = ast.parse('[2, *range(10), 1]')
    expected_node = ast.parse('[2] + list(range(10)) + [1]')
    assert_equal_graph(starred_unpacking(node), expected_node)


# Generated at 2022-06-14 02:25:23.120411
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '[2, *range(10), 1]'
    tree = ast.parse(source)

    xformer = StarredUnpackingTransformer()
    xformer.visit(tree)

    assert ast.dump(tree) == 'Module(body=[Expr(value=BinOp(left=List(elts=[Num(n=2)]), op=Add(), right=Call(func=Name(id=\'list\', ctx=Load()), args=[Call(func=Name(id=\'range\', ctx=Load()), args=[Num(n=10)], keywords=[])], keywords=[])))])'



# Generated at 2022-06-14 02:25:43.850651
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tr = StarredUnpackingTransformer()

    name = ast.Name(id='print')
    args = [ast.Name(id='foo'), ast.Starred(value=ast.Name(id='bar'))]
    call = ast.Call(func=name, args=args, keywords=[])
    res = tr.visit(call)
    assert ast.dump(call) == ast.dump(res)

    name = ast.Name(id='print')
    args = [ast.Name(id='foo'),
            ast.Starred(value=ast.Name(id='bar')),
            ast.Starred(value=ast.Name(id='baz'))]
    call = ast.Call(func=name, args=args, keywords=[])
    res = tr.visit(call)

# Generated at 2022-06-14 02:25:48.253363
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    try:
        StarredUnpackingTransformer()
    except TypeError as e:
        assert 'StarredUnpackingTransformer() takes at most 1 argument (0 given)' == str(e)
    else:
        raise Exception('Incorrect argument number to constructor')


# Generated at 2022-06-14 02:25:54.592688
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import tree_unwrapper
    source = """
print(*range(1), *range(3))
    """
    expected = """
print(*(list(range(1)) + list(range(3))))
    """
    tree = tree_unwrapper.parse(source)
    tree = StarredUnpackingTransformer().visit(tree)
    assert tree_unwrapper.dumps(tree) == expected

# Generated at 2022-06-14 02:25:59.108861
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = '[2, *range(10), 1]'
    expected = '[2] + list(range(10)) + [1]'

    tree = ast.parse(src)
    StarredUnpackingTransformer().visit(tree)
    module = ast.Module(body=tree.body)
    actual_code = compile(module, filename='<string>', mode='exec')
    actual = str(actual_code)

    assert expected in actual


# Generated at 2022-06-14 02:26:10.357865
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected = ast.Call(func=ast.Name(id='print'),
                        args=[ast.Starred(value=ast.BinOp(
                            left=ast.Call(
                                func=ast.Name(id='list'),
                                args=[ast.Call(
                                    func=ast.Name(id='range'),
                                    args=[ast.Num(n=1)],
                                    keywords=[])],
                                keywords=[]), right=ast.Call(
                                    func=ast.Name(id='list'),
                                    args=[ast.Call(
                                        func=ast.Name(id='range'),
                                        args=[ast.Num(n=3)],
                                        keywords=[])],
                                    keywords=[]), op=ast.Add()))],
                        keywords=[])


# Generated at 2022-06-14 02:26:22.506638
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code_to_test = """
    baz(1, *(range(10)), 2, *[1], *(range(8, 10)) )
    """
    expected_code = """
    baz(*(list(range(1, 11)) + list(range(8, 10))))
    """
    utils = BaseNodeTransformer.Utils()
    module = utils.to_module(code_to_test, 'test_code_1')
    transformer = StarredUnpackingTransformer()
    module = transformer.visit(module)
    generated_code = utils.to_source(module)
    expected_module = utils.to_module(expected_code, 'test_code_2')
    expected_code_cleaned = utils.to_source(expected_module)
    assert expected_code_cleaned

# Generated at 2022-06-14 02:26:26.694335
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .helpers import get_ast
    transformer = StarredUnpackingTransformer()
    code = '[2, *range(10), 1]'
    ast_ = get_ast(code)
    transformer.visit(ast_)
    code = transformer.compile()
    assert code == '[2] + list(range(10)) + [1]'


# Generated at 2022-06-14 02:26:32.697340
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .testing import assert_code_equal

    code = '[2, *range(10), 1]'
    expected = '[2] + list(range(10)) + [1]'

    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)

    assert_code_equal(expected, tree)


# Generated at 2022-06-14 02:26:37.721347
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(2, *range(10), 1)").body[0]
    result = StarredUnpackingTransformer().visit(node)
    expected = ast.parse(
"""
print(*(list([2]) + list(range(10)) + list([1])))
""").body[0]
    assert result == expected


# Generated at 2022-06-14 02:26:45.660843
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer.target == (3, 4)
    assert StarredUnpackingTransformer._has_starred([]) == False
    assert StarredUnpackingTransformer._has_starred([ast.Starred(value=ast.Name(id='asd'))]) == True
    assert StarredUnpackingTransformer._has_starred([ast.Name(id='asd')]) == False
    assert StarredUnpackingTransformer._split_by_starred([]) == [[]]
    assert StarredUnpackingTransformer._split_by_starred([ast.Name(id='a'), ast.Name(id='b')]) == [[ast.Name(id='a'), ast.Name(id='b')]]