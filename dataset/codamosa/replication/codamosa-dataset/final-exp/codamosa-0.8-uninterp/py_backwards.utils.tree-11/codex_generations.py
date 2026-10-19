

# Generated at 2022-06-14 03:01:43.470203
# Unit test for function get_parent
def test_get_parent():
    """Unit test for get_parent."""
    node = ast.parse("print('Hello, world!')")
    assert get_parent(node, node.body[0].value.s) == node.body[0]
    assert get_parent(node, node.body[0].value) == node.body[0]
    assert get_parent(node, node.body[0]) == node


# Generated at 2022-06-14 03:01:49.918431
# Unit test for function find
def test_find():
    import unittest
    import astor
    from . import ast_config
    from . import source_code

    class TestCase(unittest.TestCase):
        def test_find(self):
            tree = astor.parse_file(ast_config.TEST_DATA_DIR + '/test.py')
            nodes = find(tree, ast.ClassDef)
            self.assertEqual(len(list(nodes)), 1)

            nodes = find(tree, ast.FunctionDef)
            self.assertEqual(len(list(nodes)), 2)

            nodes = find(tree, ast.While)
            self.assertEqual(len(list(nodes)), 1)


# Generated at 2022-06-14 03:01:52.821996
# Unit test for function find
def test_find():
    # Test find function on a simple tree
    class A(ast.AST):
        pass

    class B(ast.AST):
        pass

    class C(ast.AST):
        pass

    class D(ast.AST):
        pass

    t = A(B(), C(), D(), B(), C(), D())
    result = find(t, B)
    assert list(result) == [t.body[0], t.body[-2]]



# Generated at 2022-06-14 03:02:02.044404
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from astor import to_source
    from ast_helpers import insert_at  # type: ignore

    tree = ast.parse('''def a():
        pass''')
    test_node = tree.body[0]
    insert_at(0, tree, ast.FunctionDef('b', ast.arguments([]), [], [], []))
    # x = get_parent(tree, test_node)

    x = get_closest_parent_of(tree, test_node, ast.Module)
    x = get_closest_parent_of(tree, test_node, ast.Module)

# Generated at 2022-06-14 03:02:11.830948
# Unit test for function find
def test_find():
    node = ast.parse("""
for x in range(5):
    if x == 4:
        break
    print(x)
    """)
    for_loop_nodes = list(find(node, ast.For))
    assert isinstance(for_loop_nodes[0], ast.For)
    assert len(for_loop_nodes) == 1
    break_statement_nodes = list(find(node, ast.Break))
    assert isinstance(break_statement_nodes[0], ast.Break)
    assert len(break_statement_nodes) == 1
    print_statement_nodes = list(find(node, ast.Print))
    assert isinstance(print_statement_nodes[0], ast.Print)
    assert len(print_statement_nodes) == 1

# Generated at 2022-06-14 03:02:19.049311
# Unit test for function find
def test_find():
    code = """#!/usr/bin/env python3
if __name__ == "__main__":
    pass
    # I'm a comment
    """
    tree = ast.parse(code)
    assert [n.id for n in find(tree, ast.Name)] == ['__name__']
    assert [n.lineno for n in find(tree, ast.If)] == [2]
    assert [n.col_offset for n in find(tree, ast.Pass)] == [4]
    assert [n.value.s for n in find(tree, ast.Str)] == ['__name__', 'main']
    assert [n.s for n in find(tree, ast.AnnAssign)] == []
    assert [n.value.s for n in find(tree, ast.Str)] == ['__name__', 'main']


# Generated at 2022-06-14 03:02:19.845013
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:22.330795
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:23.602742
# Unit test for function replace_at

# Generated at 2022-06-14 03:02:32.122335
# Unit test for function find
def test_find():
    m = ast.parse(
        'def foo():\n'
        '    def bar(): pass\n'
        '\n'
        '    def baz():\n'
        '        pass\n')

    assert len(list(find(m, ast.FunctionDef))) == 3

    assert len(list(find(m, ast.Name))) == 1



# Generated at 2022-06-14 03:02:36.403676
# Unit test for function find
def test_find():
    assert(list(find(ast.parse('True'), ast.Name)))

# Generated at 2022-06-14 03:02:45.489485
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import inspect
    import astor

    tree = ast.parse(inspect.getsource(test_get_non_exp_parent_and_index))
    # print(astor.dump_tree(tree))

    line = 10
    col = None

    for i, statement in enumerate(tree.body):
        print(i)
        print(astor.to_source(statement))
        if statement.lineno > line:
            break
        col = statement.col_offset
        print("-------------------")
    i -= 1

    print("\n-------------------")
    print("id: {}".format(id(statement)))
    print("line: {}".format(statement.lineno))
    print("col: {}".format(statement.col_offset))
    print("-------------------")
    print("\n-------------------")

   

# Generated at 2022-06-14 03:02:57.783918
# Unit test for function replace_at
def test_replace_at():
    """Unit test for replace_at function."""
    # test replace_at method
    parent_body = ast.Module(body=[
        ast.Expr(value=ast.Call(func=ast.Name('f'),
                                args=[ast.Num(1), ast.Name('b')],
                                keywords=[ast.keyword(arg='c', value=3)])),
        ast.Expr(value=ast.Call(func=ast.Name('f'),
                                args=[ast.Num(2), ast.Name('b')])),
        ast.Return(value=ast.Call(func=ast.Name('f'),
                                  args=[ast.Num(3), ast.Name('b')]))
    ])
    parent = ast.FunctionDef(name='func', body=parent_body.body)

# Generated at 2022-06-14 03:03:02.118613
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    node = ast.parse("test = 1").body[0]
    parent = get_closest_parent_of(node, node.targets[0], ast.Module)
    assert isinstance(parent, ast.Module)

# Generated at 2022-06-14 03:03:13.711673
# Unit test for function find
def test_find():
    # test for arguments
    if find(ast.parse('print("Test")'), ast.Name) is not None:
        assert (True)
    else:
        assert (False)
    # test for assert
    if find(ast.parse('assert ("Test")'), ast.Assert) is not None:
        assert (True)
    else:
        assert (False)
    # test for delete
    if find(ast.parse('del ("Test")'), ast.Delete) is not None:
        assert (True)
    else:
        assert (False)
    # test for function
    if find(ast.parse('def functest(): pass'), ast.FunctionDef) is not None:
        assert (True)
    else:
        assert (False)
    # test for class

# Generated at 2022-06-14 03:03:18.025785
# Unit test for function find
def test_find():
    found_nodes = list(find(ast.parse('def foo(x, y=5):\n    pass\n'),
                            ast.FunctionDef))
    assert found_nodes == [ast.parse('def foo(x, y=5):\n    pass\n').body[0]]



# Generated at 2022-06-14 03:03:25.110583
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('''\
    def f():
        for i in range(4):
            for j in range(5):
                break
            else:
                continue
            break
        else:
            for i in range(4):
                pass
        ''')
    node = tree.body[0].body[0].body[1]
    parent = get_parent(tree, node)
    assert isinstance(parent, ast.For)

    parent = get_parent(tree, parent)
    assert isinstance(parent, ast.For)
    assert parent.body[0].body == [node]



# Generated at 2022-06-14 03:03:28.206226
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    _tree = ast.parse('def a():\n    pass')
    _class = _tree.body[0].body[0]
    assert get_closest_parent_of(_tree, _class, ast.ClassDef) is None
    assert get_closest_parent_of(_tree, _class, ast.FunctionDef) is _tree.body[0]



# Generated at 2022-06-14 03:03:34.300223
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import ast
    tree = ast.parse('a.b.c.d.')
    node = list(ast.walk(tree))[-1]
    assert isinstance(node, ast.Attribute)
    parent = get_closest_parent_of(tree, node, ast.Name)
    assert isinstance(parent, ast.Name)
    assert parent.id == 'c'

# Generated at 2022-06-14 03:03:39.197676
# Unit test for function find
def test_find():
    a = ast.parse("x = [1, 2]")
    b = ast.parse("y = [3, 4]")
    body = a.body + b.body
    c = ast.Module(body)
    a = find(c, ast.List)
    b = find(c, ast.Module)
    print([i.elts[0].value for i in a])
    print(list(b))



# Generated at 2022-06-14 03:03:47.145165
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert_exception_message_equals(
        NodeNotFound,
        lambda: get_non_exp_parent_and_index(ast.parse("print('1')"),
                                             ast.parse("print('1')")),
        "Parent for <_ast.Module object at 0x7f5df5bcd828> not found"
    )



# Generated at 2022-06-14 03:03:56.512303
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import logging
    import os
    import unittest

    from typed_ast import ast3 as ast

    from ..ast_manipulation import get_non_exp_parent_and_index

    class TestGetNonExpParentAndIndex(unittest.TestCase):
        def setUp(self):
            logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))

        def test_get_non_exp_parent_and_index(self):

            source = '''def foo():
                                if foo:
                                    pass
                                else:
                                    pass
                            '''

            ast_ = ast.parse(source)
            If = get_non_exp_parent_and_index(ast_, ast_.body[0].body[0])[0]


# Generated at 2022-06-14 03:04:03.920401
# Unit test for function find
def test_find():
    source = """
            class Foo:
                pass
            
            print(Foo)
            """

    module = ast.parse(source)

    assert len(list(find(module, ast.ClassDef))) == 1
    assert len(list(find(module, ast.Name))) == 2

    class_def = get_closest_parent_of(module, module.body[1], ast.ClassDef)

    for _ in find(class_def, ast.Name):
        assert False



# Generated at 2022-06-14 03:04:11.543533
# Unit test for function replace_at
def test_replace_at():
    root = ast.parse('def f():\n pass')
    first_parent = root.body[0]
    assert len(first_parent.body) == 1
    assert isinstance(first_parent.body[0], ast.Pass)
    replace_at(0, first_parent, ast.Expr(ast.Str('s')))
    assert len(first_parent.body) == 1
    assert isinstance(first_parent.body[0], ast.Expr)
    assert isinstance(first_parent.body[0].value, ast.Str)

# Generated at 2022-06-14 03:04:22.728282
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    source = """\
    def f():
      a = 1 + 2
      b = 3 + 4
      return b + a
    """
    tree = ast.parse(source)
    a = tree.body[0].body[0]
    c = a.value
    # print(c)
    b = tree.body[0].body[1]
    # print(b)
    func = get_closest_parent_of(tree, c, ast.FunctionDef)
    assert(func.name == 'f')
    func = get_closest_parent_of(tree, b, ast.FunctionDef)
    assert(func.name == 'f')

if __name__ == '__main__':
    test_get_closest_parent_of()

# Generated at 2022-06-14 03:04:35.274021
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    import typed_ast.ast3 as ast
    ast3 = ast.parse("x = '''\n\n\n\n'''")
    tree: ast.Module = ast3
    expr: ast.Expr = ast.parse("'''\n\n\n\n'''").body[0]
    func: ast.FunctionDef = ast.FunctionDef(name='fn', args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[expr], decorator_list=[])
    module: ast.Module = ast.Module(body=[func])
    assert(module, func) == get_non_exp_parent_and_index(tree, expr)



# Generated at 2022-06-14 03:04:39.140732
# Unit test for function find
def test_find():
    tree = ast.parse('{0: str, 1: str}')
    parent_node = find(tree, ast.Dict)

    assert next(parent_node) == tree.body[0].value


# Generated at 2022-06-14 03:04:55.394912
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():

    # Test 1
    node = ast.parse('''
        def some_function(arg):
            for i in range(4):
                print(i)
    ''')
    parent = get_closest_parent_of(node, node.body[0].body[0], ast.FunctionDef)
    assert parent.name == 'some_function'

    # Test 2
    node = ast.parse('''
        i = 4
        j = 5
        while i < 10:
            print(i)
            i = i + 1
            j = j + 1
    ''')
    parent = get_closest_parent_of(node, node.body[2].body[0], ast.While)
    assert parent.test.comparators[0].n == 10
    assert parent.body[1].value

# Generated at 2022-06-14 03:05:03.180460
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from unittest import TestCase, main
    from ..cpp2ast import parse
    from ..cpp2ast.cpp_type import CFunc
    from ..cpp2ast.helpers import get_non_exp_parent_and_index

    def get_nodes(code):
        mod = parse(code)
        func = CFunc(CFunc.parse_declaration(('void', 'foo'), code))[0]
        return mod, func

    class TestGetNonExpParentAndIndex(TestCase):
        def test_simple(self):
            mod, func = get_nodes("""int main() {
                    int a;
                    int b;
                    int c;
                    if (a) {
                        b;
                    }
                }""")


# Generated at 2022-06-14 03:05:07.422643
# Unit test for function find
def test_find():
    tree = ast.parse("if a + 5 == 10: b = 10 if True: print('test')\n"
                     "else: print('test')")  # type: ast.Module
    for node in find(tree, ast.Name):
        assert node.id in ['a', 'b', 'True', 'test', 'print']



# Generated at 2022-06-14 03:05:20.443903
# Unit test for function replace_at
def test_replace_at():
    import ast
    import astunparse as unparsing
    # 1 + 2 => (1 + 2)
    code = """
    x = 1 + 2
    """
    ast_tree = ast.parse(code)
    new_ast_tree = ast.copy_location(ast.Expression(body=ast.copy_location(ast.BinOp(left=ast_tree.body[0].value.left, op=ast_tree.body[0].value.op, right=ast_tree.body[0].value.right), ast_tree.body[0].value)), ast_tree.body[0].value)
    replace_at(0, ast_tree, new_ast_tree)
    assert(unparsing.unparse(ast_tree) == '(x = (1 + 2))')
    # 1 + 2 => 3

# Generated at 2022-06-14 03:05:21.401091
# Unit test for function find

# Generated at 2022-06-14 03:05:26.516587
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse('''
if a:
    a = 1
else:
    a = 2
a = a
''')
    if_body_a = tree.body[0].body[0].value
    get_non_exp_parent_and_index(tree, if_body_a)

# Generated at 2022-06-14 03:05:36.833079
# Unit test for function find
def test_find():
    source = '''
    def test():
        a = 1
        print(a)
        b = 2
    '''
    tree = ast.parse(source)

    print('FunctionDefs:')
    result = list(find(tree, ast.FunctionDef))
    assert len(result) == 1
    assert result[0].name == 'test'
    print(result[0])

    print('Assigns:')
    result = list(find(tree, ast.Assign))
    assert len(result) == 2
    assert result[0].targets[0].id == 'a'
    assert result[1].targets[0].id == 'b'
    print(result[1])

    print('Exprs:')
    result = list(find(tree, ast.Expr))

# Generated at 2022-06-14 03:05:39.583313
# Unit test for function find
def test_find():
    tree = ast.parse("a = foo(1, 2)")
    func = list(find(tree, ast.FunctionDef))[0]
    assert func.name == 'foo'

# Generated at 2022-06-14 03:05:40.546769
# Unit test for function find

# Generated at 2022-06-14 03:05:41.522487
# Unit test for function find

# Generated at 2022-06-14 03:05:42.515356
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:05:47.008694
# Unit test for function replace_at
def test_replace_at():
    from typed_ast import parse
    node = parse('(x+y)*z', mode='eval')
    parent, index = get_non_exp_parent_and_index(node, node.body)
    replace_at(index, parent, parse('y+x*z', mode='eval').body)
    assert node.body == parse('y+x*z', mode='eval').body


# Generated at 2022-06-14 03:05:56.378548
# Unit test for function get_parent
def test_get_parent():
    """Test function get_parent."""
    assert_equal(
        get_parent(ast.parse("0"), ast.parse("0"), rebuild=False),
        None
    )
    assert_equal(
        type(get_parent(ast.parse("a(1)"), ast.parse("1"), rebuild=False)),
        ast.Call
    )
    assert_equal(
        type(get_parent(ast.parse("def a(): pass"), ast.parse("pass"), rebuild=False)),
        ast.FunctionDef
    )
    assert_equal(
        type(get_parent(ast.parse("a=1"), ast.parse("1"), rebuild=False)),
        ast.Assign
    )

# Generated at 2022-06-14 03:06:15.458117
# Unit test for function find
def test_find():
    import astor

    # Test for astor.parse()
    tree = astor.parse("def my_function(a, b):\n\tprint(a + b)")
    assert len([x for x in find(tree, ast.FunctionDef)]) == 1
    assert len([x for x in find(tree, ast.Call)]) == 1

    # Test for ast.parse()
    tree = ast.parse("def my_function(a, b):\n\tprint(a + b)")
    assert len([x for x in find(tree, ast.FunctionDef)]) == 1
    assert len([x for x in find(tree, ast.Call)]) == 1

# Generated at 2022-06-14 03:06:16.565850
# Unit test for function find

# Generated at 2022-06-14 03:06:20.965149
# Unit test for function find
def test_find():
    # type: () -> None
    source = 'x = 1 + 1'
    tree = ast.parse(source)
    assert len(list(find(tree, ast.Num))) == 2



# Generated at 2022-06-14 03:06:30.129876
# Unit test for function get_parent
def test_get_parent():
    test_tree = ast.parse('def foo(bar):\n'
                          '    pass\n'
                          '\n'
                          '\n'
                          'foo(None)')
    parent = get_parent(test_tree, test_tree.body[0])
    assert parent == test_tree
    parent = get_parent(test_tree, test_tree.body[0].args[0])
    assert parent == test_tree.body[0]



# Generated at 2022-06-14 03:06:30.533705
# Unit test for function find
def test_find():
    pass

# Generated at 2022-06-14 03:06:36.773998
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('def test():\n'
                     '    a = None\n'
                     '    b = a')
    node = find(tree, ast.Name).__next__()
    assert get_closest_parent_of(tree, node, ast.FunctionDef) == \
        find(tree, ast.FunctionDef).__next__()

# Generated at 2022-06-14 03:06:37.983333
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:06:49.179149
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import typing

    from .. import ast3 as ast

    def test_func():
        for i in range(1, 2):
            pass

    a = ast.parse(test_func.__code__)
    ast.fix_missing_locations(a)

    f = typing.cast(ast.FunctionDef, find(a, ast.FunctionDef).__next__())
    f.body[0].body.append(ast.Expr(value=ast.Call()))

    assert(isinstance(
        get_closest_parent_of(f, f.body[-1].value, ast.FunctionDef),
        ast.FunctionDef,
    ))

# Generated at 2022-06-14 03:06:51.544673
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse('a = 1')
    assert get_parent(tree, tree.body[0].value) == tree.body[0]

# Generated at 2022-06-14 03:06:54.966373
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():  # pylint: disable=unused-argument
    tree = ast.parse('a')

    assert tree == get_non_exp_parent_and_index(tree,
                                                tree.body[0])[0]

# Generated at 2022-06-14 03:07:10.145969
# Unit test for function find

# Generated at 2022-06-14 03:07:15.265896
# Unit test for function find
def test_find():
    import astor
    with open("./dummy.py") as f:
        dummy_code = f.read()
    dummy_tree = ast.parse(dummy_code)
    dummy_tree_str = astor.to_source(dummy_tree)
    assert str(dummy_tree_str) == dummy_code

# Generated at 2022-06-14 03:07:22.165393
# Unit test for function replace_at
def test_replace_at():
    tree = ast.parse("")
    func_def = ast.FunctionDef("f", [], [], [], None)
    func_def.body.append(ast.Return(ast.Name("foo")))
    tree.body.append(func_def)
    replace_at(0, tree, [ast.Return(ast.Name("bar"))])

    assert tree.body[0].body[0].value.id == "bar"

# Generated at 2022-06-14 03:07:28.903831
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    ast_node = ast.parse('''
if True:
    if False:
        pass
    else:
        pass
else:
    pass
''')
    else_node = get_closest_parent_of(ast_node, ast_node.body[0].body[0].body[0],
                                      type_=ast.If)
    assert isinstance(else_node, ast.If)

# Generated at 2022-06-14 03:07:36.899673
# Unit test for function find
def test_find():
    code = """
if max(5, 6) == 5:
    print('test')
    """

    tree = ast.parse(code)
    if_node = find(tree, ast.If)
    assert isinstance(if_node, Iterable)
    assert len(list(if_node)) == 1
    assert isinstance(list(if_node)[0], ast.If)

    call_node = find(tree, ast.Call)
    assert isinstance(call_node, Iterable)
    assert len(list(call_node)) == 1
    assert isinstance(list(call_node)[0], ast.Call)

    name_node = find(tree, ast.Name)
    assert isinstance(name_node, Iterable)
    assert len(list(name_node)) == 2

# Generated at 2022-06-14 03:07:39.351693
# Unit test for function find
def test_find():
    tree = ast.parse('def foo() -> int: return 1')
    print([x for x in find(tree, ast.FunctionDef)])
    print([x for x in find(tree, ast.Return)])

# Generated at 2022-06-14 03:07:41.197259
# Unit test for function find
def test_find():
    obj = ast.parse('print()\n[1,2,3]\ndef fn(): pass')
    for i in find(obj, ast.List):
        assert isinstance(i, ast.List)



# Generated at 2022-06-14 03:07:41.880548
# Unit test for function find

# Generated at 2022-06-14 03:07:47.167621
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    # Test when the node is functionDef
    node1 = ast.FunctionDef(name='a', args=ast.arguments(args=[], vararg=None,
                                                         kwonlyargs=[],
                                                         kw_defaults=[],
                                                         kwarg=None,
                                                         defaults=[]),
                            body=[], decorator_list=[], returns=None)
    # Should return the same node1 as it's the closest parent
    assert get_closest_parent_of(node1, node1, ast.FunctionDef) == node1

    # Test when the node is argument
    node2 = ast.Name(id='a')

# Generated at 2022-06-14 03:07:58.014126
# Unit test for function find
def test_find():
    import unittest
    from validate_ast import _test_data
    import astunparse
    import ast

    class TestFindMethods(unittest.TestCase):
        def test_find(self):
            tree = ast.parse(astunparse.unparse(_test_data.get_ast_tree()))
            for f in find(tree, ast.Lambda):
                print(f'LAMBDA FOUND: {f}')
                self.assertIsInstance(f, ast.Lambda)

        def test_replace_at(self):
            tree = ast.parse(astunparse.unparse(_test_data.get_ast_tree()))
            lambda_ = find(tree, ast.Lambda).__next__()
            parent = get_parent(tree, lambda_)
            index = parent.body

# Generated at 2022-06-14 03:08:45.667506
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:08:51.381831
# Unit test for function replace_at
def test_replace_at():
    """Test func replace_at"""
    module = ast.parse('print(1 + 1)')
    parent = module.body[0]
    new_node = ast.Expr(value=ast.Str(s='test'))
    replace_at(0, parent, new_node)
    assert ast.dump(module) == "Module(body=[Expr(value=Str(s='test'))])"



# Generated at 2022-06-14 03:09:02.941848
# Unit test for function find
def test_find():
    tree = ast.parse("""
        def main():
            a = 1
            b = 2

            if a > b:
                print(a)
            else:
                print(b)
        """)

    assert len(list(find(tree, ast.Num))) == 3
    assert len(list(find(tree, ast.Name))) == 4
    assert len(list(find(tree, ast.Num))) == 3
    assert len(list(find(tree, ast.Assign))) == 2
    assert len(list(find(tree, ast.If))) == 1
    assert len(list(find(tree, ast.BinOp))) == 1
    assert len(list(find(tree, ast.FunctionDef))) == 1
    assert len(list(find(tree, ast.body))) == 1

# Generated at 2022-06-14 03:09:06.067622
# Unit test for function find
def test_find():
    assert list(find(ast.parse('pass'), ast.Pass)) == [ast.Pass(lineno=1, col_offset=0)]

if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 03:09:11.137426
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = load_ast_from_file('tests/examples/numbers.py')
    print(tree)
    test_exp = tree.body[0].body.body[1]
    print(test_exp)
    parent, index = get_non_exp_parent_and_index(tree, test_exp)
    print(parent)
    print(index)
    assert isinstance(parent.body[index], ast.Expr)


# Generated at 2022-06-14 03:09:15.912846
# Unit test for function replace_at
def test_replace_at():
    import astor
    code = astor.parse_file('./example.py')
    replace_at(1, code.body[0], [ast.Num(n=2)])
    # print(astor.to_source(code))

# Generated at 2022-06-14 03:09:20.409175
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    from textwrap import dedent

    tree = ast.parse(dedent('''
    def f(x: int, y: list, z) -> str:
        if 1:
            for x in y:
                pass
            pass
        pass
    '''))

    body = find(tree, ast.FunctionDef).__next__().body

    child = body[1]
    parent = get_closest_parent_of(tree, child, ast.FunctionDef)
    assert astor.to_source(parent) == 'def f(x: int, y: list, z) -> str: ...'

    child = body[1].body[0]
    parent = get_closest_parent_of(tree, child, ast.FunctionDef)

# Generated at 2022-06-14 03:09:26.866494
# Unit test for function find
def test_find():
    test_ast = ast.parse('def f():\n    def d():\n        raise Exception')
    test_ast_found = [
        node for node in find(test_ast, ast.FunctionDef)
    ]

    assert len(test_ast_found) == 2, 'Two functions expected'

    for func in test_ast_found:
        assert isinstance(func, ast.FunctionDef),\
            'Expected FunctionDef found {}'.format(type(func))

    assert test_ast_found[0].name == 'f', 'Wrong function founf'
    assert test_ast_found[1].name == 'd', 'Wrong function founf'



# Generated at 2022-06-14 03:09:28.009930
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor


# Generated at 2022-06-14 03:09:42.362954
# Unit test for function find
def test_find():
    class ExampleNode(ast.AST):
        _fields = ('test',)

        def __init__(self, test: ast.AST) -> None:
            super().__init__()
            self.test = test

    class ExampleClass(ast.AST):
        _fields = ('a', 'b', 'body', 'c')

        def __init__(self, a: ast.AST, b: ast.AST,
                     body: List[ast.AST], c: ast.AST) -> None:
            super().__init__()
            self.a = a
            self.b = b
            self.body = body
            self.c = c
