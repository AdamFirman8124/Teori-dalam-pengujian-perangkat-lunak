

# Generated at 2022-06-14 01:55:02.613134
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    from typed_ast import ast3 as ast

    transformer = Python2FutureTransformer()
    src = 'x = "foo"'
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = "foo"
    """
    tree = ast.parse(src)
    new_tree = transformer.visit(tree)
    result = astor.to_source(new_tree)
    assert result == expected

# Generated at 2022-06-14 01:55:07.504911
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Unit test for method visit_Module of class Python2FutureTransformer"""
    
    # Set up test data
    module = ast.parse('')
    
    # Construct argument dependencies
    
    # Perform the test
    pt = Python2FutureTransformer(())
    result = pt.visit_Module(module)
    
    # Verify the test result
    # TODO: assert the result

# Generated at 2022-06-14 01:55:15.053430
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """
    import x
    """
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    import x
    """
    tree = ast.parse(source)
    tree = Python2FutureTransformer().visit(tree)
    assert expected == tree_to_str(tree)



# Generated at 2022-06-14 01:55:24.136412
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node_orig = ast.parse('print(1)')
    node_trans = Python2FutureTransformer().visit(node_orig)
    code_orig = astor.to_source(node_orig)
    code_trans = astor.to_source(node_trans)
    assert code_orig == 'print(1)\n'
    assert code_trans == 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nprint(1)\n'

# Generated at 2022-06-14 01:55:31.899911
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from typing import List
    from ..utils.ast_helpers import get_body
    from ..utils.ast_helpers import get_body_str

    from . import BaseNodeTransformer
    from .python2future import Python2FutureTransformer
    from .tests.transformer_test_case import TransformerTestCase

    def create_init_ast(node) -> ast.Module:
        tree = ast.parse("", "", "exec")
        tree.body = node
        return tree

    class T(TransformerTestCase):
        transformer = Python2FutureTransformer
        expected = imports.get_body(future='__future__') # type: ignore
        
        def test_simple_module(self):
            tree = ast.parse("")

# Generated at 2022-06-14 01:55:36.447970
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source2ast
    from ..utils.snippet import ast2source
    from . import run_all_nodes
    #

# Generated at 2022-06-14 01:55:38.726158
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Arrange
    import astor
    from wily import utils

    target = (2, 7)

# Generated at 2022-06-14 01:55:39.766775
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:55:45.574791
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer(ast.parse, '', {})
    node = ast.Module(body=[])
    node_new = transformer.visit_Module(node)
    # Note: we corcate the list because the unit test uses a dummy
    # versions of imports where __future__ is replaced with the
    # string 'future'.
    assert node_new.body[:4] == imports.get_body(future='future')


# Generated at 2022-06-14 01:55:54.696159
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    @snippet
    def original_module(**kwargs):
        """This is a original module."""

    @snippet
    def expected_module(**kwargs):
        """This is a original module."""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

    expected = expected_module.get_ast(future='__future__')

    transformer = Python2FutureTransformer()
    actual = transformer.visit(original_module.get_ast())

    assert ast.dump(actual, include_attributes=True) == ast.dump(expected, include_attributes=True)

# Generated at 2022-06-14 01:55:58.853269
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    _transformer = Python2FutureTransformer()
    assert isinstance(_transformer, Python2FutureTransformer)


# Generated at 2022-06-14 01:56:04.219291
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Given
    from typed_ast.ast3 import parse
    from .mocks import MockNodeTransformer
    from textwrap import dedent
    node = parse(dedent("""
        def foo():
            pass

        def bar():
            pass
    """))
    # When
    transformer = Python2FutureTransformer(MockNodeTransformer())
    node = transformer.visit(node)
    # Then
    assert transformer._tree_changed
    assert transformer.generic_visit.called
    assert node.body[0].body[0].value.s == 'absolute_import'  # type: ignore
    assert node.body[0].body[1].value.s == 'division'  # type: ignore
    assert node.body[0].body[2].value.s == 'print_function'  # type: ignore

# Generated at 2022-06-14 01:56:04.889882
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 01:56:05.798374
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:10.577699
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils import unit_test_ast  # type: ignore
    node = unit_test_ast.build_ast_from_snippet(imports)
    assert isinstance(node, ast.Module)
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    assert isinstance(node, ast.Module)
    assert isinstance(node.body[0], ast.ImportFrom)

# Generated at 2022-06-14 01:56:17.649478
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('print("")')
    Python2FutureTransformer().visit(tree)
    expected = (
        'from __future__ import absolute_import\n'
        'from __future__ import division\n'
        'from __future__ import print_function\n'
        'from __future__ import unicode_literals\n\n'
        'print("")\n'
    )
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 01:56:27.938673
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tests = []
    node = ast.parse('print("Hello world")')
    expected = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nprint("Hello world")')

    tests.append((node, expected))
    for i, (node, expected) in enumerate(tests):
        actual = Python2FutureTransformer().visit(node)
        
        assert ast.dump(actual) == ast.dump(expected), "For test #{}: expected {}, but got {}".format(
            i, ast.dump(expected), ast.dump(actual)
        )

# Generated at 2022-06-14 01:56:29.870892
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)


# Generated at 2022-06-14 01:56:40.222232
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('print(1)')
    ret = Python2FutureTransformer().visit(node)
    
    output = ast.dump(node) if isinstance(node, ast.AST) else node

# Generated at 2022-06-14 01:56:50.168160
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code_before = """
    def hello():
        print('hello, world!')
    """
    code_after = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    def hello():
        print('hello, world!')
    """
    # Run the test
    transfromer = Python2FutureTransformer(2, 7)
    transformed_node = transfromer.visit(ast.parse(code_before))
    # Compare the results
    assert astor.to_source(transformed_node) == code_after

# Generated at 2022-06-14 01:56:54.014752
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:00.654783
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    from .base import Python2_7AstOptimizationTestCase
    tree = astor.parse_file('./tests/resources/sample2.py')
    print(Python2FutureTransformer().transform(tree))
    # Test what happens if nothing to transform
    print(Python2FutureTransformer().transform(tree))
    assert True


# Generated at 2022-06-14 01:57:05.680237
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import_arguments = ast.parse('from __future__ import absolute_import; from __future__ import division; from __future__ import print_function; from __future__ import unicode_literals')
    module = ast.Module(body= [])
    transformer = Python2FutureTransformer()
    assert transformer.visit(module) == import_arguments.body + module.body

# Generated at 2022-06-14 01:57:07.139909
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    obj = Python2FutureTransformer()
    assert (obj.target == (2, 7))
    assert (obj.tree_changed == False)
    assert (obj.module is None)



# Generated at 2022-06-14 01:57:16.356179
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from ..utils.ast_helper import compile_snippet, compare_ast
    module = compile_snippet(imports.get_ast(future='__future__'), mode='exec')
    mod = compile_snippet(module_source, mode='exec')
    expected = ast.Module(
        body=module.body + mod.body
    )
    mod = Python2FutureTransformer().visit(mod)
    compare_ast(mod, expected)


# Generated at 2022-06-14 01:57:19.041261
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:20.309502
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:26.508933
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ast_helper.compare import compare_ast
    from ast_helper.generic import generic_visit
    from ..utils.fixtures import future_module, future_module_expected

    transformer = Python2FutureTransformer()
    tree_actual = generic_visit(future_module, transformer)
    assert compare_ast(tree_actual, future_module_expected)

# Generated at 2022-06-14 01:57:31.458216
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    generated_ast = astor.to_source(Python2FutureTransformer().visit(ast.parse("")))
    assert generated_ast == 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n'

# Generated at 2022-06-14 01:57:41.613011
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typing import List

    from ..utils.preprocess import preprocess


# Generated at 2022-06-14 01:57:57.049374
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformer import ast_to_str
    ast_str_before = """
        def f(foo):
            return foo
    """
    ast_str_after = """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        def f(foo):
            return foo
    """
    tree_before = ast.parse(ast_str_before)
    tree_after = ast.parse(ast_str_after)
    t = Python2FutureTransformer()
    tree_after_ = t.visit(tree_before)
    assert ast_to_str(tree_after_) == ast_to_str(tree_after)

# Generated at 2022-06-14 01:57:58.266080
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tr = Python2FutureTransformer()
    assert tr.target == (2, 7)

# Generated at 2022-06-14 01:58:01.287125
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.testutils import round_trip

    source = imports.get_source(future='__future__')
    result = round_trip(source)
    assert result == source

# EOF

# Generated at 2022-06-14 01:58:06.970506
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    file_path = os.path.realpath(__file__)
    with open(file_path, 'r') as f:
        module = ast.parse(f.read())

    t = Python2FutureTransformer()
    t.visit(module)

    t_ = Python2FutureTransformer()
    t_.visit(module)

    assert t._tree_changed
    assert not t_._tree_changed

# Generated at 2022-06-14 01:58:07.778701
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:58:09.189780
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.targets == (2, 7)
    assert Python2FutureTransformer.future_import == True


# Generated at 2022-06-14 01:58:14.544101
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import textwrap
    from ..transformers.python2_future import Python2FutureTransformer

    input = textwrap.dedent('''\
        import os
        from sys import platform

        from future import absolute_import
        from future import division
        from future import print_function
        from future import unicode_literals

        import typing
        ''')

    root = ast.parse(input)
    output = ast.parse(input)
    Python2FutureTransformer().visit(output)

    assert ast.dump(root) == ast.dump(output)

# Generated at 2022-06-14 01:58:18.243731
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from future.utils import PY2
    assert PY2
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import parse
    from .fixes.Python2FutureTransformer import Python2FutureTransformer


# Generated at 2022-06-14 01:58:25.721176
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    input_code = '''
x = "hello world"
print(x)
'''
    expected_code = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = "hello world"
print(x)
'''
    tree = ast.parse(input_code)
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)  # type: ignore
    assert expected_code == codegen.to_source(tree)

# Generated at 2022-06-14 01:58:26.999010
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transp = Python2FutureTransformer()
    assert hasattr(transp, 'target')

# Generated at 2022-06-14 01:58:47.241331
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    source = """
a = 1
b = '1'
print(a,b)
"""
    source2 = """
from future import *

a = 1.1
b = '1.1'
print(a,b)
"""

    source_ast = ast.parse(source)
    source_ast2 = ast.parse(source2)

    target = Python2FutureTransformer()
    target_ast = target.visit(source_ast)
    target_source = astor.to_source(target_ast)

    assert target_source == astor.to_source(source_ast2)

# Generated at 2022-06-14 01:58:48.418055
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer


# Generated at 2022-06-14 01:58:58.158415
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3
    from typed_ast.ast3 import Module
    from darglint.transforms.Python2FutureTransformer import visit_Module
    from darglint import util
    util.log_msg = None  # type: ignore

# Generated at 2022-06-14 01:59:03.531460
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()

    node = ast.parse('print "hello world"')

    transformer.visit(node)

    assert transformer.tree_changed
    assert ast.dump(node) == (
        imports() +
        '\n'
        'print "hello world"')

# Generated at 2022-06-14 01:59:06.424993
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert transformer.pattern == transformer.target

# Generated at 2022-06-14 01:59:11.672064
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import astunparse
    tree = ast.parse('a = 2')
    tt = Python2FutureTransformer()
    tt.visit(tree)
    unparse_tree = astunparse.unparse(tree)
    assert unparse_tree == '\n'.join([
        "from __future__ import absolute_import",
        "from __future__ import division",
        "from __future__ import print_function",
        "from __future__ import unicode_literals",
        "",
        "a = 2"])

# Generated at 2022-06-14 01:59:25.168905
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():

    # Test case 1:
    module = ast.parse('x = 1')

    transformer = Python2FutureTransformer()
    transformer.visit(node=module)

    assert len(module.body) == transformer.get_body(imports).size() + 1
    assert module.body[0].names[0].name == 'absolute_import'

    # Test case 2:
    module = ast.parse('x = 1')

    transformer = Python2FutureTransformer(future='__future__')
    transformer.visit(node=module)

    assert len(module.body) == transformer.get_body(imports).size() + 1
    assert module.body[0].names[0].name == 'absolute_import'

    # Test case 3:
    module = ast.parse('x = 1')

    transformer = Python2FutureTransformer

# Generated at 2022-06-14 01:59:33.981295
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast
    import typing

# Generated at 2022-06-14 01:59:41.141551
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *
from past.builtins import basestring

from .base import BaseNodeTransformer
from ..utils.snippet import snippet
from .base import BaseNodeTransformer
from .base import BaseNodeTransformer
from .base import BaseNodeTransformer
"""
    code = ast.parse(source)
    obj = Python2FutureTransformer()
    obj.visit(code)

# Generated at 2022-06-14 01:59:42.005932
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == "Python2FutureTransformer"

# Generated at 2022-06-14 02:00:09.012168
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 02:00:16.409819
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    test = """
a = 2
print(a)
"""
    tree = ast.parse(test)
    Python2FutureTransformer().visit(tree)
    # visits the children
    assert ast.dump(tree) == """Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=2)), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[]))])"""



# Generated at 2022-06-14 02:00:17.690756
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:19.037057
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()


# Generated at 2022-06-14 02:00:20.881341
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ast_inspector import inspector

# Generated at 2022-06-14 02:00:24.214351
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    target = (2, 7)
    p2ft = Python2FutureTransformer(target)
    assert p2ft.target == target

# Generated at 2022-06-14 02:00:34.460772
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse("30 + 42")
    tree = Python2FutureTransformer().visit(tree)  # type: ignore
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 6
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert isinstance(tree.body[1], ast.ImportFrom)
    assert isinstance(tree.body[2], ast.ImportFrom)
    assert isinstance(tree.body[3], ast.ImportFrom)
    assert isinstance(tree.body[4], ast.ImportFrom)
    assert isinstance(tree.body[5], ast.Expr)

# Generated at 2022-06-14 02:00:36.268333
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(2, 7).target == (2, 7)


# Generated at 2022-06-14 02:00:46.847896
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    tree = ast.parse('import os')
    result = Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 02:00:47.896035
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is not object

# Generated at 2022-06-14 02:01:43.816379
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer

    _shutil = Python2FutureTransformer()
    assert isinstance(_shutil, BaseNodeTransformer)
    assert _shutil.target == (2, 7)



# Generated at 2022-06-14 02:01:51.010083
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # given
    code = '''print("Hello, world!")'''
    # when
    result = Python2FutureTransformer().transform_code(code)
    # then
    assert result == dedent('''\
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    print("Hello, world!")''')

# Generated at 2022-06-14 02:01:55.267761
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.sample import sample
    from ..utils.visitor import print_python_source
    from ..utils.diff import diff

    print(diff(sample.py2,
               Python2FutureTransformer().visit(sample.py2)))



# Generated at 2022-06-14 02:02:02.567574
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import pathlib

    from ..utils.ast import get_ast, compare_asts

    tree_changed = Python2FutureTransformer().run(
        get_ast(pathlib.Path('tests/fixtures/NodeTransformer_visit_Module.py'))
    )
    assert tree_changed

    correct_ast = get_ast(pathlib.Path('tests/fixtures/NodeTransformer_visit_Module.refactored.py'))

    assert compare_asts(correct_ast, correct_ast), 'The unit test for method visit_Module failed'



# Generated at 2022-06-14 02:02:06.883043
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    def check(input, output):
        module = ast.parse(input)
        pft = Python2FutureTransformer()
        new_module = pft.visit(module)
        assert ast.dump(new_module) == ast.dump(ast.parse(output))


# Generated at 2022-06-14 02:02:13.447502
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    tr = Python2FutureTransformer()
    x = ast.parse('x = 2')
    result = tr.visit(x)
    assert isinstance(result, ast.Module)
    assert astor.to_source(result) == '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
x = 2
'''

# Generated at 2022-06-14 02:02:17.353881
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import parse
    from .test_utils import assert_equal_ast

    tree = parse("")
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    assert_equal_ast(tree, parse(imports(future='__future__')))

# Generated at 2022-06-14 02:02:23.239191
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    from py2to3.tests.test_transformer_classbase import TestTransformerClassbase
    TestTransformerClassbase(transformer_class=Python2FutureTransformer).run_test(test_file='test_py2future.py')

# Generated at 2022-06-14 02:02:32.609780
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    @snippet
    def f(x, y, z):
        return x + y + z

    t = Python2FutureTransformer()
    t.parse_tree(f)
    t.visit_Module(t.tree)
    l = t.tree.body  # type: ignore

    assert(isinstance(l[0], ast.ImportFrom))
    assert(l[0].module == '__future__')
    assert(l[0].names[0].name == 'division')

    assert(isinstance(l[1], ast.ImportFrom))
    assert(l[1].module == '__future__')
    assert(l[1].names[0].name == 'print_function')

    assert(isinstance(l[2], ast.ImportFrom))

# Generated at 2022-06-14 02:02:34.446147
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.visitor import run_visitor
    from ..utils.utils import load_module

    module = load_module('examples.sample_source2.fixtures.sample_tree')
    m = run_visitor(module, [Python2FutureTransformer])
    assert m.body[-1].name == 'print_function'

# Generated at 2022-06-14 02:04:43.931119
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = '1 + 2'
    expected = 'from __future__ import absolute_import\n' \
               'from __future__ import division\n' \
               'from __future__ import print_function\n' \
               'from __future__ import unicode_literals\n' \
               '\n' \
               '1 + 2'
    assert Python2FutureTransformer().transform_code(code) == expected

# Generated at 2022-06-14 02:04:44.951066
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:04:47.433607
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Simple smoke test for Python2FutureTransformer."""
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 02:04:58.453237
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None, None).__class__ == Python2FutureTransformer
    assert Python2FutureTransformer(None, None).target == (2, 7)
    assert Python2FutureTransformer(None, None)._tree_changed == False