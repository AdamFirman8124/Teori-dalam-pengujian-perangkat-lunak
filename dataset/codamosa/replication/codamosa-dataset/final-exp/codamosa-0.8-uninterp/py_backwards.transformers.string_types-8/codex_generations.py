

# Generated at 2022-06-14 02:17:12.527025
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # No value
    code_before = '''
string = "abc"
string2 = str(3) + str(4)
'''
    code_after = '''
string = "abc"
string2 = unicode(3) + unicode(4)
'''
    tr = StringTypesTransformer()
    result = tr.transform_code(code_before)
    assert result.code == code_after

    # None value
    code_before = '''
string = str(None) + "abc"
string2 = "abc" + str(None)
'''
    code_after = '''
string = unicode(None) + "abc"
string2 = "abc" + unicode(None)
'''
    tr = StringTypesTransformer()
    result = tr.transform_code(code_before)
   

# Generated at 2022-06-14 02:17:16.897201
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer('str') == 'unicode'
    assert StringTypesTransformer('str_1') == 'str_1'
    assert StringTypesTransformer('def str(self):') == 'def unicode(self):'

# Generated at 2022-06-14 02:17:21.680441
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = """
        def foo():
            a = str("hello")
    """
    expected_result = """
        def foo():
            a = unicode("hello")
    """

    tree = ast.parse(src)
    new_tree = StringTypesTransformer.run_it(tree)

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected_result))

# Generated at 2022-06-14 02:17:25.375693
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Given
    class Foo: pass


# Generated at 2022-06-14 02:17:29.186611
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree_in = ast.parse("str")
    tree_correct = ast.parse("unicode")
    tree_test = StringTypesTransformer.transform(tree_in).tree
    assert ast.dump(tree_correct) == ast.dump(tree_test)

# Unit test that transformer actually changes the tree

# Generated at 2022-06-14 02:17:30.047481
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:34.772546
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .test_helpers import expect_no_additional_import_statements, get_example_tree, roundtrip

    tree = get_example_tree(arguments=['2.7'])

    roundtrip(tree, StringTypesTransformer)

    expect_no_additional_import_statements(tree)


# Generated at 2022-06-14 02:17:44.751472
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    # test1
    tree = ast.parse('print(str(2))')
    new_tree, tree_changed, _ = StringTypesTransformer.transform(tree)
    assert tree_changed == True, 'tree_changed should be True'
    assert isinstance(new_tree, ast.AST) and isinstance(tree, ast.AST) and new_tree.body[0].value.func.id == 'str', 'str should be unicode'

    # test2
    tree = ast.parse('print(str(2))')
    new_tree, tree_changed, _ = StringTypesTransformer.transform(tree)
    assert tree_changed == True, 'tree_changed should be True'

# Generated at 2022-06-14 02:17:47.823815
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astunparse
    import sys

    tree = ast.parse("str(arg)")

    if sys.version_info[0] == 2:
        assert astunparse.unparse(StringTypesTransformer.transform(tree).tree) == 'unicode(arg)'

# Unit tests for transformer StringTypesTransformer

# Generated at 2022-06-14 02:17:51.819816
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("a = str(b)")
    t = StringTypesTransformer()
    tree = t.transform(tree)
    assert(str(tree) == "a = unicode(b)")

# Generated at 2022-06-14 02:17:58.189874
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_ast

    code = '''
from typed_ast import ast3 as ast
ast.parse('x = str(None)')
'''
    tr = StringTypesTransformer()
    r = tr.transform(source_to_ast(code))
    assert r.changed

# Generated at 2022-06-14 02:18:02.278551
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import check_transformer

    tree = ast.parse("""x = "abc" + str(123) + str(456)""")
    check_transformer(StringTypesTransformer, tree)

# Generated at 2022-06-14 02:18:10.123358
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
        def foo():
            return str('bar')
    """
    module2 = ast.parse(source)
    expected = """
        def foo():
            return unicode('bar')
    """
    module3 = ast.parse(expected)
    t = StringTypesTransformer()
    result = t.transform(module2)
    compare_ast(result.tree, module3)

# Generated at 2022-06-14 02:18:15.024895
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test for function transform
    result = StringTypesTransformer.transform(ast.parse("a = str('test')"))
    assert result.tree_changed
    assert result.messages == []
    assert result.tree == ast.parse("a = unicode('test')")

# Generated at 2022-06-14 02:18:23.409178
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer('print(str(x))') == "print(unicode(x))"
    assert StringTypesTransformer('print(str(x) + str(y))') == "print(unicode(x) + unicode(y))"
    assert StringTypesTransformer('def f(x: str):\n    x + str(1)') == 'def f(x: unicode):\n    x + unicode(1)'

# Generated at 2022-06-14 02:18:26.320312
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import transform

    input = """
    x = str()
    """

    expected = """
    x = unicode()
    """

    assert expected == transform(input, [(StringTypesTransformer, {})])

# Generated at 2022-06-14 02:18:29.296897
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    src = """str"""
    res = StringTypesTransformer(src)
    assert res == "unicode"

# Generated at 2022-06-14 02:18:36.167629
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse('print(str() + "Bar")')
    result = StringTypesTransformer.transform(t)

    assert result.tree_changed
    assert str(result.tree) == "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Call(func=Name(id='unicode', ctx=Load()), args=[], keywords=[]), op=Add(), right=Str(s='Bar')), keywords=[]))])"
    assert result.warnings == []

# Generated at 2022-06-14 02:18:39.396509
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    tree = astor.parse_file('example.py')
    new_tree = StringTypesTransformer.transform(tree)
    assert(new_tree.tree != tree)

# Generated at 2022-06-14 02:18:42.275584
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    print('In StringTypesTransformer unit tests')
    assert StringTypesTransformer is not None
    assert StringTypesTransformer.__class__ is StringTypesTransformer



# Generated at 2022-06-14 02:18:51.937622
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # To test this transformer, we'll convert this code:
    tree = ast.parse("""
a = str(b) if b is str else ""
""")
    # In this code:
    expected_tree = ast.parse("""
a = unicode(b) if b is unicode else ""
""")
    result = StringTypesTransformer.transform(tree)
    assert result.tree == expected_tree
    assert not result.errors
    assert result.tree_changed

# Generated at 2022-06-14 02:19:03.362505
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    import typed_ast.ast3 as typed_ast
    typ = StringTypesTransformer()

    x = typed_ast.Name(id="str")
    y = typ.visit(x)
    assert y.id == "unicode"
    assert not isinstance(y, typed_ast.Name)

    
    class TreeWrapper(object):
        def __init__(self, node_):
            self.node = node_

    x = TreeWrapper(typed_ast.Name(id="str"))
    y = typ.visit(x)
    assert y.node.id == "unicode"
    assert not isinstance(y.node, typed_ast.Name)
    assert isinstance(y, TreeWrapper)

    x = typed_ast.Name(id="str")

# Generated at 2022-06-14 02:19:16.182121
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit test for StringTypesTransformer
    """
    import typed_ast.ast3
    tree = typed_ast.ast3.parse('def foo(x): return str(x)')

    StringTypesTransformer.transform(tree)

# Generated at 2022-06-14 02:19:21.634309
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Initialize a StringTypesTransformer instance
    transformer = StringTypesTransformer()

    # Initialize a Python 2 AST
    node = ast.Name(id='str', ctx=ast.Load())

    # Transform Python 2 AST
    node_transformed, tree_changed, _ = transformer.transform(node)

    # Ensure correct result
    assert(node_transformed is not None)
    assert(isinstance(node_transformed, ast.Name))
    assert(isinstance(tree_changed, bool))
    assert(tree_changed)

# Generated at 2022-06-14 02:19:27.964661
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
s = str(s)
l = [s1, s2]
""")
    out = StringTypesTransformer.transform(tree)
    src = astunparse.unparse(out.tree)
    # check if the transformer has modified the source code as expected
    assert src == """
s = unicode(s)
l = [s1, s2]
"""

# Generated at 2022-06-14 02:19:32.442912
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "print('some string')"
    tree = ast.parse(code)
    print(astor.to_source(tree))
    StringTypesTransformer.transform(tree)
    source = astor.to_source(tree)
    print(source)
    assert source == "print(u'some string')\n"

if __name__ == "__main__":
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:19:38.756680
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:47.360142
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('''hasattr(cls, '__%s__' % name)''')) == TransformationResult(None, False, [])
    assert StringTypesTransformer.transform(ast.parse('''if type(func).__name__ == 'instancemethod':''')) == TransformationResult(None, False, [])
    assert StringTypesTransformer.transform(ast.parse('''if type(func).__name__ == 'function':''')) == TransformationResult(None, False, [])
    assert StringTypesTransformer.transform(ast.parse('''if type(func).__name__ == 'builtin_function_or_method':''')) == TransformationResult(None, False, [])

# Generated at 2022-06-14 02:19:57.196846
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():

    # Unit test for class method transform() of class StringTypesTransformer
    def test_transform():
        original_source = 'str'
        expected_source = 'unicode'
        tree = ast.parse(original_source)
        tree_copy = copy.deepcopy(tree)
        result = StringTypesTransformer.transform(tree_copy)
        assert result.tree != tree
        assert result.tree_changed == True
        assert ast.dump(tree_copy) == ast.dump(tree)
        assert ast.dump(result.tree) == ast.dump(ast.parse(expected_source))

    test_transform()

# Generated at 2022-06-14 02:20:07.196426
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    t = ast.parse(dedent('''\
    def foo(bar):
        return str(bar)
    '''))
    tt = StringTypesTransformer().visit(t)
    #print(ast.dump(tt, include_attributes=True))

# Generated at 2022-06-14 02:20:17.593805
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import parse
    transformer = StringTypesTransformer()

    code = 'str("toto")'
    tree = parse(code)
    new_tree, changed = transformer.transform(tree)

    assert changed is True
    assert isinstance(new_tree, ast.AST)
    assert transformer.name == "StringTypesTransformer"

# Generated at 2022-06-14 02:20:20.781999
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = "def foo(): print(str('Hello'))\n"
    result = StringTypesTransformer.transform(astor.parse_string(code))
    print(astor.to_source(result.tree))

if __name__ == "__main__":
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:20:23.875517
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("x = str(1)"))[0] == ast.parse("x = unicode(1)")

# Generated at 2022-06-14 02:20:32.452083
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'x = "foo"\nstr(y)'

    expected = 'x = "foo"\nunicode(y)'

    # Make sure the transformer works as expected
    result, tree_changed = StringTypesTransformer(2, 7).transform_code(code)
    assert(result == expected)

    # Make sure the transformer does not change code unnecessarily
    result, tree_changed = StringTypesTransformer(3, 6).transform_code(code)
    assert(result == code)
    assert(not tree_changed)

# Generated at 2022-06-14 02:20:43.240685
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_astunparse
    from ..scope import Scope
    from ..transformers import TransformationError
    from .string import StringTransformer

    tree = ast.parse("""
x = str()
    """)
    tree = StringTransformer.run(tree, Scope.from_node(tree))

    # test changes str -> unicode
    t = StringTypesTransformer.run(tree, Scope.from_node(tree))
    assert typed_astunparse.dump(t) == "x = unicode()\n"

    # test raises error when no str() is found
    tree = ast.parse("""
x = str()
    """)
    with pytest.raises(TransformationError):
        StringTypesTransformer.run(tree, Scope.from_node(tree))

# Generated at 2022-06-14 02:20:48.771513
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # If a class is defined, then the class name is used.
    string_types_transformer = StringTypesTransformer()

    assert (string_types_transformer.name == 'StringTypesTransformer')
    assert (string_types_transformer.target == (2, 7))


# Unit tests for transform()

# Generated at 2022-06-14 02:20:57.719735
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import textwrap

    prog = textwrap.dedent('''\
    """This is a test"""
    from __future__ import print_function

    x = (type(1), str, int, float)
    THE_ANSWER = 42
    ''')

    tree = ast.parse(prog)
    transformer = StringTypesTransformer()
    new_tree = transformer.visit(tree)

    assert new_tree is not None

    code = compile(new_tree, filename="<test>", mode="exec")
    globals_ = {}
    locals_ = {}
    exec(code, globals_, locals_)

    assert len(locals_['x']) == 4
    assert locals_['x'][0] == type(1)
    assert locals_['x'][1] == unicode
    assert locals

# Generated at 2022-06-14 02:21:04.306989
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    '''Tests that function works as expected'''
    t = ast.parse('def test():\n  print str("123")')
    tree_changed = StringTypesTransformer.transform(t)
    assert t == ast.parse('def test():\n  print unicode("123")')
    assert tree_changed is True
test_StringTypesTransformer()

# Generated at 2022-06-14 02:21:12.552708
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test case for constructor of class StringTypesTransformer.

    """
    tree = ast.parse("""
    my_str = 'bla'
    """)

    tree.name = '<unnamed>'

    tree_str = ast.dump(tree)

    assert 'bla' in str(tree)

    assert 'name' in tree.body[0].value.s

    transformer = StringTypesTransformer()

    res = transformer.transform(tree)

    assert 'bla' not in str(tree)

    assert 'unicode' in str(res.tree)

    assert 'bla' in str(res.tree)

    assert res.tree.body[0].value.s == 'bla'

    assert 'name' not in res.tree.body[0].value.s


# Generated at 2022-06-14 02:21:20.224862
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # __init__
    assert isinstance(StringTypesTransformer('https://example.com'),
                      StringTypesTransformer)
    # transform
    tree = ast.parse('str')
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert isinstance(result.tree, ast.AST)
    # Bad input
    with pytest.raises(TypeError) as excinfo:
        StringTypesTransformer.transform(None)
    assert 'AST' in str(excinfo.value)

# Generated at 2022-06-14 02:21:35.920355
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .. import transform
    from ..utils.tests.test_utils import assert_correct_transformation

    code = 'x = str()'
    expected = 'x = unicode()'

    assert_correct_transformation(StringTypesTransformer, code, expected)

# Generated at 2022-06-14 02:21:38.647605
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test 1: Constructor
    StringTypesTransformer()

    # Test 2: Check generation of class name
    assert StringTypesTransformer.get_name() == 'StringTypesTransformer'

# Generated at 2022-06-14 02:21:45.246847
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    ast_string = '''
        s = str(10)
        c = callable(s)
    '''

    expected_ast_string = '''
        s = unicode(10)
        c = callable(s)
    '''

    tr = StringTypesTransformer()
    actual_ast = tr.transform(ast_string)
    expected_ast = ast_string
    assert expected_ast == str(ast.parse(actual_ast))

# Generated at 2022-06-14 02:21:54.526250
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..types import TransformationResult
    import astor
    tree = ast.parse('x = str(0)')
    tree_copy = tree.copy()
    res = StringTypesTransformer().transform(tree)
    assert isinstance(res, TransformationResult)
    assert astor.to_source(res.transformed_tree) == 'x = unicode(0)\n'
    assert res.transformed_tree is not tree, 'Tree was not copied properly'
    assert astor.to_source(tree) == astor.to_source(tree_copy), 'Tree was changed when it should not have been'
    assert res.tree_changed == True

# Generated at 2022-06-14 02:21:56.881653
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert "ThisIsNotAString".startswith("ThisIsNotA")
    assert 'ThisIsNotAString'.startswith('ThisIsNotA')

# Generated at 2022-06-14 02:21:57.938060
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:22:07.714593
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from ...tests.programs.utils import build_program_from_ast
    from .string_formatting import StringFormattingTransformer

    code = '''def fn(x):\n    print(str(x))'''
    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    py_code = astor.to_source(tree)
    assert py_code == 'def fn(x):\n    print(unicode(x))'
    build_program_from_ast(tree)

    code = '''def fn(x):\n    print(str(x))'''
    tree = ast.parse(code)
    program = build_program_from_ast(tree)
    StringTypesTransformer.transform_program(program)
    py_code = astor.to

# Generated at 2022-06-14 02:22:13.809543
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import get_ast, dump_ast
    from ..utils import roundtrip

    code = """a = str(a)"""
    tree = get_ast(code)

    assert dump_ast(tree) == dump_ast(roundtrip(tree, [StringTypesTransformer]))


# Generated at 2022-06-14 02:22:17.431838
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("test = str()")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert result.node_changed == [ast.Name(id='str', ctx=ast.Load())]
    assert result.tree == ast.parse("test = unicode()")

# Generated at 2022-06-14 02:22:24.656069
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    def main(arg):
        return arg.decode('utf-8')
    """
    target = """
    def main(arg):
        return unicode(arg, "utf-8")
    """
    tree = ast.parse(code)
    new_tree = StringTypesTransformer.run_on(tree)
    ast.fix_missing_locations(new_tree)
    assert ast.dump(new_tree) == ast.dump(ast.parse(target))

# Generated at 2022-06-14 02:22:52.411412
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code_str = """a = str(x)"""

    expected_result = """a = unicode(x)"""

    tree = ast.parse(code_str)
    assert StringTypesTransformer.transform(tree).code == expected_result

# Generated at 2022-06-14 02:22:54.644604
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # arrange
    from ..utils.source import source_to_str_ast

# Generated at 2022-06-14 02:23:02.006383
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        x = str()
        f(foo=str())
        """
    parser = ast.PyCF_ONLY_AST
    tree = ast.parse(code, parser, mode='exec')
    expected_tree = ast.parse("""
        x = unicode()
        f(foo=unicode())
        """, parser, mode='exec')
    StringTypesTransformer.transform(tree)
    assert_equal(ast.dump(tree, include_attributes=True), ast.dump(expected_tree, include_attributes=True))
    # TODO: Compare without line numbers when that's actually implemented for dump

# Generated at 2022-06-14 02:23:04.116399
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from ..utils import parse
    from pprint import pprint


# Generated at 2022-06-14 02:23:11.221754
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source_code = "for i in range(5):\n print(str(i))"
    expected_source_code = "for i in range(5):\n print(unicode(i))"
    tree = ast.parse(source_code)
    StringTypesTransformer.transform(tree)
    new_tree = ast.parse(expected_source_code)
    assert ast.dump(tree) == ast.dump(new_tree)

# Generated at 2022-06-14 02:23:15.266538
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
        def foo() -> str:
            return 'foo'
    '''
    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)

    new_code = '''
        def foo() -> unicode:
            return 'foo'
    '''
    new_tree = ast.parse(new_code)

    assert result.tree_changed
    assert result.tree.body[0].returns.id == 'unicode'
    assert result.tree == new_tree

# Generated at 2022-06-14 02:23:25.148678
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils import check_pre_post_transform
    code = """
        assert type(str()) == str
        assert type(str('')) == str
        assert type(str(123)) == str
        assert type(str(True)) == str
        assert type(str([1, 2, 3])) == str
        assert type(str((1, 2, 3))) == str
        assert type(str({'1': 2})) == str
    """
    check_pre_post_transform(code, 2, 7, StringTypesTransformer)

# Generated at 2022-06-14 02:23:31.633634
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Unit tests for constructor of class StringTypesTransformer. 
    
    """
    # import ast
    import astor
    # from typed_ast import ast3 as ast


    tree = ast.parse('''
        a = str()
    ''')

    tree = StringTypesTransformer.transform(tree)

    print(astor.to_source(tree))

# Generated at 2022-06-14 02:23:38.672009
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .util import round_trip
    from ..parser import PythonParser

    source = "the_str"
    parsed = PythonParser(2, 7).parse(source)
    fixed = round_trip(parsed, StringTypesTransformer)
    assert fixed == "the_unicode"

if __name__ == '__main__':
    test_StringTypesTransformer()

# Generated at 2022-06-14 02:23:47.596719
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('a = str()')
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed
    assert result.name == 'StringTypesTransformer'
    assert result.messages == []

    # 'unicode' -> 'str'
    assert ast.dump(result.tree) == "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Name(id='unicode', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:24:39.606569
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('str')
    result = StringTypesTransformer.transform(tree)
    assert result.tree == ast.parse('unicode')
    assert result.changed

# Generated at 2022-06-14 02:24:42.459326
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = 'str'

    tree = ast.parse(code)
    StringTypesTransformer.transform(tree)
    assert code == 'unicode'

# Generated at 2022-06-14 02:24:45.134607
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    StringTypesTransformer.run_test('def foo(x):\n    return str(x)', 'def foo(x):\n    return unicode(x)')

# Generated at 2022-06-14 02:24:51.478834
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test function for StringTypesTransformer class.
    
    """
    t = StringTypesTransformer()
    expected_result1 = TransformationResult(ast.parse('unicode = str'), True, [])
    code = 'str = str'
    result1 = t.transform(ast.parse(code))
    assert result1 == expected_result1, "Expected: {}, found: {}".format(expected_result1, result1)



# Generated at 2022-06-14 02:24:55.539590
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Test(object):
        def __init__(self):
            pass

    # If a = 'string', a == type(a)
    assert Test(1)

# Generated at 2022-06-14 02:24:57.830196
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast
    from .base import BaseTransformerTest
    

# Generated at 2022-06-14 02:25:01.990426
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Setup
    import ast

    # Exercise
    transformer = StringTypesTransformer.from_version(2, 7)
    node = ast.Name("str", ast.Load())
    
    # Verify
    assert transformer.transform(node).tree == ast.Name("unicode", ast.Load())


# Generated at 2022-06-14 02:25:04.093239
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:25:04.965491
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

# Generated at 2022-06-14 02:25:09.035798
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.source import source_to_tree
    from .base import BaseTestTransformer

    class TestStringTypesTransformer(BaseTestTransformer):
        target_tree = source_to_tree("""
        str
        """)

        expected_tree = source_to_tree("""
        unicode
        """)

    TestStringTypesTransformer(StringTypesTransformer).test()