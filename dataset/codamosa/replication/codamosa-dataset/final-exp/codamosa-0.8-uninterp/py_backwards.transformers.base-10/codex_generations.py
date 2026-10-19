

# Generated at 2022-06-14 01:44:13.797917
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    node = ast.parse('import foo').body[0]
    result = Transformer.visit_Import(node)
    expected = ast.parse('try:\n'
                         '    import foo\n'
                         'except ImportError:\n'
                         '    import bar\n').body[0]
    assert result == expected



# Generated at 2022-06-14 01:44:21.159363
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast, astor, textwrap
    from typed_ast import ast3 as ast
    from typed_astunparse import unparse

    tree = ast.parse(textwrap.dedent("""\
        from urllib.request import urlopen
        """))

    transformer = type(b'Transformer', (BaseImportRewrite,), {
        'rewrites': [('urllib.request', 'urllib3.request')],
    })

    tree = transformer.transform(tree)


# Generated at 2022-06-14 01:44:27.904496
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    import astor
    
    class SampleTransformer(BaseImportRewrite):
        rewrites = (
            ("some.package", "another.package"),
        )
        
    tree = ast.parse('from some.package import a')
    
    result = SampleTransformer.transform(tree)
    result = astor.to_source(result.tree)
    
    expectation = "import another.package as a"

    assert expectation == result

# Generated at 2022-06-14 01:44:38.923858
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from ..types import CompilationTarget

    class TestNode(ast.ImportFrom):
        _fields = ("module", "names", "level")
        module = 'collections'
        names = [ast.alias(name="deque", asname=None), 
                 ast.alias(name="defaultdict", asname="d"), 
                 ast.alias(name="*", asname=None)]
        level = 0

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYPY2
        rewrites = [('collections.deque', 'collections_deque')]

    result = TestTransformer.transform(TestNode())
    assert result.changed
    assert isinstance(result.tree, ast.Try)

# Generated at 2022-06-14 01:44:48.215382
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    imports = ast.ImportFrom(module='path',
                             names=[
                                 ast.alias(name='abspath',
                                           asname='abspath')
                             ],
                             level=0)
    result = BaseImportRewrite._get_replaced_import_from_part(imports, imports.names[0],
                                                              {'path.abspath': ('path', 'os.path')})
    assert result.module == 'os.path'
    assert result.names[0].name == 'abspath'
    assert result.names[0].asname == 'abspath'
    assert result.level == imports.level



# Generated at 2022-06-14 01:44:53.680157
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class FakeTransformer(BaseImportRewrite):
        rewrites = [('old', 'new')]

    import_node = ast.Import(names=[ast.alias(name='old.one', asname='one')])
    fake = FakeTransformer(ast.Module(body=[import_node]))
    fake.visit(import_node)
    assert isinstance(import_node, ast.Try)



# Generated at 2022-06-14 01:45:03.490315
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from unittest.mock import patch
    from ..target.python import PythonTransformer

    # pylint:disable=attribute-defined-outside-init
    class TestTransformer(BaseImportRewrite):
        dependencies = []  # type: List[str]
        target = PythonTransformer
        rewrites = [('django.conf', 'mylib.myconf')]

    tree = ast.parse('import django.conf')
    with patch('..utils.snippet.extend') as mock_extend:
        result = TestTransformer.transform(tree)
    assert result.changed

    assert mock_extend.call_count == 1
    mock_extend.assert_called_once_with(expected_import_rewrite)



# Generated at 2022-06-14 01:45:12.983979
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class DummyTransformer(BaseImportRewrite):
        rewrites = [('django.utils.translation', 'django.utils.translation.lazy')]

    import_from = ast.parse("""from django.utils.translation import ugettext
    from django.utils.translation import ugettext as _
    from django.utils.translation import *
    from django.utils.translation.lazy import ugettext
""")


# Generated at 2022-06-14 01:45:24.413252
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewrites = [('six', 'six.moves')]
    func_name = 'test'

    class TestClass(BaseImportRewrite):
        rewrites = rewrites

    # 1. Module import
    old_import = ast.Import(names=[
        ast.alias(name='six'),
    ])
    old_func_def = ast.FunctionDef(name=func_name, body=[
        ast.Pass(),
    ])
    old_module = ast.Module(body=[
        old_import,
        old_func_def,
    ])

    new_import = ast.Import(names=[
        ast.alias(name='six.moves')
    ])
    new_func_def = ast.FunctionDef(name=func_name, body=[
        ast.Pass(),
    ])
    new_module

# Generated at 2022-06-14 01:45:33.489221
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        """Test class."""
        rewrites = [("xmlrpc.client", "xmlrpclib")]

    code = """
    import xmlrpc.client
    import _thread

    """
    tree = ast.parse(code, filename="<ast>")

    TestTransformer.transform(tree)

    expected = """
    try:
        import xmlrpc.client
    except ImportError:
        import xmlrpclib as client

    import _thread

    """
    expected = ast.parse(expected, filename="<ast>")

    assert ast.dump(tree, include_attributes=False) == ast.dump(expected, include_attributes=False)


# Generated at 2022-06-14 01:46:00.946523
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class SimpleImportRewrite(BaseImportRewrite):
        rewrites = (
            ('django.core', 'django'),
        )

    node = ast.parse('import django.core.urlresolvers')
    result = SimpleImportRewrite.transform(node)
    assert isinstance(result.tree, ast.Try)
    assert len(result.tree.body) == 2
    assert isinstance(result.tree.body[0], ast.Import)
    assert len(result.tree.body[0].names) == 1
    assert result.tree.body[0].names[0].name == 'django.core.urlresolvers'
    assert isinstance(result.tree.body[1], ast.ExceptHandler)
    assert len(result.tree.body[1].body) == 1

# Generated at 2022-06-14 01:46:12.503380
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    from typed_ast import ast3 as ast
    from mopy.transformations.base import BaseImportRewrite, TransformationResult

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('sqlalchemy', 'pony.orm'),
            ('sqlalchemy.orm', 'pony.orm')
        ]

    tree = ast.parse("""
    from os import path
    from sqlalchemy.orm import relationship
    from sqlalchemy import (
        create_engine,
        Column,
        Integer,
        String,
        ForeignKey
    )
    import sqlalchemy
    import os
    """)

    result = TestImportRewrite.transform(tree)


# Generated at 2022-06-14 01:46:21.734780
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    before = ast.parse('from test import A, B as C, * as *')
    instance = BaseImportRewrite(before)
    instance.rewrites = [('test', '__test__')]
    after = instance.visit(before)
    expected = ast.parse('''try:
        from __test__ import A, B as C, * as *
    except ImportError:
        from test import A, B as C, * as *''')
    assert ast.dump(after) == ast.dump(expected)

    after = ast.parse('from test.test2 import A, B as C, * as *')
    instance = BaseImportRewrite(after)
    instance.rewrites = [('test.test2', '__test__')]
    after = instance.visit(after)

# Generated at 2022-06-14 01:46:31.603070
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    class TestTransformer(BaseImportRewrite):
        rewrites = [('cStringIO', 'io')]

    tree = parse('''import cStringIO as cio

cio.StringIO()
''')
    TestTransformer.transform(tree)

    assert parse('''try:
    import cStringIO as cio
except ImportError:
    import io as cio

cio.StringIO()
''') == tree

    tree = parse('''import cStringIO_

cStringIO_.StringIO()
''')
    TestTransformer.transform(tree)

    assert parse('''import cStringIO_

cStringIO_.StringIO()
''') == tree


# Generated at 2022-06-14 01:46:45.858819
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import astor
    from nuitka.ast_nodes import scoped_nodes
    from nuitka.transforms import TransformBaseNuitkaModules

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('renamed1', 'renamed1_rewrite')]

    tree = scoped_nodes.compile_to_module(
        source_code=astor.to_source(ast.parse("""
            import renamed1.submodule1
        """, mode='exec')),
        filename='<test>'
    )
    print(astor.to_source(tree))
    TestBaseImportRewrite.transform(tree)
    print(astor.to_source(tree))
    # Check that _tree_changed is set to True
    assert TestBaseImportRew

# Generated at 2022-06-14 01:46:55.609393
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as std_ast
    import astunparse

    class TestTransformer(BaseImportRewrite):
        rewrites = (
            ('subprocess', 'subprocess32'),
        )

    transformed_tree = TestTransformer.transform(std_ast.parse('''
        import os
        import subprocess
        import subprocess.Popen
    '''))
    assert not transformed_tree.tree_changed
    assert astunparse.unparse(transformed_tree.tree) == '\nimport os\nimport subprocess\nimport subprocess.Popen\n'

    transformed_tree = TestTransformer.transform(std_ast.parse('''
        import subprocess
    '''))
    assert transformed_tree.tree_changed

# Generated at 2022-06-14 01:47:07.207367
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astunparse import unparse
    from ..transformer import BaseTransformer
    from ..utils.ast import get_changed
    import os

    ORIGINAL_SOURCE = '''
import module
'''

    EXPECTED_SOURCE = '''
try:
    import module
except ImportError:
    import module as module
'''

    tree = ast.parse(ORIGINAL_SOURCE)
    transformer = BaseTransformer(CompilationTarget.python, BaseImportRewrite, ())
    transformer.transform(tree)
    changed = get_changed(ORIGINAL_SOURCE, tree)
    assert changed == EXPECTED_SOURCE



# Generated at 2022-06-14 01:47:16.966668
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astor
    from typing import Dict, List
    from ..types import CompilationTarget
    from ..utils.snippet import snippet
    from ..transforms.bases import BaseImportRewrite

    @snippet
    def good():
        import import_target as import_target
        import import_target as import_target_as
        import import_target.module as module
        import import_target.module.module as module_as

    @snippet
    def bad():
        import not_import_target as import_target

    @snippet
    def good_other():
        import not_import_target as not_import_target

    @snippet
    def expected_rewrite():
        import import_target as import_target

# Generated at 2022-06-14 01:47:20.934130
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('some_module', 'another.module')]

    ast_module = ast.parse('''
import some_module
import some_module.something
import something_else
''')
    result = TestImportRewrite.transform(ast_module)
    assert astor.to_source(result.tree) == '''\
try:
    import some_module
except ImportError:
    import another.module

try:
    import some_module.something
except ImportError:
    import another.module.something

import something_else
'''
    assert result.changed is True



# Generated at 2022-06-14 01:47:28.433618
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    from typed_ast import ast3 as ast

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.transformer = BaseImportRewrite()

        def test_rewrite_import(self):
            import_statement = ast.parse('import urllib.request')
            expected_statement = ast.parse('''
try:
    import urllib.request
except ImportError:
    import urllib2.request
''')
            result = self.transformer.visit(import_statement)
            self.assertEqual(result, expected_statement)

        def test_dont_rewrite_import(self):
            import_statement = ast.parse('import sys')
            expected_statement = ast.parse('import sys')
            result = self.transformer.vis

# Generated at 2022-06-14 01:47:55.076062
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    import unittest

    import typed_astunparse
    import six

    class BaseImportRewriteTester(unittest.TestCase):
        def run_test(self, source, expected_output):
            func = compile(source, '<string>', 'exec', ast.PyCF_ONLY_AST)
            expected = compile(expected_output, '<string>', 'exec', ast.PyCF_ONLY_AST)

            transformer = BaseImportRewrite({'io': 'io'})
            actual = transformer.transform(func)
            if six.PY3:
                self.assertEqual(ast.dump(expected), ast.dump(actual))

# Generated at 2022-06-14 01:48:05.925942
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typed_ast.ast3 as ast
    import sys
    import types
    import collections
    import itertools

    import os

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

    import sys
    import types
    import collections
    import itertools

# Generated at 2022-06-14 01:48:13.986445
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Subclass(BaseImportRewrite):
        rewrites = [('re', 'regex')]
    node = ast.Import(names=[ast.alias(name='re', asname='re')])
    ast.copy_location(node, node)
    res = Subclass.transform(node)
    assert res.tree == ast.Try(body=[ast.Import(names=[ast.alias(name='regex', asname='re')])],
                               handlers=[],
                               orelse=[],
                               finalbody=[],
                               lineno=1,
                               col_offset=0)
    assert res.changed == True



# Generated at 2022-06-14 01:48:24.896658
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import tempfile
    import os

    import typed_astunparse
    from typed_ast.ast3 import parse

    tree = parse("import sys")
    result = BaseImportRewrite.transform(tree)
    assert result.tree == tree

    class Rewrite(BaseImportRewrite):
        imports = [
            ('threading', '_thread'),
            ('math', 'mathlib')]

    tree = parse("import sys")
    result = Rewrite.transform(tree)
    assert result.tree == tree

    tree = parse("import threading")
    result = Rewrite.transform(tree)
    assert typed_astunparse.unparse(result.tree) == '''\
try:
    import threading
except ImportError:
    import _thread'''

    tree = parse("import math")
    result = Rewrite.transform

# Generated at 2022-06-14 01:48:34.065861
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    sample_import = "import astor.codegen"
    sample_import_transformed = ("try:\n"
                                 "    import astor.codegen\n"
                                 "except ImportError:\n"
                                 "    import astor")
    tree = ast.parse(sample_import)
    rewrites = [('astor', 'astor.codegen')]
    rewriter = BaseImportRewrite(tree)
    rewriter.rewrites = rewrites
    rewriter.visit(tree)
    assert astor.to_source(tree) == sample_import_transformed


# Generated at 2022-06-14 01:48:40.281730
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_rewrite_obj = BaseImportRewrite()
    node = ast.Import(names = [ast.alias(name='foo', asname = 't')])
    import_rewrite_obj.rewrites = [('foo', 'bar')]
    ret_val = import_rewrite_obj.visit_Import(node)
    assert isinstance(ret_val, ast.Import)


# Generated at 2022-06-14 01:48:50.115588
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from_ = 'urllib'
    to = 'urllib3'
    module = 'urllib.request'
    name = 'urlopen'

    module2 = 'urllib.request'
    name2 = 'urlopen'

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [(from_, to)]

    inst = TestBaseImportRewrite(None)
    node1 = ast.ImportFrom(module=module, names=[ast.alias(name=name, asname=name)], level=0)
    node2 = ast.ImportFrom(module=module2, names=[ast.alias(name=name2, asname=name2)], level=0)

    new_node = inst.visit_ImportFrom(node1)

# Generated at 2022-06-14 01:49:00.645151
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ...common import ast as ee_ast
    from .mock import import_from_mock

    input = ee_ast.parse("from io import StringIO")
    rw = BaseImportRewrite(input).visit_ImportFrom(input.body[0])
    assert import_from_mock == ee_ast.dump(rw)

    input = ee_ast.parse("from os import *")
    rw = BaseImportRewrite(input).visit_ImportFrom(input.body[0])
    assert import_from_mock == ee_ast.dump(rw)

    input = ee_ast.parse("""from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta""")

# Generated at 2022-06-14 01:49:11.552380
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse
    import os
    import sys

    from ..utils.make_tree  import make_tree

    code = """
    import six
    import functools
    import datetime
    """
    rewrites = {
            'six': ('six', 'sixer')
    }

    tree = make_tree(code, 'python3')

    class Transformer(BaseImportRewrite):
        rewrites = list(rewrites.values())

    trans = Transformer(tree)
    trans.visit(tree)

    expected_code = """
    import six
    import functools
    import datetime
    """
    assert astunparse.unparse(tree) == expected_code

    code = """
    import six
    import functools
    import datetime
    """

# Generated at 2022-06-14 01:49:19.159859
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typing
    import astor

    class TestTransformer(BaseImportRewrite):
        rewrites = [('typing', 'tp')]

    test_code = 'from typing import Iterable'
    fixed_code = '''try:
    from typing import Iterable
except ImportError:
    from tp import Iterable'''

    result = TestTransformer.transform(ast.parse(test_code, mode='exec'))
    assert astor.to_source(result[0]) == fixed_code
    assert result[1] == True
    assert result[2] == []

# Generated at 2022-06-14 01:49:39.986607
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('six', 'past')]


# Generated at 2022-06-14 01:49:44.888241
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node = ast.parse('from datetime import datetime').body[0]
    visitor = BaseImportRewrite(None)
    visitor.rewrites.append(('datetime', 'dateutil'))
    visitor.generic_visit(node)
    assert visitor._tree_changed



# Generated at 2022-06-14 01:49:52.830064
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    before = astor.to_source(ast.parse("""from tqdm import tqdm"""))
    after = astor.to_source(ast.parse("""try:
        from tqdm import tqdm
    except ImportError:
        from tqdm import tqdm_notebook as tqdm"""))

    class Rewrite(BaseImportRewrite):
        rewrites = [
            ('tqdm', 'tqdm.notebook')
        ]

    assert Rewrite.transform(ast.parse(before)).tree_code == after



# Generated at 2022-06-14 01:50:02.774217
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from typed_ast import ast3 as ast

    import_from = '''from six import string_types'''

    class UnitTest(BaseImportRewrite):
        rewrites = [('six', 'six.moves')]

    tree = astor.parse_file(import_from, mode="exec")  # type: ast.Module
    transformed_tree = UnitTest.transform(tree)
    assert astor.to_source(transformed_tree.tree) == '''try:
    from six import string_types
except ImportError:
    from six.moves import string_types'''

# Generated at 2022-06-14 01:50:08.220487
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class RewriteClass(BaseImportRewrite):
        rewrites = [('pandas', 'pandas_profiling')]

    code = "from pandas import read_csv"
    tree = ast.parse(code)
    rewrite_tree = RewriteClass.transform(tree).tree
    print(ast.dump(rewrite_tree))

    assert_equal(rewrite_tree.body[0].body[0].body[0].body[0].value.func.id, "extend")
    assert_equal(rewrite_tree.body[0].body[0].body[0].body[0].value.args[0].elts[0].value.names[0].name, "pandas")


# Generated at 2022-06-14 01:50:15.855696
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse('from a.b.c import d as e')
    class MockTransformer(BaseImportRewrite):
        rewrites = [('a.b.c', 'd.e.f')]
    result = MockTransformer.transform(tree)
    assert result.changed is True
    assert result.dependencies == ['a.b.c', 'd.e.f']
    assert result.tree == ast.parse('''
try:
    from a.b.c import d as e
except ImportError:
    from d.e.f import d as e''')

# Generated at 2022-06-14 01:50:24.179792
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import typed_ast.ast3 as ast
    from typed_ast.transforms.import_rewrite import BaseImportRewrite
    from typed_ast.transforms import CompilationTarget
    from typed_ast import ast3 as ast

    class MyImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PY26
        rewrites = [('typed_ast', '_ast27')]

    result = MyImportRewrite.transform(
        ast.parse(
            'from typed_ast import ast3\n'
            'from typed_ast.transforms import import_rewrite\n'
            'from typed_ast.ast3 import parse, Import\n'))

    assert result.changed is True
    assert result.dependencies == ['_ast27']


# Generated at 2022-06-14 01:50:36.194049
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils.codegen import GeneratedCode

    from_ = '__future__'
    to = 'asyncio'

    f = functools.partial(BaseImportRewrite._replace_import, from_=from_, to=to)


# Generated at 2022-06-14 01:50:46.722685
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typed_ast.ast3 as ast
    import astor
    code = 'from foo import bar as baz; import foo; from foo import *'
    tree = astor.parse_file(code)

    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    transformer = TestTransformer(tree)
    new_tree = transformer.visit(tree)

    expected = 'try:\n    from bar import bar as baz\n    import bar\n    from bar import *\nexcept ImportError:\n    from foo import bar as baz\n    import foo\n    from foo import *'
    assert astor.to_source(new_tree) == expected

# Generated at 2022-06-14 01:50:53.810318
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Foo(BaseImportRewrite):
        rewrites = [('first', 'second')]

    import_from = ast.parse("from first import a as b").body[0]
    result = Foo().visit(import_from)
    assert isinstance(result, ast.Try)
    assert result.body[0].body[0].names[0].name == 'second.a'
    assert result.body[0].body[0].names[0].asname == 'b'



# Generated at 2022-06-14 01:51:18.775862
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformImportFrom(BaseImportRewrite):
        rewrites = [('form', 'to')]

    node = ast.parse('from form import *')
    TestTransformImportFrom.transform(ast.Module(body=[node]))
    assert TestTransformImportFrom._tree_changed
    assert 'from to import *' in ast.dump(node)



# Generated at 2022-06-14 01:51:23.427454
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node = ast.parse("from fake_module import bar, baz as foo").body[0]
    BaseImportRewrite.rewrites = [
        ('fake_module', 'real_module')
    ]
    node = BaseImportRewrite.transform(node).tree
    print(node.lineno)
    print(ast.dump(node))

# Generated at 2022-06-14 01:51:32.824143
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .. import py2
    from ..utils import dump

    @py2.register_rewrite('test_module')
    class TestRewrite(BaseImportRewrite):
        rewrites = [('test_module', 'new_module')]

    source = """
    # Imports
    import test_module
    """

    expected = """
    # Imports
    try:
        import test_module
    except ImportError:
        import new_module
    """

    tree = ast.parse(source)
    transformed = TestRewrite.transform(tree).tree
    assert dump(transformed) == expected



# Generated at 2022-06-14 01:51:46.333686
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import test_utils
    import ast_transformer
    import transformers

    source = 'import foo'
    tree = ast.parse(source)
    BaseImportRewrite(tree).visit(tree)
    expected_source = 'try:\n    import foo\nexcept ImportError:\n    import test_utils.foo'
    assert ast_transformer.unparse(tree) == expected_source

    source = 'import foo'
    tree = ast.parse(source)
    BaseImportRewrite.transform(tree)
    expected_source = 'try:\n    import foo\nexcept ImportError:\n    import transformers.foo'
    assert ast_transformer.unparse(tree) == expected_source

    source = 'from os import path'
    tree = ast.parse(source)
    BaseImportRewrite.transform(tree)


# Generated at 2022-06-14 01:51:49.522515
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    node = ast.parse('import typing')
    cls = BaseImportRewrite(node)
    transform = cls.transform(node)
    assert transform == TransformationResult(ast.parse('import typing'), False, [])



# Generated at 2022-06-14 01:51:56.730280
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import utils.snippet
    utils.snippet.Scope.set_current(utils.snippet.Scope.Module)
    old_name = ast.Import(names=[ast.alias(name='name',asname=None)])
    new_name = ast.Import(names=[ast.alias(name='old_name',asname=None)])
    body = BaseImportRewrite._replace_import(expected_result,old_name,new_name)
    tree = ast.parse(body)
    assert isinstance(tree, ast.Try)


# Generated at 2022-06-14 01:52:06.777785
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("""from foo import bar""")
    inst = BaseImportRewrite(ast.parse(""))
    inst.rewrites = [("foo", "baz")]
    assert ast.dump(inst.visit(ast.parse("from foo import bar"))) == \
        ast.dump(ast.parse("""
try:
    from foo import bar
except ImportError: 
    from baz import bar
        """))
    assert ast.dump(inst.visit(ast.parse("from foo import a"))) == \
        ast.dump(ast.parse("""
try:
    from foo import a
except ImportError: 
    from foo import a
        """))

# Generated at 2022-06-14 01:52:17.913063
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # original code
    original_code = """
        from os import path, stat

        from six import string_types as strings
    """

    # code after transformation
    transformed_code = """
        try:
            from os import path, stat
        except ImportError:
            from os import path, stat


        try:
            from six import string_types as strings
        except ImportError:
            from six import string_types as strings
    """

    # rewrites from os -> six
    rewrites = [('os', 'six')]

    # create transformer
    transformer = BaseImportRewrite(rewrites=rewrites)

    # parse code
    tree = ast.parse(original_code)

    # do transformation
    transformed_tree = transformer.visit(tree)

    # check if tree was changed
    assert transformer._tree_

# Generated at 2022-06-14 01:52:25.807951
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import _ast
    from .base import get_visitor

    visitor = get_visitor(BaseImportRewrite)
    # With import module rewrote
    input_tree = _ast.Module([
        _ast.Import([_ast.alias(name='io.StringIO',
                                asname='StringIO')])])


# Generated at 2022-06-14 01:52:40.492166
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import sys
    if sys.version_info.major != 3:
        assert False


# Generated at 2022-06-14 01:53:11.414538
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import Module as Module
    from typed_ast.ast3 import Import as Import
    from typed_ast.ast3 import ImportFrom as ImportFrom
    from typed_ast.ast3 import alias as alias
    from typed_ast.ast3 import Try as Try
    
    from .test_utils import get_test_data
    from .test_utils import run_test_node
    
    test_data = get_test_data()
    
    module_node = parse(test_data.get_import_rewrite_node())
    

# Generated at 2022-06-14 01:53:21.175468
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..types import CompilationTarget
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet, extend
    from ..utils import get_code
    from mypy_extensions import TypedDict
    from .base_transformer import BaseTransformer, BaseNodeTransformer, import_rewrite
    from typing import List, Tuple, Union, Optional, Iterable, Dict
    from abc import ABCMeta, abstractmethod


    class BaseImportRewrite(BaseNodeTransformer):
        rewrites = []  # type: List[Tuple[str, str]]

        def _get_matched_rewrite(self, name: Optional[str]) -> Optional[Tuple[str, str]]:
            """Returns rewrite for module name."""
            if name is None:
                return None


# Generated at 2022-06-14 01:53:27.578126
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import typed_ast.ast3 as ast

    class MyTransformer(BaseImportRewrite):
        rewrites = [
            ('module1', 'module2')
        ]

    node = ast.parse('import module1')
    result = MyTransformer.transform(node)
    print(astor.to_source(result.tree))
    assert astor.to_source(result.tree) == "try:\n    import module1\nexcept ImportError:\n    import module2"



# Generated at 2022-06-14 01:53:39.267090
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_statement = ast.parse('import module').body[0]  # type: ignore

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('module', 'new_module')]

    assert TestTransformer._replace_import(TestTransformer(None), *TestTransformer.rewrites[0]) == \
        ast.parse(
            'try:\n'
            '    import module'
            'except ImportError:\n'
            '    import new_module').body[0]  # type: ignore

    assert TestTransformer.transform(import_statement).tree == \
        ast.parse(
            'try:\n'
            '    import module'
            'except ImportError:\n'
            '    import new_module').body[0]  # type: ignore

    # Test that not matched module will

# Generated at 2022-06-14 01:53:43.337951
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse("import test")
    expected = ast.parse("""try:
    import test
except ImportError:
    import test
""")
    result = BaseImportRewrite(tree).visit(tree)
    assert ast.dump(result) == ast.dump(expected)



# Generated at 2022-06-14 01:53:53.349375
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('kazoo', 'boo'),
            ('boo.baz', 'boo.maz')
        ]
