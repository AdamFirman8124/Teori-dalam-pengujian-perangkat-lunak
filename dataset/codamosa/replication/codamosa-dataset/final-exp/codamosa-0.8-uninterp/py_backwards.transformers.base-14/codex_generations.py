

# Generated at 2022-06-14 01:44:14.303053
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node_1 = ast.ImportFrom(module='foo', names=[ast.alias(name='bar')])
    node_2 = ast.ImportFrom(module='foo', names=[ast.alias(name='baz')])
    node_3 = ast.ImportFrom(module='foo', names=[ast.alias(name='quux')])
    node_4 = ast.ImportFrom(module='foo', names=[ast.alias(name='test')])
    node_5 = ast.ImportFrom(module='foo', names=[ast.alias(name='test.test')])
    node_6 = ast.ImportFrom(module='foo',
                            names=[ast.alias(name='foo'),
                                   ast.alias(name='bar')])

# Generated at 2022-06-14 01:44:21.314202
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
        def __init__(self, tree):
            pass
        def _replace_import(self, node, from_, to):
            return node
    transformer = TestTransformer([])
    assert 'bar' == transformer.visit_Import(ast.parse('import foo').body[0]).names[0].name
    assert None == transformer.visit_Import(ast.parse('import bar').body[0]).names[0].name
    assert None == transformer.visit_Import(ast.parse('import bar.foo').body[0]).names[0].name
    assert None == transformer.visit_Import(ast.parse('import bar.foo as bla').body[0]).names[0].name
    assert None

# Generated at 2022-06-14 01:44:30.441796
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from pytuber.transforms.nodes import BaseImportRewrite

    class FakeTransformer(BaseImportRewrite):
        source = """from foo import bar"""
        rewrites = [
            ("foo", "new_foo")]

        @classmethod
        def transform(cls, tree):
            inst = cls(tree)
            new_tree = inst.visit(tree)
            return new_tree, inst._tree_changed

    actual_tree, changed = FakeTransformer.transform(
        ast.parse(FakeTransformer.source))

    expected = """\
try:
    from foo import bar
except ImportError:
    from new_foo import bar
"""
    assert actual_tree == ast.parse(expected)
    assert changed is True


# Generated at 2022-06-14 01:44:42.120206
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from itertools import product

    # imports
    import_from_list = [
        ast.ImportFrom(
            module='foo.bar',
            names=[ast.alias(name='baz')],
            level=0),
        ast.ImportFrom(
            module='foo.bar',
            names=[ast.alias(name='baz', asname='bar')],
            level=0),
        ast.ImportFrom(
            module='foo.bar',
            names=[ast.alias(name='*')],
            level=0),
    ]

    # rewrites

# Generated at 2022-06-14 01:44:48.891159
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        rewrites = [
            ('typing.List', 'list')]

    node = ast.parse("import typing.List").body[0]
    node = Test.visit(Test(), node)
    assert ast.dump(node) == "try:\n    extend(typing.List)\nexcept ImportError:\n    extend(list)"



# Generated at 2022-06-14 01:44:58.121796
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # arrange
    import astor
    import six
    import typing
    import typing_extensions
    import unittest.mock

    class MyArg(BaseImportRewrite):
        rewrites = [(
            six.__name__, typing_extensions.__name__
        )]


# Generated at 2022-06-14 01:45:05.070046
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    t = ast.parse('from foo import a, b, c\nfrom bar import b\n', filename='<string>', mode='exec')
    class Transformer(BaseImportRewrite):
        rewrites = [('foo', 'foo2')]
    assert ast.dump(Transformer.transform(t).tree) == 'try:\n    import foo2\n    from foo2 import a, b, c\n    from bar import b\nexcept ImportError:\n    import foo\n    from foo import a, b, c\n    from bar import b\n'
    

# Generated at 2022-06-14 01:45:09.563576
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.codegen import to_source
    from textwrap import dedent


    class Tr(BaseImportRewrite):
        rewrites = [('other_module', 'new_other_module')]


    code = dedent('''
    from other_module import a, b, other_name
    from other_module.other import c, d
    ''')
    tree = ast.parse(code)
    tree = Tr().visit(tree)


# Generated at 2022-06-14 01:45:20.141750
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    import unittest.mock as mock

    # Mock BaseImportRewrite
    target = mock.Mock(spec=CompilationTarget)
    cls = mock.Mock(spec=BaseImportRewrite)
    cls._get_matched_rewrite.return_value = None
    cls.target = target
    cls.rewrites = [
        ('example', 'rewrite'),
    ]
    cls._tree_changed = False
    cls.dependencies = []
    cls.generic_visit = mock.MagicMock()
    cls._replace_import = mock.Mock()

    # Run
    node = ast.parse('import example')
    cls.visit_Import(node)

    # Test
    cls.generic_visit.assert_

# Generated at 2022-06-14 01:45:27.245769
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    base_import_rewrite = BaseImportRewrite([('previous', 'current')])
    node = ast.parse('import module').body[0]
    rewrote = ast.parse('try:\n    import previous\nexcept ImportError:\n    import current').body[0]
    assert rewrote == base_import_rewrite.visit_Import(node)


# Generated at 2022-06-14 01:45:44.695507
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast, typing

    if not hasattr(typing, 'TYPE_CHECKING'):
        raise RuntimeError('You forgot to specify typing annotations!')

    class TestTransformer(BaseImportRewrite):
        rewrites = [('oldmodule', 'newmodule')]

    source = """
    import oldmodule
    from oldmodule import foo1, foo2
    from oldmodule import *
    from oldmodule.submodule import foo3, foo4
    from oldmodule.submodule.submodule import foo5, foo6
    from oldmodule.submodule import *
    """


# Generated at 2022-06-14 01:45:57.282069
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astunparse import unparse

    class TestClass(BaseImportRewrite):
        rewrites = [
            ('test', 'test1'),
            ('test2', 'test12'),
        ]

    node = ast.parse('import test.test2')
    res = TestClass.transform(node)

    assert res.changed
    assert res.dependencies == ['test1']

    assert unparse(res.tree) == """try:
    import test.test2
except ImportError:
    import test1.test2
"""



# Generated at 2022-06-14 01:46:01.793851
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    ast_ = ast.parse('import x')
    transformer = BaseImportRewrite()
    rewrite = (x, y)
    transformer.rewrites = [rewrite]

    expected = ast.Try(
        handler=None,
        body=[
            ast.Import(names=[ast.alias(name='y', asname=None)]),
        ],
        orelse=[],
        finalbody=[],
        lineno=1,
        col_offset=0,
    )

    node = transformer.visit(ast_)

    assert node == expected
    assert transformer._tree_changed == True


# Generated at 2022-06-14 01:46:12.611481
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('import_1', 'import_2'),
                    ('import_1.module', 'import_2.module')]

    import_from_1 = "from import_1.module import module_11 as m11, module_12 as m12"
    import_from_2_as_ast = """
        import import_1.module as im
    """

    # Test: import 1.1
    tree = ast.parse(import_from_1)
    TestBaseImportRewrite.transform(tree)

# Generated at 2022-06-14 01:46:20.007437
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astroid

    transformer = BaseImportRewrite.__new__(BaseImportRewrite)
    transformer.rewrites = [('six', 'future_builtins')]

    node = astroid.extract_node('''
    import six
    ''')

    result_node = transformer.visit_Import(node)

    expected_result = ['''
    try:
        import six
    except ImportError:
        import future_builtins as six
    ''']

    assert astroid.dump_tree(result_node) in expected_result



# Generated at 2022-06-14 01:46:31.425007
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import typed_ast.ast3 as typed_ast
    from src.transformers.base import BaseImportRewrite

    class ExampleTransformer(BaseImportRewrite):
        rewrites = [
            ('a', 'b'),
        ]

    test_case = 'import a'

    tree1 = ast.parse(test_case).body[0]
    tree2 = typed_ast.parse(test_case).body[0]

    # Check that classes are compatible
    assert ast.dump(tree1) == typed_ast.dump(tree2)

    result = ExampleTransformer.transform(tree2).result
    assert ast.dump(result) == typed_ast.dump(ExampleTransformer.transform(tree1).result)


# Generated at 2022-06-14 01:46:41.139288
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    class Test(BaseImportRewrite):
        rewrites = [('urllib.request', 'urllib.request_new')]
    result = Test.transform(ast.parse('import urllib.request'))
    assert astor.to_source(result.tree) == (
        'try:\n'
        '    import urllib.request\n'
        'except ImportError:\n'
        '    import urllib.request_new')



# Generated at 2022-06-14 01:46:51.180202
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    t = BaseImportRewrite(None)
    t.rewrites = [('six', 'six.moves')]

# Generated at 2022-06-14 01:47:05.234559
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    a = ast.parse('from collections import Counter')
    BaseImportRewrite.transform(a)
    assert (ast.dump(a) == 'Module(body=[ImportFrom(module=\'collections\', names=[alias(name=\'Counter\', asname=None)], level=0)])')
    a = ast.parse('from collections import Counter, defaultdict')
    BaseImportRewrite.transform(a)
    assert (ast.dump(a) == 'Module(body=[ImportFrom(module=\'collections\', names=[alias(name=\'Counter\', asname=None), alias(name=\'defaultdict\', asname=None)], level=0)])')
    a = ast.parse('from collections import Counter as c')
    BaseImportRewrite.transform(a)

# Generated at 2022-06-14 01:47:12.806083
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import typed_ast.ast3 as ast

    class Test(BaseImportRewrite):
        rewrites = [
            ('collections', 'collections.abc')
        ]

    tree = ast.parse("from foo import collections")
    result = Test.transform(tree)

    assert result.tree_changed
    assert Test.dependencies
    assert Test.dependencies[0] == 'typed_ast.ast3'
    assert result.result.body[0].body[0].orelse is not None



# Generated at 2022-06-14 01:47:28.625247
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewrite_from = BaseImportRewrite
    rewrite_from.rewrites = [('from', 'from_from')]
    test_tree = ast.parse("from from import foo")
    assert isinstance(rewrite_from.transform(test_tree)
                      .tree.body[0].body[0].value, ast.Try)



# Generated at 2022-06-14 01:47:35.148387
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    source = '''
import module
    '''
    expected = '''
try:
    import module
except ImportError:
    import module2
    '''
    class MockImportRewrite(BaseImportRewrite):
        rewrites = [('module', 'module2')]

    expected_tree = ast.parse(expected)
    tree = ast.parse(source)
    assert MockImportRewrite.transform(tree).tree == expected_tree



# Generated at 2022-06-14 01:47:45.802197
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    expected = ast.Try(
        body=[
            ast.TryExcept(
                body=[
                    ast.ImportFrom(
                        module='module.submodule1',
                        names=[ast.alias(name='B', asname=None)],
                        level=None)
                ],
                handlers=[ast.ExceptHandler(
                    type=None,
                    name=None,
                    body=[
                        ast.ImportFrom(
                            module='module.submodule3',
                            names=[ast.alias(name='B', asname=None)],
                            level=None)
                    ])
                ],
                orelse=[])
        ],
        handlers=[],
        finalbody=[])

# Generated at 2022-06-14 01:47:54.289575
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class MyT(BaseImportRewrite):
        rewrites = [('lib', 'lib2')]

    tree = ast.parse('''
import lib
        ''')
    MyT.transform(tree)
    print(astor.to_source(tree))
    tree = ast.parse('''
import lib.sub
        ''')
    MyT.transform(tree)
    print(astor.to_source(tree))
    tree = ast.parse('''
import not_lib
        ''')
    MyT.transform(tree)
    print(astor.to_source(tree))



# Generated at 2022-06-14 01:48:01.224785
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_name = 'module'
    new_import_name = 'new_module'
    import_as = 'new_module_name'
    import_node = ast.Import(names=[ast.alias(name=import_name, asname=import_as)])

    class ImportRewrite(BaseImportRewrite):
        rewrites = [(import_name, new_import_name)]

    tree = ast.Module()
    tree.body = [import_node]

    result = ImportRewrite.transform(tree)

    assert result.changed == True
    try_node = result.tree.body[0]
    assert isinstance(try_node, ast.Try)
    assert len(try_node.body) == 1
    assert isinstance(try_node.body[0], ast.Import)
    assert try_node.body

# Generated at 2022-06-14 01:48:08.388727
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    from .utils import test_transformer

    class Transformer(BaseImportRewrite):
        rewrites = [('email.mime', 'email.mime.nonmultipart')]

    source = '''
from email.mime.text import MIMEText
'''
    node = ast3.parse(source).body[0]
    assert type(node) is ast3.Expr
    node = node.value

    expected = '''
try:
    from email.mime.text import MIMEText
except ImportError:
    from email.mime.nonmultipart.text import MIMEText
'''
    test_transformer(Transformer, source, expected)


# Generated at 2022-06-14 01:48:17.051675
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astunparse
    from typed_ast.ast3 import parse

    class ImportRename(BaseImportRewrite):
        rewrites = [('collections', 'collections.abc')]

    class Test(unittest.TestCase):
        def test_rewrite(self):
            node = parse('''
                import collections
            ''')
            res = ImportRename.transform(node)
            expected = '''
                try:
                    import collections
                except ImportError:
                    import collections.abc as collections
            '''
            self.assertEqual(astunparse.unparse(res.tree), expected)

    unittest.main()



# Generated at 2022-06-14 01:48:28.263326
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    node = ast.ImportFrom(module = 'prefix.subpackage.module', names = [ast.alias(name = 'alias1', asname = 'alias1')], level = 0)
    transformer = BaseImportRewrite(node)
    transformer.rewrites = [('prefix.subpackage.module', 'prefix.subpackage.subsubpackage.module')]
    result = ast.dump(transformer.visit_ImportFrom(node))

# Generated at 2022-06-14 01:48:38.425550
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import parse_tree_from_code, code_from_tree

    code = """
from typing import List
from typing import Tuple
from typing import Optional

from .models import Question, Choice

from .foo.models import Foo, Bar
"""
    tree = parse_tree_from_code(code)
    transformer = BaseImportRewrite(tree)

    # skipping nothing
    expected_code = code
    assert transformer._get_matched_rewrite(None) is None
    assert transformer._get_matched_rewrite('typing.Tuple.foo') is None
    assert transformer._get_matched_rewrite('.models.Question') is None
    assert transformer._get_matched_rewrite('') is None
    assert transformer._get_rewrite('foo.models') is None

    # import rewrite

# Generated at 2022-06-14 01:48:46.016025
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import ast

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('old', 'new'),
            ('foo.bar', 'baz.qux')
        ]

    source = astor.to_source(
        ast.parse(
            textwrap.dedent('''
            from old.foo import baz
            from old import foo
            from foo import bar, qux, guard
            from foo.bar.baz import qux
            from foo.bar import baz
            from foo.bar.baz.qux import bar
            ''')
        ),
        indent_with=' ' * 4
    )

    print('before:')
    print(source)

    tree = ast.parse(source)
    result = TestImportRewrite.transform(tree)
   

# Generated at 2022-06-14 01:49:18.930170
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    from ..utils.compiler import Compiler

    class TestTransformer(BaseImportRewrite):
        target = 'py2.7'
        rewrites = [
            ('a', 'b'),
            ('b.c', 'b.d'),
            ('d.e.f', 'e.f.g')
        ]

    class TestCase(unittest.TestCase):
        def test_simple(self):
            tree = Compiler.parse('''
from a import foo, bar
from b import *
from b.c import baz, *
from d.e.f import qux
from e import kwarg
''')
            result = TestTransformer.transform(tree)
            self.assertTrue(result.changed)

# Generated at 2022-06-14 01:49:21.491534
# Unit test for method visit_ImportFrom of class BaseImportRewrite

# Generated at 2022-06-14 01:49:30.392680
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast
    import astor
    import_module = BaseImportRewrite(None)
    code = """from xml.etree.ElementTree import ElementTree"""
    root = ast.parse(code).body[0] # type: ast.ImportFrom
    visited_no_rewrites = import_module.visit_ImportFrom(root)
    code_no_rewrites = astor.to_source(visited_no_rewrites)
    assert(code == code_no_rewrites)
    import_module.rewrites = [
        ('xml.etree.ElementTree', 'lxml.etree')
    ]
    visited_rewrites = import_module.visit_ImportFrom(root)
    code_rewrites = astor.to_source(visited_rewrites)

# Generated at 2022-06-14 01:49:43.457585
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # tests for import from with module name replacement
    module = ast.parse('from foo import bar')
    transformer = BaseImportRewrite(module)
    transformer.rewrites = [('foo', 'baz')]
    transformer.visit(module)
    assert transformer._tree_changed == True

# Generated at 2022-06-14 01:49:54.236658
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor


# Generated at 2022-06-14 01:50:01.296627
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ExampleImportRewrite(BaseImportRewrite):
        rewrites = [('numpy', 'numpy.core')]

    tree = ast.parse('from numpy import array')
    expected = ast.parse(
        '''from numpy.core import array
try:
    from numpy import array
except ImportError:
    from numpy.core import array
''')

    tree_changed, tree_new = ExampleImportRewrite.transform(tree)
    assert ast.dump(tree_new) == ast.dump(expected)


# Generated at 2022-06-14 01:50:07.603582
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import module')
    result = BaseImportRewrite.transform(tree)
    assert 'import module' == ast.dump(result.tree)

    tree = ast.parse('import module.submodule')
    result = BaseImportRewrite.transform(tree)
    assert 'import module.submodule' == ast.dump(result.tree)

    class TestImportRewriter1(BaseImportRewrite):
        rewrites = [('module', 'new_module')]

    tree = ast.parse('import module')
    result = TestImportRewriter1.transform(tree)
    assert ('try:\n'
            '    import module\n'
            'except ImportError:\n'
            '    import new_module\n') == ast.dump(result.tree)


# Generated at 2022-06-14 01:50:16.975358
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast2 as ast2
    import ast2 as ast3
    b = BaseImportRewrite()

    class Rewrite(BaseImportRewrite):
        rewrites = ['ast2', 'ast3']

    import_2 = ast.Import(names=[ast.alias(name='ast2', asname=None)])  # type: ignore
    assert isinstance(Rewrite().visit_Import(import_2), ast.Try)  # type: ignore
    assert Rewrite().visit_Import(import_2).body[0].body[0].names[0].name == 'ast3'  # type: ignore

    import_3 = ast.Import(names=[ast.alias(name='ast3', asname='ast_3')])  # type: ignore
    assert Rewrite().visit_Import(import_3) == import_3

# Generated at 2022-06-14 01:50:26.424961
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import traceback
    from .test_transformation_visitor import get_test_visitor
    from ..visitors import visitors
    from ..types import CompilationTarget
    from ..utils.snippet import extend

    visitor = get_test_visitor(visitors.get_visitor(CompilationTarget.PYPY))

    import_from_str1 = '''\
from datetime import * 
'''

    tree1 = ast.parse(import_from_str1).body[0]
    visitor.visit(tree1)
    expected1 = '''\
try:
    from datetime import * 
except ImportError:
    import _datetime_cffi
    _datetime_cffi.monkey_patch_datetime()
    import datetime
'''

# Generated at 2022-06-14 01:50:35.575459
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Mock(BaseImportRewrite):
        rewrites = [('a', 'b')]

    import_import = ast.Import(
        names=[ast.alias(name='a', asname='c')])

    import_try = Mock.transform(import_import).ast

    assert isinstance(import_try, ast.Try)
    assert len(import_try.body) == 1
    assert isinstance(import_try.body[0], ast.Import)
    assert import_try.body[0].names[0].name == 'b'
    assert import_try.body[0].names[0].asname == 'c'



# Generated at 2022-06-14 01:51:03.024884
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # code = """\
    # import os
    # """
    #
    # import inspect
    # import os
    #
    # tree = ast.parse(code)
    # BaseImportRewrite.rewrites = [('os', 'posix')]
    # BaseImportRewrite.transform(tree)
    #
    # expected = inspect.cleandoc("""\
    # import os
    # # try:
    # #     import os
    # # except ImportError:
    # #     import posix as os
    # """)
    #
    # assert(expected == astunparse.unparse(tree))
    pass


# # Unit test for method visit_Import of class BaseImportRewrite
# def test_BaseImportRewrite_visit_Import():
#     code = """\
# import os
# """

# Generated at 2022-06-14 01:51:10.976893
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    def visit_ImportFrom(node: ast.ImportFrom) -> Union[ast.ImportFrom, ast.Try]:
        rewrite = self._get_matched_rewrite(node.module)
        if rewrite:
            return self._replace_import_from_module(node, *rewrite)
        names_to_replace = dict(self._get_names_to_replace(node))
        if names_to_replace:
            return self._replace_import_from_names(node, names_to_replace)
        return self.generic_visit(node)

# Generated at 2022-06-14 01:51:22.574615
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    """BaseImportRewrite.visit_Import() should replace imported module."""
    transformer = BaseImportRewrite()
    transformer.rewrites = [('m', 'n')]

    node = ast.Import([ast.alias(name='m.v')])
    result = transformer.visit_Import(node)
    expected = ast.Try([
        ast.Import([ast.alias(name='m.v')]),
        ast.ExceptHandler(
            type=None,
            name=None,
            body=[ast.Import([ast.alias(name='n.v')])])],
        [], [], None)

    assert transformer._tree_changed
    assert isinstance(result, ast.Try)
    assert ast.dump(expected) == ast.dump(result)



# Generated at 2022-06-14 01:51:31.122314
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from ..examples.monitored import monitored_import, monitored_import_from
    node = astor.parse(monitored_import_from).body[0]

    transformer = BaseImportRewrite()
    transformer._get_matched_rewrite = lambda name: ('os.path', 'pathlib')
    try_node = transformer.visit_ImportFrom(node)
    assert astor.to_source(try_node).strip() == """\
try:
    from os.path import realpath
    from os.path import DirEntry
    from os.path import Path
except ImportError:
    from pathlib import realpath
    from pathlib import DirEntry
    from pathlib import Path
"""


# Generated at 2022-06-14 01:51:39.946202
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import astunparse
    tree = ast.parse('import mod')

    class A(BaseImportRewrite):
        rewrites = [('mod', 'foo')]

    assert astor.to_source(A.transform(tree).tree, indent_with=' '*4) == 'try:\n' \
                                                                        '    import foo\n' \
                                                                        'except ImportError:\n' \
                                                                        '    import mod'

    assert astunparse.unparse(A.transform(tree).tree) == 'try:\n' \
                                                         '    import foo\n' \
                                                         'except ImportError:\n' \
                                                         '    import mod'



# Generated at 2022-06-14 01:51:44.632190
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    result = BaseImportRewrite(None).visit_Import(ast.Import(names=[ast.alias(name='six', asname='six')]))  # type: ignore
    assert isinstance(result, ast.Try)


# Generated at 2022-06-14 01:51:51.988519
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..util import compile_source
    import astor

    source = """
    from mod import a, b

    def foo():
        pass
    """

    class Transformer(BaseImportRewrite):
        rewrites = [
            ('mod', 'replaced.mod')
        ]

    tree, changed = compile_source(source, Transformer)
    assert changed
    assert astor.to_source(tree).strip() == """
    try:
        from mod import a, b
    except ImportError:
        from replaced.mod import a, b


    def foo():
        pass
    """



# Generated at 2022-06-14 01:51:56.928440
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_ast = ast.Import(names=[
        ast.alias(name='foo.bar',
                  asname='bar')])


    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('foo.bar', 'test.test')]

    result = TestImportRewrite.transform(import_ast)
    assert result.modified



# Generated at 2022-06-14 01:52:00.391112
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse

    tree = parse(
        'from typing import List, Dict, Tuple\n'
        'from collections import defaultdict')

    import_rewrite_instance = BaseImportRewrite()

    import_rewrite_instance.visit(tree)

    assert tree.body[0].body[0].value.names[0].name == 'typing.Generator'
    assert tree.body[0].body[0].value.names[1].name == 'typing.Generator'
    assert tree.body[1].body[0].value.names[0].name == 'typing.Dict'

# Generated at 2022-06-14 01:52:04.489106
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from ..registry import registry
    from ..utils import compile_snippet

    registry.set_default_target(registry.targets[0])

    class BaseImportRewriteTests(BaseImportRewrite):
        def __init__(self, tree: ast.AST) -> None:
            super().__init__(tree)
            self.rewrites = [('json', 'somejson')]

    tree = compile_snippet('from json import JSONEncoder')
    result = BaseImportRewriteTests.transform(tree)

# Generated at 2022-06-14 01:52:54.044851
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    import typed_ast.ast3 as ast

    from typed_python import Function
    from typed_python.compiler.transforms.base import BaseImportRewrite

    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('typed_ast', 'typed_ast')
        ]

    class TestImportRewrte(unittest.TestCase):

        def test_absolute_import(self):
            input_ = ast.parse('import typed_ast\na=1')
            TestTransformer.transform(input_)

            self.assertEqual('import typed_ast\ntry:\n    import typed_ast\nexcept ImportError:\n    from . import typed_ast\n\na=1\n',
                             Function(input_).to_source())


# Generated at 2022-06-14 01:53:03.348698
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import numpy as np

    class FooImportRewriter(BaseImportRewrite):
        rewrites = [
            ('numpy', 'numpy.foo')]

    tree = ast.parse(
        """
import numpy
import numpy as np
        """, '<ast>')

    rewriter = FooImportRewriter()
    transformed = rewriter.visit(tree)

    assert len(transformed.body) == len(tree.body)

    
    assert isinstance(transformed.body[0], ast.Try)
    assert len(transformed.body[0].body) == 1
    assert isinstance(transformed.body[0].body[0], ast.Import)
    assert transformed.body[0].body[0].names[0].name == 'numpy.foo'

    

# Generated at 2022-06-14 01:53:11.146676
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('six.moves', 'six.moves')]
    node = ast3.Import(names=[ast3.alias(name='six',
                                         asname='six')])
    result = TestImportRewrite(node)
    assert result._get_matched_rewrite('six.moves') == ('six.moves', 'six.moves')
    result.visit_Import(node)
    assert result._tree_changed



# Generated at 2022-06-14 01:53:21.018884
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom(): # type: ignore
    from ..target import GeventTarget
    from ..utils.unittest import from_pyfile
    from ..utils.ast import ast_to_str

    import_to_rewrite = (
        ("future.types", "gevent.greenlet"),
        ("future.types.newobject", "gevent.greenlet"),
        ("future.builtins", "gevent.greenlet"),
        ("gevent.monkey", "gevent.monkey"),
        ("gevent.socket", "gevent.socket"),
        ("gevent.ssl", "gevent.ssl"),
        ("gevent.thread", "gevent.thread"),
        ("gevent.timeout", "gevent.timeout"),
    )

    class GeventImportRewrite(BaseImportRewrite):
        target = GeventTarget
        rewrites = import_to_

# Generated at 2022-06-14 01:53:28.449160
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils import typed_astunparse 
    from ..utils.pytest_utils import check_transformation

    tree = ast.parse('import time')
    expected_tree = ast.parse('try:\n    import time\nexcept ImportError:\n    import time1')

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('time', 'time1')]

    actual_tree = check_transformation(ImportRewrite, tree)
    assert typed_astunparse.unparse(actual_tree) == typed_astunparse.unparse(expected_tree)



# Generated at 2022-06-14 01:53:37.467139
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # test rewritten import
    import astor
    import_node = astor.to_source(ast.parse('import Something'))
    rewrite = (
        'Something',
        'REWRITTEN_Something',
    )
    cls = type('Test', (BaseImportRewrite,), {'rewrites': [rewrite], })
    result = astor.to_source(cls.transform(ast.parse(import_node)).tree)
    expected = 'try:\n    import Something\nexcept ImportError:\n    import REWRITTEN_Something'
    assert result.strip() == expected.strip()



# Generated at 2022-06-14 01:53:42.717033
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ast import parse
    from ..utils.trees import assert_ast_equal
    from ..types import CompilationTarget

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_34
        rewrites = [('test_rewrite_from', 'test_rewrite_to')]

    tree = parse('import test_rewrite_from')
    actual = TestTransformer.transform(tree).tree
    expect = parse('''
try:
    import test_rewrite_from
except ImportError:
    import test_rewrite_to
''')
    assert_ast_equal(actual, expect)


# Generated at 2022-06-14 01:53:52.919362
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as Py2Ast
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
    
    code = 'import foo'
    tree = ast.parse(code)
    new_tree = TestTransformer.transform(tree).tree
    control_tree = ast.parse('''
try:
    import foo
except ImportError:
    import bar as foo
    ''')
    assert ast.dump(new_tree) == ast.dump(control_tree)

    code = 'import foo.bar'
    tree = ast.parse(code)
    new_tree = TestTransformer.transform(tree).tree
    control_tree = ast.parse('''
try:
    import foo.bar
except ImportError:
    import bar.bar as foo
    ''')
   

# Generated at 2022-06-14 01:54:01.847620
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class FakeTransformer(BaseImportRewrite):
        rewrites = [('django.template', 'django.template_loader')]

    import astor
    tree = astor.parse('from django.template.base import Library\n'
                       'from django.template.base.tags import BaseIncludeNode')
    tree = FakeTransformer().visit(tree)