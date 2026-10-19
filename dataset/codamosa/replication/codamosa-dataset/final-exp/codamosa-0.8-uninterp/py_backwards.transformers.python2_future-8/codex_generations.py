

# Generated at 2022-06-14 01:55:05.843561
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:55:09.759188
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.helper import parsed_snippet 
    assert parsed_snippet(imports.get_body(future='__future__')) == Python2FutureTransformer.visit_Module(Python2FutureTransformer(), ast.parse(''))

# Generated at 2022-06-14 01:55:19.718009
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    src = dedent('''
        def func():
            return 1
    ''')
    expected = dedent('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        def func():
            return 1
    ''')

    actual = transformer.visit_Module(ast.parse(src))
    assert transformer._tree_changed is True
    assert ast.dump(actual) == expected

# Generated at 2022-06-14 01:55:24.201794
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse('print("hello")')
    transformer = Python2FutureTransformer()
    transformer.visit(module)
    assert str(module) == 'from __future__ import absolute_import, division, print_function, unicode_literals\nprint("hello")'

# Generated at 2022-06-14 01:55:26.457303
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Case 1: simple module
    transformer = Python2FutureTransformer()

# Generated at 2022-06-14 01:55:40.934196
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from textwrap import dedent
    from .python2 import python2
    import os
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test_data', 'main.py')
    with open(file_path, 'rb') as f:
        root_node = ast.parse(f.read())
    Python2FutureTransformer.run(root_node)

# Generated at 2022-06-14 01:55:46.907273
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .utils import roundtrip

    code = """def myfunction():
    pass"""

    tree = ast.parse(code)
    trans = Python2FutureTransformer()
    trans.visit(tree)
    new_source = roundtrip(tree)

# Generated at 2022-06-14 01:55:55.454408
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import parse
    from test.test_transpilers.utils import assert_equal_src
    from .base import get_visitor
    with open('./test/test_transpilers/test_transformers.py', 'r') as tt:
        source = tt.readlines()  # type: ignore

    assert_equal_src(
        expected=source[:23],
        actual=get_visitor(
            visitor=Python2FutureTransformer,
            version=(2, 7)
        ).visit(parse(
            source=''.join(source)
        )).body,
        compare_lineno=True
    )

# Generated at 2022-06-14 01:55:59.841250
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.ast_helpers import parse_module

    module = parse_module('print("Hello")')
    assert isinstance(module, ast.Module)
    result = Python2FutureTransformer().visit(module)
    assert isinstance(result, ast.Module)



# Generated at 2022-06-14 01:56:02.633297
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_base import BaseNodeTransformerTest
    class Mock_Python2FutureTransformer(Python2FutureTransformer, BaseNodeTransformerTest):
        pass
    return Mock_Python2FutureTransformer(__file__)

# Generated at 2022-06-14 01:56:08.651789
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()
    program_node = ast.parse("""
x = True
""")
    new_program_node = transformer.visit(program_node)

    assert new_program_node is not program_node
    assert transformer._tree_changed

    assert transformer.result == """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = True"""

# Generated at 2022-06-14 01:56:16.998736
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import Module

    tree = Module(body=[])
    transformer = Python2FutureTransformer()

    code = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
    """
    node = transformer.visit(tree)  # type: ignore
    assert node._fields == ('body',)
    assert len(node.body) == 4
    expected = ast.parse(code)
    assert ast.dump(node.body) == ast.dump(expected.body)

# Generated at 2022-06-14 01:56:21.439579
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    assert_equal(
        Python2FutureTransformer().visit(ast.parse("")),
        ast.parse('''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
'''))

# Generated at 2022-06-14 01:56:22.830773
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:32.605738
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    code = '''
print("hello world")
'''
    node = ast.parse(code)
    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    expected_code = '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


print("hello world")
'''
    expected_node = ast.parse(expected_code)
    assert ast.dump(new_node) == ast.dump(expected_node)
    assert transformer.tree_changed()

# Unit tests for module Python2FutureTransformer

# Generated at 2022-06-14 01:56:38.331868
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    code_snippet = """\
x = 2
y = 3
z = x + y
"""
    expected_code_snippet = """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
x = 2
y = 3
z = x + y
"""
    tree = ast.parse(code_snippet)
    transformer = Python2FutureTransformer()
    tree = transformer.visit(tree)
    assert ast.dump(tree) == ast.dump(ast.parse(expected_code_snippet))

# Generated at 2022-06-14 01:56:48.185231
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    target = (2, 7)
    py2_future_transformer = Python2FutureTransformer(target=target)
    assert py2_future_transformer._tree_changed == False
    module_node = ast.Module(body=[])
    py2_future_transformer._visit_body = mock.Mock()

    py2_future_transformer.visit_Module(module_node)
    assert py2_future_transformer._tree_changed == True

    py2_future_transformer._visit_body.assert_called_once_with(module_node.body)


# Generated at 2022-06-14 01:57:01.134010
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from tests.unit.utils_for_tests import dedent
    from ..utils.snippet import snippet
    from .base import BaseNodeTransformer

    @snippet
    def imports(future):
        from future import absolute_import
        from future import division
        from future import print_function
        from future import unicode_literals


    class Python2FutureTransformer(BaseNodeTransformer):
        """Prepends module with:
            from __future__ import absolute_import
            from __future__ import division
            from __future__ import print_function
            from __future__ import unicode_literals
            
        """
        target = (2, 7)

        def visit_Module(self, node: ast.Module) -> ast.Module:
            self._tree_changed = True
           

# Generated at 2022-06-14 01:57:08.347515
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    transformer = Python2FutureTransformer()

    actual = transformer.visit_Module(ast.parse("print('this is a string')"))
    desired = ast.Module(body=imports.get_body(future='__future__') + [ast.Expr(value=ast.Call(
        func=ast.Name(id='print', ctx=ast.Load()),
        args=[ast.Str(s="'this is a string'")],
        keywords=[]))])  # type: ignore
    assert ast.dump(desired) == ast.dump(actual)

# Generated at 2022-06-14 01:57:18.886541
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = source_for_test(Python2FutureTransformer)
    module_tree = parse(source)
    Python2FutureTransformer().visit(module_tree)
    output = unparse(module_tree)
    assert output == dedent("""\
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals


        def __fake():
            abs = 2
            div = 1 / 2
            print("hello")
            name = "Ada"


        target = (2, 7)


        class A(object):
            def __init__(self, a={1}):
                self.a = a
        """)

# Generated at 2022-06-14 01:57:29.690399
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """Test visit_Module method of class Python2FutureTransformer."""
    test_ast = ast.parse("")
    expected_ast = ast.parse("""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
""")
    Python2FutureTransformer().visit(test_ast)
    assert ast.dump(test_ast) == ast.dump(expected_ast)

# Generated at 2022-06-14 01:57:38.386625
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    node0 = ast.parse("""
print("Hello, World!")
""").body
    node1 = ast.parse("""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print("Hello, World!")
""").body

    node = ast.Module(body=node0)

    tf = Python2FutureTransformer()
    tf.visit(node)

    assert node.body == node1

# Generated at 2022-06-14 01:57:50.848986
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    # Transformer class
    transformer = Python2FutureTransformer()
    # Module snippet
    module = 'import os'
    # Make AST
    module_ast = ast.parse(module)
    # Transform
    module_ast = transformer.visit(module_ast)
    # Check
    module_str = astor.to_source(module_ast)
    assert 'from __future__ import absolute_import' in module_str
    assert 'from __future__ import division' in module_str
    assert 'from __future__ import print_function' in module_str
    assert 'from __future__ import unicode_literals' in module_str

# Generated at 2022-06-14 01:57:59.040732
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    expected_source = """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

x = 1
""".strip()
    source = """
x = 1
""".strip()
    module = ast.parse(source)
    expected_module = ast.parse(expected_source)
    transformer = Python2FutureTransformer()
    module = transformer.visit(module)
    assert ast.dump(expected_module, include_attributes=True) == ast.dump(module, include_attributes=True)

# Generated at 2022-06-14 01:58:05.005327
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor

    # Create a Python2FutureTransformer and call visit_Module
    transformer = Python2FutureTransformer()
    tree = ast.parse('x = 1')
    new_tree = transformer.visit_Module(tree)

    # Test that visit_Module returns the correct value
    assert astor.to_source(new_tree) == imports.get_source(future='__future__') + 'x = 1'



# Generated at 2022-06-14 01:58:11.033956
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    module = ast.parse("""
    print('hello world')
    """)
    expected_module = ast.parse("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    print('hello world')
    """)
    Python2FutureTransformer(module).visit(module)
    assert astor.to_source(module) == astor.to_source(expected_module)

# Generated at 2022-06-14 01:58:18.794567
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.Module(
        body=[
            ast.Import(
                names=[
                    ast.alias(
                        name='os',
                        asname=None,
                    ),
                ],
            ),
        ],
    )
    transformer = Python2FutureTransformer(target=(2, 7))
    new_node = transformer.visit(node)
    assert new_node.body[0].names[0].name == 'absolute_import'
    assert new_node.body[1].names[0].name == 'division'
    assert new_node.body[2].names[0].name == 'print_function'
    assert new_node.body[3].names[0].name == 'unicode_literals'
    assert new_node.body[4].names[0].name == 'os'

# Generated at 2022-06-14 01:58:27.249770
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    from .helper import get_module_as_module
    from .helper import get_func_as_func

    from typed_ast.ast3 import Module, FunctionDef, parse
    from typed_ast import ast3 as ast

    # Create a module
    module = ast.parse(
        """
        class A():
            pass
    """)
    # Check that we have only one import
    assert len(module.body) == 1
    # Transform the module
    transformer = Python2FutureTransformer()
    ret = transformer.visit(module)
    # Check the length of body
    assert len(ret.body) == 5



# Generated at 2022-06-14 01:58:36.901122
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source_code import SourceCode
    code = SourceCode("""
    class MyClass:
        pass
    
    if __name__ == '__main__':
        my_instance = MyClass()
        print(my_instance)
    """)
    module = Python2FutureTransformer().visit(code.tree)
    assert str(module).replace("\n", "").strip() == \
           "from future import absolute_import;from future import division;" \
           "from future import print_function;from future import unicode_literals;" \
           "class MyClass:\n\tpass\n\nif __name__ == '__main__':\n" \
           "\tmy_instance = MyClass()\n\tprint(my_instance)"

# Generated at 2022-06-14 01:58:44.649240
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..ast_transformer import AstTransformer
    from ..examples.module_1_simple import module_1_simple_ast

    transformer = AstTransformer(module_1_simple_ast)
    transformer.add_transformer(Python2FutureTransformer())
    new_module = transformer.transform()

    import astor
    astor.dump_tree(new_module)
    print(astor.code_gen.to_source(new_module))

# Generated at 2022-06-14 01:59:08.801750
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('a = 1.0')
    t = Python2FutureTransformer()
    t(node)
    assert t._tree_changed == True

# Generated at 2022-06-14 01:59:22.077889
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .base import BaseNodeTransformer
    from ..utils.snippet import snippet

    @snippet
    def node(future):
        class Foo:
            pass
        print('hello')
        for i in range(10):
            print(i)

    node = ast.parse(node.get_source())

    transformer = Python2FutureTransformer()
    new_node = transformer.visit(node)

    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import node_test_util
    print(node_test_util.format_diff(node, new_node))
    assert node != new_node
    assert transformer.tree_changed


# Generated at 2022-06-14 01:59:32.613488
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse(dedent('''
    import sys
    import re
    '''))
    Python2FutureTransformer().visit(node)
    assert len(node.body) == 6
    assert node.body[0].names[0].name == '__future__'
    assert node.body[0].names[0].asname is None
    assert node.body[1].names[0].name == 'absolute_import'
    assert node.body[1].names[0].asname is None
    assert node.body[2].names[0].name == 'division'
    assert node.body[2].names[0].asname is None
    assert node.body[3].names[0].name == 'print_function'
    assert node.body[3].names[0].asname is None
    assert node

# Generated at 2022-06-14 01:59:36.716861
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)
    assert isinstance(transformer, Python2FutureTransformer)


# Generated at 2022-06-14 01:59:47.119473
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Test that Python2FutureTransformer prepends module with:
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
    """
    module = ast.parse('import abc\n')
    result = ast.parse('from __future__ import absolute_import\nfrom __future__ import division\nfrom __future__ import print_function\nfrom __future__ import unicode_literals\nimport abc\n')
    Python2FutureTransformer().visit(module)
    assert ast.dump(module) == ast.dump(result)

# Generated at 2022-06-14 01:59:52.011004
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse(
        '''def __init__():
        pass
''')
    result = Python2FutureTransformer().visit(node)

# Generated at 2022-06-14 02:00:03.397292
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .context import Context
    from .python2 import Python2Transformer
    from .python3 import Python3Transformer
    from ..core.preparser import PreParser
    from ..core.visitor import Visitor
    from .unused_variables import UnusedVariablesTransformer
    from .whitespace import WhitespaceTransformer
    from ..migrations.python_27_to_python_35.python_27_asyncio import Python27AsyncioTransformer
    from ..migrations.python_27_to_python_35.python_27_builtins import Python27BuiltinsTransformer
    context = Context(target=(2, 7))
    context = PreParser(context).visit()
    context = Python3Transformer(context).visit()
    context = Python2Transformer(context).visit()
    context = Python27

# Generated at 2022-06-14 02:00:08.127178
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    root = ast.parse('def foo():\n    print(5 / 2)')
    trans = Python2FutureTransformer()
    trans.visit(root)
    assert ast.dump(root) == """(Module (FunctionDef (
    name foo params return) (
        Print (
            Str print (BinOp (Num 5) (Num 2) Div)) nl))
)"""



# Generated at 2022-06-14 02:00:18.830367
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from regraph.utils import get_node

    # Create a future node
    future = ast.Module([], [
        ast.ImportFrom(
            module="__future__",
            names=[ast.alias(name="absolute_import")],
            level=0
        ),
    ])

    # Create a new module that does not include the future node

# Generated at 2022-06-14 02:00:32.502148
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    cell = {'cell_type': 'code',
            'metadata': {},
            'source': 'print("Hello")',
            'outputs': [],
            'execution_count': 2}
    old = 'print("Hello")'
    new = imports.get_body(future='__future__') + [ast.parse(old).body[0]]

    trans = Python2FutureTransformer(cell)
    trans.visit(ast.parse(old))
    res = trans.cell
    assert res['cell_type'] == cell['cell_type']
    assert res['metadata'] == cell['metadata']
    assert res['execution_count'] == cell['execution_count']
    assert res['outputs'] == cell['outputs']

# Generated at 2022-06-14 02:00:54.982618
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    import textwrap
    source = textwrap.dedent(r'''
    def spam():
        pass
    ''')
    module = astor.parse_file(io.StringIO(source))
    transformer = Python2FutureTransformer()
    module_ = transformer.visit(module)
    assert isinstance(module_, ast.Module)
    assert astor.to_source(module_) == textwrap.dedent(r'''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def spam():
        pass''')

# Generated at 2022-06-14 02:00:55.654906
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:00:56.736152
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:00:57.365679
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 02:01:05.532922
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from qlckh.snippet import snippet
    assert snippet.get_body(future='__future__') == [ast.ImportFrom(module='__future__',
                                                                    names=[
                                                                    ast.alias(name='absolute_import', asname=None),
                                                                    ast.alias(name='division', asname=None),
                                                                    ast.alias(name='print_function', asname=None),
                                                                    ast.alias(name='unicode_literals', asname=None)
                                                                    ],
                                                                    level=0)
                                                    ]

# Generated at 2022-06-14 02:01:07.599613
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None).__class__.__name__ == "Python2FutureTransformer"

# Generated at 2022-06-14 02:01:12.590919
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Test of constructor of Python2FutureTransformer.
    """
    transformer = Python2FutureTransformer(raise_exception=True)
    assert isinstance(transformer, Python2FutureTransformer)

# Generated at 2022-06-14 02:01:20.298685
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    inputs = [
        """import sys""",
        """def foo(x): return x""",
    ]

# Generated at 2022-06-14 02:01:29.545305
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .base import BaseNodeTransformer
    from .context import NodeTransformerContext

    class TmpNodeTransformer(BaseNodeTransformer):
        pass

    assert Python2FutureTransformer(context=NodeTransformerContext(in_place=True)).__class__ == Python2FutureTransformer
    assert Python2FutureTransformer(context=NodeTransformerContext(in_place=False)).__class__ == Python2FutureTransformer
    assert Python2FutureTransformer(context=NodeTransformerContext(in_place=True), target=TmpNodeTransformer.target).__class__ == Python2FutureTransformer
    assert Python2FutureTransformer(context=NodeTransformerContext(in_place=False), target=TmpNodeTransformer.target).__class__ == Python2FutureTransformer

# Generated at 2022-06-14 02:01:35.128257
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from six import exec_
    x = ast.parse("assert 1 == 1")
    y = x
    Python2FutureTransformer(2, 7).visit(y)
    assert y.body[0].lineno == x.body[0].lineno, "Failed to transform module test_Python2FutureTransformer in class Py2Future"
    assert isinstance(y.body[0], ast.Assert), "Failed to transform module test_Python2FutureTransformer in class Py2Future"
    assert isinstance(y.body[1], ast.ImportFrom), "Failed to transform module test_Python2FutureTransformer in class Py2Future"

# Generated at 2022-06-14 02:01:51.690379
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    for pyversion in Python2FutureTransformer.target:
        assert Python2FutureTransformer('pass', pyversion=pyversion)._tree_changed


# Generated at 2022-06-14 02:02:02.618087
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import sys

    import_node = ast.ImportFrom(
        module='__future__',
        names=[
            ast.alias(name='absolute_import', asname=None),
            ast.alias(name='division', asname=None),
            ast.alias(name='print_function', asname=None),
            ast.alias(name='unicode_literals', asname=None),
        ],
        level=0,
    )

    node = ast.Module(
        body=[
            ast.FunctionDef(
                name='test',
                args=ast.arguments(args=[], vararg=None, kwarg=None, defaults=[]),
                body=[],
                decorator_list=[],
                returns=None,
            ),
        ]
    )

    transformer = Python2FutureTransformer()
    transformer

# Generated at 2022-06-14 02:02:03.668432
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:02:10.709660
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_pipeline import _test_transform
    _test_transform(Python2FutureTransformer, '''
    print('Hello world!')
''', '''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print('Hello world!')
''')

# Generated at 2022-06-14 02:02:17.956595
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import make_fixtures  # type: ignore

    # Create fixtures
    make_fixtures(__file__, globals())

    # Perform transformations
    Python2FutureTransformer(None).visit(module_node)  # type: ignore

    # Check results
    # FIXME: this is not perfect, but close
    # module_result = inspect.getsource(module)
    module_result = ast.parse(module_source)
    assert ast.dump(module_node, include_attributes=False) == ast.dump(module_result, include_attributes=False)

# Generated at 2022-06-14 02:02:25.476833
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__doc__


if __name__ == '__main__':
    # Unit test
    config_logging(level=logging.DEBUG)
    default_test_file = inspect.getfile(inspect.currentframe())
    test_file = input('Enter test file name ({}): '.format(default_test_file)) or default_test_file
    with open(test_file, 'r') as f:
        code = f.read()
    print('Original code:\n{}'.format(code))
    print('Transformed code:\n{}'.format(Python2FutureTransformer().transform_source(code)))

# Generated at 2022-06-14 02:02:31.810057
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from typing import List
    transformer = Python2FutureTransformer([])
    module = ast.Module([])
    module = transformer.visit(module)
    assert isinstance(module, ast.Module), "visit_Module of Python2FutureTransformer doesn't return ast.Module"
    assert isinstance(module.body, List), "visit_Module of Python2FutureTransformer doesn't set ast.Module body"
    for item in module.body:
        assert isinstance(item, ast.ImportFrom)

# Generated at 2022-06-14 02:02:33.945670
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    r = Python2FutureTransformer().visit(ast.parse('xyzzy'))
    expected = ast.parse('''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
xyzzy''')
    assert ast.dump(r) == ast.dump(expected)

# Generated at 2022-06-14 02:02:39.288930
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    _future = ast.parse(imports.get_body(future='__future__'))
    _module = ast.parse('x=2')
    _module.body = _future.body + _module.body
    with Python2FutureTransformer() as t:
        _node = t.visit(_module)
    
    assert ast.dump(_node) == ast.dump(_module)

# Generated at 2022-06-14 02:02:43.125236
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    class_ = Python2FutureTransformer()
    assert(class_._tree_changed == False)
    assert(isinstance(class_, BaseNodeTransformer))
    assert(isinstance(class_, ast.NodeTransformer))

# Generated at 2022-06-14 02:03:26.644038
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import setup_test_environment

    module = setup_test_environment.setup_module('future.builtins', 'future.standard_library')

    tree = ast.parse(module)
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    ast.fix_missing_locations(tree)

    assert transformer._tree_changed == True
    assert isinstance(tree.body[0], ast.ImportFrom)
    assert tree.body[0].module == '__future__'
    assert tree.body[0].names[0].name == 'unicode_literals'
    assert tree.body[0].level == 0

# Generated at 2022-06-14 02:03:28.076674
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 02:03:35.186383
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..transpile import transpile
    source = """\
    import os
    import sys

    def func(param):
        pass
    """
    expected = """\
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import os
    import sys

    def func(param):
        pass
    """
    module = ast.parse(source)
    module = Python2FutureTransformer().visit(module)  # type: ignore
    assert transpile(module) == expected

# Generated at 2022-06-14 02:03:36.914210
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer
    

# Generated at 2022-06-14 02:03:38.449890
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:03:40.885135
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == 'Python2FutureTransformer'
    assert Python2FutureTransformer.target == (2, 7)


# Generated at 2022-06-14 02:03:53.156270
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('a = 1')
    Python2FutureTransformer().visit(node)

    assert ast.dump(node) == "Module(body=[ImportFrom(module='__future__', names=[alias(name='absolute_import', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='division', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='print_function', asname=None)], level=0), ImportFrom(module='__future__', names=[alias(name='unicode_literals', asname=None)], level=0), Expr(value=BinOp(left=Name(id='a', ctx=Load()), op=Add(), right=Num(n=1)))])\n"

# Unit test

# Generated at 2022-06-14 02:03:59.721949
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils import run_python_module
    source = """\
if __name__ == '__main__':
    print(4/2)
    print(4//2)
"""
    out, err, exitcode = run_python_module(Python2FutureTransformer.run, source)
    assert out == '2.0\n2\n'
    assert err == ''
    assert exitcode == 0

# Generated at 2022-06-14 02:04:12.467207
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from ..utils.ast_utils import assert_same_ast
    from .base import BaseNodeTransformer
 
    @snippet
    def source():
        pass

    # Expect this
    @snippet
    def expected():
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals
        pass

    source_ast = source.get_ast()
    expected_ast = expected.get_ast()
    
    transformer = Python2FutureTransformer()
    transformed_ast = transformer.visit(source_ast)
    assert_same_ast(expected_ast, transformed_ast)
    print('Success')

# Generated at 2022-06-14 02:04:13.065696
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer(): pass