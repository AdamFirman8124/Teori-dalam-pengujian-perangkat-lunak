

# Generated at 2022-06-14 01:44:17.595386
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from . import six
    tree = six.import_rewrite.parse()
    BaseImportRewrite.rewrites = [('six', 'six.moves')]
    new_tree = BaseImportRewrite.transform(tree)
    expected = six.import_rewrite_expected.parse()
    assert ast.dump(new_tree, include_attributes=False) == ast.dump(expected, include_attributes=False)


# Generated at 2022-06-14 01:44:27.802802
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.snippet import ast_parse, compilable


# Generated at 2022-06-14 01:44:38.899762
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    mock_dict = dict()

    def mock__replace_import_from_module(self, node: ast.ImportFrom, from_: str, to: str) -> ast.Try:
        mock_dict['from'] = from_
        mock_dict['to'] = to

    def mock__replace_import_from_names(self, node: ast.ImportFrom,
                                   names_to_replace: Dict[str, Tuple[str, str]]) -> ast.Try:
        mock_dict['from'] = names_to_replace['from']
        mock_dict['to'] = names_to_replace['to']

    import_from_names = [
    ast.alias(name='BaseApp',
              asname=None),
    ast.alias(name='Command',
              asname=None)
    ]

    real_from

# Generated at 2022-06-14 01:44:47.504790
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Arrange
    from ..utils.ast import get_ast
    tree = get_ast('''
a = 1
''')

    class RewriteTest(BaseImportRewrite):
        rewrites = [
            ('re', 'regex'),
            ]

    # Act
    result = RewriteTest.transform(tree)

    # Assert
    assert result.changed
    assert result.tree.body[0].value.func.value.func.value.id == 'regex'
    assert result.tree.body[0].value.func.value.func.attr == 'sub'



# Generated at 2022-06-14 01:44:57.039160
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class TestRewrites(BaseImportRewrite):
        rewrites = [('math', 'math2')]

    node = ast.Import([
        ast.alias(name='math.sin'),
    ])

    expected = ast.Try(
        body=[
            ast.Import([
                ast.alias(name='math.sin'),
            ]),
        ],
        handlers=[
            ast.ExceptHandler(
                type=ast.Name(id='ImportError'),
                name=None,
                body=[
                    ast.Import([
                        ast.alias(name='math2.sin'),
                    ])
                ],
                lineno=1,
                col_offset=0
            ),
        ],
        orelse=[],
        finalbody=[],
    )


# Generated at 2022-06-14 01:45:07.948646
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    class Test(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def testVisitImportFrom(self):
            class BaseImportRewrite(BaseNodeTransformer):
                rewrites = [('a', 'b')]

                def visit_ImportFrom(self, node):
                    import ast

                    rewrite = self._get_matched_rewrite(node.module)
                    if rewrite:
                        return self._replace_import_from_module(node, *rewrite)

                    names_to_replace = dict(self._get_names_to_replace(node))
                    if names_to_replace:
                        return self._replace_import_from_names(node, names_to_replace)

                    return self.generic_visit(node)

               

# Generated at 2022-06-14 01:45:14.908360
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Class(BaseImportRewrite):
        rewrites = [('a.b.c', 'foo.bar.baz')]

    import_ = ast.Import(names=[
        ast.alias(name='a.b.c',
                  asname='abc')])

    rewrote = Class.visit_Import(import_)

    assert rewrote.body[0].body[0].names[0].name == 'foo.bar.baz'
    assert rewrote.body[0].body[0].names[0].asname == 'abc'



# Generated at 2022-06-14 01:45:26.282799
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import typed_astunparse
    from typed_ast.ast3 import parse
    from textwrap import dedent

    class TestBaseImportRewrite(unittest.TestCase):
        def setUp(self):
            class Transformer(BaseImportRewrite):
                rewrites = [('django.utils.http', 'http')]
                dependencies = []
            self.transformer = Transformer
            self.maxDiff = None

        def test_simple_import(self):
            source = dedent('''
            import django.utils.http
            ''')
            result = dedent('''
            try:
              extend(django.utils.http)
            except ImportError:
              extend(http)
            ''')
            tree = parse(source)
            self.transformer.transform

# Generated at 2022-06-14 01:45:36.297216
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    visitor = BaseImportRewrite(None)
    visitor.rewrites = [('django.db', 'sadiki.core.utils.mydjango')]

    visitor.visit(ast.parse('import django.db'))

    assert visitor._tree_changed == True
    assert visitor._tree

    visitor.visit(ast.parse('from django.db import models'))

    assert visitor._tree_changed == True
    assert visitor._tree

    visitor.visit(ast.parse('from django.db.some_module import some, *'))

    assert visitor._tree_changed == True
    assert visitor._tree

    visitor.visit(ast.parse('from datetime import date'))

    assert visitor._tree_changed == False
    assert visitor._tree == None


# Generated at 2022-06-14 01:45:44.844104
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.test_node import test_node
    from .imports import RewriteImports

    class RewriteImportsTest(RewriteImports):
        rewrites = [('somedummy', 'dummy')]

    tree = ast.parse('import somedummy')
    assert test_node(tree, RewriteImportsTest)

    tree = ast.parse('import somedummy.somedummy2')
    assert test_node(tree, RewriteImportsTest)

    tree = ast.parse('import somedummy as sd')
    assert test_node(tree, RewriteImportsTest)



# Generated at 2022-06-14 01:45:59.781248
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("""
from datetime import date, timedelta
from urllib.request import urlopen
""")
    result = BaseImportRewrite(tree).visit(tree)
    assert ast.dump(result) == ast.dump(ast.parse("""
try:
    from datetime import date, timedelta
except ImportError:
    from datetime import date, timedelta

try:
    from urllib.request import urlopen
except ImportError:
    from urllib.request import urlopen
"""))



# Generated at 2022-06-14 01:46:02.771475
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('b', 'c')]

    tree = ast.parse('from b import a, b, c')
    expected_tree = ast.parse('try: from c import a, b, c\nexcept ImportError: from b import a, b, c')

    assert ImportRewrite.transform(tree).tree == expected_tree

# Generated at 2022-06-14 01:46:12.872429
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    import_from_with_module_to_replace = ast.parse('import foo.bar')
    import_from_with_name_to_replace = ast.parse('from foo import bar')

    assert (ast.dump(TestBaseImportRewrite.transform(import_from_with_module_to_replace).tree) ==
            ast.dump(ast.parse('try:\n    import foo.bar\nexcept ImportError:\n    import bar.bar')))


# Generated at 2022-06-14 01:46:23.018343
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typed_ast.ast3 as ast
    from ..backports import typing as typing_backports
    from ..compat import itervalues

    node = ast.Import(names=[
        ast.alias(name='typing',
                  asname=None)])

    import_statement = ast.Import(names=[
        ast.alias(name='typing_backports',
                  asname=None)])

    tree = ast.Module(body=[
        node,
    ])

    class TestTransformer(BaseImportRewrite):
        rewrites = [('typing', 'typing_backports')]

    transformed = TestTransformer.transform(tree)

    try_stmt = transformed.tree.body[0]
    assert isinstance(try_stmt, ast.Try)

# Generated at 2022-06-14 01:46:30.552588
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..example_files import BaseImportRewrite as BaseImportRewriteModule
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('unittest', 'test'),
        ]
    tree = ast.parse('from unittest import TestCase')
    tr = TestTransformer(tree)
    result = tr.visit(tree)
    assert type(result) == ast.Try
    assert tr._tree_changed
    assert BaseImportRewriteModule.import_rewrite in tr.dependencies


# Generated at 2022-06-14 01:46:44.959419
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import SourceWithMarker, assert_source
    from .. import target
    from ..visitors.constants import name as constants_name

    source = SourceWithMarker("""
    import module
    import another_module
    from module.submodule import SomeClass, SomeOtherClass
    from module.submodule import *
    from .. import unused_module
    from unused_module import unused_class
    """)
    tree = ast.parse(source)

    class TestImportRewrite(BaseImportRewrite):
        target = target.Python27
        rewrites = [('module', 'new_module')]

    transformed = TestImportRewrite.transform(tree)

# Generated at 2022-06-14 01:46:50.494025
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    result = BaseImportRewrite.transform(ast.parse('import foo'))
    assert_equal(ast.dump(result.tree), 'Import(names=[alias(name="foo", asname=None)])\n')

    result = BaseImportRewrite.transform(ast.parse('import foo as bar'))
    assert_equal(ast.dump(result.tree), 'Import(names=[alias(name="foo", asname="bar")])\n')


# Generated at 2022-06-14 01:46:57.799615
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    module = ast.parse('from typing import List, Tuple\n')
    transformer = BaseImportRewrite(module)
    transformer.visit(module)
    print(ast.dump(module))
    module = ast.parse('from ._typing import List, Tuple\n')
    transformer = BaseImportRewrite(module)
    transformer.visit(module)
    print(ast.dump(module))


# Generated at 2022-06-14 01:47:09.388297
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astunparse

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('defusedxml.ElementTree', 'xml.etree.ElementTree')]

    class TestImport(unittest.TestCase):
        def test_Import(self):
            input_code = """
            import defusedxml.ElementTree
            """
            result = TestBaseImportRewrite.transform(ast.parse(input_code))
            output_code = astunparse.unparse(result.tree).strip()

            expected = """
            try:
                extend(import defusedxml.ElementTree)
            except ImportError:
                extend(import xml.etree.ElementTree)
            """
            self.assertEqual(expected.strip(), output_code)


# Generated at 2022-06-14 01:47:18.550019
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astunparse import unparse
    import ast
    import base64
    import importlib
    import sys
    from io import BytesIO
    _m_sys = sys.modules[__name__]

    # 0
    class TestCase(unittest.TestCase):
        def test(self):
            self.assertTrue(True)

    # 1
    def test():
        # 2
        class A:
            pass
        # 3
        class B(A):
            pass

    # 4
    def main():
        # 5
        class A:
            pass
        # 6
        class B(A):
            pass

        # 7
        test()

    # 8
    class Test(unittest.TestCase):
        def test(self):
            # 9
            class A:
                pass
            # 10

# Generated at 2022-06-14 01:47:32.478574
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import astor
    import unittest
    from typed_ast import ast3 as typed_ast

    class TestTransformer(BaseImportRewrite):
        target = '3.6'
        rewrites = [
            ('os', 'cgi'),
            ('os.path', 'http.client'),
            ('shutil', 'fileinput'),
        ]

    class TestImportFrom(unittest.TestCase):
        def _test_rewrite(self, module_name, alias, expected_module, expected_asname):
            node = typed_ast.parse(
                'from {module_name} import {alias}'.format(module_name=module_name, alias=alias))
            result = TestTransformer.transform(node)

# Generated at 2022-06-14 01:47:38.062809
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    module = ast.parse(
        "import foo\n"
        "import bar"
    )

    expected = ast.parse(
        "try:\n"
        "    import foo\n"
        "except ImportError:\n"
        "    import bar"
    )

    class ImportTestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    source = ImportTestTransformer.transform(module)
    assert source.tree == expected

# Generated at 2022-06-14 01:47:45.371816
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor  # noqa

    code = 'import copy'
    expected = 'try:\n    import copy\nexcept ImportError:\n    import copy_backport'

    class CopyTransformer(BaseImportRewrite):
        target = CompilationTarget.PY2
        rewrites = [('copy', 'copy_backport')]

    tree = ast.parse(code)
    CopyTransformer.transform(tree)
    result = astor.to_source(tree)
    assert result == expected



# Generated at 2022-06-14 01:47:55.329526
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import astunparse
    import_stmts = [
        'import some',
        'import some.other',
        'import some.other.module',
        'import some as some_with_other_name',
        'import some.other as some_other_with_other_name',
        'import some.other.module as some_module_with_other_name',
    ]
    for import_stmt in import_stmts:
        parsed = ast.parse(import_stmt)

        class Rewrite(BaseImportRewrite):
            rewrites = [('some', 'new')]

        assert not Rewrite.transform(parsed).is_changed
        assert astunparse.unparse(parsed) == import_stmts[0]


# Generated at 2022-06-14 01:48:05.925910
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TransformerSubclass(BaseImportRewrite):
        rewrites = [('import_module.submodule', 'another_module.submodule')]

    tree = ast.parse("import import_module.submodule as module")
    result = TransformerSubclass.transform(tree)
    assert result.tree.body[0].body[0].value.names[0].name == 'another_module.submodule'
    assert result.tree.body[0].body[0].value.names[0].asname == 'module'
    assert len(result.tree.body[0].body[0].handlers[0].body) == 1
    assert result.tree.body[0].body[0].handlers[0].body[0].value.names[0].name == 'import_module.submodule'
    assert result.tree.body

# Generated at 2022-06-14 01:48:14.802434
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astng  # type: ignore

    class DummyTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('baz', 'qux'),
        ]

    tree = astng.extract_node('''
    import foo
    import foo.bar
    import baz.bar
    import foo.bar.baz
    ''')


# Generated at 2022-06-14 01:48:26.037179
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.ast import parse_ast


# Generated at 2022-06-14 01:48:36.742500
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # global fixture
    import_rewrite = ImportRewrite([('a', 'b')])

    # test 1
    import ast
    import sys
    import_node = ast.parse('import a').body[0]
    node_rewrited = import_rewrite.visit(import_node)
    try:
        extend(import_node)
    except ImportError:
        extend(ast.Import(names=[ast.alias(name='b', asname='a')]))
    assert sys.modules.keys() == {'a'}

    # test 2
    import a
    assert sys.modules.keys() == {'a'}

    # test 3
    import ast
    import sys
    import_node = ast.parse('import c').body[0]
    node_rewrited = import_rewrite.visit

# Generated at 2022-06-14 01:48:41.963700
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .. import ast3 as ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('email', 'email3')]

    tree = ast.parse("""from email import parser
from a.b import c, d as e
import email""")
    TestImportRewrite.transform(tree) # should not raise exception



# Generated at 2022-06-14 01:48:48.577762
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import compile_snippet
    from ..transformer.base import BaseImportRewrite

    # pylint: disable=abstract-method
    class ImportRewriteTest(BaseImportRewrite):
        rewrites = [('typing', '_typing')]

    source = 'import typing'

    actual = compile_snippet(source, target=ImportRewriteTest.target, transformers=[ImportRewriteTest])
    expected = compile_snippet('import _typing', target=ImportRewriteTest.target)

    assert actual == expected

# Generated at 2022-06-14 01:49:05.805265
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    class DummyImportRewrite(BaseImportRewrite):
        rewrites = []  # type: List[Tuple[str, str]]

    from_ = 'tensorflow'
    to = 'tensorflow.python'

    # Not matched rewrite
    node_not_matched = ast.ImportFrom(
        module='numpy',
        names=[
            ast.alias(name='add',
                      asname='add'),
            ast.alias(name='sub',
                      asname='sub')])

    dummy = DummyImportRewrite(None)
    assert dummy.visit_ImportFrom(node_not_matched) == node_not_matched

    # Matched rewrite, import from module

# Generated at 2022-06-14 01:49:17.304474
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    class ImportRewriteTester(BaseImportRewrite):
        rewrites = [("abc.abc", "new_abc.abc")]

    # test module level import
    test_module = ast.parse("""
    import abc.abc

    def test():
        abc.abc.test()
    """)

    ImportRewriteTester.transform(test_module)
    assert len(test_module.body) == 2
    assert isinstance(test_module.body[0], ast.Try)
    assert test_module.body[0].body[0].names[0].name == "abc.abc"
    assert test_module.body[0].body[1].names[0].name == "new_abc.abc"

# Generated at 2022-06-14 01:49:26.718056
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse

    import_node = ast.parse('''from module import test1, test2''')
    node = BaseImportRewrite()
    result = node.visit_ImportFrom(import_node.body[0])
    assert astunparse.unparse(result) == """try:
    from module import test1, test2
except ImportError:
    from module import test1, test2
"""

    import_node = ast.parse('''from module.test1 import test2''')
    result = node.visit_ImportFrom(import_node.body[0])
    assert astunparse.unparse(result) == """from module.test1 import test2"""


# Generated at 2022-06-14 01:49:36.554912
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import re
    import random
    from random import randint
    from re import split
    with BaseImportRewrite(rewrites=[('re', 'typed_ast.simple_ast')]):
        tree = ast.parse('''
            import re
            split('.', 'a.b.c', 1)
        ''')
        result = tree.body[0]
        assert isinstance(result, ast.Expr)
        assert isinstance(result.value, ast.Call)
        assert isinstance(result.value.func, ast.Name)
        assert result.value.func.id == 'split'


# Generated at 2022-06-14 01:49:46.705989
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    import typing

    import_ = ast.Import(names=[
        ast.alias(name='collections',
                  asname='collections')
    ])

    import_rewrite = BaseImportRewrite([])
    import_rewrite.rewrites = [('collections', 'typing')]
    import_rewrite.visit_Import(import_)

    assert isinstance(import_, ast.Try)
    assert import_.body[0].body[0].names[0].name == 'collections'
    assert import_.body[0].body[0].names[0].asname == 'collections'
    assert import_.body[1].body[0].names[0].name == 'typing'

# Generated at 2022-06-14 01:49:57.245574
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import typing
    import_typing_node = ast.parse('import typing').body[0]
    rewrote_node = BaseImportRewrite(ast.parse('')).visit(import_typing_node)
    assert rewrote_node == import_typing_node

    import six.moves
    import_six_moves_node = ast.parse('import six.moves').body[0]
    rewrote_node = BaseImportRewrite(ast.parse('')).visit(import_six_moves_node)
    assert rewrote_node == import_six_moves_node

    from six.moves import range
    import_six_moves_range_node = ast.parse('from six.moves import range').body[0]

# Generated at 2022-06-14 01:50:02.313522
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..imports import import_from_import_statement
    from ..utils import reset_imports

    code = "from six.moves import zip"
    tree = ast.parse(code)

    assert import_from_import_statement(tree, "six.moves.zip")

    reset_imports()
    tree = ast.parse(code)

    assert import_from_import_statement(tree, "six.moves.zip")



# Generated at 2022-06-14 01:50:10.154696
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    '''Matched import from is replaced with try/except block.

    '''
    import ast
    import sys
    import six
    from broadway.transformers.base import BaseImportRewrite
    class Test(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')]
    module = ast.parse('from six.moves.urllib.parse import quote')
    Test.transform(module)
    assert module.body[0].body[0].finalbody[0].body[0].value.s == (
        'six.urllib.parse.quote(123)')


# Generated at 2022-06-14 01:50:16.796490
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('six', 'builtins')]

    tree = ast.parse(
        'import six\n')

    result = Test.transform(tree)
    assert len(result.new.body) == 2
    assert isinstance(result.new.body[0], ast.Try)
    assert isinstance(result.new.body[0].body[0], ast.Import)
    assert result.new.body[0].body[0].names[0].name == 'builtins'



# Generated at 2022-06-14 01:50:26.281110
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.testing_utils import assert_ast, assert_changes

    code = """
    import foo
    import foo.bar

    from foo import bar
    from foo import bar as baz
    from foo import *

    from foo import bar, baz

    from foo.bar import baz
    from foo.bar.baz import qux
    """

# Generated at 2022-06-14 01:50:54.469395
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [('six.moves', 'past.moves')]

    imp = ast.parse("import six").body[0]
    node = Transformer.transform(imp).tree
    assert str(node).strip() == "try:\n import six\nexcept ImportError:\n import past.moves as six"

    imp = ast.parse("import six.moves").body[0]
    node = Transformer.transform(imp).tree
    assert str(node).strip() == "try:\n import six.moves\nexcept ImportError:\n import past.moves"

    imp = ast.parse("import six.moves as sm").body[0]
    node = Transformer.transform(imp).tree

# Generated at 2022-06-14 01:51:05.786650
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Rewriter(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    source = "import foo\nfoo.bar"
    import_node = ast.parse(source).body[0]
    rewriter = Rewriter(import_node)
    result = rewriter.visit_Import(import_node)
    assert isinstance(result, ast.Try)
    assert result.body[0].body[0].names[0].name == 'bar'

    source = "import foo.bar\nfoo.bar"
    import_node = ast.parse(source).body[0]
    rewriter = Rewriter(import_node)
    result = rewriter.visit_Import(import_node)
    assert isinstance(result, ast.Try)

# Generated at 2022-06-14 01:51:12.788964
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astroid
    import astroid.exceptions
    class TestClass(BaseImportRewrite):
        rewrites = [
            ('astroid.exceptions', 'astroid.nodes')
        ]

    code = '''
import astroid.exceptions
'''
    tree = ast.parse(code)
    result = TestClass.transform(tree)

    expected = '''
try:
    import astroid.exceptions
except ImportError:
    import astroid.nodes
'''

    assert ast.dump(tree) == ast.dump(ast.parse(expected))



# Generated at 2022-06-14 01:51:19.932705
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    import os
    import tempfile
    import sys

    # sys.path
    sys_path = sys.path

    # Create temp folder for tests.
    import_path = os.path.join(tempfile.mkdtemp(), 'import_folder')
    os.mkdir(import_path)


# Generated at 2022-06-14 01:51:27.653504
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast_helpers
    # example.moduleX -> example.moduleY
    # example.moduleX.submoduleA -> example.moduleY.submoduleA
    # example.moduleX.submoduleA.ClassA -> example.moduleY.submoduleA.ClassA
    # example.moduleX.submoduleA.ClassA.CONSTANT_A -> example.moduleY.submoduleA.ClassA.CONSTANT_A

    # example.moduleX.submoduleA.subsubmoduleA
    # example.moduleX.submoduleA.subsubmoduleA.subsubsubmoduleA
    # example.moduleX.submoduleA.subsubmoduleA.subsubsubmoduleA.subsubsubsubmoduleA
    # example.moduleX.submoduleA.subsubmoduleA.subsubsubmoduleA.subsubsubsubmoduleA.

# Generated at 2022-06-14 01:51:33.306335
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('http.server', 'http.server2')]

    tree = ast.parse('from http.server import HTTPServer')
    tree = ImportRewrite.transform(tree).tree
    assert ast.dump(tree) == '''\
try:
    from http.server import HTTPServer
except ImportError:
    from http.server2 import HTTPServer'''



# Generated at 2022-06-14 01:51:40.752193
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    test_tree = ast.parse("""
import six
from ast import AST
""")

    def test_transform(tree):
        return BaseImportRewrite(tree).visit(tree)

    new_tree = test_transform(test_tree)
    assert isinstance(new_tree.body[0], ast.Try)
    assert isinstance(new_tree.body[1], ast.ImportFrom)



# Generated at 2022-06-14 01:51:49.426790
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse

    class TestTransformer(BaseImportRewrite):
        rewrites = [('a', 'b')]

    source = '''import a'''

    tree = ast.parse(source)
    tree = TestTransformer.transform(tree).tree
    result = astunparse.unparse(tree)

    expected = '''try:
    import a
except ImportError:
    import b'''

    assert(result == expected)



# Generated at 2022-06-14 01:51:55.719314
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typed_ast.ast3 as ast
    from ..base_transformer import BaseImportRewrite
    class Test(BaseImportRewrite):
        rewrites = [('a.b', 'c.d')]

    ast.dump(
        Test.transform(ast.parse('from a import bar as bar\n'
                                 'from a import *\n'
                                 'from a.b import foobar as foobar\n'))[0],
        include_attributes=True)

# Generated at 2022-06-14 01:52:06.187514
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    from typed_ast import ast3 as ast
    from ..utils.text import get_text_from_source
    import typed_astunparse

    class Transformer(BaseImportRewrite):
        rewrites = [('collections', 'collections.abc'),
                    ('collections.abc', 'collections_abc')]

    source = """
        import collections
        import collections.abc"""
    expected = """
        try:
            import collections
        except ImportError:
            import collections.abc as collections
        try:
            import collections.abc
        except ImportError:
            import collections_abc as collections.abc"""

    tree = ast.parse(source)
    files, changed = Transformer.transform(tree).result
    assert changed
    assert get_text_from_source(expected) == typed_astunparse

# Generated at 2022-06-14 01:52:58.590477
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import pyspark
    import pytest
    from testfixtures import compare

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('pyspark', 'pyspark_ng')]

    tree = ast.parse(
        "import pyspark.sql")
    expected_tree = ast.parse(
        "try:\n"
        "    import pyspark.sql\n"
        "except ImportError:\n"
        "    import pyspark_ng.sql")
    expected_tree_changed = True
    expected_dependencies = []

    result = TestImportRewrite.transform(tree)

    compare(result,
            transformation_result(transformation_result=expected_tree,
                                  tree_changed=expected_tree_changed,
                                  dependencies=expected_dependencies))


# Unit

# Generated at 2022-06-14 01:53:10.459161
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrites = [('base', 'rewritten')]
    class ImportRewrite(BaseImportRewrite):
        rewrites = rewrites

    import_from = ast.parse('''
        from base import *
        from base import a as b
        from base.a import c as d
    ''').body

# Generated at 2022-06-14 01:53:18.175937
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ExampleImportRewrite(BaseImportRewrite):
        target = 'python'
        rewrites = [('bob', 'bob.bob')]

    import ast
    import bob

    module = ast.parse('import bob')
    res = ExampleImportRewrite.transform(module)

    assert isinstance(res.transformed, ast.Try)
    assert isinstance(res.transformed.body[0], ast.Import)
    assert res.transformed.body[0].names[0].name == 'bob.bob'
    assert res.changed


# Generated at 2022-06-14 01:53:24.679969
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from .test_utils import assert_equal_ast_structure
    from ..transforms import BaseImportRewrite

    class Test(BaseImportRewrite):
        target = 'test'
        rewrites = [
            ('foo', 'bar'),
        ]

    # Test 'foo' import with asname
    tree = ast3.parse('import foo as fuu')
    Test.transform(tree)
    assert_equal_ast_structure(
        tree, ast3.parse("try:\n    import foo as fuu\nexcept ImportError:\n    import bar as fuu"))

    # Test 'foo.bar' import with asname
    tree = ast3.parse('import foo.bar as fuu')
    Test.transform(tree)

# Generated at 2022-06-14 01:53:36.915917
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import transform

    tree = ast.parse('''from foo import bar as bleh
from foo.bar import bleh as bloh
from foo.bar import *
from foo.bar.bleh import *
from foo.bar.bleh import bleh as blee
from bar import bar''')

    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]


# Generated at 2022-06-14 01:53:47.499799
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import textwrap
    import astor
    from astor.code_gen import to_source

    tree = astor.parse_file('test/import_rewrite.py')
    BaseImportRewrite.rewrites = [('urllib.request', 'urllib.request.urlopen')]
    BaseImportRewrite.visit(tree)
    result = to_source(tree.body[0]).rstrip()
    expect_result = textwrap.dedent("""
    import_rewrite(
        _previous_module=__import__("urllib.request", fromlist=("Request", "urlopen", "urlretrieve")),
        _current_module=__import__("urllib.request.urlopen", fromlist=("Request", "urlopen", "urlretrieve")),
    )""")
    assert result

# Generated at 2022-06-14 01:53:52.959263
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """Rewrite unittest"""
    import astor

    source = """from os import path, name"""
    tree = astor.parse_file(source)
    transformer = BaseImportRewrite(tree)
    result = astor.dump_tree(transformer.visit(tree))
    expected = """try:
    from os import path, name
except ImportError:
    from os import path, name

"""
    assert result == expected

