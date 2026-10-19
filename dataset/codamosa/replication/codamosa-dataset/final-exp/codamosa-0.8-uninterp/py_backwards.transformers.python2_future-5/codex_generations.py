

# Generated at 2022-06-14 01:55:10.073050
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astunparse
    node = ast.parse("x = 2")
    t = Python2FutureTransformer()
    node = t.visit(node)
    unparse_node = astunparse.unparse(node)
    assert t._tree_changed is True
    assert unparse_node.startswith("from __future__ import absolute_import"), "Adding from __future__ import absolute_import failed"
    assert unparse_node.startswith("from __future__ import division"), "Adding from __future__ import division failed"
    assert unparse_node.startswith("from __future__ import print_function"), "Adding from __future__ import print_function failed"
    assert unparse_node.startswith("from __future__ import unicode_literals"), "Adding from __future__ import unicode_literals failed"

# Generated at 2022-06-14 01:55:19.452822
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    assert Python2FutureTransformer().visit(ast.parse(dedent('''\
        from future import print_function
        
        from past import print
        from past import print_function
    '''))) == ast.parse(dedent('''\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ imports unicode_literals
        
        from future import print_function
        
        from past import print
        from past import print_function
    '''))

# Generated at 2022-06-14 01:55:27.077384
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('def f(): return 1')
    transformer = Python2FutureTransformer()
    transformed = transformer.visit(module)

# Generated at 2022-06-14 01:55:31.905956
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import unparse
    from . import parse
    from .base import BaseNodeTransformer
    from ..utils.snippet import snippet

    # Unit test with string

# Generated at 2022-06-14 01:55:40.233052
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse("x = 'б'")
    assert ast.dump(node) == 'Module(body=[Assign(targets=[Name(id="x", ctx=Store())], value=Str(s="б"))])'
    t = Python2FutureTransformer()
    _node = t.visit(node)

# Generated at 2022-06-14 01:55:48.697388
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from collections import OrderedDict
    from ..utils.test_utils import assert_source
    from ..utils.test_utils import assert_source_snippet
    from ..utils.test_utils import statement

    source = """
        None
    """
    expected = """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        None
    """
    module = statement.transform(Python2FutureTransformer, OrderedDict([
        ('source', source),
    ]))
    assert_source(module, expected)



# Generated at 2022-06-14 01:55:57.254170
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    input_source = """
    def func(a, b):
    pass
    """
    expected_output = """
    # coding: utf-8
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def func(a, b):
    pass
    """
    input_ast = ast.parse(input_source)
    transformer = Python2FutureTransformer()
    new_ast = transformer.visit(input_ast)
    output_source = ast.unparse(new_ast)
    assert output_source == expected_output

# Generated at 2022-06-14 01:56:08.519017
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Tests that the visit_Module method does what is expected.
    """
    import astor
    
    from .base import BaseNodeTransformer
    from .base import NodeTransformerTestCase

    from .base import patch_ast_node, patch_generic_visit
    from ..modes import OutSource
    from ..modes import ToPython27

    class MockPython2FutureTransformer(Python2FutureTransformer):
        def __init__(self, tree, mode):
            BaseNodeTransformer.__init__(self, tree, mode)
            self._tree_changed = False
            
    class TestCase(NodeTransformerTestCase):
        target = ToPython27

        def setUp(self):
            self.transformer = MockPython2FutureTransformer(self.tree, self.mode)


# Generated at 2022-06-14 01:56:19.493923
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils import cst
    from .context import Context
    code = "def foo(): return 1"
    node = cst.parse_expression(code)
    context = Context.from_node(node, future='__future__')
    # node.body = imports.get_body(future='__future__') + node.body  # type: ignore
    transformed_node = Python2FutureTransformer(context).visit(node)
    assert isinstance(transformed_node, ast.Module)
    code_after = cst.unparse(transformed_node).strip()

# Generated at 2022-06-14 01:56:31.255330
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformers import Python2FutureTransformer
    from ..transformers import Python2StrToBytesTransformer
    from ..transformers import Python2UnicodeTransformer
    from ..utils.fixtures import snippet_with_future_unicode

    snippet_with_future_unicode.get_tree()
    Python2FutureTransformer(snippet_with_future_unicode).visit()
    assert snippet_with_future_unicode.get_source() == \
           'from __future__ import absolute_import\n' \
           'from __future__ import division\n' \
           'from __future__ import print_function\n' \
           'from __future__ import unicode_literals\n' \
           '\n' \
           's = u""'

    # Test that adding another future import is fine.


# Generated at 2022-06-14 01:56:39.869419
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    import textwrap
    from typed_ast.ast3 import parse
    from typed_ast.ast3 import Module
    from beniget import Python2FutureTransformer
    transformer = Python2FutureTransformer()
    input_code = textwrap.dedent('''
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    ''')
    tree: Module = parse(input_code)
    expected_code = textwrap.dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    ''')
    new_tree = transformer

# Generated at 2022-06-14 01:56:47.874394
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.test_utils import parse, compare_ast
    ast1 = parse("sys.exit()")
    ast2 = parse("from __future__ import absolute_import; from __future__ import division; from __future__ import print_function; from __future__ import unicode_literals; sys.exit()")
    transformer = Python2FutureTransformer()
    result = transformer.visit(ast1)
    compare_ast(result, ast2)
    assert transformer.tree_changed is True


# Generated at 2022-06-14 01:56:57.735831
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse("print('Hello, World!')")
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    assert tree.body[0].value.s == "__future__"
    assert tree.body[1].value.s == "absolute_import"
    assert tree.body[2].value.s == "division"
    assert tree.body[3].value.s == "print_function"
    assert tree.body[4].value.s == "unicode_literals"
    assert tree.body[5].value.s == "Hello, World!"



# Generated at 2022-06-14 01:57:08.428059
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('print("ok")')
    Python2FutureTransformer(node).visit(node)

# Generated at 2022-06-14 01:57:19.174053
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Given
    code = """
    print("Hello, World!")
    """

    expected_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    print("Hello, World!")
    """

    t = Python2FutureTransformer()
    s = textwrap.dedent(code).strip()
    module = ast.parse(s)
    # When
    t.visit(module)
    # Then
    expected_module = ast.parse(textwrap.dedent(expected_code).strip())
    assert ast.dump(module, annotate_fields=False) == ast.dump(expected_module, annotate_fields=False)

# Generated at 2022-06-14 01:57:28.271195
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse("print('hello')")
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    body = node.body
    expected_body = imports.get_body(future='__future__') + [ast.Expr(ast.Call(ast.Name('print', ast.Load()), [ast.Str('hello')], [])), ast.Pass()]
    assert len(body) == len(expected_body)
    for stmt, expected_stmt in zip(body, expected_body):
        assert ast.dump(stmt) == ast.dump(expected_stmt)

# Generated at 2022-06-14 01:57:32.047234
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    target = (2, 7)
    transformer = Python2FutureTransformer(target=target)
    module = ast.parse('pass')
    transformer.visit(module)
    assert transformer._tree_changed
    assert module.body[0].value.s == '__future__'

# Generated at 2022-06-14 01:57:38.464341
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse("print('Hello World!')")
    Python2FutureTransformer().visit(node)
    assert ast.dump(node) == dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        print('Hello World!')
        """).strip()

# Generated at 2022-06-14 01:57:45.362365
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astunparse
    from nfldraft.utils.parse import ParsingError
    from nfldraft.transformers.base import PythonTransformer
    from nfldraft.transformers.noop import NoopTransformer
    from nfldraft.transformers.future import Python2FutureTransformer
    from nfldraft.transformers.unicode_literals import Python3UnicodeLiteralsTransformer
    pipeline = PythonTransformer([
        NoopTransformer(),
        Python2FutureTransformer(),
        Python3UnicodeLiteralsTransformer()
    ])
    with pytest.raises(ParsingError):
        pipeline.parse("""
            print('test')
        """)

# Generated at 2022-06-14 01:57:55.695827
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astunparse
    tree = ast.parse(
        """
        A + B
        """
    )
    result = astunparse.unparse(tree)
    expected = """
    A + B
    """
    result = result.strip()
    expected = expected.strip()
    assert result == expected
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree=tree)
    result = astunparse.unparse(tree)
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    A + B
    """
    result = result.strip()
    expected = expected.strip()
    assert result == expected

# Generated at 2022-06-14 01:58:04.912469
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast

    # Expected Output
    expected_output = ast.parse(
        "from __future__ import absolute_import\n"
        "from __future__ import division\n"
        "from __future__ import print_function\n"
        "from __future__ import unicode_literals\n"
    )

    # Actual output
    actual_output = Python2FutureTransformer().visit(ast.parse(""))

    # Check for equality
    assert ast.dump(actual_output) == ast.dump(expected_output)

# Generated at 2022-06-14 01:58:06.966788
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    node = ast.parse('k=12')
    Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 01:58:10.472429
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    module = ast.parse("print('test')")
    transformer = Python2FutureTransformer(None)
    assert transformer.visit(module) is not None
    assert 'from __future__ import absolute_import' in astor.to_source(module)

# Generated at 2022-06-14 01:58:17.070044
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Given
    import astor
    string = '''
    assert isinstance(x, int)
    '''
    # When
    mod = ast.parse(string)
    result = Python2FutureTransformer().visit(mod)
    # Then
    assert(astor.to_source(result) == dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    assert isinstance(x, int)
    '''))


# Generated at 2022-06-14 01:58:23.626717
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    ast_tree = ast.parse('a=1\nb=2\nc=3')
    transformer = Python2FutureTransformer()
    transformer.visit(ast_tree)
    source = source_code_visit(ast_tree)
    assert source == "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\na=1\nb=2\nc=3"

# Generated at 2022-06-14 01:58:25.650486
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)



# Generated at 2022-06-14 01:58:35.798604
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = "print('hello')"
    tree = ast.parse(code)
    Python2FutureTransformer().visit(tree)
    assert ast.dump(tree) == "Module(body=[ImportFrom(module='future', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='unicode_literals', asname=None)], level=0), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='hello')], keywords=[]))])"

# Generated at 2022-06-14 01:58:37.523911
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    instance = Python2FutureTransformer()
    assert isinstance(instance, Python2FutureTransformer)


# Generated at 2022-06-14 01:58:47.590615
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import Module
    # Arrange
    # Act
    transformer = Python2FutureTransformer()
    source = "print('Hello from Python 2')"
    node = ast.parse(source, mode="exec")
    module_node = transformer.visit(node)
    # Assert
    assert isinstance(module_node, Module)
    assert module_node._fields == ('body',)
    assert module_node.body[0]._fields == ('names',)
    assert module_node.body[0].names == [('absolute_import', None), ('division', None), ('print_function', None), ('unicode_literals', None)]

# Generated at 2022-06-14 01:58:54.255851
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    src = '''
a = 1
b = a
    '''

    expected = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

a = 1
b = a
    '''

    tree = ast.parse(src)
    Python2FutureTransformer().visit(tree)
    actual = ast.unparse(tree)
    assert actual == expected

# Generated at 2022-06-14 01:59:05.705893
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
    import numpy."""
    expect_code = """
import future
from future import absolute_import
from future import division
from future import print_function
from future import unicode_literals
    import numpy."""
    tree = ast.parse(code)
    tr = Python2FutureTransformer()
    tr.visit(tree)
    assert ast.dump(tree, include_attributes=False) == expect_code



# Generated at 2022-06-14 01:59:12.808048
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    a = ast.parse('module = 1')
    assert ast.dump(a) == 'Module(body=[Assign(targets=[Name(id=\'module\', ctx=Store())], value=Num(n=1))])'

    b = Python2FutureTransformer()
    b.visit(a)

# Generated at 2022-06-14 01:59:24.678454
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    test_string = "import os\nprint('test')"
    test_tree = ast.parse(test_string)
    transformer.visit(test_tree)
    assert transformer._tree_changed == True
    assert len(test_tree.body) == 5
    assert test_tree.body[0].names[0].name == 'absolute_import'
    assert test_tree.body[1].names[0].name == 'division'
    assert test_tree.body[2].names[0].name == 'print_function'
    assert test_tree.body[3].names[0].name == 'unicode_literals'
    assert test_tree.body[4].names[0].name == 'os'

# Generated at 2022-06-14 01:59:28.365546
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..transformers import _transformers_by_version

    for version in _transformers_by_version.keys():
        if version[0] != 2:
            continue
        assert Python2FutureTransformer in _transformers_by_version[version]
        break

# Generated at 2022-06-14 01:59:33.749414
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils import generate_syntax_tree
    from ..utils import unit_test_ast

    unit_test_ast(
        generate_syntax_tree(Python2FutureTransformer),
        imports().get_node(future='__future__') + unit_test_ast()
    )


registry.register_transformer(Python2FutureTransformer)

# Generated at 2022-06-14 01:59:41.581352
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    before = ast.parse('1+1')
    after = ast.parse(
        """
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        1+1
        """
    )
    assert Python2FutureTransformer().visit(before) == after

# Generated at 2022-06-14 01:59:42.933384
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    f = sut.Python2FutureTransformer()
    assert f

# Generated at 2022-06-14 01:59:53.521069
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('import os')
    x = Python2FutureTransformer()
    node = x.visit(node)

# Generated at 2022-06-14 01:59:55.087848
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:59:58.073073
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)
    assert t.generic_visit(None) is None
    assert t.visit_Module(None) is None

# Generated at 2022-06-14 02:00:14.460333
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    test_code = '''
    def f():
        pass
    '''
    output_code = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    def f():
        pass
    '''
    node = ast.parse(test_code)
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)
    assert transformer._tree_changed is True
    assert ast.dump(new_node) == ast.dump(ast.parse(output_code))

# Generated at 2022-06-14 02:00:20.751414
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    transformer = Python2FutureTransformer(target=(2, 7))
    transformer._tree_changed = False

    node = ast.parse(
        """
import os, sys

print('hello')
    """
    )
    module = transformer.visit(node)
    assert transformer._tree_changed == True
    expected = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os, sys

print('hello')
    """
    actual = astor.to_source(module)
    assert expected == actual

# Generated at 2022-06-14 02:00:22.658580
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert isinstance(t, BaseNodeTransformer)

# Generated at 2022-06-14 02:00:24.864610
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None).target == (2, 7)


# Generated at 2022-06-14 02:00:36.049587
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast as ast_module   
    # check if Module object is created
    assert isinstance(Python2FutureTransformer().visit(ast_module.Module(body=[])), ast_module.Module)
    # check if Module object is created and it's body contains absolute_import
    assert Python2FutureTransformer().visit(ast_module.Module(body=[])).body[0].name == 'absolute_import'
    # check if Module object is created and it's body contains division
    assert Python2FutureTransformer().visit(ast_module.Module(body=[])).body[1].name == 'division'
    # check if Module object is created and it's body contains print_function
    assert Python2FutureTransformer().visit(ast_module.Module(body=[])).body[2].name == 'print_function'
    # check if

# Generated at 2022-06-14 02:00:39.409724
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer
    """
    # Given
    from ..lexer import Python2Lexer

    # When
    transformer = Python2FutureTransformer(Python2Lexer())

    # Then
    assert transformer

# Generated at 2022-06-14 02:00:43.861108
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.test_visitor import TestVisitor
    TestVisitor(Python2FutureTransformer)
    
    code = """assert(True)"""
    expected_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    assert(True)
    """
    TestVisitor.test_code(code, expected_code)

# Generated at 2022-06-14 02:00:45.673218
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:00:48.009158
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for Python2FutureTransformer class"""
    assert Python2FutureTransformer.target == (2, 7)

# Generated at 2022-06-14 02:00:50.036954
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'


# Generated at 2022-06-14 02:01:10.921553
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3
    from typed_ast import parse

    transformer = Python2FutureTransformer()
    before = ast3.parse('a = 1\na = 2')
    after = transformer.visit(before)
    assert after is not before
    assert transformer._tree_changed
    assert transformer.visit(after) is after

# Generated at 2022-06-14 02:01:11.734388
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:12.509800
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # No exception thrown
    return Python2FutureTransformer()

# Generated at 2022-06-14 02:01:14.240145
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    py2transformer = Python2FutureTransformer()
    assert py2transformer

# Generated at 2022-06-14 02:01:25.522287
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # pylint: disable=unused-variable
    try:
        from typed_ast import ast3
        import astor
    except ImportError:
        # typed_ast isn't available, so we can't run the test, but that is okay.
        pass
    in_code = """
    def add(a, b):
        return a + b
    """
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    
    def add(a, b):
        return a + b
    """
    pt = astor.parse_tree(in_code, line_numbers=False, file_name='main')

# Generated at 2022-06-14 02:01:26.781376
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 02:01:34.598027
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    t = Python2FutureTransformer()
    node = ast.parse(textwrap.dedent('''\
        import six
        print('hello world')
        '''))
    node = t.visit(node)
    code = ast.unparse(node)
    assert code == textwrap.dedent('''\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        
        import six
        print('hello world')
        
        ''')
    return



# Generated at 2022-06-14 02:01:35.847968
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast
    import astunparse
    import _ast


# Generated at 2022-06-14 02:01:37.289657
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer._tree_changed == False

# Generated at 2022-06-14 02:01:44.552560
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import get_ast

    ast1 = get_ast(
        '''
a = 1
b = 2
        '''
    )
    
    ast2 = get_ast(
        '''
from future import absolute_import
from future import division
from future import print_function
from future import unicode_literals
a = 1
b = 2
        '''
    )
    
    tr = Python2FutureTransformer()
    tr.visit(ast1)
    assert ast1 == ast2

# Generated at 2022-06-14 02:02:16.490628
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseNodeTransformer)
    
    

# Generated at 2022-06-14 02:02:27.932996
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.Module()
    node.body = [
        ast.Assign(targets=ast.Name('x', ast.Store()), value=ast.Num(1)),
        ast.Assign(targets=ast.Name('y', ast.Store()), value=ast.Num(2))

    ]
    transformer.visit(node)
    future = ast.ImportFrom(module='__future__', names=[
        ast.alias(name='absolute_import', asname=None),
        ast.alias(name='division', asname=None),
        ast.alias(name='print_function', asname=None),
        ast.alias(name='unicode_literals', asname=None)
    ],
                            level=0)
    assert node.body == ast

# Generated at 2022-06-14 02:02:29.522071
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.__class__.__name__ == "Python2FutureTransformer"


# Generated at 2022-06-14 02:02:40.132175
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.parse("a = 1")
    node_changed = transformer.visit(node)
    assert node != node_changed
    assert ast.dump(node) == ast.dump(ast.parse("a = 1"))
    expected = ast.parse("""\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
a = 1
""")

    assert ast.dump(expected) == ast.dump(node_changed)
    assert transformer._tree_changed is True

# This test is used to verify that the method visit_Module of Python2FutureTransformer is not
# used during type checking.

# Generated at 2022-06-14 02:02:50.510927
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.nodeprint import format_node
    from ..test import snippet_test
    from typing import Any

    class Dummy(ast.AST):
        _fields = ()
        def __init__(self):
            pass
        def __repr__(self) -> str:
            return 'Dummy'


    node: ast.Module = ast.parse(
        "import os\n"
        "import sys")
    assert format_node(node) == \
        "Module(body=[\n" \
        "    Import(names=[\n" \
        "        alias(name='os', asname=None),\n" \
        "        alias(name='sys', asname=None)]),\n" \
        "    Dummy()])"
    res

# Generated at 2022-06-14 02:02:57.951203
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.parse("a = 1")
    node = transformer.visit(node)
    assert isinstance(node, ast.Module)
    assert transformer.tree_changed
    assert transformer.targets == [(2, 7)]
    assert transformer.future_import
    assert node.body[0].lineno == 1
    assert 'from __future__ import absolute_import' in ast.dump(node.body[0])
    assert node.body[1].lineno == 1
    assert 'from __future__ import division' in ast.dump(node.body[1])
    assert node.body[2].lineno == 1
    assert 'from __future__ import print_function' in ast.dump(node.body[2])
    assert node.body[3].lineno == 1

# Generated at 2022-06-14 02:03:02.605578
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    assert Python2FutureTransformer().visit(ast.parse("a = 2")) == ast.parse(
        """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
a = 2
"""
    )

# Generated at 2022-06-14 02:03:11.745770
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import make_snippet, make_future_snippet
    from ..utils.general import compare_ast
    from ..utils.matchers import ANY, Call, Name, ImportFrom
    
    
    code = make_snippet(
        "print('Hello World!')"
    )
    expected = make_future_snippet(code)
    
    py2ft = Python2FutureTransformer()
    tree = ast.parse(code)
    new_tree = py2ft.visit(tree)
    compare_ast(new_tree, expected)
    assert py2ft.tree_changed is True



# Generated at 2022-06-14 02:03:21.507887
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..transformer import NodeTransformer

    class EmptyTransformer(NodeTransformer):
        def visit_Str(self, node: ast.Str) -> ast.Str:
            return node

    expected = ast.parse(imports(future='''__future__''') + '''
x = "hello"
''')
    t = EmptyTransformer(Python2FutureTransformer())
    actual = t.visit(ast.parse('''
x = "hello"
'''))  # type: ignore
    assert ast.dump(expected, annotate_fields=False) == ast.dump(actual, annotate_fields=False)



# Generated at 2022-06-14 02:03:27.795726
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Test python 2 future transformer"""
    from .. import ast_conversion
    from ..parse import parse_string
    from ..unparse import dump_ast

    test_src = """
    import abc
    import os

    def test():
        print('Hello world')

    """
    tree = parse_string(test_src)
    tree = ast_conversion(tree, target=(2, 7))
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    print(dump_ast(tree))

# Generated at 2022-06-14 02:04:45.265205
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from test import test_future
    try:
        test_future
    except NameError:
        module = ast.parse(future_import_snippet)
        module.body = imports.get_body(future="__future__") + module.body  # type: ignore

# Generated at 2022-06-14 02:04:49.911043
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    module = ast.parse("1 + 2")
    assert module.body[0].value.op == ast.Add()
    module2 = Python2FutureTransformer().visit(module)
    assert module2.body[0].value.op == ast.Add()


# Generated at 2022-06-14 02:05:00.200422
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
  from typed_ast import ast3 as typed_ast
  import astor
  from ..utils.sample_programs import python2_sample
  from .base import MockNodeTransformer

  # Patch typed_ast.parse
  typed_ast.parse = ast.parse

  class MockNodeTransformer(MockNodeTransformer):
    def __init__(self, *args, **kwargs):
      self.future_import_line = None
      super(MockNodeTransformer, self).__init__(*args, **kwargs)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
      if len(node.names) == 4:
        self.future_import_line = node
        return
      return node

  nt = MockNodeTransformer()