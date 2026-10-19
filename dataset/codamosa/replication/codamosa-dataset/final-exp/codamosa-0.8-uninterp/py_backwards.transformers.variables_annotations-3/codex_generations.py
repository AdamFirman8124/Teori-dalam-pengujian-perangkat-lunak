

# Generated at 2022-06-14 02:28:01.782915
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("x: int\ny: str")
    tree_changed = VariablesAnnotationsTransformer.transform(tree)
    print(ast.dump(tree))
    assert tree_changed
    tree_new = ast.parse("x: int\nx = None")
    assert ast.dump(tree) == ast.dump(tree_new)

# Generated at 2022-06-14 02:28:09.814351
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Make write_print_to_file function available for tests
    from ..utils import write_print_to_file
    from .__test_utils__ import run_transformer_test

    # Simple test
    def test_VariablesAnnotationsTransformer_1(capsys):
        run_transformer_test(VariablesAnnotationsTransformer, capsys,
                             '''a: int = 10\nb: int''',
                             '''a = 10''')


if __name__ == '__main__':
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:28:17.847049
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10\nb: int\n')
    result = VariablesAnnotationsTransformer.transform(tree)
    expected_output = 'a = 10\n'
    expected_output_tree = ast.parse(expected_output)
    assert ast.dump(result.tree) == ast.dump(expected_output_tree)
    
# To run the unit test
# python -m unittest transformers.variables_annotations_transformer

# Generated at 2022-06-14 02:28:29.376379
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Creating node AnnAssign
    node = ast.AnnAssign(
        target = ast.Name(id = "x", ctx = ast.Store()),
        annotation = ast.Name(id = "int", ctx = ast.Load()),
        value = ast.Constant(value = 100),
        simple = 0
    )
    # Creating node Assign
    expected_node = ast.Assign(
        targets = [ast.Name(id = "x", ctx = ast.Store())],
        value = ast.Constant(value = 100),
        type_comment = ast.Name(id = "int", ctx = ast.Load())
    )
    # Creating node Module
    node_module = ast.Module(body = [node])
    expected_node_module = ast.Module(body = [expected_node])



# Generated at 2022-06-14 02:28:36.076927
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    #Tests on correct input
    tree=ast.parse('x:int = 5\na:int = 10')
    transformer = VariablesAnnotationsTransformer()
    str(transformer.node)
    tree1=TransformationResult(tree,True,[])
    assert tree1 == transformer.transform(tree)
    #Tests on wrong input
    tree=ast.parse('')
    transformer = VariablesAnnotationsTransformer()
    tree1=TransformationResult(tree,False,[])
    assert tree1 == transformer.transform(tree)

# Generated at 2022-06-14 02:28:37.959758
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print("In method 'test_VariablesAnnotationsTransformer'")
    # Arrange

# Generated at 2022-06-14 02:28:41.269967
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    instance = VariablesAnnotationsTransformer()
    assert instance.target == (3, 5)
    assert callable(instance.transform)



# Generated at 2022-06-14 02:28:53.282162
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()), annotation=ast.Name(id="int"), value=ast.Num(n=10), simple=1)
    b = ast.AnnAssign(target=ast.Name(id="b", ctx=ast.Store()), annotation=ast.Name(id="int"), value=None, simple=0)
    g = ast.Global(names=["c"])
    assign = ast.Assign(targets=[ast.Name(id="c", ctx=ast.Store())], value=ast.Num(n=5))

    tree = ast.Module(body=[a, b, g, assign])

# Generated at 2022-06-14 02:28:59.409836
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    with open('tests/samples/3_5/variables_annotations.py', 'r') as file:
        tree = ast.parse(file.read())
        tree = VariablesAnnotationsTransformer.transform(tree)

    assert test_ast(tree) == []
    assert get_sample('3_5/variables_annotations.py') in dump_python_source(tree)

# Generated at 2022-06-14 02:29:09.882888
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import ast
    from math import sin as _sin
    from typing import List, Union

    a = int(10)
    b = int
    with open('Tests/test_files/test_variable_annotations.py', 'r') as f:
        tree = ast.parse(f.read())
        tree = VariablesAnnotationsTransformer.transform(tree)

    treeComp = """\
a = int(10)
b = int
c: int = b
d: List[Union[int, str]] = [1, "a"]
e: int = 1 if True else 0
f: int = _sin(1)
g: int = a + 1
"""
    assert(str(tree.code) == treeComp)

# Generated at 2022-06-14 02:29:15.671762
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int")
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree_changed
    assert result.tree == ast.parse("a = 10\n")

# Generated at 2022-06-14 02:29:19.620199
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils import get_test_data

    VariablesAnnotationsTransformer.transform(get_test_data(__file__, 1)[0])


if __name__ == "__main__":
    test_VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:29:26.776725
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # The desired output
    output_tree = ast.parse(
        '''x = 30'''
    )
    output_tree_changed = True
    output_errors = []

    # The code to annotate
    input_code = '''x: int = 30'''
    input_tree = ast.parse(input_code)

    # The expected output
    expected_output = (output_tree, output_tree_changed, output_errors)

    # Assert the actual output equals the expected output
    assert(
        VariablesAnnotationsTransformer.transform(input_tree) == expected_output
    )

# Generated at 2022-06-14 02:29:31.669539
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    source = 'a: int = 10\nb: int'
    VARIABLES_ANNOTATIONS_TRANSFORMER = VariablesAnnotationsTransformer()
    result = VARIABLES_ANNOTATIONS_TRANSFORMER.transform(source)

    assert result.transformed == ['a = 10']

# Generated at 2022-06-14 02:29:36.911301
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
    def f(a,b,c):
        a: int = 10
        b: int
    """)

    expected = ast.parse("""
    def f(a,b,c):
        a = 10
    """)

    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree == expected

# Generated at 2022-06-14 02:29:39.085318
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_object = VariablesAnnotationsTransformer()
    assert class_object.target == (3, 5)



# Generated at 2022-06-14 02:29:48.814127
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Arrange
    # Create instance of class VariablesAnnotationsTransformer
    instance = VariablesAnnotationsTransformer()

    # Act
    # Transforms the following code:
    # x: int = 10
    # y: int
    # To:
    # x = 10
    # y = None
    tree_actual = ast.parse('x: int = 10\ny: int')
    instance.transform(tree_actual)

    # Assert
    # The correct transformed code is:
    # x = 10
    # y = None
    tree_expected = ast.parse('x = 10\ny = None')
    assert ast.dump(tree_actual, include_attributes=False) == ast.dump(
        tree_expected, include_attributes=False)
    # There has been a change in the AST
    assert instance.script

# Generated at 2022-06-14 02:29:52.904182
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = "a: int = 10"
    tree = ast.parse(code)
    res = VariablesAnnotationsTransformer.transform(tree)
    expected = "a = 10"
    assert astunparse.unparse(res.tree) == expected



# Generated at 2022-06-14 02:29:57.065946
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    input = \
"""def func():
    a: int = 10
    b: int
"""
    expected = \
"""def func():
    a = 10
"""
    tree = ast.parse(input)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert result.tree.body[0].body == [ast.parse(expected).body[0].body[0]]

# Generated at 2022-06-14 02:30:06.156911
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.testing import get_test_cases
    from ..utils.tree import tree_to_str
    from .base import BaseTest

    test_cases = get_test_cases(__file__, 'VariablesAnnotationsTransformer')

    for test_case in test_cases:  # type: BaseTest
        transformer = VariablesAnnotationsTransformer(test_case)
        result = transformer.result

        assert tree_to_str(result.tree) == test_case.expected
        assert result.tree_changed == test_case.tree_changed
        assert result.errors == test_case.expected_errors

# Generated at 2022-06-14 02:30:15.674509
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""from typing import List, Dict\n\n"""
                     """a: List[int] = [1,2,3]\n"""
                     """b: Dict[str, int] = {"asdf": 1, "zxcv": 2}\n""")
    VariablesAnnotationsTransformer.transform(tree)
    code = compile(tree, '<test>', mode='exec')
    exec(code)
    assert a == [1,2,3]
    assert b == {'asdf':1, 'zxcv':2}

# Generated at 2022-06-14 02:30:23.034604
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    exec('''
if __name__ == '__main__':
    a: int = 10
    b: int
''') in globals(), locals()
    ast_tree = ast.parse('''
if __name__ == '__main__':
    a: int = 10
    b: int
''')
    result = VariablesAnnotationsTransformer.transform(ast_tree)
    exec(compile(result.tree, filename="", mode="exec")) in globals(), locals()
    assert result.tree_changed == True
    assert result.errors == []


# Generated at 2022-06-14 02:30:24.053678
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:33.458509
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test_class = VariablesAnnotationsTransformer()
    test_tree_1 = ast.parse("x: int = 10")
    test_tree_1_answer = ast.parse("x = 10")
    test_result_1 = test_class.transform(test_tree_1)[0]
    assert ast.dump(test_result_1) == ast.dump(test_tree_1_answer)
    test_tree_2 = ast.parse("y: int")
    test_tree_2_answer = ast.parse("pass")
    test_result_2 = test_class.transform(test_tree_2)[0]
    assert ast.dump(test_result_2) == ast.dump(test_tree_2_answer)

# Generated at 2022-06-14 02:30:38.414819
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse("a:int=10")) == \
        TransformationResult(tree=ast.parse("a=10"), tree_changed = True, logs = [])

    # Test warning
    assert VariablesAnnotationsTransformer.transform(ast.parse(""""print("Hello")\n a:int=10""")) == \
        TransformationResult(tree=ast.parse(""""print("Hello")\n a=10"""), tree_changed = True, logs = [])

# Generated at 2022-06-14 02:30:46.410240
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import build_ast
    # a: int = 10
    # b: int
    result = VariablesAnnotationsTransformer.transform(build_ast('a: int = 10\nb: int'))

    assert isinstance(result.tree, ast.Module)
    assert len(result.tree.body) == 1
    assert isinstance(result.tree.body[0], ast.Assign)
    assert isinstance(result.tree.body[0].value, ast.Num)
    assert result.tree.body[0].value.n == 10

# Generated at 2022-06-14 02:30:51.307068
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = '''def f():
        a: str = 'hello'
        b: int
    '''
    expected = 'def f():\n\ta = \'hello\'\n'

    t = VariablesAnnotationsTransformer()
    t = t.transform_string(code)
    assert t == expected

# Generated at 2022-06-14 02:30:51.904995
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass

# Generated at 2022-06-14 02:30:56.593582
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = VariablesAnnotationsTransformer()
    assert a.transform(ast.AnnAssign(target=ast.Name(id='a',
                                                    ctx=ast.Store()),
                                     annotation=ast.Name(id='var',
                                                         ctx=ast.Load()),
                                     value=ast.Name(id='b', ctx=ast.Store()))) == TransformationResult(None, True, [])

# Generated at 2022-06-14 02:31:06.105586
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:31:20.526471
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .utils import assert_equal_ast
    from typed_ast import ast3 as ast
    print("Test for VariablesAnnotationsTransformer")
    print("Tests for class VariablesAnnotationsTransformer\n")
    node = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()), annotation=ast.Name(id="int", ctx=ast.Load()),
                         value=ast.Name(id="10", ctx=ast.Load()))
    tree = ast.parse("a: int = 10")
    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert_equal_ast(result[0], node)
    print("Test 1: Passed")

# Generated at 2022-06-14 02:31:23.568689
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_object = VariablesAnnotationsTransformer()
    print(class_object)
    assert(isinstance(class_object, VariablesAnnotationsTransformer))



# Generated at 2022-06-14 02:31:26.196523
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse('a: int = 10')) == (ast.parse('a = 10'), True)

# Generated at 2022-06-14 02:31:38.573280
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    source1 = 'a: int = 10\nb: int'
    source2 = 'from typing import List\nnew_list: List[int] = [1, 2, 3]'
    source3 = 'from typing import Dict\nnew_dict: Dict[str, int] = {"a": 1, "b": 2}'

    result1 = 'a = 10'
    result2 = 'from typing import List\nnew_list = [1, 2, 3]'
    result3 = 'from typing import Dict\nnew_dict = {"a": 1, "b": 2}'

    assert VariablesAnnotationsTransformer.transform(parse(source1))[0] == result1
    assert VariablesAnnotationsTransformer.transform(parse(source2))[0] == result2

# Generated at 2022-06-14 02:31:46.603688
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = ast.parse('class Hello: \
    def __init__(self,test: int,test2): \
        self.test = test \
        self.test2 = test2 \
        string:str = "hello"\
        self.test3:str = "world"\
    def test(self):\
        var:str = "ho"\
        var2:int = 1\
        var3 = 3')
    new_code = VariablesAnnotationsTransformer.transform(code)
    result = ast.dump(new_code[0])

# Generated at 2022-06-14 02:31:54.612685
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = \
"""
a: float = 10.3
"""
    expected = \
"""
a = 10.3
"""
    # Printing tree before
    print("Input: [{}]".format(tree))

    # Convert to ast
    tree = ast.parse(tree)

    # Transform
    result = VariablesAnnotationsTransformer.transform(tree)

    # Convert to string
    result = astor.to_source(result.tree).strip()

    # Printing tree after
    print("Output: [{}]".format(result))

    # Assert
    assert result == expected

# Generated at 2022-06-14 02:31:56.754655
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert (isinstance(VariablesAnnotationsTransformer(), BaseTransformer)) == True


# Generated at 2022-06-14 02:32:01.186271
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert len(VariablesAnnotationsTransformer.transform(ast.parse("a: int = 10")).tree.body) == 1

# testcase for find function of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:32:09.074662
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .base import BaseTransformer
    from .context import Context

    test_ctx = Context(3, 5)

    id = BaseTransformer.transform(VariablesAnnotationsTransformer,
                                   test_ctx)

    assert hasattr(id, 'transform')
    assert hasattr(id, 'target')
    assert hasattr(id, 'context')

    assert id.context == test_ctx
    assert id.target == (3, 5)
    assert callable(id.transform)


# Generated at 2022-06-14 02:32:09.761615
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass

# Generated at 2022-06-14 02:32:16.651009
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Tests if the class can be initialized
    try:
        VariablesAnnotationsTransformer()
    except:
        assert False

# Generated at 2022-06-14 02:32:24.094188
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a : int = 10
    b : int
    class DummyClass():
        def __init__(self):
            self.b = b
            self.a = a
    f = DummyClass()
    x = f.b
    y = f.a
# expected
    class DummyClass():
        def __init__(self):
            self.a = 10
            self.b = None
    f = DummyClass()
    x = f.b
    y = f.a



# Generated at 2022-06-14 02:32:33.858448
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    test1 = ast.AnnAssign(target=ast.Name(id='b', ctx=ast.Store()), annotation=ast.Name(id='int'), value=None)
    test2 = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()), annotation=ast.Name(id='int'), value=ast.Num(n=10))
    test3 = ast.AnnAssign(target=ast.Name(id='c', ctx=ast.Store()), annotation=ast.Name(id='str'), value=ast.Str(s='foo'))

# Generated at 2022-06-14 02:32:39.952992
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = parse_and_clean('''
    import typing
    a: typing.List[typing.List[int]] = []
    a.append([1, 2, 3])
    b: int = a[0][1]
    ''')
    new_tree = VariablesAnnotationsTransformer.transform(tree)
    assert isinstance(new_tree.tree, ast.Module)
    assert not new_tree.changed
    assert len(new_tree.diagnostics) == 0
    assert new_tree.tree.body[0].lineno == 1
    assert new_tree.tree.body[0].col_offset == 0
    assert new_tree.tree.body[0].end_lineno == 1
    assert new_tree.tree.body[0].end_col_offset == 14
    assert new_tree.tree

# Generated at 2022-06-14 02:32:40.452297
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert False

# Generated at 2022-06-14 02:32:42.645968
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test tree structure
    tree = ast.parse('a: int = 10')

    # Check if class constructor works correctly
    assert VariablesAnnotationsTransformer.transform(tree).tree_changed == True

# Generated at 2022-06-14 02:32:46.465943
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('a: int = 10\nb: int')
    transformed = VariablesAnnotationsTransformer.transform(tree)
    assert transformed.tree.body[0]._fields == ('target', 'value')

# Generated at 2022-06-14 02:32:54.171076
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.syntax_tool import parse
    from .test_base import TestBase
    from ..utils.helpers import assertDeepAlmostEqual

    # NOTE: This test will only work with Python 3.5+
    source = '''
        a: int = 10
        b: int
    '''
    expected = '''
        a = 10
    '''
    tree = parse(source)
    t = VariablesAnnotationsTransformer()
    result = t.transform(tree)
    assertDeepAlmostEqual(result.tree, expected)


# Unit test 2 for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:04.613824
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..utils.context import Context
    from ..main import run_transformer_class
    from ..utils.helpers import get_ast, dump_python_source

    code = '''
from typing import List, Tuple

a: int
b: List[str]
c: Tuple[int, str]
d: int = 10
    '''
    tree = get_ast(code)
    new_tree = run_transformer_class(tree, Context(), VariablesAnnotationsTransformer)
    assert dump_python_source(new_tree) == dump_python_source(get_ast('''
from typing import List, Tuple

a = 10
b = []
c = (10, '')
d = 10
    '''))

# Generated at 2022-06-14 02:33:10.986845
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Format: transformer, input, expected
    tests = [
        (VariablesAnnotationsTransformer,
         '''a = 10
            b: int = 10
            c: int
            ''',
         '''a = 10
            b = 10
            c = None
            ''')
    ]
    for f, inp, expected in tests:
        test_input = ast.parse(inp)
        actual = f.transform(test_input).tree
        expected = ast.parse(expected)
        assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 02:33:30.228386
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from copy import deepcopy
    from typed_ast import ast3 as ast
    from .base import BaseTransformerTest
    from .variables import VariableTransformer
    import textwrap
    import unittest

    class TestVariablesAnnotationsTransformer(BaseTransformerTest):
        def test_simple_annotations(self):
            code = textwrap.dedent(
                """\
                a: int = 10
                b: int
                """
            )

            try:
                tree = ast.parse(code)
            except Exception as e:
                self.fail(e)
            tree = deepcopy(tree)

            result: TransformationResult = VariablesAnnotationsTransformer.transform(tree)
            self.assertTrue(result.tree_changed)
            self.assertIsInstance(result.tree, ast.Module)


# Generated at 2022-06-14 02:33:41.567374
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
  stmts = [
    ast.AnnAssign(target = ast.Name(id = 'a', ctx = ast.Store(), annotation = ast.Name(id = 'int', ctx = ast.Load())),
              annotation = None, value = ast.Num(n = 10), simple = 1),
    ast.AnnAssign(
      target=ast.Name(id='b', ctx=ast.Store(), annotation=ast.Name(id='int', ctx=ast.Load())),
      annotation=None, value=None, simple=1)
  ]

# Generated at 2022-06-14 02:33:45.149826
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    with open('tests/fixtures/example_code.py') as f:
        tree = ast.parse(f.read())

    c = VariablesAnnotationsTransformer()
    res = c.transform(tree)
    assert(res.tree_changed == True)
    assert(res.warnings == [])

# Generated at 2022-06-14 02:33:45.977568
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:52.301963
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astunparse, astor
    input_code = "a: int = 10"
    tree = ast.parse(input_code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    print(ast.dump(tree))
    return_code = astunparse.unparse(tree)
    print(astor.to_source(tree))
    return return_code

# Generated at 2022-06-14 02:33:55.556299
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # initialization
    instance = VariablesAnnotationsTransformer()
    assert isinstance(instance, VariablesAnnotationsTransformer)
    assert instance.target == (3, 5)


# Generated at 2022-06-14 02:33:57.512239
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(
        ast.parse("a: int = 10\nb: int"))

# Generated at 2022-06-14 02:34:00.110622
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import typed_ast.ast3 as ast
    from ..utils.tree import inline_comments

# Generated at 2022-06-14 02:34:05.380432
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    node = ast.parse('''
        a: int = 10
        b: int
    ''', mode='exec')

    tree_changed, _, _ = VariablesAnnotationsTransformer.transform(node)
    assert tree_changed is True



# Generated at 2022-06-14 02:34:16.162399
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import test_VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer
    from .variables_annotations_transformer import VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:34:40.012467
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
        a: int = 10
        b: int
        """)

    t = VariablesAnnotationsTransformer()
    assert t.transform(tree)

# Generated at 2022-06-14 02:34:42.289347
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t = VariablesAnnotationsTransformer()
    assert isinstance(t, BaseTransformer)
    assert getattr(t, "target") == (3, 5)



# Generated at 2022-06-14 02:34:45.995003
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Constructor
    assert VariablesAnnotationsTransformer.__bases__[0] == BaseTransformer
    # Method .transform()
    VariablesAnnotationsTransformer.transform(ast.AST())

# --------------------------
# Unit tests for VariablesAnnotationsTransformer
# --------------------------

# Test 1:
# Test the class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:34:51.607793
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    #####TEST 1#####
    tree = ast.parse('''
        a: int = 10
        b: int
        c = 20
    ''')

    expected_tree = ast.parse('''
        a = 10
        b
        c = 20
    ''')
    actual_tree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(expected_tree) == ast.dump(actual_tree.tree)

    #####TEST 2#####
    tree = ast.parse('''
        a: int
    ''')

    expected_tree = ast.parse('''
        a
    ''')
    actual_tree = VariablesAnnotationsTransformer.transform(tree)
    assert ast.dump(expected_tree) == ast.dump(actual_tree.tree)

    #####T

# Generated at 2022-06-14 02:34:57.897267
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import Fake
    constructor_test = VariablesAnnotationsTransformer()
    assert constructor_test.target == (3, 5)

    # Unit test for method transform of class VariablesAnnotationsTransformer
    transform_test = VariablesAnnotationsTransformer()
    tree = ast.parse('''a: int = 10\nb: int''')
    result = transform_test.transform(tree)
    assert result.tree_changed == True

# Generated at 2022-06-14 02:35:08.399695
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from . import variablesAnnotationsTransformer as v
    from typed_ast import ast3 as ast

    vTest = v.VariablesAnnotationsTransformer()
    testNode = ast.AnnAssign(target=ast.Name(id='x'), annotation=ast.parse('int'), value=ast.parse('10'))
    testNode2 = ast.AnnAssign(target=ast.Name(id='y'), annotation=ast.parse('str'))

    vTest.visit(testNode)
    print('The transformed Tree is: ')
    print(vTest.tree)
    print('=========================================================================================')
    vTest.visit(testNode2)
    print('The transformed Tree is: ')
    print(vTest.tree)

# Generated at 2022-06-14 02:35:17.250118
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import parse
    from .test_utils import should_transform_equal
    should_transform_equal(VariablesAnnotationsTransformer,
                           parse("a: int = 10"),
                           (parse("a = 10"), True))
    should_transform_equal(VariablesAnnotationsTransformer,
                           parse("b: int = 10 = 20"),
                           (parse("b = 10 = 20"), True))

    should_transform_equal(VariablesAnnotationsTransformer,
                           parse("a: int = 10\nb: int = 20"),
                           (parse("a = 10\nb = 20"), True))

# Generated at 2022-06-14 02:35:19.288591
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:35:20.743214
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    pass


# Generated at 2022-06-14 02:35:22.130752
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:36:10.236118
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:36:11.475748
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:36:22.908036
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..ast_transformer import get_code
    code = get_code(VariablesAnnotationsTransformer)
    assert 'def test_VariablesAnnotationsTransformer():' in code
    assert 'from ..utils.tree import find, get_non_exp_parent_and_index, insert_at' in code
    assert 'from ..utils.helpers import warn' in code
    assert 'from ..types import TransformationResult' in code
    assert 'from ..exceptions import NodeNotFound' in code
    assert 'from .base import BaseTransformer' in code
    assert 'class VariablesAnnotationsTransformer(BaseTransformer):' in code
    assert r'''    target = (3, 5)''' in code
    assert r'''    @classmethod''' in code

# Generated at 2022-06-14 02:36:25.791996
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    transformer = VariablesAnnotationsTransformer()
    # Check that the target version is set correctly
    assert transformer.target == (3, 5)

# Unit tests for transform method of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:36:27.467062
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    vat = VariablesAnnotationsTransformer()
    assert vat.target == (3,5)


# Generated at 2022-06-14 02:36:29.897128
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
    a: int = 10
    b: int
    """
    result = VariablesAnnotationsTransformer.run_from_text(code)
    assert result.tree.body[0].value.n == 10

# Generated at 2022-06-14 02:36:35.800433
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.test_visitor import TestVisitor

    tree = ast.parse('''\
        from a.b import c, d as e
        from .f import g, h as i
        from i import j, k as l
        f: int = 10
        g: int''')
    exp_tree = ast.parse('''\
        from a.b import c, d as e
        from .f import g, h as i
        from i import j, k as l
        f = 10''')

    TestVisitor(tree, exp_tree, VariablesAnnotationsTransformer)



# Generated at 2022-06-14 02:36:44.212311
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Test that VariablesAnnotationsTransformer can transform this input into expected output."""
    from ..utils import get_ast, get_code

    src = get_code('''
        a: int = 10
        b: int
    ''')

    exp = get_code('''
        a = 10
    ''')
    tree = get_ast(src)
    result = VariablesAnnotationsTransformer.transform(tree)
    result.assert_matches(exp)


# Generated at 2022-06-14 02:36:55.445619
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():

    v = VariablesAnnotationsTransformer()
    test_tree = ast.parse('a:int = 10')
    test_result = v.transform(test_tree)

    assert test_result.tree_changed == True
    assert len(test_result.errors) == 0
    assert len(test_result.tree.body) == 1
    assert test_result.tree.body[0].__class__.__name__ == 'Assign'
    assert len(test_result.tree.body[0].targets) == 1
    assert test_result.tree.body[0].targets[0].__class__.__name__ == 'Name'
    assert test_result.tree.body[0].targets[0].id == 'a'

# Generated at 2022-06-14 02:37:03.711027
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = "a: int = 10"  # code is a string
    tree = ast.parse(code)  # create an abstract syntax tree
    res = VariablesAnnotationsTransformer.transform(tree)  # run the transformation
    assert res.tree_changed == True  # assert tree changed
    expected_code = "a = 10"
    compiled = compile(res.tree, '<test>', 'exec')  # compile the tree
    actual_code = "".join(line.strip() for line in (inspect.getsourcelines(compiled) or [''])[0]).strip() # extract the code for testing
    assert actual_code == expected_code