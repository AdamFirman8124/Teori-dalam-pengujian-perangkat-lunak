

# Generated at 2022-06-14 01:44:10.223129
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast
    import asct
    import astor

    class ImportRewriteTest(BaseImportRewrite):
        rewrites = [('asct', 'asct')]

    class Import(ast.NodeTransformer):
        def visit_Import(self, node):
            return node

    node = ast.parse('import asct')
    result = ImportRewriteTest.transform(node).tree
    assert result == Import().visit(node)



# Generated at 2022-06-14 01:44:17.831598
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert ast.parse('from . import module').body[0] == ast.Import(names=[ast.alias(name='.',
                                                                                   asname=None,
                                                                                   ctx=ast.Store())])
    assert ast.parse('import module').body[0] == ast.Import(names=[ast.alias(name='module',
                                                                             asname=None,
                                                                             ctx=ast.Store())])


# Generated at 2022-06-14 01:44:24.627526
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class RewriteTransformer(BaseImportRewrite):
        rewrites = [('mock', 'unittest.mock')]

    tree = ast.parse('''
    import mock
    ''')

    expected = '''
    try:
        import mock
    except ImportError:
        import unittest.mock as mock
    '''

    rewriter = RewriteTransformer(tree)
    rewriter.visit(tree)

    assert ast.dump(tree) == expected


# Generated at 2022-06-14 01:44:33.328955
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..tests.test_transpilers import get_tree
    import astor

    rewrites = [('somemodule.module1', 'module1_rewrite')]
    class CustomTransformer(BaseImportRewrite):
        rewrites = rewrites

    tree = get_tree('import somemodule.module1')
    transformed_tree = CustomTransformer.transform(tree).tree
    assert astor.to_source(transformed_tree) == \
        'try:\n    import somemodule.module1\n    somemodule.module1 = somemodule.module1\n' \
        'except ImportError:\n    import module1_rewrite\n    somemodule.module1 = module1_rewrite\n'


# Generated at 2022-06-14 01:44:36.746652
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    transformer = BaseImportRewrite()
    node = ast.Import(names=[ast.alias(name='name', asname=None)])
    assert transformer.visit_Import(node) == node


# Generated at 2022-06-14 01:44:47.424699
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils import get_test_target, parse

    tree = parse('import foo')
    original = astor.to_source(tree)

    class Test(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = Test.transform(tree).tree
    assert astor.to_source(tree).strip() == "try:\n    import foo\nexcept ImportError:\n    import bar"

    tree = parse('import foo.bar')
    tree = Test.transform(tree).tree
    assert astor.to_source(tree).strip() == "try:\n    import foo.bar\nexcept ImportError:\n    import bar.bar"

    tree = parse('import foo.bar as foo')
    tree = Test.transform(tree).tree
    assert astor.to_source

# Generated at 2022-06-14 01:44:58.248082
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # Setup
    rewrites = [('six', 'typed_astunparse')]

    # Exercise
    tree = ast.parse("import six")
    transformer = BaseImportRewrite(tree)
    transformer.rewrites = rewrites
    result = transformer.visit(tree)

    # Verify
    expected = ast.parse("""\
import typed_astunparse as six
try:
    import six
except ImportError:
    pass
""")
    assert ast.dump(result) == ast.dump(expected)

    # Cleanup - none necessary



# Generated at 2022-06-14 01:45:08.018403
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class ImportRewriter(BaseImportRewrite):
        rewrites = [
            ('a', 'b'),
        ]

    tree = ast.parse('import a')

    result = ImportRewriter.transform(tree)

    assert result.tree == ast.parse('try:\n    import a\nexcept ImportError:\n    import b')

    tree = ast.parse('import a.b')

    result = ImportRewriter.transform(tree)

    assert result.tree == ast.parse('try:\n    import a.b\nexcept ImportError:\n    import b.b')

    tree = ast.parse('import a as x')

    result = ImportRewriter.transform(tree)

    assert result.tree == ast.parse('try:\n    import a as x\nexcept ImportError:\n    import b')


# Generated at 2022-06-14 01:45:18.084997
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import six
    import_node = ast.parse('import six').body[0]

    class Tested(BaseImportRewrite):
        rewrites = [
            ('six', 'six.moves')
        ]

    assert Tested.transform(import_node).tree == ast.parse('import six.moves').body[0]

    class Tested(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]

    assert Tested.transform(import_node).tree == ast.parse('import six').body[0]

    class Tested(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six')
        ]

    assert Tested.transform(import_node).tree == ast.parse('import six').body[0]


# Unit test

# Generated at 2022-06-14 01:45:27.901162
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    pre_import_from = ast.ImportFrom(
        module="a.b",
        names=[
            ast.alias(
                name="c",
                asname="c"
            ),
            ast.alias(
                name="d",
                asname="d"
            )
        ],
        level=0
    )
    pre_import_from_node = ast.parse(ast.dump(pre_import_from))
    new_import_from = ast.ImportFrom(
        module="a.c",
        names=[
            ast.alias(
                name="d",
                asname="d"
            )
        ],
        level=0
    )
    new_import_from_node = ast.parse(ast.dump(new_import_from))

# Generated at 2022-06-14 01:45:42.320505
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Rewriter(BaseImportRewrite):
        rewrites = [('six.moves', 'moves')]

    tree = ast.parse('from six.moves import reload_module as six_reload')

    expected = ast.parse('''
    try:
        from six.moves import reload_module as six_reload
    except ImportError:
        from moves import reload_module as six_reload
    ''')

    result = Rewriter.transform(tree)

    assert result.tree == expected

# Generated at 2022-06-14 01:45:47.698963
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    target = 'import a.b as c, d.e as f'
    rewrites = [('a.b', 'a.b_new'), ('d.e', 'd.e_new')]

    assert BaseImportRewrite._visit_ImportFrom(target, rewrites) == \
           ('try:\n    import a.b_new as c, d.e as f\n'
            'except ImportError:\n    import a.b as c, d.e_new as f')



# Generated at 2022-06-14 01:46:00.470445
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class Transformer(BaseImportRewrite):
        rewrites = [
            ('Class1', 'Class1_rewrote'),
        ]

    tree = ast.parse('''\
from Class1 import *
from Class1 import A, B

from Class1_rewrote import A
''')

    Transformer.transform(tree)

    assert tree == ast.parse('''\
try:
    from Class1 import *
except ImportError:
    from Class1_rewrote import *
try:
    from Class1 import A, B
except ImportError:
    from Class1_rewrote import A, B

from Class1_rewrote import A
''')



# Generated at 2022-06-14 01:46:12.467452
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_rewrite_transformer = BaseImportRewrite()
    import_rewrite_transformer.rewrites = [('foo', 'bar')]

    import_ast = ast.Import(
        names=[ast.alias(name='foo',
                         asname=None)]
    )
    actual = import_rewrite_transformer.visit(import_ast)
    expected = ast.Import(
        names=[ast.alias(name='bar',
                         asname='foo')]
    )
    assert actual == expected

    import_ast = ast.Import(
        names=[ast.alias(name='foo.a',
                         asname='a')]
    )
    actual = import_rewrite_transformer.visit(import_ast)

# Generated at 2022-06-14 01:46:21.736764
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import_from1 = ast.ImportFrom(module='module',
                                  names=[ast.alias(name='name', asname='asname')],
                                  level=0)
    import_from2 = ast.ImportFrom(module='test.module',
                                  names=[ast.alias(name='name', asname='asname')],
                                  level=0)
    import_from3 = ast.ImportFrom(module='test.module.test',
                                  names=[ast.alias(name='name', asname='asname')],
                                  level=0)
    import_from4 = ast.ImportFrom(module='test.module',
                                  names=[ast.alias(name='test.name', asname='asname')],
                                  level=0)

# Generated at 2022-06-14 01:46:31.812553
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor

    node = ast.parse('from module_a import a, b, c')
    rewritten = astor.to_source(BaseImportRewrite._replace_import_from_names(
        node, {'module_a.a': ('module_a', 'module_b'), 'module_a.c': ('module_a', 'module_b')}))
    assert rewritten == 'try:\n    from module_b import a, b, c\nexcept (ImportError, ):\n    from module_a import a, b, c\n'

    node = ast.parse('from module_a import a, b, c')
    rewritten = astor.to_source(BaseImportRewrite._replace_import_from_module(
        node, 'module_a', 'module_b'))

# Generated at 2022-06-14 01:46:46.560912
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import unittest
    import astor
    from ..utils.source import Source

    class TestClass(unittest.TestCase):
        def test(self):
            cls = BaseImportRewrite
            source = Source("""
            from a import b as c, d
            from a import x
            import a as b
            from .b import y
            from . import z
            from . import y as z
            """)
            tree = ast.parse(source.content)
            cls.rewrites = [('a', 'test.a')]
            result = cls.transform(tree)
            #print(astor.to_source(result.tree))

# Generated at 2022-06-14 01:46:55.877589
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('abc', 'abc1')]

    tree = ast.parse(dedent('''\
        from abc import abc1, abc2
        from abc import *
        from abc.abc1 import abc3
        from abc.abc2.abc1 import abc4, abc5
        from abc.abc2.abc2.abc3 import abc6 as abc6_
        '''))


# Generated at 2022-06-14 01:46:58.379515
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():

    import astor

    rewrites = [('test_import', 'test_import1')]

    class TestNodeTransformer(BaseImportRewrite):
        rewrites = rewrites


# Generated at 2022-06-14 01:47:09.689568
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import sys
    from io import StringIO
    from ..libs.six import StringIO as StringIO2
    from ..utils.faketree import get_tree
    from ..utils.compile import compile_ast
    code = "import datetime as dt"
    tree = get_tree(code, __name__, __file__)
    module = compile_ast(tree, __file__)
    old_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        module.dt
    except ImportError:
        result = out.getvalue().strip()
    finally:
        sys.stdout = old_stdout
    assert result == ''

    class SimpleRewrite(BaseImportRewrite):
        rewrites = [('datetime', 'io')]


# Generated at 2022-06-14 01:47:28.762797
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from typed_ast.ast3 import parse
    class Dummy(BaseImportRewrite):
        rewrites = [('old', 'new')]
    tree = parse('import old')
    Dummy.transform(tree) == TransformationResult(
        tree=parse('try:\n  import old\nexcept ImportError:\n  import new'),
        changed=True,
        dependencies=[])
    tree = parse('import old.mod')
    Dummy.transform(tree) == TransformationResult(
        tree=parse('try:\n  import old.mod\nexcept ImportError:\n  import new.mod'),
        changed=True,
        dependencies=[])
    tree = parse('import not_matched')
    Dummy.transform(tree) == TransformationResult(
        tree=parse('import not_matched'),
        changed=False,
        dependencies=[])

# Generated at 2022-06-14 01:47:38.576497
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from typed_ast.ast3 import PyCF_ONLY_AST
    tree = ast.parse('import six')
    result = BaseImportRewrite.transform(tree)
    assert result.tree_changed
    assert 'try:' in astor.to_source(result.tree)
    assert 'except ImportError' in astor.to_source(result.tree)
    assert 'import six' in astor.to_source(result.tree)
    assert result.dependencies == ['six']
    assert not ast.dump(tree, include_attributes=False) == ast.dump(result.tree, include_attributes=False)
    tree = ast.parse('import six', mode='exec')
    result = BaseImportRewrite.transform(tree)
    assert not result.tree_changed
    assert astor.to_

# Generated at 2022-06-14 01:47:48.368078
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from ..types import CompilationTarget
    import astor
    import importlib
    import sys

    # Set of compilation targets used in our unit test
    # These targets will be transformed
    targets = [
        CompilationTarget(module='types', module_name='types',
                          source_file='/root/test/types.py', mtime=0),
        CompilationTarget(module='utils', module_name='utils',
                          source_file='/root/test/utils.py', mtime=0)]

    # Create ASTs for target modules
    trees = []
    for target in targets:
        # Save original target module to be able to reload it
        original_module = importlib.import_module(target.module_name)
        # Add target module to sys.modules to be able to import it

# Generated at 2022-06-14 01:47:56.758385
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    from .test_utils import compare_ast

    code = """
from module import *
from module import name
from module import name as new_name
from module import name as name2
from module import name as name2, name3
    """

    for import_rewrites in [
        [('module', 'renamed_module')],
        [('module', 'renamed_module')],
        [('module', 'renamed_module'), ('module.name', 'submodule.subname')],
    ]:
        class Rewriter(BaseImportRewrite):
            rewrites = import_rewrites

        compare_ast(Rewriter, code, rewrite_imports=True)

# Generated at 2022-06-14 01:48:01.688317
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    node_kwargs = {
        'module': 'base',
        'names': [ast.alias(name='name', asname=None)],
        'level': None
    }
    node = ast.ImportFrom(**node_kwargs)
    assert BaseImportRewrite(None).visit_ImportFrom(node) == node

# Generated at 2022-06-14 01:48:12.000250
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.visitor import ASTVisitorForTesting
    from .test_transformer_classes import MoveImportNode, rewrite_registry

    tree = ast.parse(
        "import argparse\n"
        "import pdb\n"
        "import numpy as np\n")

    # No value for `rewrites` shall lead to no changes in tree.
    class TransformerNoValueRewrites(BaseImportRewrite):
        rewrites = []

    visitor = ASTVisitorForTesting(tree,
                                   transformations={MoveImportNode: TransformerNoValueRewrites})
    visitor.transform()
    assert tree == ast.parse(
        "import argparse\n"
        "import pdb\n"
        "import numpy as np\n")

    # No matching imports shall lead to no changes in tree.
    # `

# Generated at 2022-06-14 01:48:17.829962
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..utils.tree import parse

    class ReplaceModuleTransformer(BaseImportRewrite):
        rewrites = [('unittest', 'test_module')]

    tree = parse("""
    import unittest

    class Test():
        pass
    """)

    result = ReplaceModuleTransformer.transform(tree)
    assert result.tree.body[1].decorator_list[0].value.func.value.id == 'TestModule'



# Generated at 2022-06-14 01:48:28.802513
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import ast
    from typed_ast import ast3 as typed_ast
    from typed_ast.transforms.compat import BaseImportRewrite

    class NewImportRewrite(BaseImportRewrite):
        rewrites = [
            ('compat', 'typed_ast.transforms.compat'),
            ('typed_ast', 'typed_ast.ast3'),
            ('exceptions', 'typed_ast.transforms.compat.exceptions'),
            ]

    tree = ast.parse("""
    from compat import PY2
    from compat.exceptions import ParentChildIssueError
    """)

# Generated at 2022-06-14 01:48:35.979704
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    # GIVEN
    class ImportTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

        def __init__(self, tree: ast.AST) -> None:
            super().__init__(tree)
            self.visit(tree)

    class Tree(ast.AST):
        _fields = ['body']

        def __init__(self, body: ast.AST) -> None:
            self.body = body

    # WHEN
    tree = Tree(body=[ast.Import(names=[ast.alias(name='foo.foo', asname='foo')]),
            ast.Import(names=[ast.alias(name='bar.bar', asname='bar')])])
    transformer = ImportTransformer(tree)

    # THEN
    assert transformer._tree_changed is True

# Generated at 2022-06-14 01:48:46.421981
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import ast as std_ast
    import astunparse as std_astunparse

    class RewriteImportTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    std_tree = std_ast.parse(std_astunparse.unparse(std_ast.parse('''
        from foo import bar
        from foo import bar as baz
        from foo.boo import boo

        from notfoo import bar
        
        from foo import bar as foo_bar, boo
        from foo import bar as foo_bar, boo as foo_boo
    ''')))


# Generated at 2022-06-14 01:49:05.506896
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_from1 = ast.ImportFrom(
    module='future', 
    names=[
        ast.alias(name='division', asname='division')], 
    level=0)

    import_from2 = ast.ImportFrom(
    module='future.utils', 
    names=[
        ast.alias(name='division', asname='division'),
        ast.alias(name='integer_types', asname='integer_types')], 
    level=0)

    import_from3 = ast.ImportFrom(
    module='future.builtins', 
    names=[
        ast.alias(name='base_integer', asname='base_integer')], 
    level=0)


# Generated at 2022-06-14 01:49:17.058588
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class Rewrite(BaseImportRewrite):
        target = CompilationTarget.PYTHON_LEGACY
        rewrites = [('to_replace', 'replacement'), ('noreplace', 'no')]

    replacement = ast.parse('import replacement')
    import_ = ast.Import(names=[ast.alias(name='to_replace', asname=None)])


# Generated at 2022-06-14 01:49:25.830027
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from_, to = 'old_mod', 'new_mod'
    source = """
    from old_mod import a, b, c as d
    """
    expected = """
    try:
        from old_mod import a, b, c as d
    except ImportError:
        from new_mod import a, b, c as d
    """

    class TestRewrite(BaseImportRewrite):
        rewrites = [(from_, to)]

    tree = ast.parse(source)
    TestRewrite.transform(tree)

    code = ast.unparse(tree)
    assert code.strip() == expected.strip()



# Generated at 2022-06-14 01:49:32.750249
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class RewriteImport(BaseImportRewrite):
        rewrites = [('from', 'to')]

    tree = ast.parse('import from')
    rewrote_tree = RewriteImport.transform(tree)[0]

    expected = '''\
try:
    import from
except ImportError:
    import to'''
    assert ast.unparse(rewrote_tree) == expected



# Generated at 2022-06-14 01:49:45.074167
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class ConcreteImportRewrite(BaseImportRewrite):
        rewrites = [
          ('foo.foo', 'bar.bar')
        ]
    
    import_foo = ast.ImportFrom(module='foo.foo',names=[ast.alias(name='foo_mod', asname='foo_mod')],level=0)
    import_bar = ast.ImportFrom(module='bar.bar',names=[ast.alias(name='foo_mod', asname='foo_mod')],level=0)
    expected = ast.Try(body = [import_bar], handlers = [ast.ExceptHandler(type=None, name=None, body=[import_foo])], finalbody = [],orelse = [])
    result = ConcreteImportRewrite.visit_ImportFrom(import_foo)
    assert result == expected



# Unit

# Generated at 2022-06-14 01:49:55.827690
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast.ast3 import parse
    import unittest

    class TestRewrite(BaseImportRewrite):
        rewrites = [('numpy', 'pandas')]

    tree = parse('''
from numpy import pi, cos
from numpy.core.defchararray import upper
from networkx import *
from networkx.core.database import Database
from xxx import yyy
''')
    expected = parse('''
from pandas import pi, cos
from pandas.core.defchararray import upper
try:
    from networkx import *
except ImportError:
    from networkx.core.database import Database
from xxx import yyy
''')
    actual = TestRewrite.transform(tree).tree

# Generated at 2022-06-14 01:50:04.623210
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    imports = ast.parse('from a import b\n')
    rewriter = BaseImportRewrite(imports)
    rewriter.rewrites = [('a', 'b')]
    rewriter.visit(imports)
    expected = ast.parse(
        'try:\n    from b import b\n    b = b\n'
        'except ImportError:\n    from a import b\n'
    )
    assert ast.dump(imports) == ast.dump(expected)

    imports = ast.parse('from a import b\n')
    rewriter = BaseImportRewrite(imports)
    rewriter.rewrites = [('a', 'b')]
    rewriter.visit(imports)

# Generated at 2022-06-14 01:50:14.009848
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        target = CompilationTarget.PYTHON
        rewrites = [('foo', 'bar')]

    tree = ast.parse("import foo")
    tr = TestTransformer(tree)

    result = tr.visit_Import(tree.body[0])

    assert isinstance(result, ast.Try)
    assert len(result.handlers) == 1
    assert result.handlers[0].type.id == 'ImportError'
    assert isinstance(result.handlers[0].body[0], ast.Import)
    assert result.handlers[0].body[0].names[0].name == 'bar'
    assert result.handlers[0].body[0].names[0].asname == 'foo'



# Generated at 2022-06-14 01:50:18.683090
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from .test_rewrites import ImportFromTransformer
    import astor

    snippet = 'from re import (compile, escape, group)'
    tree = ast.parse(snippet)
    transformer = ImportFromTransformer(tree)
    transformer.visit(tree)

    print(astor.to_source(tree))

# Generated at 2022-06-14 01:50:28.725033
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():

    import unittest  # This is used to test the function
    # Unit test for method visit_ImportFrom of class BaseImportRewrite
    class Test(unittest.TestCase):

        def test_visit_ImportFrom(self):

            class testBaseImportRewrite(BaseImportRewrite):
                rewrites = [('old', 'new')]

            # Condition 1: when the import doesn't need to be replaced
            # expr_29 is the input, expr_27 is the actual output,
            # expr_28 is the expected output
            expr_29 = ast.ImportFrom(
                level=0,
                module='dummy',
                names=[
                    ast.alias(
                        name='foo',
                        asname=None),
                    ast.alias(
                        name='bar',
                        asname=None)
                ])
            expr

# Generated at 2022-06-14 01:50:48.906440
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import unittest
    import astor
    from ..transformer import BaseImportRewrite

    class Foo(BaseImportRewrite):
        rewrites = [('app', 'app2')]

    class Test(unittest.TestCase):
        def test_rewrite_import(self):
            tree = ast.parse('import app.foo')
            Foo.transform(tree)

            result = astor.to_source(tree).strip()
            self.assertEqual(result, 'try:\n    import app.foo\nexcept ImportError:\n    import app2.foo')

        def test_rewrite_import_as(self):
            tree = ast.parse('import app.foo as bar')
            Foo.transform(tree)

            result = astor.to_source(tree).strip()

# Generated at 2022-06-14 01:50:57.967757
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    class TestTransformer(BaseImportRewrite):
        rewrites = [
            ('module1', 'module2')]

    test_module = ast.parse('from module1 import x, y')
    transformer = TestTransformer(test_module)
    actual = transformer.visit(test_module)
    try_node = ast.parse('try:\n    from module2 import x\n    from module2 import y\nexcept ImportError:\n    from module1 import x\n    from module1 import y')
    # ast.dump(actual) == ast.dump(try_node)
    assert ast.dump(actual) == ast.dump(try_node)

    test_module = ast.parse('from module1.submodule import x, y')
    transformer = TestTransformer(test_module)

# Generated at 2022-06-14 01:51:08.561977
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typed_ast.ast3 as ast
    from typed_ast.ast3 import Module, ImportFrom, alias, Str, Try, Name, Load, ExceptHandler, Expr, Call
    from unittest import TestCase

    class BaseImportRewrite(BaseNodeTransformer):
        """Examples of import rewrite."""
        rewrites = [
            ('six', 'six.moves')
        ]


# Generated at 2022-06-14 01:51:21.014610
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestTransformer(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse('''
    import foo
    import foo.baz
    import foo as bar
    import foo.baz as fizbuz
    import foo_bar.baz
    ''')
    expected = '''
    try:
        import foo
    except ImportError:
        import bar
    try:
        import foo.baz
    except ImportError:
        import bar.baz
    try:
        import foo as bar
    except ImportError:
        import bar as bar
    try:
        import foo.baz as fizbuz
    except ImportError:
        import bar.baz as fizbuz
    import foo_bar.baz
    '''
    TestTrans

# Generated at 2022-06-14 01:51:25.845783
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree = ast.parse('import foo')
    transformer = BaseImportRewrite([('foo', 'bar')])
    transformer.visit(tree)
    assert transformer._tree_changed
    print(ast.dump(tree))

    tree = ast.parse('import foo')
    transformer = BaseImportRewrite([('foo', 'bar')])
    transformer.visit(tree)
    assert transformer._tree_changed
    print(ast.dump(tree))



# Generated at 2022-06-14 01:51:37.483791
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import_stmt = ast.parse('import foo')
    tree = ast.Module(body=[
        import_stmt,
        ast.Import(names=[ast.alias(name='foo', asname="bar")]),
        ast.Import(names=[ast.alias(name='foo.bar')]),
    ])

    class RewriteTransformer(BaseImportRewrite):
        rewrites = [('foo', 'shoobop')]

    result = RewriteTransformer.transform(tree)


# Generated at 2022-06-14 01:51:49.484017
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import typed_ast.ast3 as ast
    class CustomImportRewrite(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    tree = ast.parse("from foo import bar")
    visitor = CustomImportRewrite(tree)
    visitor.visit(tree)

    assert "from bar import bar" in astunparse.unparse(tree).strip()

    tree = ast.parse("from foo.bar import baz")
    visitor = CustomImportRewrite(tree)
    visitor.visit(tree)

    assert "from bar.bar import baz" in astunparse.unparse(tree).strip()

    tree = ast.parse("from foo.bar import *")
    visitor = CustomImportRewrite(tree)
    visitor.visit(tree)

    assert "from bar.bar import *" in ast

# Generated at 2022-06-14 01:51:59.500448
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Test for import from for module
    import_from_node = ast.parse("""from datetime import timezone""").body[0]
    import_from_result = ast.parse("""from typing import timezone\ntry:
    from datetime import timezone
except ImportError:
    from typing import timezone
""").body[0]
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [("datetime", "typing")]
        
    result = TestImportRewrite.transform(import_from_node)
    assert result.tree == import_from_result
    assert result.changed

    # Test for import from for name
    import_from_node = ast.parse("""from datetime import timezone""").body[0]

# Generated at 2022-06-14 01:52:11.403022
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    # Assert 
    # from six.moves import html_parser
    tree = ast.parse('from six.moves import html_parser')
    tree_changed = False
    result = ast.parse('from html import parser')
    # Act
    class TestImportRewrite(BaseImportRewrite):
        rewrites = [('six.moves.html_parser', 'html.parser')]
    transformer = TestImportRewrite(tree)
    transformer.visit(tree)
    tree_changed = transformer._tree_changed
    assert tree.body[0] == result.body[0]
    assert tree_changed is True
    # Assert 
    # from six.moves.html_parser import HTMLParser
    tree = ast.parse('from six.moves.html_parser import HTMLParser')
    tree_changed = False

# Generated at 2022-06-14 01:52:21.657736
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import ast as pt

    tree = pt.parse('''import foo''')
    BaseImportRewrite(tree).visit(tree.body[0])

    assert pt.dump(tree) == '''try:
    import foo
except ImportError:
    import _foo'''

    tree = pt.parse('''import foo.zoo''')
    BaseImportRewrite(tree).visit(tree.body[0])

    assert pt.dump(tree) == '''try:
    import foo.zoo
except ImportError:
    import _foo.zoo'''

    tree = pt.parse('''try:
    import foo
except ImportError:
    import _foo''')
    BaseImportRewrite(tree).visit(tree.body[0])


# Generated at 2022-06-14 01:52:41.106296
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    some_class = ast.Name(id='SomeClass', ctx=ast.Load())
    some_other_class = ast.Name(id='SomeOtherClass', ctx=ast.Load())
    some_var = ast.Name(id='some_var', ctx=ast.Load())
    some_const = ast.Name(id='SOME_CONST', ctx=ast.Load())


# Generated at 2022-06-14 01:52:54.991306
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    tree_changed = False
    import_node = ast.Import(names=[
        ast.alias(name='a', asname='b')])

    result_node = ast.Import(names=[
        ast.alias(name='a', asname='b')])

    tree_changed2 = True
    import_node2 = ast.Import(names=[
        ast.alias(name='foo', asname='bar')])

    result_node2 = ast.Import(names=[
        ast.alias(name='foo', asname='bar')])

    simple_rewrite = 'foo', 'bar'
    submodule_rewrite = 'foo.bar', 'foo'

    class TestClass(BaseImportRewrite):
        rewrites = [simple_rewrite]

    inst = TestClass(import_node)

# Generated at 2022-06-14 01:53:03.202622
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import astor
    import_from_node = ast.parse('import json, yaml').body[0]
    class ImportRewrite(BaseImportRewrite):
        rewrites = [('json', 'simplejson'), ('yaml', 'ruamel.yaml')]
        target = 'py2'
    import_rewrite = ImportRewrite(import_from_node)
    import_rewrite.visit_Import(import_from_node)
    result = astor.to_source(import_from_node)
    expected = 'try:\n    import json, yaml\nexcept ImportError:\n    import simplejson, ruamel.yaml'
    assert result == expected




# Generated at 2022-06-14 01:53:17.724965
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    from typed_ast import ast3 as ast
    import textwrap
    from ..utils.ast_helpers import parse_code

    class Test(BaseImportRewrite):
        rewrites = [('foo', 'bar')]

    def test_rewrite_import_from(code: str) -> ast.AST:
        return Test.transform(parse_code(code)).tree

    def check(code: str) -> bool:
        tree = Test.transform(parse_code(code)).tree
        return Test.transform(tree).tree_changed

    # Check that other import types are not changed
    assert not check('from foo import *')
    assert not check('from foo import a')
    assert not check('import foo')

    # Check fully matched import from

# Generated at 2022-06-14 01:53:24.098991
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    from ..compiler import Compiler
    source = """
try:
    import _pyshader_math as _math
except ImportError:
    import _math

print(_math.tanh(0.5))
"""

    tree = Compiler.compile_string(source)
    transformer = BaseImportRewrite(tree)
    transformer.visit(tree)

    assert Compiler.compile_string(source) == tree

# Generated at 2022-06-14 01:53:30.973113
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    assert BaseImportRewrite.transform(ast.parse('import blah')) == TransformationResult(ast.parse('import blah'), False, [])
    assert BaseImportRewrite.transform(ast.parse('import blah as blah2')) == TransformationResult(ast.parse('import blah as blah2'), False, [])
    assert BaseImportRewrite.transform(ast.parse('import blah.blah2')) == TransformationResult(ast.parse('import blah.blah2'), False, [])
    assert BaseImportRewrite.transform(ast.parse('import blah.blah2 as blah')) == TransformationResult(ast.parse('import blah.blah2 as blah'), False, [])


# Generated at 2022-06-14 01:53:40.398765
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    import astor
    from ..utils.testing import assert_transformation

    class Dummy(BaseImportRewrite):
        rewrites = [
            ('six.moves', 'six.moves.http_client'),
            ('cliff', 'sdk.utils.cliff')]

    final = '''
try:
    import six.moves.http_client as urllib
except ImportError:
    import six.moves as urllib
'''

    assert_transformation(Dummy,
                          'import six.moves.urllib as urllib',
                          final,
                          ast_kwargs={'mode': 'exec'})



# Generated at 2022-06-14 01:53:50.771418
# Unit test for method visit_ImportFrom of class BaseImportRewrite
def test_BaseImportRewrite_visit_ImportFrom():
    import_stmt = ast.ImportFrom(module='django.conf.settings',
                                 names=[ast.alias(name='CELERY_MONGODB_BACKEND_SETTINGS',
                                                  asname=None)],
                                 level=0)
    import_stmt_with_alias = ast.ImportFrom(module='django.conf.settings',
                                            names=[ast.alias(name='CELERY_MONGODB_BACKEND_SETTINGS',
                                                             asname='settings')],
                                            level=0)

    class ImportRewrite(BaseImportRewrite):
        rewrites = [('django.conf.settings', 'django.conf')]
        target = 'south==0.8.4'


# Generated at 2022-06-14 01:53:57.239970
# Unit test for method visit_Import of class BaseImportRewrite
def test_BaseImportRewrite_visit_Import():
    class TestClass(BaseImportRewrite):
        rewrites = [('__future__', 'future')]

    tree = ast.parse('import __future__')
    node = tree.body[0]
    assert isinstance(node, ast.Import)
    assert node.names[0].name == '__future__'

    new_tree = TestClass().visit(tree)
    assert isinstance(new_tree, ast.Try)
    assert isinstance(new_tree.body[0], ast.Import)
    assert new_tree.body[0].names[0].name == 'future'
    assert isinstance(new_tree.handlers[0], ast.ExceptHandler)
    assert isinstance(new_tree.handlers[0].body[0], ast.Import)
    assert new_tree.handlers[0].body