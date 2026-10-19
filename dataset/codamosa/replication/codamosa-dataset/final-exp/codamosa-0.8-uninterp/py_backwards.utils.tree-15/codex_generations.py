

# Generated at 2022-06-14 03:01:29.729510
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    pass

# Generated at 2022-06-14 03:01:37.198224
# Unit test for function find
def test_find():
    tree = ast.parse('def foo2(a: int) -> str:\n    return "bar"')
    functions = list(find(tree, ast.FunctionDef))

    assert len(functions) == 1
    assert functions[0].name == 'foo2'
    assert functions[0].args.args[0].arg == 'a'
    assert isinstance(functions[0].args.args[0].annotation, ast.Name)
    assert functions[0].args.args[0].annotation.id == 'int'

# Generated at 2022-06-14 03:01:37.809717
# Unit test for function get_parent

# Generated at 2022-06-14 03:01:39.139401
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:01:47.675455
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:01:48.260754
# Unit test for function replace_at
def test_replace_at():
    pass

# Generated at 2022-06-14 03:01:53.315373
# Unit test for function get_parent
def test_get_parent():
    tree = ast.parse("""
                      [1,
                      2,
                      3]
                      """)
    elt = tree.body[0].value.elts[0]
    parent = get_parent(tree, elt)
    assert isinstance(parent, ast.List)
    assert parent.elts[0] == 1



# Generated at 2022-06-14 03:02:04.123622
# Unit test for function get_parent
def test_get_parent():
    class MyNode(ast.AST): pass
    class MyNode2(ast.AST): pass
    class MyNode3(ast.AST): pass

    def func(a, b, c=1, d=2):
        return a + b + c + d

    node = MyNode()
    node2 = MyNode2()
    node3 = MyNode3()

    func_def = get_closest_parent_of(func.__code__, node, ast.FunctionDef)
    func_def.body = [node2, node3]
    arg_b = get_closest_parent_of(func.__code__, node3, ast.arg)
    arg_b.args = [node]

    assert get_parent(func.__code__, node) == arg_b

# Generated at 2022-06-14 03:02:10.503595
# Unit test for function replace_at
def test_replace_at():
    import typed_astunparse
    from . import ast_utils    
    
    body = ast_utils.ast_parse("""
foo = 1
bar = 2
baz = 3
    """)
    print(typed_astunparse.astunparse(body))
    print('---')
    replace_at(2, body, ast_utils.ast_parse("foo = 2"))
    print(typed_astunparse.astunparse(body))

if __name__ == '__main__':
    test_replace_at()

# Generated at 2022-06-14 03:02:11.392584
# Unit test for function replace_at

# Generated at 2022-06-14 03:02:15.240033
# Unit test for function find

# Generated at 2022-06-14 03:02:22.272965
# Unit test for function get_parent
def test_get_parent():
    """Test for get_parent function."""
    test_tree_str = """
        def func(x):
            return x + 1
    """

    test_tree = ast.parse(test_tree_str)
    assert get_parent(test_tree, test_tree.body[0].body[0].value.args[0]) == \
           test_tree.body[0].body[0].value
    assert get_parent(test_tree, test_tree.body[0].body[0].value) == \
           test_tree.body[0]


# Generated at 2022-06-14 03:02:33.226122
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    import astunparse
    import sys
    if len(sys.argv) < 2:
        print("""First arg must be a string to test get_closest_parent_of.
This function takes in an ast node and returns an ast node of requested type.
""")
        return

    src = astunparse.unparse(ast.parse(sys.argv[1]))
    tree = ast.parse(src)
    node = tree.body[0]
    print(astunparse.unparse(node))
    print(astunparse.unparse(get_closest_parent_of(tree, node, ast.FunctionDef)))
    print(astunparse.unparse(get_closest_parent_of(tree, node, ast.Module)))

# Generated at 2022-06-14 03:02:40.998226
# Unit test for function replace_at
def test_replace_at():
    root = ast.parse('def func1():pass')
    def_node = root.body[0]
    assert isinstance(def_node, ast.FunctionDef)
    body_node = def_node.body

    node_to_replace = ast.Pass()

    insert_at(0, body_node, node_to_replace)
    assert body_node.body[0] is node_to_replace

    node_to_insert = ast.Pass()
    replace_at(0, body_node, node_to_insert)
    assert body_node.body[0] is node_to_insert



# Generated at 2022-06-14 03:02:42.688075
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:02:49.644135
# Unit test for function get_parent
def test_get_parent():
    code = "def foo(x, y):\n  return x + y"
    tree = ast.parse(code)
    node = tree.body[0]

    assert get_parent(tree, node) is tree

    node = node.body[0].value

    assert get_parent(tree, node) is tree.body[0]



# Generated at 2022-06-14 03:02:54.681147
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    from tests.utils.helpers import random_function_declaration

    func = random_function_declaration()
    assert(isinstance(get_closest_parent_of(func, func.body[0], ast.FunctionDef),
                      ast.FunctionDef))

# Generated at 2022-06-14 03:02:55.932362
# Unit test for function find

# Generated at 2022-06-14 03:02:57.794390
# Unit test for function get_non_exp_parent_and_index

# Generated at 2022-06-14 03:03:02.678586
# Unit test for function get_closest_parent_of
def test_get_closest_parent_of():
    tree = ast.parse('for _ in []:\n    pass')
    node = ast.parse(tree.body[0].body[0].value.args[0].s)
    parent = get_closest_parent_of(tree, node, ast.For)
    assert isinstance(parent, ast.For)

    tree = ast.parse('(1, 2)')
    node = ast.parse(tree.body[0].value.args[1].s)
    parent = get_closest_parent_of(tree, node, ast.Module)
    assert isinstance(parent, ast.Module)