

# Generated at 2022-06-14 01:44:13.797859
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..target import Python27, Python35
    from .transformers import Python2to3CompatibilityVisitor

    # rewrite import from
    source = '''\
from . import a
import collections.abc
'''
    tree = ast.parse(source)
    Python2to3CompatibilityVisitor.transform(tree)
    assert ast.dump(tree) == '''\
Module(body=[ImportFrom(module='.', names=[alias(name='a', asname=None)], level=0),
               Import(names=[alias(name='collections', asname=None)])])
'''
    # rewrite import from by module name
    source = '''\
import .a
import collections.abc as abc
'''
    tree = ast.parse(source)
    Python2to3CompatibilityVisitor.transform(tree)


# Generated at 2022-06-14 01:44:23.608108
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import sys
    import astunparse
    import ast

    class Test(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            import sys
            sys.path.append('test/test_code')

        @classmethod
        def tearDownClass(cls):
            import sys
            del sys.path[-1]

    class BaseImportRewriteSubclass(BaseImportRewrite):
        rewrites = [('foo.bar', 'baz.buz')]

    class Test_visit_Import(Test):
        def test_base(self):
            class_ = BaseImportRewriteSubclass
            tree = ast.parse('import foo.bar')
            transformer = class_.transform(tree)

# Generated at 2022-06-14 01:44:28.729311
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')
        ]

    tree = ast.parse('import foo')
    expected = 'try:\n    import foo\nexcept ImportError:\n    import bar'

    result = TestImportRewrite.transform(tree)
    assert result == TransformationResult(ast.parse(expected), True, [])



# Generated at 2022-06-14 01:44:38.065917
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests._support import ast_helper

    rewrites = [('yaml', 'yaml3')]

    class TestTransformer(BaseImportRewrite):
        rewrites = rewrites

    tree = ast_helper.parse("""
        import yaml

        print(yaml.load)
    """)

    TestTransformer.transform(tree)

    expected_tree = ast_helper.parse("""
        try:
            import yaml
        except ImportError:
            import yaml3 as yaml

        print(yaml.load)
    """)

    ast_helper.assert_tree_eq(tree, expected_tree)



# Generated at 2022-06-14 01:44:47.446247
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]

    # If there is no match, nothing changes
    node = ast.parse('import old.foo as my_foo').body[0]
    assert isinstance(TestBaseImportRewrite.transform(node).tree, ast.Import)

    # If module match, we import module from try/except with old and new
    node = ast.parse('import old.foo as my_foo').body[0]
    result = TestBaseImportRewrite.transform(node)
    assert isinstance(result.tree, ast.Try)
    assert result.tree_changed

    # If module does not match and name match, we import module from try/except with 
    # module from and name from

# Generated at 2022-06-14 01:44:54.513381
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    from .test_transformer import get_tree, transform

    class MockBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('requests', 'httpx')
        ]

    fake_tree = get_tree(
        """
        import requests
        """)

    result = transform(MockBaseImportRewrite, fake_tree)

    assert result.ast_changed, 'AST must be changed'
    assert len(result.dependencies) == 1, 'Must have 1 dependency'
    assert result.dependencies[0] == 'httpx==0.11.1', 'Must have correct dependency'
    assert astor.to_source(result.ast) == '''
try:
    import requests
except ImportError:
    import httpx
    ''', 'Must wrap import with try/except'



# Generated at 2022-06-14 01:45:04.981608
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as _ast
    import copy as _copy
    import typed_ast.ast3 as _ast3
    import typed_astunparse as _unparse
    class BaseImportRewrite(_ast3.NodeTransformer, metaclass=_ast3.NodeVisitorMeta):
        _fields = ('rewrites',)
        _attributes = ('rewrites',)
        rewrites = []  # type: List[Tuple[str, str]]
        def _get_matched_rewrite(self, name: Optional[str]) -> Optional[Tuple[str, str]]:
            """Returns rewrite for module name."""
            if name is None:
                return None
            for from_, to in self.rewrites:
                if name == from_ or name.startswith(from_ + '.'):
                    return from_, to


# Generated at 2022-06-14 01:45:09.464682
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo.bar', 'foo')]

        def __init__(self):
            super().__init__(None)

    def _get_node(module):
        return ast.parse("from {module} import foo, bar, baz".format(module=module)).body[0]

    transformer = TestTransformer()
    node = _get_node("foo.bar")

    rewritten = transformer.visit(_get_node("foo"))
    assert isinstance(rewritten, ast.Try)

    rewritten = transformer.visit(node)
    assert isinstance(rewritten, ast.Try)

    node = _get_node("foo.bar.baz")
    rewritten = transformer.visit(node)
    assert isinstance(rewritten, ast.Try)



# Generated at 2022-06-14 01:45:20.042694
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from flake8.api import legacy as flake8

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'baz'),
        ]

    tree = ast.parse('import foo')
    TestBaseImportRewrite.transform(tree)
    result = astor.to_source(tree).rstrip()
    assert result == 'try:\n    import foo\nexcept ImportError:\n    import baz', result

    tree = ast.parse('import foo.bar')
    TestBaseImportRewrite.transform(tree)
    result = astor.to_source(tree).rstrip()
    assert result == 'try:\n    import foo.bar\nexcept ImportError:\n    import baz.bar', result

    tree = ast.parse('import bar')
    Test

# Generated at 2022-06-14 01:45:28.312379
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.fake import get_ast_for_code
    from .settings import ImportRewriteSetting

    tree = get_ast_for_code('import django')
    transformer = BaseImportRewrite(tree)
    transformer.initialize(None, ImportRewriteSetting())
    transformer.visit(tree)

    assert transformer._tree_changed is True
    assert 'ImportError' in ast.dump(tree)
    assert 'import django' in ast.dump(tree)
    assert 'NotImplemented' in ast.dump(tree)


# Generated at 2022-06-14 01:45:45.096713
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Initial setup
    tree = ast.parse('''
import test
test.test_0()
''', mode='exec')
    # End of initial setup
    # Test
    transformer = BaseImportRewrite('test', 'test_rewrite', tree)
    transformer.visit_Import(tree.body[0])
    # End of Test
    actual_result = ast.dump(tree, include_attributes=False)
    expected_result = 'Module(body=[Try(body=[Import(names=[alias(name=\\\'test_rewrite\\\', asname=None)])], handlers=[ExceptHandler(type=ImportError(), name=None, body=[Import(names=[alias(name=\\\'test\\\', asname=None)])])], orelse=[])])'
    assert expected_result == actual_result

# Unit

# Generated at 2022-06-14 01:45:54.986231
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('from __future__ import unicode_literals\n')
    class MyTransformer(BaseImportRewrite):
        rewrites = [('__future__.unicode_literals', 'six.unicode_literals')]

    result = MyTransformer.transform(tree)
    assert result.tree_changed
    assert result.dependencies == ['six']



# Generated at 2022-06-14 01:46:01.039033
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewrites = [
        ('previous', 'current')]
    result = """
import current

"""
    cls = type('DummyImportRewrite', (BaseImportRewrite,), {'rewrites': rewrites})
    assert cls.transform(ast.parse('import previous\n'))[0] == ast.parse(result)



# Generated at 2022-06-14 01:46:10.771179
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import sys
    import _ast
    from typed_ast import ast3 as typed_ast

    with open('./tests/data/import_rewrite_test.py',
              'rb') as file:
        tree = typed_ast.parse(file.read().decode('utf-8'))

    before = ast.dump(tree)
    BaseImportRewrite.transform(tree)
    after = ast.dump(tree)

    # // import_rewrite.py
    #
    # try:
    #     import unittest2
    # except ImportError:
    #     import unittest as unittest2
    # try:
    #     import unittest2.case
    # except ImportError:
    #     import unittest.case as unittest2_case


# Generated at 2022-06-14 01:46:20.742092
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    _import_from_simple_input = ("from old.module import *",
                                 ast.ImportFrom(module="old.module",
                                                names=[ast.alias(name="*",
                                                                 asname=None)],
                                                level=0))

# Generated at 2022-06-14 01:46:29.362041
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor as ast
    from ..parse import parse
    from ..utils.dummy import visit_imports

    tree = parse('from datetime import datetime')
    instance = BaseImportRewrite(tree)
    instance.target = CompilationTarget.Python35
    instance.rewrites = [(b'urllib', b'urllib.request')]

    visit_imports(instance)

    assert ast.to_source(tree) == 'try:\n    from datetime import datetime\nexcept ImportError:\n    from urllib.request import datetime'



# Generated at 2022-06-14 01:46:36.960456
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('base', 'foo')]

    import_from = ast.ImportFrom(module='foo', names=[ast.alias(name='bar')], level=0)
    rewrite = TestBaseImportRewrite(import_from).visit(import_from)
    assert rewrite.body[0].value.names[0].name == 'foo.bar'


if __name__ == '__main__':
    # Unit test for method visit_ImportFrom of class BaseImportRewrite
    test_BaseImportRewrite_visit_ImportFrom()

# Generated at 2022-06-14 01:46:49.643002
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import AnnAssign
    from typed_ast.ast3 import With
    from typed_ast.ast3 import AugAssign
    from typed_ast.ast3 import Raise
    from typed_ast.ast3 import Exec
    from ..transforms import BaseImportRewrite
    from ..transforms import ImportRewriteDuet  # noqa

    class TestImport(BaseImportRewrite):
        target = 'python.3'
        rewrites = [('float', 'decimal')]

    tree = parse('import decimal as dec')
    TestImport.transform(tree)
    assert parse('import decimal as dec') == tree
    tree = parse('import decimal')
    TestImport.transform(tree)
    assert parse('import decimal') == tree

# Generated at 2022-06-14 01:46:57.254792
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class MyTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('import foo')

    res = MyTransformer.transform(tree)

    expected = """
try:
    import foo
except ImportError:
    import bar
    """

    assert expected.strip() == ast.dump(res.tree).strip()
    assert res.changed is True



# Generated at 2022-06-14 01:47:05.301356
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class _Import(BaseImportRewrite):
        rewrites = [('os.path', 'os.path2')]

    code = "import os.path as test"

    node = ast.parse(code)

    _Import.transform(node)

    expected = "try:\n    import os.path as test\nexcept ImportError:\n    import os.path2 as test"

    assert str(node) == expected



# Generated at 2022-06-14 01:47:20.448079
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import astor
    from collections import namedtuple
    from ..utils import test
    from ..utils.snippet import get_ast_code, get_ast_ast
    body = test.get_test_body("importfrom.py")
    tree = ast.parse(body)
    class Mock(BaseImportRewrite):
        rewrites = [("from_from_from", "from_from_from")]
    Mock.visit_ImportFrom(tree)
    test.run(astor.dump_tree(tree), "importfrom.py")
    tree = ast.parse(body)
    class Mock(BaseImportRewrite):
        rewrites = [("from_from_from", "from_from_from_from")]
    Mock.visit_ImportFrom(tree)

# Generated at 2022-06-14 01:47:28.059998
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('previous_name', 'current_name'),
            ('previous_name2', 'current_name2'),
        ]

    class TestNodeTransformer(BaseNodeTransformer):
        def visit_Import(self, node):
            return self.parent.visit_Import(node)

    class TestCase(unittest.TestCase):
        def test_import(self):
            module = ast.parse('import previous_name')

            result = TestNodeTransformer(module).transform(module)

            expected = """
            try:
                import previous_name
            except ImportError:
                import current_name
            """


# Generated at 2022-06-14 01:47:34.269291
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from typed_ast.ast3 import parse
    import_node = parse("from six.moves import abc").body[0]
    bimp = BaseImportRewrite(None)
    assert astor.to_source(bimp.visit_ImportFrom(import_node)) == 'try:\n    from six.moves import abc\nexcept ImportError:\n    from six import abc'


# Generated at 2022-06-14 01:47:44.927110
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse
    import textwrap
    from . import simple

    program = textwrap.dedent('''
        from a import b as c
        
        from a.b.c import d
        from a.b.c import e as f
        
        from django.http import HttpResponse
        
        if __name__ == '__main__':
            a = HttpResponse()
    ''')

    class TestImportRewrite(BaseImportRewrite):

        rewrites = [
            ('a.b.c', 'a.c.b')
        ]

    tree = ast.parse(program)
    result = TestImportRewrite.transform(tree)

# Generated at 2022-06-14 01:47:52.188456
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    from . import BaseImportRewrite
    from .utils import RecursiveImportRewrite, _get_namespace

    source = """
from django import forms
"""

    class DummyTransformer(RecursiveImportRewrite, BaseImportRewrite):
        rewrites = [
            ('django.forms', 'flask_wtf'),
        ]

    tree = parse(source)
    old_namespace = _get_namespace(source)
    tr = DummyTransformer(tree)
    tr.visit(tree)
    new_namespace = _get_namespace(compile(tree, '<string>', 'exec'))
    assert 'django' not in new_namespace
    assert new_namespace['forms'] == old_namespace['forms']


# Generated at 2022-06-14 01:48:00.182683
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ... import parse_ast
    import os
    import sys
    from ..utils.testing import fix_assert_raises_regex

    tree = parse_ast('''
    import os
    ''')
    transformer = BaseImportRewrite(tree)
    rewrites = [(os.__name__, sys.__name__)]
    transformer.rewrites = rewrites
    transformer.visit(tree)
    result = transformer._tree.body[0]
    assert isinstance(result, ast.Try)
    assert isinstance(result.body[0], ast.Import)
    assert result.body[0].names[0].name == sys.__name__
    assert isinstance(result.body[1], ast.ExceptHandler)
    assert isinstance(result.body[1].body[0], ast.Import)
   

# Generated at 2022-06-14 01:48:08.135911
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    def run_test(node, expected_node_str, expected_changed):
        import_rewrite_class = type('import_rewrite_class', (BaseImportRewrite,),
                              {
                                  'rewrites': [('oldmodule', 'newmodule')],
                                  'dependencies': []
                              })

        from_str = astor.to_source(node)
        result = import_rewrite_class.transform(node)

        assert astor.to_source(result.tree) == expected_node_str
        assert result.changed == expected_changed
        assert result.tree == ast.parse(expected_node_str)

    # test for import module

# Generated at 2022-06-14 01:48:17.872552
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import textwrap

    from .base import BaseTestTransformer

    class TestTransformer(BaseImportRewrite, BaseTestTransformer):
        rewrites = [
            ('old_module_name', 'new_module_name'),
        ]

    import_statements = [
        'import old_module_name',
        'import old_module_name.something',
        'from old_module_name import something',
        'from old_module_name import something_else',
    ]


# Generated at 2022-06-14 01:48:28.838894
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'abc').result == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'def.abc').result == None
    assert BaseImportRewrite._get_matched_rewrite(BaseImportRewrite(), 'abc.def.abc').result == None

    tree = ast.parse('import abc')
    result, _, _ = BaseImportRewrite.transform(BaseImportRewrite(), tree=tree)
    assert ast.dump(result) == ast.dump(tree)

    tree = ast.parse('import def.abc')
    result, _, _ = BaseImportRewrite.transform(BaseImportRewrite(), tree=tree)
    assert ast.dump(result) == ast.dump(tree)


# Generated at 2022-06-14 01:48:36.001639
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Arrange
    node = ast.ImportFrom(
        module='mod1',
        names=[ast.alias(name='a1',
                         asname='b1')],
        level=0
    )

# Generated at 2022-06-14 01:48:52.992800
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from . import six_import_rewrite
    from ..utils.ast_tools import dump_ast, remove_locations, code_ast
    import ast

    code = '''
from cx_Freeze.freezer import Freezer
from PySide.QtGui import QApplication
from six import PY2, PY3
'''
    tree = code_ast(code)
    visitor = six_import_rewrite.BaseImportRewrite(tree)
    visitor.visit(tree)

# Generated at 2022-06-14 01:49:02.471800
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    tree = ast.parse('import argparse')
    transformer = BaseImportRewrite.__new__(BaseImportRewrite)
    transformer.rewrites = [('argparse', 'optparse')]
    body = transformer.visit(tree.body[0])
    assert type(body) is ast.Try
    assert body.handlers[0].type.id == 'ImportError'
    assert type(body.handlers[0].body[0]) is ast.Import
    assert body.handlers[0].body[0].names[0].name == 'optparse'
    assert body.finalbody[0].value.id == 'argparse'
test_BaseImportRewrite_visit_Import.BaseImportRewrite_visit_Import = True # type: ignore


# Generated at 2022-06-14 01:49:13.922029
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestCase(unittest.TestCase):
        def test(self):
            class Test(BaseImportRewrite):
                rewrites = [
                    ('old', 'new'),
                    ('other.old', 'other.new'),
                ]


# Generated at 2022-06-14 01:49:24.787856
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    from typed_ast import ast3 as ast

    class DummyTransformer(unittest.TestCase, BaseImportRewrite):
        def __init__(self, tree: ast.AST) -> None:
            super().__init__(tree)
            self.rewrites = [('_aep_target_module.Dummy', 'typed_ast.ast3')]

    check_import_from = DummyTransformer.visit_ImportFrom

    self = DummyTransformer(None)
    node = ast.ImportFrom(module='_aep_target_module.Dummy',
                          names=[ast.alias(name='Dummy', asname='Dummy')],
                          level=0)
    # import_from = check_import_from(self, node)
    # self.assertEqual(

# Generated at 2022-06-14 01:49:36.898342
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class _BaseImportRewrite(BaseImportRewrite):
        rewrites = [('six', 'six.moves')]

    tree = ast.parse('import six')
    _BaseImportRewrite.transform(tree)
    assert ast.dump(tree) == '''
try:
    import six
except ImportError:
    import six.moves as six
'''

    tree = ast.parse('import six.moves as six')
    _BaseImportRewrite.transform(tree)
    assert ast.dump(tree) == '''
try:
    import six.moves as six
except ImportError:
    import six.moves as six
'''

    tree = ast.parse('import six.moves')
    _BaseImportRewrite.transform(tree)

# Generated at 2022-06-14 01:49:46.844884
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('old.module', 'new.module'),
            ('old', 'new')
        ]

    @snippet
    def example_module():
        import old.module
        import old
        import old.module.name

    tree = ast.parse(example_module)
    result = TestImportRewrite.transform(tree)
    ast.fix_missing_locations(result.tree)

    assert result.tree.body[0].body[4].body[0].test.name == 'new.module'
    assert result.tree.body[0].body[4].body[0].test.args[0].s == 'old.module'
    assert result.tree.body[0].body[4].body[1].test.args[0].s

# Generated at 2022-06-14 01:49:57.386590
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    snippet_source = '''
    from a import b
    from a.c import d
    from b import c
    from a.b import d
    from a.d import e as f
    from a.f import e as g, h as i
    '''.lstrip().splitlines()
    snippet_source = [line + '\n' for line in snippet_source]

# Generated at 2022-06-14 01:50:02.781250
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    class DummyTransformer(BaseImportRewrite):
        rewrites = [('os', 'posixpath')]

    code = """
import os
import json
"""
    tree = ast.parse(code)
    tree = DummyTransformer.transform(tree)[0]
    code = ast.unparse(tree)

    assert code == """
try:
    import os
except ImportError:
    import posixpath as os
import json
"""



# Generated at 2022-06-14 01:50:07.842341
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import astor
    import typing

    import astunparse
    import z3
    from z3 import z3types

    from typed_astunparse import ast3

    import_tree = astor.parse_file('tests/examples/import_rewrite_test.py')
    from typed_ast import ast3 as typed_ast3
    tree = typed_ast3.fix_missing_locations(typed_ast3.parse(astunparse.unparse(import_tree)))

    class TransformImport(BaseImportRewrite):
        target = 'python2'
        rewrites = [('typing', 'typing2')]

    transformed = TransformImport.transform(tree)
    print(astunparse.unparse(transformed.tree))

# Generated at 2022-06-14 01:50:17.194349
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    import_original = astor.parse('''
import foo

import foo.bar

import foo.bar.baz

import foo
import foo.as_foo
import foo.bar
import foo.bar.as_bar
import foo.bar.baz
import foo.bar.baz.as_baz
''')


# Generated at 2022-06-14 01:50:36.764790
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class SubTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
            ('spam', 'eggs')
        ]

    @snippet
    def f():
        import foo
        import foo.baz

        import spam
        import spam.eggs

        import bar
        import bar.baz

        import eggs
        import eggs.baz

    tree = f.get_tree()
    SubTransformer.transform(tree)

    assert tree.body[0].body[0].body[0].value.names[0].name == 'bar'
    assert tree.body[0].body[0].body[0].value.names[0].asname is None


# Generated at 2022-06-14 01:50:48.462240
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.typed_ast_helper import parse, dump

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('time', 'datetime')]

    source = """
    from time import sleep
    from time import time
    from time import time as now
    from time import time, sleep as sleep2
    sleep(1)
    """
    expected_source = """
    from datetime import sleep
    from datetime import time
    from datetime import time as now
    from datetime import time, sleep as sleep2
    sleep2(1)
    """
    tree = parse(source)
    expected_tree = parse(expected_source)

    tree = TestImportRewrite.transform(tree)
    assert dump(tree) == dump(expected_tree)



# Generated at 2022-06-14 01:50:55.626473
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ObjectTransformer(BaseImportRewrite):
        rewrites = [('django.db.models', 'django.db.models.query')]

    previous = ast.parse('import django.db.models')
    expected = ast.parse("""
    try:
        extend(previous)
    except ImportError:
        extend(current)
    """)

    tree = ObjectTransformer.transform(previous)
    assert tree.is_changed is True
    assert ast.dump(tree.tree) == ast.dump(expected)



# Generated at 2022-06-14 01:51:04.178410
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .. import stdlib
    from .tests.utils import cmp_ast
    from typed_ast import ast3
    from ..testing import run_transformer_test


# Generated at 2022-06-14 01:51:12.162079
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test(BaseImportRewrite):
        rewrites = [('urllib.request', 'urllib.request2')]

    source = 'from urllib.request import urlopen'

    expected = '''
from urllib.request import urlopen

try:
    from urllib.request2 import urlopen
except ImportError:
    from urllib.request import urlopen
'''.strip()

    ast_node = ast.parse(source)
    result = Test.transform(ast_node)
    output = astor.to_source(result.tree, indent_with=' ' * 4)

    assert expected == output

# Generated at 2022-06-14 01:51:22.926305
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    tree = ast.parse("""
    from foo import bar
    from baz import *
    from qux.abc import def as ghi
    import jkl
    """)  # type: ast.AST

    class Test(BaseImportRewrite):
        rewrites = [
            ('foo', 'foo_rewrite1'),
            ('baz', 'baz_rewrite2'),
        ]

    result = Test.transform(tree)
    assert result[1]

    assert astor.to_source(result[0]) == """
    import foo_rewrite1.bar
    try:
        from baz import *
    except ImportError:
        from baz_rewrite2 import *
    import qux.abc
    import jkl
    """

# Generated at 2022-06-14 01:51:32.540749
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor  # type: ignore

    from_, to = 'foo', 'bar'

    # Single import
    old = ast.parse("import foo")
    transformer = BaseImportRewrite(old)
    transformer.rewrites = [(from_, to)]
    transformer.visit(old)
    assert astor.to_source(old) == 'try:\n    import foo\nexcept ImportError:\n    import bar'

    # Single import with alias
    old = ast.parse("import foo as bar")
    transformer = BaseImportRewrite(old)
    transformer.rewrites = [(from_, to)]
    transformer.visit(old)
    assert astor.to_source(old) == 'try:\n    import foo as bar\nexcept ImportError:\n    import bar'

    # Single import with dotted name
    old

# Generated at 2022-06-14 01:51:45.992371
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        target = CompilationTarget('2.7')

        rewrites = [
            ('foo', 'foo2'),
        ]

    import1_old = ast.Import(
        names=[ast.alias(
            name='foo',
            asname='foo1')])

# Generated at 2022-06-14 01:51:54.722404
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest

    module = ast.parse("import os\nos.makedirs('/tmp')\n")

    class MockImportRewrite(BaseImportRewrite):
        rewrites = [('os', 'subprocess')]

    MockImportRewrite.transform(module)
    # print(ast.dump(module, include_attributes=True))


    class MockImportRewrite2(BaseImportRewrite):
        rewrites = [('subprocess', 'subprocess')]

    unittest.TestCase().assertRaises(SyntaxError, MockImportRewrite2.transform, module)

    module = ast.parse("from os import *\n")

    class MockImportRewrite3(BaseImportRewrite):
        rewrites = [('os', 'subprocess')]

    MockImportRewrite3.transform(module)

# Generated at 2022-06-14 01:52:01.892699
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    transformer = BaseImportRewrite()
    transformer.rewrites = [('attr', 'attr2')]
    node = ast.parse('''import attr''')
    rewrote = transformer.visit_Import(node.body[0])
    rewrote_string = ast.unparse(rewrote)
    assert rewrote_string == 'try:\n    import attr\nexcept ImportError:\n    import attr2'
    assert transformer._tree_changed == True



# Generated at 2022-06-14 01:52:20.552466
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as typed_ast
    from ..rewriters.common import BaseImportRewrite
    from .test_utils import Code

    # Case 1: import from module
    module = typed_ast.parse(Code.from_import('import datetime').source)
    result = BaseImportRewrite.visit_ImportFrom(module.body[0])
    assert result == typed_ast.parse(Code.from_import('import datetime').source).body[0]

    # Case 2: import from module with alias
    module = typed_ast.parse(Code.from_import('import datetime as dt').source)
    result = BaseImportRewrite.visit_ImportFrom(module.body[0])

# Generated at 2022-06-14 01:52:29.323455
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import ast
    import re
    import_st = "from a.b.c.d import e"
    node = ast.parse(import_st).body[0]
    node = ast.fix_missing_locations(node)
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [("a.b.c.d", "w.x.y.z")]
    a = TestImportRewrite.visit_ImportFrom(node)
    print(astor.to_source(a))
    lines = astor.to_source(a).split("\n")
    if lines[0] == 'try:':
        has_try_except, from_import, except_var = lines[1], lines[3], lines[5]
        m_from_import = re.search

# Generated at 2022-06-14 01:52:41.595196
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    previous = ast.Import(
        names=[
            ast.alias(name='foo', asname='bar')
        ]
    )

    current = ast.Import(
        names=[
            ast.alias(name='bar', asname='foo')
        ]
    )

    # py2
    import_tree = ast.parse('import foo as bar')
    BaseImportRewrite._tree = import_tree
    BaseImportRewrite._tree_changed = False
    result = BaseImportRewrite.visit_Import(previous)
    assert astor.to_source(result) == astor.to_source(
        ast.parse('try:\n    import foo as bar\nexcept ImportError:\n    import bar as foo'))
    assert not BaseImportRewrite._tree_changed

    # py3

# Generated at 2022-06-14 01:52:55.165386
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom(): 
    from typed_ast.ast3 import parse
    obj = BaseImportRewrite()
    module = parse("from foo import bar")
    obj.rewrites.append(('foo','boo'))
    obj.visit(module)
    assert(str(module) == "try:\n    from foo import bar\nexcept ImportError:\n    from boo import bar")
    module = parse("from foo import bar as baz")
    obj.visit(module)
    assert(str(module) == "try:\n    from foo import bar as baz\nexcept ImportError:\n    from boo import bar as baz")
    module = parse("from foo import bar")
    obj.rewrites.append(('bar','baz'))
    obj.visit(module)

# Generated at 2022-06-14 01:53:02.074275
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():  # type: ignore
    import astor
    import astroid
    import typed_ast.ast3 as ast
    import typed_astunparse
    import os
    import sys

    class ImportTransformerRewrite(BaseImportRewrite):
        rewrites = [('astroid', 'astor')]
        target = CompilationTarget('test_BaseImportRewrite_visit_Import', 'ast3')

    class ImportTransformer(ImportTransformerRewrite):
        rewrites = []
        target = CompilationTarget('test_BaseImportRewrite_visit_Import', 'ast3')

    snip = '''import astroid'''
    root = astor.code_to_ast.parse_file(snip)
    assert ImportTransformer().visit(root) == root


# Generated at 2022-06-14 01:53:17.336081
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class MyTransformer(BaseImportRewrite):
        rewrites = [
            ('sys', 'builtins')
        ]

    class MyTransformer2(BaseImportRewrite):
        rewrites = [
            ('sys.foo', 'builtins.foo')
        ]

    class MyTransformer3(BaseImportRewrite):
        rewrites = [
            ('sys', 'builtins'),
            ('sys.foo', 'builtins.foo')
        ]

    class MyTransformer4(BaseImportRewrite):
        rewrites = [
            ('sys', 'builtins'),
            ('sys.foo', 'builtins.foo')
        ]


# Generated at 2022-06-14 01:53:24.295673
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = """from bs4 import BeautifulSoup"""
    tree = ast.parse(import_from, '', 'exec')
    import_from_ast = tree.body[0]

    class TestRewrite(BaseImportRewrite):
        rewrites = [
            ('bs4', 'bs3'),
        ]

    TestRewrite.transform(tree)
    assert ast.dump(tree) == ast.dump(ast.parse("""try:
    from bs3 import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup""", '', 'exec'))

    class TestRewrite(BaseImportRewrite):
        rewrites = [
            ('bs4.element', 'bs4.element'),
        ]

    TestRewrite.transform(tree)
    assert ast.dump(tree) == ast

# Generated at 2022-06-14 01:53:31.392874
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import ast
    tree = ast.parse('from test import foo')
    class Transformer(BaseImportRewrite):
        rewrites = [
            ('test', 'test_rewritten')
        ]
    
    transformer = Transformer(tree)
    transformed_tree = transformer.visit(tree)
    assert isinstance(transformed_tree, ast.Try)
    try_except_items = [
        item for item in transformed_tree.body[0].body
        if isinstance(item, ast.ImportFrom)]
    assert len(try_except_items) == 2
    assert try_except_items[0].module == 'test'
    assert try_except_items[1].module == 'test_rewritten'

# Generated at 2022-06-14 01:53:41.950520
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    _locals = locals()
    _locals.update(globals())
    import astunparse
    import sys
    from io import StringIO

    saved, sys.stdout = sys.stdout, StringIO()
    try:
        a = ast.parse('import re')
        b = ast.parse('import re')
        c = ast.parse('import re')
        c = BaseImportRewrite._replace_import(c, 're', 'regex')
        result = astunparse.unparse([a, b, c])
    finally:
        sys.stdout = saved
    assert 'import re' == result.splitlines()[0]
    assert 'import re' == result.splitlines()[3]
    assert 'import regex as re' in result
    assert 'import re as re' in result

# Generated at 2022-06-14 01:53:47.304422
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast

    transformer = BaseImportRewrite()
    transformer.rewrites = [('http.server', 'wsgiref')]

    node = ast.parse('import http.server').body[0]
    assert isinstance(transformer.visit(node), ast.Try)

    node = ast.parse('import sys').body[0]
    assert transformer.visit(node) is node