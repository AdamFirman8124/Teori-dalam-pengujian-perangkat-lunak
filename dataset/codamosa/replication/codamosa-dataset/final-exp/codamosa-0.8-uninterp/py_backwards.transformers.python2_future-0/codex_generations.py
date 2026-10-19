

# Generated at 2022-06-14 01:54:58.578134
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .utils import roundtrip
    from . import parse


# Generated at 2022-06-14 01:55:07.216333
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
    import sys
    print('Hello World!')
    """
    node = ast.parse(code)
    Python2FutureTransformer().visit(node)
    new_code = astor.to_source(node)
    # assert new_code == "imports()\n" + code
    assert new_code == imports.get_code(future='__future__') + '\n' + code

# Generated at 2022-06-14 01:55:11.559907
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    visitor = Python2FutureTransformer()
    visitor.visit(ast.parse('def foo(): pass'))
    assert len(visitor.tree.body) == 7

# Generated at 2022-06-14 01:55:13.184156
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is Python2FutureTransformer


# Generated at 2022-06-14 01:55:22.536360
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.testutils import assert_node_transformed
    from ..utils.testutils import get_test_case_as_module
    module = get_test_case_as_module('2-7_future-imports')
    node = module.body[0]
    expected = 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nfrom test_source import *'
    assert_node_transformed(Python2FutureTransformer(), node, expected)

# Generated at 2022-06-14 01:55:24.107082
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert isinstance(Python2FutureTransformer(), Python2FutureTransformer)

# Generated at 2022-06-14 01:55:27.214559
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import six

    # Check that we copy the tree
    t = Python2FutureTransformer()  # type: ignore
    a = b = ast.parse('')
    t.visit(a)
    assert six.PY2 is True
    assert a is not b



# Generated at 2022-06-14 01:55:29.195738
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseNodeTransformer)



# Generated at 2022-06-14 01:55:37.636527
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    original_code = '''
        def f():
            x = 3
            return x
        print(f())
        '''
    expected_code = '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        
        def f():
            x = 3
            return x
        print(f())
        '''
    original_ast = ast.parse(original_code)
    expected_ast = ast.parse(expected_code)
    t = Python2FutureTransformer()
    t.visit(original_ast)
    assert ast.dump(original_ast) == ast.dump(expected_ast)

# Generated at 2022-06-14 01:55:41.384379
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .base import BaseNodeTransformerTest
    source = 'import x'
    expected = imports.format(future='__future__') + '\nimport x'
    result = BaseNodeTransformerTest(Python2FutureTransformer, source)
    assert result == expected

# Generated at 2022-06-14 01:55:53.428300
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    # 1. Basic usage
    code = """
    '''
    Module docstring
    '''

    def hello_world():
        print('hello world')


    if __name__ == '__main__':
        hello_world()
    """
    tree = ast.parse(code)
    expected = """
    '''
    Module docstring
    '''

    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals


    def hello_world():
        print('hello world')


    if __name__ == '__main__':
        hello_world()
    """
    transformer.visit(tree)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 01:56:00.349959
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    transformed_tree = transformer.visit(ast.parse('print("Hello, world")'))
    assert isinstance(transformed_tree, ast.Module)
    assert len(transformed_tree.body) == 5
    assert isinstance(transformed_tree.body[0], ast.ImportFrom)
    assert transformed_tree.body[0].module == '__future__'
    assert transformed_tree.body[0].names[0].name == 'absolute_import'



# Generated at 2022-06-14 01:56:10.434352
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..sanity import generator
    from .. import nodes
    from . import mockbuilder

    # Creating the AST

# Generated at 2022-06-14 01:56:15.742118
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('''for i in range(1):
    print(i)''')
    new_tree = Python2FutureTransformer().visit(tree)
    assert new_tree.body[0].__class__ == future_imports.get_body(future='__future__')[0].__class__  # type: ignore

# Generated at 2022-06-14 01:56:24.747104
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    n = ast.parse(
        """
        # comment
        from os import path
        def f():
            pass
    """
    )
    expected = ast.parse(
        """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        # comment
        from os import path
        def f():
            pass
        """
    )

    t = Python2FutureTransformer()
    new_n = t.visit(n)
    assert ast.dump(new_n, annotate_fields=False, include_attributes=True) == \
           ast.dump(expected, annotate_fields=False, include_attributes=True)
    assert t.tree_changed is True

# Generated at 2022-06-14 01:56:25.973068
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:37.642740
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast2 as ast2
    import sys

    class NodeVisitor(ast2.NodeVisitor):
        def __init__(self):
            self.symbols = []

        def visit_Name(self, node):
            self.symbols.append(node.id)

    source = '''
a = b = 1
c = a + b
print(c)
    '''

    expected = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
a = b = 1
c = a + b
print(c)
    '''

    tree = ast2.parse(source)
    Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 01:56:40.597970
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    a = Python2FutureTransformer()
    assert a._tree_changed == False
    assert a.target == (2, 7)


# Generated at 2022-06-14 01:56:52.790733
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse(dedent('''
        def fib(n):
            a, b = 0, 1
            while a < n:
                print(a, end=' ')
                a, b = b, a+b
            print()
        '''))
    expected = ast.parse(dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals


        def fib(n):
            a, b = 0, 1
            while a < n:
                print(a, end=' ')
                a, b = b, a+b
            print()
        '''))
    transformer = Python2FutureTransformer()
    assert transformer.visit(module) == expected

# Generated at 2022-06-14 01:56:53.283626
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()

# Generated at 2022-06-14 01:57:05.543993
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None)


if __name__ == '__main__':
    import sys
    from typed_ast import ast3
    from typed_ast.ast3 import fix_missing_locations as fix
    from lark import Lark
    from lark.tree import pydot__tree_to_png as to_png
    from .parser import python_parser
    from . import Transformer
    from ..utils.common import _format
    from ..utils.tests import parse_and_transform
    from .visitor import NodeVisitor
    from ..utils.type_vars import TypeInfoVisitor
    from ..type_inference import TypeInferer


# Generated at 2022-06-14 01:57:06.065786
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer



# Generated at 2022-06-14 01:57:08.401969
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().prefix == 'PY2FUTURE'

# Generated at 2022-06-14 01:57:14.671444
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    transform = Python2FutureTransformer()
    result = transform.visit(ast.parse("""def foo(a=None): pass"""))

# Generated at 2022-06-14 01:57:17.099398
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)



# Generated at 2022-06-14 01:57:21.509313
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    input = """
    import os
    import numpy as np
    """
    output = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    import os
    import numpy as np
    """
    module = astor.parse_string(input)
    module = Python2FutureTransformer().visit(module)  # type: ignore
    assert astor.to_source(module).strip() == output.strip()

# Generated at 2022-06-14 01:57:23.901448
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)

# Generated at 2022-06-14 01:57:34.252625
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse("print('hello')")
    Python2FutureTransformer().visit(tree)
    assert ast.dump(tree) == '''Module(body=[ImportFrom(module='__future__', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='unicode_literals', asname=None)], level=0), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='hello')], keywords=[]))])'''


# Generated at 2022-06-14 01:57:35.658931
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer

# Generated at 2022-06-14 01:57:43.446186
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_node = ast.parse("x = 5")
    node_transformer = Python2FutureTransformer()
    transformed_node = node_transformer.visit(module_node)
    code_transformed = ast.unparse(transformed_node)
    assert ast.parse(code_transformed).body[0].value.id == 'absolute_import'  # type: ignore

# Generated at 2022-06-14 01:58:01.405693
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    tree = ast.parse('a = 3\nprint(a)')  # type: ignore
    tree = transformer.visit(tree) # type: ignore
    assert isinstance(tree, ast.Module)
    assert transformer._tree_changed
    print(ast.dump(tree))

# Generated at 2022-06-14 01:58:04.821504
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    import sys
    tree = ast.parse("print('A')")
    transformer = Python2FutureTransformer(sys.version_info)
    transformer.visit(tree)
    assert transformer._tree_changed == True


# Generated at 2022-06-14 01:58:05.800605
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor


# Generated at 2022-06-14 01:58:08.539890
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor  # type: ignore
    from asttokens import ASTTokens  # type: ignore

    test_python_version = 2.7

# Generated at 2022-06-14 01:58:14.072309
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    src = "import sys\nprint(sys.version)"
    expected =  ("from __future__ import absolute_import\n"
                 "from __future__ import division\n"
                 "from __future__ import print_function\n"
                 "from __future__ import unicode_literals\n"
                 "import sys\n"
                 "print(sys.version)")
    node = ast.parse(src)
    Python2FutureTransformer.run(node)
    result = astor.to_source(node)
    assert result == expected

# Generated at 2022-06-14 01:58:24.987835
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from six import StringIO
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import parse
    from .pgen2.token import tokenize
    from .pgen2.parser import parser
    from .transformer import Python3Transformer
    from .imports_transformer import ImportsTransformer

    code = """
    a = 42
    b = 24
    """.strip()

    src = StringIO(code)
    tokens = tokenize(src.readline)
    parser.tokens = tokens
    astree = parser.parse_file(src)
    result = Python3Transformer().visit(astree)
    assert isinstance(result, ast.Module)
    assert not result.body[0].targets[0].id == 'print'

    module = ImportsTransformer().visit

# Generated at 2022-06-14 01:58:35.215082
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from future import absolute_import
    from future import division
    from future import print_function
    from future import unicode_literals
    node = ast.parse('''
    x = 1
    y = 2
    z = 3
    ''')
    tree_transformer = Python2FutureTransformer()
    new_node = tree_transformer.visit(node)
    assert len(new_node.body) == 7
    assert isinstance(new_node.body[0], ast.ImportFrom)
    assert isinstance(new_node.body[1], ast.ImportFrom)
    assert isinstance(new_node.body[2], ast.ImportFrom)
    assert isinstance(new_node.body[3], ast.ImportFrom)
    assert isinstance(new_node.body[4], ast.Assign)


# Generated at 2022-06-14 01:58:44.601173
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class MyTransformer(Python2FutureTransformer):
        def visit_Module(self, node: ast.Module) -> ast.Module:
            return super().visit_Module(node)

    tree = ast.parse("")
    transformed = MyTransformer().visit(tree)
    assert len(transformed.body) == 4
    assert isinstance(transformed.body[0], ast.ImportFrom)
    assert transformed.body[0].module == '__future__'
    assert transformed.body[0].names[0].name == 'absolute_import'
    assert transformed.body[0].names[0].asname is None

# Generated at 2022-06-14 01:58:48.437505
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..testing.utils import assert_python_transformation
    assert_python_transformation(Python2FutureTransformer, 'f = 2.0',
'''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
f = 2.0''')

# Generated at 2022-06-14 01:58:49.482475
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()


# Generated at 2022-06-14 01:59:05.704607
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for Python2FutureTransformer"""
    t = Python2FutureTransformer()
    assert t

# Generated at 2022-06-14 01:59:07.781089
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    futurize_py2 = Python2FutureTransformer()
    assert futurize_py2.target == (2, 7)

# Generated at 2022-06-14 01:59:14.084572
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.visitor import compare_nodes
    from .common import parse
    
    code = '''
# hi
from __future__ import print_function
# by

import os
    '''
    expected_code = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import print_function
# hi
# by

import os
    '''
    expected_tree = parse(expected_code)
    tree = parse(code)
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    compare_nodes(tree, expected_tree)  # assert tree == expected_tree

# Generated at 2022-06-14 01:59:19.255947
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():  # noqa: D103
    tree = ast.parse(imports.get_source())  # type: ignore
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    assert tree.body[0].names[0].name == 'absolute_import'

# Generated at 2022-06-14 01:59:31.571171
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from flake8_future_import.utils.node_utils import node_to_str
    from flake8_future_import.utils.tree_utils import compare_ast

    tree_before = ast.parse('''
        def test():
            print('hello')
    ''').body[0]

    tree_after = ast.parse('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals


        def test():
            print('hello')
    ''').body[4]

    p = Python2FutureTransformer(tree_before)
    compare_ast(p.tree, tree_after)

# Generated at 2022-06-14 01:59:41.966617
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor  # type: ignore

    source = 'print("hello")'
    target = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("hello")"""

    transform = Python2FutureTransformer()
    tree = astor.parse_file(source)
    transform.visit(tree)
    result = astor.to_source(tree)

    print(result)
    assert result == target

# Generated at 2022-06-14 01:59:44.057962
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.target == (2, 7)


# Generated at 2022-06-14 01:59:51.380234
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('''
    a = 1
    b = 2
    ''')
    node = Python2FutureTransformer().visit(node)
    assert node.body[0].value.s == '__future__'
    assert node.body[1].value.s == '__future__'
    assert node.body[2].value.s == '__future__'
    assert node.body[3].value.s == '__future__'
    assert node.body[4].value.id == 'a'

# Generated at 2022-06-14 01:59:53.153005
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    trf = Python2FutureTransformer()
    assert trf.log is None
    
    

# Generated at 2022-06-14 01:59:54.586877
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()


# Generated at 2022-06-14 02:00:24.931331
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    instance = Python2FutureTransformer()
    assert instance is not None


# Generated at 2022-06-14 02:00:26.729069
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer


# Generated at 2022-06-14 02:00:28.014915
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:35.590902
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ..utils.ast_builder import build_ast
    tree = build_ast("a**2")
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    result = astor.to_source(tree)

    # Asserts
    assert transformer._tree_changed is True
    assert result == "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\na**2"

# Generated at 2022-06-14 02:00:37.077677
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert x


# Generated at 2022-06-14 02:00:47.121707
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    mt = ast.Module(body=[ast.ImportFrom(module='math', names=[ast.alias(name='sin', asname='sin')], level=0)])
    transformed = Python2FutureTransformer().visit(mt)
    assert transformed.body[0].names[0].name.s == 'absolute_import'
    assert transformed.body[1].names[0].name.s == 'division'
    assert transformed.body[2].names[0].name.s == 'print_function'
    assert transformed.body[3].names[0].name.s == 'unicode_literals'
    assert transformed.body[4].names[0].name.s == 'sin'

if __name__ == "__main__":
    test_Python2FutureTransformer_visit_Module()

# Generated at 2022-06-14 02:00:52.715889
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """
    Test Python2FeatureTransformer.visit_Module()

    """
    # Arrange
    snippet = 'pass\n'
    tree = ast.parse(snippet)
    transformer = Python2FutureTransformer()

    # Act
    transformed_tree = transformer.visit(tree)

    # Assert
    assert snippet != astunparse.unparse(tree)
    assert snippet in astunparse.unparse(transformed_tree)

# Generated at 2022-06-14 02:00:53.736323
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:01:00.471280
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = '''
        mails = ["1@gmail.com", "2@gmail.com", "3@gmail.com"]
        print(mails)
    '''
    tree = ast.parse(code)
    module = tree.body
    transformer = Python2FutureTransformer()
    new_module = transformer.visit(module)
    code_snippet = transformer.get_code_snippet(new_module)
    assert code == code_snippet

# Generated at 2022-06-14 02:01:02.566946
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor

# Generated at 2022-06-14 02:02:04.042107
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)

# Generated at 2022-06-14 02:02:09.912370
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # given
    code = "print('hello world')"
    expected_code = imports.get_source(future='__future__') + code
    # when
    actual_code = transform(Python2FutureTransformer, code, target=(2, 7))
    # then
    assert expected_code == actual_code

# Generated at 2022-06-14 02:02:11.853661
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    f = Python2FutureTransformer() 
    assert f._tree_changed == None
    assert isinstance(f.visit_Module, type(f.visit_Module))

# Generated at 2022-06-14 02:02:13.265610
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:02:14.721086
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3
    import astor


# Generated at 2022-06-14 02:02:20.952027
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    assert_equal(
        Python2FutureTransformer.run(""),
        """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
    )

    assert_equal(
        Python2FutureTransformer.run("""

a = 1


    """),
        """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


a = 1


    """
    )

# Generated at 2022-06-14 02:02:23.568546
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert x.tree_changed is False
    assert x.target == (2, 7)
    assert x.visit_Module is not None

# Generated at 2022-06-14 02:02:25.360676
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast

    assert isinstance(Python2FutureTransformer(), BaseNodeTransformer)


# Generated at 2022-06-14 02:02:31.734788
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_helpers import NodeAssertionHelper
    from typed_ast import ast3
    transformer = Python2FutureTransformer()
    helper = NodeAssertionHelper()
    node = ast3.parse('print(2 / 3)')
    expected = ast3.parse(
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print(2 / 3)
""")

    helper.assert_transform(transformer, node, expected)

# Generated at 2022-06-14 02:02:33.906700
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None).__class__.__name__ == 'Python2FutureTransformer'
