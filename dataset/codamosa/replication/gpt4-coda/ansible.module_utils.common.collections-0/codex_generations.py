

# Generated at 2024-03-18 01:01:26.728266
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=1, b=3)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}
    assert not (immutable_dict1 == regular_dict), "An ImmutableDict should not be equal to a regular dict"

   

# Generated at 2024-03-18 01:01:32.384237
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=1, b=3)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different ImmutableDict with different size
    immutable_dict4 = ImmutableDict(a=1, b=2, c=3)

# Generated at 2024-03-18 01:01:39.263216
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:01:46.956757
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type

# Generated at 2024-03-18 01:01:51.983020
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True, "List should be iterable"

# Generated at 2024-03-18 01:01:56.844396
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:02:01.715702
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type

# Generated at 2024-03-18 01:02:08.015524
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:02:14.274732
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict_a != different_regular_dict

# Generated at 2024-03-18 01:02:19.358726
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type

# Generated at 2024-03-18 01:02:31.700860
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:02:36.361537
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:02:41.867239
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:02:47.937555
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:02:54.620567
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:03:00.397827
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=1, b=3)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different ImmutableDict with a different number of items
    immutable_dict4 = ImmutableDict(a=1, b=2, c=3)

# Generated at 2024-03-18 01:03:05.926439
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:03:11.139922
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict1 != different

# Generated at 2024-03-18 01:03:15.869928
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself."

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal."

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=1, b=3)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal."

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}
    assert not (immutable_dict1 == regular_dict), "An ImmutableDict should not be equal to a regular dict."

   

# Generated at 2024-03-18 01:03:22.727878
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:03:42.526760
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a non-dict type
    non_dict = [1, 2]

# Generated at 2024-03-18 01:03:51.954255
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}

# Generated at 2024-03-18 01:03:57.288185
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict1, "ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}

# Generated at 2024-03-18 01:04:05.651810
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:04:12.742083
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with an equivalent regular dict
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to an equivalent regular dict"

    # Test inequality with a non-dict type
    non_dict = "{'a': 1, 'b': 2}"

# Generated at 2024-03-18 01:04:21.154510
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type

# Generated at 2024-03-18 01:04:25.789360
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict_a != different_regular_dict

# Generated at 2024-03-18 01:04:31.171464
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:04:35.785706
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:04:43.006540
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict1, "ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different ImmutableDict with different size
    immutable_dict4 = ImmutableDict({'a': 1})

# Generated at 2024-03-18 01:05:21.562052
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:05:27.922670
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:05:35.393741
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=3, b=4)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}

# Generated at 2024-03-18 01:05:40.419114
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict_a != different_regular_dict

# Generated at 2024-03-18 01:05:46.127013
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True, "List should be iterable"

# Generated at 2024-03-18 01:05:49.995435
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:05:54.883298
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert not dict1 == dict3, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type
    assert not dict1 == [1, 2], "ImmutableDict should not be equal to a list"

    # Test inequality with

# Generated at 2024-03-18 01:06:09.218870
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:06:16.277714
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:06:21.470855
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a different type

# Generated at 2024-03-18 01:07:27.825332
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict_a != different_regular_dict

# Generated at 2024-03-18 01:07:33.012798
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True, "List should be iterable"

# Generated at 2024-03-18 01:07:38.668909
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with an equivalent regular dict
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to an equivalent regular dict"

    # Test inequality with a non-dict type
    non_dict = "{'a': 1, 'b': 2}"

# Generated at 2024-03-18 01:07:43.765067
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:07:48.943065
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) == True, "List should be iterable"

# Generated at 2024-03-18 01:07:53.637114
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:08:00.558216
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:08:05.873585
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}

# Generated at 2024-03-18 01:08:13.522080
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same content
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert dict_a != dict_c, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict_a == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a regular dict with different content
    different_regular_dict = {'a': 1, 'b': 3}
    assert dict_a != different_regular_dict

# Generated at 2024-03-18 01:08:18.007136
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True, "List should be iterable"

# Generated at 2024-03-18 01:10:20.132435
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with an equivalent regular dict
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to an equivalent regular dict"

    # Test inequality with a non-dict type
    non_dict = "{'a': 1, 'b': 2}"

# Generated at 2024-03-18 01:10:25.033032
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "Two ImmutableDicts with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "Two ImmutableDicts with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a non-dict type
    non_dict = "{'a': 1, 'b': 2}"

# Generated at 2024-03-18 01:10:31.652575
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:10:37.562086
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict1, "An ImmutableDict should be equal to itself"

    # Test equality with a different ImmutableDict with the same items
    immutable_dict2 = ImmutableDict(a=1, b=2)
    assert immutable_dict1 == immutable_dict2, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict with different items
    immutable_dict3 = ImmutableDict(a=1, b=3)
    assert not (immutable_dict1 == immutable_dict3), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}
    assert not (immutable_dict1 == regular_dict), "An ImmutableDict should not be equal to a regular dict"

   

# Generated at 2024-03-18 01:10:45.050475
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:10:49.627333
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True

# Generated at 2024-03-18 01:10:57.398721
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([]) == True

# Generated at 2024-03-18 01:11:03.920460
# Unit test for function is_iterable
def test_is_iterable():    assert is_iterable([1, 2, 3]) is True, "List should be iterable"

# Generated at 2024-03-18 01:11:09.174067
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with the same ImmutableDict
    dict_a = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_a, "An ImmutableDict should be equal to itself"

    # Test equality with an identical ImmutableDict
    dict_b = ImmutableDict({'a': 1, 'b': 2})
    assert dict_a == dict_b, "Two ImmutableDicts with the same items should be equal"

    # Test inequality with a different ImmutableDict
    dict_c = ImmutableDict({'a': 1, 'b': 3})
    assert not (dict_a == dict_c), "Two ImmutableDicts with different items should not be equal"

    # Test inequality with a different type
    regular_dict = {'a': 1, 'b': 2}
    assert not (dict_a == regular_dict), "An ImmutableDict should not be equal to a regular dict"

    # Test equality with a

# Generated at 2024-03-18 01:11:14.008673
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():    # Test equality with same content
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert dict1 == dict2, "ImmutableDict instances with the same content should be equal"

    # Test inequality with different content
    dict3 = ImmutableDict({'a': 1, 'b': 3})
    assert dict1 != dict3, "ImmutableDict instances with different content should not be equal"

    # Test equality with a regular dict with the same content
    regular_dict = {'a': 1, 'b': 2}
    assert dict1 == regular_dict, "ImmutableDict should be equal to a regular dict with the same content"

    # Test inequality with a non-dict type
    non_dict = "{'a': 1, 'b': 2}"