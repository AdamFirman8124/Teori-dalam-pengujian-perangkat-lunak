

# Generated at 2022-06-14 01:54:58.501278
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)
    assert t.future == None


# Generated at 2022-06-14 01:55:00.255985
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:55:06.174422
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from astor import to_source
    from astor.code_gen import NodeVisitor
    import ast
    import sys

    node = ast.parse('')
    node = Python2FutureTransformer().visit(node)
    print(to_source(node))

# Generated at 2022-06-14 01:55:13.376817
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    snippet1 = """
        def func(a, b):
            return a + b
    """
    snippet2 = """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        def func(a, b):
            return a + b
    """
    t = Python2FutureTransformer()
    node1 = ast.parse(snippet1.strip(), mode='exec')
    node2 = ast.parse(snippet2.strip(), mode='exec')
    t.visit(node1)
    assert ast.dump(node1) == ast.dump(node2)

# Generated at 2022-06-14 01:55:20.213401
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import Module
    from ast_tools.transforms.future import Python2FutureTransformer

    module = Module(body=[])
    transformer = Python2FutureTransformer(module)

    module = transformer.visit(module)
    # print(module)
    assert transformer._tree_changed
    assert module.body[0].body[0].names[0].asname == 'unicode_literals'

# Generated at 2022-06-14 01:55:21.902095
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..optimizer import optimize_ast
    from ..utils.source import source_to_ast
    from ..utils.ast2code import ast2code

# Generated at 2022-06-14 01:55:25.733994
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    l1 = ast.Module(body=[])
    l2 = ast.Module(body=imports.get_body(future='__future__'))
    trans = Python2FutureTransformer()
    assert l1 != trans.visit(l1)
    assert l2 == trans.visit(l1)

# Generated at 2022-06-14 01:55:33.798032
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformer import Transformer
    from ..utils import source
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, '../../examples/simple_2to3.py')
    transformer = Transformer(path)
    transfomer = Python2FutureTransformer(transformer)
    transformer.register_transformer(transfomer)
    transformer.transform()
    with open(path) as f:
        assert f.read() == source("""
        def main():
            print "Hello, world!\\n"
        """)

# Generated at 2022-06-14 01:55:35.415307
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert(x._tree_changed == False)



# Generated at 2022-06-14 01:55:46.245248
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    transformer = Python2FutureTransformer()
    node = ast.parse('''
    import sys
    ''')  # type: ignore
    transformer.visit(node)

# Generated at 2022-06-14 01:55:54.975787
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    core_transforms = [Python2FutureTransformer]
    source = 'a = 2'
    expected = 'from __future__ import absolute_import\n' + \
               'from __future__ import division\n' + \
               'from __future__ import print_function\n' + \
               'from __future__ import unicode_literals\n' + \
               '\n' + \
               'a = 2\n'
    result = apply_transforms(source, core_transforms, target=(2, 7))
    assert result == expected

# Generated at 2022-06-14 01:55:58.979275
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    x = Python2FutureTransformer()
    y = x.transform(ast.parse("a=1"))
    assert astor.to_source(y) == imports.get_code(future='__future__') + '\na=1\n'

# Generated at 2022-06-14 01:55:59.945351
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert repr(Python2FutureTransformer())

# Generated at 2022-06-14 01:56:05.090151
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.parse('import os')
    assert transformer.visit(node) == ast.parse('''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
''')

# Generated at 2022-06-14 01:56:06.049518
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__doc__ is not None

# Generated at 2022-06-14 01:56:08.074353
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert repr(x) == '<Python2FutureTransformer>'

# Generated at 2022-06-14 01:56:09.079610
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()


# Generated at 2022-06-14 01:56:10.592597
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None


# Generated at 2022-06-14 01:56:21.130389
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from textwrap import dedent

    from typed_ast.ast3 import parse

    class_code = """
    class Foo:
        pass
    """
    import_code = dedent("""
    from __future__ import print_function  # see typed_ast.ast3.__future__
    from __future__ import unicode_literals
    from __future__ import absolute_import
    from __future__ import division""")

    test_classes_code = dedent("""
    class A:
        pass
    class B:
        pass
    """)
    test_classes_code_with_imports = dedent("""
    {0}    
    class A:
        pass
    class B:
        pass
    """.format(import_code))
    test_classes_code_with_imports_str = dedent

# Generated at 2022-06-14 01:56:27.430863
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = '''
    def a():
        """return something"""
        return 2
    '''
    tree = ast.parse(code)
    transformer = Python2FutureTransformer()
    new_tree = transformer.visit(tree)

# Generated at 2022-06-14 01:56:34.382064
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    test_str = ''
    expected_str = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
'''
    node = ast.parse(test_str)
    Python2FutureTransformer().visit(node)
    actual_str = astor.to_source(node)
    assert actual_str == expected_str, f'Expected\n{expected_str}\nbut got\n{actual_str}'

# Generated at 2022-06-14 01:56:40.794900
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Create an instance of Python2FutureTransformer
    t = Python2FutureTransformer()
    
    # Instantiate a Module node, 
    node = ast.parse('import sys')
    # Run the Module node through the visitor, get the modified node
    modified_node = t.visit(node)

    # Print the modified node, check the output
    print(ast.dump(modified_node))

# Generated at 2022-06-14 01:56:52.932606
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    parser = ast.cst_to_ast.Python2Parser()
    transformer = Python2FutureTransformer()
    node = parser.parse_module(dedent("""
    import os
    import sys
    import logging
    """).lstrip())
    transformer.visit(node)

# Generated at 2022-06-14 01:56:53.570737
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    with pytest.raises(TypeError):
        Python2FutureTransformer()

# Generated at 2022-06-14 01:57:03.926671
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_case import TransformerTestCase
    from ..utils import evaluate_ast

    class MockModules(object):
        def __enter__(self):
            self.mock = {}
            imports.get_body(future='__future__')
            self.mock.update(imports.mock)
            return self.mock

        def __exit__(self, exc_type, exc_val, exc_tb):
            imports.unmock()

    test = TransformerTestCase(Python2FutureTransformer)

# Generated at 2022-06-14 01:57:05.546695
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
	assert Python2FutureTransformer().visit(ast.parse("import json")) == '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json'''


# Generated at 2022-06-14 01:57:09.767547
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    node = ast.parse('import numpy as np')
    out_ast_orig = astor.to_source(node)

    transformer = Python2FutureTransformer()
    out_visited_node = transformer.visit(node)
    out_ast = astor.to_source(out_visited_node)
    #print(out_ast)
    assert "from __future__ import absolute_import\n" in out_ast
    assert "from __future__ import division\n" in out_ast
    assert "from __future__ import print_function\n" in out_ast
    assert "from __future__ import unicode_literals\n" in out_ast
    assert out_ast_orig in out_ast

# Generated at 2022-06-14 01:57:13.533584
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    result = transformer.visit(ast.parse('var = 1'))
    assert str(result) == str(ast.parse('import __future__\nvar = 1'))

# Generated at 2022-06-14 01:57:21.433141
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_ = ast.parse(
        '''
        test = ['print', 1]
        '''
    )

    module = Python2FutureTransformer().visit(module_)
    result = ast.dump(
        module
    )

# Generated at 2022-06-14 01:57:22.403358
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()


# Generated at 2022-06-14 01:57:33.456589
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.tree_changed == False
    assert transformer.target == (2, 7)
    assert transformer.visit_Module(ast.Module([ast.Pass()])) == ast.Module(imports.get_body(future='__future__') + [ast.Pass()])  # type: ignore


# Generated at 2022-06-14 01:57:34.849469
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ptpython
    ptpython.__all__

# Generated at 2022-06-14 01:57:37.524836
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == "Python2FutureTransformer"

# Tests for method visit_Module

# Generated at 2022-06-14 01:57:51.117029
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    def get_tree():
        import astor
        m = ast.parse('1')
        m.body.insert(0, ast.Expr(ast.Str('# random comment')))
        return astor.to_source(m, indent_with=' '*4)

    transformer = Python2FutureTransformer()
    node = ast.parse(get_tree())
    transformer.visit(node)

    expected = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    # random comment
    1'''
    assert transformer._tree_changed
    assert astor.to_source(node) == expected

# Generated at 2022-06-14 01:58:01.634070
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .fixtures.simple_module import c as module_c
    from ast_toolbox.context import Context
    context = Context()
    transformer = Python2FutureTransformer(context, module_c)
    module_body = module_c.body
    node_body = transformer.visit(module_body)
    import astdump
    result = astdump.dump_ast(node_body)
    print(result)

# Generated at 2022-06-14 01:58:09.841919
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    s = ''' 
        class Something:
            def __init__(self):
                self.name = "something"
        '''
    tree = ast.parse(s)
    t = Python2FutureTransformer()
    t.visit(tree)
    # test that we have indeed prepended the module with `from __future__ import ...`
    assert "from __future__ import absolute_import" in ast.dump(tree)
    assert "from __future__ import division" in ast.dump(tree)
    assert "from __future__ import print_function" in ast.dump(tree)
    assert "from __future__ import unicode_literals" in ast.dump(tree)

# Generated at 2022-06-14 01:58:15.833390
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from pprint import pprint
    from typed_ast import ast3 as ast
    from typed_ast import parse

    # Tests for Python2FutureTransformer
    #
    # TODO:
    #   - value_specifiers: list[ast.expr]
    class Python2FutureTransformerTestCase(unittest.TestCase):
        def assertIsModule(self, module: ast.Module):
            self.assertIsInstance(module, ast.Module)

        def assertInTree(self, module: ast.Module, tree_str: str):
            pprint(ast.dump(module))
            self.assertTrue(tree_str in ast.dump(module))


# Generated at 2022-06-14 01:58:17.201156
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None
    

# Generated at 2022-06-14 01:58:20.087251
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Test that the constructor of the class Python2FutureTransformer works as expected."""
    try:
        Python2FutureTransformer()
    except Exception:
        assert False


# Generated at 2022-06-14 01:58:21.122740
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()



# Generated at 2022-06-14 01:58:42.154265
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test for method visit_Module of class Python2FutureTransformer."""
    from typed_ast import ast3 as ast
    from typed_ast.transforms import TypedImportFinder
    transformer = Python2FutureTransformer()
    assert transformer._tree_changed is False
    module = ast.parse("print('123')")
    module = transformer.visit(module)  # type: ignore
    assert transformer._tree_changed is True
    assert len(module.body) == len(imports.get_body(future='__future__')) + 1
    assert isinstance(module.body[0], ast.ImportFrom)
    assert module.body[0].module == '__future__'
    assert isinstance(module.body[1], ast.ImportFrom)
    assert module.body[1].module == '__future__'

# Generated at 2022-06-14 01:58:51.470637
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = '''
    import datetime
    import os
    import sys
    from future import unicode_literals
    from future import absolute_import
    from . import now

    def test():
        return datetime.datetime.now()
    '''
    tree = ast.parse(code)
    Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 01:58:54.350663
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Transformer = Python2FutureTransformer
    assert Transformer.target == (2, 7)

    assert Transformer(verbose=False).verbose == False
    assert Transformer(verbose=True).verbose == True

# Generated at 2022-06-14 01:59:08.048003
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # tree with imports
    tree = ast.parse("""from __future__ import print_function
from future import unicode_literals
print("Hello world!")
""")
    transformer = Python2FutureTransformer(target=(2, 7))
    transformer.visit(tree)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 01:59:10.148769
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert repr(t) == Python2FutureTransformer.__module__ + '.' + Python2FutureTransformer.__qualname__



# Generated at 2022-06-14 01:59:23.009230
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ..utils.singleton import NodeTransformerSingleton
    tree = astor.parse_file(r'C:\Users\troye\Documents\Programming\Python\Scripts\py2to3\test_data\test_py2to3\imports.py')
    tree.body = Python2FutureTransformer().visit(tree)
    print(astor.to_source(tree))
    tree = astor.parse_file(r'C:\Users\troye\Documents\Programming\Python\Scripts\py2to3\test_data\test_py2to3\print_function.py')
    tree.body = Python2FutureTransformer().visit(tree)
    print(astor.to_source(tree))


# Generated at 2022-06-14 01:59:33.447142
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test for method visit_Module of class Python2FutureTransformer"""

    # Get the AST of:
    #   foo = 'foo'
    #   bar = 'bar'
    node = ast.parse("""
        foo = 'foo'
        bar = 'bar'
    """, mode='eval')

    # Declare the transformer
    transformer = Python2FutureTransformer()

    # Apply the transformer
    node = transformer.visit(node)

    # Check if the transformer has changed the tree
    assert transformer._tree_changed is True

    # Check if the transformer has changed the tree
    assert transformer._tree_changed is True

    # Check the result

# Generated at 2022-06-14 01:59:40.027548
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ...parser import parse_str
    node = parse_str('x = 1', mode='exec')
    expected = parse_str(imports.get_code(future='__future__') + 'x = 1', mode='exec')
    actual = Python2FutureTransformer().visit(node)
    assert expected == actual

# Generated at 2022-06-14 01:59:48.615848
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()

    source = dedent('''
    from sys import version_info
    import sys
    print(version_info)
    print('"Hello, World!"')
    ''')

    expected = dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    from sys import version_info
    import sys
    print(version_info)
    print('"Hello, World!"')
    ''')

    tree = ast.parse(source)
    tree = transformer.visit(tree)  # type: ignore
    result = compile(tree, '', 'exec')

    assert expected.strip() == ast.unparse(tree).strip()
    assert transformer._tree

# Generated at 2022-06-14 01:59:58.206496
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # type: () -> None
    
    from typed_ast import ast3, parse
    
    source = """
    from __future__ import print_function
    from __future__ import unicode_literals
    
    x = 5
    """

    tree = parse(source)
    t = Python2FutureTransformer()
    t.visit(tree)
    # print(astunparse.unparse(tree))
    
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 3
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert isinstance(tree.body[1], ast.ImportFrom)
    assert isinstance(tree.body[2], ast.Assign)
    assert tree.body[2].value.value == 5

# Generated at 2022-06-14 02:00:32.135718
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    test_tree = ast.parse('from __future__ import unicode_literals')
    transformer = Python2FutureTransformer(from_version=3)
    transformer.visit(test_tree)
    assert_equal(ast.dump(test_tree), 'Module(body=[ImportFrom(module=\'__future__\', names=[alias(name=\'unicode_literals\', asname=None)], level=0)])')

# Generated at 2022-06-14 02:00:33.758411
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:34.873872
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:49.426237
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    import libcst as cst
    from libcst.metadata import PositionProvider
    from ..utils.linespace import Linespace
    from .base import BaseMetadataWrapper

    code = '''a = 1'''
    module = ast.parse(code)
    metadata = PositionProvider()
    metadata = Linespace.add_newlines(metadata, code)
    metadata = BaseMetadataWrapper(metadata)

    Python2FutureTransformer().visit(module)  # type: ignore
    new_code = cst.MetadataWrapper(module).code
    # print(new_code)

# Generated at 2022-06-14 02:00:53.640017
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class DummyNodeTransformer(NodeTransformer):
        def __init__(self):
            super().__init__()

    transformer = Python2FutureTransformer(DummyNodeTransformer())
    assert tuple(transformer.target) == (2, 7)
    assert transformer._tree_changed is False
    assert transformer._transformer is DummyNodeTransformer


# Generated at 2022-06-14 02:01:01.752182
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor

    node = ast.parse('print("Hello")\n')
    transformer = Python2FutureTransformer(target=(2, 7))

    transformed = transformer.visit(node)
    expected = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("Hello")
"""

    assert astor.to_source(transformed) == expected

# Generated at 2022-06-14 02:01:07.991219
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ast_tools.transformers import Python2FutureTransformer
    import asttokens
    """
    def greet(name):
        return 'Hello ' + name
    """

# Generated at 2022-06-14 02:01:09.562962
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:11.391013
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import parse


# Generated at 2022-06-14 02:01:16.291983
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ..utils.fixtures import future_import as __future__

    source = """\
x = 1
print("x = {}".format(x))
"""
    tree = ast.parse(source)
    Python2FutureTransformer().visit(tree)
    expected = """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = 1
print("x = {}".format(x))
"""
    assert astor.to_source(tree) == expected

# Generated at 2022-06-14 02:02:18.175629
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer"""
    parser = ast.parse(imports.get_ast())
    tree = Python2FutureTransformer()(parser)
    assert isinstance(tree, ast.Module)

# Generated at 2022-06-14 02:02:19.311870
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Test if class exists
    Python2FutureTransformer()



# Generated at 2022-06-14 02:02:27.484746
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    text = '''
        import numpy as np
        x = np.array([1, 2, 3])
        print(x)
    '''
    expected = '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
    
        import numpy as np
        x = np.array([1, 2, 3])
        print(x)
    '''
    tree = ast.parse(text)

    visitor = Python2FutureTransformer()
    visitor.visit(tree)

    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:02:31.025429
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    transformer = Python2FutureTransformer()
    source = textwrap.dedent("""
        """)
    root_node = ast.parse(source)
    expected = textwrap.dedent("""
          from __future__ import absolute_import
          from __future__ import division
          from __future__ import print_function
          from __future__ import unicode_literals
        """)

    transformed_node = transformer.visit(root_node)
    transformed_src = astunparse.unparse(transformed_node).strip()
    assert transformed_src == expected

# Generated at 2022-06-14 02:02:32.834443
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.target == (2, 7)


# Generated at 2022-06-14 02:02:40.530047
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.mock import MockNodeTransformer
    from typed_ast import ast3 as ast

    source = """
        def foo():
            pass
    """
    expected = """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        def foo():
            pass
    """
    tree = ast.parse(source)
    visitor = MockNodeTransformer(Python2FutureTransformer)
    new_tree = visitor.visit(tree)
    assert ast.dump(new_tree) == expected

# Generated at 2022-06-14 02:02:49.094580
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..common import File
    from .utils import transform_and_compare

    with File('test_module.py', 'w') as f:
        f.write('')

    new_content = transform_and_compare(
        Python2FutureTransformer,
        'test_module.py',
        'test_module.py',
    )

    assert 'from __future__ import absolute_import' in new_content
    assert 'from __future__ import division' in new_content
    assert 'from __future__ import print_function' in new_content
    assert 'from __future__ import unicode_literals' in new_content

# Generated at 2022-06-14 02:02:53.529531
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    future_transformer = Python2FutureTransformer()
    assert repr(future_transformer) == '<Python2FutureTransformer>'
    assert future_transformer._tree_changed == False
    assert callable(future_transformer.visit_Module) == True
    assert callable(future_transformer.visit) == True
    assert callable(future_transformer.generic_visit) == True


# Generated at 2022-06-14 02:03:03.575495
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from typed_ast import convert
    import astor
    from .base import BaseNodeTransformer

    class TestTransformer(BaseNodeTransformer):
        def visit_Assign(self, node):
            node.value.n = 10  # type: ignore
            return self.generic_visit(node)  # type: ignore

        def visit_Expr(self, node):
            if isinstance(node.value, ast.Str):
                node.value = ast.Name(id="True", ctx=ast.Load())  # type: ignore
            return self.generic_visit(node)  # type: ignore
    

# Generated at 2022-06-14 02:03:06.845013
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert issubclass(Python2FutureTransformer, BaseNodeTransformer)
    assert not issubclass(Python2FutureTransformer, ast.AST)
    Python2FutureTransformer()
