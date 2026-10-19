

# Generated at 2022-06-12 23:07:02.393821
# Unit test for function dict_merge
def test_dict_merge():

    a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
    b = {'d':6, 'e':7, 'f':8, 'g':9}
    c = dict_merge(a,b)
    assert c == {'a':1, 'b':2, 'c':3, 'd':6, 'e':7, 'f':8, 'g':9}

    d = {'a':{'ea':1, 'eb':2}, 'b':2, 'c':3, 'd':4, 'e':5}
    e = {'a':{'ea':10, 'eb':20}, 'd':6, 'e':7, 'f':8, 'g':9}
    f = dict_merge(d,e)

# Generated at 2022-06-12 23:07:12.557075
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_object_dict = {'HTTPEndpoint':
                             {'Destinations': [{'LambdaArn': 'arn:aws:lambda:us-east-1:123456789012:function:ExampleFunction',
                                               'Type': 'LAMBDA'}],
                              'Endpoint': 'arn:aws:s3:::my_bucket'}
                         }

    snake_object_dict = {'h_t_t_p_endpoint':
                             {'destinations': [{'lambda_arn': 'arn:aws:lambda:us-east-1:123456789012:function:ExampleFunction',
                                               'type': 'LAMBDA'}],
                              'endpoint': 'arn:aws:s3:::my_bucket'}
                         }
    assert camel_

# Generated at 2022-06-12 23:07:20.056012
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    d_dict = {'fooBar':{'barFoo':{'foobar':{'fooBar':{'fooBar':'test1','barFoo':'test2'}}}}}
    d_dict['fooBar']['barFoo']['foobar']['fooBar']['foo'] = ['test',{'test':'ing'}]
    d_dict['fooBar']['barFoo']['foobar']['fooBar']['bar'] = 'test'
    d_dict['fooBar']['barFoo']['foobar']['fooBar']['baz'] = {'foo':'test', 'bar':{'foo':'bar'}}
    d_dict['fooBar']['barFoo']['foobar']['barFoo'] = 'test'

# Generated at 2022-06-12 23:07:30.642056
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    example_dict = {
        'HTTPMethod': "GET",
        'HTTPTarget': {
            'HTTPStatus': 200,
            'HTTPPath': "/",
        },
        'Tags': {
            'Foo': "Bar",
        }
    }

    assert(camel_dict_to_snake_dict(example_dict) == {
                                            'http_method': "GET",
                                            'http_target': {
                                                'http_status': 200,
                                                'http_path': "/",
                                            },
                                            'tags': {
                                                'Foo': "Bar",
                                            }
                                        })



# Generated at 2022-06-12 23:07:38.294455
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Simple list
    data = [{'HTTPEndpoint': {'Path': '/test', 'Protocol': 'HTTP'}}]
    result = [{'h_t_t_p_endpoint': {'path': '/test', 'protocol': 'HTTP'}}]
    assert camel_dict_to_snake_dict(data) == result, 'Failed to convert simple list'

    # Simple dictionary with list as value
    data = {'HTTPEndpoint': {'Path': '/test', 'Protocol': 'HTTP'}}
    result = {'h_t_t_p_endpoint': {'path': '/test', 'protocol': 'HTTP'}}
    assert camel_dict_to_snake_dict(data) == result, 'Failed to convert simple dictionary'

    # List in list

# Generated at 2022-06-12 23:07:45.118356
# Unit test for function recursive_diff
def test_recursive_diff():
    """Recursively diff two dictionaries

    Raises ``TypeError`` for incorrect argument type.

    :arg dict1: Dictionary to compare against.
    :arg dict2: Dictionary to compare with ``dict1``.
    :return: Tuple of dictionaries of differences or ``None`` if there are no differences.
    """

    # Test the left, right and sub dictionary
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': {'d1': 'test', 'd2': 'test2'}}
    dict2 = {'b': 2, 'c': 4, 'd': {'d1': 'test', 'd2': 'test3'}}
    x = recursive_diff(dict1, dict2)

# Generated at 2022-06-12 23:07:56.155766
# Unit test for function recursive_diff
def test_recursive_diff():

    dict1 = {'name': 'all_tags', 'tags': {'tag1': 'val1', 'tag2': 'val2', 'tag3': 'val3'}}
    dict2 = {'name': 'all_tags', 'tags': {'tag1': 'val1', 'tag2': 'val3'}}
    test_result = recursive_diff(dict1, dict2)
    expected_result = ({'tags': {'tag2': 'val2'}}, {'tags': {'tag2': 'val3'}})
    assert test_result == expected_result

    dict1 = {'name': 'all_tags', 'tags': {'tag1': 'val1', 'tag2': 'val2', 'tag3': 'val3'}}

# Generated at 2022-06-12 23:08:04.498980
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(camel_dict_to_snake_dict({'CamelCase': 'camel'}) == {'camel_case': 'camel'})
    assert(camel_dict_to_snake_dict({'CamelCase': {'CamelCase': 'camel'}}) == {'camel_case': {'camel_case': 'camel'}})
    assert(camel_dict_to_snake_dict({'CamelCase': ['camel']}) == {'camel_case': ['camel']})
    assert(camel_dict_to_snake_dict({'CamelCase': ['CamelCase']}) == {'camel_case': ['camel_case']})

# Generated at 2022-06-12 23:08:15.059084
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit tests for function recursive_diff"""

    test_dict1 = {
        'foo': {
            'a': 1,
            'b': {
                'x': 2,
                'y': 3,
                'z': 4
            },
            'c': 5
        },
        'bar': 6,
        'baz': 7,
        'qux': 8
    }

    test_dict2 = {
        'foo': {
            'a': 1,
            'b': {
                'x': 2,
                'y': 3,
                'z': 7
            },
            'c': 5
        },
        'bar': 6,
        'baz': 8,
        'qux': 8
    }


# Generated at 2022-06-12 23:08:24.767025
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test1 = {'KMSKeyId': 'test', 'SSECustomerKeyMD5': 'test'}
    camel1 = camel_dict_to_snake_dict(test1, False)
    assert camel1 == {'kms_key_id': 'test', 'sse_customer_key_md5': 'test'}

    test2 = {'HTTPEndpoint': 'test', 'SSEKMS': 'test'}
    camel2 = camel_dict_to_snake_dict(test2, True)
    assert camel2 == {'h_t_t_p_endpoint': 'test', 's_s_e_k_m_s': 'test'}
    recamel2 = snake_dict_to_camel_dict(camel2)

# Generated at 2022-06-12 23:08:37.116530
# Unit test for function recursive_diff
def test_recursive_diff():  # noqa: F811
    assert recursive_diff({'state': 'present'}, {'state': 'absent'}) == ({'state': 'present'}, {'state': 'absent'})
    assert recursive_diff({'state': 'present'}, {'state': 'present'}) is None
    assert recursive_diff({'state': 'state'}, {'state': 'state'}) is None
    assert recursive_diff({'state': 'present'}, {'state': 'present', 'name': 'cdk'}) == ({}, {'name': 'cdk'})
    assert recursive_diff({'state': 'present', 'name': 'cdk'}, {'state': 'present'}) == ({'name': 'cdk'}, {})

# Generated at 2022-06-12 23:08:47.412919
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict1 = dict(Subnets=[{u'EbsOptimized': False, u'DeleteOnTermination': True, u'VpcId': u'vpc-e1d56f86'}, {u'EbsOptimized': False, u'DeleteOnTermination': True, u'VpcId': u'vpc-e1d56f86'}], Tags=[{u'Value': u'igw-8d1adff3', u'Key': u'Name'}, {u'Value': u'Ansible-managed', u'Key': u'Purpose'}], VpcId=u'vpc-e1d56f86')

# Generated at 2022-06-12 23:08:57.423185
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        "HTTPEndpoint": {
            "Description": "A description",
            "EndpointURI": "http://example.com",
            "HostHeader": "example.com"
        }
    }

    expected_snake_dict = {
        "http_endpoint": {
            "description": "A description",
            "endpoint_uri": "http://example.com",
            "host_header": "example.com"
        }
    }

    actual_snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert expected_snake_dict == actual_snake_dict

    actual_camel_dict = snake_dict_to_camel_dict(expected_snake_dict)
    assert camel_dict == actual_camel_dict


#

# Generated at 2022-06-12 23:09:07.568935
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Unit test"""
    camel_dict_sample = {
        'someKey': 'someValue',
        'nestedDict': {
            'anotherKey': 'anotherValue',
            'list': [1, 2, 3, 4],
            'nestedDict': {
                'lastKey': 'lastValue',
                'mixedCaseKey': 'mixedCaseValue',
                'httpEndpoint': {
                    'protocol': 'http',
                    'port': '8080',
                    'path': '/'
                }
            }
        }
    }

    # We want to ensure the API call returns a snake_case dictionary
    # and that we can put it back into camelCase if we want
    # to do a diff between the original and the returned value

    # OrderedDict for Python 2.6

# Generated at 2022-06-12 23:09:15.352040
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Create a simple dictionary
    camel_dict = {'one': 1, 'two': 2, 'three': 3}

    # Convert camel_dict to snake_dict
    snake_dict = camel_dict_to_snake_dict(camel_dict)

    # Test that the original dictionary is unchanged
    assert(snake_dict != camel_dict)

    # Test that the converted dictionary matches expectations
    assert(snake_dict['one'] == 1)
    assert(snake_dict['two'] == 2)
    assert(snake_dict['three'] == 3)



# Generated at 2022-06-12 23:09:23.971946
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert _camel_to_snake('HTTPEndpoint') == 'http_endpoint'
    assert _camel_to_snake('HTTPEndpoint', reversible=True) == 'h_t_t_p_endpoint'
    assert _camel_to_snake('ApplicationARN') == 'application_ar_n'
    assert _camel_to_snake('ApplicationARNs') == 'application_ar_ns'
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_ar_ns'

    assert _snake_to_camel('http_endpoint') == 'httpEndpoint'
    assert _snake_to_camel('http_endpoint', capitalize_first=True) == 'HttpEndpoint'


# Generated at 2022-06-12 23:09:32.194438
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "PortMappings": [
            {
                "HostPort": 80,
                "Protocol": "tcp",
                "ContainerPort": 80
            }
        ],
        "ContainerPort": 80,
        "EnableLogging": False
    }
    snake_dict = {
        'port_mappings': [
            {
                'host_port': 80,
                'protocol': 'tcp',
                'container_port': 80
            }
        ],
        'container_port': 80,
        'enable_logging': False
    }

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

# Generated at 2022-06-12 23:09:42.834648
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:50.950499
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:59.340411
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"k1": "v1", "k2": "v2", "k3": {"nk1": "nv1", "nk2": "nv2"}}) == \
        {"k1": "v1", "k2": "v2", "k3": {"nk1": "nv1", "nk2": "nv2"}}

    assert camel_dict_to_snake_dict({'Tags': {'key': 'value'}}) == \
        {'tags': {'key': 'value'}}

    assert camel_dict_to_snake_dict({'target_group_arns': ['arn1', 'arn2']}, reversible=True) == \
        {'target_group_ar_ns': ['arn1', 'arn2']}


#

# Generated at 2022-06-12 23:10:07.004116
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # This returns dromedaryCase rather than true CamelCase.

    camel = {'HTTPEndpoint': {'Endpoint': 'https://example.com', 'HTTPPath': '/api/v1'}}
    snake = {'h_t_t_p_endpoint': {'endpoint': 'https://example.com', 'h_t_t_p_path': '/api/v1'}}

    assert snake == camel_dict_to_snake_dict(camel)



# Generated at 2022-06-12 23:10:14.981154
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'Test': 'test'}) == {'test': 'test'}
    assert camel_dict_to_snake_dict({'Test1': 'test'}) == {'test1': 'test'}
    assert camel_dict_to_snake_dict({'Test1': 1}) == {'test1': 1}
    assert camel_dict_to_snake_dict({'Test1Test2': 'test'}) == {'test1_test2': 'test'}
    assert camel_dict_to_snake_dict({'Test1Test2': 2}) == {'test1_test2': 2}

# Generated at 2022-06-12 23:10:26.211086
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:36.065690
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_response = {'DBClusterIdentifier': 'test', 'Endpoint': '127.0.0.1', 'Port': 3306,
                      'DBClusterMembers': [{'DBInstanceIdentifier': 'test-1', 'IsClusterWriter': True},
                                           {'DBInstanceIdentifier': 'test-2', 'IsClusterWriter': False}]}

    snake_response = {'db_cluster_identifier': 'test', 'endpoint': '127.0.0.1', 'port': 3306,
                      'db_cluster_members': [{'db_instance_identifier': 'test-1', 'is_cluster_writer': True},
                                             {'db_instance_identifier': 'test-2', 'is_cluster_writer': False}]}

    result = camel_dict_

# Generated at 2022-06-12 23:10:45.246338
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'AlfaBeta': 'AlfaBeta', 'A': {'B': {'C': 'C'}}}) == {'alfa_beta': 'AlfaBeta', 'a': {'b': {'c': 'C'}}}
    assert camel_dict_to_snake_dict({'AlfaBeta': 'AlfaBeta', 'HTTPEndpoint': 'http://example.com'}) == {'alfa_beta': 'AlfaBeta', 'http_endpoint': 'http://example.com'}

# Generated at 2022-06-12 23:10:53.894064
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Original data structure
    camel_dict = {
        'InstanceId': 'i-123456789',
        'InstanceType': 't2.micro',
        'Tags': [
            {
                'Key': 'Name',
                'Value': 'test'
            },
            {
                'Key': 'Environment',
                'Value': 'test'
            }
        ]
    }
    # Converted data structure

# Generated at 2022-06-12 23:11:02.185580
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:07.863588
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    sample_dict = {
        'CamelDict': [
            {'BoolParam': True, 'NestedDict': {'StringParam': 'sample'}},
            {'BoolParam': False, 'NestedDict': {'StringParam': 'example'}}
        ],
        'NotACamelDict': [{'EndpointUrl': 'test_url'}]
    }
    assert camel_dict_to_snake_dict(sample_dict, False) == {'camel_dict': [{'bool_param': True, 'nested_dict': {'string_param': 'sample'}}, {'bool_param': False, 'nested_dict': {'string_param': 'example'}}], 'not_a_camel_dict': [{'endpoint_url': 'test_url'}]}

# Generated at 2022-06-12 23:11:15.432924
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Basic testing
    camel_dict = {"fooBar": "test", "baz": "testing", "foo_bar": {"sayHey": "hello", "say_hey": "world"}}
    assert camel_dict_to_snake_dict(camel_dict) == {"foo_bar": "test", "baz": "testing", "foo_bar": {"say_hey": "hello", "say_hey": "world"}}
    # Reversible testing
    camel_dict_reversed = {"fooBar": "test", "bazHTTPEndpoint": "testing", "foo_bar": {"sayHTTPServer": "hello", "say_hey": "world"}}

# Generated at 2022-06-12 23:11:26.532641
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        'Blargh': 'A',
        'Thing': {
            'Blargh': 'B',
            'Flip': {
                'Flop': 'C',
            },
        },
        'OtherThing': [
            {
                'Blargh': 'D',
            },
            {
                'Thing': {
                    'Blargh': 'E',
                    'Flip': {
                        'Flop': 'F',
                    },
                },
            },
        ],
    }

    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict['blargh'] == 'A'
    assert snake_dict['thing']['flip']['flop'] == 'C'

# Generated at 2022-06-12 23:11:37.904966
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({"key": 123}) == {"key": 123}
    assert camel_dict_to_snake_dict({"mixedCase": 123}) == {"mixed_case": 123}
    assert camel_dict_to_snake_dict({"MixedCase": 123}) == {"_mixed_case": 123}
    assert camel_dict_to_snake_dict({"MixedCase": 123, "mixeD": 456}) == {"_mixed_case": 123, "mixe_d": 456}

# Generated at 2022-06-12 23:11:38.469114
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    pass

# Generated at 2022-06-12 23:11:46.703635
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'foo': {
            'bar': {
                'baz': 'foo',
                'httpEndpoint': {
                    'endpoint': 'foo',
                    'region': 'us-east-2'
                }
            }
        },
        'targetGroups': [
            {
                'targetGroupArn': 'arn-foo',
                'fooTargetGroup': {
                    'bar': 'foo'
                },
                'HTTPTargetGroup': {
                    'bar': 'foo',
                    'httpEnabled': True
                },
                'httpsEnabled': True,
                'tags': [
                    {
                        'key': 'foo'
                    }
                ]
            }
        ]
    }

    test_dict_copy = deepcopy(test_dict)
    snake_dict_1 = camel_

# Generated at 2022-06-12 23:11:56.419338
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # pylint: disable=bare-except
    try:
        from unittest import TestCase
    except ImportError:
        from unittest2 import TestCase


# Generated at 2022-06-12 23:12:05.464502
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel1 = {'Key1': 'Value1', 'Key2': 'Value2', 'Key3': 'value3'}
    assert camel_dict_to_snake_dict(camel1) == {
        'key1': 'Value1', 'key2': 'Value2', 'key3': 'value3'}
    assert camel_dict_to_snake_dict({'HTTPServer': 'server1', 'NTPEndpoint': 'ntp.com'}) == {
        'http_server': 'server1', 'ntp_endpoint': 'ntp.com'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'http.com'}, reversible=True) == {
        'h_t_t_p_endpoint': 'http.com'}

# Generated at 2022-06-12 23:12:13.813993
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test for simple dictionary
    test_camel_dict = {'Key': 'val'}
    result = camel_dict_to_snake_dict(test_camel_dict)
    assert (result == {'key': 'val'})

    # Test for nested dictionary
    test_camel_dict = {'OuterKey': {'InnerKey': 'val'}}
    result = camel_dict_to_snake_dict(test_camel_dict)
    assert (result == {'outer_key': {'inner_key': 'val'}})

    # Test for list
    test_camel_dict = {'Key': ['val']}
    result = camel_dict_to_snake_dict(test_camel_dict)
    assert (result == {'key': ['val']})

    # Test

# Generated at 2022-06-12 23:12:21.575151
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    correct_result = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': {
            'key3_1': 'value3_1',
            'key3_2': 'value3_2',
            'key3_3': {
                'key3_3_1': 'value3_3_1',
                'key3_3_2': 'value3_3_2',
            },
        },
        'key4': [
            'value4_1',
            'value4_2',
            {'key4_3_1': 'value4_3_1'},
        ],
    }


# Generated at 2022-06-12 23:12:32.225745
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        'FooBarBaz': 'fubar',
        'HTTPEndpoint': {
            'URL': 'https://foobar.com'
        }
    }

    camel_dict_reversible = {
        'HTTPEndpoint': {
            'URL': 'https://foobar.com'
        }
    }

    camel_dict_with_list = {
        'FooBarBaz': 'fubar',
        'HTTPEndpoint': [
            {
                'URL': 'https://foobar.com'
            },
            {
                'URL': 'https://foobar.com'
            }
        ]
    }


# Generated at 2022-06-12 23:12:41.188842
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'someKey': 'someValue',
                  'httpEndpoint': {'someOtherKey': 'someOtherValue'},
                  'httpEndpoints': [{'someOtherKey': 'someOtherValue'},
                                    {'someOtherKey': 'someOtherValue'}]}

    snake_dict = {'some_key': 'someValue',
                  'http_endpoint': {'some_other_key': 'someOtherValue'},
                  'http_endpoints': [{'some_other_key': 'someOtherValue'},
                                     {'some_other_key': 'someOtherValue'}]}

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict


# Generated at 2022-06-12 23:12:51.091298
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'TestDict': {'TestKey': 'TestValue', 'TestList': [{'TestDict': {'TestKey': 'TestValue', 'TestList': [{'TestDict': {'TestKey': 'TestValue'}}]}}]}, 'HTTPEndpoint': 'http://endpoint.com'}
    expected_dict = {'test_dict': {'test_key': 'TestValue', 'test_list': [{'test_dict': {'test_key': 'TestValue', 'test_list': [{'test_dict': {'test_key': 'TestValue'}}]}}]}, 'http_endpoint': 'http://endpoint.com'}
    result_dict = camel_dict_to_snake_dict(test_dict)
    assert expected_dict == result_dict


#

# Generated at 2022-06-12 23:13:00.972896
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': [{
            'E': '4',
            'F': '5',
            'G': '6'
        }],
        'H': {
            'I': [{
                'J': '7',
                'K': '8',
                'L': '9'
            }, {
                'J': '10',
                'K': '11',
                'L': '12'
            }]
        }
    }

# Generated at 2022-06-12 23:13:11.483112
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        dict(fooBar="foo", FooBar="bar"),
        reversible=False
    ) == dict(foo_bar="foo", foo_bar="bar")

    assert camel_dict_to_snake_dict(
        dict(HTTPEndpoint="http", AmazonS3Bucket="bucket"),
        reversible=False
    ) == dict(http_endpoint="http", amazon_s3_bucket="bucket")

    assert camel_dict_to_snake_dict(
        dict(fooBar="foo", FooBar="bar", fooBarList=[dict(fooBar="foo")]),
        reversible=False
    ) == dict(foo_bar="foo", foo_bar="bar", foo_bar_list=[dict(foo_bar="foo")])

    assert camel_dict_to

# Generated at 2022-06-12 23:13:17.623538
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    import json
    import pytest


# Generated at 2022-06-12 23:13:28.505541
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    def assert_it(camel_dict, reversible, ignore_list):
        snake_dict_response = {
            'allow_insecure_connections': True,
            'tags': {
                'Duplicates': 'retain',
                'Pants': 'off'
            }
        }
        assert(camel_dict_to_snake_dict(camel_dict, reversible, ignore_list) == snake_dict_response)

    camel_dict = {
        'AllowInsecureConnections': True,
        'Tags': {
            'Duplicates': 'retain',
            'Pants': 'off'
        }
    }

    assert_it(camel_dict, False, ())
    assert_it(camel_dict, True, ())

    # Test ignore_list

# Generated at 2022-06-12 23:13:36.034684
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:43.110594
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:54.420413
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'thing': 'value',
        'httpEndpoint': {
            'httpMethod': 'POST',
            'url': 'http://www.example.com',
            'params': {
                'subject': 'Action',
                'body': 'state changed to {$state}'
            },
            'auth': {
                'type': 'BASIC',
                'basic': {
                    'username': 'username',
                    'password': 'password'
                }
            }
        },
        'tags': {
            'http': 'endpoint'
        }
    }


# Generated at 2022-06-12 23:14:02.709473
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': 'http://www.example.com',
        'Tags': {
            'Key': 'Value',
            'SubKey': {
                'SubSubKey': 'Value'
            }
        }
    }
    expected_snake_dict = {
        'http_endpoint': 'http://www.example.com',
        'tags': {
            'Key': 'Value',
            'SubKey': {
                'SubSubKey': 'Value'
            }
        }
    }

# Generated at 2022-06-12 23:14:04.993318
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'do'}) == {'http_endpoint': 'do'}



# Generated at 2022-06-12 23:14:15.606041
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # test normal case
    input_camel_dict = {'HTTPEndpoint': {'Url': 'string', 'ClientCertificateId': 'string', 'AuthType': 'string', 'AuthConfiguration': {'Username': 'string', 'Password': 'string'}}, 'TCPEndpoint': {'Port': 0, 'ClientCertificateId': 'string', 'AuthType': 'string', 'AuthConfiguration': {'Username': 'string', 'Password': 'string'}}, 'Name': 'string', 'Tags': {'key': 'string'}, 'TargetType': 'string', 'TargetArn': 'string', 'CreatedAt': 'string', 'UpdatedAt': 'string'}

# Generated at 2022-06-12 23:14:28.450050
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'InstanceId': 'i-1234',
                  'IPAddress': '10.0.0.1',
                  'Domain': 'vpc',
                  'Monitoring': {'State': 'disabled'},
                  'Tags': [{'Key': 'Name',
                            'Value': 'ansible-test'},
                           {'Key': 'Env',
                            'Value': 'dev'}]
                  }

# Generated at 2022-06-12 23:14:36.357086
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    data_camel = {
        "DryRun": True,
        "Filters": [
            {
                "Name": "string",
                "Values": [
                    "string"
                ]
            }
        ],
        "MaxResults": 123,
        "NextToken": "string",
        "Tags": [
            {
                "Key": "string",
                "Value": "string"
            }
        ],
        "VolumeIds": [
            "string"
        ]
    }

# Generated at 2022-06-12 23:14:45.129132
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    simple_dict = { 'KeyOne': 'Value1',
                    'KeyTwo': { 'KeyThree': 'Value3' },
                    'KeyFour': [ 'ItemOne', 'ItemTwo']}
    simple_dict_snake = { 'key_one': 'Value1',
                          'key_two': { 'key_three': 'Value3' },
                          'key_four': [ 'ItemOne', 'ItemTwo']}

    complex_dict = { 'HTTPEndpoint': {
                                    'EndpointURL': 'http://example.com',
                                    'EndpointType': 'EXTERNAL',
                                    'StaticIPRequired': False
                                  }
                     }

# Generated at 2022-06-12 23:14:52.851329
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'Key1': {
            'Key2': 'Value2',
            'Key3': 'Value3'
        },
        'Key4': {
            'Key5': 'Value5',
            'Key6': [
                'Value6-1',
                'Value6-2',
                'Value6-3'
            ],
            'Key7': {
                'Key8': 'Value8'
            }
        }
    }

    assert camel_dict_to_snake_dict(camel_dict_to_snake_dict(test_dict)) == test_dict



# Generated at 2022-06-12 23:15:02.823008
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Simple test
    test_dict = {
        'HTTPHeader': {
           'HTTPHeaderName': "TestName",
           'HTTPHeaderValue': "TestValue",
        },
        'HTTPMethod': 'GET',
        'Path': '/',
        'Priority': 1
    }
    # Test that a shallow copy is returned
    output = camel_dict_to_snake_dict(test_dict)
    assert id(test_dict) != id(output)
    assert test_dict == output

    # Test that a deep copy is returned
    test_dict['HTTPHeader']['HTTPHeaderName'] = "NewName"
    assert test_dict != output

    # Test that keys are converted as expected
    assert set(test_dict.keys()) - set(output.keys()) == {'HTTPHeader'}

# Generated at 2022-06-12 23:15:10.169629
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:18.437860
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({
        "HTTPEndpoint": 12345,
        "Tags": {
            "Key": "value"
        }
    },
        reversible=True
    ) == {
        "h_t_t_p_endpoint": 12345,
        "tags": {
            "Key": "value"
        }
    }

    assert camel_dict_to_snake_dict({
        "HTTPEndpoint": 12345,
        "Tags": {
            "Key": "value"
        }
    }) == {
        "http_endpoint": 12345,
        "tags": {
            "key": "value"
        }
    }


# Generated at 2022-06-12 23:15:28.319106
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_val = {
        'fooFoo': 'bar',
        'FooBar': [
            'foo',
            {
                'fooFoo': 'bar',
                'HTTPS': 16172
            }
        ],
        'HTTPS': 16174,
        'Tags': {
            'Tag': 'test'
        }
    }
    expected_val = {
        'fooFoo': 'bar',
        'foo_bar': [
            'foo',
            {
                'fooFoo': 'bar',
                'h_t_t_p_s': 16172,
            }
        ],
        'h_t_t_p_s': 16174,
        'Tags': {
            'Tag': 'test'
        }
    }
    result = camel_dict_to_snake_

# Generated at 2022-06-12 23:15:37.296906
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        {
            "Tags": [
                {
                    "Key": "string",
                    "Value": "string"
                }
            ],
            "DesiredCapacity": 123,
            "NewInstancesProtectedFromScaleIn": True
        },
        reversible=True,
        ignore_list=["Tags"]
    ) == {
        "tags": [
            {
                "key": "string",
                "value": "string"
            }
        ],
        "desired_capacity": 123,
        "new_instances_protected_from_scale_in": True
    }


# Generated at 2022-06-12 23:15:46.157085
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'TestKey1': 'TestValue1',
                 'TestKey2': {'TestKey3': 'TestValue3',
                              'TestKey4': [{'TestKey5': 'TestValue5',
                                            'TestKey6': {'TestKey7': 'TestValue7'}}]}}
    expected_dict = {'test_key1': 'TestValue1',
                     'test_key2': {'test_key3': 'TestValue3',
                                   'test_key4': [{'test_key5': 'TestValue5',
                                                  'test_key6': {'test_key7': 'TestValue7'}}]}}

    result = camel_dict_to_snake_dict(test_dict)

# Generated at 2022-06-12 23:15:59.102017
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    data = {'instanceIds': ['i-2d4ad4eb7', 'i-4d4ad4eb3'],
            'TagFilters': [{'Key': 'env', 'Values': ['dev', 'test']}, {'Key': 'name', 'Values': ['ansible']}],
            'regions': 'us-west-2'}

    data_with_tag_filters = {'instanceIds': ['i-2d4ad4eb7', 'i-4d4ad4eb3'],
                             'TagFilters': [{'Key': 'env', 'Values': ['dev', 'test']}, {'Key': 'name', 'Values': ['ansible']}],
                             'regions': 'us-west-2'}


# Generated at 2022-06-12 23:16:07.739174
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:14.661511
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {
        'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict(
        {'fooBar': {'fooBarBaz': 'qux'}}) == {
        'foo_bar': {'foo_bar_baz': 'qux'}}
    assert camel_dict_to_snake_dict(
        {
            'fooBar': {
                'fooBarBaz': 'qux'},
            'corge': 'grault'}) == {
        'foo_bar': {
            'foo_bar_baz': 'qux'},
        'corge': 'grault'}

# Generated at 2022-06-12 23:16:19.907224
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_camel_dict = {
        'instanceId': 'i-723314',
        'instanceType': 'm3.medium',
        'tags': {'tag1': {
            'key1': 'val1',
            'key2': 'val2',
            },
            'tag2': 'val3',
        }
    }
    test_snake_dict = {
        'instance_id': 'i-723314',
        'instance_type': 'm3.medium',
        'tags': {'tag1': {
            'key1': 'val1',
            'key2': 'val2',
            },
            'tag2': 'val3',
        }
    }

# Generated at 2022-06-12 23:16:25.727865
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {"FooBar": {"SomeOtherKey": 1},
                 "Baz": {"Quux": {"Test": "Test"}},
                 "TopLevel": {"SecondLevel": {"Name": "John", "Age": 1}}}
    expected_dict = {"foo_bar": {"some_other_key": 1},
                     "baz": {"quux": {"test": "Test"}},
                     "top_level": {"second_level": {"name": "John", "age": 1}}}

    assert camel_dict_to_snake_dict(test_dict) == expected_dict


# Generated at 2022-06-12 23:16:34.841622
# Unit test for function camel_dict_to_snake_dict