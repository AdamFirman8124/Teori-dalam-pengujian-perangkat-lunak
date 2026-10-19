

# Generated at 2024-03-18 01:01:39.750799
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'TopLevel': {
            'SecondLevel': {
                'ThirdLevelKey': 'value'
            },
            'AnotherSecondLevel': 'anotherValue'
        }
    }

# Generated at 2024-03-18 01:01:44.692522
# Unit test for function dict_merge
def test_dict_merge():    # Test cases for dict_merge function
    def test_simple_merge():
        a = {'x': 1, 'y': 2}
        b = {'y': 3, 'z': 4}
        expected = {'x': 1, 'y': 3, 'z': 4}
        assert dict_merge(a, b) == expected

    def test_nested_merge():
        a = {'a': {'x': 1}, 'b': 2}
        b = {'a': {'y': 3}, 'b': {'c': 4}}
        expected = {'a': {'x': 1, 'y': 3}, 'b': {'c': 4}}
        assert dict_merge(a, b) == expected

    def test_deep_merge():
        a = {'a': {'x': {'y': 1}}}

# Generated at 2024-03-18 01:01:49.511162
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_dict = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_case_dict)

    #

# Generated at 2024-03-18 01:01:54.504182
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase keys
    camel_case_dict = {'simpleTest': 'value', 'anotherOne': 123}
    expected_snake_dict = {'simple_test': 'value', 'another_one': 123}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_dict)

    # Test with nested camelCase keys
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_dict)

    # Test with reversible option

# Generated at 2024-03-18 01:01:59.052803
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCaseKey': 'innerValue'
        }
    }

# Generated at 2024-03-18 01:02:03.819749
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'TopLevel': {
            'NestedCamelCaseKey': 'nestedValue',
            'AnotherNestedKey': 'anotherNestedValue'
        },
        'AnotherTopLevelKey': 'anotherTopLevelValue'
    }
    expected_nested_snake_case_dict

# Generated at 2024-03-18 01:02:11.694535
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    def assert_diff(dict1, dict2, expected):
        diff = recursive_diff(dict1, dict2)
        assert diff == expected, f"Expected {expected}, got {diff}"

    # Test with no differences
    assert_diff({}, {}, None)
    assert_diff({'a': 1}, {'a': 1}, None)

    # Test with simple differences
    assert_diff({'a': 1}, {'a': 2}, ({'a': 1}, {'a': 2}))
    assert_diff({'a': 1}, {'b': 1}, ({'a': 1}, {'b': 1}))

    # Test with nested differences
    assert_diff({'a': {'b': 1}}, {'a': {'b': 2}}, ({'a': {'b': 1}}, {'a': {'b': 2}}))

# Generated at 2024-03-18 01:02:19.720005
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    def assert_diff(dict1, dict2, expected):
        diff = recursive_diff(dict1, dict2)
        assert diff == expected, f"Expected {expected}, got {diff}"

    # Test with simple non-nested dictionaries
    assert_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 3}, ({'b': 2}, {'b': 3}))
    assert_diff({'a': 1}, {'b': 1}, ({'a': 1}, {'b': 1}))
    assert_diff({}, {'a': 1}, ({}, {'a': 1}))
    assert_diff({'a': 1}, {}, ({'a': 1}, {}))

    # Test with nested dictionaries

# Generated at 2024-03-18 01:02:27.261670
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCase': 'innerValue'
        }
    }

# Generated at 2024-03-18 01:02:32.234135
# Unit test for function dict_merge
def test_dict_merge():    # Test cases for dict_merge function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, "Expected {} to equal {}".format(dict1, dict2)

    # Test merging with empty dictionary
    assert_dicts_equal(dict_merge({}, {'a': 1}), {'a': 1})
    assert_dicts_equal(dict_merge({'a': 1}, {}), {'a': 1})

    # Test merging with non-overlapping keys
    assert_dicts_equal(dict_merge({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})

    # Test merging with overlapping keys and different values
    assert_dicts_equal(dict_merge({'a': 1}, {'a': 2}), {'a': 2})

    # Test merging with overlapping keys and same values

# Generated at 2024-03-18 01:02:43.035537
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    def assert_diff(dict1, dict2, expected):
        diff = recursive_diff(dict1, dict2)
        assert diff == expected, f"Expected {expected}, got {diff}"

    # Test with no differences
    assert_diff({}, {}, None)
    assert_diff({'a': 1}, {'a': 1}, None)

    # Test with simple differences
    assert_diff({'a': 1}, {'a': 2}, ({'a': 1}, {'a': 2}))
    assert_diff({'a': 1}, {'b': 1}, ({'a': 1}, {'b': 1}))

    # Test with nested differences
    assert_diff({'a': {'b': 1}}, {'a': {'b': 2}}, ({'a': {'b': 1}}, {'a': {'b': 2}}))

# Generated at 2024-03-18 01:02:49.618000
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    assert recursive_diff({}, {}) is None, "Empty dictionaries should return None"
    assert recursive_diff({'a': 1}, {'a': 1}) is None, "Identical dictionaries should return None"
    assert recursive_diff({'a': 1}, {'b': 1}) == ({'a': 1}, {'b': 1}), "Different keys should be returned in the diff"
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2}), "Different values should be returned in the diff"
    assert recursive_diff({'a': {'b': 1}}, {'a': {'b': 2}}) == ({'a': {'b': 1}}, {'a': {'b': 2}}), "Differences in nested dictionaries should be returned"

# Generated at 2024-03-18 01:02:54.505462
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested dictionaries
    camel_case_dict = {'CamelCaseKey': {'NestedCamelCaseKey': 'nestedValue'}}
    expected_snake_case_dict = {'camel_case_key': {'nested_camel_case_key': 'nestedValue'}}

# Generated at 2024-03-18 01:03:00.469406
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    def assert_diff(dict1, dict2, expected):
        diff = recursive_diff(dict1, dict2)
        assert diff == expected, f"Expected {expected}, got {diff}"

    # Test with no differences
    assert_diff({}, {}, None)
    assert_diff({'key': 'value'}, {'key': 'value'}, None)

    # Test with simple differences
    assert_diff({'key1': 'value1'}, {'key2': 'value2'}, ({'key1': 'value1'}, {'key2': 'value2'}))
    assert_diff({'key': 'value1'}, {'key': 'value2'}, ({'key': 'value1'}, {'key': 'value2'}))

    # Test with nested differences

# Generated at 2024-03-18 01:03:05.662348
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase keys
    camel_case_dict = {'simpleTest': 1, 'anotherOne': 2}
    expected_snake_dict = {'simple_test': 1, 'another_one': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_dict)

    # Test with nested camelCase keys
    nested_camel_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_dict), expected_nested_snake_dict)

    # Test with reversible option

# Generated at 2024-03-18 01:03:11.146883
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    def assert_diff(dict1, dict2, expected):
        diff = recursive_diff(dict1, dict2)
        assert diff == expected, f"Expected {expected}, got {diff}"

    # Test with no differences
    assert_diff({}, {}, None)
    assert_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 2}, None)

    # Test with simple differences
    assert_diff({'a': 1}, {'a': 2}, ({'a': 1}, {'a': 2}))
    assert_diff({'a': 1}, {'b': 1}, ({'a': 1}, {'b': 1}))

    # Test with nested dictionaries

# Generated at 2024-03-18 01:03:21.775653
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    test_data = {
        'SimpleCase': 'value',
        'CamelCaseKey': 'camelValue',
        'NestedCamelCase': {
            'InnerCamelCase': 'innerValue',
            'AnotherInnerCamel': 'anotherValue'
        },
        'ListWithCamelCase': [
            'listValue1',
            {'ListInnerCamel': 'listInnerValue'}
        ],
        'IgnoreThis': {
            'DoNotChange': 'staySame'
        }
    }


# Generated at 2024-03-18 01:03:28.524898
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    test_data = {
        'SimpleCase': 'value',
        'CamelCaseKey': 'camelValue',
        'nestedCamelCase': {
            'innerCamelCase': 'innerValue',
            'AnotherInnerCamel': 'anotherValue'
        },
        'ListWithCamel': [
            'listValue1',
            {'listCamelCaseKey': 'listCamelValue'}
        ],
        'ignoreThis': {
            'DoNotChange': 'stayAsIs'
        }
    }


# Generated at 2024-03-18 01:03:33.687802
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'ParentKey': {
            'ChildKey': 'childValue',
            'AnotherChild': {
                'GrandChildKey': 'grandChildValue'
            }
        }
    }

# Generated at 2024-03-18 01:03:40.359880
# Unit test for function recursive_diff
def test_recursive_diff():    # Test cases for recursive_diff function
    assert recursive_diff({}, {}) is None, "Empty dictionaries should return None"
    assert recursive_diff({'a': 1}, {'a': 1}) is None, "Identical dictionaries should return None"
    assert recursive_diff({'a': 1}, {'b': 1}) == ({'a': 1}, {'b': 1}), "Different keys should be returned in the diff"
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2}), "Different values should be returned in the diff"
    assert recursive_diff({'a': {'b': 1}}, {'a': {'b': 2}}) == ({'a': {'b': 1}}, {'a': {'b': 2}}), "Differences in nested dictionaries should be returned"

# Generated at 2024-03-18 01:03:53.127580
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_dict = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_case_dict)

    #

# Generated at 2024-03-18 01:03:57.767528
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_dict = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_case_dict)

    #

# Generated at 2024-03-18 01:04:04.046455
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'TopLevel': {
            'NestedCamelCaseKey': 'nestedValue',
            'AnotherNestedKey': 'anotherNestedValue'
        },
        'AnotherTopLevelKey': 'topLevelValue'
    }

# Generated at 2024-03-18 01:04:08.968946
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:04:13.909951
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test case 1: simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test case 2: nested camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': {'NestedCamelCaseKey': 'nestedValue'}}
    expected_snake_case_dict = {'camel_case_key': {'nested_camel_case_key': 'nestedValue'}}

# Generated at 2024-03-18 01:04:20.964300
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    test_data = {
        'SimpleCase': 'value',
        'ComplexCaseValue': {
            'NestedCamelCase': 'nestedValue',
            'AnotherNestedCase': {
                'DeeplyNestedCase': 'deepValue'
            }
        },
        'ListCase': [
            'simpleListValue',
            {'ListDictCase': 'listDictValue'}
        ],
        'IgnoreThis': {
            'DoNotChange': 'stayAsIs'
        }
    }


# Generated at 2024-03-18 01:04:26.910786
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:04:32.881804
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherCamelCaseKey': 'value2'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_camel_case_key': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_nested_input = {
        'CamelCaseKey': {'NestedCamelCaseKey': 'nestedValue'},
        'AnotherKey': 'value'
    }

# Generated at 2024-03-18 01:04:37.578252
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_output = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test reversible conversion
    reversible_input = {'HTTPResponseCode': 200, 'URLPath': '/test'}
    expected_reversible_output = {'h_t_t_p_response_code': 200, 'u_r_l_path': '/test'}
    assert_dicts_equal(camel_dict_to_snake_dict(reversible_input, reversible=True), expected_reversible_output)

    # Test

# Generated at 2024-03-18 01:04:42.538223
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 1, 'anotherOne': 2}
    expected_snake_case_output = {'simple_test': 1, 'another_one': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    # Test reversible conversion


# Generated at 2024-03-18 01:04:54.048375
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:04:58.992067
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase keys
    camel_case_dict = {'simpleTest': 'value', 'anotherKey': 123}
    expected_snake_dict = {'simple_test': 'value', 'another_key': 123}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_dict)

    # Test with nested camelCase keys
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_dict)

    # Test with reversible option

# Generated at 2024-03-18 01:05:05.923972
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherCamelCaseKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_camel_case_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_nested_input = {
        'CamelCaseKey': {'NestedCamelCaseKey': 'nestedValue'},
        'AnotherKey': 'value'
    }

# Generated at 2024-03-18 01:05:10.552394
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:05:15.349106
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {
        'outerKey': {
            'innerKey': 'value',
            'anotherInner': {'deepKey': 'deepValue'}
        },
        'simpleKey': 'simpleValue'
    }

# Generated at 2024-03-18 01:05:19.840743
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCase': 'innerValue'
        }
    }

# Generated at 2024-03-18 01:05:24.904645
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCase': 'innerValue'
        }
    }

# Generated at 2024-03-18 01:05:29.617416
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase keys
    camel_case_dict = {'simpleTest': 1, 'anotherOne': 2}
    expected_snake_dict = {'simple_test': 1, 'another_one': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_dict)

    # Test with nested camelCase keys
    nested_camel_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_dict), expected_nested_snake_dict)

    # Test with reversible option

# Generated at 2024-03-18 01:05:34.801193
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:05:39.855410
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    test_data = {
        'SimpleCase': 'value',
        'CamelCaseKey': 'camelValue',
        'nestedCamelCase': {
            'innerCamelCase': 'innerValue',
            'AnotherInnerCamel': 'anotherValue'
        },
        'ListWithCamelCase': [
            'listValue1',
            {'listCamelCaseKey': 'listValue2'}
        ],
        'HTTPEndpoint': 'endpointValue'
    }


# Generated at 2024-03-18 01:06:06.424729
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():import unittest


# Generated at 2024-03-18 01:06:11.032976
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'NestedCamelCaseKey': 'nestedValue'
        }
    }

# Generated at 2024-03-18 01:06:16.222345
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:06:21.262984
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {
        'outerKey': {
            'innerKey': 'value',
            'anotherInner': {'deepKey': 'deepValue'}
        }
    }

# Generated at 2024-03-18 01:06:27.842671
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:06:33.399357
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_output = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_nested_input = {'outerKey': {'innerKey': 'value', 'anotherKey': 3}}
    expected_snake_case_nested_output = {'outer_key': {'inner_key': 'value', 'another_key': 3}}

# Generated at 2024-03-18 01:06:41.206816
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test case 1: simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_dict = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test case 2: reversible conversion
    reversible_camel_case_dict = {'HTTPResponseCode': 200, 'URLPath': '/test'}
    expected_reversible_snake_case_dict = {'h_t_t_p_response_code': 200, 'u_r_l_path': '/test'}

# Generated at 2024-03-18 01:06:46.429195
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'ParentKey': {
            'NestedCamelCaseKey': 'nestedValue',
            'AnotherNestedKey': 'anotherNestedValue'
        },
        'SimpleKey': 'simpleValue'
    }

# Generated at 2024-03-18 01:06:51.155378
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'TopLevel': {
            'SecondLevel': {
                'ThirdLevelKey': 'value'
            },
            'AnotherSecondLevel': 'anotherValue'
        }
    }

# Generated at 2024-03-18 01:06:51.888379
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():import unittest


# Generated at 2024-03-18 01:07:12.174563
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_dict = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested dictionaries
    nested_camel_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_dict), expected_nested_snake_dict)

    # Test with reversible option
    reversible_camel

# Generated at 2024-03-18 01:07:17.656609
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_output = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with reversible option

# Generated at 2024-03-18 01:07:23.850482
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:07:29.610122
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:07:36.137321
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:07:43.086682
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:07:48.247825
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:07:48.878419
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():import unittest


# Generated at 2024-03-18 01:07:53.943870
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase keys
    camel_case_dict = {'simpleTest': 1, 'anotherOne': 2}
    expected_snake_dict = {'simple_test': 1, 'another_one': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_dict)

    # Test with nested camelCase keys
    nested_camel_case_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_dict), expected_nested_snake_dict)

    # Test with reversible option

# Generated at 2024-03-18 01:08:01.109255
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:08:49.983810
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_dict = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested dictionaries
    nested_camel_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_dict), expected_nested_snake_dict)

    # Test with reversible option
    reversible_camel

# Generated at 2024-03-18 01:08:54.961307
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test nested camelCase to snake_case conversion
    nested_camel_case_input = {
        'outerKey': {
            'innerKey': 'value',
            'anotherInner': {
                'deepKey': 'deepValue'
            }
        }
    }

# Generated at 2024-03-18 01:08:59.531495
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCaseKey': 'innerValue',
            'AnotherInnerKey': 'anotherInnerValue'
        }
    }

# Generated at 2024-03-18 01:09:07.772034
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_dict = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested dictionaries
    nested_camel_dict = {
        'outerKey': {
            'innerKey': 'value',
            'anotherInnerKey': 3
        },
        'secondOuterKey': 'outerValue'
    }

# Generated at 2024-03-18 01:09:13.601273
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_dict = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested dictionaries
    nested_camel_dict = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_dict = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_dict), expected_nested_snake_dict)

    # Test with reversible option
    reversible_camel

# Generated at 2024-03-18 01:09:18.857152
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherCamelCaseKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_camel_case_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    camel_case_nested_input = {
        'CamelCaseKey': {'NestedCamelCaseKey': 'nestedValue'},
        'AnotherCamelCaseKey': [{'ListCamelCaseKey': 'listValue'}]
    }

# Generated at 2024-03-18 01:09:24.102101
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {
        'outerKey': {
            'innerKey': 'value',
            'anotherInner': {
                'deepKey': 'deepValue'
            }
        }
    }

# Generated at 2024-03-18 01:09:29.679161
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_dict = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_dict = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_dict), expected_snake_case_dict)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_dict = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'NestedCamelCaseKey': 'nestedValue'
        }
    }

# Generated at 2024-03-18 01:09:36.097877
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    test_data = {
        'SimpleCase': 'value',
        'ComplexCaseValue': {
            'NestedCamelCase': 'nestedValue',
            'AnotherNestedCase': {
                'DeepCase': 'deepValue'
            }
        },
        'ListCase': [
            'listItem',
            {'ListDictCase': 'listDictValue'}
        ],
        'IgnoreThis': {
            'DoNotChange': 'stayAsIs'
        }
    }


# Generated at 2024-03-18 01:09:42.574628
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 'value', 'anotherOne': 'value2'}
    expected_snake_case_output = {'simple_test': 'value', 'another_one': 'value2'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested camelCase to snake_case conversion
    nested_camel_case_input = {'outerKey': {'innerKey': 'value'}}
    expected_nested_snake_case_output = {'outer_key': {'inner_key': 'value'}}
    assert_dicts_equal(camel_dict_to_snake_dict(nested_camel_case_input), expected_nested_snake_case_output)

    #

# Generated at 2024-03-18 01:11:11.547598
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'CamelCaseKey': 'value', 'AnotherKey': 'anotherValue'}
    expected_snake_case_output = {'camel_case_key': 'value', 'another_key': 'anotherValue'}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {
        'CamelCaseKey': 'value',
        'NestedDict': {
            'InnerCamelCase': 'innerValue'
        }
    }

# Generated at 2024-03-18 01:11:17.097663
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def assert_dicts_equal(dict1, dict2):
        assert dict1 == dict2, f"Expected {dict1} to equal {dict2}"

    # Test with simple camelCase to snake_case conversion
    camel_case_input = {'simpleTest': 1, 'moreComplexExample': 2}
    expected_snake_case_output = {'simple_test': 1, 'more_complex_example': 2}
    assert_dicts_equal(camel_dict_to_snake_dict(camel_case_input), expected_snake_case_output)

    # Test with nested dictionaries
    camel_case_input = {'outerKey': {'innerKey': 'value', 'anotherKey': 3}}
    expected_snake_case_output = {'outer_key': {'inner_key': 'value', 'another_key': 3}}

# Generated at 2024-03-18 01:11:21.596654
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():    # Test cases for camel_dict_to_snake_dict function
    def test_single_level():
        camel_case = {'CamelCaseKey': 'value', 'AnotherKey': 'another_value'}
        expected_snake_case = {'camel_case_key': 'value', 'another_key': 'another_value'}
        assert camel_dict_to_snake_dict(camel_case) == expected_snake_case

    def test_nested_dict():
        camel_case = {'CamelCaseKey': {'NestedKey': 'nested_value'}}
        expected_snake_case = {'camel_case_key': {'nested_key': 'nested_value'}}
        assert camel_dict_to_snake_dict(camel_case) == expected_snake_case

    def test_list_of_dicts():
        camel_case = {'ListOfDicts': [{'CamelKeyOne': 'value1'}, {'CamelKeyTwo': 'value2'}]}