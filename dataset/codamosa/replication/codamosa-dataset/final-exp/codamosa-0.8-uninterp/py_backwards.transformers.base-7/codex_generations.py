

# Generated at 2022-06-14 01:44:19.065214
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    transformer = BaseImportRewrite()
    transformer.rewrites = [('six', 'pysix_compat')]
    import_from_tree = ast.parse('from six import reraise as reraise_six')
    replaced_import_from = ast.parse('try:\n    from pysix_compat import reraise as reraise_six\n'
                                     'except ImportError:\n    from six import reraise as reraise_six\n')

    assert transformer.visit(import_from_tree) == replaced_import_from

# Generated at 2022-06-14 01:44:29.402730
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import test_import1
    old_code = "from test_import1 import TestImport"
    import test_import2
    new_code = "from test_import2 import TestImport"
    method_name = 'visit_Import'
    class_name = 'BaseImportRewrite'
    node = ast.parse(old_code).body[0]
    cls = getattr(sys.modules[__name__], class_name)
    instance = cls(None)
    instance.rewrites = [(old_code.split(" ")[1], new_code.split(" ")[1])]
    new_node = getattr(instance, method_name)(node)
    assert new_node.body[0].handlers[0].type.id == 'ImportError'

# Generated at 2022-06-14 01:44:41.488555
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import re
    import typing as t
    import astor as a

    rewrites = [('_re', 're'), ('typing', 't')]

    class Rewriter(BaseImportRewrite):
        rewrites = rewrites

    tree = ast.parse('import re; import typing as t')
    Rewriter.transform(tree)
    assert a.to_source(tree) == ('import re; '
                                 'try:\n'
                                 '    import re\n'
                                 'except ImportError:\n'
                                 '    import _re as re\n'
                                 'try:\n'
                                 '    import t\n'
                                 'except ImportError:\n'
                                 '    import typing as t')


# Generated at 2022-06-14 01:44:50.274735
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from_ = "unittest_module"
    to = "some_module"
 
    import_ = ast.ImportFrom(module=from_,
        names=[
            ast.alias(name="Test", asname=None),
            ast.alias(name="TestCase", asname=None)],
        level=0)

    trans = BaseImportRewrite()
    trans.rewrites = [(from_, to)]
    result = trans.visit_ImportFrom(import_)

    assert isinstance(result, ast.Try)
    assert result.finalbody == []
    assert len(result.handlers) == 1
    assert result.handlers[0].name == None
    assert result.handlers[0].type.id == 'ImportError'
    assert result.handlers[0].body[0].value.func.attr

# Generated at 2022-06-14 01:45:01.700595
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # set up
    import_from = ast.parse('from my_module import abc, fgh, xyz').body[0]

    class Transformer(BaseImportRewrite):
        dependencies = []
        rewrites = [('my_module', 'other_module')]

    assert Transformer.transform(import_from).tree == \
        ast.parse('try:\n    from other_module import abc, fgh, xyz\nexcept ImportError:\n    from my_module import abc, fgh, xyz').body[0]

    import_from = ast.parse('from my_module import abc, fgh').body[0]

    class Transformer(BaseImportRewrite):
        dependencies = []
        rewrites = [('my_module.abc', 'other_module')]


# Generated at 2022-06-14 01:45:09.256797
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse("""
import module
""")

    class MockRewriter(BaseImportRewrite):
        rewrites = [('module', 'mock')]

    trans = MockRewriter.transform(tree)
    assert trans.modified

    expected = ast.parse("""
try:
    import module
except ImportError:
    import mock
""")

    assert ast.dump(trans.tree) == ast.dump(expected)



# Generated at 2022-06-14 01:45:19.813632
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # GIVEN
    tree = ast.parse('''
from flask import Flask
from flask.json import JSONEncoder

try:
    from flask.json import JSONEncoder as JSONEncoder_
except ImportError:
    from flask_rest_jsonapi.jsonapi_jr import JSONEncoder as JSONEncoder_
''')
    new_rewrite = ('flask.json', 'flask_rest_jsonapi.jsonapi_jr')
    transformer = BaseImportRewrite(tree)
    transformer.rewrites = [(rewrite, new_rewrite) for rewrite, new_rewrite in transformer.rewrites] + [new_rewrite]

    # WHEN
    result = transformer.transform(tree)

    # THEN
    assert transformer._tree_changed

# Generated at 2022-06-14 01:45:27.500426
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    body = ast.parse("""
    import a
    import b
    """).body

    rewrites = [('a', 'c')]

    class TestTransformer(BaseImportRewrite):
        rewrites = rewrites

    target = CompilationTarget.PYTHON_36
    expected = parse("""
    try:
        import a
    except ImportError:
        import c
    import b
    """).body

    result = TestTransformer.transform(target, body)
    assert result.changed, "Import rewrite should change tree"
    assert result.tree == expected


# Generated at 2022-06-14 01:45:32.152663
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('mock', 'unittest.mock')]

    tree = ast.parse('import mock')
    assert ast.dump(TestTransformer.transform(tree)[0]) == """Module(body=[Import(names=[alias(name='unittest.mock', asname=None)])])"""



# Generated at 2022-06-14 01:45:40.593558
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import _ast as ast

    from ..version import parse_version

    if parse_version(ast.__version__) < parse_version('0.4'):
        import sys
        sys.modules['typed_ast'] = None  # type: ignore

    from typed_ast import ast3 as ast
    import astunparse



# Generated at 2022-06-14 01:46:03.066900
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import astunparse

    class ImportRewriteTest(unittest.TestCase):
        def setUp(self):
            self.rewrites = [
                ('os', 'myos'),
                ('json', 'myjson')]

            class Mock(BaseImportRewrite):
                rewrites = self.rewrites

            self.transformer = Mock(ast.Module(body=[]))


        def test_import_from_none(self):
            node = ast.ImportFrom(module='xml',
                                  names=[
                                      ast.alias(name='ParseError',
                                                asname=None)],
                                  level=0)
            new_node = self.transformer.visit_ImportFrom(node)

# Generated at 2022-06-14 01:46:08.737219
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.source_snippets import source
    from ..utils.ast_tools import parse_ast_tree, compare_ast

    source_code = source('''
        import re

        ''')

    tree = parse_ast_tree(source_code)
    BaseImportRewrite.rewrites = [('re', 'regex')]

    new_tree = BaseImportRewrite.transform(tree).new_tree
    expected_code = source('''
        try:
            extend(re)
        except ImportError:
            extend(regex)

        ''')

    compare_ast(expected_code, new_tree)


# Generated at 2022-06-14 01:46:19.646088
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(
        level=0,
        module='foo',
        names=[
            ast.alias(name='bar', asname='baz')
        ]
    )
    rewrites = BaseImportRewrite(None)
    rewrites.rewrites = [
        ('foo', 'rewritten_foo')
    ]
    new_import_from = rewrites.visit_ImportFrom(import_from)
    assert new_import_from.__class__.__name__ == 'Try'
    assert new_import_from.body[0].__class__.__name__ == 'ImportFrom'
    assert new_import_from.body[0].module == 'rewritten_foo'
    assert new_import_from.body[0].names[0].name == 'bar'

# Generated at 2022-06-14 01:46:31.060228
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class DummyTransformer(BaseImportRewrite):
        rewrites = [('six', 'six.moves')]

    code = '''
import six
'''
    tree = ast.parse(code)

    new_tree = DummyTransformer.transform(tree).tree

    try:
        import six.moves as six  # noqa
    except ImportError:
        six = None

    assert isinstance(new_tree, ast.Try)
    assert isinstance(new_tree.body[0], ast.Import)
    assert new_tree.body[0].names[0].name == 'six'
    assert new_tree.body[0].names[0].asname == 'six'
    assert len(new_tree.body) == 1


# Generated at 2022-06-14 01:46:42.702157
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    code = '''\
from urllib2 import urlopen
import shutil
'''
    tree = ast.parse(code)
    new_tree = ast.parse(code)
    rewrites = [('urllib2', 'urllib.request')]
    new_class = type('NewClass', (BaseImportRewrite,), {'rewrites': rewrites})
    new_class(new_tree).visit(new_tree)
    assert 'urllib2' not in new_tree.dump()
    assert 'urllib.request' in new_tree.dump()

# Generated at 2022-06-14 01:46:52.133729
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('timestamp.tz', 'timestamp.tz_fixed')]

    t = Test(None)

    def compare(source, expected):
        t = Test(ast.parse(source))
        parsed = ast.dump(t.visit(ast.parse(source)))
        assert parsed == ast.dump(ast.parse(expected))

    compare('import timestamp.tz',
            'try:\n    extend(import timestamp.tz)\nexcept ImportError:\n    extend(import timestamp.tz_fixed)')
    compare('import timestamp.tz.timestamp',
            'try:\n    extend(import timestamp.tz)\nexcept ImportError:\n    extend(import timestamp.tz_fixed)')
    compare('import timestamp',
            'import timestamp')



# Generated at 2022-06-14 01:47:06.528329
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_rewrite_base = BaseImportRewrite()
    import_rewrite_base.rewrites = []
    import_rewrite_base._tree_changed = False

    # Replace import from for module
    import_rewrite_base.rewrites = [('os', 'pathlib')]
    node1 = ast.parse("import os")
    node2 = import_rewrite_base.visit(node1)

    assert(node2.body[0].body[0].value.body.module == 'pathlib')
    assert(isinstance(node2, ast.Try))

    # Replace import from for module
    import_rewrite_base.rewrites = [('os', 'pathlib')]
    node3 = ast.parse("import os.path")
    node4 = import_rewrite_base.visit(node3)

# Generated at 2022-06-14 01:47:16.915011
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Given:
    node = ast.ImportFrom(module="tensorflow", names=[ast.alias(name="*", asname=None)], level=0)
    tree = ast.parse("")

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON
        rewrites = [("tensorflow", "tf")]

    # When:
    transformed = TestTransformer.transform(tree)

    # Then:
    import_module_and_names = ast.ImportFrom(module="tf",
                                             names=[ast.alias(name="*",
                                                              asname=None)],
                                             level=0)
    except_block = ast.ExceptHandler(
        type=None,
        name=None,
        body=[import_module_and_names])
   

# Generated at 2022-06-14 01:47:25.342648
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.mock_ast import mock_ast
    from ..utils.mock_ast import get_node_names

    def get_result(original):
        from typed_ast.ast3 import parse
        from ..utils import transform

        @transform(CompilationTarget.PYTHON3)
        class Test(BaseImportRewrite):
            rewrites = [
                ('setuptools', 'distutils'),
                ('setuptools.command', 'distutils.command')
            ]
            dependencies = []

        tree = parse(original)
        result = Test(tree).visit(tree)
        return get_node_names(result)

    def get_expect(original, expect):
        from ..utils.mock_ast import get_transformed_code
        from ..utils import transform


# Generated at 2022-06-14 01:47:35.917047
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils import assert_ast_same

    class Test(BaseImportRewrite):
        rewrites = [('old_module', 'new_module')]

    tree = ast.parse('import old_module')
    result = Test.transform(ast.Module(body=[tree.body[0]]))
    expected = ast.Try(body=[
        ast.Import(names=[ast.alias(name='new_module', asname=None)]),
        ast.ExceptHandler(body=[ast.Import(names=[ast.alias(name='old_module', asname=None)])],
                          type=None,
                          name=None)],
                       orelse=[],
                       finalbody=[])

    assert_ast_same(result.tree.body[0], expected)


# Unit

# Generated at 2022-06-14 01:47:57.181037
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    @snippet
    def test(a, b, c):
        from module.a import X, Y  # type: ignore
        Y.x()

    @snippet
    def test_rewrote(a, b, c):
        try:
            from module.a import X, Y  # type: ignore
        except ImportError:
            from new_module.a import X, Y  # type: ignore
        Y.x()

    s = test.get_source()
    t = ast.parse(s)
    transformer = BaseImportRewrite([('.module.a', '.new_module.a')])
    new_tree = transformer.transform(t)
    assert test_rewrote.get_source() == new_tree

# Generated at 2022-06-14 01:48:04.802441
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.helpers import transformed_tree, check_tree_equality, input_with_changes

    for old_input, new_input in input_with_changes(
            'import PySide',
            'import PyQt5'):
        class Replacement(BaseImportRewrite):
            rewrites = [('PySide', 'PyQt5')]

        tree = ast.parse(old_input)
        new_tree = ast.parse(new_input)

        check_tree_equality(
            transformed_tree(Replacement, tree),
            new_tree)



# Generated at 2022-06-14 01:48:13.829501
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils.tree import compare_trees

    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    class ExpectedTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

        def visit_Import(self, node):
            if node.names[0].name == 'foo' or node.names[0].name.startswith('foo.'):
                return import_rewrite.get_body(previous=node,  # type: ignore
                                               current=self._replace_import(node, 'foo', 'bar'))[0]
            return self.generic_visit(node)

    code = 'import foo'
    tree = ast.parse(code)
    expected_tree = ast

# Generated at 2022-06-14 01:48:24.113309
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # python3.4:
    assert BaseImportRewrite().visit_Import(ast.parse("import requests").body[0]) == ast.parse("import requests").body[0]
    # python2.7:
    assert BaseImportRewrite().visit_Import(ast.parse("import requests").body[0]) == ast.parse("import requests").body[0]

    assert BaseImportRewrite(rewrites=[("requests", "new_requests")]).visit_Import(
        ast.parse("import requests").body[0]) == \
           ast.parse("""\
try:
    import requests
except ImportError:
    import new_requests
""").body[0]


# Generated at 2022-06-14 01:48:32.509771
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.base import BaseNodeTransformerTest as TestCase
    from ..types import CompilationTarget
    from .transforms_common.unittest_fixtures import TEST_REWRITES

    class ImportRewrite(BaseImportRewrite):
        target = CompilationTarget.PY2
        rewrites = TEST_REWRITES

    class Test(TestCase):
        TRANSFORMER = ImportRewrite
        CODE_TO_TRANSFORM = 'from module import value'
        EXPECTED_CODE = 'from module import value'
        TESTS = [
            dict(
                module_name='_import_rewrite'),
        ]

    Test().run_tests()



# Generated at 2022-06-14 01:48:41.018745
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils.snippet import snippet, extend

    @snippet
    def import_rewrite(previous, current):
        try:
            extend(previous)
        except ImportError:
            extend(current)

    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ('os', 'fake_os'),
            ('time', 'fake_time'),
        ]

    def convert(tree: ast.AST) -> ast.AST:
        return astor.to_source(tree).replace(
            ' ', ''
        ).replace(
            '\n', ''
        ).replace(
            '\t', ''
        )


# Generated at 2022-06-14 01:48:49.102777
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    name_node = ast.alias(name='six')
    import_node = ast.Import(names=[name_node])
    tree = ast.AST()
    setattr(tree, 'body', [import_node])
    class Rewrite(BaseImportRewrite):
        rewrites = [('six', 'sixer')]

    import_rewrite, _ = Rewrite.transform(tree)
    assert import_rewrite.body[0].handlers[0].body[0].names[0].name == 'six'
    assert import_rewrite.body[0].handlers[0].body[1].names[0].name == 'sixer'



# Generated at 2022-06-14 01:48:59.024123
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..tests.utils import compare_ast

    # TODO: implement
    rewrites = [
        ('foo', 'bar'),
    ]
    node = ast.ImportFrom(module='foo',
                          names=[ast.alias(name='a'), ast.alias(name='b', asname='c')],
                          level=2)
    class_node = type('Foo', (BaseImportRewrite,), {'rewrites': rewrites})
    btr = class_node(node)
    try_node = btr.visit(node)
    assert type(try_node) == ast.Try
    assert not hasattr(try_node, 'finalbody')

    ex = None
    handler = None

# Generated at 2022-06-14 01:49:06.622361
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import typed_ast.ast3 as typed_ast

    tree = ast.parse('import a.Sample')
    node = tree.body[0]
    node2 = ast.parse('import a.Sample2')
    rewriter = BaseImportRewrite(tree)

    # Replace using "_replace_import"
    result = rewriter._replace_import(node, 'a', 'b')
    # Add import from "a" in the beginning of the "try" statement
    result.body.insert(0, node)
    result.body[1].names[0].asname = "Sample"


# Generated at 2022-06-14 01:49:17.890844
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    from testcases.common import MethodTestCase


# Generated at 2022-06-14 01:49:52.934008
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewrite = BaseImportRewrite([('test_module_name', 'test_module_name_rewrite')])
    body = []

    name = ast.alias(name='test_module_name', asname=None)
    import_from = ast.ImportFrom(module='test_module_name_rewrite',
                                 names=[name],
                                 level=0)
    try_ = ast.Try(body=[import_from], handlers=[], orelse=[], finalbody=[])
    body.append(try_)

    result = ast.Module(body=body)

    node = ast.ImportFrom(module='test_module_name',
                          names=[name],
                          level=0)
    assert isinstance(rewrite.visit(node), ast.Try)
    assert rewrite._tree == result
    assert rewrite.transform

# Generated at 2022-06-14 01:50:00.726009
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # given
    class Test(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    # when
    node = Test.visit_Import(Test, ast.parse('import foo').body[0])

    # then
    assert Test._tree_changed, 'AST must be changed.'
    assert str(node) == "try:\n    import bar\nexcept ImportError:\n    import foo", \
        'Module import must be rewritten'



# Generated at 2022-06-14 01:50:11.058881
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    import pylint.__pkginfo__
    import os.path
    # import os.path as a
    # this is the node to be transformed into try..catch
    node = ast.parse('''import pylint.__pkginfo__''').body[0]
    assert isinstance(node, ast.Import)

    alias = node.names[0]
    assert alias.name == 'pylint.__pkginfo__'
    assert alias.asname is None

    # C++ does not have __pkginfo__
    class TestTransformer(BaseImportRewrite):
        dependencies = []
        targets = [CompilationTarget.CPP]
        rewrites = [('pylint', 'pylint.__pkginfo__')]


# Generated at 2022-06-14 01:50:15.809847
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class RewriteA(BaseImportRewrite):
        rewrites = [('mymodule', 'newmodule')]

    tree = ast.parse('import mymodule')
    result = RewriteA.transform(tree)
    assert result.tree == ast.parse('import newmodule')
    assert result.changed
    assert RewriteA.dependencies == ['mymodule', 'newmodule']

# Generated at 2022-06-14 01:50:22.536923
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse

    class MyTransformer(BaseImportRewrite):
        rewrites = [('os', 'toos')]

    source = 'from os import path, remove'
    tree = ast.parse(source)
    MyTransformer.transform(tree)

    expected = '''\
try:
    from toos import path, remove
except ImportError:
    from os import path, remove
'''

    assert astunparse.unparse(tree) == expected



# Generated at 2022-06-14 01:50:27.109996
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    source = '''
    import foo
    '''
    tree = ast.parse(source)  # type: ast.AST
    BaseImportRewrite(tree).visit_Import(tree.body[0])
    expected = '''
    try:
        import foo
    except ImportError:
        import bar
    '''
    assert ast.dump(tree) == ast.dump(ast.parse(expected))


# Generated at 2022-06-14 01:50:38.067514
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from_example = ast.parse("from test import test").body[0]  # type: ast.ImportFrom
    imports_rewrites = [('.test', '.module.test')]
    class DynamicImportRewritter(BaseImportRewrite):
        rewrites = imports_rewrites
    rewritter = DynamicImportRewritter(ast.parse(""))
    result = rewritter.visit_ImportFrom(import_from_example)
    assert isinstance(result, ast.Try)
    assert len(result.handlers) == 1
    assert len(result.handlers[0].body) == 1
    assert isinstance(result.handlers[0].body[0], ast.ImportFrom)
    import_from = result.handlers[0].body[0]  # type: ast.ImportFrom

# Generated at 2022-06-14 01:50:49.486307
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('module_a', 'module_b')]
        

# Generated at 2022-06-14 01:51:00.307278
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from .test_utils import check_visitor

    class MyNodeTransformer(BaseImportRewrite):
        rewrites = [
            ('requests', 'mylib.requests'),
            ('aiohttp', 'mylib.aiohttp')]
    visitor = check_visitor(MyNodeTransformer)

    import_raw = ast3.parse('import requests').body[0]
    visitor.check(import_raw,
                  'try: import requests\nexcept ImportError:\n    import mylib.requests')

    import_as_raw = ast3.parse('import requests as req').body[0]
    visitor.check(import_as_raw,
                  'try: import requests as req\nexcept ImportError:\n    import mylib.requests as req')

    import_full_

# Generated at 2022-06-14 01:51:10.276874
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    with pytest.raises(TypeError):
        node = ast.Import(names=[ast.alias(name=1,
                                          asname=2)])
        BaseImportRewrite(ast.Module([node])).visit(node)

    node = ast.Import(names=[ast.alias(name='six',
                                      asname='six')])

# Generated at 2022-06-14 01:52:06.024125
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    input = """
    import os.path
    import os
    import math
    """
    tree = ast.parse(input)  # type: ast.Module
    rewrites = [('os', 'pathlib')]

    class Rewrite(BaseImportRewrite):
        rewrites = rewrites

    expected = """
    try:
        import pathlib.path
    except ImportError:
        import os.path
    import pathlib
    import os
    import math
    """

    result = Rewrite.transform(tree)
    assert expected == ast.fix_missing_locations(result.tree).body[0].body  # type: ignore
    assert result.changed



# Generated at 2022-06-14 01:52:13.555537
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Assert that when there is a name that matches a rewrite, the result
    # is a try/except statement containing a node with replaced name.
    class FooTransformer(BaseImportRewrite):
        rewrites = [('foo_module', 'bar_module')]

    node = ast.ImportFrom(level=0,
                          module='foo_module',
                          names=[ast.alias(name='foo_name',
                                           asname='foo_asname')])

    inst = FooTransformer(None)
    result = inst.visit(node)
    assert isinstance(result, ast.Try)
    assert len(result.handlers) == 1
    assert result.handlers[0].type.id == 'ImportError'
    assert result.handlers[0].name is None

# Generated at 2022-06-14 01:52:23.448689
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    class ImportRewriteTest(BaseImportRewrite):
        rewrites = [('requests', 'urllib')]

    node = ast.ImportFrom(module='requests',
                          names=[ast.alias(name='get',
                                           asname='make_get')])


# Generated at 2022-06-14 01:52:34.539379
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..compiler import compile_to_python

    class Rewriter(BaseImportRewrite):
        rewrites = [
            ('shlex', 'shutil')
        ]

    result = compile_to_python(
        '''
        from shlex import split
        from subprocess import Popen
        from shlex import foo
        import shlex
        import requests
        import shlex.bar
        ''',
        Rewriter
    )

# Generated at 2022-06-14 01:52:43.064060
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [('six', 'six'), ('six.moves', 'six.moves')]

    import_node = ast.parse('import six', mode='exec').body[0]
    transformed = Transformer.transform(import_node)
    transformed.tree  # type: ast.Try
    # end

    _, node = transformed.tree.handlers[0].body

    assert isinstance(node, ast.Import)
    assert node.names[0].name == 'six'

    import_node = ast.parse('import six.moves', mode='exec').body[0]
    transformed = Transformer.transform(import_node)
    transformed.tree  # type: ast.Try
    # end

    _, node = transformed.tree.handlers[0].body

   

# Generated at 2022-06-14 01:52:49.004851
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node = ast.parse("""
from sweet import translate
import ast
from ast import parse
from ast import parse as parse_alias
from ast import parse as parse_local, parse as parse_alias2, parse2
from . import parse as parse_as
""", mode='exec')
    BaseImportRewrite(node).visit_ImportFrom(node.body[1])

# Generated at 2022-06-14 01:52:58.426380
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astunparse
    # setup
    rewrites = [('urlparse', 'urllib.parse'), ]
    input_ = ast.parse("import urlparse")
    expected = ast.parse("try:\n    import urlparse\nexcept ImportError:\n    import urllib.parse")

    # test
    transformer = BaseImportRewrite(rewrites=rewrites)
    output_ = transformer.visit(input_)
    assert expected == output_
    assert astunparse.unparse(expected) == astunparse.unparse(output_)

    # cleanup - done automatically



# Generated at 2022-06-14 01:53:10.295574
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import CompilationTarget, TransformationResult
    from ..utils.ast_factory import ast_from_python

    class HasReplace(BaseImportRewrite):
        rewrites = [('os.path', 'pathlib')]

    class NoReplace(BaseImportRewrite):
        rewrites = [('os', 'pathlib')]

    NO_REPLACE = ast_from_python('import os')
    HAS_REPLACE = ast_from_python('import os.path')
    HAS_REPLACE_OTHER_NAME = ast_from_python('import os.path as path')


# Generated at 2022-06-14 01:53:20.298690
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typed_astunparse

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('some_module', 'other_module'),
            ('other_module.sub_module', 'other_module_new.sub_module'),
        ]

    tree = ast.parse(
        '''
import some_module as a
import other_module.sub_module as b
import other_module_new.sub_module as c
import other_module_new.sub_module.sub_sub_module as d
'''
        )

    transformed = TestTransformer.transform(tree)

    assert transformed.changed

# Generated at 2022-06-14 01:53:29.572196
# Unit test for method visit_Import of class BaseImportRewrite