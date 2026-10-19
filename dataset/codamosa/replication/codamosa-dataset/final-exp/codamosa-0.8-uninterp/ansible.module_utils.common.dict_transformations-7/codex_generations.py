

# Generated at 2022-06-12 23:06:53.677016
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'Key1': 'Value',
        'Key2': {
            'Subkey': 'Subvalue',
            'Subkey2': {
                'SubSubkey': 'SubSubvalue'
            }
        },
        'Key3': [1, 2, 3],
        'key4': 'foobar',
        'HTTPEndpoint': 'Value2',
        'HTTPEndpointNotRev': 'Value3',
        'HTTPEndpointCamelCase': 'Value4'
    }
    # Ensure non-reversible conversion is not affected by the reversible option

# Generated at 2022-06-12 23:07:04.514896
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:07:14.656206
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_object = {
        'HTTPEndpoint': {
            'EndpointType': 'HTTP',
            'Url': 'https://www.google.com'
        },
        'CustomEndpoint': {
            'EndpointType': 'CUSTOM',
            'Url': 'www.google.com',
            'SubscriptionList': [
                {
                    'Format': 'JSON',
                    'MatchingAttributes': [
                        {
                            'Key': 'my_key',
                            'Value': 'my_value'
                        },
                        {
                            'Key': 'your_key',
                            'Value': 'your_value'
                        }
                    ]
                }
            ]
        },
        'ApplicationId': 'test_application_id'
    }


# Generated at 2022-06-12 23:07:21.376550
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_data = {
        "HTTPEndpoint": "foo",
        "Tags": [],
        "DependentHTTPEndpoints": [
            {
                "Host": "bar",
                "HostHeader": "baz",
                "Protocol": "HTTPS",
                "ClientCA": "foobar"
            },
            {
                "Host": "bar2",
                "HostHeader": "baz2",
                "Protocol": "HTTPS"
            }
        ]
    }


# Generated at 2022-06-12 23:07:32.646147
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "Str": "x",
        "TopList": [
            {
                "One": "1",
                "Two": "2",
                "Three": "3",
                "Four": "4",
                "HTTPEndpoint": "http://example.com"
            }
        ],
        "Tags": [
            {
                "KeyOne": "KeyValueOne",
                "KeyTwo": "KeyValueTwo"
            }
        ],
        "TagSet": [
            {
                "Value": "TagValue",
                "Key": "TagKey"
            }
        ]
    }


# Generated at 2022-06-12 23:07:39.850976
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test recursive_diff function"""

    # Dictionaries are same
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    assert recursive_diff(dict1, dict2) is None

    # Dictionaries are different
    dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    dict2 = {'a': 1, 'b': {'c': 2, 'd': 4}}
    diff = recursive_diff(dict1, dict2)
    assert diff == ({'b': {'d': 3}}, {'b': {'d': 4}})

    # Value is different

# Generated at 2022-06-12 23:07:51.189347
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test snake_dict_to_camel_dict
    # Test that non-string values are untouched
    non_string_values = {
        'key1': 1,
        'key2': {
            'key2a': 2.0,
            'key2b': [{'key': 3}],
            'key2c': {'key': [4]}
        }
    }
    assert non_string_values == camel_dict_to_snake_dict(non_string_values)

    # Test that key, value gets transformed

# Generated at 2022-06-12 23:08:01.183469
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    x = {
        "ManagedPolicyArns": [
            "arn:aws:iam::aws:policy/AmazonS3FullAccess"
        ],
        "Path": "/",
        "GroupName": "test_ansible_group",
        "Arn": "arn:aws:iam::012345678901:group/test_ansible_group",
        "CreateDate": "2017-12-13T00:05:00Z",
        "GroupId": "AGPAJF76N6GZ7OIAJMB6U"
    }

    y = camel_dict_to_snake_dict(x, False, [])

    assert y['managed_policy_arns'] == [
            "arn:aws:iam::aws:policy/AmazonS3FullAccess"
        ]

# Generated at 2022-06-12 23:08:11.535726
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'foo': 'bar',
        'baz': {'qux': 'foo', 'mux': {'fiz': 'bux'}},
        'spam': 'eggs'
    }
    dict2 = {
        'foo': 'bar',
        'baz': {'qux': None, 'mux': {'fiz': 'bux'}},
        'sizzle': 'pop'
    }
    assert recursive_diff(dict1, dict2) == ({'baz': {'qux': 'foo'}}, {'baz': {'qux': None}, 'sizzle': 'pop'})


# Generated at 2022-06-12 23:08:22.040612
# Unit test for function recursive_diff
def test_recursive_diff():
    # A function to simulate the test cases
    # and print the output in a more human readable way.
    def run_tests(tests):
        # Iterate over test cases
        for test in tests:
            # Run the function
            result = recursive_diff(*test[0])
            # Assert the result
            if result == test[1]:
                print('Test passed: ' + str(test[0]) + ' => ' + str(result))
            else:
                print('Test failed: ' + str(test[0]) + ' => ' + str(test[1]) + ' != ' + str(result))

    # Test cases
    # Test with two dictionaries

# Generated at 2022-06-12 23:08:36.323084
# Unit test for function dict_merge
def test_dict_merge():

    assert dict_merge({'a': 'A', 'b': 'B'}, {'b': 'C', 'd': 'D'}) == {'a': 'A', 'b': 'C', 'd': 'D'}
    assert dict_merge({'a': 'A', 'b': {'b': 'B'}}, {'b': {'c': 'C', 'd': 'D'}, 'd': 'E'}) == {'a': 'A', 'b': {'b': 'B', 'c': 'C', 'd': 'D'}, 'd': 'E'}
    assert dict_merge({'a': 'A', 'b': [{'b': 'B'}]}, {'b': [{'c': 'C', 'd': 'D'}], 'd': 'E'})

# Generated at 2022-06-12 23:08:46.477890
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'foo': 'bar', 'int': 1, 'dict': {'foo': 'bar'}}
    dict2 = {'foo': 'bar2', 'int': 1, 'dict': {'foo': 'bar'}}
    dict3 = {'int': 1, 'dict': {'foo': 'bar'}}
    dict4 = {'foo': 'bar', 'int': 1, 'dict': {'foo': 'bar2'}}
    dict5 = {'foo': 'bar', 'int': 1, 'dict': {'foo': 'bar'}}
    dict6 = {'foo': 'bar', 'int': 1, 'dict': {'foo': 'bar', 'bar': 'foo'}}

# Generated at 2022-06-12 23:08:52.914395
# Unit test for function dict_merge
def test_dict_merge():
    a = dict(
        age=1,
        size=dict(
            height=1,
            width=2,
            ),
        )
    b = dict(
        age=1,
        size=dict(
            height=1,
            depth=2,
            ),
        )
    result = dict_merge(a, b)
    assert result == {'age': 1, 'size': {'height': 1, 'depth': 2, 'width': 2}}

# Generated at 2022-06-12 23:08:59.281064
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    dict1 = {'HTTPEndpoint': {'method': 'GET', 'path': '/path', 'port': 80, 'protocol': 'HTTP'},
             'HTTPSEndpoint': {'method': 'GET', 'path': '/path', 'port': 443, 'protocol': 'HTTPS'},
             'TargetGroupArns': ['arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067',
                                 'arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-other-targets/b7d98fbd90e8380c'],
             'Tags': [{'Key': 'random_tag', 'Value': 'random_value'}]}

# Generated at 2022-06-12 23:09:07.781340
# Unit test for function dict_merge
def test_dict_merge():
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    expected_result = {
        'first':
        {
            'all_rows':
            {
                'pass': 'dog',
                'fail': 'cat',
                'number': '5'
            }
        }
    }

    # Function under test
    result = dict_merge(a, b)

    assert result == expected_result


# Generated at 2022-06-12 23:09:18.590610
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge({}, {}) == {}
    assert dict_merge({}, {'foo': 'bar'}) == {'foo': 'bar'}
    assert dict_merge({'foo': 'bar'}, {}) == {'foo': 'bar'}
    assert dict_merge({'foo': 'bar'}, {'baz': 'tan'}) == {'foo': 'bar', 'baz': 'tan'}
    assert dict_merge({'foo': {'bar': 'baz'}}, {}) == {'foo': {'bar': 'baz'}}
    assert dict_merge({}, {'foo': {'bar': 'baz'}}) == {'foo': {'bar': 'baz'}}

# Generated at 2022-06-12 23:09:26.238331
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from ansible.module_utils.aws.core import AnsibleAWSModule

    # Test that simple dictionary is converted correctly
    camel_dict = {
        'Bucket': 'mybucket',
        'Key': 'mykey',
        'Body': 'Very secret data.',
        'ACL': 'private'
    }
    snake_dict = {
        'acl': 'private',
        'body': 'Very secret data.',
        'bucket': 'mybucket',
        'key': 'mykey'
    }
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

    # Test that camel-case list is converted correctly

# Generated at 2022-06-12 23:09:36.518113
# Unit test for function dict_merge
def test_dict_merge():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'a': 2, 'd': 4, 'e': 5}
    d3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    assert dict_merge(d1, d2) == d3
    d1 = {'a': {'b': {'c': 1}}}
    d2 = {'a': {'b': {'d': 2}}}
    d3 = {'a': {'b': {'c': 1, 'd': 2}}}
    assert dict_merge(d1, d2) == d3
    d1 = {'a': {'b': {'d': 2}}}

# Generated at 2022-06-12 23:09:40.593527
# Unit test for function dict_merge
def test_dict_merge():

    assert dict_merge({'a': 1, 'b': {'c': 2}}, {'b': {'d': 3}, 'e': 4}) == \
        {'a': 1, 'b': {'d': 3, 'c': 2}, 'e': 4}

# Generated at 2022-06-12 23:09:49.480012
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Base case
    assert camel_dict_to_snake_dict({"HTTPEndpoint": {}}) == {"http_endpoint": {}}

    # Nested case
    assert camel_dict_to_snake_dict({"HTTPEndpoint": {"Foo": "bar"}}) == {"http_endpoint": {"foo": "bar"}}

    # Reverse case
    assert camel_dict_to_snake_dict({"HTTPEndpoint": {"Foo": "bar"}}, reversible=True) == {"h_t_t_p_endpoint": {"foo": "bar"}}

    # Ignore list case

# Generated at 2022-06-12 23:10:00.157290
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:09.450309
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) is None
    assert recursive_diff({'a': 'b'}, {'a': 'b'}) is None
    assert recursive_diff({'a': 1, 'b': '2'}, {'a': 1, 'b': '2'}) is None
    assert recursive_diff({'a': {'b': 'c'}}, {'a': {'b': 'c'}}) is None

    assert recursive_diff({'a': 1}, {'a': 'b'}) == ({'a': 1}, {'a': 'b'})
    assert recursive_diff({'a': 1, 'b': '2'}, {'a': 1}) == ({'b': '2'}, None)

# Generated at 2022-06-12 23:10:15.755420
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(
        FooBar = dict(
            Baz = 'Buz',
            Boom = [
                dict(Bap = 'Bang'),
                dict(Bap = 'Bing'),
            ]
        ),
    )
    snake_dict = dict(
        foo_bar = dict(
            baz = 'Buz',
            boom = [
                dict(bap = 'Bang'),
                dict(bap = 'Bing'),
            ],
        ),
    )
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict



# Generated at 2022-06-12 23:10:26.937817
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from ansible.module_utils.basic import AnsibleModule
    am = AnsibleModule({})

    assert camel_dict_to_snake_dict({'Foo': 1, 'BarBaz': 2}) == {'foo': 1, 'bar_baz': 2}
    assert camel_dict_to_snake_dict({'HTTPRetryCount': 1}) == {'http_retry_count': 1}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 1}) == {'h_t_t_p_endpoint': 1}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 1}, reversible=True) == {'h_t_t_p_endpoint': 1}

# Generated at 2022-06-12 23:10:36.778787
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test conversion of a simple dictionary
    camel_dict = {
        "aBc": 1,
        "dEf": 2
    }
    expected = {
        "a_bc": 1,
        "d_ef": 2,
    }
    result = camel_dict_to_snake_dict(camel_dict, False)
    assert result == expected

    # Test conversion of a dictionary of nested dictionaries
    camel_dict = {
        "abc": 1,
        "def": 2,
        "ghi": {
            "jKl": 3,
            "Mn0": 4,
            "pQr": {
                "stu": 5,
            }
        }
    }

# Generated at 2022-06-12 23:10:45.877832
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test a dict with primitive values
    dict_http_endpoint = {
        "HTTPEndpointId": "testid",
        "URL": "https://test.com"
    }

    expected_dict_http_endpoint = {
        "h_t_t_p_endpoint_id": "testid",
        "url": "https://test.com"
    }

    assert camel_dict_to_snake_dict(dict_http_endpoint) == expected_dict_http_endpoint

    # Test a dict with complex values
    dict_tags = {
        "Tags": [
            {
                "Key": "Environment",
                "Value": "development"
            },
            {
                "Key": "Project",
                "Value": "xray"
            }
        ]
    }

    expected_

# Generated at 2022-06-12 23:10:54.363971
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'tags': [{
            'key': 'foo',
            'value': 'bar'
        }],
        'fooBar': 'buzz'}
    camel_dict_with_tags_fixed = {
        'tags': [{
            'Key': 'foo',
            'Value': 'bar'
        }],
        'fooBar': 'buzz'}

    assert camel_dict_to_snake_dict(camel_dict) == {'foo_bar': 'buzz', 'tags': [{'key': 'foo', 'value': 'bar'}]}
    assert camel_dict_to_snake_dict(camel_dict_with_tags_fixed) == {'foo_bar': 'buzz', 'tags': [{'Key': 'foo', 'Value': 'bar'}]}

# Generated at 2022-06-12 23:11:02.666686
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    class _ObjectWithCamelCaseMethod(object):

        def camelCaseMethod(self):
            pass

        def _camelCaseMethod(self):
            pass

        def CamelCaseMethod(self):
            pass

    def test():
        dict1 = dict(SomeKey=dict(CamelCaseKey=dict(Foo="Bar")), SomeOtherKey=42,
                     _someOtherKey=dict(CamelCaseKey=dict(foo="bar")),
                     SomeList=[dict(CamelCaseKey="foo")])
        dict2 = dict(some_key=dict(camel_case_key=dict(foo="Bar")), some_other_key=42,
                     some_list=[dict(camel_case_key="foo")])

# Generated at 2022-06-12 23:11:12.779469
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'a': 1, 'b': 2, 'c': {'d': 3}}
    dict2 = {'a': 1, 'b': 2, 'c': {'d': 3}}
    dict3 = {'a': 1, 'b': 2, 'c': {'d': 4}}
    dict4 = {'a': 1, 'b': {'d': 4}}
    dict5 = dict4.copy()
    dict5['b'] = dict1['b']
    dict6 = dict4.copy()
    dict6['b'] = dict2['b']
    dict7 = dict4.copy()
    dict7['b'] = dict3['b']

    assert recursive_diff(dict1, dict2) is None

# Generated at 2022-06-12 23:11:23.254416
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff"""
    test1_dict1 = dict(test1=dict(a=1, b=2, c=dict(d=3, e=4)),
                       test2=dict(f=5, g=6, h=dict(i=7, j=8)))
    test1_dict2 = dict(test1=dict(a=11, b=2, c=dict(d=3, e=4)),
                       test2=dict(f=5, g=6, h=dict(i=7, j=8)))
    test1_expected = dict(test1=dict(a=1), test2=dict())


# Generated at 2022-06-12 23:11:35.794671
# Unit test for function recursive_diff
def test_recursive_diff():
    import unittest
    class MyTestCase(unittest.TestCase):
        def test_recursive_diff(self):
            dict1 = dict(key1="value1", key2=dict(key3="value3"), key4=dict(key5="value5"))
            dict2 = dict(key1="value1", key2=dict(key3="value3"), key4=dict(key5="value5"))
            self.assertEqual(None, recursive_diff(dict1, dict2))

            dict1 = dict(key1="value1", key2=dict(key3="value3"), key4=dict(key5="value5"))
            dict2 = dict(key1="value1", key2=dict(key3="value3"), key4=dict(key5="value5"), key6="value6")
           

# Generated at 2022-06-12 23:11:43.968815
# Unit test for function recursive_diff
def test_recursive_diff():
    "Provide unit test for function recursive_diff."

    # Test that function returns a tuple of the differences.
    def assertDiff(diff, expected_result):
        assert diff == expected_result
        assert type(diff) is tuple

    # Test that function raises an exception for improper type.
    def assertRaises(expected_msg):
        try:
            recursive_diff(dict1, dict2)
        except TypeError as e:
            assert str(e) == expected_msg

    # Test for different values at the same key.
    dict1 = {'key1': 'val1', 'key2': 'val2'}
    dict2 = {'key1': 'val1', 'key2': 'val3'}
    expected_diff = ({}, {'key2': 'val3'})

# Generated at 2022-06-12 23:11:53.108233
# Unit test for function recursive_diff
def test_recursive_diff():
    import json

    json1 = json.loads("""{
            "name": "test-vpc-recursive-diff",
            "cidrBlock": "10.0.19.0/24",
            "enableDnsHostnames": true,
            "enableDnsSupport": true,
            "instanceTenancy": "default",
            "tags": {
                "Name": "test-vpc-recursive-diff"
            }
        }""")


# Generated at 2022-06-12 23:12:01.668077
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:11.390649
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'KeyName': 'value', 'SomeKeyName': 'some_value',
                  'aVPC': {'AvailZone': 'us-east-1a', 'InternetGatewayId': 'igw-654321',
                           'Subnet': {'Id': 'subnet-123456', 'AvailabilityZone': 'us-east-1a'}},
                  'FooBar': 'BarFoo',
                  'Foo': None,
                  'Bar': ['1', 2, '3'],
                  'Baz': {'BazBaz': [{'BazBazBaz': '1'}]},
                  'BazBaz': 'BarBar'}


# Generated at 2022-06-12 23:12:20.036723
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # test with reversible true
    simple_dict = {"testKey1": "testValue1", "testKey2": ["testValue2", "testValue3"], "testKey3": "testValue4"}
    assert camel_dict_to_snake_dict(simple_dict, reversible=True) == {'test_key1': 'testValue1', 'test_key2': [
        'testValue2', 'testValue3'], 'test_key3': 'testValue4'}

    complex_dict = {"testKey1": "testValue1", "testKey2": [{"innerTestKey1": ["testValue2", "testValue3"]}, "testValue4"], "testKey3": {"innerTestKey2": "testValue5"}}

# Generated at 2022-06-12 23:12:30.314349
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:40.669414
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'foo': 1,
                 'bar': 2,
                 'Tags': {'key1': 'value1', 'key2': 'value2'},
                 'baz': [{'a': {'HTTPEndpoint': 'X'}}, {'b': {'HTTPEndpoint': 'Y'}}],
                 'things': {'subDict': {'subSubDict': {'subSubKey': 'subvalue', 'subSubKey2': 'subvalue2'}}}}
    result = camel_dict_to_snake_dict(test_dict)

    assert 'foo' in result
    assert 'bar' in result
    assert 'tags' in result
    assert 'baz' in result
    assert 'things' in result

# Generated at 2022-06-12 23:12:50.336525
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {
        'a': 'a',
        'b': {
            'c': 'c',
            'd': 'd',
        },
        'e': 'a',
    }

    d2 = {
        'a': 'a',
        'b': {
            'c': 'c',
            'd': 'b',
        },
        'f': 'a',
    }

    d3 = {
        'a': 'a',
        'b': {
            'c': 'c',
            'd': 'd',
        },
        'e': 'a',
    }

    expected_result1 = (
        {'b': {'d': 'd'}},
        {'b': {'d': 'b'}},
    )

# Generated at 2022-06-12 23:12:59.278420
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'camelCase': 'foo'}) == {'camel_case': 'foo'}
    assert camel_dict_to_snake_dict({'camelCase': 'foo'}, True) == {'camel_c_a_s_e': 'foo'}
    assert camel_dict_to_snake_dict({'camel2Case': 'foo'}) == {'camel2_case': 'foo'}
    assert camel_dict_to_snake_dict({'camel2Case': 'foo'}, True) == {'camel2_c_a_s_e': 'foo'}

# Generated at 2022-06-12 23:13:13.572475
# Unit test for function recursive_diff
def test_recursive_diff():
    d = {
        "foo": 1,
        "bar": {
            "a": 1,
            "b": 2,
            "c": {
                "foo": 1,
                "bar": 1,
                "baz": 3
            }
        },
        "baz": 2
    }
    e = {
        "foo": 1,
        "bar": {
            "a": 1,
            "b": 2,
            "c": {
                "foo": 1,
                "bar": 3,
                "baz": 4
            }
        },
        "baz": 2
    }

# Generated at 2022-06-12 23:13:17.833116
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # This function tests the function camel_dict_to_snake_dict()
    test_cases = [
        # test_case, expected_output
        [{"keyName": "myKey"}, {"key_name": "myKey"}],
        [{"keyName": "myKey", "Tags": [{"keyName2": "myKey2"}]}, {"key_name": "myKey", "tags": [{"keyName2": "myKey2"}]}],
    ]
    for test_case, expected_output in test_cases:
        output = camel_dict_to_snake_dict(test_case)
        assert output == expected_output



# Generated at 2022-06-12 23:13:28.724395
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    good_case = {'SubnetIds': ['subnet-897d0b9e', 'subnet-b85d0bc7', 'subnet-c17d0bdc', 'subnet-324745af', 'subnet-0db445c1'], 'ResponseMetadata': {'RequestId': '2e090ffb-a9b6-11e8-a534-63e6acf98fed', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'text/xml', 'date': 'Wed, 29 Aug 2018 15:12:10 GMT', 'server': 'AmazonEC2', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding'}, 'RetryAttempts': 0}, 'VpcIds': ['vpc-cd8a78a0']}



# Generated at 2022-06-12 23:13:36.286057
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = dict()
    camel_dict['Name'] = '_'
    camel_dict['HTTPEndpoint'] = '_'
    camel_dict['Attributes'] = dict()
    camel_dict['Attributes']['aws:elb:healthcheck:target'] = 'HTTP:80'
    camel_dict['Attributes']['Key2'] = 'Value2'
    camel_dict['Tags'] = [{
        'Key': 'Key1',
        'Value': 'Value1'
    }, {
        'Key': 'Key2',
        'Value': 'Value2'
    }]
    camel_dict['Tags'].append(dict())

    expected_dict = dict()
    expected_dict['name'] = '_'
    expected_dict['h_t_t_p_endpoint'] = '_'
   

# Generated at 2022-06-12 23:13:45.159804
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {
        'a': 'b',
        'c': {
            'd': 'e',
            'f': {
                'g': 'h'
            },
            'list': [
                {
                    'i': 'j',
                    'k': 'l'
                }
            ]
        }
    }

    snake = camel_dict_to_snake_dict(camel)

    assert snake['a'] == 'b'
    assert snake['c']['d'] == 'e'
    assert snake['c']['f']['g'] == 'h'
    assert snake['c']['list'][0]['i'] == 'j'
    assert snake['c']['list'][0]['k'] == 'l'



# Generated at 2022-06-12 23:13:55.634203
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Test camel_dict_to_snake_dict function"""

    # This dictionary is taken from the docs
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_internet_gateways
    # -snip-
    # 'Tags': [
    #     {'Key': 'string', 'Value': 'string'},
    # ],
    # 'Attachments': [
    #     {
    #         'VpcId': 'string',
    #         'State': 'attaching'|'attached'|'detaching'|'detached'
    #     },
    # ],
    # -snip-
    #
    # This is camelCase. We want to test that the Values in Tags and
    # Attach

# Generated at 2022-06-12 23:14:03.568566
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(camel_dict={
        'Test': 1,
        'Camel': 2,
        'Dict': {
            'Test': 1,
            'Camel': 2
        },
        'List': [
            1,
            '2'
        ]
    }) == {
        'test': 1,
        'camel': 2,
        'dict': {
            'test': 1,
            'camel': 2
        },
        'list': [
            1,
            '2'
        ]
    }


# Generated at 2022-06-12 23:14:13.884621
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:18.872013
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'subnet0': {'subnet1': {
            'subnet2': {
                'subnet3': 'subnet3'
            }
        }},
        'subnet4': {
            'subnet5': 'subnet'
        },
        'subnet6': [{
            'subnet7': {
                'subnet8': 'subnet8'
            }
        }],
        'subnet9': [
            'subnet9'
        ],
        'subnet10': [],
        'subnet11': [{
            'subnet12': {
                'subnet13': [{
                    'subnet14': []
                }]
            }
        }]
    }


# Generated at 2022-06-12 23:14:28.539780
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test key transform
    assert _camel_to_snake("TestKey") == "test_key"
    assert _camel_to_snake("_TestKey") == "_test_key"
    assert _camel_to_snake("Test_key") == "test_key"
    assert _camel_to_snake("Test_key_") == "test_key_"
    assert _camel_to_snake("test_key") == "test_key"
    assert _camel_to_snake("test_key_") == "test_key_"
    assert _camel_to_snake("test__key") == "test___key"
    assert _camel_to_snake("testkey") == "testkey"
    # Test that reversible options avoids overlowering
    assert _camel

# Generated at 2022-06-12 23:14:46.918036
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:57.004076
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test conversion of simple camelized key and value
    test_dict = {'KeyName': 'mysshkey'}
    expected_dict = {'key_name': 'mysshkey'}
    result = camel_dict_to_snake_dict(test_dict)
    assert result == expected_dict, 'key not converted to snake case'

    # Test conversion of camelized key with capital letters
    test_dict = {'HTTPEndpoint': 'http://www.amazon.com'}
    expected_dict = {'h_t_t_p_endpoint': 'http://www.amazon.com'}
    result = camel_dict_to_snake_dict(test_dict)
    assert result == expected_dict, 'key not converted to snake case'

    # Test conversion of camelized value

# Generated at 2022-06-12 23:15:05.932679
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test simple cases
    assert _camel_to_snake('CamelCase') == 'camel_case'
    assert _camel_to_snake('HTTPSEndpoint') == 'https_endpoint'
    assert _camel_to_snake('EndPoint') == 'end_point'
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_ar_ns'
    assert _camel_to_snake('TargetGroupARNs', reversible=True) == 'target_group_a_r_ns'

    # Test dictionary case - casing

# Generated at 2022-06-12 23:15:13.451944
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test for both dictionaries are the same
    d1 = {"a": 1, "b": 2}
    d2 = {"a": 1, "b": 2}
    assert recursive_diff(d1, d2) == None

    # Test for no intersection of keys
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    assert recursive_diff(d1, d2) == ({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

    # Test for intersection of keys and values are the same
    d1 = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    d2 = {"b": 2, "c": {"d": 3, "e": 4}, "f": 5}

# Generated at 2022-06-12 23:15:21.131410
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:15:32.052903
# Unit test for function recursive_diff
def test_recursive_diff():
    complex_dict = {
        "key1": 1,
        "key2": "str",
        "key3": [1, 2, 3],
        "key4": {"key5": 1},
        "key6": "str",
        "key7": [1, 2, 3, 4],
        "key8": {"key5": 1, "key9": 123},
    }
    complex_dict1 = {
        "key1": 1,
        "key2": "str",
        "key3": [1, 2, 3],
        "key4": {"key5": 1},
        "key6": "str",
        "key7": [1, 2, 3, 4],
        "key8": {"key5": 1, "key9": 123},
    }

# Generated at 2022-06-12 23:15:42.031721
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:15:49.564481
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'sub': {
            'subsub': {
                'camelWord': 'foo',
                'camelUPPER': 'bar',
                'subsubsub': {
                    'HTTPEndpoint': 'baz',
                    'Subkey': 'spam',
                    'SubkeyConvert': {
                        'Subsubkey': 'ham',
                        'Subsubkey2': 'eggs'
                    }
                },
                'Tags': {
                    'Tag': 'value'
                }
            }
        }
    }

# Generated at 2022-06-12 23:15:59.410380
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:06.125117
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        {
            'a': 1,
            'b': 2,
            'cD': 3,
            'SubDict': {
                'a': 1,
                'b': 2,
                'cD': 3,
            }
        },
    ) == {
        'a': 1,
        'b': 2,
        'c_d': 3,
        'sub_dict': {
            'a': 1,
            'b': 2,
            'c_d': 3,
        }
    }



# Generated at 2022-06-12 23:16:23.764061
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    original_dict = {
        'NetworkInterfaces': [
            {
                'MacAddress': "ab:cd:ef:00:01:02",
                'PrivateIpAddress': "10.2.3.4"
            }
        ],
        'NotificationConfigurations': [
            {
                'TopicARN': "arn:aws:sns:us-east-1:123456789012:some-topic",
                'NotificationTopicARN': "arn:aws:sns:us-east-1:123456789012:some-topic",
                'TopicStatus': "active"
            }
        ],
        'Tags': {
            'Key': 'Value',
            'AnotherKey': 'AnotherValue'
        }
    }


# Generated at 2022-06-12 23:16:32.854317
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test recursive_diff function"""
    i = {
        'a': [1, 2, 3],
        'b': [4, 5, 6],
    }
    v = {
        'a': [1, 2, 3],
        'b': [4, 5, 7],
    }
    r = [
        {'b': [6]},
        {'b': [7]}
    ]
    assert recursive_diff(i, v) == r
    i = {
        'a': {
            'b': [1, 2],
            'c': [3, 4]
        }
    }
    v = {
        'a': {
            'b': [1, 3],
            'c': [3, 4]
        }
    }