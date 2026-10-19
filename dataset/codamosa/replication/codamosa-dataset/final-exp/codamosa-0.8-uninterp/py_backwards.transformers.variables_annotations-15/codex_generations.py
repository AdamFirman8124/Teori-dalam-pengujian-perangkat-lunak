

# Generated at 2022-06-14 02:27:58.969594
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astunparse
    from .. import transformers
    from ..transforms import VariablesAnnotationsTransformer
    from ..__pkginfo__ import version as bocadillo_version

    code = """
a: int = 10
b: int
"""
    tree = ast.parse(code)
    result = VariablesAnnotationsTransformer.transform(tree)
    assert astunparse.unparse(result.tree).strip() == 'a = 10'

    tree = ast.parse('b: int = 42')
    result = VariablesAnnotationsTransformer.transform(tree)
    assert astunparse.unparse(result.tree).strip() == 'b = 42'

    tree = ast.parse('b: int')
    result = VariablesAnnotationsTransformer.transform(tree)

# Generated at 2022-06-14 02:28:06.302318
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import parse

    # Defines an empty node
    node = ast.parse('a: int = 10\nb: int')

    # Asserts that the method transform of the above class is defined
    assert hasattr(VariablesAnnotationsTransformer, 'transform')

    # Asserts that the method transform of the above class returns a
    # TransformationResult object with the expected values
    assert VariablesAnnotationsTransformer.transform(node) == \
        TransformationResult(parse('a = 10\nb'), True, [])



# Generated at 2022-06-14 02:28:15.926743
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from ..interfaces import Transformation

    cls = VariablesAnnotationsTransformer
    assert issubclass(cls, Transformation)
    assert cls.target == (3, 5)

    empty_constructor = ast.Module()
    c = cls.transform(empty_constructor)
    assert c == TransformationResult(empty_constructor, False, [])

    tree = ast.Module(body=[ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Load()), annotation=ast.Name(id="int", ctx=ast.Load()), value=ast.Num(n=10), simple=1)])
    c = cls.transform(tree)

# Generated at 2022-06-14 02:28:23.720340
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from astunparse import unparse
    from ..utils.helpers import load_example_snippet

    snippet = load_example_snippet("variables_annotations.py")
    tree = ast.parse(snippet)
    new_tree, changed, errors = VariablesAnnotationsTransformer.transform(
        tree)
    assert(not errors)
    assert(changed)
    assert(unparse(new_tree) == "a = 10\nb = 1000\nc:\n\tpass\n")



# Generated at 2022-06-14 02:28:31.029592
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import unittest
    from typed_ast import ast3 as ast
    from ..transformations.base import BaseTransformer

    class TestVariablesAnnotationsTransformer(unittest.TestCase):
        def test_constructor(self):
            self.assertTrue(isinstance(VariablesAnnotationsTransformer(), BaseTransformer))
            self.assertTrue(isinstance(VariablesAnnotationsTransformer(), VariablesAnnotationsTransformer))

    # Executes:
    tester = TestVariablesAnnotationsTransformer()
    tester.test_constructor()

# Generated at 2022-06-14 02:28:37.673714
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    expected_output = '''def test():
        a = 10
        b = 1
        return a + b'''
    input_code = '''def test() -> int:
        a: int = 10
        b: int
        b = 1
        return a + b'''
    tree = ast.parse(input_code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    assert astor.to_source(tree).strip() == expected_output

# Generated at 2022-06-14 02:28:39.365548
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:28:44.734219
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.parse('''a: int = 10
                     b: int
                     ''')
    b = ast.parse('''a = 10
                     ''')
    c = VariablesAnnotationsTransformer.transform(a)
    assert c.tree == b

# Generated at 2022-06-14 02:28:54.944085
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""
    a: int = 10
    b: int
    """)

    expected_tree = ast.parse("""
    a = 10
    """)

    transformed_tree, tree_changed, file_changed =\
        VariablesAnnotationsTransformer.transform(tree)
    assert tree_changed == True
    assert file_changed == []
    assert ast.dump(transformed_tree) == ast.dump(expected_tree)

    tree = ast.parse("""
    def func():
      a: int = 10
      return a
    """)

    expected_tree = ast.parse("""
    def func():
      return 10
    """)

    transformed_tree, tree_changed, file_changed =\
        VariablesAnnotationsTransformer.transform(tree)
    assert tree_changed == True


# Generated at 2022-06-14 02:29:05.169030
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # test__doc__:
    expected = """Compiles:
        a: int = 10
        b: int
    To:
        a = 10
    """
    actual = VariablesAnnotationsTransformer.__doc__
    assert expected == actual
    # test__doc___:
    expected = """Compiles:
        a: int = 10
        b: int
    To:
        a = 10
    """
    actual = VariablesAnnotationsTransformer.transform.__doc__
    assert expected == actual
    # test_target__:
    expected = (3, 5)
    actual = VariablesAnnotationsTransformer.target
    assert expected == actual
    # test_transform__:
    expected = """Compiles:
        a: int = 10
        b: int
    To:
        a = 10
    """
    actual

# Generated at 2022-06-14 02:29:18.239941
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    x = ast.parse('a: int = 10\nb: int\nc = 20', mode='exec')
    x = VariablesAnnotationsTransformer.transform(x).value
    print(x.body[0])
    print(x.body[1])
    print(x.body[2])
    assert ast.dump(x.body[0]) == 'Assign(targets=[Name(id="a", ctx=Store())], value=Num(n=10), type_comment="int")'
    assert ast.dump(x.body[1]) == 'Pass()'
    assert ast.dump(x.body[2]) == 'Assign(targets=[Name(id="c", ctx=Store())], value=Num(n=20), type_comment=None)'

# Generated at 2022-06-14 02:29:24.502369
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .testing_utils import expect_unchanged
    from ..utils.source import source_to_tree

    tree_before = source_to_tree("""\
    a: int
    b: int = 10
    c: int
    """)
    tree_after = source_to_tree("""\
    a
    b = 10
    c
    """)
    expect_unchanged(
        VariablesAnnotationsTransformer,
        tree_before, tree_after,
    )

# Generated at 2022-06-14 02:29:31.936174
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """
a: int = 10
b: int
"""
    tree = ast3.parse(code)
    tree_new = VariablesAnnotationsTransformer.transform(tree)
    assert(ast3.dump(tree_new.tree) == 'Module(body=[Assign(targets=[Name(id=\'a\', ctx=Store())], value=Num(n=10), type_comment=Name(id=\'int\', ctx=Load()))])')

# Generated at 2022-06-14 02:29:40.074988
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import inspect
    import os
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    test_file = os.path.join(script_dir, "test_files/variables_annotations_test.py")
    with open(test_file, "r") as file:
        data = file.read()
    code = ast.parse(data)
    VariablesAnnotationsTransformer.transform(code)
    assert len(code.body) == 7
    assert len(code.body[0].body) == 1

# Generated at 2022-06-14 02:29:44.044232
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Initializing VariablesAnnotationsTransformer
    abc = VariablesAnnotationsTransformer()

    # Checking its type
    assert isinstance(abc, VariablesAnnotationsTransformer)

    # Checking its parent class
    assert isinstance(abc, BaseTransformer)


# Generated at 2022-06-14 02:29:51.206328
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse('''
# a: int = 10
# b: int
#
# def f():
#     a: str = 10
#     b: str
#     c: str = 20
#     return a + b + c
    '''
    )

    res = VariablesAnnotationsTransformer().transform(tree)
    res = ast.dump(res.tree)
    print(res)

    # TODO: better test

# Generated at 2022-06-14 02:29:51.967354
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'

# Generated at 2022-06-14 02:29:57.407263
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer(): # pragma: no cover
    class TestVariablesAnnotationsTransformer(VariablesAnnotationsTransformer):
        pass

    # checking basic attributes of class
    assert TestVariablesAnnotationsTransformer.target == (3, 5)
    assert isinstance(TestVariablesAnnotationsTransformer.tree_type, ast.AST)

    test_instance = TestVariablesAnnotationsTransformer()
    assert isinstance(test_instance, VariablesAnnotationsTransformer)


# Generated at 2022-06-14 02:30:00.409626
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    new_VariableAnnotationsTransformer = VariablesAnnotationsTransformer("3.5")
    assert new_VariableAnnotationsTransformer.target == (3,5)

# Generated at 2022-06-14 02:30:13.040738
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3
    from ..utils.tree import cst_to_ast
    from .class_def_transformer import ClassDefTransformer
    from .decorators_transformer import DecoratorsTransformer
    from .function_def_transformer import FunctionDefTransformer
    from .if_transformer import IfTransformer
    from ..utils.helpers import ast_to_source_code
    from ..utils.helpers import ast_to_cst
    import ast as py_ast

    # a: int = 10
    node = ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                         annotation=ast.Name(id='int', ctx=ast.Load()),
                         value=ast.Num(n=10), simple=1)

    assert ast_to_c

# Generated at 2022-06-14 02:30:17.289232
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    my_class = VariablesAnnotationsTransformer()
    assert my_class.target == (3, 5)

# Generated at 2022-06-14 02:30:19.551182
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test the constructor
    try:
        VariablesAnnotationsTransformer()
    except NameError:
        raise AssertionError()


# Generated at 2022-06-14 02:30:22.709702
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    """Unit test for constructor of class VariablesAnnotationsTransformer"""
    class_object = VariablesAnnotationsTransformer()

    assert class_object.target == (3, 5)


# Generated at 2022-06-14 02:30:29.147885
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:30:33.319836
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import assert_transformation

    assert_transformation(VariablesAnnotationsTransformer,
"""
import typing
x: typing.List[int] = []
y: 'A' = 10 # type: ignore
z: int
""",
"""
import typing
x = []
y = 10
""")

# Generated at 2022-06-14 02:30:34.168032
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor


# Generated at 2022-06-14 02:30:41.532984
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code: str = '''
        import org.foo as foo
        import org.bar as bar

        class A(foo.Foo, bar.Bar):

            a: int
            b: int = 10

            def f1(self, a: int) -> int:
                b: int = 10

                try:
                    return 20
                except:
                    return 30
    '''
    tree = ast3.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree)
    assert isinstance(tree, TransformationResult)


# Generated at 2022-06-14 02:30:52.282907
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..samples import VARIABLES_ANNOTATIONS_TEST
    from ..utils import prettify

    tree = VARIABLES_ANNOTATIONS_TEST

    VariablesAnnotationsTransformer.apply_on_tree(tree)
    assert prettify(tree) == '''
    def test() -> None:
        a = 10
        b
        return None
    '''

    # test empty function
    tree = ast.parse('def test(): pass')

    VariablesAnnotationsTransformer.apply_on_tree(tree)
    assert prettify(tree) == '''
    def test():
        pass
    '''

# Generated at 2022-06-14 02:30:53.220077
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..compiler import compile_string


# Generated at 2022-06-14 02:30:58.194095
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import parser
    import typed_astunparse

    tree = parser.parse("a: int = 10")
    tree = VariablesAnnotationsTransformer.transform(tree)
    assert typed_astunparse.unparse(tree.node) == "a = 10"

# Generated at 2022-06-14 02:31:09.914110
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import get_node_name
    from ..utils.tree import ASTHelper, ast_to_str

    tree = ASTHelper(3).parse("a: int = 10\nb: int")
    tree_str = ast_to_str(tree)

    assert tree_str == "Module(body=[AnnAssign(target=Name(id='a', ctx=Store()), annotation=Name(id='int', ctx=Load()), value=Num(n=10), type_comment=None), AnnAssign(target=Name(id='b', ctx=Store()), annotation=Name(id='int', ctx=Load()), value=None, type_comment=None)])"
    node = get_node_name(tree, "AnnAssign")
    assert VariablesAnnotationsTransformer.transform(tree).tree_

# Generated at 2022-06-14 02:31:22.194852
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class TestVariablesAnnotationsTransformer(BaseTransformerTestCase):
        transformer = VariablesAnnotationsTransformer

        def test_remove_annotations(self):
            """Test to remove asg targets"""
            tree = ast.parse('a: int = 10')
            self.transformed_tree = self.transformer.transform(tree)
            self.assertEqual(len(self.transformed_tree.body), 1)
            self.assertEqual(self.transformed_tree.body[0].__class__, ast.Assign)


        def test_remove_annotations_multiple(self):
            """Test to remove asg targets"""
            tree = ast.parse('a: int = 10\nb: int = 20')
            self.transformed_tree = self.transformer.transform(tree)
            self.assertEqual

# Generated at 2022-06-14 02:31:26.870900
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.dummy_context import DummyContext as Context

    code = '''
    a: int = 10
    b: int
    '''

    res, _ = VariablesAnnotationsTransformer.transform(ast.parse(code))
    assert str(res) == '''
    a = 10
    '''

# Generated at 2022-06-14 02:31:28.097678
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    _ = VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:31:40.003219
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from .variable_annotation_to_type_comment import TransformNode
    node = ast.AnnAssign(target=ast.Name(id='b1', ctx=ast.Store()),
                         annotation=ast.Name(id='int', ctx=ast.Load()),
                         value=ast.Num(n=10.0), simple=0)
    node = TransformNode(node)
    assert node.targets[0].id == 'b1'
    assert node.value.n == 10.0
    assert node.type_comment == 'int'

# Generated at 2022-06-14 02:31:45.017373
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # sample tree
    t = ast.parse("a: int = 10")
    # test if the constructor is working
    assert VariablesAnnotationsTransformer(3, 5)
    # test if the default value of the constructor is working
    assert VariablesAnnotationsTransformer()


# Generated at 2022-06-14 02:31:56.474171
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.python_source_utils import compile_as_module
    from ..visitors.base import BaseVisitor
    import astor

    code = """a:int = 10"""
    module = compile_as_module(code, mode='exec')
    module_tree = ast.parse(code)
    result = VariablesAnnotationsTransformer.transform(module_tree)
    print(astor.to_source(result.tree))
    print(VariablesAnnotationsTransformer.transform(result.tree))
    assert BaseVisitor().visit(module).strip() == BaseVisitor().visit(result.tree).strip()

# Generated at 2022-06-14 02:32:09.482811
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    #local imports
    from ..utils.tree import dump
    from ..utils.helpers import compile_snippet
    #Create AST for a=2 and b=4
    tree1 = compile_snippet('a:int=2\nb:int=4','test')
    #Create AST for a=2 and b=4 with assignment outside of body
    tree2 = compile_snippet('a:int=2\n\nb:int=4','test')
    #Create typed AST expected after transformation

# Generated at 2022-06-14 02:32:11.349763
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    a = ast.parse('''
        a: int = 10
        b: int
    ''')
    VariablesAnnotationsTransformer.transform(a)

# Generated at 2022-06-14 02:32:14.122277
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    vat = VariablesAnnotationsTransformer()
    assert vat is not None


# Generated at 2022-06-14 02:32:26.446329
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    trans = VariablesAnnotationsTransformer()
    assert(trans.target == (3,5))
    assert(issubclass(VariablesAnnotationsTransformer, BaseTransformer))


# Generated at 2022-06-14 02:32:39.455388
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.tree import parse_tree
    from ..utils.helpers import evaluate_ast
    import sys
    modules = {'__main__': sys.modules[__name__]}
    variables = {}

    # test with statement "a: int = 10"
    tree = parse_tree("a: int = 10")

    variables['a'] = None

    tree = VariablesAnnotationsTransformer.transform(tree)

    assert evaluate_ast(tree, modules, variables) is None
    assert variables['a'] == 10

    # test with statement "b: int"
    tree = parse_tree("b: int")

    variables['b'] = None

    tree = VariablesAnnotationsTransformer.transform(tree)

    assert evaluate_ast(tree, modules, variables) is None
    assert variables['b'] is None

# Generated at 2022-06-14 02:32:40.854062
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Test 1.
    print("====== Test 1 ======")

# Generated at 2022-06-14 02:32:43.867376
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert isinstance(VariablesAnnotationsTransformer, BaseTransformer)
    assert VariablesAnnotationsTransformer.transform('') == TransformationResult('')

# Generated at 2022-06-14 02:32:47.954094
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    code = """a: int = 10\nb: int"""
    tree = ast.parse(code)
    result = VariablesAnnotationsTransformer.transform(tree)
    expected = ast.parse("""a = 10""")
    assert expected == result.tree

# Generated at 2022-06-14 02:32:49.953346
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform == VariablesAnnotationsTransformer.transform

# Generated at 2022-06-14 02:32:54.274180
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("""a:int=10""")
    transformer = VariablesAnnotationsTransformer()
    tree = transformer.transform(tree)
    assert(transformer.tree_changed is True)
    assert(isinstance(tree.body[0], ast.Assign))

# Generated at 2022-06-14 02:32:56.961110
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    print("Testing start")
    t = VariablesAnnotationsTransformer()
    assert (t.target == (3,5))
    print("Testing end")

# Generated at 2022-06-14 02:33:04.112228
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\nb: int\nc = [10, 20]")
    transformer = VariablesAnnotationsTransformer()
    transformer.transform(tree)
    assert isinstance(tree, ast.Module)
    assert isinstance(tree.body[0], ast.Assign)
    assert isinstance(tree.body[0].targets[0], ast.Name)
    assert isinstance(tree.body[0].value, ast.Num)
    assert isinstance(tree.body[1], ast.AnnAssign)
    assert isinstance(tree.body[1].target, ast.Name)
    assert tree.body[1].value is None
    assert isinstance(tree.body[1].annotation, ast.Name)
    assert isinstance(tree.body[2], ast.Assign)
   

# Generated at 2022-06-14 02:33:05.808045
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse('a: int = 10')) == TransformationResult(ast.parse('a = 10'), True, [])

# Generated at 2022-06-14 02:33:33.751985
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast

    class expected:
        body = [ast.Assign(
            targets=[ast.Name(id='a', ctx=ast.Store())],
            value=ast.Num(n=10),
            type_comment=None
        )]
        type_ignores = []

    tree = ast.parse(
        'a: int = 10'
    )
    result = VariablesAnnotationsTransformer.transform(tree)

    assert result.tree.body == expected.body
    assert result.type_ignores == expected.type_ignores
    assert result.tree_changed == True



# Generated at 2022-06-14 02:33:44.167144
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Can run tests with a command like: mypy --strict pegen/transformers/test_variables_annotations_transformer.py::test_VariablesAnnotationsTransformer
    from pegen.ast_compile import PythonAstCompiler
    from pegen.parser_generator import ParserGenerator
    from pegen.grammar_parser import GrammarParser, GrammarError

    g = GrammarParser(grammar_text=r"""
        start: a
        a: STRING
    """)
    ast_compiler = PythonAstCompiler(encoding="utf8")
    pg = ParserGenerator(g.rule2func, ast_compiler)
    parser = pg.build_parser()
    parser.parse("hello")
    ast_ = parser.ast

# Generated at 2022-06-14 02:33:50.708222
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    python_code = """
a: int = 10
b: int
    """
    expected_code = """
a = 10
b: int
    """
    tree = ast.parse(python_code)
    transformer = VariablesAnnotationsTransformer()
    result = transformer.transform(tree)
    assert expected_code == astunparse.unparse(result.tree)

# Generated at 2022-06-14 02:33:52.077651
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:53.298719
# Unit test for constructor of class VariablesAnnotationsTransformer

# Generated at 2022-06-14 02:33:55.566310
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
	cls = VariablesAnnotationsTransformer()
	assert cls.target == (3, 5)




# Generated at 2022-06-14 02:33:59.802131
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from ..utils.helpers import generate_code
    code = generate_code(lambda: dict(a=10))
    transformer = VariablesAnnotationsTransformer.get_transformer()
    transformer.transform_code(code)
    assert code == 'a=10'

# Generated at 2022-06-14 02:34:05.133112
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from astor.source_repr import dump_tree

    code = """
    a: int = 10
    b: int
    """

    expected = """
    a = 10
    """

    module = parse(code)
    result = VariablesAnnotationsTransformer.transform(module)

    print(dump_tree(result))
    assert expected == dump_tree(result)

# Generated at 2022-06-14 02:34:08.554232
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(
        ast.parse('x: int = 10')).changed

    assert not VariablesAnnotationsTransformer.transform(
        ast.parse('x: int')).changed

# Generated at 2022-06-14 02:34:13.538587
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.parse("a: int = 10\n"
                     "b: int\n")

    expected_tree = ast.parse("a = 10\n"
                              "")

    new_tree = VariablesAnnotationsTransformer.transform(tree).result_tree

    assert ast.dump(new_tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 02:34:56.531952
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:34:58.833768
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from astor import to_source
    from ..utils.helpers import parse_source

# Generated at 2022-06-14 02:35:09.335811
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    # Given
    class_definition = ast.FunctionDef(name='foo',
                                       args=ast.arguments(args=[],
                                                          defaults=[],
                                                          vararg=None,
                                                          kwonlyargs=[],
                                                          kw_defaults=[],
                                                          kwarg=None,
                                                          posonlyargs=[]),
                                       body=[ast.AnnAssign(target=ast.Name(id='a', ctx=ast.Store()),
                                                           annotation=ast.Name(id='str', ctx=ast.Load()),
                                                           value=ast.Constant(value='hello', kind=None),
                                                           simple=1)],
                                       decorator_list=[],
                                       returns=None)

    # When

# Generated at 2022-06-14 02:35:11.360539
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    class_obj = VariablesAnnotationsTransformer()
    assert(class_obj.target == (3, 5))

# Generated at 2022-06-14 02:35:22.308257
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3 as ast
    from typing import List
    ast1 = ast.AnnAssign(
        target=ast.Name(id='a', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=ast.Num(n=10),
        simple=1
    )
    ast2 = ast.AnnAssign(
        target=ast.Name(id='b', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        simple=1
    )

# Generated at 2022-06-14 02:35:24.468958
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'


# Generated at 2022-06-14 02:35:27.846712
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.transform(ast.parse("a:int=10\nb:int")).changed
    assert VariablesAnnotationsTransformer.transform(ast.parse("a:int=10")).changed

# Generated at 2022-06-14 02:35:37.023619
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast import ast3

    node = ast.AnnAssign(
        target=ast.Name(id='a', ctx=ast.Store()),
        annotation=ast.Name(id='int', ctx=ast.Load()),
        value=ast.Num(n=10),
        simple=1
    )
    parent = ast.FunctionDef(
        name='fun',
        args=ast.arguments(
            args=[],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[node],
        decorator_list=[],
        returns=None
    )


# Generated at 2022-06-14 02:35:43.611021
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    import astor
    from typed_ast import ast3 as ast

    code = astor.to_source(VariablesAnnotationsTransformer.transform(
        ast.parse('''
from typing import List

a: int = 10
b: List[int]
c: int = 0
d: int = 10
            '''
        ))[0])

    expected_code = '''
from typing import List
a = 10
b = List[int]
c = 0
d = 10'''

    assert code == expected_code

VariablesAnnotationsTransformer()

# Generated at 2022-06-14 02:35:49.227756
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    x = ast.parse('a: int = 10')
    print(VariablesAnnotationsTransformer.transform(x.body[0]).tree)
    x = ast.parse('b: int')
    print(VariablesAnnotationsTransformer.transform(x.body[0]).tree)
    x = ast.parse('a: int')
    print(VariablesAnnotationsTransformer.transform(x.body[0]).tree)

# Generated at 2022-06-14 02:37:29.878736
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .. import settings
    import ast
    import textwrap
    settings.INLINE_TYPES = False
    code = textwrap.dedent('''
    from typing import List, Dict, Optional
    x: int = 10
    y: List[int]
    z: List[int] = []
    t: Optional[int] = 5
    ''')
    tree = ast.parse(code)
    tree = VariablesAnnotationsTransformer.transform(tree).tree
    print(ast.unparse(tree))

# Generated at 2022-06-14 02:37:37.493884
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    t1 = ast.AnnAssign(target=ast.Name(id="a", ctx=ast.Store()), annotation=ast.Name(id="int", ctx=ast.Load()), value=ast.Num(n=10))
    t2 = ast.AnnAssign(target=ast.Name(id="b", ctx=ast.Store()), annotation=ast.Name(id="int", ctx=ast.Load()), value=None)
    tree = ast.Module(body=[t1, t2])
    tt = VariablesAnnotationsTransformer()
    transformed_tree = tt.transform(tree)
    print(ast.dump(transformed_tree))

# Generated at 2022-06-14 02:37:38.554285
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    assert VariablesAnnotationsTransformer.__name__ == 'VariablesAnnotationsTransformer'

# Generated at 2022-06-14 02:37:42.770433
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    tree = ast.AnnAssign(target=ast.Name('a', ast.Store()),
                         annotation=ast.Name('int', ast.Load()),
                         value=ast.Num(0))
    assert VariablesAnnotationsTransformer.transform(tree).tree == ast.Assign(targets=[ast.Name('a', ast.Store())], value=ast.Num(0))

# Generated at 2022-06-14 02:37:45.387773
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from .test_helpers import parse

    tree = parse("a: int = 10\nb: int")
    new_tree = VariablesAnnotationsTransformer.transform(tree)

    assert "a = 10\nb" == str(new_tree.tree).strip()

# Generated at 2022-06-14 02:37:50.904261
# Unit test for constructor of class VariablesAnnotationsTransformer
def test_VariablesAnnotationsTransformer():
    from typed_ast.ast3 import parse
    from typed_ast import ast3
    from ..utils.tree import find, get_non_exp_parent_and_index, insert_at
    from ..types import TransformationResult
    from ..exceptions import NodeNotFound
    from ..compiler import COMPILER_VERSION
    import sys

    code_text = """
    def func() -> None:
        a: int = 10
        b: int
    """
    tree = parse(code_text)

    assert COMPILER_VERSION == 3.5
    transformer = VariablesAnnotationsTransformer()
    transformation_result = transformer.transform(tree)
    assert transformation_result.tree_changed == True
    assert len(transformation_result.exceptions) == 0

    #Following code tests the functionality of VariablesAnnotationsTransformer