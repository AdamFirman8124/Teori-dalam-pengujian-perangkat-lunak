

# Generated at 2022-06-14 01:44:11.416964
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]

    class TestImportRewrite2(BaseImportRewrite):
        rewrites = [('other', 'new')]

    node12 = ast.ImportFrom(level=0,
                            module='old',
                            names=[ast.alias(name='old_name',
                                             asname=None)])
    node13 = ast.ImportFrom(level=0,
                            module='old',
                            names=[ast.alias(name='new_name',
                                             asname='old_name')])
    node14 = ast.ImportFrom(level=0,
                            module='old',
                            names=[ast.alias(name='new_name',
                                             asname=None)])


# Generated at 2022-06-14 01:44:21.110447
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('six.moves.urllib.request', 'urllib.request'),
        ]


    node = ast.parse('import requests as req')
    tree = TestTransformer.transform(node)

    assert ast.dump(tree) == ast.dump(ast.parse('import requests as req'))

    node = ast.parse('import six.moves.urllib.request')
    tree = TestTransformer.transform(node)


# Generated at 2022-06-14 01:44:24.914773
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..transpilers import get_transpilers
    from .visitor import get_imports_and_names

    transpilers = [transpiler for transpiler in get_transpilers()
                   if BaseImportRewrite in type(transpiler).__bases__]

    for transpiler in transpilers:
        module = ast.parse('import {}'.format(transpiler.rewrites[0][0]))
        transpiler().visit(module)
        if transpiler.dependencies:
            imports, names = get_imports_and_names(module)
            assert len(imports) == 1 and len(names) == 1
            assert imports[0].names[0].name == transpiler.rewrites[0][1]


# Generated at 2022-06-14 01:44:33.241291
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = [
            ('some.module', 'new.module')
        ]

    old_node = ast.parse(
'''
import some.module
''').body[0]

    new_node = ast.parse(
'''
try:
    import some.module as some_module
except ImportError:
    import new.module as some_module
''').body[0]

    transformed = Transformer.transform(old_node)
    assert transformed.changed == True
    assert transformed.tree == new_node



# Generated at 2022-06-14 01:44:42.531799
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.tester import AbstractTransformerTester
    from ..utils.tester import UnimplementedTransformerTester
    from ..utils.tester import UnmodifiedTransformerTester

    # check if all methods are properly implemented
    class Dummy(BaseImportRewrite):
        pass

    tester = UnimplementedTransformerTester(Dummy,
                                            'BaseImportRewrite.transform',
                                            'BaseImportRewrite.visit_Import')
    tester.test()

    # tests

# Generated at 2022-06-14 01:44:54.049571
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class TestBaseImportRewrite_visit_Import(BaseImportRewrite):
        rewrites = [
            ('typed_ast.ast3', 'typed_ast')
        ]


# Generated at 2022-06-14 01:44:57.488196
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    code = ast.parse("import requests")
    expected_code = ast.parse("try:\n    import requests\nexcept ImportError:\n    import requests2")

    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ("requests", "requests2")
        ]

    actual_code = ImportRewrite.transform(code).tree

    assert ast.dump(expected_code) == ast.dump(actual_code)



# Generated at 2022-06-14 01:45:06.560148
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # sample
    import os
    os.path.join(os.path.dirname(__file__), 'test')

    class Test(BaseImportRewrite):
        rewrites = [('os', 'pathos')]

        def visit_Assign(self, node):
            return node

        def visit_Expr(self, node):
            return node

    tree = ast.parse(dedent(test_BaseImportRewrite_visit_Import.__doc__))
    res = Test.transform(tree)
    assert_equal(res.tree, ast.parse(dedent("""\
        try:
            import os
        except ImportError:
            import pathos
        pathos.path.join(pathos.path.dirname(__file__), 'test')
        """)))

# Generated at 2022-06-14 01:45:15.787281
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    original = ast.parse(
        """
import foo
from foo import bar
from foo import *
from foo import bar as baz, quux
"""
    )

    transformer = BaseImportRewrite()

    # transform needs to be done to get the visitor initialized
    Transformer.transform(transformer, original)

    def test(before, after):
        assert after == transformer.visit(before)

    # No rewrite
    test(ast.Import(names=[ast.alias(name='foo')]),
         ast.Import(names=[ast.alias(name='foo')]))
    test(ast.ImportFrom(module='foo', names=[ast.alias(name='bar')], level=0),
         ast.ImportFrom(module='foo', names=[ast.alias(name='bar')], level=0))

# Generated at 2022-06-14 01:45:27.027507
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Setting up testing objects
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]

    # type: Union[ast.Import, ast.Try]
    from_import = ast.Import(names=[ast.alias(name='six.moves',
                                              asname=None)])
    # type: Union[ast.Import, ast.Try]
    to_import = import_rewrite.get_body(previous=from_import,
                                        current=ast.Import(names=[ast.alias(name='six',
                                                                            asname=None)]))[0]

    # Testing BaseImportRewrite.visit_Import
    assert TestBaseImportRewrite.transform(from_import).tree == to_import


# Generated at 2022-06-14 01:45:42.838059
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo.bar', 'bar.baz'),
            ('foo.dummy', 'bar.dummy'),
        ]

    code = """
    from foo.bar import bar
    from foo.bar import baz
    from foo.bar import bar as bar_alias
    from foo.dummy import *
    from foo.bar.dummy import *
    from foo.bar.sub.dummy import *
    """

    tree = ast.parse(code)
    TestImportRewrite.transform(tree)


# Generated at 2022-06-14 01:45:52.207436
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(module='math',
                                 names=[ast.alias(name='sin',
                                                  asname=None)],
                                 level=0)

    rewrites = [('math', 'another_math')]
    tree, _, _ = BaseImportRewrite.transform(
        import_from, rewrites=rewrites)


# Generated at 2022-06-14 01:45:55.473607
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast

    class ImportTransformer(BaseImportRewrite):
        rewrites = [
            ('some.module', 'another.module')]


# Generated at 2022-06-14 01:46:02.640982
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .._testutils import assert_ast_equal

    class ExampleImportRewrite(BaseImportRewrite):
        rewrites = [('django', 'mysite.django')]

    node = ast.parse('from django.conf import settings')
    rewritten_node = ast.parse('''
try:
    from django.conf import settings
except ImportError:
    from mysite.django.conf import settings
''').body[0]

    result = ExampleImportRewrite.transform(node)
    assert result.changed
    assert_ast_equal(result.tree, rewritten_node)

# Generated at 2022-06-14 01:46:08.726813
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    tree = ast.parse("from __future__ import absolute_import")
    transformer = BaseImportRewrite(tree)
    node = transformer.visit(tree)
    assert astor.to_source(node) == "try:\n    from __future__ import absolute_import\nexcept ImportError:\n    pass\n"


# Generated at 2022-06-14 01:46:19.218010
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse
    import unittest.case
    import_rewrite_stmt = 'from __future__ import absolute_import'
    import_stmt = 'from typing import Dict'
    import_from_stmt = 'from typing import (Dict, List, Tuple)'
    import_from_with_alias_stmt = 'from typing import (Dict as d, List as l, Tuple as t)'
    tree = parse(import_stmt)
    results = BaseImportRewrite.transform(tree)
    assert type(results.tree) is ast.Import
    unittest.case.assert_equal(tree, results.tree)
    unittest.case.assert_equal(False, results.changed)
    tree = parse(import_from_stmt)
    results = BaseImportRew

# Generated at 2022-06-14 01:46:30.646324
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from . import helpers
    from ..types import CompilationTarget
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('os', 'pathlib')
        ]
        target = CompilationTarget.NODE
    tree = helpers.parse('''
import os
import os.path as path
from os import path
from os import *
''')
    result = TestTransformer.transform(tree)

    assert result.changes == True

# Generated at 2022-06-14 01:46:45.021460
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    import unittest
    import astor
    from typed_ast import ast3 as ast

    class Transformer(BaseImportRewrite):
        rewrites = [('old', 'new')]

    def compare(original: str, expected: str) -> None:
        root = ast.parse(original)

        transformer = Transformer(root)
        transformer.visit(root)

        result = astor.to_source(root)
        print(result)
        assert result == expected

    class Test(unittest.TestCase):
        def test_simple(self):
            compare('''\
import a
''', '''\
try:
    import a
except ImportError:
    import a as a
''')


# Generated at 2022-06-14 01:46:55.377227
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # test with node whose name doesn't match
    name_import = ast.Import(names=[ast.alias(name="name",
                                             asname=None)])
    assert BaseImportRewrite.transform(name_import).tree == name_import

    # test with node whose name matches
    rewrites = [('oldmodule', 'newmodule')]
    rewrites_rewriter = type('Test', (BaseImportRewrite,), {'rewrites': rewrites})

    transformed_name_import = rewrites_rewriter.transform(name_import).tree
    name_import_rewrite = ast.Import(names=[ast.alias(name="newmodule",
                                                     asname=None)])
    assert transformed_name_import == name_import_rewrite

    # test with node whose name matches as submodule
    name

# Generated at 2022-06-14 01:46:58.940408
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from tests.ConverterTestCase import ConverterTestCase
    import astor

    tree = ConverterTestCase.get_ast('import_import')
    expected = ConverterTestCase.get_ast('import_import_expected')

    result = BaseImportRewrite.transform(tree)
    assert astor.to_source(result.new_tree), astor.to_source(expected)



# Generated at 2022-06-14 01:47:13.670005
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert BaseImportRewrite._get_matched_rewrite(None) is None
    assert BaseImportRewrite._get_matched_rewrite('') is None
    assert BaseImportRewrite._get_matched_rewrite('random') is None
    assert BaseImportRewrite._get_matched_rewrite('random.main') is None
    assert BaseImportRewrite._get_matched_rewrite('random.foo') is None
    assert BaseImportRewrite._get_matched_rewrite('foo.random.main') is None

    assert BaseImportRewrite._get_matched_rewrite('foo') == ('foo', 'bar')
    assert BaseImportRewrite._get_matched_rewrite('foo.baz') == ('foo', 'bar')

# Generated at 2022-06-14 01:47:21.418001
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils.py_ver import TEST_PY_VER
    from ..utils import get_ast_tree, get_target_node

    class TestableBaseImportRewrite(BaseImportRewrite):
        rewrites = [('a.b', 'c.d')]

    nodes = get_ast_tree(
        """
import a.b

""", target_version=TEST_PY_VER)

    assert isinstance(get_target_node(nodes, ast.ImportFrom), ast.ImportFrom)
    assert isinstance(get_target_node(
        TestableBaseImportRewrite.transform(nodes).transformed, ast.Try), ast.Try)



# Generated at 2022-06-14 01:47:25.961217
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import sys
    class MyTransformer(BaseImportRewrite):
        rewrites = [
            ('os', 'pathlib')
        ]
    code = '''import os'''
    ast_tree = ast.parse(code)
    transformer = MyTransformer(ast_tree)
    new_tree = transformer.visit(ast_tree)
    sys.stdout.write(ast.unparse(new_tree))


# Generated at 2022-06-14 01:47:35.458211
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    from . import BaseImportRewrite
    from .utils import get_ast

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = get_ast(
        'import foo',
        python_version='3.5')
    expected_tree = get_ast(
        'try:\n'
        '    import foo\n'
        'except ImportError:\n'
        '    import bar',
        python_version='3.5')

    node = ImportRewrite.transform(tree).tree
    assert ast.dump(node, annotate_fields=False) == ast.dump(expected_tree, annotate_fields=False)


# Generated at 2022-06-14 01:47:42.307850
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewriter = BaseImportRewrite()
    node = ast.parse('import six.moves.urllib.request')

    expected = ast.parse('try:\n    import six.moves.urllib.request\nexcept ImportError:\n    import urllib3.request')

    changed = ast.fix_missing_locations(rewriter.visit(node))
    assert ast.dump(changed) == ast.dump(expected)

    rewriter._tree_changed is True



# Generated at 2022-06-14 01:47:50.322236
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast, astunparse
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('baz', 'qux')]
    node = ast.parse('from foo import bar; from baz import qux')
    new_node = ImportRewrite().visit(node)

    assert astunparse.unparse(new_node) == \
           'try:\n    import qux\nexcept ImportError:\n    from baz import qux\n\n'


# Generated at 2022-06-14 01:47:59.514216
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('urllib', 'urllib2')]

    tree = ast.parse('import urllib.request\n'
                     'import urllib.response')
    transformer = TestTransformer(tree)
    transformer.visit(tree)

# Generated at 2022-06-14 01:48:10.191581
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import a')
    res = BaseImportRewrite(tree).visit(tree)
    assert res.names[0].name == 'a'
    assert not res.names[0].asname
    assert len(res.names) == 1

    tree = ast.parse('import b as c')
    res = BaseImportRewrite(tree).visit(tree)
    assert res.names[0].name == 'b'
    assert res.names[0].asname == 'c'
    assert len(res.names) == 1

    tree = ast.parse('import aaa.aaa')
    res = BaseImportRewrite(tree).visit(tree)
    assert res.names[0].name == 'aaa.aaa'
    assert not res.names[0].asname
    assert len(res.names)

# Generated at 2022-06-14 01:48:14.241494
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestRewrite(BaseImportRewrite):
        rewrites = [('a', 'b')]

    code = 'import a'
    tree = ast.parse(code)
    TestRewrite.transform(tree)

    assert code == 'import a'



# Generated at 2022-06-14 01:48:25.282637
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils import parser_wrapper as parser
    from .base_import_rewrite import BaseImportRewrite

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]

    class TestNodeVisitor(ast.NodeVisitor):
        visitor = TestImportRewrite()

        def visit_Import(self, node):
            self.visitor.visit_Import(node)

        def visit_ImportFrom(self, node):
            self.visitor.visit_ImportFrom(node)

    root = parser.parse_string('import six.moves')
    node_visitor = TestNodeVisitor()
    node_visitor.visit(root)


# Generated at 2022-06-14 01:48:38.535082
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse

    code = 'from werkzeug.utils import cached_property'
    expected = 'from werkzeug.utils import cached_property'
    source = ast.parse(code)
    assert astunparse.unparse(source) == expected

    class Test(BaseImportRewrite):
        target = "Python >= 3.5.0"
        rewrites = [("werkzeug", "flask")]

    code = 'from werkzeug.utils import cached_property'
    expected = \
        '''try:
    from werkzeug.utils import cached_property
except ImportError:
    from flask.utils import cached_property'''

    source = ast.parse(code)
    assert astunparse.unparse(source) == expected

    Test.transform(source)
    result = ast

# Generated at 2022-06-14 01:48:46.082015
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .. import transformer
    from ..transformer import BaseImportRewrite
    import ast

    tree = ast.parse("from foo import bar, baz")
    class TestClass(BaseImportRewrite):
        rewrites = [
            ('foo', 'x')
        ]
    node = ast.parse("from x import bar, baz")

    transformer.BaseImportRewrite = TestClass
    assert node == TestClass(tree).visit_ImportFrom(tree.body[0])

    tree = ast.parse("from wx import foo")
    class TestClass(BaseImportRewrite):
        rewrites = [
            ('bar', 'x')
        ]
    node = ast.parse("from wx import foo")

    transformer.BaseImportRewrite = TestClass

# Generated at 2022-06-14 01:48:54.326941
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert BaseImportRewrite.transform(ast.parse('''
import base64
import hashlib
import foo
''')) == TransformationResult(ast.parse('''
import base64
import hashlib
try:
    import foo
except ImportError:
    import foo.foo as foo
'''), True, [])

    assert BaseImportRewrite.transform(ast.parse('''
import base64
import hashlib
import requests
''')) == TransformationResult(ast.parse('''
import base64
import hashlib
try:
    import requests
except ImportError:
    import requests.requests as requests
'''), True, [])


# Generated at 2022-06-14 01:49:03.120180
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_COMPILER
        rewrites = [('abc', 'abc.def')]
        
    tree = ast.parse('import abc')
    trans = Transformer(tree)
    trans.visit(tree)

    assert trans._tree_changed
    assert tree.body == [
        import_rewrite.get_body(previous=ast.Import(names=[
            ast.alias(name='abc', asname=None)]),  # type: ignore
                                 current=ast.Import(names=[
                                     ast.alias(name='abc.def', asname=None)]))[0]]  # type: ignore



# Generated at 2022-06-14 01:49:14.422234
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ast import parse

    # Try/Except transform
    changes = set()
    for from_, to in [('scipy.misc', 'scipy.misc.pilutil'),
                      ('sklearn.model_selection', 'sklearn.cross_validation')]:
        st = astor.code_to_ast(
            '''
            import {from_}
            {from_}.imrotate(arr, angle, interp='bilinear')
            '''.format(from_=from_))
        rewrote = BaseImportRewrite(st).visit(st)

# Generated at 2022-06-14 01:49:23.283053
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from_ = 'foo'
    to = 'bar'

    import_from_rewrites = [
        ast.ImportFrom(
            module=from_,
            names=[ast.alias(name='bar', asname='bar')],
            level=0),
        ast.ImportFrom(
            module=from_,
            names=[ast.alias(name='true_bar', asname='bar')],
            level=0),
        ast.ImportFrom(
            module=from_,
            names=[ast.alias(name='false_bar', asname='bar')],
            level=0),
    ]


# Generated at 2022-06-14 01:49:30.228380
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse("""
import os
import re
import sys
""", mode='exec')
    expected_tree = ast.parse("""
try:
    import os
except ImportError:
    import os2
try:
    import re
except ImportError:
    import re2
import sys
""", mode='exec')
    order = ['os', 're', 'sys']
    for module, i in zip(order, range(len(order))):
        assert expected_tree.body[i] == BaseImportRewrite([(module, '{}2'.format(module))]).visit(tree.body[i])


# Generated at 2022-06-14 01:49:43.267763
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as _ast

    # Define nodes of different types
    try_node = _ast.Try(
        body=[
            _ast.Import(
                names=[
                    _ast.alias(
                        name='foo',
                        asname=None
                    )
                ]
            )
        ]
    )

    # Check if all nodes are different
    assert try_node != _ast.Try(
        body=[
            _ast.Import(
                names=[
                    _ast.alias(
                        name='foo',
                        asname=None
                    )
                ]
            )
        ]
    )

    # Check if nodes are equal

# Generated at 2022-06-14 01:49:52.512594
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import astunparse

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('_six', 'six')]

    text = '''
import _six
'''

    expected_text = '''
try:
    import _six
except ImportError:
    import six
'''

    tree = ast.parse(text)
    TestBaseImportRewrite.transform(tree)

    print(astor.to_source(tree))
    print(ast.dump(tree))
    print(astunparse.unparse(tree))
    assert astor.to_source(tree) == expected_text



# Generated at 2022-06-14 01:50:04.604762
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse
    import os
    import sys
    import astor
    sys.path.append(os.path.abspath('../../'))
    from sodacomm.tools import testwrapper
    # Test 1:
    class TestTransformer1(BaseImportRewrite):
        target = CompilationTarget.PYTHON
        rewrites = [
            ('importlib', 'importlib2')
        ]

    test_tree = parse('''from importlib import reload''')
    res_tree = parse('''from importlib import reload
from importlib import reload''').body
    TestTransformer1.transform(test_tree)
    assert(astor.to_source(test_tree) == astor.to_source(res_tree[0]))
    # Test 2:

# Generated at 2022-06-14 01:50:18.128739
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse
    import ast
    import re

    def check_import(node):
        assert isinstance(node, ast.Try)
        assert len(node.body) == 1
        assert isinstance(node.body[0], ast.ImportFrom)
        assert node.body[0].module == 'collections'

        assert len(node.body[0].names) == 4
        assert all(alias.name == name for alias, name in zip(node.body[0].names, ['*', 'defaultdict', 'namedtuple', 'OrderedDict']))
        assert all(alias.asname is None for alias in node.body[0].names)

        assert len(node.handlers) == 1
        assert isinstance(node.handlers[0], ast.ExceptHandler)

# Generated at 2022-06-14 01:50:27.244466
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils import ast_utils

    import_1 = ast.Import(names=[ast.alias(name='os', asname=None)])
    import_2 = ast.Import(names=[ast.alias(name='os.path', asname='path')])

    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('os', 'os.path')]
        dependencies = []

    node_transformer = TestBaseImportRewrite(ast_utils.empty_tree())
    assert_equal(ast_utils.dump(node_transformer.visit_Import(import_1)),
                 '''try:
    import os
except ImportError:
    import os.path as os''')

# Generated at 2022-06-14 01:50:35.525776
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Mock(BaseImportRewrite):
        rewrites = [
            ('previous', 'mock'),
        ]

    class ASTMock(ast.AST):
        def __init__(self, name: str):
            self.names = [ast.alias(name=name,
                                    asname=None)]

    assert Mock.transform(ASTMock('previous')).tree == import_rewrite.get_body(  # type: ignore
        previous=ASTMock('previous'),
        current=ASTMock('mock'))[0]



# Generated at 2022-06-14 01:50:47.466601
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    code = '''
from A import B
from A import B as B2
from A import *
from A.B import C
from A.B import C as C2

from A.B import *
'''
    tree = astor.parse_file(io.StringIO(code))
    cls = type('TestImportRewrite', (BaseImportRewrite,), dict(rewrites=[
        ('A', 'A_rewrite')
    ]))
    result = cls.transform(tree)
    assert result.changed


# Generated at 2022-06-14 01:50:56.999297
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import pytest

    import six
    from typed_ast.ast3 import parse
    from typed_ast.pygram.python_symbols import import_name

    from .utils import transform

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('six', 'future.moves'),
            ('six.moves.http_client', 'http.client'),
        ]
        dependencies = ['future', 'urllib']


# Generated at 2022-06-14 01:51:02.932245
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import inspect, ast, typing
    class Test(BaseImportRewrite):
        rewrites = [('typing', 'typing_extensions')]
    inst = Test()
    code = inspect.getsource(ast.Import)
    tree = ast.parse(code)
    inst.visit(tree)
    globals().update(locals()) # for debugging


# Generated at 2022-06-14 01:51:11.219757
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import typed_ast.ast3 as typed_ast
    from typed_ast import ast3 as typed_ast3
    node1 = typed_ast.parse('from matplotlib import colors')
    node2 = typed_ast.parse('from matplotlib.colors import rgb2hex')
    node3 = typed_ast.parse('from matplotlib import colors as colors_')
    node4 = typed_ast.parse('from matplotlib.colors import rgb2hex as rgb2hex_')
    node5 = typed_ast.parse('from matplotlib.colors import (rgb2hex, hex2color)')
    node6 = typed_ast.parse('from matplotlib.colors import (rgb2hex as rgb2hex_, '
                            'hex2color as hex2color_)')
    node7

# Generated at 2022-06-14 01:51:22.969332
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [('.pip', '.pip._internal')]

    import_from_node = ast.parse('#coding:utf-8\nfrom pip.commands.install import InstallCommand').body[1]

    transformed_node = MyBaseImportRewrite(None).visit(import_from_node)
    assert astor.to_source(transformed_node) == '''\
try:
    from pip.commands.install import InstallCommand
except ImportError:
    from pip._internal.commands.install import InstallCommand
'''

    class MyBaseImportRewrite(BaseImportRewrite):
        rewrites = [('.pip.commands.install', 'pip._internal.commands.install')]

    import_from_

# Generated at 2022-06-14 01:51:32.653901
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class ImportTransformer(BaseImportRewrite):
        target = 'python38'
        rewrites = [
            ('os.path', 'pathlib'),
            ('builtins', '__builtin__'),
        ]

    import_from = ast.ImportFrom(
        module='os.path',
        names=[ast.alias(name='abspath',
                         asname='my_abspath'),
                ast.alias(name='isfile',
                         asname='my_isfile')],
        level=0)


# Generated at 2022-06-14 01:51:41.757955
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('foo.bar', 'foo.bar.baz')
        ]
    import_node = ast.parse("import foo.bar").body[0]
    result = Test.transform(import_node).transformed
    assert isinstance(result, ast.Try)
    assert len(result.handlers) == 1
    assert len(result.body) == 1
    assert len(result.orelse) == 1



# Generated at 2022-06-14 01:51:54.762702
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.graph import graph_sorted

    class Test1(BaseImportRewrite):
        rewrites = [('foo', 'baz')]

    from . import ast as ast_test
    ast_tree = ast_test.a

    graph_sorted(Test1.transform(ast_tree).tree) == [
        ast.Try,
        ast.Import,
        ast.Import,
        ast.Import,
        ast.Import,
        ast.ImportFrom,
        ast.ImportFrom,
        ast.ImportFrom,
        ast.ImportFrom,
        ast.Try,
        ast.Import,
        ast.Import,
        ast.Import,
        ast.Import,
        ast.ImportFrom,
        ast.ImportFrom,
        ast.ImportFrom,
        ast.ImportFrom,
    ]




# Generated at 2022-06-14 01:52:05.700543
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import AST
    from typed_ast.ast3 import ImportFrom
    from typed_ast.ast3 import alias
    from typed_ast.ast3 import TryExcept
    from typed_ast.ast3 import TryFinally
    from typed_ast.ast3 import Try

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('far', 'far.far')]

    module = AST()
    assert hasattr(module, 'body')
    
    assert TestImportRewrite(module).visit_ImportFrom(ImportFrom('self', [alias('t', 't')], 0)) == \
        Try(
            [ImportFrom('self', [alias('t', 't')], 0)],
            [],
            [],
            [],
            None
        )

    assert TestImportRewrite

# Generated at 2022-06-14 01:52:16.769127
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.snippet import create_module  # Needed for type checking

    rewrites = [('six', 'future')]
    # Test for import
    tree = create_module('import six')
    assert tree.body == [ast.Import(names=[ast.alias(name='six', asname=None)])]
    result = BaseImportRewrite(tree).visit(tree)
    assert result.body == [
        ast.Try(body=[ast.Import(names=[ast.alias(name='six', asname=None)])],
                handlers=[ast.ExceptHandler(type=None,
                                            name=None,
                                            body=[ast.Import(names=[ast.alias(
                                                name='future', asname=None)])])],
                orelse=[], finalbody=[])]

   

# Generated at 2022-06-14 01:52:26.071354
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rew = BaseImportRewrite()
    code = """
import a
import b as c
from m import n
from m import o as p
from m import *
"""
    tree = ast.parse(code)
    rew.rewrites.append(('m', 'm_rew'))
    rew.visit(tree)
    result = ast.dump(tree).strip()

# Generated at 2022-06-14 01:52:39.650250
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from jinja2 import Template as jinja2_Template
    from ..comp.jinja2 import BaseImportRewrite
    import ast, inspect

    filename = inspect.getfile(jinja2_Template)
    with open(filename, encoding='utf8') as fh:
        source = fh.read()

    tree = ast.parse(source, filename=filename)

    BaseImportRewrite.rewrites.append(('jinja2.utils', 'jinja2.bundled.utils'))

    class TestBaseImportRewrite(BaseImportRewrite):
        pass

    TestBaseImportRewrite.transform(tree)

    assert tree is not None



# Generated at 2022-06-14 01:52:44.880786
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_node = ast.parse('import base').body[0]
    rw = BaseImportRewrite(ast.Module(body=[]))

    assert isinstance(rw.visit(import_node), ast.Try)



# Generated at 2022-06-14 01:52:55.164696
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    module = ast.parse(
        '''from foo import bar, baz as qux''',
        mode='exec')
    BaseImportRewrite.rewrites = [('foo.baz', 'foo.quux')]
    result = BaseImportRewrite.transform(module)
    module_str = ast._convert(result.tree, None)
    assert ast.parse(
        '''from foo import bar
try:
    from foo import baz as qux
except ImportError:
    from foo import quux as qux
''',
        mode='exec').body == ast.parse(
        module_str.strip(), mode='exec').body

# Generated at 2022-06-14 01:53:05.359864
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class FakeNodeTransformer(BaseImportRewrite):
        rewrites = [
            ('xml.etree.ElementTree', 'lxml.etree'),
            ('xml.dom', 'lxml.dom')
        ]

    code = """
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml import dom
"""
    tree = ast.parse(code)
    FakeNodeTransformer.transform(tree)

    # Expected AST after transformation

# Generated at 2022-06-14 01:53:13.850902
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from unittest import TestCase
    import ast as stdlib_ast

    from typed_astunparse import unparse
    from ..utils.compile_source import compile_source
    from ..utils.node_visitor import NodeVisitor
    from ..utils.ast_compare import ast_equal

    class BaseImportRewrite_visit_Import(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')
        ]

    class Test(TestCase):
        def test(self):
            source = 'import foo'
            tree = compile_source(source, stdlib_ast, 'single')
            result = BaseImportRewrite_visit_Import.transform(tree)
            expected_tree = compile_source(
                'import bar', stdlib_ast, 'single')

# Generated at 2022-06-14 01:53:22.626028
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(module='foo',
                                 names=[ast.alias(name='a')],
                                 level=0)
    fist_transformer = BaseImportRewrite(None)
    setatattr(fist_transformer,
              'rewrites',
              [('foo', 'bar')])
    result_node = fist_transformer.visit_ImportFrom(import_from)
    assert(isinstance(result_node, ast.Try))

# Generated at 2022-06-14 01:53:33.266675
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    code = astor.to_source(ast.parse('import foo'))
    print(code)



# Generated at 2022-06-14 01:53:39.316738
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..testing.utils import assert_ast

    class Transform(BaseImportRewrite):
        rewrites = [
            ('to_be_replaced', 'replaced'),
        ]

    original = """import to_be_replaced"""
    expected = """try:
    import to_be_replaced
except ImportError:
    import replaced"""

    assert_ast(Transform, original, expected)



# Generated at 2022-06-14 01:53:46.532197
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .helper import ValidationTransformer
    from ..utils.nodes import extract_nodes_from_body

    transformer = ValidationTransformer(BaseImportRewrite,
                                        target=[CompilationTarget.REAL_PYTHON_37],
                                        body=ast.parse("import a;").body,
                                        expected=[ast.Import(names=[ast.alias(name='a',
                                                                             asname=None)])])
    extract_nodes_from_body(transformer.transformed_body)



# Generated at 2022-06-14 01:53:55.937837
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import typed_ast3 as ast

    ast_node = ast.ImportFrom('a',
                              names=[ast.alias(name='a', asname=None)],
                              level=0)
    tree = ast.Module(body=[ast_node])
    class DummyTransformer(BaseImportRewrite):
        rewrites = [('a', 'b')]

    transformed_tree = DummyTransformer.transform(tree)
    tree_changed = transformed_tree.tree_changed
    dependencies = transformed_tree.dependencies

    import_from_node = transformed_tree.tree.body[0]
    assert isinstance(import_from_node, ast.Try)
    except_handler = import_from_node.handlers[0]
    assert isinstance(except_handler, ast.ExceptHandler)