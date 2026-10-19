

# Generated at 2022-06-14 02:39:06.411023
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()


# Generated at 2022-06-14 02:39:07.413416
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:39:14.081896
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .test_yield import a, b, c, f1, f2
    from ..utils.source import source

    source1 = source(f1)
    source2 = source(f2)

    assert source(YieldFromTransformer.run(ast.parse(source1))) == source1
    assert source(YieldFromTransformer.run(ast.parse(source2))) == source2
    assert source(YieldFromTransformer.run(a)) == source(a)
    assert source(YieldFromTransformer.run(b)) == source(b)
    assert source(YieldFromTransformer.run(c)) == source(c)


# Generated at 2022-06-14 02:39:19.378502
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Case 1: init
    yield_from_transformer = YieldFromTransformer()
    assert isinstance(yield_from_transformer, YieldFromTransformer)
    # Case 2: init
    yield_from_transformer = YieldFromTransformer("", "", "")
    assert isinstance(yield_from_transformer, YieldFromTransformer)


# Generated at 2022-06-14 02:39:25.675184
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    target = (3, 2)
    result_assignment = 'result_assignment'
    yield_from = 'yield_from'

    obj1 = YieldFromTransformer(target, result_assignment, yield_from)
    try:
        obj1.generic_visit(None)
    except NotImplementedError:
        pass

    obj2 = YieldFromTransformer(target, result_assignment, yield_from)
    try:
        obj2.visit(None)
    except NotImplementedError:
        pass

# Generated at 2022-06-14 02:39:28.645644
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)
    assert not transformer._tree_changed
    assert transformer._get_yield_from_index(transformer, ast.Assign) == None

# Generated at 2022-06-14 02:39:38.638817
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.imports import import_module
    from ..utils.fake import FakeBuilder

    builder = FakeBuilder(
        'import ast\n'
        'from typed_ast import ast3\n'
        'from cst_transforms.yield_from import YieldFromTransformer\n',
        __file__,
    )

    builder.add_function(
        'test_func',
        'def test_func():\n'
        '    yield from list(range(2))',
    )

    with builder as module:
        tree = import_module(module)
        YieldFromTransformer(tree).visit(tree)
        assert tree.body[0].body[0].body[0].value.args[0].elts[0].n == 0

# Generated at 2022-06-14 02:39:46.302810
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..tranformers.yieldfrom import YieldFromTransformer
    from ..utils.helpers import VariablesGenerator
    from typing import Any

    assert(isinstance(YieldFromTransformer, object))
    assert(isinstance(YieldFromTransformer.target, tuple))
    assert(isinstance(YieldFromTransformer.visit, Any))
    assert(isinstance(YieldFromTransformer._get_yield_from_index, Any))
    assert(isinstance(YieldFromTransformer._emulate_yield_from, Any))
    assert(isinstance(YieldFromTransformer._handle_expressions, Any))
    assert(isinstance(YieldFromTransformer._handle_assignments, Any))
    assert(isinstance(YieldFromTransformer.generic_visit, Any))

# Generated at 2022-06-14 02:39:48.017160
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().__class__.__name__ == 'YieldFromTransformer'

# Generated at 2022-06-14 02:39:56.260088
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from typed_ast import ast3 as ast
    from ..utils.test_helpers import is_snippet_in_ast, get_ast_body

    def test_assignment(source: str, target_source: str,
                        body_source: str = None) -> bool:
        tree = ast.parse(source)
        tr = YieldFromTransformer()
        tr.visit(tree)
        if not tr.is_changed:
            return False

        target = ast.parse(target_source).body
        root = tree.body.pop()
        is_snippet_in_ast(get_ast_body(root), target)
        if body_source:
            body = ast.parse(body_source).body
            root = tree.body.pop()

# Generated at 2022-06-14 02:40:03.194828
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    print("Testing constructor for class YieldFromTransformer")
    transformer = YieldFromTransformer()



# Generated at 2022-06-14 02:40:09.069154
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import from_str
    node = from_str('def func()->int:\n yield from foo')
    node = YieldFromTransformer.run_on(node)
    assert node is not None
    assert node.body[0].body[0].value.func.id == 'iter'

# Generated at 2022-06-14 02:40:10.105133
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None

# Generated at 2022-06-14 02:40:11.984601
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
	visitor = YieldFromTransformer()
	assert visitor.target == (3, 2)


# Generated at 2022-06-14 02:40:13.156900
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:40:14.476043
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert(YieldFromTransformer())


# Generated at 2022-06-14 02:40:15.813316
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer("x")

# Generated at 2022-06-14 02:40:16.464560
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass


# Generated at 2022-06-14 02:40:22.121153
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert YieldFromTransformer.__module__ == __name__
    assert YieldFromTransformer.__doc__ == 'Compiles yield from to special while statement.'
    assert YieldFromTransformer.target == (3, 2)

    assert YieldFromTransformer._get_yield_from_index.__module__ == __name__
    assert YieldFromTransformer._get_yield_from_index.__doc__ == 'Internal. Get index of yield from statement.\n\n        Args:\n            node: AST node.\n            type_: Type of node which contains yield from.\n\n        Returns:\n            Index of yield from statement.\n        '

    assert YieldFromTransformer._emulate_yield_from.__module__

# Generated at 2022-06-14 02:40:32.068330
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    constructor = ast.parse("def __init__(self): self.a = '1'; self.b = yield from iter(range(2)); self.c = yield from iter(range(3))").body[0].body[1]
    assert str(constructor) == "self.b = yield from iter(range(2)); self.c = yield from iter(range(3));"

# Generated at 2022-06-14 02:40:49.027388
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    vars = VariablesGenerator()
    ast_ = pytest.importorskip("ast")
    if ast.Try:
        try_ = ast.Try(body=[ast.YieldFrom(value=vars.get('generator'))],
                       handlers=[
                            ast.ExceptHandler(type=vars.get('StopIteration'),
                                              name=vars.get('exc'),
                                              body=[ast.Assign(
                                                  targets=[ast.Name(id='target', ctx=ast_.Store())],
                                                  value=ast.Attribute(
                                                      value=vars.get('exc'),
                                                      attr='value',
                                                      ctx=ast_.Load()
                                                  )
                                              )])
                        ],
                       orelse=[])


# Generated at 2022-06-14 02:40:55.070207
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..compiler import compile
    from astor.code_gen import to_source
    tree = ast.parse(
        'def myfunc(arg1, arg2):\n'
        '\tdef func():\n'
        '\t\tfor i in range(10):\n'
        '\t\t\tyield i\n'
        '\tfor i in range(10):\n'
        '\t\tyield from func()\n'
        '\twhile True:\n'
        '\t\tprint("hello")\n'
        '\t\tyield from func()\n'
        '\t\tprint("world")\n'
        '\tresult = yield from func()\n'
        '\tprint("result =", result)\n'
        )


# Generated at 2022-06-14 02:40:59.012167
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ast_helpers import parse, ast_dump
    from ..utils.helpers import get_variables
    from ..utils.compare import compare_ast
    import ast


# Generated at 2022-06-14 02:41:05.884156
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import get_ast

    class_ = YieldFromTransformer()
    assert class_.visit(get_ast('yieldvalue = yield from iterable')) == \
            get_ast('yieldvalue = iterable')
    assert class_.visit(get_ast('yield from iterable')) == \
            get_ast('iterable')

# Generated at 2022-06-14 02:41:18.875216
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from unittest import TestCase
    import astunparse
    from ..utils.helpers import get_test_data

    class TestYieldFromTransformer(TestCase):
        """Test class for constructor of class YieldFromTransformer."""

        def test_basic(self):
            """Basic test case."""

            test_cases = get_test_data('yield_from.json')
            for test_case in test_cases:
                with self.subTest(key=test_case['key']):
                    code = test_case['code']
                    ast_ = ast.parse(code)
                    tree = ast_.body[0]
                    transformer = YieldFromTransformer()
                    new_tree = transformer.visit(tree)
                    result = astunparse.unparse(new_tree)

# Generated at 2022-06-14 02:41:20.111744
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:23.452093
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    _YieldFromTransformer = YieldFromTransformer()
    assert _YieldFromTransformer



# Generated at 2022-06-14 02:41:25.965692
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:27.991983
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert isinstance(YieldFromTransformer(), YieldFromTransformer)


# Generated at 2022-06-14 02:41:29.170936
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:41:48.383693
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from . import TestTransformer
    from typed_ast import ast3
    # Test for function __init__(self)
    YieldFromTransformer()
    # Test for function _get_yield_from_index(self, node: ast.AST,
    #                                         type_: Type[Holder]) -> Optional[int]
    YieldFromTransformer()._get_yield_from_index(
        node=ast3.Try(
            body=[
                ast3.Expr(
                    ast3.YieldFrom())],
            handlers=[ast3.ExceptHandler()],
            finalbody=[ast3.Pass()],
            orelse=[],
            type_=None),
        type_=ast.Expr)
    # Test for function _emulate_yield_from(self, target: Optional[ast.AST],


# Generated at 2022-06-14 02:41:49.912888
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    pass
# vim: set tabstop=8 softtabstop=4 shiftwidth=4 expandtab:

# Generated at 2022-06-14 02:41:51.422578
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:41:53.312371
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer([])


# Generated at 2022-06-14 02:41:55.008073
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(3, 3).target == (3, 3)

# Generated at 2022-06-14 02:41:55.984124
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer(None)

# Generated at 2022-06-14 02:41:58.756372
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # This is how you create an object of the class
    obj = YieldFromTransformer()
    assert obj is not None



# Generated at 2022-06-14 02:42:00.325151
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer().visit is not None

# Generated at 2022-06-14 02:42:01.855120
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.AST()
    try:
        if True:
            test = True
            node = YieldFromTransformer().visit(node)
    except Exception:
        print("Exception")
# Possible Output:
#   Exception

# Generated at 2022-06-14 02:42:04.015268
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import inspect
    import ast as ast_new

    # Creates an instance of the class YieldFromTransformer
    instance = YieldFromTransformer(inspect.getsource(inspect.currentframe()), ast_new)
    assert instance


# Generated at 2022-06-14 02:42:25.573597
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 02:42:27.702906
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer()
    assert transformer.target == (3, 2)


# Generated at 2022-06-14 02:42:35.193852
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import parse

    code = 'yield from some_generator()'
    result = 'while True:\n    try:\n        yield next(iterable)\n    except StopIteration as exc:\n        if hasattr(exc, \'value\'):\n            target = exc.value\n        break\niterable = iter(some_generator())'
    tree = parse(code)
    assert str(YieldFromTransformer().visit(tree)) == result

# Generated at 2022-06-14 02:42:45.690661
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import node_to_string

    i = 0
    while i < 3:
        i += 1
        yield 'TA', i

    node_to_string(ast.parse('''
    def A(self):
        while True:
            try:
                _i = 0
                while _i < 3:
                    _i += 1
                    yield 'TA', _i
            except StopIteration as exc:
                return

    def B(self):
        while True:
            try:
                _i = 0
                while _i < 3:
                    _i += 1
                    yield 'TA', _i
            except StopIteration:
                break
    '''))
    from pprint import pprint

    t = ast.parse('i = yield from A()')
    tr = YieldFromTransformer()

# Generated at 2022-06-14 02:42:49.879764
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    obj = YieldFromTransformer()

    assert 'YieldFromTransformer' == obj.__class__.__name__

    assert hasattr(obj, 'target')

    assert hasattr(obj, '_get_yield_from_index')
    assert hasattr(obj, '_handle_assignments')
    assert hasattr(obj, '_handle_expressions')
    assert hasattr(obj, 'visit')

    assert hasattr(obj, '_emulate_yield_from')

# Generated at 2022-06-14 02:42:51.089591
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()._tree_changed == False


# Generated at 2022-06-14 02:42:53.084697
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    class Test(BaseNodeTransformer):
        pass

    assert Test.__name__ == 'Test'


# Generated at 2022-06-14 02:42:59.572806
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert 'from typing import Union, List, Type, Optional, ast' in YieldFromTransformer.__module__
    assert YieldFromTransformer.__name__ == 'YieldFromTransformer'
    assert type(YieldFromTransformer.target) == tuple
    assert isinstance(YieldFromTransformer.target, tuple)
    assert YieldFromTransformer.target == (3, 2)
    assert YieldFromTransformer.visit
    assert YieldFromTransformer.generic_visit

# Generated at 2022-06-14 02:43:01.390422
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    transformer = YieldFromTransformer('example.py')
    assert isinstance(transformer, YieldFromTransformer)


# Generated at 2022-06-14 02:43:03.433202
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = YieldFromTransformer()
    assert a is not None

# Generated at 2022-06-14 02:43:42.267772
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # For correctly work of docstring tests
    assert YieldFromTransformer(None, None)



# Generated at 2022-06-14 02:43:43.312185
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:43:45.305236
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:43:46.339864
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    YieldFromTransformer()

# Generated at 2022-06-14 02:43:53.765917
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import Q, c
    from ..distiller import Distiller
    from ..replacer import Replacer
    from ..fixer import Fixer

    n = c(YieldFromTransformer)
    
    # 1
    n = n.visit(Q('''
    def gtest():
        while 1:
            yield from test()
    '''))
    assert n == Q('''
    def gtest():
        while 1:
            let(iterable)
            iterable = iter(test())
            while True:
                try:
                    yield next(iterable)
                except StopIteration as exc:
                    break
    ''')
    
    # 2
    n = n.visit(Q('''
    def test():
        yield from test()
    '''))
    assert n == Q

# Generated at 2022-06-14 02:43:57.420036
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer(): 
    """Unit test for constructor of class YieldFromTransformer"""
    node = ast.Module([])
    obj = YieldFromTransformer()
    assert (isinstance(obj, YieldFromTransformer))


# Generated at 2022-06-14 02:43:58.776817
# Unit test for constructor of class YieldFromTransformer

# Generated at 2022-06-14 02:44:01.530970
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import sys
    from ..parser import parse

    YieldFromTransformer(sys.modules[__name__], parse(
        'result = yield from other_function(*args, **kwargs)'))

# Generated at 2022-06-14 02:44:06.788497
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .. import compile_to_ast
    code = '''def gen():\n    yield from range(1, 1000)\n'''
    compiled = compile_to_ast(code)

    assert compiled.code.startswith('def gen():')

    while True:
        index = compiled.code.find('yield from')
        if index < 0:
            break
        compiled.code = compiled.code[:index] + 'yield (yield ('\
            + compiled.code[index + 12:]

    assert eval(compiled.code) == list(range(1, 1000))

# Generated at 2022-06-14 02:44:10.087481
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert hasattr(YieldFromTransformer,'__init__') and callable(YieldFromTransformer.__init__)


# Generated at 2022-06-14 02:45:40.487565
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils import cst
    from ..utils.testing import assert_type

    assert_type(YieldFromTransformer, BaseNodeTransformer)
    assert YieldFromTransformer().__doc__

    assert_type([], YieldFromTransformer()._get_yield_from_index(cst.Module(), ast.Assign))

# Generated at 2022-06-14 02:45:42.636656
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert repr(YieldFromTransformer()) == "YieldFromTransformer()"

# Generated at 2022-06-14 02:45:44.640842
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer() is not None


# Generated at 2022-06-14 02:45:59.609507
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    import astor
    from ..utils.helpers import get_ast

    d = {'x': 1, 'y': 2}
    tree = get_ast('''
    def test(d):
        some = yield from d
        other = yield from d
        return some
    ''')
    YieldFromTransformer().visit(tree)

# Generated at 2022-06-14 02:46:04.772301
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    # Test 1: test handle_assignments method
    with open('tests/syntax_samples/yield_from/sample_1.py', 'r') as source:
        source_code = source.read()

# Generated at 2022-06-14 02:46:18.230207
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from ..utils.helpers import tree

    # Test 1, test a tree with only yield from statement
    test_tree_1 = tree(root=ast.Module(body=[ast.Expr(value=ast.YieldFrom(value=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Num(n=10)], keywords=[])))]))

# Generated at 2022-06-14 02:46:19.616400
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    assert YieldFromTransformer()

# Generated at 2022-06-14 02:46:34.521294
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    from .stripper import Stripper
    from .ast_unparser import Unparser
    from ..utils.snippet import snippet, let

    @snippet
    def non_generic_visit(self, node):
        return node

    # Constructor
    yft = YieldFromTransformer(tree_changed=False,
                               node_mapping={},
                               generic_visit=non_generic_visit,
                               target=(3, 2))

    # _get_yield_from_index
    def visit_Expr(self, node):
        while True:
            index = self._get_yield_from_index(node, ast.Expr)
            if index is None:
                return node
            exp = node.body.pop(index)
            exc = VariablesGenerator.generate('exc')

# Generated at 2022-06-14 02:46:43.142294
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    node = ast.parse('def foo(): yield from bar()')
    YieldFromTransformer().visit(node)

# Generated at 2022-06-14 02:46:49.943008
# Unit test for constructor of class YieldFromTransformer
def test_YieldFromTransformer():
    a = ast.Expr(value=ast.YieldFrom(value=ast.Name(id='a')))
    node = YieldFromTransformer.visit(ast.Module(body=a))