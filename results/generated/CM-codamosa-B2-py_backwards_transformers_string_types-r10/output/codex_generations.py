

# Generated at 2026-11-03 02:43:01.152823
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():# Test that 'str' is replaced with 'unicode' and tree is marked as changed
    tree = ast.parse("str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []
    assert result.tree is tree  # transformation happens in place
    names = find(result.tree, ast.Name)
    assert len(names) == 1
    assert names[0].id == 'unicode'

    # Test multiple occurrences of 'str'
    tree = ast.parse("str + str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = find(result.tree, ast.Name)
    assert len(names) == 2
    assert all(node.id == 'unicode' for node in names)

    # Test that a tree without 'str' is not marked as changed
    tree = ast.parse("int")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []
    names = find(result.tree, ast.Name)
    assert len(names) == 1
    assert names[0].id == 'int'

    # Test 'str' inside a function call
    tree = ast.parse("x = str(value)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = [n for n in find(result.tree, ast.Name) if n.id == 'unicode']
    assert len(names) == 1

    # Test target version attribute
    assert StringTypesTransformer.target == (2, 7)
# nonce:4fae1795

# Generated at 2026-11-03 02:45:39.051948
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Since StringTypesTransformer does not define its own __init__,
    # it should be instantiable without arguments (inheriting from BaseTransformer).
    transformer = StringTypesTransformer()

    # Verify the instance is created successfully
    assert transformer is not None
    assert isinstance(transformer, StringTypesTransformer)
    assert isinstance(transformer, BaseTransformer)

    # Verify class-level attributes are accessible via the instance
    assert transformer.target == (2, 7)

# Generated at 2026-11-03 02:48:48.600189
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Constructor should produce a valid instance with expected attributes
    transformer = StringTypesTransformer()
    assert isinstance(transformer, BaseTransformer)
    assert transformer.target == (2, 7)

    # `str` must be replaced with `unicode` and change must be reported
    tree = ast.parse('x = str(y)')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.warnings == []
    names = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

    # Tree without `str` must remain unchanged
    tree = ast.parse('x = int(y)')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.warnings == []
    names = [node.id for node in find(result.tree, ast.Name)]
    assert 'int' in names
    assert 'unicode' not in names

# Generated at 2026-11-03 02:50:20.885260
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Verify class-level attributes
    assert StringTypesTransformer.target == (2, 7)
    assert hasattr(StringTypesTransformer, 'transform')
    assert callable(StringTypesTransformer.transform)

    # Case 1: code containing 'str' should be transformed to 'unicode'
    tree = ast.parse("x = str('hello')\ny = str")
    result = StringTypesTransformer.transform(tree)

    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.warnings == []

    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids

    # Case 2: code without 'str' should remain unchanged
    tree = ast.parse("x = int('5')")
    result = StringTypesTransformer.transform(tree)

    assert isinstance(result, TransformationResult)
    assert result.tree_changed is False
    assert result.warnings == []

    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'str' not in name_ids

    # Case 3: attribute names and string literals named 'str' are not replaced
    tree = ast.parse("obj.str = 'str'")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is False
    assert result.warnings == []