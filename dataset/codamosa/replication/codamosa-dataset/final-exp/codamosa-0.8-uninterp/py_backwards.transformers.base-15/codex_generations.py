

# Generated at 2022-06-14 01:44:11.399935
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import os
    import astor
    import unittest

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('test_module', 'other_name')]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._tree_changed = False

    class TestCase(unittest.TestCase):
        def test_1(self):
            import test_module as a
            import test_module.other_name as b
            import test_module.some_func
            from test_module import *
            from test_module.other_name import *
            from test_module.other_name import some_func
            from test_module import some_func

            def f():
                pass


# Generated at 2022-06-14 01:44:21.110632
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(
        module='foo.bar',
        names=[
            ast.alias(name='baz', asname=None),
            ast.alias(name='dummy', asname=None)
        ],
        level=0)


# Generated at 2022-06-14 01:44:33.066642
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import body
    import os


# Generated at 2022-06-14 01:44:40.068275
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Transformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse("""
    import mymodule
    from mymodule import myclass
    from mymodule.foo import Something
    from mymodule.foo import *
    from mymodule.foo.baz import SomethingElse
    from mymodule.foo.baz.bar import SomethingElse
    from mymodule2 import *
    """)
    # Should produce output with no errors
    Transformer.transform(tree).tree



# Generated at 2022-06-14 01:44:46.732636
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_node = ast.parse("""
    import boto
    """).body[0]  # type: ast.Import

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('boto', 'moto')]

    
    assert TestImportRewrite.transform(import_node).changed
    assert TestImportRewrite.transform(import_node).tree.body[0].body[0].names[0].name == 'moto'



# Generated at 2022-06-14 01:45:00.196248
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import parse

    class Rewriter(BaseImportRewrite):
        rewrites = [
            ('base', 'rewritten_base')
        ]

    body = [
        ast.ImportFrom(module='base',
                       names=[ast.alias(name='test')],
                       level=0),
        ast.ImportFrom(module='base.test',
                       names=[ast.alias(name='test')],
                       level=0),
    ]

    tree = parse(content=body)
    res = Rewriter.transform(tree=tree)
    assert str(tree) == "try:\n    import rewritten_base\nexcept ImportError:\n    import base\nexcept ImportError:\n    import base.test\n"

# Generated at 2022-06-14 01:45:10.781850
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.fixtures import ast_Import
    from ..utils.fixtures import ast_Try
    import ast as myast

    transformer = BaseImportRewrite()

    # assert that method generic_visit is called correctly when no import to rewrite
    assert transformer.visit(ast_Import) == ast_Import

    # assert that method _replace_import works correctly for direct import
    transformer.rewrites = [('os', 'myos')]
    assert transformer.visit(ast_Import) == ast_Try

    # assert that method _replace_import works correctly for submodule import
    transformer.rewrites = [('os.path', 'myos.path')]
    assert transformer.visit(ast_Import) == ast_Try


# Generated at 2022-06-14 01:45:21.617466
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    class Transformer(BaseImportRewrite):
        rewrites = [('a', 'b')]

        def visit_ImportFrom(self, node: ast.ImportFrom) -> Union[ast.ImportFrom, ast.Try]:
            return super().visit_ImportFrom(node)

    code = """
    from a.a import a, b as d
    from a import a as c, d
    import a.a
    """

    transform_result = Transformer.transform(ast.parse(code))
    assert transform_result.changed == True


# Generated at 2022-06-14 01:45:30.661831
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransform(BaseImportRewrite):
        target = CompilationTarget('test', 'test')

    source = '''
    import test
    import foolib.foo
    '''
    tree = ast.parse(source)

    TestTransform.rewrites = [('foolib', 'test')]
    TestTransform.transform(tree)

    expected_source = '''
    import test
    try:
        import foolib.foo
    except ImportError:
        import test.foo
    '''
    expected_tree = ast.parse(expected_source)
    assert ast.dump(tree) == ast.dump(expected_tree)



# Generated at 2022-06-14 01:45:37.657209
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    node = ast.Import(names=[ast.alias(name='foo.bar', asname='foo')])
    tree = TestTransformer._replace_import(TestTransformer(None), node, 'foo', 'bar')
    assert str(tree) == 'try:\n    import bar.bar as foo\nexcept ImportError:\n    import foo.bar as foo'



# Generated at 2022-06-14 01:45:52.122381
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..compat import typed_ast

    class TestTransform(BaseImportRewrite):
        rewrites = [('six', 'six')]

    # check ImportFrom
    class_def = ast.parse(
        """
        import six
        """)
    tree = TestTransform.transform(class_def)
    assert tree.changed is True
    tree_str = astor.to_source(tree.tree)
    assert tree_str == dedent(
        """\
        try:
            import six
        except ImportError:
            import sixx
        """)

    # check no match
    class_def = ast.parse(
        """
        import six
        """)
    tree = TestTransform.transform(class_def)
    assert tree.changed is False
    tree_str = astor.to

# Generated at 2022-06-14 01:45:55.699740
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    transformer = BaseImportRewrite(ast.parse('import foo'))
    transformer.rewrites = [('foo', 'bar')]
    result = transformer.visit(ast.parse('import foo'))
    assert isinstance(result, ast.Try)


# Generated at 2022-06-14 01:46:02.418910
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():  # noqa
    from textwrap import dedent  # noqa
    from typed_ast.ast3 import parse  # noqa

    class FooTransformer(BaseImportRewrite):  # noqa
        rewrites = [('six', 'backports.six')]

    tree = parse(dedent("""
    import six
    """))
    visitor = FooTransformer(tree)

    visitor.visit(tree)
    assert tree.body[0].body[0].body[0].value.names[0].name == 'backports.six'



# Generated at 2022-06-14 01:46:08.505538
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    t = BaseImportRewrite(None) # type: ignore
    t._tree_changed = True
    n = ast.Import(names=[
        ast.alias(name='os', asname='os')])
    assert t.visit_Import(n).body[0].test.right.value == 'os' # type: ignore


# Generated at 2022-06-14 01:46:16.408854
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import ast
    
    
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('rewrite_this', 'to_this'),
        ]
    
    ast_tree = ast.parse(
        'import rewrite_this\n'
        'from rewrite_this import *\n'
        'from rewrite_this import Something\n'
    )

# Generated at 2022-06-14 01:46:22.987595
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    src, expected = r"""
        import numpy as np
        import tensorflow as tf
        
        import pytest
        
        print(np.zeros((3, 3)))
        print(tf.zeros((3, 3)))
        
        def foo():
            print(pytest.zeros((3, 3)))
        """.split('\n')
    rewrites = [('numpy', 'numpy-tf'), ('tensorflow', 'tensorflow-tf')]
    tree = ast.parse(src)
    BaseImportRewrite.rewrites = rewrites
    BaseImportRewrite.transform(tree)
    actual = ast.Module(body=tree.body).__str__()
    assert strip_comments(expected) == strip_comments(actual)



# Generated at 2022-06-14 01:46:33.149058
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import pytest
    import typed_ast

    tree = typed_ast.parse('import six; from django.core import management;')
    # Test replace import with import of same module
    class RewriteWithoutAlias(BaseImportRewrite):
        rewrites = [('six', 'six')]

    new_tree = RewriteWithoutAlias.transform(tree).tree
    assert typed_ast.ast3.dump(new_tree) == 'try:\n    import six\nexcept ImportError:\n    pass\n'

    # Test replace import with import of another module
    class RewriteWithAlias(BaseImportRewrite):
        rewrites = [('django.core', 'django.core.management')]

    new_tree = RewriteWithAlias.transform(tree).tree

# Generated at 2022-06-14 01:46:47.807021
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import textwrap
    # s = import_rewrite
    s = textwrap.dedent('''\
    try:
        import re, sys
    except ImportError:
        import regex as re, sys
    ''')
    assert BaseImportRewrite(None).visit_ImportFrom(ast.parse(s)) == ast.parse(s)

    s = textwrap.dedent('''\
    try:
        import re
        import sys
    except ImportError:
        import regex as re
        import sys
    ''')
    assert BaseImportRewrite(None).visit_ImportFrom(ast.parse(s)) == ast.parse(s)

    s = textwrap.dedent('''\
    import re
    ''')

# Generated at 2022-06-14 01:46:56.391820
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import ast
    import astunparse

    from .utils import assert_transformer

    from .test_import_rewrite_rewrite_test import test

    source = """
import os
import sys
import re
import os.path
import abc
import abc.def
import test.test
import notest.test
import unitest.test

"""

# Generated at 2022-06-14 01:47:01.080606
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_1 = ast.Import(names=[
        ast.alias(name='bar', asname='BAR')])
    import_2 = ast.Import(names=[
        ast.alias(name='foo', asname='FOO')])
    import_3 = ast.Import(names=[
        ast.alias(name='foo.baz', asname='BAZ')])
    import_4 = ast.Import(names=[
        ast.alias(name='foo.baz.quux', asname='QUUX')])

    # 1.
    transformer = BaseImportRewrite(None)
    transformer.rewrites = [('foo', 'bar')]
    assert transformer.visit(import_1) == import_1

    # 2.

# Generated at 2022-06-14 01:47:21.026667
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrite = {
        'six.moves': 'six',
        'six.moves.urllib.parse': 'django.utils.six.moves.urllib.parse'
    }

    class TestClass(BaseImportRewrite):
        rewrites = rewrite.items()


# Generated at 2022-06-14 01:47:26.677193
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astor import to_source
    from ast import parse

    class TestImportRewrite(BaseImportRewrite):
        target = 'test'
        rewrites = [('a.b', 'c')]

    input = 'from a.b import x, y'
    tree = parse(input)
    TestImportRewrite.transform(tree)
    assert to_source(tree) == ('try:\n'
                               '    from c import x, y\n'
                               'except ImportError:\n'
                               '    from a.b import x, y')



# Generated at 2022-06-14 01:47:36.922954
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    # Given
    from ..test.test_transformer import BaseTestTransformer
    from ..types import CompilationTarget
    import_module = ast.ImportFrom(module='.test_module',
                                   names=[ast.alias(name='test_name')],
                                   level=0)
    import_name = ast.ImportFrom(module='test_module',
                                 names=[ast.alias(name='test_name')],
                                 level=0)
    # When
    target = CompilationTarget.PYTHON
    import_rewrites = BaseTestTransformer.__subclasses__()[0].rewrites + BaseImportRewrite.rewrites

# Generated at 2022-06-14 01:47:43.058630
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Test case 1 - update of import module
    module_to_test = ast.parse(
        r'''
from django.db import models

# class Signature(models.Model):
#     pass
''')
    module_to_test_expected = ast.parse(
        r'''
try:
    from django.db import models
except ImportError:
    from django.core import models

# class Signature(models.Model):
#     pass
''')
    rewrites = [('django.core', 'django.db')]
    assert (BaseImportRewrite(module_to_test).transform(module_to_test) in
            [module_to_test_expected, module_to_test])

    # Test case 2 - skip, because there is no rewrite

# Generated at 2022-06-14 01:47:51.163604
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .base import BaseImportRewrite

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('baz', 'qux'),
            ('baz.spam', 'egg')
        ]

    def test_rewrite_module(tree):
        TestImportRewrite.transform(tree)
        assert(tree.body[0].type == 'Try')

        node = tree.body[0]
        assert(node.body[0].names[0].name == 'egg')

    def test_rewrite_names(tree):
        TestImportRewrite.transform(tree)
        assert(tree.body[0].type == 'Try')

        node = tree.body[0]
        assert(node.body[0].names[0].name == 'bar')

# Generated at 2022-06-14 01:47:56.221065
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astunparse import unparse
    from ast import ImportFrom
    
    class BaseImportRewriteStub(BaseImportRewrite):
        rewrites = [('future', 'past'), ('six.moves', 'six.move')]
        
    original = unparse(ImportFrom(level=0,
                                  module='six.moves',
                                  names=[ast.alias(name='http_cookies',
                                                   asname=None)],
                                  lineno=1, col_offset=0)).replace("\n", "")
    
    rewroted = BaseImportRewriteStub.transform(ast.parse(original))
    rewroted_code = unparse(rewroted.tree).replace("\n", "")
    

# Generated at 2022-06-14 01:48:06.220612
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from_statement_1 = ast.parse(
        'from importlib import import_module, reload')

    import_from_statement_2 = ast.parse(
        'from importlib import import_module as im')

    import_from_statement_3 = ast.parse(
        'from importlib import reload as r')

    import_from_statement_4 = ast.parse(
        'from importlib import *')

    class SampleTransformer(BaseImportRewrite):
        target = CompilationTarget.python_36
        rewrites = [
            ('importlib', 'importlib2')
        ]

        def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
            return super().visit_ImportFrom(node)

    # importlib -> importlib2
    sample_transformer = SampleTrans

# Generated at 2022-06-14 01:48:15.088266
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # when
    result = BaseImportRewrite.visit_ImportFrom(None,
                                                ast.ImportFrom(module='os',
                                                               names=[ast.alias(name='path',
                                                                                asname=None),
                                                                      ast.alias(name='foo',
                                                                                asname='bar')],
                                                               level=0))
    # then
    assert isinstance(result, ast.Try)
    assert isinstance(result.body[0], ast.Expr)
    assert isinstance(result.body[0].value, ast.List)
    assert isinstance(result.body[0].value.elts[0], ast.Import)
    assert result.body[0].value.elts[0].names[0].name == 'os.path'

# Generated at 2022-06-14 01:48:26.357123
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest.mock as mock
    from ..utils.ast import compare_ast

    tree = ast.parse('from helloworld import A, B, C\n')

    class ConcreteImportRewrite(BaseImportRewrite):
        rewrites = [
            ('helloworld', 'helloworld_rewritten')
        ]


# Generated at 2022-06-14 01:48:34.799906
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class TestTransformer(BaseImportRewrite):
        rewrites = [('time', 'datetime.time')]

    tree = ast.parse(r'''
    import time
    ''')

    result = TestTransformer.transform(tree)
    expected = ast.parse(r'''
    try:
        import time
    except ImportError:
        import datetime.time
    ''')

    assert ast.dump(result.tree) == ast.dump(expected)
    assert result.changed is True, result.changed


# Generated at 2022-06-14 01:48:50.621794
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..test_utils import assert_compiled_output
    from .test_ast import module
    from . import BaseImportRewrite
    BaseImportRewrite.rewrites = [('bisect', '_bisect')]

    expected_output = '''
    from _bisect import bisect, insort

    def foo():
        bisect(x)
        insort(x)
    '''.strip()

    assert_compiled_output(BaseImportRewrite, module, expected_output)



# Generated at 2022-06-14 01:48:55.567953
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse("import foo")
    rewrites = [("foo", "bar")]
    class TestTransformer(BaseImportRewrite):
        rewrites = rewrites
    transformer = TestTransformer(tree)
    visitor = transformer.visit_Import(tree.body[0])
    assert isinstance(visitor, ast.Try)


# Generated at 2022-06-14 01:49:04.747326
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrites = [('foo', 'bar')]
    class dummy(BaseImportRewrite):
        rewrites = rewrites

    tree = ast.parse('from foo import bar')
    res = dummy.transform(tree).tree
    assert(str(res) == 'try:\n    from foo import bar\nexcept ImportError:\n    from bar import bar')

    tree = ast.parse('from foo import *')
    res = dummy.transform(tree).tree
    assert(str(res) == 'from foo import *')

    rewrites = [('foo', 'bar'), ('bar', 'baz')]
    class dummy(BaseImportRewrite):
        rewrites = rewrites

    tree = ast.parse('from foo import bar')
    res = dummy.transform(tree).tree

# Generated at 2022-06-14 01:49:13.033797
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Given
    module = ast.parse('from urllib.request import urlopen')
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('urllib.request', 'urllib3.request')]

    # When
    result = TestTransformer.transform(module).tree

    # Then
    assert module != result
    assert result == ast.parse('try:\n    from urllib.request import urlopen\nexcept ImportError:\n    from urllib3.request import urlopen')


# Generated at 2022-06-14 01:49:23.983106
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..rewrites import urllib
    from unittest.mock import Mock

    class MockTransformer(BaseImportRewrite, ast.NodeTransformer):
        def __init__(self, tree: ast.AST):
            super().__init__(tree)

    mocktree = Mock(ast.AST, spec=ast.AST)
    mockraw = Mock(ast.ImportFrom, spec=ast.ImportFrom)
    mockraw.module = 'urllib.request'
    from_node = Mock(ast.alias)
    from_node.name = 'from_'
    mockraw.names = [from_node]
    mockraw.level = 0
    result = MockTransformer.transform(mockraw)
    assert result == (mockraw, True, ['urllib'])



# Generated at 2022-06-14 01:49:31.346261
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    from . import test_utils
    from . import test_utils_2
    from . import test_utils_3

    class InvalidImportTransformer(BaseImportRewrite):
        rewrites = [
            ('test_utils_2', 'test_utils_3'),
        ]

    tree = ast.parse('''
import sys
import test_utils
import test_utils_2
import test_utils_2.some
import test_utils_2.some.other

''')

    tree = InvalidImportTransformer.transform(tree).tree  # type: ignore


# Generated at 2022-06-14 01:49:41.326808
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Import(BaseImportRewrite):
        rewrites = [('module_a', 'module_b')]

    expected_body = [ast.Try(
        body=[ast.Import(names=[ast.alias(name='module_b', asname='module_a'),
                                ast.alias(name='module_c', asname='module_c')])],
        handlers=[ast.ExceptHandler(
            type=ast.Name(id='ImportError', ctx=ast.Load()),
            name=None,
            body=[ast.Import(names=[ast.alias(name='module_a', asname='module_a'),
                                    ast.alias(name='module_c', asname='module_c')])])],
        orelse=[],
        finalbody=[])]


# Generated at 2022-06-14 01:49:52.877194
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('os.path', 'pathlib')
            ]

    node = ast.parse('import foo').body[0]  # type: ast.AST

    result = TestTransformer.transform(node)

    assert result == TransformationResult(
        ast.parse('try:\n    import foo\nexcept ImportError:\n    import bar').body[0],
        True,
        [])

    node = ast.parse('import os.path').body[0]  # type: ast.AST

    result = TestTransformer.transform(node)

    assert result == TransformationResult(
        ast.parse('try:\n    import os.path\nexcept ImportError:\n    import pathlib').body[0],
        True,
        [])

# Generated at 2022-06-14 01:50:02.695859
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """Test for method visit_ImportFrom of class BaseImportRewrite."""
    class Empty(BaseImportRewrite):
        rewrites = [
            ('old_pkg', 'new_pkg'),
            ('old_pkg2', 'new_pkg2'),
        ]
        # Class empty, since we want to control the result in each case

    class ImportFrom1(Empty):
        def visit_ImportFrom(self, node):
            # Replace import from with different module name
            if node.module == 'old_pkg':
                return self._replace_import_from_module(node, 'old_pkg', 'new_pkg')
            return self.generic_visit(node)


# Generated at 2022-06-14 01:50:12.778192
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    t = BaseImportRewrite(None)
    node = ast.parse("from t1 import a, b, c", mode="exec")
    t.visit(node)
    expected = ast.parse("from t1 import a, b, c\n", mode="exec")
    assert node == expected

    node = ast.parse("from t1 import a as b, b, c", mode="exec")
    t.visit(node)
    expected = ast.parse("from t1 import a as b, b, c\n", mode="exec")
    assert node == expected

    node = ast.parse("from t1 import *", mode="exec")
    t.visit(node)
    expected = ast.parse("from t1 import *\n", mode="exec")
    assert node == expected


# Generated at 2022-06-14 01:50:36.725167
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from .utils import compare_ast, test_tree, parse_str
    from .test_base_import_rewrite_visit_import import rewrites

    class MyTransformer(BaseImportRewrite):
        rewrites = rewrites

    tree = test_tree('from re import findall, search')
    transformed = MyTransformer.transform(tree)
    result = parse_str(transformed.code)
    expected = parse_str('import re, re2; try: from re import findall, search; from re2 import findall as re2_findall, search as re2_search except ImportError: from re2 import findall, search as re2_search, findall as re2_findall')
    assert compare_ast(result, expected)
    assert transformed.changed

   

# Generated at 2022-06-14 01:50:48.465596
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('os', 'new_os')]

    program = ast.parse("from os import path\nimport os")
    body = program.body
    assert isinstance(body[0], ast.ImportFrom)
    # should not change anything for import os
    assert isinstance(body[1], ast.Import)
    assert len(body) == 2

    result = TestTransformer.transform(program)
    assert result.is_changed
    assert len(result.tree.body) == 3

    # try/except node for import from os
    assert isinstance(result.tree.body[0], ast.Try)
    try_body = result.tree.body[0].body
    assert len(try_body) == 2

# Generated at 2022-06-14 01:50:59.702441
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('six', 'py3compat')]

    tree = ast.parse('import six')
    transformer = TestTransformer(tree)
    node = transformer.visit_Import(tree.body[0])

    assert node.handlers[0].type.id == 'six'
    assert node.handlers[0].type.lineno == 1
    assert node.handlers[0].type.col_offset == 0
    assert node.handlers[0].body[0].value.id == 'py3compat'
    assert node.handlers[0].body[0].value.lineno == 1
    assert node.handlers[0].body[0].value.col_offset == 8
    assert node.body[0].value.id == 'six'
   

# Generated at 2022-06-14 01:51:09.835764
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .test_fixtures.import_rewrite import from_raw, from_changed, from_changed_module,\
        from_changed_both
    import astor
    import ast
    import copy

    module_node = ast.parse(from_raw)
    transformer = BaseImportRewrite(module_node)
    transformer.visit(module_node)
    assert astor.to_source(module_node) == from_raw

    module_node = ast.parse(from_changed)
    transformer = BaseImportRewrite(module_node)
    transformer.visit(module_node)
    assert astor.to_source(module_node) == from_changed

    module_node = ast.parse(from_changed_module)
    transformer = BaseImportRewrite(module_node)

# Generated at 2022-06-14 01:51:22.276519
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    import unittest.mock

    tree = ast.parse('''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
    ''')

    transformer = BaseImportRewrite()
    transformer.rewrites = [('unittest', 'unittest2')]
    result = transformer.transform(tree)
    assert result.tree.body[2].body[0].body[0].body[0].value.left.value.body[0].value.value == 'unittest2'
    with unittest.mock.patch('importlib.import_module') as import_module:
        import_module.side_effect = ImportError()
        exec(compile(result.tree, '', 'exec'))



# Generated at 2022-06-14 01:51:31.237813
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    tree = ast.parse("""
import os 
import sys 
import astor 
import codecs
    """)

    class Rewrite(BaseImportRewrite):
        rewrites = [('astor', 'astunparse')]

    r = Rewrite(tree)
    r.visit(tree)
    assert astor.to_source(tree) == """
try:
    import os 
except ImportError:
    pass

try:
    import sys 
except ImportError:
    pass

try:
    import astor 
except ImportError:
    import astunparse as astor 

try:
    import codecs
except ImportError:
    pass"""



# Generated at 2022-06-14 01:51:38.714669
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    imports = ast.parse('import a.b')
    results = BaseImportRewrite(imports).visit(imports)
    assert results == ast.Try(
        body=[ast.Import(names=[ast.alias(name='a.b', asname='b')])],
        handlers=[ast.ExceptHandler(
            type=ast.Name(id='ImportError', ctx=ast.Load()),
            name=None,
            body=[ast.Import(names=[ast.alias(name='a.b', asname='b')])])],
        orelse=[],
        finalbody=[])


# Generated at 2022-06-14 01:51:47.954832
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]

    source = """
import old
x = old.attr
Y = old.Cls
"""
    expected = """
try:
    import old
except ImportError:
    import new
x = old.attr
Y = old.Cls
"""
    tr = TestImportRewrite.transform(ast.parse(source))
    assert tr.tree_changed
    assert ast.dump(tr.tree) == ast.dump(ast.parse(expected))


# Generated at 2022-06-14 01:51:52.452973
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_test = ast.Import(names=[
        ast.alias(name='test', asname=None)])

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('test', 'test_rewrite')]

    result = TestImportRewrite.transform(import_test)
    assert isinstance(result.tree, ast.Try)
    assert result.tree_changed is True

# Generated at 2022-06-14 01:51:55.618942
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('''
from foo import bar
        ''')

    expected = ast.parse('''
try:
    from foo import bar
except ImportError:
    import bar
        ''')

    Transformer.transform(tree)

    assert ast.dump(expected) == ast.dump(tree)



# Generated at 2022-06-14 01:52:16.767188
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from pprint import pprint
    from ..parsing import parse

    class ImportRewriter(BaseImportRewrite):
        rewrites = [('sre_compile', 're')]

    tree = parse('''
from re import match
from sre_compile import compile
from sre_compile import compile as new_compile
from sre_compile import compile as compile, match as match
from sre_matcher import match
from sre_matcher.match import match
''')
    import_rewriter = ImportRewriter(tree)
    import_rewriter.visit(tree)

    pprint(import_rewriter._tree)
    assert False

# Generated at 2022-06-14 01:52:26.072410
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    class TestTransformer(BaseImportRewrite):
        rewrites = [('from_module', 'to_module')]

    class TestVisitor(ast.NodeTransformer):

        def __init__(self):
            self.test_tree1 = ast.parse("from from_module import a, b")
            self.test_tree2 = ast.parse("from from_module import *")
            self.test_tree3 = ast.parse("from from_module import a, b as c")
            self.test_tree4 = ast.parse("from from_module import a as b")
            self.test_tree5 = ast.parse("from from_module import a as b, c as d")
            self.test_tree6 = ast.parse("from from_module import a")

# Generated at 2022-06-14 01:52:36.390681
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    transformer = BaseImportRewrite()
    def result(previous, current) -> ast.Try:
        transformer._tree_changed = False
        rewrote = transformer.visit_ImportFrom(previous)
        assert transformer._tree_changed is True
        assert rewrote.body == current.body
        return rewrote
    previous = ast.ImportFrom(level=0,
                              module="from_module",
                              names=[ast.alias(name="from_name",
                                               asname="from_asname")])
    current = ast.ImportFrom(level=0,
                             module="to_module",
                             names=[ast.alias(name="to_name",
                                              asname="to_asname")])
    rewrote = result(previous, current)
    assert rewrote.orelse[0].body

# Generated at 2022-06-14 01:52:45.019321
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from astunparse import unparse

    rewrites = [('pytest', 'unittest')]

    class SubImportRewrite(BaseImportRewrite):
        rewrites = rewrites

    code = """
from pytest import main
from pytest import fixture
from pytest.fixtures import test
from not_to_rewrite import main as m

"""

    tree = ast.parse(code)
    SubImportRewrite.transform(tree)

    expected_code = """
from unittest import main
from unittest import fixture
from unittest.fixtures import test
from not_to_rewrite import main as m

"""

    assert unparse(tree).strip() == expected_code.strip()


# Generated at 2022-06-14 01:52:54.819402
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse

    class TestClass(BaseImportRewrite):
        rewrites = (('module1', 'module2'),
                    ('module3', 'module4'))

    tree = ast.parse("import module1", "<test_file>", "exec")
    transformed = TestClass.transform(tree)
    expected = ast.parse("""
try:
    import module1
except ImportError:
    import module2
""", "<test_file>", "exec")
    assert astunparse.unparse(transformed.tree) == astunparse.unparse(expected)



# Generated at 2022-06-14 01:53:05.055906
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # import smtplib as smtp
    node = ast.parse('import smtplib as smtp').body[0]
    assert isinstance(node, ast.Import)
    # After transformation
    #   try:
    #       import smtplib as smtp
    #   except ImportError:
    #       import smtp_stub as smtp
    assert (
        BaseImportRewrite(None).visit_ImportFrom(node).body[0].names[0].name ==
        'smtplib'
    )
    # import smtplib as smtp
    node = ast.parse('import smtplib as smtp').body[0]
    assert isinstance(node, ast.Import)
    # After transformation
    #   try:
    #       import smtplib as smtp
    #

# Generated at 2022-06-14 01:53:13.696434
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .test_helpers import assert_equal_ast
    from .test_snippets import import_rewrite
    from ..types import CompilationTarget

    class Test(BaseImportRewrite):
        target = CompilationTarget('.py', (3, 5))
        rewrites = [('os', 'pypy_os')]

    tree = ast.parse('from os import path')
    inst = Test(tree)
    new_tree = inst.visit(tree)


# Generated at 2022-06-14 01:53:22.570006
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('old', 'new'),
        ]

        def visit_Import(self, node: ast.Import) -> Union[ast.Import, ast.Try]:
            return super().visit_Import(node)

    tree = ast.parse('''
    import old.mod1
    ''')
    expected_tree = ast.parse('''
    try:
        import old.mod1
    except ImportError:
        import new.mod1
    ''')

    result = TestTransformer.transform(tree)

    assert result.transformed == 'import new.mod1\n'
    assert astor.to_source(result.tree) == astor.to_source(expected_tree)



# Generated at 2022-06-14 01:53:31.008052
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import astor
    
    from ast_builder import astobj
    
    from ..types import CompilationTarget
    from .base import BaseImportRewrite
    from .rewrite_future_builtins import FutureBuiltinsRewrite
    
    
    class DummyImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PY35
        dependencies = []
        rewrites = [('foo', 'bar')]
    
    class TestDummyImportRewrite(unittest.TestCase):

        def test_visit_ImportFrom(self):
            tree = astobj(
                ImportFrom(module='foo.bar',
                           names=[alias(name='Z', asname='Z')],
                           level=0),
            )
            rewrite = DummyImportRewrite.transform(tree)


# Generated at 2022-06-14 01:53:41.802869
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import os.path
    from io import StringIO
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import parse, dump
    from typed_ast.transforms import BaseImportRewrite
    from typing import Dict, List, Tuple

    class Visitor(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six'),
            ('six.moves.tkinter', 'tkinter'),
            ('six.moves.tkinter_ttk', 'tkinter.ttk')]

        def __str__(self):
            return 'test'
