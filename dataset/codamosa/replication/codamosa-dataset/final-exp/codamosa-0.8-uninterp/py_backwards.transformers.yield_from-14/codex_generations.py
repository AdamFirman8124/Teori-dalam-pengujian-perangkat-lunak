

# Generated at 2022-06-14 02:39:07.602668
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    generator_name = 'test_name'
    exc_var = 'exc'
    target_name = 'test_targ'

# Generated at 2022-06-14 02:39:08.547151
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()


# Generated at 2022-06-14 02:39:13.639048
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import compile_to_pyc
    from ..parser import Parser

    parser = Parser()
    mod = parser.parse("""def foo(bar):
        try:
            yield from bar
        except StopIteration:
            pass
    """)
    ast.fix_missing_locations(mod)

    module, _ = compile_to_pyc(mod)
    print(module.foo('a'))

if __name__ == '__main__':
    test_YieldFromTransformer()

# Generated at 2022-06-14 02:39:16.721007
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.tree import parse

    tree = parse('''
    def _f():
        yield from range(10)
    ''')
    YieldFromTransformer().visit(tree)
    print(tree)

# Generated at 2022-06-14 02:39:18.304099
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:20.016830
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    instance = YieldFromTransformer()

    assert(isinstance(instance.tree, ast.AST))


# Generated at 2022-06-14 02:39:21.812237
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)


# Generated at 2022-06-14 02:39:24.311805
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from astunparse import unparse

    # Example from PEP 380

# Generated at 2022-06-14 02:39:25.342363
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:26.428299
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:32.969019
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().__class__.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:39:42.631670
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:39:51.498640
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import compile_snippet, get_node
    from ..transformers.base import BaseNodeTransformer
    from .base import BaseTransformer

    code = """
    a = yield from b
    """
    tree = compile_snippet(code, "exec", 3)
    node = get_node(tree, 2)
    transformer = YieldFromTransformer()
    assert isinstance(transformer, BaseNodeTransformer)
    assert isinstance(transformer, BaseTransformer)
    assert isinstance(transformer, object)
    assert transformer.target == (3, 2)
    assert transformer._get_yield_from_index(node, ast.Assign) is None


# Generated at 2022-06-14 02:39:55.532439
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): 
    # Test that YieldFromTransformer is a subclass of BaseNodeTransformer
    assert issubclass(YieldFromTransformer, BaseNodeTransformer)
   
    # Test that the class can be instantiated
    YieldFromTransformer()


# Generated at 2022-06-14 02:39:56.954537
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)

# Generated at 2022-06-14 02:40:00.605094
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys

    # Default predicate, which return false
    YieldFromTransformer()
    # User-defined predicate
    YieldFromTransformer(lambda exc: sys.exit('Error!'))


# Generated at 2022-06-14 02:40:09.262811
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..codegen import to_source
    from ..parser import parser

    # Simply test that the pattern works
    source = 'a = yield from [1, 2, 3]'
    tree = parser.parse(source)
    transformed = YieldFromTransformer().visit(tree)
    new_source = to_source(transformed)
    expect = '''
    let(iterable)
    iterable = iter([1, 2, 3])
    while True:
        try:
            a = next(iterable)
        except StopIteration as exc:
            if hasattr(exc, 'value'):
                a = exc.value
            break
    '''
    assert new_source.strip() == expect.strip()

# Generated at 2022-06-14 02:40:13.863859
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from = ast.YieldFrom(value=1)
    target = ast.Name(id="test")
    node = ast.Assign(targets=[target], value=yield_from)
    assert node.value == yield_from
    assert node.targets[0] == target



# Generated at 2022-06-14 02:40:15.813074
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
  parser = YieldFromTransformer()
  return parser


# Generated at 2022-06-14 02:40:16.644214
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Test constructor of class YieldFromTransformer"""
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:32.353067
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('''
        def func(s):
            t = yield from s
    ''')

    assert not hasattr(node, 'body') or not isinstance(node.body, list)
    assert not hasattr(node.body, 'body') or not isinstance(node.body.body, list)
    assert not hasattr(node.body.body, 'value') or not isinstance(node.body.body.value, ast.Call)


# Generated at 2022-06-14 02:40:35.166458
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:40:40.780148
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code_str = """
    def foo():
        a = yield from bar()
        yield from bar()
        ((yield from bar()))
    """
    root = ast.parse(code_str)
    YieldFromTransformer().visit(root)
    code_transformed = compile(root, '<test>', 'exec')
    assert eval(code_transformed)

# Generated at 2022-06-14 02:40:43.766182
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .constructor_test import ConstructorTestCase
    ConstructorTestCase().run_test(YieldFromTransformer)


# Generated at 2022-06-14 02:40:45.282351
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None)



# Generated at 2022-06-14 02:40:53.763357
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast import Module, FunctionDef, Assign, Name, Load, YieldFrom, Expr, Str
    a = Module(body=[
        FunctionDef(name="f",
                    args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                    body=[
                        Assign(targets=[Name(id='a', ctx=Store())],
                               value=YieldFrom(value=Name(id='b', ctx=Load()))),
                        Expr(value=Str(s='str'))],
                    decorator_list=[], returns=None)])

# Generated at 2022-06-14 02:40:54.664230
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = YieldFromTransformer()

# Generated at 2022-06-14 02:40:58.911639
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test empty class
    node = ast.Module([])
    obj = YieldFromTransformer(node)
    assert obj.visit(node) == node
    assert obj.target == (3, 2)

# Generated at 2022-06-14 02:41:00.741560
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert type(YieldFromTransformer) == YieldFromTransformer


# Generated at 2022-06-14 02:41:10.816275
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Simple test case
    transformer = YieldFromTransformer()
    code = 'def foo(): yield 42'
    tree = ast.parse(code)
    expected_tree = ast.parse('def foo(): yield 42')
    assert transformer.visit(tree).body[0] == expected_tree.body[0]

    # Another simple test case
    code = 'def foo(): yield from [1, 2, 3]'
    tree = ast.parse(code)
    expected_tree = ast.parse(
        'def foo():\n'
        '    yield from [1, 2, 3]')
    assert transformer.visit(tree).body[0] == expected_tree.body[0]

    # Another simple test case, different indentation
    code = 'def foo():\n    yield from [1, 2, 3]'
    tree

# Generated at 2022-06-14 02:41:34.159113
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_transformer import TestTransformer
    from ..utils.test_data import yield_from_function
    TestTransformer(YieldFromTransformer()).transform(yield_from_function)

# Generated at 2022-06-14 02:41:35.342479
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys

# Generated at 2022-06-14 02:41:39.908438
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    if (str(a) == "<YieldFromTransformer: target=(3, 2)>"):
        print('Pass\n')
    else:
        print('Fail\n')
    a.visit() # tested elsewhere
    #print(a)


# Generated at 2022-06-14 02:41:42.831356
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert repr(YieldFromTransformer) == '<YieldFromTransformer>'
    assert callable(YieldFromTransformer)


# Generated at 2022-06-14 02:41:44.860277
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None, None).pyversion is None
    assert YieldFromTransformer(None, None).features == {}

# Generated at 2022-06-14 02:41:52.466384
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.test_utils import transform_and_compile

    def generator():
        yield from iter([1, 2, 3])
        yield from iter([4, 5, 6])

    yield_from = transform_and_compile(YieldFromTransformer, generator).__code__.co_name
    assert yield_from == 'generator'

    @transform_and_compile(YieldFromTransformer)
    def generator2():
        yield from iter([1, 2, 3])

    yield_from = generator2.__code__.co_name
    assert yield_from == 'generator2'

    @transform_and_compile(YieldFromTransformer)
    def generator3():
        yield from iter([1, 2, 3])
        yield from iter([4, 5, 6])

# Generated at 2022-06-14 02:41:55.230805
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()
    t._tree_changed = True


# Generated at 2022-06-14 02:42:00.407069
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    code = '''
    def test():
        x = yield from range(10)
        print(x)
        
    '''
    tree = ast.parse(code)
    yield_from_transformer = YieldFromTransformer()
    tree = yield_from_transformer.transform(tree)
    print(ast.dump(tree))

# Generated at 2022-06-14 02:42:01.192684
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer

# Generated at 2022-06-14 02:42:01.700249
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass

# Generated at 2022-06-14 02:42:43.773058
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    """Unit test of YieldFromTransformer constructor."""
    transform_object = YieldFromTransformer()
    assert transform_object.target == (3, 2)



# Generated at 2022-06-14 02:42:45.065075
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:42:46.156218
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    yield_from_transformer = YieldFromTransformer()


# Generated at 2022-06-14 02:42:47.099221
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    _YieldFromTransformer = YieldFromTransformer()



# Generated at 2022-06-14 02:42:56.886798
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    source = """
        def foo():
            yield from bar()

        while True:
            yield from bar()

        foo = yield from bar()

        yield from bar()

        if True:
            yield from bar()

        try:
            yield from bar()
        except Exception:
            pass

        for i in range(10):
            yield from bar()
    """
    module = ast.parse(source)
    YieldFromTransformer().visit(module)

# Generated at 2022-06-14 02:42:58.666591
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:42:59.972557
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'


# Generated at 2022-06-14 02:43:01.226824
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().visit(Holder())

# Generated at 2022-06-14 02:43:02.843832
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    t = YieldFromTransformer()

# Generated at 2022-06-14 02:43:13.558418
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    import textwrap

    source = textwrap.dedent(
        """
        def f():
            exc = None
            try:
                exc = 1
            except Exception:
                exc = 2
            yield from exc
        """
    )
    tree = ast.parse(source)
    tree = YieldFromTransformer().visit(tree)
    print(ast.dump(tree))

    source = textwrap.dedent(
        """
        def f():
            yield from 1
        """
    )
    tree = ast.parse(source)
    tree = YieldFromTransformer().visit(tree)
    print(ast.dump(tree))

    source = textwrap.dedent(
        """
        def f():
            yield from 1 + 1
        """
    )


# Generated at 2022-06-14 02:45:46.150595
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    if __debug__:
        from typed_ast import ast3 as ast
        from ..parser import parse_ast
        from ..utils.helpers import VariablesGenerator
        tree = parse_ast('x = yield from [1, 2, 3]')
        let(YT)
        YT = YieldFromTransformer(tree)
        let(node)
        node = YT.visit(tree)
        let(result)
        result = ast.dump(node)
        let(expected)

# Generated at 2022-06-14 02:45:47.570303
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

# Generated at 2022-06-14 02:45:50.305903
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()

# Testing a method of class YieldFromTransformer

# Generated at 2022-06-14 02:45:51.846132
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()


# Generated at 2022-06-14 02:45:53.404274
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:45:54.886080
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer(None)

# Generated at 2022-06-14 02:45:58.193156
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    x = ast.parse('a = yield from foo')
    YieldFromTransformer().visit(x)


# Generated at 2022-06-14 02:45:59.629475
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():

    with pytest.raises(TypeError):
        YieldFromTransformer(None)


# Generated at 2022-06-14 02:46:13.834076
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..parser.parser import parse
    from .tree import print_tree
    from .remove_comments import RemoveCommentsTransformer
    from .remove_imports import RemoveImportsTransformer
    from .resolve_index import ResolveIndexTransformer
    from .unpack_tuples import UnpackTuplesTransformer

    ast_orig = '''
    if foo:
        x = yield from foo()
    '''
    ast_final = '''
    if foo:
        iterable = iter(foo())
        while True:
            try:
                yield next(iterable)
            except StopIteration as exc:
                x = exc.value
            break
    '''

    tree = parse(ast_orig)
    tree = YieldFromTransformer()(tree)
    ast_final = parse(ast_final)


# Generated at 2022-06-14 02:46:15.764676
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:48:58.021177
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    print(transformer)


# Generated at 2022-06-14 02:49:01.290625
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    "Test constructor of class YieldFromTransformer"
    try_transformer = YieldFromTransformer()
    assert try_transformer

