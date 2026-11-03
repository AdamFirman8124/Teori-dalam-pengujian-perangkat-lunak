

# Generated at 2026-11-01 19:35:33.205771
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
# nonce:befad962
    # Test 1: 'str' is replaced with 'unicode' and tree_changed is True
    tree = ast.parse("x = str('hello')")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    assert result.dependencies == []
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids

    # Test 2: other identifiers are left untouched and tree_changed is False
    tree = ast.parse("x = int('10')")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is False
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'int' in name_ids
    assert 'unicode' not in name_ids

    # Test 3: multiple occurrences of 'str' are all replaced
    tree = ast.parse("a = str('a')\nb = str('b')")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is True
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert name_ids.count('unicode') == 2
    assert 'str' not in name_ids

    # Test 4: target version attribute
    assert StringTypesTransformer.target == (2, 7)

# Generated at 2026-11-01 19:36:15.449452
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # nonce:8e49f22c
    # Class-level checks (constructor/attributes)
    assert StringTypesTransformer.target == (2, 7)
    assert issubclass(StringTypesTransformer, BaseTransformer)

    # Replaces 'str' with 'unicode' and marks the tree as changed
    tree = ast.parse("x = str(y)")
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.tree is tree
    assert result.dependencies == []
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids
    assert 'y' in name_ids

    # All occurrences of 'str' are replaced
    tree = ast.parse("a = str\nb = str(a)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert name_ids.count('unicode') == 2
    assert 'str' not in name_ids

    # Tree without 'str' is left unchanged
    tree = ast.parse("x = int('42')")
    original_ids = [node.id for node in find(tree, ast.Name)]
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert [node.id for node in find(result.tree, ast.Name)] == original_ids

    # Identifiers merely containing 'str' are untouched
    tree = ast.parse("string = my_str + strict")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert {node.id for node in find(result.tree, ast.Name)} == {'string', 'my_str', 'strict'}

    # Trivial tree without any names
    result = StringTypesTransformer.transform(ast.parse("pass"))
    assert result.tree_changed is False

# Generated at 2026-11-01 19:36:53.644774
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test instantiation
    transformer = StringTypesTransformer()
    assert transformer is not None

    # Verify class attributes
    assert StringTypesTransformer.target == (2, 7)

    # Test transformation: str -> unicode
    tree = ast.parse("x = str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []

    # Verify all 'str' names are replaced with 'unicode'
    name_nodes = find(result.tree, ast.Name)
    for node in name_nodes:
        assert node.id != 'str'

    # Test with no 'str' references - tree should not change
    tree2 = ast.parse("x = int")
    result2 = StringTypesTransformer.transform(tree2)
    assert result2.tree_changed is False
    assert result2.dependencies == []

    # Test with multiple 'str' references
    tree3 = ast.parse("a = str\nb = str\nc = str")
    result3 = StringTypesTransformer.transform(tree3)
    assert result3.tree_changed is True
    unicode_count = sum(1 for node in find(result3.tree, ast.Name) if node.id == 'unicode')
    assert unicode_count == 3

    # Test that original tree is returned in result
    tree4 = ast.parse("y = str")
    result4 = StringTypesTransformer.transform(tree4)
    assert result4.tree is tree4

# Generated at 2026-11-01 19:37:52.217845
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert transformer.target == (2, 7)
    assert hasattr(transformer, 'transform')
    assert callable(transformer.transform)

# Generated at 2026-11-01 19:38:39.327047
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Case 1: `str` occurrences are replaced with `unicode`
    tree = ast.parse("x = str(1)\ny = str")
    result = StringTypesTransformer.transform(tree)

    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []

    ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in ids
    assert 'str' not in ids

    # Case 2: no `str` present, tree remains unchanged
    tree = ast.parse("x = int(1)")
    result = StringTypesTransformer.transform(tree)

    assert result.tree_changed is False
    assert result.dependencies == []

    # Case 3: original tree object is returned unmodified structurally apart from renames
    tree = ast.parse("s = str(s)")
    result = StringTypesTransformer.transform(tree)

    call_func = find(result.tree, ast.Name)[0]
    assert call_func.id == 'unicode'
    assert result.tree_changed is True

# Generated at 2026-11-01 19:39:27.448512
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # The class requires no constructor arguments and inherits from BaseTransformer
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert isinstance(transformer, BaseTransformer)
    # Class-level attributes should be intact after instantiation
    assert transformer.target == (2, 7)
    assert hasattr(transformer, 'transform')


# Additional tests for the transform classmethod
def test_StringTypesTransformer_transform_replaces_str():
    tree = ast.parse("x = str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree is tree
    assert result.tree_changed is True
    assert result.transformations == []
    assert result.tree.body[0].value.id == 'unicode'


def test_StringTypesTransformer_transform_no_match():
    tree = ast.parse("x = unicode")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.transformations == []


def test_StringTypesTransformer_transform_partial_match_untouched():
    # Names like 'str_' or 'strange' must not be replaced
    tree = ast.parse("str_ = strange")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.tree.body[0].targets[0].id == 'str_'
    assert result.tree.body[0].value.id == 'strange'

# Generated at 2026-11-01 19:40:05.644436
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # The transformer should be instantiable (inherits BaseTransformer)
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert StringTypesTransformer.target == (2, 7)

    # Transform should replace `str` name with `unicode` and report changes
    tree = ast.parse('a = str(b)')
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []
    assert isinstance(result.tree, ast.AST)

    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

    # Transform should leave trees without `str` untouched
    tree = ast.parse('a = bytes(b)')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []
    names = [n.id for n in ast.walk(result.tree) if isinstance(n, ast.Name)]
    assert 'bytes' in names
    assert 'unicode' not in names

# Generated at 2026-11-01 19:40:34.813600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test instantiation and class attributes
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)
    assert transformer.target == (2, 7)

    # Test transform replaces 'str' with 'unicode'
    tree = ast.parse("a = str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.transformations == []
    assert result.tree is tree
    node_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in node_ids
    assert 'str' not in node_ids

    # Test transform leaves tree unchanged when no 'str' present
    tree2 = ast.parse("a = int")
    result2 = StringTypesTransformer.transform(tree2)
    assert result2.tree_changed is False
    assert result2.tree is tree2
    assert result2.transformations == []

# Generated at 2026-11-01 19:41:43.337936
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
# nonce:3fd37616
    # Test instantiation (constructor inherited from BaseTransformer)
    transformer = StringTypesTransformer()
    assert isinstance(transformer, StringTypesTransformer)

    # Test class attributes
    assert StringTypesTransformer.target == (2, 7)

    # Test transform: 'str' should be replaced with 'unicode'
    tree = ast.parse("x = str")
    result = StringTypesTransformer.transform(tree)

    assert result.tree is not None
    assert result.tree_changed is True
    assert result.transformed_by == []

    # Verify the replacement happened
    name_ids = [node.id for node in ast.walk(result.tree) if isinstance(node, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids

    # Test transform on a tree without 'str' - tree should not be changed
    tree_no_str = ast.parse("x = int('5')")
    result_no_str = StringTypesTransformer.transform(tree_no_str)

    assert result_no_str.tree_changed is False
    assert result_no_str.transformed_by == []

    # Test transform with multiple 'str' occurrences
    tree_multiple = ast.parse("a = str\nb = str(a)")
    result_multiple = StringTypesTransformer.transform(tree_multiple)

    assert result_multiple.tree_changed is True
    names = [node.id for node in ast.walk(result_multiple.tree) if isinstance(node, ast.Name)]
    assert names.count('unicode') == 2
    assert 'str' not in names

# Generated at 2026-11-01 19:42:18.365131
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Constructor (inherited from BaseTransformer) creates a usable instance
    transformer = StringTypesTransformer()
    assert transformer is not None
    assert isinstance(transformer, BaseTransformer)

    # Class-level metadata
    assert StringTypesTransformer.target == (2, 7)
    assert callable(StringTypesTransformer.transform)

    # Functional check: replaces 'str' with 'unicode' and reports change
    tree = ast.parse("a = str(b)\nc = list(d)\ne = str(f)")
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []

    names = {node.id for node in ast.walk(result.tree)
             if isinstance(node, ast.Name)}
    assert 'unicode' in names
    assert 'str' not in names

    # No change reported when there is nothing to replace
    tree = ast.parse("a = int(b)")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False

# Generated at 2026-11-01 19:42:48.667297
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # 'str' should be replaced with 'unicode'
    tree = ast.parse('a = str')
    result = StringTypesTransformer.transform(tree)

    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []

    ids = {node.id for node in find(result.tree, ast.Name)}
    assert ids == {'a', 'unicode'}

    # All occurrences of 'str' should be replaced
    tree = ast.parse('a = str\nb = str')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.dependencies == []

    ids = {node.id for node in find(result.tree, ast.Name)}
    assert ids == {'a', 'b', 'unicode'}

    # Trees without 'str' should not be changed
    tree = ast.parse('a = int')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []

    ids = {node.id for node in find(result.tree, ast.Name)}
    assert ids == {'a', 'int'}

    # Names merely containing 'str' should be left untouched
    tree = ast.parse('string = 1\nstrict = 2')
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []

    ids = {node.id for node in find(result.tree, ast.Name)}
    assert ids == {'string', 'strict'}

    # Transformer targets Python 2.7
    assert StringTypesTransformer.target == (2, 7)

# Generated at 2026-11-01 19:43:18.978340
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
# nonce:0e6fdc95
    # The transformer can be instantiated and exposes its target version
    transformer = StringTypesTransformer()
    assert transformer.target == (2, 7)

    # `str` is replaced with `unicode`
    tree = ast.parse("x = str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    assert result.overrides == []
    names = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in names
    assert 'str' not in names

    # Multiple occurrences are all replaced
    tree = ast.parse("a = str\nb = str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    names = [node.id for node in find(result.tree, ast.Name)]
    assert names.count('unicode') == 2
    assert 'str' not in names

    # Nothing changes when there is no `str` in the tree
    tree = ast.parse("x = int")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.overrides == []
    names = [node.id for node in find(result.tree, ast.Name)]
    assert names == ['x', 'int']

# Generated at 2026-11-01 19:44:09.975284
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Class exposes the expected interface
    assert StringTypesTransformer.target == (2, 7)
    assert callable(getattr(StringTypesTransformer, 'transform', None))

    # Default construction succeeds
    instance = StringTypesTransformer()
    assert isinstance(instance, StringTypesTransformer)
    assert isinstance(instance, BaseTransformer)

    # 'str' occurrences are replaced with 'unicode'
    tree = ast.parse("x = str(y)")
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree is tree
    assert result.tree_changed is True
    assert result.dependencies == []
    assert ast.dump(result.tree) == ast.dump(ast.parse("x = unicode(y)"))

    # Trees without 'str' are reported unchanged
    other_tree = ast.parse("x = list(y)")
    other_result = StringTypesTransformer.transform(other_tree)
    assert other_result.tree_changed is False
    assert other_result.dependencies == []
    assert ast.dump(other_result.tree) == ast.dump(ast.parse("x = list(y)"))

# Generated at 2026-11-01 19:44:38.595994
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():
    # Test replacing a simple 'str' name with 'unicode'
    tree = ast.parse("x = str")
    result = StringTypesTransformer.transform(tree)
    assert isinstance(result, TransformationResult)
    assert result.tree_changed is True
    assert result.dependencies == []
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'unicode' in name_ids
    assert 'str' not in name_ids

    # Test that unrelated names are left untouched
    tree = ast.parse("x = int('5')")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False
    assert result.dependencies == []
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert 'int' in name_ids
    assert 'unicode' not in name_ids

    # Test multiple occurrences of 'str' in different contexts
    tree = ast.parse("a = str\nb = str(x)\nc: str = 'text'")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is True
    name_ids = [node.id for node in find(result.tree, ast.Name)]
    assert name_ids.count('unicode') == 3
    assert 'str' not in name_ids

    # Test that string literals containing 'str' are not modified
    tree = ast.parse("x = 'str'")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False

    # Test that an attribute named 'str' is not affected (Attribute, not Name)
    tree = ast.parse("obj.str")
    result = StringTypesTransformer.transform(tree)
    assert result.tree_changed is False

    # Test target version attribute
    assert StringTypesTransformer.target == (2, 7)