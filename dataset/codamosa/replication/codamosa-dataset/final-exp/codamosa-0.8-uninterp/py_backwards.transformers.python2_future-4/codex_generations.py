

# Generated at 2022-06-14 01:55:07.919182
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse(
        '''
        a = 1
        b = 2
        '''
    )
    expected = ast.parse(
        '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        a = 1
        b = 2
        '''
    )
    Python2FutureTransformer().visit(module)
    assert ast.dump(expected) == ast.dump(module)

# Generated at 2022-06-14 01:55:18.342621
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import sys
    import ast
    import pytest
    from ast_inspector import node_inspector
    node_inspector.inspect.config.verbose = 2
    code = '''
    source = -1
    source = 2/3
    source = 2 // 3
    print('test')
    '''
    input_node = ast.parse(code)
    trans = Python2FutureTransformer()
    trans.visit(input_node)
    trans.print_tree()
    trans.print_tree_clean()

'''
if __name__ == "__main__":
    test_Python2FutureTransformer()
'''

# Generated at 2022-06-14 01:55:28.355436
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.tree is None
    assert transformer.tree_changed is False
    # TODO: add test for transformer.target
    assert callable(transformer.visit_Module)
    assert callable(transformer.visit_Import)
    assert callable(transformer.visit_ImportFrom)
    assert callable(transformer.visit_alias)
    assert callable(transformer.visit_Attribute)
    assert callable(transformer.visit_FunctionDef)
    assert callable(transformer.visit_arguments)
    assert callable(transformer.visit_arg)
    assert callable(transformer.visit_Return)
    assert callable(transformer.generic_visit)
    assert callable(transformer.visit)
    assert not call

# Generated at 2022-06-14 01:55:34.790094
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import untokenize
    import astor
    import sys
    import ast
    from ..utils.ast_node_utils import get_module_body

    # Parse code
    source = '''
        def f():
            print(1 / 2)
            print(2 / 3)
    '''
    tree = ast.parse(source, filename='<unknown>')

    # Test body of method visit_Module of class Python2FutureTransformer
    transformer = Python2FutureTransformer(tree, (2, 7))
    result = transformer.visit_Module(tree)
    assert transformer._tree_changed == True

    # Make new code from new tree
    new_source = untokenize.untokenize(get_module_body(result.body))

    # Result

# Generated at 2022-06-14 01:55:45.574815
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from .base import MockTransformer
    from .base import transform_snippet

    tree = astor.parse_file('python-modernize/modernize/fixes/__init__.py')
    transformer = MockTransformer(Python2FutureTransformer(tree))
    transformer.visit(tree)
    assert 'from __future__ import absolute_import' in astor.to_source(tree) \
           == imports.get_body(future='__future__')

    assert transform_snippet('a=1', transformer).source == 'from __future__ import absolute_import\n' \
                                                         'from __future__ import division\n' \
                                                         'from __future__ import print_function\n' \
                                                         'from __future__ import unicode_literals\n' \
                                

# Generated at 2022-06-14 01:55:55.812735
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source2ast
    from ..utils.snippet import snippet_compare
    from .recast_literal import RecastLiteralTransformer

    source = '''\
# This is a comment

print("Dummy1")
print("Dummy2")
    '''

    expected = '''\
# This is a comment

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("Dummy1")
print("Dummy2")
    '''

    tree = source2ast(source)
    visitor = Python2FutureTransformer()
    visitor.visit(tree)
    assert snippet_compare(expected, ast.dump(tree, include_attributes=True)) is True

    tree

# Generated at 2022-06-14 01:56:00.589030
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    
    assert not t._tree_changed

    t.visit_Module(ast.dump(imports.get_ast(future='__future__')))
    
    assert not t._tree_changed

    t.visit_Module(ast.dump(ast.parse('')))

    assert t._tree_changed

# Generated at 2022-06-14 01:56:10.632407
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('x=5')
    tree = Python2FutureTransformer()
    tree.visit(node)
    assert tree.tree_changed == True

# Generated at 2022-06-14 01:56:18.491292
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from textwrap import dedent

    source = dedent('''
        import os
        import sys
        ''')

    expected_output = dedent('''
        from future import absolute_import
        from future import division
        from future import print_function
        from future import unicode_literals

        import os
        import sys
        ''')

    node = ast.parse(source)
    Python2FutureTransformer.run(node)
    output = astor.to_source(node)

    assert output == expected_output

# Generated at 2022-06-14 01:56:29.923745
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse('a = 1')
    Python2FutureTransformer().visit(tree)
    assert ast.dump(tree) == "Module(body=[ImportFrom(module='__future__', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='unicode_literals', asname=None)], level=0), Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=1))])"

# Generated at 2022-06-14 01:56:36.229970
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    def test_future_modules(code, future_module):
        module = ast.parse(code)
        obj = Python2FutureTransformer()
        module = obj.visit(module)
        from .visitor import assertASTNodesEqual
        assertASTNodesEqual(module, ast.parse(code).body, check_meta=False)
        assertASTNodesEqual(module.body[0], ast.parse(future_module).body[0], check_meta=False)

    code = 'def func():\r\n    pass\r\n'
    future_module = 'from __future__ import (absolute_import, division, print_function,unicode_literals)\r\n'
    test_future_modules(code=code, future_module=future_module)


# Generated at 2022-06-14 01:56:40.747233
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    
    # __init__
    mock_tree = ast.parse("print('Hello, world!')")
    transformer = Python2FutureTransformer(mock_tree)
    
    assert isinstance(transformer, Python2FutureTransformer)
    assert transformer.tree == mock_tree
    assert transformer._node == mock_tree
    assert transformer._tree_changed == False


# Generated at 2022-06-14 01:56:52.933404
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..testing import run_local_tests

    text = """
    print("Python 2 module")
    """
    expected1 = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals


    print("Python 2 module")
    """
    expected2 = """
    from __future__ import absolute_import, division, print_function, unicode_literals


    print("Python 2 module")
    """

    actual = ast.parse(text)
    result = Python2FutureTransformer().visit_Module(actual)  # type: ignore
    code1 = str(result).split("\n")
    code2 = str(result).split("\n")

# Generated at 2022-06-14 01:56:56.185949
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    def check(code, expected):
        node = ast.parse(code)
        transformer = Python2FutureTransformer()
        new_node = transformer.visit(node)
        assert ast.dump(new_node) == ast.dump(ast.parse(expected))


# Generated at 2022-06-14 01:56:59.157884
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Unit test for method visit_Module of class Python2FutureTransformer"""
    # TODO: implement.
    pass



# Generated at 2022-06-14 01:57:01.600482
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # This is for line coverage for the constructor of class Python2FutureTransformer
    try:
        Python2FutureTransformer()
    except TypeError:
        pass

# Generated at 2022-06-14 01:57:06.120544
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from types import ModuleType
    from typed_ast import ast3 as ast
    from ..utils import get_node_type, get_node_body
    from .base import BaseNodeTransformer
    from .utils import source_to_ast
    

# Generated at 2022-06-14 01:57:08.464710
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 01:57:11.442765
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)

# Generated at 2022-06-14 01:57:17.088242
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import transformer_test_utils as utils
    node = utils.run_test(Python2FutureTransformer, utils.get_test_data('future.py'))
    assert node.body[0].module == '__future__'
    assert node.body[1].module == '__future__'
    assert node.body[2].module == '__future__'

# Generated at 2022-06-14 01:57:21.012085
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # type: () -> None
    assert Python2FutureTransformer(None, None).target == (2, 7)

# Generated at 2022-06-14 01:57:22.403895
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None


# Generated at 2022-06-14 01:57:23.604248
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None)

# Generated at 2022-06-14 01:57:25.940875
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer"""
    x: Python2FutureTransformer = Python2FutureTransformer()



# Generated at 2022-06-14 01:57:27.896540
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().target == (2, 7)


# Generated at 2022-06-14 01:57:30.598766
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert issubclass(Python2FutureTransformer, BaseNodeTransformer)


# Generated at 2022-06-14 01:57:39.277605
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    code = imports.get_code()
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    expected_result = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import absolute_import
from future import division
from future import print_function
from future import unicode_literals"""
    assert ast.dump(tree) == ast.dump(ast.parse(expected_result))


# Generated at 2022-06-14 01:57:42.048093
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert issubclass(Python2FutureTransformer, BaseNodeTransformer) == True


# Generated at 2022-06-14 01:57:52.394128
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('a = 100 + 200')
    transformer = Python2FutureTransformer()
    t = transformer.visit(node)

# Generated at 2022-06-14 01:58:01.761399
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse("""
    import math

    x = 1
    """)
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)

# Generated at 2022-06-14 01:58:07.908649
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..transformer import Transformer
    from ..utils.source_code import SourceCode
    from typing import Union, Any
    from ..utils.code_generator import to_source

    transformer = Transformer(Python2FutureTransformer)

# Generated at 2022-06-14 01:58:12.841251
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from .. import ELLIPSIS
    source = """
str_a = 'Hello'
str_b = 'world'
str_c = str_a + ' ' + str_b
    """
    tree = ast.parse(source)
    Python2FutureTransformer().visit(tree)
    assert ast.dump(tree) == ELLIPSIS

# Generated at 2022-06-14 01:58:24.222366
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Save the result of method visit_Module of class Python2FutureTransformer
    # in file 'tests/results/visit_Module.out'
    # and test the content of result against file 'tests/results/visit_Module.expect'
    source = """
"""
    expected_result = ""

    import astor
    from typing import Dict, List
    from ..utils.test_utils import run_test, test_tree_changed

    import_nodes = []

    def test_visit_Module(tree_changed: bool, result: ast.Module):
        if tree_changed:
            assert result == astor.parse(expected_result)

    transformer = Python2FutureTransformer()
    run_test(transformer, test_visit_Module, source, expected_result, import_nodes)
    test_tree_

# Generated at 2022-06-14 01:58:25.169938
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()



# Generated at 2022-06-14 01:58:27.703616
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    visitor = Python2FutureTransformer()
    assert visitor.target == (2, 7)
    assert visitor.visit_Module == Python2FutureTransformer.visit_Module

# Generated at 2022-06-14 01:58:28.724061
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:58:30.058562
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().target == (2, 7)


# Generated at 2022-06-14 01:58:39.401286
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse("""
a = 5
""")
    node = Python2FutureTransformer().visit(tree)
    assert isinstance(node, ast.Module)
    assert isinstance(node.body[0], ast.ImportFrom)
    assert node.body[0].module == '__future__'
    assert node.body[0].names[0].name == 'absolute_import'
    assert node.body[1].names[0].name == 'division'
    assert node.body[2].names[0].name == 'print_function'
    assert node.body[3].names[0].name == 'unicode_literals'
    assert isinstance(node.body[4], ast.Assign)
    assert isinstance(node.body[4].value, ast.Num)

# Generated at 2022-06-14 01:58:40.963463
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Just exercise the constructor.
    Python2FutureTransformer()

# Generated at 2022-06-14 01:58:43.969818
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.Module(body=[])
    tn = Python2FutureTransformer()
    node = tn.visit(node)  # type: ignore
    assert node is not None

# Generated at 2022-06-14 01:59:01.668403
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """\
for i in range(5):
    if i > 3:
        print(i)"""
    expected = """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
for i in range(5):
    if i > 3:
        print(i)"""
    tree = ast.parse(source)  # type: ignore
    Python2FutureTransformer().visit(tree)
    actual = astunparse.unparse(tree)  # type: ignore
    assert actual == expected

# Generated at 2022-06-14 01:59:10.112685
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .utils import assert_equal_ast
    code = """print('a')"""
    tree = ast.parse(code)
    Python2FutureTransformer.run(tree)
    assert_equal_ast(
        # note that untyped_ast does not support __future__ imports
        dedent("""
            from __future__ import absolute_import
            from __future__ import division
            from __future__ import print_function
            from __future__ import unicode_literals

            print('a')
        """),
        tree,
    )

# Generated at 2022-06-14 01:59:17.250749
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..parser import parse
    from ..utils.source import source
    node = parse(source('tests/samples/sample21_py2_import.py'))
    t = Python2FutureTransformer()
    node = t.visit(node)
    assert source(node) == source('tests/samples/sample21_py2_import_transformed.py')

# Generated at 2022-06-14 01:59:24.773950
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor  # type: ignore

    source = """
x = 1 + 1
"""
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = 1 + 1\n"""

    tree = astor.parse_file(StringIO(source))  # type: ignore
    Python2FutureTransformer().visit(tree)
    result = astor.to_source(tree).strip()

    assert result == expected

# Generated at 2022-06-14 01:59:31.747158
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    test_code = '''
    import x
    import y
    '''
    expected_code = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    
    import x
    import y
    '''

    tree = ast.parse(test_code)
    tree = Python2FutureTransformer().visit(tree)
    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 01:59:34.357224
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseNodeTransformer)



# Generated at 2022-06-14 01:59:37.728879
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None


if __name__ == '__main__':
    test_Python2FutureTransformer()

# Generated at 2022-06-14 01:59:45.437750
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """import x
x = 1
"""
    expected_code = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import x
x = 1
"""
    node = ast.parse(code)
    assert expected_code == Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 01:59:52.259588
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import parse
    from typed_ast.ast3 import SyntaxError
    from .util import transform 
    source = '''
a = 10
b = 11
'''
    
    node = parse(source)
    transformer = Python2FutureTransformer()
    new_node = transform(transformer, node)
    code = compile(new_node, '<test>', 'exec')
    globals = {}
    exec(code, globals)
    assert globals['a'] == 10
    assert globals['b'] == 11

# Generated at 2022-06-14 01:59:53.200636
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    print(Python2FutureTransformer())


# Generated at 2022-06-14 02:00:09.147796
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:10.326608
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t is not None


# Generated at 2022-06-14 02:00:19.923340
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .test_utils import Generator
    import unittest
    class T(unittest.TestCase):
        def test_Python2FutureTransformer_constructor_1(self):
            trans = Python2FutureTransformer(None)
            self.assertEqual(trans.target, (2, 7))
    def get_suite():
        return unittest.TestLoader().loadTestsFromTestCase(T)
    def get_tests():
        suite = get_suite()

# Generated at 2022-06-14 02:00:30.088923
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .codegen import Python2CodeGenerator
    from ..tokens import python_tokens
    from ..parser import Python2Parser

    parser = Python2Parser(python_tokens)
    code = parser.parse_string(imports.get_body(future='__future__'))
    code.visit(Python2FutureTransformer())
    assert code.visit(Python2CodeGenerator()) == '''\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
'''

# Generated at 2022-06-14 02:00:39.012529
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast3

    class Python2FutureTransformer(BaseNodeTransformer):
        """Prepends module with:
            from __future__ import absolute_import
            from __future__ import division
            from __future__ import print_function
            from __future__ import unicode_literals

        """
        target = (2, 7)

        def visit_Module(self, node: ast3.Module) -> ast3.Module:
            self._tree_changed = True
            node.body = im.get_body(future='__future__') + node.body  # type: ignore
            return self.generic_visit(node)  # type: ignore
            
    ct = ast3.parse('')
    ct.body = [ct.body[1]]

# Generated at 2022-06-14 02:00:40.150719
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()

# Generated at 2022-06-14 02:00:53.338564
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from ..utils.source_code import source
    from ..utils.unparse import Unparser
    class Python2FutureTransformer(BaseNodeTransformer):
        """Prepends module with:
            from __future__ import absolute_import
            from __future__ import division
            from __future__ import print_function
            from __future__ import unicode_literals
                
        """
        target = (2, 7)

        def visit_Module(self, node: ast.Module) -> ast.Module:
            self._tree_changed = True
            node.body.insert(0, ast.parse("from __future__ import absolute_import\n").body[0])

# Generated at 2022-06-14 02:00:59.147417
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    p2ft = Python2FutureTransformer()
    assert type(p2ft) == Python2FutureTransformer
    assert p2ft.target == (2, 7)
    assert type(p2ft._tree_changed) == bool
    assert p2ft._tree_changed == False


# Generated at 2022-06-14 02:01:00.524959
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

# Generated at 2022-06-14 02:01:01.118806
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 02:01:36.266951
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse("")
    Python2FutureTransformer().visit(node)
    expected = ast.Module([imports.get_node(future='__future__')])  # type: ignore
    assert_ast_equal(expected, node)

# Generated at 2022-06-14 02:01:40.376108
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('<snippet>')
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    module = ast.Module(body=imports.get_body() + [])
    assert ast.dump(module) == ast.dump(node)

# Generated at 2022-06-14 02:01:44.342668
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse("print('hello')")
    Python2FutureTransformer().visit(node)
    assert ast.dump(node) == imports.get_tree(future='__future__').dump() + ast.dump(node)

# Generated at 2022-06-14 02:01:46.995154
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor

# Generated at 2022-06-14 02:01:51.398885
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert isinstance(x, Python2FutureTransformer)
    assert isinstance(x, BaseNodeTransformer)
    assert hasattr(x, 'target')
    assert hasattr(x, 'visit_Module')


# Generated at 2022-06-14 02:02:00.681399
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Initialize
    node = ast.parse(textwrap.dedent("""\
        import sys
        print("hello")
        """))

    # Run transformer
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    # Basic tests
    assert transformer.tree_changed is True
    assert isinstance(new_node, ast.Module)
    assert isinstance(new_node, ast.AST)

    # Test new_node
    assert new_node.body[0].module == '__future__'
    assert new_node.body[1].module == '__future__'
    assert new_node.body[2].module == '__future__'
    assert new_node.body[3].module == '__future__'

# Generated at 2022-06-14 02:02:11.429443
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformer import transform_ast
    from ..visitor import ASTNodeVisitor
    from ..utils.ast_helpers import get_ast_from_source
    from ..utils.source_helpers import dedent

    source = dedent("""
    import os

    def foo():
        print("Hallo")

    if __name__ == '__main__':
        foo()
    """)
    expected_source = dedent("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import os

    def foo():
        print("Hallo")

    if __name__ == '__main__':
        foo()
    """)

    tree = get_ast_from_source(source)


# Generated at 2022-06-14 02:02:13.605738
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # type: () -> None
    transformer = Python2FutureTransformer(None, None)
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 02:02:23.140563
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source
    from ..utils.ast import get_ast, get_changed_ast
    from .base import COMPATIBLE_VERSIONS

    source_ = source(
        '''
        def fn():
            pass
    '''
    )

    ast_ = get_ast(
        source_,
        min_python_version=COMPATIBLE_VERSIONS[0],
    )

    python2futuretransformer = Python2FutureTransformer()
    python2futuretransformer.visit(ast_)
    changed_ast = get_changed_ast(
        ast_,
        python2futuretransformer,
        min_python_version=COMPATIBLE_VERSIONS[0],
    )


# Generated at 2022-06-14 02:02:24.457655
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

# Generated at 2022-06-14 02:03:39.451773
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import logging
    logger = logging.getLogger(__file__)


# Generated at 2022-06-14 02:03:44.853684
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sys

    try:
        sys.modules.pop('typed_ast', None)
    except KeyError:
        pass

    assert Python2FutureTransformer(2).visit(ast.parse(
        'import os')) == \
        ast.parse('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import os''')

# Generated at 2022-06-14 02:03:55.148557
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert imports.get_body(future='__future__') == [
        ast.ImportFrom(module='future',
                       names=[ast.alias(name='absolute_import',
                                        asname=None)],
                       level=0),
        ast.ImportFrom(module='future',
                       names=[ast.alias(name='division',
                                        asname=None)],
                       level=0),
        ast.ImportFrom(module='future',
                       names=[ast.alias(name='print_function',
                                        asname=None)],
                       level=0),
        ast.ImportFrom(module='future',
                       names=[ast.alias(name='unicode_literals',
                                        asname=None)],
                       level=0)]

# Generated at 2022-06-14 02:04:00.228622
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    new_node = Python2FutureTransformer().visit(ast.parse('pass'))
    expected_node = ast.parse(''.join(imports.get_body(future='__future__')) + 'pass')
    ast.fix_missing_locations(expected_node)
    assert ast.dump(new_node) == ast.dump(expected_node)

# Generated at 2022-06-14 02:04:05.024944
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..transpile import Transpiler

    t = Transpiler(target='2')
    t.register_transformers([Python2FutureTransformer])
    assert t.transform_code('x=1') == 'import __future__\nx=1'

# Generated at 2022-06-14 02:04:12.716848
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ in globals(), 'You need to rename the class'
    assert Python2FutureTransformer.__doc__ is not None, 'You need to write a docstring'
    assert Python2FutureTransformer.target == (2, 7), 'Set correct Python 2.7 version as a target version'
    assert type(Python2FutureTransformer({}).transform('', ''.split())) is str, \
        'You need to return string as a result of transformation'

# Generated at 2022-06-14 02:04:16.436430
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    f1 = Python2FutureTransformer()
    assert 'Python2FutureTransformer' in f1.__repr__()
    assert f1.target == (2, 7)



# Generated at 2022-06-14 02:04:27.136430
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..conftest import get_function_ast, get_module_ast, get_class_ast
    
    # Test on a module
    code = '''
        def func():
            return True
        '''
    source = dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        {code}
    '''.format(code=code))
    expected_ast = get_module_ast(source)
    
    node = get_module_ast(code)
    actual_ast = Python2FutureTransformer().visit(node)
    assert expected_ast == actual_ast
    
    # Test on a function
    code = 'def func(): return True'

# Generated at 2022-06-14 02:04:36.245001
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Set up test data
    import string
    import random
    import astor
    from ..base import BaseNodeTransformer
    from ..utils.sample import SampleNodeTransformer
    from ..utils.fuzz import FuzzyASTGenerator
    from ..utils.setup import setup_module

    # Set up test data
    configs = [
        dict(target=(2, 7))
    ]
    nodes = [ast.Module]
    functions = [SampleNodeTransformer.visit_Module]
    settings = dict(
        max_attributes=2,
        max_nodes=2,
        random_imports=False
    )
    # Generate random test data

# Generated at 2022-06-14 02:04:37.561441
# Unit test for method visit_Module of class Python2FutureTransformer