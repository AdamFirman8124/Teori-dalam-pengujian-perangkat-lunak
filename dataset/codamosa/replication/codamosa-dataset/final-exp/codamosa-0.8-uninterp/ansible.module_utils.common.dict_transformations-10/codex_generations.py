

# Generated at 2022-06-12 23:06:49.538411
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Testing camel_dict_to_snake_dict function
    """

    camel_dict = {
        "HTTPEndpoint": {
            "Protocol": "http",
            "Endpoint": {
                "Address": "arm-insights.azure.net",
                "Port": "443"
            },
            "Authorization": "Anonymous"
        }
    }

    snake_dict = {
        "http_endpoint": {
            "protocol": "http",
            "endpoint": {
                "address": "arm-insights.azure.net",
                "port": "443"
            },
            "authorization": "Anonymous"
        }
    }

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict


# Generated at 2022-06-12 23:07:01.043499
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_test_dict = {
        "KeyName": "test-key-pair",
        "IamInstanceProfile": "global-role",
        "NetworkInterfaces": [
            {
                "AssociatePublicIpAddress": True
            },
            {
                "AssociatePublicIpAddress": True
            }
        ],
        "Tags": {
            "Name": "test_tag"
        }
    }

# Generated at 2022-06-12 23:07:07.149959
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': {
                '1': {
                    '2': 2,
                    '3': 3,
                    '4': 4,
                },
                '2': 2,
                '3': 3,
            }
        }
    }

# Generated at 2022-06-12 23:07:15.032677
# Unit test for function recursive_diff
def test_recursive_diff():
    a = dict(
        dict1={'a':1, 'b':2},
        dict2={'a':3, 'b':4, 'c':5}
    )
    b = dict(
        dict1={'a':1, 'b':2},
        dict2={'a':3, 'b':4, 'c':6}
    )
    diff_result = recursive_diff(a, b)
    assert(diff_result != None)
    assert(diff_result[0] == {'c': 5})
    assert(diff_result[1] == {'c': 6})


# Generated at 2022-06-12 23:07:21.189728
# Unit test for function recursive_diff
def test_recursive_diff():
    import unittest
    class TestRecursiveDiff(unittest.TestCase):
        def test_recursive_diff_with_int(self):
            dict1 = {'a':1, 'b':2, 'c':3}
            dict2 = {'a':1, 'b':2, 'c':4}
            self.assertEqual(recursive_diff(dict1, dict2), ({'c':3}, {'c':4}))

        def test_recursive_diff_with_string(self):
            dict1 = {'a':'a', 'b':'b', 'c':'c'}
            dict2 = {'a':'a', 'b':'b', 'c':'f'}

# Generated at 2022-06-12 23:07:31.231424
# Unit test for function recursive_diff
def test_recursive_diff():
    left = {
        'a': 1,
        'b': {
            'c': 3,
            'd': 4
        },
        'e': 5
    }
    right = {
        'a': 2,
        'b': {
            'c': 3,
            'd': 6
        },
        'e': 7
    }

    result = recursive_diff(left, right)
    assert result == ({'a': 1}, {'a': 2, 'e': 7, 'b': {'d': 6}})

    # 'left' and 'right' have same values and get returned as None
    result = recursive_diff(right, left)
    assert result is None

# Generated at 2022-06-12 23:07:38.902702
# Unit test for function recursive_diff
def test_recursive_diff():
    '''Unit test for recursive_diff'''
    assert recursive_diff({}, {}) == None
    assert recursive_diff({1: 1}, {1: 1}) == None
    assert recursive_diff({1: 1}, {2: 1}) == ({1: 1}, {2: 1})
    assert recursive_diff({1: 1}, {}) == ({1: 1}, {})
    assert recursive_diff({1: 1}, {1: 2}) == ({1: 1}, {1: 2})
    assert recursive_diff({1: {2: 3}}, {1: {2: 3}}) == None
    assert recursive_diff({1: {2: 3}}, {1: {5: 3}}) == ({1: {2: 3}}, {1: {5: 3}})

# Generated at 2022-06-12 23:07:49.229815
# Unit test for function recursive_diff
def test_recursive_diff():

    from ansible.module_utils.common._collections_compat import Mapping

    # Helper function to test
    def _assert_isinstance(k1, k2, klass):
        assert isinstance(k1, klass)
        assert isinstance(k2, klass)

    # Quick check of proper TypeError if wrong type
    try:
        recursive_diff("a", "b")
    except TypeError:
        pass

    # Test simple differences
    d = {'a': 1, 'b': 2}
    diff = recursive_diff(d, {})
    assert len(diff) == 2
    assert diff[0] == d
    assert diff[1] == {}

    diff = recursive_diff({}, d)
    assert len(diff) == 2
    assert diff[0] == {}

# Generated at 2022-06-12 23:07:59.611264
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': '1',
        'HttpEndpoint': '2',
        'HTTPReader': {'httpEndpoint': '1'},
        'httpEndpoint': '3',
        'myHTTPEndpoint': '4',
        'myHttpEndpoint': '5',
        'HTTPEndpointARN': '6',
        'HTTPEndpointARNs': [
            {
                'HTTPEndpointARN': '7'
            }
        ],
        'Tags': {
            'HTTPEndpoint': {'Key': 'MyKey', 'Value': 'MyValue'},
            'httpEndpoint': {'Key': 'MyKey', 'Value': 'MyValue'},
            'Key': 'MyKey',
            'Value': 'MyValue'
        }
    }

    snake

# Generated at 2022-06-12 23:08:04.189339
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    #Test case 1:
    # Check case where no conversion is required
    input_dict = {"Test": "value", "testKey": "value"}
    assert camel_dict_to_snake_dict(input_dict) == input_dict

    # Test case 2:
    # Check case where conversion is required
    input_dict = {"TestKey": "value", "test": "value", "testName": "value"}
    expected_dict = {"test_key": "value", "test": "value", "test_name": "value"}
    assert camel_dict_to_snake_dict(input_dict) == expected_dict

    # Test case 3:
    # Check case where conversion is not required for nested dict

# Generated at 2022-06-12 23:08:24.211543
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    d = {
        "Key1": "val1",
        "Key2": "val2",
        "Key3": {
            "Key31": "val31",
            "Key32": "val32",
            "Key33": [
                "val331",
                "val332",
            ],
            "Key34": {
                "Key341": "val341",
                "Key342": "val342",
                "Key343": [
                    "val3431",
                    "val3432",
                ],
                "Key344": {
                    "Key3441": "val3441",
                    "Key3442": "val3442",
                },
            },
        },
    }


# Generated at 2022-06-12 23:08:32.244004
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': 'http_endpoint', 'HTTPPassThroughResponses': ['http_pass_through_responses'], 'EndpointType': 'endpoint_type', 'Tags': {'Key': 'Value'}}
    assert camel_dict_to_snake_dict(camel_dict) == {'h_t_t_p_endpoint': 'http_endpoint', 'h_t_t_p_pass_through_responses': ['http_pass_through_responses'], 'endpoint_type': 'endpoint_type', 'tags': {'Key': 'Value'}}


# Generated at 2022-06-12 23:08:37.557549
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        'Foo': 'bar',
        'Baz': [
            {'Bar': 'baz'},
            {'FooBar': 'foobar'}
        ],
        'Tags': {
            'Tag': [{'Key': 'Name', 'Value': 'my_test_demo_server'}]
        }
     }

    expected = {
        'foo': 'bar',
        'baz': [
            {'bar': 'baz'},
            {'foo_bar': 'foobar'}
        ],
        'tags': {
            'tag': [{'key': 'Name', 'value': 'my_test_demo_server'}]
        }
    }

    result = camel_dict_to_snake_dict(d)
    assert result == expected




# Generated at 2022-06-12 23:08:47.833444
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:57.773512
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge(
        { 'alpha': 1, 'bravo': 3 },
        { 'alpha': 2, 'charlie': 5 }
    ) == { 'alpha': 2, 'bravo': 3, 'charlie': 5 }

    assert dict_merge(
        { 'alpha': { 'x': 1 }, 'bravo': 3 },
        { 'alpha': { 'y': 2 }, 'charlie': 5 }
    ) == { 'alpha': { 'x': 1, 'y': 2 }, 'bravo': 3, 'charlie': 5 }

    assert dict_merge(
        { 'alpha': { 'x': 1, 'y': 2 }, 'bravo': 3 },
        { 'alpha': { 'x': 4, 'z': 5 }, 'charlie': 5 }
    )

# Generated at 2022-06-12 23:09:08.069164
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    snake_dict = {'name': 'test'}

    assert camel_dict_to_snake_dict({'Name': 'test'}) == snake_dict
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'test'}) == {'http_endpoint': 'test'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'test'}, True) == {'h_t_t_p_endpoint': 'test'}
    assert camel_dict_to_snake_dict({'Tags': {'key': 'value'}, 'TagsToRemove': {'key1': ['value1']}}) == \
        {'tags': {'key': 'value'}, 'tags_to_remove': {'key1': ['value1']}}
    assert camel_dict_to_

# Generated at 2022-06-12 23:09:18.805342
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'testKey1': 'testValue1',
                 'testKey2': 'testValue2',
                 'testKey3': {'testKey3Child1': 'testValue3',
                              'testKey3Child2': 'testValue4',
                              'testKey3Child3': {'testKey3Child3Child1': 'testValue5',
                                                 'testKey3Child3Child2': {'testKey3Child3Child2Child1': 'testValue6'},
                              },
                 },
                 'testKey4': ['testValue7', 'testValue8'],
    }

# Generated at 2022-06-12 23:09:26.547224
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:36.902515
# Unit test for function dict_merge
def test_dict_merge():

    d1 = {
        'name': 'foo',
        'test': {
            'environment': 'dev',
            'set': {'verbose': True, 'tunnel-port' : 3306},
            'int_list': [1, 2],
            'string_list': ['a', 'b']
        }
    }

    d2 = {
        'name': 'bar',
        'test': {
            'environment': 'qa',
            'set': {'tunnel-port' : 7777, 'verbose': False},
            'int_list': [3, 4],
            'string_list': ['c', 'd']
        }
    }


# Generated at 2022-06-12 23:09:46.864050
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'SubnetIds': ['subnet1', 'subnet2', 'subnet3'],
                                     'SubnetId': 'subnet1'}) == {'subnet_ids': ['subnet1', 'subnet2', 'subnet3'],
                                                                 'subnet_id': 'subnet1'}

# Generated at 2022-06-12 23:09:57.285599
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    tested_dict = {
        "a": "test",
        "b": {
            "c": "test",
            "d": {
                "e": "test",
                "f": [
                    {
                        "g": 1,
                        "h": [1, 2, 3, 4],
                    },
                    {
                        "i": 1,
                        "j": 2,
                    }
                ]
            }
        }
    }


# Generated at 2022-06-12 23:10:04.655179
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'a': 'A', 'b': 'B'}) == {
        'a': 'A',
        'b': 'B'
    }
    assert camel_dict_to_snake_dict({'aB': 'A', 'B': 'B'}) ==  {
        'a_b': 'A',
        'b': 'B'
    }
    assert camel_dict_to_snake_dict({'HttpEndpoint': 'A', 'B': 'B'}) ==  {
        'http_endpoint': 'A',
        'b': 'B'
    }

# Generated at 2022-06-12 23:10:13.781462
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {}
    test_dict['InstanceId'] = 'i-1234567890abcdef0'
    test_dict['Placement'] = {}
    test_dict['Placement']['AvailabilityZone'] = 'us-east-1a'
    test_dict['Tags'] = [{'Key': 'Name', 'Value': 'foo'}, {'Key': 'Environment', 'Value': 'production'}]
    test_dict['Tags'].append({'Key': 'Test', 'Value': 'TestValue'})
    # Add another tag for testing.
    test_dict['Tags'].append({'Key': 'Test', 'Value': 'TestValue2'})
    # Test a key that shouldn't be converted:
    test_dict['BlockDeviceMappings'] = []

# Generated at 2022-06-12 23:10:24.974128
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'Abbreviation': 'HTTP', 'Component': 'foo', 'HttpEndpoint': {'Protocol': 'http', 'Port': 80, 'Path': '/'},
                 'HttpAuth': {'Type': 'basic', 'User': 'testuser', 'Password': 'testpass'},
                 'GrpcEndpoint': {'Port': 8081},
                 'Tags': {'foo': 'fooval', 'bar': 'barval'}}


# Generated at 2022-06-12 23:10:34.744016
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test for dictionary with empty value
    test_dict = {'test_key': ''}
    assert camel_dict_to_snake_dict(test_dict) == test_dict

    # Test for dictionary with empty value and key
    test_dict = {'': ''}
    assert camel_dict_to_snake_dict(test_dict) == {'': ''}

    # Test for dictionary with empty value and key
    test_dict = {'': 'test_value'}
    assert camel_dict_to_snake_dict(test_dict) == {'': 'test_value'}

    # Test for dictionary with values as list
    test_dict = {'test_key': ['test_value1', 'test_value2']}
    assert camel_dict_to_snake_dict(test_dict) == test

# Generated at 2022-06-12 23:10:41.878177
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'ID': 'AZ-1',
        'Name': 'Ansible AZ',
        'DNSName': 'AnsibleAZ.example.com',
        'HTTPEndpoint': 'http',
        'Tags': {
            'Name': 'Ansible',
            'Environment': 'Dev'
        }
    }
    assert camel_dict_to_snake_dict(camel_dict, False) == {
        'id': 'AZ-1',
        'name': 'Ansible AZ',
        'dns_name': 'AnsibleAZ.example.com',
        'http_endpoint': 'http',
        'tags': {
            'Name': 'Ansible',
            'Environment': 'Dev'
        }
    }



# Generated at 2022-06-12 23:10:51.657032
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
  camel_dict = { 'Comment' : 'This is a test.',
		 'Tags' : [ { 'Key' : 'color', 'Value' : 'blue'}, { 'Key' : 'size', 'Value' : 'medium'}]
               }
  camel_dict['InstanceIds'] = ['i-123456']
  camel_dict['VolumeIds'] = ['vol-abcdef']
  camel_dict['DryRun'] = False
  camel_dict['MaxResults'] = 1000
  test_dict = camel_dict_to_snake_dict(camel_dict, True)

# Generated at 2022-06-12 23:10:59.997541
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Tests the normal flow where a regular camelCase is converted to snake_case
    test_dict_1 = { 'key1': 'value1', 'key2': 2, 'key3': 3.0, 'key4': [5, 6], 'key5': {'key6': 'value6', 'key7': 'value7'}, 'Tags': [{'Key': 'testTagKey', 'Value': 'testTagValue'}] }
    test_dict_2 = { 'key1': 'value1', 'key2': 2, 'key3': 3.0, 'key4': [5, 6], 'key5': {'key6': 'value6', 'key7': 'value7'}, 'tags': [{'key': 'testTagKey', 'value': 'testTagValue'}] }

# Generated at 2022-06-12 23:11:10.280531
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "Tags": [
            {
                "Value": "staging",
                "Key": "environment"
            },
            {
                "Value": "db",
                "Key": "role"
            }
        ],
        "SubnetIds": [
            "subnet-01e42f748e7f9c0cf",
            "subnet-04f22e35c04a85d80"
        ],
        "CapacityReservationName": "",
        "CapacityReservationPreference": "none",
        "StackName": "ec2-instance"
    }


# Generated at 2022-06-12 23:11:19.769949
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "HTTPPassword": "password",
            "HTTPUsername": "username",
            "Ports": [80, 8080],
            "Protocols": ["http"],
            "TimeoutMillis": 123,
        },
        "Name": "name",
        "Protocol": "http",
        "Tags": {"a": "b"},
    }


# Generated at 2022-06-12 23:11:35.158861
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "HTTPEndpoint": {
            "EndpointLoggingEnabled": True,
            "TimeoutInMillis": 60000,
            "AuthorizationValue": "Basic",
            "IdleTimeoutInMillis": 900000,
            "Authorization": {
                "Type": "AWS_IAM"
            },
            "Path": "/test"
        },
        "Tags": {
            "Tags": {
                "TagSource": "tagSource",
                "TagKey": "tagKey",
                "TagValue": "tagValue"
            }
        }
    }

# Generated at 2022-06-12 23:11:43.038848
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Protocol': 'HTTPS',
            'AuthorizationType': 'AWS_IAM',
            'Tags': {
                'Tag1': 'Value1',
                'Tag2': 'Value2'
            }
        },
        'VpcLink': {
            'VpcLinkId': 'test-vpc-link'
        }
    }


# Generated at 2022-06-12 23:11:51.939556
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 1}) == {'http_endpoint': 1}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 1}, True) == {'h_t_t_p_endpoint': 1}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'HTTPEndpoint': 1}}) == {'http_endpoint': {'http_endpoint': 1}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': [{'HTTPEndpoint': 1}]}) == {'http_endpoint': [{'http_endpoint': 1}]}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 1}, False) == {'http_endpoint': 1}

# Generated at 2022-06-12 23:12:00.978022
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(dict()) == dict()
    assert camel_dict_to_snake_dict({'foo': 'bar'}) == {'foo': 'bar'}
    assert camel_dict_to_snake_dict({'fooBar': 'bar'}) == {'foo_bar': 'bar'}
    assert camel_dict_to_snake_dict({'fooBar': 'bar', 'baz_bar': 'baz'}) == {'foo_bar': 'bar', 'baz_bar': 'baz'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'bar'}) == {'http_endpoint': 'bar'}

# Generated at 2022-06-12 23:12:11.104315
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:19.795522
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({}, True) == {}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'foo'}) == {'http_endpoint': 'foo'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'foo'}, True) == {'h_t_t_p_endpoint': 'foo'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'foo', 'HTTPSEndpoint': 'http://foo'}) == {'http_endpoint': 'foo', 'https_endpoint': 'http://foo'}

# Generated at 2022-06-12 23:12:29.959381
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Dictionary with no nested values
    camel_dict = {
        "bool_type": True,
        "string_type": "abc123",
        "int_type": 123
    }

    snake_dict = {
        "bool_type": True,
        "string_type": "abc123",
        "int_type": 123
    }

    # Dictionary with nested values

# Generated at 2022-06-12 23:12:40.393744
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict(None) is None
    assert camel_dict_to_snake_dict(True) is True
    assert camel_dict_to_snake_dict(False) is False
    assert camel_dict_to_snake_dict("foo") == "foo"
    assert camel_dict_to_snake_dict(1) == 1
    assert camel_dict_to_snake_dict(1.0) == 1.0
    assert camel_dict_to_snake_dict(b"foo") == b"foo"
    assert camel_dict_to_snake_dict(bytearray(b"foo")) == bytearray(b"foo")
    assert camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:47.929773
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:57.517963
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    def run_test(camel_dict, snake_dict):
        result = camel_dict_to_snake_dict(camel_dict)
        module.assertEqual(result, snake_dict,
                           msg="camel_dict_to_snake_dict failed on:\n%s\nGot:\n%s" % (str(camel_dict), str(result)))


# Generated at 2022-06-12 23:13:11.792994
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "location": {
            "latitude": 0,
            "longitude": 0
        },
        "name": "Foo Bar",
        "tags": {
            "TagKey": "TagValue"
        },
        "configuration": {
            "BucketName": "MyBucket",
            "BucketPrefix": "FooBarPrefix",
            "EncodingType": "gzip",
            "FileFormat": "Parquet",
            "CompressionFormat": "SNAPPY",
            "RoleARN": "arn:aws:iam::123456789012:role/AthenaResultsRole",
            "EnableEncryption": False
        }
    }


# Generated at 2022-06-12 23:13:18.302767
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Dict to test
    camel_dict = {
        "refreshToken": "example",
        "HTTPEndpoint": {
            "public": True
        },
        "tags": {
            "a": "1",
            "b": "2"
        }
    }

    # Expected result of conversion
    expected_snake_dict = {
        "refresh_token": "example",
        "h_t_t_p_endpoint": {
            "public": True
        },
        "tags": {
            "a": "1",
            "b": "2"
        }
    }

    actual_snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert actual_snake_dict == expected_snake_dict



# Generated at 2022-06-12 23:13:29.188827
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    my_dict = {'fooBar': {'nestedFooBaz': 'baz',
                          'nestedFoo': 'bar',
                          'deeplyNested': {'foo': 'bar'},
                          'list': [{'foo': 'baz'}]},
               'fooBarBaz': {'nestedFooBar': 'baz',
                             'nestedFooBaz': 'bar',
                             'list': [{'foo': 'baz'}]},
               'bazFoo': 'bar'}


# Generated at 2022-06-12 23:13:38.435983
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # test 1, simple dictionary
    camel_dict = {'HTTPEndpoint': 'http://www.example.com'}
    test_dict = {'h_t_t_p_endpoint': 'http://www.example.com'}
    assert camel_dict_to_snake_dict(camel_dict) == test_dict

    # test 2, nested dictionary
    camel_dict = {'Tags': {'HTTPEndpoint': 'http://www.example.com'}}
    test_dict = {'tags': {'h_t_t_p_endpoint': 'http://www.example.com'}}
    assert camel_dict_to_snake_dict(camel_dict) == test_dict

    # test 3, recursive conversion

# Generated at 2022-06-12 23:13:47.677823
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_data = {
        "SecurityGroups": ["sg1", "sg2"],
        "Tags": {
            "Name": "instance1",
            "Tags": "t1"
        },
        "Name": "value"
    }
    expected_output = {
        "security_groups": ["sg1", "sg2"],
        "tags": {
            "Name": "instance1",
            "Tags": "t1"
        },
        "name": "value"
    }
    output = camel_dict_to_snake_dict(test_data)
    assert output == expected_output

# Generated at 2022-06-12 23:13:57.438920
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Trying to test a (very) complex object.
    camel_dict = {
        "User": {
            "Name": {
                "FirstName": "Alice",
                "MiddleInitial": "",
                "LastName": "Liddel"
            },
            "HomeAddress": {
                "StreetAddressLine1": "123 Anywhere Place",
                "City": "Neverland",
                "PostalCode": "12345",
                "CountryCode": "USA"
            }
        }
    }

# Generated at 2022-06-12 23:14:02.365176
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'aB': 1, 'bB': 2, 'attachmentSet': [{'a': 5, 'bC': 6}]}
    expected_output = {'a_b': 1, 'b_b': 2, 'attachment_set': [{'a': 5, 'b_c': 6}]}
    output = camel_dict_to_snake_dict(test_dict)
    assert output == expected_output



# Generated at 2022-06-12 23:14:11.845080
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_cases = []
    default = None
    expected = None
    description = "Default"
    test_cases.append({'test_case': default, 'expected': expected, 'description': description})

    default = {}
    expected = {}
    description = "Empty Dict"
    test_cases.append({'test_case': default, 'expected': expected, 'description': description})

    default = {'bob': 'fred'}
    expected = {'bob': 'fred'}
    description = "Non-Camel Dict"
    test_cases.append({'test_case': default, 'expected': expected, 'description': description})

    default = {'Bob': 'fred'}
    expected = {'bob': 'fred'}
    description = "Camel to Snake"

# Generated at 2022-06-12 23:14:21.428660
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Prepare input and correct output
    camel_dict = {
        'keyOne': 'valueOne',
        'keyTwo': 'valueTwo',
        'subDict': {
            'subKeyOne': 'subValueOne',
            'subKeyTwo': 'subValueTwo'
        }
    }
    snake_dict = {
        'key_one': 'valueOne',
        'key_two': 'valueTwo',
        'sub_dict': {
            'sub_key_one': 'subValueOne',
            'sub_key_two': 'subValueTwo'
        }
    }

    # Perform conversion
    converted = camel_dict_to_snake_dict(camel_dict)

    # Test conversion
    assert converted == snake_dict



# Generated at 2022-06-12 23:14:32.225660
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    import json
    import textwrap


# Generated at 2022-06-12 23:14:44.889779
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:54.202806
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {'targetGroupARNs': ['arn:aws:elasticloadbalancing:us-west-2:187157862766:targetgroup/exampleservice/0'],
                  'HTTPEndpoint': {'Path': '/service/example',
                                   'Port': 80}}
    result = camel_dict_to_snake_dict(input_dict)
    expected = {'target_group_arns': ['arn:aws:elasticloadbalancing:us-west-2:187157862766:targetgroup/exampleservice/0'],
                'h_t_t_p_endpoint': {'path': '/service/example',
                                     'port': 80}}
    assert result == expected



# Generated at 2022-06-12 23:15:03.961642
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'HTTPURL': 'foo'}, 'HTTPSEndpoint': {'HTTPSURL': 'foo'}}) == \
        {'h_t_t_p_endpoint': {'http_url': 'foo'}, 'h_t_t_p_s_endpoint': {'https_url': 'foo'}}

# Generated at 2022-06-12 23:15:12.165165
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test base case
    test_dict = {'HTTPEndpoint': 'test'}
    test_result = camel_dict_to_snake_dict(test_dict)
    expected_result = {'http_endpoint': 'test'}
    assert expected_result == test_result

    # Test nested dict case
    test_dict = {'HTTPEndpoint': {'UserGuidIsOpaque': 'irrelevant'}}
    test_result = camel_dict_to_snake_dict(test_dict)
    expected_result = {'http_endpoint': {'user_guid_is_opaque': 'irrelevant'}}
    assert expected_result == test_result

    # Test list case

# Generated at 2022-06-12 23:15:20.278055
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:31.057290
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # test case 1
    original = {
        "TagList": [
            {
                "Key": "string",
                "Value": "string"
            }
        ],
        "HTTPEndpoint": {
            "EndpointURL": "string",
            "RequestTimeoutSeconds": 123,
            "Authorization": {
                "SigningRegion": "string",
                "SigningServiceName": "string",
                "CredentialScope": {
                    "Service": "string",
                    "Region": "string"
                },
                "RoleARN": "string"
            }
        }
    }


# Generated at 2022-06-12 23:15:41.103520
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test dictionary of dictionary type
    camel_dict = {
        'TestString': 'string',
        'Test1': 1,
        'TestBool': True,
        'TestList': [
            'list1',
            'list2',
            'list3'],
        'NestedDict': {
            'NestedString': 'string',
            'Nested1': 1,
            'Nested2': 2
        }
    }

    # Expected keys in snake case
    expected_keys = set(['test_string', 'test_1', 'test_bool', 'test_list', 'nested_dict'])

    # Expected keys in snake case with nested dictionary
    expected_nested_keys = {'nested_string', 'nested_1', 'nested_2'}

    snaked_dict

# Generated at 2022-06-12 23:15:48.447791
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    data = {
        'SubnetIds': ['subnet-1', 'subnet-2'],
        'Tags': {'TAG_NAME': 'VALUE'},
        'HTTPEndpoint': {'Enabled': True},
        'TargetGroupARNs': [
            'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/73e2d6bc24d8a067'
        ]
    }

# Generated at 2022-06-12 23:15:53.586747
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:02.816356
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:19.177067
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "EC2SecurityGroupId": "sg-4dd3fe21",
        "EC2SecurityGroupName": "test-sg",
        "EC2SecurityGroupOwnerId": "123456789012",
        "Status": "authorized"
    }

    assert camel_dict_to_snake_dict(camel_dict) == {
        "ec2_security_group_id": "sg-4dd3fe21",
        "ec2_security_group_name": "test-sg",
        "ec2_security_group_owner_id": "123456789012",
        "status": "authorized"
    }

    # Test that camel_dict_to_snake_dict works when used twice

# Generated at 2022-06-12 23:16:25.042574
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Url': 'http://www.example.com'}}) == \
        {'h_t_t_p_endpoint': {'url': 'http://www.example.com'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Url': 'http://www.example.com'}}, reversible=True) == \
        {'h_t_t_p_end_point': {'url': 'http://www.example.com'}}



# Generated at 2022-06-12 23:16:33.996761
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:39.958406
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    new_dict = camel_dict_to_snake_dict({
        'fooBar': {
            'baz': 'qux',
            'quux': {
                'corge': 'grault'
            }
        },
        'HTTPEndpoint': 'http://www.example.com',
        'FooBar': {
            'Grault': 'Garply',
            'Waldo': 'Fred'
        }
    }, reversible=True)
