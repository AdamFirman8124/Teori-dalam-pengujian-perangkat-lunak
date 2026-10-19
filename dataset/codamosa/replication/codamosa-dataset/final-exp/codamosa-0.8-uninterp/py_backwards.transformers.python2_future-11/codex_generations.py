

# Generated at 2022-06-14 01:55:01.163388
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()



# Generated at 2022-06-14 01:55:10.220785
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.Module([], lineno=1, col_offset=0)


# Generated at 2022-06-14 01:55:18.553305
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    source = '''print("Hello World!")'''
    tree = astor.parse_file(source)
    node_transformer = Python2FutureTransformer()
    final = node_transformer.visit(tree)

    expected = '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
print("Hello World!")'''

    assert astor.to_source(final) == expected

# Generated at 2022-06-14 01:55:28.496789
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_node = ast.parse("print(1)")
    Python2FutureTransformer().visit(module_node)
    assert(len(module_node.body[0].names) == 4)
    assert(module_node.body[0].names[0].name == 'absolute_import')
    assert(module_node.body[0].names[1].name == 'division')
    assert(module_node.body[0].names[2].name == 'print_function')
    assert(module_node.body[0].names[3].name == 'unicode_literals')
    assert(module_node.body[1].value.func.id == 'print')
    assert(module_node.body[1].value.args[0].n == 1)



# Generated at 2022-06-14 01:55:32.153837
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Unit test for constructor of class Python2FutureTransformer
    print('::: TEST: Python2FutureTransformer::__init__()')

    transformer = Python2FutureTransformer()
    print('>>> transformer:', transformer)
    assert transformer
    print('>>> transformer.target:', transformer.target)
    assert transformer.target == (2, 7)
    

# Generated at 2022-06-14 01:55:38.434814
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.fake_ast import FakeAST
    from ..base import BaseNodeTransformer
    fake_ast = FakeAST()
    for name, args in inspect.getmembers(BaseNodeTransformer):
        if name not in Python2FutureTransformer.__dict__:
            continue
        t = Python2FutureTransformer(fake_ast)
        func = getattr(t, name)
        node = getattr(fake_ast, args[0])
        func(node)

# Generated at 2022-06-14 01:55:40.621581
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    output = Python2FutureTransformer(None).visit(ast.parse('print(2)'))
    # print(ast.dump(output))

# Generated at 2022-06-14 01:55:51.070508
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast  # type: ignore
    from typed_ast.ast3 import Module, FunctionDef, arguments, Name, Load, NameConstant, Return, Str, Expr, Bytes, Call, Name, Load, Attribute, Store, AnnAssign, List, Num, Constant, NameConstant, Num, arguments, arg  # type: ignore
    #
    node = Module()
    node.body = []
    node.body.append(FunctionDef(name='greet', args=arguments(args=[arg(arg='name', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=NameConstant(value=None))], decorator_list=[], returns=None))

# Generated at 2022-06-14 01:55:51.871703
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:55:57.522279
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astunparse
    code = 'def f(): return 1'
    ast_tree = ast.parse(code)
    trans = Python2FutureTransformer()
    trans.visit(ast_tree)
    assert astunparse.unparse(ast_tree).startswith("from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\ndef f(): return 1")

# Generated at 2022-06-14 01:56:09.763570
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast
    from typed_ast import ast3 as ast
    from typed_ast import rewriter
    from typed_ast_extensions import Python2FutureTransformer

    node = ast.parse('some_code()')
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    rewriter.dump(node)
    assert transformer._tree_changed is True

# Generated at 2022-06-14 01:56:13.884201
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    cls = type('Python2FutureTransformer', (Python2FutureTransformer,), {})
    cls.target = (2, 7)
    obj = cls() 
    assert not obj._tree_changed


# Generated at 2022-06-14 01:56:18.675436
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    ast = compile("def foo(x):\n    return x + 1", filename='', mode='exec', flags=0, dont_inherit=False)
    ast = ast.body[0]
    assert_equal(transform(ast, {}).body[0].body[0].value.left.id, 'x')

# Generated at 2022-06-14 01:56:30.333534
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from stdlib_list import stdlib_list
    from test.fixtures.module_fixtures import Python2ModuleFixture, Python3ModuleFixture

    code = '''
a = 1
b = 2
c = a + b
'''.strip()

    tree = ast.parse(code)
    assert isinstance(tree, ast.Module)
    assert 0 == len(tree.body)

    transformer = Python2FutureTransformer(stdlib_list(2))
    tree = transformer.visit(tree)
    assert transformer._tree_changed

    assert isinstance(tree, ast.Module)
    assert 4 == len(tree.body)

    for i, stmt in enumerate(tree.body):
        assert isinstance(stmt, ast.ImportFrom)
        assert '__future__' == stmt.module

# Generated at 2022-06-14 01:56:40.072825
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse(imports.get_source(future='__future__'))
    assert isinstance(node, ast.Module)
    expected_body = [ast.ImportFrom(
        module='__future__',
        names=[
            ast.alias(
                name='absolute_import',
                asname=None
            ),
            ast.alias(
                name='division',
                asname=None
            ),
            ast.alias(
                name='print_function',
                asname=None
            ),
            ast.alias(
                name='unicode_literals',
                asname=None
            )]
        ,
        level=0
    )]
    assert node.body == expected_body


# Generated at 2022-06-14 01:56:52.293154
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    src = "some_code"
    tree = ast.parse(src)  # type: ignore
    assert isinstance(tree, ast.Module)
    assert len(tree.body) == 1
    assert isinstance(tree.body[0], ast.Expr)
    assert isinstance(tree.body[0].value, ast.Str)
    assert tree.body[0].value.s == 'some_code'
    Python2FutureTransformer().visit(tree)
    assert len(tree.body) == 5
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert tree.body[0].module == '__future__'
    assert tree.body[0].names[0].name == 'absolute_import'
    assert tree.body[1].names[0].name == 'division'

# Generated at 2022-06-14 01:57:02.223340
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Arrange
    import ast2json
    import json

    # Act
    input_tree = ast2json.loads("""
    print("test")
    """)
    expected_tree = ast2json.loads("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    print("test")
    """)
    transformer = Python2FutureTransformer()
    transformer.visit(input_tree)

    # Assert
    assert json.dumps(input_tree, indent=4) == json.dumps(expected_tree, indent=4)

# Generated at 2022-06-14 01:57:07.663670
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    node = ast.parse('print("Hello")')
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("Hello")
    """.strip()
    assert expected == astor.to_source(Python2FutureTransformer().visit(node)).strip()

# Generated at 2022-06-14 01:57:19.143439
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    class TestModule(unittest.TestCase):
        
        def test_some_tree(self):
            tree = ast.parse('''
                x = 1
                y = 2
            ''')
            Python2FutureTransformer.run(tree)

# Generated at 2022-06-14 01:57:30.746672
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:50.160986
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Unit test for method visit_Module of class Python2FutureTransformer"""
    # Test with modified tree
    module_node = ast.parse('x = 1', mode='eval')
    expected = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nx = 1', mode='eval')
    Python2FutureTransformer.visit_Module(module_node)
    assert ast.dump(module_node) == ast.dump(expected)
    # Test with unchanged tree
    module_node = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nx = 1', mode='eval')


# Generated at 2022-06-14 01:57:54.060468
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None
    assert transformer.target == (2, 7)
    assert transformer.name == 'Python2FutureTransformer'

# Generated at 2022-06-14 01:57:56.577289
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Construct instance of class Python2FutureTransformer
    instance = Python2FutureTransformer()
    assert isinstance(instance, Python2FutureTransformer)



# Generated at 2022-06-14 01:58:04.552050
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    class TestNode(object):
        """
        A node for testing.

        """
        _fields = ('body', 'type_ignores', 'future')

        def __init__(self):
            self.body = [ast.Expr(value=ast.Str(s='Hello world'))]
            self.type_ignores = None
            self.future = '__future__'

    node = TestNode()
    transformer = Python2FutureTransformer()
    result = transformer.visit_Module(node)
    correct = TestNode()
    correct.body = imports.get_body(future='__future__') + correct.body
    assert result == correct

# Generated at 2022-06-14 01:58:05.893207
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import parse

# Generated at 2022-06-14 01:58:07.518602
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.test_utils import check_transformer

    transformer = Python2FutureTransformer()
    assert check_transformer(transformer, '1 + 1')

# Generated at 2022-06-14 01:58:08.966503
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

#assert transformer.target == (2, 7)

# Generated at 2022-06-14 01:58:13.055084
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    line = "print('hello, world')\n"
    tree = ast.parse(line)
    new_tree = Python2FutureTransformer().visit(tree)
    print(new_tree)
    print(ast.dump(new_tree, include_attributes=True))


if __name__ == '__main__':
    test_Python2FutureTransformer()

# Generated at 2022-06-14 01:58:16.613524
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    py2ftr = Python2FutureTransformer()
    assert py2ftr._tree_changed == False
    assert py2ftr.target == (2, 7)

# Generated at 2022-06-14 01:58:26.871626
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass
# Code for module level docstring.
# This is required in order to generate documentation with sphinx.
if __name__ == "__main__":
    import argparse
    from seed.io.may_open import may_open_stdout, may_open_stdin
    parser = argparse.ArgumentParser(
        description='Prepends module with: from __future__ import absolute_import, from __future__ import division, from __future__ import print_function, from __future__ import unicode_literals',
        epilog='Unit test for Python2FutureTransformer'
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')

# Generated at 2022-06-14 01:58:32.813574
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.target == (2, 7)

if __name__ == '__main__':
    test_Python2FutureTransformer()

# Generated at 2022-06-14 01:58:39.965944
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    module = ast.parse("import a\n"
                       "import b\n"
                       "import future\n")
    transformer = Python2FutureTransformer()
    result = transformer.visit(module)
    assert isinstance(result, ast.Module)
    assert len(result.body) == 8  # type: ignore
    assert isinstance(result.body[0], ast.ImportFrom)  # type: ignore
    assert result.body[0].module == '__future__'  # type: ignore
    assert result.body[0].names[0].name == 'absolute_import'  # type: ignore

# Generated at 2022-06-14 01:58:49.232689
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ... import ast as unsafe_ast
    from ...testing import assert_code_equal
    from ...testing import assert_unchanged

    assert_unchanged(Python2FutureTransformer, 'print("hello")')
    assert_code_equal(Python2FutureTransformer,  # type: ignore
                      'print("hello")',
                      """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("hello")""")


# Generated at 2022-06-14 01:58:51.912357
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t is not None

# Unit test the visit_Module method of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:05.575447
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = textwrap.dedent("""
    print('hello world')
    """)
    node = ast.parse(code)
    Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 01:59:12.762646
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast
    class Node(ast.AST):
        _fields = ()
    node = Node()
    visitor = Python2FutureTransformer(target=(2, 7))
    new_node = visitor.visit(node)
    # import sys; print(sys.version_info)
    assert(isinstance(new_node.body[0], ast.Expr) and isinstance(new_node.body[0].value, ast.Call) and isinstance(new_node.body[0].value.func, ast.Attribute) and new_node.body[0].value.func.attr == 'version_info')

# Generated at 2022-06-14 01:59:14.121728
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:59:17.669454
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    '''
    Unit test for constructor of class Python2FutureTransformer
    '''
    # When
    transformer = Python2FutureTransformer()
    # Then
    assert transformer

# Generated at 2022-06-14 01:59:27.890871
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    src = """
try:
    from . import json
except ImportError:
    try:
        import json
    except ImportError:
        from django.utils import simplejson as json

"""
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
try:
    from . import json
except ImportError:
    try:
        import json
    except ImportError:
        from django.utils import simplejson as json
"""
    # When
    tree = astor.parse_file(StringIO(src))
    Python2FutureTransformer().visit(tree)
    # Then
    assert astor.to_source(tree).strip() == expected.strip()

# Generated at 2022-06-14 01:59:28.864105
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:59:47.702336
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .. import parse
    from .. import unpythonic
    from .. import transforms

    tree = parse(
        "from __future__ import nested_scopes\n"
        "from __future__ import generators\n"
        "from __future__ import division\n"
        "from __future__ import with_statement\n"
        "from __future__ import print_function\n"
        "from __future__ import unicode_literals\n"
        "from __future__ import absolute_import\n"
    )
    transformed = unpythonic.macros.walk(tree, transforms.Python2FutureTransformer)
    assert transformed.body[0].module == '__future__'
    assert transformed.body[1].module == '__future__'
    assert transformed.body[2].module == '__future__'

# Generated at 2022-06-14 01:59:53.293023
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('a = 1\nb = 2\n')  # type: ast.AST
    transformer = Python2FutureTransformer()
    transformed = transformer.visit(node)
    assert str(transformed) == 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\na = 1\nb = 2\n'

# Generated at 2022-06-14 01:59:59.657967
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.test_utils import compile_source, assert_correct_tree
    source = 'import os'
    source_tree = compile_source(source, '<string>', 'exec')
    expected_tree = compile_source(imports(future='__future__') + source, '<string>', 'exec')
    assert_correct_tree(Python2FutureTransformer, source, source_tree, expected_tree)

# Generated at 2022-06-14 02:00:00.643265
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:07.141831
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()

    node = ast.parse('foo = 42')
    expected = ast3.parse(
        'from __future__ import absolute_import\n'
        'from __future__ import division\n'
        'from __future__ import print_function\n'
        'from __future__ import unicode_literals\n'
        'foo = 42\n'
    )

    transformer.visit(node)

    assert ast3.dump(node) == ast3.dump(expected)

# Generated at 2022-06-14 02:00:10.279029
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class EmptySubclass(Python2FutureTransformer):
        pass
    instance = EmptySubclass()
    assert instance.__class__.__name__ == "EmptySubclass"

# Generated at 2022-06-14 02:00:11.233589
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:00:13.063212
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformers.tests.utils import transform, ast_equal

# Generated at 2022-06-14 02:00:21.252453
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import os
    import sys
    from typing import List, Tuple
    
    from typed_ast import ast3 as ast
    
    from typed_astunparse import dump
    from typed_astunparse import NodeTransformer
    from typed_astunparse import NodeVisitor
    from typed_astunparse import unparse
    
    from typed_astunparse.unparser import Unparser
    
    class Collector(NodeVisitor):
        
        def __init__(self, visitor, *args, **kwargs):
            self.visitor = visitor
            self.collector = []
            self.result = []
            self.visitor.result = self.result
        
        def visit(self, node: ast.AST) -> None:
            self.result.append((node, self.visitor.result))
            self.visitor

# Generated at 2022-06-14 02:00:27.109910
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.parse('')
    expected = imports.get_ast(future='__future__') + node.body  # type: ignore
    result = transformer.visit_Module(node)
    assert result.body == expected



# Generated at 2022-06-14 02:00:50.280024
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.snippet import snippet
    from ..utils.transform import transform
    from .future import Python2FutureTransformer

    @snippet
    def module_test(test):
        print(test)

    module_test_py2 = module_test.module_v2
    assert type(module_test_py2) == ast.Module
    assert module_test_py2.body[0].value.s == "print(test)"

    module_test_py2 = Python2FutureTransformer().visit(module_test_py2)
    assert module_test_py2.body[0].value.s == "from __future__ import absolute_import"
    assert module_test_py2.body[1].value.s == "from __future__ import division"

# Generated at 2022-06-14 02:01:00.868743
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..test.test_utils import get_test_case


# Generated at 2022-06-14 02:01:06.617029
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    python_version = (2, 7)
    source = "import sys, math"
    expected = "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\nimport sys, math"
    tree = ast.parse(source)
    Python2FutureTransformer(python_version).visit(tree)
    actual = astor.to_source(tree)
    assert actual == expected

# Generated at 2022-06-14 02:01:16.770689
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    ast_tree = ast.parse("""if a:
    pass""")
    Python2FutureTransformer().visit(ast_tree)
    pt_tree = ast.dump(ast_tree)
    assert pt_tree == "Module(body=[ImportFrom(module='future', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='unicode_literals', asname=None)], level=0), If(test=Name(id='a', ctx=Load()), body=[Pass()], orelse=[])])"

# Generated at 2022-06-14 02:01:18.673249
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)



# Generated at 2022-06-14 02:01:25.521251
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import make_dummy_future_node, make_dummy_future_tree
    from ..utils.source import source
    from ..utils.visitor import dump
    from .base import BaseNodeTransformer

    # When
    dummy_tree = make_dummy_future_tree()
    dummy_node = make_dummy_future_node()
    dummy_node.body = dummy_tree.body
    dummy_transformer = Python2FutureTransformer()
    result = dummy_transformer.visit_Modul

# Generated at 2022-06-14 02:01:26.947898
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer



# Generated at 2022-06-14 02:01:32.547217
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
x = 1
"""
    transformed_code = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = 1
"""
    tree = ast.parse(code)
    visitor = Python2FutureTransformer()
    visitor.visit(tree)
    assert astor.to_source(tree) == transformed_code

# Generated at 2022-06-14 02:01:38.688715
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from astor import to_source
    program = """
    class Foo:
        pass
    """
    tree = ast.parse(program=program)
    tree_updated = Python2FutureTransformer().visit(tree=tree)
    assert to_source(tree_updated) == '\nimport __future__\nfrom __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\n\nclass Foo:\n    pass\n'

# Generated at 2022-06-14 02:01:48.655234
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    source = """
import os
import sys

import abc

from future import absolute_import
from future import division
from future import print_function
from future import unicode_literals

print('hello world')
    """
    tree = ast.parse(source)
    result =  Python2FutureTransformer().visit(tree)
    print(astor.to_source(result))
    assert astor.to_source(result) == """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import os
import sys

import abc



print('hello world')
"""


# Generated at 2022-06-14 02:02:19.652849
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 02:02:23.052009
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import inspect
    import astor
    from ..transformers import Python2FutureTransformer

    assert inspect.isclass(Python2FutureTransformer)

    # from ..transformers import Python2FutureTransformer

# Generated at 2022-06-14 02:02:25.892947
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('stmt')
    node = tree.body[0]
    trans = Python2FutureTransformer()
    trans.visit_Module(node)
    assert trans._tree_changed



# Generated at 2022-06-14 02:02:27.269962
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert callable(Python2FutureTransformer)

# Generated at 2022-06-14 02:02:33.527550
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = inspect.cleandoc(
    '''
    def a(): pass
    def b(): pass
    '''    
    )
    expected = inspect.cleandoc(
    '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def a(): pass
    def b(): pass
    '''    
    )    
    tree = ast.parse(source)
    Python2FutureTransformer().visit(tree)
    result = astor.to_source(tree)
    assert expected == result

# Generated at 2022-06-14 02:02:40.207339
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import run_transformer_on_single_file
    file_contents = '''
    from __future__ import print_function
    '''
    assert run_transformer_on_single_file(file_contents, Python2FutureTransformer) == \
        '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
       
    from __future__ import print_function
    '''

# Generated at 2022-06-14 02:02:46.012090
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import parse
    from ast_transformer.utils.ast_diff import diff
    tree = parse('a = 5\nb = 6')
    tree = Python2FutureTransformer().visit(tree)  # type: ignore
    assert diff(tree, parse(imports + '\na = 5\nb = 6')) == ""



# Generated at 2022-06-14 02:02:47.419506
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 02:02:52.491295
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from yatiflask.transformer.base import BaseNodeVisitor
    from .fixtures.general import code as module_code

    visitor = BaseNodeVisitor()
    node = visitor.visit(ast.parse(module_code))

    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    assert transformer._tree_changed == True

# Generated at 2022-06-14 02:02:55.826802
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import parse
    from ..utils.source_code import SourceCode


# Generated at 2022-06-14 02:04:09.828133
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:04:16.265218
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_factory import ast_factory
    tree = ast.parse('x = 1')
    node = tree.body[0]
    tr = Python2FutureTransformer()
    res = tr.visit_Module(node)
    assert res == ast_factory("x = 1")

# Generated at 2022-06-14 02:04:18.746600
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    trans = Python2FutureTransformer()
    assert trans.target == (2, 7)


# Generated at 2022-06-14 02:04:22.353543
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import parse
    from . import run_transformer_test


# Generated at 2022-06-14 02:04:24.944488
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert isinstance(x, BaseNodeTransformer)
    assert x.target == (2, 7)
    # Python2FutureTransformer.visit_Module not implemented

# Generated at 2022-06-14 02:04:26.612241
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tr = Python2FutureTransformer(None)
    assert isinstance(tr, Python2FutureTransformer)


# Generated at 2022-06-14 02:04:27.437785
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:04:30.952637
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    trs = Python2FutureTransformer(None)
    node = ast.parse('print("test")')
    node_result = trs.visit_Module(node)
    assert node_result.body == imports.get_body(future='__future__') + node.body  # type: ignore

# Generated at 2022-06-14 02:04:36.775678
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tf = Python2FutureTransformer()
    n = ast.parse("print('foo')")
    tf.visit(n)
    assert tf._tree_changed is True
    assert isinstance(n, ast.Module)
    assert len(n.body) == 5
    assert isinstance(n.body[0], ast.ImportFrom)
    assert n.body[0].names[0].name == 'absolute_import'
    assert n.body[4].value.s == 'foo'

# Generated at 2022-06-14 02:04:45.089154
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Module
    from typed_ast.ast3 import Assign

    module = Module(
        body=[
            Assign(
                targets=[ast.Name(id='a', ctx=ast.Store())],
                value=ast.Num(n=1)
            )
        ]
    )

    result = Python2FutureTransformer().visit(module)  

    assert isinstance(result, Module)
    assert len(result.body) == 5
    assert result.body[0].module == '__future__'

