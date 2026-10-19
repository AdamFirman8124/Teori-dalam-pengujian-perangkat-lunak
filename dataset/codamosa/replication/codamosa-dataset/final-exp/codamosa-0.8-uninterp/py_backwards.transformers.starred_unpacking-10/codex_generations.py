

# Generated at 2022-06-14 02:17:12.422684
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    source_code = astor.to_source(ast.parse("[2, *range(10), 1]"))
    expected_code = astor.to_source(ast.parse("[2] + list(range(10)) + [1]"))

    tr = StarredUnpackingTransformer("some_name")
    tr.visit(ast.parse(source_code))
    assert tr._tree_changed
    new_code = astor.to_source(tr.result)
    assert expected_code == new_code



# Generated at 2022-06-14 02:17:21.784872
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer()

    s = ast.parse("[2, *range(10), 1]")
    s = trans.visit(s)
    assert str(s) == "[2] + list(range(0, 10)) + [1]"

    s = ast.parse("print(*range(1), *range(3))")
    s = trans.visit(s)
    assert str(s) == "print(*(list(range(0, 1)) + list(range(0, 3))))"

# Generated at 2022-06-14 02:17:33.737460
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from typed_ast import ast3
    import typing

    class UnpackingTransformer(StarredUnpackingTransformer):
        target = ()

        def parse(self, source: typing.Union[str, typing.List[str]]) -> ast3.AST:
            return ast3.parse(source)

    trans = UnpackingTransformer()

# Generated at 2022-06-14 02:17:34.771638
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:17:44.054591
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import textwrap
    from ..tools import AssertASTEqual

    src = textwrap.dedent('''
        [2, *range(10), 1]
    ''')
    expected = textwrap.dedent('''
        [2] + list(range(10)) + [1]
    ''')
    tree = ast.parse(src)
    StarredUnpackingTransformer().visit(tree)
    AssertASTEqual(tree, expected)

    src = textwrap.dedent('''
        [2, *range(2, 10), *range(2, 3), 1]
    ''')
    expected = textwrap.dedent('''
        [2] + list(range(2, 10)) + list(range(2, 3)) + [1]
    ''')

# Generated at 2022-06-14 02:17:55.466247
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .unparse_dumper import UnparseDumper
    from .exceptions import TreeChangedError

    node = ast.parse("print(*range(1), **{'a': 2, 'b': 3})").body[0]
    assert UnparseDumper.to_string(node) == 'print(*range(1), **{\'a\': 2, \'b\': 3})'
    try:
        StarredUnpackingTransformer().visit(node)
    except TreeChangedError:
        pass
    else:
        raise AssertionError("TreeChangedError was not raised.")
    assert UnparseDumper.to_string(node) == 'print(*list(range(1)) + list([]), **{\'a\': 2, \'b\': 3})'

# Generated at 2022-06-14 02:18:01.704716
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    assert StarredUnpackingTransformer().visit(
        ast.parse('''[2, *range(10), 1]''').body[0]) == (
        ast.parse('''[2] + list(range(10)) + [1]''').body[0])

    assert StarredUnpackingTransformer().visit(
        ast.parse('''[2]''').body[0]) == (
        ast.parse('''[2]''').body[0])

    assert StarredUnpackingTransformer().visit(
        ast.parse('''[2, 1, 2]''').body[0]) == (
        ast.parse('''[2, 1, 2]''').body[0])


# Generated at 2022-06-14 02:18:10.672902
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    global ast_text
    global compiled_node
    ast_text = 'print(*range(1), *range(3))'
    compiled_node = compile(ast_text, '<ast>', 'exec', ast.PyCF_ONLY_AST)
    StarredUnpackingTransformer().visit(compiled_node)
    assert ast.dump(compiled_node) == "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Starred(value=BinOp(left=List(elts=[Num(n=1)], ctx=Load()), op=Add(), right=List(elts=[Num(n=2)], ctx=Load())))], keywords=[]))])"


# Generated at 2022-06-14 02:18:12.955122
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer().visit(
        ast.parse(
            'print(10, *range(10), 1)'
        )
    )

# Generated at 2022-06-14 02:18:23.423432
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import Compiler
    from .test_helpers import generate_python_str
    from .test_helpers import run_python_str
    from .test_helpers import unindent
    from .test_helpers import compare_with_native_ast
    
    
    class Compiler(Compiler):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            self._tree_changed = True
            
            body = node.body
            node.body = [StarredUnpackingTransformer().visit(node) for node in body]
    
    source = unindent("""
    def foo(a, b, c, d):
        print(a, b, c, d)
        
    foo(2, 3, 4, 5)
    """)
    compare_with_native_

# Generated at 2022-06-14 02:18:39.444961
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(1), *range(3))")

# Generated at 2022-06-14 02:18:46.437640
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # Simple case
    node = ast.parse('print(2, 3, *range(3))').body[0]
    expected = ast.parse('print(*(list(range(3)) + [2, 3]))').body[0]

    result = StarredUnpackingTransformer().visit(node)
    assert ast.dump(result) == ast.dump(expected)

    # Case with arguments, keywords and more starargs and kwargs
    node = ast.parse('print(a, *range(10), 4, *range(6), d=3, *range(12), x=3)').body[0]

# Generated at 2022-06-14 02:18:49.201052
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
    print(*range(1), *range(3))
    """

    expected = """
    print(*(list(range(1)) + list(range(3))))
    """

    tr = StarredUnpackingTransformer()
    result, = ast.parse(source).body
    expected, = ast.parse(expected).body
    tr.visit(result)
    assert ast.dump(result) == ast.dump(expected)


# Generated at 2022-06-14 02:18:56.452795
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """
    Tests constructor of class StarredUnpackingTransformer
    """

    unpack_starred_transformer = StarredUnpackingTransformer()
    assert unpack_starred_transformer.target == (3,4)
    assert unpack_starred_transformer.context == None
    assert unpack_starred_transformer.name == 'StarredUnpackingTransformer'
    assert unpack_starred_transformer.tree_changed == False


if __name__ == '__main__':
    test_StarredUnpackingTransformer()

# Generated at 2022-06-14 02:19:01.432484
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    st = ast.parse('[2, 3, *range(10), 1]')
    assert StarredUnpackingTransformer().visit(st).body[0].value.elts[0].left.left.elts == [ast.Num(n=2), ast.Num(n=3)]


# Generated at 2022-06-14 02:19:06.237606
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    input_ast_tree = ast.parse('[2, *range(10), 1]')
    output_ast_tree = ast.parse('[2] + list(range(10)) + [1]')
    star_unpacking = StarredUnpackingTransformer()
    star_unpacking.visit(input_ast_tree)
    assert input_ast_tree == output_ast_tree


# Generated at 2022-06-14 02:19:11.789689
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3
    from .ast_utils import tree_equal

    tree_equal(
        StarredUnpackingTransformer().visit(ast3.parse('f(*range(1), *range(2))')),
        ast3.parse('f(*(list(range(1)) + list(range(2))))')
    )

# Generated at 2022-06-14 02:19:19.205157
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.parse('print(*range(3))').body[0]
    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert isinstance(node.value.func, ast.Name)
    assert node.value.func.id == 'print'
    assert node.value.args[0].elts[0].args[0].n == 3

    StarredUnpackingTransformer().visit(node)
    assert node.value.args[0].value.elts[0].func.id == 'list'


# Generated at 2022-06-14 02:19:22.910960
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse

    s = """print(*range(1), *range(2), 3)"""
    node = ast.parse(s)
    node = StarredUnpackingTransformer().visit(node)
    s_new = unparse(node)

    print(s)
    print(s_new)
    assert s_new == """print(*(list(range(1)) + list(range(2)) + [3]))"""

# Generated at 2022-06-14 02:19:24.078619
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer(0)

# Generated at 2022-06-14 02:19:35.997769
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    """Test case for constructor."""
    StarredUnpackingTransformer()


# Generated at 2022-06-14 02:19:45.245814
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast

    input_list: List[ast.AST] = []
    input_list.append(ast.parse('range(1)', mode='eval'))

    input_list.append(ast.parse('print(range(1))', mode='exec'))

    input_list.append(ast.parse('print(*range(1))', mode='exec'))

    input_list.append(ast.parse('[1, *range(3)]', mode='eval'))

    input_list.append(ast.parse('print(*range(1), *range(3))', mode='exec'))

    output_list: List[ast.AST] = []
    output_list.append(ast.parse('list(range(1))', mode='eval'))


# Generated at 2022-06-14 02:19:56.266809
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    source = '[2, *range(10), 1]'
    source_ast = ast.parse(source)
    expected = "[2] + list(range(10)) + [1]"
    expected_ast = ast.parse(expected)

    transformer = StarredUnpackingTransformer()
    result_ast = transformer.visit(source_ast)

    assert isinstance(result_ast, ast.Module)
    assert len(result_ast.body) == 1
    assert isinstance(result_ast.body[0], ast.Expr)
    assert result_ast.body[0].value is not expected_ast.body[0].value
    assert ast.dump(result_ast.body[0].value) == ast.dump(expected_ast.body[0].value)
    assert transformer._tree_changed

# Generated at 2022-06-14 02:20:06.622149
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    xs = [ast.Num(1), ast.Starred(value=ast.List(elts=[ast.Num(2), ast.Num(3)])), ast.Num(4)]
    node = ast.List(elts=xs)
    assert repr(node) == "[1, *[2, 3], 4]"

    assert repr(StarredUnpackingTransformer().visit(node)) == "[1, list([2, 3]), 4]"

    xs = [ast.Num(1), ast.Starred(value=ast.List(elts=[ast.Num(2), ast.Num(3)])), ast.Num(4),
         ast.Starred(value=ast.List(elts=[ast.Num(5), ast.Num(6)]))]
    node = ast.List(elts=xs)
    assert repr

# Generated at 2022-06-14 02:20:19.523855
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from ast import parse
    from typed_ast import ast3
    from typed_ast import NodeVisitor
    class SampleNodeVisitor(NodeVisitor):
        def __init__(self):
            self.sample = list()

        def generic_visit(self, node):
            self.sample.append(node)

        
    sample = "print(*[1, 2], *[3, 4])"
    node = parse(sample)
    assert(isinstance(node, ast3.Module))
    node = node.body[0]
    assert(isinstance(node, ast3.Expr))
    node = node.value
    assert(isinstance(node, ast3.Call))
    assert(len(node.args) == 3)
    assert(isinstance(node.args[0], ast3.Num))

# Generated at 2022-06-14 02:20:24.971332
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = """
    [2, *range(10), 1]
    """
    expected = """
    [2] + list(range(10)) + [1]
    """
    tree = ast.parse(code)
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)
    assert transformer.tree_changed == True
    assert astor.to_source(tree) == expected


# Generated at 2022-06-14 02:20:39.407109
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .unittest_tools import generate_function_test
    from .pretty_printer import PrettyPrinter
    from .test_case_generator import get_test_case

    test_cases = (
        'print(a, b, c)',
        'print(a, *b, c)',
        'print(a, *b, c, *d)',
        'print(a, *b, c, *d, e)',
        'print(a, *range(10), b)',
        'print(*range(1), *range(1))',
    )


# Generated at 2022-06-14 02:20:43.715026
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .parser import parse
    code = 'print(1, *[2, 3], 4)'
    tree = parse(code)
    StarredUnpackingTransformer().visit(tree)
    assert "print(*(list([1, 2, 3, 4])))" in ast.dump(tree)

# Generated at 2022-06-14 02:20:55.713112
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Testing visit_List method of StarredUnpackingTransformer"""

    # [2, *range(10), 1]
    test_code = """\
[2, *range(10), 1]
"""
    expected_code = """\
[2] + list(range(10)) + [1]
"""
    tree = ast.parse(test_code)
    test_transformer = StarredUnpackingTransformer()
    tree = test_transformer.visit(tree)
    print(ast.dump(tree))
    assert ast.dump(tree) == expected_code

    # [2, *range(10)]
    test_code = """\
[2, *range(10)]
"""
    expected_code = """\
[2] + list(range(10))
"""

# Generated at 2022-06-14 02:20:57.619942
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer() is not None

# Generated at 2022-06-14 02:21:28.821811
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    class ListTransformer(StarredUnpackingTransformer):
        def __init__(self):
            super(ListTransformer, self).__init__()
            self._test_tree_changed = False

        def generic_visit(self, node):
            return node

        @property
        def tree_changed(self):
            return self._test_tree_changed

    test_ast = ast.parse('[1, 2, *range(10), *range(10, 20), 3]')
    node_transformer = ListTransformer()
    changed_ast = node_transformer.visit(test_ast)
    assert node_transformer.tree_changed

# Generated at 2022-06-14 02:21:40.140066
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class Visitor(StarredUnpackingTransformer):
        def __init__(self):
            super().__init__()
            self.node = None

        def generic_visit(self, node):
            self.node = super().generic_visit(node)
            return self.node

    ast_ = ast.parse(textwrap.dedent("""
        func_i_will_replace(arg1, *arg2, arg3)
        """))

    print("\n---\nSource:")
    print(ast_.body[0])

    visitor = Visitor()
    visitor.visit(ast_)
    print("\n---\nResult:")
    print(visitor.node)

    assert isinstance(visitor.node, ast.Call)

# Generated at 2022-06-14 02:21:52.803142
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    '''Unit test for method visit_Call of class StarredUnpackingTransformer'''
    from examples.call_starred_stmt_example import call_node
    # Instance of class Call
    call = call_node()
    # Instance of class StarredUnpackingTransformer
    star_unpack = StarredUnpackingTransformer()
    # Visit call instance
    result = star_unpack(call)

# Generated at 2022-06-14 02:21:58.911104
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    #arrange
    transformer = StarredUnpackingTransformer()

    node = ast.parse("[2, *range(10), 1]")
    expected_node_1 = ast.parse("[2] + list(range(10)) + [1]")

    node = ast.parse("print(*range(1), *range(3))")
    expected_node_2 = ast.parse("print(*(list(range(1)) + list(range(3))))")

    # act
    actual_node_1 = transformer.visit(node)
    actual_node_2 = transformer.visit(node)

    # assert
    assert ast.dump(actual_node_1) == ast.dump(expected_node_1)
    assert ast.dump(actual_node_2) == ast.dump(expected_node_2)

# Generated at 2022-06-14 02:22:09.889903
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    list_ = ast.List([
        ast.Num(n=2),
        ast.Starred(value=ast.Name(id='range', ctx=ast.Load())),
        ast.List([ast.Num(n=10)], ctx=ast.Load()),
        ast.Num(n=1)
    ], ctx=ast.Load())

    tree = StarredUnpackingTransformer().visit(list_)


# Generated at 2022-06-14 02:22:16.028551
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = '[2, *range(10), 1]'
    expected_result = '[2] + list(range(10)) + [1]'
    tree = ast.parse(code)
    transformer = StarredUnpackingTransformer()
    result = transformer.visit(tree)
    assert_equal(ast.unparse(result).strip(), expected_result)



# Generated at 2022-06-14 02:22:19.413111
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # import astunparse
    # test_data = '''
    #     [2, *range(10), 1]
    #     '''
    # tree = ast.parse(test_data)
    # StarredUnpackingTransformer().visit(tree)
    # astunparse.unparse(tree)
    pass

# Generated at 2022-06-14 02:22:26.438796
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[1, *[2, 3], 4]", mode='eval')
    result = StarredUnpackingTransformer().visit(node)
    expected = ast.List(elts=[
        ast.Num(n=1),
        ast.Call(
            func=ast.Name(id='list'),
            args=[ast.List(elts=[ast.Num(n=2), ast.Num(n=3)])],
            keywords=[]),
        ast.Num(n=4)
    ])
    assert isinstance(result, ast.List)
    assert result.elts == expected.elts


# Generated at 2022-06-14 02:22:32.124642
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = [
        '[2, *range(10), 1]',
    ]
    for c in code:
        tree = ast.parse(c)
        t = StarredUnpackingTransformer()
        t.visit(tree)
        assert str(t) == '[' + str(t.tree)[1:]
        assert 'Starred' not in str(t)
        assert 'range' in str(t)
        assert 'list' in str(t)


# Generated at 2022-06-14 02:22:39.817705
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    with pytest.warns(None) as warnings:
        macro = StarredUnpackingTransformer()

        node = ast.parse(
            '[2, *range(10), 1]', mode='eval').body     # type: ast.List
        node = macro.visit(node)
        assert isinstance(node, ast.BinOp)
        assert isinstance(node.left, ast.List)  # type: ignore
        assert isinstance(node.op, ast.Add)  # type: ignore
        assert isinstance(node.right, ast.List)  # type: ignore
        assert macro.tree_changed

        node = ast.parse(
            '[2, 4, *range(10), 1, 2]', mode='eval').body  # type: ast.List
        node = macro.visit(node)

# Generated at 2022-06-14 02:23:11.133643
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.parse('[2, *range(10), 1]')
    transformer = StarredUnpackingTransformer()
    new_node = transformer.visit(node)
    assert isinstance(new_node, ast.Module)
    assert isinstance(new_node.body[0], ast.Expr)
    
    node = ast.parse('print(*range(1), *range(3))')
    transformer = StarredUnpackingTransformer()
    new_node = transformer.v

# Generated at 2022-06-14 02:23:15.387807
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expected = ast.parse("result = [2] + list(range(10)) + [1]")
    tree = ast.parse("result = [2, *range(10), 1]")
    assert expected.body[0].value.elts[1].func.id == "list"
    assert expected.body[0].value.elts[1].args[0].id == "range"
    assert expected.body[0].value == StarredUnpackingTransformer().visit(tree.body[0].value)


# Generated at 2022-06-14 02:23:21.256867
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = "[2, *range(10), 1]"
    tree = ast.parse(code)
    StarredUnpackingTransformer().visit(tree)
    new_code = compile(tree, '<>', 'exec')
    assert code == new_code.co_code


# Generated at 2022-06-14 02:23:32.788742
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()
    code = 'print(*list(range(10)), 2)'
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    # tr = ast.Assign(targets=[ast.Name(id='tree')], value=tree)
    # mod = ast.Module(body=[tr])
    code_transformed = ast.dump(tree)
    print(code_transformed)

# Generated at 2022-06-14 02:23:34.600129
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert isinstance(StarredUnpackingTransformer(), StarredUnpackingTransformer)

# Generated at 2022-06-14 02:23:46.786401
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    # Example 1: Split list of args with Starred
    # [2, *range(10), 1]
    # [2] + list(range(10)) + [1]
    node = ast.parse('[2, *range(10), 1]')
    expected = ast.parse('[2] + list(range(10)) + [1]')
    node = StarredUnpackingTransformer().visit(node)
    assert astor.to_source(node) == astor.to_source(expected)

    # Example 2: Split list of args with Starred
    # [2, *range(10)]
    # [2] + list(range(10))
    node = ast.parse('[2, *range(10)]')

# Generated at 2022-06-14 02:23:56.985015
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_utils import transform, assert_equal
    code_to_transform = """
mylist = [2, *range(10), 1, *range(2)]
print(*range(1), *range(3))
"""
    expected_result = """
mylist = (2 + list(range(10)) + 1 + list(range(2)))
print(*(list(range(1)) + list(range(3))))
"""
    result = transform(code_to_transform, StarredUnpackingTransformer)
    assert_equal(result, expected_result)

# Generated at 2022-06-14 02:24:01.049147
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .utils import do_test

    code = "print(*range(1), *range(3))"
    expected = "print(*(list(range(1)) + list(range(3))))"
    do_test(code, expected, StarredUnpackingTransformer)


# Generated at 2022-06-14 02:24:06.368075
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer().visit(
        ast.parse('max(1, *range(2), 3, 4, *range(5), 6, *range(7))')) == \
        ast.parse('max(*(([1] + list(range(2)) + [3, 4] + list(range(5)) + [6] + list(range(7)))))')



# Generated at 2022-06-14 02:24:17.106678
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer."""
    from astmonkey import transformers
    wayround_i2p.utils.lg.set_debug_level(1)
    transformer = StarredUnpackingTransformer()
    transformer.visit(ast.parse("x = [1, 2, *range(8), 9, *range(10), 10, 11, 12]"))
    assert transformer.result == "x = [1, 2] + list(range(8)) + [9] + list(range(10)) + [10, 11, 12]"
    wayround_i2p.utils.lg.set_debug_level(0)

# Generated at 2022-06-14 02:25:14.272582
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
print(2, 3, 4)
print(*[2, 3, 4])
print(*[2, 3, 4], *[5, 6, 7])
print(*[2, 3, 4], *[5, 6, 7], *[8, 9, 10])
"""

    expected = """
print(2, 3, 4)
print(*[2, 3, 4])
print(*(list([2, 3, 4]) + list([5, 6, 7])))
print(*(list([2, 3, 4]) + list([5, 6, 7]) + list([8, 9, 10])))
"""

    compare_ast(source, expected, StarredUnpackingTransformer)


# Generated at 2022-06-14 02:25:23.363367
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer"""
    # assert does nothing if test passes
    assert StarredUnpackingTransformer().visit(ast.parse("[2, *range(10), 1]").body[0]) == ast.parse("[2] + list(range(10)) + [1]").body[0]
    assert StarredUnpackingTransformer().visit(ast.parse("[2,range(10), 1]").body[0]) == ast.parse("[2,range(10), 1]").body[0]
    assert StarredUnpackingTransformer().visit(ast.parse("[2, 1]").body[0]) == ast.parse("[2, 1]").body[0]


# Generated at 2022-06-14 02:25:30.713723
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast.ast3 import parse
    stmt = parse("print(*range(1), *range(3))").body[0]

    transformer = StarredUnpackingTransformer()
    assert transformer.visit(stmt) == parse("print(*(list(range(1)) + list(range(3))))").body[0]
    assert transformer._tree_changed


# Generated at 2022-06-14 02:25:40.694199
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from . import dump
    from . import CompileError
    from . import transform

    # No changes
    assert dump(transform(3, 4, 'a=[2, 3]')) == '[2, 3]'
    assert dump(transform(3, 4, 'a={2, 3}')) == '{2, 3}'
    assert dump(transform(3, 4, 'a={2: 7, 3: 2}')) == '{2: 7, 3: 2}'
    assert dump(transform(3, 4, 'a=()')) == '()'

    # Success
    assert dump(transform(3, 4, 'a=[2, *range(10), 8]')) == '[2] + list(range(10)) + [8]'

# Generated at 2022-06-14 02:25:52.119607
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    expected = ast.parse("[1, 2, *range(10), 4, 5]")
    input = ast.parse("[1, 2, *range(10), 4, 5]")
    value = StarredUnpackingTransformer().visit(input)
    assert ast.dump(value) == ast.dump(expected)

    expected = ast.parse("[1, 2, *range(10), 4, 5]")
    input = ast.parse("[1, 2] + list(range(10)) + [4, 5]")
    value = StarredUnpackingTransformer().visit(input)
    assert ast.dump(value) == ast.dump(expected)

    expected = ast.parse("[1, 2, *range(10), 4, 5]")

# Generated at 2022-06-14 02:26:01.097677
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import textwrap
    test_code = textwrap.dedent("""
        def foo():
            [1, *data, 2]
            print(*data, 3)
        """)

    expected_code = textwrap.dedent("""
        def foo():
            [1] + list(data) + [2]
            print(*(list(data) + [3]))
        """)

    StarredUnpackingTransformer()(test_code) == expected_code

# Generated at 2022-06-14 02:26:07.176328
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .fixtures import StarredUnpackingTransformer_visit_Call as test_values
    for test_value in test_values:
        # ARRANGE #
        sut = StarredUnpackingTransformer()
        # ACT #
        actual = sut.visit(ast.parse(test_value.input))
        # ASSERT #
        assert ast.dump(actual) == test_value.expected

# Generated at 2022-06-14 02:26:12.879452
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import astor
    from .python_transpile import PythonTranspile
    from .base import TranspileTestCase

    class Test(TranspileTestCase):
        def test_empty(self):
            self.assertEqualProgram(
                PythonTranspile,
                [
                    ast.List(elts=[],
                             ctx=ast.Load())
                ],
                [
                    "[]"
                ])

        def test_normal(self):
            self.assertEqualProgram(
                PythonTranspile,
                [
                    ast.List(elts=[
                        ast.Num(n=1),
                        ast.Num(n=2),
                        ast.Num(n=3),
                    ],
                        ctx=ast.Load())
                ],
                [
                    "[1, 2, 3]"
                ])



# Generated at 2022-06-14 02:26:24.747729
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import sys
    try:
        from typed_ast import ast3 as ast
    except ImportError:
        sys.stderr.write("Skip test, typed_ast not installed")
        return
    source_1 = """
        a = [2, *range(10), 1]
        """
    source_2 = """
        a = [2, *range(10), 1, b]
        """
    source_3 = """
        a = [2]
        """
    source_4 = """
        a = [2, 3, *range(10)]
        """
    source_5 = """
        a = [2, 3, *range(0)]
        """
    origin_1 = ast.parse(source_1)
    origin_2 = ast.parse(source_2)

# Generated at 2022-06-14 02:26:28.630495
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    case = ast.parse("print(*range(1), *range(3))").body[0]
    ult = StarredUnpackingTransformer()
    result = ult.visit(case)
    assert result == ast.parse("print(*(list(range(1)) + list(range(3))))").body[0]
