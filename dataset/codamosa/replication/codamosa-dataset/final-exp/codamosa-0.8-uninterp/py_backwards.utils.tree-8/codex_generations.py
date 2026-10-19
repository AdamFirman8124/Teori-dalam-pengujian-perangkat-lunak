

# Generated at 2022-06-14 03:01:41.239580
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    from . import ast_from_source as afs
    
    code = 'def foo(a,b):\n\tc = d\n'
    tree = afs(code)
    node = find(tree, ast.Name).__next__()
    parent, index = get_non_exp_parent_and_index(tree, node)
    assert isinstance(parent, ast.FunctionDef)
    assert index == 1


# Generated at 2022-06-14 03:01:48.506477
# Unit test for function replace_at
def test_replace_at():
    import astor
    code_1 = '''
    class A(object):
        def __init__(self):
            self.a = 1
    '''

    code_2 = '''
    class A(object):
        def __init__(self):
            self.a = 2
    '''

    code_3 = '''
    class A(object):
        def __init__(self):
            self.a = 2
            self.b = 3
    '''

    code_4 = '''
    class A(object):
        def __init__(self):
            self.a = 2
            self.b = 4
            self.c = 5
    '''

    def assert_replace(code_from, code_to, node_type, idx, value, code_to_assert):
        tree1

# Generated at 2022-06-14 03:01:49.172432
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    assert False

# Generated at 2022-06-14 03:01:56.541249
# Unit test for function get_parent
def test_get_parent():
    import unittest
    from .parser import parse

    class GetParentTest(unittest.TestCase):
        def test(self):
            ast_ = parse('''
                def foo():
                    a = 1
                    return a
                ''')
            parent = get_parent(ast_, ast_.body[0].body[0].value)

            self.assertEqual(ast_.body[0].body[0], parent)

    unittest.TestCase(GetParentTest().test())


# Generated at 2022-06-14 03:01:59.405625
# Unit test for function find
def test_find():
    tree = ast.parse('''
        for i in range(10):
            print('Hello world')
    ''')

    for_node = find(tree, ast.For).__next__()
    assert for_node.__class__.__name__ == 'For'



# Generated at 2022-06-14 03:02:03.902523
# Unit test for function get_parent
def test_get_parent():
    t = ast.parse('a = 1 + 1')
    assert get_parent(t, t.body[0].targets[0]) == t.body[0]
    assert get_parent(t, t.body[0]) == t

# Generated at 2022-06-14 03:02:08.993547
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    """Function to test get_closest_parent_of."""
    ast_tree = ast.parse('def a():\n\tpass')
    parent = get_closest_parent_of(ast_tree, ast_tree.body[0], ast.FunctionDef)

    assert(isinstance(parent, ast.FunctionDef))
    assert(parent.name == 'a')



# Generated at 2022-06-14 03:02:11.770916
# Unit test for function find
def test_find():
    def func():
        a = 1 + 1
        b = a + 1
        c = b + 1
        return c

    tree = ast.parse(inspect.getsource(func))
    assert len(list(find(tree, ast.Num))) == 3

# Generated at 2022-06-14 03:02:21.070546
# Unit test for function find
def test_find():
    # type: (None) -> None
    # Example code
    code = "for i in range(10):\n\tprint(i)"
    print("Testing function on code:")
    print(code)
    # Build AST tree
    tree = ast.parse(code)
    # Find all for loops in code
    for for_loop in find(tree, ast.For):
        print("For loop found!")
        # Find all if statements in for loop
        for if_statement in find(for_loop, ast.If):
            print("If statement found!")
    # Test if for loop was found
    if for_loop:
        print("Passed!")
    else:
        print("Failed!")


# Generated at 2022-06-14 03:02:26.946917
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("""
        class A(object):
            def add(self, a, b):
                return a + b
    """)
    func = tree.body[0].body[0]
    parent, index = get_non_exp_parent_and_index(tree, func)
    assert isinstance(parent, ast.ClassDef)
    assert parent.body[index] is func
    assert index == 0



# Generated at 2022-06-14 03:03:37.987149
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    test_ast = ast.parse("a = [i for i in range(0, 10)]")
    test_expr = get_closest_parent_of(test_ast, test_ast.body[0].value, ast.Expr)

    assert isinstance(test_expr, ast.Expr)


# Generated at 2022-06-14 03:03:44.480377
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class A():
        def __init__(self, value):
            self.value = value

    true = A(True)
    false = A(False)

    # Asserting that get_non_exp_parent_and_index returns result for the 'true'
    # variable.
    assert get_non_exp_parent_and_index(true, false) == (true, 0)

# Generated at 2022-06-14 03:03:45.768599
# Unit test for function find
def test_find():
    pass



# Generated at 2022-06-14 03:03:50.592670
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    assert get_closest_parent_of(ast.parse(textwrap.dedent('''
        def foo(x):
            y = x + 1
            return y
        ''')), ast.parse(textwrap.dedent('''
        y = x + 1
        ''')).body[0], ast.FunctionDef) == ast.parse(textwrap.dedent('''
        def foo(x):
            y = x + 1
            return y
        ''')).body[0]

# Generated at 2022-06-14 03:03:54.844203
# Unit test for function find
def test_find():
    code = """
    class A:
        pass
        
    def func():
        pass
        
    a = A()
    func()
    """
    tree = ast.parse(code)
    assert(len(list(find(tree, ast.ClassDef))) == 1)

# Generated at 2022-06-14 03:03:58.490388
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import sys
    from . import ASTTestCase


# Generated at 2022-06-14 03:03:59.761324
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astunparse


# Generated at 2022-06-14 03:04:07.715962
# Unit test for function find
def test_find():
    import unittest

    from . import ast3 as ast

    class Tests(unittest.TestCase):

        def test_find(self):
            nodes = list(find(ast.parse('a = 1\na = 2'), ast.Assign))

            self.assertEqual(len(nodes), 2)
            self.assertTrue(nodes[0].lineno == 1)
            self.assertTrue(nodes[1].lineno == 2)

    unittest.main()

# Generated at 2022-06-14 03:04:09.801308
# Unit test for function find

# Generated at 2022-06-14 03:04:11.858096
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:09:14.043820
# Unit test for function find
def test_find():
    code = """
        from pylint.testutils import _FakeChecker
        from astroid.node_classes import Assign, Attribute, Name, Const


        class Some(object):
            pass
        """

    tree = ast.parse(code)  # type: ignore
    nodes = list(find(tree, ast.Import))

    assert len(nodes) == 1
    assert str(nodes[0]) == 'from pylint.testutils import _FakeChecker'

    nodes = list(find(tree, ast.ClassDef))

    assert len(nodes) == 2
    assert str(nodes[1]) == 'class Some(object):'

    nodes = list(find(tree, ast.Attribute))

    assert len(nodes) == 3
    assert str(nodes[2]) == 'pass'


#

# Generated at 2022-06-14 03:09:23.118330
# Unit test for function find
def test_find():
    tree = ast.parse("""
    class A(object):
        def __init__(self, a):
            self.a = a

        def __eq__(self, other):
            return self.a == other.a

    a = A(1)
    """)

    assert len(list(find(tree, ast.ClassDef))) == 1
    assert len(list(find(tree, ast.Assign))) == 1
    assert len(list(find(tree, ast.Load))) == 2
    assert len(list(find(tree, ast.Name))) == 2

# Generated at 2022-06-14 03:09:30.043533
# Unit test for function find
def test_find():
    tree = ast.parse('x=x+1')
    list(find(tree, ast.Assign))
    list(find(tree, ast.Name))
    assert len(list(find(tree, ast.Load))) == 1

    tree = ast.parse('x=x+1\nx=x+1')
    assert len(list(find(tree, ast.Load))) == 2



# Generated at 2022-06-14 03:09:45.823037
# Unit test for function find
def test_find():
    prog = ast.parse("""
        from collections import namedtuple as named_tuple
        import logging
        def main():
            tuple_ = named_tuple()
            logging.info(tuple_.name)
    """)

    mod_refs = find(prog, ast.Name)
    mod_names = [ref.id for ref in mod_refs]

    assert "logging" in mod_names
    assert "named_tuple" in mod_names

    fun_refs = find(prog, ast.FunctionDef)
    fun_names = [ref.name for ref in fun_refs]

    assert "main" in fun_names

    call_refs = find(prog, ast.Call)
    call_names = [ref.func.id for ref in call_refs]


# Generated at 2022-06-14 03:09:54.210483
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    a = ast.parse("a, b = 0, 1")
    b =  ast.Assign(targets=[
        ast.Name(id="a", ctx=ast.Store()),
        ast.Name(id="b", ctx=ast.Store())],
                   value=ast.Tuple(elts=[
                       ast.Num(n=0),
                       ast.Num(n=1)],
                       ctx=ast.Load())
                    )
    print("Input:")
    print(astor.to_source(a))
    test_value = ast.Name(id="a", ctx=ast.Store())
    test_type = ast.Attribute
    t = get_closest_parent_of(a, test_value, test_type)
    print("Output:")
    print

# Generated at 2022-06-14 03:10:07.838965
# Unit test for function find
def test_find():
    from typed_ast import ast3 as ast
    tree = ast.parse('''
    def foo():
        for x in range(10):
            pass
    ''')

    for x in find(tree, ast.Name):
        print(x)



# Generated at 2022-06-14 03:10:12.788317
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    tree = ast.parse("for i in range(10): print(i)")
    assert get_non_exp_parent_and_index(tree, tree.body[0].body[0]) == (tree.body[0].body[0], 0)



# Generated at 2022-06-14 03:10:20.780641
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astor
    from typo.preprocessor import preprocess
    from ..refactor import RefactorTool, RefactorError

    class TestTool(RefactorTool):
        def visit_BinOp(self, node: ast.BinOp) -> None:
            super().generic_visit(node)

            node.left = get_closest_parent_of(node, node, ast.FunctionDef)

    tree = ast.parse('''
    def foo():
        return 5 + 4
    ''')

    preprocess(tree)
    TestTool().refactor_tree(tree)
    assert astor.to_source(tree) == '''
    def foo():
        return foo
    '''

# Generated at 2022-06-14 03:10:32.098036
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    print("Testing get_non_exp_parent_and_index()...")

    assert(ast.parse("pass").body == get_non_exp_parent_and_index(
           ast.parse("pass"), ast.parse("pass").body[0])[0].body)
    assert(ast.parse("if 1:\n    pass").body[0].body ==
           get_non_exp_parent_and_index(ast.parse("if 1:\n    pass"),
                                        ast.parse("if 1:\n    pass").body[0]
                                        .body[0])[0].body)

    print("get_non_exp_parent_and_index() is working correctly.")



# Generated at 2022-06-14 03:10:36.449314
# Unit test for function find
def test_find():
    """Find all nodes with type ast.Assign."""
    tree = ast.parse('abc = 123')
    found_nodes = find(tree, ast.Assign)
    assert len(list(found_nodes)) == 1
