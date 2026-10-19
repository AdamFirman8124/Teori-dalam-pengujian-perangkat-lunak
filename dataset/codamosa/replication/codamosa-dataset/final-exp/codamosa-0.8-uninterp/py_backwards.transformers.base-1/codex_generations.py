

# Generated at 2022-06-14 01:44:18.114701
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import unittest
    import tempfile
    import os

    class TestBaseImportRewrite(BaseImportRewrite):
        target = 'test'
        rewrites = [('collections', 'collections.abc')]


# Generated at 2022-06-14 01:44:27.240765
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astor

    class Transformer(BaseImportRewrite):
        rewrites = [
            ('collections', 'collections.abc')
        ]

    class Tests(unittest.TestCase):
        def test_simple(self):
            code = 'import collections'
            expected_code = 'try:\n    import collections\nexcept ImportError:\n    import collections.abc'

            tree = ast.parse(code)
            Transformer.transform(tree)

            self.assertEqual(astor.to_source(tree), expected_code)

    unittest.main()


if __name__ == '__main__':
    test_BaseImportRewrite_visit_Import()

# Generated at 2022-06-14 01:44:37.416432
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3

    import astor

    BaseImportRewrite.rewrites = [('collections', 'typing'),
                                  ('abc', 'typing')]
    tree = astor.parse('''
import abc
import collections
import os
import sys
''')
    result = BaseImportRewrite.transform(tree)
    assert type(result.tree.body[0]) == ast3.Try
    assert type(result.tree.body[1]) == ast3.Try
    assert type(result.tree.body[2]) == ast3.Import
    assert type(result.tree.body[3]) == ast3.Import


# Generated at 2022-06-14 01:44:47.446753
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import tempfile
    import sys
    import os

    import astor

    def _get_module(name: str, module: str) -> None:
        with tempfile.TemporaryDirectory() as dir_:
            sys.path.append(dir_)
            path = os.path.join(dir_, name + '.py')

            with open(path, 'w') as f:
                f.write('from {} import *\n'.format(module))

            importlib.invalidate_caches()
            yield importlib.import_module(name)

    def _check_module(name: str, module: str, before: List[str],
                      after: List[str], imports: List[ast.Import]) -> None:
        for mod in _get_module(name, module):
            assert sorted(dir(mod)) == sorted

# Generated at 2022-06-14 01:45:02.617278
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [(('__future__', 'future'), ('futures', 'future'))]

    class TestImportRewrite1(BaseImportRewrite):
        rewrites = [(('__future__', 'future'), ('future', 'future'))]

    class TestImportRewrite2(BaseImportRewrite):
        rewrites = [(('six', 'sixtools'), ('futures', 'future'))]

    class TestImportRewrite3(BaseImportRewrite):
        rewrites = [(('six', 'sixtools'), ('future', 'future'))]

    class TestImportRewrite4(BaseImportRewrite):
        rewrites = [(('six', 'sixtools'), ('futures', 'futures'))]


# Generated at 2022-06-14 01:45:11.332354
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from ..transformer import BaseImportRewrite

    class DummyTransformer(BaseImportRewrite):
        target = 'python35'
        rewrites = [('urllib.request', 'urllib.request')]

    tree = ast3.parse('import urllib.request')
    DummyTransformer.transform(tree)
    assert ast3.dump(tree) == 'try:\n    extend(urllib.request)\nexcept ImportError:\n    extend(urllib.request)\n'



# Generated at 2022-06-14 01:45:22.264295
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    from_, to = '_foo', 'foo'

    import_names = [
        ast.alias(name=from_ + '.bar',
                  asname='baz'),
        ast.alias(name=from_,
                  asname=from_)]

    import_node = ast.Import(names=import_names)


# Generated at 2022-06-14 01:45:23.588345
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Tests the Visit_ImportFrom method of BaseImportRewrite class
    pass


# Generated at 2022-06-14 01:45:32.534440
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Arrange
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('django.contrib.auth', 'django.contrib.auth.models')]

    source = '''\
import django.contrib.auth
'''
    tree = ast.parse(source)
    expected = '''\
try:
    import django.contrib.auth
except ImportError:
    import django.contrib.auth.models as django.contrib.auth
'''

    # Act
    result = ImportRewrite.transform(tree)

    # Assert
    assert result.changed
    assert result.dependencies == []
    assert ast.dump(tree) == expected


# Generated at 2022-06-14 01:45:39.506524
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    module = ast.parse("""
import collections
""")
    tr = BaseImportRewrite(module)
    tr.visit(module)
    assert "collections" in [_.name for _ in module.body]



# Generated at 2022-06-14 01:46:00.210806
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import astunparse
    import textwrap

    class Test(BaseImportRewrite):
        rewrites = [
            ('os', 'six.moves.os'),
        ]

    @snippet
    def previous(module, name, asname):
        import module.name

        import module.name as asname

    @snippet
    def current(module, name, asname):
        try:
            import module.name
        except ImportError:
            import six.moves.module.name

        try:
            import module.name as asname
        except ImportError:
            import six.moves.module.name as asname

    for node in previous.get_body():
        for _, m in Test.transform(node):
            print(astunparse.unparse(m))
            print()


# Generated at 2022-06-14 01:46:10.747463
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astunparse import unparse
    from typed_ast.ast3 import parse
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
    tree = parse('from foo.bar import x')
    tree2 = parse('from bar.bar import x')
    tree3 = parse('from bar import *')
    tree4 = parse('from foo import *')
    tree = ImportRewrite.transform(tree)
    tree2 = ImportRewrite.transform(tree2)
    tree3 = ImportRewrite.transform(tree3)
    tree4 = ImportRewrite.transform(tree4)
    assert unparse(tree.tree) == 'from bar.bar import x'
    assert unparse(tree2.tree) == 'from bar.bar import x'

# Generated at 2022-06-14 01:46:20.710564
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.visitor_test_helper import VisitorTestHelper
    from . import six
    visitor_test_helper = VisitorTestHelper()

    def _helper(node_str, expected_str):
        node = visitor_test_helper.parse(node_str)
        BaseImportRewrite.rewrites = [('six.moves', 'six')]
        visitor = BaseImportRewrite()
        result = visitor.visit(node)
        assert visitor_test_helper.dump(result) == expected_str

    # no change
    _helper('import os', 'import os')
    _helper('import os.path', 'import os.path')
    _helper('import six', 'import six')

    # no change

# Generated at 2022-06-14 01:46:30.214777
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    imp = ast.ImportFrom(module='foo',
                         names=[ast.alias(name='bar',
                                          asname='bar1')],
                         level=0)
    module = ast.Module(body=[imp])

    rewriter = BaseImportRewrite([('foo', 'oost', 'oost')])
    res = rewriter.visit_ImportFrom(imp)
    assert res.body[0].type == 'Try'
    assert res.body[0].body == imp
    assert res.body[0].finalbody[0].value.type == 'ImportFrom'
    assert res.body[0].finalbody[0].value.module == 'oost'

# Generated at 2022-06-14 01:46:43.711083
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import importlib
    import inspect

    import pytest

    from typed_ast.ast3 import Module, Import, alias

    from ..utils import snippet
    from . import BaseImportRewrite

    @snippet
    def code():
        import foo  # nosec
        import bar

    @snippet
    def expected_code():
        try:
            import foo  # nosec
        except ImportError:
            import bar

    def test_transform_code():
        class Test(BaseImportRewrite):
            rewrites = [('foo', 'bar')]

        module = Module(body=[Import(names=[alias(name='foo', asname=None)])])
        transformer = Test(module)
        transformer.visit(module)
        node = module.body[0]
        assert isinstance(node, Try)

       

# Generated at 2022-06-14 01:46:55.268945
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from_ = '__future__'
    to = 'future'
    import_node = """from __future__ import absolute_import"""
    body = """
from __future__ import absolute_import
"""
    import_as_node = """from __future__ import absolute_import as abc"""
    body_as = """
from __future__ import absolute_import as abc
"""
    import_from_as_node = """from future import absolute_import as abc"""
    body_from_as = """
from future import absolute_import as abc
"""
    import_from_node = """from future import absolute_import"""
    body_from = """
from future import absolute_import
"""

# Generated at 2022-06-14 01:47:08.552296
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    def do_test(from_, to, input_, expected):
        class MyBaseImportRewrite(BaseImportRewrite):
            rewrites = [(from_, to)]
    
        result = MyBaseImportRewrite.transform(ast.parse(input_))
        assert result.tree == ast.parse(expected)
        assert result.changed
        assert result.dependencies == ["from __future__ import absolute_import"]
    
    do_test('urllib.request', 'urllib.request.urlopen',
            """
            import urllib.request
            """, """
            try:
                import urllib.request
            except ImportError:
                import urllib.request.urlopen as urllib.request
            """)
    

# Generated at 2022-06-14 01:47:23.870499
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import pytest

    tree = ast.parse(
        import_rewrite.get_snippet(
            previous="""
import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestRegressor
            """.strip(),
            current="""
import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble.tests import RandomForestRegressor
            """.strip()
        )
    )

    class Rewrite(BaseImportRewrite):
        rewrites = [
            ('sklearn.ensemble', 'sklearn.ensemble.tests')
        ]


# Generated at 2022-06-14 01:47:34.505043
# Unit test for method visit_Import of class BaseImportRewrite

# Generated at 2022-06-14 01:47:45.175166
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Test for a normal import
    import_from = ast.parse('''from foo import bar, baz''').body[0]
    tr = BaseImportRewrite(import_from)
    tr.visit_ImportFrom(import_from)
    assert import_from == ast.parse('''from foo import bar, baz''').body[0]

    # Test for a import with import rewrite
    import_from = ast.parse('''from foo import bar, baz''').body[0]
    tr = BaseImportRewrite(import_from)
    tr.rewrites = [('foo', 'firinga')]
    tr.visit_ImportFrom(import_from)
    assert import_from == ast.parse('''from firinga import bar, baz''').body[0]

    # Test for a import with

# Generated at 2022-06-14 01:47:54.658846
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # arrange
    tree = ast.parse('import blah')
    rewrites = [('blah', 'foo')]
    visitor = BaseImportRewrite(tree, rewrites)
    # act
    visitor.visit(tree)
    # assert
    assert ast.dump(tree) == """try:
    import blah
except ImportError:
    import foo
"""


# Generated at 2022-06-14 01:48:01.393775
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class MyImportRewrite(BaseImportRewrite):
        rewrites = [
            ('sqlalchemy', 'sqlalchemy.ext.declarative')
        ]

    tree = ast.parse('from sqlalchemy import Column, Table')
    result = ast.parse('try:\n'
                       '    from sqlalchemy import Column, Table\n'
                       'except ImportError:\n'
                       '    from sqlalchemy.ext.declarative import Column, Table')
    assert MyImportRewrite.transform(tree).tree == result.body[0]

    tree = ast.parse('from sqlalchemy.ext.declarative import Column, Table')

# Generated at 2022-06-14 01:48:08.942654
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from io import StringIO
    import ast
    import textwrap
    from .transform import BaseImportRewrite

    transformer = BaseImportRewrite()

    input = textwrap.dedent("""
    from unicodedata import normalize

    normalize(u"hello")
    """)

    tree = ast.parse(input)
    tree = transformer.visit(tree)

    BaseImportRewrite.rewrites = [('unicodedata', 'unicodedata2')]

    input = textwrap.dedent("""
    from unicodedata import normalize

    normalize(u"hello")
    """)

    tree = ast.parse(input)
    tree = transformer.visit(tree)

# Generated at 2022-06-14 01:48:14.463249
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..test_utils import build_test_tree

    class FakeTransform(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = build_test_tree("""
    import foo
    """)

    FakeTransform.transform(tree)

    assert tree.body[0] == ast.Try(
        body=[ast.Import(names=[ast.alias(name='foo', asname=None)])],
        handlers=[ast.ExceptHandler(
            type=ast.Name(id='ImportError', ctx=ast.Load()),
            name=None,
            body=[ast.Import(names=[ast.alias(name='bar', asname=None)])])],
        orelse=[],
        finalbody=[])



# Generated at 2022-06-14 01:48:25.570210
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse
    import ast
    import copy

    class A(BaseImportRewrite):
        rewrites = [
            ('six', 'six.moves')]

    test_input = ast.Import(names=[
        ast.alias(name='six.moves', asname='m')])
    test_transform = ast.Try(body=[
        ast.Import(names=[
            ast.alias(name='six.moves', asname='m')])
    ], handlers=[
        ast.ExceptHandler(type=None, name=None, body=[
            ast.Import(names=[
                ast.alias(name='six', asname='m')]),
        ])
    ], orelse=[], finalbody=[])

    assert test_transform == A.transform(test_input).tree



# Generated at 2022-06-14 01:48:34.150516
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from . import import_rewrite

    import_rewrite.from_to_rewrites = [(from_, to) for from_, to in BaseImportRewrite.rewrites]

    tree = ast.parse('import argparse')

    class TestTransformer(BaseImportRewrite):
        rewrites = [('argparse', 'argparse2')]
    
    result = TestTransformer.transform(tree)

    assert result.tree == ast.parse('''
try:
    import argparse
except ImportError:
    import argparse2 as argparse''')



# Generated at 2022-06-14 01:48:45.160742
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('six', 'future.six')]

    tree = ast.parse(textwrap.dedent("""\
    import future.six
    from future.six import PY3"""))
    result = TestImportRewrite.transform(tree)
    assert result.changed
    assert result.modules == ['future.six']

    expected = ast.parse(textwrap.dedent("""\
    try:
        import future.six
    except ImportError:
        import six as future_six

    try:
        from future.six import PY3
    except ImportError:
        from six import PY3 as PY3
    """))

# Generated at 2022-06-14 01:48:55.538922
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from appyratus.test import BaseTestCase, mark, skip_unless


# Generated at 2022-06-14 01:49:00.568891
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    t = ast.parse('from foo import bar')
    tr = BaseImportRewrite(t)
    tr.rewrites = [('foo', 'bar')]
    tr.visit(t)
    assert(astor.to_source(t).strip() == 'try:\n    from foo import bar\nexcept ImportError:\n    from bar import bar')

# Generated at 2022-06-14 01:49:08.530475
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    node = ast.Import(names=[ast.alias(name='re', asname='re')])
    BaseImportRewrite._replace_import = BaseImportRewrite._replace_import.__func__ # adding test
    import_rewrite.get_body = import_rewrite.get_body.__func__ # adding test
    rewrite = BaseImportRewrite(None)
    assert rewrite.visit_Import(node).body[0].body[1].value.func.id == 'extend'


# Generated at 2022-06-14 01:49:23.499579
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import pdb
    class MyTransformer(BaseImportRewrite):
        rewrites = [
            ('foo.bar', 'bar.baz')
        ]

        def visit_Import(self, node):
            return super().visit_Import(node)

    tree = ast.parse('from foo import bar')
    t = MyTransformer(tree)
    astor.dump_tree(t.visit(tree)) == '''
try:
    from foo import bar as bar
except ImportError:
    from bar.baz import bar as bar
'''

    tree = ast.parse('import foo as new_foo')
    t = MyTransformer(tree)

# Generated at 2022-06-14 01:49:35.456008
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        target = NotImplemented
        rewrites = [
            ('os', 'path'),
            ('os.path', 'sys.sub')
        ]

    tree = ast.parse('import os\n'
                     'from os import path\n'
                     'from os import environ as env\n'
                     'from os.path import sep\n'
                     'from os.path import join as j\n'
                     'from os.path import split as s')

    transformer = TestTransformer(tree)
    transformer.visit(tree)

    assert transformer._tree_changed is True


# Generated at 2022-06-14 01:49:39.816996
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    tree = astor.parse('import redis')
    class TestTransformer(BaseImportRewrite):
        rewrites = [('redis', 'redis-py')]
    res = TestTransformer.transform(tree)
    assert 'try' in astor.to_source(res.tree)


# Generated at 2022-06-14 01:49:47.611735
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    project = ast.parse('import foo')

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    test_rewrite = TestImportRewrite(project)
    test_rewrite.visit(project)
    assert ast.dump(project) == 'try:\n    import bar\nexcept ImportError:\n    import foo\n'

    project = ast.parse('from foo import foo')
    test_rewrite = TestImportRewrite(project)
    test_rewrite.visit(project)
    assert ast.dump(project) == 'try:\n    from bar import foo\nexcept ImportError:\n    from foo import foo\n'

    project = ast.parse('from foo import foo as bar')

# Generated at 2022-06-14 01:49:56.962111
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..py import py_grammar

    class MockImportRewrite(BaseImportRewrite):
        rewrites = [('collections', 'collections.abc')]

    code = astor.to_source(py_grammar.parse("""
        from collections import a, b as c
    """))

    tree = ast.parse(code)
    tree = MockImportRewrite.transform(tree).tree
    result = astor.to_source(tree)
    expected_code = """    try:
        from collections import a, b as c
    except (ImportError):
        from collections.abc import a, b as c

"""
    assert result == expected_code



# Generated at 2022-06-14 01:50:03.097342
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.ast import parse_source, get_body

    tree = parse_source("""
    import ast, os
    """)

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('ast', 'typed_ast')]

    result = TestBaseImportRewrite.transform(tree)

    expected = """
    try:
        import ast
    except ImportError:
        import typed_ast as ast
    
    import os
    """
    assert get_body(result.tree) == expected



# Generated at 2022-06-14 01:50:11.785788
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.examples import code_to_ast
    from .metrics import TransformationsChecker

    class TestTransformer(BaseImportRewrite):
        rewrites = [('math', 'py.math')]

    tree = code_to_ast("""\
import math

math.pi
""")
    expected_tree = code_to_ast("""\
try:
    import math
except ImportError:
    import py.math as math

math.pi
""")
    checker = TransformationsChecker(tree, expected_tree)

    checker.assert_result(TestTransformer.transform)



# Generated at 2022-06-14 01:50:22.258093
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class SimpleImport(BaseImportRewrite):
        rewrites = [('mymodule', 'mymodule_rewrite')]

    tree = ast.parse("""
import mymodule
import zlib
import mymodule.util
import mymodule.util.http
""")

    SimpleImport.transform(tree)


# Generated at 2022-06-14 01:50:28.674212
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest.mock as mock
    import astor
    import_stmt_str = 'import simplejson'
    import_stmt = ast.parse(import_stmt_str).body[0]

    rewrites = [('simplejson', 'json')]
    transformer = BaseImportRewrite(mock.Mock())
    transformer.rewrites = rewrites

    try_stmt_str = 'try:\n    import simplejson\nexcept ImportError:\n    import json'
    result = transformer.visit_Import(import_stmt)
    assert astor.to_source(result) == try_stmt_str



# Generated at 2022-06-14 01:50:36.561111
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    from ..utils.unparse import Unparser
    from io import StringIO

# Generated at 2022-06-14 01:50:57.618490
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import sys
    sys.path.append('tests')
    from tests.data.my_module import my_func

    rewrites = [('tests.data.my_module.my_func', 'tests.data.other_module.my_func')]
    target = CompilationTarget.PYTHON, (3, 7)

    class MyTransformer(BaseImportRewrite):
        target = target
        rewrites = rewrites

    stmt = 'from tests.data.my_module import my_func'
    tree = astor.parse(stmt)
    result = MyTransformer.transform(tree)
    assert result.changed


# Generated at 2022-06-14 01:51:08.283102
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.test_transformation import get_node

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('typing', 'six')
        ]

    result = TestImportRewrite.transform(get_node('import typing'))
    assert result.tree.body[0] == ast.Try(
        body=[ast.Import(names=[ast.alias(name='six',
                                          asname=None)])],
        handlers=[ast.ExceptHandler(type=ast.Name(
            id='ImportError',
            ctx=ast.Load()), name=None, body=[ast.Import(names=[
                ast.alias(name='typing',
                          asname=None)])])],
        orelse=[],
        finalbody=[])


# Generated at 2022-06-14 01:51:20.660127
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..python import PythonTarget
    from astor import dump
    from ..structures.tree import Module

    class TestBaseImportRewrite(BaseImportRewrite):
        target = CompilationTarget(PythonTarget, '3.5')
        rewrites = [('foo', 'foo_rewrote')]

    node = Module(body=[ast.Import(names=[ast.alias(name='foo',
                                                   asname='bar')])])

# Generated at 2022-06-14 01:51:29.798563
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import ast
    import random
    import test_jupyter_importer
    node = ast.parse("import jupyter_importer")
    visitor_instance = BaseImportRewrite(node)
    new_node = visitor_instance.visit(node)
    assert( astor.to_source(new_node) == 
    """import_rewrite(
    ast.parse("import jupyter_importer"),
    ast.parse("import test_jupyter_importer")
)"""
    )
    assert(visitor_instance._tree_changed == True)


# Generated at 2022-06-14 01:51:39.624569
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('_ssl', 'ssl'),
            ('_io', 'io'),
        ]

    tree = ast.parse("""\
from _ssl import SSLContext, wrap_socket
from _io import FileIO
from _random import Random
""")
    transformer = TestTransformer(tree)
    transformer.visit(tree)
    assert transformer._tree_changed is True
    expected = ast.parse("""\
try:
    from _ssl import SSLContext, wrap_socket
except ImportError:
    from ssl import SSLContext, wrap_socket
try:
    from _io import FileIO
except ImportError:
    from io import FileIO
from _random import Random
""")
    assert ast.dump(tree) == ast.dump(expected)

# Generated at 2022-06-14 01:51:51.691263
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test(BaseImportRewrite):
        rewrites = [('old', 'new')]

    input = 'from old.a import a, b, c'

    expected = '''
try:
    from old.a import a
    from old.a import b
    from old.a import c
except ImportError:
    from new.a import a
    from new.a import b
    from new.a import c
'''

    assert Test.transform(ast.parse(input)).tree_str.strip() == expected.strip()

    input = 'from old import a, b, c'

    expected = '''
try:
    from old import a
    from old import b
    from old import c
except ImportError:
    from new import a
    from new import b
    from new import c
'''

    assert Test

# Generated at 2022-06-14 01:52:02.028206
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Mock(BaseImportRewrite):
        rewrites = [
            ('os.path', 'pathlib'),
            ('email', 'mail')]

    node1 = ast.parse('import os.path')
    node2 = ast.parse('import email.mime.text')
    node3 = ast.parse('import sys')

    # Rewrite
    new_node1 = Mock.transform(node1).tree

    assert isinstance(new_node1.body[0], ast.Try)
    assert isinstance(new_node1.body[0].body[0], ast.Import)
    assert new_node1.body[0].body[0].names[0].name == 'pathlib'

    # Rewrite
    new_node2 = Mock.transform(node2).tree


# Generated at 2022-06-14 01:52:12.641577
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """Test for method visit_ImportFrom of class BaseImportRewrite."""
    from ..compilers import Python36Compiler
    from ..compilers.python import Python36PlatformSpecificModules
    import unittest

    class DummyImportRewriteModule(BaseImportRewrite):
        rewrites = [('module1', 'module2')]

    Python36Compiler.platform_specific_modules = Python36PlatformSpecificModules

    class TestBaseImportRewriteVisitImportFrom(unittest.TestCase):
        def test_import_from_module_rewrite(self):
            import astor

            node = ast.parse('from module1 import fun1').body[0]

            new_node = DummyImportRewriteModule().visit(node)


# Generated at 2022-06-14 01:52:22.715826
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import compile_snippet
    from tstyping import TYPE_CHECKING

    if TYPE_CHECKING:
        original = """
        from django.http import Http404, HttpResponseRedirect
        """
        expected = """
        try:
            from django.http import Http404, HttpResponseRedirect
        except ImportError:
            from django_http import Http404, HttpResponseRedirect
        """
    else:
        original = """
        from django.http import Http404, HttpResponseRedirect
        """
        expected = """
        try:
            from django.http import Http404, HttpResponseRedirect
        except ImportError:
            from django_http import Http404, HttpResponseRedirect
        """


# Generated at 2022-06-14 01:52:28.137937
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.parse('from urlparse import urlparse')
    transformer = BaseImportRewrite(import_from)
    transformer.visit_ImportFrom(import_from.body[0])
    assert transformer._tree_changed == True
    #from typed_ast import ast3 as ast
    #import astor
    #print(ast.dump(import_from))
    #print(astor.to_source(import_from))
    #print(astor.to_source(transformer._tree))


# Generated at 2022-06-14 01:52:43.413974
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    """This test asserts that the method visit_Import of class BaseImportRewrite
    correctly transforms the AST node Import.
    """
    import_node = ast.parse("from math import *").body[0]
    assert isinstance(BaseImportRewrite.transform(import_node).tree, ast.Try)
    assert BaseImportRewrite.transform(import_node).changed

    import_node = ast.parse("import datetime").body[0]
    assert isinstance(BaseImportRewrite.transform(import_node).tree, ast.Import)
    assert not BaseImportRewrite.transform(import_node).changed


# Generated at 2022-06-14 01:52:54.762143
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    eval(
        compile(
            ast.parse(
                'from aiohttp.web import get, Application'),
            filename='<test>',
            mode='exec'))

    node = ast.parse(
        'from aiohttp.web import get, Application')

    for mode in ('aiohttp.web', 'aiohttp', 'a'):
        class Transform(BaseImportRewrite):
            rewrites = [(mode, 'aiotest')]

        transformed = Transform.transform(node)
        assert transformed.tree.body[0].body[0].name == 'aiotest.web'
        assert transformed.tree.body[0].body[1].name == 'aiotest.web'

# Generated at 2022-06-14 01:53:04.891773
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..utils.fixtures import import_from_snippet
    import_from_snippet.add_line('from typing import Dict')
    
    code = import_from_snippet.get_code()
    tree = ast.parse(code)
    BaseImportRewrite.rewrites = [('typing', 'a_very_unlikely_name_that_does_not_exist')]
    BaseImportRewrite.transform(tree)
    

# Generated at 2022-06-14 01:53:15.760220
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from .tests.utils import check_equal_asts
    from . import six
    from .. import py2to3
    from .. import py2to3_fixes
    from .. import rfc3987

    class Transform(BaseImportRewrite):
        rewrites = [('six', 'six')]

    tree = ast3.parse("""
        import six
    """)

    tree_expected = ast3.parse("""
        try:
            import six
        except ImportError:
            import six
    """)

    result = Transform.transform(tree)
    assert check_equal_asts(tree, tree_expected)
    assert result.changed
    assert result.dependencies == ['six']
    assert result.tree is tree  # type: ignore



# Generated at 2022-06-14 01:53:20.577434
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class MockBaseImportRewrite(BaseImportRewrite):
        def _get_matched_rewrite(self, name: Optional[str]) -> Optional[Tuple[str, str]]:
            return 'foo', 'bar'

    tree = ast.parse('import foo')
    MockBaseImportRewrite.transform(tree)

    assert tree.body[0].body[0].type == ast.Import
    assert tree.body[0].body[0].body[0].names[0].name == 'bar'
    assert tree.body[0].body[0].body[0].names[0].asname == 'foo'



# Generated at 2022-06-14 01:53:24.824646
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    module = ast.parse("import mock")
    tr = BaseImportRewrite(module)
    tr.rewrites = [("mock", "unittest.mock")]
    result = tr.visit(module)
    assert isinstance(result, ast.Try)


# Generated at 2022-06-14 01:53:37.076531
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo.bar.baz', 'thud.blat'),
                    ('foo', 'bar')]

    tests = [
        ('import foo', 'import bar'),
        ('import foo.bar.baz', 'import thud.blat'),
        ('import foo.bar', 'import foo.bar'),
        ('import foo as bar', 'import bar as bar'),
        ('import foo.bar.baz as bar', 'import thud.blat as bar'),
        ('import foo', 'try:\n    import bar\nexcept ImportError:\n    import foo')
    ]

    for test, result in tests:
        node = astor.code_to_ast(test)
        transformer = TestTransformer(node)
        transformer.visit

# Generated at 2022-06-14 01:53:46.723184
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Test code
    import unittest
    import typed_astunparse
    from typed_ast.ast3 import parse

    class Test(unittest.TestCase):
        def test(self):
            code = 'from django.db.models import CharField, ForeignKey, OneToOneField'
            expected = '''\
try:
    from django.db.models import CharField, ForeignKey, OneToOneField
except ImportError:
    from django.db.base import CharField, ForeignKey, OneToOneField'''
            tree = parse(code)
            BaseImportRewrite(tree).visit(tree)
            self.assertEqual(typed_astunparse.unparse(tree), expected)

    unittest.main()

# Generated at 2022-06-14 01:53:56.151389
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from . import transformation_test_helper
    from .testtransformer import TestTransformer
    from .testtransformer2 import Test2Transformer
    import pytest
    import os
    import platform

    file_name = os.path.join(os.path.dirname(__file__), 'test_classes', 'test_import_rewrite.py')
    file_name = os.path.abspath(file_name)
    expected_file_name = os.path.join(os.path.dirname(__file__), 'expected_classes', 'test_import_rewrite.py')

    if platform.machine() == 'x86_64':
        expected_file_name += '.64bit'

    expected = open(expected_file_name, 'rb').read()

    test_transformer = Test