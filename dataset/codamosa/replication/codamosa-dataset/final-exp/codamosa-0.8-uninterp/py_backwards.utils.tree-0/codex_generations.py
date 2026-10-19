

# Generated at 2022-06-14 03:01:28.200392
# Unit test for function find

# Generated at 2022-06-14 03:01:29.538683
# Unit test for function get_closest_parent_of

# Generated at 2022-06-14 03:01:36.011458
# Unit test for function insert_at
def test_insert_at():
    module = ast.parse('def foo():\n    pass')
    module.body[0].body.append(ast.Pass(lineno=3, col_offset=4))
    insert_at(1, module, ast.Pass(lineno=1, col_offset=2))
    assert str(module) == 'def foo():\n    pass\n    pass\n'

# Generated at 2022-06-14 03:01:39.738576
# Unit test for function find
def test_find():
    module = ast.parse('import os\nprint(os.getcwd())')
    for import_ in find(module, ast.Import):
        print(import_.names)
    for name in find(module, ast.Name):
        print(name.id)



# Generated at 2022-06-14 03:01:45.750310
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    class Parent(ast.AST):
        _fields = ('body',)

    class Child(ast.AST):
        _fields = ('arg',)

    parent = Parent()
    parent.body = [Child(), Child()]
    assert (parent, 1) == \
        get_non_exp_parent_and_index(parent, parent.body[1])

    grandparent = Parent()
    grandparent.body = [parent]
    assert (grandparent, 0) == \
        get_non_exp_parent_and_index(grandparent, parent.body[1])

# Generated at 2022-06-14 03:01:57.443251
# Unit test for function find
def test_find():
    import astor
    code = """
    def foo(a):
        a = a +1
        return a
    """
    tree = ast.parse(code)
    _build_parents(tree)

    def_foo = find(tree, ast.FunctionDef).__next__()
    assert isinstance(def_foo, ast.FunctionDef)

    return_a = find(tree, ast.Return).__next__()
    assert isinstance(return_a, ast.Return)
    assert astor.to_source(return_a).strip() == 'return a'

    a_plus1 = get_parent(tree, return_a)
    assert astor.to_source(a_plus1).strip() == 'a +1'

    a_plus1_parent, a_plus1_index = get_non_exp_parent

# Generated at 2022-06-14 03:01:58.214391
# Unit test for function find

# Generated at 2022-06-14 03:02:06.074114
# Unit test for function get_non_exp_parent_and_index
def test_get_non_exp_parent_and_index():
    def test_func():
        foo = 1
        if foo:
            print(foo)
        else:
            print(1)

    tree = ast.parse(inspect.getsource(test_func))

    parent_and_index = get_non_exp_parent_and_index(tree, tree.body[0].body[0].body[0].body[0])
    assert isinstance(parent_and_index, tuple)
    assert isinstance(parent_and_index[0], ast.If)
    assert isinstance(parent_and_index[1], int)
    assert parent_and_index[1] == 0

# Generated at 2022-06-14 03:02:12.213117
# Unit test for function insert_at
def test_insert_at():
    """Unit test for function insert_at."""
    code = 'if a:\n  pass\n  pass\n'
    tree = ast.parse(code)
    _build_parents(tree)
    if_node = get_parent(tree, tree.body[0].body[0])  # type: ignore
    insert_at(1, if_node, ast.parse(code).body[0].body[0])  # type: ignore
    assert len(if_node.body) == 3
    print('Test for function insert_at passed.')



# Generated at 2022-06-14 03:02:14.706992
# Unit test for function get_parent
def test_get_parent():
    node = ast.parse("print(__name__)")
    parent = get_parent(node, node.body[0])
    assert parent == node

