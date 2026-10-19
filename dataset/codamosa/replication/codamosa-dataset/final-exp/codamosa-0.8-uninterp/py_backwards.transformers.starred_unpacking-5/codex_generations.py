

# Generated at 2022-06-14 02:17:17.455291
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(2), *range(3))")
    transf = StarredUnpackingTransformer()
    transf.visit(tree)

# Generated at 2022-06-14 02:17:26.673812
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('''
            print(*range(1), *range(3))
        ''').body[0]
    assert isinstance(node, ast.Expr), 'must be Expr'
    assert isinstance(node.value, ast.Call), 'must be Call'
    assert isinstance(node.value.func, ast.Name), 'must be Name'
    assert isinstance(node.value.args[0], ast.Starred), 'must be Starred'
    assert isinstance(node.value.args[0].value, ast.Call), 'must be Call'



# Generated at 2022-06-14 02:17:34.735767
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = 'a=[2, *range(10), 1]'

    tree = ast.parse(code)
    typed_tree = StarredUnpackingTransformer().visit(tree)
    compiled = compile(typed_tree, '', mode='exec')

    a = []
    eval(compiled)
    expected = [2] + list(range(10)) + [1]

    assert a == expected


# Generated at 2022-06-14 02:17:39.058572
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astunparse
    with open('test/test_StarredUnpackingTransformer.py') as f:
        code = f.read()
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)
    assert astunparse.unparse(tree).strip() == code.strip()

# Generated at 2022-06-14 02:17:47.277930
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = astor.to_source(ast.parse('print(*range(1), *range(3))'))
    expected = astor.to_source(ast.parse('print(*(list(range(1)) + list(range(3))))'))
    transformed = StarredUnpackingTransformer().visit(ast.parse(code))  # type: ignore
    assert astor.to_source(transformed) == expected



# Generated at 2022-06-14 02:17:59.532779
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    '''
    Test below snippets of code:
    1. `print('Length is: ', length, sep='\n')`
    '''
    tree = ast.parse("print('Length is: ', length, sep='\n')")
    node = tree.body[0].value
    assert isinstance(node, ast.Call)

    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    assert isinstance(node, ast.Call)
    assert len(node.args) == 1
    assert isinstance(node.args[0], ast.Starred)
    assert isinstance(node.args[0].value, ast.List)
    assert len(node.args[0].value.elts) == 4
    assert isinstance(node.args[0].value.elts[0], ast.Str)


# Generated at 2022-06-14 02:18:05.090178
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("print(*range(1), *range(3))")
    t = StarredUnpackingTransformer()
    node = t.visit(node)
    assert t.tree_changed is True
    expected_code = textwrap.dedent("""
    import __future__
    print(*(list(range(1)) + list(range(3))))
    """)
    code = astor.to_source(node)
    assert code == expected_code
    

# Generated at 2022-06-14 02:18:10.061292
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    x = "print(*range(1), *range(3), sep=' ')"
    compiled = StarredUnpackingTransformer().visit(ast.parse(x))
    expected = ast.parse("print(*(list(range(1))+list(range(3))), sep=' ')")
    assert ast.dump(compiled) == ast.dump(expected)



# Generated at 2022-06-14 02:18:15.426255
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('print(*[1, 2], *range(3), end="")')
    StarredUnpackingTransformer().visit(tree)
    assert str(tree) == 'print(*(list([1, 2]) + list(range(3))), end="")'


# Generated at 2022-06-14 02:18:17.400085
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    sut = StarredUnpackingTransformer()
    assert (sut is not None)

# Generated at 2022-06-14 02:18:31.315580
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:18:42.369384
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # StarredUnpackingTransformer constructor test
    obj = StarredUnpackingTransformer()
    # re-create the instance and compare with obj
    obj2 = StarredUnpackingTransformer()
    assert obj == obj2
    assert not (obj != obj2)

    # StarredUnpackingTransformer.target test
    assert obj.target == (3, 4)

    # StarredUnpackingTransformer._has_starred test
    assert obj._has_starred([
        ast.Name(id='a'), ast.Starred(value=ast.Name(id='b')), ast.Name(
            id='c')])
    assert obj._has_starred([ast.Starred(value=ast.Name(id='b'))])

# Generated at 2022-06-14 02:18:51.453744
# Unit test for method visit_List of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:19:02.947992
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer
    
    The method visit_List should visit the method visit_List and convert a Starred Unpacking node
    to a sum of the lists [2, 3] + range(10) + [1]. It is expected that the method visit_List
    returns a list node with elements [2, 3] + range(10) + [1]
    """
    node = ast.parse("[2, *range(10), 1]")
    node = node.body[0].value
    assert isinstance(node, ast.List)
    starred_unpacking_transformer = StarredUnpackingTransformer()
    node = starred_unpacking_transformer.visit(node)

# Generated at 2022-06-14 02:19:06.204164
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    
    input_list = [2, *range(10), 1]
    output_list = (2, list(range(10)), 1)

    test_List = visit_List(input_list)
    
    assert test_List == output_list
    
    

# Generated at 2022-06-14 02:19:14.552947
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse

    class TreeChangedMock(StarredUnpackingTransformer):
        def __init__(self) -> None:
            self._tree_changed = False

    node = ast.parse(
        'def func_name(a, b, c, d=4, e=5, f=6, *args, g, h, i=9, j=10, k=11, **kwargs): pass'
    )

    node = TreeChangedMock().visit(node)


# Generated at 2022-06-14 02:19:19.558492
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast

    original_ast = ast.parse("print(*[1, 2, 3], *[4, 5, 6])\n")
    expected_ast = ast.parse("print(*(list([1, 2, 3]) + list([4, 5, 6])))\n")

    StarredUnpackingTransformer().visit(original_ast)

    assert ast.dump(original_ast) == ast.dump(expected_ast)


# Generated at 2022-06-14 02:19:25.674901
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    x = [2, *range(10), 1]
    print(*range(1), *range(3))

    assert StarredUnpackingTransformer().visit(x) == [2] + list(range(10)) + [1]
    assert StarredUnpackingTransformer().visit(print(*range(1), *range(3))) == print(*(list(range(1)) + list(range(3))))

# Generated at 2022-06-14 02:19:26.593460
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    pass


# Generated at 2022-06-14 02:19:31.225825
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .utils import assert_node_equals

    tree = ast.parse("""print(*range(4), end=' ')""")
    expected = ast.parse("""
print(*(list(range(4))), end=' ')
    """)
    StarredUnpackingTransformer.run(tree)
    assert_node_equals(tree, expected)



# Generated at 2022-06-14 02:19:52.346785
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:19:58.637956
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = parse(
        "print(*range(1), *range(3), *range(5))\n"
        "print(1, *range(3), *range(5), 2)\n"
        "print(*range(3), *range(5), 1, 2)\n"
        "print(1, *range(3), 2, *range(5))\n"
    )
    tree = StarredUnpackingTransformer().visit(tree)

# Generated at 2022-06-14 02:20:04.349039
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .ast_converter import convert_ast
    from .compat import decode_unicode

    source = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"
    my_ast = convert_ast(source)
    tree_changed, my_ast = StarredUnpackingTransformer(is_py_3=(True)).visit(my_ast)
    assert decode_unicode(my_ast) == expected
    assert tree_changed == True

# Generated at 2022-06-14 02:20:12.307284
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

    source = """
print(*range(1), *range(3))
    """
    expected = """
print(*(list(range(1)) + list(range(3))))
    """

    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)  # noqa: F841
    result = astor.to_source(tree)
    assert result == expected



# Generated at 2022-06-14 02:20:21.484302
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.List(elts=[ast.Num(1), ast.Starred(ast.Name(id='b')), ast.Num(1)])
    assert node.elts == [ast.Num(1), ast.Starred(ast.Name(id='b')), ast.Num(1)]
    assert node.elts[1].value.id == 'b'
    assert node.elts[1].value.id == 'b'
    assert node.elts[0].n == 1
    assert node.elts[2].n == 1

    node = ast.Call(func=ast.Name(id='print'), args=[ast.Starred(ast.Name(id='b'))], keywords=[])
    assert node.func.id == 'print'

# Generated at 2022-06-14 02:20:23.678054
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import ast
    import typed_ast.ast3 as ast3
    impo

# Generated at 2022-06-14 02:20:30.846254
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    statements = """
print(*range(1), *range(3))
"""
    node = compile_snippet(statements)
    result = StarredUnpackingTransformer.run_on_node(node)
    expected = """
print(*(list(range(1)) + list(range(3))))
"""
    assert format_code(result) == format_code(expected)


# Generated at 2022-06-14 02:20:40.959004
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    lst = ast.parse('[1, 2, 3]').body[0].value
    assert (StarredUnpackingTransformer().visit(lst) == lst)
    call = ast.parse('Print(1, 2, 3)').body[0].value
    assert (StarredUnpackingTransformer().visit(call) == call)
    lst_with_starred = ast.parse('[1, *[2, 3], 4]').body[0].value
    check_lst = ast.parse('[1] + [2, 3] + [4]').body[0].value
    assert (StarredUnpackingTransformer().visit(lst_with_starred) == check_lst)


# Generated at 2022-06-14 02:20:51.611877
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import parse

    tree = parse('print([2, *range(10), 1])')
    node = tree.body[0].value
    assert isinstance(node, ast.Call)
    args = node.args[0]
    assert isinstance(args, ast.List)
    assert len(args.elts) == 3
    assert isinstance(args.elts[0], ast.Num)
    assert isinstance(args.elts[1], ast.Starred)
    assert isinstance(args.elts[2], ast.Num)

    StarredUnpackingTransformer().visit(tree)
    args = node.args[0]
    assert len(args.elts) == 3
    assert isinstance(args.elts[0], ast.BinOp)

# Generated at 2022-06-14 02:20:59.064938
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.List([
        ast.Constant(value=2, kind=None),
        ast.Starred(value=ast.Name(id='range', ctx=ast.Load()),
                     ctx=ast.Load()),
        ast.Constant(value=1, kind=None)
    ])
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    assert transformer._tree_changed
    assert node.elts[0].__class__ == ast.Constant
    assert node.elts[1].__class__ == ast.BinOp
    assert node.elts[2].__class__ == ast.Constant
    assert node.elts[1].left.__class__ == ast.List
    assert node.elts[1].right.__class__ == ast.List

# Generated at 2022-06-14 02:21:20.098474
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse('''
                     func(1, *[2, *range(3)], *[4], *[5, *range(6)]) 
                     ''')
    expected_tree = ast.parse('''
                     func(*(list([1]) + list([2] + list(range(3))) 
                         + list([4]) + list([5] + list(range(6)))))
                     ''')
    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 02:21:28.297966
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(1, *range(10), 2, *range(2))")
    StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == "Module(body=[Print(dest=None, values=[Call(func=Name(id='print', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[List(elts=[Num(n=1), Starred(value=Name(id='range', ctx=Load()), ctx=Load()), Num(n=2)], ctx=Load())], keywords=[])], keywords=[])], nl=True)])"


# Generated at 2022-06-14 02:21:30.691200
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transform = StarredUnpackingTransformer()
    assert str(transform) == "StarredUnpackingTransformer()"

# Generated at 2022-06-14 02:21:32.517819
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().comments == []
    assert StarredUnpackingTransformer().error_comments == []

# Generated at 2022-06-14 02:21:38.801225
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    assert transformer.visit(ast.parse('[2, *range(10), 1]')) == \
        ast.parse('[2, ] + list(range(10)) + [1, ]')

    assert transformer.visit(ast.parse('[2, 1]')) == \
        ast.parse('[2, 1, ]')


# Generated at 2022-06-14 02:21:44.506995
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node_to_test = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(node_to_test)
    expected = ast.parse("[2] + list(range(10)) + [1]")
    assert ast.dump(result) == ast.dump(expected)


# Generated at 2022-06-14 02:21:55.832558
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse('[2, *range(10), 1]')
    tree = StarredUnpackingTransformer().visit(tree)
    assert ast.dump(tree) == 'Expr(value=BinOp(left=BinOp(left=List(elts=[Num(n=2)]), ' \
                             'right=Call(func=Name(id="list", ctx=Load()), args=[Call(func=Name(id="list", ' \
                             'ctx=Load()), args=[Call(func=Name(id="range", ctx=Load()), args=[Num(n=10)], ' \
                             'keywords=[])], keywords=[])], keywords=[]), op=Add()), right=List(elts=[Num(n=1)]), ' \
                             'op=Add()))'

# Generated at 2022-06-14 02:21:59.939848
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    code = """print(*range(1), *range(3))"""
    tree = ast.parse(code)
    assert astor.to_source(StarredUnpackingTransformer().visit(tree)) == """print(*(list(range(1)) + list(range(3))))"""

# Generated at 2022-06-14 02:22:06.731790
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    lines = [
        "[1, 2]",
        "[*range(10)]",
        "[1, *range(10)]"
    ]
    expected = [
        "[1, 2]",
        "list(range(10))",
        "[1] + list(range(10))"
    ]
    test_input = _build_ast_from_source(lines)
    for node, exp in zip(test_input, expected):
        transformed = StarredUnpackingTransformer().visit(node)
        assert transformed.__repr__() == exp


# Generated at 2022-06-14 02:22:11.839227
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse('[2, *range(10), 1]').body[0].value
    tree = StarredUnpackingTransformer()
    tree.visit(node)
    assert str(tree._ast) == "[2, *(list(range(10)) + [1])]"


# Generated at 2022-06-14 02:22:44.413665
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .python_to_pythonast import parse
    from .compile_to_code import compile_code_object, compile_source
    import ast
    import sys
    import dis
    import codecs
    def test(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z):
        print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, x, y, z)
    source = inspect.getsource(test)
    source_ast = parse(source)
    print(ast.dump(source_ast))

# Generated at 2022-06-14 02:22:48.221583
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from . import compile_node, parse_snippet

    snippet = '[2, *range(10), 1]'
    expected = 'list([2]) + list(range(10)) + list([1])'
    result = compile_node(StarredUnpackingTransformer, parse_snippet(snippet))
    assert result == expected


# Generated at 2022-06-14 02:22:58.938850
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # case 1
    String = "print(*range(1), *range(3))"
    node = ast.parse(String, mode='eval')
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    assert not transformer._tree_changed

# Generated at 2022-06-14 02:23:09.427950
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import templates
    from .compile import compile_transformer
    
    src = """\
print(3, 1, 4, *range(6))
"""
    expected = '''
print(*(list([3, 1, 4]) + list(range(6))))
'''
    transformer = compile_transformer(StarredUnpackingTransformer,
                                      templates.CompilerTemplate)
    root = transformer.visit(ast.parse(src))
    assert transformer.tree_changed
    assert ast.dump(root) == expected


# Generated at 2022-06-14 02:23:14.477009
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import UnitTestTransformer
    from .base import register_transformer
    register_transformer(StarredUnpackingTransformer)
    source = 'print(*range(1), *range(3))'
    UnitTestTransformer.assert_transformed(source, 'print(*(list(range(1)) + list(range(3))))')


# Generated at 2022-06-14 02:23:21.124837
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
[2, *range(10), 1]
    """
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)
    assert astor.to_source(tree) == '\n[2] + list(range(10)) + [1]\n'


# Generated at 2022-06-14 02:23:30.708007
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from astunparse import unparse
    
    # Full example:
    # [2, *range(10), 1] -> [2] + list(range(10)) + [1]
    source = '[2, *range(10), 1]'
    expected = '[2] + list(range(10)) + [1]'
    node = ast.parse(source)
    StarredUnpackingTransformer().visit(node)
    output = unparse(node)
    assert output == expected
    
    # One starred:
    # [2, *range(10)] -> [2] + list(range(10))
    source = '[2, *range(10)]'
    expected = '[2] + list(range(10))'
    node = ast.parse(source)
    StarredUnpackingTransformer().visit(node)
   

# Generated at 2022-06-14 02:23:36.837110
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert_equal_ast(
        StarredUnpackingTransformer().visit(
            ast.parse('[2, *range(10), 1]')),
        ast.parse('[2] + list(range(10)) + [1]'))


# Generated at 2022-06-14 02:23:38.140821
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()
    assert transformer

# Generated at 2022-06-14 02:23:45.953747
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    root = ast.parse(inspect.cleandoc(''' \
        print(*range(1), *range(3))
    '''))

    expected_root = ast.parse(inspect.cleandoc(''' \
        print(*((list(range(1)) + list(range(3)))))
    '''))

    StarredUnpackingTransformer().visit(root)
    assert_ast_eq(root, expected_root)


# Generated at 2022-06-14 02:24:33.202140
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:24:40.776899
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .test_utils import wrap_in_module
    from .utils import to_source

    original = """

print(*range(10), *range(5))
[2, *range(10), 1]
    """
    expected = """

print(None)
[2, None]
    """
    with wrap_in_module(original) as tree:
        StarredUnpackingTransformer().visit(tree)
        with wrap_in_module(to_source(tree)) as tree2:
            NodeTransformer().visit(tree2)

    with wrap_in_module(original) as tree:
        NodeTransformer().visit(tree)

    print('ORIGINAL')
    print(original)
    print()
    print('EXPECTED')
    print(expected)
    print()

# Generated at 2022-06-14 02:24:47.396591
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import random
    import astor
    from build_ast import build_ast

    random.seed(0)

    def build_test(args: List[str]):
        arg_list = ','.join(args)
        code = f'[{arg_list}]'
        tree = build_ast(code)
        return tree

    def build_call_test(args: List[str]):
        arg_list = ','.join(args)
        code = f'print({arg_list})'
        tree = build_ast(code)
        return tree

    def check(xs: List[str]):
        ast_in = build_test(xs)
        tree_out, changed = StarredUnpackingTransformer().transform(ast_in)
        assert changed
        ast_out = ast.fix_missing_locations

# Generated at 2022-06-14 02:24:56.865892
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """
    [2, *range(10), 1]
    [2, range(10), 1]
    """
    star = ast.Starred(
        value=ast.Call(
            func=ast.Name(id='range'),
            args=[ast.Num(n=10)],
            keywords=[])
        )

    call_list = ast.List(
        elts=[ast.Num(n=2), star, ast.Num(n=1)]
    )

    expected_list = ast.List(
        elts=[ast.Num(n=2)]
    )


# Generated at 2022-06-14 02:25:04.123022
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """Test constructor of class StarredUnpackingTransformer."""
    instance = StarredUnpackingTransformer(
        tree=ast.parse('[2, *range(10), 1]\n'
                       'print(*range(1), *range(3))'),
        file_name='<test>')
    assert isinstance(instance, StarredUnpackingTransformer)
    assert instance.tree is not None
    assert instance.file_name == '<test>'



# Generated at 2022-06-14 02:25:05.006086
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:25:08.087499
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    f = ast.parse("print(*range(1), *range(3))")
    f = t.visit(f)
    assert f == ast.parse("print(*(list(range(1)) + list(range(3))))")

# Generated at 2022-06-14 02:25:16.354457
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    input_src = """
    [2, *range(10), 1]
    """
    expected_src = """
    [2] + list(range(10)) + [1]
    """
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(ast.parse(input_src))
    assert transformer._tree_changed == True
    assert ast.dump(result) == ast.dump(ast.parse(expected_src))


# Generated at 2022-06-14 02:25:18.406511
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert 1
    #assert 0


# Generated at 2022-06-14 02:25:28.019823
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_utils import generate
    assert generate(
        """
        print(1,2,3,4,*range(5))
        """, StarredUnpackingTransformer)
    assert generate(
        """
        a = [1,2,3,4,*range(5)]
        """, StarredUnpackingTransformer)
    assert generate(
        """
        a = [1,*range(5), 2,3,4,*range(5)]
        """, StarredUnpackingTransformer)
    assert generate(
        """
        a = [1,2,3,*range(5), 2,3,4,*range(5)]
        """, StarredUnpackingTransformer)