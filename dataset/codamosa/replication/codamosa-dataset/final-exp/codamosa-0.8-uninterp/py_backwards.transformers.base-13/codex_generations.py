

# Generated at 2022-06-14 01:44:21.110352
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('baz', 'qux'),
        ]

    tree = ast.parse("""
        import foo
        import foo.bar
        import baz
        import baz.qux
        import quuz
    """)

    expected = ast.parse("""
        try:
            import foo
        except ImportError:
            import bar
        try:
            import foo.bar
        except ImportError:
            import bar.bar
        try:
            import baz
        except ImportError:
            import qux
        try:
            import baz.qux
        except ImportError:
            import qux.qux
        import quuz
    """)  # yapf: disable

    result = TestBase

# Generated at 2022-06-14 01:44:26.819684
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import sys
    import six

    def test(rewrites: List[Tuple[str, str]], input: str, output: str) -> None:
        class Test(BaseImportRewrite):
            rewrites = rewrites

        tree = ast.parse(input)
        Test.transform(tree)
        assert output == astor.to_source(tree)

    test(rewrites=[('six', 'six.moves')], input="import six", output="""try:
    import six
except ImportError:
    import six.moves as six""")

# Generated at 2022-06-14 01:44:33.277721
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    tree = ast.parse("""
import six
import types""")
    transformer = BaseImportRewrite({'six': 'six'})
    new_tree = transformer.visit(tree)

    expected = ast.parse("""
try:
    import six
except ImportError:
    import six
import types""")

    assert astor.to_source(new_tree) == astor.to_source(expected)



# Generated at 2022-06-14 01:44:42.555400
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ast import fix_missing_locations
    from .utils import parse_ast

    from_ = 'pandas'
    to = 'pandas_extras'
    module_name = 'pd'

    class RewriteTransformer(BaseImportRewrite):
        rewrites = [(from_, to)]

    ast_node = fix_missing_locations(ast.Import(
        names=[ast.alias(
            name=from_,
            asname=module_name)]))

    try_ast_node = RewriteTransformer._replace_import(  # pylint: disable=protected-access
        ast_node, from_, to)

# Generated at 2022-06-14 01:44:52.123182
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    from ..utils.testing import get_test_nodes

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            (
                'foo',
                'bar'
            )
        ]

    class Test(unittest.TestCase):
        def test(self):
            for node in get_test_nodes(
                'import foo',
                'import foo as foo_bar',
                'import foo.bar',
                'import foo.bar as foo_bar'
            ):
                new = TestTransformer.transform(node)
                self.assertIsInstance(new.tree, ast.Try)

# Generated at 2022-06-14 01:45:02.405758
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import TransformationResult
    from .common import get_ast
    import ast
    import unittest

    mock_tree = get_ast('import six')
    result = BaseImportRewrite.transform(mock_tree)
    assert isinstance(result, TransformationResult)
    assert isinstance(result.tree, ast.AST)
    assert result.tree_changed is False

    mock_tree = get_ast('import six_next')
    result = BaseImportRewrite.transform(mock_tree)
    assert result.tree_changed is True
    assert 'six_next' not in str(result.tree)
    assert 'six_next' in str(result.tree.body[0].body[1].body[0].body[0])

# Generated at 2022-06-14 01:45:13.894686
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    node = ast.Import(names=[ast.alias(name='import_target',
                                       asname='import_target')])
    class Rewrite(BaseImportRewrite):
        rewrites = [
            ('import_target', 'rewrite_target')]

    res = Rewrite.transform(node)

    expected = ast.Try(
        body=[ast.Import(names=[ast.alias(name='rewrite_target',
                                         asname='import_target')])],
        handlers=[ast.ExceptHandler(
            type=ast.Name(id='ImportError', ctx=ast.Load()),
            name=None,
            body=[ast.Import(names=[ast.alias(name='import_target',
                                              asname='import_target')])])],
        orelse=[],
        finalbody=[])

   

# Generated at 2022-06-14 01:45:24.551948
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import asttokens

    def _assert_rewrote(rewrites):
        tree = ast.parse('''from foo import bar, baz''')
        BaseImportRewrite.rewrites = rewrites
        BaseImportRewrite.visit(tree)
        atok = asttokens.ASTTokens(source=None, tree=tree)
        assert 'from foo import bar' in atok
        assert 'from _bar import bar' in atok

    class Bar(BaseImportRewrite):
        rewrites = (('foo', '_bar'),)

    class Baz(BaseImportRewrite):
        rewrites = (('foo.bar', '_bar.bar'),)

    _assert_rewrote(Bar.rewrites)
    _assert_rewrote(Baz.rewrites)

# Generated at 2022-06-14 01:45:33.955518
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import to_source
    from ..compiler import Compiler

    source = to_source(ast.Import(names=[ast.alias(name='logging', asname='logging')]))
    compiler = Compiler(CompilationTarget.PY35)
    result = compiler.transform(source)
    assert result.code == source

    source = to_source(ast.Import(names=[ast.alias(name='urlparse', asname='urlparse')]))
    compiler = Compiler(CompilationTarget.PY35)
    result = compiler.transform(source)

    source_expected = """\
try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse"""

    assert result.code == source_expected



# Generated at 2022-06-14 01:45:45.142391
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils import compile_and_transform_ast


# Generated at 2022-06-14 01:46:01.651329
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('''
from ast import copy_location
from os import path
import sys

from ast import parse as ast_parse

from os.path import sep
from os import path as os_path
''')

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('ast', 'typed_ast'),
            ('os.path', 'os.path'),
        ]

    new_tree, changed, _ = TestImportRewrite.transform(tree)
    assert changed

# Generated at 2022-06-14 01:46:12.021237
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from ..fake import TestTransformer

    import_from = ast.ImportFrom(
        module='sqlalchemy',
        names=[
            ast.alias(name='Table'),
            ast.alias(name='Column', asname='col')],
        level=0)

    tree = ast.parse('''
import sqlalchemy

from sqlalchemy import Table, Column as col
''')
    transformer = TestTransformer(tree)
    import_rewrite = transformer._name_visiter
    import_rewrite.rewrites = [('sqlalchemy', 'sqlalchemy.ext.declarative')]
    import_rewrite.visit(tree)
    print(import_rewrite._tree)

# Generated at 2022-06-14 01:46:21.405907
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..utils import compile_as_module

    class Rewriter(BaseImportRewrite):
        rewrites = [
            ('foo.bar', 'qux.quux')
        ]

    test_inputs = [
        'import foo.bar.test',
        'from foo import bar',
        'from foo import bar as test',
        'from foo import bar.test as test',
        'from foo.bar import test',
        'from foo.bar import test as test',
        'from foo.bar import test.names as test',
    ]


# Generated at 2022-06-14 01:46:31.380709
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import test.utils
    
    t = BaseImportRewrite()
    test_import = ast.parse("import time").body[0]
    assert t.visit(test_import) == test_import
    
    test_import = ast.parse("import concurrent.futures").body[0]
    
    t.rewrites = [
        ('concurrent.futures', 'concurrent_futures')
    ]
    
    expected = test.utils.as_source(
        """
        try:
            import concurrent.futures
        except ImportError:
            import concurrent_futures
        """
    )

    assert test.utils.as_source(t.visit(test_import)) == expected


# Generated at 2022-06-14 01:46:45.679901
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('''import re''')
    BaseImportRewrite.transform(tree)
    assert ast.dump(tree) == ast.dump(ast.parse('''import re'''))

    tree = ast.parse('''import re as reg''')
    BaseImportRewrite.transform(tree)
    assert ast.dump(tree) == ast.dump(ast.parse('''import re as reg'''))

    tree = ast.parse('''from re import fullmatch''')
    BaseImportRewrite.transform(tree)
    assert ast.dump(tree) == ast.dump(ast.parse('''from re import fullmatch'''))

    tree = ast.parse('''from re import fullmatch as fm''')
    BaseImportRewrite.transform(tree)
    assert ast.dump(tree)

# Generated at 2022-06-14 01:46:50.619310
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import module')
    rewriter = BaseImportRewrite(tree)
    rewriter.rewrites = [('module', 'new_module')]
    rewriter.visit(tree)
    expected = "try:\n    import new_module\nexcept ImportError:\n    import module"
    assert ast.dump(tree) == expected


# Generated at 2022-06-14 01:46:58.400581
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    tree = ast.parse('import foo')
    transformer = BaseImportRewrite(tree)  # type: ignore
    transformer.rewrites = [('baz', 'foo')]
    result = transformer.visit(tree)
    assert astor.to_source(result) == 'try:\n    import foo\nexcept ImportError:\n    import foo'
    assert transformer._tree_changed == True



# Generated at 2022-06-14 01:47:09.727559
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse
    from pprint import pformat
    
    class TestTransformer(BaseImportRewrite):
        rewrites = [('urllib.request', 'urllib.request.new')]
        
    tree = parse('''
        from urllib.request import urlopen
        from urllib.request import Request
        from urllib.request import ProxyHandler
        from urllib.request.foo import bar

        import urllib.request.foo
    ''')

    result = TestTransformer.transform(tree)


# Generated at 2022-06-14 01:47:10.365052
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    pass

# Generated at 2022-06-14 01:47:19.299144
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.testing import compare_ast
    
    from . import python3x
    from . import python3x_mock

    for module in (python3x, python3x_mock):
        original_import_from = ast.parse(
            'from collections import OrderedDict, defaultdict').body[0]
        new_import_from = ast.parse('from pytest import test').body[0]

        transformer = BaseImportRewrite()
        transformer.rewrites.append(('collections', 'pytest')) # type: ignore

        result = transformer.visit_ImportFrom(original_import_from)
        expected = ast.Try(body=[new_import_from], # type: ignore
                           handlers=[],
                           orelse=[],
                           finalbody=[])


# Generated at 2022-06-14 01:47:35.708897
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import parse
    from ..transformers import BaseImportRewrite
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name') == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name1') == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name1.name') == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name1.name.name') == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name1.name.name.name') == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'name.name') == None
    assert BaseImportRewrite._get_matched_rew

# Generated at 2022-06-14 01:47:46.115220
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import typed_ast.ast3 as ast
    ast.parse('') # type: ast.AST
    transformer = BaseImportRewrite()

# Generated at 2022-06-14 01:47:51.585577
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Mock(BaseImportRewrite):
        rewrites = [('foo', 'mock_foo')]

    tree = ast.parse('import foo')
    trans = Mock.transform(tree)
    assert not trans.changed
    assert trans.changed_by_transformer.get(Mock.__name__, False)
    assert isinstance(ast.dump(trans.tree), str)



# Generated at 2022-06-14 01:48:01.971395
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    import unittest

    class TestRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    class Test(unittest.TestCase):
        def test_invalid(self):
            node = ast3.Import(names=[ast3.alias(name='foo.something')])
            self.assertEqual(ast3.dump(TestRewrite().visit(node)),
                             ast3.dump(node))

        def test_valid(self):
            node = ast3.Import(names=[ast3.alias(name='foo')])
            rewrote = TestRewrite().visit(node)

# Generated at 2022-06-14 01:48:12.285050
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    _locals = locals()
    test_source = """
import datetime

from datetime import datetime
"""
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('datetime', 'backports.datetime_fromisoformat'),
        ]
    test_ast = ast.parse(test_source)
    returned_ast = TestImportRewrite.transform(test_ast).tree
    print(ast.dump(returned_ast))

# Generated at 2022-06-14 01:48:22.539434
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..types import CompilationTarget
    from ..utils.source_generation import SourceGeneratorContext
    from ..utils.source_generation import SourceGeneratorHelper
    from ..utils.source_generation import AutoSourceGenerator
    from .parser import parse
    from .unparser import unparse
    from .modifier import SourceModifierContext
    from .modifier import SourceModifierHelper
    from .modifier import AutoSourceModifier
    import astor
    import astunparse

    class BaseImportRewrite_visit_ImportFromTestCase(AutoSourceGenerator, AutoSourceModifier):

        def __init__(self, target_tree, result_tree, target_source, result_source, **kwargs):
            super().__init__()
            self._result_source = result_source
            self._target_source = target_source
            self._

# Generated at 2022-06-14 01:48:26.311483
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class import_rewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    import_rewrite.visit_ImportFrom(ast.parse('from foo import *').body[0])


# Generated at 2022-06-14 01:48:37.211917
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrites = [('old', 'new')]

    class TestTransformer(BaseImportRewrite):
        rewrites = rewrites

    node = ast.parse("import math").body[0]
    expected = ast.parse("import new").body[0]
    assert isinstance(TestTransformer.transform(node).tree, list)
    assert TestTransformer.transform(node).tree[0].body[0].body[0] == expected

    rewrites = [('old.module1', 'new.module1')]
    node = ast.parse("from old.module1 import a, b").body[0]
    expected = ast.parse("from new.module1 import a, b").body[0]
    assert TestTransformer.transform(node).tree[0].body[0].body[0] == expected

    re

# Generated at 2022-06-14 01:48:47.675688
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    from ..utils.snippet import to_text, to_ast

    class Test(unittest.TestCase):
        def test(self):
            import_ast = to_ast('from foo import bar, foo as f, baz as b')
            from_ = 'foo'
            to = 'bar'
            rewrites = [(from_, to)]
            base_import_rewrite = BaseImportRewrite(import_ast)
            result = base_import_rewrite.visit_ImportFrom(import_ast)
            expected = to_text(
                "try:\n"
                "    from foo import bar as bar, foo as f, baz as b\n"
                "except ImportError:\n"
                "    from bar import bar as bar, foo as f, baz as b\n")

# Generated at 2022-06-14 01:48:57.555507
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    class A(BaseImportRewrite):
        rewrites = [('a', 'b'), ('c', 'd')]
    class B(BaseImportRewrite):
        rewrites = [('a', 'd'), ('c', 'e')]

    class TestCase(unittest.TestCase):
        def test_it(self):
            self.assertEqual(A.transform(ast.parse('''import a, c''')).tree,
                             B.transform(ast.parse('''import d, e''')).tree)
            self.assertEqual(A.transform(ast.parse('''import a.x''')).tree,
                             B.transform(ast.parse('''import d.x''')).tree)

# Generated at 2022-06-14 01:49:07.488313
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import TransformerTestCase

    import_rewrite_test_cases = TransformerTestCase.from_yaml_files(
        'import_rewrite.yaml', BaseImportRewrite)
    import_rewrite_test_cases.run_tests(BaseImportRewrite)


# Generated at 2022-06-14 01:49:18.446617
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    import os

    class MockTransformer(BaseImportRewrite):
        rewrites = [('old', 'new'),
                    ('foo', 'bar')]

    tree = ast.parse(
        'from old.a import a\n'
        'from foo.a import a\n'
        'from old.a import b\n'
        'from foo.b import b\n'
        'from old import a\n'
        'from foo import a\n'
        'from old import b\n'
        'from foo import b\n'
        'from old.a.b import b\n')

    MockTransformer.transform(tree)


# Generated at 2022-06-14 01:49:26.594727
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typing import Any

    from typed_ast import (ast3 as ast)

    from ..transpiler import BaseImportRewrite

    ast_module = ast.parse('import os')

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('os', 'my_os')]

    result = TestImportRewrite.transform(ast_module)

    assert result.tree.body[0].body[0].test.names[0].name == 'os'
    assert result.tree.body[0].body[1].names[0].name == 'my_os'



# Generated at 2022-06-14 01:49:38.371165
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    from typed_ast import ast3 as ast

    class Dummy(BaseImportRewrite):
        rewrites = [('typed_ast.ast3', 'typed_ast')]

    dummy = Dummy(None)
    imp = ast.parse('import from from from from from from from from')
    rewrote = dummy.visit_ImportFrom(imp.body[0])

    assert isinstance(rewrote, ast.Try)
    assert rewrote.handlers[0].type.id == 'ImportError'
    assert len(rewrote.body) == 1
    assert isinstance(rewrote.body[0], ast.ImportFrom)

    imp = ast.parse('from typed_ast.ast3 import SomeClass')
    rewrote = dummy.visit_ImportFrom(imp.body[0])


# Generated at 2022-06-14 01:49:46.205823
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import_from = astor.parse_statement("from imported.name import name")
    visitor = BaseImportRewrite(import_from)
    visitor.rewrites = [("imported.name", "rewrote_name")]
    visitor.visit(import_from)
    assert astor.to_source(import_from) == "try:\n    from imported.name import name\nexcept ImportError:\n    from rewrote_name import name"



# Generated at 2022-06-14 01:49:51.677141
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse
    import ast

    class Test(BaseImportRewrite):
        rewrites = [('subprocess', 'subprocess32')]

    tree = ast.parse("from subprocess import Popen")
    print("Before: {}".format(astunparse.unparse(tree)))
    tree = Test.transform(tree).tree
    print("After: {}".format(astunparse.unparse(tree)))

# Generated at 2022-06-14 01:49:58.367502
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..compilers.base import BaseCompiler
    from ..compilers.python import Python3Compiler
    import astunparse


# Generated at 2022-06-14 01:50:06.095946
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.ast_dump import dump
    import astor, copy

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')
        ]

    tree = ast.parse('''
import foo

from foo import bar, baz

from foo.qux import corge

from foo.bar.baz import quux

from foo.bar.baz import qux as quux_0

from foo.bar.baz import qux as quux_1, grault as garply_0, garply, waldo, fred as fred_0, fred

from foo import *
    ''')

    transformed = TestTransformer.transform(tree)
    transformed_tree = transformed.tree


# Generated at 2022-06-14 01:50:15.503997
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """Test for method visit_ImportFrom of class BaseImportRewrite"""
    import astor
    from ..types import CompilationTarget

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PY2

        rewrites = [
            ('future', 'past'),
        ]

    tree = ast.parse('''
    from future import __future__, generators
    from builtins import __builtin__
    import other
    import other.submodule
    ''')
    results = CompilationTarget.PY2.run(TestTransformer, tree)

# Generated at 2022-06-14 01:50:23.891298
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import pytest
    from ..utils.ast import parse_ast, ast_mysqlify
    from ..utils.dumper import ast_dump
    from ..utils.compiler import compile_source

    @register
    class PAIR(BaseImportRewrite):
        rewrites = [('sqlalchemy.sql.expression', 'mysql.connector.expression')]

    source = """
        from sqlalchemy.sql.expression import and_
        and_

        from sqlalchemy.sql.expression import and_
        and_()
    """


# Generated at 2022-06-14 01:50:47.101238
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils import nodes_equal
    from ..utils.compat import cmp

    class TestImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PY36
        rewrites = [
            ('test_import1', 'test_import2')
        ]

    test_snippet = 'import test_import1.module'
    expected = \
    'try:\n' \
    '    import test_import1.module\n' \
    'except ImportError:\n' \
    '    import test_import2.module'

    tree = ast.parse(test_snippet)
    TestImportRewrite.transform(tree)
    assert nodes_equal(expected, tree, ignore_attributes=['col_offset', 'lineno'])

# Generated at 2022-06-14 01:50:56.709857
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(module = 'six',
                                 names = [ast.alias(name = "odict",
                                                    asname = None),
                                          ast.alias(name = "string_types",
                                                    asname = None),
                                          ast.alias(name = "text_type",
                                                    asname = None),
                                          ast.alias(name = "reload_module",
                                                    asname = None),
                                          ast.alias(name = "next",
                                                    asname = None),
                                          ast.alias(name = "binary_type",
                                                    asname = None),
                                          ast.alias(name = "MovedAttribute",
                                                    asname = None)],
                                 level = 0)

    import_from_rewrite

# Generated at 2022-06-14 01:51:02.638819
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .x import base_import_rewrite as base
    tree = ast.parse("from urllib.error import HTTPError as HTTP_ERROR")
    tree = ast.fix_missing_locations(tree)
    base.rewrites = [('urllib.error', 'urllib3.error')]
    base.transform(tree)



# Generated at 2022-06-14 01:51:11.020845
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from ..utils.ast_to_source import ast_to_source

    for rewrite in (('itertools', 'typed_itertools'),
                    ('itertools.filterfalse', 'typed_itertools.filterfalse'),
                    ('typed_itertools', 'itertools'),
                    ('typed_itertools.filterfalse', 'itertools.filterfalse'),
                    ('random', 'typed_random'),
                    ('random.randint', 'typed_random.randint'),
                    ('typed_random', 'random'),
                    ('typed_random.randint', 'random.randint')):
        class TestTransformer(BaseImportRewrite):
            rewrites = [rewrite]

# Generated at 2022-06-14 01:51:22.926326
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.testutils import assert_contains, transform_test
    tree = ast.parse("from foo import bar")
    assert_contains(tree, ast.Name(id='foo', ctx=ast.Load()))

    result = transform_test(tree, [BaseImportRewrite.transform], rewrites=[('foo', '')])
    assert_contains(result, ast.Name(id='', ctx=ast.Load()))

    tree = ast.parse("from foo import bar")
    assert_contains(tree, ast.Name(id='foo', ctx=ast.Load()))

    result = transform_test(tree, [BaseImportRewrite.transform], rewrites=[('foo', 'baz')])

# Generated at 2022-06-14 01:51:31.329284
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..types import CompilationTarget

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON2
        rewrites = [('six', 'six2')]

    code = 'from six import iteritems'
    tree = ast.parse(code, '<test>', 'exec')

    result = TestTransformer.transform(tree)
    if result.tree_changed:
        code = compile(result.tree, '<test>', 'exec')
        exec(code, globals(), locals())

    # six.iteritems should be replaced with six2.iteritems
    assert 'six.iteritems' not in locals()
    assert 'six2.iteritems' in locals()



# Generated at 2022-06-14 01:51:40.685093
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse('''
        from os.path import relpath
        
        from sys import stdin, path, stdout

        from pyscipopt.scip import Model
        ''')
    transformer = BaseImportRewrite(tree)
    transformer.rewrites = [
        ('pyscipopt.scip', 'scipyopt'),
        ('os.path', 'os.path'),
    ]
    transformer.visit(tree)

# Generated at 2022-06-14 01:51:47.495173
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    @snippet
    def test_code(a, b, c):
        from a import b as c

    tree = ast.parse(test_code.code)
    rewrite = BaseImportRewrite.transform(tree)
    assert isinstance(rewrite.tree, ast.Try)
    assert rewrite.changed



# Generated at 2022-06-14 01:51:56.881105
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    module = ast.parse('''import asyncio
import sys''')
    BaseImportRewrite(module).visit(module)
    assert str(module) == '''import asyncio
import sys'''

    module = ast.parse('''import asyncio
import sys as sys1''')
    BaseImportRewrite(module).visit(module)
    assert str(module) == '''import asyncio
import sys as sys1'''

    module = ast.parse('''import asyncio
import sys.modules''')
    BaseImportRewrite(module).visit(module)
    assert str(module) == '''import asyncio
import sys.modules'''

    module = ast.parse('''import asyncio
import sys.modules as sys1''')
    BaseImportRewrite(module).visit(module)

# Generated at 2022-06-14 01:52:06.890944
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    tree = ast.parse("""
    import foo
    """)

    class Test(BaseImportRewrite):
        rewrites = [('foo', 'foo2'), ]

    Test.transform(tree)

    expected = """
    try:
        import foo
    except ImportError:
        import foo2 as foo
    """
    assert astor.to_source(tree) == expected
    tree = ast.parse("""
    import foo.bar as bar
    """)

    Test.transform(tree)

    expected = """
    try:
        import foo.bar as bar
    except ImportError:
        import foo2.bar as bar
    """
    assert astor.to_source(tree) == expected
    tree = ast.parse("""
    import foo2
    """)


# Generated at 2022-06-14 01:52:26.001876
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # import from
    from_ = ast.ImportFrom(
        module='os.path',
        names=[
            ast.alias(name='join', asname='j')
        ],
        level=0
    )
    # rewrite os to posixpath
    rewrote_import_from = BaseImportRewrite(ast.Module([from_]))
    rewrote_import_from.rewrites = [('os', 'posixpath')]
    rewrote_import_from.visit(from_)

    # expected import

# Generated at 2022-06-14 01:52:33.382236
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [('previous', 'current')]

    tree = ast.parse("""
import previous
""")

    expected = ast.parse("""
try:
    import previous
except ImportError:
    import current
""")

    assert Transformer.transform(tree).tree == expected


# Generated at 2022-06-14 01:52:42.686090
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    class T(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
        ]

    tree = ast.parse("""
        from foo import a, b
        from foo import c as _c, d as _d
        from foo import *
        from foo.some import a, b
        from foo.some import c as _c, d as _d
        from foo.some import *
        """)

    t = T(tree)


# Generated at 2022-06-14 01:52:55.049255
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.transform import parse_and_transform
    _, tree = parse_and_transform(
        """
import re
""",
        (BaseImportRewrite, {'rewrites': [('re', 're2')]}))
    assert tree.body[0].value.__class__ == ast.If
    assert tree.body[0].value.orelse == []
    assert tree.body[0].value.body[0].__class__ == ast.Import
    assert tree.body[0].value.body[0].names[0].name == 're'
    assert tree.body[0].value.body[1].__class__ == ast.Import
    assert tree.body[0].value.body[1].names[0].name == 're2'


# Generated at 2022-06-14 01:53:01.077441
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import os
    import sys

    from .transformer_test_case import TransformerTestCase, run_tests

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('test', 'test2')]

    class ImportRewriteTest(TransformerTestCase):
        transformer = ImportRewrite
        directory = os.path.dirname(__file__)
        target = sys.version_info[:2]

    run_tests(ImportRewriteTest)

# Generated at 2022-06-14 01:53:16.705495
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ast import parse
    import inspect
    from ..transformers.transformations import BaseImportRewrite

    nodes = {
        'rewrote_from_module': parse('from os import path'),
        'rewrote_from_names': parse('from typing import List, Optional'),
        'unrewrote_from_module': parse('from pkg_resources import resource_filename'),
        'unrewrote_from_names': parse('from typing import Mapping'),
    }

    def get_visit_method():
        return inspect.getmembers(BaseImportRewrite)[1][1]

    def get_transform_method():
        return inspect.getmembers(BaseImportRewrite)[5][1]

    def test_rewrote_from_module():
        visit_method = get_visit_method()

# Generated at 2022-06-14 01:53:24.022379
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..types import CompilationTarget

    class MyTransformer(BaseImportRewrite):
        target = CompilationTarget.PY2
        rewrites = [
            ('six', 'six.moves'),
            ('urllib', 'six.moves.urllib')]

    class_node = ast.parse(
        'class A:\n'
        '    def m(self):\n'
        '        from urllib import parse').body[0]
    assert astor.to_source(class_node) == (
        'class A:\n'
        '    def m(self):\n'
        '        from urllib import parse')

    function_node = ast.parse(
        'def f():\n'
        '    import urllib.request').body[0]


# Generated at 2022-06-14 01:53:32.004861
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import numpy as np
    import tensorflow as tf
    import tensorflow.contrib.layers as layers

    modules_to_replace = [
        ('tensorflow', 'keras'),
        ('tensorflow.contrib', 'tensorflow.contrib.keras'),
    ]

    # Original import
    nodes = ast.parse('''
        import numpy as np
        import tensorflow as tf
        from tensorflow.contrib import layers
    ''')

    class TestTransformer(BaseImportRewrite):
        rewrites = modules_to_replace
    
    assert TestTransformer.transform(nodes).changed == True

    # Original import with `as`

# Generated at 2022-06-14 01:53:42.346170
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Rewriter(BaseImportRewrite):
        rewrites = [
            ('module1', 'module2'),
            ('module3', 'module4')]

    # Test rewritten module
    node = ast.Import(names=[ast.alias(name='module1', asname=None),
                             ast.alias(name='module1.submodule', asname=None)])

# Generated at 2022-06-14 01:53:52.596773
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    ref = astor.code_to_ast('''
    try:
        from foo.bar.baz import x, y, z
    except ImportError:
        from bar.baz import x, y, z
    ''')
    result = astor.code_to_ast('''
    try:
        from foo.bar.baz import x, y, z
    except ImportError:
        from foo.baz import x, y, z
    ''')
    assert BaseImportRewrite._replace_import_from_names(ref, {
        'foo.bar.baz.x': ('foo.bar', 'foo')
    }) == result