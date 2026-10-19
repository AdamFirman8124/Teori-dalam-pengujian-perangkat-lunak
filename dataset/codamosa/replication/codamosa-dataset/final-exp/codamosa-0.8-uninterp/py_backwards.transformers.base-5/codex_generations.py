

# Generated at 2022-06-14 01:44:14.917075
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    for import_text, import_rewrite_text in [
            ('import to_rewrite',
             'try:\n    import to_rewrite\nexcept ImportError:\n    import from_rewrite'),
            ('import to_rewrite.test',
             'try:\n    import to_rewrite.test\nexcept ImportError:\n    import from_rewrite.test'),
    ]:
        tree = ast.parse(import_text)
        node = tree.body[0]
        assert isinstance(node, ast.Import)

        class Rewrites(BaseImportRewrite):
            rewrites = [('to_rewrite', 'from_rewrite')]
        import_rewrite = Rewrites.transform(tree)

        assert import_rewrite.tree_changed
        import_rewrite_ast = ast

# Generated at 2022-06-14 01:44:24.814746
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Transformer(BaseImportRewrite):
        rewrites = (
            ('foo', 'bar'),
        )

    tree = ast.parse(
        'import foo.bar\n'
        'import foo.bar.baz'
    )

    result = Transformer.transform(tree)

    assert result.tree.body[0].body[0].body[0].value.body[0].value.names[0].name == 'bar'
    assert result.tree.body[0].body[0].body[0].value.body[0].value.names[0].asname == 'bar'
    assert result.tree.body[0].body[0].body[0].value.body[1].value.names[0].name == 'bar.baz'
    assert result.tree.body[0].body[0].body

# Generated at 2022-06-14 01:44:36.352145
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    import os
    import sys
    import inspect
    import pytest
    import astor
    from distutils.sysconfig import get_python_lib
    from skbuild import setup
    from cpy2py.utility.compatibility import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        sys.path.append(tmpdir)

        demo_dir = os.path.dirname(os.path.abspath(inspect.getsourcefile(BaseImportRewrite)))
        copy(os.path.join(demo_dir, 'demo_package'), os.path.join(tmpdir, 'demo_package'))

        assert not os.path.exists(os.path.join(tmpdir, 'demo_package', '__init__.py'))
        # creating the

# Generated at 2022-06-14 01:44:42.346922
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astor import codegen
    from ..tests.transformer_test import _get_tree, _get_tree_changed

    import_stmt = 'from typing import List'
    import_rewrite = 'from list import List'

    tree = _get_tree(import_stmt)
    inst = BaseImportRewrite(tree)
    changed_tree = inst.visit(tree)

    assert codegen.to_source(changed_tree) == import_rewrite
    assert inst._tree_changed is True


# Generated at 2022-06-14 01:44:53.871702
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("from threading import (\n"
                     "    Condition,\n"
                     "    Lock,\n"
                     "    Thread,\n"
                     "    RLock,\n"
                     "    Event,\n"
                     "    _start_new_thread,\n"
                     "    _allocate_lock,\n"
                     ")\n"
                     "from threading import current_thread, active_count, enumerate, main_thread\n"
                     "from threading import stack_size, time, Timer, util, Barrier\n")
    class Rewriter(BaseImportRewrite):
        rewrites = [('threading', 'test_module.threading')]
    Rewriter.transform(tree)

# Generated at 2022-06-14 01:44:57.600249
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('six', 'six_c')]
        target = 'py36'

    tree = ast.parse('import six')
    actual = TestTransformer.transform(tree)
    expected = ast.parse('''
try:
    import six
except ImportError:
    import six_c as six
''')

    assert ast.dump(actual[0], sort_keys=True) == ast.dump(expected, sort_keys=True)


# Generated at 2022-06-14 01:44:58.126897
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    pass

# Generated at 2022-06-14 01:45:05.605744
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test1(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar')]


# Generated at 2022-06-14 01:45:07.936178
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import aiohttp')
    transformer = BaseImportRewrite(tree)  # type: ignore
    transformer.rewrites = [('aiohttp', 'requests')]
    transformer.visit_Import(tree.body[0])

    assert transformer._tree_changed


# Generated at 2022-06-14 01:45:14.236985
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    inputs = """
        import collections
        import typing as T
        import unittest.mock
        import os.path
        import io.StringIO
        from mpl_toolkits.basemap import Basemap
    """
    tree = astor.parse_file(astor.code_to_ast(inputs))
    expected_outputs = """
        import collections
        import typing as T
        import_rewrite(
            previous = unittest.mock,
            current = mock
        )
        import os.path
        import import_rewrite(
            previous = io.StringIO,
            current = StringIO
        )
        from mpl_toolkits.basemap import Basemap
    """

# Generated at 2022-06-14 01:45:27.625387
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImporter(BaseImportRewrite):
        rewrites = [('test', 'rewrote')]

    node = ast.ImportFrom(module='test',
                          names=[ast.alias(name='Test', asname='T')],
                          level=0)

    result = TestImporter.transform(node)
    assert result.tree == ast.Try(body=[
        ast.ImportFrom(module='rewrote',
                       names=[ast.alias(name='Test', asname='T')],
                       level=0)
    ],
        handlers=[ast.ExceptHandler(body=[
            ast.ImportFrom(module='test',
                           names=[ast.alias(name='Test', asname='T')],
                           level=0)
        ])])

# Generated at 2022-06-14 01:45:33.287422
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    from ..utils.code_gen import to_source

    input = 'from six.moves import queue, map'
    output = 'from builtins.moves import queue, map'

    import_rewrites = [('six.moves', 'builtins.moves')]

    class ImportRewriteTransformer(BaseImportRewrite):
        rewrites = import_rewrites

    target = CompilationTarget(ImportRewriteTransformer)
    target.transform()



# Generated at 2022-06-14 01:45:43.399472
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Given
    source = "import foo\n"
    expected_source = "try:\n    import foo\nexcept ImportError:\n    import bar\n"
    expected_tree_changed = True
    expected_dependencies = []
    class M(BaseImportRewrite):
        rewrites = [('foo', 'bar')]
    # When
    result = M.transform(ast.parse(source))
    # Then
    assert result.tree.body[0].__dict__ == ast.parse(expected_source).body[0].__dict__
    assert result.tree_changed == expected_tree_changed
    assert result.dependencies == expected_dependencies



# Generated at 2022-06-14 01:45:51.216956
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from transpyler.types import CompilationTarget
    from transpyler.utils import runner
    import os

    test_dir = os.path.dirname(__file__)
    replace_map = {
        'import_rewrite_src.a': ('import_rewrite_src', 'import_rewrite_src2')
    }

    class TestImportRewrite(BaseImportRewrite):
        rewrites = list(replace_map.values())
        target = CompilationTarget.PYTHON_33

    with open(os.path.join(test_dir, 'import_rewrite_src.py')) as file:
        tree = astor.parse_file(file)

        result = TestImportRewrite.transform(tree)


# Generated at 2022-06-14 01:46:01.611719
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    import unittest.mock

    from ..types import CompilationTarget, TransformationResult
    from ..utils.ast_utils import ast_to_text

    tree = ast.parse('''
from test_replaced import test_replaced
from test_not_replaced import test_not_replaced
from test_replaced.test_replaced import test_replaced
from test_not_replaced.test_replaced import test_replaced
from test_replaced.test_not_replaced import test_not_replaced
from test_not_replaced.test_not_replaced import test_not_replaced
        ''')

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PY2

# Generated at 2022-06-14 01:46:12.556894
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    # For cases where no rewriting is done
    def _get_import_from(module, names, level=None):
        if level is not None:
            return ast.ImportFrom(module=module,
                                  names=[ast.alias(name=name,
                                                   asname=alias) for name, alias in names],
                                  level=level)
        else:
            return ast.ImportFrom(module=module,
                                  names=[ast.alias(name=name,
                                                   asname=alias) for name, alias in names])


# Generated at 2022-06-14 01:46:19.972596
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Transformer(BaseImportRewrite):
        rewrites = [('a', 'b')]

    tree = ast.parse("from a import b as x; from a import c, d")
    result = Transformer.transform(tree)
    assert result.tree.body[1].body[0].values[1].value.values[0].value.value == 'b.b'
    assert hasattr(result.tree.body[1].body[0], 'finalbody')
    assert isinstance(result.tree.body[1].body[1].value, ast.ImportFrom)

# Generated at 2022-06-14 01:46:31.380287
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestClass(BaseImportRewrite):
        rewrites = [
            ('aiohttp.web', 'sanic.app'),
            ('aiohttp.web.BaseRequest', 'sanic.request')
        ]

    tree = ast.parse('''
    from aiohttp.web import BaseRequest as req
    from aiohttp.web import BaseRequest as req2
    from aiohttp.web.BaseRequest import get_path
    from aiohttp.web.BaseRequest import *
    import aiohttp.web
    import aiohttp.web.BaseRequest
    ''')
    transformer = TestClass(tree)
    transformer.visit(tree)
    assert transformer._tree_changed == True


# Generated at 2022-06-14 01:46:37.312428
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_statement = ast.Import(names=[
        ast.alias(name='a',
                  asname='a')])

    rewrite = [('a', 'b')]
    tree = BaseImportRewrite.transform(import_statement)
    assert tree.changed



# Generated at 2022-06-14 01:46:44.959593
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Test(BaseImportRewrite):
        rewrites = [(
            'translator.tests.utils.test_rewrites',
            'translator.tests.utils.test_rewrites2'
        )]

    tree = ast.parse('from translator.tests.utils.test_rewrites import X')
    inst = Test(tree)
    inst.visit_ImportFrom(tree.body[0])
    assert inst._tree_changed



# Generated at 2022-06-14 01:47:07.240146
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .testing.utils import assert_run_ast_transform, parse_ast

    source = """
    import module

    module.func()
    """

    expected = """
    try:
        import module
    except ImportError:
        import module as module
    module.func()
    """

    tree = parse_ast(source)
    BaseImportRewrite.rewrites = [('module', 'module')]
    tree = BaseImportRewrite.transform(tree).tree

    assert_run_ast_transform(tree,
                             source,
                             expected,
                             imports=['module'])



# Generated at 2022-06-14 01:47:15.891190
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.ast import parse
    import inspect
    import os

    class Simple(BaseImportRewrite):
        rewrites = []

    class Rewrite(BaseImportRewrite):
        rewrites = [('os', 'os.path')]

    class Rewrite2(BaseImportRewrite):
        rewrites = [('math', 'math.math')]

    # Basic cases
    assert Simple().visit(parse('''
        import numpy
    ''')) == parse('''
        import numpy
    ''')
    assert Rewrite().visit(parse('''
        import os
    ''')) == parse('''
        try:
            import os
        except ImportError:
            import os.path
    ''')

# Generated at 2022-06-14 01:47:28.933985
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    class TestTransformer(BaseImportRewrite):
        rewrites = (('six.moves', 'foo.bar'),)

    inst = TestTransformer(ast.Module(body=[]))

    import_from = ast.ImportFrom(level=0,
                                 module="six.moves",
                                 names=[ast.alias(name="six.moves.urllib.parse.urlparse",
                                                  asname="urllib_parse_urlparse"),
                                        ast.alias(name="six.moves.urllib.parse.urljoin",
                                                  asname="urllib_parse_urljoin")])
    inst.visit(import_from)

# Generated at 2022-06-14 01:47:38.716522
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from astor.code_gen import to_source
    from .visitor import print_ast

    class MyTransformer(BaseImportRewrite):
        rewrites = [('a.b', 'c.d')]

    node = ast.parse("""
from a.b import foo
from a.b.bar import baz

from a.b.foo import qux as quxx

from a.b.bar import qux as quxx

from a.b.bar import *
    """).body
    # print_ast(node)
    t = MyTransformer.transform(node)
    # print_ast(node)
    print(t)
    print(to_source(node))


# Generated at 2022-06-14 01:47:48.096309
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as _ast
    import astor as _astor
    import_node = _ast.parse(
        'from foo import bar')

    import_copy = _astor.to_source(import_node)
    transform = BaseImportRewrite(import_node)
    import_node = transform.visit(import_node)
    modified = _astor.to_source(import_node)
    assert modified == "try:\n    from foo import bar\n\nexcept ImportError:\n    from baz import bar\n"

    transform._tree_changed = False
    import_node = transform.visit(import_node)
    unmodified = _astor.to_source(import_node)
    assert import_copy == unmodified



# Generated at 2022-06-14 01:47:57.710632
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest.mock as mock
    transformer_mock = mock.Mock()

    BaseImportRewrite.rewrites = [
        (from_, to)
        for from_, to in {
            'old.mod': 'new.mod',
            'old.func': 'new.func',
        }.items()
    ]

    tree = ast.parse('''
import old.mod.a
from old.mod.b import c
from old.mod.b import *

from old.mod.b import d as f
from old.mod.b import e as g
''')

    BaseImportRewrite.transform(tree)

# Generated at 2022-06-14 01:48:07.971777
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    rewriter = BaseImportRewrite()

    tree = ast.parse(
        "from a.b.c import Test"
    )
    rewriter.rewrites = [('a.b.c', 'd.e.f')]
    rewriter.visit(tree)

    assert ast.dump(tree) == "import sys\ntry:\n    from d.e.f import Test\nexcept ImportError:\n    from a.b.c import Test\n"

    tree = ast.parse(
        "from importlib import import_module"
    )
    rewriter.rewrites = [('importlib', 'six')]
    rewriter.visit(tree)


# Generated at 2022-06-14 01:48:17.702987
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewrites = [
        ('foo', 'bar'),
    ]
    class Tr(BaseImportRewrite):
        rewrites = rewrites
    # Import is not changed
    node = ast.parse('''import foo''').body[0]
    assert Tr.transform(node).tree == node

    # Import is replaced
    node = ast.parse('''import foo''').body[0]
    assert Tr.transform(node).tree == ast.parse('''
try:
    import foo
except ImportError:
    import bar
''').body[0]

    # Nested import is replaced
    node = ast.parse('''import foo.bar''').body[0]

# Generated at 2022-06-14 01:48:28.699307
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ....tests import test_packages
    from .... import parse
    from . import transform_import_rewriters
    from . import transforms
    from . import node_transformer_utils

    import_rewrite_transformer = node_transformer_utils.create_import_rewrite_transformer(
        import_rewriters=transform_import_rewriters.get_import_rewriters(
            target=transforms.PythonTarget))

    target = test_packages.TestPackages().load_target(
        name='python-pytest-test-package',
        base=test_packages.PackageSource.TEST)

    with open(target.target_path, 'r', encoding='utf8') as f:
        [tree] = parse(f.read())

    [tree] = import_rewrite_transformer.transform(tree)

# Generated at 2022-06-14 01:48:35.906886
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import pip
    import astunparse

    from ..utils.nodes import dump_ast

    class ExampleTransformer(BaseImportRewrite):
        rewrites = [('pip', 'pip-mock')]

    code = 'import pip'

    tree = ast.parse(code)
    tree = ExampleTransformer().visit(tree)

    # FIXME: astunparse import fails here
    # assert astunparse.dump_python_source(tree) == 'try:\n' \
    #                                               '    import pip\n' \
    #                                               'except ImportError:\n' \
    #                                               '    import pip-mock'


# Generated at 2022-06-14 01:48:55.573528
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..compiler import to_source
    from ..types import Transformations

    rewrite = BaseImportRewrite(ast.parse(''))

# Generated at 2022-06-14 01:49:00.282936
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    source = 'import foo'
    tree = astor.parse_file(source)
    BaseImportRewrite.rewrites = [('foo', 'bar')]
    BaseImportRewrite.transform(tree)
    assert astor.to_source(tree) == 'try:import foo\nexcept ImportError:import bar'



# Generated at 2022-06-14 01:49:08.749839
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.ast_checker import assert_equal_ast

    class TestRewrite(BaseImportRewrite):
        rewrites = [('old', 'new')]

    original_source = """\
import old
"""
    expected_source = """\
try:
    import old
except ImportError:
    import new
"""
    module = ast.parse(original_source)
    result = TestRewrite.transform(module)
    assert str(result.new_tree) == expected_source
    assert_equal_ast(original_source, expected_source, result)



# Generated at 2022-06-14 01:49:19.251101
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    def test(tree, expected_tree, rewrites):
        class TestImportRewrite(BaseImportRewrite):
            rewrites = rewrites

        assert TestImportRewrite.transform(ast.parse(tree)).new_tree == ast.parse(expected_tree)

    test('import requests', 'import requests', [])
    test('import requests', 'import requests', [('aiohttp', 'requests')])
    test('import requests', 'import aiohttp', [('aiohttp', 'requests')])
    test('import requests', 'import requests', [('aiohttp', 'requests'), ('foo', 'bar')])
    test('import aiohttp', 'import requests', [('aiohttp', 'requests')])
    test('import aiohttp', 'import aiohttp', [('foo', 'bar')])


# Generated at 2022-06-14 01:49:29.233420
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..testutils.python_wrappers import python_to_ast

    class ExampleCase(BaseImportRewrite):
        dependencies = ['typed_ast', 'typing']
        rewrites = [
            ('BuiltinSuper', 'super'),
            ('typing', 'typing')
        ]

    code = 'from typing import Union, Tuple, List'
    result = '''try:
    from typing import Union, Tuple, List
except ImportError:
    from typing import Union, Tuple, List'''

    tree = python_to_ast(code, target=CompilationTarget.PY36)
    ExampleCase.transform(tree)

    assert python_to_ast(result, target=CompilationTarget.PY36).body[0] == tree.body[0]


# Generated at 2022-06-14 01:49:42.379811
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    @snippet
    class Foo(BaseImportRewrite):
        rewrites = []

    tree = ast.parse("""
    import foo
    """)

    result = Foo.transform(tree)
    assert result.changed is False
    assert ast.dump(result.tree) == ast.dump(tree)

    @snippet
    class Foo(BaseImportRewrite):
        rewrites = [('foo', 'foo_rewrite')]

    tree = ast.parse("""
    import foo
    """)

    result = Foo.transform(tree)
    assert result.changed is True

# Generated at 2022-06-14 01:49:48.907178
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from_ = 'ast'
    to = 'ast3'
    node = ast.Import(names=[ast.alias(name=from_,
                                      asname=None)])

    rewrote = BaseImportRewrite(node).visit(node)
    assert isinstance(rewrote, ast.Try)
    assert rewrote.body[0].names[0].name == to



# Generated at 2022-06-14 01:50:03.264017
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

# Generated at 2022-06-14 01:50:13.742127
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('json', 'ujson')]

    expected = ast.Import(names=[ast.alias(name='ujson')])
    try:
        extend(ast.Import(names=[ast.alias(name='json')]))
    except ImportError:
        extend(expected)

    tree = ast.parse(textwrap.dedent("""
    import json
    """), mode='exec')

    result = ImportRewrite.transform(tree)
    assert result.result == ast.parse(textwrap.dedent("""
    try:
        extend(ast.Import(names=[ast.alias(name='json')]))
    except ImportError:
        extend(ast.Import(names=[ast.alias(name='ujson')]))
    """), mode='exec')


# Generated at 2022-06-14 01:50:20.940898
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class FakeTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    import astor
    a = astor.code_to_ast('from foo import *')
    b = astor.to_source(a)
    assert FakeTransformer.transform(a) == TransformationResult(
        tree=astor.parse_file('_test_BaseImportRewrite_visit_ImportFrom.py'),
        tree_changed=True,
        dependencies=['bar'])

# Generated at 2022-06-14 01:50:50.945744
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astunparse
    import astor
    source = """
    from typing import Dict
    from sys import path as sys_path
    from os import getcwd, sep as os_sep
    from sys.path import listdir as ls
    """

    tree = ast.parse(source)
    transformer = BaseImportRewrite()
    tree = transformer.visit(tree)

# Generated at 2022-06-14 01:51:01.262785
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    code = """
from datetime import date
date()
"""
    tree = ast.parse(code)
    node = tree.body[0]

    class TestTransformer(BaseImportRewrite):
        rewrites = [('datetime', 'datetime.datetime')]

    TestTransformer.transform(tree)
    rewrote = tree.body[0]  # type: ignore

    assert isinstance(rewrote, ast.Try)

    try_ = rewrote
    assert isinstance(try_.body[0], ast.Import)
    assert try_.body[0].names[0].name == 'datetime.datetime'
    assert try_.body[0].names[0].asname == 'date'

    excepts = try_.handlers
    assert len(excepts) == 1

# Generated at 2022-06-14 01:51:08.048812
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import parse
    tree = parse("from module import DataClass, a, b")
    BaseImportRewrite.rewrites = [('module', 'new_module')] # type: ignore
    BaseImportRewrite().visit(tree)
    expected = "try:\n    from module import DataClass, a, b\nexcept ImportError:\n    from new_module import DataClass, a, b\n"
    text = ast.unparse(tree, '<unknown>')
    assert text == expected

# Generated at 2022-06-14 01:51:14.882930
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import string
    import random
    node = ast.parse("import foo")
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [
            ('foo','baz')
        ]
    obj = TestBaseImportRewrite(node)
    node = obj.visit_Import(node)
    assert "try" in ast.dump(node)


# Generated at 2022-06-14 01:51:24.874421
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_snippet = """from django.utils import _os
from future.utils import _bytes

print(_os.path)
print(_bytes.decode())
"""
    tree = ast.parse(import_snippet)
    rewriter = BaseImportRewrite(tree)

    class FakeRewrite(BaseImportRewrite):
        rewrites = [
            ('django.utils', 'six.moves'),
            ('future.utils', 'six')]

    rewriter.rewrites = FakeRewrite.rewrites[:]
    rewriter.visit_ImportFrom(tree.body[0])
    assert ast.dump(tree.body[0]).strip() == 'try: from django.utils import _os\nexcept ImportError: from six.moves import _os'


# Generated at 2022-06-14 01:51:34.553514
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('cryptography', 'cryptography.legacy')]

    source = '''
import cryptography as crypto

foo = crypto.bar
'''
    expected_source = '''
try:
    import cryptography as crypto
except ImportError:
    import cryptography.legacy as crypto

foo = crypto.bar
'''

    tree = ast.parse(source)
    tree = TestImportRewrite.transform(tree).tree
    source = astor.to_source(tree)
    assert source == expected_source



# Generated at 2022-06-14 01:51:47.669860
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import io as StringIO  # type: ignore
    import six  # type: ignore

    class TestTransformer(BaseImportRewrite):
        rewrites = [('six.moves.StringIO', 'io')]

    code = 'import six.moves.StringIO'
    tree = ast.parse(code)
    transformer = TestTransformer(tree)
    node = tree.body[0]

    assert isinstance(node, ast.Import)
    transformer.visit_Import(node)

    assert tree.body[0].names[0].name == 'six.moves.StringIO'
    assert isinstance(tree.body[0].body[0], ast.Import)
    assert tree.body[0].body[0].names[0].name == 'io'



# Generated at 2022-06-14 01:51:55.057359
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest.mock
    import typing_inspect_trickery as typing
    import astunparse

    cls = BaseImportRewrite
    cls.rewrites = [('typing_inspect_trickery.typing', 'typing'),
                    ('typing_inspect_trickery.utils', 'typing.utils')]

    import_from_unrelated = '''from unrelated import *'''
    import_from_unrelated_tree = ast.parse(import_from_unrelated)

    result = cls.transform(import_from_unrelated_tree)
    new_tree = result[0]
    assert result[1] is False
    assert astunparse.unparse(new_tree) == import_from_unrelated


# Generated at 2022-06-14 01:52:06.024843
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    import_node = ast.Import(names=[ast.alias(name='foo', asname=None)])
    import_rewrite_node = ast.Import(names=[ast.alias(name='bar', asname=None)])
    try_node = ast.Try(
        body=[import_rewrite_node],
        handlers=[ast.ExceptHandler(type=None,
                                    name=None,
                                    body=[import_node])],
        orelse=[],
        finalbody=[]
    )

    import_from_node = ast.ImportFrom(
        module='foo',
        names=[ast.alias(name='bar', asname=None)],
        level=0
    )

# Generated at 2022-06-14 01:52:17.294727
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    rewrites = [('http.client', 'urllib.request')]

    class ImportRewrite(BaseImportRewrite):
        rewrites = rewrites

    node = ast.parse('import http.client').body[0]
    out = ImportRewrite.visit(node)
    assert isinstance(out, ast.Try)
    assert isinstance(out.body[0], ast.Import)
    assert out.body[0].names[0].name == 'urllib.request'

    node = ast.parse('import http.client.server').body[0]
    out = ImportRewrite.visit(node)
    assert isinstance(out, ast.Try)
    assert isinstance(out.body[0], ast.Import)

# Generated at 2022-06-14 01:53:02.531768
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    source = 'from six.moves.urllib.parse import urlparse'
    tree = ast.parse(source)
    node = tree.body[0]
    assert isinstance(node, ast.ImportFrom)
    transformer = BaseImportRewrite()
    result = transformer.visit_Import(node)
    assert isinstance(result, ast.Try)
    assert isinstance(result.body[0], ast.ImportFrom)
    assert isinstance(result.body[1], ast.ExceptHandler)
    assert 'from urllib.parse import urlparse' in astor.to_source(result.body[0])
    assert 'from six.moves.urllib.parse import urlparse' in astor.to_source(result.body[1].body[0])



# Generated at 2022-06-14 01:53:17.497489
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Example:
    #   from six.moves.urllib.parse import urlparse
    #   from six import print_ as print
    #   from future.utils import iteritems
    #   from __future__ import print_function
    #   from builtins import map
    #   from urllib.request import urlopen
    #   from django.utils.text import slugify
    import_from_modules = [
        'six.moves.urllib.parse',
        'six',
        'future.utils',
        '__future__',
        'builtins',
        'django.utils.text'
    ]

# Generated at 2022-06-14 01:53:27.861683
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    """Unit test for method visit_ImportFrom of class BaseImportRewrite"""
    tree = ast.parse(
        """
        from os.path import join as jn
        from signalfx.core.agent import SignalFxBaseAgent
        from signalfx.core.signals import SignalFxBaseSignal, SignalFxBaseSquareSignal
        from signalfx.core import agent, signals
        from signalfx.core.agent import *
        from signalfx.core.signals import *
        import os
        import os.path
        import signalfx.core.signals
        import signalfx.core.agent
        import signalfx
        import signalfx.core.signals as sfs
        import signalfx.core.agent as sfa
        import signalfx as sf
        """
    )

   

# Generated at 2022-06-14 01:53:39.549735
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast

    # Replaces import from with try/except with old and new import module.
    class Test(BaseImportRewrite):  # type: ignore
        rewrites = [
            ('six.moves', 'six')]

    code = 'from six.moves import urllib\n'
    tree = ast.parse(code)
    expected_code = 'from six.moves import urllib\ntry:\n    from six import urllib\nexcept ImportError:\n    from six.moves import urllib\n'

    Test.transform(tree)
    result_code = ast.dump(tree)
    assert result_code == expected_code

    # Replaces import from with try/except with old and new import module.

# Generated at 2022-06-14 01:53:49.900361
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import os
    import io
    from ..tests.samples.sample_base_import_rewrite import a_transformer
    from ..tests.samples.sample_base_import_rewrite import get_source
    from ..utils import dump_ast

    transformer = a_transformer()  # type: BaseImportRewrite
    source = get_source()
    ast_ = ast.parse(source)
    transformer.visit(ast_)

    source = source.replace('import ast', 'try:\n    import ast\n'
                                          'except ImportError:\n    import ast3\n')
    source = source.replace('ast.Str', 'ast3.Str')
    source = source.replace('ast.Name', 'ast3.Name')
    source = source.replace('ast.expr', 'ast3.expr')

   