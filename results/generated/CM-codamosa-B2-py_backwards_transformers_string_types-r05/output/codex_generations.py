

# Generated at 2026-11-03 05:14:38.651397
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert transformer is not None
    assert isinstance(transformer, StringTypesTransformer)
    assert transformer.target == (2, 7)
    assert issubclass(StringTypesTransformer, BaseTransformer)

# Generated at 2026-11-03 05:17:41.151588
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Constructor should produce a usable instance with expected metadata
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert transformer.target == (2, 7)

    # `str` occurrences should be replaced with `unicode`
    tree = ast.parse("a = str\nb = str(x)\n")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'str' not in name_ids
    assert name_ids.count('unicode') == 2

    # A tree without `str` should be left unchanged
    tree = ast.parse("a = int\nb = bytes(x)\n")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'int' in name_ids
    assert 'bytes' in name_ids

    # Annotations using `str` should be transformed as well
    tree = ast.parse("def f(x: str) -> str:\n    return x\n")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'str' not in name_ids
    assert name_ids.count('unicode') == 2

    # `str` inside string literals or attribute names must not be touched
    tree = ast.parse('a = "str"\nb.attr = 1\n')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'str' not in name_ids

# Generated at 2026-11-03 05:20:30.724575
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Class metadata
    assert StringTypesTransformer.target == (2, 7)

    # 'str' should be replaced with 'unicode'
    tree = ast.parse("x = str('hello')")
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []

    names = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

    # Multiple occurrences are all replaced
    tree = ast.parse("a = str\nb = str(a)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = [node.id for node in find(result.tree, ast.Name)]
    assert names.count('unicode') == 2
    assert 'str' not in names

    # Code without 'str' is left unchanged
    tree = ast.parse("x = int('1')")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []
    names = [node.id for node in find(result.tree, ast.Name)]
    assert 'int' in names
    assert 'unicode' not in names

# Generated at 2026-11-03 05:22:35.886798
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # nonce:ba3abc7b
    from typed_ast import ast3 as ast

    # Verify class-level target
    assert StringTypesTransformer.target == (2, 7)

    # Case 1: 'str' is replaced with 'unicode', tree is flagged as changed
    tree = ast.parse("x = str(y)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []
    assert result.tree is tree  # modified in place

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

    # Case 2: multiple 'str' occurrences (including nested calls) all replaced
    tree = ast.parse("a = str(b) + len(str(c))")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert names.count('unicode') == 2
    assert 'str' not in names

    # Case 3: no 'str' present -> tree unchanged, no dependencies
    tree = ast.parse("x = bytes(y)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []
    names = set(n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name))
    assert names == {'x', 'bytes', 'y'}

    # Case 4: other builtins with similar names are untouched
    tree = ast.parse("s = structure(str_)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    names = set(n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name))
    assert names == {'s', 'structure', 'str_'}