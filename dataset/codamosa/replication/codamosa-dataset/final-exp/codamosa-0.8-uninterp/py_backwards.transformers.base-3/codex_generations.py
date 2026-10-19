

# Generated at 2022-06-14 01:44:13.797870
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    module = ast.parse('import foo; import foo as bar;')
    transformer = BaseImportRewrite([('foo', 'foo_mock')])
    transformer.visit(module)
    assert transformer.rewrites == [('foo', 'foo_mock')]
    assert transformer._tree_changed
    assert ast.dump(module) == '\n'.join([
        'try:',
        '    import foo',
        'except ImportError:',
        '    import foo_mock',
        'try:',
        '    import foo',
        'except ImportError:',
        '    import foo_mock',
    ])

# Generated at 2022-06-14 01:44:22.543668
# Unit test for method visit_ImportFrom of class BaseImportRewrite

# Generated at 2022-06-14 01:44:31.725881
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3
    from ..transforms import BaseImportRewrite
    from ..utils import compile_transformation, is_same_ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('a.b.c', 'a.b.x'),
            ('d.e.f', 'd.e.g')]

    def get_expected(module_name: str, import_names: List[str], rewrite_dict: Dict[str, str]) -> ast.Try:
        body_list = []

# Generated at 2022-06-14 01:44:42.264786
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import alias

    class T(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]


# Generated at 2022-06-14 01:44:53.827160
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import typed_ast.ast3 as ast

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('mymodule', 'foo')
        ]

    tree = ast.parse('import mymodule')

    class MockNodeTransformer:
        def generic_visit(self, node):
            pass

    transformer = TestTransformer(MockNodeTransformer())
    node_rewritten = transformer.visit_Import(tree.body[0])

    assert isinstance(node_rewritten, ast.Try)
    assert isinstance(node_rewritten.body[0], ast.ImportFrom)
    assert node_rewritten.body[0].module == 'foo'

    assert isinstance(node_rewritten.body[1], ast.ImportFrom)

# Generated at 2022-06-14 01:45:01.990937
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class MyImportRewrite(BaseImportRewrite):
        rewrites = [('dummy_from', 'dummy_to')]

    tree = ast.parse('import dummy_from')
    inst = MyImportRewrite(tree)
    result = inst.visit(tree)
    output = ast.dump(result)
    exp_output = 'Module(body=[Try(body=[import dummy_to as dummy_from],handlers=[ExceptHandler(type=None,name=None,body=[import dummy_from])],finalbody=[])])'
    assert output == exp_output



# Generated at 2022-06-14 01:45:08.098058
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astor import to_source
    tree = ast.parse('''import something''')
    transformer = BaseImportRewrite(tree)
    transformer.visit(tree)
    assert to_source(tree) == "try:\n    import something\nexcept ImportError:\n    pass\n"


# Generated at 2022-06-14 01:45:13.308145
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    module = ast.parse("from math import pow")
    _, func, _ = BaseImportRewrite.visit_ImportFrom(module.body[0])
    assert func.body[0].body[0].body[0].values[0].func.id == 'pow'
    assert func.body[0].body[0].body[0].values[0].args[0].n == 2
    assert func.body[0].body[0].body[0].values[0].args[1].n == 3
    assert isinstance(func.body[0].body[0].body[0].values[0].func, ast.Attribute)



# Generated at 2022-06-14 01:45:24.273586
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import six
    node = astor.code_to_ast('import six')
    transformer = BaseImportRewrite(node)
    transformed_node = transformer.visit_Import(node)
    assert astor.to_source(transformed_node) == \
        'try:\n    import six\nexcept ImportError:\n    from mysix import six'

    node = astor.code_to_ast('import sext', parser='unparse')
    transformer = BaseImportRewrite(node)
    transformed_node = transformer.visit_Import(node)
    assert astor.to_source(transformed_node) == \
        'try:\n    import sext\nexcept ImportError:\n    import six as sext'



# Generated at 2022-06-14 01:45:34.041577
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from_ = 'from foo import bar1, bar2'

    def test(to, expected_to):
        node = ast.parse(from_)
        rewrote = BaseImportRewrite(node).visit_ImportFrom(node.body[0])

        assert isinstance(rewrote, ast.Try)
        assert isinstance(rewrote.body[0], ast.ImportFrom)
        assert isinstance(rewrote.handlers[0].body[0], ast.ImportFrom)

        assert rewrote.body[0].names[0].name == to
        assert rewrote.handlers[0].body[0].names[0].name == expected_to

    test('foo.bar1', 'foo.bar1')
    test('foobar.bar1', 'foo.bar1')



# Generated at 2022-06-14 01:45:45.684355
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..types import CompilationTarget
    from ..utils.helpers import parse_text

    class Transformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_2
        rewrites = [
            ('textwrap', 'textwrap2'),
            ('py2', 'py2_py3')
        ]


# Generated at 2022-06-14 01:46:00.663146
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse

    rewrites = [
        ('foo', 'foo_rewrite'),
        ('food', 'food_rewrite'),
        ('foobar', 'foobar_rewrite')]

    class ImportRewrite(BaseImportRewrite):
        rewrites = rewrites

    tree = parse('from foo import *\n'  # original tree
                 'from foo import a, b\n'
                 'from food import c\n'
                 'from foobar import d as d_rewrite\n'
                 'from foo.bar import e\n')

    ImportRewrite.transform(tree)


# Generated at 2022-06-14 01:46:12.498568
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Rewriter(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('''
from foo import name1, name2
from spam.foo import name3, name4
from .spam import name5
from spam import name6, name7
import spam.name8
''')

# Generated at 2022-06-14 01:46:21.735095
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():  # noqa
    from typed_ast import ast3 as typed
    import unittest


# Generated at 2022-06-14 01:46:31.812604
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('package1', 'package2'),
            ('package3.subpackage1', 'package3.subpackage2')
        ]

    tree = ast.parse("""
import package1.module1
from package2 import module2
from package3.subpackage1 import module3
""")
    expected_tree = ast.parse("""
import package2.module1
from package2 import module2
try:
    from package3.subpackage1 import module3
except ImportError:
    from package3.subpackage2 import module3
""")

    transformed = TestTransformer.transform(tree)

    assert(transformed.changed)
    assert(transformed.updated_tree)

# Generated at 2022-06-14 01:46:43.060730
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast as original_ast
    from .test_data import test_data


# Generated at 2022-06-14 01:46:55.262151
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from _fixtures.modules import module_six_text
    from ..utils.tree import ast_from_module

    class TestClass(BaseImportRewrite):
        rewrites = [('six', 'six_moves')]

    module = ast_from_module(module_six_text)
    module = TestClass().visit(module)

    assert module._fields == ('body',)
    assert module.body[1]._fields == ('body',)
    assert module.body[1].body[1]._fields == ('body',)
    assert module.body[1].body[1].body[0]._fields == ('body',)
    assert module.body[1].body[1].body[0].body[0]._fields == ('test', 'body', 'orelse')

# Generated at 2022-06-14 01:47:04.876345
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
        dependencies = []

    tree = ast.parse('from foo import baz\n')  # type: ignore
    result = TestTransformer.transform(tree)
    expected_tree = ast.parse('try:\n    from foo import baz\nexcept ImportError:\n    from bar import baz\n')  # type: ignore
    expected_result = TransformationResult(expected_tree, True, [])
    assert result == expected_result



# Generated at 2022-06-14 01:47:15.611699
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import parse, ast3
    from typed_ast import ast3 as ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('typed_ast', 'typed_ast.ast3')]

    sample = """
import socket
from six.moves import range, queue
import six
from six import moves
from socket import *

import http.client as client
from http.client import *

from http.client import HTTPResponse

from socket import socket as Socket
"""

# Generated at 2022-06-14 01:47:28.837227
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import astor
    stmt1 = ast.ImportFrom(module='module_a', names=[ast.alias(name='name1', asname=None)], level=0)
    stmt2 = ast.ImportFrom(module='module_a', names=[ast.alias(name='name2', asname=None)], level=0)
    stmt3 = ast.ImportFrom(module='module_b', names=[ast.alias(name='name', asname=None)], level=0)
    stmt4 = ast.ImportFrom(module='module_b', names=[ast.alias(name='name1', asname=None)], level=0)
    stmt5 = ast.ImportFrom(module='module_b.c', names=[ast.alias(name='name', asname=None)], level=0)


# Generated at 2022-06-14 01:47:45.684557
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from typed_ast import ast3 as ast

    class TestTransformer(BaseImportRewrite):
        rewrites = [('previous-name', 'new-name')]


# Generated at 2022-06-14 01:47:51.579568
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typing
    from typed_ast import ast3 as ast
    from typed_ast import ast3 as typed_ast
    from typed_ast.transforms.import_rewrites import BaseImportRewrite

    class TestTransformer(BaseImportRewrite):
        target = 'py2'
        rewrites = [('typing', 'future')]

    node = ast.parse('import typing').body[0]
    assert node.names[0].name == 'typing'

    assert isinstance(TestTransformer.transform(typed_ast.parse('import typing'))[0].body[0],
                      ast.Try)



# Generated at 2022-06-14 01:47:59.858633
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    stmts = [ast.Import(names=[ast.alias(name="foo.old")])]
    new_stmts = BaseImportRewrite.transform(stmts).new_tree
    assert astor.to_source(new_stmts) == """\
try:
    import foo.old as foo_old
except ImportError:
    import foo.new as foo_old"""

    stmts = [ast.Import(names=[ast.alias(name="foo.old", asname="bar")])]
    new_stmts = BaseImportRewrite.transform(stmts).new_tree
    assert astor.to_source(new_stmts) == """\
try:
    import foo.old as bar
except ImportError:
    import foo.new as bar"""

# Unit

# Generated at 2022-06-14 01:48:06.917035
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    src = 'from foo import baz'
    node = ast.parse(src).body[0]
    tree = TestTransformer.transform(node)
    assert tree.tree.body[0].body[0].value.value == 'baz'
    assert tree.tree.body[0].body[2].body[0].value.value == 'from bar import baz'


# Generated at 2022-06-14 01:48:16.825739
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('pip', 'pip._internal.main'),
            ('six.moves.queue', 'queue'),
            ('sys', 'six.moves')
        ]
    mod = ast.parse("""import pip
    import os
    import sys
    import six.moves.queue as q
    import six
    import sys.platform""")
    class_ = MyBaseImportRewrite(mod)
    class_.visit(mod)

# Generated at 2022-06-14 01:48:22.888829
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_ = ast.Import(names=[ast.alias(name='foo.bar')])
    rewrite = BaseImportRewrite(import_)
    try_ = rewrite.visit(import_)
    assert isinstance(try_, ast.Try)
    assert isinstance(try_.body[0], ast.Import)
    assert isinstance(try_.body[1], ast.ExceptHandler)


# Generated at 2022-06-14 01:48:28.698275
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node = ast.parse('from requests import get, post').body[0]
    rewrites = [('requests', 'requests_rewrite')]
    transformer = BaseImportRewrite(ast.parse(''))  # type: ignore
    transformer.rewrites = rewrites
    rewrote = transformer.visit_ImportFrom(node)
    print(ast.dump(rewrote))



# Generated at 2022-06-14 01:48:38.500338
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import a as b')
    t = BaseImportRewrite(tree)
    t.rewrites = [('a', 'c')]
    result = t.visit(tree)
    assert result.body[0].body[0].values[0].value.elts[0].value.names[0].name == 'a'
    assert result.body[0].body[0].values[0].value.elts[0].value.names[0].asname == 'b'
    assert result.body[0].body[1].values[0].value.elts[0].value.names[0].name == 'c'
    assert result.body[0].body[1].values[0].value.elts[0].value.names[0].asname == 'b'

# Generated at 2022-06-14 01:48:43.835950
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from unittest.mock import Mock
    from ..utils.testutils import assert_ast_equal

    rewrites = [('six', 'six.moves')]
    node = ast.parse("from six import Iterator")

    expected = ast.parse("""
    try:
        from six import Iterator
    except ImportError:
        from six.moves import Iterator
    """)

    class Transformer(BaseImportRewrite):
        rewrites = rewrites

    assert_ast_equal(expected, Transformer.transform(node).tree)

# Generated at 2022-06-14 01:48:49.652478
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest.mock as mock
    import_node = mock.Mock(name="import_node", module="module", names=[mock.Mock(name="alias",
                                                                                   name="name")])
    baseImportRewrite = BaseImportRewrite()
    baseImportRewrite.rewrites = [('x', 'y')]
    import_node.name = 'x'
    assert baseImportRewrite.visit_Import(import_node) is not None

# Generated at 2022-06-14 01:49:02.973561
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astunparse import unparse
    from astor import parse
    from .utils import get_node

    class MyTransformer(BaseImportRewrite):
        rewrites = [
            ('six', 'future.moves.six')]

    source = get_node('''
        import six
        import future.moves.six as m
    ''')

    result = MyTransformer().visit(source)
    assert unparse(result) == unparse(source)

    source = get_node('''
        import six
    ''')
    rewrote = MyTransformer().visit(source)
    expected = parse('try:\n    import six\nexcept ImportError:\n    import future.moves.six')
    assert unparse(rewrote) == unparse(expected)



# Generated at 2022-06-14 01:49:14.324869
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import get_ast_node, get_ast_node_func

    class SampleImportsRewrite(BaseImportRewrite):
        rewrites = [('oldmodule', 'newmodule'),
                    ('.oldmodule', '.newmodule')]


# Generated at 2022-06-14 01:49:25.220990
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    passes = [BaseImportRewrite]
    code_in = 'import os'
    code_out = code_in

    node = ast.parse(code_in)
    BaseImportRewrite.transform(node)
    assert code_out == ast.unparse(node)

    code_in = 'import typing'
    code_out = 'try:\n    import typing\nexcept ImportError:\n    pass'

    node = ast.parse(code_in)
    BaseImportRewrite.transform(node)
    assert code_out == ast.unparse(node)

    code_in = 'from typing import List, Any'
    code_out = code_in

    node = ast.parse(code_in)
    BaseImportRewrite.transform(node)
    assert code_out == ast.unparse(node)

    code_

# Generated at 2022-06-14 01:49:37.207054
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import typing

    from obj_tables.utils.import_rewrite import BaseImportRewrite

    class TestTransformer(BaseImportRewrite):
        rewrites = (
            ('dummy', 'actual'),
        )

        def visit_ImportFrom(self, node):
            return super().visit_ImportFrom(node)

    transformer = TestTransformer.from_string(
        'from dummy.dummy import dummy\n'
        'from dummy import dummy\n'
        'from dummy.dummy import *\n'
        'from dummy import *\n'
    )
    assert isinstance(transformer, TestTransformer)

    class TestTransformer(BaseImportRewrite):
        rewrites = (
            ('dummy.dummy', 'actual.actual'),
        )


# Generated at 2022-06-14 01:49:45.615810
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import os
    import unittest
    import typed_ast.ast3 as ast
    from ..base import BaseImportRewrite

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('test.test_module', 'os.path')]

    class Test(unittest.TestCase):
        def setUp(self):
            self.rewriter = TestImportRewrite(None)

        def test_generic_visit(self):
            self.assertTrue(
                self.rewriter.generic_visit(ast.Import(
                    names=[ast.alias(name='os', asname='os')])))

        def test_rewrite(self):
            rewritten = self.rewriter.visit_Import(
                ast.Import(names=[ast.alias(name='test.test_module')]))
           

# Generated at 2022-06-14 01:49:56.259747
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import sys
    import os
    import re
    import textwrap
    import six
    import inspect
    import ast
    import astmonkey
    import astunparse

    # unit tests for a function named BaseImportRewrite.visit_ImportFrom
    # ast of the function after transforming BaseImportRewrite.visit_ImportFrom
    # the test is based on BaseImportRewrite.visit_ImportFrom and snippet named import_rewrite
    # the file of snippet is /Users/dave/src/python-ast-transformer/python_ast_transformer/transformers/base.py
    # the line number of snippet is 66
    # the path in project of snippet is python_ast_transformer/transformer/base.py
    #
    # set 'input_ast' to ast of the function after transforming BaseImportRewrite.visit_

# Generated at 2022-06-14 01:49:59.501364
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # import_rewrite_test_case.test_import_rewrite_from_names_changes_rewritted_names is test case.
    # `from xx import a, b as c`
    # `from xx import a, b as c`
    pass

# Generated at 2022-06-14 01:50:10.784833
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import tempfile
    from textwrap import dedent

    from typing import Any, Dict
    from typed_ast import ast3 as ast

    from ..utils.astparser import parse_ast
    from ..transforms.base import BaseImportRewrite

    def _get_rewrite_class(rewrites: Dict[str, str]) -> BaseImportRewrite:
        class Rewriter(BaseImportRewrite):
            rewrites = list(rewrites.items())

        return Rewriter

    def _check_import_from(code: str, 
                           rewrites: Dict[str, str], 
                           expected: Optional[str] = None) -> None:
        if not expected:
            expected = code

        Rewriter = _get_rewrite_class(rewrites)
        _, filename = tempfile.mkstemp()


# Generated at 2022-06-14 01:50:21.311109
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse('''
from a import b as c, d
from e import f
from g import *
    ''')

    class SampleTransformer(BaseImportRewrite):
        rewrites = [
            ('a', 'x'),
            ('e', 'y')
        ]

    transformer = SampleTransformer(tree)
    rewritten = transformer.visit(tree)

# Generated at 2022-06-14 01:50:29.013981
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Create ast.AST instance
    tree = ast.parse('import foo')
    # Create instance of BaseImportRewrite and set rewrites attribute
    cls = BaseImportRewrite()
    cls.rewrites = [('foo', 'bar')]
    # Call method visit_Import by BaseImportRewrite
    result = cls.visit(tree)
    assert isinstance(result, ast.Try)
    assert isinstance(result.body[0], ast.Import)
    assert result.body[0].names[0].name == 'bar'
    assert result.body[0].names[0].asname == 'foo'
    assert isinstance(result.handlers[0].body[0], ast.Import)
    assert result.handlers[0].body[0].names[0].name == 'foo'

# Generated at 2022-06-14 01:50:46.916547
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class Test(BaseImportRewrite):
        rewrites = [
            ('test.test', 'typed_ast.test.test'),
            ('test', 'typed_ast.test')
        ]

    node = ast.parse('import test')
    expected = ast.parse('try:\n    import test\nexcept ImportError:\n    import typed_ast.test')
    assert Test.visit_Import(node) == expected
    expected = ast.parse('try:\n    import test.test\nexcept ImportError:\n    import typed_ast.test.test')
    assert Test.visit_Import(ast.parse('import test.test')) == expected


# Generated at 2022-06-14 01:50:50.148699
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from moto.core.compat import ast_str

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('moto', 'mymoto')]

    tree = ast.parse("""
from moto.ec2 import ec2_backend
ec2 = ec2_backend()
""", mode='exec')  # type: ignore
    expected = """
try:
    from moto.ec2 import ec2_backend
except ImportError:
    from mymoto.ec2 import ec2_backend
ec2 = ec2_backend()
"""
    assert ast_str(TestImportRewrite.transform(tree).tree) == expected

# Generated at 2022-06-14 01:51:00.534550
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.quack_ast import get_ast
    class TestImportRewrite(BaseImportRewrite):
        target = CompilationTarget('2.7')
        rewrites = [
            ('future.builtins', 'future.utils'),
            ('types', 'future.utils'),
            ('StringIO', 'io')]


# Generated at 2022-06-14 01:51:10.438663
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..utils.snippet import get_module_name, get_class_name, get_function_name, get_method_class_name, get_method_function_name

    module_name = get_module_name(BaseImportRewrite)
    class_name = get_class_name(BaseImportRewrite)
    function_name = get_function_name(BaseImportRewrite)
    method_class_name = get_method_class_name(BaseImportRewrite)
    method_function_name = get_method_function_name(BaseImportRewrite)

    # [0] Test full replacement of import from module
    source = """
    import os
    from datetime import datetime
    """

# Generated at 2022-06-14 01:51:22.620293
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ModelBaseImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PYTHON_UNIT_TEST
        rewrites = [('a', 'b')]

    tree = ast.parse("import a")
    class_ = ModelBaseImportRewrite(tree)
    result = class_.visit_Import(tree.body[0])
    assert isinstance(result, ast.Try)

# Generated at 2022-06-14 01:51:31.979833
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrite_class = BaseImportRewrite
    rewrite_class.rewrites = [
        ('module1', 'module2'),
        ('packageA.moduleB', 'packageC.moduleD')]
    input_code = """
import module1
import packageA.moduleB
from module1 import something
from packageA.moduleB import something
from packageA.moduleB import some_other_thing
from packageA.moduleB import *
from module1 import *
    """

# Generated at 2022-06-14 01:51:41.140439
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import astroid
    from py3.visitors.base import BaseImportRewrite

    class BaseTransformerMock(BaseImportRewrite):
        rewrites = [
            ('os', 'pathlib'),
            ]

    node = ast.parse("from os import path")
    tree = astroid.parse(astor.to_source(node))

    assert astor.to_source(node) == "from os import path"

    transformer = BaseTransformerMock(None)
    new_tree = transformer.visit(tree)

    assert astor.to_source(new_tree) == "import pathlib; try:\n    from os import path\nexcept ImportError:\n    from pathlib import path"

    node = ast.parse("from os.path import path, exists")
    tree = astroid.parse

# Generated at 2022-06-14 01:51:50.366939
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class Rewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('zoo', 'bee'),
        ]

    original = """
import foo.bar
import zoo.bee
import zoo
import foo
import zoop as z
"""

    expected = """
try:
    import foo.bar
except ImportError:
    import bar.bar

try:
    import zoo.bee
except ImportError:
    import bee.bee

try:
    import zoo
except ImportError:
    import bee

try:
    import foo
except ImportError:
    import bar

import zoop as z
"""

    tree = ast.parse(original)
    result = astor.to_source(Rewrite.transform(tree).tree)
    assert result == expected


#

# Generated at 2022-06-14 01:51:57.843710
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import CompilationTarget
    from ..utils.ast import parse


    class SpecificImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PYTHON_2
        rewrites = [
            ('io', 'io2'),
        ]


    tree = parse('import io')
    new_tree, changed, imports = SpecificImportRewrite.transform(tree)
    assert changed is True
    assert new_tree == parse('''
try:
    import io
except ImportError:
    import io2 as io
''')



# Generated at 2022-06-14 01:52:07.708656
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('from_1', 'to_1')]

    tree = ast.parse('''
import from_1
import from_1.abc
import from_1.abc as faa
''')

    TestImportRewrite.transform(tree)


# Generated at 2022-06-14 01:52:30.354062
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from typed_ast._ast3 import parse as parse3
    from typing import NamedTuple
    from typing import Union


    import_tree = parse3('''
    import module3;
    ''')
    class TransformationResult(NamedTuple):
        tree: ast.AST
        changed: bool
        dependencies: List[str]
        pass

    # test starts here
    import_tree = import_tree

    class BaseImportRewrite(BaseNodeTransformer):
        rewrites = [('module3', 'module2')]
        pass

    tree = import_tree
    inst = BaseImportRewrite(tree)
    
    node = parse3('''
    import module3;
    ''')
    node = inst.visit_Import(node)


# Generated at 2022-06-14 01:52:40.712421
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class DummyImportRewrite(BaseImportRewrite):
        pass

    class DummyImportRewriteWithRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('import foo')
    assert ast.dump(DummyImportRewrite().visit(tree)) == ast.dump(tree)

    assert ast.dump(DummyImportRewriteWithRewrite().visit(tree)) == \
        ast.dump(ast.parse('""""Try to import bar."""\ntry:\n    import bar\nexcept ImportError:\n    import foo'))



# Generated at 2022-06-14 01:52:54.644748
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.typed_ast import ast3 as ast

    import_rewrite = BaseImportRewrite([])

    tree = ast.parse("""
    from six import text_type
    from future.types import newbytes
    from aiohttp import ClientResponse
    from future.moves.urllib.response import addbase, addclosehook
    import errno
    """)
    visit = import_rewrite.visit_ImportFrom

    node = tree.body[0]
    assert isinstance(visit(node), ast.ImportFrom)

    node = tree.body[1]
    assert isinstance(visit(node).body[0], ast.Try)

    node = tree.body[2]
    assert isinstance(visit(node), ast.ImportFrom)

    node = tree.body[3]
   

# Generated at 2022-06-14 01:53:04.147971
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    trans = BaseImportRewrite([('datetime', 'datetime_compat')])
    from_ = ast.ImportFrom(
        module='datetime',
        names=[ast.alias(name='date')],
        level=0)
    to = ast.ImportFrom(
        module='datetime_compat',
        names=[ast.alias(name='date')],
        level=0)
    assert trans.visit(from_) == to

    from_ = ast.ImportFrom(
        module='datetime',
        names=[ast.alias(name='datetime')],
        level=0)
    to = ast.ImportFrom(
        module='datetime_compat',
        names=[ast.alias(name='datetime')],
        level=0)
    assert trans.visit(from_) == to


# Generated at 2022-06-14 01:53:16.235566
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    class DummyTransformer(BaseImportRewrite):
        rewrites = [
            ('os', 'MyModule'),
        ]

    tree = ast3.parse("""
import os
""")
    tree = ast3.fix_missing_locations(tree)
    assert tree.body[0]

    res = DummyTransformer.transform(tree)
    assert res.tree.body[0].body[0].body[0]
    assert ast3.dump(res.tree) == """try:
    import os
except ImportError:
    import MyModule"""



# Generated at 2022-06-14 01:53:21.460479
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    class Rewrite(BaseImportRewrite):
        rewrites = [('os', 'posix')]

    source = """from os import path, old
from os.path import join
from os.path import join as some_name
from os import path as os_path, old as os_old
"""

# Generated at 2022-06-14 01:53:30.505498
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test(BaseImportRewrite):
        rewrites = [('foo', 'foo_rewritten')]


# Generated at 2022-06-14 01:53:41.572072
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import_ = ast.ImportFrom(module='module.name', names=[
        ast.alias(name='name', asname=None)], level=0)
    import_.lineno = 1
    import_.col_offset = 1

    class TestTransformer(BaseImportRewrite):
        rewrites = [('module', 'new_module')]

    assert TestTransformer(import_).visit(import_) == import_rewrite.get_body(previous=import_,  # type: ignore
                                                                              current=ast.ImportFrom(module='new_module.name', names=[
    ast.alias(name='name', asname=None)], level=0))[0]

    assert TestTransformer(import_).visit(import_).lineno == 1

# Generated at 2022-06-14 01:53:50.431293
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('os.path', 'pathlib')]

    test_snippet = """
    import os.path
    """

    expected = import_rewrite.get_body(previous=ast.parse(test_snippet).body[0],  # type: ignore
                                       current=ast.parse('import pathlib').body[0])[0]
    node = ast.parse(test_snippet).body[0]
    result = ast.parse(test_snippet, type_comments=True).body[0]

    Test().visit(result)
    assert result == expected



# Generated at 2022-06-14 01:53:56.467239
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest.mock as mock

    class RewriteTestCase(unittest.TestCase):
        def test_import_rewrite(self):
            test_class = BaseImportRewrite
            test_class.rewrites = [('from', 'to')]
            tree = mock.MagicMock()
            node = mock.MagicMock()
            node.names = [mock.MagicMock()]
            node.names[0].name = 'from'
            node.names[0].asname = None

            result = test_class._replace_import(node, 'from', 'to')
            self.assertIsInstance(result, ast.Try)

    unittest.main()