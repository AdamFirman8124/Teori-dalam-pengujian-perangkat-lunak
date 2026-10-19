

# Generated at 2022-06-14 01:44:18.082067
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import compare_ast

    source = '''
from foo import bar
from baz import quux
from foo import quux
from baz import bar
from foo import bar as barfoo
from baz import bar as barbaz
    '''

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'newfoo')]


# Generated at 2022-06-14 01:44:28.343067
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [('some.module', 'other.module')]

    node = ast.Import(names=[
        ast.alias(name='some.module', asname='s'),
        ast.alias(name='some.module.function', asname='f'),
        ast.alias(name='some.module.function.name', asname='n')])

    import_rewrite = Test.transform(node)

# Generated at 2022-06-14 01:44:37.456100
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Target(BaseImportRewrite):
        target = 'target'
        rewrites = [('a', 'b')]

    tree = ast.parse('''
import a
import c
import b.a as aa
''')
    expected_tree = ast.parse('''
try:
    import a
except ImportError:
    import b
import c
try:
    import b.a as aa
except ImportError:
    import b.b as aa
    ''')
    Target.transform(tree)
    assert ast.dump(tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 01:44:49.115753
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('import_this', 'antigravity')]
        dependencies = ['import_this']

    assert TestImportRewrite.dependencies[0] == 'import_this'
    assert TestImportRewrite.rewrites[0][0] == 'import_this'

    node = ast.ImportFrom(module='import_this',
                          names=['import_this'],
                          level=0)

    result = TestImportRewrite.transform(ast.parse('\n')).tree
    rewrote = TestImportRewrite.visit_ImportFrom(TestImportRewrite(result), node)

    assert isinstance(rewrote, ast.Try)
    assert isinstance(rewrote.body[0], ast.ImportFrom)
    assert rewrote.body[0].module

# Generated at 2022-06-14 01:44:55.575284
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import re
    from typed_ast import ast3 as ast

    #
    # https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
    import sys
    import resource
    resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
    sys.setrecursionlimit(10**6)

    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('typed_ast.conversions.ast3', 'my_typed_ast.conversions.ast3')]


# Generated at 2022-06-14 01:45:05.848894
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # case 1:
    # node.names[0].name is None
    node = ast.Import(names=[ast.alias(name=None, # type: ignore
                                       asname='foo')])
    result = BaseImportRewrite(None).visit_Import(node)
    assert result == node

    # case 2:
    # node.names[0].name is not None and node.names[0].name does not start with from_
    node = ast.Import(names=[ast.alias(name='foo',
                                       asname='foo')])
    result = BaseImportRewrite(None).visit_Import(node)
    assert result == node

    # case 3:
    # node.names[0].name is not None and node.names[0].name starts with from_
    from_ = 'foo'

# Generated at 2022-06-14 01:45:10.363315
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import sys

    sys.modules.pop('typing', None)

    source = inspect.cleandoc("""
        from typing import Text, List
        from six.moves import urllib
        
        a = Text('')
        b = List[int]()
        c = urllib.parse.urlparse('')
    """)

    tree = astor.parse_file(StringIO(source))
    tree = BaseImportRewrite.transform(tree).tree

# Generated at 2022-06-14 01:45:21.132410
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    code = 'import os'

    assert astor.to_source(BaseImportRewrite([('os', 'macos')]).visit(ast.parse(code))) == 'try:\n    import os\nexcept ImportError:\n    import macos\n'

    code = 'import os.path'

    assert astor.to_source(BaseImportRewrite([('os', 'macos')]).visit(ast.parse(code))) == 'try:\n    import os.path\nexcept ImportError:\n    import macos.path\n'

    code = 'import os.path.join'


# Generated at 2022-06-14 01:45:31.329130
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import ast_utils
    import ast as ast3
    import_from = ast3.parse(
        'from a.b import c, d, e as f, g, h').body[0]
    node_transformer = BaseImportRewrite(ast3.parse('pass'))
    # Test 1

# Generated at 2022-06-14 01:45:36.865915
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Testrewrite(BaseImportRewrite):
        rewrites = [
            ('a', 'b')
        ]

    original = ast.parse('import x')
    expected = ast.parse('''
try:
    import x
except ImportError:
    import b as x
''')

    assert Testrewrite.transform(original).tree == expected

    original = ast.parse('import x as y')
    expected = ast.parse('''
try:
    import x as y
except ImportError:
    import b as y
''')

    assert Testrewrite.transform(original).tree == expected

    original = ast.parse('import a')
    expected = ast.parse('import b')

    assert Testrewrite.transform(original).tree == expected

    original = ast.parse('import a as b')
    expected = ast

# Generated at 2022-06-14 01:45:52.006637
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Test 1: given import statement will not be changed
    rewritten_class = BaseImportRewrite()
    import_statement = 'import requests'
    import_ast = ast.parse(import_statement).body[0]
    rewritten = rewritten_class.visit_Import(import_ast)
    assert isinstance(rewritten, ast.Import)
    assert rewritten == import_ast

    # Test 2: given import statement will be replaced with two import statements
    rewritten_class = BaseImportRewrite()
    rewritten_class.rewrites = [('requests', 'test_test')]
    import_statement = 'import requests'
    import_ast = ast.parse(import_statement).body[0]
    rewritten = rewritten_class.visit_Import(import_ast)
    assert isinstance(rewritten, ast.Try)

# Generated at 2022-06-14 01:46:02.266505
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    class MockTransformer(BaseImportRewrite):
        rewrites = [
            ('mock1', 'mock2')
        ]

    import_from = ast.ImportFrom(module='mock1', names=[
        ast.alias(name='Foo', asname='Bar'),
        ast.alias(name='Baz')],
        level=0)


# Generated at 2022-06-14 01:46:12.638654
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as pyast
    from ast import parse
    from ..utils.ast import unwrap_ast

    class TestTransformer(BaseImportRewrite):
        source = 'import smtplib'
        target = CompilationTarget.METAPYTHON

        rewrites = [('smtplib', 'smtp')]

    result = unwrap_ast(TestTransformer.transform(parse(TestTransformer.source)).tree)
    assert result == pyast.parse('try:\n    import smtplib\nexcept:\n    import smtp')

    class TestTransformer(BaseImportRewrite):
        source = 'import sys'
        target = CompilationTarget.METAPYTHON

        rewrites = [('smtplib', 'smtp')]


# Generated at 2022-06-14 01:46:21.840605
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    primary_nodes = [
        ast.Import([ast.alias(name='glob', asname='glob')]),
        ast.Import([ast.alias(name='os', asname=None)]),
        ast.Import([ast.alias(name='__future__', asname=None)]),
        ast.Import([ast.alias(name='os.path', asname='path')])
    ]

    for primary in primary_nodes:
        secondary = ast.Import([ast.alias(name='some.other', asname=None)])

        class ModuleImportRewrite(BaseImportRewrite):
            rewrites = [
                ('os', '_os'),
                ('os.path', '_os.path')
            ]

        module_rewriter = ModuleImportRewrite(secondary)

# Generated at 2022-06-14 01:46:30.550452
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import astor
    from textwrap import dedent

    class ImportTransformer(BaseImportRewrite):
        rewrites = [('dto', 'entity')]

    t = ast.parse(dedent('''
        from dto import *
        import dto
    '''))

    ImportTransformer.transform(t)

    assert astor.to_source(t) == dedent('''
        try:
            from entity import *
        except ImportError:
            from dto import *
        try:
            import entity
        except ImportError:
            import dto
    ''').strip()



# Generated at 2022-06-14 01:46:44.957713
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('os', 'six.moves.os'), 
            ('copy', 'copy'), 
            ('copy.deepcopy', 'copy.deepcopy')
        ]
    src = '''
from copy import copy
from copy import deepcopy
import os
    '''
    expected = '''
try:
    from copy import copy
except ImportError:
    from copy import copy
try:
    from copy import deepcopy
except ImportError:
    from copy.deepcopy import deepcopy
try:
    import os
except ImportError:
    import six.moves.os as os
    '''
    tree = ast.parse(src)
    TestBaseImportRewrite().transform(tree)
    result = astor.to_source

# Generated at 2022-06-14 01:46:55.349961
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import tempfile
    import os
    import sys
    import contextlib
    import shutil

    @contextlib.contextmanager
    def library_exists(module_name: str) -> Iterable[str]:
        package_name = module_name.rsplit('.', 1)[0]
        module_name = module_name.rsplit('.', 1)[1]


# Generated at 2022-06-14 01:47:07.941374
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        target = 'python36'
        rewrites = [
            ('six', 'six3'),
            ('six3', 'six33'),
        ]

    tree = ast.parse("""
from six import binary_divmod
import six
from six.moves import input
from six import *
""")

    tt = TestTransformer(tree)
    tt.visit(tree)

# Generated at 2022-06-14 01:47:23.108745
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import typed_ast.ast3 as ast
    from typed_ast.transforms.rewrites.utils import get_node

    class TestTransformer(BaseImportRewrite):
        target = 'Python-3.8'
        rewrites = [('old_module', 'new_module')]

    class Test(unittest.TestCase):
        def test_simple(self):
            node = get_node('from old_module import a')
            new_node = TestTransformer.transform(node).tree
            assert isinstance(new_node, ast.Try)

            handler = new_node.handlers[0]
            assert isinstance(handler.type, ast.Name)
            assert handler.type.id == 'ImportError'

            assert isinstance(new_node.body[0], ast.ImportFrom)

# Generated at 2022-06-14 01:47:31.888632
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    bmp = BaseNodeTransformer
    tree = ast.parse("from foo.bar import Hello")
    inst = bmp(tree)
    res = inst.visit(tree)
    assert isinstance(res, ast.Try)
    assert isinstance(res.body[1], ast.ImportFrom)
    assert res.body[1].module == "foo.bar"
    assert res.body[1].names[0].name == "Hello"
    assert res.body[0].body[0].name == "foo"
    assert res.body[1].names[0].name == "Hello"
    assert res.body[1].names[0].name == "Hello"
    assert res.body[0].body[0].name == "foo"

# Generated at 2022-06-14 01:47:50.210784
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    base_import_rewrite = BaseImportRewrite()
    module = 'a.b'
    node = ast.ImportFrom(module, [], 0)
    result = base_import_rewrite.visit(node)
    assert result.__class__ == ast.ImportFrom
    assert base_import_rewrite._tree_changed == False

    node = ast.ImportFrom('a.b', [], 0)
    result = base_import_rewrite.visit(node)
    assert result.__class__ == ast.ImportFrom
    assert base_import_rewrite._tree_changed == False

    node = ast.ImportFrom('os.sys', [], 0)
    result = base_import_rewrite.visit(node)
    assert result.__class__ == ast.ImportFrom
    assert base_import_rewrite._tree

# Generated at 2022-06-14 01:47:59.858995
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import interpreter.codetransformer # Defined by PyFlakes
    import six # Defined by PyFlakes

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_3
        rewrites = [
            ('interpreter.codetransformer', 'interpreter.compiler')
        ]


    input_tree = ast.parse('''
        from interpreter import codetransformer, six
        from . import a
        from interpreter.codetransformer import test
        from interpreter.codetransformer import *
        from interpreter.codetransformer import a as b
        from interpreter.codetransformer.test import a, b
        from interpreter.codetransformer.test import *
        from interpreter.codetransformer.test import a as b
    ''')
    expected_

# Generated at 2022-06-14 01:48:10.525346
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    t = BaseImportRewrite(ast.parse(''))


# Generated at 2022-06-14 01:48:20.817314
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    import astor
    import typed_astunparse
    from typed_ast.ast3 import parse as parse_ast

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('in1', 'out1'),
                    ('in2', 'out2'),
                    ('in3', 'out3')]

    class MyTests(unittest.TestCase):
        def _test_transform(self, input, expected_output):
            tree = parse_ast(input)
            transformed_tree, tree_changed, _ = TestBaseImportRewrite.transform(tree)
            self.assertEqual(tree_changed, True)
            self.assertEqual(typed_astunparse.unparse(transformed_tree), expected_output)


# Generated at 2022-06-14 01:48:30.689244
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # import
    import_node = ast.Import(names=[ast.alias(name='foo')])

    # import foo
    import_node_foo = ast.Import(names=[ast.alias(name='foo')])

    # import foo as bar
    import_node_foo_as_bar = ast.Import(names=[ast.alias(name='foo', asname='bar')])

    # import foo.bar
    import_node_foo_dot_bar = ast.Import(names=[ast.alias(name='foo.bar')])

    # import foo.bar as bar
    import_node_foo_dot_bar_as_bar = ast.Import(names=[ast.alias(name='foo.bar', asname='bar')])

    # from . import foo

# Generated at 2022-06-14 01:48:36.999854
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Given
    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ('old', 'new')
        ]

    import_rewrite = ast.Import(names=[ast.alias(
        name='old',
        asname='old')])

    # When
    import_rewrite_t = ImportRewrite.transform(import_rewrite)

    # Then
    assert import_rewrite_t.transformed_tree == import_rewrite_t.tree
    assert import_rewrite_t.changed



# Generated at 2022-06-14 01:48:47.519104
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..typing_compatibility import is_python_26
    import_from = ast.parse("from collections import namedtuple").body[0]
    import_from_with_alias = ast.parse("from collections import namedtuple as nt").body[0]
    import_from_with_alias_again = ast.parse("from collections import namedtuple as nt, defaultdict").body[0]
    import_from_with_double_alias = ast.parse("from collections import namedtuple as nt, defaultdict as dd").body[0]
    import_from_with_triple_alias = ast.parse("from collections import namedtuple, defaultdict as dd, OrderedDict as od").body[0]

# Generated at 2022-06-14 01:48:53.318335
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    class C(BaseImportRewrite):
        rewrites = [('pandas', 'pandas_sw')]

    tree = ast.parse('import pandas\n')
    expected_tree = ast.parse('try:\n    import pandas\nexcept ImportError:\n    import pandas_sw')

    result = C.transform(tree)
    assert result.tree == expected_tree


# Generated at 2022-06-14 01:49:02.973801
# Unit test for method visit_ImportFrom of class BaseImportRewrite

# Generated at 2022-06-14 01:49:14.325174
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.snippet import to_source
    from ..utils.node import unparse, parse

    code = 'from foo.bar import baz, qux'
    node = parse(code)
    node_extended = parse(code)

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('foo.bar', 'foo.bar.baz')]

    # import will be replaced with `try/except` around nodes with new imports
    node_transformed = ImportRewrite().visit(node)
    assert isinstance(node_transformed.body[0], ast.Try)
    assert isinstance(node_transformed.body[0].body[0], ast.ImportFrom)

# Generated at 2022-06-14 01:49:36.551114
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..codegen import to_source
    from ..utils.import_rewrites import numpy_rewrites
    import astor
    import ast

    class ImportNumpyRewrite(BaseImportRewrite):
        rewrites = numpy_rewrites

    simple_import = ast.parse('''
    import numpy as np
    ''').body[0]
    transformed = to_source(ImportNumpyRewrite.transform(simple_import)[0],
                            with_indentation=False)
    check_import = astor.code_to_ast('''
    try:
        import numpy as np
    except ImportError:
        import cupy as np
    ''').body[0]
    assert astor.to_source(transformed) == astor.to_source(check_import)

    import_

# Generated at 2022-06-14 01:49:45.014960
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.ast import (
        load,
        dump,
        compare_asts,
    )
    from ..utils.source import get_source
    from .six import six
    from .unittest_backport import mock

    expected_source = get_source(six.__file__)
    expected_ast = load(expected_source)
    mock.patch('__builtin__.open', mock.mock_open(read_data=expected_source), create=True).start()

    class TestTransformer(BaseImportRewrite):
        target = six.python2

        rewrites = [
            ('__builtin__', 'builtins'),
            ('six.moves', 'six.moves.py27'),
        ]


# Generated at 2022-06-14 01:49:53.259206
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ('import1', 'import2')
        ]

    # before
    import1  # type: ignore
    import import1

    # after
    try:
        import import1
    except ImportError:
        import import2

    code = inspect.getsource(test_BaseImportRewrite_visit_Import)
    tree = ast.parse(code)
    result = ImportRewrite.transform(tree)

    assert result.tree_changed
    assert len(result.dependencies) == 1
    assert result.dependencies[0] == 'import2'


# Generated at 2022-06-14 01:50:01.028277
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    code = 'from django.forms import Select as S'
    tree = ast.parse(code)

    class Transformer(BaseImportRewrite):
        rewrites = [('django.forms', 'wtforms.fields')]

    Transformer.transform(tree)
    assert astor.to_source(tree) == """
try:
    from django.forms import Select as S
except ImportError:
    from wtforms.fields import Select as S
"""

# Generated at 2022-06-14 01:50:11.177131
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import compare_source
    from .six import PY3, PY36, PY37

    from .. import ast, transformations

    source = """
        import test.test_support
        import test_importlib
        import unittest.case
    """

    tree = ast.parse(source, target=PY3)
    transformations.ImportRewrite().visit(tree)
    result = transformations.to_source(tree)
    expected = """
    try:
        import test.test_support
    except ImportError:
        import test.test_support
    try:
        import test_importlib
    except ImportError:
        import test_importlib
    try:
        import unittest.case
    except ImportError:
        import unittest.case
    """
    compare_source(result, expected)

# Generated at 2022-06-14 01:50:21.669179
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    @snippet
    def tree():
        import scipy.io as io  # this import should not be changed
        import re  # this import should not be changed
        import requests  # should be changed to urllib.request
        from a.b import m1, m2, m3  # should be changed to m3
        from a.b.m3 import v1  # should be changed to v2
        from a.b.m3 import v2  # should be changed to v2
        from a.b.m4 import m5 as mkk  # should be changed to c.m4.m5
        from c.m4 import m5  # should be changed to c.m4.m5
        from c.m6.m7 import m8  # should be changed to c.m6.m9

# Generated at 2022-06-14 01:50:29.188078
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    # Simple case
    source = 'from functools import lru_cache'
    expected = 'from fastcache import lru_cache'
    body = [ast.parse(source).body[0]]
    body[0].names.append(ast.alias(name='lru_cache',
                                   asname='cache'))
    expected = ast.parse(expected).body[0]

    rewriter = BaseImportRewrite(ast.Module(body))
    rewriter.rewrites = [('functools', 'fastcache')]
    result = rewriter.visit(body[0])

    assert astor.to_source(result) == astor.to_source(expected)

    # Import from with aliasing different names
    source = 'from functools import lru_cache, partial'

# Generated at 2022-06-14 01:50:39.582597
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import typed_ast.ast3 as ast

    import typedtransforms.transformers as transformers

    class TestImportRewrite(transformers.BaseImportRewrite):
        rewrites = [
            ('mock.mock', 'unittest.mock'),
        ]


# Generated at 2022-06-14 01:50:50.945917
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    source = """\
import a
import a as a_
from b import c
import d.e as e_
import f.g.h as h_"""  # noqa

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('a', 'newa'),
            ('b.c', 'newb.c'),
            ('d', 'newd'),
        ]

    tree = ast.parse(source)
    transformer = TestTransformer(tree)

    assert transformer.visit_Import(
        ast.parse('import a').body[0]
    ).test.left.value.names[0].name == 'newa'


# Generated at 2022-06-14 01:51:01.263027
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    class MyTransformer(BaseImportRewrite):
        rewrites = [('six.moves', 'six.moves3k')]

    import_from = ast.ImportFrom(
        module='six.moves',
        names=[ast.alias(
            name='range',
            asname='range'),
            ast.alias(
                name='map',
                asname='map')],
        level=0)

    result = MyTransformer.transform(import_from)

    assert result.changed
    assert result.tree.body[0].names[0].name == 'range'
    assert result.tree.body[0].names[1].name == 'map'
    assert result.tree.body[0].names[0].asname == 'range'

# Generated at 2022-06-14 01:51:26.675032
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    foo = ast.ImportFrom(module='foo.bar',
                         names=['some',
                                'other'],
                         level=0)
    baz = ast.ImportFrom(module='baz',
                         names=[ast.alias(name='some', asname='other')],
                         level=0)

    ast.fix_missing_locations([foo, baz])

    import_rewrite_transformer = BaseImportRewrite(foo)
    import_rewrite_transformer.visit = lambda x: x  # noqa: E731
    import_rewrite_transformer.rewrites = [('foo.bar', 'bar')]

    result = import_rewrite_transformer.visit_ImportFrom(foo)
    assert isinstance(result, ast.Try)
    assert len(result.body) == 1
   

# Generated at 2022-06-14 01:51:37.870484
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    node = ast.parse(
        'import datetime as dt\n'
        'from base.datetime import date, datetime as dt\n'
        'from base.util import name\n'
        'from base.datetime import *\n'
        'from base import util as u')

    class Transformer(BaseImportRewrite):
        rewrites = [('base.datetime', 'jellysnake.datetime')]

    result = Transformer(node).visit(node)
    assert result.body[0].lineno == 1
    assert result.body[1].lineno == 2
    assert astor.to_source(result.body[2]) == 'from base.util import name\n'
    assert result.body[3].lineno == 4
    assert result.body

# Generated at 2022-06-14 01:51:49.619438
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class MyImportRewrite(BaseImportRewrite):
        rewrites = [
            ('os', 'system'),
            ('sys', 'system'),
        ]

    class ImportRewriteTest(BaseNodeTransformer):
        def visit_Import(self, node):
            return MyImportRewrite.visit_Import(self, node)

    tree = ast.parse("import os")
    new_tree = ImportRewriteTest.transform(tree)
    assert new_tree == ast.parse("""
try:
    import os
except ImportError:
    import system as os
""")

    tree = ast.parse("import sys.path")
    new_tree = ImportRewriteTest.transform(tree)

# Generated at 2022-06-14 01:51:59.739289
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    """
    Testing visit_Import method of BaseImportRewrite class
    """
    rewrites = [('a', 'b')]
    transformed_node = BaseImportRewrite.visit_Import(None, ast.Import(names=[ast.alias(name='a', asname=None)]), rewrites)
    assert isinstance(transformed_node, ast.Try)
    assert transformed_node.body[0].names[0].name == 'b'
    assert transformed_node.body[0].names[0].asname == None
    assert [] == transformed_node.orelse
    assert len(transformed_node.excepts) == 1
    assert 'ImportError' == transformed_node.excepts[0].type.id
    assert transformed_node.excepts[0].name.id == 'e'

    rewrites

# Generated at 2022-06-14 01:52:09.095103
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typed_ast.ast3 as ast
    import src.transforms.base as base
    class ExampleTransformer(base.BaseImportRewrite):
        rewrites = [('six', 'six.moves')]
        dependencies = []

    tree = ast.parse('from six import print_\n')
    ExampleTransformer.transform(tree)
    assert str(tree) == 'from six.moves import print_\n'

    tree = ast.parse('from six import print_, range\n')
    ExampleTransformer.transform(tree)
    assert str(tree) == 'try:\n\tfrom six import print_, range\nexcept ImportError:\n\tfrom six.moves import print_, range\n'

    tree = ast.parse('from six.moves import print_, range\n')
    ExampleTrans

# Generated at 2022-06-14 01:52:19.838358
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from_ = 'unittest'
    to = 'unittest2'
    module_name = 'unittest.mock'
    import_as = 'mock'

    tree = ast.parse('''\
import unittest.mock as mock
''')
    cls = type('cls', (BaseImportRewrite,), {
        'rewrites': [(from_, to)],
    })
    result = cls.transform(tree)


# Generated at 2022-06-14 01:52:26.676206
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tr = BaseImportRewrite({'rewrites': [('a', 'b')]})
    # import from a
    assert tr.visit(ast.parse('import a').body[0]) == ast.parse("""
try:
    import a
except ImportError:
    import b
""")
    # import from a as b
    assert tr.visit(ast.parse('import a as b').body[0]) == ast.parse("""
try:
    import a as b
except ImportError:
    import b as b
""")
    # from a import b
    assert tr.visit(ast.parse('from a import b').body[0]) == ast.parse("""
try:
    from a import b
except ImportError:
    from b import b
""")
    # from a import b as c
    assert tr

# Generated at 2022-06-14 01:52:40.769045
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("""
from cffi import FFI
import cffi
from cffi.model import _cffi_backend as backend
cffi.FFI.verify(backend.new_verifier()) 
""")
    # from cffi import FFI
    # import cffi
    # from cffi.model import _cffi_backend as backend
    # cffi.FFI.verify(backend.new_verifier()) 
    # cffi.cdef("""
    # """)

    class Transformer(BaseImportRewrite):
        rewrites = [('cffi', 'fake_cffi')]
        dependencies = ['fake_cffi']

    res = Transformer.transform(tree)

    assert res.rewritten
    assert res

# Generated at 2022-06-14 01:52:54.723961
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    test_src = '''
import os
import sys
'''
    test_expected = '''try:
    import os
except ImportError:
    import posixpath as os
try:
    import sys
except ImportError:
    import _sys as sys
'''
    from ..types import CompilationTarget
    from . import Python3toIronPython3

    transpiler = Python3toIronPython3.Python3toIronPython3(CompilationTarget.CODE)
    transpiler.rewrites = [('os', 'posixpath')]
    test_src_ast = ast.parse(test_src)
    test_transformed = transpiler.visit(test_src_ast)
    test_expected_ast = ast.parse(test_expected)
    assert ast.dump(test_transformed) == ast.dump

# Generated at 2022-06-14 01:53:01.816418
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_tree = ast.parse('import foo').body[0]  # type: ast.AST
    class Rewriter(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
    rewrote_tree = Rewriter.visit(import_tree)
    assert isinstance(rewrote_tree, ast.Try)
    rewrote_tree = ast.fix_missing_locations(rewrote_tree)
    assert ast.dump(rewrote_tree) == 'try:\n    import bar\nexcept ImportError:\n    import foo\n'



# Generated at 2022-06-14 01:53:25.793421
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import(): # noqa
    from ..utils.compiler import Compiler

    compiler = Compiler.get_compiler('Py2_2')

    class MyNodeTransformer(BaseImportRewrite):
        rewrites = [('unittest', 'my_unittest')]


# Generated at 2022-06-14 01:53:31.149700
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_rewrite(previous=ast.Import(names=[
        ast.alias(name='foo',
                  asname='foo')]),
        current=ast.Import(names=[
            ast.alias(name='bar',
                      asname='foo')]))



# Generated at 2022-06-14 01:53:39.088726
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from .simple import simple_transformer

    code = astor.to_source(ast.parse("from a.b.c import d as e"))
    np_tran = simple_transformer.NPTransformer(ast.parse(code))
    tree2 = np_tran.visit()

    assert astor.to_source(tree2) == """\
try:
    from a.b.c import d as e
except ImportError:
    from a.b.c import d as e"""


# Generated at 2022-06-14 01:53:46.166931
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from_str = '''from six.moves import map, range'''
    import_from = ast.parse(import_from_str).body[0]
    assert isinstance(import_from, ast.ImportFrom)

    import_from_rewrite_str = '''try:
    from six.moves import map, range
except ImportError:
    from six import map, range
'''
    import_from_rewrite = ast.parse(import_from_rewrite_str).body[0]
    assert isinstance(import_from_rewrite, ast.Try)

    class Rewriter(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]
    rewrite_result, tree_changed, dependencies = Rewriter.transform(import_from)
    assert tree_changed

# Generated at 2022-06-14 01:53:55.185693
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():  # noqa: F811
    def assert_result(before, after):
        tree = ast.parse(before)
        cls = BaseImportRewrite(tree)
        cls._tree_changed = False

        result = cls.visit(tree)

        assert result == ast.parse(after), "expected {} but got {}".format(
            after, ast.dump(result))
        assert cls._tree_changed, "expected tree to be changed"
        assert cls.dependencies == [], "expected no dependencies"

    assert_result("""
import sys
import os

print(os.path.abspath('.'))
""", """
import sys
try:
    import os
except ImportError:
    import pathlib as os

print(os.path.abspath('.'))
""")

    assert_