

# Generated at 2022-06-14 01:55:11.410095
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Arrange
    text = '# coding: utf-8\nimport os'
    node = ast.parse(text)
    
    # Act
    p = Python2FutureTransformer()
    new_node = p.visit(node)
    updated_text = astor.to_source(new_node)

    # Assert
    assert p.tree_changed() is True
    assert 'from __future__ import absolute_import' in updated_text
    assert 'from __future__ import division' in updated_text
    assert 'from __future__ import print_function' in updated_text
    assert 'from __future__ import unicode_literals' in updated_text



# Generated at 2022-06-14 01:55:12.540944
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:55:17.680684
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    expected = ast.Module(
        imports.get_body(future='__future__'), 
        []
    )

    actual = ast.parse("pass")
    actual = Python2FutureTransformer.visit(actual)
    assert ast.dump(expected) == ast.dump(actual)

# Generated at 2022-06-14 01:55:25.339963
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # Tests that Python2FutureTransformer adds the imports properly
    code = '''import abc
import collections'''

    expected_code = '''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc
import collections
'''
    tree = ast.parse(code)
    tr = Python2FutureTransformer()
    tree = tr.visit(tree)
    assert astor.to_source(tree) == expected_code

# Generated at 2022-06-14 01:55:29.151319
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    # Construct Python2FutureTransformer
    transformer = Python2FutureTransformer()
    # Test __init__
    assert transformer.name == "Python2FutureTransformer"
    assert transformer.target == (2, 7)
    assert transformer.future == "__future__"
    # Test _tree_changed
    assert transformer._tree_changed == False


# Generated at 2022-06-14 01:55:35.284669
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from textwrap import dedent
    import ast

    from typed_astunparse import unparse

    from ast_tools.visitors import ast2 as ast2
    from ast_tools.visitors import ast3 as ast3
    from ast_tools.visitors.base import BaseNodeTransformer

    class OldNodeTransformer(BaseNodeTransformer):
        """docstring"""
        target = (2, 7)

    class NewNodeTransformer(OldNodeTransformer):
        target = (3, 6)

    # Module
    source = dedent('''
    def foo():
        pass
    ''')
    tree = ast.parse(source)
    tree_old = ast2.to_old_syntax(tree)
    tree_new = ast3.to_new_syntax(tree)


# Generated at 2022-06-14 01:55:40.112868
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    def check_future(node):
        assert isinstance(node, ast.ImportFrom) and str(node.module) == '__future__'
    mod = ast.parse('pass')
    out = Python2FutureTransformer().visit(mod)
    for node in out.body:
        check_future(node)

# Generated at 2022-06-14 01:55:47.715218
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast import ast3 as ast
    from ..transformers.base import BaseNodeTransformer
    import inspect
    assert inspect.isclass(Python2FutureTransformer)
    assert issubclass(Python2FutureTransformer, BaseNodeTransformer)
    assert Python2FutureTransformer.target == (2, 7)
    node = ast.Module()
    node.body = []
    obj = Python2FutureTransformer(node, (2, 7))
    assert obj.tree is node
    assert obj._tree_changed is False
    assert obj.target == (2, 7)


# Generated at 2022-06-14 01:55:49.612342
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)



# Generated at 2022-06-14 01:55:55.983966
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:56:06.653489
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .base import BaseNodeTransformer
    from ..utils.sample import sample

    transformer = Python2FutureTransformer()
    code = sample.get_sample_code()

    assert isinstance(transformer, BaseNodeTransformer)
    assert transformer.tree_changed == False
    assert transformer.target == (2, 7)
    assert transformer.current_module == None

    code_tree = transformer.get_code_tree(code, "test.py")
    assert transformer.current_module == "test"

    code_tree = transformer.visit_Module(code_tree)
    assert transformer.tree_changed == True
    assert transformer._tree_changed == True

# Generated at 2022-06-14 01:56:11.906506
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import ast
    import __future__

    node = ast.parse(source="")

    transformer = Python2FutureTransformer()
    transformer.visit(node)

    t = transformer.show_tree()

    assert """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
""" in t

# Generated at 2022-06-14 01:56:13.880980
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert t.target == (2, 7)
    assert t.__class__.__name__ == 'Python2FutureTransformer'

# Generated at 2022-06-14 01:56:18.675230
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from vistir.compat import Path
    from ..utils import get_test_data

    filename = Path(get_test_data("py2/test_print.py"))
    t = ast.parse(filename.read_text())
    t = Python2FutureTransformer().visit(t)
    print(ast.dump(t))

# Generated at 2022-06-14 01:56:27.785576
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .test_files.test_module import example_module_body, example_module_body_after_transform
    import astor
    imports = ast.parse('from __future__ import absolute_import; from __future__ import division; from __future__ import print_function; from __future__ import unicode_literals;').body
    module_body = imports + example_module_body
    module = ast.Module(body=module_body)
    transformer = Python2FutureTransformer(module)
    assert astor.to_source(transformer.visit(module)) == astor.to_source(module)

# Generated at 2022-06-14 01:56:30.204240
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__name__ == "Python2FutureTransformer"
    node = ast.Module()
    node = Python2FutureTransformer().visit(node)
    assert node.__class__.__name__ == "Module"


# Generated at 2022-06-14 01:56:31.694630
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None

# Generated at 2022-06-14 01:56:41.038038
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import ast as pyast

    source = "\n".join([
        "def a(x):",
        "    return x",
        "# some comment",
    ])
    expected = "\n".join([
        "from __future__ import absolute_import",
        "from __future__ import division",
        "from __future__ import print_function",
        "from __future__ import unicode_literals",
        "",
        "def a(x):",
        "    return x",
        "# some comment",
    ])

    tree = pyast.parse(source)

    # Constructor should not fail
    Python2FutureTransformer()

    actual = Python2FutureTransformer().visit(tree)

    assert actual is not None
    assert pyast.dump(actual) == pyast.dump(pyast.parse(expected))

# Generated at 2022-06-14 01:56:53.178101
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_node = ast.parse('x=1+1')
    assert (ast.dump(module_node) ==
            "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])")
    transformer = Python2FutureTransformer()
    module_node = transformer.visit_Module(
        module_node)  # type: ignore
    expected_ast = ast.parse('''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
x=1+1''')
    assert (ast.dump(module_node) ==
            ast.dump(expected_ast))

# Generated at 2022-06-14 01:56:58.868183
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module = ast.parse(textwrap.dedent('''
    import os
    import sys
    import re
    import types
    def func():
        pass
    '''))
    tf = Python2FutureTransformer()
    tf.visit(module)
    assert unparse(module) == textwrap.dedent('''
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    import os
    import sys
    import re
    import types
    def func():
        pass
    ''')




# Generated at 2022-06-14 01:57:05.269545
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():

    python2_future_transformer = Python2FutureTransformer()
    assert type(python2_future_transformer) == Python2FutureTransformer


# Generated at 2022-06-14 01:57:07.091243
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    t = Python2FutureTransformer()
    assert isinstance(t, Python2FutureTransformer)

# Generated at 2022-06-14 01:57:14.111860
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    # type: () -> None
    from .. import transform
    from . import util
    tree = ast.parse('def test():pass')
    tree = transform(tree, Python2FutureTransformer, (2, 7))
    assert util.dump_ast(tree) == util.dump_ast(imports.get_ast(future='__future__') + tree)



# Generated at 2022-06-14 01:57:15.088416
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:16.653369
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer.__doc__ is not None

# Generated at 2022-06-14 01:57:21.855694
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .test_base_transformer import node
    from .test_base_transformer import check_node

    node = ast.Module(body=[])

    check_node(Python2FutureTransformer(target=(2, 7)).visit(node),
               ast.Module(body=imports.get_body(future='__future__')))
    


# Generated at 2022-06-14 01:57:23.239117
# Unit test for constructor of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:24.526858
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    Python2FutureTransformer()

# Generated at 2022-06-14 01:57:34.624941
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast

    code = '''
        x = 1
        s = 'hi'
        # TODO
    '''
    node = ast.parse(code)
    transformer = Python2FutureTransformer()
    node = transformer.visit(node)
    assert len(node.body) == 5
    assert isinstance(node.body[0], ast.ImportFrom)
    assert isinstance(node.body[1], ast.ImportFrom)
    assert isinstance(node.body[2], ast.ImportFrom)
    assert isinstance(node.body[3], ast.ImportFrom)
    assert isinstance(node.body[4], ast.Assign)
    assert node.body[0].names[0].name == 'absolute_import'
    assert node.body[0].names[0].asname

# Generated at 2022-06-14 01:57:37.383578
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    tr = Python2FutureTransformer()
    assert tr.target == (2, 7)


# Generated at 2022-06-14 01:57:47.114118
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from .fixtures.python_2_module import example_module
    from ..utils import dump_ast
    xformer = Python2FutureTransformer()
    xformer.visit(example_module)
    assert dump_ast(xformer.module) == dump_ast(imports.get_module(future='__future__') + example_module) # type: ignore

# Generated at 2022-06-14 01:57:50.464917
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from python_modernizer.transformations import Python2FutureTransformer
    module = Python2FutureTransformer(None)
    assert isinstance(module, object)

# Generated at 2022-06-14 01:57:52.677833
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 01:57:55.746157
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transform = Python2FutureTransformer()
    tree = ast.parse(textwrap.dedent("""
    # Should have absolute_import, division, print_function, and unicode_literals
    """))
    assert transform.visit(tree) is tree

# Generated at 2022-06-14 01:58:02.995931
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    module_node = ast.parse("""
    import os

    def foo():
        pass
    """)

    actual_node = Python2FutureTransformer().visit(module_node)

    expected_module_node = ast.parse("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    import os

    def foo():
        pass
    """)

    assert ast.dump(expected_module_node) == ast.dump(actual_node) # nosec

# Generated at 2022-06-14 01:58:11.114859
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ...utils.fixtures import some_python_source

    # given
    py_code = '''
        some_python_code()
    '''

    # when
    node = ast.parse(py_code)
    v = Python2FutureTransformer()
    from astunparse_jit import dump
    v.visit(node)
    expected = some_python_source('''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        some_python_code()
    ''')

    # then
    assert expected.strip() == dump(node).strip()

# Generated at 2022-06-14 01:58:18.887469
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import os.path
    from shutil import copy2
    from glob import glob
    from astor import to_source
    from typo import utils
    from typo.utils.tree import get_tree
    from typo.visitors.python2_future import Python2FutureTransformer

    filepath_input: str
    filepath_output: str
    test_data: str = os.path.join(os.path.dirname(__file__), 'data', 'python2_future')
    filepaths = glob(os.path.join(test_data, '*.py'))

    for filepath in filepaths:
        filepath_input = filepath
        filepath_output = filepath + '.output'

        copy2(filepath_input, filepath_output)

        tr = Python2FutureTransformer()

# Generated at 2022-06-14 01:58:28.979800
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    """
    Python2FutureTransformer - visit_Module
    """
    modules_before = ['a = 1',
                      'from __future__ import absolute_import',
                      '',
                      'from __future__ import unicode_literals',
                      ''
                      ]

    modules_after = ['from __future__ import absolute_import',
                     'from __future__ import unicode_literals',
                     'from __future__ import division',
                     'from __future__ import print_function',
                     '',
                     'a = 1',
                     'from __future__ import absolute_import',
                     '',
                     'from __future__ import unicode_literals',
                     ''
                     ]

    for module_before, module_after in zip(modules_before, modules_after):
        tree_before = ast.parse(module_before)
       

# Generated at 2022-06-14 01:58:30.353766
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer(None, False)


# Generated at 2022-06-14 01:58:38.169073
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from .testing import assert_node
    from typed_ast import ast3 as ast

    source = textwrap.dedent("""
    def foo():
        pass
    """)
    expected = textwrap.dedent("""
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    def foo():
        pass
    """)
    root_node = ast.parse(source)
    t = Python2FutureTransformer()
    t.visit(root_node)
    assert_node(root_node, expected)
    assert t._tree_changed

# Generated at 2022-06-14 01:58:54.130490
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    node = ast.parse('print("Hello World!")')
    transformer = Python2FutureTransformer()
    node = transformer.visit(node)
    assert transformer._tree_changed == True
    assert transformer.target == (2, 7)
    assert node.body[0].value.future == '__future__'
    assert isinstance(node.body[0], ast.ImportFrom)
    assert isinstance(node.body[1], ast.ImportFrom)
    assert isinstance(node.body[2], ast.ImportFrom)
    assert isinstance(node.body[3], ast.ImportFrom)



# Generated at 2022-06-14 01:59:07.858062
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.source import source
    from ..utils.ast import ast_equal, dump
    from .base import BaseNodeTransformer
    from .transforms.utils import strip_future_import
    from .parsing import parse
    node = parse(source("""
        #!/usr/bin/env python
        # -*- coding: utf-8 -*-
        import sys
        
        '''this is a docstring'''
        # this is a comment
        if __name__ == '__main__':
            print('hello')
    """))
    with BaseNodeTransformer.init_context(node):
        visit(Python2FutureTransformer(), node) # type: ignore
        stripped_node = copy(node)
        visit(strip_future_import(), stripped_node)

# Generated at 2022-06-14 01:59:11.512994
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    T = Python2FutureTransformer
    assert T.__name__ == 'Python2FutureTransformer'
    assert T.__doc__ == """Prepends module with:
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals\n        \n    """
    assert T.target == (2, 7)

# Generated at 2022-06-14 01:59:13.183117
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert repr(Python2FutureTransformer()) == 'Python2FutureTransformer()'

# Generated at 2022-06-14 01:59:14.376362
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer()

# Generated at 2022-06-14 01:59:17.471172
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    visitor = Python2FutureTransformer()

# Generated at 2022-06-14 01:59:18.266440
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 01:59:19.060763
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    pass

# Generated at 2022-06-14 01:59:27.776375
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast import ast3 as ast
    import astor
    node = ast.parse('')
    node = ast.Module(body=[])
    t = Python2FutureTransformer()
    t.visit(node)
    assert astor.to_source(node) == 'from __future__ import absolute_import\n' \
                                    'from __future__ import division\n' \
                                    'from __future__ import print_function\n' \
                                    'from __future__ import unicode_literals\n'

# Generated at 2022-06-14 01:59:29.376537
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor  # type: ignore


# Generated at 2022-06-14 01:59:50.163601
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse("x = 1; y = 2")
    transformer = Python2FutureTransformer()
    result = transformer.visit(node)
    expected = ast.parse("from __future__ import absolute_import; from __future__ import division; from __future__ import print_function; from __future__ import unicode_literals; x = 1; y = 2")
    assert ast.dump(result) == ast.dump(expected)

# Generated at 2022-06-14 01:59:51.427151
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None



# Generated at 2022-06-14 02:00:00.203135
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from six import StringIO

    class MockFile(StringIO):
        def write(self, x): pass

    node = ast.parse(
'''
print('hello, world!')
''',
        filename='test.py',
        mode='exec')
    transformer = Python2FutureTransformer(MockFile())
    node = transformer.visit(node)
    assert len(node.body) == 5
    assert isinstance(node.body[0], ast.ImportFrom)
    assert isinstance(node.body[1], ast.ImportFrom)
    assert isinstance(node.body[2], ast.ImportFrom)
    assert isinstance(node.body[3], ast.ImportFrom)
    assert isinstance(node.body[4], ast.Expr)

# Generated at 2022-06-14 02:00:01.645803
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer().target == (2, 7)

# Generated at 2022-06-14 02:00:03.184272
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:00:11.174695
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
  from typed_ast import parse
  tree = parse('c = 1\ndef f(b: int):\n    return b + c')
  new_tree = Python2FutureTransformer().visit(tree)
  assert new_tree.body[0] == tree.body[0]
  assert new_tree.body[0].value == tree.body[0].value
  assert new_tree.body[1].args.args[0].arg == tree.body[1].args.args[0].arg
  assert new_tree.body[1].args.args[0].annotation == tree.body[1].args.args[0].annotation
  assert new_tree.body[1].body[0].value.left == tree.body[1].body[0].value.left

# Generated at 2022-06-14 02:00:17.797924
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.fixtures import module_test_template
    from ..utils.visitor import dump_ast
    from ..utils.source import indent
    from ..transpile import Transpiler

    input = module_test_template.format(
        '''def test(): pass  # noqa''',
    )

# Generated at 2022-06-14 02:00:18.551491
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    return

# Generated at 2022-06-14 02:00:20.434252
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer.target == (2, 7)

# Generated at 2022-06-14 02:00:26.351815
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('a = 1')
    Python2FutureTransformer().visit(node)
    assert ast.dump(node) == "from __future__ import absolute_import; from __future__ import division; from __future__ import print_function; from __future__ import unicode_literals; a = 1"

# Generated at 2022-06-14 02:00:57.911858
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer._tree_changed is False
    assert transformer.target == (2, 7)


# Generated at 2022-06-14 02:00:59.855186
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    """Unit test for constructor of class Python2FutureTransformer"""
    Python2FutureTransformer("test")

# Generated at 2022-06-14 02:01:10.419060
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    lines = ['import datetime', '', 'print("hello, world!")']
    assert Python2FutureTransformer().transform_lines(lines) == ['from __future__ import absolute_import\n', 'from __future__ import division\n', 'from __future__ import print_function\n', 'from __future__ import unicode_literals\n', '\n', 'import datetime\n', '\n', '\n', 'print("hello, world!")\n']

# Generated at 2022-06-14 02:01:14.175964
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    tree = ast.parse("print('Hello, world!')", mode='exec')
    transformer = Python2FutureTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed



# Generated at 2022-06-14 02:01:22.764946
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from ..utils.vistransformer import node_visit_transformer
    assert(node_visit_transformer(Python2FutureTransformer, ast.Module(body=[]), 'visit_Module')) == ast.Module(body=[ast.ImportFrom(module='__future__',names=[ast.alias(name='absolute_import',asname=None), ast.alias(name='division', asname=None), ast.alias(name='print_function', asname=None),ast.alias(name='unicode_literals', asname=None)], level=0)])

# Generated at 2022-06-14 02:01:29.359325
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    from typed_ast.ast3 import parse

    tree = parse('print(1)')

    transformer = Python2FutureTransformer(tree, (2, 7))
    module = transformer.visit(tree)

    assert module.body[0].value.s == 'absolute_import'
    assert module.body[1].value.s == 'division'
    assert module.body[2].value.s == 'print_function'
    assert module.body[3].value.s == 'unicode_literals'
    assert module.body[4].value.n == 1

# Generated at 2022-06-14 02:01:34.256097
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import typed_ast.ast3 as ast
    from ast_helper import parse
    from ast_helper import dump
    from ast_helper import assert_program
    from ast_helper import equal_program

    for source in ['', 'y = 1', 'y = 1; x = 2']:
        tree = parse(source, '<string>')
        expected = parse(imports.get_source(future='__future__') + source)
        assert_program(
            expected,
            Python2FutureTransformer().visit(tree),
        )

# Generated at 2022-06-14 02:01:35.287460
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:36.423701
# Unit test for method visit_Module of class Python2FutureTransformer

# Generated at 2022-06-14 02:01:47.348150
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    from typed_ast.ast3 import Module
    from typed_ast.ast3 import parse
    import os
    import sys
    import tempfile
    # Create a temp file
    tmpdir = tempfile.mkdtemp()
    path = os.path.join(tmpdir, "tmp_test_Py2FutureTransformer.py")
    with open(path, "w") as file:
        file.write("print(2 + 3)")
    sys.path.insert(0, tmpdir)
    # Read source code from file
    with open(path, 'r') as content_file:
        content = content_file.read()    
    # Parse code
    tree = parse(content)
    assert isinstance(tree, Module)
    # Apply Python2FutureTransformer

# Generated at 2022-06-14 02:02:57.011276
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    import astor
    code = astor.to_source(Python2FutureTransformer().visit(ast.parse("")))
    assert code == '''
# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
    '''.strip()

# Generated at 2022-06-14 02:03:05.701581
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    node = ast.parse('')
    node = Python2FutureTransformer().visit(node)
    assert ast.dump(node, include_attributes=False) == '''Module(body=[ImportFrom(
    module='future',
    names=[alias(
        name='absolute_import',
        asname=None)],
    level=0), ImportFrom(
    module='future',
    names=[alias(
        name='division',
        asname=None)],
    level=0), ImportFrom(
    module='future',
    names=[alias(
        name='print_function',
        asname=None)],
    level=0), ImportFrom(
    module='future',
    names=[alias(
        name='unicode_literals',
        asname=None)],
    level=0)])'''

# Generated at 2022-06-14 02:03:14.946304
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    import astor
    from ..utils.ast_helper import ast_to_str
    code = """a = 1"""
    t = Python2FutureTransformer()
    t.visit(ast.parse(code))
    assert astor.to_source(t.visit(ast.parse(code))).strip() == ast_to_str(t.visit(ast.parse(code))).strip()
    assert ast_to_str(t.visit(ast.parse(code))).strip() == """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

a = 1"""

# Generated at 2022-06-14 02:03:16.413845
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
  assert Python2FutureTransformer()

# Generated at 2022-06-14 02:03:20.267355
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    source = """
    from abc import ABCMeta
    from builtins import print_function
    import os
    import sys
    """
    expected = """
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals

    from abc import ABCMeta
    from builtins import print_function
    import os
    import sys
    """
    tree = ast.parse(source)
    t = Python2FutureTransformer()
    t.visit(tree)
    assert ast.dump(tree) == expected

# Generated at 2022-06-14 02:03:24.448428
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer(): 
    from typed_ast.ast3 import parse

    node = parse("print(3+4)")
    future = Python2FutureTransformer()
    node = future.visit(node)
    assert(future._tree_changed)
    assert(len(node.body) == 5)


# Generated at 2022-06-14 02:03:25.631624
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    assert Python2FutureTransformer is not None


# Generated at 2022-06-14 02:03:26.811122
# Unit test for constructor of class Python2FutureTransformer
def test_Python2FutureTransformer():
    transformer = Python2FutureTransformer()
    assert transformer is not None



# Generated at 2022-06-14 02:03:34.990932
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():
    input_ast = ast.parse(dedent(r'''
        def foo():
            pass
        '''))
    expected_ast = ast.parse(dedent(r'''
        from __future__ import absolute_import
        from __future__ import division
        from __future__ import print_function
        from __future__ import unicode_literals

        def foo():
            pass
        '''))
    transformer = Python2FutureTransformer()
    actual_ast = transformer.visit(input_ast)
    # Can't use assertEqual because Python 2.7 does not have assertCountEqual
    assert ast.dump(actual_ast) == ast.dump(expected_ast)

# Generated at 2022-06-14 02:03:41.541292
# Unit test for method visit_Module of class Python2FutureTransformer
def test_Python2FutureTransformer_visit_Module():

    import sys
    import os
    import ast as AST
    import tempfile

    tmpdir = tempfile.mkdtemp()

    def cleanup():
        try:
            os.rmdir(tmpdir)
        except:
            pass

    # Clean up the temp dir
    import atexit
    atexit.register(cleanup)

    sys.path.insert(0, tmpdir)

    from typed_ast import ast3 as typed_ast
