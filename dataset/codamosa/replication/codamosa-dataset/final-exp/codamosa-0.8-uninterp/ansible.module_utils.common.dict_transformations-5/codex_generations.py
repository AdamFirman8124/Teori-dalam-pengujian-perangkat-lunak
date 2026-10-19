

# Generated at 2022-06-12 23:06:58.387680
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test recursive_diff

    :returns: Nothing
    :raises: AssertionError if there is a bug
    """

    # None raised if no difference
    assert(recursive_diff({}, {}) is None)

    assert(recursive_diff({'a': 1}, {'a': 1}) is None)
    assert(recursive_diff({'a': {'b': 2}}, {'a': {'b': 2}}) is None)

    # Difference
    assert(recursive_diff({}, {'a': 1}) == ({}, {'a': 1}))
    assert(recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2}))

# Generated at 2022-06-12 23:07:05.264030
# Unit test for function dict_merge
def test_dict_merge():
    # This has to be imported here so that it doesn't get run twice if
    # test_dict_merge is run from the CLI
    from ansible.module_utils.common.dict_transformations import recursive_diff
    # List of checks to perform [firstdict, seconddict, resultdict]

# Generated at 2022-06-12 23:07:15.387436
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        "foo": {
            "bar": {
                "keyOne": 1,
                "keyTwo": 2
            },
            "baz": {
                "keyThree": 3,
                "keyFour": 4
            },
            "list": [
                { "keyFive": 5 },
                { "keySix": 6 }
            ]
        }
    }

    snake_dict = {
        "foo": {
            "bar": {
                "key_one": 1,
                "key_two": 2
            },
            "baz": {
                "key_three": 3,
                "key_four": 4
            },
            "list": [
                { "key_five": 5 },
                { "key_six": 6 }
            ]
        }
    }

    assert snake

# Generated at 2022-06-12 23:07:24.412953
# Unit test for function recursive_diff
def test_recursive_diff():
    from ansible.module_utils.common._collections_compat import Mapping

    assert recursive_diff({}, {}) is None
    assert recursive_diff({"a": 1}, {}) == ({'a': 1},)
    assert recursive_diff({}, {"a": 1}) == ({'a': 1},)
    assert recursive_diff({"a": 1}, {"a": 1}) is None
    assert recursive_diff({"a": 1}, {"a": 2}) == ({'a': 1}, {'a': 2})
    assert recursive_diff({"a": 1}, {"b": 2}) == ({'a': 1}, {'b': 2})
    assert recursive_diff({"a": 1}, {"a": 1, "b": 2}) == (None, {'b': 2})

# Generated at 2022-06-12 23:07:34.950075
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict_camel = {
        "HTTPEndpoint":
            {"HTTPEndpointConfiguration": {
                "Retain": True,
                "URL": "url"
            }
             },
        "CPUUsage": {
            "CpuOptions": {
                "PerCpu": "1",
                "Shared": "2"
            }
        },
        "plop": [
            {
                "HTTPEndpointConfiguration": {
                    "Retain": True,
                    "URL": "url"
                }
            },
            {
                "HTTPEndpointConfiguration": {
                    "Retain": True,
                    "URL": "url"
                }
            }
        ]
    }


# Generated at 2022-06-12 23:07:40.769577
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'first': 'one'}
    dict2 = {'first': 'one'}
    assert recursive_diff(dict1, dict2) is None

    dict3 = {'first': 'one', 'second': 'two'}
    dict4 = {'first': 'one'}
    result1 = recursive_diff(dict3, dict4)
    assert isinstance(result1, tuple)
    assert 'second' in result1[0]
    assert 'second' not in result1[1]

    dict5 = {'first': 'one'}
    dict6 = {'first': 'one', 'second': 'two'}
    result2 = recursive_diff(dict5, dict6)
    assert isinstance(result2, tuple)
    assert 'second' not in result2[0]

# Generated at 2022-06-12 23:07:52.048112
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:01.858593
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_input = {
        "property1": "TestString1",
        "property2": "TestString2",
        "testList": [
            {
                "testCamelDict": {
                    "CamelProperty1": "CamelTestString1",
                    "CamelProperty2": "CamelTestString2"
                }
            },
            {
                "testCamelDict": {
                    "CamelProperty1": "CamelTestString1",
                    "CamelProperty2": "CamelTestString2"
                }
            }
        ],
        "httpEndpoint": {
            "property3": "TestString3",
            "property4": "TestString4"
        },
        "Tags": {
            "Key": "Value"
        }
    }


# Generated at 2022-06-12 23:08:12.401838
# Unit test for function dict_merge
def test_dict_merge():

    # Test simple, single level Dictionary merge
    a = {'red': 1, 'blue': 1, 'green': 2}
    b = {'red': 2, 'black': 1, 'yellow': 2}
    c = {'magenta': 3, 'cyan': 4, 'yellow': 5}

    d = dict_merge(a, b)
    assert d == {'red': 2, 'blue': 1, 'green': 2, 'black': 1, 'yellow': 2}

    # Test multi level merge
    d = dict_merge(a, c)
    assert d == {'red': 1, 'blue': 1, 'green': 2, 'magenta': 3, 'cyan': 4, 'yellow': 5}

    # Test multi level merge, with nested dictionary in one of the top level keys

# Generated at 2022-06-12 23:08:18.239343
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = camel_dict_to_snake_dict({'snakeIsReal': True,
                                      'HTTPEndpoint': True})
    assert camel == {'snake_is_real': True,
                     'http_endpoint': True}
    camel = camel_dict_to_snake_dict({'HTTPEndpoint': True}, True)
    assert camel == {'h_t_t_p_endpoint': True}


# Generated at 2022-06-12 23:08:32.553779
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test basic conversion
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}

    # Test conversion of long string
    long_string = 'HTTPVersion'
    assert camel_dict_to_snake_dict({long_string: 'baz'}) == {'http_version': 'baz'}

    # Test conversion of nested dictionary
    assert camel_dict_to_snake_dict({'fooBar': {'baz': 'qux', 'fizz': 'buzz'}}) == {'foo_bar': {'baz': 'qux', 'fizz': 'buzz'}}

    # Test conversion of a list of strings as a value

# Generated at 2022-06-12 23:08:37.802055
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:48.067195
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'camel': 'test'}) == {'camel': 'test'}
    assert camel_dict_to_snake_dict({'Camel': 'test'}) == {'camel': 'test'}
    assert camel_dict_to_snake_dict({'CamelCase': 'test'}) == {'camel_case': 'test'}
    assert camel_dict_to_snake_dict({'CamelCase': 'test', 'camel': 'test'}) == {'camel_case': 'test', 'camel': 'test'}
    assert camel_dict_to_snake_dict({'CamelCaseHTTP': 'test'}) == {'camel_case_http': 'test'}

# Generated at 2022-06-12 23:08:57.922215
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    sourceDict = {}
    assert camel_dict_to_snake_dict(sourceDict) == sourceDict, "Test of empty dict failed"

    sourceDict = {'HTTPEndpoint': {'port': 80, 'host': 'example.com', 'attributes': {'color': 'red', 'shape': 'square', 'tags': {'color': 'blue', 'shape': 'round'}}}}
    expectedDict = {'h_t_t_p_endpoint': {'port': 80, 'host': 'example.com', 'attributes': {'color': 'red', 'shape': 'square', 'tags': {'color': 'blue', 'shape': 'round'}}}}
    assert camel_dict_to_snake_dict(sourceDict) == expectedDict, "Test of complex dict failed"

    sourceD

# Generated at 2022-06-12 23:09:03.881965
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {'a': {'b': {'c': 3, 'd': 4}}}
    d2 = {'a': {'b': {'c': 5, 'e': 6}}}
    res = recursive_diff(d1, d2)
    assert res is not None
    assert res[0] == {'a': {'b': {'c': {}}}}
    assert res[1] == {'a': {'b': {'c': {}, 'e': 6}}}

# Generated at 2022-06-12 23:09:14.848547
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test simple conversion case
    original = {'testKey1': 'testValue1', 'testKey2': 'testValue2', 'test_key3': 'test_value3'}
    expected = {'test_key1': 'testValue1', 'test_key2': 'testValue2', 'test_key3': 'test_value3'}
    result = camel_dict_to_snake_dict(original)
    assert result == expected

    # Test nested dicts
    original = {'testKey1': 'testValue1', 'testKey2': {'testKey3': 'testValue3', 'testKey4': 'testValue4'},
                'test_key5': 'test_value5'}

# Generated at 2022-06-12 23:09:22.927812
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict = { "fooBar": "foobar", "BazQux": { "fooBar": "foobar" }, "Tags" : { "Key" : "value" } }
    assert camel_dict_to_snake_dict(dict) == { "foo_bar": "foobar", "baz_qux" : { "foo_bar": "foobar" }, "tags" : { "Key" : "value" } }
    assert camel_dict_to_snake_dict(dict, True) == { "foo_bar": "foobar", "baz_q_ux" : { "foo_bar": "foobar" }, "tags" : { "Key" : "value" } }



# Generated at 2022-06-12 23:09:32.539380
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def test_same_dict(dict1, dict2):
        assert all(item[0] == item[1] for item in zip(dict1, dict2))

    # Create a camelized dictionary
    gimme_dromedary = {
        'DromedaryCase': {'DromedaryCase': 'foo'},
        'camelCase': True,
        'CamelCase': {
            'DromedaryCase': 'foo'
        },
        'CamelCaseDromedaryCase': ['foo', 'bar'],
        'CamelCaseCamelCase': ['foo', 'bar'],
    }

    # Create snake dictionary

# Generated at 2022-06-12 23:09:43.232297
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'keyA': 'value_a',
        'keyB': ['value_b_1', 'value_b_2'],
        'keyC': [{
            'keyC1': 'value_c_1',
            'tags': {
                'tagA': 'tag_a',
                'tagB': {
                    'tagB1': 'tag_b1',
                    'tagB2': 'tag_b2'
                }
            }
        }],
        'keyD': [{
            'keyD1': 'value_d_1',
        }, {
            'keyD1': 'value_d_2',
        }]
    }

# Generated at 2022-06-12 23:09:51.255170
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:02.585163
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "Tags": [{
            "Key": "something"
        }],
        "HTTPEndpoint": {
            "Enabled": True
        },
        "HttpsEndpoint": {
            "Enabled": False
        },
        "A_B_C": "somevalue",
        "D_E_F": "somevalue2"
    }
    # Ensure that camel_dict_to_snake_dict is returning a dictionary and not a list
    assert isinstance(camel_dict_to_snake_dict(camel_dict), dict)
    # Ensure that camel_dict_to_snake_dict preserves the 'Tags' key by not converting it to snake case
    assert 'Tags' in camel_dict_to_snake_dict(camel_dict)
    assert camel_dict_to_

# Generated at 2022-06-12 23:10:12.223568
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:23.015388
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_input = {
        "Name": "camel-dict-to-snake-dict-test",
        "Tags": {"Name": "camel-dict-to-snake-dict-test"},
        "TargetGroupARNs": [
            "arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/camel-dict-to-snake-dict-test/1234567890123456"
        ],
        "HTTPEndpoint": "http://example.com/",
        "EnableHTTPCompression": True
    }


# Generated at 2022-06-12 23:10:27.451199
# Unit test for function dict_merge
def test_dict_merge():
    a = {'a': 1, 'b': 2, 'c': {'c1': 12, 'c2': 22}}
    b = {'b': 3, 'c': {'c1': 13}}
    assert dict_merge(a, b) == {'a': 1, 'b': 3, 'c': {'c1': 13, 'c2': 22}}



# Generated at 2022-06-12 23:10:37.229937
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'SomeName': 'value'}) == {'some_name': 'value'}
    assert camel_dict_to_snake_dict({'SomeName': 'value', 'SomeOtherName': 'other_value'}) == \
           {'some_name': 'value', 'some_other_name': 'other_value'}
    assert camel_dict_to_snake_dict({'SomeName': 'value', 'someOtherName': 'other_value'}) == \
           {'some_name': 'value', 'some_other_name': 'other_value'}

# Generated at 2022-06-12 23:10:46.530138
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "Name": "ansible-test-role-lambda",
        "Version": "$LATEST",
        "Code": {
            "ZipFile": "def main(event, context): print('Hello from Lambda!')"
        },
        "Runtime": "python3.6",
        "Handler": "index.main",
        "Publish": True,
        "Tags": {
            "Name": "test-role-lambda"
        }
    }


# Generated at 2022-06-12 23:10:52.578572
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'OneThing': {'OtherThing': {'OtherOtherThing': 'Hello'},
                              'OneMoreThing': 'End'},
                 'Name': 'John'}
    expected_dict = {'one_thing': {'other_thing': {'other_other_thing': 'Hello'},
                                   'one_more_thing': 'End'},
                     'name': 'John'}
    assert camel_dict_to_snake_dict(test_dict) == expected_dict



# Generated at 2022-06-12 23:11:00.947394
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:11.210614
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test case #1: Simple case.
    camel_dict = {
        'HTTPEndpoint': {
            'first_name': 'John',
            'last_name': 'Doe',
        }
    }
    expected_output = {
        'h_t_t_p_endpoint': {
            'first_name': 'John',
            'last_name': 'Doe',
        }
    }
    assert camel_dict_to_snake_dict(camel_dict) == expected_output

    # Test case #2: List of dicts.

# Generated at 2022-06-12 23:11:21.138096
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test 1
    test_dict = {'HTTPEndpoint': 'http.example.com',
                 'Tags': {'httpEndpoint': 'http.example.com'}}

    expected_dict = {'h_t_t_p_endpoint': 'http.example.com',
                     'tags': {'httpEndpoint': 'http.example.com'}}

    result_dict = camel_dict_to_snake_dict(test_dict)

    assert result_dict == expected_dict

    # Test 2
    test_dict = {'HTTPEndpoint': 'http.example.com',
                 'Tags': {'httpEndpoint': 'http.example.com', 'App': 'app1'}}


# Generated at 2022-06-12 23:11:32.748264
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test dictionary
    d = {
        "TargetGroupArns": ["arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067"],
        "LoadBalancerNames": ["my-load-balancer"]
    }

    result = camel_dict_to_snake_dict(d)
    expected = {
        "target_group_arns": ["arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067"],
        "load_balancer_names": ["my-load-balancer"]
    }
    assert expected == result



# Generated at 2022-06-12 23:11:41.550176
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {"ResponseMetadata": {"RequestId": "2cca5d5a-0f38-47c0-a51a-b6a8ee01c1c9"},
                  "MarkedAsDefault": False,
                  "Tags": {
                      "mytag": "tagvalue",
                      "myTag": "tagvalue2"
                  },
                  "Container": {
                      "Docker": {
                          "Image": "602401143452.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest",
                          "Args": ["sh", "-c", "echo success"],
                      }
                  }}
    transformed_dict = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:11:48.453258
# Unit test for function recursive_diff
def test_recursive_diff():
    """
    Unit tests for the function recursive_diff
    """
    complex1 = {'a': {'b': {'c': 1}, 'd': 2}}
    complex1_same = {'a': {'d': 2, 'b': {'c': 1}}}
    complex_diff = {'a': {'d': 3, 'b': {'c': 1}, 'e': {'f': 4}}}

    assert recursive_diff(complex1, complex1_same) is None
    result = recursive_diff(complex1, complex_diff)
    assert result is not None
    assert result[0] == {'a': {'d': 2}}
    assert result[1] == {'a': {'d': 3, 'e': {'f': 4}}}

# Generated at 2022-06-12 23:11:58.241996
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'Key': 'value',
        'Key2': ['something', 'else'],
        'Key3': {
            'SomeKey': 'value2',
            'OtherKey': 'value3',
        }
    }
    dict2 = {
        'Key': 'value',
        'Key2': ['something', 'else'],
        'Key3': {
            'SomeKey': 'value2',
            'OtherKey': 'value3',
            'AnotherKey': 'value4',
        }
    }

# Generated at 2022-06-12 23:12:08.424217
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'HTTPEndpoint': True}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'http_endpoint': True}

    camel_dict = {'HTTPEndpoint': True, 'AbcDef': 23, 'AbcDefXyz': 'HelloWorld'}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'http_endpoint': True, 'abc_def': 23, 'abc_def_xyz': 'HelloWorld'}

    camel_dict = {'HTTPEndpoint': True, 'AbcDef': 23, 'AbcDefXyz': 'HelloWorld', 'list': ['value1', 'value2']}
    snake_dict = camel_dict_to_sn

# Generated at 2022-06-12 23:12:17.214061
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    original_camel_dict = {
        'ListServices': ['name1', 'name2'],
        'foo': {
            'bar': {
                'Tags': {}
            },
            'ListTagsForResource': [{'foo': 'bar'}]
        }
    }

    expected_snake_dict = {
        'list_services': ['name1', 'name2'],
        'foo': {
            'bar': {
                'Tags': {}
            },
            'list_tags_for_resource': [{'foo': 'bar'}]
        }
    }

    result = camel_dict_to_snake_dict(original_camel_dict)

    assert(expected_snake_dict == result)


# Generated at 2022-06-12 23:12:25.066011
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'InstanceIds': ['i-0123456789abcdef0', 'i-0123456789abcdef1']}) == {
        'instance_ids': ['i-0123456789abcdef0', 'i-0123456789abcdef1']}

    assert camel_dict_to_snake_dict({'InstanceIds': ['i-0123456789abcdef0', 'i-0123456789abcdef1'], 'Foo': 'bar'}) == {
        'instance_ids': ['i-0123456789abcdef0', 'i-0123456789abcdef1'], 'foo': 'bar'}


# Generated at 2022-06-12 23:12:35.790613
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {
        'ListPartitions': ["p1", "p2"],
        'PartitionName': 'p3',
        'Tags': {
            'Key': 'k1',
            'Value': 'v1',
            'Tags': ['t1', 't2']
        }
    }
    output = camel_dict_to_snake_dict(input_dict, ignore_list=('Tags',))
    assert output == {
        'list_partitions': ["p1", "p2"],
        'partition_name': 'p3',
        'tags': {
            'Key': 'k1',
            'Value': 'v1',
            'Tags': ['t1', 't2']
        }
    }



# Generated at 2022-06-12 23:12:44.939270
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:55.063593
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:08.975343
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit tests for recursive_diff()"""
    import pytest

    with pytest.raises(TypeError) as excinfo:
        recursive_diff(['a', 'b'], ['c', 'd'])
    assert "Both must be a dictionary" in str(excinfo)

    with pytest.raises(TypeError) as excinfo:
        recursive_diff({'a': 'b', 'c': 'd'}, ['e', 'f'])
    assert "Both must be a dictionary" in str(excinfo)

    assert recursive_diff({}, {}) is None

    assert recursive_diff({'a': 'b'}, {}) == ({'a': 'b'}, {})

    assert recursive_diff({}, {'a': 'b'}) == ({}, {'a': 'b'})


# Generated at 2022-06-12 23:13:17.791525
# Unit test for function recursive_diff
def test_recursive_diff():
    import pytest

    # Indirect tests for these
    # ----------------------------
    # single value
    assert recursive_diff({'a': 1}, {}) == ({'a': 1}, {})
    assert recursive_diff({}, {'a': 1}) == ({}, {'a': 1})
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2})

    # simple dictionaries
    assert recursive_diff({'a': 1, 'b': {}},
                          {'a': 1, 'b': {'a': 1}}) == ({'b': {}}, {'b': {'a': 1}})

# Generated at 2022-06-12 23:13:28.679886
# Unit test for function recursive_diff
def test_recursive_diff():
    def assert_dict_equal(d1, d2):
        import json
        assert(json.dumps(d1, sort_keys=True) == json.dumps(d2, sort_keys=True))

    assert_dict_equal(recursive_diff({}, {}), None)

    assert_dict_equal(recursive_diff({}, {'a': 1}), (None, {'a': 1}))
    assert_dict_equal(recursive_diff({'a': 1}, {}), ({'a': 1}, None))

    assert_dict_equal(recursive_diff({'a': 1}, {'a': 2}), ({'a': 1}, {'a': 2}))

# Generated at 2022-06-12 23:13:34.853211
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        {
            'helloWorld': {
                'innerHelloWorld': 'World'
            },
            'tagKey': 'tagvalue',
            'Tags': {
                'tagKey': 'tagValue',
                'something': 'else'
            }
        }, ignore_list=['Tags']
    ) == {
        'hello_world': {
            'inner_hello_world': 'World'
        },
        'tag_key': 'tagvalue',
        'Tags': {
            'tagKey': 'tagValue',
            'something': 'else'
             }
    }


# Generated at 2022-06-12 23:13:40.935742
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'AmazonResourceName': 'arn'}) == {'amazon_resource_name': 'arn'}
    assert camel_dict_to_snake_dict({'AmazonResourceName': {'AmazonResourceName': 'arn'}}) == {'amazon_resource_name': {'amazon_resource_name': 'arn'}}
    assert camel_dict_to_snake_dict({'AmazonResourceNameList': [{'AmazonResourceName': 'arn'}]}) == {'amazon_resource_name_list': [{'amazon_resource_name': 'arn'}]}


# Generated at 2022-06-12 23:13:53.408324
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test cases for recursive_diff"""

    # Test different type
    try:
        recursive_diff("a string object", "another string object")
    except TypeError as e:
        assert True
    else:
        assert False

    # Test empty list (The difference is empty set, which cannot represent by a JSON object)
    assert recursive_diff({}, {}) == None

    # Test same object
    assert recursive_diff({'a':'a', 'b':'b'}, {'a':'a', 'b':'b'}) == None

    # Test top level key
    ret = recursive_diff({'a':'a', 'b':'b'}, {'a':'a'})
    assert ret == ({'b':'b'}, None)

    # Test list

# Generated at 2022-06-12 23:13:58.158708
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:05.126381
# Unit test for function recursive_diff
def test_recursive_diff():
    import pytest

    def create_dict1():
        return {
            'namespace': 'unitest',
            'metadata': {
                'name': 'test_name',
                'labels': {
                    'project': 'unitest'
                }
            },
            'spec': {
                'template': {
                    'metadata': {
                        'labels': {
                            'project': 'unitest'
                        }
                    },
                    'spec': {
                        'containers': [{
                            'name': 'nginx',
                            'image': 'nginx:latest'
                        }]
                    }
                }
            }
        }


# Generated at 2022-06-12 23:14:15.729347
# Unit test for function recursive_diff
def test_recursive_diff():
    """Checks that recursive_diff works as expected"""
    assert recursive_diff({}, {}) == None
    assert recursive_diff({'a': 'a'}, {'a': 'a'}) == None
    assert recursive_diff({'a': 'a'}, {'a': 'b'}) == ({'a': 'a'}, {'a': 'b'})
    assert recursive_diff({'a': 'a'}, {'b': 'a'}) == ({'a': 'a'}, {'b': 'a'})
    assert recursive_diff({'a': {'b': {'c': 'c'}}}, {'a': {'b': {'c': 'c'}}}) == None

# Generated at 2022-06-12 23:14:23.694662
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict1 = {
        'KeyName': 'foobar',
        'ImageId': 'ami-2001',
        'SecurityGroups': ['sg-1', 'sg-2'],
        'HTTPEndpoint': {
            'Enabled': False,
            'HTTPPort': 80,
            'HTTPSPort': 443,
        },
        'Tags': {
            'Name': 'foobar',
            'Env': 'test',
        },
        'S3BucketName': 'my-bucket',
    }

# Generated at 2022-06-12 23:14:35.633438
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'CreateDefault': True}) == {'create_default': True}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': None}) == {'h_t_t_p_endpoint': None}
    assert camel_dict_to_snake_dict({'EnableHTTPEndpoint': True}) == {'enable_h_t_t_p_endpoint': True}
    assert camel_dict_to_snake_dict({'AmazonResourceName': 'arn:example:foo'}) == {'amazon_resource_name': 'arn:example:foo'}
    assert camel_dict_to_snake_dict({'KeyARN': 'arn:example:key'}) == {'key_arn': 'arn:example:key'}
    assert camel_dict_to

# Generated at 2022-06-12 23:14:44.219812
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:54.347423
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    class TestClass(object):

        def __init__(self):
            pass

    test_case_1 = TestClass()
    test_case_1.input = {'Foo': 'bar'}
    test_case_1.expected_output = {'foo': 'bar'}

    test_case_2 = TestClass()
    test_case_2.input = {'Foo': 'bar', 'HTTPServices': [], 'Tags': {'Key': 'Value'}}
    test_case_2.expected_output = {'foo': 'bar', 'h_t_t_p_services': [], 'tags': {'Key': 'Value'}}

    test_case_3 = TestClass()
    test_case_3.input = {'Tags': {'Key': 'Value'}}
    test_case_

# Generated at 2022-06-12 23:15:04.040722
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test single dictionaries recursively.
    assert None == recursive_diff({}, {})
    assert recursive_diff({'foo': 'bar'}, {}) == ({'foo': 'bar'}, {})
    assert recursive_diff({}, {'foo': 'bar'}) == ({}, {'foo': 'bar'})
    assert recursive_diff({'foo': 'bar'}, {'foo': 'bar'}) == None
    assert recursive_diff({'foo': 'bar'}, {'foo': 'baz'}) == ({'foo': 'bar'}, {'foo': 'baz'})
    assert recursive_diff({'foo': {'bar': 'baz'}}, {'foo': {'bar': 'baz'}}) == None

# Generated at 2022-06-12 23:15:12.249937
# Unit test for function recursive_diff
def test_recursive_diff():
    base = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key4': 'value4',
            'key5': 'value5'
        }
    }
    test1 = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key4': 'value4',
            'key5': 'value5'
        }
    }
    test2 = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key4': 'value4',
            'key5': 'value55'
        }
    }

# Generated at 2022-06-12 23:15:20.332031
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert _camel_to_snake('RefreshToken') == 'refresh_token'
    assert _camel_to_snake('RefreshToken', True) == 'r_e_f_r_e_s_h_t_o_k_e_n'
    assert _camel_to_snake('HTTPEndpoint') == 'http_endpoint'
    assert _camel_to_snake('HTTPEndpoint', True) == 'h_t_t_p_endpoint'
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_arns'
    assert _camel_to_snake('TargetGroupARNs', True) == 'target_group_a_r_ns'

# Generated at 2022-06-12 23:15:31.109165
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = { 'a': 1, 'b': 2, 'c': { 'ca': 3, 'cb': 4, 'cc': { 'cca': 5 }}}
    dict2 = { 'a': 1, 'b': 2, 'c': { 'ca': 3, 'cb': 4, 'cc': { 'cca': 6, 'ccb': 7 }}}

    result = recursive_diff(dict1, dict2)
    if result is not None:
        left = result[0]
        right = result[1]
        if left != { 'c': { 'cc': { 'cca': 5 }}} and right != { 'c': { 'cc': { 'cca': 6, 'ccb': 7 }}}:
            print("recursive_diff didn't give back the expected results when diffing two nested dictionaries.")


# Generated at 2022-06-12 23:15:41.153807
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict_to_test = {'foobar': {'FooBarBaz': 123, 'ABC': 'xyz', 'ABCXYZ': [{'aBc': 'xyz'}]},
                    'fooBar': 'test',
                    'FooBAr': [{'fooBar': 'xYz', 'BarBaz': [1, 2, 3]}, 'test', {'RDSClusterARNs': [1, 2, 3]}]}

# Generated at 2022-06-12 23:15:47.766850
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'fooBar': 'baz', 'EnableTrafficEncryption': True}) == {'foo_bar': 'baz', 'enable_traffic_encryption': True}
    assert camel_dict_to_snake_dict({'fooBar': 'baz', 'EnableTrafficEncryption': True}, reversible=True) == {'foo_bar': 'baz', 'enable_traffic_encryption': True}
    assert camel_dict_to_snake_dict({'fooBar': 'baz', 'EnableTrafficEncryption': True}, reversible=False) == {'foo_bar': 'baz', 'enable_traffic_encryption': True}

# Generated at 2022-06-12 23:15:57.831610
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:10.153479
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "helloWorld": "hi",
        "nestedCamelDict": {
            "innerCamelDict": {
                "innerKey": {
                    "innerNestedCamelDict": {
                        "innerTopNestedCamelDict": {
                            "someInnerKey": "someInnerValue"
                        }
                    }
                }
            }
        },
        "Tags": {
            "tag1": "tag1Value",
            "tag2": "tag2Value"
        },
        "someList": [
            {
                "innerKey": "innerValue"
            }
        ]
    }

# Generated at 2022-06-12 23:16:16.810222
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'Key1': 1,
        'Key2': 2,
        'Key3': 3,
        'Key4': 4,
        'HTTPKey1': 1,
        'HTTPKey2': 2,
        'HTTPKey3': 3,
    }

    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)

    assert 'key1' in snake_dict.keys()
    assert 'key2' in snake_dict.keys()
    assert 'key3' in snake_dict.keys()
    assert 'key4' in snake_dict.keys()
    assert 'h_t_t_p_k_e_y1' in snake_dict.keys()
    assert 'h_t_t_p_k_e_y2' in snake_dict

# Generated at 2022-06-12 23:16:24.665228
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'X': 'Y'}) == {'x': 'Y'}
    assert camel_dict_to_snake_dict({'X': 'Y'}, reversible=True) == {'x': 'Y'}
    assert camel_dict_to_snake_dict({'X': 'Y'}, reversible=True, ignore_list=['x']) == {'x': 'Y'}
    assert camel_dict_to_snake_dict({'X': 'Y'}, reversible=False, ignore_list=['x']) == {'h_t_t_p_endpoint': 'Y'}
    assert camel_dict_to_snake_dict({'X': 'Y'}, reversible=True, ignore_list=['X']) == {'x': 'Y'}


# Generated at 2022-06-12 23:16:33.670340
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:39.767748
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "foo": {
            "bar": {
                "baz": {
                    "HTTPEndpoint": "http://example.com",
                    "Tags": {
                        "Examples": {
                            "Env": "Test",
                        }
                    }
                }
            }
        }
    }

    expected_pairs = [
        ("foo.bar.baz.HTTPEndpoint", "http://example.com"),
        ("foo.bar.baz.tags.Examples.Env", "Test"),
    ]

    snake_dict = camel_dict_to_snake_dict(camel_dict)

    for path, expected in expected_pairs:
        value = snake_dict
        for key in path.split("."):
            value = value[key]

        assert value == expected