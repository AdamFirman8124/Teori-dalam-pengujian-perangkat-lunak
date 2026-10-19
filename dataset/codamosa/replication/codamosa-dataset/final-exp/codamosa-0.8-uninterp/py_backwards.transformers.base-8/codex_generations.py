

# Generated at 2022-06-14 01:44:18.206343
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    # input test data
    from_, to = 'importdir1.dir2.module1', 'importdir2.module1'
    tree = ast.parse('''
import importdir1.dir2.module1
import importdir1.dir2.module1 as mod1
import importdir1.dir2.module2 as mod2, importdir1.dir2.module3 as mod3
import importdir2.module1 as module1, importdir2.module2 as module2
''')

    # expected result

# Generated at 2022-06-14 01:44:20.924213
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    transformer = BaseImportRewrite([], [])
    with pytest.raises(NotImplementedError):
        transformer.visit_Import(None)


# Generated at 2022-06-14 01:44:30.598529
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class RewriteUnittest(BaseImportRewrite):
        rewrites = [
            ('from_', 'to'),
            ('from_with_another_name', 'to_with_another_name'),
        ]

    import_from = ast.parse('from from_.module import x').body[0]
    import_from_module_rewrite = ast.parse('from module import x').body[0]
    import_from_module_rewrite = RewriteUnittest.transform(import_from_module_rewrite).tree.body[0]
    assert RewriteUnittest.transform(import_from).tree.body[0] == import_from_module_rewrite

    import_from = ast.parse('from from_.module import x, y').body[0]

# Generated at 2022-06-14 01:44:42.155934
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from astor.code_gen import to_source
    from ..utils import DummySource, DummyTarget
    from ..exceptions import CompileError
    from typing import Optional

    class TestClass(BaseImportRewrite):
        rewrites = [
            ('a.b', 'c.d'),
        ]

    source = DummySource()
    target = DummyTarget()

    source.set_source(
        'import a.b'
    )
    source.set_source(
        'import a.b.c'
    )
    source.set_source(
        'import a.b.c as d'
    )
    source.set_source(
        'import a.b.c as d, b.d.e'
    )

    result = TestClass.transform(source.get_tree())
   

# Generated at 2022-06-14 01:44:53.732457
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    """Test for method visit_Import of class BaseImportRewrite."""
    from typed_ast import convert
    from textwrap import dedent

    class NodeTransformer(BaseImportRewrite):
        rewrites = [('foo.bar', 'baz.bar')]


# Generated at 2022-06-14 01:45:04.329983
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import copy
    import textwrap

    class NewTransformer(BaseImportRewrite):
        rewrites = [('os', 'new_os')]

    # Test Python 3.6
    tree = ast.parse(textwrap.dedent(
        """
        from os import path as p, mkdir, rename as r

        from os.path import dirname as dn, join as j, splitext as se
        """
    ))
    tree_copy = copy.deepcopy(tree)
    result = NewTransformer.transform(tree)

# Generated at 2022-06-14 01:45:09.816784
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from_ = 'a'
    to = 'b'

    import_ = ast.Import(names=[ast.alias(name='a', asname='b')])
    ast.fix_missing_locations(import_)
    import_to = ast.Import(names=[ast.alias(name='b', asname='b')])
    ast.fix_missing_locations(import_to)

    class ImportRw(BaseImportRewrite):
        rewrites = [(from_, to)]

    result = ImportRw.transform(import_)
    assert isinstance(result.tree, ast.Try)

    tree = result.tree
    assert isinstance(tree.body[0], ast.Import)
    assert tree.body[0].names[0].name == from_

# Generated at 2022-06-14 01:45:20.041929
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    source = '''
    from typing import List, Dict
    
    class Autocomplete:
        def __init__(self):
            self._data: Dict[int, List[str]] = {}
    '''
    tree = ast.parse(source, mode='exec')
    assert BaseImportRewrite.transform(tree).changed is True

    expected = '''
    from typing import List, Dict


    class Autocomplete:
        def __init__(self):
            self._data: Dict[int, List[str]] = {}
    '''

    class TypingBaseImportRewrite(BaseImportRewrite):
        rewrites = [('typing', 'abc')]
        target = 'python35'


    assert ast.dump(tree) == expected

# Generated at 2022-06-14 01:45:26.930934
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from .. import Context
    from ..types import CompilationTarget

    stmt = ast.parse('import os')

    class TestTransformer(BaseImportRewrite):
        rewrites = [('os', 'os.path')]

    result = TestTransformer.transform(stmt)
    expected = ast.parse('''
try:
    import os
except ImportError:
    import os.path as os
    ''').body

    assert (result.tree.body == expected)



# Generated at 2022-06-14 01:45:33.039487
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("from previous import alias", mode="exec")
    rewrites = [("previous", "new")]

    transformer = BaseImportRewrite(tree)
    transformer.rewrites = rewrites

    expected = ast.parse("""try:
    from previous import alias
except ImportError:
    from new import alias""", mode="exec")

    actual = transformer.visit_ImportFrom(tree.body[0])

    assert ast.dump(actual) == ast.dump(expected)


# Generated at 2022-06-14 01:45:45.499561
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import typed_ast.ast3 as ast
    from textwrap import dedent
    from typed_astunparse.unparser import Unparser

    class FooTransformer(BaseImportRewrite):
        rewrites = [
            ('foo', 'bar'),
        ]

    class TestVisitImport(unittest.TestCase):
        def test1(self):
            code = dedent("""
            import foo""")
            expected = dedent("""
            try:
                import foo
            except ImportError:
                import bar as foo""")
            tree = ast.parse(code)
            actual = Unparser(FooTransformer().visit(tree))
            self.assertEqual(expected, str(actual))

        def test2(self):
            code = dedent("""
            import foo.bar""")

# Generated at 2022-06-14 01:46:00.609708
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import astunparse

    rewrites = [('importlib', 'importlib2'), ('re', 're2')]

    class Test(BaseImportRewrite):
        target = 'python38'
        rewrites = rewrites

    expected = (
        "try:\n"
        "    import importlib.abc as abc  # type: ignore\n"
        "except ImportError:\n"
        "    import importlib2.abc as abc  # type: ignore\n"
        "\n"
        "try:\n"
        "    import re\n"
        "except ImportError:\n"
        "    import re2\n"
    )

    source = '''
from importlib import abc # type: ignore

import re
'''
    tree = astor.parse_

# Generated at 2022-06-14 01:46:05.331989
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..types import CompilationTarget
    from ..utils.tree import get_tree
    from ..transformers.imports import TryImport

    for _, tree in get_tree('import importlib.import_module'):
        t = TryImport().transform(tree)
        tree_changed, _, _ = t.tree_changed, t.tree, t.dependencies
        assert tree_changed is True, 'import importlib.import_module should be replaced'


# Generated at 2022-06-14 01:46:13.700752
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestRewrite(BaseImportRewrite):
        rewrites = [('asyncio', 'trollius')]

    source = 'import asyncio'
    tree = ast.parse(source)
    node = tree.body[0]  # type: ast.Import

    new_node = TestRewrite.visit_Import(node)
    assert isinstance(new_node, ast.Try)

    new_node = ast.fix_missing_locations(new_node)
    check_source = ast.NodeVisitor().visit(new_node)
    assert isinstance(check_source, ast.Try)
    assert check_source.handlers[0].type.id == 'ImportError'
    assert check_source.handlers[0].body[0].names[0].name == 'trollius'

    # Part

# Generated at 2022-06-14 01:46:22.143954
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from textwrap import dedent
    from typed_ast.ast3 import parse
    from .base import CompilationTarget, BaseNodeTransformer

    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_27
        rewrites = [
            ('module1', 'module_1.module1'),
            ('module2', 'module_2.module2')
        ]

    code = dedent('''
    from module1 import *
    from module1 import module2
    from module3 import module1
    ''')

    tree = parse(code)

    actual = TestTransformer.transform(tree)
    assert isinstance(actual._tree.body[0].body[0], ast.Try)
    assert isinstance(actual._tree.body[1].body[0], ast.Try)
   

# Generated at 2022-06-14 01:46:31.834532
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import parse
    from astpretty import pprint

    class Transformer(BaseImportRewrite):
        rewrites = [
            ('foo.bar', 'bar.foo')
        ]

        @classmethod
        def transform(cls, tree):
            inst = cls(tree)
            inst.visit(tree)
            return TransformationResult(tree, inst._tree_changed, cls.dependencies)

    tree_before = parse('import foo.bar')
    tree_after = parse(
"""
try:
    import foo.bar as bar
except ImportError:
    import bar.foo as bar
"""
    )
    res = Transformer.transform(tree_before)
    tree_after = res.tree
    print(res.tree_changed)
    print('-' * 80)

# Generated at 2022-06-14 01:46:42.579576
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..target.javascript import ES6
    from ..transformer.import_rewrite import BaseImportRewrite
    import astunparse
    BaseImportRewrite.target = ES6
    BaseImportRewrite.rewrites = [('typing', 'libtyping')]
    source = '''import typing'''
    source_tree = ast.parse(source)
    BaseImportRewrite.transform(source_tree)
    assert astunparse.unparse(source_tree) == 'try:\n    import typing\nexcept ImportError:\n    import libtyping'


# Generated at 2022-06-14 01:46:52.112445
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..transforms import base_import_rewrite
    from typed_ast import ast3 as ast
    # ast_ = ast.parse('import os')
    # print(ast.dump(ast_, annotate_fields=True, include_attributes=True))
    # print(ast)
    base_import_rewrite.BaseImportRewrite._tree_changed = False
    base_import_rewrite.BaseImportRewrite.rewrites = [('os', 'new_os')]
    # nodes = base_import_rewrite.BaseImportRewrite(ast.Module(body=[ast.Import(names=[ast.alias(name='os', asname=None)])])).visit(ast.Module(body=[ast.Import(names=[ast.alias(name='os', asname=None)])]))
    # for node in nodes:

# Generated at 2022-06-14 01:47:04.876905
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    code = """
from typing import List
from six.moves import map

x = [1, 2, 3]
# type: List[int]
m = map
"""
    tree = ast.parse(code)
    BaseImportRewrite.transform(tree)
    print(astor.to_source(tree))
    assert(astor.to_source(tree) == '\nimport six.moves.map\ntry:\n    from typing import List\n    from six.moves import map\nexcept ImportError:\n    from typing import List\n    from future.moves.map import map\n\nx = [1, 2, 3]\n# type: List[int]\nm = map\n')

# Generated at 2022-06-14 01:47:12.805799
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..compiler import Compiler

    for old, new in BaseImportRewrite.rewrites:
        code = "import {}".format(old)
        tree = ast.parse(code)
        BaseImportRewrite.transform(tree)
        compiler = Compiler(target=CompilationTarget.PY32)
        new_code = compiler.compile_ast(tree)

        expected = 'try:\n    import {0}\nexcept ImportError:\n    import {1}'.format(old, new)
        assert new_code == expected


# Generated at 2022-06-14 01:47:28.884615
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('requests', 'urllib3')]

    tree = ast.parse("import requests")
    new_node = TestImportRewrite.transform(tree)
    assert new_node.changed
    assert isinstance(tree.body[0], ast.Try)
    assert isinstance(tree.body[0].body[0].body[0], ast.Import)
    assert tree.body[0].body[0].body[0].names[0].name == 'requests'
    assert tree.body[0].body[1].body[0].body[0].names[0].name == 'urllib3'
    assert isinstance(tree.body[0].body[1].body[1], ast.Raise)

# Generated at 2022-06-14 01:47:35.026019
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    input_ = ast.parse('from e import f')
    output = ast.parse(
        'try:\n    from e import f\nexcept ImportError:\n    from d import f')

    class FakeTransformer(BaseImportRewrite):
        rewrites = [('e', 'd')]

    result = FakeTransformer.transform(input_)

    assert result.tree == output, 'BaseImportRewrite for import statement failed'



# Generated at 2022-06-14 01:47:45.762494
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Given
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'foobar')]

    tree = ast.parse("""
import foo
import foobar
import baz
""")

    # When
    transform = TestTransformer.transform(tree)

    # Then
    assert transform.changed == True
    assert transform.target == tree

# Generated at 2022-06-14 01:47:52.658270
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Rewrite(BaseImportRewrite):
        target = 'py2'
        rewrites = [('some_module', 'some.other_module')]

    sourcecode = """
import some_module
"""
    tree = ast.parse(sourcecode)
    new_tree = Rewrite.transform(tree).tree

# Generated at 2022-06-14 01:48:00.103280
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Given
    class TestNodeTransformer(BaseImportRewrite):
        rewrites = [('six.moves', 'six')]

    tree = ast.parse('import six.moves')

    # When
    result = TestNodeTransformer.transform(tree)

    # Then
    assert result.tree == ast.parse(
        'try:\n    import six.moves\n'
        'except ImportError:\n    import six')



# Generated at 2022-06-14 01:48:10.290172
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import parse
    from ..utils import codegen

    class MyTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    t = MyTransformer(parse('from foo.a import b as bb, c'))
    result = t.visit(t._tree)

    assert codegen(result) == 'try:\n    from foo.a import b as bb, c\nexcept ImportError:\n    from bar.a import b as bb, c'

    t = MyTransformer(parse('from foo import a'))
    result = t.visit(t._tree)

    assert codegen(result) == 'try:\n    from foo import a\nexcept ImportError:\n    import bar'



# Generated at 2022-06-14 01:48:17.314896
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('os', 'posix')]

    code = '''
    import os
    '''

    tree = ast.parse(code)
    import_rewrite = ImportRewrite(tree)
    import_rewrite.visit(tree)
    result = astor.to_source(tree)
    expected = '''
    try:
        import os
    except ImportError:
        import posix
    '''

    assert result == expected


# Generated at 2022-06-14 01:48:28.410984
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Test(BaseImportRewrite):
        target = 'test'
        rewrites = (
            ('test', 'testing'),
        )

    tree_ = ast.parse('''
    import test
    ''')
    assert Test.transform(tree_).tree == ast.parse('''
    try:
        import test
    except ImportError:
        import testing
    ''')

    tree_ = ast.parse('''
    import test.module
    ''')
    assert Test.transform(tree_).tree == ast.parse('''
    try:
        import test.module
    except ImportError:
        import testing.module
    ''')

    tree_ = ast.parse('''
    import test.module.foo
    ''')
    assert Test.transform(tree_).tree == ast

# Generated at 2022-06-14 01:48:35.882237
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    
    # Test for condition: rewrite
    # Expecting: self._replace_import
    tree = ast.parse("""
import some_module
    """)
    dependencies = []
    instance = BaseImportRewrite(tree)
    result = instance.visit_Import(tree.body[0])
    assert isinstance(result, ast.Try)
    assert tree.body[0] == result.handlers[0].body[0]
    assert isinstance(result.handlers[1].body[0], ast.Import)



# Generated at 2022-06-14 01:48:43.324541
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    import sys
    import ast, six

    class ImportTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON_27
        rewrites = [('six', 'six.moves')]
        dependencies = []

    inst = ImportTransformer(ast.parse('import six'))
    result = inst.visit(inst._tree)

    assert astor.to_source(result).strip() == "try:\n    import six\nexcept ImportError:\n    import six.moves as six"



# Generated at 2022-06-14 01:49:02.709775
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    from string import Template
    from unittest import TestCase
    from typed_ast.ast3 import parse

    from . import BaseImportRewrite

    class TestTransformer(BaseImportRewrite):
        target = "2to3"
        rewrites = [('configparser', 'ConfigParser')]


# Generated at 2022-06-14 01:49:14.129845
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    rewrites = [
        ('a.b', 'c.d'),
        ('e.f.g', 'h.i')
    ]

    class TestImportRewrite(BaseImportRewrite):
        rewrites = rewrites

    import a.b as b
    import a.b as c
    import a.b.e
    import a.b.e.f as f
    import a.b.e.f.g as g
    import a.b.e.f.g.h as h

    import a.b as d
    import a.b.e as b
    import a.b.x.e as a
    import a.b.e.f as e
    import a.b.e.f.g as f
    import a.b.e.f.g.h as g

    import a

# Generated at 2022-06-14 01:49:22.119608
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse(
    """
    import os
    from sys import *
    from os import path, path2
    """
    )

    transformer = BaseImportRewrite()
    transformer.rewrites = [('os', 'os.orig')]
    transformer.visit(tree)
    assert transformer._tree_changed

    code = compile(tree, '', 'exec')
    ns = {}
    exec(code, ns)

    assert ns['os'] == os

    assert ns['path'] == os.path
    assert ns['path2'] == os.path2



# Generated at 2022-06-14 01:49:30.651638
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor  # type: ignore

    import_stmt = ast.parse("import base64")
    import_stmt_visited = BaseImportRewrite.visit_ImportFrom(import_stmt)  # type: ignore
    assert astor.to_source(import_stmt) == astor.to_source(import_stmt_visited)

    import_from_stmt = ast.parse("from base64 import b64encode")
    import_from_stmt_visited = BaseImportRewrite.visit_ImportFrom(import_from_stmt)  # type: ignore
    assert astor.to_source(import_from_stmt) == astor.to_source(import_from_stmt_visited)


# Generated at 2022-06-14 01:49:40.888144
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from astunparse import unparse

    class Test(BaseImportRewrite):
        rewrites = [('old', 'new')]

    class Test2(BaseImportRewrite):
        rewrites = [('old.submodule', 'new2.submodule2')]

    class Test3(BaseImportRewrite):
        rewrites = [('old.submodule', 'new2.submodule2')]

    # rewrite module
    node = ast.parse('import old')
    res = unparse(Test.transform(node).tree).strip()
    assert res == (
        'try:\n'
        '    import old\n'
        'except ImportError:\n'
        '    import new')

    # rewrite module import
    node = ast.parse('import old.module')

# Generated at 2022-06-14 01:49:52.286416
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    
    # Case 1: module name without dots
    transformer = BaseImportRewrite()
    transformer.rewrites = [('django', 'mydjango')]
    
    assert {'module': 'mydjango'} == transformer.visit_Import(ast.parse('import django')).body[1].body[0].value.keywords[0].value.__dict__
    assert {'names': [{'name': 'django', 'asname': None}]} == transformer.visit_Import(ast.parse('import django')).body[1].body[1].value.__dict__
    
    # Case 2: module name with dots

# Generated at 2022-06-14 01:50:04.127106
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..transforms.compat import transforms
    module1 = 'module1'
    module2 = 'module2'
    ast_module = ast.parse('import module1')
    BaseImportRewrite.rewrites = [(module1, module2)]
    BaseImportRewrite._tree_changed = False
    node = BaseImportRewrite._replace_import(ast_module.body[0], module1, module2)
    base_import_rewrite_module2 = ast.parse('''
try:
    __import__('module1')
except ImportError:
    __import__('module2')''').body[0]
    assert astor.to_source(node) == astor.to_source(base_import_rewrite_module2)



# Generated at 2022-06-14 01:50:08.051516
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("from os.path import join")
    import_rewriter = BaseImportRewrite(tree)
    node = tree.body[0]
    import_rewriter.visit_ImportFrom(node)
    assert tree == ast.parse("from os.path import join")



# Generated at 2022-06-14 01:50:18.777297
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    import typing
    module = ast.Module([ast.Import(names=[ast.alias(name='typing',
                                                    asname=None)])])
    transformer = BaseImportRewrite(module)
    transformer.rewrites = [('typing', 'typing_extensions')]
    transformer.visit(module)

# Generated at 2022-06-14 01:50:27.652560
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # given
    from ..utils.testutils import get_node
    import_from = get_node('''
    from old_module import old_name
    ''')

    class MyTransformer(BaseImportRewrite):
        rewrites = [('old_module', 'new_module')]

    # when
    result = MyTransformer.transform(import_from)
    # then
    assert result.changed
    assert result.result.body[0].body[0].body[0].value.args[0].body[0].body[0].value.module == 'old_module'
    assert result.result.body[0].body[0].body[0].value.args[0].body[0].body[0].value.names[0].name == 'old_name'

# Generated at 2022-06-14 01:50:47.506817
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet, extend
    import_rewrite = extend(import_rewrite)

    class Transformer(BaseImportRewrite):
        rewrites = [('time', 'datetime')]

    node = ast.ImportFrom(module='time', names=[ast.alias(name='time')], level=0)
    expected = import_rewrite.get_body(previous=node,  # type: ignore
                                       current=ast.ImportFrom(module='datetime',
                                                              names=[ast.alias(name='time')],
                                                              level=0))[0]
    result = Transformer.transform(node)[0]
    assert isinstance(result, ast.Try)
    assert result._fields == expected._fields


# Generated at 2022-06-14 01:50:54.481603
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    node = ast.parse("import mock\n")
    tree = node.body[0]

    class TestTransformer(BaseImportRewrite):
        rewrites = [('mock', 'unittest.mock')]

    r = TestTransformer.transform(tree)
    assert r.tree == ast.parse("try:\n    import mock\nexcept ImportError:\n    import unittest.mock")
    assert r.tree_changed
    assert r.dependencies == ['unittest.mock']



# Generated at 2022-06-14 01:51:05.775688
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    mod = ast.parse('''
import os
import re
import collections
import collections.abc
import test_import
''')
    mod = BaseImportRewrite(mod).visit(mod)
    mod = ast.fix_missing_locations(mod)

# Generated at 2022-06-14 01:51:15.231394
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest

    from typed_ast import ast3 as ast

    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ('hello', 'goodbye'),
            ('world', 'planet')]

    class TestCase(unittest.TestCase):

        def test_single(self):
            tree = ast.parse('import hello')
            result = ImportRewrite.transform(tree)

# Generated at 2022-06-14 01:51:25.104379
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils import get_code

    tree = ast.parse(get_code('''
        from unittest import TestCase
        from unittest import *

        from unittest import *
        import unittest.TestCase as TestCaseAlias

        from unittest.mock import Mock
        from unittest.mock import MagicMock as MagicMockAlias

        from unittest.mock import *
        from unittest.mock import *
    '''))

    class ImportRewrite(BaseImportRewrite):
        rewrites = [
            ('unittest', 'unittest2')
        ]

    ImportRewrite.transform(tree)


# Generated at 2022-06-14 01:51:37.003610
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import astunparse

    class Rewrite1(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    class Rewrite2(BaseImportRewrite):
        rewrites = [('foo.a', 'bar.b')]

    class Rewrite3(BaseImportRewrite):
        rewrites = [('foo', 'bar'), ('foo.a', 'bar.b')]

    class Rewrite4(BaseImportRewrite):
        rewrites = [('foo.x.y', 'bar.z')]


# Generated at 2022-06-14 01:51:46.390063
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    tree = ast.parse("from mysql.connector import connect")

    class Rewriter(BaseImportRewrite):
        rewrites = [('mysql.connector', 'mysql.connector.django')]

    new_tree = Rewriter.transform(tree).tree
    assert isinstance(new_tree.body[0], ast.Try)
    assert isinstance(new_tree.body[0].body[0].value, ast.ImportFrom)
    assert new_tree.body[0].body[0].value.module == 'mysql.connector.django'


# Generated at 2022-06-14 01:51:51.530437
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.ImportFrom(
        module='aiohttp', 
        names=[ast.alias(name='ClientSession', 
                         asname='session')],
        level=0)

    class Test(BaseImportRewrite):
        rewrites = [('aiohttp', 'aiohttp.client')]

    tree = Test.transform(import_from).tree
    assert isinstance(tree, ast.Try)
    stmt = tree.body[0]
    assert isinstance(stmt, ast.ImportFrom)
    assert stmt.names[0].name == 'ClientSession'

# Generated at 2022-06-14 01:52:01.939585
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet, extend
    import_rewrite = snippet(
    """
    try:
        extend(previous)
    except ImportError:
        extend(current)
    """
    )

    class BaseImportRewrite(ast.NodeTransformer):
        rewrites = [('a', 'b')]
        _tree_changed = False

        def _get_matched_rewrite(self, name: Optional[str]) -> Optional[Tuple[str, str]]:
            """Returns rewrite for module name."""
            if name is None:
                return None

            for from_, to in self.rewrites:
                if name == from_ or name.startswith(from_ + '.'):
                    return from_, to

            return None


# Generated at 2022-06-14 01:52:12.549812
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from = ast.parse(
        """from collections import OrderedDict""").body[0]

    res1 = BaseImportRewrite(import_from)
    assert isinstance(res1.visit(import_from), ast.ImportFrom)

    res2 = BaseImportRewrite(import_from)
    res2.rewrites = [('collections.OrderedDict', 'db.models.OrderedDict')]
    assert isinstance(res2.visit(import_from), ast.Try)
    
    import_from2 = ast.parse(
        """from collections import OrderedDict, defaultdict""").body[0]

    res3 = BaseImportRewrite(import_from)
    res3.rewrites = [('collections.OrderedDict', 'db.models.OrderedDict')]


# Generated at 2022-06-14 01:52:29.998235
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestBaseImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    with open('../tests/fixtures/import_rewrite_test.py') as f:
        tree = ast.parse(f.read())

    result = TestBaseImportRewrite.transform(tree)

    import_rewrite_test_transformed = """import bar
try:
    import foo
except ImportError:
    import bar
import bar
"""
    code_transformed = compile(ast.fix_missing_locations(result.tree), '<string>', 'exec')

    import import_rewrite_test
    code = compile(compile(import_rewrite_test.__code__, '<string>', 'exec'), '<string>', 'exec')

    assert code == code_transformed


#

# Generated at 2022-06-14 01:52:41.809163
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
    from ..utils.snippet import snippet
    from ..utils.snippet import extend
    try:
        extend(snippet)
    except ImportError:
        extend(snippet)
    from ..utils import build_ast as b
    import_ = b.import_from('somedummy.module', [b.alias('SomeClass', None)])
    trans = BaseImportRewrite(import_)
    trans._get_matched_rewrite = lambda x: ('somedummy.module', 'somemodule')
    tr = trans.visit_ImportFrom(import_)
    assert tr.body[0].value.value.names[0].name

# Generated at 2022-06-14 01:52:55.328764
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('from collections import OrderedDict')
    cls = BaseImportRewrite.__new__(BaseImportRewrite)
    cls.rewrites = [('collections', 'modcollections')]
    cls.visit_ImportFrom(tree)

# Generated at 2022-06-14 01:52:57.007391
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    assert BaseImportRewrite.visit_ImportFrom(None, None) is None



# Generated at 2022-06-14 01:53:08.333880
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.testing import make_imports_from_tuples, write_python_version, assert_python_version, assert_import_from_visit, make_import_from_from_tuples, assert_import_visit
    tree = make_imports_from_tuples([('urllib', 'urllib.request')])
    write_python_version('2', tree)
    tree = BaseImportRewrite(tree).visit(tree)
    assert_python_version('3', tree)
    assert_import_visit('urllib.request', 'urllib', tree)
    assert_import_from_visit('urllib.parse', 'urllib', tree)
    

# Unit tests for method visit_ImportFrom of class BaseImportRewrite

# Generated at 2022-06-14 01:53:19.327560
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .. import Transformer
    from ..snippets import snippets

    class _TestClass(BaseImportRewrite):
        rewrites = [('flask', 'flask_test')]

    snippets.import_rewrite = import_rewrite

    additional_transforms = {
        ast.ImportFrom: _TestClass,
        ast.Import: _TestClass}

    simple_code = 'import flask'
    test_code = 'from flask import Blueprint'

    class Test(Transformer):
        @classmethod
        def transform(cls, tree: ast.AST) -> TransformationResult:
            tree = super().transform(tree)
            return cls.transform_with(tree, additional_transforms)

    with pytest.raises(ImportError):
        Test.run(simple_code)


# Generated at 2022-06-14 01:53:26.481973
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor

    code = '''
try:
    import module_previous
except ImportError:
    import module_current
'''

    tree = ast.parse(code)
    node = tree.body[0]
    rewrites = [('module_previous', 'module_current')]

    class Transformer(BaseImportRewrite):
        rewrites = rewrites

    generated = Transformer.transform(tree).tree

    assert astor.to_source(node) == astor.to_source(generated)


# Generated at 2022-06-14 01:53:38.761708
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [
            ('six', 'six2'),
            ('pywinauto', 'pywinauto2')
        ]

    import_stmt = ast.Import(names=[
        ast.alias(name='six',
                  asname='six')])

    try_stmt = TestImportRewrite.transform(import_stmt)
    assert try_stmt._tree_changed is True
    assert try_stmt.tree.body[0] == import_rewrite.get_body(previous=import_stmt,
                                                            current=
                                                                ast.Import(names=[
                                                                    ast.alias(name='six2',
                                                                              asname='six')]))[0]

    import_stmt = ast.Import

# Generated at 2022-06-14 01:53:49.072713
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..utils.ast_helpers import node_to_str

    class MockTransform(BaseImportRewrite):
        rewrites = [('mock1', 'mock2'), ('mock3', 'mock4')]

    tree = ast.parse('from mock1.mock1 import Test\n'
                     'from mock1 import Test2')
    MockTransform.transform(tree)

# Generated at 2022-06-14 01:53:58.071987
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse
    from ..utils.snippet import get_snippet_ast
    
    result = BaseImportRewrite.transform(parse(u"""
        from b.c import d
    """))
    assert not result.changed
    assert result.tree == parse(u"""
        from b.c import d
    """)

    result = BaseImportRewrite.transform(parse(u"""
        from d.e import f
    """))
    assert result.changed
    assert result.tree == get_snippet_ast(u"""
        try:
            from d.e import f
        except ImportError:
            from f import g
    """)
