

# Generated at 2024-03-18 06:37:04.085421
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:05.285515
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:07.911404
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:09.561600
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:16.695504
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:18.164924
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:19.461841
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:22.067916
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:24.251904
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:26.215497
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:37.252177
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:39.077509
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:45.421764
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:47.523887
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:37:54.134735
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:37:56.072410
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:00.139553
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    # Create an AST tree that contains a `str` type
    tree = ast.parse("x = str()")

    # Transform the tree
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)

    # Check if the tree was changed
    assert result.tree_changed == True

    # Check if the `str` was replaced with `unicode`
    assert isinstance(result.tree.body[0].value, ast.Call)
    assert result.tree.body[0].value.func.id == 'unicode'

    # Check if there are no errors
    assert result.errors == []

# Generated at 2024-03-18 06:38:02.258312
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:23.781981
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:38:36.332216
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:51.075666
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:52.708295
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:54.915869
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:38:58.344900
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    # Create an AST tree that contains a `str` type
    tree = ast.parse("x = str()")

    # Transform the tree
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)

    # Check if the tree was changed
    assert result.tree_changed == True

    # Check if the `str` was replaced with `unicode`
    new_tree_str = ast.dump(result.tree)
    assert "Name(id='unicode'" in new_tree_str

    # Check if there are no errors
    assert len(result.errors) == 0

# Generated at 2024-03-18 06:39:02.096073
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:04.254242
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:06.276192
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:11.994846
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:13.931877
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:17.126293
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    # Create an AST tree that contains a `str` type
    tree = ast.parse("x = str()")

    # Transform the tree
    transformer = StringTypesTransformer()
    result = transformer.transform(tree)

    # Check if the tree was changed
    assert result.tree_changed == True

    # Check if the `str` was replaced with `unicode`
    new_tree_str = ast.dump(result.tree)
    assert "Name(id='unicode'" in new_tree_str

    # Check if there are no errors
    assert len(result.errors) == 0

# Generated at 2024-03-18 06:39:40.916907
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:42.858937
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:50.394468
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:52.117341
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:39:58.422754
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:40:00.167675
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:40:07.641937
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:40:13.979993
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:40:15.153022
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:40:28.255043
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:09.595859
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:15.007837
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:22.996913
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:28.965339
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:30.951758
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:42.902429
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:52.475853
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:54.585814
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:41:56.295698
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:41:57.903514
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:07.062770
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:11.781993
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:43:12.987245
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:14.708872
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:23.093057
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:24.642517
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:32.539648
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:40.397212
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:43:42.472893
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:43:56.533852
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:46:20.088034
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()

# Generated at 2024-03-18 06:46:22.832236
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:46:31.906415
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:46:33.264567
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:46:35.768424
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:46:41.756710
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:46:53.700052
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()


# Generated at 2024-03-18 06:47:00.571791
# Unit test for constructor of class StringTypesTransformer
def test_StringTypesTransformer():    transformer = StringTypesTransformer()