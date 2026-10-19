

# Generated at 2022-06-14 01:55:04.700560
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.compat import NamedConstant
    from .six import to_bytes
    from .base import BaseNodeTransformer, transform

    if six.PY2:
        unistr = unicode
        unibytes = str
    else:
        unistr = str
        unibytes = bytes

    value = to_bytes('""""MetaclassTransformer docstring""""')

    # with metaclass on Python 2
    src = """
        class A(metaclass=B):
            pass
    """
    expected = """
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """
    tree = ast.parse(textwrap.dedent(src))

# Generated at 2022-06-14 01:55:05.986366
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:06.956828
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:55:14.841972
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    transformer = MetaclassTransformer()

    module = ast.Module([
        ast.ClassDef(
            name='A',
            bases=[
                ast.Name(id='B', ctx=ast.Load())
            ],
            body=[],
            keywords=[
                ast.keyword(arg='metaclass', value=ast.Name(id='C', ctx=ast.Load()))
            ]
        )
    ], type_ignores=[])

    new_module = transformer.visit_Module(module)

# Generated at 2022-06-14 01:55:25.700294
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast as python_ast
    from ...py2bpf.translators.ast.typed_ast import ast3 as typed_ast

    # python_node = python_ast.parse('''
    #     class A(metaclass=B):
    #         pass
    # ''')
    python_node = python_ast.parse('class A(metaclass=B): pass')


    def check(python_node, py_to_bpf):
        typed_node = py_to_bpf.translate_ast(python_node)
        typede_node_string = typed_ast.ast3.dump(typed_node)
        print(typede_node_string)

    check(python_node, MetaclassTransformer())
    # MATCH: ('def _py_backwards_0_

# Generated at 2022-06-14 01:55:28.945491
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    tree = ast.parse('class A(metaclass=str): pass')
    assert tree_to_str(MetaclassTransformer().visit(tree)) == 'class A(_py_backwards_six_withmetaclass(str)): pass'


# Generated at 2022-06-14 01:55:29.784361
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:55:35.639505
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    # input
    root = ast.Module(
        body=[
            ast.ClassDef(
                name='A',
                bases=[],
                keywords=[
                    ast.keyword(
                        arg='metaclass',
                        value=ast.Name(
                            id='B',
                            ctx=ast.Load(),
                        ),
                    ),
                ],
            ),
        ],
    )
    # process
    MetaclassTransformer().visit(root)
    # output

# Generated at 2022-06-14 01:55:46.345040
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils.testutils import TestCase, sample_python_tree
    from .six import six_import
    from .base import SPECIAL_SECTIONS, Context
    from ..unparse import Unparser
    from ..resolve import ScopeVisitor

    class T(TestCase):
        maxDiff = None
        tree = None
        context = None
        scope = None

        def setUp(self) -> None:
            six_import.set_enabled(True)
            self.context = Context()
            self.context.add_section('six', six_import,
                                     *SPECIAL_SECTIONS[six_import])

            self.tree = sample_python_tree('class A(metaclass=type): pass')
            self.scope = ScopeVisitor().visit(self.tree)


# Generated at 2022-06-14 01:55:56.533292
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_ast.ast3

    A = typed_ast.ast3.ClassDef(name='A',
                                bases=[],
                                keywords=[typed_ast.ast3.keyword(arg='metaclass',
                                                                  value=typed_ast.ast3.Name(id='B',
                                                                                            ctx=typed_ast.ast3.Load()))],
                                body=[],
                                decorator_list=[])

    module = typed_ast.ast3.Module(body=[A])
    compiled = compile_ast(module, 'exec')
    # import six
    # class A:
    #     pass

# Generated at 2022-06-14 01:56:11.810414
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    import sys
    from ..utils.test_utils import parse
    mod = parse('from multiprocessing import Process\n'
                'class A(metaclass=Process): pass\n')
    mod = MetaclassTransformer(target=sys.version_info).visit(mod)

    if six.PY2:
        assert mod.body == six_import.get_body() + [ast.ClassDef(name='A',
                                                                bases=[class_bases.get_body('Process', [])],
                                                                keywords=[],
                                                                starargs=None,
                                                                kwargs=None,
                                                                body=[],
                                                                decorator_list=[])]

# Generated at 2022-06-14 01:56:13.078034
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:22.994034
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    
    import typing
    if typing.TYPE_CHECKING:
        from typed_ast import ast3 as ast
    class visitor(ast.NodeVisitor):
        pass
    
    
    class tester(visitor):
        def visit_Assign(self, node):
            assert isinstance(node, ast.Assign)
            assert len(node.targets) == 1
            assert isinstance(node.targets[0], ast.Name)
            assert node.targets[0].id == 'A'
            assert isinstance(node.value, ast.Call)
            assert isinstance(node.value.func, ast.Name)
            assert node.value.func.id == '_py_backwards_six_withmetaclass'
            assert len(node.value.args) == 2
           

# Generated at 2022-06-14 01:56:24.524939
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:56:35.265327
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class_def = ast.parse("""class A(B, C, metaclass=D): pass""").body[0]
    six_node = six_import.get_body()[0]
    class_bases_node = class_bases.get_body()
    class_bases_node.body = class_bases_node.body[1:]
    with_metaclass_call = class_bases_node.body[0]
    assert with_metaclass_call.keywords[0].arg == 'metaclass'
    with_metaclass_call.keywords[0].arg = 'metaclass'
    ast.fix_missing_locations(class_bases_node)
    expected = ast.Module(body=[six_node, class_def])
    metaclass_transformer = Met

# Generated at 2022-06-14 01:56:38.494320
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse
    from .context import Context
    from .rewrite_init import RewriteInitTransformer


# Generated at 2022-06-14 01:56:47.768809
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import run_test_node

    class_ = ast.ClassDef(
        name='A',
        keywords=[ast.keyword(arg='metaclass',
                              value=ast.Str(s='B'))],
        bases=[ast.Name(id='object', ctx=ast.Load())],
        body=[],
        decorator_list=[],
    )

    expected = ast.parse('class A(_py_backwards_six_withmetaclass(B, object)): pass')  # noqa


    assert run_test_node(class_, expected=expected) == expected

# Generated at 2022-06-14 01:56:58.219835
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse("""
    class A(metaclass=B, object=C):
        pass
    """)
    transformer = MetaclassTransformer()
    res = transformer.visit(node)

    assert transformer.changed == True
    assert transformer.dependencies == ['six']
    assert transformer.target == (2, 7)
    assert ast.dump(res).strip() == """
    from six import with_metaclass as _py_backwards_six_with_metaclass
    class A(_py_backwards_six_with_metaclass(B, [])):
    pass
    """.strip()

# Generated at 2022-06-14 01:57:05.850132
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from typed_ast import parse
    from .ast_converter import code_to_ast

    code = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B, *bases)):
        pass
    """
    test = parse(code)
    test = MetaclassTransformer.run_on_node(test)
    compare = code_to_ast.convert(code)

    assert test == compare


# Generated at 2022-06-14 01:57:16.355723
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import builtins
    node = ast.parse("""
    class Meta(type):
        pass
    
    class A(metaclass=Meta):
        pass
    """)
    transformer = MetaclassTransformer()
    transformer.visit(node)
    exec(compile(node, filename="<ast>", mode="exec"), {'__builtins__': __builtins__})  # type: ignore
    assert globals()['a'] == A
    assert globals()['A'].__name__ == 'A'
    assert globals()['A'].__bases__ == (object,)


# Generated at 2022-06-14 01:57:21.822159
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_visitor import assert_equal_source

# Generated at 2022-06-14 01:57:28.955771
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_equal_ignore_ws
    assert_equal_ignore_ws(MetaclassTransformer().visit(ast.parse('''
    class A(metaclass=B):
        pass''')), '''
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B, )):
        pass
    ''')


# Generated at 2022-06-14 01:57:35.653417
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    @six_import.register_transformer
    def mock_six_import():
        return six_import.get_body()

    @class_bases.register_transformer
    def mock_class_bases():
        return class_bases.get_body()

    target = ast.parse("""
        class A():
            pass
    """)

    expected = ast.parse("""
        from six import with_metaclass as _py_backwards_six_withmetaclass

        class A():
            pass
    """)

    assert MetaclassTransformer().visit(target) == expected



# Generated at 2022-06-14 01:57:37.141546
# Unit test for method visit_Module of class MetaclassTransformer

# Generated at 2022-06-14 01:57:48.004527
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    input = ast.parse("""\
        class A:
            pass
        class B(metaclass=type):
            pass
    """)
    expected = ast.parse("""\
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A:
            pass
        class B(_py_backwards_six_withmetaclass(type)):
            pass
    """)
    node = MetaclassTransformer().visit(input)
    assert node == expected



# Generated at 2022-06-14 01:57:51.852988
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    from ..utils import get_ast
    node = get_ast("""
    class A(metaclass=B):
        pass
    """)

    node = MetaclassTransformer().visit(node)

    from ..utils import compare_ast
    compare_ast(node, """
    import six
    class A(six.with_metaclass(B)):
        pass
    """)



# Generated at 2022-06-14 01:57:53.971628
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_runners import NodeAssertionBuilder


# Generated at 2022-06-14 01:57:56.925810
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..unittest_tools import assert_compiled_output


# Generated at 2022-06-14 01:58:02.903836
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    tree = """
    class A(metaclass=B):
        pass
    """
    exp_tree = """
    from six import with_metaclass as _py_backwards_six_withmetaclass
    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """

    assert_equal(MetaclassTransformer().visit_Module(ast.parse(tree)),
                 ast.parse(exp_tree))


# Generated at 2022-06-14 01:58:09.194442
# Unit test for method visit_Module of class MetaclassTransformer
def test_MetaclassTransformer_visit_Module():
    """Visit module."""
    ast_tree = ast.parse("class A(B, C)")
    transformed = MetaclassTransformer().visit(ast_tree)
    expected = ast.parse("from six import with_metaclass as _py_backwards_six_withmetaclass\n\nclass A(with_metaclass(_py_backwards_six_withmetaclass, B, C))")
    assert ast.dump(transformed) == ast.dump(expected)



# Generated at 2022-06-14 01:58:23.577151
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class A(six.with_metaclass(int)):
        pass

    tree = ast.parse(inspect.cleandoc("""
    class A(metaclass=int):
        pass
    """), mode='exec')

    tree = MetaclassTransformer().visit(tree)
    compiled = compile(tree, '<test>', mode='exec').co_consts[0].__dict__['__bases__']
    assert compiled == A.__bases__

# Generated at 2022-06-14 01:58:24.857376
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:58:35.069834
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.transforms.backports.metaclass_transformer import MetaclassTransformer
    from typed_ast import ast3 as ast
    import typed_ast.ast3 as typed_ast
    import sys
    import six

    # Test with simple class and metaclass as a name
    node = ast.ClassDef(name='A',
                        bases=[],
                        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B'))],
                        body=[],
                        decorator_list=[])
    result = MetaclassTransformer().visit(node)
    assert '_py_backwards_six_withmetaclass' in result.bases[0].elts

# Generated at 2022-06-14 01:58:46.637826
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils import load_test_module, parse_test_ast
    module, source = load_test_module('test_compat_metaclass', do_compile=False)
    tree = parse_test_ast(source, module)
    transformer = MetaclassTransformer()
    result = transformer.visit(tree)

    assert result.body[0].body[0].bases[0].elts[0].func.id == '_py_backwards_six_withmetaclass'
    assert result.body[0].body[0].bases[0].args[0].id == 'object'

    assert result.body[0].body[1].keywords[0].arg == 'metaclass'

# Generated at 2022-06-14 01:58:56.984523
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import ast
    import six
    import _fixtures.six_import
    import _fixtures.class_bases
    import subprocess
    import sys
    import os

    class TestMetaclassTransformer_visit_ClassDef(ast.NodeVisitor):
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                if node.func.id == '_py_backwards_six_withmetaclass':
                    assert node.args[0] is metaclass
                    assert isinstance(node.args[1], ast.Name)
                    assert node.args[1].id == 'B'
    transform = MetaclassTransformer()
    tree = ast.parse('class A(metaclass=B): pass')

# Generated at 2022-06-14 01:59:03.019536
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    fixer = MetaclassTransformer()
    class_def: ast.ClassDef = ast.parse('class A(metaclass=B):\n    pass').body[0]
    assert fixer.visit(class_def).bases.elts[0].value.args == [ast.Name(id='B')]



# Generated at 2022-06-14 01:59:11.145731
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast

    node = ast.ClassDef(name='A',
                        bases=[],
                        keywords=[ast.keyword(arg='metaclass',
                                              value=ast.Name(id='B'))],
                        body=[])
    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)
    assert new_node is not node
    assert transformer._tree_changed is True
    assert new_node == ast.ClassDef(name='A',
                                    bases=class_bases.get_body(metaclass=ast.Name(id='B'),
                                                               bases=ast.List(elts=[])),
                                    keywords=[],
                                    body=[])


# Generated at 2022-06-14 01:59:24.604799
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    a, b = mock.Mock(spec=ast.Name), mock.Mock(spec=ast.expr)
    b.id = "b"
    c = mock.Mock(spec=ast.arg)
    d = mock.Mock(spec=ast.arg)
    kw = mock.Mock(spec=ast.keyword)
    kw.value = b
    classdef = mock.Mock(spec=ast.ClassDef,
                         bases=[c],
                         keywords=[kw]
                         )
    m = MetaclassTransformer()
    with mock.patch.object(m, 'generic_visit', return_value=a):
        m.visit_ClassDef(classdef)
    assert m._tree_changed

# Generated at 2022-06-14 01:59:29.954783
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse("""
        class B:
            pass
        class A(metaclass=B):
            pass
    """)
    module2 = MetaclassTransformer(from_version='3.3').visit(module)
    exec(compile(module2, '', 'exec'), {})



# Generated at 2022-06-14 01:59:31.797722
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .util import source_to_ast

# Generated at 2022-06-14 01:59:46.531861
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 01:59:56.657326
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    """
    Test that MetaclassTransformer works as expected.
    """
    class test1(ast.AstTransformer):
        """
        Produce a ClassDef node that uses a keyword.
        """
        def visit_Module(self, node: ast.Module) -> ast.Module:
            node.body.append(ast.ClassDef(name="test1",
                                          bases=[],
                                          keywords=[ast.keyword(arg="metaclass",
                                                                value=ast.Name(id="test", ctx=ast.Load()))],
                                          body=[ast.Pass()],
                                          decorator_list=[]))
            return node

    class test2(ast.AstTransformer):
        """
        Produce a ClassDef node that uses no keyword.
        """

# Generated at 2022-06-14 01:59:58.841035
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import round_trip
    
    round_trip(MetaclassTransformer, 'class A(metaclass=B, bases=C): pass')

# Generated at 2022-06-14 02:00:08.579127
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from py_backwards.transformers.six import MetaclassTransformer, six_import
    with_metaclass = ast.Name(id="with_metaclass", ctx=ast.Load())
    six = ast.Name(id="six", ctx=ast.Load())
    B = ast.Name(id="B", ctx=ast.Load())
    node = ast.ClassDef(name="A",
                        bases=[ast.Name(id="A", ctx=ast.Load())],
                        keywords=[ast.keyword(arg="metaclass",
                                              value=B)])
    transformed_node = MetaclassTransformer().visit(node)

# Generated at 2022-06-14 02:00:17.498308
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # We need to make sure that class objects are not transformed
    source = """
    class A:
        pass
    
    class B(object):
        pass
    
    class C(object, metaclass=type):
        pass
    
    class D(metaclass=type):
        pass
    """
    assert MetaclassTransformer(source).output == """
    class A:
        pass
    
    
    
    
    
    class _py_backwards_six_withmetaclass(type, object, metaclass=type):
        pass
    
    
    class _py_backwards_six_withmetaclass(type, object, metaclass=type):
        pass
    """

# Generated at 2022-06-14 02:00:20.817988
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node = ast.parse('class A(B):pass')
    assert node == MetaclassTransformer().visit(node)



# Generated at 2022-06-14 02:00:26.221237
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    node_tree = ast.parse("class A(object, metaclass=B): pass")
    MetaclassTransformer().visit(node_tree)
    assert str(node_tree) == "class A(_py_backwards_six_withmetaclass(B)): pass\n"

# Generated at 2022-06-14 02:00:27.497351
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:00:35.087388
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from ..utils.helpers import parse_ast, compare_ast

    code = """
        class A(metaclass=B):
            pass
    """

    expected = """
        class A(_py_backwards_six_withmetaclass(B)):
            pass
    """

    tree = parse_ast(code)
    new_tree = MetaclassTransformer().visit(tree)
    assert compare_ast(ast.parse(expected), new_tree)

# Generated at 2022-06-14 02:00:41.276734
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    module = ast.parse('class A(metaclass=bool): pass')
    MetaclassTransformer().visit(module)
    assert_equal(unparse(module), textwrap.dedent('''\
        from six import with_metaclass as _py_backwards_six_withmetaclass
        class A(_py_backwards_six_withmetaclass(bool))'''))
# /test_MetaclassTransformer_visit_ClassDef

# Generated at 2022-06-14 02:01:16.767372
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import parse, round_trip
    from .six_transforms import SixTransformer
    from .with_transforms import WithTransformer

    code = '''
        class A(metaclass=B):
            with C as c:
                pass
    '''
    module = parse(code)
    tree = module.body[0]

    node = MetaclassTransformer().visit(tree)
    node = WithTransformer().visit(node)
    node = SixTransformer().visit(node)
    actual = round_trip(node)

    expected = '''
        from six import with_metaclass as _py_backwards_six_with_metaclass
        class A(_py_backwards_six_with_metaclass(B)):
            with C as c:
                pass
    '''

# Generated at 2022-06-14 02:01:23.817090
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astor
    from ..utils import parse

    # Given
    src = """
    class A(metaclass=B):
        pass
    """

    node = parse(src, 'exec')
    MetaclassTransformer().visit(node)

    exp = """
    from six import with_metaclass as _py_backwards_six_withmetaclass

    class A(_py_backwards_six_withmetaclass(B)):
        pass
    """

    # Then
    assert astor.to_source(node) == exp

# Generated at 2022-06-14 02:01:31.926912
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import sys
    import pathlib
    sys.path.insert(
        0,
        str(pathlib.Path(__file__).parent.parent)
    )
    from pynode.utils import ast_from_source, compare

    class_def = ast_from_source(
        '''class A(metaclass=B):
            pass
        '''
    )
    expected_class_def = ast_from_source(
        '''from six import with_metaclass as _py_backwards_six_withmetaclass

        class A(_py_backwards_six_withmetaclass(B)):
            pass
        '''
    )
    transformer = MetaclassTransformer()
    compare(transformer.visit(class_def), expected_class_def)

# Generated at 2022-06-14 02:01:42.432448
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    class TestTransformer(MetaclassTransformer):
        def __init__(self, node: ast.ClassDef) -> None:
            self.new_tree = node

    def test(code: str, expected: str) -> None:
        et = ast.parse(expected)
        tree = ast.parse(code)
        tx = TestTransformer(tree)
        tx.visit(tree)
        sys.stderr.write(str(et) + '\n')
        sys.stderr.write(str(tx.new_tree) + '\n')
        assert tx.new_tree == et


# Generated at 2022-06-14 02:01:44.343473
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_code_equal


# Generated at 2022-06-14 02:01:46.521612
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from .utils import transform, compare_source


# Generated at 2022-06-14 02:01:53.626826
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from . import typed_astunparse

    source = '''
    class A(metaclass=B):
        pass
    '''
    expected = '''
    class A(_py_backwards_six_with_metaclass(B))
        pass
    '''
    node = ast.parse(source)
    MetaclassTransformer.run(node)
    result = typed_astunparse.unparse(node)
    assert result == expected



# Generated at 2022-06-14 02:01:55.463595
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast.ast3 import parse

# Generated at 2022-06-14 02:01:56.762932
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:02:06.526186
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    from .utils import roundtrip_code, roundtrip_tree

    t = MetaclassTransformer()
    class_node = ast.ClassDef(name='A',
                              bases=[ast.Name(id='object')],
                              keywords=[ast.keyword(arg='metaclass',
                                                    value=ast.Name(id='B'))],
                              body=[])
    node = ast.Module(body=[class_node])
    t.visit(node)
    assert len(node.body) == 1
    assert isinstance(node.body[0], ast.ClassDef)

# Generated at 2022-06-14 02:03:18.136584
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import astunparse

    tree = ast.parse("class C(metaclass=M): pass")
    module = MetaclassTransformer().visit(tree)
    assert module.body[0].value.elts[0].value.args[0].id == 'M'
    assert astunparse.unparse(module).strip() == six_import.get_source() + class_bases.get_source(metaclass='M')

# Generated at 2022-06-14 02:03:20.020495
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils.test_utils import assert_string_equal
    from .test_utils import transform


# Generated at 2022-06-14 02:03:29.242372
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from ..utils import parse
    from ..utils.tree import dump

    tree = parse("""
    class Foo(metaclass=Meta):
        pass
    """)
    assert dump(tree) == """Module(body=[ClassDef(name='Foo', bases=[Attribute(value=Name(id='Meta', ctx=Load()), attr='__new__', ctx=Load())], keywords=[], body=[], decorator_list=[])])"""
    new_tree = MetaclassTransformer().visit(tree)

# Generated at 2022-06-14 02:03:36.142332
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    # given
    from typed_ast import ast3 as ast
    node = ast.ClassDef(name='A',
                        bases=[ast.Name(id='object', ctx=ast.Load())],
                        keywords=[ast.keyword(arg='metaclass', value=ast.Name(id='B', ctx=ast.Load()))])

    # when
    with_metaclass = MetaclassTransformer().visit(node)

    # then
    import astor
    assert astor.to_source(with_metaclass) == \
        "class A(_py_backwards_six_withmetaclass(B, object))\n"

# Generated at 2022-06-14 02:03:37.550763
# Unit test for method visit_ClassDef of class MetaclassTransformer

# Generated at 2022-06-14 02:03:45.874978
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    code = """
    class A:
        pass
    """
    expected = """
    class A:
        pass
    """
    node = ast.parse(code)
    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)
    result = ast.unparse(new_node)
    assert result == expected

    code = "class A(metaclass=B):\n    pass"
    expected = "class A(_py_backwards_six_withmetaclass(B)):\n    pass"
    node = ast.parse(code)
    transformer = MetaclassTransformer()
    new_node = transformer.visit(node)
    result = ast.unparse(new_node)
    assert result == expected

# Generated at 2022-06-14 02:03:47.736241
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast


# Generated at 2022-06-14 02:03:57.300791
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    
    source = 'class A(metaclass=B):\n    pass\n'
    tree = ast.parse(source)
    
    assert isinstance(tree, ast.Module)
    transformer = MetaclassTransformer()
    transformer.visit(tree)
    assert transformer._tree_changed is True
    
    source = source.strip()
    expected = '\n'.join(('from six import with_metaclass as _py_backwards_six_withmetaclass',
                          'class A(_py_backwards_six_withmetaclass(B)):',
                          '    pass',
                          ''))

    assert astor.to_source(tree).strip() == expected

# Generated at 2022-06-14 02:03:58.918666
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    import typed_astunparse
    from ..visitor import DOTVisitor


# Generated at 2022-06-14 02:04:08.293765
# Unit test for method visit_ClassDef of class MetaclassTransformer
def test_MetaclassTransformer_visit_ClassDef():
    from typed_ast import ast3 as ast
    node = ast.parse("class A(B, C, D, metaclass=F):\n    pass")

    tree = MetaclassTransformer()
    tree.visit(node)

    assert format_ast(node) == "from six import with_metaclass as _py_backwards_six_withmetaclass\n\n\nclass A(_py_backwards_six_withmetaclass(F, B, C, D)):\n    pass"

