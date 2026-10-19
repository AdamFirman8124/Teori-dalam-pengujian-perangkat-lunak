

# Generated at 2022-06-14 02:17:17.131163
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # given
    import ast, typed_astunparse
    from ast_helpers import print_ast, ast_eq

    node = ast.parse('print(1, *range(3), 4, *range(3), 5)').body[0].value
    assert isinstance(node, ast.Call)

    # when
    actual_code = typed_astunparse.unparse(StarredUnpackingTransformer().visit(node))

    # then
    expected_code = "print(*([1] + list(range(3)) + [4] + list(range(3)) + [5]))"
    assert ast_eq(actual_code, expected_code)


# Generated at 2022-06-14 02:17:23.466485
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import os
    import textwrap
    from nuitka.tree.Building import parseFromTextCode

    source_code = textwrap.dedent(
    '''
    call_func(1, *range(a), b, c=[*range(c), d, *range(e)], *range(f), g, h, i=[*range(i), j])
    ''')
    expected_code = textwrap.dedent(
    '''
    call_func(*(list([1]) + list(range(a)) + [b] + [c] + list(range(c)) + [d] + list(range(e)) + list(range(f)) + [g] + [h] + [i] + list(range(i)) + [j]))
    ''')

# Generated at 2022-06-14 02:17:28.818908
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse
    def test(code):
        module = ast.parse(code)
        StarredUnpackingTransformer().visit(module)
        print(unparse(module))

    test("print(*range(1), 2)")

# Generated at 2022-06-14 02:17:39.325433
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    nodes = [
        ast.parse(
            """
print(*range(1), *range(3))
            """
        ),
        ast.parse(
            """
[2, *range(10), 1]
            """
        )
    ]

    expected = [
        ast.parse(
            """
print(*(list(range(1)) + list(range(3))))
            """
        ),
        ast.parse(
            """
[2] + list(range(10)) + [1]
            """
        )
    ]

    for node, expected_node in zip(nodes, expected):
        expected_node.body[0].value.args[0].value.value.args[0].value.value.value.value.args[0].value.value.value.value.value.value.value.value.value

# Generated at 2022-06-14 02:17:53.950704
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_helpers import get_node

    def check(old: str, new: str):
        node = get_node(old)
        tr = StarredUnpackingTransformer()
        tr.visit(node)
        assert new == tr.root.print()

    # Simple case
    check('foo(*range(1))', 'foo(*(list(range(1))))')

    # With kwargs
    check('foo(10, 3, 2, *range(15), x=1)',
          'foo(10, 3, 2, *(list(range(15))), x=1)')

    # Without args
    check('foo()', 'foo()')

    # With keywords
    check('foo(*range(3), **{})', 'foo(*(list(range(3))), **{})')

    #

# Generated at 2022-06-14 02:17:54.610604
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:18:04.901156
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    t = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:18:10.697504
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    actual_code = (
        "print(*range(1), *range(3))"
    )
    expected_code = (
        "print(*(list(range(1)) + list(range(3))))"
    )
    expected_code = expected_code.encode('utf8')

    node = ast.parse(actual_code)
    StarredUnpackingTransformer().visit(node)

    assert ast.dump(node) == expected_code



# Generated at 2022-06-14 02:18:21.520014
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Testing method visit_Call of class StarredUnpackingTransformer."""
    from typed_ast import ast3 as ast

    tree = ast.parse("""print(*range(1), 2, *range(3), 4)""")

    StarredUnpackingTransformer().visit(tree)

    expected = """
print(*(list(range(1)) + [2] + list(range(3)) + [4]))
    """.strip().split("\n")

    assert tree.body[0].dump() == expected[0], \
        "Doesn't transform print(*range(1), 2, *range(3), 4)"
    assert tree.body[0].value.args[0].dump() == expected[1], \
        "Doesn't transform print(*range(1), 2, *range(3), 4)"

# Generated at 2022-06-14 02:18:26.919894
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = """
    print(*range(1), *range(3))
    """
    module = ast.parse(code)
    StarredUnpackingTransformer().visit(module)
    expected = """
    print(*(list(range(1)) + list(range(3))))
    """
    assert ast.dump(module, include_attributes=True) == ast.dump(ast.parse(expected), include_attributes=True)


# Generated at 2022-06-14 02:18:41.542003
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import unittest
    from typed_ast.ast3 import parse
    from .utils import TreeMatcher
    from .base import BaseTestTransformer
    from .unpacking import UnpackingTransformer
    from .elif_simplification import ElifSimplificationTransformer

    class TestTransformer(BaseTestTransformer):
        transformations = [StarredUnpackingTransformer, UnpackingTransformer, ElifSimplificationTransformer]

        def assert_code(self, before, after):
            def normalize(code):
                code = code.rstrip().rstrip(';')
                code = code.replace(" ", "")
                code = code.replace("print(", "__print(").replace("print ", "__print(")
                code = code.replace("input(", "__input(").replace("input ", "__input(")
               

# Generated at 2022-06-14 02:18:50.948232
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .stringify import unparse
    from .uncompyle_test_data import typed_scripts
    from . import transform

    source = typed_scripts['starred_unpacking']['source']
    tree = transform(StarredUnpackingTransformer, source=source)
    after = unparse(tree)

# Generated at 2022-06-14 02:18:59.418663
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = '[2, *range(10), 1]'
    expected = '__builtins__.list([2]) + __builtins__.list(range(10)) + __builtins__.list([1])'
    tree = ast.parse(source)
    edit = StarredUnpackingTransformer()
    new_tree = edit.visit(tree)
    code = compile(new_tree, '<string>', 'exec')
    context = {}
    exec(code, context)
    assert expected == repr(context['__builtins__'].list([2, 1, 2]))


# Generated at 2022-06-14 02:19:05.727025
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    mapping = {'list': ast.Name(id='list')}
    transformer = StarredUnpackingTransformer(mapping)
    tree = ast.parse("print(0, *[1, 2], 3)")
    tree = transformer.visit(tree)

    reference = ast.parse("print(*(list([0]) + list([1, 2]) + list([3])))")

    assert ast.dump(tree) == ast.dump(reference)


# Generated at 2022-06-14 02:19:11.792972
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    src = ["print(*range(1), *range(3))"]
    src = ast.parse('\n'.join(src))
    src = StarredUnpackingTransformer(src).visit(src)
    src = ast.fix_missing_locations(src)
    exec(compile(src, filename="<ast>", mode="exec"))


# Generated at 2022-06-14 02:19:15.451438
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .util import roundtrip_unparse, build_module
    
    code = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'
    module = build_module(code)
    assert expected == roundtrip_unparse(module)


# Generated at 2022-06-14 02:19:22.792730
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_list = [2, ast.Starred(value=ast.Name(id='range', ctx=ast.Load()), elt=ast.Load()), 1]
    expected_list = ast.List(elts = [2, 1], ctx = ast.Load())
    expected_list = ast.BinOp(
        left = expected_list,
        op = ast.Add(),
        right = ast.Call(
            func = ast.Name(id = 'list'),
            args = [ast.Call(
                func = ast.Name(id = 'range', ctx = ast.Load()),
                args = [],
                keywords = []
            )],
            keywords = []
        )
    )

    result = StarredUnpackingTransformer().visit(ast.List(elts = test_list))

# Generated at 2022-06-14 02:19:32.153212
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    import ast
    import textwrap
    t = StarredUnpackingTransformer()
    before = ast.parse(textwrap.dedent("""
        class A:
            pass
        [2, *range(10), 1]"""))
    expected = textwrap.dedent("""
        class A:
            pass
        [2] + list(range(10)) + [1]""")
    after = t.visit(before)
    expected_after = ast.parse(expected)
    assert ast.dump(after, include_attributes=False) == ast.dump(
        expected_after, include_attributes=False)



# Generated at 2022-06-14 02:19:40.145737
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code = [
        'print(2, *range(5))',

        'print([1, *range(9)])',
        '[1, *range(9)]',

        #'[1, [1, *range(9)], *range(9)]',
        # Not supported: *args inside list.
    ]
    output = [
        'print(2, *list(range(5)))',
        'print(list([1]) + list(range(9)))',
        'list([1]) + list(range(9))',
    ]

    StarredUnpackingTransformer.test_transform(code)

# Generated at 2022-06-14 02:19:51.227866
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast
    from .utils import compile_source

    node = ast.Call(
        func=ast.Name(id='foo'),
        args=[ast.Constant(value=1),
              ast.List(elts=[], ctx=ast.Load()),
              ast.Constant(value=2)])
    exp_node = ast.Call(
        func=ast.Name(id='foo'),
        args=[ast.Starred(value=ast.BinOp(left=ast.List(elts=[ast.Constant(value=1)]),
                                          right=ast.List(elts=[]),
                                          op=ast.Add()))])

    print(compile_source(ast.Module([ast.Expr(value=node)]), mode='exec'))
    assert exp

# Generated at 2022-06-14 02:20:02.414575
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = "[1, 2, *range(10)]"
    expected = "[1, 2] + list(range(10))"
    utils.assert_one_line_transformation(StarredUnpackingTransformer, source, expected)



# Generated at 2022-06-14 02:20:11.980927
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .annotations import get_annotations

    # test original body
    node = ast.parse('l = [2, *range(10), 1]\n'
                     'print(*range(1), *range(3))\n')
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)
    orig = ast.dump(node)

    # test optimized body
    node = ast.parse('l = [2, *range(10), 1]\n'
                     'print(*range(1), *range(3))\n')
    expected = ast.dump(node)
    orig_annotations = get_annotations(node)
    expected_annotations = orig_annotations.copy()
    transformer = StarredUnpackingTransformer()
    transformed_node = transformer.visit(node)
    optimized = ast

# Generated at 2022-06-14 02:20:23.902934
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class FuncDefExample(ast.FunctionDef):
        __slots__ = ('names',)
        _fields = ('name', 'args', 'body')

        def __init__(self, *args, **kwargs):
            self.names = kwargs.pop('names', [])
            super(FuncDefExample, self).__init__(*args, **kwargs)

    def visit_FunctionDef(self, node):
        self.names.append(node.name)
        return node


# Generated at 2022-06-14 02:20:30.144655
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .fixtures import compile_visitor
    from astor import to_source
    code = "[2, *range(10), 1]"
    expected = "[2] + list(range(10)) + [1]"
    tree = compile_visitor(code, StarredUnpackingTransformer)
    assert to_source(tree) == expected


# Generated at 2022-06-14 02:20:30.793394
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    StarredUnpackingTransformer()

# Generated at 2022-06-14 02:20:42.060568
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import unittest

    class TestCase(unittest.TestCase):
        def test(self):
            transformer = StarredUnpackingTransformer()

            def check(before, after):
                node = ast.parse(before)
                transformer.visit(node)
                self.assertEqual(ast.dump(node), after)

            check('f(*[1], *[2])', 'f(*(list(1) + list(2)))')
            check('f(*[1], 2, *[3], 4, *[5])', 'f(*(list(1) + [2] + list(3) + [4] + list(5)))')
            check('f(*[1, 2], 3, *[4, 5])', 'f(*([1, 2] + [3] + [4, 5]))')
           

# Generated at 2022-06-14 02:20:47.347366
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import pprint
    code = """
    a, *b = [1,3,4]
    """
    ast_module = ast.parse(code)
    t = StarredUnpackingTransformer()
    t.visit(ast_module)
    pprint.pprint(ast.dump(ast_module))
# End of test for method visit_Call of class StarredUnpackingTransformer


# Generated at 2022-06-14 02:20:57.235346
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    obj = StarredUnpackingTransformer()
    obj.visit_List(ast.List(elts=[ast.Num(n=2),ast.Starred(value=ast.Name(id='range', ctx=ast.Load())),ast.Num(n=1)])) #returns ast.BinOp
    obj.visit_Call(ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Starred(value=ast.Name(id='range', ctx=ast.Load())),ast.Starred(value=ast.Name(id='range', ctx=ast.Load()))], keywords=[])) #returns ast.Call

# Generated at 2022-06-14 02:21:08.403945
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .common import compile_to_ast, unparse

    code = 'print(*range(5), *range(1))'
    ast_tree = compile_to_ast(code)
    assert isinstance(ast_tree, ast.Module)

    xformer = StarredUnpackingTransformer()
    new_tree = xformer.visit(ast_tree)

    assert isinstance(new_tree, ast.Module)
    assert isinstance(new_tree.body[0], ast.Expr)

    new_code = unparse(new_tree)
    assert 'print(*(' in new_code and '))' in new_code
    assert len(new_code) == 18

# Generated at 2022-06-14 02:21:14.571043
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    tree = ast.parse("[2, *range(10), 1]")
    out = "tmp___0 = list(range(10))\n[2] + tmp___0 + [1]\n"
    assert out == str(StarredUnpackingTransformer().visit(tree))



# Generated at 2022-06-14 02:21:28.374051
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import compile_source

    assert compile_source('print(42, *range(1), *range(1))',
                          StarredUnpackingTransformer) \
           == 'print(*(list(range(1)) + list(range(1))))'

# Generated at 2022-06-14 02:21:38.650996
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    source = inspect.getsource(StarredUnpackingTransformer)

# Generated at 2022-06-14 02:21:50.764207
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    code = """
    [2, *range(10), 1]
    print(*range(1), *range(3))
    """

    expected_code = """
    [2] + list(range(10)) + [1]
    print(*(list(range(1)) + list(range(3))))
    """

    # Get AST
    node = ast.parse(code)

    # Transform
    transformer = StarredUnpackingTransformer()
    new_node = transformer.visit(node)

    # Make code from AST
    gen = ast.PyCF_ONLY_AST | ast.PyCF_INDENT_INCREMENTAL
    module_code = compile(new_node, '<string>', 'exec', gen)

# Generated at 2022-06-14 02:21:52.793137
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .transpile_test import transpile_func
    
    

# Generated at 2022-06-14 02:21:56.573841
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    stmt = 'sort([2, *range(10), 1])'
    expected = 'sort([2] + list(range(10)) + [1])'
    tested = StarredUnpackingTransformer(stmt)
    assert tested == expected


# Generated at 2022-06-14 02:22:06.817907
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .helpers import get_ast, compare_asts

    source = '''
        import typing
        import random
        import numpy as np
        import pandas as pd

        d = pd.DataFrame(np.random.randint(0,10,size=(5, 1)))
        data = list(range(10))
        random.shuffle(data)
        print(*data)
        '''

    expected = '''
        import typing
        import random
        import numpy as np
        import pandas as pd

        d = pd.DataFrame(np.random.randint(0,10,size=(5, 1)))
        data = list(range(10))
        random.shuffle(data)
        print(*(list(data)))
        '''

    tree = get_ast(source)
    new

# Generated at 2022-06-14 02:22:08.228861
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().target == (3, 4)

# Generated at 2022-06-14 02:22:11.637278
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    with pytest.raises(Exception):
        x = ast.List()
        StarredUnpackingTransformer().visit(x)


# Generated at 2022-06-14 02:22:12.745504
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor


# Generated at 2022-06-14 02:22:21.001485
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    node = ast.parse('[2, *range(10), 1]').body[0].value
    
    # Arguments: 0
    ast.fix_missing_locations(transformer.visit(node))
    
    with pytest.raises(AssertionError):
        ast.fix_missing_locations(transformer.visit(node))
    
    # Arguments: 1
    result = transformer.visit(node)
    
    assert isinstance(result, ast.List)
    
    assert len(result.elts) == 1
    
    assert isinstance(result.elts[0], ast.BinOp)
    
    assert isinstance(result.elts[0].left, ast.BinOp)
    

# Generated at 2022-06-14 02:22:52.412152
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import sys
    import io
    import astunparse

    class ModuleStream(io.StringIO):
        # Prevents ValueError: Mixing iteration and read methods would lose data
        def read(self, n=-1):
            return super().read(n)

    old_stdout = sys.stdout
    sys.stdout = ModuleStream()

# Generated at 2022-06-14 02:22:58.149957
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    print("test_StarredUnpackingTransformer")

    import astunparse
    test = ast.parse("[2, *range(10), 1]")
    test1 = ast.parse("[2, *range(10), 1] + [10]")
    test2 = ast.parse("print(*range(1), *range(3))")

# Generated at 2022-06-14 02:23:09.728467
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source = """
        print(*range(1), *range(3))
    """

    from .util import roundtrip, compare_ast, print_tree_difference
    from .tidy_imports import TidyImportsTransformer
    from .import_to_full_name import ImportToFullNameTransformer

    node = next(ast.parse(source).body)

    node2 = roundtrip(node)
    nodes = [node, node2]
    for node in nodes:
        StarredUnpackingTransformer().visit(node)
        TidyImportsTransformer().visit(node)
        ImportToFullNameTransformer().visit(node)

    compare_ast(nodes[0], nodes[1])


# Generated at 2022-06-14 02:23:14.143323
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    t = StarredUnpackingTransformer()
    node = ast.parse('print([1, *range(3), 2])').body[0]
    node = t.visit(node)
    expected = 'print(*([1] + list(range(3)) + [2]))'
    assert to_source(node) == expected


# Generated at 2022-06-14 02:23:20.388392
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astunparse
    source = 'list([1, 2] + [a, b])'
    tree = ast.parse(source)
    StarredUnpackingTransformer().visit(tree)
    print(astunparse.dump(tree))
    # assert astunparse.dump(tree) == None


# Generated at 2022-06-14 02:23:31.909178
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    test1 = ast.parse('iter([1, *A, 3, 4])')
    StarredUnpackingTransformer().visit(test1)
    mod = ast.parse(star_unpack_transform(test1))
    assert star_unpack_transform(test1) == 'iter(list([1]) + A + list([3, 4]))'

    test2 = ast.parse('a[1, *x, 2]')
    StarredUnpackingTransformer().visit(test2)
    mod = ast.parse(star_unpack_transform(test2))
    assert star_unpack_transform(test2) == 'a[list([1]) + x + list([2])]'


# Generated at 2022-06-14 02:23:40.661688
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer."""
    from .test_utils import round_trip
    source = 'print(*range(1), *range(3))'
    expected = 'print(*(list(range(1)) + list(range(3))))'
    node = round_trip(source)
    node = StarredUnpackingTransformer().visit(node)
    got = round_trip(node)
    assert_equal(expected, got)


# Generated at 2022-06-14 02:23:48.872505
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    code_before = """[2, *range(10), 1]"""

    expected_after = """[2] + list(range(10)) + [1]"""

    tree_before = ast.parse(code_before)
    tree_after = ast.parse(expected_after)

    transformer = StarredUnpackingTransformer()
    transformer.visit(tree_before)
    assert transformer.tree_changed is True
    assert ast.dump(tree_before) == ast.dump(tree_after)

# Generated at 2022-06-14 02:23:50.543105
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().target == (3, 4)


# Generated at 2022-06-14 02:24:02.503927
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    node1 = ast.parse('print(*range(10))')
    node2 = ast.parse('print(*range(1))')
    node3 = ast.parse('print(*range(1), *range(3))')
    node4 = ast.parse('print(*[1, 2, 3], *[4, 5, 6])')
    StarredUnpackingTransformer().visit(node1)
    StarredUnpackingTransformer().visit(node2)
    StarredUnpackingTransformer().visit(node3)
    StarredUnpackingTransformer().visit(node4)
    assert astor.to_source(node1) == 'print(*list(range(10)))\n'
    assert astor.to_source(node2) == 'print(*list(range(1)))\n'

# Generated at 2022-06-14 02:24:41.475423
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    # parametrize input, output
    args = [ast.Call(
                    ast.Name(id='print'),
                    [ast.Starred(ast.Call(
                                    ast.Name(id='list'),
                                    [ast.Call(
                                        ast.Name(id='range'),
                                        [ast.Num(n=1)],
                                        [])],
                                    []))],
                    [])]


# Generated at 2022-06-14 02:24:51.842947
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Test StarredUnpackingTransformer(BaseNodeTransformer).visit_Call"""
    import astor
    from .pytree import PyTree
    from .unparse import Unparser
    from .unparse import Unparser
    
    source = """
        from typing import List, Dict, Union
        def f(x: List[int]):
            print(*range(1), *range(3), *range(4))
        """
    tree = PyTree(source, 'test_StarredUnpackingTransformer_visit_Call')
    result = tree.transform(StarredUnpackingTransformer)
    unparse = Unparser(result, tree._source).unparse()

# Generated at 2022-06-14 02:25:04.552372
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    # Should not change this
    inp = [ast.Num(n=2), ast.Num(n=1)]
    expected = [ast.Num(n=2), ast.Num(n=1)]

    res = StarredUnpackingTransformer().visit_List(ast.List(elts=inp))
    assert expected == res.elts
    assert isinstance(res, ast.List)

    # Should convert this
    inp = [ast.Num(n=2), ast.Starred(value=ast.Name(id='range')), ast.Num(n=1)]
    expected = ast.Num(n=2) + ast.Call(
        func=ast.Name(id='list'),
        args=[ast.Name(id='range')],
        keywords=[]) + ast.Num(n=1)

    res

# Generated at 2022-06-14 02:25:05.704760
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    pass


# Generated at 2022-06-14 02:25:13.250928
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import astor

    code_str = '[2, *range(10), 1]'
    tree = ast.parse(code_str)
    expected_str = '[2] + list(range(10)) + [1]'

    StarredUnpackingTransformer().visit(tree)

    result_str = astor.to_source(tree).strip()

    assert expected_str == result_str

# Generated at 2022-06-14 02:25:21.402237
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert ast.dump(StarredUnpackingTransformer().visit(ast.parse('print(1, *[1], 2)'))) \
           == "Call(func=Name(id='print', ctx=Load()), args=[Starred(value=List(elts=[Num(n=1), Call(func=Name(id='list', ctx=Load()), args=[List(elts=[Num(n=1)], ctx=Load())], keywords=[]), Num(n=2)], ctx=Load()))], keywords=[])"

# Generated at 2022-06-14 02:25:30.917801
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor
    from aiida_verdi import logger

    def _check(before: str, after: str):
        logger.setLevel(10)

        tree = ast.parse(before)
        StarredUnpackingTransformer().visit(tree)
        logger.info('Before:  {}'.format(before))
        logger.info('After:   {}'.format(astor.to_source(tree)))
        logger.info('Expected: {}'.format(after))

    _check(
        'def test(x): return x + y',
        'def test(x): return x + y'
    )

    _check(
        'def test(): print(*args)',
        "def test(): print(*(list(args)))"
    )


# Generated at 2022-06-14 02:25:40.047833
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import assert_transform

    assert_transform(
        StarredUnpackingTransformer,
        r'''
        [2, *range(10), 1]
        ''',
        r'''
        list([2]) + list(range(10)) + list([1])
        '''
    )

    assert_transform(
        StarredUnpackingTransformer,
        r'''
        [2, *range(1), *range(3), 1]
        ''',
        r'''
        list([2]) + list(range(1)) + list(range(3)) + list([1])
        '''
    )


# Generated at 2022-06-14 02:25:45.757497
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    actual = ast.parse(
        'print(*range(1), *range(3))'
    )
    expected = ast.parse(
        'print(*(list(range(1)) + list(range(3))))'
    )
    assert StarredUnpackingTransformer().visit(actual) == expected

# Generated at 2022-06-14 02:25:47.056945
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_astunparse import unparse