

# Generated at 2022-06-14 02:16:58.915547
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert True

# Generated at 2022-06-14 02:17:01.833501
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """
a = 'hello world'
"""
    
    module = ast.parse(source)
    expected = """
a = u'hello world'
"""
    
    assert StringTypesTransformer.transform(module) == expected

# Generated at 2022-06-14 02:17:10.268826
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..types import TransformedFileContent

    file_lines = ['var = str(32)\n']
    file_content = TransformedFileContent('<string>', ''.join(file_lines))
    tree = ast.parse(file_content.source_code)
    result = StringTypesTransformer.transform(tree)

    tree = ast.parse('var = unicode(32)\n')

    assert result.tree == tree
    assert result.file_content.source_code == file_content.source_code

# Generated at 2022-06-14 02:17:13.064452
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class Foo:
        def __init__(self):
            pass


    # Assert that the class can be instantiated
    assert(StringTypesTransformer() is not None)

# Generated at 2022-06-14 02:17:22.287439
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..parse import parse
    from .base import BaseTransformerTest

    source = """foo = str('bar')"""

    expected_tree = ast.Module(
        body=[
            ast.Assign(
                targets=[
                    ast.Name(id='foo', ctx=ast.Store())
                ],
                value=ast.Call(
                    func=ast.Name(id='unicode', ctx=ast.Load()),
                    args=[
                        ast.Str(s='bar')
                    ],
                    keywords=[],
                    starargs=None,
                    kwargs=None
                )
            )
        ]
    )

    class TestTransformer(StringTypesTransformer, BaseTransformerTest):
        pass

    ast_tree = parse(source)
    TestTransformer.check_tree(ast_tree, expected_tree)

# Generated at 2022-06-14 02:17:32.765183
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = '''
        import typing

        class MyClass:
            def __init__(self, text: str):
                self.text = text
    '''
    tree = ast.parse(source)
    transformer = StringTypesTransformer()
    new_tree = transformer.visit(tree)

    expected_source = '''
        import typing

        class MyClass:
            def __init__(self, text: unicode):
                self.text = text
    '''

    assert ast.dump(new_tree, include_attributes=True, annotate_fields=True) == ast.dump(expected_source, include_attributes=True, annotate_fields=False)


# Generated at 2022-06-14 02:17:41.340605
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('''
x = "unicode"
''')
    assert ast.dump(tree) == ast.dump(StringTypesTransformer.transform(tree).tree) 

if __name__ == '__main__':
    tree = ast.parse('''
x = "unicode"
''')
    assert ast.dump(tree) == ast.dump(StringTypesTransformer.transform(tree).tree) 
    print(ast.dump(tree))

    tree = ast.parse('''
x = str
''')
    assert ast.dump(tree) == ast.dump(StringTypesTransformer.transform(tree).tree) 
    print(ast.dump(tree))

# Generated at 2022-06-14 02:17:41.921315
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    pass

# Generated at 2022-06-14 02:17:42.847346
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:17:44.548796
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
  """ Tests the constructor of `StringTypesTransformer` class. """
  assert StringTypesTransformer.target == (2, 7)

# Generated at 2022-06-14 02:17:55.068218
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast
    from textwrap import dedent

    # test case
    code = dedent('''\
    def foo():
        assert isinstance(b'', str)
        assert isinstance(u'', unicode)
    ''')

    expected_result = dedent('''\
    def foo():
        assert isinstance(b'', unicode)
        assert isinstance(u'', unicode)
    ''')

    # test
    succ, result, _err = StringTypesTransformer.transform_snippet(code, target=(2, 7))
    if not succ:
        raise RuntimeError(result)
    assert result == expected_result

    # test using AST
    ast_tree = ast.parse(code)
    transformed = StringTypesTransformer.transform(ast_tree)

# Generated at 2022-06-14 02:17:57.956828
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.testing import assert_transformer
    assert_transformer(StringTypesTransformer())

# Generated at 2022-06-14 02:17:59.012261
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:02.729524
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Expected result:
    tree_expected = ast.parse("unicode('a')")
    # Test input:
    tree_test = ast.parse("str('a')")
    StringTypesTransformer.transform(tree_test)
    assert ast.dump(tree_expected) == ast.dump(tree_test)

# Generated at 2022-06-14 02:18:03.905511
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:04.837640
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:13.214619
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    source = """str(obj)"""

    tree = ast.parse(source)
    tree = StringTypesTransformer.transform(tree)[0]
    assert ast.dump(tree) == "Module(body=[Expr(value=Call(func=Name(id='unicode', ctx=Load()), args=[Name(id='obj', ctx=Load())], keywords=[], starargs=None, kwargs=None))])"

# Generated at 2022-06-14 02:18:15.024284
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Testing for the constructor of class StringTypesTransformer."""

# Generated at 2022-06-14 02:18:17.544823
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.cst_parser import parse_module
    from ..utils.tree import find

# Generated at 2022-06-14 02:18:27.095954
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test if the `unicode` not working if using python 3.x
    if sys.version_info.major == 3:
        return

    code = """
            old_string = 'This is a string' 
            new_string = unicode('This is a string')
            """
    expected_code = """
            old_string = 'This is a string' 
            new_string = unicode('This is a string')
            """
    # python 2.x does not support typing, so we disable warnings
    module, _ = astor.parse_file(io.StringIO(textwrap.dedent(code)),
                                 ignore_errors=True,
                                 mode="exec")
    StringTypesTransformer.apply(module)

# Generated at 2022-06-14 02:18:31.793679
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer(ast.parse('a = str()')).transform().code == 'a = unicode()'

# Generated at 2022-06-14 02:18:32.839630
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:18:37.337028
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
  global tree_str
  tree_str = """a = "Hello" """
  print(tree_str)
  tree = ast.parse(tree_str)
  new_tree = StringTypesTransformer.transform(tree).tree
  print(ast.dump(new_tree, include_attributes=True))

#test_StringTypesTransformer()

# Generated at 2022-06-14 02:18:40.715535
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse('def f(x): pass')
    tree_changed = StringTypesTransformer.transform(tree)
    assert tree_changed.tree_changed

# Generated at 2022-06-14 02:18:45.755471
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("""
a = str('string')
b = str('string')
    """)
    tree = StringTypesTransformer.run_pipeline(tree)
    assert ast.dump(tree) == ast.dump(ast.parse("""
a = unicode('string')
b = unicode('string')
    """))

# Generated at 2022-06-14 02:18:49.960792
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
        def example():
            return str('Unicode')
    """
    expected = """
        def example():
            return unicode('Unicode')
    """
    result = StringTypesTransformer.run_test(code)
    assert result == expected

# Generated at 2022-06-14 02:18:52.596412
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert transformer.transform(ast.parse("str('hello')")) \
           == TransformationResult(ast.parse("unicode('hello')"), True, [])

# Generated at 2022-06-14 02:18:54.607538
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse("a = str(b)")).tree_changed
    assert not StringTypesTransformer.transform(ast.parse("c = d")).tree_changed


# Generated at 2022-06-14 02:18:58.735936
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    text = "s = str(2)"
    tree = ast.parse(text)
    result = TransformationResult.run_transformer(tree, StringTypesTransformer)
    assert result.tree_changed
    assert result.transformed_text == "s = unicode(2)"

# Generated at 2022-06-14 02:19:06.808209
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    s = StringTypesTransformer()
    x = ast.parse('"Hello, World!"')
    y = ast.parse('"Hello, World!"')
    s.transform(y)
    assert ast.dump(x) == ast.dump(y)
    x = ast.parse('str(5)')
    y = ast.parse('str(5)')
    s.transform(y)
    assert ast.dump(x) == ast.dump(y)
    x = ast.parse('str')
    y = ast.parse('str')
    s.transform(y)
    assert ast.dump(x) != ast.dump(y)

# Generated at 2022-06-14 02:19:19.709852
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = '''
if __name__ == '__main__':
    a = str(1)
    b = str(a)
    c = str()
    d = [str(e) for e in [1, 2, 3]]
    f = [g for g in [1, 2, 3] if str(g) == 'g']
    '''
    tree = ast.parse(code)
    tree = StringTypesTransformer.transform(tree)
    exec(compile(tree, '', 'exec'))
    assert a == '1'
    assert b == '1'
    assert c == ''
    assert d == ['1', '2', '3']
    assert f == []

# Generated at 2022-06-14 02:19:25.758480
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.test_utils import transform_test
    from ..utils import top_level
    from .. import transformations

    source = r"""
x = str
"""

    tranformed_code = r"""
x = unicode
"""

    transform_test(source,
                   tranformed_code,
                   [StringTypesTransformer, transformations.RemovePassTransformation()],
                   top_level)
    


# Generated at 2022-06-14 02:19:26.670914
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:19:31.006466
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test StringTypesTransformer.

    """
    tree = ast.parse('def foo(s: str): pass', mode='exec')
    assert StringTypesTransformer.transform(tree).tree == ast.parse('def foo(s: unicode): pass', mode='exec')

# Generated at 2022-06-14 02:19:35.708192
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor

    code = """
    foo = str()
    """
    expected_code = """
    foo = unicode()
    """

    tree = ast.parse(code)
    result = StringTypesTransformer.transform(tree)

    assert astor.to_source(result.tree) == expected_code
    assert result.tree_changed == True
    assert result.new_imports == []

# Generated at 2022-06-14 02:19:45.626465
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class X(StringTypesTransformer):
        pass

    print('Test for class StringTypesTransformer')

    ####
    print('\nTesting for target = (2, 7)')
    X.target = (2, 7)
    assert isinstance(X.target, tuple)
    assert X.target == (2, 7)
    ####

    ####
    print('\nTesting for str -> unicode')
    code = 'a=str(input())'
    expected_code = 'a=unicode(input())'
    tree = ast.parse(code)
    x = X().visit(tree)
    assert x.tree_changed == True
    result_code = compile(x.tree, '', 'exec')
    exec(result_code)

# Generated at 2022-06-14 02:19:55.505121
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..main import transform
    import textwrap

    source = textwrap.dedent('''\
    def test():
        a = str(5)
        print(a)
    ''')
    expected = textwrap.dedent('''\
    def test():
        a = unicode(5)
        print(a)
    ''')

    with open('test.py', 'w') as f:
        f.write(source)
    
    tree = ast.parse(source)
    new_tree = transform(tree, '2.7')

    assert ast.dump(new_tree) == ast.dump(ast.parse(expected))

# Generated at 2022-06-14 02:20:02.669935
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ast import parse
    from ..utils.source import generate_source

    source = 'x = "hello" if True else str(4)'
    tree = parse(source)
    newTree = StringTypesTransformer.transform(tree)

    assert (generate_source(newTree.tree) == 'x = "hello" if True else unicode(4)')
    assert (newTree.tree_changed == True)

# Generated at 2022-06-14 02:20:07.578335
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    class_name = 'StringTypesTransformer'
    class_obj = eval(class_name)
    assert isinstance(class_obj, type)
    assert issubclass(class_obj, BaseTransformer)
    instance_obj = class_obj()
    assert isinstance(instance_obj, BaseTransformer)


# Generated at 2022-06-14 02:20:19.342169
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test StringTypesTransformer.

    """
    ls = [
        'str = "hello"',
        "print(str)"
    ]
    ls = [ast.parse(line) for line in ls]
    tree = ast.Module(body=ls)

    res = StringTypesTransformer.transform(tree)
    mod = ast.fix_missing_locations(res.tree)

    ls_expected = [
        'unicode = "hello"',
        "print(unicode)"
    ]
    ls_expected = [ast.parse(line) for line in ls_expected]
    tree_expected = ast.Module(body=ls_expected)

    assert ast.dump(mod) == ast.dump(tree_expected)

# Generated at 2022-06-14 02:20:42.304533
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Case 1
    input_str = "a = str('123')"
    tree = ast.parse(input_str)
    res = StringTypesTransformer.transform(tree)
    assert res.new_code == "a = unicode('123')"

    # Case 2
    input_str = "def words(c, d):\n    return str(c + d)"
    tree = ast.parse(input_str)
    res = StringTypesTransformer.transform(tree)
    assert res.new_code == "def words(c, d):\n    return unicode(c + d)"

    # Case 3
    input_str = "a = str()\nb = str('1')"
    tree = ast.parse(input_str)
    res = StringTypesTransformer.transform(tree)
    assert res.new_

# Generated at 2022-06-14 02:20:50.281197
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    sample = """
        def f():
            return unicode('s')
            return str(1)
    """
    expected = """
        def f():
            return unicode('s')
            return unicode(1)
    """
    tree = ast.parse(textwrap.dedent(sample))
    new_tree = StringTypesTransformer.run_on_single_file(tree)
    assert ast.dump(new_tree) == textwrap.dedent(expected)

# Generated at 2022-06-14 02:20:58.241832
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .utils import transform, ast_to_source
    from ..types import TransformationResult

    tree = transform("s = 'a'")[0]
    ns = {'unicode': str}
    exec(compile(tree, filename="<ast>", mode="exec"), ns)
    assert ns['s'] == 'a'

    tree = transform("s = str('a')")[0]
    ns = {'unicode': str}
    exec(compile(tree, filename="<ast>", mode="exec"), ns)
    assert ns['s'] == 'a'

    tree = transform("s = str(unicode('a'))")[0]
    ns = {'unicode': str}
    exec(compile(tree, filename="<ast>", mode="exec"), ns)

# Generated at 2022-06-14 02:20:59.238909
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:21:06.791669
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    text = "str('a')"
    tree = ast.parse(text)
    assert text == astor.to_source(StringTypesTransformer.transform(tree).tree)
    return True


# if __name__ == '__main__':
#     import sys
#     text = "str('a')"
#     tree = ast.parse(text)
#     print astor.to_source(StringTypesTransformer.transform(tree).tree)

# Generated at 2022-06-14 02:21:11.125727
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    code = """
    def foo():
        x = str(3)
        return x
    """
    expected_code = """
    def foo():
        x = unicode(3)
        return x
    """
    tree = ast.parse(code)
    transformed_tree, tree_changed = StringTypesTransformer.transform(tree)
    assert expected_code == astunparse.unparse(transformed_tree)

# Generated at 2022-06-14 02:21:16.755882
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("def foo(s: str): pass")

    transformer = StringTypesTransformer.default_factory()
    result = transformer.visit(tree)
    
    assert result.tree.body[0].args.args[0].annotation.id == 'unicode'
    assert result.changed

# Generated at 2022-06-14 02:21:24.481003
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3
    from ..utils.source import source_to_ast
    filename = "tests/fixtures/StringTypesTransformer.py"
    tree = source_to_ast(filename)

    StringTypesTransformer.transform(tree)
    assert(type(tree.body[0].type) == ast3.Name)

# Generated at 2022-06-14 02:21:29.943687
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert 'cdef unicode x' == codetransformer.to_source(
        StringTypesTransformer.transform(
            codetransformer.from_source('cdef str x')[0]
        )[0]
    )

# Generated at 2022-06-14 02:21:36.133198
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    from ..main import compile_ast
    source = "name = 'Isaac'\nprint(type(name))"
    tree = ast.parse(source)
    StringTypesTransformer.transform(tree)

    assert astor.to_source(tree).startswith(
        "name = u'Isaac'\nprint(type(name))"
    )

# Generated at 2022-06-14 02:22:08.343574
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.ast import parse_ast
    from .decorators import to_kwargs

    class Test:
        def __init__(self, name, where=None):
            self.name = name
            self.where = where

    # Test two types.
    class Test2(Test): pass

    kwargs = to_kwargs(Test, dict(name='foo', where='bar'))
    kwargs2 = to_kwargs(Test2, dict(name='foo', where='bar'))
    assert kwargs == kwargs2

    # And, we should be able to parse that.
    node = parse_ast("""foo = {Test}(bar, where='baz')""".format(Test=Test.__name__))

    # And, we should be able to transform that.
    transformer = StringTypes

# Generated at 2022-06-14 02:22:15.124629
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor  # type: ignore
    import textwrap
    program_str = """
        def foo(a: str):
            return a
    """
    tree = astor.parse_file(textwrap.dedent(program_str))
    StringTypesTransformer.transform(tree)
    expected = """
        def foo(a: unicode):
            return a
    """
    assert astor.to_source(tree) == textwrap.dedent(expected)

# Generated at 2022-06-14 02:22:24.373925
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from ..utils.fake_ast import make_tree

    t = make_tree(ast.Assign(
        targets=[ast.Name(id='x', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Name(id='str', ctx=ast.Load()),
            args=[ast.Str(s='hello')],
            keywords=[],
            starargs=None,
            kwargs=None),
    ))
    tr = StringTypesTransformer.transform(t)
    assert isinstance(tr.tree.body[0].value.func, ast.Name)
    assert tr.tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:22:33.476592
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.validate_target(2, 7)
    assert not StringTypesTransformer.validate_target(3, 0)

    from typed_ast import ast3 as ast
    from ..utils.source_code import SourceCode
    source_code = SourceCode()
    source_code.source = "a = str()"
    tree = ast.parse(source_code.source)
    StringTypesTransformer.transform(tree)
    source_code.set_tree(tree)
    assert source_code.source == "a = unicode()"

# Generated at 2022-06-14 02:22:34.940719
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test if constructor works:
    assert StringTypesTransformer()



# Generated at 2022-06-14 02:22:39.017043
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    in_ast = ast.parse('str()')
    expected_out_ast = ast.parse('unicode()')
    out_ast = StringTypesTransformer.transform(in_ast)
    assert ast.dump(out_ast.tree, False) == ast.dump(expected_out_ast, False)

# Generated at 2022-06-14 02:22:44.842600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # pylint: disable=W0122

    t = StringTypesTransformer.transform

    assert t(ast.parse("str('abc')")) == \
           TransformationResult(ast.parse("unicode('abc')"), True, [])
    assert t(ast.parse("b = str(a) + str(b)")) == \
           TransformationResult(ast.parse("b = unicode(a) + unicode(b)"), True, [])

    # pylint: enable=W0122

# Generated at 2022-06-14 02:22:48.039825
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    """Test for replacment of str with unicode.

    """
    tree = ast.parse('a = str()')
    t = StringTypesTransformer()
    t.transform(tree)

    tree.body[0].value.func.id == 'unicode'

# Generated at 2022-06-14 02:22:50.341883
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import typed_ast.ast3 as ast

    # Test class initialization
    # Should not raise an exception
    StringTypesTransformer()



# Generated at 2022-06-14 02:23:01.123794
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .utils import parse_python_to_ast, compare_ast
    from .test_LambdaTransformer import lambda_test_ast
    from ..types import TransformationResult

    t = StringTypesTransformer()

    # Single function
    parsed_ast = parse_python_to_ast(
        '''def hello():
            return str()
        '''
    )
    transformed_ast_without_changed, messages = t.transform(parsed_ast)
    transformed_ast, changed, messages = t.transform(transformed_ast_without_changed)
    assert not changed
    assert isinstance(parsed_ast, ast.Module)
    assert transformed_ast.body[0].body.body[0].value.func.id == 'unicode'

    # Single function 2
    parsed_ast = parse_python_to_

# Generated at 2022-06-14 02:23:56.130641
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test 1: Simple usage of `str`
    test1 = "str(4.4)"
    expected1 = "unicode(4.4)"

    tree1 = ast.parse(test1)
    transformed_tree1 = StringTypesTransformer.transform(tree1).tree

    assert expected1 == ast.unparse(transformed_tree1)

# Generated at 2022-06-14 02:24:04.353098
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from .unittransformer import UnitTransformer

    string_types_transformer = StringTypesTransformer()
    unit_transformer = UnitTransformer()

    tree = ast.parse('str(\'abc\')')
    unit_transformer.visit(tree)

    new_tree, tree_changed, _ = string_types_transformer.transform(tree)

    assert tree_changed

    code = compile(new_tree, '<string>', 'exec')
    ns = {}
    exec(code, ns)

    assert ns['str'](u'abc') == u'abc'

# Generated at 2022-06-14 02:24:06.988868
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    tree = ast.parse("self.encode('utf8')")
    assert StringTypesTransformer.transform(tree).valid

# Generated at 2022-06-14 02:24:20.213882
# Unit test for constructor of class StringTypesTransformer

# Generated at 2022-06-14 02:24:24.751771
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import astor
    code = 'def f(i, j):\n    return str(i) + str(j)'
    tree = astor.parse_file(code)
    new_tree = StringTypesTransformer.transform(tree)
    assert astor.to_source(new_tree.tree) == 'def f(i, j):\n    return unicode(i) + unicode(j)'

# Generated at 2022-06-14 02:24:31.241457
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
	code = """str"""
	tree = ast.parse(code)
	tree_changed, _, _ = StringTypesTransformer().transform(tree)
	print(ast.dump(tree))
	new_tree = ast.parse(code)
	new_tree_changed, _, _ = StringTypesTransformer().transform(new_tree)
	print(ast.dump(new_tree))

# test_StringTypesTransformer()

# Generated at 2022-06-14 02:24:40.349790
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    assert StringTypesTransformer.transform(ast.parse('str(1234)', mode='eval')) == TransformationResult(ast.parse('unicode(1234)', mode='eval'), True, [])
    assert StringTypesTransformer.transform(ast.parse('x = "abcd"', mode='exec')) == TransformationResult(ast.parse('x = "abcd"', mode='exec'), True, [])
    assert StringTypesTransformer.transform(ast.parse('str.join(["a", "b"])', mode='eval')) == TransformationResult(ast.parse('str.join(["a", "b"])', mode='eval'), False, [])

# Generated at 2022-06-14 02:24:44.372534
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    from typed_ast import ast3 as ast

    example = "def foo(x: str) -> None: pass"

    tree = ast.parse(example)
    tree = StringTypesTransformer.transform(tree)


# Generated at 2022-06-14 02:24:54.326119
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast, typed_ast.ast3
    # Given
    class Foo:
        def __init__(self, name: str):
            self.name = name
    tree = ast.parse(inspect.getsource(Foo))
    # When
    actual_tree, _ = StringTypesTransformer().transform(tree)
    # Then
    class Foo:
        def __init__(self, name: unicode):
            self.name = name
    expected_tree = ast.parse(inspect.getsource(Foo))
    typed_ast.ast3.fix_missing_locations(expected_tree)
    assert ast.dump(actual_tree, include_attributes=True) == ast.dump(expected_tree, include_attributes=True)

# Test for transforming function from class StringTypesTransformer

# Generated at 2022-06-14 02:25:06.293521
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    import ast
    from typed_ast import ast3
    from ..utils.code_gen import code_gen
    from ..utils.tree import find
    import typing
    
    tree = ast.parse('from string import ascii_letters as letters')
    tree = ast3.fix_missing_locations(tree)

    transformer = StringTypesTransformer()
    #changes, new_issues = transformer.transform(tree)
    new_tree, changes, new_issues = transformer.transform(tree)
    assert not changes, f'Code changes are {changes} and should be empty'
    assert not new_issues, 'Returned issues are {new_issues} and should be empty'
    
    # All names of type str should be replaced with unicode
    names = find(new_tree, ast3.Name)
    assert len(names) == 1