

# Generated at 2022-06-12 23:07:05.119767
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    from ansible.module_utils.ec2 import camel_dict_to_snake_dict
    import json

    try:
        import botocore
    except ImportError:
        botocore = None

    # input data
    desc_data = json.load(open('./unit_tests/camel_dict_to_snake_dict.json'))
    test_cases = []
    for test_item in desc_data:
        test_case_dict = {}
        test_case_dict['description'] = test_item['description']
        test_case_dict['input'] = test_item['input']
        test_case_dict['output'] = test_item['output']
        test_cases.append(test_case_dict)

    for test_case in test_cases:

        # run test
        output_

# Generated at 2022-06-12 23:07:15.230512
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_test_dict = {'testCamelKey': 'testCamelValue',
                       'testCamelKey2': 'testCamelValue2',
                       'testCamel_Key': 'testCamelValue',
                       'test-camel-key': 'test-camel-value',
                       'test': 'test',
                       'TEST': 'TEST'}

    snake_test_dict = {'test_camel_key': 'testCamelValue',
                       'test_camel_key_2': 'testCamelValue2',
                       'test_camel__key': 'testCamelValue',
                       'test_camel_key': 'test-camel-value',
                       'test': 'test',
                       'TEST': 'TEST'}


# Generated at 2022-06-12 23:07:24.114393
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'A': {'B': 1, 'C': 2}, 'D': '1'}) == {'a': {'b': 1, 'c': 2}, 'd': '1'}
    assert camel_dict_to_snake_dict({'A': {'B': {'C': 1, 'D': 2}, 'E': 3}, 'F': '1'}) == {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': '1'}

# Generated at 2022-06-12 23:07:34.745371
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test various conversions
    assert camel_dict_to_snake_dict({'CamelCase': {'CamelCase': 'CamelCase'}}) == {'camel_case': {'camel_case': 'CamelCase'}}
    assert camel_dict_to_snake_dict({'HTTPSecurityPolicy': {'HTTPSecurityPolicy': {'HTTPSecurityPolicy': 'HTTPSecurityPolicy'}}}) == {'h_t_t_p_security_policy': {'h_t_t_p_security_policy': {'h_t_t_p_security_policy': 'HTTPSecurityPolicy'}}}

# Generated at 2022-06-12 23:07:42.060563
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function ``recursive_diff``

    :return: ``None``
    """


# Generated at 2022-06-12 23:07:50.518108
# Unit test for function dict_merge
def test_dict_merge():
    # constants
    a = {
        'a': 'a',
        'b': 'b'
    }
    b = {
        'a': 'A',
        'b': 'B',
        'c': 'C'
    }

    # perform the merge
    m = dict_merge(a, b)

    # verify that key in a and b were overridden
    assert(m['a'] == 'A')
    assert(m['b'] == 'B')

    # verify that key in b was added to m
    assert(m['c'] == 'C')


# Generated at 2022-06-12 23:08:00.694757
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    common_tags = {
        'Key': 'key',
        'Value': 'value'
    }

    example_dict = {
        'HTTPEndpoint': 'https://foo.com',
        'Tags': [
            {
                'Key': 'key0',
                'Value': 'value0'
            },
            {
                'Key': 'key1',
                'Value': 'value1'
            }
        ]
    }

    assert camel_dict_to_snake_dict(example_dict) == {'http_endpoint': 'https://foo.com', 'tags': [{'key': 'key0', 'value': 'value0'}, {'key': 'key1', 'value': 'value1'}]}


# Generated at 2022-06-12 23:08:05.854376
# Unit test for function dict_merge
def test_dict_merge():

    a = {'a': 1, 'b': 2, 'c': {'x': 11, 'y': 12}}
    b = {'b': 3, 'c': {'y': 8, 'z': 13}, 'd': 4}
    c = {'a': 1, 'b': 3, 'c': {'x': 11, 'y': 8, 'z': 13}, 'd': 4}
    assert dict_merge(a, b) == c

    a = {'a': 1, 'b': 2, 'c': {'x': 11, 'y': 12}}
    b = {'b': 3, 'c': {'y': 8, 'z': 13}, 'd': 4}
    c = b
    b['new_key'] = "new_value"
    assert dict_merge(a, b)

# Generated at 2022-06-12 23:08:16.246123
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'k1': 'v1',
        'k2': 1,
        'k3': {
            'k4': 1,
            'k5': '',
        },
        'k6': [{
            'k7': 'v7',
            'k8': [],
            'k9': {
                'k10': 'v10',
                'k11': {
                    'k12': None,
                },
                'k13': [{
                    'k14': 'v14',
                }],
            },
        }],
    }

# Generated at 2022-06-12 23:08:25.678114
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:34.072492
# Unit test for function recursive_diff
def test_recursive_diff():

    def test_case(dict1, dict2, expected_diff, message=None):

        diff = recursive_diff(dict1, dict2)

        if diff != expected_diff:
            raise AssertionError('Failed test case: %s\n'
                                 '    With dict1: %s\n'
                                 '    and dict2: %s\n'
                                 '    Expected diff: %s\n'
                                 '    Actual diff: %s\n'
                                 % (message, dict1, dict2, expected_diff, diff))

    # No differences
    test_case({}, {}, None, 'No differences between dicts')
    test_case(dict(k='v'), dict(k='v'), None, 'No differences between dicts')

    # Different length dicts

# Generated at 2022-06-12 23:08:44.133289
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({'foo':{'bar':{'chaz':'baz'}}}, {'foo':{'bar':{'chaz':'baz'}}}) is None
    assert recursive_diff({'foo':{'bar':{'chaz':'baz'}}}, {'foo':{'bar':{'chaz':'baz'}}}) is None
    assert recursive_diff({'foo':{'bar':{'chaz':'baz'}}}, {'foo':{'bar':{'chaz':'bam'}}}) == ({'foo':{'bar':{'chaz':'baz'}}}, {'foo':{'bar':{'chaz':'bam'}}})

# Generated at 2022-06-12 23:08:54.654415
# Unit test for function recursive_diff
def test_recursive_diff():
    d = {'x': 1, 'y': 2, 'z': 3}
    d1 = {'x': 1, 'y': 2, 'z': 3, 'w': 4}
    d2 = {'x': 1, 'y': 2, 'z': 4, 'k': 5}
    d3 = {'x': 1, 'y': 2, 'z': 3}
    d4 = {'x': 1, 'y': 2, 'a': 5, 'z': 3}
    d5 = {'x': 1, 'y': 2, 'z': 3, 'b': {'a': 'A', 'b': 'B'}}
    d6 = {'x': 1, 'y': 2, 'z': 3, 'b': {'a': 'C', 'b': 'B'}}

# Generated at 2022-06-12 23:09:01.842747
# Unit test for function recursive_diff
def test_recursive_diff():
    changed_dict = {
        'test1': {
            'test2': {
                'test3': 1
            }
        },
        'test4': {
            'test5': 'test6',
            'test7': None,
            'test8': 'test9',
            'test10': 1
        },
        'test11': {
            'test12': 1,
            'test13': None
        }
    }

# Generated at 2022-06-12 23:09:13.094317
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'Node': [{'Name': 'x', 'CPU': 2},
                                              {'Name': 'y', 'CPU': 2}]}) == \
           {'node': [{'name': 'x', 'cpu': 2},
                     {'name': 'y', 'cpu': 2}]}


# Generated at 2022-06-12 23:09:22.545588
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:09:32.034490
# Unit test for function recursive_diff
def test_recursive_diff():
    a = {
        'b': [1, 2, 3],
        'c': {
            'd': 'e',
            'f': 42,
        },
    }
    b = {
        'b': [1, 2, 3, 4],
        'c': {
            'd': 'E',
            'f': 42,
        },
    }
    c = {
        'b': [1, 2, 3, 4],
        'c': {
            'd': 'E',
            'f': 42,
        },
        'g': 'h',
    }
    d = {
        'b': [1, 2, 3, 4],
        'c': {
            'd': 'E',
            'f': 42,
            'i': 1,
        },
    }
    e

# Generated at 2022-06-12 23:09:37.749824
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {'firstName': 'John',
         'lastName': 'Smith'}
    assert(camel_dict_to_snake_dict(d)) == {'first_name': 'John', 'last_name': 'Smith'}
    assert(snake_dict_to_camel_dict(d)) == {'firstName': 'John', 'lastName': 'Smith'}



# Generated at 2022-06-12 23:09:47.434963
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {}
    d2 = {}
    assert recursive_diff(d1, d2) == None

    d1 = {}
    d2 = {'k1': 'v1'}
    left, right = recursive_diff(d1, d2)
    assert set(left) == set(right) == {'k1'}
    assert left['k1'] == None
    assert right['k1'] == 'v1'

    d1 = {'k1': 'v1'}
    d2 = {'k1': 'v1'}
    assert recursive_diff(d1, d2) == None

    d1 = {'k1': 'v1'}
    d2 = {'k1': 'v1', 'k2': 'v2'}

# Generated at 2022-06-12 23:09:55.421804
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict_camel_1 = {
        'fooBar': {
            'fizzBuzz': [0]
        },
        'barBuzz': [1]
    }

    dict_camel_2 = {
        'RequestAttributes': {
            'someKey': 'someValue'
        }
    }

    dict_camel_3 = {
        'Tags': [
            {
                'Key': 'fooBar',
                'Value': 'fooBar_value',
            },
            {
                'Key': 'fooBar2',
                'Value': 'fooBar2_value',
            }
        ]
    }

    dict_camel_4 = {
        'Tags': {
            'fooBar': {
                'fooBar2': 'fooBar_value'
            }
        }
    }

    dict_

# Generated at 2022-06-12 23:10:05.032260
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'fooBar': {'fooBar1': {
        'fooBar2': {'fooBar3': 'foobar', 'fooBar4': 'foobar1'}}, 'fooBar5': {
            'fooBar6': ['foobar1', 'foobar2']
        }
    }, 'foobar0': 'foobar3', 'fooBar8': ['foobar', 'foobar1'], 'fooBar7': ['foobar', 'foobar1']}
    out_dict = camel_dict_to_snake_dict(camel_dict, ignore_list='Tags')

# Generated at 2022-06-12 23:10:13.960129
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test results for non-reversible case
    # Test for a non-dictionary case
    assert camel_dict_to_snake_dict("camel_test") == "camel_test"
    # Test for an empty dictionary case
    assert camel_dict_to_snake_dict({}) == {}
    # Test for a single key case
    assert camel_dict_to_snake_dict({"TestKey": "TestValue"}) == {"test_key": "TestValue"}
    # Test for a sub-dictionary case
    assert camel_dict_to_snake_dict({"TestKey": {"TestSubKey": "TestSubValue"}}) == {"test_key": {"test_sub_key": "TestSubValue"}}
    # Test for a list of sub-dictionaries case
    assert camel_dict_to_sn

# Generated at 2022-06-12 23:10:25.156541
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Name': 'http-endpoint-1',
            'Description': 'Make a cluster API call'
        },
        'TestString': 'http-endpoint-1',
        'TestInteger': 123,
        'TestList': [{
            'TestString2': 'http-endpoint-2',
            'TestInteger2': 123,
        }],
        'Tags': {
            'SubTag': 'TestString',
            'SubTag2': 'TestString2',
        }
    }


# Generated at 2022-06-12 23:10:32.452197
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "subnets": [
            "subnet-9d4a7b6c",
            "subnet-94767cbb"
        ],
        "name": "subnet-group-1234",
        "description": "subnet description",
        "creationDate": 1234567
    }

    expected_output_dict = {
        "subnets": [
            "subnet-9d4a7b6c",
            "subnet-94767cbb"
        ],
        "name": "subnet-group-1234",
        "description": "subnet description",
        "creation_date": 1234567
    }

    assert expected_output_dict == camel_dict_to_snake_dict(camel_dict)


# Generated at 2022-06-12 23:10:38.384586
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_data = {"fooBar": 1, "fooBaz": [1, 2, 3],
                 "Foo": {"bar": [{"baz": "bog"}]}}
    exp_data = {"foo_bar": 1, "foo_baz": [1, 2, 3],
                "foo": {"Bar": [{"Baz": "bog"}]}}
    ret = camel_dict_to_snake_dict(test_data)
    assert ret == exp_data



# Generated at 2022-06-12 23:10:48.066754
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'ServiceId': 'svc-12345678',
                  'HttpRouteName': 'example_1',
                  'HttpRoute': {'Match': {'Prefix': '/foo/'},
                                'Action': {'WeightedTarget': {'VirtualNode': 'ECS-VN-Node',
                                                              'Weight': 0}}},
                  'Priority': 10}

# Generated at 2022-06-12 23:10:54.887155
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict(
        {
            'Tags': [
                {
                    'Key': 'foo',
                    'Value': 'bar'
                }
            ]
        },
        ignore_list=['Tags']
    ) == {
        'tags': [
            {
                'Key': 'foo',
                'Value': 'bar'
            }
        ]
    }

    assert camel_dict_to_snake_dict(
        {
            'MyKey': 'myValue'
        },
        reversible=True
    ) == {
        'my_key': 'myValue'
    }


# Generated at 2022-06-12 23:11:02.246258
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict1 = {'thisIsAKey': 'thisIsAValue'}
    camel_dict2 = {'thisIsAKey': 'thisIsAValue', 'isAnotherValue': 'anotherValue'}
    camel_dict3 = {'thisIsAKey': 'thisIsAValue', 'thisIsAnotherKey': 'thisIsAnotherValue'}
    camel_dict4 = {'thisIsAKey': 'thisIsAValue', 'isAnotherValue': 'anotherValue',
                   'thisIsAnotherKey': 'thisIsAnotherValue'}
    camel_dict5 = {'isAnotherKey': 'thisIsAValue'}
    camel_dict6 = {'isAnotherKey': 'thisIsAValue', 'IsAnotherValue': 'anotherValue'}

# Generated at 2022-06-12 23:11:07.910951
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:13.143955
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = { "fooBar": "spam", "eggs": "ham", "baz": {"quux": { "quuz": 1 } }, "boolean": False, "stuff": [ 1, 2, 3 ] }
    snake_dict = { "foo_bar": "spam", "eggs": "ham", "baz": {"quux": { "quuz": 1 } }, "boolean": False, "stuff": [ 1, 2, 3 ] }

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict



# Generated at 2022-06-12 23:11:26.581511
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {"InstanceIds": ["i-12345678", "i-abcdef12"], "Filters": [{"Name": "tag:Name", "Values": ["test-instance"]}]}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"instance_ids": ["i-12345678", "i-abcdef12"], "filters": [{"name": "tag:Name", "values": ["test-instance"]}]}

    tags = [{"Key": "Name", "Value": "Production"}]
    camel_dict = {"Tags": tags}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {"tags": [{"key": "Name", "value": "Production"}]}

    # Test for when

# Generated at 2022-06-12 23:11:36.584556
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test that camel_dict_to_snake_dict is reversible
    """

    camel_dict = {
        'fooBarBaz': 'foobarbaz',
        'foo_bar_baz': 'foobarbaz',
        'tagKey': {
            'tagKey': 'tagValue',
            'fooBar': 'foobar'
        },
        'tags': [
            {
                'tagKey': 'tagValue',
                'fooBar': 'foobar'
            },
            {
                'key': 'value',
            }
        ]
    }

    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict


# Generated at 2022-06-12 23:11:44.512816
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(
        HTTPEndpoint=dict(Path='/foo', Method='GET'),
        HostHeader='foo.foo.com',
        UseDualStack=True,
        Tags=[dict(Key='foo', Value='bar')],
        HttpCode=['403'],
    )
    snake_dict = dict(
        h_t_t_p_endpoint=dict(path='/foo', method='GET'),
        host_header='foo.foo.com',
        use_dual_stack=True,
        tags=[dict(key='foo', value='bar')],
        http_code=['403'],
    )
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict
    assert snake_dict_to_camel_dict(snake_dict) == camel_

# Generated at 2022-06-12 23:11:53.787840
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:02.105093
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Testing for parameters
    camel_data = {"HTTPEndpoint": "API", "HTTPSEndpoint": "API", "TCPPort": 1234, "Tags": {}}

    assert camel_dict_to_snake_dict(camel_data) == {'http_endpoint': 'API', 'https_endpoint': 'API', 'tcp_port': 1234, 'tags': {}}

    camel_data = {"HTTPEndpoint": "API", "HTTPSEndpoint": "API", "TCPPort": 1234, "Tags": {}}

# Generated at 2022-06-12 23:12:11.418630
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'Foo': 'bar'}) == {'foo': 'bar'}
    assert camel_dict_to_snake_dict({'foo': 'bar'}) == {'foo': 'bar'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBarBaz': 'quux'}) == {'foo_bar_baz': 'quux'}
    assert camel_dict_to_snake_dict({'fooBarBaz': 'quux'}, reversible=True) == {'f_o_o_b_a_r_b_a_z': 'quux'}
    assert camel_dict_to_

# Generated at 2022-06-12 23:12:20.067788
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'TestCase1': {
            'setting1': 'value1',
            'setting2': 'value2'
        },
        'TestCase2': {
            'setting3': 'value3',
            'settings4': 'value4'
        },
        'testCase3': {
            'setting5': 'value5',
            'setting6': 'value6'
        },
        'tags': {
            'TestTag1': 'value1',
            'TestTag2': 'value2'
        },
    }


# Generated at 2022-06-12 23:12:30.401249
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    obj = {'LoadBalancerName': 'foobar',
           'HttpEndpointSpec': {'Endpoint': {'Host': 'localhost', 'Port': 8000},
                                'Path': '/'}
    }
    non_recursive_result = camel_dict_to_snake_dict(obj, reversible=False)
    assert non_recursive_result == {'load_balancer_name': 'foobar', 'http_endpoint_spec': {'endpoint': {'host': 'localhost', 'port': 8000}, 'path': '/'}}
    recursive_result = camel_dict_to_snake_dict(obj, reversible=True)

# Generated at 2022-06-12 23:12:40.712537
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'TestHTTPEndpoint': {'EndpointURL': 'http://www.testing.com', 'HttpPath': 'test-http'}}

    assert _camel_to_snake('TestHTTPEndpoint') == 'test_http_endpoint', \
        'Bad snake_case conversion'

    expected = {'test_http_endpoint': {'endpoint_url': 'http://www.testing.com', 'http_path': 'test-http'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == expected, \
        'Bad camel_dict_to_snake_dict conversion'

    # Reversible dict conversion
    inverted = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert camel_

# Generated at 2022-06-12 23:12:50.386232
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {"TransitGatewayId": "transit-gateway-id",
                  "NonDefaultRouteTable": True,
                  "Options": {
                      "DisableVpnEcmpSupport": True,
                      "EnableBgpAttachments": True,
                      "AssociationDefaultRouteTableId": "tbl-id",
                      "DerivedAssociationDefaultRouteTableId": "tbl-id2",
                      "PropagationDefaultRouteTableId": "tbl-id3"
                      }
                  }

# Generated at 2022-06-12 23:12:59.771852
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test dict with a dict and a list
    camel1 = {
        'testDict': {'testCamelKey1': 'testCamelVal1', 'testCamelKey2': 'testCamelVal2'},
        'testList': [ {'testCamelKey1': 'testCamelVal1', 'testCamelKey2': 'testCamelVal2'}, {'testCamelKey1': 'testCamelVal1', 'testCamelKey2': 'testCamelVal2'}]
    }

# Generated at 2022-06-12 23:13:09.991390
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'fooBar': {'fooBarBaz': 1}}
    assert camel_dict_to_snake_dict(test_dict) == {'foo_bar': {'foo_bar_baz': 1}}

    test_dict = {'fooBar': {'fooBarBaz': 1}, 'Bar': {'BarBaz': 2}}
    assert camel_dict_to_snake_dict(test_dict) == {'foo_bar': {'foo_bar_baz': 1}, 'bar': {'bar_baz': 2}}

    test_dict = {'HTTPEndpoint': {'fooBarBaz': 1}, 'Bar': {'BarBaz': 2}}

# Generated at 2022-06-12 23:13:18.453343
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "HTTPEndpoint": {
            "HTTPEndpointConfiguration": {
                "Method": "PATCH",
                "AuthorizationConfig": {
                    "AuthorizationType": "AWS_IAM",
                    "AWS_IAMConfig": {
                        "SigningRegion": "us-east-1"
                    }
                }
            },
            "Url": "https://example.com",
            "InvocationRole": "arn:aws:iam::012345678910:role/example",
            "Name": "TEST",
            "Tags": {
                "Key": "TagKey",
                "Value": "TagValue"
            }
        }
    }


# Generated at 2022-06-12 23:13:29.347201
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'keyName': 'value',
        'keyName2': {
            'keyName3': 'value'
        }
    }
    result = camel_dict_to_snake_dict(test_dict, reversible=True)
    assert result == {
        'key_name': 'value',
        'key_name2': {
            'key_name3': 'value'
        }
    }


# Generated at 2022-06-12 23:13:38.585905
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"FooBarBaz": {
                  "Zoo": {'HttpEndpoint': 1},
                  "FooBar": [],
                  "Tags": {'key1': 'value1',
                           'key2': 'value2'},
                  "BazBaz": ['v1', 'v2', 'v3', {'v4': 'v5'}],
                  "BoolBaz": True},
                  "boolean": False}

    # convert to snake_case, but don't use reversible conversion
    snake_dict_default=camel_dict_to_snake_dict(camel_dict)

    assert snake_dict_default['foo_bar_baz']['http_endpoint'] == 1

# Generated at 2022-06-12 23:13:44.700865
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    result = camel_dict_to_snake_dict(
        {"DomainName": "test", "HelloWorld": "sample", "Tags": [{"Tag": "key"}]},
        True)
    assert result == {"domain_name": "test", "h_e_l_l_o_world": "sample", "tags": [{"tag": "key"}]}



# Generated at 2022-06-12 23:13:55.285722
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:03.329204
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def compare_dicts(d1, d2):
        for k in d1:
            assert k in d2
            assert d1[k] == d2[k]

    mock = {
        'HTTPEndpoint': {
            'Protocols': [
                'http',
                'https'
            ],
            'HTTPMethods': [
                'GET',
                'POST'
            ],
            'AuthorizationScopes': [
                'string'
            ]
        },
        'TCPEndpoint': {
            'Protocols': [
                'tcp'
            ]
        }
    }


# Generated at 2022-06-12 23:14:13.247985
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:22.531811
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:35.041057
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    orig_dict = {
        'dish': 'lasagna',
        'name': 'Emily',
        'HTTPEndpoint': 'httpEndpoint',
        'things': [
            {'item1': 'someValue1'},
            {'item2': 'someValue2'},
        ],
        'another': {
            'thing': 'someValue3'
        },
        'Tags': {
            'key': 'value'
        }
    }

# Generated at 2022-06-12 23:14:41.751227
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "Description": "b",
            "Url": "http://127.0.0.1:8080/post.php",
            "Timeout": 60,
            "Method": "POST",
            "Headers": [],
            "Body": "echo hello world"
        }
    }
    expected_dict = {
        "http_endpoint": {
            "description": "b",
            "url": "http://127.0.0.1:8080/post.php",
            "timeout": 60,
            "method": "POST",
            "headers": [],
            "body": "echo hello world"
        }
    }

    result_dict = camel_dict_to_snake_dict(camel_dict)
    assert result_dict == expected

# Generated at 2022-06-12 23:14:51.993636
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:02.067280
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'Description': 'test description',
        'HTTPEndpoint': 'http://mytesturl.com',
        'Tags': {
            'Key1': 'Value1',
            'Key2': 'Value2'
        },
        'TestList': [
            1,
            2,
            {
                'NestedKey': 'NestedValue'
            }
        ]
    }


# Generated at 2022-06-12 23:15:10.894639
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from pprint import pprint

    # Verify that the dict_merge function works as intended
    a = {
        'SubnetId': 'subnet-abcd1234',
        'Tags': {
            'abc': 'xyz',
            'foo': 'bar'
        },
        'AssignPublicIp': 'ENABLED'
    }
    b = {
        'SubnetId': 'subnet-abcd1234',
        'Tags': {
            'abc': 'xyz',
            'foo': 'bar'
        },
        'AssignPublicIp': 'ENABLED'
    }
    assert dict_merge(a, b) == a

    # Verify that the camel_dict_to_snake_dict function works as intended with a basic example

# Generated at 2022-06-12 23:15:19.191891
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_data = {
        "test": {
            "testKey": "testValue1",
            "testKeyList": [
                "testValue2",
                "testValue3"
            ]
        },
        "testKey2": "testValue4",
        "testKey3": "testValue5",
        "tags": {
            "key": "value"
        }
    }

    test_result_1 = {
        "test": {
            "test_key": "testValue1",
            "test_key_list": [
                "testValue2",
                "testValue3"
            ]
        },
        "test_key2": "testValue4",
        "test_key3": "testValue5",
        "tags": {
            "key": "value"
        }
    }



# Generated at 2022-06-12 23:15:29.446369
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        "TestString": "Hi",
        "TestNum": 1,
        "TestList": ["one", "two"],
        "TestDict": {
            "TestDictString": "Hi",
            "TestDictNum": 1,
            "TestDictList": ["one", "two"],
            "TestDictDict": {
                "TestDictDictString": "Hi",
                "TestDictDictNum": 1,
                "TestDictDictList": ["one", "two"],
                "HTTPEndpoint": "www.test.com"
            },
            "HTTPEndpoint": "www.test.com"
        },
        "HTTPEndpoint": "www.test.com"
    }


# Generated at 2022-06-12 23:15:39.845428
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:47.779746
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:57.830227
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    with pytest.raises(TypeError):
        camel_dict_to_snake_dict()

    input_dict_1 = {'aB': 1, 'cDe': '2'}
    snake_dromedary = {'a_b': 1, 'c_de': '2'}
    snake_camel = {'a_b': 1, 'c_de': '2'}
    assert camel_dict_to_snake_dict(input_dict_1) == snake_dromedary
    assert camel_dict_to_snake_dict(input_dict_1, reversible=True) == snake_camel

    input_dict_2 = {'aB': 1, 'cD': {'cDe': 3}}

# Generated at 2022-06-12 23:16:14.358835
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        "Key1": "value1",
        "Key2": "value2",
        "Key3": {
            "Key4": "value4",
            "Key5": "value5",
            "Key6": {
                "Key7": "value7"
            }
        }
    }

    assert (camel_dict_to_snake_dict(test_dict) == {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key4": "value4",
            "key5": "value5",
            "key6": {
                "key7": "value7"
            }
        }
    })


# Generated at 2022-06-12 23:16:19.110116
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({
        "AutoScalingGroups": [],
        "ListenerArn": "listener-arn",
        "LoadBalancerArn": "load-balancer-arn",
        "TargetGroupArns": [],
        "RegistrationEnabled": True,
        "TargetType": "instance"
    }, True) == {
        "auto_scaling_groups": [],
        "listener_arn": "listener-arn",
        "load_balancer_arn": "load-balancer-arn",
        "target_group_ar_ns": [],
        "registration_enabled": True,
        "target_type": "instance"
    }



# Generated at 2022-06-12 23:16:27.384897
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict_1 = {
        "httpEndpoint": {
            "path": "/foo",
            "serviceName": "bar",
            "method": "POST",
            "authorizationType": "NONE"
        },
        "httpApiId": "1234567890",
        "defaultRouteSettings": {
            "dataTraceEnabled": True,
            "detailedMetricsEnabled": True,
        },
        "routeKey": "$default",
        "routeSelectionExpression": "",
        "target": "integration"
    }

    result = camel_dict_to_snake_dict(test_dict_1)


# Generated at 2022-06-12 23:16:35.283216
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert 'http_endpoint' == _camel_to_snake('HTTPEndpoint', False)
    assert 'h_t_t_p_endpoint' == _camel_to_snake('HTTPEndpoint', True)

    assert 'http_endpoint' == _camel_to_snake('httpEndpoint', False)
    assert 'h_t_t_p_endpoint' == _camel_to_snake('httpEndpoint', True)

    assert 'http_endpoint' == _camel_to_snake('hTTPEndpoint', False)
    assert 'h_t_t_p_endpoint' == _camel_to_snake('hTTPEndpoint', True)