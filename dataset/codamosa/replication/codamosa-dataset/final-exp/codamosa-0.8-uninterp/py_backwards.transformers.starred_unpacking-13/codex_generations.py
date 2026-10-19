

# Generated at 2022-06-14 02:17:06.386678
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:17:10.260705
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert ast.parse('print(*range(10))').body[0] == StarredUnpackingTransformer().visit(ast.parse('print(*range(10))').body[0])


# Generated at 2022-06-14 02:17:15.207669
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = 'C([2, *range(10), 1])'
    expected_code = 'C([2] + list(range(10)) + [1])'
    node = ast.parse(code)
    StarredUnpackingTransformer(node).visit(node)
    assert astor.to_source(node) == expected_code



# Generated at 2022-06-14 02:17:28.705873
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse("f(1, *a, 2, *b)")
    tr = StarredUnpackingTransformer()
    tr.visit(node)

# Generated at 2022-06-14 02:17:33.926076
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
        [2, *range(10), 1]
    """
    expected = """
        [2] + list(range(10)) + [1]
    """

    result_tree = parse(code)
    result_tree_compiled = StarredUnpackingTransformer().visit(result_tree)
    result_code = codegen.to_source(result_tree_compiled)

    assert result_code.strip() == expected.strip()


# Generated at 2022-06-14 02:17:43.478995
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(1), *range(3))", filename='<ast>', mode='eval')
    transform = StarredUnpackingTransformer()
    node = transform.visit(tree)
    # f = open("../test/StarredUnpackingTransformer_visit_Call.txt", 'w')
    # print(ast.dump(node, include_attributes=True), file=f)
    # f.close()

# Generated at 2022-06-14 02:17:52.701602
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .mock_nodes import mock_list, mock_starred
    from .mock_nodes import mock_call, mock_binop
    from .mock_nodes import mock_tuple


# Generated at 2022-06-14 02:17:59.780596
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from aioreflection.util import ast_dump
    from .test_compat import assert_ast_equal

    code = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'
    source = ast.parse(code)
    compiled = StarredUnpackingTransformer()(source)
    assert_ast_equal(expected, ast_dump(compiled))


# Generated at 2022-06-14 02:18:07.118525
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    to_be_compiled = ast.parse("print(*range(1), [2, *range(10), 1])")
    expected = ast.parse("print(*((list(range(1)) + [2]) + list(range(10)) + [1]))")
    StarredUnpackingTransformer().visit(to_be_compiled)
    assert ast.dump(to_be_compiled) == ast.dump(expected)


# Generated at 2022-06-14 02:18:13.761422
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    module = ast.parse("""
result = print(*range(1), *range(3))
""")

    expected_module = ast.parse("""
result = print(*(list(range(1)) + list(range(3))))
""")

    StarredUnpackingTransformer().visit(module)
    assert ast.dump(module) == ast.dump(expected_module)


# Generated at 2022-06-14 02:18:25.571186
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='print'),
                    args=[ast.Starred(value=ast.Name(id='x'), ctx=ast.Load()),
                          ast.Starred(value=ast.Name(id='y'), ctx=ast.Load()),
                          ast.Name(id='z')], 
                    keywords=[])
    

# Generated at 2022-06-14 02:18:36.638523
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from .base import BaseNodeTransformer
    from .starred_unpacking import StarredUnpackingTransformer
    from .anamorphism import AnamorphismCompiler
    from .monomorphism import MonomorphismCompiler
    from .apply import ApplyCompiler
    BaseNodeTransformer.reset_all_counters()
    StarredUnpackingTransformer.reset_counter()
    AnamorphismCompiler.reset_counter()
    MonomorphismCompiler.reset_counter()
    ApplyCompiler.reset_counter()
    ast_module = ast.parse("""
    foo(*args)
    print(*args)
    """)
    result = StarredUnpackingTransformer().visit(ast_module)

# Generated at 2022-06-14 02:18:47.772596
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import do_test
    from .test_starred_unpacking import input_Call

    tree = ast.parse(input_Call, 'exec')
    star_unpacking = StarredUnpackingTransformer()

    result = star_unpacking.visit(tree)


# Generated at 2022-06-14 02:18:54.509638
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    obj = """print(*range(1), *range(3))"""
    expected = """print(*(list(range(1)) + list(range(3))))"""

    node = ast.parse(obj)
    node = StarredUnpackingTransformer().visit(node)
    node = ast.fix_missing_locations(node)
    result = compile(node, '', 'exec')
    expected = compile(expected, '', 'exec')
    assert result == expected

# Generated at 2022-06-14 02:19:02.101579
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    print(5, 6, 7, 8, sep='.')
    print(*[5, 6, 7, 8], sep='.')
    print(sep='.', *[5, 6, 7, 8])
    print(*[5, 6, 7], sep='.', *[8])
    print(*[5, 6, 7], sep='.', *[8, 9, 10])
    print(*[5, 6, 7], *[8, 9, 10], sep='.')


# Generated at 2022-06-14 02:19:07.871691
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = 'print(1, *range(2), 3, *range(1))'
    expected = 'print(*(list([1]) + list(range(2)) + list([3]) + list(range(1))))'

    t = StarredUnpackingTransformer()
    tree = ast.parse(code)
    new_tree = t.visit(tree)

    generated_code = compile(new_tree, '<test>', 'exec')
    exec(generated_code, {})

    assert(expected in str(generated_code))

# Generated at 2022-06-14 02:19:18.907043
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():

    # input
    input_node = ast.Call(
        func=ast.Name(id='print'),
        args=[
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=1)],
                    keywords=[])),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range'),
                    args=[ast.Num(n=3)],
                    keywords=[]))],
        keywords=[])

    # expected

# Generated at 2022-06-14 02:19:31.535009
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()

    test_cases = (
        (
            'print(2, 3)',
            'print(2, 3)'
        ),
        (
            'print(1, *range(3))',
            'print(*([1] + list(range(3))))'
        ),
        (
            'print(*range(1), *range(2))',
            'print(*(list(range(1)) + list(range(2))))'
        ),
        (
            'print(*range(5), 2, 3)',
            'print(*(list(range(5)) + [2, 3]))'
        )
    )

    for program, expected_result in test_cases:
        result = transformer.visit(ast.parse(program))

# Generated at 2022-06-14 02:19:36.431355
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """print(*range(1), *range(3))"""
    expected = """print(*(list(range(1)) + list(range(3))))"""

    t = StarredUnpackingTransformer()
    res = t.visit(ast.parse(source))
    assert ast.dump(res) == expected


# Generated at 2022-06-14 02:19:46.692995
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    tree1 = ast.parse('print(*range(10))')
    tree2 = ast.parse('print(1, *range(10), 3)')
    tree3 = ast.parse('print(1, *range(10), *range(20), 3)')
    tree4 = ast.parse('print(1, 2, 3, 4)')

    StarredUnpackingTransformer().visit(tree1)
    StarredUnpackingTransformer().visit(tree2)
    StarredUnpackingTransformer().visit(tree3)
    StarredUnpackingTransformer().visit(tree4)


# Generated at 2022-06-14 02:19:57.095878
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = "print(*range(1), *range(3))"
    expected = """\
if __name__ == '__main__':
    print(*(list(range(1)) + list(range(3))))"""

    node = ast.parse(source)
    t = StarredUnpackingTransformer()
    result = t.visit(node)
    assert expected == astunparse.unparse(result)

# Generated at 2022-06-14 02:20:06.510945
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tests = [
        ('print(*[1], *[2, 3])',
         'print(*(list([1]) + list([2, 3])))'),
        ('print(*[1], *{2, 3})',
         'print(*(list([1]) + list({2, 3})))'),
        ('print(*[1, *{2, 3}])',
         'print(*(list([1]) + list(list({2, 3}))))'),
        ('print(*[], *[])',
         'print(*(list([]) + list([])))'),
    ]

    for code, output in tests:
        assert compile_stripped_tree(
            code, mode='exec',
            transformers=[StarredUnpackingTransformer]) == output

# Generated at 2022-06-14 02:20:19.404752
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .base import compile_function
    from .base import eval_function

    # test passing *vargs
    fn_src = 'def fn(a, *vargs): return a, vargs'
    fn = compile_function(fn_src, StarredUnpackingTransformer)
    assert eval_function(fn) == 1, 'test for only *vargs failed'

    # test passing args after *vargs
    fn_src = 'def fn(a, *vargs, b, c): return a, vargs, b, c'
    fn = compile_function(fn_src, StarredUnpackingTransformer)
    assert eval_function(fn) == 1, 'test for only *vargs failed'

    # test passing args before and after *vargs

# Generated at 2022-06-14 02:20:23.713882
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Given
    source = "print(*range(1), *range(3))"
    expected = "print(*(list(range(1)) + list(range(3))))"

    # When
    actual = compile(source, '<string>', 'exec', optimize=0).co_code
    expected = compile(expected, '<string>', 'exec').co_code

    # Then
    assert actual == expected


# Generated at 2022-06-14 02:20:29.375953
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected = """print(*(list(range(1)) + list(range(3))))"""
    actual = StarredUnpackingTransformer().visit(
        ast.parse("""print(*range(1), *range(3))"""))
    assert expected == astor.to_source(actual)


# Generated at 2022-06-14 02:20:34.301565
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected = ast.parse('print(*(list(range(1)) + list(range(3))))')
    node = ast.parse('print(*range(1), *range(3))')
    actual = StarredUnpackingTransformer().visit(node)
    assert actual == expected



# Generated at 2022-06-14 02:20:46.024857
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Tests the method visit_Call of class StarredUnpackingTransformer."""
    from astunparse import unparse
    from textwrap import dedent
    from .util import roundtrip

    expr_source = dedent("""\
    f(*args)
    f(1, *args, 2)
    f(3, *args, *args, 4)
    """)
    expected_ast = list(ast.parse(dedent("""\
    f(*args)
    f(*(list(args) + [1, *args, 2]))
    f(*(list(args) + list(args) + [3, *args, *args, 4]))
    """)))
    expected_source = unparse(expected_ast).split('\n')
    actual_source = []

# Generated at 2022-06-14 02:20:54.945350
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    data = ast.parse('''
print([1, 2, 3, 4], [5, 6, 7, 8])

print(*[1, 2], *[3, 4])
    ''')
    StarredUnpackingTransformer().visit(data)
    new_data = ast.parse('''\
print([1, 2, 3, 4], [5, 6, 7, 8])

print(*(list([1, 2]) + list([3, 4])))
    ''')
    assert ast_equal(new_data, data)


# Generated at 2022-06-14 02:21:08.454318
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    node = ast.Call(func=ast.Name(id='f'),
                    args=[ast.Starred(value=ast.Name(id='a')),
                          ast.Num(n=1)],
                    keywords=[])
    expected_node = ast.Call(func=ast.Name(id='f'),
                             args=[ast.Starred(value=
                                        ast.BinOp(left=ast.List(elts=[ast.Name(id='a')]),
                                                  right=ast.List(elts=[ast.Num(n=1)]),
                                                  op=ast.Add()))],
                             keywords=[])
    transformed = t.visit(node)
    assert ast.dump(transformed) == ast.dump(expected_node)

# Unit test

# Generated at 2022-06-14 02:21:17.389791
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
print(1, 2, *range(3), *range(4))
"""
    tree = ast.parse(source)
    expected_source = """
print(*(list([1, 2]) + list(range(3)) + list(range(4))))
"""
    expected_tree = ast.parse(expected_source)
    result = StarredUnpackingTransformer().visit(tree)
    assert ast.dump(result, include_attributes=True) == ast.dump(expected_tree, include_attributes=True)


# Generated at 2022-06-14 02:21:36.002104
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    @transformer
    def test_transformer(node):
        return StarredUnpackingTransformer(node).visit_Call(node)

    # Test case #1 from docstring
    src_code = "print(*range(1), *range(3))"
    expected_transformed_code = "print(*(list(range(1)) + list(range(3))))"
    assert test_transformer(src_code) == expected_transformed_code

    # Test case #2
    src_code = "print(*range(1), 2, *range(3))"
    expected_transformed_code = "print(*(list(range(1)) + [2] + list(range(3))))"
    assert test_transformer(src_code) == expected_transformed_code

    # Test case #3

# Generated at 2022-06-14 02:21:45.296336
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    la = ast.List(elts=[ast.Num(n=2), ast.Name(id='b'), ast.Num(n=1)])
    lb = ast.Call(func=ast.Name(id='list'), args=[ast.Name(id='c')], keywords=[])
    node0 = ast.Call(func=ast.Name(id='foo'), args=[la], keywords=[])
    node1 = ast.Call(func=ast.Name(id='foo'), args=[la, lb], keywords=[])
    node2 = ast.Call(
        func=ast.Name(id='foo'),
        args=[la, lb, ast.Starred(value=la), lb],
        keywords=[])

# Generated at 2022-06-14 02:21:56.626697
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    msg = "StarredUnpackingTransformer visit_Call: "
    filename = "example.py"
    
    code = "print(*range(1))"
    expected = "print(*(list(range(1))))"
    tree = ast.parse(code, filename=filename)
    StarredUnpackingTransformer().visit(tree)
    actual = astor.to_source(tree)
    assert expected == actual, msg + "failed for args"
    
    code = "print(1, *range(2))"
    expected = "print(1, *(list(range(2))))"
    tree = ast.parse(code, filename=filename)
    StarredUnpackingTransformer().visit(tree)
    actual = astor.to_source(tree)
    assert expected == actual, msg + "failed for args"


# Generated at 2022-06-14 02:21:59.344739
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import parse
    node = parse('foo(*args)')
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(node)
    print(result)

# Generated at 2022-06-14 02:22:10.024955
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

    class TestTransformer:
        def __init__(self):
            self._method = None
            self._before = None

        def run(self, node):
            method = self._get_method(node)
            if method is None:
                return None
            return method(node)

        def _get_method(self, node):
            if self._method is None:
                return None

            if not isinstance(node, self._before):
                return None

            return getattr(self, self._method)

        def set_method(self, method, before=None):
            self._method = method
            self._before = before or ast.AST

    transformer = TestTransformer()
    transformer.set_method('visit_Call')

# Generated at 2022-06-14 02:22:16.034552
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import typed_astunparse
    code = """a(b, *c, d, *e, f)"""
    expected_code = """a(*((list(c) + list(e))))"""
    node = typed_astunparse.ast_parse(code)
    node = StarredUnpackingTransformer().visit(node)
    assert typed_astunparse.unparse(node) == expected_code


# Generated at 2022-06-14 02:22:20.527174
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast, parse

    source = 'print(*range(1), *range(3))'
    expected = 'list.__add__(list(range(1)), list(range(3)))\n'

    tree = parse(source)
    transformer = StarredUnpackingTransformer()
    transformed = transformer.visit(tree)
    assert expected == compile(transformed, filename='<ast>', mode='eval')



# Generated at 2022-06-14 02:22:24.149160
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = ast.parse("print(*range(1), *range(3))")
    expected = ast.parse("print(*(list(range(1)) + list(range(3))))")
    actual = StarredUnpackingTransformer()(source)
    assert expected == actual


# Generated at 2022-06-14 02:22:33.241396
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
	# Takes a call node and determines if it's arguments have unpacking operators, if not then it just returns the ast node
	# otherwise it will replace the arguments with a sum of lists
	class _MockStarredUnpackingTransformer(StarredUnpackingTransformer):
		def __init__(self):
			super().__init__()
			self._tree_changed = False

	# Test when call node has a starred argument
	node = ast.parse("os.path.join('foo', 'bar', *args)")

	transformer = _MockStarredUnpackingTransformer()
	transformer.visit(node)


# Generated at 2022-06-14 02:22:37.531401
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Test case for method visit_Call"""
    source = "print(*range(1), *range(3))"
    expected = "print(*(list(range(1)) + list(range(3))))\n"
    check_transformation(StarredUnpackingTransformer, source, expected)

