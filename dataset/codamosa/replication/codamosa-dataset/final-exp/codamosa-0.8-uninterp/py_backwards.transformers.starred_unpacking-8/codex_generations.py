

# Generated at 2022-06-14 02:17:07.170230
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    test_string = '[2, *range(10), 1]'
    test_tree = ast.parse(test_string)
    transformer = StarredUnpackingTransformer()
    transformer.visit(test_tree)
    expected_string = '[2] + list(range(10)) + [1]'
    expected_tree = ast.parse(expected_string)
    assert ast.dump(test_tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 02:17:16.501881
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from compiler import compile
    from .test_utils import compare

    def transform_test():
        return print(*[1, 2], *[3, 4], *[5, 6], *[7, 8])  # type: ignore

    # expected output
    def expected():
        return print(*(list([1, 2]) + list([3, 4]) + list([5, 6]) + list([7, 8])))  # type: ignore

    # compare
    compare(expected, transform_test, StarredUnpackingTransformer)

    # compile
    assert compile(expected(), filename='', mode='exec')



# Generated at 2022-06-14 02:17:23.466413
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert StarredUnpackingTransformer.run_on_single_file(
        'print(*range(0), *range(1))',
        ast.parse('print(*(list(range(0)) + list(range(1))))')
    )
    assert StarredUnpackingTransformer.run_on_single_file(
        'x = [1, 2, *range(10), *range(11), 3, 4]',
        ast.parse('x = [1, 2] + list(range(10)) + list(range(11)) + [3, 4]')
    )

# Generated at 2022-06-14 02:17:30.427611
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    assert ast.dump(StarredUnpackingTransformer().visit(ast.parse('print(*[1, 2, 3])').body[0])) == 'Call(func=Name(id=\'print\', ctx=Load()), args=[Starred(value=BinOp(left=List(elts=[Num(n=1), Num(n=2), Num(n=3)], ctx=Load()), right=List(elts=[], ctx=Load()), op=Add()))], keywords=[])'


# Generated at 2022-06-14 02:17:34.312074
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse("print(*range(1), *range(3))")
    expected = ast.parse("print(*(list(range(1)) + list(range(3))))")
    actual = StarredUnpackingTransformer().visit(tree)

    assert ast.dump(expected, include_attributes=False) == ast.dump(actual, include_attributes=False)


# Generated at 2022-06-14 02:17:44.380673
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    star = lambda x: ast.Starred(value=x)
    name = lambda x: ast.Name(id=x)
    t = StarredUnpackingTransformer()
    tree1 = ast.List()
    tree2 = ast.List(elts=[name('a')])
    tree3 = ast.List(elts=[name('a'), name('b')])
    tree4 = ast.List(elts=[name('a'), name('b'), name('c')])
    tree5 = ast.List(elts=[name('a'), star(name('b')), name('c')])
    tree6 = ast.List(elts=[star(name('a')), name('b'), name('c')])
    tree7 = ast.List(elts=[name('a'), name('b'), star(name('c'))])
   

# Generated at 2022-06-14 02:17:48.784994
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from . import patch_ast

    root = ast.parse("[2, *range(10), 1]")
    root = StarredUnpackingTransformer().visit(root)
    print(patch_ast(root))

    assert patch_ast(root) == "[2] + list(range(10)) + [1]"


# Generated at 2022-06-14 02:17:50.897833
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert hasattr(StarredUnpackingTransformer, '__annotations__')

# Generated at 2022-06-14 02:18:01.615081
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .helper import get_ast, dump_ast
    code = """
    print(1, *range(3))
    print(*range(3))
    print(*range(3), *range(5))
    """
    old_ast = get_ast(code)
    new_ast = StarredUnpackingTransformer().visit(old_ast)
    expected_code = """
    print(([1] + list(range(3))))
    print(*(list(range(3))))
    print(*((list(range(3)) + list(range(5)))))
    """
    expected_ast = get_ast(expected_code)
    assert dump_ast(new_ast) == dump_ast(expected_ast)


# Generated at 2022-06-14 02:18:05.389328
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    x = StarredUnpackingTransformer(
            source='[*range(1), *range(3)]', 
            filename='<string>')
    x.visit_mod()
    assert x.to_source() == 'list(*range(1)) + list(*range(3))', x.to_source()


# Generated at 2022-06-14 02:18:19.502980
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .helpers import get_visit_test_cases
    from .helpers import run_visit_test_cases
    cases = get_visit_test_cases(
        filename='StarredUnpackingTransformer_test_cases/test_visit_List.txt',
        method_name='visit_List',
        transform_class=StarredUnpackingTransformer,
        additional_context=dict(
            additional_imports=[
                {
                    'from': 'typed_ast.ast3',
                    'import': 'ast',
                    'alias': None
                }
            ],
            tree_changed=False
        )
    )
    run_visit_test_cases(visit_case_list=cases)


# Generated at 2022-06-14 02:18:21.493552
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    transformer = StarredUnpackingTransformer()
    assert transformer is not None



# Generated at 2022-06-14 02:18:26.232727
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = ast.parse('[2, *range(10), 1]')
    expected = ast.parse('[2] + list(range(10)) + [1]')
    result = StarredUnpackingTransformer.run_on(
        source,
        is_top_level=True
    )
    assert ast.dump(result) == ast.dump(expected)



# Generated at 2022-06-14 02:18:37.521241
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    tree = ast.parse(
        """
        spam_eggs('spam', 'eggs', 'ham', 'bacon')
        spam_eggs('spam', 'eggs', *range(10))
        spam_eggs('spam', 'eggs', *range(10), 'ham', 'bacon')
        spam_eggs('spam', *range(10), 'eggs')
        spam_eggs('spam', 'eggs', 'ham', *range(10))
        spam_eggs('spam', 'eggs', 'ham', *range(10), 'bacon')
        """)

    transformer = StarredUnpackingTransformer()
    new_tree = transformer.visit(tree)
    transformer.raise_if_changed()


# Generated at 2022-06-14 02:18:39.120904
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:18:43.972622
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    expected_tree = ast.parse("print(*(list(range(1)) + list(range(3))))")
    tree = ast.parse("print(*range(1), *range(3))")
    StarredUnpackingTransformer().visit(tree)
    assert expected_tree == tree


# Generated at 2022-06-14 02:18:55.408667
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .test_utils import make_test_tree

    tree = make_test_tree("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)

    source = tree.body[0].value
    assert isinstance(source, ast.BinOp)
    assert isinstance(source.left, ast.List)
    assert len(source.left.elts) == 1
    assert source.left.elts[0].n == 2

    assert isinstance(source.right, ast.BinOp)
    assert isinstance(source.right.left, ast.Call)
    assert isinstance(source.right.left.func, ast.Name)
    assert source.right.left.func.id == 'list'

# Generated at 2022-06-14 02:19:06.110728
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    class A:
        def __init__(self):
            self.b = None
            self.d = None

        def c(self, e=None, f=None, *args, **kwargs):
            pass
    a = A()

# Generated at 2022-06-14 02:19:15.805552
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .. import Compiler
    from astor.codegen import to_source

    c = Compiler(
        version=3,
        features={'StarredUnpackingTransformer'},
    )
    result = to_source(c.visit_raw_ast(ast.parse('[2, *range(10), 1]')))
    assert result.strip() == '[2] + list(range(10)) + [1]', result

    result = to_source(c.visit_raw_ast(ast.parse('[*range(10)]')))
    assert result.strip() == 'list(range(10))', result



# Generated at 2022-06-14 02:19:22.011181
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .typed_uncompyle6 import typed_uncompyle6

    code = dedent("""
        def f(x, y, z):
            print(x, y, z)

        f(2, 3, *range(10))
    """)

    result = typed_uncompyle6(code, version=3.4)
    # print(result)
    expected = dedent("""
        def f(x, y, z):
            print(x, y, z)

        f(2, 3, *(list(range(10)) + []))
    """)

    assert result == expected


# Generated at 2022-06-14 02:19:35.099195
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from typed_ast import ast3 as ast

    node = ast.Call(
        func=ast.Name(id='print'),
        args=[ast.Starred(value=ast.Name(id='range'), ctx=ast.Load())],
        keywords=[])

    trans = StarredUnpackingTransformer()
    res = trans.visit(node)

    assert isinstance(res, ast.Call)
    assert len(res.args) == 1
    assert isinstance(res.args[0], ast.Starred)
    assert isinstance(res.args[0].value, ast.Call)
    assert isinstance(res.args[0].value.func, ast.Name)
    assert res.args[0].value.func.id == 'list'

# Generated at 2022-06-14 02:19:39.015485
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    src = """ls = [2, *range(10), 1]"""
    expected = """ls = [2] + list(range(10)) + [1]"""
    module, _ = StarredUnpackingTransformer().transform_ast(src)
    assert module == expected



# Generated at 2022-06-14 02:19:43.567760
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    transformer = StarredUnpackingTransformer()
    args = ast.parse('''\
[2, *range(10), 1]
''').body[0].value.elts
    args_new = transformer.visit(args)
    print(ast.dump(ast.List(elts=args_new)))


# Generated at 2022-06-14 02:19:56.022400
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer"""
    from treehugger.tree import build_module
    from treehugger.unparser import Unparser
    src = """
a = [1, 2, 3]
b = []
c = [4, 5, 6]
"""
    mod = build_module(src)
    supt = StarredUnpackingTransformer()

    supt.visit(mod)

    assert Unparser(mod).unparse() == """\
from treehugger.transform.starred_unpacking import *

a = [1, 2, 3]
b = []
c = [4, 5, 6]
"""
    assert not supt.tree_changed()

# Generated at 2022-06-14 02:20:06.587773
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    # Check that class StarredUnpackingTransformer is defined
    assert("StarredUnpackingTransformer" in globals()), "StarredUnpackingTransformer class should be defined"
    # Check the body of the class
    star_stmt = ast.parse("[2, *range(10), 1]").body[0]
    assert(isinstance(star_stmt, ast.Expr)), "star_stmt should be an expression statement"
    assert(isinstance(star_stmt.value, ast.List)), "star_stmt should contain a list"
    star_list = star_stmt.value
    assert(isinstance(star_list, ast.List)), "star_list should be an instance of ast.List"
    assert(len(star_list.elts) == 3), "star_list should contain three elements"
   

# Generated at 2022-06-14 02:20:11.287472
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    try:
        StarredUnpackingTransformer()
    except NameError as e:
        assert False, "Tests will fail unless you implement the constructor for StarredUnpackingTransformer"
    assert True

# Unit tests for method _has_starred in class StarredUnpackingTransformer

# Generated at 2022-06-14 02:20:18.642738
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import tree_compile
    code = "print(*[1], *[2, 3])"
    compiler = StarredUnpackingTransformer()
    tree = tree_compile(code)
    ast.fix_missing_locations(compiler.visit(tree))
    assert tree_compile(
        tree, mode='exec') == tree_compile("print(*(([1] + [2, 3])))", mode='exec')

# Generated at 2022-06-14 02:20:25.417662
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Tests the method visit_List of the class StarredUnpackingTransformer."""
    input_ = ast.parse("[2, *range(10), 1]").body[0].value
    output = StarredUnpackingTransformer().visit(input_)

# Generated at 2022-06-14 02:20:26.237659
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:20:40.520819
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from .tools import as_source
    from .tools import assert_equal_code
    from .tools import parse
    from .tools import unparse

    # [1, *a] => [1] + list(a)
    assert_equal_code(StarredUnpackingTransformer().visit(parse(as_source([1, *a]))),
        unparse(ast.parse(as_source('[1] + list(a)'))))

    # [1, *[2]] => [1] + list([2])
    assert_equal_code(StarredUnpackingTransformer().visit(parse(as_source([1, *[2]]))),
        unparse(ast.parse(as_source('[1] + list([2])'))))

    # [1, 2, *[3, 4]] => [1, 2]

# Generated at 2022-06-14 02:20:57.518240
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    x = StarredUnpackingTransformer()
    assert not x._has_starred([])
    assert x._has_starred([ast.Starred(value=None)])
    assert x._has_starred([ast.Starred(value=None), ast.Starred(value=None)])
    assert x._has_starred([ast.Name(id="a")])
    assert x._has_starred([ast.Name(id="a"), ast.Starred(value=5)])
    assert x._has_starred([ast.Name(id="a"), ast.Starred(value=5), ast.Starred(value=6)])
    assert x._has_starred([ast.Starred(value=None), ast.Name(id="a")])



# Generated at 2022-06-14 02:20:59.553660
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    assert StarredUnpackingTransformer().target == (3, 4)

# Generated at 2022-06-14 02:21:09.444281
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .utils import NodeTransformerTestCase
    from astor.code_gen import to_source
    from .fixtures import CALL_EXPRESSION

    source = '''
    print(*range(1), *range(3))
    '''
    compare = '''
    print(*(list(range(1)) + list(range(3))))
    '''
    call_exp = CALL_EXPRESSION.substitute(expect=compare, code=source)
    NodeTransformerTestCase.source_to_source(
        StarredUnpackingTransformer(), call_exp, 'test_StarredUnpackingTransformer_visit_Call')



# Generated at 2022-06-14 02:21:11.955517
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    print(StarredUnpackingTransformer)

# Generated at 2022-06-14 02:21:23.738786
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node_List = ast.List(
        elts=[
            ast.Num(n=2),
            ast.Starred(
                value=ast.Call(
                    func=ast.Name(id='range', ctx=ast.Load()),
                    args=[
                        ast.Num(n=10)
                    ],
                    keywords=[])),
            ast.Num(n=1)],
        ctx=ast.Load())

# Generated at 2022-06-14 02:21:33.319891
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for StarredUnpackingTransformer.visit_Call."""
    # Const args
    node_1 = ast.parse('print(1, 2, 3)')
    result = StarredUnpackingTransformer().visit(node_1)
    assert result == node_1

    # One starred
    node_2 = ast.parse('print(*range(10))')
    result = StarredUnpackingTransformer().visit(node_2)
    assert result.body[0].value.func.id == 'list'
    assert result.body[0].value.args[0].value.id == 'range'

    # Plain args, one starred
    node_3 = ast.parse('print(1, 2, *range(10), 3)')
    result = StarredUnpackingTransformer().visit(node_3)


# Generated at 2022-06-14 02:21:43.348429
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():

    # scenario: [2, *range(10), 1]
    a = gc.ast_and_type_from_str('[2, *range(10), 1]')
    t = StarredUnpackingTransformer()
    a = t.visit(a)
    assert gc.is_valid_type(a, 'typing.List[int]')
    assert gc.type_str(a) == '[2] + list(range(10)) + [1]'
    assert t.tree_changed

    # scenario: [2]
    a = gc.ast_and_type_from_str('[2]')
    t = StarredUnpackingTransformer()
    a = t.visit(a)
    assert gc.is_valid_type(a, 'typing.List[int]')

# Generated at 2022-06-14 02:21:50.585934
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    import astor

    program = 'print("Hello world!", end="\\n")'
    expected_result = 'print("Hello world!", end="\\n", *("Hello world!",))'

    program_ast = ast.parse(program)
    result_ast = StarredUnpackingTransformer().visit(program_ast)
    result = astor.to_source(result_ast)

    assert result == expected_result


# Generated at 2022-06-14 02:22:00.780130
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    node = ast.parse("[2, *range(10), 1]")
    transformer = StarredUnpackingTransformer()
    transformer.visit(node)

    assert isinstance(node.body[0].value, ast.BinOp)
    assert isinstance(node.body[0].value.left, ast.List)
    assert isinstance(node.body[0].value.op, ast.Add)
    assert node.body[0].value.left.elts == [ast.Num(n=2)]
    assert isinstance(node.body[0].value.right, ast.Call)
    assert isinstance(node.body[0].value.right.func, ast.Name)
    assert node.body[0].value.right.func.id == 'list'

# Generated at 2022-06-14 02:22:06.122208
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    source_code = 'print(*range(1), *range(3))'
    expected_source_code = 'print(*(list(range(1)) + list(range(3))))'

    node = ast.parse(source_code)
    StarredUnpackingTransformer().visit(node)
    assert ast.dump(node, annotate_fields=False) == expected_source_code


# Generated at 2022-06-14 02:22:28.750213
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
  class Node:
    def __init__(self, value=None):
      self.value = value
    def __add__(self, other):
      return Node(value=[self.value, other.value])
    def __repr__(self):
      return 'Node(value={})'.format(self.value)
  class List(Node):
    pass
  class Call(Node):
    pass
  class BinOp(Node):
    pass
  class Starred(Node):
    pass
  class Add(Node):
    pass
  class Name(Node):
    pass
  class NodeTransformer(Node):
    def visit(self, node):
      return getattr(self, 'visit_' + node.__class__.__name__)(node)

# Generated at 2022-06-14 02:22:38.839088
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    """Unit test for method visit_Call of class StarredUnpackingTransformer."""
    from ..macros import Macro
    from ..processor import Processor

    class StarredUnpackingTransformer_visit_Call_TestMacro(Macro):
        def run(self, tree) -> ast.AST:
            processor = Processor(
                tree,
                transformers=[StarredUnpackingTransformer()])
            return processor.visit_Call()
    
    t = StarredUnpackingTransformer_visit_Call_TestMacro()
    t.run()
    assert t._tree_changed == True
    assert t._tree == ast.parse("print(*list(range(10))+list(range(5)))")

# Generated at 2022-06-14 02:22:45.113419
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """Unit test for method visit_List of class StarredUnpackingTransformer"""
    from textwrap import dedent
    import astor
    from .utils import transform_and_compare

    src = dedent("""
        a = [2, *range(10), 1]
    """)
    expected = dedent("""
        a = [2] + list(range(10)) + [1]
    """)

    transform_and_compare(StarredUnpackingTransformer, src, expected)



# Generated at 2022-06-14 02:22:52.598818
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    """
    Test that visit_List when called with a list, it returns a list with the
    Starred object replaced by a sum of lists.
    """
    node = ast.List(elts=[ast.Constant(2), ast.Starred(value=ast.Call(func=ast.Name(id='range'), args=[ast.Constant(10)], keywords=[]), ctx=ast.Load()), ast.Constant(1)])
    result = StarredUnpackingTransformer().visit(node)
    expected_result = ast.List(elts=[ast.Constant(2), ast.Call(func=ast.Name(id='list'), args=[ast.Call(func=ast.Name(id='range'), args=[ast.Constant(10)], keywords=[])], keywords=[]), ast.Constant(1)])
   

# Generated at 2022-06-14 02:22:53.229329
# Unit test for method visit_Call of class StarredUnpackingTransformer

# Generated at 2022-06-14 02:23:08.129159
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from . import analyse_ast, parse

    tree = parse("print(*range(1), *range(3))")
    assert tree.body[0].value.args[0].value.elts[0].func.id == 'range'
    assert tree.body[0].value.args[1].value.elts[0].func.id == 'range'

    transformer = StarredUnpackingTransformer()
    transformer.visit(tree)

    assert transformer._tree_changed

    assert tree.body[0].value.args[0].func.id == 'list'
    assert tree.body[0].value.args[0].args[0].value.elts[0].func.id == 'range'

# Generated at 2022-06-14 02:23:16.040477
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = ("print(*range(2), 3, *range(3), 4)")


# Generated at 2022-06-14 02:23:30.594572
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from pyt.core import St
    from pyt.core import ast as astcore
    from pyt.transformation.starred_unpacking import StarredUnpackingTransformer
    source = """
        [2, *range(10), 1]
        """
    tree = St.parse(source, parser='cpython')
    nodes = tree.findall_by_type(ast.List)
    target = nodes[0]
    trans = StarredUnpackingTransformer()
    trans._visit_List(target)

# Generated at 2022-06-14 02:23:44.243216
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    node = ast.Call(func = ast.Name(id = "print"),
                    args = [ast.Starred(value = ast.Call(func = ast.Attribute(value = ast.Name(id = "range"),
                                                                       attr = "range", ctx = ast.Load()),
                                                          args = [ast.Num(n = 1)], keywords = []), ctx = ast.Load()),
                            ast.Starred(value = ast.Call(func = ast.Attribute(value = ast.Name(id = "range"),
                                                                       attr = "range", ctx = ast.Load()),
                                                          args = [ast.Num(n = 3)], keywords = []), ctx = ast.Load())],
                    keywords = [], starargs = None, kwargs = None)
    Starred

# Generated at 2022-06-14 02:23:53.743565
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from ..transformer import Transformer
    from ..unparser import Unparser

    transformer = Transformer()
    transformer.visitors.append(StarredUnpackingTransformer())

    unparser = Unparser(transformer)

    unparser("[2, *range(10), 1]")
    assert unparser._buffer == "[2] + list(range(10)) + [1]"

    unparser("[2,]")
    assert unparser._buffer == "[2,]"

    unparser("[*range(10), 1]")
    assert unparser._buffer == "list(range(10)) + [1]"

    unparser("[2, *range(10)]")
    assert unparser._buffer == "[2] + list(range(10))"

    

# Generated at 2022-06-14 02:24:21.096777
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    fixture = [
        (
            ast.parse("[2, *range(10), 1]"),
            "[2] + list(range(10)) + [1]"
        ),
        (
            ast.parse("[*range(1), *range(3)]"),
            "list(range(1)) + list(range(3))"
        ),
        (
            ast.parse("[*range(1), *range(3), *range(5)]"),
            "(list(range(1)) + list(range(3))) + list(range(5))"
        ),
    ]

    for tree, expected in fixture:
        got = ast.dump(StarredUnpackingTransformer().visit(tree))
        assert got == expected, (got, expected)


# Generated at 2022-06-14 02:24:26.272811
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .test_helpers import assert_equal_ast
    from .test_helpers import get_python_source

    source = get_python_source(StarredUnpackingTransformer)
    expected_source = get_python_source(StarredUnpackingTransformer, suffix='_expected')
    assert_equal_ast(StarredUnpackingTransformer, source, expected_source)


if __name__ == '__main__':
    import pytest
    pytest.main(args=[__file__])

# Generated at 2022-06-14 02:24:36.561275
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    from astor import to_source

    node = ast.parse(
        "[2, *range(10), 1]")
    expected = ast.parse(
        "[2] + list(range(10)) + [1]")
    result = StarredUnpackingTransformer().visit(node)
    assert to_source(expected) == to_source(result)

    node = ast.parse(
        "[2, *range(10), 1, [1, *range(3)]]")
    expected = ast.parse(
        "[2] + list(range(10)) + [1] + [list(range(3))]")
    result = StarredUnpackingTransformer().visit(node)
    assert to_source(expected) == to_source(result)


# Generated at 2022-06-14 02:24:49.116750
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    def compare(code, expected_code):
        tree = ast.parse(code)
        expected_tree = ast.parse(expected_code)
        transformer = StarredUnpackingTransformer()

        result = transformer.visit(tree)
        assert ast.dump(result) == ast.dump(expected_tree)

    compare("[*[1, 2, 3]]", "[1, 2, 3]")
    compare("[*[1, 2, 3], 1]", "[1, 2, 3] + [1]")
    compare("[1, *[1, 2, 3], 1]", "[1] + [1, 2, 3] + [1]")

# Generated at 2022-06-14 02:24:57.435601
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from genast import ast2
    from cnorm.parsing.declaration import Declaration
    from cnorm.parsing.declaration import DeclarationTransformer
    from kooc_class.class_transformer import ClassTransformer
    from kooc_array.array_transformer import ArrayTransformer
    from kooc_typedef.typedef_transformer import TypedefTransformer
    from kooc_enum.enum_transformer import EnumTransformer
    from kooc_enum.enum_value import EnumValue

    test_cases = [
    ]
    for test in test_cases:
        print(test)
        tree = ast.parse(test)
        tree = DeclarationTransformer().visit(tree)
        tree = ClassTransformer().visit(tree)
        tree = ArrayTransformer().visit(tree)
       

# Generated at 2022-06-14 02:25:03.507759
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    source = 'assert [a, b, c, d] == "abcd"'
    expect = 'assert [a, b, c, d] == "abcd"'
    NodeTransformerTestCase(StarredUnpackingTransformer, source, expect)

    source = 'assert [a, *b, c, d] == "abcd"'
    expect = 'assert [a] + list(b) + [c, d] == "abcd"'
    NodeTransformerTestCase(StarredUnpackingTransformer, source, expect)

    source = 'assert [a, b, *c, d] == "abcd"'
    expect = 'assert [a, b] + list(c) + [d] == "abcd"'
    NodeTransformerTestCase(StarredUnpackingTransformer, source, expect)


# Generated at 2022-06-14 02:25:10.310278
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    node = ast.Call(func=ast.Name(id='print'),
                    args=[ast.Starred(value=ast.Num(n=8))],
                    keywords=[])
    assert StarredUnpackingTransformer().visit(node) == ast.Call(
                        func=ast.Name(id='print'),
                        args=[ast.Starred(value=ast.List(elts=[ast.Num(n=8)]))],
                        keywords=[])

    node = ast.Call(func=ast.Name(id='print'),
                    args=[ast.Num(n=8), ast.Starred(value=ast.Num(n=9))],
                    keywords=[])

# Generated at 2022-06-14 02:25:22.257831
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    from .base import BaseNodeTransformer
    from typed_ast.ast3 import Call, List, Starred, Name, BinOp, Add
    node1 = List(elts=[1, Starred(value=Name(id='a', ctx=Load())), 3])
    node2 = Call(func=Name(id='print', ctx=Load()), 
                 args=[Starred(value=Name(id='a', ctx=Load()), ctx=Load()), 
                       Starred(value=Name(id='a', ctx=Load()), ctx=Load())])
    transformer = StarredUnpackingTransformer()
    result1 = transformer.visit(node1) 
    result2 = transformer.visit(node2)
    
    assert isinstance(result1, List)

# Generated at 2022-06-14 02:25:28.487068
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    code = "print(*range(1), *range(3))"
    from .. import compile_restricted
    from ast_compat_patched import parse
    tree = parse(code)
    expected = parse("""
print(*(list(range(1)) + list(range(3))))
""")
    result = StarredUnpackingTransformer().visit(tree)
    assert compile_restricted(expected, mode='exec') == compile_restricted(result, mode='exec')


# Generated at 2022-06-14 02:25:37.682993
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from .test_utils import assert_equal_ast
    code = """
print(*range(1), *range(3))
print(*[], 1)
""".strip()
    expected_code = """
print(*(list(range(1)) + list(range(3))))
print(*(list([]) + [1]))
""".strip()
    node = ast.parse(code)
    node = StarredUnpackingTransformer().visit(node)
    expected_node = ast.parse(expected_code)
    assert_equal_ast(node, expected_node)


# Generated at 2022-06-14 02:26:27.210606
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    transformer = StarredUnpackingTransformer()

# Generated at 2022-06-14 02:26:30.978689
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    trans = StarredUnpackingTransformer()
    assert trans.target == (3, 4)
    assert trans.is_tree_changed() == False
    assert str(trans.get_tree()) == ''


# Generated at 2022-06-14 02:26:36.077596
# Unit test for method visit_List of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_List():
    program = ast.parse(
        """
        [2, *range(10), 1]
    """)

    expected_program = ast.parse(
        """
        [2] + list(range(10)) + [1]
    """)

    assert expected_program == StarredUnpackingTransformer().visit(program)


# Generated at 2022-06-14 02:26:50.711629
# Unit test for method visit_Call of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer_visit_Call():
    from ..python_as_protobuf import PythonAsProtobuf
    from ..bazel_to_protobuf import BazelToProtobuf
    from google.protobuf.descriptor import ServiceDescriptor
    from google.protobuf.compiler.plugin_pb2 import CodeGeneratorResponse
    from ..protobuf_to_bazel import ProtobufToBazel
    import os

    proto_file_1 = os.path.join(os.path.dirname(__file__), 'test_01.proto')
    proto_name_1 = 'test_01.proto'
    proto_file_2 = os.path.join(os.path.dirname(__file__), 'test_02.proto')
    proto_name_2 = 'test_02.proto'

# Generated at 2022-06-14 02:26:57.838943
# Unit test for constructor of class StarredUnpackingTransformer
def test_StarredUnpackingTransformer():
    import astor
    from .literal_transformer import LiteralTransformer

    # test case
    source = """
spam = [1, *range(10), 2]
foo(1, *range(10), 2)
"""
    tree = ast.parse(source)
    tree = StarredUnpackingTransformer().visit(tree)
    program = astor.to_source(tree)
    print(program)

    # unittest
    tree = ast.parse(program)
    StarredUnpackingTransformer().visit(tree)
    # if StarredUnpackingTransformer is not idempotent, raise AssertionError
    LiteralTransformer().visit(tree) # if no SyntaxError, test success