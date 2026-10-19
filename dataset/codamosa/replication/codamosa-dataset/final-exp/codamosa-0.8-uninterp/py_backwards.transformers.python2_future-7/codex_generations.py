

# Generated at 2022-06-14 01:55:03.314301
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .fixtures import Python2FutureTransformer_visit_Module_test
    # Test AST created from: "print('Hello, world!');"
    src = Python2FutureTransformer_visit_Module_test.test_source
    expected_result = Python2FutureTransformer_visit_Module_test.test_tree
    module_node = ast.parse(src)

    transformer = Python2FutureTransformer()
    new_module_node = transformer.visit(module_node)

    assert ast.dump(new_module_node) == ast.dump(expected_result)
    assert transformer._tree_changed



# Generated at 2022-06-14 01:55:12.612622
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .setup_tester import setup_tester
    from .test_nodes import test_nodes

    tester = setup_tester(
        test_nodes,
        transformer=Python2FutureTransformer,
        is_main=True,
        target=(2, 7)
    )
    source = """
from __future__ import print_function
from __future__ import unicode_literals
print(isinstance(test, int))
    """
    expected = """
from future import print_function
from future import unicode_literals
from __future__ import print_function
from __future__ import unicode_literals
print(isinstance(test, int))
    """
    tester.assertEqual(
        expected = expected,
        actual = tester.run_transform(source)
    )

# Generated at 2022-06-14 01:55:21.620961
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_astunparse
    from typed_ast import ast3 as ast
    from .renamer import Renamer
    
    code = '''import math'''
    tree = ast.parse(code, mode='exec')
    tree = Python2FutureTransformer().visit(tree)  # type: ignore
    tree = Renamer(rename_to='test_renamer').visit(tree)  # type: ignore
    print(typed_astunparse.unparse(tree, include_encoding=False))

# Generated at 2022-06-14 01:55:28.104360
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer(None)
    node = ast.parse('x = 1')
    result = transformer.visit_Module(node)
    assert len(result.body) == 4 + len(node.body)
    assert isinstance(result.body[0], ast.ImportFrom)
    assert isinstance(result.body[1], ast.ImportFrom)
    assert isinstance(result.body[2], ast.ImportFrom)
    assert isinstance(result.body[3], ast.ImportFrom)
    assert result.body[4].value.n == 1
    assert transformer._tree_changed is True
    assert transformer._module_changed is True

# Generated at 2022-06-14 01:55:32.369031
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    argument_values = {
        'future': '__future__',
    }
    expected_output = "from __future__ import absolute_import\n" \
        "from __future__ import division\n" \
        "from __future__ import print_function\n" \
        "from __future__ import unicode_literals"
    generated_output = imports.get_body(**argument_values)

    assert generated_output == expected_output

# Generated at 2022-06-14 01:55:39.135143
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.Module(body=[])
    visitor = Python2FutureTransformer()
    assert visitor.visit(node).body[0].names[0].name == 'absolute_import'
    assert visitor.visit(node).body[0].names[1].name == 'division'
    assert visitor.visit(node).body[0].names[2].name == 'print_function'
    assert visitor.visit(node).body[0].names[3].name == 'unicode_literals'



# Generated at 2022-06-14 01:55:47.533580
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.tester import make_dummy_code

    code = make_dummy_code(
        '''
        a = 1
        b = 2
        ''',
        target_code='''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        a = 1
        b = 2
        '''
    )
    node = code.parsed_tree
    visitor = Python2FutureTransformer()
    visitor.visit(node)
    assert code.target_code == code.stringify(node)

# Generated at 2022-06-14 01:55:57.333464
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    s = snippet(imports)
    tree = ast.parse(s)
    node = tree.body[0]
    assert isinstance(node, ast.Module)

    transformer = Python2FutureTransformer(filename='<test>')
    transformer.visit(node)
    tree = transformer.get_tree()
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 5
    for node in tree.body:
        assert isinstance(node, ast.ImportFrom)
        assert node.module == '__future__'
        assert node.level == 0
        assert len(node.names) == 1
        node_name = node.names[0]
        assert isinstance(node_name, ast.alias)

# Generated at 2022-06-14 01:56:07.222703
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source
    from ..utils.ast import dump
    from ..utils.visitor import ASTNodeVisitor
    input_source = source(r"""
        import requests
    """)
    expected_source = source(r"""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import requests
    """)
    visitor = Python2FutureTransformer()
    visitor.visit(input_source.get_ast())
    assert visitor._tree_changed
    assert dump(input_source.get_ast()) == dump(expected_source.get_ast())

# Generated at 2022-06-14 01:56:18.293530
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    st = dedent('''\
        import os
        x = 1
        y = 2
        z = 3
        ''')

    tree = ast.parse(st)

# Generated at 2022-06-14 01:56:31.742433
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('a = 2/3')
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    assert transformer._tree_changed == True

# Generated at 2022-06-14 01:56:40.700432
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import textwrap
    from typed_ast.ast3 import parse

    code = """\
    def a():
        pass
    """
    test_code = textwrap.dedent(textwrap.dedent(code))
    tree = parse(test_code)
    check_future = Python2FutureTransformer(future='__future__')
    new_tree = check_future.visit(tree)
    generated_code = check_future.dump_tree(new_tree)

    assert generated_code.replace('\n', '') == ''.join((
        "from future import absolute_import",
        "from future import division",
        "from future import print_function",
        "from future import unicode_literals",
        test_code))

# Generated at 2022-06-14 01:56:42.290304
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer


# Generated at 2022-06-14 01:56:53.988114
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Given
    node = ast.parse('')

    # When
    node = Python2FutureTransformer().visit(node)

    # Then

# Generated at 2022-06-14 01:57:06.044423
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    code = "print(1)\nprint(2)\nprint(3)\n"
    ast_module = ast.parse(code)
    ast_module = transformer.visit(ast_module)

# Generated at 2022-06-14 01:57:17.247916
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..parser import get_parser
    parser = get_parser('2.7', experimental=False)
    transformer = Python2FutureTransformer(parser)

    code_in = """
        import math

        print(math.pow(2, 2))
    """
    tree = parser.parse(code_in)
    transformer.visit(tree)
    code_out = parser.get_source(tree)
    assert code_out == """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        import math

        print(math.pow(2, 2))
    """

# Generated at 2022-06-14 01:57:22.663904
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .python_ast import PythonAst
    from .python_parser import ast_to_str
    from ..utils.file import get_script

    filename = get_script('python2', 'python2sample.py')
    ast_ = PythonAst().get_ast(filename, 2)
    transformer = Python2FutureTransformer()
    transformer.visit(ast_)
    print(ast_to_str(ast_))
    assert transformer.tree_changed

# Generated at 2022-06-14 01:57:27.788112
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    # given
    tree = ast.parse("print('hello')")
    visitor = Python2FutureTransformer()

    # when
    tree = visitor.visit(tree)

    # then
    assert astor.to_source(tree).startswith("from __future__ import absolute_import")

# Generated at 2022-06-14 01:57:36.758785
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sys
    import os
    import ast
    import unittest
    from typed_ast import ast3 as typed_ast
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ..utils.snippet import snippet
    from ..utils.source import source
    from ..utils.source import Source
    from ..visitors.base import BaseNodeTransformer

    @snippet
    def import_stdlib():
        import math
        import time
        import random

    @snippet
    def import_own():
        from . import test_other
        from .other import foo

    @snippet
    def import_as():
        import math as square
        import time as now
        import os as operating_system


# Generated at 2022-06-14 01:57:38.943902
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t is not None


# Generated at 2022-06-14 01:57:53.263500
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    indented_lines = [
        """\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        def foo(): ...\
        """
    ]
    module = ast.parse(''.join(indented_lines))  # type: ignore
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)  # type: ignore
    lines = [line.strip() for line in indented_lines]
    for body_node, input_line in zip(module.body, lines):  # type: ignore
        assert isinstance(body_node, ast.Expr)  # type: ignore
        assert isinstance(body_node.value, ast.Str)  # type: ignore
        assert body_node

# Generated at 2022-06-14 01:57:54.500717
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.target == (2, 7)


# Generated at 2022-06-14 01:58:03.745016
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from py2c.tests import test_pipeline
    import typed_ast.ast3 as ast
    from typed_ast.ast3 import Module, FunctionDef, arguments, \
        Load, Num, Str, Name, NameConstant, Expr, Dict, List, Store, Mod, BitOr, \
        And, Div, USub, Add, Eq, Not, Return, Call, Subscript, ListComp, Tuple, \
        Attribute, Compare, BinOp, AugAssign, Param, Pass
    from py2c.utils.source import fix_source_coding
    from py2c.utils.source import SourceMap
    from py2c.codegen.codegen import TargetCodeGenerator


# Generated at 2022-06-14 01:58:04.252740
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class_ = Python2FutureTransformer



# Generated at 2022-06-14 01:58:10.782541
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import parse
    from ..unittest_tools import assert_equals_ast


    filename = 'test.py'
    source = 'print("Hello, World!")'
    expected = 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nprint("Hello, World!")'
    tree = parse(source)
    Python2FutureTransformer.run(tree)
    assert_equals_ast(expected, tree)

# Generated at 2022-06-14 01:58:13.545320
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse('import sys')
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    assert tree == imports.get_tree(future='__future__')
    assert transformer.tree_changed()

# Generated at 2022-06-14 01:58:17.055597
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    a_class = Python2FutureTransformer()
    assert a_class.target == (2, 7)
    assert a_class.future == "__future__"


# Generated at 2022-06-14 01:58:24.760642
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
    import sys
    import os
    
    
    a = 5
    """.strip()
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    import sys
    import os
    
    
    a = 5
    """.strip()
    tree = ast.parse(code)
    tree = Python2FutureTransformer().visit(tree)
    assert astor.to_source(tree).strip() == expected

# Generated at 2022-06-14 01:58:30.353870
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    mod = ast.parse('l = [1, "a", {1}]')
    transformer = Python2FutureTransformer()
    mod = transformer.visit(mod)
    ast.fix_missing_locations(mod)
    if transformer.is_changed():
        code = compile(mod, filename="<ast>", mode="exec")
        exec(code)
    assert l == [1, "a", {1}]




# Generated at 2022-06-14 01:58:39.651369
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Fully qualified name is required so that Mypy knows this is the correct
    # class
    transformer = Python2FutureTransformer()
    
    node = ast.Module(
        body=[
            ast.Import(names=[ast.alias(name='six', asname=None)])
        ]
    )
    
    actual = transformer.visit(node)

# Generated at 2022-06-14 01:58:45.059619
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Tests instantiating class Python2FutureTransformer."""
    assert Python2FutureTransformer()

# Generated at 2022-06-14 01:58:51.150771
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    seg = ast.parse('print(2)')
    visitor = Python2FutureTransformer()
    visitor.visit(seg)
    expected = 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\nprint(2)'
    assert(str(seg)==expected)

# Generated at 2022-06-14 01:58:53.380004
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None



# Generated at 2022-06-14 01:58:55.378429
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert(Python2FutureTransformer(None) is not None)



# Generated at 2022-06-14 01:59:01.098921
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import parse
    from typed_ast.typed_ast import AST
    from ni_ide.transforms.transformers.python2future_transformer import Python2FutureTransformer
    from typing import cast


# Generated at 2022-06-14 01:59:11.260663
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils import get_ast
    from ..transforms import Python2FutureTransformer

    code = """
    print(2)
    """
    t = Python2FutureTransformer()
    result = t.visit(get_ast(code))
    print(result)   


"""
# simple test case
>>> import ast_toolbox
>>> import ast
>>> code = """

# Generated at 2022-06-14 01:59:23.210230
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import typing
    import astor
    # The code to be transformed
    code = '''
    """Some docstring"""
    pass
    '''
    # Try importing using astor library
    try:
        module = ast.parse(code)
    except Exception:
        pass
    tree = Python2FutureTransformer().visit(module)
    result = astor.to_source(tree, indent_with=' ' * 4)
    expected = '''\
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    \"\"\"Some docstring\"\"\"
    pass
    '''
    assert result == expected

# Generated at 2022-06-14 01:59:23.825909
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:25.541095
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert x.target == (2, 7)


# Generated at 2022-06-14 01:59:35.713831
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sys
    import astor
    from .base import BaseNodeTransformer
    from typed_ast import ast3 as ast
    from typed_ast import util

    class TestTransformer(BaseNodeTransformer):
        def __init__(self):
            self.test_ran = False

        def visit_Module(self, node: ast.Module) -> ast.Module:
            self.test_ran = True
            return node

    fake_filename_for_test = "fake_filename_for_test"
    fake_ast_for_test = ast.parse("def foo(): pass", filename=fake_filename_for_test, mode="exec")
    fake_ast_for_test = ast.fix_missing_locations(fake_ast_for_test)

    transformer = TestTransformer()

# Generated at 2022-06-14 01:59:43.255853
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:53.844147
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    data = '''
    def my_function():
        print('Hello, World!')
    '''
    source = list(ast.parse(data).body)

# Generated at 2022-06-14 02:00:05.086250
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = """
    print(1)
    """
    tt = ast.parse(code)
    t = Python2FutureTransformer()
    t.visit(tt)

# Generated at 2022-06-14 02:00:16.372463
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils import parse_ast, roundtrip_unparse
    from .base import Python2to3FixerTestCase
    from .base import dict_to_node, wrap_in_module
    class TestCase(Python2to3FixerTestCase):
        fixer = Python2FutureTransformer
        def test_simple_module(self):
            module = wrap_in_module({'a': 1, 'b': 2})
            fixed = imports.get_module(future='__future__') + roundtrip_unparse(module)  # type: ignore
            assert self.fix(module) == fixed
            node_fixed = parse_ast(fixed)
            assert node_fixed == dict_to_node({'a': 1, 'b': 2})
    from unittest import main
    main

# Generated at 2022-06-14 02:00:28.127218
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Setup
    import astor
    import textwrap
    node = ast.parse(textwrap.dedent(""" \
        # This is a comment
        import os
        def foo():
            return 42
        """))
    expected = textwrap.dedent("""
        # This is a comment
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import os
        def foo():
            return 42
        """)

    # Exercise
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    # Verify
    assert astor.to_source(new_node) == expected



# Generated at 2022-06-14 02:00:29.884024
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:00:36.726263
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse('import ast')
    transformer = Python2FutureTransformer.instance(target_version=(2, 7))
    tree = transformer.visit(tree)
    assert transformer.tree_changed
    expected = 'from __future__ import absolute_import\n'\
               'from __future__ import division\n'\
               'from __future__ import print_function\n'\
               'from __future__ import unicode_literals\n'\
               '\n'\
               'import ast\n'
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:00:38.092303
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:00:48.002981
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """
import io
import os
import sys
import sysconfig

if sys.version_info[0] < 3:
    import imp
    import urllib2
    import urllib
else:
    import importlib.util
    import urllib.request
    import urllib.parse

_PY_PY2 = sys.version_info[0] == 2
"""
    source_tree = ast.parse(source)
    source_tree = Python2FutureTransformer().visit(source_tree)
    result = ast.dump(source_tree)

# Generated at 2022-06-14 02:00:54.607676
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ..utils.ast_helpers import make_module_for_transformation

    code = """
    import sys
    import os

    """
    expected_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import sys
    import os
    """
    before = ast.parse(code)
    after = Python2FutureTransformer.transform(before)
    assert astor.to_source(after) == expected_code

# Generated at 2022-06-14 02:01:15.534201
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = dedent('''\
        def f ():
            pass
        ''')
    expected = dedent('''\
        from future import absolute_import
        from future import division
        from future import print_function
        from future import unicode_literals
        def f ():
            pass
        ''')
    assert transform(Python2FutureTransformer, source) == expected
    assert Python2FutureTransformer.transformed(source)



# Generated at 2022-06-14 02:01:25.930036
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
  assert issubclass(Python2FutureTransformer, BaseNodeTransformer), 'should be subclass of `BaseNodeTransformer`'

  with open('./tests/fixtures/transforms/python2/future.py', 'rb') as file_content:
    py_tree = ast.parse(file_content.read())
    py_tree = Python2FutureTransformer().visit(py_tree)
    python2_future_import = imports.get_body(future='__future__')
    assert str(py_tree.body[0]) == str(python2_future_import[0]), 'python2 future should contain __future__ import'
    assert str(py_tree.body[1]) == str(python2_future_import[1]), 'python2 future should contain __future__ import'

# Generated at 2022-06-14 02:01:27.045102
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer

# Generated at 2022-06-14 02:01:29.150743
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)

# Generated at 2022-06-14 02:01:39.795795
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import_node = ast.ImportFrom(module='__future__',
                                 names=[
                                     ast.alias(
                                         name='absolute_import',
                                         asname=None),
                                     ast.alias(
                                         name='division',
                                         asname=None),
                                     ast.alias(
                                         name='print_function',
                                         asname=None),
                                     ast.alias(
                                         name='unicode_literals',
                                         asname=None)
                                 ],
                                 level=0)
    module = ast.Module([])
    module_future = Python2FutureTransformer().visit(module)
    assert module_future.body[0].names[0].name == \
        import_node.names[0].name
    assert module_future.body[0].names[1].name

# Generated at 2022-06-14 02:01:49.972127
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from pprint import pprint
    from ..testing_utils import assert_valid_ast
    import sys
    import os

    #
    # This snippet
    snippet_path = os.path.join(
        os.path.dirname(__file__), '../..', 'snippets', 'imports.py')
    node = ast.parse(open(snippet_path).read())  # type: ast.Module
    print('\n## Before future imports:')
    pprint(ast.dump(node))
    #
    # is transformed into this snippet
    expected = ast.parse(open(snippet_path).read())  # type: ast.Module
    expected.body = imports.get_body(future='__future__') + expected.body  # type: ignore


# Generated at 2022-06-14 02:01:50.644756
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

# Generated at 2022-06-14 02:01:59.218089
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .fixtures import make_node
    from ..managers import node_manager
    from typed_ast.ast3 import Module, Name, Load

    node_manager.register(Python2FutureTransformer)

    node = make_node(
        Module,
        body=[
            make_node(Name, id='a'),
        ]
    )

    assert str(node_manager.visit(node)) == """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

a"""

# Generated at 2022-06-14 02:02:00.235571
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:02:11.069081
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    fixture = Python2FutureTransformer(None)

# Generated at 2022-06-14 02:02:42.410418
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is not None


# Generated at 2022-06-14 02:02:49.239536
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.fixtures import some_module
    from ..utils.source import Source
    from ..utils.visitor import print_node

    source = Source(some_module)
    parsed = ast.parse(source.read())
    assert parsed.body[0].value.s == 'some_module'
    assert parsed.body[1].value.s == 'foo - module'
    # parsed = Python2FutureTransformer().visit(parsed)      # type: ignore
    # print(print_node(parsed))


# Generated at 2022-06-14 02:02:50.394745
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
        assert isinstance(Python2FutureTransformer(), BaseNodeTransformer)

# Generated at 2022-06-14 02:02:50.918209
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 02:02:57.323740
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
  """Test transform snippet:
  # BEGIN IMPORTS
  import os
  import subprocess
  import codecs
  import sys
  # END IMPORTS
  """
  t = Python2FutureTransformer()
  t.visit_Module(ast.parse(test_Python2FutureTransformer_visit_Module.__doc__.strip()))
  assert not t._tree_changed
  t = Python2FutureTransformer()
  t.visit_Module(ast.parse("""
  # BEGIN IMPORTS
  import os
  import subprocess
  # END IMPORTS
  from future.utils import with_metaclass
  """))
  assert t._tree_changed

# Generated at 2022-06-14 02:03:01.850735
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    assert astor.to_source(Python2FutureTransformer().visit(ast.parse("2+2"))) == '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

2 + 2'''

# Generated at 2022-06-14 02:03:07.896064
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    with_future = Python2FutureTransformer().transform_module(
        '''
        print('Hello World!')
        ''')

    assert with_future == dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        print('Hello World!')
        ''')

# Generated at 2022-06-14 02:03:14.797653
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse(textwrap.dedent("""
        print('test')
        from os import path
        from os.path import join
    """))
    transformer = Python2FutureTransformer(target=(2, 7))
    node = transformer.visit(node)
    assert ast.dump(node) == ast.dump(ast.parse(textwrap.dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        print('test')
        from os import path
        from os.path import join
    """)))

# Generated at 2022-06-14 02:03:24.721947
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import ast_from_snippet
    from ..utils.source_code import Source

    source = Source(
        '''
        print('test')
        '''
    )
    tree = ast.parse(str(source))
    visitor = Python2FutureTransformer()
    visitor.visit(tree)
    assert str(source) == imports.get_code(future='__future__') + "\nprint('test')\n"

# Generated at 2022-06-14 02:03:32.353939
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    source = """
a = 5
b = 6
"""
    tree = ast.parse(source)
    Python2FutureTransformer(tree).visit(tree)
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

a = 5
b = 6
"""
    assert astor.to_source(tree).strip() == expected.strip()
test_Python2FutureTransformer_visit_Module()

# Generated at 2022-06-14 02:04:38.154274
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    trans = Python2FutureTransformer()
    assert trans.target == (2, 7)


# Generated at 2022-06-14 02:04:40.208136
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert repr(Python2FutureTransformer((2, 7))) == "<Python2FutureTransformer [2.7]>"

# Generated at 2022-06-14 02:04:47.256990
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from autoflake import remove
    from autoflake.transformers.future_transformers import Python2FutureTransformer

    module = ast.parse("from future import print_function")  # type: ignore
    Python2FutureTransformer().visit(module)
    assert remove(ast.dump(module)) == remove(
        "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import "
        "print_function\nfrom __future__ import unicode_literals\nfrom future import print_function"
    )

# Generated at 2022-06-14 02:05:01.879288
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import sys
    import os
    import astor
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    from python_transpile.utils import test_ast
    from python_transpile.utils import test_ast_error
    from python_transpile.python_2_transpile import Python2Transpiler
    from python_transpile.utils import get_ast
    from python_transpile.utils import get_source

    # class declarations
    class_source_code = """
    class DummyClass:
        pass
    """
    class_tree = get_ast(class_source_code)
    assert not test_ast(class_tree, Python2FutureTransformer)