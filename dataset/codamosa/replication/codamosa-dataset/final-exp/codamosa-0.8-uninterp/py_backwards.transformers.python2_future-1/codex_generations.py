

# Generated at 2022-06-14 01:55:11.294867
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    #
    # Cases:
    #
    #   - Any module
    #
    module = ast.parse(src="")
    #
    # Apply transformation and check result
    #
    transformed = Python2FutureTransformer().visit(module)
    assert isinstance(transformed, ast.Module)
    assert len(transformed.body) == 4
    assert isinstance(transformed.body[0], ast.ImportFrom)
    assert transformed.body[0].names[0].name == 'absolute_import'
    assert transformed.body[1].names[0].name == 'division'
    assert transformed.body[2].names[0].name == 'print_function'
    assert transformed.body[3].names[0].name == 'unicode_literals'

# Generated at 2022-06-14 01:55:23.160365
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test the method visit_Module of class Python2FutureTransformer by
    checking that the source of the module
    """
    from ..utils import parse_source
    source = [
        "number = 0.1"
    ]
    expected = [
        "from __future__ import absolute_import",
        "from __future__ import division",
        "from __future__ import print_function",
        "from __future__ import unicode_literals",
        "number = 0.1"
    ]
    module = parse_source(source)

    visitor = Python2FutureTransformer(target=(2, 7))
    new_module = visitor.visit(module)
    assert expected == [line.strip() for line in new_module.ast.body]

# Generated at 2022-06-14 01:55:30.300681
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.builder import build
    from ..utils.source import source
    from .base import get_transformer_classes
    tree = build(source("""
        def foo(x):
            return x
        def bar(y):
            return y
    """))
    transformer_classes = get_transformer_classes(Python2FutureTransformer)
    transformer = Python2FutureTransformer(tree, transformer_classes, 1)
    tree = transformer.visit(tree)
    assert transformer.tree_changed == True
    assert transformer.target == Python2FutureTransformer.target
    assert tree.body[:4] == imports.get_body(future='__future__')
    assert tree.body[4:] == tree

# Generated at 2022-06-14 01:55:38.893107
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .base import BaseNodeTransformer
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from ..utils import get_ast
    from ..utils.snippet import snippet

    @snippet
    def m1(a):
        return a

    node = get_ast(m1)

    t = Python2FutureTransformer()
    new_node = t.visit(node)  # type: ignore

    # Tree did change
    assert new_node is not node

    # Methods visit_Module of class Python2FutureTransformer added 4 new lines at the top of module
    assert len(new_node.body) == 5
    assert isinstance(new_node.body[0], ast.Expr)
    assert isinstance(new_node.body[1], ast.Expr)

# Generated at 2022-06-14 01:55:43.175888
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import ast_utils
    from . import parse_ast

    module = ast_utils.extract_module(imports.get_body())
    tree = parse_ast(module)
    Python2FutureTransformer().visit(tree)
    assert ast_utils.dump_ast(tree) == module

# Generated at 2022-06-14 01:55:53.475019
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    initial_ast = ast.parse("print('Hello world')")
    expected = ast.Module(body=[
        ast.ImportFrom(module='__future__', 
                       names=[
                           ast.alias(name='absolute_import', asname=None),
                            ast.alias(name='division', asname=None),
                            ast.alias(name='print_function', asname=None),
                            ast.alias(name='unicode_literals', asname=None)
                       ], 
                       level=0)
        , ast.Expr(value=ast.Str(s='Hello world'))
    ])
    actual = Python2FutureTransformer().visit(initial_ast)
    assert ast.dump(actual, include_attributes=False) == ast.dump(expected, include_attributes=False)

# Generated at 2022-06-14 01:56:03.797738
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = """
    # comment
    import sys as s
    import six as x
    import os
    import decimal

    print("test")
    """

    tests = (
        # input, expected
        (code, """
    # comment
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import sys as s
    import six as x
    import os
    import decimal

    print("test")
        """),
    )

    for i, test in enumerate(tests):
        i += 1  # <== test number
        logger.debug('')
        logger.debug('test {}: starting'.format(i))
        logger.debug('input:\n{!r}'.format(test[0]))


# Generated at 2022-06-14 01:56:10.694867
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_utilities import parse_ast

    code = """
    class Foo(object):
        pass
    """
    expected_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    class Foo(object):
        pass
    """

    tree = parse_ast(code)
    Python2FutureTransformer().visit(tree)  # type: ignore
    assert code != expected_code
    assert ast.dump(tree) == expected_code

# Generated at 2022-06-14 01:56:21.206447
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer(from_version=(2,7))
    module = ast.parse("a = 2\nb = 3")
    with pytest.raises(NotImplementedError):
        transformer.visit(module)
    assert transformer._tree_changed
    assert not transformer._from_version
    assert transformer._to_version == (2, 7)
    assert isinstance(module.body[0], ast.ImportFrom)
    assert module.body[0].module == '__future__'
    assert module.body[0].names == [ast.alias(name='absolute_import', asname=None), 
        ast.alias(name='division', asname=None), ast.alias(name='print_function', asname=None), 
        ast.alias(name='unicode_literals', asname=None)]

# Generated at 2022-06-14 01:56:32.609150
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # assert ast.parse(""""
    # """") == ast.parse(""""
    # """)

    assert ast.parse("""
    """) == ast.parse("""
    """)

    assert ast.parse("""
        import six
        import base
    """) == ast.parse("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import six
        import base
    """)

    assert ast.parse("""
        from . import base
    """) == ast.parse("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        from . import base
    """)



# Generated at 2022-06-14 01:56:38.870239
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import astor
    node = ast.parse("import sys")
    node = Python2FutureTransformer(debug=False).visit(node)
    print(astor.to_source(node))
    assert astor.to_source(node) == dedent("""\
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    
    import sys""")

# Generated at 2022-06-14 01:56:46.825932
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .. import parse

    # Testing code snippet
    code = """
print("hi")
"""

    # Expected output
    expected_code = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
print("hi")
"""

    # unit test
    module = parse(code)
    new_module = Python2FutureTransformer().visit(module)
    assert str(new_module) == expected_code

# Generated at 2022-06-14 01:56:59.294684
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    fname = "dummy.py"
    src = "\n".join([
            "print('Hello World')",
            "x = 3",
            "print(x)"
    ])
    tree = ast.parse(src)
    transformer.visit(tree)
    transformer.tree = tree
    newcode = transformer.to_sourcecode()
    expected = "\n".join([
            "from __future__ import absolute_import",
            "from __future__ import division",
            "from __future__ import print_function",
            "from __future__ import unicode_literals",
            "print('Hello World')",
            "x = 3",
            "print(x)"
    ])
    assert newcode == expected

# Generated at 2022-06-14 01:57:05.847871
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():   
    # Given
    tree = ast.parse("'some string'")

    # When
    transformer = Python2FutureTransformer()
    transformer.visit(tree)

    # Then
    assert transformer._tree_changed == True
    assert astor.to_source(tree) == "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n'some string'"

# Generated at 2022-06-14 01:57:15.307387
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    # Test function
    def test(snippet, expected):
        node = ast.parse(snippet)
        Python2FutureTransformer().visit(node)
        actual = ast.dump(node)
        assert expected == actual

    # Test snippets
    module = "{0}\n\n{1}\n\n"

    test(
        snippet=module.format("pass", "pass"),
        expected=module.format(imports, "pass").replace("\n", "\n    ").replace("\n\n", "\n") + "\n",
    )

# Generated at 2022-06-14 01:57:24.968997
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('def foo():\n    pass')
    Python2FutureTransformer().visit(tree)
    result = '\n'.join(ast.dump(tree, include_attributes=True).split('\n')[1:7])
    expected = 'Module(body=[ImportFrom(module="__future__", names=[alias(name="absolute_import", asname=None)], level=0), ImportFrom(module="__future__", names=[alias(name="division", asname=None)], level=0), ImportFrom(module="__future__", names=[alias(name="print_function", asname=None)], level=0), ImportFrom(module="__future__", names=[alias(name="unicode_literals", asname=None)], level=0)'
    assert result == expected

# Generated at 2022-06-14 01:57:31.412546
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ast import parse

    module = parse("import ujson")
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)
    assert transformer._tree_changed
    assert astor.to_source(module) == """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import ujson
    """.strip()

# Generated at 2022-06-14 01:57:41.580140
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # arrange
    node_module = ast.parse('print("test")')
    node_module.body[0].lineno = 1
    node_module.body[0].col_offset = 0
    node_module.body[0].end_lineno = 1
    node_module.body[0].end_col_offset = 1
    node_module.body[0].value.lineno = 1
    node_module.body[0].value.col_offset = 0
    node_module.body[0].value.end_lineno = 1
    node_module.body[0].value.end_col_offset = 1

# Generated at 2022-06-14 01:57:48.774962
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    code = '''print(a, b)'''
    module = ast.parse(code, 'example.py')
    Python2FutureTransformer.run(module)
    assert astor.to_source(module).strip() == '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print(a, b)
'''.strip()

# Generated at 2022-06-14 01:57:58.618398
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from ..utils import get_fixture_path
    from ..utils.examples import python2_example_module
    from ..utils.visitor import AstVisitor

    class _(AstVisitor):
        def __init__(self):
            super().__init__()

            self.visitor = Python2FutureTransformer()

        def get_transformed_module(self):
            self.visitor.visit(self.module)
            return self.module

    module = _().parse_module(python2_example_module)
    expected_module = _().parse_module(get_fixture_path('python2_future.py'))

    assert astor.to_source(module) == astor.to_source(expected_module)

# Generated at 2022-06-14 01:58:05.477521
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import typed_ast.ast3 as ast
    node = ast.parse('def foo(): pass')
    new_node = Python2FutureTransformer().visit(node)
    expected = ast.parse('''
    from __future__ import (absolute_import, division, 
                            print_function, unicode_literals)


    def foo(): pass''')
    ast.fix_missing_locations(new_node)
    assert ast.dump(expected) == ast.dump(new_node)

# Generated at 2022-06-14 01:58:09.498612
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test visit_Module method of class Python2FutureTransformer"""
    import ast as pyast

    mod = pyast.parse('a = 42')
    transformer = Python2FutureTransformer()
    mod = transformer.visit(mod)
    expected = pyast.parse(imports(future='__future__'))
    expected.body.extend(pyast.parse('a = 42').body)
    assert ast.dump(mod) == ast.dump(expected)


__transformer__ = Python2FutureTransformer

# Generated at 2022-06-14 01:58:17.514823
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from typed_ast.ast3 import parse
    import textwrap

    source = textwrap.dedent(
        '''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        def func(x):
            return x
        '''
    )
    expected = imports.get_body(future='__future__') + parse(source).body
    module = parse(source)
    visitor = Python2FutureTransformer()
    visitor.visit(module)
    result = module.body
    assert astor.to_source(expected) == astor.to_source(result)

# Generated at 2022-06-14 01:58:27.653877
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """This unit test requires that the method "visit_Module" in the class
    "Python2FutureTransformer" returns a tree where the top-level node is a
    "Module" node containing a list of four "ImportFrom" nodes and the rest of
    the original tree as children.

    """
    code = '''x = 1
    y = x
    z = y
    '''
    tree = ast.parse(code)
    transformer = Python2FutureTransformer()
    new_tree = transformer.visit(tree)
    assert isinstance(new_tree, ast.Module)
    assert len(new_tree.body) == 6
    assert isinstance(new_tree.body[0], ast.ImportFrom)
    assert new_tree.body[0].module == '__future__'

# Generated at 2022-06-14 01:58:37.559413
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    m = ast.parse('name = "Earth"')
    t = Python2FutureTransformer()
    t.visit(m)

# Generated at 2022-06-14 01:58:46.281469
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test for method visit_Module of class Python2FutureTransformer
    
    """
    obj = Python2FutureTransformer()
    import astor
    src = '''
    def hello():
        x = 1 // 3
        y = {"x" : 1, "y" : 2}
        for k, v in y.items():
            print(k, v)
    '''
    tree = ast.parse(src)
    obj.visit(tree)
    print(astor.to_source(tree))
    print(obj._tree_changed)

# Generated at 2022-06-14 01:58:53.887375
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import make_test_module
    from ..utils.visitor import generate_source

    module = make_test_module(r"""
        """
    )
    module_ast = ast.parse(module)
    Python2FutureTransformer().visit(module_ast)
    assert generate_source(module_ast) == r"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
    """.lstrip()

# Generated at 2022-06-14 01:59:02.888102
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils import get_visitor_method

    transformer = Python2FutureTransformer()

    module_node = ast.parse('x = 1')
    expected_module_node = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nx = 1')

    assert get_visitor_method(transformer, module_node) == expected_module_node

# Generated at 2022-06-14 01:59:11.106052
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..bin.replacer import replace
    from ..utils.ast_helper import ast_equal, dump
    from ..utils.source_helper import source
    from ..register import get_transformer_classes

    node = ast.parse(source("""
        x = 1
    """))

    for cls in (Python2FutureTransformer, ):
        node = replace(node, get_transformer_classes([cls]))
        expected = ast.parse(source("""
            from __future__ import absolute_import
            from __future__ import division
            from __future__ import print_function
            from __future__ import unicode_literals

            x = 1
        """))

        assert ast_equal(expected, node), dump(node)

# Generated at 2022-06-14 01:59:21.346927
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .python_ast_test_case import PythonAstTestCase
    from .python_transformer_test_case import PythonTransformerTestCase

    # Arrange
    transformer = Python2FutureTransformer()
    test_case = PythonTransformerTestCase()
    test_case.source = "print(\"Hello world\")"
    test_case.expected_transformed = imports + '\nprint("Hello world")'

    # Act
    transformer.transform(test_case.source)

    # Assert
    test_case.assert_tree(transformer)
    test_case.assert_source(transformer)

# Generated at 2022-06-14 01:59:33.793342
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # GIVEN
    transformer = Python2FutureTransformer()
    tree = ast.parse("print('Hello World')")
    expected_tree = ast.parse(
        "from __future__ import absolute_import\n"
        "from __future__ import division\n"
        "from __future__ import print_function\n"
        "from __future__ import unicode_literals\n"
        "print('Hello World')\n"
    )

    # WHEN
    transformed_tree = transformer.visit(tree)

    # THEN
    assert ast.dump(expected_tree) == ast.dump(transformed_tree)

# Generated at 2022-06-14 01:59:38.331159
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert isinstance(t, BaseNodeTransformer)
    assert t.target == (2, 7)
    # If a transformer does not yet have a defined `visit_*()` method,
    # it should raise a NotImplementedError.
    node = ast.parse('1')
    try:
        t.visit(node)  # type: ignore
    except NotImplementedError:
        pass


# Generated at 2022-06-14 01:59:39.269222
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert isinstance(Python2FutureTransformer(), ast.NodeTransformer)


# Generated at 2022-06-14 01:59:44.241867
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..transformer_utils import run_on_lines
    from ..transformer_utils import PYTHON_SHEBANG
    from ..transformer_utils import assert_transformation

    code = PYTHON_SHEBANG + '\n' \
           + 'x = 1\n' \
           + 'y = 2\n'

    @assert_transformation
    def do():
        return run_on_lines(Python2FutureTransformer, code.split('\n'))


# Generated at 2022-06-14 01:59:49.278680
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import unittest
    import astor
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Python2FutureTransformerTestCase))
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    assert res.wasSuccessful()


# Generated at 2022-06-14 01:59:59.055981
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # No change for non-Python 2.7 files
    py27_code = "print('1')"
    py3 = Python3Parser()
    tree = py3.parse(py27_code)
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    assert py27_code == py3.unparse(tree)
    assert not transformer._tree_changed

    # Python 2.7 code is changed
    py2_code_before = """
# Comment line

print '2'
"""
    py2_code_after = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Comment line


print '2'
"""
    py2 = Python2Parser()

# Generated at 2022-06-14 02:00:02.370683
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('print(1)')
    arg = Python2FutureTransformer([])
    assert arg.tree_changed == False
    assert arg.visit_Module(node) is not node

# Generated at 2022-06-14 02:00:04.903163
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import typed_ast.ast3 as ast
    from typed_ast.transforms import Python2FutureTransformer


# Generated at 2022-06-14 02:00:06.601155
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Should not raise error
    assert Python2FutureTransformer  # type: ignore

# Generated at 2022-06-14 02:00:07.795808
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:00:17.532834
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse("")
    transformer = Python2FutureTransformer()
    module_transformed = transformer.visit(module)
    assert len(module_transformed.body) == 4
    assert module_transformed.body[0].names == ['absolute_import']
    assert module_transformed.body[1].names == ['division']
    assert module_transformed.body[2].names == ['print_function']
    assert module_transformed.body[3].names == ['unicode_literals']

# Generated at 2022-06-14 02:00:31.625684
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.fake import FakeFile
    from ..utils.source_code import SourceCode
    from ..utils.visitor import FakeVisitor

    source_code = SourceCode.from_string('\n'.join(['def foo():',
                                                    '    pass']))

    file_ast = ast.parse(source_code.code)

    tree_changed = False
    transformed_file_ast = Python2FutureTransformer(FakeVisitor(),
                                                    FakeFile(source_code)) \
                                                    .visit(file_ast)
    assert transformed_file_ast.body[0].lineno == 0
    assert transformed_file_ast.body[0].col_offset == 0
    assert transformed_file_ast.body[1].lineno == 0
    assert transformed_file

# Generated at 2022-06-14 02:00:36.886598
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """
    Unit test for constructor of class Python2FutureTransformer.

    """
    python2_future_transformer = Python2FutureTransformer()

    assert isinstance(python2_future_transformer, BaseNodeTransformer,
                      msg='Python2FutureTransformer is a BaseNodeTransformer')


# Generated at 2022-06-14 02:00:40.709139
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = """
a = 1
b = 2
c = a + b
print(c)
    """
    compare(code, 2, 7, expect=True, transformer=Python2FutureTransformer)

    # NOTE: asserts for Python2FutureTransformer did not work for some reason
    # I made a separate unit test for the functionality


# Generated at 2022-06-14 02:00:42.675157
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tester = Python2FutureTransformer()
    assert repr(tester) == 'Python2FutureTransformer()'

# Generated at 2022-06-14 02:00:45.757221
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert repr(transformer) == '<Python2FutureTransformer(target=(2, 7))>'



# Generated at 2022-06-14 02:00:49.583354
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer."""
    instance = Python2FutureTransformer()
    assert instance.tree_changed is False
    assert instance.visit_count == 0


# Generated at 2022-06-14 02:00:55.263061
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    
    src = """
assert a == 2
    """.strip()
    tree = ast.parse(src)
    transformer = Python2FutureTransformer()
    new_tree = transformer.visit(tree)  # type: ignore
    code_src = compile(new_tree, '<test>', 'exec')
    code_ast = ast.parse(code_src)
    assert hasattr(code_ast.body[0], 'module')
    assert 'compile' in dir(code_ast)

# Generated at 2022-06-14 02:00:58.719488
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert isinstance(x, Python2FutureTransformer)
    assert x.target == (2, 7)
    assert x.visit_Module(None)


# Generated at 2022-06-14 02:01:07.870870
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code = textwrap.dedent("""
    import os
    import sys
    from typing import Any
    from typing import Dict
    from typing import List
    from typing import Tuple
    from typing import Union
    from typing import Optional
    from typing import Set
    """)

    tree = ast.parse(code)
    new_tree = Python2FutureTransformer().visit(tree)
    new_code = astunparse.unparse(new_tree)
    # print(new_code)

# Generated at 2022-06-14 02:01:21.425110
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    lines = """
        import os
        import sys
    """
    node = ast.parse(lines)
    Python2FutureTransformer().visit(node)
    code = astor.to_source(node)
    assert code == \
        """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys""", code

# Generated at 2022-06-14 02:01:24.059628
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer
    assert transformer.target == (2, 7)
    assert transformer.code_key == 'FUTURE'


# Generated at 2022-06-14 02:01:32.366603
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:33.101562
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:01:35.095228
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():  # noqa: D103
    transformer = Python2FutureTransformer()
    # TODO: test this transformer
    pass

# Generated at 2022-06-14 02:01:40.534541
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('1 + 1')
    transformer = Python2FutureTransformer()
    transformer.visit(node)
    expected = """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

1 + 1"""
    assert expected == astor.to_sourc

# Generated at 2022-06-14 02:01:46.060142
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('''import os''')
    Python2FutureTransformer().visit(node)
    assert ast.dump(ast.parse('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        import os
    '''), annotate_fields=False) == ast.dump(node)



# Generated at 2022-06-14 02:01:50.054834
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .fixtures import code_to_ast
    from .fixtures import ast_to_code


# Generated at 2022-06-14 02:01:53.693388
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ast_transformer import ast_transformer
    from typed_ast import ast3
    import ast

    @ast_transformer(Python2FutureTransformer)
    def func(a,b):
        return a

# Generated at 2022-06-14 02:01:56.571731
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class_name = 'Python2FutureTransformer'
    my_object = Python2FutureTransformer()
    assert my_object.target == (2, 7)

# Generated at 2022-06-14 02:02:16.212490
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    expected = 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\na = 42'
    actual = astor.to_source(Python2FutureTransformer(target=(2, 7)).visit(ast.parse('a = 42')))
    assert expected == actual, 'Test failed'

# Generated at 2022-06-14 02:02:27.931631
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sql_to_python.python_transformer.transformers.python2_future_transformer
    reload(sql_to_python.python_transformer.transformers.python2_future_transformer)
    from sql_to_python.python_transformer.transformers.python2_future_transformer import Python2FutureTransformer

    transformer = Python2FutureTransformer()
    code = "def f():\n    pass\n"
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    imports_expected = "from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n"
    assert ast.dump(tree) == imports_expected + code


# Generated at 2022-06-14 02:02:29.190631
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is not None


# Generated at 2022-06-14 02:02:32.888026
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert transformer.name == 'Python 2 future'


# Generated at 2022-06-14 02:02:33.855129
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()


# Generated at 2022-06-14 02:02:41.283133
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import textwrap
    transformer = Python2FutureTransformer()
    module = textwrap.dedent("""
    class C(object):
        pass
    """)
    tree = ast.parse(module)
    transformer.visit(tree)
    assert (
        astunparse.unparse(tree) ==
        textwrap.dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        
        class C(object):
            pass
        """))



# Generated at 2022-06-14 02:02:50.994234
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import Module
    from typed_ast.ast3 import ImportFrom
    from typed_ast.ast3 import alias
    from typed_ast.ast3 import parse
    from ..utils.test_visitor import TestVisitor

    node = parse("x=3")
    new_node = Module(body=[ImportFrom(module='__future__', names=[alias(name='absolute_import', asname=None), alias(name='division', asname=None), alias(name='print_function', asname=None), alias(name='unicode_literals', asname=None),], level=0), ImportFrom(module='__future__', names=[alias(name='unicode_literals', asname=None)], level=0), *node.body,])

# Generated at 2022-06-14 02:02:55.777075
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    src = "import os\ndef f():\n    pass\n"
    before = ast.parse(src)
    after = astor.to_source(Python2FutureTransformer().visit(before))
    expected = ("from __future__ import absolute_import\n"
                "from __future__ import division\n"
                "from __future__ import print_function\n"
                "from __future__ import unicode_literals\n\n"
                "import os\n\n\n"
                "def f():\n    pass\n")
    assert after == expected

# Generated at 2022-06-14 02:03:00.630310
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Given
    node = ast.parse('print(1 + "1")')
    # When
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)
    # Then
    assert ast.dump(new_node) == ast.dump(ast.parse(imports + '\nprint(1 + "1")'))

# Generated at 2022-06-14 02:03:06.149844
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import_node = ast.ImportFrom(
        module='__future__',
        names=[
            ast.alias(name='absolute_import', asname=None),
            ast.alias(name='division', asname=None),
            ast.alias(name='print_function', asname=None),
            ast.alias(name='unicode_literals', asname=None)
        ],
        level=0
    )
    transformer = Python2FutureTransformer()
    module = ast.Module(body=[import_node])
    transformer.visit(module)
    assert len(module.body) == 5

# Generated at 2022-06-14 02:03:52.805663
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """
    Test method Python2FutureTransformer.visit_Module
    """
    with open('../data/test_python2/test_Python2FutureTransformer_visit_Module.in', 'r') as f:
        source = f.read()
    source = source.replace('\r\n', '\n')
    with open('../data/test_python2/test_Python2FutureTransformer_visit_Module.out', 'r') as f:
        expected = f.read()
    expected = expected.replace('\r\n', '\n')
    tree = astor.parse_file(
        '../data/test_python2/test_Python2FutureTransformer_visit_Module.in',
        future_imports=python2_future_imports,
    )
    tree = Python2Future

# Generated at 2022-06-14 02:03:55.629922
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer(None)
    assert x is not None


# Generated at 2022-06-14 02:04:03.519097
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_py2_body = [
        ast.Assign([
            ast.Name("x", ast.Store())
        ], [
            ast.Num(0)
        ])
    ]
    module_py2 = ast.Module(body=module_py2_body)

# Generated at 2022-06-14 02:04:13.026675
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from typed_ast import ast3 as ast
    
    class MockNode(ast.AST):
        _fields = ['body']
    
    node = MockNode(body=[])

    node_transformer = Python2FutureTransformer()
    node_transformer.visit(node)

    expected = imports.get_body(future='__future__')
    
    assert node.body == expected
    assert astor.to_source(node.body) == imports.get_source(future='__future__')

# Generated at 2022-06-14 02:04:14.604170
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert repr(Python2FutureTransformer())

# Generated at 2022-06-14 02:04:23.705295
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = textwrap.dedent("""
        def a():
            pass
    """)
    expected = textwrap.dedent("""
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        def a():
            pass
    """)
    tree = ast.parse(source)
    transf = Python2FutureTransformer()
    new_tree = transf.visit(tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:04:25.490521
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    test_module_ast = ast.parse("")
    Python2FutureTransformer().visit(test_module_ast)
    assert True

# Generated at 2022-06-14 02:04:26.967827
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 02:04:33.683982
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..utils.source import source

    @snippet
    def source():
        print('123')

    before = source.get_ast()
    # create a transformer and visit the tree
    transformer = Python2FutureTransformer()
    after = transformer.visit(before)
    # Check that the transformer has created a new tree
    assert before is not after
    # check that the imports have been inserted
    assert isinstance(after.body[0], ast.ImportFrom)
    assert after.body[0].module == '__future__'


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:04:37.224959
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, BaseNodeTransformer)


#  Unit test for the method Python2FutureTransformer.visit_Module()