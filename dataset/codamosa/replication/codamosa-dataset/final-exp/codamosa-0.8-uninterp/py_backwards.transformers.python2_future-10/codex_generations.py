

# Generated at 2022-06-14 01:55:04.715750
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    from typed_ast.ast3 import parse


# Generated at 2022-06-14 01:55:11.965534
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    expected = ast.Module(
        body=[
            ast.ImportFrom(module='__future__', names=[
                ast.alias(name='absolute_import', asname=None),
                ast.alias(name='division', asname=None),
                ast.alias(name='print_function', asname=None),
                ast.alias(name='unicode_literals', asname=None)
            ], level=0)
        ]
    )
    source = ast.parse('')
    actual = Python2FutureTransformer().visit_Module(source)
    assert ast.dump(actual) == ast.dump(expected)

# Generated at 2022-06-14 01:55:19.454874
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils import code_equal
    from .python2unittest import transform

    module = ast.parse('def x():pass')
    expected = """def x():
    pass
"""
    module_2 = transform(module, Python2FutureTransformer)
    module_3 = ast.parse(expected)
    assert code_equal(module_2, module_3)

# Generated at 2022-06-14 01:55:20.726143
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:55:27.657943
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class DummyTransformer(Python2FutureTransformer):
        def __init__(self, dummy=None):
            self._dummy = dummy

        def run(self):
            self.visit(self._dummy)

    tree = ast.parse("pass")
    transformer = DummyTransformer(tree)
    transformer.run()
    assert isinstance(transformer._dummy, ast.Module)
    assert len(transformer._dummy.body) == 4
    assert isinstance(transformer._dummy.body[0], ast.ImportFrom)



# Generated at 2022-06-14 01:55:32.736350
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    p = Python2FutureTransformer('a.py')
    p._tree_changed = False
    node = ast.parse('module_body')
    node = p.visit_Module(node)
    assert p._tree_changed
    assert node.body[0].value.s == 'absolute_import'
    assert node.body[1].value.s == 'division'
    assert node.body[2].value.s == 'print_function'
    assert node.body[3].value.s == 'unicode_literals'

# Generated at 2022-06-14 01:55:39.230263
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    source = '''
x = 1
y = 2
    '''
    expected = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
x = 1
y = 2
    '''
    tree = ast.parse(source)
    transformed = transformer.visit(tree)
    assert astor.to_source(transformed) == expected

# Generated at 2022-06-14 01:55:44.676801
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('x = 1\nprint(x)')
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)
    assert new_node.body[0]._fields == ('module', 'identifier')
    assert new_node.body[0].module == '__future__'
    assert new_node.body[0].identifier == 'absolute_import'

# Generated at 2022-06-14 01:55:54.930134
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import get_ast
    from .base import BaseNodeTransformerTestCase
    from ..visitor import compare_trees
    from ..utils.list_comprehension import EMPTYLIST_CONSTRUCTOR
    from ..utils.list_comprehension import EMPTYLIST_COMPREHENSION

    class TestCase(BaseNodeTransformerTestCase):
        target = (2, 7)
        transformer = Python2FutureTransformer
        code = '''
            a = b
            c = d
        '''

        def test_pre_visit(self, node: ast.Node) -> None:
            self.assertIsInstance(node, ast.Module)

        def test_post_visit(self, node: ast.Node) -> None:
            self.assertIsInstance(node, ast.Module)

# Generated at 2022-06-14 01:56:01.396489
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import numpy as np
    from ..utils.source import as_source
    from ..utils.ast import as_ast, compare_ast
    from . import rel
    from .base import BaseNodeTransformer
    from .python3 import Python3StandardLibraryTransformer
    from . import transforms
    import typing
    import astunparse

    source = as_source(np.__name__)
    source += "\ndef f(x):\n    return x+1\n"
    root_node = as_ast(source)
    root_node = TestPython2FutureTransformer().visit(root_node)  # type: ignore
    root_node = TestPython2FutureTransformer().visit(root_node)  # type: ignore

# Generated at 2022-06-14 01:56:08.913058
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..transpile import transpile
    from ..config import default_config
    from ..utils.source import get_source, get_ast

    config = default_config.copy()
    config.update({
        'target': (2, 7),
        'debug': True
    })


# Generated at 2022-06-14 01:56:10.851970
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == "Python2FutureTransformer"


# Generated at 2022-06-14 01:56:18.292767
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Given
    simple_module = """
import sys

a = 1
"""
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

a = 1
"""
    # When
    result = Python2FutureTransformer().visit(ast.parse(simple_module))

    # Then
    assert ast.dump(result) == ast.dump(ast.parse(expected))


# Generated at 2022-06-14 01:56:29.820676
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .transformer_test_case import TransformerTestCase
    from .test_base import assert_tree
    import ast

    class Test(TransformerTestCase):
        module = __file__
        transformer = Python2FutureTransformer

        def test_insert_future_import(self):
            before = """import os"""
            after = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os"""
            self.assertTransform(before, after)

    assert_tree(ast.parse(imports.get_source(future='__future__')), ast.parse(imports.get_body(future='__future__')))

    Test.main(verbose=True)

# Generated at 2022-06-14 01:56:39.750881
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet
    from .base import BaseNodeTransformer

    @snippet
    def original():
        pass


    @snippet
    def expected():
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        pass


    node = ast.parse(original.get_source())
    t = Python2FutureTransformer()
    new_node = t.visit_Module(node)
    ast.fix_missing_locations(new_node)
    assert ast.dump(new_node) == ast.dump(ast.parse(expected.get_source()))

# Generated at 2022-06-14 01:56:44.806946
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # The method visit_Module directly prepends the module body
    # with the future imports and returns the resulting module.
    # We do not need to define any fixture and we can use the 
    # default implementation of the fixture 'test_node_transformer' provided
    # by the module 'transformers.testing'
    pass

# Generated at 2022-06-14 01:56:51.231619
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class DummyModule(ast.Module):
        def __init__(self):
            self.body = []  # type: List[ast.stmt]
    
    dummy_module = DummyModule()
    python2_future_transformer = Python2FutureTransformer()
    actual = python2_future_transformer.visit_Module(dummy_module)
    assert dummy_module is actual

# Generated at 2022-06-14 01:56:52.879172
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None


# Generated at 2022-06-14 01:57:03.550273
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():  # type: ignore
    # Test Module with zero, one and two lines of code.
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet
    from ..utils.random import random_string
    from ..utils.ast import dump

    @snippet
    def module():
        pass

    @snippet
    def module():
        a = 1

    @snippet
    def module():
        a = 1
        b = 2

    @snippet
    def expected_module():
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        pass

    @snippet
    def expected_module():
        from __future__ import absolute_import
        from __future__ import division

# Generated at 2022-06-14 01:57:08.926746
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """
    Test to ensure that the Python2FutureTransformer is working properly, plus checking if assignment statements are
    getting appended to the body list
    """
    # Testing imports() method, whether the list body is returned properly which
    # assigns the future import module to the main body of code

# Generated at 2022-06-14 01:57:22.751489
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from astor.code_gen import to_source
    import os
    import sys
    sys.path.insert(0, os.path.abspath('src'))
    from .. import Python2FutureTransformer

    module_name = 'Py2Future'
    file_name = 'main.py'
    code = '''
    print("hello")
    '''
    module = astor.parse_file(code, module_name, file_name)
    trans = Python2FutureTransformer()
    new_module = trans.visit(module)
    source = to_source(new_module, indent_with='    ')

# Generated at 2022-06-14 01:57:29.586912
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse(
        '''
        print('Test')
        '''
    )
    expected_ast_tree = ast.parse(
        '''
        from __future__ import (
            absolute_import,
            division,
            print_function,
            unicode_literals
        )
        print('Test')
        '''
    )
    assert Python2FutureTransformer().visit(module) == expected_ast_tree

# Generated at 2022-06-14 01:57:34.890703
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    ast_node = ast.parse('from __future__ import unicode_literals\n'
                         'a = 1')
    assert Python2FutureTransformer().visit(ast_node) == ast.parse('from future import absolute_import\n'
                                                                  'from future import division\n'
                                                                  'from future import print_function\n'
                                                                  'from future import unicode_literals\n\n'
                                                                  'a = 1')

# Generated at 2022-06-14 01:57:45.133271
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    before = dedent('''
    print('hello')
    ''')
    after = dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literal

    print('hello')
    ''')
    node = ast.parse(before)
    Python2FutureTransformer().visit(node)  # type: ignore
    assert_code_equal(after, node)

# Generated at 2022-06-14 01:57:55.833495
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test whether visit_Module method of Python2FutureTransformer class
    prepends module with:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    """
    module = ast.parse("print('Hello, world!')")
    new_module = Python2FutureTransformer().visit(module)

# Generated at 2022-06-14 01:58:05.846749
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('pass')
    transformed_module = Python2FutureTransformer().visit(module)
    assert len(transformed_module.body) == 6
    assert isinstance(transformed_module.body[0], ast.ImportFrom)
    assert isinstance(transformed_module.body[1], ast.ImportFrom)
    assert isinstance(transformed_module.body[2], ast.ImportFrom)
    assert isinstance(transformed_module.body[3], ast.ImportFrom)
    assert isinstance(transformed_module.body[4], ast.Pass)
    assert isinstance(transformed_module.body[5], ast.Pass)
    assert transformed_module.body[0].module == '__future__'
    assert transformed_module.body[0].names[0].name == 'absolute_import'


# Generated at 2022-06-14 01:58:14.001923
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast27 as ast
    from _ast import Module
    from _ast import Str
    from _ast import Name
    from _ast import Load
    from _ast import Import
    from _ast import ImportFrom
    tree = Module(body=[])
    tree_transformed = Python2FutureTransformer(transform_type='module').visit(tree)

# Generated at 2022-06-14 01:58:23.824206
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    code = textwrap.dedent("""
        import pandas as pd
        import numpy as np
        import scipy as sp
    """)
    expected = textwrap.dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        import pandas as pd
        import numpy as np
        import scipy as sp
    """)

    tree = ast.parse(code, mode='exec')
    transformer.visit(tree)
    actual = astor.to_source(tree).strip()

    assert actual == expected

# Generated at 2022-06-14 01:58:31.555810
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse("")
    transformed = Python2FutureTransformer().visit(module)
    assert transformed is not None
    assert transformed.body
    assert isinstance(transformed.body[0], ast.ImportFrom)
    assert transformed.body[0].module == '__future__'
    assert transformed.body[0].names[0].name == "absolute_import"
    assert transformed.body[1].names[0].name == "division"
    assert transformed.body[2].names[0].name == "print_function"
    assert transformed.body[3].names[0].name == "unicode_literals"

# Generated at 2022-06-14 01:58:40.546023
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from astor import dump
    from . import test_utils
    import textwrap

    class TestNode:
        def __init__(self, source_code, **kwargs):
            self.tree = test_utils.get_ast_tree(source_code)
            self.args = kwargs

    class TestCase(object):
        def __init__(self, name, input, expect_code, expect_ast=None):
            self.name = name
            self.input = input
            self.expect_code = expect_code
            self.expect_ast = expect_ast

        def test(self, node: TestNode):
            transformer = Python2FutureTransformer(node.args, node.tree)

# Generated at 2022-06-14 01:58:52.691955
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transpiled_code = Python2FutureTransformer.run_test('./tests/files/to_transform/simple_2.py')
    expected_code = Python2FutureTransformer.run_test('./tests/files/expected/simple_2.py')
    assert(transpiled_code == expected_code)


# Generated at 2022-06-14 01:58:53.506452
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 01:58:55.512660
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 01:58:57.452208
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 01:59:03.402646
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    module = ast.parse("def foo():\n    bar = 42")
    Python2FutureTransformer().visit(module)

    module = ast.parse("from __future__ import absolute_import\ndef foo():\n    pass")
    Python2FutureTransformer().visit(module)

# Generated at 2022-06-14 01:59:09.319965
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import get_ast_node
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    
    a = 1
    """
    node = ast.parse(expected)
    transformed = Python2FutureTransformer().visit(node)  # type: ignore
    assert transformed == get_ast_node(expected)

# Generated at 2022-06-14 01:59:22.514340
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast

    transformer = Python2FutureTransformer()
    transformed = transformer.visit(ast.parse('x=1'))
    assert len(transformed.body) == 5
    print(ast.dump(transformed, annotate_fields=False, include_attributes=False))

# Generated at 2022-06-14 01:59:27.107286
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from py2modernize.transformer.base import _get_tree
    from code_fixer import transform  # noqa

    node = _get_tree('', target_version='2.7')
    Python2FutureTransformer().visit(node)



# Generated at 2022-06-14 01:59:29.598604
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = ast.parse('x=1')
    y = Python2FutureTransformer().visit(x)
    

# Generated at 2022-06-14 01:59:33.446942
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:48.794691
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert isinstance(Python2FutureTransformer, type)

# Generated at 2022-06-14 01:59:55.249738
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast as python_ast
    import typed_ast.ast3 as typed_ast

    tree = python_ast.parse('pass', mode='exec')
    tree = typed_ast.ast3.parse('pass', mode='exec')  # type: ignore

    visitor = Python2FutureTransformer(tree)
    new_tree = visitor.visit(tree)  # type: ignore

    import typed_astunparse
    typed_astunparse.dump_tree(tree)
    typed_astunparse.dump_tree(new_tree)

# Generated at 2022-06-14 02:00:05.929896
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import Module
    from typed_ast import ast3 as ast
    from .. import node_test_util as util

    code = "\n"

    tree = ast.parse(code, mode="exec")

# Generated at 2022-06-14 02:00:16.853724
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.test_utils import round_trip
    from ..utils.test_utils import parse_ast

    transformer = Python2FutureTransformer()
    src = """\
# coding: utf-8
# This module is a port of Python 2.7's ast.py
# It'll not be compatible with Python 3's ast.py
#
# The list of Future keywords.  This is initialized by Future().
#

"""

# Generated at 2022-06-14 02:00:18.105240
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 02:00:19.861179
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(target_version=(2, 7)).type_comment is True

# Generated at 2022-06-14 02:00:21.800259
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'

# Generated at 2022-06-14 02:00:29.250323
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    tree = ast.parse("import sys")
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    assert astor.to_source(tree)\
        == "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\nimport sys\n"

# Generated at 2022-06-14 02:00:34.069735
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = """
        import sys

        def main():
            pass

    """

# Generated at 2022-06-14 02:00:41.943271
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = 'abc+1'
    target = 'from __future__ import absolute_import\n'+\
             'from __future__ import division\n'+\
             'from __future__ import print_function\n'+\
             'from __future__ import unicode_literals\n'+\
             '{}\n'.format(source)
    module = ast.parse(source)
    Python2FutureTransformer().visit(module)
    assert ast.dump(module) == ast.dump(ast.parse(target))
    assert Python2FutureTransformer().visit(module) is None

# Generated at 2022-06-14 02:01:16.181096
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .utils import get_and_run_transformed
    from typed_ast import ast3
    from ..utils.snippet import snippet
    def f():
      return 1
    module_old, module_new = get_and_run_transformed(f, Python2FutureTransformer)
    print(module_old)
    print(module_new)
    assert type(module_old) == module_new.__class__
    assert module_old.body == module_new.body

# Generated at 2022-06-14 02:01:16.781959
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:17.828380
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:01:27.699777
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from mypy.nodes import MypyFile

    import_lines = ["from __future__ import absolute_import",
                    "from __future__ import division",
                    "from __future__ import print_function",
                    "from __future__ import unicode_literals"]

    class_lines = ["class TestClass(object):",
                    "    def test_method(self, param1, param2):",
                    "        method_body = 'test'",
                    "",
                    ""]

    def_lines = ["def test_function(param1, param2):",
                    "    method_body = 'test'",
                    ""]

    for_lines = ["for i in range(10):",
                    "    print(i)"]

    lines = import_lines + class_lines + def_lines + for_lines


# Generated at 2022-06-14 02:01:35.539771
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('x = 0')
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    assert transformer._tree_changed == True  # type: ignore
    assert node.body[0].value.left.id == 'absolute_import'  # type: ignore
    assert node.body[1].value.left.id == 'division'  # type: ignore
    assert node.body[2].value.left.id == 'print_function'  # type: ignore
    assert node.body[3].value.left.id == 'unicode_literals'  # type: ignore

# Generated at 2022-06-14 02:01:46.724146
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # test if imports are successfully added to the Python script
    node = ast.parse("print(1)\nsum = 3")
    expected = ast.parse("from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nprint(1)\nsum = 3")
    actual = Python2FutureTransformer().visit(node)
    assert ast.dump(actual) == ast.dump(expected)

    # test if root node is a Module
    node = ast.parse("from __future__ import absolute_import\nprint(1)\nsum = 3")

# Generated at 2022-06-14 02:01:53.484914
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .. import tree
    module = tree.import_("typed_ast.ast3")
    imports_ = tree.import_("sys", "os")[0]
    t = Python2FutureTransformer()
    t.visit(module)
    t.visit(imports_)

# Generated at 2022-06-14 02:01:54.814759
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 02:01:56.635123
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.tree_changed is False

# Generated at 2022-06-14 02:01:58.710619
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass



# Generated at 2022-06-14 02:03:10.546269
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast

    from flake8_future_import.transforms.base import BaseNodeTransformer
    
    cls = Python2FutureTransformer
    target = (2, 7)
    node = ast.Module(body=[])
    expected = ast.Module(body=(imports.get_body(future='__future__')))
    instance = cls()
    actual = instance.visit_Module(node)
    assert isinstance(instance.target, tuple)
    assert isinstance(instance, BaseNodeTransformer)
    assert actual == expected

# Generated at 2022-06-14 02:03:13.060009
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Test that the constructor works with no parameters
    _ = Python2FutureTransformer()



# Generated at 2022-06-14 02:03:16.339067
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer('abc', (2, 7))

# Unit test of method Python2FutureTransformer.visit_Module()

# Generated at 2022-06-14 02:03:21.416602
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = Module(body=[Expr(value=Str(s='a'))])
    transformed_node = transformer.visit(node)
    assert isinstance(transformed_node, Module)

# Generated at 2022-06-14 02:03:23.453488
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer(None)
    assert transformer is not None

# Generated at 2022-06-14 02:03:31.550261
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Test for not changing the tree if it already has the necessary import
    t = ast.parse(
        'from __future__ import absolute_import\n'
        'from __future__ import division\n'
        'from __future__ import print_function\n'
        'from __future__ import unicode_literals\n'
    )
    future = Python2FutureTransformer()
    future.visit(t)
    assert not future._tree_changed  # pylint: disable=protected-access

    # Test for changing the tree
    t = ast.parse('a = 1')
    future = Python2FutureTransformer()
    future.visit(t)

    assert len(t.body) == 5  # pylint: disable=protected-access

# Generated at 2022-06-14 02:03:33.869954
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from snippets import abs_import1
    t = Python2FutureTransformer(abs_import1.my_function)
    assert t.future == '__future__'
    assert t._tree_changed == False


# Generated at 2022-06-14 02:03:44.013033
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    tree = ast.parse('''
        def f(x):
            print x
    ''')
    transformer = Python2FutureTransformer()
    ast.fix_missing_locations(transformer.visit(tree))
    assert transformer.tree_changed == True
    assert transformer.target_changed == True

# Generated at 2022-06-14 02:03:48.556653
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)
    assert callable(Python2FutureTransformer)
    assert callable(Python2FutureTransformer())


# Generated at 2022-06-14 02:03:58.656910
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..test_utils import assert_ast_snippets
    from .. import is_mac_os_x
    from os import linesep

    if is_mac_os_x():
        print('skip test_Python2FutureTransformer::test_Python2FutureTransformer_visit_Module')
        return
