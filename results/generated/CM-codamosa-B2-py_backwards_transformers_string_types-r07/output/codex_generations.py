

# Generated at 2026-11-03 02:58:15.824459
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert isinstance(transformer, BaseTransformer)
    assert transformer.target == (2, 7)

# Generated at 2026-11-03 03:00:21.342298
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Since StringTypesTransformer has no explicit __init__,
    # it should be instantiable without arguments (inheriting from BaseTransformer)
    instance = StringTypesTransformer()
    assert instance is not None

    # Verify class attributes are correctly defined
    assert hasattr(StringTypesTransformer, 'target')
    assert StringTypesTransformer.target == (2, 7)

    # Verify transform is a callable classmethod
    assert callable(StringTypesTransformer.transform)

    # Instantiation again should work (stateless transformer)
    instance2 = StringTypesTransformer()
    assert instance2 is not None
    assert isinstance(instance2, StringTypesTransformer)
    assert isinstance(instance2, BaseTransformer)

# Generated at 2026-11-03 03:02:22.868964
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Constructor should create a valid instance of the transformer
    transformer = StringTypesTransformer()
    assert isinstance(transformer, BaseTransformer)
    assert StringTypesTransformer.target == (2, 7)

    # Test that 'str' occurrences are replaced with 'unicode'
    tree = ast.parse("str('hello')")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []

    names = find(result.tree, ast.Name)
    assert len(names) == 1
    assert names[0].id == 'unicode'

    # Test that multiple 'str' occurrences are all replaced
    tree = ast.parse("str(x) + str(y)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = find(result.tree, ast.Name)
    assert len(names) == 2
    assert all(node.id == 'unicode' for node in names)

    # Test that trees without 'str' remain unchanged
    tree = ast.parse("unicode('hello')")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    names = find(result.tree, ast.Name)
    assert all(node.id != 'str' for node in names)

# Generated at 2026-11-03 03:06:31.011030
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():# Constructor should produce a valid instance with expected class metadata
    transformer = StringTypesTransformer()
    assert transformer is not None
    assert transformer.target == (2, 7)

    # transform() should replace `str` with `unicode` and report the change
    tree = ast.parse("x = str(y)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []
    assert result.tree is tree

    name_ids = [node.id for node in ast.walk(result.tree) if isinstance(node, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids

    # All occurrences of `str` in a more complex expression should be replaced
    tree = ast.parse("print(str(1), len(str))")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []
    name_ids = [node.id for node in ast.walk(result.tree) if isinstance(node, ast.Name)]
    assert name_ids.count('unicode') == 3
    assert 'str' not in name_ids

    # Trees without `str` should remain unchanged
    tree = ast.parse("x = unicode(y)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []

    # Trees without any Name nodes should remain unchanged
    tree = ast.parse("pass")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []