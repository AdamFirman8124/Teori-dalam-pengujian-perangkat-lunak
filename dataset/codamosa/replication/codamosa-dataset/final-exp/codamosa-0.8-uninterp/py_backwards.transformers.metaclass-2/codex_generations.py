

# Generated at 2022-06-14 01:55:11.560842
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import Optional

    class Root(ast.NodeTransformer):
        def __init__(self) -> None:
            self._result: Optional[MetaclassTransformer] = None

        @property
        def result(self) -> MetaclassTransformer:
            return self._result

        @result.setter
        def result(self, value: MetaclassTransformer) -> None:
            self._result = value

        def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
            self.result = MetaclassTransformer(version=(2, 7))
            return self.result.visit(node)

    tree = ast.parse('''
        class A(B, metaclass=C):
            pass
    ''')
    root = Root()
    root.result  # Initialize

# Generated at 2022-06-14 01:55:24.476569
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List
    from ..utils.test_utils import _transform, assert_transformed_tree

    snippets = [
        "class C(metaclass=type): pass",
        "class C(b1, metaclass=type): pass",
        "class C(b1, b2, metaclass=type): pass",
        "class C(b1, b2, b3, metaclass=type, **kwargs): pass",
        "class C(b1, b2, b3, metaclass=type, *args, **kwargs): pass",
    ]

    def _validate_ClassDef(node: ast.ClassDef, bases: List[ast.expr]) -> None:
        assert node.keywords == []
        assert isinstance(node.bases, ast.Call)
        assert node.bases

# Generated at 2022-06-14 01:55:27.616062
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class CodeTest(object):

        def __init__(self, test_text, expected_text):
            self.test_tree = ast.parse(test_text)
            self.expected_tree = ast.parse(expected_text)


# Generated at 2022-06-14 01:55:34.360419
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typing import List
    from typed_ast import ast3 as ast
    from ..utils.compare_ast import compare_ast

    source = '''  \
    class A(metaclass=B):
        pass'''
    expected = '''  \
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B))
        pass'''

    tree = compile(source, '<string>', mode='exec',
                   flags=ast.PyCF_ONLY_AST)
    tree = MetaclassTransformer().visit(tree)

    assert compare_ast(tree, compile(expected, '<string>', mode='exec',
                                     flags=ast.PyCF_ONLY_AST))

# Generated at 2022-06-14 01:55:42.239750
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = """
        class A(metaclass=B, other=C):
            pass
    """
    expected = """
        from six import with_metaclass as _py_backwards_six_withmetaclass


        class A(_py_backwards_six_withmetaclass(B, )):
            pass
    """

    tree = ast.parse(source)
    transform = MetaclassTransformer()
    new_tree = transform.visit(tree)
    assert expected == astor.to_source(new_tree)



# Generated at 2022-06-14 01:55:42.933588
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:53.232558
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.fixtures import make_test_function, mock_get_target
    from ..utils.visitor import NodeTransformerVisitor
    from ..utils.context import Context

    class Test(metaclass=NodeTransformerVisitor):
        def test_no_metaclass(self, ctx: Context):
            node = make_test_function(
                """
                class A:
                    pass
                """)

            ctx.assert_no_error()
            assert not MetaclassTransformer(ctx).visit(node)

        def test_with_metaclass(self, ctx: Context):
            node = make_test_function(
                """
                class A(metaclass=B):
                    pass
                """)

            ctx.assert_no_error()

# Generated at 2022-06-14 01:55:59.138534
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """Test that:
        class A(metaclass=B):
            pass
    Is transformed to:
        class A(_py_backwards_six_with_metaclass(B))
    
    """
    from typed_ast import parse

    node = parse("class A(metaclass=B): pass").body[0]

    assert metaclass(node) is None

    NodeTransformer = MetaclassTransformer()
    transformed = NodeTransformer.visit(node)

    assert transformed is not None
    assert metaclass(transformed) is None



# Generated at 2022-06-14 01:56:09.552536
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .test_utils import assert_transform
    from typed_ast import ast3 as ast

    example_metaclass_node = ast.ClassDef(name='MyClass',
                                          bases=[ast.Name(id='object', ctx=ast.Load())],
                                          keywords=[ast.keyword(arg='metaclass',
                                                                value=ast.Name(id='MyMetaclass', ctx=ast.Load()))],
                                          body=[],
                                          decorator_list=[])


# Generated at 2022-06-14 01:56:20.454592
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse(
        """

        class A(metaclass=B):
            pass

        """
    )

    expected = ast.Module(
        body=[
            six_import.get_body(),
            ast.ClassDef(
                name='A',
                bases=[
                    class_bases.get_body(
                        metaclass=ast.Name(id='B', ctx=ast.Load()),
                        bases=ast.List(elts=[])
                    )
                ],
                keywords=[],
                body=[],
                decorator_list=[]
            )
        ]
    )

    MetaclassTransformer.run_visitor(module)
    assert ast.dump(module, include_attributes=False) == ast.dump(expected, include_attributes=False)

# Generated at 2022-06-14 01:56:29.111978
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import assert_code_equal, ast_compare
    from typed_ast import ast3 as ast

    mod = ast.parse("class A(metaclass=B): pass", '', 'exec')
    mmt = MetaclassTransformer()
    r = mmt.visit(mod)
    assert_code_equal(snippet(r), snippet(MetaclassTransformer.visit_ClassDef.test_data))
    assert ast_compare(r, MetaclassTransformer.visit_ClassDef.test_data)



# Generated at 2022-06-14 01:56:38.025560
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as pyast
    from ..tests import BackportTestCase
    from ..converter import _apply_transformer

    class Test(BackportTestCase):
        def test_metaclass(self):
            node = pyast.parse(
                'class MyClass(metaclass=OtherClass):\n'
                '    def __init__(self):\n'
                '        pass\n'
            )
            actual = _apply_transformer(MetaclassTransformer, node)

# Generated at 2022-06-14 01:56:50.562482
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    m = ast.parse('class A(C, metaclass=B): pass')
    c = MetaclassTransformer()
    m = c.visit(m)
    assert ast.dump(m) == "Module(body=[ImportFrom(module='six', names=[alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0), ClassDef(name='A', bases=[Call(func=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), args=[Name(id='B', ctx=Load())], keywords=[], starargs=None, kwargs=None)], keywords=[], body=[Pass()], decorator_list=[])])"

# Generated at 2022-06-14 01:57:01.508907
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    source = """
        class A(metaclass=B, c=3):
            pass
    """
    expected = f"""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A({class_bases.get_body(metaclass=ast.Name(id='B', ctx=ast.Load()), bases=ast.List(elts=[], ctx=ast.Load()))}):
            pass
    """
    node = ast.parse(source)
    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)
    assert ast.dump(new_node) == expected

# Generated at 2022-06-14 01:57:05.455915
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse("""class A(metaclass=B): pass""")
    MetaclassTransformer().visit(tree)

# Generated at 2022-06-14 01:57:10.639934
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    class_def0 = ast.parse("""
        class A(metaclass=B):
            pass
        """)

    class_def1 = ast.parse("""
        class A(_py_backwards_six_with_metaclass(B)):
            pass
        """)

    transformer = MetaclassTransformer()
    result = transformer.visit(class_def0)
    assert astor.to_source(result) == astor.to_source(class_def1)

# Generated at 2022-06-14 01:57:21.450634
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.snippet import snippet
    from ..utils.tree import insert_at

    @snippet
    def test1(metaclass, bases):
        class A(metaclass):
            pass

    @snippet
    def test2(metaclass, bases):
        class A():
            pass

    @snippet
    def expected(metaclass, bases):
        class A(_py_backwards_six_withmetaclass(metaclass)):
            pass

    transform = MetaclassTransformer()

    module = ast.Module(body=[])
    module = transform.visit(module)
    assert module.body == [six_import.get_ast()]


# Generated at 2022-06-14 01:57:29.006634
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse('class A(metaclass=B): pass')
    expected = ast.parse('from six import with_metaclass as _py_backwards_six_withmetaclass\n'
                         '\n'
                         '\n'
                         'class A(_py_backwards_six_withmetaclass(B)):\n'
                         '    pass')
    # noinspection PyTypeChecker
    MetaclassTransformer.run_visitor(tree)
    assert tree == expected

# Generated at 2022-06-14 01:57:40.324021
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.ast_builder import build_ast
    import astunparse

    bases_list = [ast.Name(id="object", ctx=ast.Load())]
    metaclass = ast.Name(id="metaclass", ctx=ast.Load())
    base_class = ast.ClassDef(name="A", 
                              bases=bases_list, 
                              keywords=[ast.keyword(arg="metaclass", 
                                                    value=metaclass)], 
                              body=[])

    ast_module = build_ast([base_class])
    MetaclassTransformer().visit(ast_module)


# Generated at 2022-06-14 01:57:51.286939
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from _py_backwards.tests.utils import make_test_case_from_snippet
    import six

    # See issue #4 for details
    if six.PY3:
        return

    test_cases = [
        make_test_case_from_snippet(
            metaclass=type('Meta', (type,), {}),
            inputs=MetaclassTransformer,
            outputs=six.with_metaclass
        ),
        make_test_case_from_snippet(
            metaclass=type('Meta', (type,), {}),
            inputs=MetaclassTransformer,
            outputs=six.with_metaclass
        ),
    ]

    return test_cases

# Generated at 2022-06-14 01:58:02.578332
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent
    from typed_ast import ast3
    from ..utils.test_visitor import run_visitor

    snippet = '''
    class A(object, metaclass=B):
        pass
    '''

    expected = dedent('''
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, object)):
        pass
    ''').strip()

    assert expected == run_visitor(snippet, MetaclassTransformer)



# Generated at 2022-06-14 01:58:10.338534
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import parse
    from ..utils.python import version_tuple
    from .base import reverse_transformer_test
    if version_tuple() >= (3, 7, 0):
        class check(metaclass=type):
            pass
    else:
        class check(object):
            pass

    example = "class check(metaclass=type): pass"
    node = parse(example)

    res = reverse_transformer_test(MetaclassTransformer, node)
    assert res.body[0].body[0].bases[0].value.id == '_py_backwards_six_with_metaclass'

# Generated at 2022-06-14 01:58:14.725789
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
    class A(metaclass=B):
        pass"""
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass"""
    result = transform_code(MetaclassTransformer, code)
    assert result == expected

# Generated at 2022-06-14 01:58:21.432612
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from tests.utils import assert_converted

    src = '''
    class A(metaclass=B):
        pass
    '''
    expected = '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''

    assert_converted(src, expected, MetaclassTransformer)



# Generated at 2022-06-14 01:58:31.162583
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import textwrap
    from ..utils.ast_tools import as_code, pformat_ast

    class _DoNothingTransformer(ast.NodeTransformer):
        def visit_Name(self, node: ast.Name) -> ast.Name:
            return node

    # NOTE: this is the only way to use six.with_metaclass() in the old version
    class _Class(six.with_metaclass(type)):
        pass

    expected = pformat_ast(ast.parse(textwrap.dedent("""
        import six
        class _Class(_py_backwards_six_withmetaclass(type, six.with_metaclass)):
            pass
    """)))

    tr = MetaclassTransformer()


# Generated at 2022-06-14 01:58:38.811135
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.unparse import unparse_ast
    from ..utils.test_utils import assert_transformation
    from ..utils.python import remove_whitespace

    source = '''
        class Test(object):
            __metaclass__ = Other
        '''
    assert_transformation(
        MetaclassTransformer,
        source,
        remove_whitespace(r'''
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class Test(_py_backwards_six_with_metaclass(Other)):
            pass
        ''')
    )

# Generated at 2022-06-14 01:58:48.882554
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from textwrap import indent
    code = """
    import six

    class A(metaclass=six.Meta):
        pass
    """
    expected = """
    import six

    class A(_py_backwards_six_withmetaclass(six.Meta)):
        pass
    """
    # This file will contain the "six" import and the function "_py_backwards_six_withmetaclass"
    six_import_path = Path('./six_import')
    # This file will contain the class "A"
    class_a_path = Path('./class_a')
    six_import_path.write_text(six_import.to_string())
    class_a_path.write_text(code)

# Generated at 2022-06-14 01:58:58.521399
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six
    import ast

    s = """class A(metaclass=B): pass"""
    a = ast.parse(s)

    t = MetaclassTransformer()
    t.visit_ClassDef(a.body[0])

    assert ast.dump(t.visit_ClassDef(a.body[0])) == "ClassDef(name='A', bases=[Call(func=Name(id='_py_backwards_six_with_metaclass', ctx=Load()), args=[Name(id='B', ctx=Load())], keywords=[], starargs=None, kwargs=None)], keywords=[], body=[Pass()], decorator_list=[])"
    t = MetaclassTransformer()
    t.visit_ClassDef(a.body[0])


# Generated at 2022-06-14 01:59:01.993749
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestFile(six.StringIO):
        name = "test.py"

    input = TestFile()

# Generated at 2022-06-14 01:59:08.451270
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test import do_test
    code = """class A(metaclass=B):pass"""
    co = ast.parse(code)
    tr = MetaclassTransformer()
    t = tr.visit(co)

# Generated at 2022-06-14 01:59:23.076560
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer()
    cls = ast.ClassDef(name='A', bases=[], keywords=[], body=[], decorator_list=[])
    node = transformer.visit(cls)
    assert node.bases[0].func.id == '_py_backwards_six_withmetaclass'
    assert node.bases[0].keywords == []


# Generated at 2022-06-14 01:59:31.709477
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six_extras._ast_fixer as astfixer
    node = ast.parse("""
    class A(metaclass=B):
        pass
    """)
    node = astfixer.fix_missing_locations(node)

    class Meta(type):
        pass

    class A(Meta):
        pass
    expected = ast.parse("""
    class A(B):
        pass
    """)
    expected = astfixer.fix_missing_locations(expected)
    m = MetaclassTransformer()
    assert m.visit(node) == expected.body[0]

# Generated at 2022-06-14 01:59:33.346785
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:47.045506
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import six

    assert six.PY2

    import ast as pyast

    six_import_body = six_import.get_body()
    class_bases_body = class_bases.get_body(metaclass=pyast.parse('B').body[0], bases=pyast.List(elts=[]))


# Generated at 2022-06-14 01:59:54.132110
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:58.651255
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestMetaclassTransformer(MetaclassTransformer):
        def __init__(self):
            self._tree_changed = False

        def _tree_changed(self) -> bool:
            return self._tree_changed

    T = TestMetaclassTransformer()


# Generated at 2022-06-14 02:00:08.452727
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:18.974741
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    metaclass = ast.Name(id='object', ctx=ast.Load())
    bases = [ast.Name(id='MyType', ctx=ast.Load())]

    classdef = ast.ClassDef(name='A',
                            bases=bases,
                            keywords=[ast.keyword(arg='metaclass', value=metaclass)],
                            body=[])

    classdef = MetaclassTransformer().visit_ClassDef(classdef)

    assert isinstance(classdef.bases, ast.Call)
    assert classdef.bases.func.id == '_py_backwards_six_withmetaclass'
    assert isinstance(classdef.bases.args[0], ast.Name)
    assert classdef.bases.args[0].id == 'object'
    assert isinstance

# Generated at 2022-06-14 02:00:31.071620
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import get_module
    import sys

    module_ast = get_module("""
        class A(metaclass=B):
            pass
    """)

    MetaclassTransformer(
        sys.meta_path[-1].compile(module_ast, '<test>', 'exec')).visit(module_ast)

    assert six_import.get_body() in module_ast.body

    class_node = None

    for node in module_ast.body:
        if isinstance(node, ast.ClassDef):
            if node.name == 'A':
                class_node = node
                break

    assert class_node is not None

    (node,) = class_node.bases

    assert node.args[0].value.id == 'B'

# Generated at 2022-06-14 02:00:39.471421
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from unittest import TestCase
    from ..utils import compare_source

    class TestMetaclassTransformer_visit_ClassDef(TestCase):
        def test(self):
            # type: () -> None
            source = """
            class A(metaclass=B):
                pass
            """
            expected = """
            from six import with_metaclass as _py_backwards_six_withmetaclass


            class A(_py_backwards_six_withmetaclass(B)):
                pass
            """
            transformed = MetaclassTransformer().visit(ast.parse(source))
            compare_source(self, expected, transformed)
    TestMetaclassTransformer_visit_ClassDef().test()

# Generated at 2022-06-14 02:01:05.025533
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("""
    class ClassMetaclass(metaclass=type):
        pass
    """)
    trans = MetaclassTransformer()
    new = trans.visit(node)
    print(ast.dump(new))
    assert ast.dump(new) == """Module(body=[ImportFrom(module='six', names=[alias(name='with_metaclass', asname='_py_backwards_six_withmetaclass')], level=0), ClassDef(name='ClassMetaclass', bases=[Call(func=Name(id='_py_backwards_six_withmetaclass', ctx=Load()), args=[Name(id='type', ctx=Load())], keywords=[], starargs=None, kwargs=None)], keywords=[], body=[], decorator_list=[])])"""

# Generated at 2022-06-14 02:01:14.925130
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    before = ast.Module(body=[
        ast.ClassDef(name='Example', bases=[],
                     keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='ExampleMeta'))],
                     body=[]),
        ast.ClassDef(name='ExampleMeta', bases=[ast.Name(id='type')],
                     body=[
                         ast.Pass()
                     ])
    ])

    after = ast.parse(dedent('''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class Example(_py_backwards_six_withmetaclass(ExampleMeta, )):
            pass

        class ExampleMeta(type):
            pass
    ''').lstrip())

    transformer = MetaclassTransformer('test.py')
    transformer.visit(before)

# Generated at 2022-06-14 02:01:19.918297
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    import six
    m = ast.parse("""\
        class A(_py_backwards_six_with_metaclass(B)):
            pass""")
    MetaclassTransformer().visit(m)
    assert six.PY2 and six.PY3

# Generated at 2022-06-14 02:01:29.321330
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import textwrap
    from .utils import transform
    # Simple class
    before = ast.parse(textwrap.dedent('''
        from six import with_metaclass

        class A(metaclass=B, object):
            pass
    '''))
    after = ast.parse(textwrap.dedent('''
        class A(with_metaclass(B, object)):
            pass
    '''))
    assert after == transform(MetaclassTransformer.visit, before)

    # Python 2 class inheriting from a Python 3 class
    before = ast.parse(textwrap.dedent('''
        from six import with_metaclass

        class A(metaclass=B, C):
            pass
    '''))

# Generated at 2022-06-14 02:01:34.952983
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    mod1 = ast.parse('class A(metaclass=B):\n    pass')
    mod2 = ast.parse('class A(_py_backwards_six_with_metaclass(B)):\n    pass')

    assert MetaclassTransformer.can_run(2, 6)
    assert not MetaclassTransformer.can_run(2, 7)

    transformer = MetaclassTransformer()
    res = transformer.visit(mod1)

    assert transformer._tree_changed
    assert ast.dump(res, include_attributes=False) == ast.dump(mod2, include_attributes=False)

# Generated at 2022-06-14 02:01:39.183922
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse("""
    class A(metaclass=B): pass
    """)
    transformer = MetaclassTransformer()
    module = transformer.visit(module)
    assert "class A(_py_backwards_six_withmetaclass(B)):" in ast.dump(module)

# Generated at 2022-06-14 02:01:46.528294
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..unit_test import assert_compile

    code = """
    class Foo(object, metaclass=aaa.bbb.Ccc):
        pass
    """
    expected = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class Foo(_py_backwards_six_withmetaclass(aaa.bbb.Ccc,object)):
        pass
""".lstrip()
    assert_compile(code, expected, MetaclassTransformer)

# Generated at 2022-06-14 02:01:57.557253
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    code = "class A(metaclass=B): pass"
    expected_code = "from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)):\n    pass"
    visitor = MetaclassTransformer()
    module = ast.parse(code)
    visitor.visit(module)
    code_transformed = astor.to_source(module)
    assert code_transformed == expected_code

# Generated at 2022-06-14 02:02:04.750043
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from textwrap import dedent

    from ..core import get_ast, CompilerError

    from .six import SixMetaclassTransformer
    from .typing import TypingTransformer

    # Test case reference: https://docs.python.org/3/reference/compound_stmts.html#class-definitions
    class_def_source = """
        class A(metaclass=B):
            pass
    """
    class_def = get_ast(class_def_source)

    # Compile class_def to:
    # class A(_py_backwards_six_withmetaclass(B),):
    #    pass
    class_def = MetaclassTransformer().visit(class_def)
    class_def = TypingTransformer().visit(class_def)
    class_def = SixMetac

# Generated at 2022-06-14 02:02:09.742985
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    transformer = MetaclassTransformer(None)
    node = ast.parse("class A(object, metaclass=B): pass")
    assert transformer.visit(node) == ast.parse("from six import with_metaclass as _py_backwards_six_withmetaclass\nclass A(_py_backwards_six_withmetaclass(B)): pass")

# Generated at 2022-06-14 02:02:23.905828
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:25.268513
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:33.979163
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    import tempfile
    from typed_ast import ast3 as ast
    from tests.unit.utils.snippet import file_snippet
    from ..visitors.parse import parse

    source = file_snippet.get('metaclass_source')
    parsed_tree = parse(source)

    expected_tree = parse(file_snippet.get('metaclass_target'))

    transformer = MetaclassTransformer()

    result_tree = transformer.visit(parsed_tree)

    assert ast.dump(expected_tree) == ast.dump(result_tree)

    temp_file = tempfile.TemporaryFile(mode='w+', suffix='.py')
    temp_file.write(ast.unparse(result_tree))
    temp_file.seek(0)

    import sys
    import built

# Generated at 2022-06-14 02:02:43.120252
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..testing import assert_code_equal, build_visitor_testcase
    import ast
    import six

    MetaclassTransformerTestCase = build_visitor_testcase(
        MetaclassTransformer,
        'visit_ClassDef',
        {
            'metaclass': ast.Name()
        })

    # With metaclass
    with_metaclass_expectation = six.u(
        'import six as _six_imported_by_py_backwards; '
        'class A(_six_imported_by_py_backwards.with_metaclass(metaclass, object)): '
        'pass')

# Generated at 2022-06-14 02:02:50.334162
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # Define the AST
    input_ast = ast.parse("""
    class Foo(metaclass=Bar):
        pass
    """)

    # Initialize NodeTransformer
    node_transformer = MetaclassTransformer()
    new_ast = node_transformer.visit(input_ast)
    #print(astor.to_source(new_ast))

    expected_result = ast.parse("""
    class Foo(_py_backwards_six_withmetaclass(Bar)):
        pass
    """)

    assert ast.dump(new_ast) == ast.dump(expected_result)

# Generated at 2022-06-14 02:02:53.195622
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from .test_utils import make_test, compare_source
    module = """class A(metaclass=B): pass"""

# Generated at 2022-06-14 02:03:00.637460
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..utils.test import parse

    node = parse('''
        class A(metaclass=B, arg=None):
            pass
    ''')
    assert node == parse('''
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B), arg=None):
            pass
    ''')

# Generated at 2022-06-14 02:03:01.583291
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:09.497382
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from .test_compiler import compile_and_indent
    assert compile_and_indent('''
    class A(metaclass=B):
        pass
    ''') == '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    
    
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    '''


# Generated at 2022-06-14 02:03:18.773721
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.sample import SampleNodeTransformer
    from ..utils.visitor import Visitor
    from ..typing import type_of

    visitor = Visitor()
    source = """
    class A(metaclass=B):
        pass
    """

    visitor.visit_source(source, SampleNodeTransformer(MetaclassTransformer))
    answer = """
    'from six import with_metaclass as _py_backwards_six_withmetaclass\n\n\nclass A(_py_backwards_six_withmetaclass(B))\n    pass\n'
    """
    assert type_of(visitor.get_ast()) == answer

# Generated at 2022-06-14 02:03:59.301348
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    source = """
    class A(object, metaclass=B):
        pass
    """
    tree = ast.parse(source)
    node = tree.body[0]
    assert isinstance(node, ast.ClassDef)
    MetaclassTransformer(verbose=True).visit(tree)
    assert tree.body[0].bases[0].args[0].id == '_py_backwards_six_withmetaclass'
    assert tree.body[0].bases[0].args[1].id == 'B'
    assert tree.body[0].bases[0].args[2].id == 'object'
    assert not tree.body[0].keywords



# Generated at 2022-06-14 02:04:05.981952
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    class_ = ast.ClassDef(name='Test',
                          bases=[],
                          keywords=[],
                          body=[],
                          decorator_list=[])
    module = ast.Module(body=[class_])
    module_ = MetaclassTransformer(target=(2, 7)).visit(module)
    assert module_.body[1].bases[0].elts == []

# Generated at 2022-06-14 02:04:18.623655
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3 as ast
    from ..utils import parse_snippet
    tree = parse_snippet('class A(metaclass=B): pass')
    MetaclassTransformer().visit(tree)
    assert type(tree) == ast.Module
    assert len(tree.body) == 2
    import_six = tree.body[0]
    assert type(import_six) == ast.ImportFrom
    assert import_six.module == 'six'
    assert len(import_six.names) == 1
    assert import_six.names[0].name == 'with_metaclass'
    assert import_six.names[0].asname == '_py_backwards_six_withmetaclass'
    class_A = tree.body[1]
    assert type(class_A) == ast

# Generated at 2022-06-14 02:04:21.365278
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    from ..test_utils import assert_equal_code

    # Test case with a class that contains a metaclass keyword

# Generated at 2022-06-14 02:04:22.205018
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    assert MetaclassTransformer.__init__

# Generated at 2022-06-14 02:04:27.668067
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    node = ast.parse('class A(metaclass=B): pass')
    transformer = MetaclassTransformer(py_version=(2, 7))
    transformer.visit(node)
    assert transformer.tree_changed

# Generated at 2022-06-14 02:04:35.116766
# Unit test for constructor of class MetaclassTransformer
def test_MetaclassTransformer():
    assert ast.parse('pass') == MetaclassTransformer().visit(ast.parse('pass'))  # type: ignore
    assert (ast.parse("""
    class A(B):
        pass
    """) == MetaclassTransformer().visit(ast.parse("""
    class A(metaclass=B):
        pass
    """)))  # type: ignore
    assert (ast.parse("""
    class A(C, D):
        pass
    """) == MetaclassTransformer().visit(ast.parse("""
    class A(*[C, D]):
        pass
    """)))  # type: ignore

# Generated at 2022-06-14 02:04:38.934584
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    assert ast.parse("class A(metaclass=B): pass") == \
        MetaclassTransformer().visit(ast.parse("class A(metaclass=B): pass"))

# Generated at 2022-06-14 02:04:40.104210
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 02:04:49.718860
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class SimpleClassDef(ast.ClassDef):
        """A simple class node"""

        def __init__(self, metaclass, bases=()):
            super().__init__(name='MyClass', bases=[ast.AST(b) for b in bases],
                             keywords=[ast.arg(arg='metaclass', value=metaclass)],
                             body=[], decorator_list=[])

    transformer = MetaclassTransformer()
    tree = ast.Module(body=[SimpleClassDef(metaclass=ast.Name(id='B',
                                                              ctx=ast.Load()),
                                           bases=['C'])])
    tree = transformer.visit(tree)

    assert transformer._tree_changed