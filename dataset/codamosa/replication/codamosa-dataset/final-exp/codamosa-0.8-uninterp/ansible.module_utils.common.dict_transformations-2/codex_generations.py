

# Generated at 2022-06-12 23:06:50.088437
# Unit test for function dict_merge
def test_dict_merge():
    # No error if empty dicts
    dict_merge({},{})

    # Both simple dicts
    assert dict_merge({'a':1, 'b':2}, {'a':2, 'c':3}) == {'a':2, 'b':2, 'c':3}

    # Nested dicts
    assert dict_merge({'a': {'a1':1}, 'b':2}, {'a': {'a1':2, 'a2':3}, 'c':3}) == \
        {'a': {'a1':2, 'a2':3}, 'b':2, 'c':3}

    # Deeply nested dicts

# Generated at 2022-06-12 23:07:00.968692
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    source = {
            'HTTPEndpoint': {
                'HTTPMethod': 'POST',
                'URL': 'https://example.com/',
                'AccessToken': '*'
                },
            'InsufficientData': [
                'StatusCheckFailed',
                'StatusCheckFailed_Instance'
                ],
            'OK': [
                'StatusCheckFailed_System'
                ]
            }

    case_sensitive_ignore_list = [
            'Tags',
            'Dimensions'
            ]

    camel_dict = deepcopy(source)
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    new_camel_dict = snake_dict_to_camel_dict(snake_dict)

    assert new_camel_dict == source

    # The original

# Generated at 2022-06-12 23:07:07.105216
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'abc'}, True) == {'h_t_t_p_endpoint': 'abc'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'abc'}, False) == {'http_endpoint': 'abc'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'abc'}) == {'http_endpoint': 'abc'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'foo': 'bar'}}) == {'http_endpoint': {'foo': 'bar'}}

# Generated at 2022-06-12 23:07:16.813683
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge(dict(a=1, b=dict(b1=1, b2=2, b3=3), c=3),
                      dict(a=2, b=dict(b1=2, b2=2, b5=5), d=5)) == \
        dict(a=2, b=dict(b1=2, b2=2, b3=3, b5=5), c=3, d=5)

# Generated at 2022-06-12 23:07:27.879733
# Unit test for function recursive_diff
def test_recursive_diff():
    from collections import OrderedDict
    assert(recursive_diff({}, {}) is None)
    assert(recursive_diff({1: None}, {1: None}) is None)
    assert(recursive_diff({1: {2: 3}}, {1: {2: 3}}) is None)

    # Expected behavior for missing key
    assert(recursive_diff({1: {3: 4}}, {1: {2: 3}}) == ({1: {3: 4}}, {1: {2: 3}}))
    assert(recursive_diff({1: {2: 3}}, {1: {}}) == ({1: {2: 3}}, {1: {}}))

# Generated at 2022-06-12 23:07:36.483662
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
      'google': 'cloud',
      'foo_bar': {
        'baz_qux': 123,
        'big_bang': [
          'fred',
          {
            'john': 'smith'
          }
        ]
      },
      'my_list': [
        'list1',
        {
          'my_dict': {
            'item1': 'value1',
            'item2': ['value2', 'value3']
          }
        },
        'list2'
      ],
      'tags': {
        'Name': 'ansible',
        'Application': 'webserver'
      }

    }


# Generated at 2022-06-12 23:07:43.854545
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test module for camel_dict_to_snake_dict
    """

# Generated at 2022-06-12 23:07:54.894017
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert(
        camel_dict_to_snake_dict({"aB": "cd"}, False) ==
        {"a_b": "cd"})
    assert(
        camel_dict_to_snake_dict({"aB": {"cD": "ef"}}, False) ==
        {"a_b": {"c_d": "ef"}})
    assert(
        camel_dict_to_snake_dict({"aB": [{"cD": "ef"}]}, False) ==
        {"a_b": [{"c_d": "ef"}]})
    assert(
        camel_dict_to_snake_dict({"aB": [{"aB": "ef"}]}, False) ==
        {"a_b": [{"a_b": "ef"}]})

# Generated at 2022-06-12 23:08:03.835028
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:08:14.424600
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test case 1
    camel_dict = {
        'a': 'Test',
        'b': {
            'c': 'Test',
        },
    }
    expected_snake_dict = {
        'a': 'Test',
        'b': {
            'c': 'Test',
        },
    }
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert expected_snake_dict == snake_dict

    # Test case 2
    camel_dict = {
        'a': 'Test',
        'b': {
            'c': 'Test',
        },
    }
    expected_snake_dict = {
        'a': 'Test',
        'b': {
            'c': 'Test',
        },
    }
    snake_dict = camel

# Generated at 2022-06-12 23:08:26.247122
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "HealthCheckPath": "/",
            "TimeoutSeconds": 30,
            "UnhealthyThresholdCount": 3
        },
        "PortMappings": [{
            "ContainerPort": 80,
            "HostPort": 80,
            "Protocol": "tcp"
        }],
        "Volumes": [],
        "WorkingDirectory": ""
    }


# Generated at 2022-06-12 23:08:35.894083
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:45.947245
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({'a': 'x'}, {'b': 'x'}) == ({'a': 'x'}, {'b': 'x'})
    assert recursive_diff({'a': 'x'}, {'a': 'x'}) is None
    assert recursive_diff({'a': 'x'}, {'a': 'y'}) == ({'a': 'x'}, {'a': 'y'})
    assert recursive_diff({'a': 'x'}, {'a': 'y', 'b': 1, 'c': None}) == ({'a': 'x'}, {'a': 'y', 'b': 1, 'c': None})

# Generated at 2022-06-12 23:08:53.997725
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({
        'InstanceType': 't2.micro',
        'Tags': {
            'Name': 'test',
            'Owner': 'test-owner'
        },
        'HTTPEndpoint': {
            'Enabled': True
        }
    }) == {
        'instance_type': 't2.micro',
        'tags': {
            'Name': 'test',
            'Owner': 'test-owner'
        },
        'h_t_t_p_endpoint': {
            'enabled': True
        }
    }



# Generated at 2022-06-12 23:09:01.448089
# Unit test for function recursive_diff
def test_recursive_diff():
    # First test case
    dict1 = {'a' : {'b' : 1, 'c' : 2}, 'de': ['foo', 'bar'], 'fg': 'Hello'}
    dict2 = {'a' : {'b' : 2, 'c' : 2}, 'de': 'fobar', 'fg': ['Hello', 'World']}
    expected_result = ({'a' : {'b': 1}, 'de': ['foo', 'bar'], 'fg': 'Hello'},
                       {'a' : {'b': 2}, 'de': 'fobar', 'fg': ['Hello', 'World']})
    result = recursive_diff(dict1, dict2)
    assert result == expected_result, "Unexpected result when comparing two dictionaries"
    # Second test case
    dict1 = {}

# Generated at 2022-06-12 23:09:12.535052
# Unit test for function recursive_diff
def test_recursive_diff():

    def _test_data(left, right):
        """Test data for recursive_diff

        :arg left: Dict to compare against.
        :arg right: Dict to compare with ``left``.
        :return: Expeted value from ``recursive_diff``.
        """

        return recursive_diff(left, right)

    assert _test_data({}, {}) is None

    assert _test_data(left={'a': 'a'}, right={'b': 'b'}) == ({'a': 'a'}, {'b': 'b'})

    assert _test_data(left={'a': 'a'}, right={'a': 'b'}) == ({'a': 'a'}, {'a': 'b'})


# Generated at 2022-06-12 23:09:21.884841
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_dict"""

    import json

    dict1 = {
        'test': 'example',
        'test2': {
            'key': 'value'
        }
    }
    dict2 = {
        'test': 'example',
        'test2': {
            'key': 'value',
            'key2': 'value2'
        }
    }
    expected_result = json.loads('[{"test2": {"key2": null}}, {"test2": {"key2": "value2"}}]')
    result = recursive_diff(dict1, dict2)
    if result != expected_result:
        raise AssertionError('Function recursive_diff return wrong result %s instead of %s' % (result, expected_result))

# Generated at 2022-06-12 23:09:31.174131
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'Tags': {
            'Name': 'foo',
            'Bar': 'baz'
        },
        'TestBool': True,
        'TestInt': 0,
        'TestFloating': 1.0,
        'TestString': 'test',
        'TestList': [1, 2, 3, 4],
        'TestDict': {
            'AnotherTest': 'test'
        },
        'SomeAttr': {
            'AnotherAttr': {
                'NestedAttr': 'test'
            }
        }
    }


# Generated at 2022-06-12 23:09:41.844668
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # GIVEN: A dictionary of mixed case keys, lists and nested dictionaries
    camel_data = {
        "HTTPEndpoint": {
            "BooleanMember": True,
            "StringMember": "string",
            "NestedStructure": {
                "list": [
                    "third",
                    "fourth"
                ],
                "nested": {
                    "fifth": "fifth"
                }
            },
            "ListMember": [
                "first",
                "second"
            ],
            "DoubleMember": 1.2
        },
        "Tags": {
            "MyInstance": "my_instance",
            "MyProject": "my_project"
        }
    }

    # WHEN: Converting to snake_case

# Generated at 2022-06-12 23:09:49.797694
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "k1": "Value 1",
        "k2": "Value 2",
        "k3": [
            {
                "k4": {
                    "k5": "Value 5"
                },
                "k6": "Value 6"
            }
        ]
    }
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict['k1'] == 'Value 1'
    assert snake_dict['k2'] == 'Value 2'
    assert snake_dict['k3'][0]['k4']['k5'] == "Value 5"
    assert snake_dict['k3'][0]['k6'] == "Value 6"



# Generated at 2022-06-12 23:10:01.683173
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'aBcDef': {'GhI': 'Jkl'}, 'MnoPqrStu': [{'VwXyZ': 'aBcDeFgH'}, {'IjKlMnOpQrSt': 'UvWxYz'}],
                  'VwXyZ': 'aBcDeFgH'}
    snake_dict = camel_dict_to_snake_dict(camel_dict)


# Generated at 2022-06-12 23:10:11.444508
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) == None
    assert recursive_diff({'a': {}}, {'a': {}}) == None
    assert recursive_diff({'a': {'b': {}}}, {'a': {'b': {}}}) == None
    assert recursive_diff({'a': {'b': {'c': 1}}}, {'a': {'b': {'c': 1}}}) == None
    # None in this context means no difference
    assert recursive_diff({'a': 1}, {'a': 1}) == None
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2})
    assert recursive_diff({'a': {'b': 1}}, {'a': {'b': 1}}) == None

# Generated at 2022-06-12 23:10:21.784815
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'name': 'python',
        'version': 3,
        'isFun': True,
        'almostCamelCase': False,
        'CAPitalized': True,
        'HTTPEndpoint': 'http://127.0.0.1',
        'TargetGroupARNs': ['arn:aws:elasticloadbalancing:us-east-1:812812312:targetgroup/foo/123123123123123'],
        'Tags': {
            'SomeKey': 'SomeValue',
            'SomeOtherKey': 'SomeOtherValue'
        }
    }

# Generated at 2022-06-12 23:10:30.400883
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Instantiate testing data
    camel_dict = dict(
        RedrivePolicy=dict(
            maxReceiveCount=1,
            deadLetterTargetArn='deadlettertargetarn'
        ),
        AttributeNames=[
            'All',
            'Policy'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        QueueUrl='queueurl',
        VisibilityTimeout=1,
        WaitTimeSeconds=1,
        ReceiveRequestAttemptId='receiverequestattemptid'
    )


# Generated at 2022-06-12 23:10:39.713487
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"HTTPEndpoint": {"TargetArn": "thethings", "Tags": {'sometag': 'somevalue'}}}, True) == {'h_t_t_p_endpoint': {'target_arn': 'thethings', 'tags': {'sometag': 'somevalue'}}}
    assert camel_dict_to_snake_dict({"HTTPEndpoint": {"TargetArn": "thethings", "Tags": {'sometag': 'somevalue'}}}, False) == {'http_endpoint': {'target_arn': 'thethings', 'tags': {'sometag': 'somevalue'}}}

# Generated at 2022-06-12 23:10:49.769913
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        'HTTPEndpoint': {
            'Id': '1',
            'Url': 'https://endpoint.com',
            'Protocol': 'HTTPS'},
        'Method': 'GET',
        'Notification': {
            'Email': {
                'Status': 'Disable'}},
        'ProtocolVersion': '1'}

    converted_dict = camel_dict_to_snake_dict(test_dict)

    assert converted_dict['h_t_t_p_endpoint']['id'] == '1'
    assert converted_dict['h_t_t_p_endpoint']['url'] == 'https://endpoint.com'
    assert converted_dict['method'] == 'GET'

# Generated at 2022-06-12 23:10:57.477417
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    input_dict = {'HTTPEndpoint': {'URLEndpoint': 'http://www.amazonaws.com', 'TimeoutInSeconds': 10},
                  'Tags': {'Sloth': 'Sloth', 'Sloths': 'Sloths', 'Slothful': 'Slothful'}}

    expected_dict = {'http_endpoint': {'url_endpoint': 'http://www.amazonaws.com', 'timeout_in_seconds': 10},
                     'tags': {'Sloth': 'Sloth', 'Sloths': 'Sloths', 'Slothful': 'Slothful'}}

    returned_dict = camel_dict_to_snake_dict(input_dict)
    assert returned_dict == expected_dict

    # Test that tags are not converted
    assert input_dict['Tags'] == returned_dict['tags']

   

# Generated at 2022-06-12 23:11:05.040275
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'fooBar': 1, 'bazCamel': 2}) == {'foo_bar': 1, 'baz_camel': 2}

    assert camel_dict_to_snake_dict({'fooBar': {'bazCamel': {'one': 1, 'two': 2}}}) == \
        {'foo_bar': {'baz_camel': {'one': 1, 'two': 2}}}

    assert camel_dict_to_snake_dict({'fooBar': [{'bazCamel': {'one': 1, 'two': 2}}, 1, 2, 3]}) == \
        {'foo_bar': [{'baz_camel': {'one': 1, 'two': 2}}, 1, 2, 3]}

    assert camel_dict

# Generated at 2022-06-12 23:11:14.505601
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:25.447913
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function ``recursive_diff()``.

    This test validates dictionaries that are the same, nested dictionaries
    where the primes differ, dictionaries with different keys, mixed keys
    between dictionaries, and differing values between dictionaries.

    :return: None
    """

    # Validate equality
    result = recursive_diff({}, {})
    assert result is None, "Expected 'None' but got '%s'" % result

    # Validate a nested dictionary
    result = recursive_diff(
        {'name': 'bob'},
        {'name': 'bob', 'nested': {'name': 'nested-bob', 'language': 'english'}}
    )
    assert result is None, "Expected 'None' but got '%s'" % result

    # Validate a nested dictionary
   

# Generated at 2022-06-12 23:11:35.713726
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {
        "Tags": {
            "Key": "Ansible",
            "Value": "True"
        }
    }
    snake = {
        "tags": {
            "Key": "Ansible",
            "Value": "True"
        }
    }

    assert camel_dict_to_snake_dict(camel) == snake_dict_to_camel_dict(snake)
    assert camel_dict_to_snake_dict(camel) == {
        'tags': {'Key': 'Ansible', 'Value': 'True'}
    }



# Generated at 2022-06-12 23:11:43.842965
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'SubDict': {
            'D': 1,
            'E': 2
        },
        'Tags': {
            'Key1': 'Value1',
            'Key2': 'Value2'
        },
        'Listofdict': [
            {
                'F': 1,
                'G': 2
            }
        ],
        'Listoflist': [
            [1, 2, 3]
        ],
        'HTTP': {
            'HTTPEndpoint': {}
        }
    }


# Generated at 2022-06-12 23:11:52.963503
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:01.326700
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict_in = {
        "SecurityGroupIds": [
            "sg-2bff4f43"
        ],
        "HTTPEndpoint": {
            "EndpointType": "string"
        },
        "Tags": {
            "Name": "xgboost-training"
        }
    }
    dict_out = {
        'security_group_ids': ['sg-2bff4f43'],
        'h_t_t_p_endpoint': {'endpoint_type': 'string'},
        "tags": {
            "Name": "xgboost-training"
        }
    }
    result = camel_dict_to_snake_dict(dict_in, reversible=True)
    assert result == dict_out


# Generated at 2022-06-12 23:12:11.249117
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:19.934959
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = dict(
        HTTPEndpoint=dict(
            Port=80
        ),
        Tags=[
            dict(
                Key="foo",
                Value="bar"
            )
        ]
    )

    expected_dict = dict(
        h_t_t_p_endpoint=dict(
            port=80
        ),
        tags=[
            dict(
                key="foo",
                value="bar"
            )
        ]
    )

    assert camel_dict_to_snake_dict(test_dict) == expected_dict

    # Test case-preservation of tag keys
    test_dict = dict(
        HTTPEndpoint=dict(
            Port=80
        ),
        Tags=[
            dict(
                Key="foo",
                Value="bar"
            )
        ]
    )



# Generated at 2022-06-12 23:12:30.166319
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:33.307028
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {'FooBar': 'baz'}
    snake = camel_dict_to_snake_dict(camel)
    assert snake == {'foo_bar': 'baz'}

# Generated at 2022-06-12 23:12:43.043778
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = dict(
        Foo=1234,
        Bar='abcd',
        Baz=dict(
            Hello=1,
            World=2,
            HTTPEndPoint='abcd',
            PluralsAreFun=dict(
                TargetGroupARNs=['arn:abc:123:abc:456'],
                LoadBalancerARNS=['arn:abc:123:abc:789'],
                SubnetIDs=['subnet-123', 'subnet-234'],
                SecurityGroupIDs=['sg-123', 'sg-234'],
                ListenerARNs=['arn:abc:123:abc:111'],
            ),
        ),
        Tags=[
            dict(Key='Name', Value='foo-bar'),
            dict(Key='Type', Value='LoadBalancer'),
        ]
    )
    expected

# Generated at 2022-06-12 23:12:53.111510
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) is None
    assert recursive_diff('abc', 'abc') == (None, None)
    assert recursive_diff('abc', 'def') == (('abc', 'def'), None)
    assert recursive_diff({'a': 'b'}, {'a': 'b'}) is None
    assert recursive_diff({'b': 'b'}, {}) == ({'b': 'b'}, None)
    assert recursive_diff({}, {'b': 'b'}) == (None, {'b': 'b'})
    assert recursive_diff({'a': 'b'}, {'c': 'd'}) == ({'a': 'b'}, {'c': 'd'})

# Generated at 2022-06-12 23:13:08.520405
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:17.468066
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for recursive_diff
    """
    assert recursive_diff({1: 1}, {1: 1}) is None
    assert recursive_diff({'a': 1, 'b': 2}, {'a': 2, 'b': 2}) == ({'a': 1}, {'a': 2})
    assert recursive_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 3}) == ({'b': 2}, {'b': 3})
    assert recursive_diff({'a': 1, 'b': 2}, {'a': 1}) == ({'b': 2}, {})
    assert recursive_diff({'a': 1, 'b': 2}, {'c': 1, 'b': 2}) == ({'a': 1}, {'c': 1})

# Generated at 2022-06-12 23:13:28.324772
# Unit test for function recursive_diff
def test_recursive_diff():
    # Left difference only
    left_1 = {
        'one': True,
        'two': False,
        'three': {
            'four': {
                'five': True
            },
            'six': True
        }
    }
    right_1 = {
        'one': True,
        'two': False,
        'three': {
            'four': {},
            'six': True
        }
    }
    left_only = {
        'three': {
            'four': {
                'five': True
            }
        }
    }
    # Right difference only
    left_2 = {
        'one': True,
        'two': False,
        'three': {
            'four': {},
            'six': True
        }
    }

# Generated at 2022-06-12 23:13:35.838913
# Unit test for function recursive_diff
def test_recursive_diff():
    import json
    """
    File: test_recursive_diff.py
    """
    def test(a, b):
        print(json.dumps(recursive_diff(a, b), indent=4, sort_keys=True))

    # Test case 1
    a = {
        'name': 'some app',
        'code': 'myapp',
        'tags': {
            'resource_type': 'app'
        }
    }
    b = {
        'name': 'some app',
        'code': 'myapp',
        'tags': {
            'resource_type': 'app'
        }
    }
    test(a, b)

    # Test case 2

# Generated at 2022-06-12 23:13:42.147347
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "fooBar": {
            "baz": "bam"
        },
        "FooBarBaz": [{
            "fooBarBaz": [{
                "test": "test"
            }]
        }]
    }

    expected_result = {
        "foo_bar": {
            "baz": "bam"
        },
        "foo_bar_baz": [{
            "foo_bar_baz": [{
                "test": "test"
            }]
        }]
    }

    assert expected_result == camel_dict_to_snake_dict(camel_dict)


# Generated at 2022-06-12 23:13:54.013964
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:02.402281
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        "Protocol": "HTTPS",
        "EFSVolumeConfiguration": {
            "FileSystemId": "fs-xyz1234",
            "RootDirectory": "/",
            "TransitEncryption": "ENABLED",
            "AuthorizedCidrBlocks": ["10.0.0.1/32"]
        },
        "AutoScalingGroups": [{"Name": "SomeName"}],
        "Tags": { "Tag1": "Value1" },
        "TagKey": "TagValue"
    }

# Generated at 2022-06-12 23:14:11.885616
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'URL': 'http://example.com',
            'Description': 'An example HTTP endpoint.',
            'Created': '2015-09-15T16:24:18.716Z',
            'LastModified': '2015-09-15T16:24:18.716Z',
            'Port': 4567,
            'Scope': 'Request',
            'PoweredOn': True
        }
    }

    # Standard conversion

# Generated at 2022-06-12 23:14:21.755613
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    complex_dict = {'HTTPEndpoint': {'Path': '/test', 'Protocol': 'HTTPS'}, 'Tags': {'Key1': 'Value1'}}
    inverted_snakes = {'http_endpoint': {'path': '/test', 'protocol': 'HTTPS'}, 'tags': {'Key1': 'Value1'}}
    assert camel_dict_to_snake_dict(complex_dict, False) == inverted_snakes

    normal_snakes = {'http_endpoint': {'path': '/test', 'protocol': 'HTTPS'}, 'tags': {'key1': 'Value1'}}
    assert camel_dict_to_snake_dict(complex_dict) == normal_snakes


# Generated at 2022-06-12 23:14:32.546953
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "vpcID": "vpc-123",
        "OtherProp": "Test.",
        "SubDict": {
            "vpcID": "vpc-321",
            "OtherProp": "Test."
        },
        "SubList": [
            {
                "vpcID": "vpc-321",
                "OtherProp": "Test.",
                "SubList": [
                    {
                        "vpcID": "vpc-321",
                        "OtherProp": "Test.",
                    }
                ]
            }
        ]
    }


# Generated at 2022-06-12 23:14:44.121353
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {"one": 1, "two": 2, "Three": 3, "four": {'five': 5, 'six': {'SubSubDict': {'seven': 7}}},
                 'eight': [1, 2, {'nine': 9}]}
    snake_dict = camel_dict_to_snake_dict(test_dict)
    assert snake_dict == {'one': 1, 'two': 2, 'three': 3, 'four': {'five': 5, 'six': {'sub_sub_dict': {'seven': 7}}},
                          'eight': [1, 2, {'nine': 9}]}


# Generated at 2022-06-12 23:14:54.248872
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert(camel_dict_to_snake_dict({'camel': 'case'}, False) == {'camel': 'case'})
    assert(camel_dict_to_snake_dict({'Camel': 'case'}, False) == {'camel': 'case'})
    assert(camel_dict_to_snake_dict({'Camel': 'case'}, True) == {'c_a_mel': 'case'})
    assert(camel_dict_to_snake_dict({'camel': 'case', 'Camel': 'case'}, False) == {'camel': 'case', 'camel_1': 'case'})

# Generated at 2022-06-12 23:15:03.964461
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict_1 = {
        'IncludeGlobalServiceEvents': True,
        'IsMultiRegionTrail': True,
        'IsOrganizationTrail': True,
        'KmsKeyId': 'Arn',
        'S3BucketName': 'bucket',
        'S3KeyPrefix': 'string',
        'SnsTopicName': 'string',
        'Tags': {
            'Key': 'string',
            'Value': 'string'
        },
        'TrailARN': 'arn',
        'TrailName': 'name',
    }


# Generated at 2022-06-12 23:15:12.163494
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:20.242111
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_case_dict = {
        'HTTPEndpoint': {
            'endpointGroups': [
                {
                    'endpointGroupRegion': 'us-east-2',
                    'endpointGroupType': 'EDGE'
                }
            ],
            'endpointId': 'd-3B0B816C7',
            'id': 'd-3B0B816C7',
            'tags': {
                'HTTPTest': 'HTTPTest'
            }
        }
    }

    # Basic test
    snake_case_dict = camel_dict_to_snake_dict(camel_case_dict)

# Generated at 2022-06-12 23:15:31.056690
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:41.103506
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert _camel_to_snake("JumboAcronym") == "jumbo_acronym"
    assert _camel_to_snake("JumboAcronym", True) == "j_u_m_b_o_acronym"
    assert _camel_to_snake("HTTPEndpoint") == "http_endpoint"
    assert _camel_to_snake("HTTPEndpoint", True) == "h_t_t_p_endpoint"
    assert _camel_to_snake("JumboAcronym", True) == "j_u_m_b_o_acronym"
    assert _snake_to_camel("jumbo_acronym") == "jumbo_acronym"

# Generated at 2022-06-12 23:15:47.631000
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_data = {
        'AllFieldsCamel': 'Value1',
        'Field2': {
            'CamelSubField': 'SubValue'
        },
        'Field3': [
            {
                'CamelListField1': 'ListValue1',
                'CamelListField2': 'ListValue2'
            }
        ]
    }
    expected_data = {
        'all_fields_camel': 'Value1',
        'field2': {
            'camel_sub_field': 'SubValue'
        },
        'field3': [
            {
                'camel_list_field1': 'ListValue1',
                'camel_list_field2': 'ListValue2'
            }
        ]
    }

# Generated at 2022-06-12 23:15:57.692156
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    import json

    test_dict = camel_dict_to_snake_dict(
        {
            "IamUserAccessToBilling": "ALLOW",
            "IAMUserARN": "arn:aws:iam::123456789012:user/user1",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "user1"
                },
                {
                    "Key": "Department",
                    "Value": "Finance"
                }
            ]
        },
        ignore_list=['Tags']
    )

    print(json.dumps(test_dict, indent=4))


# Generated at 2022-06-12 23:16:06.522558
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        'TagKey': '1',
        'TagValue': '2',
        'Tags': [
            {'TagKey': 'key1', 'TagValue': 'value1'},
            {'TagKey': 'key2', 'TagValue': 'value2'},
        ],
        'Endpoints': [
            {'HTTPEndpoint': {'URL': 'http://www.url.com'}},
            {'HTTPSEndpoint': {'URL': 'https://www.url.com'}},
        ]
    }

    d1 = camel_dict_to_snake_dict(d, False)
    d2 = camel_dict_to_snake_dict(d, True)

    # Verify tags are unchanged
    assert d['Tags'] == d1['tags'] == d2['tags']
   

# Generated at 2022-06-12 23:16:23.944989
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {
        'HTTPEndpoint': {'Endpoint': '1.1.1.1', 'EndpointType': 'dns'},
        'HTTPVersion': 'HTTP_2',
        'ProtocolName': 'protocol_name',
        'TargetGroupARNs': [
            'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/target_group_name/6d0ecf831eec9f09',
            'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/target_group_name/6d0ecf831eec9f09'
        ]
    }


# Generated at 2022-06-12 23:16:33.052608
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    reversibles = [("HTTPEndpointList", "h_t_t_p_endpoint_list"),
                   ("TargetGroupARNsList", "target_group_a_r_ns_list")]
