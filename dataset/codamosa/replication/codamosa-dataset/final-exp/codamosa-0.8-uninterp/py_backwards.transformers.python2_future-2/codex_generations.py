

# Generated at 2022-06-14 01:55:08.910382
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    # Code before transformation
    code = '''def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()'''
    node = ast.parse(code)
    Python2FutureTransformer().visit(node)
    # Code after transformation
    # Expectation

# Generated at 2022-06-14 01:55:18.284657
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    code = """
        import sys
        import os
        print("hi")
    """
    future_import = 'from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n'
    expected = future_import + code
    tree = ast.parse(code)
    new_tree = Python2FutureTransformer().visit(tree)
    new_code = astor.to_source(new_tree)
    assert(new_code == expected)

# Generated at 2022-06-14 01:55:25.374851
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from promnesia.utils import ast_utils as U
    code = 'print("hello, world!")'
    tree = ast.parse(code)
    res = U.dump(Python2FutureTransformer().visit(tree))

    expected_code = '\n'.join(imports.get_body(future='__future__')) + '\n' + code
    expected_tree = ast.parse(expected_code)
    expected_res = U.dump(expected_tree)

    assert res == expected_res

# Generated at 2022-06-14 01:55:35.159573
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    module = ast.parse("def foo():\n    pass")
    module = transformer.visit(module)
    assert module.body[0].func.name == 'absolute_import'
    assert module.body[1].func.name == 'division'
    assert module.body[2].func.name == 'print_function'
    assert module.body[3].func.name == 'unicode_literals'
    assert module.body[4].name == 'foo'

# Generated at 2022-06-14 01:55:41.155226
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_fake_1 = ast.Module([], [])
    module_fake_2 = ast.Module([], [])
    visitor = Python2FutureTransformer()
    visitor.visit(module_fake_1)
    visitor.visit(module_fake_2)

    assert 'from __future__ import absolute_import' == str(module_fake_1.body[0]) # type: ignore

# Generated at 2022-06-14 01:55:51.684770
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Arrange
    node = ast.parse("print(2)")
    transformer = Python2FutureTransformer()

    # Act
    new_node = transformer.visit(node)
    # Assert
    print(ast.dump(new_node))

# Generated at 2022-06-14 01:55:54.494535
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    module = ast.parse("hello")
    res = Python2FutureTransformer().visit(module)
    print(ast.dump(res))

# Generated at 2022-06-14 01:56:01.182203
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    for future in ['__future__', 'future']:
        for node_str in ['node = ast.Module(body=[])',
                         'node = ast.Module(body=None)']:
            node = eval(node_str)
            new_node = Python2FutureTransformer().visit_Module(node)
            assert new_node.body  # type: ignore
            assert isinstance(new_node.body, list)  # type: ignore
            ns = imports.get_namespace(future=future)
            assert new_node.body[0].name == ns
            assert new_node.body[0].asname is None
            assert new_node.body[0].names[0].name == 'absolute_import'
            assert new_node.body[1].names[0].name == 'division'

# Generated at 2022-06-14 01:56:08.796603
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    expected_code = '''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    x += 1
    print(x)
    '''
    tree = ast.parse(expected_code)
    t = Python2FutureTransformer()
    t._apply_transformation(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code))
    assert t._tree_changed == False

# Generated at 2022-06-14 01:56:16.741351
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    class _Module(ast.Module):
        def __init__(self, body=None):
            super().__init__(body=body or [])
        def __eq__(self, other):
            return (
                isinstance(other, _Module) and
                self.body == other.body
            )
    source = _Module()
    target = _Module(body=imports.get_body(future='__future__'))
    transformed = Python2FutureTransformer.run_pipeline(source)
    assert transformed == target

# Generated at 2022-06-14 01:56:28.002199
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    module = ast.parse('print("Hello, World!")')
    module = Python2FutureTransformer().visit(module)
    assert module.body[0].value.s == 'from __future__ import absolute_import'
    assert module.body[1].value.s == 'from __future__ import division'
    assert module.body[2].value.s == 'from __future__ import print_function'
    assert module.body[3].value.s == 'from __future__ import unicode_literals'

# Generated at 2022-06-14 01:56:30.761629
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)
    assert isinstance(t, BaseNodeTransformer)


# Generated at 2022-06-14 01:56:35.229071
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    m = ast.parse("print('hello')")
    Python2FutureTransformer().visit(m)
    assert str(m) == '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print('hello')
'''

# Generated at 2022-06-14 01:56:41.288985
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source2ast

    def node2source(self, node: ast.Module) -> str:
        return astor.to_source(node)

    def convert(code: str) -> str:
        node = source2ast(code)
        for transformer in transformers:
            node = transformer.visit(node)  # type: ignore
        return node2source(node)

    code = dedent("""\
        # file: test.py
        # -*- coding: utf-8 -*-
        print("Hello, world!")
    """)

    transformers = [Python2FutureTransformer()]
    result = convert(code)

# Generated at 2022-06-14 01:56:42.843019
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is not None


# Generated at 2022-06-14 01:56:52.790366
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class Test(ast.AST):
        pass
    import_node = ast.ImportFrom(module="__future__", names=[
        ast.alias(name="absolute_import", asname=None)
    ], level=0)
    transformer = Python2FutureTransformer()
    module = ast.Module(body=[
        ast.Expression(value=ast.Str(s="hello")),
        ast.Expression(value=ast.Str(s="world"))
    ])
    new_module = transformer.visit_Module(module)
    assert isinstance(new_module.body[0], import_node)



# Generated at 2022-06-14 01:56:55.001729
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert(type(transformer) == Python2FutureTransformer)

# Generated at 2022-06-14 01:57:06.362814
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    code = "import sys"
    node = ast.parse(code)
    node = transformer.visit(node)
    actual = ast.dump(node)
    expected = "Module(body=[ImportFrom(module='future', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='future', names=[alias(name='unicode_literals', asname=None)], level=0), Import(names=[alias(name='sys', asname=None)])])"
    assert actual == expected

# Generated at 2022-06-14 01:57:13.000855
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    source = \
        """def f(x):
            y = x + 5
            return y
        """

# Generated at 2022-06-14 01:57:23.269012
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from pprint import pprint
    from ..utils.source import source_to_unicode
    from ..utils.string_py2 import StringIO
    from ..parser import FutureParser
    from ..transformer import FutureTransformer

    future = '__future__'

    code = source_to_unicode(r"""
            import os
            print("Hello, world!")
        """)
    tree = FutureTransformer().visit(FutureParser(future=future).parse(code))  # type: ignore
    with StringIO() as f:
        ast.fix_missing_locations(tree)
        tree = FutureTransformer().visit(tree)  # type: ignore
        ast.unparse(tree, f)
        new_code = f.getvalue()
    print(new_code)


# Generated at 2022-06-14 01:57:33.416709
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse(dedent('''
        example = '''))
    transformer = Python2FutureTransformer()
    transformer.visit(module)

    # Expected code
    expected = dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        example = ''')

    # Returned code
    result = compile(module, '<string>', 'exec')
    code = ''.join(line for line in result.co_consts[1].splitlines(True))

    assert expected == code

# Generated at 2022-06-14 01:57:34.778798
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()

# Generated at 2022-06-14 01:57:45.594327
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    transformer = Python2FutureTransformer()
    module: ast.Module = ast.parse('a = 1 + 2')
    expected_module: ast.Module = ast.parse('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    a = 1 + 2
    ''')
    assert transformer.visit(module) == expected_module



# Generated at 2022-06-14 01:57:47.642058
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert repr(x) == 'Python2FutureTransformer()'

# Generated at 2022-06-14 01:57:51.597628
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('print(2 + 4)')
    result = ast.parse(imports.get_source(future='__future__') + 'print(2 + 4)')
    tr = Python2FutureTransformer()
    assert tr.visit(node) == result


# Generated at 2022-06-14 01:58:01.486181
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ...testing import assert_code_equal
    from ...testing import transform_and_compile

    code = '''
    def a(): pass
    print(a())
    '''

    correct_code = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    def a(): pass
    print(a())
    """

    module = ast.parse(code, mode="exec")
    new_module = Python2FutureTransformer().visit(module)
    transformed_code = compile(new_module, "<string>", "exec")
    assert_code_equal(transformed_code, correct_code)

    transformed_code2 = transform_and_compile(code, Python2FutureTransformer)
    assert_

# Generated at 2022-06-14 01:58:11.114750
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from textwrap import dedent
    from mypy_extensions import NO_TYPE_CHECK
    from ..utils.source_snippets import CodeSnippet
    from ..utils.fixtures import source
    # Arrange
    source_object = CodeSnippet.from_string(dedent('''
        import os
        
        def main():
            print('Hello, World!')
    '''))
    expected_source = dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        import os
        
        def main():
            print('Hello, World!')
    ''')
    expected_source_object = CodeSnippet.from_

# Generated at 2022-06-14 01:58:13.199996
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    obj = Python2FutureTransformer()
    assert isinstance(obj, BaseNodeTransformer) is True
    assert obj.target == (2, 7)

# testing imports() snippet

# Generated at 2022-06-14 01:58:15.180424
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__doc__

# Generated at 2022-06-14 01:58:20.138164
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3
    module = ast3.parse('''if True:
            print ('hello, world')
        ''')
    Python2FutureTransformer(target=(2, 7)).visit(module)
    imports.get_body()  # type: ignore
    imports.get_body(future='__future__')  # type: ignore

# Generated at 2022-06-14 01:58:34.028838
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..parser import parse

    pre_code_1 = """def func():
    print(1)
    return 1
    """
    pre_code_2 = """from __future__ import absolute_import\n""" + pre_code_1
    pre_code_3 = """from __future__ import division\n""" + pre_code_2
    pre_code_4 = """from __future__ import print_function\n""" + pre_code_3
    pre_code_5 = """from __future__ import unicode_literals\n""" + pre_code_4

    code = parse(pre_code_1)
    expected_code = parse(pre_code_5)

    transformer = Python2FutureTransformer()
    transformer.visit(code)  # type: ignore

    assert_code_equal(code, expected_code)

# Generated at 2022-06-14 01:58:39.509657
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    original_tree = ast.parse('1/2\nprint("Hello World")')
    expected_tree = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\n\n1/2\nprint("Hello World")')
    xformer = Python2FutureTransformer()
    assert_equal(ast.dump(xformer.visit(original_tree)), ast.dump(expected_tree))

# Generated at 2022-06-14 01:58:48.003354
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from textwrap import dedent
    from typed_ast import ast3 as ast
    from typed_ast.ast3 import Module

    source = dedent("""\
    a = 1
    print(a)
    """)

    expected = dedent("""\
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    a = 1
    print(a)
    """)

    module: Module = ast.parse(source)
    module = Python2FutureTransformer().visit(module)
    assert ast.dump(module) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 01:58:49.429403
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

# Generated at 2022-06-14 01:58:52.062768
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    from python_transformer.unparse_visitor import UnparseVisitor
    import ast

# Generated at 2022-06-14 01:59:05.705129
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test a function that prepends module with:
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    from ..utils.snippet import snippet
    """
    import_future_transformer = Python2FutureTransformer()
    module = ast.parse(
        textwrap.dedent("""\
        import os
        import sys
        import ast
        """))
    import_future_transformer.visit(module)

# Generated at 2022-06-14 01:59:07.212701
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().target == (2, 7)

# Generated at 2022-06-14 01:59:11.087673
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    trans = Python2FutureTransformer()
    assert trans.target is None
    assert trans._tree_changed is False
    import copy
    from . import sample
    from . import sample_expected
    node = copy.deepcopy(sample.node)
    node_expected = copy.deepcopy(sample_expected.node)
    trans.visit(node)
    assert trans._tree_changed is True
    assert node == node_expected

# Generated at 2022-06-14 01:59:12.539526
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:59:24.738463
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from ..transforms import TransformManager
    from ..ast import Py2FutureVisitor
    from ..utils.test_utils import run_test_ast_transform
    manager = TransformManager()
    manager.register(Python2FutureTransformer)
    visitor = Py2FutureVisitor(manager)
    visitor.setup()

    source = inspector.SourceInspector(None, '<test>', '0 / 1')
    visitor.visit(source.ast)
    expected = ("from __future__ import absolute_import\n"
                "from __future__ import division\n"
                "from __future__ import print_function\n"
                "from __future__ import unicode_literals\n"
                "\n"
                "0 / 1\n")
    assert source.source == expected

# Generated at 2022-06-14 01:59:33.961001
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer  # Using just to pyflakes


# Generated at 2022-06-14 01:59:40.460492
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = """num=1\nprint(num)"""
    node = ast.parse(code, '', 'exec')
    node = Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 01:59:41.428364
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer(): # test: no cover
    assert Python2FutureTransformer.__doc__ is not None

# Generated at 2022-06-14 01:59:42.731319
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    # Before

# Generated at 2022-06-14 01:59:46.720794
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import future_module
    module = future_module.get_ast()
    transformer = Python2FutureTransformer()
    transformer.visit(module)
    future_module.assert_equivalent(module)


# Generated at 2022-06-14 01:59:54.455878
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_node: ast.Module = ast.parse('', '<string>', 'exec')
    transformer = Python2FutureTransformer(module_node)
    module_node = transformer.visit(module_node)
    assert transformer.tree_changed

    # check the result
    from astmonkey.transformers.code_generator import CodeGenerator
    code_generator = CodeGenerator()
    code = code_generator.visit(module_node)
    assert code == """from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
"""

# Generated at 2022-06-14 01:59:57.475532
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    a = ast.parse('def a(): pass').body[0]
    transformer = Python2FutureTransformer()
    transformer.visit(a)
    assert transformer._tree_changed



# Generated at 2022-06-14 02:00:00.691559
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from . import parse
    t = Python2FutureTransformer()
    tree = parse('''
    print("Hello world!")
    ''')
    assert tree == t.visit(tree)

# Generated at 2022-06-14 02:00:03.932256
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Test if the class Python2FutureTransformer initializes correctly
    """
    trans = Python2FutureTransformer()
    assert trans.target == (2, 7)
    assert trans._tree_changed == False

# Generated at 2022-06-14 02:00:06.699070
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast

    # Creating a Module node
    module = ast.Module(body=[])

    # Creating a Python2FutureTransformer object for the module
    trans = Python2FutureTransformer(module)

# Generated at 2022-06-14 02:00:27.109793
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_import_inliner import TestImportInliner
    from base64 import b64encode

# Generated at 2022-06-14 02:00:28.926224
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert isinstance(Python2FutureTransformer(), Python2FutureTransformer)

# Generated at 2022-06-14 02:00:30.216984
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()._tree_changed == False

# Generated at 2022-06-14 02:00:38.527853
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    code = """
#!/usr/bin/python
"""
    tree = ast.parse(code, filename='', mode='exec')
    Python2FutureTransformer().visit(tree)
    new_code = compile(tree, filename="<ast>", mode="exec")
    scope = dict()
    exec(new_code, scope)
    assert scope['future'].__doc__ == '__future__ is an interface to advanced language features which are not yet available by default, but may be scheduled to become standard in a subsequent Python release.'
    assert scope['absolute_import'].__doc__ == 'Enables absolute imports, e.g.: from foo import bar instead of from .foo import bar.'
    assert scope['division'].__doc__ == 'Enables normal division: 3/4 is 0.75, and not 0 as in Python 2.'

# Generated at 2022-06-14 02:00:42.803056
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert not transformer._tree_changed
    assert transformer.visit_Module(ast.parse("x"))



# Generated at 2022-06-14 02:00:53.265177
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tree = ast.parse(
        'def foo():\n'
        '    pass'
    )
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    ref = ast.parse(
        'from __future__ import absolute_import\n'
        'from __future__ import division\n'
        'from __future__ import print_function\n'
        'from __future__ import unicode_literals\n'
        'def foo():\n'
        '    pass'
    )
    assert transformer._tree_changed == True
    assert ast.dump(tree) == ast.dump(ref)

# Generated at 2022-06-14 02:00:55.104356
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert isinstance(x, Python2FutureTransformer)


# Generated at 2022-06-14 02:01:05.682903
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast
    import textwrap
    sample_code = textwrap.dedent('''
        import os
        
        print('hello')
    ''')
    tree = ast.parse(sample_code)
    t = Python2FutureTransformer()
    t.visit(tree)
    result = ast.dump(tree)

# Generated at 2022-06-14 02:01:12.672855
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse('class TestClass:\n    pass')
    tree = Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 02:01:14.826131
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    parser = ast.parse
    tree = parser("print('Hello world!')")
    r = Python2FutureTransformer()
    new_tree = r.visit(tree)
    assert new_tree is not None

# Generated at 2022-06-14 02:01:47.938546
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)
    Python2FutureTransformer()

# Generated at 2022-06-14 02:01:51.248465
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert isinstance(t, BaseNodeTransformer)
    

# Generated at 2022-06-14 02:01:53.105608
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.target == (2, 7)

# Generated at 2022-06-14 02:01:59.486664
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    node = ast.parse("import sys; print ('hi')")
    node = transformer.visit(node)
    expected = ast.parse(imports.get_snippet(future='__future__') + 'import sys; print(\'hi\')')
    assert ast.dump(node) == ast.dump(expected)

# Generated at 2022-06-14 02:02:06.651550
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast.ast3 import Module
    from ..utils.fixtures import future_future
    from ..utils.source import Source
    from ..transformers import Python2FutureTransformer
    import typing

    source = Source(future_future)
    module = source.ast  # type: Module
    assert isinstance(module, Module)
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)  # type: typing.Any
    assert isinstance(module, Module)

# Generated at 2022-06-14 02:02:17.144950
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ...testing import run_module_suite
    from ...testing.utils import get_visitor_output
    from ..utils.transformtesting import assert_equal_node
        
    module = ast.parse("""
        import os
        import sys
    """)

    # get_visitor_output
    output = get_visitor_output(module, Python2FutureTransformer)
    module_future = output['module']

    # Expected output
    module_future_expected = ast.parse("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import os
    import sys
    """)

    assert_equal_node(module_future_expected, module_future)

# Generated at 2022-06-14 02:02:18.313963
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    x = Python2FutureTransformer()
    assert x.target == (2, 7)

# Generated at 2022-06-14 02:02:29.361619
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from nuitka.nodes.AssignNodes import ExpressionTargetTempVariableRef
    from nuitka.nodes.BuiltinRefNodes import ExpressionBuiltinImport
    from nuitka.nodes.VariableRefNodes import ExpressionTargetVariableRef
    from nuitka.nodes.ConstantRefNodes import ExpressionConstantRef
    from nuitka.nodes.ComparisonNodes import ExpressionComparisonIs
    from nuitka.nodes.OperatorNodes import ExpressionOperationBinary
    from nuitka.nodes.ConditionalNodes import ExpressionConditional
    from nuitka.tree.ReformulationTryExceptStatements import makeTryExceptNode
    from nuitka.tree.ReformulationTryFinallyStatements import makeTryFinallyNode
    from nuitka.tree.ReformulationWithStatements import makeTryFinallyNode

# Generated at 2022-06-14 02:02:40.703806
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import unittest
    import typed_ast.ast3 as ast3
    from flake8_typing_imports.transforms import Python2FutureTransformer

    class Test(unittest.TestCase):
        def test_visit_Module(self):
            tree = ast3.parse("print('Hello')")
            transformer = Python2FutureTransformer()
            tree = transformer.visit(tree)

            assert transformer._tree_changed
            assert isinstance(tree, ast3.Module)
            assert isinstance(tree.body[0], ast3.ImportFrom)
            assert isinstance(tree.body[1], ast3.Expr)
            assert isinstance(tree.body[1].value, ast3.Call)
            assert isinstance(tree.body[1].value.func, ast3.Name)

# Generated at 2022-06-14 02:02:44.071439
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('pass')
    Python2FutureTransformer().visit(module)
    assert ast.dump(module, 'exec') == 'exec(imports(\'__future__\'))\npass'

# Generated at 2022-06-14 02:04:03.520720
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('print(2)')
    Python2FutureTransformer.run(node)

# Generated at 2022-06-14 02:04:07.356762
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)
    assert t.description is not None
    assert t.description != ''



# Generated at 2022-06-14 02:04:08.970792
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .. import transform


# Generated at 2022-06-14 02:04:10.131937
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()

# Generated at 2022-06-14 02:04:13.103503
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import parse
    tree = parse("print('Hello World')\n")
    Python2FutureTransformer().visit(tree)

# Generated at 2022-06-14 02:04:15.016069
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    instance = Python2FutureTransformer()
    assert(instance)

# Generated at 2022-06-14 02:04:15.925346
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 02:04:21.741625
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    ast_m = astor.parse_file('../tests/data/simple_program_python2.py')
    transformer = Python2FutureTransformer()
    transformer.visit(ast_m)

# Generated at 2022-06-14 02:04:24.114156
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    try:
        _ = Python2FutureTransformer()
        assert True == True # Unit test passed
    except:
        assert True == False # Unit test failed
        

# Generated at 2022-06-14 02:04:31.144473
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    tree = astor.parse_file('tests/fixtures/python2_module.py')
    tree = transformer.visit(tree)
    assert transformer._tree_changed is True
    assert astor.to_source(tree, False, False) == (
        "from __future__ import absolute_import\n"
        "from __future__ import division\n"
        "from __future__ import print_function\n"
        "from __future__ import unicode_literals\n\n"
        "def my_func(x):\n"
        "    print(x)\n"
    )