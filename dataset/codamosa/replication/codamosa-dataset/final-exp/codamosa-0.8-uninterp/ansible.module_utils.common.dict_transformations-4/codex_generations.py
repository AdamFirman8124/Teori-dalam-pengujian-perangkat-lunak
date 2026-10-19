

# Generated at 2022-06-12 23:06:52.053052
# Unit test for function recursive_diff
def test_recursive_diff():
    x = {'a': 1, 'b': 2, 'c': 3}
    y = {'a': 1, 'b': 2, 'c': 7}
    z = {'a': 1, 'b': 2, 'd': 3}
    t = {'a': 1, 'b': 2, 'd': 7}
    u = {'a': 1, 'b': 2, 'c': {'x': 9, 'y': 10, 'z': 11}, 'd': 7}
    v = {'a': 1, 'b': 2, 'c': {'q': 9, 'y': 10, 'z': 11}, 'd': 3}
    w = {'a': 1, 'b': 2, 'c': {'q': 3, 'y': 4, 'z': 11}, 'd': 3}
    s

# Generated at 2022-06-12 23:07:02.925738
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) is None
    assert recursive_diff({"x": "y"}, {}) == ({"x": "y"}, {})
    assert recursive_diff({1: {"x": "y"}}, {}) == ({1: {"x": "y"}}, {})
    assert recursive_diff({1: {"x": "y"}}, {1: {"x": "y"}}) is None
    assert recursive_diff({1: {"x": "y", "z": "a"}}, {1: {"x": "y"}}) == \
        ({1: {"z": "a"}}, {1: {}})

# Generated at 2022-06-12 23:07:13.109377
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
                 'KeyOne': 1,
                 'KeyTwo': {
                             'Key_Three': 3,
                             'NestedDict': {
                                             'Key_Four': [4, 'Four']
                                           }
                           },
                 'SubList': [{'KeyFive': 5}, {'KeySix': 6}]
                }
    expected_result = {
                       'key_one': 1,
                       'key_two': {
                                   'key_three': 3,
                                   'nested_dict': {
                                                   'key_four': [4, 'Four']
                                                  }
                                  },
                       'sub_list': [{'key_five': 5}, {'key_six': 6}]
                      }

    assert camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:19.959076
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict = {
        'VpcEndpoint': 'endpoint',
        'ServiceName': 'test',
        'PolicyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': '*',
                    'Resource': '*',
                    'Effect': 'Allow'
                }
            ]
        },
        'RouteTableIds': [
            'rtb-12345678'
        ],
        'PrivateDnsEnabled': False,
        'ClientToken': '123',
        'SubnetIds': [
            'subnet-12345678'
        ],
        'SecurityGroupIds': [
            'sg-12345678'
        ]
    }

# Generated at 2022-06-12 23:07:31.649998
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {
        'a': {
            'b': 2,
            'c': 3,
            'd': {
                'e': 2
            },
            'g': {
                'h': 'test'
            },
            'i': {
                'j': 'test'
            }
        },
        'b': 'test2',
        'c': 'test3'
    }
    d2 = {
        'a': {
            'b': 2,
            'c': 4,
            'd': {
                'e': 3
            },
            'g': {
                'h': 'test2'
            },
            'i': {
                'j': 'test'
            }
        },
        'b': 'test2',
        'c': 'test3'
    }


# Generated at 2022-06-12 23:07:39.215448
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        "dummy": {
            "Index": 1,
            "list": [
                1,
                2,
                3
            ],
            "test": "sample"
        },
        "sample": "test",
        "sample_dict": {
            "Key1": "Value1",
            "Key2": "Value2"
        }
    }
    dict2 = {
        "dummy": {
            "Index": 2,
            "list": [
                1,
                2
            ],
            "test": "sample1"
        },
        "sample": "test",
        "sample_dict": {
            "Key1": "Value1",
            "Key2": "Value3"
        }
    }

# Generated at 2022-06-12 23:07:50.016541
# Unit test for function dict_merge
def test_dict_merge():
    d1 = {'a': 1, 'b': 2, 'c': {'c1': 'a', 'c2': 'b'}, 'g': 'h'}
    d2 = {'a': 2, 'b': 2, 'c': {'c1': 'a', 'c3': 'c'}, 'd': 'f'}
    result = {'a': 2, 'b': 2, 'c': {'c1': 'a', 'c2': 'b', 'c3': 'c'}, 'd': 'f', 'g': 'h'}
    assert result == dict_merge(d1, d2)
    # Test for merge in a deep nesting of dictionaries.

# Generated at 2022-06-12 23:08:00.290986
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'key1': {'key1a': 'value1a', 'key1b': 'value1b'},
             'key2': 'value2',
             'key3': {'key3a': {'key3aa': 'value3aa',
                                'key3ab': 'value3ab'}},
             'key4': [1, 2, 3, 4]}
    dict2 = {'key1': {'key1a': 'value1a', 'key1c': 'value1c'},
             'key3': {'key3a': {'key3aa': 'value3aa',
                                'key3ab': 'value3ab'}},
             'key4': [1, 2, 3],
             'key5': 'value5'}

# Generated at 2022-06-12 23:08:10.767074
# Unit test for function recursive_diff
def test_recursive_diff():
    a = {'one': 1, 'two': 2, 'three': 3, 'four': {'five': 5, 'six': 6, 'seven': 7}, 'eight': 8}
    b = {'one': 1, 'two': 2, 'three': 3, 'four': {'five': 5, 'six': 6, 'seven': 7}, 'eight': 8}
    assert recursive_diff(a, b) is None
    a = {'one': 1, 'two': 2, 'three': 3, 'four': {'five': 5, 'six': 6, 'seven': 7, 'twelve': 12}, 'eight': 8}
    b = {'one': 1, 'two': 2, 'three': 3, 'four': {'five': 5, 'six': 6, 'seven': 7}, 'eight': 8}
    assert recursive_

# Generated at 2022-06-12 23:08:21.327167
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:34.823037
# Unit test for function recursive_diff
def test_recursive_diff():
    """Tests for recursive_diff function."""
    first = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}, 'f': 5}
    second = {'a': 1, 'b': 20, 'g': {'h': 5, 'i': 6}, 'c': {'j': 7, 'e': 8}}
    expected = ({'b': 2, 'c': {'d': 3, 'e': 4}}, {'b': 20, 'c': {'e': 8}, 'g': {'h': 5, 'i': 6}})
    assert recursive_diff(first, second) == expected
    assert recursive_diff(second, first) == expected


# Generated at 2022-06-12 23:08:44.578220
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def _test_dict(camel_dict, snake_dict, reversible=False):
        assert camel_dict_to_snake_dict(camel_dict, reversible) == snake_dict

    # Basic test of string keys
    _test_dict({'foo': 1, 'barBaz': 2},
               {'foo': 1, 'bar_baz': 2})

    # Test of unicode keys
    _test_dict({u'foo': 1, u'barBaz': 2},
               {u'foo': 1, u'bar_baz': 2})

    # Test of list keys

# Generated at 2022-06-12 23:08:55.053488
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test recursive_diff

    Raises ``TypeError`` for incorrect argument type.

    :return: Tuple of dictionaries of differences or ``None`` if there are no differences.
    """
    dict1 = {'a': 1, 'b': 2, 'c': {'1': 1, '2': 2, '3': 3}, 'd': 4, 'e': {'5': 5, '6': {'7': 7, '9': 9}, '10': 10}}
    dict2 = {'a': 2, 'b': 2, 'c': {'1': 1, '2': 3, '4': 4}, 'd': 4, 'e': {'5': 5, '6': {'7': 7, '9': 8}, '10': 11}}

# Generated at 2022-06-12 23:09:03.444082
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    print("Testing camel_dict_to_snake_dict")

    # Test normal example

# Generated at 2022-06-12 23:09:14.457039
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'ARN': 'abc123', 'name': 'abc', 'list': ['a', 'b'], 'arn': 'xyz', 'dict': {'other': 'stuff'}, 'Tags': [{'Key': 'name', 'Value': 'my-name'}]}) == \
        {'arn': 'xyz', 'name': 'abc', 'list': ['a', 'b'], 'dict': {'other': 'stuff'}, 'Tags': [{'Key': 'name', 'Value': 'my-name'}]}


# Generated at 2022-06-12 23:09:23.432035
# Unit test for function recursive_diff
def test_recursive_diff():
    """
    Test the recursive_diff function
    """

    # test for empty dictionaries
    dict1 = {}
    dict2 = {}
    assert recursive_diff(dict1, dict2) == None
    # test for same dictionary
    dict1 = {'sub1': {'subsub1': [1, 2, 3],
                      'subsub2': {'subsubsub1': 'string1', 'subsubsub2': 'string2'}},
             'sub2': 'this'}
    assert recursive_diff(dict1, dict1) == None
    # test for different dictionaries

# Generated at 2022-06-12 23:09:33.154676
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    res = camel_dict_to_snake_dict({'UserName': 'Bob', 'UserEmail': 'Bob@example.com'})
    assert res['user_name'] == 'Bob'
    assert res['user_email'] == 'Bob@example.com'

    res = camel_dict_to_snake_dict({'UserName': 'Bob', 'UserEmail': 'Bob@example.com'}, reversible=True)
    assert res['u_ser_name'] == 'Bob'
    assert res['u_ser_email'] == 'Bob@example.com'

    res = camel_dict_to_snake_dict({'UserName': 'Bob', 'UserEmail': 'Bob@example.com'}, reversible=True,
                                   ignore_list=('Tags'))
    assert res['u_ser_name'] == 'Bob'

# Generated at 2022-06-12 23:09:43.875121
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:51.674996
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        'Tags': {
            'key-1': 'value-1',
            'key-2': 'value-2'
        },
        'TargetGroupARNs': [
            'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
            'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/73e2d6bc24d8a068'
        ],
        'HTTPEndpoint': 'true'
    }


# Generated at 2022-06-12 23:10:00.237423
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    testdata = {
        'test_dict': {
            'ChildObject': {
                'camelCase': 'camel_case',
                'HTTPEndPoint': 'h_t_t_p_endpoint'
            },
            'camelCase': 'camel_case',
            'HTTPEndPoint': 'h_t_t_p_endpoint',
            'Tags': {
                'Ansible': 'Test',
                'ansible': 'test'
            }
        }
    }

# Generated at 2022-06-12 23:10:12.782645
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    x = {'ThingName': 'myThing', 'ThingTypeName': 'myThingType', 'ThingAttributes': {'string': 's', 'number': 1}}
    y = {'thing_name': 'myThing', 'thing_type_name': 'myThingType', 'thing_attributes': {'string': 's', 'number': 1}}
    assert camel_dict_to_snake_dict(x) == y
    assert camel_dict_to_snake_dict(y, reversible=True) == x
    assert camel_dict_to_snake_dict(y, reversible=True) == y

    # Tags is a special case, must use ignore_list
    x = {'Tags': {'Key': 'First Tag'}}
    y = {'tags': {'key': 'First Tag'}}

# Generated at 2022-06-12 23:10:23.704535
# Unit test for function recursive_diff
def test_recursive_diff():
    # Left side is different from right side
    dict1 = {'foo': 'bar', 'baz': 'qux', 'abc': {'mno': 'pqr'}}
    dict2 = {'foo': 'bar', 'baz': 'qux', 'abc': {'mno': 'xyz'}}
    res = recursive_diff(dict1, dict2)
    assert res is not None, "Result of recursive_diff() is None"
    assert len(res) == 2, "Expected list of 2 elements but received %s" % len(res)
    assert len(res[0]) == 1, "Expected list size 1 but received %s" % len(res[0])
    assert len(res[1]) == 1, "Expected list size 1 but received %s" % len(res[1])

# Generated at 2022-06-12 23:10:31.673657
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    required_parameters = ['ec2_url', 'aws_access_key', 'aws_secret_key']
    optional_parameters = {'region': 'us-west-2', 'validate_certs': True, 'profile': {}}

    # test to make sure that required parameters are given
    if not all(param in optional_parameters for param in required_parameters):
        missing_params = [param for param in required_parameters if param not in optional_parameters]
        raise Exception("Missing required arguments: %s" % ",".join(missing_params))

    if 'profile' in optional_parameters:
        binary_botocore_config = True

# Generated at 2022-06-12 23:10:39.367141
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    original = dict(
        AvailabilityZone='zone',
        Bandwidth='5',
        DryRun=True,
        Ipv6CidrBlock='abcdef',
        VpcEndpointType='Interface',
        VpcId='vpc-1234567890abcdef0'
    )
    expected = dict(
        availability_zone='zone',
        bandwidth='5',
        dry_run=True,
        cidr_block='abcdef',
        type='Interface',
        vpc_id='vpc-1234567890abcdef0'
    )
    actual = camel_dict_to_snake_dict(original)
    assert actual == expected



# Generated at 2022-06-12 23:10:49.374509
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {
        'fooBar': True,
        'camelCase': 'camel',
        'lowercase': 'lower',
        'HTTPEndpoint': 'https://example.com',
        'HTTPEndpointList': ['https://example.com', 'https://example.org'],
        'Tags': {'Description': 'a description'},
        'notConverted': {
            'camelCase': 'camel',
            'lowercase': 'lower',
            'HTTPEndpoint': 'https://example.com',
            'HTTPEndpointList': ['https://example.com', 'https://example.org'],
            'Tags': {'Description': 'a description'}
        }
    }


# Generated at 2022-06-12 23:10:56.628772
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Note that this is not a perfect test, since there are some cases
    # (e.g. aaa_bbb_ccc) that are impossible to write in camel case

    camel_dict = {
        'SimpleStr': 'a string',
        'SimpleInt': 1,
        'HTTPEndpoint': 'localhost:8080',
        'something_camel': 'aaa_ccc',
        'fancyMix': {
            'foo': 'bar',
            'bazFoo': {
                'fooBaz': 'barBaz'
            }
        },
        'aaAABbB': 'sdsd'
    }

# Generated at 2022-06-12 23:11:04.540752
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:14.209959
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    '''returns True if two dicts are equal, ignores vlaues of primitives
    that are lists'''
    def dicts_equal(dict1, dict2):

        def lists_equal(list1, list2):
            if len(list1) != len(list2):
                return False
            for i in range(len(list1)):
                if list1[i] != list2[i]:
                    return False
            return True

        if len(dict1.keys()) != len(dict2.keys()):
            return False
        for k, v in dict1.items():
            if k not in dict2:
                return False
            if isinstance(v, dict):
                if not dicts_equal(v, dict2[k]):
                    return False

# Generated at 2022-06-12 23:11:25.104470
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Simple case: camelized key, string value
    test_case = {'instanceName': 'foo'}
    assert camel_dict_to_snake_dict(test_case) == {'instance_name': 'foo'}

    # Traditional issue: all-caps key, should not be converted
    test_case = {'HTTPEndpoint': 'https://foo.bar'}
    assert camel_dict_to_snake_dict(test_case) == {'http_endpoint': 'https://foo.bar'}

    # Reversible all-caps key, should be converted,
    # such that it can be converted back to camel_dict
    test_case = {'HTTPEndpoint': 'https://foo.bar'}

# Generated at 2022-06-12 23:11:35.415294
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    json = {'HTTPEndpoint': {
        'URL': 'http://ec2-54-175-184-149.compute-1.amazonaws.com',
        'EndpointStatus': 'Valid'},
        'HostKeyFingerprint': '4a:22:cc:7d:b6:8b:2e:a0:c6:9f:46:e6:ef:fa:96:a0',
        'ServerId': 'i-12345678'}

# Generated at 2022-06-12 23:11:46.548440
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    print('Testing function camel_dict_to_snake_dict')
    test_dict = {
        'StringKey': 'StringValue',
        'OtherStringKey': 'OtherStringValue',
        'Key': {
            'NestedKey': 'NestedValue',
            'OtherNestedKey': 'OtherNestedValue',
        },
        'ListKey': [
            'StringValue',
            {'NestedKey': 'NestedValue'},
            {'OtherNestedKey': 'OtherNestedValue'},
        ]
    }

# Generated at 2022-06-12 23:11:56.176025
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:05.066589
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    raw_dict = \
      { 'Tags':
          { 'Key': 'testTag'
          , 'Value': 'testValue'
          }
      , 'RoleArn': 'arn:aws:iam::012345678901:role/testBilling'
      , 'ByteSize': 100
      , 'TagsARNs': [ 'arn:aws:iam::012345678901:role/testBilling' ]
      , 'List': [ { 'Item': 'testItem' } ]
      , 'TestList': [ 'testItem1', 'testItem2' ]
      }


# Generated at 2022-06-12 23:12:12.316056
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test the function camel_dict_to_snake_dict converts a camelcased dict to snake_cased_dict
    """

    test_camel_dict = {
        'ACLID': 123456,
        'Tags': {
            'Tag1Key': "tag1value",
            'Tag2Key': "tag2value"
        },
        'HTTPEndpoint': {
            'Enabled': False
        }
    }

    test_snake_dict = {
        'a_c_l_i_d': 123456,
        'tags': {
            'Tag1Key': "tag1value",
            'Tag2Key': "tag2value"
        },
        'h_t_t_p_endpoint': {
            'enabled': False
        }
    }
    test_snake_

# Generated at 2022-06-12 23:12:20.682767
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        "stringProp": "string",
        "integerProp": 123456,
        "booleanProp": False,
        "nullProp": None,
        "dictProp": {
            "stringProp": "string",
            "integerProp": 123456,
            "booleanProp": False,
            "nullProp": None,
        },
        "listProp": [
            {
                "stringProp": "string",
                "integerProp": 123456,
                "booleanProp": False,
                "nullProp": None,
            },
            {
                "stringProp": "string",
                "integerProp": 123456,
                "booleanProp": False,
                "nullProp": None,
            },
        ],
    }


# Generated at 2022-06-12 23:12:31.113497
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict_1 = {
        "TargetGroupARNs": ["arn:a:b:c:d:e:f:g:h/i/j", "arn:a:b:c:d:e:f:g:h/i/k"],
        "TargetGroupARN": "arn:a:b:c:d:e:f:g:h/i/l",
        "Tags": {
            "Key": "Name",
            "Value": "service1"
        }
    }


# Generated at 2022-06-12 23:12:41.358896
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_data = {
        "h_t_t_p_endpoint": {
            "h_t_t_p_method": "h_t_t_p_method",
            "body": "body",
            "urlPath": "url_path",
            "timeoutInMillis": "timeout_in_millis",
            "authorizationValue": "authorization_value"
        }
    }

    test_result = {
        "HTTPEndpoint": {
            "HTTPMethod": "h_t_t_p_method",
            "Body": "body",
            "URLPath": "url_path",
            "TimeoutInMillis": "timeout_in_millis",
            "AuthorizationValue": "authorization_value"
        }
    }
    assert snake_dict_to_camel

# Generated at 2022-06-12 23:12:51.401299
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) == None
    assert recursive_diff({'a': 'b'}, {}) == ({'a': 'b'}, {})
    assert recursive_diff({'a': 'b'}, {'a': 'b'}) == None
    assert recursive_diff({'a': 'b'}, {'a': 'c'}) == ({'a': 'b'}, {'a': 'c'})
    assert recursive_diff({'a': {'b': 'inside1', 'c': 'inside2'}}, {'a': {'b': 'inside1'}}) == ({'a': {'c': 'inside2'}}, {'a': {}})

# Generated at 2022-06-12 23:13:00.006838
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Normal case
    result = camel_dict_to_snake_dict({
        'foo': '1',
        'barBaz': '2',
        'RC': '3',
        'httpEndpoint': '4',
        'pluralizedHttpEndpoints': '5',
        'InnerValue': '6',
        'innerDict': {
            'innerKey': '7',
            'innerHTTPEndpoint': '8'
        }
    })


# Generated at 2022-06-12 23:13:10.298532
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"Apple": "Banana", "CatDog": "Elephant"}) == {"apple": "Banana", "cat_dog": "Elephant"}
    assert camel_dict_to_snake_dict({"Apple": "Banana", "CatDog": "Elephant"}, True) == {"a_p_p_l_e": "Banana", "c_a_t_d_o_g": "Elephant"}

# Generated at 2022-06-12 23:13:30.420561
# Unit test for function recursive_diff
def test_recursive_diff():
    """The following values are expected to return corresponding output"""
    assert recursive_diff({}, {}) == None
    assert recursive_diff({'b': 1}, {}) == ({'b': 1}, {})
    assert recursive_diff({}, {'b': 1}) == ({}, {'b': 1})
    assert recursive_diff({'b': 1}, {'b': 1}) == None
    assert recursive_diff({'b': 1}, {'b': 2}) == ({'b': 1}, {'b': 2})
    assert recursive_diff({'a': 3, 'c': 2}, {'a': 3, 'b': 1}) == ({'c': 2}, {'b': 1})

# Generated at 2022-06-12 23:13:37.717858
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
      "HTTPEndpoint": {
        "Path": "/foo/{id}",
        "VpcLinkId": "id-1",
        "TimeoutInMillis": 200,
        "Tags": {
          "Key": "Value",
          "Key2": "Value2"
        }
      }
    }

    expected_result = {
      "h_t_t_p_endpoint": {
        "path": "/foo/{id}",
        "vpc_link_id": "id-1",
        "timeout_in_millis": 200,
        "tags": {
          "Key": "Value",
          "Key2": "Value2"
        }
      }
    }

    assert camel_dict_to_snake_dict(test_dict) == expected_result



# Generated at 2022-06-12 23:13:42.848532
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    This function checks the conversion of a simple camelized dict
    """
    camel_dict = {'HTTPEndpoint': {'UrlPath': '/foo'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)

    assert snake_dict == {u'h_t_t_p_endpoint': {u'url_path': u'/foo'}}



# Generated at 2022-06-12 23:13:54.240568
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': {
            'k4': 'v4',
            'k5': 'v5',
            'k6': {
                'k7': 'v7',
                'k8': 'v8',
                'k9': 'v9',
            }
        }
    }
    d2 = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': {
            'k4': 'v4',
            'k5': 'v5',
            'k6': {
                'k7': 'v7',
                'k8': 'v8',
                'k9': 'v99',
            }
        }
    }
   

# Generated at 2022-06-12 23:14:02.574861
# Unit test for function recursive_diff
def test_recursive_diff():
    diff = recursive_diff({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}},
                          {'b': 2, 'a': 1, 'c': {'e': 4, 'd': 3}})
    assert diff is None
    diff = recursive_diff({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}},
                          {'c': {'e': 4, 'd': 3}, 'b': 2, 'a': 1})
    assert diff is None

# Generated at 2022-06-12 23:14:12.102956
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        "description": "description of the group",
        "tags": {
            "type": "snapshots",
            "environment": "dev"
        },
        "volume_size": 10
    }

    dict2 = {
        "description": "description of the group",
        "tags": {
            "type": "snapshots",
            "environment": "prod"
        },
        "volume_size": 10
    }

    dict3 = {
        "description": "description of the group",
        "tags": {
            "type": "snapshots",
            "environment": "prod",
            "owner": "admin"
        },
        "volume_size": 10
    }


# Generated at 2022-06-12 23:14:21.924451
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"fooBar": "test", "fooBarBaz": 12}) == {"foo_bar": "test", "foo_bar_baz": 12}
    assert camel_dict_to_snake_dict({"fooBar": "test", "fooBarBaz": 12}, reversible=True) == {"h_t_t_p_endpoint": "test", "h_t_t_p_endpoint_baz": 12}
    assert camel_dict_to_snake_dict({"fooBar": "test", "fooBarBaz": 12}, True) == {"foo_bar": "test", "foo_bar_baz": 12}

# Generated at 2022-06-12 23:14:32.740849
# Unit test for function recursive_diff
def test_recursive_diff():
    # easy case
    left = {"a": 1, "b": "foo"}
    right = {"a": 2, "b": "foo"}
    result = recursive_diff(left, right)
    assert result == ({'a': 1}, {'a': 2})

    # nested dictionaries
    left = {"a": {"b": 1, "c": "foo"}, "d": 1, "e": "foo"}
    right = {"a": {"b": 2, "c": "foo"}, "d": 1, "e": "foo"}
    result = recursive_diff(left, right)
    assert result == ({'a': {'b': 1}}, {'a': {'b': 2}})

    # nested dictionaries

# Generated at 2022-06-12 23:14:40.234569
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'InstanceIds': ['i-0d53fa943611c92b8']}) == {'instance_ids': ['i-0d53fa943611c92b8']}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Endpoint': 'name'}}) == {'h_t_t_p_endpoint': {'endpoint': 'name'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Endpoint': 'name'}}, reversible=True) == {'h_t_t_p_endpoint': {'h_t_t_p_endpoint': 'name'}}

# Generated at 2022-06-12 23:14:50.330191
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) is None
    assert recursive_diff({'a': 1}, {}) == ({'a': 1}, {})
    assert recursive_diff({}, {'a': 1}) == ({}, {'a': 1})
    assert recursive_diff({'a': 1}, {'a': 1}) is None
    assert recursive_diff({'a': 1}, {'a': 1, 'b': 2}) == ({}, {'b': 2})
    assert recursive_diff({'a': 1, 'b': 2}, {'a': 1}) == ({'b': 2}, {})
    assert recursive_diff({'a': 1}, {'A': 1}) == ({'a': 1}, {'A': 1})

# Generated at 2022-06-12 23:15:03.597913
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "AutoScalingGroupName": "my-auto-scaling-group",
        "Tags": [
            {
                "ResourceId": "my-auto-scaling-group",
                "ResourceType": "auto-scaling-group",
                "Key": "foo",
                "Value": "bar",
                "PropagateAtLaunch": True
            },
            {
                "ResourceId": "my-auto-scaling-group",
                "ResourceType": "auto-scaling-group",
                "Key": "foo2",
                "Value": "bar2",
                "PropagateAtLaunch": True
            }
        ]
    }
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=False)

# Generated at 2022-06-12 23:15:11.875737
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Only test the camel to snake function, not the snake to camel function
    because it's not used in the current code base
    """

    camel_input = {'foo': 'bar', 'baz': 45.7, 'quux': [1, 2, 3], 'quuz': {'qux': 'quux'}}
    snake_output = {'foo': 'bar', 'baz': 45.7, 'quux': [1, 2, 3], 'quuz': {'qux': 'quux'}}
    assert camel_dict_to_snake_dict(camel_input) == snake_output

    camel_input = {'foo': {'bar': {'baz': 45.7}}}
    snake_output = {'foo': {'bar': {'baz': 45.7}}}
    assert camel_

# Generated at 2022-06-12 23:15:17.326451
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'fooBar': {}, 'fooBarBaz': {'barBaz': [{'baz': {}}], 'greetingsFoo': 'foo'}}
    test_dict = {'foo_bar': {}, 'foo_bar_baz': {'bar_baz': [{'baz': {}}], 'greetings_foo': 'foo'}}
    assert camel_dict_to_snake_dict(camel_dict) == test_dict



# Generated at 2022-06-12 23:15:26.740622
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"A": 1, "B": {"C": 2, "D": 3}, "E": [{"F": 4}, 5]}
    assert camel_dict_to_snake_dict(camel_dict) == {"a": 1, "b": {"c": 2, "d": 3}, "e": [{"f": 4}, 5]}
    camel_dict = {"Route": [{"RouteKey": "prefix-list-id", "RouteValue": "pl-92d8d6e7"}, {"RouteKey": "gateway-id", "RouteValue": "local"}]}

# Generated at 2022-06-12 23:15:37.337060
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:46.191286
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Unit test for camel_dict_to_snake_dict
    """

    def _assert_equals(test_case):
        camel_dict = test_case['camel_dict']
        snake_dict = test_case['snake_dict']
        reversible = test_case['reversible']

        result = camel_dict_to_snake_dict(camel_dict, reversible)
        assert (result == snake_dict)


# Generated at 2022-06-12 23:15:56.334984
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:05.322434
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Can also use pytest and pytest-cov
    # Returns test results and code coverage
    camel_dict = {'HTTPEndpoint': {'HTTPMethod': 'POST',
                                   'Protocols': ['HTTP', 'HTTPS']}}
    result = camel_dict_to_snake_dict(camel_dict)
    assert(result['http_endpoint']['http_method'] == 'POST')
    assert('protocols' in result['http_endpoint'])
    assert(len(result['http_endpoint']['protocols']) == 2)
    assert('http' in result['http_endpoint']['protocols'])

if __name__ == '__main__':
    test_camel_dict_to_snake_dict()

# Generated at 2022-06-12 23:16:12.930840
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_cases = []
    test_cases.append(({"DeviceName": "var"}, {"device_name": "var"}))
    test_cases.append(({"S3BucketName": "var"}, {"s3_bucket_name": "var"}))
    test_cases.append(({"HTTPEndpoint": "var"}, {"h_t_t_p_endpoint": "var"}))
    test_cases.append(({"HTTPEndpoint": "var", "HTTPPort": "80"},
                       {"h_t_t_p_endpoint": "var", "h_t_t_p_port": "80"}))
    test_cases.append(({"HTTPEndpoint": {"Port": "80"}},
                       {"h_t_t_p_endpoint": {"port": "80"}}))

# Generated at 2022-06-12 23:16:18.482292
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    tests = [
        ({}, {}),
        (
            {'key': 'value'},
            {'key': 'value'}),
        (
            {'key': {'another': 'value'}},
            {'key': {'another': 'value'}}),
        (
            {'key': {'Another': 'value'}},
            {'key': {'another': 'value'}}),
        (
            {'key': {'Another': 'value', 'Another2': 'value2'}},
            {'key': {'another': 'value', 'another2': 'value2'}})
    ]

    for test in tests:
        result = camel_dict_to_snake_dict(test[0])

# Generated at 2022-06-12 23:16:35.081350
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict1 = {
        "HTTPErrors": {
            "HTTPErrorCodeRanges": [
                {
                    "Min": '500',
                    "Max": '501'

                },
                {
                    "Min": '502',
                    "Max": '503'
                }
            ]
        }
    }

    dict2 = {
        "h_t_t_p_errors": {
            "h_t_t_p_error_code_ranges": [
                {
                    "min": '500',
                    "max": '501'

                },
                {
                    "min": '502',
                    "max": '503'
                }
            ]
        }
    }

    dict3 = camel_dict_to_snake_dict(dict1)
    assert dict2 == dict3

# Unit