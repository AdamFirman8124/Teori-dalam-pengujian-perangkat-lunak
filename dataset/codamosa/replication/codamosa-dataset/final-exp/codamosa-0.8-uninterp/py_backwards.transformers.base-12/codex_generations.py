

# Generated at 2022-06-14 01:44:19.123420
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class RewriteMock(BaseImportRewrite):
        rewrites = [('from_mock', 'to_mock')]
    global_ns = {}
    global_ns.update(globals())
    ast_data = ast.parse(
        'import from_mock as frommock\n'
        'from from_mock import *\n',
        filename='<unknown>',
        mode='exec')
    result = RewriteMock.transform(ast_data)
    assert result.tree.body[0].body[0].body[0].value.value == 'frommock'
    assert result.tree.body[1].body[0].body[0].value.value == 'from_mock'
    assert result.tree_changed == True
    assert result.dependencies == ['from_mock']

# Generated at 2022-06-14 01:44:29.444001
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class SimpleTransformer(BaseImportRewrite):
        rewrites = [
            ('os', 'nt'),
        ]

    class TestCase(unittest.TestCase):
        def test_names_are_changed(self):
            tree = ast.parse("import os.path")
            result = SimpleTransformer.transform(tree)

# Generated at 2022-06-14 01:44:42.084514
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    import textwrap
    import unittest
    import astunparse

    class TestCase(unittest.TestCase):
        def create_node(self, from_: str, to: str) -> ast.Import:
            class Test(BaseImportRewrite):
                rewrites = [(from_, to)]

            import_ = ast.Import(names=[ast.alias(name='test')])
            tree = Test.transform(import_)
            return tree.node

        def test_one(self):
            node = self.create_node('test', 'test2')
            self.assertEqual(type(node), ast.Try)

        def test_two(self):
            node = self.create_node('test.', 'test2.')
            self.assertEqual(type(node), ast.Try)

# Generated at 2022-06-14 01:44:53.730767
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('from1', 'to1'), ('from2', 'to2')]

    visitor = TestImportRewrite(None)

    assert astor.to_source(visitor.visit(ast.parse('from from1 import a').body[0])) == 'from to1 import a\n'
    assert astor.to_source(visitor.visit(ast.parse('from from1.from2 import a').body[0])) == 'from to1.to2 import a\n'
    assert astor.to_source(visitor.visit(ast.parse('from from1 import a, b, c as d').body[0])) == \
        'from to1 import a, b, c as d\n'

# Generated at 2022-06-14 01:45:04.329558
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node = ast.parse("from a.b import c").body[0]
    newNode = BaseImportRewrite(None).visit(node)
    assert isinstance(newNode, ast.Try)
    assert len(newNode.body) == 1
    assert isinstance(newNode.body[0], ast.ImportFrom)
    assert newNode.body[0].module == 'a.b'
    assert newNode.body[0].names[0].name == 'c'
    assert len(newNode.handlers) == 1
    assert isinstance(newNode.handlers[0].body[0], ast.ImportFrom)
    assert newNode.handlers[0].body[0].module == 'a.b'
    assert newNode.handlers[0].body[0].names[0].name == 'c'

# Generated at 2022-06-14 01:45:11.697638
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class DummyImportRewrite(BaseImportRewrite):
        rewrites = [('json', 'ujson')]

    import_stmt = ast.Import([ast.alias(name='json')])
    assert DummyImportRewrite.transform(tree=import_stmt).tree == \
        ast.Try(body=[
            ast.Import([ast.alias(name='json')]),
        ],
        handlers=[
            ast.ExceptHandler(body=[
                ast.Import([ast.alias(name='ujson')]),
            ]),
        ],
        orelse=[])



# Generated at 2022-06-14 01:45:21.514056
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Given
    class Class(BaseImportRewrite):
        rewrites = [('old', 'new')]

    import_statement = ast.parse("import old").body[0]

    # When
    node = Class(None).visit_Import(import_statement)

    # Then
    assert node.body[0].body[0].body[0].value.left.value.func.value.args[0].id == 'old'
    assert node.body[0].body[1].body[0].value.left.value.func.value.args[0].id == 'new'



# Generated at 2022-06-14 01:45:30.103134
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .. import ast_transforms as transforms

    input_from_1 = 'import builtins'
    input_from_2 = 'import builtins.async'
    input_from_3 = 'import builtins.async.v1'

    input_to_1 = 'from builtins import *'
    input_to_2 = 'from builtins.async import *'
    input_to_3 = 'from builtins.async.v1 import *'

    class RewriteBuiltins(BaseImportRewrite):
        rewrites = [
            ('builtins', 'future.builtins'),
        ]

    tree_1 = ast.parse(input_from_1)
    tree_2 = ast.parse(input_from_2)
    tree_3 = ast.parse(input_from_3)


# Generated at 2022-06-14 01:45:39.853245
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.compile import compile_snippet

    class TestRewriter(BaseImportRewrite):
        rewrites = [('some_module', 'some_module_rewrite')]

    snippet = '''
    import some_module
    import some_module.submodule
    '''
    new_snippet = '''
    import some_module
    
    try:
        import some_module
        import some_module.submodule
    except ImportError:
        import some_module_rewrite
        import some_module_rewrite.submodule
    '''

    (module_name, module) = compile_snippet(snippet)
    (new_module_name, new_module) = compile_snippet(new_snippet)

    assert module_name == new_module_name

   

# Generated at 2022-06-14 01:45:46.300461
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_in = ast.Import(names=[
        ast.alias(name="foo.bar.baz",
                  asname="baz")])

    from_, to = 'foo.bar.baz', 'foo.bar.qux.qux'
    result = BaseImportRewrite._replace_import(None, import_in, from_, to)
    import_out = ast.Try(body=[],
                         handlers=[],
                         orelse=[],
                         finalbody=[])
    import_out.body = [ast.Import(names=[
        ast.alias(name="foo.bar.qux.qux",
                  asname="baz")])]

# Generated at 2022-06-14 01:46:01.507887
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from textwrap import dedent as d

    class MyBaseImportRewrite(BaseImportRewrite):
        target = 'python3.6'
        rewrites = [('six.moves', 'six')]
        dependencies = ['six']


    class _(MyBaseImportRewrite):
        pass

    assert _.transform(ast.parse(d('''\
        import os'''))).tree == ast.parse(d('''\
        import os'''))
    assert _.transform(ast.parse(d('''\
        import six'''))).tree == ast.parse(d('''\
        import six'''))
    assert _.transform(ast.parse(d('''\
        import six.moves'''))).tree == ast.parse

# Generated at 2022-06-14 01:46:10.793192
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils.ast_importer import ast_import_from


# Generated at 2022-06-14 01:46:17.696519
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.parse(
        "from test_module import TestClass")
    class TestTransformer(BaseImportRewrite):
        rewrites = [('test_module', 'test_module2')]
    result = TestTransformer.transform(import_from)
    import_rewrite_code = """try:
    from test_module import TestClass
except ImportError:
    from test_module2 import TestClass"""
    assert ast.dump(result.tree) == import_rewrite_code


# Generated at 2022-06-14 01:46:20.848685
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    result = BaseImportRewrite.visit_Import(ast.Import(names=[ast.alias(name='foo', asname=None)]))
    assert isinstance(result, ast.Import)
    assert result.names == [ast.alias(name='foo', asname=None)]


# Generated at 2022-06-14 01:46:28.232451
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    """Unit test for method visit_Import of class BaseImportRewrite."""
    from ..testcases import equal

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('old', 'new')
        ]

    result = TestBaseImportRewrite.transform(
        ast.parse("import old")
    )
    equal(result.tree,
          ast.parse("try:\n    import old\nexcept ImportError:\n    import new"))


# Generated at 2022-06-14 01:46:37.780474
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Testable(BaseImportRewrite):
        rewrites = [('foo', 'bar'), ('foo', 'baz')] # type: List[Tuple[str, str]]

    import baz.bar.baz


# Generated at 2022-06-14 01:46:45.382925
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    ast_st = ast.parse("import json").body[0]
    trans_cls = BaseImportRewrite
    trans_cls.rewrites = [('json', 'json_mul')]
    trfrm_res = trans_cls.transform(ast_st)
    assert trfrm_res.dependencies == trans_cls.dependencies
    assert isinstance(trfrm_res.tree, ast.Try)


# Generated at 2022-06-14 01:46:53.488221
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from os.path import dirname, join


# Generated at 2022-06-14 01:47:01.954804
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import python_to_ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = python_to_ast('''
import foo
import baz
''')
    TestImportRewrite.transform(tree)
    assert tree == python_to_ast('''
try:
    import foo
except ImportError:
    import bar
import baz
''')



# Generated at 2022-06-14 01:47:10.557235
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('urllib', 'urllib.request')]

    source = """
    from urllib.parse import urlparse
    from urllib import parse
    from urllib.request import urlopen
    """

    tree = ast.parse(source)
    TestImportRewrite.transform(tree)

# Generated at 2022-06-14 01:47:28.712117
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    class FakeImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'foo_new'), ('bar', 'bar_new')]

    class FakeImportRewrite_RewriteInside(BaseImportRewrite):
        rewrites = [('foo.bar', 'foo.bar_new')]

    result = FakeImportRewrite.transform(ast.parse(textwrap.dedent(
        """
        import foo
        import bar

        import foo.bar
        import foo.bar.baz
        """
    )))

    assert result.has_changes

# Generated at 2022-06-14 01:47:36.358823
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    @snippet
    def module(foo):
        import foo
        foo.bar()

    @snippet
    def module_rewrite(new_foo):
        try:
            import foo
        except ImportError:
            import new_foo
        new_foo.bar()

    trans = BaseImportRewrite(target='')
    trans.rewrites = [('foo', 'new_foo')]

    result = trans.transform(module)
    assert result.tree == module_rewrite
    assert result.changed is True
    assert result.dependencies == []


# Generated at 2022-06-14 01:47:45.907662
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')]

    class Test(unittest.TestCase):
        def test(self):
            import_ = ast.Import(names=[
                ast.alias(name='foo.blah.blah',
                          asname='blah')])


# Generated at 2022-06-14 01:47:48.028636
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # create the tree
    tree = ast.parse("""import foo""")

    class A(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    # transform it
    r = A.transform(tree)

    # check it
    assert r.tree.body[0].body[0].body[0].names[0].name == 'foo'
    assert r.dependencies == ['bar']



# Generated at 2022-06-14 01:47:57.634785
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.codegen import to_source

    class TestTransformer(BaseImportRewrite):
        target = 'python'
        rewrites = [('foo', 'bar')]

    tree = ast.parse('from foo import wheel')
    result = TestTransformer.transform(tree)
    expected = ast.parse('try:\n    import wheel\nexcept ImportError:\n    from bar import wheel')
    assert to_source(expected) == to_source(result.tree)
    assert result.tree_changed

    tree = ast.parse('from foo import wheel as foo_wheel')
    result = TestTransformer.transform(tree)
    expected = ast.parse('try:\n    import wheel as foo_wheel\nexcept ImportError:\n    from bar import wheel as foo_wheel')
    assert to_source(expected) == to_source

# Generated at 2022-06-14 01:48:01.758632
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    class Test(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
    tree = ast.parse('import foo')
    result = Test.transform(tree)
    assert result.changed
    assert result.dependencies == ['bar']


# Generated at 2022-06-14 01:48:09.164949
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import transform
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]

    transformer = TestBaseImportRewrite(None)

    code_import_rewrite = """
foo

import old
import bar

foo
"""
    expected_code_import_rewrite = """
foo

try:
    import old
except ImportError:
    import new as old


import bar

foo
"""
    tree = transform.parse(code_import_rewrite)
    transformer.visit(tree)
    assert transform.to_source(tree) == expected_code_import_rewrite

    code_import_not_rewrite = """
foo

import bar

foo
"""
    tree = transform.parse(code_import_not_rewrite)
    transformer

# Generated at 2022-06-14 01:48:18.676390
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    transformer = BaseImportRewrite
    transformer.rewrites = [
        ('old_module', 'new_module')
    ]

    node = ast.ImportFrom(module='old_module',
                          names=[ast.alias(name='name_1',
                                           asname=None),
                                 ast.alias(name='name_2',
                                           asname=None),
                                 ast.alias(name='name_3',
                                           asname=None)],
                          level=0)
    node_ = transformer.visit_ImportFrom(node)
    assert isinstance(node_, ast.Try)

    node_ = node_.body[0]
    assert isinstance(node_, ast.ImportFrom)
    assert node_.module == 'new_module'
    for alias in node_.names:
        assert alias

# Generated at 2022-06-14 01:48:29.340217
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # test module import
    import_from_module = "from test_module.a import b"
    import_from_module_rewrite = "from test_module.b import b"
    import_from_module_tree = ast.parse(import_from_module)
    import_from_module_rewrite_tree = ast.parse(import_from_module_rewrite)

    class TestImportFromModule(BaseImportRewrite):
        rewrites = [("test_module.a", "test_module.b")]

    result = TestImportFromModule.transform(import_from_module_tree)
    assert result == TransformationResult(import_from_module_rewrite_tree, True, [])

    # test names import
    import_from_names = "from test_module import foo, bar"
    import_from_names_

# Generated at 2022-06-14 01:48:35.710265
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    src = 'import foo'
    tree = ast.parse(src)
    rewriting_class = type('Test', (BaseImportRewrite,), {'rewrites': [('foo', 'bar')]})
    rewriting_class.transform(tree)

    import_result = ast.parse('try:\n    import foo\nexcept ImportError:\n    import bar')
    assert ast.dump(tree, include_attributes=True) == ast.dump(import_result, include_attributes=True)


# Generated at 2022-06-14 01:48:55.538801
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('test_1', 'test_2'),
        ]

    transformer = TestTransformer(None)
    import_node = ast.parse('import test_1')
    rewrote = transformer.visit_Import(import_node.body[0])

# Generated at 2022-06-14 01:49:04.715421
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astrewrite_test.transformers.unittest

    import unittest
    import ast
    import astunparse

    class Test(unittest.TestCase):
        def setUp(self):
            self.t = astrewrite_test.transformers.unittest.Test()

        def get_tree(self, code):
            return ast.parse(code)

        def test_Import(self):
            code = '''import re'''
            tree = self.get_tree(code)
            self.t.transform(tree)
            self.assertEqual(astunparse.unparse(tree),
                             '''import re
try:
    import re
except ImportError:
    pass''')

        def test_Import_with_alias(self):
            code = '''import re as regex'''


# Generated at 2022-06-14 01:49:16.211810
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('collections.abc', 'collections'),
            ('collections.defaultdict', 'collections')
        ]

    code = textwrap.dedent('''\
        import collections.abc

        def test_method():
            import collections.defaultdict
            import collections.abc.Counter
    ''')
    tree = ast.parse(code).body

    TestTransformer.transform(tree)


# Generated at 2022-06-14 01:49:26.799907
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestClass(BaseImportRewrite):
        rewrites = [('foo.bar', 'foo_bar')]


# Generated at 2022-06-14 01:49:38.513426
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import CompilationTarget
    import astor

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('time', 'datetime'),
        ]
        target = CompilationTarget()

    assert TestImportRewrite.transform(ast.parse('import time')) == \
        TransformationResult(
            ast.parse('try:\n    import time\nexcept ImportError:\n    import datetime'),
            True,
            ['time'])

    assert TestImportRewrite.transform(ast.parse('import time as t')) == \
        TransformationResult(
            ast.parse('try:\n    import time as t\nexcept ImportError:\n    import datetime as t'),
            True,
            ['time'])


# Generated at 2022-06-14 01:49:49.007658
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six.moves.urllib_parse')
        ]

    test_tree = ast.parse('import six.moves.urllib.parse')
    expected_tree = ast.parse('''
        try:
            import six.moves.urllib.parse
        except ImportError:
            import six.moves.urllib_parse.parse
    ''')

    result_tree = ast.fix_missing_locations(TestTransformer.transform(test_tree).tree)
    assert result_tree == expected_tree



# Generated at 2022-06-14 01:50:03.308380
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typed_astunparse, ast
    import sys
    import os.path
    
    sys.path.append(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..","test_utils"))
    import utils
    

# Generated at 2022-06-14 01:50:13.781856
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(module='my_module',
                                 names=[ast.alias(name='my_class'),
                                        ast.alias(name='my_function')],
                                 level=0)

    import_from_unrelated = ast.ImportFrom(module='unrelated',
                                           names=[ast.alias(name='my_class'),
                                                  ast.alias(name='my_function')],
                                           level=0)

    import_from_module_with_wildcard = ast.ImportFrom(module='my_module',
                                                      names=[ast.alias(name='*')],
                                                      level=0)

    class TestTransformer(BaseImportRewrite):
        rewrites = [('my_module', 'my_module_rewrite')]


# Generated at 2022-06-14 01:50:20.236205
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Rewriter(BaseImportRewrite):
        rewrites = [('a', 'awdawd')]

        def visit_Import(self, node):
            return ast.Import(names=[ast.alias(name='dawdad')])
    actual = Rewriter.transform(ast.parse("import a.b"))
    assert actual.code == "import awdawd.b"
    assert actual.changed


# Generated at 2022-06-14 01:50:28.391679
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ExampleTransformer(BaseImportRewrite):
        target = 'python2'
        rewrites = [('six', 'six'),
                    ('pip._vendor.requests.packages.urllib3.contrib.pyopenssl',
                     'urllib3.contrib.pyopenssl')]

        def visit_Import(self, node):
            return super().visit_Import(node)


# Generated at 2022-06-14 01:50:57.028373
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from _ast import Import, alias

    # Replacements
    class DummyTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')]

    case = DummyTransformer.visit_Import(Import(names=[alias(name='foo', asname='foobar')]))
    assert isinstance(case, ast.Try)  # type: ignore
    assert len(case.handlers) == 1
    assert isinstance(case.handlers[0], ast.ExceptHandler)  # type: ignore
    assert isinstance(case.body[0], ast.Import)  # type: ignore
    assert case.body[0].names == [alias(name='foo', asname='foobar')]
    assert len(case.orelse) == 1

# Generated at 2022-06-14 01:51:03.516806
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('test.test', 'test')]

    code = """
    from test.test import X
    from test.test import Y, Z
    """
    tree = ast.parse(code)
    tree = TestImportRewrite.transform(tree)
    print(astor.to_source(tree))

    assert astor.to_source(tree) == """
    try:
        from test import (X,
        Y,
        Z)
    except ImportError:
        from test.test import (X,
        Y,
        Z)

    """


# Generated at 2022-06-14 01:51:11.443383
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('distutils', 'setuptools')]

    tree = ast.parse("from distutils.core import setup")
    result = ImportRewrite.transform(tree)
    assert isinstance(tree.body[0], ast.Try)
    assert isinstance(tree.body[0].body[0], ast.Import)
    assert tree.body[0].body[0].names[0].name == 'setuptools.core'
    assert result.changed

    tree = ast.parse("from distutils import core")
    result = ImportRewrite.transform(tree)
    assert isinstance(tree.body[0], ast.Try)
    assert isinstance(tree.body[0].body[0], ast.Import)

# Generated at 2022-06-14 01:51:22.969253
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import ast

    import_from_1 = ast.ImportFrom(
        module='DateTime',
        names=[ast.alias(name='DateTime', asname='DateTime')],
        level=0)

    import_from_2 = ast.ImportFrom(
        module='DateTime',
        names=[ast.alias(name='DateTime', asname='DateTime')],
        level=0)

    r = BaseImportRewrite(import_from_1)

    expected = """try:
    import DateTime
except ImportError:
    import gen_DateTime
"""

    BaseImportRewrite.rewrites = [('DateTime', 'gen_DateTime')]
    actual = astor.to_source(r.visit(import_from_2)).strip()

    assert actual == expected


# Generated at 2022-06-14 01:51:32.539511
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class Rewrite_A_to_B(BaseImportRewrite):
        rewrites = [('A', 'B')]

    tree = ast.parse('''
import A
A.something
import C
''')
    result = Rewrite_A_to_B.transform(tree)
    assert result.changed
    assert astor.to_source(tree) == '''
try:
    import A
except ImportError:
    import B
B.something
import C
'''

    class Rewrite_Aaa_to_Bbb(BaseImportRewrite):
        rewrites = [('Aaa', 'Bbb')]

    tree = ast.parse('''
import Aaa
Aaa.something
''')
    result = Rewrite_Aaa_to_Bbb.transform(tree)


# Generated at 2022-06-14 01:51:45.990629
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import six
    tree = ast.parse('''
import six
''')
    bir = BaseImportRewrite.transform(tree)
    assert bir._tree.body[0].body[0].value.lineno == 1
    assert bir._tree.body[0].body[0].value.col_offset == 1
    assert bir._tree.body[0].body[0].value.handlers[0].type.lineno == 1
    assert bir._tree.body[0].body[0].value.handlers[0].type.col_offset == 7
    assert isinstance(bir._tree.body[0].body[0].value.handlers[0].type.name,
                      ast.Name)

# Generated at 2022-06-14 01:51:54.722116
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .test_utils import a, b
    from .test_utils import regenerate_callee_source
    import os
    import sys

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_files'))
    sys.path.insert(0, root_dir)

    class ReformatImports(BaseImportRewrite):
        rewrites = [
            ('test_utils.a', 'test_utils_a'),
            ('test_utils.b', 'test_utils_b')]


# Generated at 2022-06-14 01:52:02.521224
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    before = ast.parse("""
from builtins import range
""")

    class MockTransformer(BaseImportRewrite):
        rewrites = [
            ('builtins', '__builtin__'),
        ]

    after = ast.parse("""
try:
    from builtins import range
except ImportError:
    from __builtin__ import range
""")

    assert after == MockTransformer.transform(before).transformed_tree

if __name__ == '__main__':
    test_BaseImportRewrite_visit_Import()

# Generated at 2022-06-14 01:52:09.931735
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    original = ast.parse('''
import mod1
''')
    replacement = ast.parse('''
try:
    import mod1
except ImportError:
    import _mod1 as mod1
''')

    class Transformer(BaseImportRewrite):
        rewrites = [
            ('mod1', '_mod1')
        ]

    result = Transformer.transform(original)
    assert astor.to_source(result.tree) == astor.to_source(replacement)



# Generated at 2022-06-14 01:52:20.468836
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Setup
    tree = ast.parse('from foo import *, bar as b\n')
    cls = BaseImportRewrite.with_args(rewrites=[('foo', 'baz')])

    # Act
    try_stmt = cls.visit_ImportFrom(tree.body[0])

    # Assert
    assert isinstance(try_stmt, ast.Try)
    assert len(try_stmt.handlers) == 1
    assert isinstance(try_stmt.handlers[0], ast.ExceptHandler)
    assert try_stmt.handlers[0].type is None
    assert isinstance(try_stmt.body[0], ast.ImportFrom)
    assert try_stmt.body[0].module == 'foo'

# Generated at 2022-06-14 01:53:05.486528
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom(): 
    from ..utils.tests.data import TEST_IMPORT_FROM_STATEMENTS
    from .asserts import assert_ast_equal
    from .utils import get_node
    for import_statement, expected_rewrite, expected_changed in TEST_IMPORT_FROM_STATEMENTS:
        class Rewrite(BaseImportRewrite):
            rewrites = [(input_module, output_module) 
                        for input_module, output_module in 
                        rewrited_modules]
        rewrite = Rewrite(get_node(import_statement))
        assert_ast_equal(expected_rewrite, rewrite.visit(get_node(import_statement)))
        assert expected_changed == rewrite._tree_changed



# Generated at 2022-06-14 01:53:13.888020
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys; sys.modules.pop('compiler', None)

    class BaseImportRewriteTest(BaseImportRewrite):
        rewrites = [('old_module', 'new_module'),
                    ('old_module.submodule', 'new_module.submodule')]

    text = 'import old_module'
    tree = ast.parse(text)
    result, _, _ = BaseImportRewriteTest.transform(tree)

# Generated at 2022-06-14 01:53:21.871598
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    source = 'from mymodule.mypackage import myclass'
    tree = ast.parse(source)
    node = next(tree.body[0].body[0].body[0].body[0].body)

    rewrites = [('mymodule.mypackage', 'mymodule_rewrite.mypackage_rewrite')]

    expected = '''
try:
    from mymodule.mypackage import myclass
except ImportError:
    from mymodule_rewrite.mypackage_rewrite import myclass
'''.strip()

    class Transformer(BaseImportRewrite):
        rewrites = rewrites

    actual = Transformer.transform(tree).tree

    assert ast.dump(actual) == expected

# Generated at 2022-06-14 01:53:28.673669
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    target = CompilationTarget(major=3, minor=5)
    module = ast.parse('import itertools')
    rewrites = [
        ('itertools', 'more_itertools')
    ]
    class Transformer(BaseImportRewrite):
        target = target
        rewrites = rewrites
    result = Transformer.transform(module)
    node = ast.parse('try:\n    import itertools\nexcept ImportError:\n    import more_itertools as itertools')
    assert result.tree == node


# Generated at 2022-06-14 01:53:37.665599
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from ..utils.tester import transform_and_compare

    node = ast3.parse('import x')
    rewritter = BaseImportRewrite(node)
    rewritter.visit(node)
    assert not rewritter._tree_changed

    rewritter.visit(ast3.parse('import xx'))
    assert rewritter._tree_changed
    assert rewritter.transform(node).tree == transform_and_compare(node, 'try:\n    import x\nexcept ImportError:\n    import xx\n')


# Generated at 2022-06-14 01:53:47.980251
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import_rewrite = BaseImportRewrite()
    import_rewrite.rewrites = [('six', 'six.moves')]

    import_node = ast.parse("import six")
    expected_output = astor.to_source(import_rewrite._replace_import(import_node, 'six', 'six.moves'))
    actual_output = astor.to_source(import_rewrite.visit(import_node))
    assert expected_output == actual_output

    import_rewrite.rewrites = []

    import_node = ast.parse("import six")
    expected_output = astor.to_source(import_node)
    actual_output = astor.to_source(import_rewrite.visit(import_node))
    assert expected_output == actual_output




# Generated at 2022-06-14 01:53:53.041516
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transform(BaseImportRewrite):
        rewrites = [('test', 'tests')]

    source = '''
    import test
    '''

    expected = '''
    try:
        import test
    except ImportError:
        import tests
    '''

    with Transform.run_on(source) as result:
        assert result.tree_changed is True

    assert result.code == expected



# Generated at 2022-06-14 01:54:01.845912
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Mock(BaseImportRewrite):
        rewrites = [
            ('a', 'b')
        ]

    tree = ast.parse('from a.b import c, d as e\nx = a')
    assert(Mock.transform(tree).tree.body[0].value.module == 'b.b')
    assert(Mock.transform(tree).tree.body[0].value.names[0].name == 'c')
    assert(Mock.transform(tree).tree.body[0].value.names[1].name == 'd')
    assert(Mock.transform(tree).tree.body[0].value.names[1].asname == 'e')
    tree = ast.parse('import a')