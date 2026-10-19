

# Generated at 2022-06-14 01:55:00.835677
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ast_visitor import ASTVisitor

    class ModuleVisitor(ASTVisitor):
        def visit_Module(self, node: ast.Module) -> None:
            print(ast.dump(node))


# Generated at 2022-06-14 01:55:10.160593
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import make_test_module
    from ..utils.testing import assert_text_transformer
    from ..utils.visitor import dump_ast
    from .inline import InlineAssignmentsTransformer
    import_future = ['from __future__ import absolute_import',
                     'from __future__ import division',
                     'from __future__ import print_function',
                     'from __future__ import unicode_literals',
                     ]
    source = '''
            def func():
                "docstring"
                print("hello")
            '''
    test_module = make_test_module(source, target_python_version=(2, 7))
    test_module = InlineAssignmentsTransformer().visit(test_module)  # type: ignore

# Generated at 2022-06-14 01:55:23.477843
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    test_node = ast.parse('print(x)')
    assert Python2FutureTransformer.transform_single_node(test_node).body[0].body[0].value.func.id == 'print'
    assert Python2FutureTransformer.transform_single_node(test_node).body[0].body[1].value.func.id == 'print'
    assert Python2FutureTransformer.transform_single_node(test_node).body[0].body[2].value.func.id == 'print'
    assert Python2FutureTransformer.transform_single_node(test_node).body[0].body[3].value.func.id == 'print'
    assert Python2FutureTransformer.transform_single_node(test_node).body[0].body[4].value.func.id == 'print'
    assert Python2

# Generated at 2022-06-14 01:55:29.957359
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    @snippet
    def before(name):
        print('Hello, World!')

    @snippet
    def after(name):
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        print('Hello, World!')

    b = ast.parse(before.get_source("", name=None))
    a = ast.parse(after.get_source("", name=None))

    c = Python2FutureTransformer()
    d = c.visit(b)
    assert ast.dump(a) == ast.dump(d)

# Generated at 2022-06-14 01:55:35.763774
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    test_tree = ast.parse('from __future__ import with_statement')
    transformer.visit(test_tree)
    expected_tree = ast.parse('''from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    from __future__ import with_statement''')
    assert ast.dump(test_tree) == ast.dump(expected_tree)

# Generated at 2022-06-14 01:55:38.820749
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import assert_transformed

    assert_transformed(Python2FutureTransformer(), 'a = 1')


# pylint: disable=R0903

# Generated at 2022-06-14 01:55:49.274931
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer(ast.parse('pass'), (2, 7))
    new_tree = transformer.visit(transformer.tree)
    print(ast.dump(new_tree))

# Generated at 2022-06-14 01:55:56.779849
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    from ..utils import setup_ast_node
    from ..utils.testutils import transform_and_compare_ast

    # Changing
    transform_and_compare_ast(Python2FutureTransformer, '''
        pass
    ''', '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        pass
    ''')

    # Not changing
    transform_and_compare_ast(Python2FutureTransformer, '''
        pass
        pass
    ''', '''
        pass
        pass
    ''')

# Generated at 2022-06-14 01:56:04.681609
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    src = '''
    def func():
        pass
    '''

    expected = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals


    def func():
        pass
    '''

    tree = ast.parse(src)
    Python2FutureTransformer().visit(tree)
    actual = astor.to_source(tree)

    assert_source_equal(actual, expected)


# Generated at 2022-06-14 01:56:07.494311
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('def f(): pass')
    module = Python2FutureTransformer().visit(module)
    assert module.body[0].lineno == 4


# Generated at 2022-06-14 01:56:17.048602
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    source = 'print "42"'
    tree = ast.parse(source)
    Python2FutureTransformer().visit(tree)
    result = astor.to_source(tree)
    expect = '''\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print "42"
'''
    assert result == expect

# Generated at 2022-06-14 01:56:18.606450
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 01:56:24.525864
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse('')
    Python2FutureTransformer().visit(tree)
    assert tree.body[0].value.s == 'absolute_import'
    assert tree.body[1].value.s == 'division'
    assert tree.body[2].value.s == 'print_function'
    assert tree.body[3].value.s == 'unicode_literals'

# Generated at 2022-06-14 01:56:31.790776
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Arrange
    code = """
        import os
        import errno
        import sys
    """
    # Act
    result = Python2FutureTransformer().transform_source(code, 'module')
    # Assert
    assert result[0]
    assert result[1] == """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import os
        import errno
        import sys
    """

# Generated at 2022-06-14 01:56:32.743218
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:37.081785
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = "import sys"
    correct_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    import sys
    """
    module = ast.parse(code)
    Python2FutureTransformer().visit(module)
    assert ast.dump(ast.parse(correct_code)) == ast.dump(module)

# Generated at 2022-06-14 01:56:38.954218
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(2.7).target == (2, 7)

# Generated at 2022-06-14 01:56:39.922204
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:52.198858
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    module = ast.parse("assert 1, '1 == 0'")
    transformer.visit(module)
    assert transformer._tree_changed == True

# Generated at 2022-06-14 01:57:02.460021
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # create a node from the import statement
    import string  # type: ignore
    print(string.hexdigits)
    parsed_node = ast.parse(inspect.getsource(string))
    node = parsed_node.body[0]

    # attempt to convert that node
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    output = astor.to_source(parsed_node)
    # print('output', output)
    assert 'from __future__ import absolute_import' in output
    assert 'from __future__ import division' in output
    assert 'from __future__ import print_function' in output
    assert 'from __future__ import unicode_literals' in output

# Generated at 2022-06-14 01:57:07.666200
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:57:17.066127
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    module = ast.parse('''
        print(1, 2, sep='')
    ''')
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)
    assert list(module.body) == imports.get_body(future='__future__') + [ast.Print(
        values=[ast.Num(1), ast.Num(2)],
        dest=None,
        nl=True,
        sep=''), ast.Expr(value=ast.Str(''))]  # type: ignore

# Generated at 2022-06-14 01:57:25.888705
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast
    from ..utils.ast import dump_ast, dump_code
    source = 'x = 5'
    module = Python2FutureTransformer.build_module(source)


# Generated at 2022-06-14 01:57:28.698760
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('pass')
    Python2FutureTransformer().transform(tree)
    assert compile(tree, '<string>', 'exec')

# Generated at 2022-06-14 01:57:35.151099
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    input_code = """
for i in range(10):
    print(i)
    """
    expected_output = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
for i in range(10):
    print(i)
    """
    tree = ast.parse(input_code)
    tree = Python2FutureTransformer().visit(tree)
    result = astor.to_source(tree)
    print(result)
    assert result == expected_output

# Generated at 2022-06-14 01:57:36.060018
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:38.867574
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 01:57:51.736334
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None)._tree_changed == False
    # check if the function imports() returns body in the expected form
    assert imports.get_body(future='__future__') == [ast.ImportFrom(module='__future__', 
                                                                    names=[ast.alias(name='absolute_import', 
                                                                                     asname=None),
                                                                           ast.alias(name='division',
                                                                                     asname=None),
                                                                           ast.alias(name='print_function',
                                                                                     asname=None),
                                                                           ast.alias(name='unicode_literals',
                                                                                     asname=None)],
                                                                    level=0)]
    # check if the function visit_Module() returns the expected body

# Generated at 2022-06-14 01:57:57.442413
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    node = ast.parse('print(1)')
    obj = Python2FutureTransformer()
    result = obj.visit(node)
    assert astor.to_source(result) == 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\nprint(1)\n'

# Generated at 2022-06-14 01:58:06.311855
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast.ast3 import Module, Expr, Tuple, Str, Name, alias

    node = Module()
    node.body = [Expr(value=Tuple(elts=[Str(s='sub-module1'), Str(s='sub-module2')], ctx=alias(Name(id='', ctx=0), 'sub-modules')))]
    expected = Module()
    expected.body = [
        Expr(value=Tuple(elts=[Str(s='sub-module1'), Str(s='sub-module2')], ctx=alias(Name(id='', ctx=0), 'sub-modules')))
    ]
    assert Python2FutureTransformer().visit(node) == expected

# Generated at 2022-06-14 01:58:24.122874
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Create the instance
    instance = Python2FutureTransformer()

    # Create an ast representation of the source code
    source = """
name = "World"
print("Hello " + name)
"""

    node = ast.parse(source)

    # Call the instance
    instance.visit(node)

    # Test the result
    source = sourcewrap.dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        name = "World"
        print("Hello " + name)
        """)
    node_parse = ast.parse(source)
    assert ast.dump(node) == ast.dump(node_parse)

# Generated at 2022-06-14 01:58:26.266549
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)

# Generated at 2022-06-14 01:58:36.383415
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # arrange
    node = ast.Module(
        body=[
            ast.Assign(
                targets=[
                    ast.Name(
                        id='x',
                        ctx=ast.Store())],
                value=ast.Num(
                    n=2))
        ]
    )

# Generated at 2022-06-14 01:58:38.513940
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None


# Generated at 2022-06-14 01:58:40.314727
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:58:47.045388
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class Test(Python2FutureTransformer):
        pass

    node = ast.parse("""
    x = 3
    """)  # type: ast.Module
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
x = 3
"""
    new_node = Test().visit(node)  # type: ignore
    assert ast.dump(new_node) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 01:58:48.213002
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()


# Generated at 2022-06-14 01:58:55.774540
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    print("Testing Python2FutureTransformer")
    import astor

    # Test 1: Create an AST object without adding a future import
    node = ast.parse('def add(x, y): return x + y')
    assert len(node.body) == 1
    print(astor.dump_tree(node))

    # Test 2: Create an AST object and add a future import
    node = ast.parse('def add(x, y): return x + y')
    Python2FutureTransformer().visit(node)
    assert len(node.body) == 5  # 4 futu

# Generated at 2022-06-14 01:59:08.878956
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from nbconvert.preprocessors import ExecutePreprocessor
    import os
    from nbformat import read, write
    from .notebook_test_util import NotebookTestBase
    from tempfile import NamedTemporaryFile


# Generated at 2022-06-14 01:59:22.133437
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    module = ast.parse('print(1/2)\n')
    assert module.body[0].__class__ == ast.Print
    module = Python2FutureTransformer().visit(module) # type: ignore
    assert module.body[0].__class__ == ast.ImportFrom
    assert module.body[1].__class__ == ast.ImportFrom
    assert module.body[2].__class__ == ast.ImportFrom
    assert module.body[3].__class__ == ast.ImportFrom
    assert module.body[4].__class__ == ast.Print


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from tests.test_transformers import main

# Generated at 2022-06-14 01:59:39.791277
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer"""
    obj = Python2FutureTransformer()
    assert obj.target == (2, 7)


# Generated at 2022-06-14 01:59:41.142690
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert(isinstance(transformer, Python2FutureTransformer))

# Generated at 2022-06-14 01:59:51.333581
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('''
        def f():
            pass
    
        def g():
            pass
    ''')
    tree_visitor = Python2FutureTransformer()
    module = tree_visitor.visit(module)
    source = ast.dump(module)

# Generated at 2022-06-14 01:59:52.736135
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:00:04.348963
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3
    import inspect
    import sys

    class Dummy(ast3.NodeVisitor):
        def visit(self, node, *args, **kwargs):
            return node

        def generic_visit(self, node, *args, **kwargs):
            ast3.NodeVisitor.generic_visit(self, node, *args, **kwargs)
            return node

    class DummyTransformer(Python2FutureTransformer):
        def __init__(self):
            super(DummyTransformer, self).__init__()

        def visit(self, node, *args, **kwargs):
            if node.__class__.__name__ in {'Module', 'Expr'}:
                return node
            return Dummy().visit(node, *args, **kwargs)


# Generated at 2022-06-14 02:00:10.331538
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    code = """# comment
    print("Hello world!")
    """
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    assert code in astor.to_source(tree)
    assert "from __future__ import absolute_import" in astor.to_source(tree)



# Generated at 2022-06-14 02:00:19.267498
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from astor.codegen import to_source
    tree = ast.parse('''
import numpy as np

a = 5
b = 4
c = a*b
print(c)
    ''')
    v = Python2FutureTransformer()
    new_tree = v.visit(tree)
    # print(astor.dump_tree(new_tree))
    source = to_source(new_tree)
    assert source == '''from future import absolute_import
from future import division
from future import print_function
from future import unicode_literals

import numpy as np

a = 5
b = 4
c = a*b
print(c)
'''

# Generated at 2022-06-14 02:00:29.378202
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse(imports.get_body(future='__future__'))
    node = tree.body[0]
    assert isinstance(node, ast.ImportFrom)
    assert node.module == 'future'
    assert node.level == 0
    assert len(node.names) == 4
    assert node.names[0] == ('absolute_import', None)
    assert node.names[1] == ('division', None)
    assert node.names[2] == ('print_function', None)
    assert node.names[3] == ('unicode_literals', None)

# Generated at 2022-06-14 02:00:35.175903
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.tester import node_test
    node_test(Python2FutureTransformer, """\
print("foo")
""", """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("foo")
""")



# Generated at 2022-06-14 02:00:36.627200
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:01:08.912712
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.Module([])
    assert Python2FutureTransformer().visit(node) == ast.Module(
        body=imports.get_body('__future__')  # type: ignore
    )

# Generated at 2022-06-14 02:01:14.860529
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import AstBuilder
    from ..snippets import imports
    from ..utils.source import Source
    from .base import BaseNodeTransformer
    from .python2_future import Python2FutureTransformer


    class test_Python2FutureTransformer_visit_Module(BaseNodeTransformer):
        AST_FIELDS = ('_tree_changed',)


# Generated at 2022-06-14 02:01:25.817493
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = dedent("""\
        #!/usr/bin/env python2
        a = 3
        print(a)
    """)
    # - Test 1
    expected1 = dedent("""\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        #!/usr/bin/env python2
        a = 3
        print(a)
    """)
    node = ast.parse(source)
    Python2FutureTransformer().visit(node)
    assert astunparse.unparse(node) == expected1
    # - Test 2

# Generated at 2022-06-14 02:01:34.453936
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    sut = Python2FutureTransformer()
    source = 'import six'
    tree = ast.parse(source)  # type: ignore
    result = sut.visit(tree)  # type: ignore
    assert ast.dump(result) == ast.dump(ast.parse(
        """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
    
        from six import absolute_import
        from six import division
        from six import print_function
        from six import unicode_literals
        import six
        """))
    assert sut._tree_changed is True

# Generated at 2022-06-14 02:01:37.662070
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer"""
    obj = Python2FutureTransformer()
    assert obj.target == (2, 7)
    assert isinstance(obj, BaseNodeTransformer)


# Generated at 2022-06-14 02:01:39.639253
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
  c = Python2FutureTransformer()
  assert c
  assert c.target == (2, 7)


# Generated at 2022-06-14 02:01:44.494601
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    node = ast.parse('''
import os
import re
''', mode='exec')
    node = Python2FutureTransformer().visit(node)
    print(astor.to_source(node))
# End of file test_Python2FutureTransformer_visit_Module

# Generated at 2022-06-14 02:01:46.521130
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    global Python2FutureTransformer
    assert Python2FutureTransformer


# Generated at 2022-06-14 02:01:50.382126
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('import foo')
    _ = Python2FutureTransformer(node)


# Generated at 2022-06-14 02:02:02.246556
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
    code stuff
    """
    tree = ast.parse(code)
    Python2FutureTransformer().visit(tree)
    assert tree.body[0].module == '__future__'
    assert tree.body[0].name == 'absolute_import'
    assert tree.body[1].module == '__future__'
    assert tree.body[1].name == 'division'
    assert tree.body[2].module == '__future__'
    assert tree.body[2].name == 'print_function'
    assert tree.body[3].module == '__future__'
    assert tree.body[3].name == 'unicode_literals'
    assert tree.body[4].col_offset == 0
    assert tree.body[4].lineno == 2
    assert tree.body[4].s

# Generated at 2022-06-14 02:03:15.510931
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import astor
    from ..utils import dump_ast
    node = ast.Module()
    node.body = [ast.Expr(ast.Str('string'))]
    expected = ast.Module()
    expected.body = [ast.ImportFrom(module='__future__',names=[
            ast.alias(name='absolute_import',asname=None),
            ast.alias(name='division',asname=None),
            ast.alias(name='print_function',asname=None),
        ], level=0),
                     ast.Expr(ast.Str('string'))]
    xformer = Python2FutureTransformer(node)
    actual = xformer.visit(node)
    str_expected = astor.to_source(expected)
    str_actual = astor

# Generated at 2022-06-14 02:03:29.399906
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Unit test for method visit_Module of class Python2FutureTransformer"""

    def parse(code: str) -> ast.Module:
        """Parse code into a typed AST node."""
        return ast.parse(code)

    def dump(node: ast.AST) -> str:
        """Dump a typed AST node to code."""
        # noinspection PyUnresolvedReferences
        return ast.unparse(node)

    # Test method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:03:31.406299
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from pprint import pprint


# Generated at 2022-06-14 02:03:36.748229
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.examples import example_python2_module

    example = example_python2_module()
    t = Python2FutureTransformer()
    example = t.visit(example)
    expected_head = imports.get_head()
    expected_body = examples.get_head()
    actual_head = '\n'.join(map(lambda line: line.strip(), example.split('\n')[:4]))
    assert expected_head == actual_head
    actual_body = '\n'.join(map(lambda line: line.strip(), example.split('\n')[4:]))
    assert expected_body == actual_body
    assert t._tree_changed is True

# Generated at 2022-06-14 02:03:44.388352
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .pythontransformer import PythonTransformer
    from ..utils.pythonparser import PythonParser
    from ..utils.source import Source
    from ..utils.astdump import dump

    class_ = Python2FutureTransformer
    source = Source(text='3 + 4')
    tree = PythonParser().parse(source)
    transformer = class_()
    new_tree = transformer.visit(tree)
    print('===> Resulting tree after applying transformer')
    print(dump(new_tree))
    assert transformer.tree_changed is True
    assert PythonTransformer().visit(new_tree) == PythonTransformer().visit(tree)


# Generated at 2022-06-14 02:03:48.810947
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.setup import setup_test_module
    from ..utils.unparse import Unparser
    meta, result = setup_test_module(Python2FutureTransformer())
    assert Unparser(result).unparse() == imports + meta.node.body



# Generated at 2022-06-14 02:03:58.879449
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    nodes = imports.get_snippet(future='__future__')
    assert len(nodes) == 4
    assert type(nodes[0]) == ast.ImportFrom
    assert nodes[0].module == '__future__'
    assert nodes[0].names[0].name == 'absolute_import'
    assert type(nodes[1]) == ast.ImportFrom
    assert nodes[1].module == '__future__'
    assert nodes[1].names[0].name == 'division'
    assert type(nodes[2]) == ast.ImportFrom
    assert nodes[2].module == '__future__'
    assert nodes[2].names[0].name == 'print_function'
    assert type(nodes[3]) == ast.ImportFrom
    assert nodes[3].module == '__future__'
    assert nodes

# Generated at 2022-06-14 02:04:04.968932
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    snippet.test_node_replacement(
        Python2FutureTransformer,
        'visit_Module',
        ('Module(body=[])', 'Module(body=[...])'),
        ast.parse,
        'Module(body=[])'
    )



# Generated at 2022-06-14 02:04:08.966941
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    nodes_to_test = [ast.Module]
    children_to_test = { ast.Module: [ast.stmt] }
    Python2FutureTransformer.test_transformer_class(nodes_to_test, children_to_test)

# Generated at 2022-06-14 02:04:17.612195
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('def square(x): return x * x', mode='exec')
    transformed_node=Python2FutureTransformer().visit(node)
    assert transformed_node.body[0].targets[0].id == "absolute_import"
    assert transformed_node.body[0].targets[1].id == "division"
    assert transformed_node.body[0].targets[2].id == "print_function"
    assert transformed_node.body[0].targets[3].id == "unicode_literals"
# Test ends