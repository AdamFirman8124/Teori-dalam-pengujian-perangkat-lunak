

# Generated at 2022-06-12 23:07:05.196732
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict= {
        "HTTPEndpoint": "https://example.com",
        "HTTPTimeout": 60,
        "HTTPResponse": {
            "code": 200,
            "phrase": "OK"
        },
        "HTTPBody": [
            {
                "IpAddress": "10.0.0.1",
                "PortRange": "2000"
            },
            {
                "IpAddress": "10.0.0.2",
                "PortRange": "3000"
            }
        ],
        "Tags": {
            "Env": "Staging",
            "App": "ExampleApp"
        }
    }

# Generated at 2022-06-12 23:07:10.347305
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    testing_dict = {'HTTPEndpoint': {'Id': 'ep-id', 'EndpointType': 'INTERNET'}}
    expected_dict = {'http_endpoint': {'id': 'ep-id', 'endpoint_type': 'INTERNET'}}
    assert camel_dict_to_snake_dict(testing_dict) == expected_dict


# Generated at 2022-06-12 23:07:18.889180
# Unit test for function recursive_diff
def test_recursive_diff():
    assert None == recursive_diff(dict1={'a': 'a'}, dict2={'a': 'a'})
    assert({'a': 'a'}, {}) == recursive_diff(dict1={'a': 'a'}, dict2={})
    assert({'a': 'a'}, {'a': 'b'}) == recursive_diff(dict1={'a': 'a'}, dict2={'a': 'b'})
    assert({'a': 'a'}, {'b': 'c'}) == recursive_diff(dict1={'a': 'a'}, dict2={'b': 'c'})
    assert({'a': 'a'}, {'b': 'c'}) == recursive_diff(dict1={'a': 'a'}, dict2={'a': 'a', 'b': 'c'})


# Generated at 2022-06-12 23:07:29.946948
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        "type": "HTTP",
        "targets": [
            "http://example.com:9000/foo"
        ],
        "failureThreshold": {
            "value": 1,
            "unit": "percent"
        }
    }

    expected_dict = {
        "type": "HTTP",
        "targets": [
            "http://example.com:9000/foo"
        ],
        "failure_threshold": {
            "value": 1,
            "unit": "percent"
        }
    }

    camel_dict_result = camel_dict_to_snake_dict(camel_dict)

    assert camel_dict_result == expected_dict



# Generated at 2022-06-12 23:07:37.628441
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert (camel_dict_to_snake_dict({"RootVolumeSize": "200",
                                      "SecurityGroups": ["sg-1", "sg-2"],
                                      "Tags": {"TagKey": "Value"}}) ==
            {"root_volume_size": "200",
             "security_groups": ["sg-1", "sg-2"],
             "tags": {"TagKey": "Value"}
             })
    assert (camel_dict_to_snake_dict({"HTTPEndpoint": {"Enabled": False,
                                                       "URL": "https://example.com"}}) ==
            {"h_t_t_p_endpoint": {"enabled": False,
                                  "u_r_l": "https://example.com"}})

# Generated at 2022-06-12 23:07:44.707557
# Unit test for function dict_merge
def test_dict_merge():
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    c = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
    d = dict_merge(a, b)

    assert(d['first']['all_rows']['pass'] == 'dog')
    assert(d['first']['all_rows']['fail'] == 'cat')
    assert(d['first']['all_rows']['number'] == '5')

    assert(d == c)


# Generated at 2022-06-12 23:07:55.773142
# Unit test for function dict_merge
def test_dict_merge():
    a = {'x': 1,
         'y': 2,
         'z': {'t': 3,
               'u': 4,
               'v': {'m': 7,
                     'n': 8,
                     }
               }
         }
    b = {'x': 10,
         'y': 20,
         'z': {'t': 30,
               'u': 40,
               'v': {'m': 70,
                     'n': 80,
                     }
               }
         }
    c = dict_merge(a, b)

# Generated at 2022-06-12 23:08:04.278026
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({"fooBarBaz": "qux"}) == {"foo_bar_baz": "qux"}
    assert camel_dict_to_snake_dict({"FooBarBaz": "qux"}, reversible=True) == {"foo_bar_baz": "qux"}
    assert camel_dict_to_snake_dict({"fooBarBaz": {"booFarBaz": "qux"}}) == {"foo_bar_baz": {"boo_far_baz": "qux"}}

# Generated at 2022-06-12 23:08:14.818957
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'key1': {
            'some_key': [
                'some_value',
                'another_value'
            ],
            'another_camel_key': [
                {
                'and_another_camel_key': {
                    'some_list': [
                        'some_list_value'
                    ]
                }
                },
                {
                'and_another_second_camel_key': {
                    'some_list': [
                        'some_list_value'
                    ]
                }
                }
            ]
        },
        'key2': {
            'some_key': 'some_value'
        }
    }

# Generated at 2022-06-12 23:08:22.768123
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'Host': 'example.com', 'Weight': 1}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'h_t_t_p_endpoint': {'host': 'example.com', 'weight': 1}}, snake_dict
    assert camel_dict_to_snake_dict(camel_dict, reversible=True) == {'h_t_t_p_end_point': {'host': 'example.com', 'weight': 1}}, snake_dict


# Generated at 2022-06-12 23:08:35.644095
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test dictionary with various key types
    complex_dict = {
        'key1': 'value 1',
        'key2': ['value 2', 'value 3'],
        'key3': {
            'key4': 'value 4',
            'key5': ['value 5', 'value 6'],
            'key6': {
                'key7': 'value 7'
            }
        }
    }

    # Test dictionary with various key types
    expected_dict = {
        'key1': 'value 1',
        'key2': ['value 2', 'value 3'],
        'key3': {
            'key4': 'value 4',
            'key5': ['value 5', 'value 6'],
            'key6': {
                'key7': 'value 7'
            }
        }
    }

   

# Generated at 2022-06-12 23:08:45.653559
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:55.876162
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def assertEqual(dict1, dict2):
        assert camel_dict_to_snake_dict(dict1) == dict2

    assertEqual(
        {'name': 'robot', 'Age': 42, 'heightInMeters': 1.75},
        {'name': 'robot', 'age': 42, 'height_in_meters': 1.75}
    )

    assertEqual(
        {'name': 'robot', 'Age': 42, 'heightInMeters': 1.75, 'tags': {'test': 'tags'}},
        {'name': 'robot', 'age': 42, 'height_in_meters': 1.75, 'tags': {'test': 'tags'}}
    )


# Generated at 2022-06-12 23:09:02.523988
# Unit test for function recursive_diff
def test_recursive_diff():
    a = {
        'a': 'a',
        'b': {
            'c': 'c',
            'd': {
                'e': [],
                'f': 'f',
            },
        },
    }

    b = {
        'a': 'a',
        'b': {
            'c': 'c',
            'd': {
                'e': [],
                'f': 'f',
            },
        },
    }
    assert(recursive_diff(a, b) is None)

    b = {
        'b': {
            'c': 'X',
            'd': {
                'e': [],
                'f': 'f',
            },
        },
    }


# Generated at 2022-06-12 23:09:13.651633
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = dict()
    dict2 = dict()

    with pytest.raises(TypeError):
        recursive_diff(dict1, dict2)

    dict1 = dict()
    dict2 = dict(foo="bar")

    assert recursive_diff(dict1, dict2) == ({}, {'foo': 'bar'})

    dict1 = dict(foo="bar")
    dict2 = dict()

    assert recursive_diff(dict1, dict2) == ({'foo': 'bar'}, {})

    dict1 = dict(foo="bar")
    dict2 = dict(foo="bar")

    assert recursive_diff(dict1, dict2) is None

    dict1 = dict(foo="bar")
    dict2 = dict(foo="bar2")


# Generated at 2022-06-12 23:09:22.927029
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Path': '/',
            'Protocols': [
                'HTTP',
                'HTTPS'
            ],
            'VirtualClusterName': 'default'
        },
        'Description': 'An example task',
        'DefaultConcurrency': 10,
        'Name': 'Example',
        'Tags': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'TaskRoleArn': 'string'
    }


# Generated at 2022-06-12 23:09:32.583552
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {"a":1, "b": 2, "c": {"d": 3, "e": 4}}
    dict2 = {"a":1, "b": 3, "c": {"d": 3, "e": 5}}
    diff = recursive_diff(dict1, dict2)
    def equal_recursive_diff(diff, expected):
        left = diff[0]
        right = diff[1]
        left_expected = expected[0]
        right_expected = expected[1]
        if left != left_expected:
            return False
        if right != right_expected:
            return False
        return True
    assert(equal_recursive_diff(diff, [{"b": 2}, {"b": 3}]))

# Generated at 2022-06-12 23:09:43.281082
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': 'http://127.0.0.1:5000',
        'CustomCamelCase': {
            'string': 'bar',
            'int': 1,
            'bool': True,
            'null': None,
            'dict': {
                'name': 'Marty',
                'job': 'Rock star'
            },
            'list': [
                {'name': 'Marty', 'job': 'Rock star'}
            ]
        },
        'Tags': {
            'Env': 'Dev',
            'Role': 'Webfrontend'
        }
    }


# Generated at 2022-06-12 23:09:51.285868
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff(
        {'foo': {'a': 'b', 'c': 'd'}},
        {'bar': 'baz', 'foo': {'a': 'b', 'c': 'def'}}
    ) == ({'foo': {'c': 'd'}}, {'bar': 'baz', 'foo': {'c': 'def'}})

    assert recursive_diff(
        {'foo': {'a': 'b', 'c': 'd'}},
        {'foo': {'a': 'b', 'c': 'd'}}
    ) == None


# Generated at 2022-06-12 23:09:59.756432
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert _camel_to_snake('TestString') == 'test_string'
    assert _camel_to_snake('TestString', True) == 't_e_s_t_string'
    assert _camel_to_snake('TestString', False) == 'test_string'
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_ar_ns'
    assert _camel_to_snake('TargetGroupARNs', True) == 't_a_r_g_e_t_group_a_r_n_s'

    assert _snake_to_camel('test_string') == 'testString'
    assert _snake_to_camel('test_string', True) == 'TestString'

# Generated at 2022-06-12 23:10:11.726741
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Id': 123}}, reversible=True) == {'h_t_t_p_endpoint': {'id': 123}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Id': 123, 'HashKey': 'blah'}}, reversible=True) == {'h_t_t_p_endpoint': {'id': 123, 'hash_key': 'blah'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Id': 123, 'HashKey': 'blah', 'Type': 'HTTP'}}, reversible=True) == {'h_t_t_p_endpoint': {'id': 123, 'hash_key': 'blah', 'type': 'HTTP'}}

# Generated at 2022-06-12 23:10:22.225637
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': True,
        'HTTPPath': '/test_path',
        'HTTPPort': 80,
        'HTTPSEndpoint': True,
        'HTTPSPath': '/test_path',
        'HTTPSPort': 443,
        'Tags': [{'Key': 'Name', 'Value': 'some_value'}, {'Key': 'Name2', 'Value': 'some_value2'}],
        'TargetGroupARNs': ['test_arn']
    }


# Generated at 2022-06-12 23:10:30.715957
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    obj = {
        "fooBar": "testBar",
        "foo": "test",
        "fooURL": {
            "bar": "test",
            "fooBar": "testBar"
        },
        "fooEndpoint": {
            "bar": "test",
            "fooBar": "testBar"
        },
        "tags": {
            "fooBar": "testBar"
        }
    }

    # Simple test
    assert obj == snake_dict_to_camel_dict(camel_dict_to_snake_dict(obj, reversible=False))

    # Add complexity and ensure it works in reverse

# Generated at 2022-06-12 23:10:39.911841
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    _SAMPLE_CAMEL_DICT = {'TestKey': {'TestKey2': {'CamelCase': 'Value'},
                                      'camelCase': 'Value',
                                      'CamelCase': 'Value',
                                      'TestFalse': False,
                                      'TestList': [1, '2', False, {'CamelCase': 'Value'}],
                                      'TestKey3': {'TestKey4': 'Value'}}}


# Generated at 2022-06-12 23:10:47.323026
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'EndpointURL': 'string',
            'TimeoutSeconds': 0,
        },
        'Tags': {
            'Key': 'string',
            'Value': 'string'
        }
    }
    snake_dict = {'h_t_t_p_endpoint': {'endpoint_url': 'string', 'timeout_seconds': 0}, 'tags': {'Key': 'string', 'Value': 'string'}}

    assert snake_dict == camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:10:55.267528
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:02.759871
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Simple conversion
    assert camel_dict_to_snake_dict({"foo": "bar", "FooBar": "baz"}) == {"foo": "bar", "foo_bar": "baz"}

    # Copes with plurals
    assert camel_dict_to_snake_dict({"targetGroupArns": ["arn:foo:bar:baz"]}) == {
        "target_group_arns": ["arn:foo:bar:baz"]
    }

    # Copes with sub-dicts
    assert camel_dict_to_snake_dict({'container': {'containerPort': 80}}) == {
        'container': {'container_port': 80}
    }

    # Copes with multiple camel cases

# Generated at 2022-06-12 23:11:12.854298
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({u'fooBar': u'baz'}) == {u'foo_bar': u'baz'}
    assert camel_dict_to_snake_dict({u'fooBar': {u'fooBaz': u'baz'}}) == {u'foo_bar': {u'foo_baz': u'baz'}}
    assert camel_dict_to_snake_dict({u'fooBar': {u'fooBaz': {u'fooBar': u'baz'}}}) == {u'foo_bar': {u'foo_baz': {u'foo_bar': u'baz'}}}

# Generated at 2022-06-12 23:11:21.059049
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "Name": "test",
        "Tags": {
            "Name": "ansible-server"
        },
        "HTTPEndpoint": "https://test.aws.amazon.com"
    }
    expected_result = {
        "name": "test",
        "tags": {
            "Name": "ansible-server"
        },
        "h_t_t_p_endpoint": "https://test.aws.amazon.com"
    }
    assert camel_dict_to_snake_dict(test_dict, True, ("tags",)) == expected_result



# Generated at 2022-06-12 23:11:31.539975
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test to make sure the function is working for 3 different dictionaries
    """
    test_dict_one = {
        "IamTest": {
            "employee": {
                "Mark": "Thunderbird",
                "Jeff": "Lizard"
            },
            "beep": {
                "John": {
                    "test": True,
                    "beep": False
                }
            }
        },
        "requestParameters": {
            "input": "test"
        },
        "tags": {
            "Test": "test"
        },
        "myTags": ["snake", "camel"]
    }

# Generated at 2022-06-12 23:11:40.640526
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:49.088938
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'key1': 'value1',
        'key2': {
            'key3': ['value2', 'value3', 'value4'],
            'key4': {
                'Key5': 'value5'
            },
            'key6': [{
                'key7': 'value6',
                'key8': 'value7'
            }]
        }
    }


# Generated at 2022-06-12 23:11:58.926877
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:09.341636
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'key1': 1, 'key2': 2, 'NestedDict': {'nestedKey1': 1, 'nestedKey2': 2}, 'CamelKey': 'Camel', 'nestedList': [1, 2, 'string', {'nestedDict': {'nestedKey1': 1, 'nestedKey2': 2}}], 'nestedListOfLists': [[1, 2, 3, 4], 1, 2]}
    normal = camel_dict_to_snake_dict(test_dict)

# Generated at 2022-06-12 23:12:13.487852
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    with open('./tests/unit/modules/cloud/amazon/fixtures/test_camel_dict_to_snake_dict.json') as f:
        data = json.load(f)
    assert data['input_dict'] == camel_dict_to_snake_dict(data['output_dict'])



# Generated at 2022-06-12 23:12:21.391136
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def assert_converted_dict(camel_dict, snake_dict):
        assert camel_dict_to_snake_dict(camel_dict) == snake_dict


# Generated at 2022-06-12 23:12:31.973781
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}, True) == {}

# Generated at 2022-06-12 23:12:36.139193
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "One": 1,
        "Two": 2,
        "Three": {
            "Three": 3,
            "Four": 4,
            "Five": [
                5,
                {
                    "Six": 6,
                    "Seven": [
                        7,
                        {
                            "Eight": 8
                        }
                    ]
                }
            ]
        },
        "Nine": 9,
        "Ten": 10,
        "Tags": {
            "Key": "test",
            "Value": "test2"
        }
    }

# Generated at 2022-06-12 23:12:45.234305
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    data = {
        'HTTPEndpoint': {
            'URL': 'RandomString',
            'HttpMethod': 'POST',
            'RetryCount': 50
        },
        'Enabled': True
    }

    assert camel_dict_to_snake_dict(data) == {
        'http_endpoint': {
            'url': 'RandomString',
            'http_method': 'POST',
            'retry_count': 50
        },
        'enabled': True
   }


# Generated at 2022-06-12 23:12:55.337088
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "Abc": "def",
        "Def": {
            "Abc": "ghi",
            "Ghi": [
                {
                    "Abc": "jkl",
                    "Def": "mno"
                },
                "pqr"
            ]
        },
        "Tags": {
            "Key1": "value1",
            "Key2": "value2"
        }
    }

# Generated at 2022-06-12 23:13:08.471124
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'CamelCaseKey': 'value'}) == {
        'camel_case_key': 'value'
    }
    assert camel_dict_to_snake_dict({'CamelCaseKey': 1}) == {
        'camel_case_key': 1
    }
    assert camel_dict_to_snake_dict({'CamelCaseKey': 1.0}) == {
        'camel_case_key': 1.0
    }
    assert camel_dict_to_snake_dict({'camelCaseKey': 1}) == {
        'camel_case_key': 1
    }

# Generated at 2022-06-12 23:13:15.859624
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"X": ["one", "two"],
                  "Y": [{"A": "one", "B": "two"}, {"A": "three", "B": "four"}],
                  "Z": {"A": "one", "B": "two"}}

    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"x": ["one", "two"],
                          "y": [{"a": "one", "b": "two"}, {"a": "three", "b": "four"}],
                          "z": {"a": "one", "b": "two"}}



# Generated at 2022-06-12 23:13:26.171785
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(camel_dict_to_snake_dict({'TestKey': 'TestValue'}) == {'test_key': 'TestValue'})
    assert(camel_dict_to_snake_dict({'TestKey': {'TestKey': 'TestValue'}}) == {'test_key': {'test_key': 'TestValue'}})
    assert(camel_dict_to_snake_dict({'TestKey': [{'TestKey': 'TestValue'}]}) == {'test_key': [{'test_key': 'TestValue'}]})
    assert(camel_dict_to_snake_dict({'TestKey': 'TestValue'}, reversible=True) == {'test_key': 'TestValue'})

# Generated at 2022-06-12 23:13:35.756055
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'id': '12345',
        'vpcId':'v-12345',
        'name': 'vpc-1',
        'ipAddressType': 'IPV4',
        'subnets': [
            {'subnetId': 'sub-12345', 'name': 'sub-1'},
            {'subnetId': 'sub-23456', 'name': 'sub-2'},
        ]
    }

    snake_dict = camel_dict_to_snake_dict(camel_dict)

    assert snake_dict['id'] == '12345'
    assert snake_dict['vpc_id'] == 'v-12345'
    assert snake_dict['name'] == 'vpc-1'

# Generated at 2022-06-12 23:13:42.963122
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input = {
        'StatsOnly': True,
        'HTTPEndpoint': 'https://www.amazonaws.com',
        'AttachedRules': 'rule1',
        'Schedule': {
            'Rate': 'rate(5 minutes)',
            'CronExpression': '* * * * *'
        },
        'TargetGroups': [
            {
                'TargetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'
            }
        ],
        'Tags': {
            'Name': 'my-rule',
            'Env': 'test'
        }
    }
    output = camel_dict_to_snake_dict(input)

# Generated at 2022-06-12 23:13:54.325517
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_case_dict = {
        "VpcId": "vpc-123456",
        "HTTPEndpoint": "http://thejedi.net",
        "HTTPSEndpoint": "https://thejedi.net",
        "TargetGroupARNs": [
            "arn:aws:elasticloadbalancing:us-east-1:012345678912:targetgroup/paul/1234567890123456",
            "arn:aws:elasticloadbalancing:us-west-2:012345678912:targetgroup/ringo/1234567890123456",
            "arn:aws:elasticloadbalancing:us-east-1:012345678912:targetgroup/lindy/1234567890123456"
        ]
    }


# Generated at 2022-06-12 23:13:58.724306
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    import json
    test_dict = {
        'HTTPEndpoint': {
            'AcceptContentType': 'text/xml',
            'ExtraHeaders': {},
            'Url': 'http://endpoint.example.com',
            'ContentType': 'text/xml',
            'TimeoutSeconds': 1,
            'AuthScheme': 'Basic',
            'AcceptContentType': 'text/xml',
            'AuthPassword': 'mySecret',
            'AuthUserName': 'myName',
        },
    }


# Generated at 2022-06-12 23:14:06.241295
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Check that function returns a dictionary
    assert isinstance(camel_dict_to_snake_dict({}), dict)
    # Check that function converts a single letter to lower case
    assert camel_dict_to_snake_dict({"A": "a"}) == {"a": "a"}
    # Check that function converts a single word to underscore lower case
    assert camel_dict_to_snake_dict({"TestString": "test_string"}) == {"test_string": "test_string"}
    # Check that function converts a single word starting with two uppercase letters to lowercase
    assert camel_dict_to_snake_dict({"Test": "test"}) == {"test": "test"}
    # Check that function converts multi word camelCase string to underscore lower case

# Generated at 2022-06-12 23:14:16.915540
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:24.342299
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(xAxis=dict(xAxisLabel='X-Axis', yAxisLabel='Y-Axis'), yAxis=dict(xAxisLabel='X-Axis', yAxisLabel='Y-Axis'))
    camel_dict_with_list = dict(xAxis=dict(xAxisLabel='X-Axis', yAxisLabel='Y-Axis'), yAxis=dict(xAxisLabel='X-Axis', yAxisLabel='Y-Axis'), tags=[dict(Key='key', Value='value'), dict(Key='key', Value='value')])

# Generated at 2022-06-12 23:14:34.949450
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:41.693460
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = None
    assert camel_dict_to_snake_dict(camel_dict) == None
    camel_dict = dict(a=1)
    assert camel_dict_to_snake_dict(camel_dict) == dict(a=1)
    camel_dict = dict(a=1)
    assert camel_dict_to_snake_dict(camel_dict, reversible=True) == dict(a=1)
    camel_dict = dict(a=1, abC=2)
    assert camel_dict_to_snake_dict(camel_dict) == dict(a=1, ab_c=2)
    camel_dict = dict(a=1, abC=2)

# Generated at 2022-06-12 23:14:51.948155
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'MyNumber': 42, 'MyString': 'James', 'MyTuple': (1, 2, 3), 'MyList': ['a', 'b', 'c'],
                  'MyDict': {'one': 1}, 'MyDeepDict': {'MyDeepNumber': '42'}, 'MyFalseBoolean': False,
                  'MyTrueBoolean': True, 'MyNone': None}
    ids = [
        "Reversible Camel to Snake",
        "Camel to Snake",
    ]
    reversible_values = [True, False]

# Generated at 2022-06-12 23:15:02.067548
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test that camel_dict_to_snake_dict() works as expected
    """

# Generated at 2022-06-12 23:15:10.896015
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:19.188579
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz', 'HTTPEndpoint': 'foo'}) == {'http_endpoint': 'foo', 'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': {'HTTPEndpoint': 'foo'}}) == {'foo_bar': {'http_endpoint': 'foo'}}
    assert camel_dict_to_snake_dict({'fooBar': {'HTTPEndpoint': 'foo'}}, reversible=True) == {'foo_bar': {'h_t_t_p_endpoint': 'foo'}}
    assert camel_dict_to_

# Generated at 2022-06-12 23:15:29.451441
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:39.888976
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "URL": "string",
            "Authorization": {
                "type": "NONE"
            },
            "endpointType": "HTTP"
        },
        "LoadBalancer": {
            "type": "EXTERNAL",
            "internal": False
        }
    }
    assert camel_dict != snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict))
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict, True))

# Generated at 2022-06-12 23:15:47.806157
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Original test cases
    camel_dict = {'Foo': 'Bar', 'Baz': '_*&^%'}
    snake_dict = {'foo': 'Bar', 'baz': '_*&^%'}
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict
    reverse = snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict))
    assert reverse == camel_dict
    # New test cases
    camel_dict = {'Foo': 'Bar', 'Baz': '_*&^%', 'ContainerName': 'abc123'}
    snake_dict = {'foo': 'Bar', 'baz': '_*&^%', 'container_name': 'abc123'}
    assert camel_dict

# Generated at 2022-06-12 23:15:57.926622
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HelloWorld': {'Foo': 0, 'Bar': 1}}) == \
        {'hello_world': {'foo': 0, 'bar': 1}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Foo': 0, 'Bar': 1}}) == \
        {'h_t_t_p_endpoint': {'foo': 0, 'bar': 1}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Foo': 0, 'Bar': 1}}, reversible=True) == \
        {'h_t_t_p_endpoint': {'foo': 0, 'bar': 1}}

# Generated at 2022-06-12 23:16:09.270288
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Test camel_dict_to_snake_dict with a sample dictionary"""

# Generated at 2022-06-12 23:16:15.821508
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert {'a_b': 1} == camel_dict_to_snake_dict({'AB': 1})
    assert {'a_b': 1} == camel_dict_to_snake_dict({'aB': 1})
    assert {'http_endpoint': {'http_path': '/http_path'}} == camel_dict_to_snake_dict({'HTTPEndpoint': {'HTTPPath': '/http_path'}})
    assert {'http_endpoint': {'http_path': '/http_path'}} == camel_dict_to_snake_dict({'httpEndpoint': {'httpPath': '/http_path'}})

# Generated at 2022-06-12 23:16:23.326860
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:32.353060
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'fooBar': {'bazBam': {'oneThing': 1, 'twoThings': 2}}}) == {'foo_bar': {'baz_bam': {'one_thing': 1, 'two_things': 2}}}
    assert camel_dict_to_snake_dict({'fooBar': {'bazBam': {'oneThing': 1, 'twoThings': 2}}}, reversible=True) == {'foo_bar': {'baz_bam': {'one_thing': 1, 'two_things': 2}}}

# Generated at 2022-06-12 23:16:38.946134
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        'InitialFoo': 'bizz',
        'fooBar': '',
        'HTTPEndpoint': '',
        'TargetARN': None,
        'TargetGroupARNs': [],
        'NotificationMetadata': 'test',
        'NotificationTargetARN': 'test',
        'tags': {},
    }
    assert camel_dict_to_snake_dict(d) == {
        'initial_foo': 'bizz',
        'foo_bar': '',
        'http_endpoint': '',
        'target_arn': None,
        'target_group_arns': [],
        'notification_metadata': 'test',
        'notification_target_arn': 'test',
        'tags': {},
    }

    assert camel_dict_to_snake_