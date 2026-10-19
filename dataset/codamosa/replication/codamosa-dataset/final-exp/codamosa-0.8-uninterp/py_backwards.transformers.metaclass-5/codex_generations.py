

# Generated at 2022-06-14 01:55:09.932801
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast

    module = ast.parse("""
    class A(metaclass=B):
        pass
    """)

    m = MetaclassTransformer()
    m.visit(module)

    # Ensure that the tree is modified
    ast.fix_missing_locations(module)
    assert ast.dump(module) == pyast.parse("""
    body = [
        _py_backwards_six_withmetaclass(B, *[
            Name(id='A', ctx=Load())
        ])
    ]
    """).body



# Generated at 2022-06-14 01:55:23.297293
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # the original code
    code = 'class A(B, metaclass=C): pass'
    expected = 'class A(_py_backwards_six_withmetaclass(C)): pass'

    # parse the code
    tree = ast.parse(code)
    # apply the transformation to the tree
    mt = MetaclassTransformer()
    mt.visit(tree)
    # assert that the tree was changed
    assert mt.changed is True
    # compile the new tree
    compiled = compile(tree, '', 'exec')
    # execute the compiled code
    scope = {}
    exec(compiled, scope)
    # assert that scope['A'] is the transformed class
    assert scope['A'].__class__.__name__ == 'A'
    # assert that the bases code is the expected value

# Generated at 2022-06-14 01:55:30.073445
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3
    transformer = MetaclassTransformer()
    expected_tokens = six_import.get_tokens() + [
        (1, 0), (0, 'class'), (1, 5), (1, 10), (0, 'A'), (1, 12), 
        (0, ':'), (1, 14), (0, 'pass'), (2, 0)]
    source = 'class A:\n    pass'
    tree = ast3.parse(source)
    transformer.visit(tree)
    assert transformer.tree_changed
    assert transformer.get_tokens() == expected_tokens 


# Generated at 2022-06-14 01:55:34.331375
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse('class A(metaclass=B, c=d): pass')
    classdef = module.body[0]

    node = MetaclassTransformer().visit(module)
    assert node.body[0].value.elts == classdef.bases
    assert node.body[0].value.elts[0].args[0] == classdef.keywords[0].value
    assert classdef.bases == class_bases.get_body(metaclass=classdef.keywords[0].value,
                                                  bases=ast.List(elts=classdef.bases))

# Generated at 2022-06-14 01:55:41.045292
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    line = '''class A(metaclass=B): pass'''
    expected_line = '''class A(_py_backwards_six_withmetaclass(B))'''
    assert expected_line in MetaclassTransformer(tree=ast.parse(line)).tree.body[0].body[0]._fields
    assert 1 == len(MetaclassTransformer(tree=ast.parse(line)).tree.body[0].body[0]._fields)

# Generated at 2022-06-14 01:55:49.504596
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    inp_ast = ast.parse(
        '''\
        class A:
            pass

        class B(metaclass=type):
            pass
        ''')
    expected_ast = ast.parse(
        '''\
        from six import with_metaclass as _py_backwards_six_withmetaclass
        
        class A:
            pass

        class B(_py_backwards_six_withmetaclass(type))
            pass
        ''')

    result_ast = MetaclassTransformer().visit(inp_ast)
    assert ast.dump(result_ast) == ast.dump(expected_ast)

# Generated at 2022-06-14 01:55:59.474413
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():

    # test_MetaclassTransformer_visit_ClassDef_with_init
    # source:
    # class D(metaclass=E):
    #     def __init__(self):
    #         pass
    #
    # Expected result:
    # class D(_py_backwards_six_withmetaclass(E)):
    #     def __init__(self):
    #         pass
    source = ast.parse("class D(metaclass=E):\n\tdef __init__(self):\n\t\tpass")
    expected = ast.parse("class D(_py_backwards_six_withmetaclass(E)):\n\tdef __init__(self):\n\t\tpass")
    result = MetaclassTransformer().visit(source)
    compare_

# Generated at 2022-06-14 01:56:06.487502
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    tree = ast.parse("class A(metaclass=B):\n    pass")
    transformer = MetaclassTransformer()
    transformer.visit(tree)

    expected = ast.parse("from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(metaclass=B):\n    pass")
    assert ast.dump(tree, include_attributes=True) == ast.dump(expected, include_attributes=True)


# Generated at 2022-06-14 01:56:09.456528
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    input_ = """class A(metaclass=B):\n    pass"""


# Generated at 2022-06-14 01:56:14.036977
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import ast3 as ast
    from .utils import make_visitor
    metaclass_transformer = MetaclassTransformer(False, False)
    m = ast.parse('pass')
    metaclass_transformer.visit(m)



# Generated at 2022-06-14 01:56:22.451005
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    s = """class A(B, metaclass=C):\n    pass"""
    module = astor.parse_file(io.StringIO(s))
    transformer = MetaclassTransformer()
    transformer.visit(module)

# Generated at 2022-06-14 01:56:33.300612
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.fixtures import make_fake_module

    # Given a class definition with a metaclass
    source = """
    class A(metaclass=B):
        pass
    """
    module = make_fake_module(source)
    classdef = module.body[0]

    # When I visit the class definition
    transformer = MetaclassTransformer()
    new = transformer.visit(classdef)  # type: ast.ClassDef

    # Then the output should be equivalent to the input
    new_source = compile(new, '<test>', 'exec')
    expected = compile(classdef, '<test>', 'exec')
    assert new_source == expected

    # I should have transformed the tree
    assert transformer.tree_changed

# Generated at 2022-06-14 01:56:34.646089
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:39.311537
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_equal_ast
    code = '''
            class A(metaclass=B, something=True):
                pass
        '''
    actual = MetaclassTransformer.run(code)
    expected = '''
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(B, *[something=True])):
            pass
    '''
    assert_equal_ast(actual, expected)

# Generated at 2022-06-14 01:56:51.362830
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    from typed_ast import ast3
    from asttokens import asttokens

    code = textwrap.dedent(
        """
        class A(metaclass=B):
        pass
        """
    )

    atok = asttokens.ASTTokens(code, parse=True)
    tree = atok.tree
    assert isinstance(tree, ast3.Module)

    # Replace identifiers with constants
    for node in ast.walk(tree):
        if isinstance(node, ast3.Name):
            if node.id == 'B':
                node.__class__ = ast3.Num
                node.n = 1
                assert node.id == 'B'
                del node.id

    MetaclassTransformer().visit(tree)
    atok.rebuild_from_tok

# Generated at 2022-06-14 01:56:57.474361
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    base_tests = MetaclassTransformer.base_tests
    base_module = base_tests.base_module

    metaclass_transformer = MetaclassTransformer({}, {})
    target_ast = metaclass_transformer.visit(base_module)
    assert ast.dump(target_ast) == ast.dump(base_tests.metaclass_module)

# Generated at 2022-06-14 01:57:08.267510
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    metaclass = ast.Attribute(value=ast.Name(id='baz', ctx=ast.Load()), attr='bar',
                              ctx=ast.Load())
    bases = [ast.Name(id='bar', ctx=ast.Load()), ast.Name(id='foo', ctx=ast.Load())]
    kwargs = [ast.keyword(arg='metaclass', value=metaclass)]
    
    from ..tests.test_transformer import transform, assert_equal
    classdef = ast.ClassDef(name='Baz',
                            bases=bases,
                            keywords=kwargs,
                            body=[ast.Pass()],
                            decorator_list=[])
    result = transform(MetaclassTransformer, classdef)



# Generated at 2022-06-14 01:57:13.946295
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(metaclass=Foo):\n    pass')
    node = MetaclassTransformer().transform(node)
    
    node = ast.parse('class A(_py_backwards_six_withmetaclass(Foo)):\n    pass')

    assert node == node

# Generated at 2022-06-14 01:57:17.912245
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.ast import dump_ast, load_ast
    from .base import BaseNodeTransformer
    import typed_astunparse
    import astor


# Generated at 2022-06-14 01:57:18.942580
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:57:22.356716
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mt = MetaclassTransformer()

# Generated at 2022-06-14 01:57:29.538907
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..tests.test_utils import make_test_case, TEST_CASES

    for version in reversed(MetaclassTransformer.target):
        for test_case in TEST_CASES:
            try:
                test_code = make_test_case(test_case, version)
                exec(test_code)
            except SyntaxError:
                raise AssertionError('Failed to parse code:\n' + test_code)



# Generated at 2022-06-14 01:57:37.894311
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import inspect
    import typed_ast.ast3
    from contextlib import redirect_stderr
    from io import StringIO
    import unittest
    import sys
    import astor
    from . import node_util

    class TestMetaclassTransformer(unittest.TestCase):
        def assertModule(self, module: typed_ast.ast3.Module, expected):
            self.assertEqual(astor.to_source(module), expected)
            self.assertTrue(node_util.compile_snippet(module))

        def test_MetaclassTransformer_visit_ClassDef(self):
            module = ast.parse(r'''class A(metaclass=B):
    pass
''')
            module = MetaclassTransformer.run_pipeline(module)

# Generated at 2022-06-14 01:57:39.408317
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor

# Generated at 2022-06-14 01:57:47.079466
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import parse

    source = """
    class A(metaclass=B): pass
    """
    node = parse(source)
    transformer = MetaclassTransformer()
    node = transformer.visit(node)
    assert transformer._tree_changed

    assert node.body[0].bases[0].func.id == "_py_backwards_six_withmetaclass"

# Generated at 2022-06-14 01:57:48.873832
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source
    from ..utils.ast import dump


# Generated at 2022-06-14 01:57:54.964817
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node_to_test = ast.parse(
        """class A(metaclass=None): pass""",
        mode="exec"
    )
    assert MetaclassTransformer().visit(node_to_test) == ast.parse(
        """class A(_py_backwards_six_withmetaclass(None)): pass""",
        mode="exec"
    ).body[0]

# Generated at 2022-06-14 01:58:00.980065
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from six import with_metaclass
    import ast
    body = ["class A(metaclass=B):",
            "    pass",
            "class C(D, metaclass=E):",
            "    pass",
            ]
    body = ast.parse('\n'.join(body)).body
    result = MetaclassTransformer.run(body)
    assert len(result) == 2

# Generated at 2022-06-14 01:58:02.483686
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import util

# Generated at 2022-06-14 01:58:06.965890
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import sys
    import astor
    import unittest

    test_code = '''
    class A(metaclass=B):
        pass
    '''


# Generated at 2022-06-14 01:58:12.655283
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import run_transform
    from .. import six


# Generated at 2022-06-14 01:58:24.024361
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import transform, make_code
    code = make_code('''
        class A():
            pass

        class C(object):
            pass

        class D(metaclass=type):
            pass

        class E(metaclass=type, foo=True):
            pass

        class F(object, metaclass=type):
            pass
    ''')

# Generated at 2022-06-14 01:58:25.887749
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:33.050893
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_equal_code

    class_def = ast.parse("""
    class ClassName(object):
        __metaclass__  =   _py_backwards_six_with_metaclass(B,C)
        pass
    """).body[0]

    expected = """
    class ClassName(_py_backwards_six_with_metaclass(B,C)):
        pass
    """
    assert_equal_code(MetaclassTransformer().visit(class_def), expected)



# Generated at 2022-06-14 01:58:36.088194
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Given
    from typed_ast import ast3 as ast
    import typed_ast.ast3 as typedast
    from ..utils.tree import clean_tree
    from .base import BaseNodeTransformer
    from ..python2to3 import fix_ast


# Generated at 2022-06-14 01:58:44.224724
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    src = """
    class A(metaclass=B):
        pass
    """
    expect = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B),):
        pass
    """
    tree = compile_as_ast(src)
    actual = MetaclassTransformer().transform_tree(tree)

    assert expect == astunparse.unparse(actual)

# Generated at 2022-06-14 01:58:52.553081
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = textwrap.dedent("""
        from six import with_metaclass

        class A(object):
            pass

        class B(metaclass=A):
            pass

        """)
    tree = ast.parse(source, filename='<input>', mode='exec')
    expected_tree = ast.parse(textwrap.dedent("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(object):
            pass

        class B(_py_backwards_six_withmetaclass(A)):
            pass

        """), filename='<input>', mode='exec')
    transformer = MetaclassTransformer()
    tree = transformer.visit(tree)

    assert_equal_node(tree, expected_tree)

# Generated at 2022-06-14 01:59:06.298036
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    import pickle
    from textwrap import dedent

    # Method to test
    m = MetaclassTransformer()
    input_source = dedent('''\
    class Foo(object):
        def __str__(self):
            return "abc"
    ''')
    input_tree = ast.parse(input_source)
    m.visit(input_tree)
    assert m._tree_changed
    output_source = dedent('''\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class Foo(_py_backwards_six_withmetaclass(object, object)):
        def __str__(self):
            return "abc"
    ''')

# Generated at 2022-06-14 01:59:10.212810
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.testing import assert_equal_ast, assert_source_equal_ast

    from ..compat import astor

    source = "class A(metaclass=B): pass"
    tree = ast.parse(source)
    tree = MetaclassTransformer().visit(tree)


# Generated at 2022-06-14 01:59:23.599898
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    from ..compiler.python_compiler_bases import BaseCompiler
    from ..utils.tree import parse_tree
    from .base import BaseNodeTransformer

    store = {}

    class TestClass(BaseCompiler):
        def compile(self, source: str) -> str:
            tree = parse_tree(source)
            mt = MetaclassTransformer()
            result = mt.visit(tree)
            store["changes"] = mt.tree_changed
            return self.to_source(result)

    source = """
    class MyClass(A):
        pass
    """

# Generated at 2022-06-14 01:59:40.725216
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from astor.codegen import to_source
    source = """class A(metaclass=B, c=1, d=2):
    pass"""
    tree = ast.parse(source)
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    actual = to_source(tree)

# Generated at 2022-06-14 01:59:46.060176
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    from .test_BaseNodeTransformer import BaseNodeTransformer_visit_ClassDef as visit_ClassDef
    from .test_BaseNodeTransformer import BaseNodeTransformer_transformer as transformer


# Generated at 2022-06-14 01:59:47.434601
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from .six import six


# Generated at 2022-06-14 01:59:57.472041
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .base import roundtrip, BaseNodeTransformerTest
    from ..utils.tree import node_equal

    class Test(BaseNodeTransformerTest):
        target = (2, 7)
        transform = MetaclassTransformer
        transform_arguments = ()

        def test_metaclass_base(self):
            """class A(metaclass=bases):
                   pass
               >>> class A(_py_backwards_six_with_metaclass(bases)):
                   pass
            """

# Generated at 2022-06-14 02:00:07.678077
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.messages import Messages
    from ..utils.source import Source

    msg = Messages()
    src = Source('', 'test.py')
    src.lines = [
        "class A(metaclass=B):",
        "    pass",
    ]

    transformer = MetaclassTransformer(src, msg)
    node = transformer.visit(ast.parse(src.text))

# Generated at 2022-06-14 02:00:09.981268
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import parse
    from ..utils.ast import to_source

# Generated at 2022-06-14 02:00:19.740921
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('''
    class A(object, B, C, metaclass=D):
        pass
        ''')
    MetaclassTransformer().visit(node)
    print(ast.dump(node))

# Generated at 2022-06-14 02:00:33.451621
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()

    class Node(ast.AST):
        _fields = ('bases', 'keywords')

    node = ast.parse("class A(metaclass=B):\n    pass\n")
    expected = ast.parse("from six import with_metaclass as _py_backwards_six_with_metaclass\n\nclass A(_py_backwards_six_with_metaclass(B)):\n    pass\n")
    classdef = node.body[0]
    assert isinstance(classdef, ast.ClassDef)
    assert classdef.keywords
    assert classdef.bases
    assert isinstance(classdef.keywords[0], ast.keyword)
    assert  isinstance(classdef.keywords[0].value, ast.Name)

# Generated at 2022-06-14 02:00:44.365048
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Test 1
    # Test with metaclass

    # Test 1 setup
    code = """
        class A(metaclass=12):
            pass
    """

    # Test 1 assert
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(12)):
            pass
    """

    # Test 1 run
    actual = MetaclassTransformer().visit_str(code)

    # Test 1 final assert
    assert actual == expected

    # Test 2
    # Test with multiple inheritance

    # Test 2 setup
    code = """
        class A(1, 2, 3, metaclass=12):
            pass
    """

    # Test 2 assert

# Generated at 2022-06-14 02:00:47.794325
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import do_test_visitor

    def visitor_init(visitor_instance):
        visitor_instance.tree_changed = False


# Generated at 2022-06-14 02:01:16.292699
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..visit_utils import get_first_expr
    from ..utils.tree import assert_tree_equal
    from .scope_transformer import ScopeTransformer

    trans = MetaclassTransformer()
    stmt = ast.parse('class A(B, metaclass=C):\n    pass')
    stmt = get_first_expr(stmt)  # type: ast.ClassDef
    assert isinstance(stmt, ast.ClassDef)

    res = trans.visit(stmt)
    assert_tree_equal('class A(_py_backwards_six_withmetaclass(C, *[B])):\n    pass', res)
    trans = ScopeTransformer()
    res = trans.visit(res)

# Generated at 2022-06-14 02:01:21.391344
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.fake import FakeFile
    from .. import transform

    code = '''class A(metaclass=B):pass'''
    module, _ = transform(FakeFile.from_code(code))

    assert 'class A(_py_backwards_six_with_metaclass(B)):pass' == module.to_code()


# Generated at 2022-06-14 02:01:26.331236
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # type: () -> None
    node = ast.parse('class A(metaclass=B, **kwargs):\n    pass')
    transformer = MetaclassTransformer()
    transformer.visit(node)
    assert_ast_equal(node, ast.parse('class A(_py_backwards_six_withmetaclass(B, *([]))):\n    pass'))

# Generated at 2022-06-14 02:01:27.341656
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:01:37.754527
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..pygram import python_symbols as syms
    from ..utils import make_ast
    from ..compiler import compile_func
    from .. import six
    from typed_ast import ast3 as ast

    node = make_ast.parse('''
    class A(metaclass=B):
        pass
    def func():
        pass
    ''', target=six.python_version)

    compiler = MetaclassTransformer()
    node1 = compiler.transform(node)

    body = node1.body

    assert len(body) == 3
    assert isinstance(body[0], ast.FunctionDef)
    assert len(body[0].body) == 1
    assert isinstance(body[1], ast.ImportFrom)
    assert body[1].module == 'six'

    classdef = body[2]


# Generated at 2022-06-14 02:01:48.575771
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Unit test for method visit_ClassDef of class MetaclassTransformer."""
    # Given
    before = ast.Module(
        body=[
            ast.ClassDef(name='A',
                         bases=[ast.Name(id='B', ctx=ast.Load())],
                         keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='C', ctx=ast.Load()))])
        ]
    )


# Generated at 2022-06-14 02:01:51.735967
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()  # type: ignore


# Generated at 2022-06-14 02:01:55.210996
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast27
    node = ast27.parse('class A(metaclass=B): pass')

# Generated at 2022-06-14 02:02:03.906196
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from . import normalize_code
    from .base import Parser
    from .six import SixTransformer
    
    
    
    class Test(metaclass=type):
        pass
    
    expected_code = """\
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class Test(_py_backwards_six_withmetaclass(type)):
        pass"""
    
    tree = Parser().parse(normalize_code(astor.to_source(Test)))
    SixTransformer().visit(tree)
    MetaclassTransformer(tree).visit(tree)
    assert normalize_code(astor.to_source(tree)) == expected_code


# Generated at 2022-06-14 02:02:13.919594
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class MetaclassTransformerTest(unittest.TestCase):
        def test_MetaclassTransformerTest(self):
            node = ast.parse('''
                import six
                class A(metaclass=six.with_metaclass):
                    pass
            ''') # type: ignore
            transformer = MetaclassTransformer()
            transformer.visit(node)
            self.assertEqual(str(node), '''
                import six
                class A(six.with_metaclass):
                    pass
            ''')

# Generated at 2022-06-14 02:02:57.912619
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.source import source_to_ast as sta
    ast_in = sta("""
    class A(metaclass=B):
        pass
    """)
    ast_out = sta("""
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """)
    assert MetaclassTransformer().visit(ast_in) == ast_out


# Generated at 2022-06-14 02:03:06.273792
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:07.129118
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:13.674779
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..pgen2.parse import parse

    node = parse(
        textwrap.dedent('''\
        class A(metaclass=B):
            pass'''))
    expected = parse(
        textwrap.dedent('''\
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass'''))
    transformer = MetaclassTransformer()
    res = transformer.visit(node)
    assert res == expected

# Generated at 2022-06-14 02:03:16.950815
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:29.777393
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    metaclass_node = ast.Name(id='B', ctx=ast.Load())
    class_node = ast.ClassDef(name='A',
                              bases=[ast.Name(id='object', ctx=ast.Load())],
                              keywords=[ast.keyword(arg='metaclass', value=metaclass_node)])
    module_node = ast.Module(body=[class_node])
    mct = MetaclassTransformer()

    mct.visit(module_node)

    assert mct._tree_changed is True

# Generated at 2022-06-14 02:03:32.277928
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_no_mutation


# Generated at 2022-06-14 02:03:33.019112
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:41.815519
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    t = MetaclassTransformer()
    node = ast.ClassDef(name='A',
                        bases=[ast.Name(id='SomeBase')],
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='SomeMetaclass'))],
                        body=[])
    node = t.visit(node)
    assert isinstance(node.bases[0], ast.Call)
    node_bases_call = node.bases[0]
    assert isinstance(node_bases_call.func, ast.Name)

# Generated at 2022-06-14 02:03:53.834378
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    from ..utils import as_code
    from .. import fixer_registry
    from .. import six_transformer
    from .. import standard_transformer

    _registry = fixer_registry.FixerRegistry()
    _registry.register(six_transformer.MetaclassTransformer)
    _registry.register(standard_transformer.StandardTransformer)

    code = '''\
        from __future__ import annotations

        class A(metaclass=B):
            pass
        
        '''
    expected = '''\
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(
            _py_backwards_six_withmetaclass(B)
        ):
            pass
        
        '''
    node = ast.parse