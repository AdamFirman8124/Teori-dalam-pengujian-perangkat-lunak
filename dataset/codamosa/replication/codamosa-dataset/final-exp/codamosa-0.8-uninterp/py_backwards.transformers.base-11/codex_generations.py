

# Generated at 2022-06-14 01:44:19.148864
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import six

    class MockClass(BaseImportRewrite):
        rewrites = [('six', 'mock_six')]

    tree = ast.parse('''import six''')
    expected = ast.parse(import_rewrite.get_body(previous='import six',
                                                 current='import mock_six')[0])
    tree2 = MockClass.transform(tree).tree
    assert tree2 == expected
    assert MockClass.dependencies == ['mock_six']

    tree = ast.parse('''import six.moves''')
    expected = ast.parse(import_rewrite.get_body(previous='import six.moves',
                                                 current='import mock_six.moves')[0])
    tree2 = MockClass.transform(tree).tree
    assert tree

# Generated at 2022-06-14 01:44:29.482749
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import traceback
    import unittest
    from typed_ast.ast3 import Module, parse, mod
    class BaseClassImportRewriteTest(unittest.TestCase):
        def setUp(self):
            self.tree = parse('import abc;', mode='eval')
            self.rewrites = [('abc', 'foo')]
        def test__get_matched_rewrite(self):
            obj = BaseImportRewrite(self.tree)
            obj._get_matched_rewrite('abc')
            obj._get_matched_rewrite('abc.')
            obj._get_matched_rewrite('abc.def')
            self.assertEqual(obj._get_matched_rewrite('acc'), None)
            obj._get_matched_rewrite('abc')
        def test__replace_import(self):
            obj

# Generated at 2022-06-14 01:44:37.677883
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import os')

    class Mock(BaseImportRewrite):
        rewrites = [('os', 'pathlib')]

    transformer = Mock(tree)
    assert transformer.visit(tree) == None
    assert str(tree) == "try:\n    import os\nexcept ImportError:\n    import pathlib\n"


# Generated at 2022-06-14 01:44:49.087317
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    @pytest.mark.parametrize('name, from_, to, expected', [
        ('future', 'future', 'past',
         'try:\n    from past import *\nexcept ImportError:\n    from future import *'),
        (None, None, None,
         'from future import *'),
    ])
    def _test(name, from_, to, expected):
        class Rewrite(BaseImportRewrite):
            rewrites = [] if from_ is None else [(from_, to)]
        import_ = ast.Import(names=[
            ast.alias(name=name,
                      asname=None)])
        import_visited = Rewrite.visit_Import(import_)
        assert ast.dump(import_visited) == expected

    _test()


# Generated at 2022-06-14 01:44:59.335902
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')]

        def visit_Import(self, node):
            return super().visit_Import(node)

    tree = ast.parse('import foo')
    assert ast.dump(Test.transform(tree).tree) == "Try(\nbody=[Import(names=[alias(name='bar', asname=None)])],\nhandlers=[ExceptHandler(type=None, name=None, body=[Import(names=[alias(name='foo', asname=None)])])],\nfinalbody=[])"


# Generated at 2022-06-14 01:45:08.080222
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert_equal = partial(assert_equal, context=globals())
    assert_equal(dedent("""
    import sys
    """).strip(), BaseImportRewrite._replace_import(
        ast.parse("""
        import sys
        """).body[0], 'sys', 'os').body[0].body[0].body[0])

    assert_equal(dedent("""
    from unittest import mock
    """).strip(), BaseImportRewrite._replace_import(
        ast.parse("""
        from unittest import mock
        """).body[0], 'unittest', 'tests').body[0].body[0].body[0])


# Generated at 2022-06-14 01:45:14.305916
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from aiowsgi.utils.compilation import Compiler
    import inspect
    import astor
    from astor.code_gen import to_source
    with open(inspect.getsourcefile(BaseImportRewrite)) as fp:
        source = fp.read()
        translated = Compiler.compile(source, import_rewrites=[('typing', 'aiowsgi.typing')])
        tree = astor.parse_file(translated)
        print(to_source(tree))

# Generated at 2022-06-14 01:45:25.313639
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    from tests.utils import extract
    from ..utils.snippet import dedent
    from ..utils import get_in_mem_ast_tree

    class Test(BaseImportRewrite):
        rewrites = [('a', 'b')]
        dependencies = ['b']

    # test1: without alias
    code = dedent('''
    import a
    
    def foo():
        pass
    ''')
    tree = get_in_mem_ast_tree(code)
    Test.transform(tree)
    assert extract(tree) == dedent('''
    try:
        import a
    except ImportError:
        import b
    
    def foo():
        pass
    ''')

    # test2: with alias

# Generated at 2022-06-14 01:45:34.815118
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from typed_ast.transforms.annotation_decorator import AnnotationDecoratorTransformer
    from typed_ast.transforms.typing_transformer import TypingTransformer


# Generated at 2022-06-14 01:45:45.380942
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('old', 'new')
        ]

    # Simple import
    source = 'import old'
    tree = ast.parse(source)
    orig_tree, changed, deps = Test.transform(tree)
    expected = ('import new\ntry:\n    import old\nexcept ImportError:\n    pass\n')
    assert orig_tree.body[0].module == 'new'
    assert orig_tree.body[1].body[0].module == 'old'
    assert changed
    assert deps == []
    assert ast.dump(orig_tree) == expected

    # Simple import with alias
    source = 'import old as new'
    tree = ast.parse(source)
    orig_tree, changed, deps = Test.transform(tree)


# Generated at 2022-06-14 01:45:53.089329
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.checker import check_transformation

    class TestImport(BaseImportRewrite):
        rewrites = [('foo', 'test.foo')]

    check_transformation(
        TransformationResult(ast.parse('from foo import bar'), True, []),
        'import foo',
        TestImport)


# Generated at 2022-06-14 01:46:02.820193
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import typed_astunparse as pprint
    tree = ast.parse("""
from importlib import reload
from typing import *
from collections import namedtuple
from collections import (
    namedtuple as nt,
    Foo as Foo,
)
from collections import namedtuple as nt
from typing import (
    foo,
    bar as baz,
)

from collections import namedtuple as nt2

from collections import namedtuple as nt3
from io import BytesIO
import pandas as pd

from pandas import DataFrame
""")

# Generated at 2022-06-14 01:46:12.873190
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    tree = ast.parse('''
import a
import a.b as b
import a.b as c, d

import a.b.c

''')

    class ITRW(BaseImportRewrite):
        rewrites = [
            ('a.b', 'b')
        ]

    result = ITRW.transform(tree)


# Generated at 2022-06-14 01:46:14.161108
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    node = ast.parse('import sys')
    assert BaseImportRewrite.transform(node).transformed



# Generated at 2022-06-14 01:46:22.286866
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # WARNING: ast.parse is not part of public API and can be changed in future releases.
    #          Use typed_ast module instead
    tree = ast.parse('import x')
    rewriter = BaseImportRewrite.__new__(BaseImportRewrite)
    rewriter.rewrites = [('x', 'y')]
    node = tree.body[0]  # type: ast.Import
    node_ = rewriter.visit_Import(node)

    assert node_
    assert isinstance(node_, ast.Try)
    assert hasattr(node_, 'body')
    assert hasattr(node_, 'handlers')
    assert hasattr(node_, 'orelse')
    assert hasattr(node_, 'finalbody')
    assert hasattr(node_, 'type_comment')
    assert node_.body

# Generated at 2022-06-14 01:46:29.462178
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse(
            "import math\n"
            "import random")
    tr = BaseImportRewrite(tree)
    tr.rewrites = [('math', 'math_rewrite')]
    tr.visit(tree)
    assert ast.dump(tree) == \
            "try:\n" \
            "    import math_rewrite\n" \
            "except ImportError:\n" \
            "    import math\n" \
            "import random\n"



# Generated at 2022-06-14 01:46:43.612692
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..base import BaseCompiler

    class RewriteImport(BaseImportRewrite):
        target = CompilationTarget.PYTHON_RUN_UNDER_PYTHON
        rewrites = [
            ('foo', 'bar')
        ]

    tree = ast.parse(
        'import foo\n'
        'import foo.bar\n'
        'import foo.bar.baz'
    )

    tree_ = RewriteImport().visit(tree)

    print(ast.dump(tree_))


# Generated at 2022-06-14 01:46:49.195947
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import parse

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('random', '_random')]

    tree = parse('import random')
    result = ImportRewrite.transform(tree)
    print(result.tree)



# Generated at 2022-06-14 01:46:53.782308
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    transformation = BaseImportRewrite()
    result = transformation.visit(ast.parse("""
import re
    """).body[0])
    assert isinstance(result, ast.Import)


# Generated at 2022-06-14 01:47:06.928854
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import io
    tree = ast.parse("""
    from urllib.request import urlopen
    from urllib import parse
    """)

    class MockTransformer(BaseImportRewrite):
        rewrites = [('urllib.request', 'urllib3.request'),
                    ('urllib.parse', 'urllib3.parse')]

    transformer = MockTransformer(tree)
    transformer.visit(tree)
    out = io.StringIO()
    out.write(ast.dump(tree, include_attributes=True))
    source = out.getvalue()

# Generated at 2022-06-14 01:47:20.407422
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('six', 'six.moves')]  # type: List[Tuple[str, str]]

    tree = ast.parse(textwrap.dedent("""
    from six import StringIO
    from six.moves import queue
    """))

    expected_tree = ast.parse(textwrap.dedent("""
    try:
        from six import StringIO
    except ImportError:
        from six.moves import StringIO

    try:
        from six.moves import queue
    except ImportError:
        from six.moves import queue
    """))

    TestImportRewrite.transform(tree)

    assert ast.dump(expected_tree) == ast.dump(tree)

# Generated at 2022-06-14 01:47:26.500173
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class MyTransformer(BaseImportRewrite):
        rewrites = [('.foo', '.bar')]

    test_data = {
        "import foo": "try:\n    import foo\nexcept ImportError:\n    import bar",
        "import foo.bar": "try:\n    import foo.bar\nexcept ImportError:\n    import bar.bar",
    }

    for current, rewrote in test_data.items():
        tree = ast.parse(current)
        MyTransformer.transform(tree)
        assert rewrote == astor.to_source(tree)



# Generated at 2022-06-14 01:47:32.229000
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('from foo import a, b\n')
    Test.transform(tree)
    expected = ast.parse('try:\n    from foo import a, b\n'
                         'except ImportError:\n    from bar import a, b\n')
    assert ast.dump(tree) == ast.dump(expected)

    tree = ast.parse('from foo.something import a, b\n')
    Test.transform(tree)
    expected = ast.parse('try:\n    from foo.something import a, b\n'
                         'except ImportError:\n    from bar.something import a, b\n')
    assert ast.dump(tree) == ast.dump(expected)


# Generated at 2022-06-14 01:47:33.654260
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    print(BaseImportRewrite._visit_Import)



# Generated at 2022-06-14 01:47:39.852715
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewriter(BaseImportRewrite):
        rewrites = [('foo.bar', 'baz.bar')]

    test_tree = ast.parse("""import foo.bar""")
    test_instance = TestImportRewriter(test_tree)
    assert test_instance.visit_Import(test_tree.body[0]).test.comparators[0].id == 'ImportError'



# Generated at 2022-06-14 01:47:49.049539
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [(from_, to) for from_ in 'abcdefghijklmnopqrstuvwxyz'
                                   for to in 'abcdefghijklmnopqrstuvwxyz']

    tree = ast.parse('''
from a import a, b
from six.moves import input, map
from six.moves.builtins import *
from six.moves.dbm_gnu import open
from past.builtins import basestring, unicode
''')

    result = TestImportRewrite.transform(tree)

# Generated at 2022-06-14 01:47:58.562735
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    code = """import module

print('hello world')
    """
    tree = ast.parse(code)
    transformer = BaseImportRewrite(tree)
    transformer.rewrites = [('module', 'new_module')]
    tree = ast.fix_missing_locations(transformer.generic_visit(tree))
    assert ast.dump(tree) == """try:
    import new_module
except ImportError:
    import module

print('hello world')
"""
    transformer = BaseImportRewrite(tree)
    transformer.rewrites = [('new_module', 'module')]
    tree = ast.fix_missing_locations(transformer.generic_visit(tree))
    assert ast.dump(tree) == """import module

print('hello world')
"""



# Generated at 2022-06-14 01:48:09.169491
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class BaseImportRewrite_visit_ImportFrom(BaseImportRewrite):
        rewrites = [
            ('renamed', 'replaced.renamed'),
            ('renamed2', 'replaced2.renamed2'),
        ]

    # simple import
    inp = ast.parse('''
import a.b.c.d
''')
    out = ast.parse('''
import a.b.c.d
''')
    BaseImportRewrite_visit_ImportFrom().visit(inp)
    assert ast.dump(inp) == ast.dump(out)

    # import with alias
    inp = ast.parse('''
import a.b.c.d as e
''')
    out = ast.parse('''
import a.b.c.d as e
''')


# Generated at 2022-06-14 01:48:14.821936
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import pytest
    import astor

    try:
        # Python 3
        from astor.code_gen import SourceGenerator
    except ImportError:
        # Python 2
        from astor.to_source import Unparser

    from typed_ast.ast3 import parse
    from typed_ast.ast3 import Print, Load, Store, Name, ImportFrom

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('django.utils.http', 'django.http')]

    def test_transform(source: str, expected: str) -> None:
        tree = parse(source)
        tree = TestImportRewrite.transform(tree).tree

        if sys.version_info[0] == 3:
            generator = SourceGenerator(indentation=' ' * 4)
            generator.visit(tree)

# Generated at 2022-06-14 01:48:26.037881
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from tranpy.migrations.django import geo
    class Y(BaseImportRewrite):
        rewrites = [('django.contrib.gis', 'tranpy.migrations.django.geo')]

    # result is a module
    result = geo.to_ogr
    body = ast.parse('import django.contrib.gis.geo.geos as g').body
    new_body = Y.transform(body).tree
    assert isinstance(new_body, ast.Try)
    assert isinstance(new_body.body[0].body[0], ast.Import)
    assert new_body.body[0].body[0].names[0].name == 'tranpy.migrations.django.geo.geos'

# Generated at 2022-06-14 01:48:37.087069
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor  # type: ignore
    code_test1 = ("from django.conf.urls import url\n"
                  "from django.contrib.auth.models import User")
    code_test2 = ("from django.conf.urls import url\n"
                  "from django.contrib.auth.models import User, User, *")
    code_test3 = "from django.conf.urls import *"
    code_test4 = ("from django.conf.urls import include, url\n"
                  "from django.contrib.auth.models import User, User, *")
    code_test5 = "from django.conf.urls import url, include"
    code_test6 = "from django.contrib.auth.models import User"

# Generated at 2022-06-14 01:48:47.592552
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..compiler import compile
    import six

    FOO = 'foo'
    FOO_F = 'foo.f'
    FOO_FOO = 'foo.foo'
    FOO_BAR = 'foo.bar'
    FOO_F_FOO_PY = 'foo/f/foo.py'

    code = '''
        from foo import f, foo, bar
        from foo import f as a
        from foo import foo as b
        from foo.f import foo
    '''
    class BarImportRewrite(BaseImportRewrite):
        #: Rewrite map.
        rewrites = [(FOO, FOO_F), (FOO_F_FOO_PY, FOO_FOO)]

    tree = compile(code, BarImportRewrite)
    assert ast

# Generated at 2022-06-14 01:48:49.779459
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.tester import run_nodes_test
    run_nodes_test('Import', BaseImportRewrite)


# Generated at 2022-06-14 01:49:00.153862
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    test_class = BaseImportRewrite()

    test_class.rewrites = [
            ('foo.bar', 'foo_bar'),
            ('baz.bar', 'baz_bar'),
            ('baz', 'baz2'),
        ]

    node = ast.ImportFrom(
        module='foo.bar.baz',
        names=[
            ast.alias(name='foo', asname='foo_alias'),
            ast.alias(name='bar', asname='bar_alias'),
        ],
        level=0)


# Generated at 2022-06-14 01:49:07.009174
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import ast
    class NodeTransformer(BaseImportRewrite):
        rewrites = [('click', 'flask_click')]

    node_transformer = NodeTransformer()
    p = ast.parse("from click import option, command")
    ast.fix_missing_locations(p)
    p = node_transformer.visit(p)
    print(astor.to_source(p))


# Generated at 2022-06-14 01:49:15.996821
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('requests', 'trequests'),
            ('aiohttp', 'trequests')]

    test_tree = ast.parse('''import requests
try:
    import trequests
except ImportError:
    import trequests
''')

    result = TestTransformer.transform(test_tree)
    assert result.tree == test_tree

    test_tree = ast.parse('''import requests
import trequests
''')

    result = TestTransformer.transform(test_tree)
    assert result.tree != test_tree



# Generated at 2022-06-14 01:49:26.636158
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from textwrap import dedent
    from typed_ast import ast3 as ast
    import typing
    import os

    class MockTransformer(BaseImportRewrite):
        rewrites = [('typing', 'types')]

    tree = ast.parse(dedent("""\
        import typing
        import os
        import os.path as osp
        import mypy_boto3"""))

    MockTransformer.transform(tree)

    assert ast.dump(tree) == dedent("""\
        try:
            extend(typing)
        except ImportError:
            extend(types)
        import os
        try:
            extend(os.path)
        except ImportError:
            from os import path as osp  # type: ignore
        import mypy_boto3""")


# Generated at 2022-06-14 01:49:31.128417
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    class DummyImportRewrite(BaseImportRewrite):
        rewrites = [
            ('ast', 'typed_ast.ast3'),
        ]


# Generated at 2022-06-14 01:49:41.168932
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astor.code_gen import to_source

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]


# Generated at 2022-06-14 01:49:49.144667
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    source = "from urlparse import urlparse, urljoin\nclass Test: pass\n"
    ast_node = ast.parse(source)
    tree = ast.parse("from urlparse import urlparse, urljoin\nclass Test: pass\n")
    visit_ImportFrom_obj = BaseImportRewrite("")
    ret_type = visit_ImportFrom_obj.visit_ImportFrom(ast_node.body[0])
    assert ret_type == tree.body[0]


# Generated at 2022-06-14 01:50:04.916272
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    module_name = 'pytest'
    import_name = 'TestCase'
    import_asname = 'TC'
    alias = ast.alias(name=import_name, asname=import_asname)
    original_statement = ast.ImportFrom(module=module_name,
                                        names=[alias],
                                        level=0)
    module_name_replaced = 'unittest'
    import_name_replaced = 'TestCase'
    import_asname_replaced = 'TC'
    alias_replaced = ast.alias(name=import_name_replaced, asname=import_asname_replaced)
    replaced_statement = ast.ImportFrom(module=module_name_replaced,
                                        names=[alias_replaced],
                                        level=0)

    # Test for method _replace_

# Generated at 2022-06-14 01:50:13.972628
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    print("test_BaseImportRewrite_visit_ImportFrom")
    import ast
    import astunparse
    expr = 'from a.b import c, d, e'
    expected = 'try: from a.b import c, d, e;' + '\n' + 'except ImportError: from a.b import c, d, e'
    class TestTransformer(BaseImportRewrite):
        rewrites = [('a.b', 'a.b.c')]
    transformer = TestTransformer(None)
    node = ast.parse(expr)
    result = transformer.visit_ImportFrom(node.body[0])
    assert astunparse.unparse(result) == expected



# Generated at 2022-06-14 01:50:20.477151
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # input tree
    tree = ast.parse('''
import os
import tempfile
import pathlib
''')
    # expected output tree
    output = ast.parse('''
import os
try:
    extend(tempfile)
except ImportError:
    extend(pathlib)
''')
    assert BaseImportRewrite(tree).visit_Import(tree.body[1]) == output.body[1]


# Generated at 2022-06-14 01:50:28.534357
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse


# Generated at 2022-06-14 01:50:39.146452
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from . import test_data

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('six', 'six.moves'),
            ('pyspark.sql', 'pyspark.sql.dataframe'),
        ]

    body = test_data.BODY_SIX_RENAME.data['body']
    new_body = TestImportRewrite.transform(body).new_tree
    assert astor.to_source(new_body) == test_data.BODY_SIX_RENAME_TRANSFORMED.data['body']

    body = test_data.BODY_SPARK_RENAME.data['body']
    new_body = TestImportRewrite.transform(body).new_tree
    assert astor.to_source(new_body) == test

# Generated at 2022-06-14 01:50:50.458684
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_stmt = ast.parse('from django.contrib.auth import get_user_model').body[0]  # type: ast.ImportFrom
    class MockImportRewriter(BaseImportRewrite):
        rewrites = [('django.contrib.auth', 'django.contrib.auth.get_user_model')]

    result = MockImportRewriter.transform(import_stmt)
    assert len(result.tree.body) == 1
    assert isinstance(result.tree.body[0], ast.Try)
    assert isinstance(result.tree.body[0].body[0], ast.ImportFrom)
    assert result.tree.body[0].body[0].module == 'django.contrib.auth.get_user_model'

# Generated at 2022-06-14 01:51:01.130608
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('os.path', 'pathlib')]

    input = ast.Import(names=[
        ast.alias(name='os.path',
                  asname=None),
    ])

    result = TestTransformer.transform(input)


# Generated at 2022-06-14 01:51:10.540304
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astor
    from ..testing import transform_compile

    class TestTransformer(BaseImportRewrite):
        target = 'test'
        rewrites = [
            ('test.test_base_import_rewrite', 'test.base_import_rewrite_test_module')
        ]

    class Test(unittest.TestCase):
        def test_transform(self):
            tree = ast.parse('import test.test_base_import_rewrite')
            tree = TestTransformer.transform(tree).tree
            self.assertEqual(
                astor.to_source(tree),
                """
try:
    import test.test_base_import_rewrite
except ImportError:
    import test.base_import_rewrite_test_module
"""[1:]
            )

       

# Generated at 2022-06-14 01:51:22.710513
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    class Test(unittest.TestCase):
        def test_BaseImportRewrite_visit_ImportFrom_1(self):
            import astor

            class Rewriter(BaseImportRewrite):
                rewrites = [('six', 'six.moves')]

            orig_code = 'from ast import literal_eval'
            expected_code = 'from ast import literal_eval'
            tree = ast.parse(orig_code)
            Rewriter.transform(tree)
            actual_code = astor.to_source(tree)
            self.assertEqual(expected_code, actual_code)

        def test_BaseImportRewrite_visit_ImportFrom_2(self):
            import astor


# Generated at 2022-06-14 01:51:31.509272
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import datetime
    module_name = datetime.__name__

    import pytest
    import astor

    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [('datetime', 'time')]

    source_code = 'from datetime import datetime' # type: ignore
    tree = ast.parse(source_code)
    new_tree = MyBaseImportRewrite.transform(tree).tree
    generated_code = astor.to_source(new_tree)

    assert generated_code == (
        'try:\n'
        '    from datetime import datetime\n'
        'except ImportError:\n'
        '    from time import datetime' # type: ignore
    )



# Generated at 2022-06-14 01:51:40.207632
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from .test_loader import test_ast

    assert BaseImportRewrite.visit(test_ast.test1, astor.to_source(test_ast.test2)) == astor.to_source(test_ast.test3)

# Generated at 2022-06-14 01:51:52.043165
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    node = ast.Import([ast.alias(name="numpy", asname="np")])
    node2 = ast.Import([ast.alias(name="numpy.random", asname="np.random")])

    rewriter = BaseImportRewrite(None)
    rewriter.rewrites = [("numpy", "np")]
    result = rewriter.visit_Import(node)
    assert hasattr(result, "body")
    assert result.body[0].value.names[0].name == "np"
    assert result.body[1].value.names[0].name == "np"
    assert result.body[0].value.names[0].asname == "np"
    assert result.body[1].value.names[0].asname == "np"

    rewriter = BaseImportRewrite(None)


# Generated at 2022-06-14 01:52:00.978273
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    ast_expr = 'from b import y, z'
    module = ast.parse(ast_expr)

    rewrite = BaseImportRewrite(None)
    rewrite.rewrites = [('a', 'b')]

    node = rewrite.visit(module)
    assert isinstance(node, ast.Try)
    assert [_[1] for _ in node.handlers[0].body[0].body] == [ast.ImportFrom(names=[ast.alias(name='y')],
                                                                           level=0),
                                                            ast.ImportFrom(names=[ast.alias(name='z')],
                                                                           level=0)]



# Generated at 2022-06-14 01:52:11.689258
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    from ..utils import get_ast

    class Test(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None

        def test_import_rewrite(self):
            src = """
            import module
            """

            class Transformer(BaseImportRewrite):
                rewrites = [('module', 'new_module')]

            tree = get_ast(src)
            tree_changed, tree = Transformer.transform(tree)

            expected = """
            try:
                import module
            except ImportError:
                import new_module
            """

            self.assertTrue(tree_changed)
            self.assertEqual(expected, ast.dump(tree, annotate_fields=False),
                             "Could not rewrite import")


# Generated at 2022-06-14 01:52:17.233209
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..compilers.formats import ast_to_source

    class TestClass(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
        
        def __init__(self, tree: ast.AST):
            super().__init__(tree)

    tree = ast.parse("import foo")
    inst = TestClass(tree)
    inst.visit_Import(tree.body[0])
    source = ast_to_source(tree)
    inst._tree_changed.should.be.ok
    source.should.equal("try:\n    import foo\nexcept ImportError:\n    import bar\n")

# Generated at 2022-06-14 01:52:25.453953
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import sys

    from typed_ast import ast3 as ast

    from dmypy_extensions.transforms import BaseImportRewrite

    class MockImportRewrite(BaseImportRewrite):
        rewrites = [('a', 'b')]

        def __init__(self):
            super().__init__(None)

    print('MockImportRewrite:')
    print(MockImportRewrite.__qualname__)
    node = ast.ImportFrom(module='a',
                          names=[ast.alias(name='c', asname=None)],
                          level=0)
    print('ast.ImportFrom:')
    print(ast.dump(node))

    transformer = MockImportRewrite()

    result = transformer.visit_ImportFrom(node)
    print('result:')

# Generated at 2022-06-14 01:52:38.209017
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('old', 'new')]

    tree = ast.parse('''
foo = 5
import old
a = old.some_stuff()
''')

    node = tree.body[1]
    assert isinstance(node, ast.Import) and node.names[0].name == 'old'

    try_node = TestTransformer(tree).visit_Import(node)
    assert isinstance(try_node, ast.Try) and try_node.body[0].names[0].name == 'new.old'


# Generated at 2022-06-14 01:52:46.224266
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast_transformer
    import ast

    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('sys.path', 'os.path.sys'),
            ('os', 'os.sys')
        ]


# Generated at 2022-06-14 01:52:58.577019
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import astor

    class TestImportRewrite(BaseImportRewrite):
        rewrites=[
            ('some.module', 'another.module'),
            ('some.module.with.long.name', 'another.module.with.long.name')]

    class Test(unittest.TestCase):
        def test_from_one_module_to_another(self):
            self.assertEqual(
                astor.to_source(TestImportRewrite.transform(
                    ast.parse("from some.module import some_function")).tree
                ),
                astor.to_source(TestImportRewrite.transform(
                    ast.parse("from some.module import some_function as some_function")
                ).tree)
            )


# Generated at 2022-06-14 01:53:10.443405
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .test_utils import assert_transformed


# Generated at 2022-06-14 01:53:23.304170
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """
    import ast
    import os
    import typing
    import zlib
    from foo.bar import baz
    from foo.bar import lol, kek
    from foo.bar import kek as kek_alias
    from gevent.httplib import HTTPSConnection
    from gevent import httplib
    from gevent.socket import socket
    from gevent import socket as socket_alias
    """


# Generated at 2022-06-14 01:53:31.531148
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import sys
    import os
    import unittest

    import typed_ast.ast3 as ast
    from types import ModuleType
    from typed_ast.transforms import BaseImportRewrite  # type: ignore

    class ImportRewriteTransformer(BaseImportRewrite):
        target = None
        rewrites = [
            ('os', 'my_os'),
            ('os.path', 'my_os.path'),
        ]

    class FakeModule(ModuleType):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.__doc__ = ''

    sys.modules['my_os'] = FakeModule('my_os')
    sys.modules['my_os.path'] = FakeModule('my_os.path')


# Generated at 2022-06-14 01:53:42.060288
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Given
    import ast
    import six
    import typing

    rewrites = [(six.__name__, 'six')]
    node = ast.parse('from six import x').body[0]
    node.names.append(ast.alias(name='typing', asname='t'))
    node.names.append(ast.alias(name='typing.List', asname='LL'))
    node.names.append(ast.alias(name='typing.Tuple', asname='T'))
    node.names.append(ast.alias(name='typing.List.append', asname='a'))

    # When
    transformed = BaseImportRewrite(None).visit_ImportFrom(node)

    # Then

# Generated at 2022-06-14 01:53:52.349967
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    import importlib
    import typing

    class TestTransformer(BaseImportRewrite):
        pass

    TEST_MODULE_NAME = 'typing'
    TEST_MODULE_ALIAS = 'typing'
    TEST_NAME = 'Optional'
    TEST_ASNAME = 'Optional'


# Generated at 2022-06-14 01:54:01.667007
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # test_replace_import_from_module
    nodes = ast.parse("from original.module import blah")
    rewrite_class = type("rewrite_class", (BaseImportRewrite,), {'rewrites': [('original.module', 'new.module')]})

    result = rewrite_class.transform(nodes)

    expected = ast.parse("""
try:
    from original.module import blah
except ImportError:
    from new.module import blah
""")

    assert ast.dump(result.tree) == ast.dump(expected)

    # test_replace_import_from_names
    nodes = ast.parse("from original.module import foo, blah, bar")