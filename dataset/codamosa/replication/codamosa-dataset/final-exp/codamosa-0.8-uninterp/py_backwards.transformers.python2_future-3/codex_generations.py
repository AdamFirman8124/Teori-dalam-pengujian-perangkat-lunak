

# Generated at 2022-06-14 01:55:09.911074
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:55:23.296503
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse("""
        print("Hello")
   """)
    transf = Python2FutureTransformer()
    transf.visit(node)

# Generated at 2022-06-14 01:55:30.972442
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # test snippet
    assert isinstance(imports.get_body(future='__future__'), list) 
    assert isinstance(imports.get_body(future='__future__')[0], ast.ImportFrom) 

    # test transformer
    transformer = Python2FutureTransformer()
    source = 'def f():\n    print("hello")\n'
    node = ast.parse(source, mode='single')
    node = transformer.visit(node)
    code = astunparse.unparse(node)
    assert transformer._tree_changed
    assert 'from future import absolute_import' in code
    assert 'from future import division' in code
    assert 'from future import print_function' in code
    assert 'from future import unicode_literals' in code

# Generated at 2022-06-14 01:55:31.999431
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Construct an instance of Python2FutureTransformer
    transformer = Python2FutureTransformer()
    assert transformer  # avoid "no coverage" warning

# Generated at 2022-06-14 01:55:34.965708
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    py2future = Python2FutureTransformer()
    assert py2future._in_scope == False
    assert py2future._tree_changed == False
    assert isinstance(py2future.target, tuple)
    assert py2future.target == (2, 7)

# Generated at 2022-06-14 01:55:37.416036
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert x  # avoid warning "x unused"


# Generated at 2022-06-14 01:55:47.766063
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .test_tree import check_module

    tree = ast.parse('print("Hello world")')
    tree = Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 01:55:48.799835
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(3, 6)

# Generated at 2022-06-14 01:55:53.755175
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from .transformer import Transformer
    
    class Src(ast.AST):
        _fields = []

    class Target(ast.AST):
        _fields = []

    t = Transformer(Python2FutureTransformer(target=(2,7), src=Src, target=Target))

    assert isinstance(t, Transformer)

# Generated at 2022-06-14 01:55:57.215636
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import check_equal_ast
    from ..utils.fixtures import future_transformer_inputs
    for input, output in future_transformer_inputs.items():
        check_equal_ast(Python2FutureTransformer().visit(input), output)

# Generated at 2022-06-14 01:56:00.851433
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 01:56:10.820258
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = astor.parse_file(os.path.join(here, '../../tests/resources/target/python_2_7.py'))
    assert tree is not None
    nodes = Python2FutureTransformer.run(tree)
    assert nodes is not None
    assert len(nodes.body) == 5
    assert isinstance(nodes.body[0], ast.ImportFrom)
    assert nodes.body[0].module == '__future__'
    assert nodes.body[0].names[0].name == 'absolute_import'
    assert isinstance(nodes.body[1], ast.ImportFrom)
    assert nodes.body[1].module == '__future__'
    assert nodes.body[1].names[0].name == 'division'

# Generated at 2022-06-14 01:56:18.242229
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse(textwrap.dedent('''
    # comment
    pass
    '''))
    node = Python2FutureTransformer().visit(node)
    assert unparse(node) == textwrap.dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    # comment
    pass
    ''').lstrip('\n')

# Generated at 2022-06-14 01:56:22.673593
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .. import transform
    from .. import ast_utils
    import ast

    tr = transform(Python2FutureTransformer())
    tr.visit(ast.parse('a=1'))
    assert tr.tree_changed



# Generated at 2022-06-14 01:56:23.792411
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 01:56:34.722687
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class current_class:
        tree_changed = False

    # Only for type checking
    from typed_ast import ast3 as ast

    node = ast.parse('    def f(x, y):\n        return x ** y\n', mode="exec")
    assert_source_equal(str(node), 'def f(x, y):\n    return x ** y\n')

    node = Python2FutureTransformer(current_class).visit(node)

    assert_source_equal(str(node), 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\ndef f(x, y):\n    return x ** y\n')
    assert current_class.tree_changed

# Generated at 2022-06-14 01:56:36.952265
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().future is None
    py2_future = Python2FutureTransformer(future='__future__')
    assert py2_future.future == '__future__'


# Generated at 2022-06-14 01:56:40.183315
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.test_utils import assert_tree_unchanged
    from ..utils.test_utils import assert_tree_changed

    from ..serializer import serialize_tree

    from ..nodes import Module

    transformer = Python2FutureTransformer()

    tree = Module()
    assert_tree_unchanged(tree, transformer)

    tree = Module(body=[])
    assert_tree_changed(tree, transformer)

# Generated at 2022-06-14 01:56:42.680227
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from typed_ast import ast3 as ast

    module = ast.parse("#Some python code")
    transformer = Python2Futur

# Generated at 2022-06-14 01:56:54.360541
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast
    import textwrap
    node = ast.parse("x = 1")
    Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 01:57:00.711567
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Arrange
    import astor

# Generated at 2022-06-14 01:57:06.327273
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    sample_text = '''
    class FooBar:
        pass
    '''
    expected = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    class FooBar:
        pass
    '''
    print(expected == Python2FutureTransformer(sample_text).result())

# Generated at 2022-06-14 01:57:09.386681
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert isinstance(x, Python2FutureTransformer)


# Generated at 2022-06-14 01:57:16.393399
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    a = astor.code_to_ast.parse_file('./tests/data/Python2FutureTransformer_in.py')
    b = Python2FutureTransformer().visit(a)
    c = astor.to_source(b).strip()

    with open('./tests/data/Python2FutureTransformer_out.py') as f:
       d = f.read().strip()
    assert c == d

# Generated at 2022-06-14 01:57:22.314807
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Test if the transform works correctly
    source_code = """
    print('hello')
    """
    result = Python2FutureTransformer().visit(ast.parse(source_code))
    assert ast.dump(result) == ast.dump(ast.parse(
        """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    print('hello')
    """
    ))

# Generated at 2022-06-14 01:57:22.886931
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 01:57:25.010600
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)



# Generated at 2022-06-14 01:57:26.056722
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass  # Just for coverage

# Generated at 2022-06-14 01:57:27.460138
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert not Python2FutureTransformer({}).tree_changed

# Generated at 2022-06-14 01:57:29.387399
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astunparse


# Generated at 2022-06-14 01:57:42.185424
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.fixtures import make_dummy_future_module
    from ..utils.fixtures import make_dummy_snippet_module
    from ..utils.fixtures import make_dummy_unittest_module
    from ..utils.fixtures import make_dummy_unittest_module_simple
    from ..utils.fixtures import make_dummy_futurize_module
    
    unittest = make_dummy_unittest_module()
    unittest_simple = make_dummy_unittest_module_simple()
    snippet = make_dummy_snippet_module()
    future = make_dummy_future_module()
    futurize = make_dummy_futurize_module()
    
    tree = ast.parse(futurize)
    tree

# Generated at 2022-06-14 01:57:53.264100
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3
    from typed_ast.ast3 import Module
    from typed_ast.ast3 import Str
    from typed_ast.ast3 import Import
    from typed_ast.ast3 import ImportFrom
    from typed_ast.ast3 import parse

    # Test with __future__ being a simple import
    m = Module(body=[
        Import(names=[alias(
            name='__future__',
            asname=None
        )])
    ])
    t = Python2FutureTransformer(target=Python2FutureTransformer.target)
    m = t.visit(m)
    assert t._tree_changed
    assert len(m.body) == 5
    assert isinstance(m.body[0], Import)  # future
    assert isinstance(m.body[1], ImportFrom)  # __future

# Generated at 2022-06-14 01:58:02.996056
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.fixtures import typed_ast_builtins
    from ..utils.snippet import snippet
    from typing import List

    sample_code = snippet[1:19]

    tree = typed_ast_builtins.ast3.parse(sample_code)
    assert tree is not None

    transformer = Python2FutureTransformer()
    assert transformer is not None

    assert ast.dump(tree) == ast.dump(transformer.visit(tree))
    assert transformer.tree_changed


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))
    
    from ..utils.fixtures import typed_ast_builtins
    from ..utils.snippet import snippet
    from typing import List


# Generated at 2022-06-14 01:58:10.429102
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.snippet import snippet
    from typed_ast import ast3 as ast

    @snippet
    def imports():
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

    @snippet
    def module():
        pass

    tree = ast.parse(module.get_source())
    t = Python2FutureTransformer()
    t.visit(tree)
    assert ast.dump(tree) == imports.get_ast().body + [ast.Expr(ast.Str(''))]

# Generated at 2022-06-14 01:58:17.269510
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from mikatools import parse_unit
    
    code = '''
        for x in range(10):
            print(x)
    '''
    expected = '''
        from future import absolute_import
        from future import division
        from future import print_function
        from future import unicode_literals
    for x in range(10):
        print(x)
    '''
    unit = parse_unit(code, '<string>', version=2)
    unit = Python2FutureTransformer().visit(unit)  # type: ignore
    assert unit.body[0].lineno == 2

# Generated at 2022-06-14 01:58:26.438229
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source
    from .. import transformer as t
    # test_input_source
    test_input_source = \
        '''
        '''

    # test_output_source
    test_output_source = \
        '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        '''

    module_node = t.parse_source_to_ast(test_input_source)
    Python2FutureTransformer().visit(module_node)
    output_source = source(module_node)
    assert test_output_source == output_source

# Generated at 2022-06-14 01:58:35.116363
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    class DummyTransformer(BaseNodeTransformer):
        target = (2, 7)

    source = """

    """
    expected = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
    
    
    """
    tree = ast.parse(source)
    Python2FutureTransformer(DummyTransformer()).visit(tree)
    result = compile(tree, filename="", mode="exec")
    codeobj = result.co_consts[0]
    assert codeobj.co_consts[0] == expected

# Generated at 2022-06-14 01:58:42.599689
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source2ast, ast_prettyprint
    from .py2to3 import Python2to3Transformer
    from .py3to2 import Python3to2Transformer

    source = source2ast(
        """
import os
from math import sin
from future import directory_traversal
import sys
from __future__ import print_function
print('hello')
""")
    target = source2ast(
        """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
from math import sin
from future import directory_traversal
import sys
from __future__ import print_function
print('hello')
""")


# Generated at 2022-06-14 01:58:48.853253
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    source = textwrap.dedent("""
    import os
    """)

    expected = textwrap.dedent("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    import os
    """)

    tree = ast.parse(source)
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    actual = compile(tree, '<string>', 'exec')
    assert actual == expected

# Generated at 2022-06-14 01:58:56.668792
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .. import get_ast
    from .generate import generate_code

    stmts = get_ast("print('hello')")
    target = (2, 7)

    transformer = Python2FutureTransformer(target=target)
    transformer.visit(stmts)
    new_code = generate_code(stmts)
    assert 'from __future__ import absolute_import' in new_code
    assert 'from __future__ import division' in new_code
    assert 'from __future__ import print_function' in new_code
    assert 'from __future__ import unicode_literals' in new_code

# Generated at 2022-06-14 01:59:06.413097
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 01:59:07.865474
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'



# Generated at 2022-06-14 01:59:09.423983
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

# Generated at 2022-06-14 01:59:12.003225
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 01:59:24.428708
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from .utils import compare_ast

    # Test case 1: no docstring
    test_case = """
foo = 'bar'
""".strip()
    expected_ast = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

foo = 'bar'
""".strip()
    expected_source = expected_ast
    module = ast.parse(test_case)
    Python2FutureTransformer().visit(module)
    actual_source = astor.to_source(module).strip()
    assert compare_ast(expected_source, actual_source)

    # Test case 2: one-liner docstring
    test_case = """
'foo bar'
foo = 'bar'
""".strip()
   

# Generated at 2022-06-14 01:59:26.298562
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    xformer = Python2FutureTransformer()
    assert isinstance(xformer, Python2FutureTransformer)


# Generated at 2022-06-14 01:59:29.326350
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer._tree_changed == False
    assert transformer.target == (2, 7)
    assert transformer.visit_Module(ast.parse("pass"))


# Generated at 2022-06-14 01:59:30.489557
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:44.991604
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    actual_code = textwrap.dedent(
        """
    from bar import bar
    foo = bar() + 1
    """
        )

    expected_code = textwrap.dedent(
        """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    from bar import bar
    foo = bar() + 1
    """
        )

    node = ast.parse(actual_code)  # type: ignore
    visitor = Python2FutureTransformer()
    visitor.visit(node)
    actual_code = astor.to_source(node)
    assert actual_code == expected_code

# Generated at 2022-06-14 01:59:46.756382
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    target = (2, 7)
    assert transformer.target == target


# Generated at 2022-06-14 02:00:07.142966
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseNodeTransformer)
    assert transformer._tree_changed is False
    assert transformer.unmodified is False
    assert transformer.modified is False
    assert transformer.target_tuple == (2, 7)


# Generated at 2022-06-14 02:00:13.063923
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    def f(a): pass
    tree = ast.parse(inspect.getsource(f))
    Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 02:00:18.938444
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('import x')
    tr = Python2FutureTransformer()
    tr.visit(node)
    assert tr.tree_changed

    expected = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import x
    '''
    actual = ast.unparse(node)
    assert expected == actual

# Generated at 2022-06-14 02:00:22.009518
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """
    Test case for method visit_Module of class Python2FutureTransformer
    
    """
    t = Python2FutureTransformer()

# Generated at 2022-06-14 02:00:24.279449
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer


# Generated at 2022-06-14 02:00:34.762427
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    try:
        from typed_ast import ast3 as ast
    except ImportError:
        import ast

    module_node: ast.Module = ast.parse("def foo():\n    print(foo)")
    transform = Python2FutureTransformer()
    result: ast.Module = transform.visit(module_node) # type: ignore
    expected: ast.Module = ast.parse("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    def foo():
        print(foo)
    """)
    assert ast.dump(result) == ast.dump(expected)

# Generated at 2022-06-14 02:00:36.652800
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:00:38.020008
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer


# Generated at 2022-06-14 02:00:46.426522
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('x = 1')
    xformer = Python2FutureTransformer()
    assert xformer.visit(node) == ast.parse('import __future__; x = 1')

    node = ast.parse('x = 1', feature_version=(3, 0))
    assert xformer.visit(node) == ast.parse('import __future__; x = 1', feature_version=(3, 0))

    node = ast.parse('x = 1', feature_version=(2, 7))
    assert xformer.visit(node) == ast.parse('import __future__; x = 1', feature_version=(3, 0))

# Generated at 2022-06-14 02:00:47.585551
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    _ = Python2FutureTransformer()

# Generated at 2022-06-14 02:01:30.279695
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    sample_filename = 'sample/untransformed_code.py'
    with open(sample_filename) as source_file:
        source = source_file.read()
    source_tree = ast.parse(source)
    transformer = Python2FutureTransformer()
    new_tree = transformer.visit(source_tree)
    new_source = astor.to_source(new_tree).strip()

# Generated at 2022-06-14 02:01:33.628993
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # pylint: disable=W0212
    assert Python2FutureTransformer._tree_changed is False
    assert Python2FutureTransformer.future == '__future__'
    assert Python2FutureTransformer.target == (2, 7)


# Generated at 2022-06-14 02:01:40.279042
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code_in = """
x = 1
    """

    code_expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = 1
    """

    module = ast.parse(code_in)
    Python2FutureTransformer().visit(module)
    code_actual = astor.to_source(module)

    assert code_expected == code_actual


# Generated at 2022-06-14 02:01:48.103819
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_helpers import assert_node
    from .test_helpers import assert_source
    from .test_helpers import get_node
    node = get_node(Python2FutureTransformer, """
        import os
        import sys
        
        print(os)
        print(sys)
    """)
    assert_node(node, """
        import future
        print(os)
        print(sys)
    """)

    file_input = get_node(Python2FutureTransformer, """
        import os
        import sys
    """, mode='exec')
    assert_node(file_input, """
        import future
        import os
        import sys
    """)


# Generated at 2022-06-14 02:01:58.530400
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    given_module = """
x = "abc"
y = 3.2
    """
    expected_module = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = "abc"
y = 3.2
    """
    given_ast = ast.parse(given_module)
    print(ast.dump(given_ast))
    expected_ast = ast.parse(expected_module)
    actual_ast = Python2FutureTransformer().visit(given_ast)
    print(ast.dump(actual_ast))
    assert ast.dump(expected_ast) == ast.dump(actual_ast)

# Generated at 2022-06-14 02:02:09.559329
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    original = ast.parse("""
    if True:
        pass
    """)

    transformer = Python2FutureTransformer(original)
    transformed = transformer.visit(original)

    assert type(transformed) is ast.Module
    assert transformer._tree_changed is True  # _tree_changed is set to True in Python2FutureTransformer.visit_Module(...)
    assert len(transformed.body) == 6  # 4 Future statements + original 2 statements

    assert type(transformed.body[0]) is ast.ImportFrom
    assert type(transformed.body[1]) is ast.ImportFrom
    assert type(transformed.body[2]) is ast.ImportFrom
    assert type(transformed.body[3]) is ast.ImportFrom

    assert type(transformed.body[4]) is ast.If

# Generated at 2022-06-14 02:02:11.471555
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().is_applicable(target_major=2)



# Generated at 2022-06-14 02:02:15.580382
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('')
    transformer = Python2FutureTransformer(tree=tree)
    transformer.visit(tree.body[0])
    target = ast.parse(imports(future='__future__')).body[0]
    assert target == transformer.tree.body[0]


# Generated at 2022-06-14 02:02:23.196428
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer
    assert transformer.target == (2, 7)
    assert transformer.source == (3, 5)


if __name__ == '__main__':
    import os
    import sys
    import logging
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(root_path)
    logging.basicConfig(level=logging.INFO)
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import parse
    from .base import ASTNodeTransformer
    from .async_def import AsyncDefTransformer
    from .function_annotations import FunctionAnnotationsTransformer
    from ..utils.inspect_source import inspect_source
    
   

# Generated at 2022-06-14 02:02:24.546438
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    trans = Python2FutureTransformer
    assert trans.target == (2, 7)

# Generated at 2022-06-14 02:03:49.692621
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """\
print('Hello world!')
"""
    expected_output = """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
print('Hello world!')
"""
    actual_output = Python2FutureTransformer().to_source(source)
    assert actual_output == expected_output



# Generated at 2022-06-14 02:03:55.444675
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_utils import generate_python_3_source_code

    # Generate source code
    source_code = generate_python_3_source_code(
            'def f(a, b):\n'
            '    return a + b\n',
        )

    # Apply Python2FutureTransformer to source code
    node = ast.parse(source_code)
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    # Generate transformed source code from transformed AST
    from .test_utils import generate_python_2_source_code # to avoid cyclic dependecy
    transformed_source_code = generate_python_2_source_code(new_node)

    # Check if transformed source code is correct

# Generated at 2022-06-14 02:04:03.465988
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import from_pyversion
    from . import to_pyversion
    from . import standard
    from . import compat
    from . import python2
    from . import python3

    tree = from_pyversion.transforms(
        code='''
        # a
        import foo as bar
        # b
        import os as _os
        # c
        from sys import path       
        # d
        from sys import exc_info as _exc_info
        ''',
        version=(2, 7))
    result = to_pyversion.transforms(tree=tree, version=(3, 7))

# Generated at 2022-06-14 02:04:14.045361
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # from __future__ import absolute_import, division, print_function, unicode_literals
    tree = ast.parse(
        """x = 1
        y = 2
        """,
        mode="exec"
    )
    assert Python2FutureTransformer().visit(tree) == ast.parse(
        """from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        x = 1
        y = 2
        """,
        mode="exec"
    )

# Generated at 2022-06-14 02:04:15.106194
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:04:21.135369
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.source import source
    from .. import transformations

    tree = source('import os', transformer=Python2FutureTransformer)
    assert transformations.unparse(tree) == '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
'''

# Generated at 2022-06-14 02:04:28.076602
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = dedent('''\
        def func1(a, b=1):
            pass
        ''')
    expected = dedent('''\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        
        def func1(a, b=1):
            pass
        ''')
    root = ast.parse(source)
    transformer = Python2FutureTransformer()
    transformed = transformer.visit(root)
    assert ast.unparse(transformed) == expected

# Generated at 2022-06-14 02:04:32.718434
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse("def f(x): return x + 1")
    node = Python2FutureTransformer().visit(module)
    assert ast.dump(node) == ast.dump(ast.parse("from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\ndef f(x): return x + 1"))

# Generated at 2022-06-14 02:04:37.788708
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.source import source
    from ..utils.visitor import NodeTransformerTestMixin
    from ..utils.visitor import visit_py_ast

    class Test(NodeTransformerTestMixin):

        transformer = Python2FutureTransformer()
        expected_tree = visit_py_ast(imports.get_ast(future='__future__'))

    Test.test_visit_Module()

# Generated at 2022-06-14 02:04:48.041660
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_python_ast_imports import check_tree_changed, _check_tree_unchanged
    import sys
    
    def _assert_transformer_works(st):
        global_namespace = sys._getframe(1).f_globals
        py2_tree = ast.parse(st, filename='<unknown>', mode='exec')
        _check_tree_unchanged(py2_tree)
        transformer = Python2FutureTransformer(py2_tree, target=(2, 6))
        
        check_tree_changed(transformer, py2_tree)
        
        # Run visitor method
        transformer.visit(py2_tree)
        # Check tree was mutated
        check_tree_changed(transformer, py2_tree)
        
        # Check code transformed to Python 3