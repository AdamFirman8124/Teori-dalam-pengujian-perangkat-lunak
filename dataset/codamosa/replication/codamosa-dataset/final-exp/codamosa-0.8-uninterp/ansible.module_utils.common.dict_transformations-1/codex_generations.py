

# Generated at 2022-06-12 23:06:52.119894
# Unit test for function recursive_diff
def test_recursive_diff():
    test1 = {
        "key1": "value1",
        "key2": "value2",
        "dict": {
            "key1": "value1",
            "key2": "value2",
            }
        }

    test2 = {
        "key1": "value1",
        "key2": "value2",
        "dict": {
            "key1": "value2",
            "key2": "value2",
            }
        }

    test3 = {
        "key1": "value1",
        "key2": "value2",
        "dict": {
            "key1": "value1",
            "key2": "value2",
            }
        }


# Generated at 2022-06-12 23:07:03.039947
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge({}, {}) == {}
    assert dict_merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert dict_merge({"a": {"b": 1}}, {"a": {"b": 2}}) == {"a": {"b": 2}}
    assert dict_merge({"a": {"b": 1}}, {"a": {"c": 2}}) == {"a": {"b": 1, "c": 2}}
    assert dict_merge({"a": {"b": 1}}, {"a": {"b": 2, "c": 3}}) == {"a": {"b": 2, "c": 3}}
    # test "in-place"
    a = {"b": 1}
    b = {"a": a}
    c = {"a": a}
   

# Generated at 2022-06-12 23:07:13.259401
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'HTTPEndpoint': 'https://foo:8080', 'HTTPRetries': 5, 'tags': {'Tag': {'Key': 'Value'}},
                 'tags_map': [{'Key': 'Key1', 'Value': 'Value1'}, {'Key': 'Key2', 'Value': 'Value2'}],
                 'TargetGroupARNs': ['foo', 'bar']}

# Generated at 2022-06-12 23:07:20.140230
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'TestString': 'myString',
        'TestNumber': 123,
        'TestBoolean': True,
        'TestList': [1,2,3],
        'TestObject': {
            'TestString': 'myString',
            'TestNumber': 123,
            'TestBoolean': True,
            'TestList': [1,2,3],
            'TestObject': {
                'TestString': 'myString',
                'TestNumber': 123,
                'TestBoolean': True,
                'TestList': [1,2,3]
            }
        }
    }

# Generated at 2022-06-12 23:07:31.393144
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(dict(fooBar=1)) == dict(foo_bar=1)
    assert camel_dict_to_snake_dict(dict(fooBar=1), reversible=True) == dict(foo_bar=1)
    assert camel_dict_to_snake_dict(dict(fooBarBaz=1), reversible=True) == dict(foo_bar_baz=1)
    assert camel_dict_to_snake_dict(dict(HTTPEndpoint=1), reversible=True) == dict(h_t_t_p_endpoint=1)
    assert camel_dict_to_snake_dict(dict(HTTPEndpoint=1), reversible=False) == dict(http_endpoint=1)


# Generated at 2022-06-12 23:07:39.021354
# Unit test for function recursive_diff
def test_recursive_diff():
    """ Unit tests for function recursive_diff """

    dict1 = {'key1': {'a': 1, 'b': 2, 'c': 3},
             'key2': 2,
             'key3': 3}

    # Test for positive case
    dict2 = {'key1': {'a': 1, 'b': 2, 'c': 4},
             'key2': 3,
             'key3': 3}

    assert recursive_diff(dict1, dict2) == ({'key1': {'c': 3}}, {'key1': {'c': 4}, 'key2': 3})

    # Test for negative case where no change
    dict2 = {'key1': {'a': 1, 'b': 2, 'c': 3},
             'key2': 2,
             'key3': 3}


# Generated at 2022-06-12 23:07:49.665560
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test that a dictionary is correctly converted to snake case.
    result = camel_dict_to_snake_dict({'camelCase': 'foo', 'camelCamelCase': 'bar', 'CapitalCamelCase': 'baz',
                                       '1NumberFirst': 'boo', 'EndsWithANumber2': 'boo', 'Abbreviation': 'boo',
                                       'AbbreviationFooBar': 'boo', 'Abbreviation1': 'boo', 'a': 'b',
                                       'HTTPEndpoint': 'foo'})

# Generated at 2022-06-12 23:08:00.036198
# Unit test for function recursive_diff
def test_recursive_diff():
    """ Unit test for recursive_diff
    """

    # Test results for correct input

# Generated at 2022-06-12 23:08:10.665134
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Testcase 1: simple test with string value
    item = {'A': 'a', 'B': 'b', 'C': 'c'}
    output = {'a': 'a', 'b': 'b', 'c': 'c'}
    assert camel_dict_to_snake_dict(item) == output

    # Testcase 2: simple test with list value
    item = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': ['g', 'h', 'i']}
    output = {'a': ['a', 'b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['g', 'h', 'i']}
    assert camel_dict_to_snake_dict(item) == output

    # Test

# Generated at 2022-06-12 23:08:21.228727
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:08:29.689177
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Id': 1}}) == {'http_endpoint': {'id': 1}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Id': 1}}, reversible=True) == {'h_t_t_p_endpoint': {'id': 1}}



# Generated at 2022-06-12 23:08:37.748198
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:48.032222
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'firstName': 'John', 'lastName': 'Smith', 'isAlive': True,
                  'age': 27, 'address': {'streetAddress': '21 2nd Street',
                                         'city': 'New York',
                                         'state': 'NY',
                                         'postalCode': '10021-3100'},
                  'phoneNumbers': [{'type': 'home', 'number': '212 555-1234'},
                                   {'type': 'office', 'number': '646 555-4567'},
                                   {'type': 'mobile', 'number': '123 456-7890'}],
                  'children': [],
                  'spouse': None}


# Generated at 2022-06-12 23:08:55.962717
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'fooBar': {
            'Baz': 'qux',
            'quxQux': {
                'fred': 'wilma'
            }
        },
        'dino': None
    }
    expected_dict = {
        'foo_bar': {
            'baz': 'qux',
            'qux_qux': {
                'fred': 'wilma'
            }
        },
        'dino': None
    }
    assert camel_dict_to_snake_dict(test_dict) == expected_dict



# Generated at 2022-06-12 23:09:05.208523
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:16.133329
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = { 'Key1' : 'value', 'Key2' : 'value', 'Key3' : { 'Key3_1' : 'value', 'Key3_2' : 'value', 'Key3_3' : { 'Key3_3_1' : 'value', 'Key3_3_2' : 'value' }, 'Key3_4' : 'value' }, 'Key4' : 'value', 'Key5' : [ 'value', 'value' ], 'Key6' : 'value' }

# Generated at 2022-06-12 23:09:24.346615
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from ansible.module_utils.ec2 import camel_dict_to_snake_dict
    from .ec2 import EC2Inventory
    ec2 = EC2Inventory(session=None, subnets=None, regions=None)

    #ec2.get_resources_from_boto3(list_all_resources,
    #                             list_all_resource_method,
    #                             get_one_resource_method,
    #                             region,
    #                             tag_list_apps,
    #                             tag_list_env,
    #                             tag_list_role,
    #                             tag_list_name,
    #                             tag_list_component,
    #                             instance_filters,
    #                             boto3_conn,
    #                             resource=None)

    resource

# Generated at 2022-06-12 23:09:34.194436
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'HTTPFullUrl': 'https://test.test.test',
                                   'HTTPStatusCode': 200,
                                   'CustomUserData': 'CBD3A4FD-8380-4C4A-89C7-0A8FAD077F97',
                                   'Tags': {
                                        'foo': 'bar',
                                        'Baz': 'qux'
                                    }
                                   }}

    result = camel_dict_to_snake_dict(camel_dict, reversible=False)

    assert result['h_t_t_p_endpoint']['h_t_t_p_full_url'] == 'https://test.test.test'

# Generated at 2022-06-12 23:09:44.766856
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "foo": "bar",
        "BarBaz": {"fooBarBaz": [{"bazFooBar": "bazFooBar"}]},
        "fizzBuzz": [
            {"fooBar": "fooBar"},
            {"testFooBar": "testFooBar"}
        ]
    }

    expected_dict = {
        "foo": "bar",
        "bar_baz": {"foo_bar_baz": [{"baz_foo_bar": "bazFooBar"}]},
        "fizz_buzz": [
            {"foo_bar": "fooBar"},
            {"test_foo_bar": "testFooBar"}
        ]
    }

    result_dict = camel_dict_to_snake_dict(camel_dict)
    assert result

# Generated at 2022-06-12 23:09:51.640750
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Protocols': ['HTTP', 'HTTPS'],
            'Authorization': {
                'AuthorizationType': 'NONE'
            },
            'TimeoutInMillis': 5000,
            'Tags': {
                'Tags': [
                    {
                        'Key': 'tagKey1',
                        'Value': 'tagValue1'
                    },
                    {
                        'Key': 'tagKey2',
                        'Value': 'tagValue2'
                    }
                ]
            }
        }
    }

# Generated at 2022-06-12 23:10:02.276247
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:11.920884
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test with simple values
    camel_dict = {"FirstKey": 1}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"first_key": 1}
    camel_dict = {"FirstKey": "test"}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"first_key": "test"}

    # Test with a list of simple values
    camel_dict = {"Keys": ["FirstKey", "SecondKey"]}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"keys": ["FirstKey", "SecondKey"]}

    # Test a nested list of simple values

# Generated at 2022-06-12 23:10:22.564019
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Converts camelized dict to snake case dict
    sample_camel_dict = {'KeyName': 'mykey', 'SecurityGroups': ['mysecgroup'], 'Tags': [{'Key': 'Name', 'Value': 'Test'}]}
    sample_snake_dict = {'key_name': 'mykey', 'security_groups': ['mysecgroup'], 'tags': [{'Key': 'Name', 'Value': 'Test'}]}
    assert sample_snake_dict == camel_dict_to_snake_dict(sample_camel_dict)

    # Converts :reversible camelized dict (e.g. HTTPEndpoint -> h_t_t_p_endpoint) to snake case dict
    sample_reversible_camel_dict = {'HTTPEndpoint': 'httpendpoint'}
    sample_

# Generated at 2022-06-12 23:10:30.978426
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:40.026947
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:50.066803
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Testing convert camel dict to snake dict

    We are simply checking the conversion is correct. The extra complexity is
    to ensure that dictionaries and lists of different types are handled correctly.

    With the possible exception of tags, we do not expect to see lists in the results.
    If a list did get converted, it is likely to contain a dictionary and would error
    in the recursive call.
    """

    dictionary_of_lists = {
        "GroupId": "1",
        "Tags": [
            {
                "Value": "1",
                "Key": "1"
            },
            {
                "Value": "2",
                "Key": "2"
            }
        ]
    }


# Generated at 2022-06-12 23:10:53.754890
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'TestKey': 'TestValue'}) == {'test_key': 'TestValue'}
    assert camel_dict_to_snake_dict({'TestKey': {'TestKey2': 'TestValue2'}}) == {'test_key': {'test_key2': 'TestValue2'}}



# Generated at 2022-06-12 23:11:02.015605
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        'Arbitrary': 1,
        'CamelCase': {'Arbitrary': 2},
        'HTTPMethod': 'GET',
        'HTTPEndpoint': 'https://www.ansible.com',
        'HTTPEndpointReversible': 'https://www.ansible.com',
        'EmailAddresses': [
            'john@example.com',
            'jane@example.com'
        ],
        'IPv4Addresses': [
            '127.0.0.1',
            '192.0.2.1'
        ],
        'IPv6Addresses': [
            '::1',
            '::ffff:192.0.2.128'
        ],
        'Tags': {
            'Key': 'Value',
        },
    }

    expected

# Generated at 2022-06-12 23:11:12.156845
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        'SubnetIds': [
            'subnet-1234567899',
            'subnet-1234567898',
            'subnet-1234567897'
        ],
        'SecurityGroups': [
            'sg-12345678',
            'sg-12345677'
        ],
        'Tags': {
            'Name': 'TestAppVPC',
            'Environment': 'Development'
        },
        'VpcId': 'vpc-12345678'
    }


# Generated at 2022-06-12 23:11:22.705586
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "Substring": "string",
        "Maximum": "number",
        "Minimum": "number",
        "Pattern": "regex",
        "Tags": dict(
            (str(x), str(x * 2))
            for x in range(10)
        )
    }

    camel_dict_copy = deepcopy(camel_dict)
    camel_dict['Tags']['TestTag'] = "test"

    snake_dict = camel_dict_to_snake_dict(camel_dict)
    reversed_snake_dict = camel_dict_to_snake_dict(camel_dict_copy, reversible=True)
    camel_dict = snake_dict_to_camel_dict(snake_dict)
    reversed_camel_dict = snake_dict_to_c

# Generated at 2022-06-12 23:11:34.909454
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict1 = {
        'HTTPEndpoint': 'http://localhost/',
        'Metrics': {'Include': '_ALL_'},
        'Name': 'MyDatabase',
        'Port': 1234,
        'SQL': 'SELECT 1;',
        'Status': 'AVAILABLE'
    }
    output_dict1 = {
        'http_endpoint': 'http://localhost/',
        'metrics': {'include': '_ALL_'},
        'name': 'MyDatabase',
        'port': 1234,
        'sql': 'SELECT 1;',
        'status': 'AVAILABLE'
    }

    assert camel_dict_to_snake_dict(input_dict1) == output_dict1


# Generated at 2022-06-12 23:11:42.677006
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    class_name = "camel_dict_to_snake_dict"
    camel_dict = {
        "foo": "bar",
        "baz": {
            "fooBar": "test",
            "value": {
                "fooBar": "test",
                "barBaz": "test",
                "fooBaz": "test"
            }
        }
    }

    expected = {
        "foo": "bar",
        "baz": {
            "foo_bar": "test",
            "value": {
                "foo_bar": "test",
                "bar_baz": "test",
                "foo_baz": "test"
            }
        }
    }
    result = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:11:49.483857
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "DBClusterIdentifier": "test-cluster",
        "SkipFinalSnapshot": "false",
        "Tags": {
            "TestTag1": "Value1",
            "TestTag2": "Value2"
        },
        "DBClusterParameterGroupName": "default.aurora5.6",
        "DeletionProtection": "false",
        "Port": 3306,
        "DBInstanceClass": "db.t2.micro",
        "StorageEncrypted": "false"
    }


# Generated at 2022-06-12 23:11:57.946483
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'Url': 'https://example.com',
                                   'Protocol': 'HTTPS'},
                  'Tags': {'test-key': 'test-value'}}
    snake_dict = {'h_t_t_p_endpoint': {'url': 'https://example.com',
                                       'protocol': 'HTTPS'},
                  'tags': {'test-key': 'test-value'}}
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict


# Generated at 2022-06-12 23:12:08.020846
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'IAMRole': 'FAKE_ROLE',
        'FirstProperty': 'value1',
        'SecondProperty': 'value2',
        'Nested': {
            'Dictionary': {
                'NestedAgain': 'value3',
                'FirstList': [
                    {
                        'SecondList': [
                            'value4',
                            'value5'
                        ]
                    },
                    'value6'
                ]
            }
        }
    }

# Generated at 2022-06-12 23:12:17.011231
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"HTTPEndpoint": {"Enabled": True, "HttpPath": "http://example.com", "TimeoutSeconds": 10}}
    snake_dict = {"h_t_t_p_endpoint": {"enabled": True, "http_path": "http://example.com", "timeout_seconds": 10}}
    assert snake_dict == camel_dict_to_snake_dict(camel_dict)
    snake_dict = {"http_endpoint": {"enabled": True, "http_path": "http://example.com", "timeout_seconds": 10}}
    assert snake_dict == camel_dict_to_snake_dict(camel_dict, reversible=False)
    camel_dict = {'A': {'A': {'B': 2}}, 'B': 1}

# Generated at 2022-06-12 23:12:24.772865
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {
        'HTTPEndpoint': {
            'HTTPSettings': [
                {
                    'AuthenticationMethod': 'NONE',
                    'Id': 'HTTPSettings_1',
                    'Name': 'HTTPSetting_1',
                    'Protocols': ['HTTP', 'HTTPS'],
                    'Timeout': 10
                }
            ],
            'Id': 'HTTPEndpoint_1',
            'Name': 'HTTPEndpoint_1',
        }
    }

# Generated at 2022-06-12 23:12:35.937805
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Assertions on standard case
    camel_dict = {'Description': 'My test database', 'SourceDBInstanceIdentifier': 'second-db', 'TargetDBInstanceIdentifier': 'first-db'}
    assert camel_dict_to_snake_dict(camel_dict) == {'description': 'My test database', 'source_d_b_instance_identifier': 'second-db', 'target_d_b_instance_identifier': 'first-db'}

    # Assertions on complex case, ie with sub-dicts
    camel_dict = {'Description': 'My test database', 'SourceDBInstanceIdentifier': 'second-db', 'Tags': [{'Key': 'foo', 'Value': 'bar'}]}

# Generated at 2022-06-12 23:12:45.048937
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'IamInstanceProfile': {
            'Arn': 'foo',
            'Name': 'bar'
        },
        'Tags': [
            {'Key': 'a', 'Value': 'b'},
            {'Key': 'c', 'Value': 'd'}
        ]
    }

    actual_snake_dict = camel_dict_to_snake_dict(camel_dict)
    expected_snake_dict = {
        'iam_instance_profile': {
            'arn': 'foo',
            'name': 'bar'
        },
        'tags': [
            {'key': 'a', 'value': 'b'},
            {'key': 'c', 'value': 'd'}
        ]
    }

    assert actual_snake_dict == expected_

# Generated at 2022-06-12 23:12:55.168074
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test the case where key is not an acronym
    source_dict = {'fooBar': 'baz'}
    result = camel_dict_to_snake_dict(source_dict)
    assert(result == {'foo_bar': 'baz'})

    # Test the case where key is an acronym
    source_dict = {'httpEndpoint': 'baz'}
    result = camel_dict_to_snake_dict(source_dict)
    assert(result == {'http_endpoint': 'baz'})

    # Test the case where the key is already in snake_case
    source_dict = {'http_endpoint': 'baz'}
    result = camel_dict_to_snake_dict(source_dict)
    assert(result == {'http_endpoint': 'baz'})



# Generated at 2022-06-12 23:13:11.161469
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    camel_dict = {'fooBar': 'baz', 'fooBaz' : {'fooQux': 'quux'}, 'Thing': 'otherThing'}
    snake_dict = snake_dict_to_camel_dict(camel_dict)
    camel_dict = {'foo_bar': 'baz', 'foo_baz' : {'foo_qux': 'quux'}, 'thing': 'otherThing'}
    assert snake_dict == camel_dict


# Generated at 2022-06-12 23:13:19.078036
# Unit test for function dict_merge
def test_dict_merge():
    d1 = {'foo': 'bar', 'fie': 'baz'}
    d2 = {'fie': 'buz'}
    expected = {'foo': 'bar', 'fie': 'buz'}
    actual = dict_merge(d1, d2)
    assert actual == expected

    d1 = {'foo': 'bar', 'fie': {'one': '1'}}
    d2 = {'fie': {'two': '2', 'three': '3'}}
    expected = {'foo': 'bar', 'fie': {'one': '1', 'two': '2', 'three': '3'}}
    actual = dict_merge(d1, d2)
    assert actual == expected


# Generated at 2022-06-12 23:13:28.225740
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    snake_dict = {'instance_id': 'i-1234567890abcdef0', 'tags': {'item': {
        'key': 'Name', 'value': 'foobar'}, 'item2': {'key': 'Foo', 'value': 'Bar'}}}
    camel_dict = snake_dict_to_camel_dict(snake_dict)
    assert camel_dict == {'InstanceId': 'i-1234567890abcdef0', 'Tags': {'item': {
        'key': 'Name', 'value': 'foobar'}, 'item2': {'key': 'Foo', 'value': 'Bar'}}}



# Generated at 2022-06-12 23:13:35.703432
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    tests = [
        # input dict, expected result
        (
            {'foo_bar': {'bazBar': 1}},
            {'fooBar': {'bazBar': 1}},
        ),
        (
            {'no_change': 'value', 'alsoNoChange': 'value'},
            {'noChange': 'value', 'alsoNoChange': 'value'},
        )
    ]
    for index, test in enumerate(tests):
        input_dict = test[0]
        expected_result = test[1]
        output = snake_dict_to_camel_dict(input_dict)

# Generated at 2022-06-12 23:13:42.937713
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    snake_dict = {
        "HTTPEndpoint": {
            "enabled": True,
            "keep_alive": {
                "max_connections": 200,
                "idle_timeout_seconds": 30
            }
        },
        "https_endpoint": {
            "enabled": True,
            "keep_alive": {
                "max_connections": 200,
                "idle_timeout_seconds": 30
            }
        },
        "http_endpoint": {
            "enabled": True,
            "keep_alive": {
                "max_connections": 200,
                "idle_timeout_seconds": 30
            }
        }
    }

# Generated at 2022-06-12 23:13:54.325737
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'camelCase': 'abcd',
        'camelABCD': {
            'camelAbCd': 'efgh',
            'camelABCDEfgh': [
                'camelAbCdEfGh',
                'camelAbCdEfGhIjKlMn'
            ]
        },
        'HTTPEndpoint': {
            'httpEndpoint': {
                'httpEndpointList': [
                    'httpEndpoint1',
                    'httpEndpoint2'
                ]
            }
        }
    }


# Generated at 2022-06-12 23:14:02.641646
# Unit test for function recursive_diff
def test_recursive_diff():
    left1 = {'port': 80}
    right1 = {'port': 8080}
    left2 = {'port': 80}
    right2 = {'port': 80, 'server': {'name': 'foo'}}
    left3 = {'port': 80, 'server': {'name': 'foo'}}
    right3 = {'port': 80, 'server': {'name': 'bar'}}
    left4 = {'port': 80, 'server': {'name': 'foo'}}
    right4 = {'port': 80, 'server': {'name': 'foo'}}
    assert recursive_diff(left1, right1) == ({'port': 80}, {'port': 8080})
    assert recursive_diff(left2, right2) == None

# Generated at 2022-06-12 23:14:12.188567
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "Key1": "value1",
        "Key2": {
            "Key3": "value3",
            "Key4": "value4",
            "Key5": "value5"
        },
        "Key6": [
            {
                "Key7": "value7",
                "Key8": "value8",
                "Key9": "value9"
            }
        ]
    }


# Generated at 2022-06-12 23:14:21.991297
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:29.194880
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    original_dict = {"my_favorite_key": "original value", "my_favorite_list": [{"my_favorite_dict": {"another_key": "another_value"}}]}

    new_dict = snake_dict_to_camel_dict(original_dict)

    assert new_dict["myFavoriteKey"] == "original value"
    assert new_dict["myFavoriteList"][0]["myFavoriteDict"]["anotherKey"] == "another_value"

# Generated at 2022-06-12 23:14:45.663965
# Unit test for function recursive_diff
def test_recursive_diff():
    base_dict = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    assert recursive_diff(base_dict, base_dict) is None
    assert recursive_diff(base_dict, {}) == ({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}, {})
    assert recursive_diff({}, base_dict) == ({}, {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    assert recursive_diff(base_dict, {'a': 1, 'b': {'x': 2, 'y': 5}, 'c': 4}) == \
        ({'b': {'y': 3}}, {'b': {'y': 5}})

# Generated at 2022-06-12 23:14:55.813077
# Unit test for function dict_merge
def test_dict_merge():
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    c = { 'second' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    d = a
    d['first'].update(b['first'])
    assert dict_merge(a,b) == d
    assert dict_merge(b,a) == d
    e = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }

# Generated at 2022-06-12 23:15:04.836710
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    test_dict = {'some_key_name': {
                    'other_key': {
                        'another_key': 'value',
                        'list': [1, 2, 3]
                    },
                    'simple_key': 'a simple string'
                }
            }

    test_dict_camelized = {'someKeyName': {
                               'otherKey': {
                                   'anotherKey': 'value',
                                   'list': [1, 2, 3]
                               },
                               'simpleKey': 'a simple string'
                        }
                    }

    camelized_dict = snake_dict_to_camel_dict(test_dict)
    # Camelized dict should equal expected dict
    assert camelized_dict == test_dict_camelized



# Generated at 2022-06-12 23:15:12.800338
# Unit test for function recursive_diff
def test_recursive_diff():
    # Simple test
    a = {'a': 'a'}
    b = {'b': 'b'}
    result = recursive_diff(a, b)
    assert result == ({'a': 'a'}, {'b': 'b'}), "recursive_diff returned '%s' but should have returned '%s'." \
                                                % (result, ({'a': 'a'}, {'b': 'b'}))

    # Nested test
    a = {'a': {'b': 'b'}}
    b = {'a': {'c': 'c'}}
    result = recursive_diff(a, b)

# Generated at 2022-06-12 23:15:20.722916
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # simple test
    test_A = {
        'TestA': 'a'
    }
    test_A_expected = {
        'test_a': 'a'
    }
    assert(camel_dict_to_snake_dict(test_A) == test_A_expected)

    # recursive dictionaries
    test_B = {
        'TestB1': 'b1',
        'TestB2': {
            'TestC': 'c'
        }
    }
    test_B_expected = {
        'test_b1': 'b1',
        'test_b2': {
            'test_c': 'c'
        }
    }
    assert(camel_dict_to_snake_dict(test_B) == test_B_expected)

    # lists
    test

# Generated at 2022-06-12 23:15:31.662523
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    d = {"a": "A", "b": "B"}
    assert snake_dict_to_camel_dict(d) == {"a": "A", "b": "B"}
    assert snake_dict_to_camel_dict(d, True) == {"A": "A", "B": "B"}

    d = {"a": {"a": "A", "b": "B", "c": {"a": "A", "b": ["A", "B"], "c": "C", "d": "D"}}}
    assert snake_dict_to_camel_dict(d) == {"a": {"a": "A", "b": "B", "c": {"a": "A", "b": ["A", "B"], "c": "C", "d": "D"}}}
    assert snake_dict_to_camel

# Generated at 2022-06-12 23:15:35.819007
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:45.057554
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    from ansible_collections.amazon.aws.plugins.module_utils.core import camel_dict_to_snake_dict, snake_dict_to_camel_dict, camel_dict_to_snake_dict
    from ansible.module_utils.six import assertRegex


# Generated at 2022-06-12 23:15:54.757114
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Simple snake_case to camelCase
    camel_dict = {'h_t_t_p_endpoint': {'h_t_t_p_endpoint_scheme': 'HTTPS'}}
    snake_dict = {'http_endpoint': {'http_endpoint_scheme': 'HTTPS'}}
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

    # Simple camelCase to snake_case
    camel_dict = {'httpEndpoint': {'httpEndpointScheme': 'HTTPS'}}
    snake_dict = {'http_endpoint': {'http_endpoint_scheme': 'HTTPS'}}
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

    # Reversible conversion

# Generated at 2022-06-12 23:16:03.966007
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    assert snake_dict_to_camel_dict({'key_name': 'value1', 'keyName': 'value2'}) == {'keyName': 'value2', 'key_name': 'value1'}
    assert snake_dict_to_camel_dict({'key_name': {'value_name': 'value1'}}) == {'keyName': {'valueName': 'value1'}}
    assert snake_dict_to_camel_dict({'Key_Name': {'value_name': 'value1'}}) == {'KeyName': {'valueName': 'value1'}}
    assert snake_dict_to_camel_dict({'key_name': {'value_name': ['value1']}}) == {'keyName': {'valueName': ['value1']}}
    assert snake_dict_