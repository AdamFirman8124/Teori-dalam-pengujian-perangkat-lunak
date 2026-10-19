

# Generated at 2022-06-12 23:06:52.466192
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'doD': 'something'}) == {'do_d': 'something'}
    assert camel_dict_to_snake_dict({'DoD': 'something'}) == {'do_d': 'something'}
    assert camel_dict_to_snake_dict({'doiD': 'something'}) == {'doi_d': 'something'}
    assert camel_dict_to_snake_dict({'DOID': 'something'}) == {'d_o_i_d': 'something'}
    assert camel_dict_to_snake_dict({'doID': 'something'}) == {'do_i_d': 'something'}

# Generated at 2022-06-12 23:07:03.330869
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:10.660423
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    data = {
        "HTTPEndpoint": {
            "IpAddress": "192.168.0.1",
            "Port": 80,
            "HTTPEndpointDescription": "Lorem Ipsum",
            "HTTPPath": "lorem/ipsum"
        }
    }

    # Convert to CamelCase, and then back to SnakeCase
    camelCased = snake_dict_to_camel_dict(data)
    snakeCased = camel_dict_to_snake_dict(camelCased)

    # Assert that both dictionaries are equal
    assert snakeCased == data

# Generated at 2022-06-12 23:07:19.083959
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:30.969081
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    '''
    Test camel_dict_to_snake_dict function
    '''


# Generated at 2022-06-12 23:07:38.664861
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:45.364621
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:56.399990
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:04.589545
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    dict_to_convert = {
        'HTTPEndpoint': 'endpoint_a',
        'temp': {
            'Max': {
                'name': 'max',
                'value': '123',
                'unit': 'celsius'
            },
            'Min': {
                'name': 'min',
                'value': '50',
                'unit': 'celsius'
            }
        },
        'Tags': {
            'Name': 'test',
            'Description': 'Test tag'
        },
        'KeyPair': 'keypair'
    }


# Generated at 2022-06-12 23:08:14.769951
# Unit test for function dict_merge
def test_dict_merge():
    a = {
        'key': 'value',
        'key2': {'l1': 'v1', 'l2': 'v2'},
        'key3': 'value3',
    }
    b = {
        'key': 'newvalue',
        'key2': {'l1': 'newv1', 'l3': 'v3'},
        'key4': 'value4',
    }
    c = dict_merge(a, b)

    assert(c == {
        'key': 'newvalue',
        'key2': {'l1': 'newv1', 'l3': 'v3', 'l2': 'v2'},
        'key3': 'value3',
        'key4': 'value4',
    })



# Generated at 2022-06-12 23:08:26.675066
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert {'foo_bar': {'baz_qux': 'hello_world'}} == camel_dict_to_snake_dict({'fooBar': {'bazQux': 'hello_world'}})



# Generated at 2022-06-12 23:08:36.129209
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}, reversible=False) == {}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}, reversible=False) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'FooBar': 'baz'}, reversible=False) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz', 'qux': {'a': 'b'}}, reversible=False) == {'foo_bar': 'baz', 'qux': {'a': 'b'}}

# Generated at 2022-06-12 23:08:44.528549
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'Tags': {'Test': 'test'}, 'test': 'test'}) == \
        {'tags': {'Test': 'test'}, 'test': 'test'}
    assert camel_dict_to_snake_dict({'Tags': ['test', 'test'], 'test': 'test'}) == \
        {'tags': ['test', 'test'], 'test': 'test'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'test': 'test'}}) == \
        {'h_t_t_p_endpoint': {'test': 'test'}}


# Generated at 2022-06-12 23:08:55.009802
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    subdict_1 = {"HTTPHeaders": [{"headerName": "X-Amzn-Trace-Id", "headerValue": "Root=1-5c22f2d2-b50ac8194440f9261fe6d490"}]}
    subdict_2 = {"tags": [{"key": "service", "value": "accountservice"}]}
    camel_dict = {"HTTPEndpoint": "http://localhost:8080", "HTTPHeaders": [{"headerName": "X-Amzn-Trace-Id", "headerValue": "Root=1-5c22f2d2-b50ac8194440f9261fe6d490"}], "Tags": [{"key": "service", "value": "accountservice"}]}


# Generated at 2022-06-12 23:09:02.050046
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:13.344237
# Unit test for function recursive_diff
def test_recursive_diff():
    """Simple self test for the recursive_diff function."""

# Generated at 2022-06-12 23:09:22.722369
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'HTTPEndpoint': {'URL': 'http://127.0.0.1', 'Method': 'POST'},
                  'TargetGroups': [{'TargetGroupArn': 'targrp1'}, {'TargetGroupArn': 'targrp2'}],
                  'Tags': {'Key1': 'Value1', 'Key2': 'Value2'}}

# Generated at 2022-06-12 23:09:31.899477
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        'LaunchTime': '2019-03-07T22:14:50+00:00',
        'UserId': 123,
        'Tasks': [{
            'k1': 'v1',
            'k2': {
                'Subk': 'subv'
            }
        }],
        'Tags': {
            'key': 'value'
        }
    }

    # Test case sensitive dict keys
    assert camel_dict_to_snake_dict(d)['tags']['key'] == 'value'

    # Test conversion of camelized dict to snake dict
    assert camel_dict_to_snake_dict(d)['launch_time'] == '2019-03-07T22:14:50+00:00'

# Generated at 2022-06-12 23:09:42.579269
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test non-dict items
    assert recursive_diff(dict1="abc", dict2="abc") is None
    assert recursive_diff(dict1=1, dict2=2) == (1, 2)

    # Test different length
    assert recursive_diff(dict1={'k1': 'v1'}, dict2={'k1': 'v1', 'k2': 'v2'}) == \
        ({}, {'k2': 'v2'})
    # Test different value
    assert recursive_diff(dict1={'k1': 'v1'}, dict2={'k1': 'v2'}) == \
        ({'k1': 'v1'}, {'k1': 'v2'})
    # Test different keys and values

# Generated at 2022-06-12 23:09:45.752817
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_list = [{"fooBar": "foo_bar"}]
    camel_dict = camel_dict_to_snake_dict(camel_list[0])
    assert camel_dict == {"foo_bar": "foo_bar"}



# Generated at 2022-06-12 23:09:57.075984
# Unit test for function recursive_diff
def test_recursive_diff():
    left, right = recursive_diff({'a': 'a', 'b': 'c', 'd': 'e'}, {'a': 'a', 'b': 'b', 'f': 'g'})
    assert left == {'b': 'c', 'd': 'e'}
    assert right == {'b': 'b', 'f': 'g'}

    left, right = recursive_diff({'a': {'b': {'d': 'e'}}}, {'a': {'b': {'d': 'e'}}})
    assert left is None
    assert right is None

    left, right = recursive_diff({'a': {'b': {'d': 'e'}}}, {'a': {'b': {'d': 'f'}}})

# Generated at 2022-06-12 23:10:02.424261
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(camel_dict_to_snake_dict({"fooBarBaz": "quux"}) == {"foo_bar_baz": "quux"})
    assert(camel_dict_to_snake_dict({"dromedaryCase": "quux"}) == {"dromedary_case": "quux"})
    assert(camel_dict_to_snake_dict({"HTTPEndpoint": "quux"}) == {"h_t_t_p_endpoint": "quux"})
    assert(camel_dict_to_snake_dict({"HTTPSecretARN": "quux"}) == {"h_t_t_p_secret_a_r_n": "quux"})

# Generated at 2022-06-12 23:10:12.074888
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = dict(a=1, b=2, dict_c=dict(d=1, e=2),
                 f=dict(g=1, h=dict(i=1, j=2)),
                 k={'l': {'m': {'n': 1, 'o': 2}, 'p': 3}},
                 q=1, r=2, s=3)
    dict2 = dict(a=2, b=2, dict_c=dict(d=1, e=3),
                 f=dict(g=2, h=dict(i=1, j=3)),
                 k={'l': {'m': {'n': 1, 'o': 3}, 'p': 3}},
                 s=2, t=3)

# Generated at 2022-06-12 23:10:22.767351
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = dict(foo=dict(bar=dict(baz=dict(qux='qux', quux='quux'))),
                 joe='joe',
                 jane=dict(bob='bob', sally='sally'))
    dict2 = dict(foo=dict(bar=dict(baz=dict(qux='quxx', quuy='quuy'))),
                 joe='joe',
                 jane=dict(bob='bobb', sally='sally'),
                 jack=dict(jill='jill', hill='hill'))

# Generated at 2022-06-12 23:10:29.690279
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) is None
    assert recursive_diff({'a': '1'}, {'a': '1'}) is None
    assert recursive_diff({'a': '1'}, {}) == ({'a': '1'}, {})
    assert recursive_diff({}, {'a': '1'}) == ({}, {'a': '1'})
    assert recursive_diff({'a': '1', 'b': '2'}, {'b': '2'}) == ({'a': '1'}, {})
    assert recursive_diff({'a': '1'}, {'a': '1', 'b': '2'}) == ({}, {'a': '1', 'b': '2'})

# Generated at 2022-06-12 23:10:34.940133
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({"myKey": "myValue", "myEndpoint": {}, "myShallowDict": {"mySubKey": "mySubValue"}}) == \
        {"my_key": "myValue", "my_endpoint": {}, "my_shallow_dict": {"my_sub_key": "mySubValue"}}



# Generated at 2022-06-12 23:10:41.964968
# Unit test for function recursive_diff
def test_recursive_diff():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:10:49.418169
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        'Cluster': 'TestCluster',
        'HTTPEndpoint': {
            'Enabled': True,
            'HostName': 'TestHost'
        },
        'Tags': {
            'Key': 'Value'
        },
    }

    result_dict = camel_dict_to_snake_dict(test_dict, reversible=False)
    assert 'http_endpoint' in result_dict
    assert 'h_t_t_p_endpoint' not in result_dict
    assert 'Key' in result_dict['Tags']



# Generated at 2022-06-12 23:10:56.982711
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'A': {
            'A': {
                'A': 'value'
            }
        },
        'B': {
            'B': {
                'B': 'value'
            }
        },
        'C': {
            'C': {
                'C': 'value'
            }
        }
    }

    expected_snake_dict = {
        'a': {
            'a': {
                'a': 'value'
            }
        },
        'b': {
            'b': {
                'b': 'value'
            }
        },
        'c': {
            'c': {
                'c': 'value'
            }
        }
    }

    assert camel_dict_to_snake_dict(camel_dict) == expected

# Generated at 2022-06-12 23:11:04.769815
# Unit test for function recursive_diff
def test_recursive_diff():
    # Expected to return None
    same_dict1 = {'key1': '1', 'key2': 1}
    same_dict2 = {'key1': '1', 'key2': 1}
    assert recursive_diff(same_dict1, same_dict2) is None

    # Expected to return differences
    different_dict1 = {
        'key1': {
            'key3': '32',
            'key2': '1'},
        'key4': '4'}
    different_dict2 = {
        'key1': {
            'key3': '3',
            'key2': '1',
            'key5': '5'},
        'key4': '4'}

# Generated at 2022-06-12 23:11:13.452638
# Unit test for function recursive_diff
def test_recursive_diff():
    test1 = {'a': 1, 'b': 2, 'c': 3, 'e': {'f': 4, 'g': 5, 'h': 6, 'i': {'j': 7, 'k': 8, 'l': 9}}}
    test2 = {'a': 0, 'b': 2, 'c': 3, 'e': {'f': 0, 'g': 5, 'h': 6, 'i': {'j': 0, 'k': 8, 'l': 9}}}
    expected = ({'a': 1}, {'a': 0})
    assert recursive_diff(test1, test2) == expected

# Generated at 2022-06-12 23:11:18.637913
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff

    All test cases are commented out because boto3 is an extra dependency.
    """

    import json

    # pylint:disable=unused-variable
    def assert_deep_equal(seen, expected):
        if python_version < 3:
            assert json.dumps(seen, sort_keys=True) == json.dumps(expected, sort_keys=True)
        else:
            assert json.dumps(seen, sort_keys=True) == json.dumps(expected, sort_keys=True)

    from ansible.module_utils.six import PY2 as python_version

    # No difference between diff1 and diff2

# Generated at 2022-06-12 23:11:29.271385
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:36.843948
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'HostHeader': 'ansibledocs.amazon.com'}}, reversible=True) == \
        {'h_t_t_p_endpoint': {'host_header': 'ansibledocs.amazon.com'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'HostHeader': 'ansibledocs.amazon.com'}}, reversible=False) == \
        {'http_endpoint': {'host_header': 'ansibledocs.amazon.com'}}



# Generated at 2022-06-12 23:11:42.401514
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'one': 'one', 'two': {'three': 'three', 'four': 'four'}, 'five': 'five'}
    dict2 = {'one': 'one', 'two': {'three': 'four', 'four': 'three'}, 'five': 'five'}
    assert recursive_diff(dict1, dict2) == ({'two': ({'three': 'three'}, {'three': 'four'})}, {'two': ({'three': 'four'}, {'three': 'three'})})



# Generated at 2022-06-12 23:11:47.190250
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = dict(a=1, b=2, c=3, d=dict(a=1, b=2, e=dict(a=1, b=2)))
    dict2 = dict(a=1, b=2, c=4, d=dict(a=1, b=2, e=dict(a=1, b=2)))
    left, right = recursive_diff(dict1, dict2)
    assert left == {'c': 3}
    assert right == {'c': 4}

# Generated at 2022-06-12 23:11:56.985768
# Unit test for function recursive_diff
def test_recursive_diff():
    dict_a = {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key4": "value4",
            "key5": "value5"
        },
        "key6": {
            "key7": "value7",
            "key8": "value8"
        }
    }
    dict_b = {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key4": "value5"
        },
        "key6": {
            "key7": "value7",
            "key8": "value8"
        }
    }
    # Negative test case

# Generated at 2022-06-12 23:12:06.517839
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'key1': 'val1',
                  'Key2ForTest': 'val2',
                  'HTTPEndpoint': 'val3',
                  'Nested2': {
                      'nestedKey1': 'nestedVal1'
                  },
                  'NestedWithList': {
                      'nestedKey1': 'nestedVal1',
                      'nestedKey2': ['nestedVal2', 'nestedVal3']
                  }
                  }

    # Non reversible test
    snake_dict = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:12:15.247588
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff
    """
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    def execute_module(module_name=None, module_args=None, tmp=None,
                       delete_on_done=None, inject=None, complex_args=None,
                       **kwargs):
        return recursive_diff(dict1, dict2)

    with basic.register_module_argument_spec({
        'dict1': {'type': 'dict'},
        'dict2': {'type': 'dict'}
    }):
        basic._ANSIBLE_ARGS = None

# Generated at 2022-06-12 23:12:19.737853
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        "first": "Shooter",
        "last": "McGavin",
        "address": {
            "city": "North Miami",
            "state": "FL",
            "zip": 33176
        }
    }
    dict2 = {
        "first": "Dr.",
        "last": "McGavin",
        "address": {
            "city": "North Miami",
            "state": "FL",
            "zip": 33176
        }
    }
    dict3 = {
        "first": "Dr.",
        "last": "McGavin",
        "address": {
            "city": "North Miami",
            "state": "FL",
            "zip": 33176,
            "country": "US"
        }
    }

# Generated at 2022-06-12 23:12:32.625225
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:42.509053
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    This test is not testing the whole module

    """
    from ansible.module_utils.ec2 import AWSRetry

    class MockAWSRetry(AWSRetry):

        def __init__(self, backoff_mode, **kwargs):
            super(MockAWSRetry, self).__init__(**kwargs)
            self.backoff_mode = backoff_mode

    backoff_mode_settings = {
        'constant': (0, 2, 0),
        'exponential': (2, 0, 0.1),
        'full_jitter': (2, 0, 0.1),
        'equal_jitter': (2, 0, 0.1),
        'random_jitter': (2, 0, 0.1),
    }

    test_cases = []


# Generated at 2022-06-12 23:12:52.730398
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'Key': 'value', 'nested_key': {'camel_key': 'value', 'other': 'value'},
              'list_key': [{'camel_list_key': 'value', 'other': 'value'}],
              'list_with_nested_dict': [{'Key': 'value', 'nested_key': {'camel_key': 'value', 'other': 'value'}}],
              }
    result = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:13:00.911756
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {'k1': 'v1', 'k2': {'k21': 'v21', 'k22': [1, 2]}}
    d2 = {'k1': 'v1', 'k2': {'k21': 'v21', 'k22': [1, 2]}}
    assert not recursive_diff(d1, d2)
    d2 = {'k2': {'k21': 'v21', 'k22': [1, 2]}}
    assert recursive_diff(d1, d2) == ({'k1': 'v1'}, {})
    d2 = {'k1': 'v1', 'k2': {'k21': 'v21_new', 'k22': [1, 2]}}

# Generated at 2022-06-12 23:13:11.385539
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    r = {}
    r['ImportedAPIKeys'] = [{'StageKeys': [{'RestApiId': 'blah', 'StageName': 'foo'}], 'Id': '1234'}]
    r['UsagePlans'] = [{'UsagePlanId': '1234', 'Name': 'foo', 'Description': ''}]
    r['DomainName'] = 'blah'
    r['Tags'] = {'foo': 'bar', 'Foo': 'Bar'}
    r['EndpointConfiguration'] = {'Types': [], 'VpcEndpointIds': []}

    s = camel_dict_to_snake_dict(r, ignore_list=['Tags'])

# Generated at 2022-06-12 23:13:17.210811
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'url': 'https://example.com'}, 'HTTPExtension': {'url': 'https://example.com'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict['h_t_t_p_endpoint']['url'] == 'https://example.com'
    assert snake_dict['h_t_t_p_extension']['url'] == 'https://example.com'


# Generated at 2022-06-12 23:13:28.028746
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    def _assert_in(haystack, needle):
        # Recursively searches for needle in haystack.
        # needle and haystack can be dictionaries and lists.
        # If all values of needle are found in haystack, then the
        # function returns silently. If a value of needle is not
        # found in haystack, then an AssertionError is raised.

        # Base case for dictionaries
        if isinstance(haystack, dict) and isinstance(needle, dict):
            for k, v in haystack.items():
                _assert_in(v, needle[k])
        # Base case for lists

# Generated at 2022-06-12 23:13:35.425058
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test strings
    camel = 'CamelCase'
    non_camel = 'test'
    snake = 'snake_case'
    non_snake = 'test_'
    space_snake = 'snake case'
    dot_snake = 'snake.case'
    space_dot_snake = 'snake.case case'

    # Test basic string conversion
    assert _camel_to_snake(camel) == 'camel_case'
    assert _camel_to_snake(non_camel) == 'test'
    assert _camel_to_snake(snake) == 'snake_case'
    assert _camel_to_snake(non_snake) == 'test'

# Generated at 2022-06-12 23:13:42.751222
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    dict1 = dict(HttpMethod="GET", HttpUri="/test", HttpHeaders="Headers",
                 HttpContentType="ContentType", HttpBody="Body",
                 HttpDelaySeconds="DelaySeconds", HttpQueryParameters="QueryParameters")

    dict2 = dict(http_method="GET", http_uri="/test", http_headers="Headers",
                 http_content_type="ContentType", http_body="Body",
                 http_delay_seconds="DelaySeconds", http_query_parameters="QueryParameters")


# Generated at 2022-06-12 23:13:54.193622
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for recursive_diff"""

    # Positive test cases
    # 1. Two empty dictionaries
    assert not recursive_diff({}, {})

    # 2. Two non-empty dictionaries with different top-level keys
    assert recursive_diff({'key1': 'value1'}, {'key2': 'value2'}) == ({'key1': 'value1'}, {'key2': 'value2'})

    # 3. Two dictionaries with the same top-level, non-dict keys
    assert not recursive_diff({'key1': 'value1'}, {'key1': 'value2'})

    # 4. Two dictionaries with the same top-level, dict keys which are equal

# Generated at 2022-06-12 23:14:04.275751
# Unit test for function recursive_diff
def test_recursive_diff():
    from ansible.module_utils.six import PY3

    # test some basic cases
    assert recursive_diff({}, {}) is None
    assert recursive_diff({}, {'key1': 'val1'}) == ({}, {u'key1': u'val1'})
    assert recursive_diff({'key1': 'val1'}, {}) == ({u'key1': u'val1'}, {})
    assert recursive_diff({'key1': 'val1'}, {'key1': 'val1'}) is None

    # Test diff of nested dictionaries

# Generated at 2022-06-12 23:14:11.293574
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'camelCase': 'foo',
        'PascalCase': {
            'foo_bar': 'baz',
            'HttpEndpoint': 'http'
        }
    }
    expected = {
        'camel_case': 'foo',
        'pascal_case': {
            'foo_bar': 'baz',
            'http_endpoint': 'http'
        }
    }
    assert camel_dict_to_snake_dict(test_dict) == expected



# Generated at 2022-06-12 23:14:21.274042
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:32.101186
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test to ensure that camel_dict_to_snake_dict works, and that inverse_dict works
    """

    test_dict = {'Variable1': {'HTTPEndpoint': {'Port': 8080, 'Timeout': 5000}}, 'Variable2': 'Test'}
    test_dict_expected = {'variable1': {'h_t_t_p_endpoint': {'port': 8080, 'timeout': 5000}}, 'variable2': 'Test'}
    assert camel_dict_to_snake_dict(test_dict) == test_dict_expected

    # AccessibleByInternet is a special case; it's in the API as it's useful but not
    # actually a Setting in the database. It should not be converted to snake case.

# Generated at 2022-06-12 23:14:38.451776
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'TargetArn': 'arn:aws:sqs:us-east-1:000000000000:queue1',
            'Type': 'HTTP',
            'AuthConfiguration': {
                'SigningRegion': 'us-east-1',
                'SigningServiceName': 'execute-api'
            }
        }
    }
    # As a result of the call to camel_dict_to_snake_dict 'HTTPEndpoint'
    # is converted to 'http_endpoint' which cannot be converted back to
    # 'HTTPEndpoint' by snake_dict_to_camel_dict

# Generated at 2022-06-12 23:14:48.212307
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"Make": True, "Tags": [{"Key": "foo", "Value": "bar"}]}) == \
        {"make": True, "tags": [{"key": "foo", "value": "bar"}]}
    assert _camel_to_snake("HTTPEndpoint") == "h_t_t_p_endpoint"
    assert _camel_to_snake("HTTPEndpoint", reversible=True) == "h_t_t_p_endpoint"
    assert _camel_to_snake("HTTPDefaultEndpoint") == "h_t_t_p_default_endpoint"
    assert _camel_to_snake("HTTPDefaultEndpoint", reversible=True) == "htt_default_endpoint"
    assert _camel_

# Generated at 2022-06-12 23:14:58.367326
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from . import ec2_argument_spec
    camel_dict = deepcopy(ec2_argument_spec.argument_spec)
    snake_dict = camel_dict_to_snake_dict(camel_dict, False)
    assert isinstance(snake_dict, dict)
    assert isinstance(snake_dict['destination_tags'], dict)
    assert isinstance(snake_dict['tags'], dict)
    assert isinstance(snake_dict['ebs_block_device'], dict)
    assert isinstance(snake_dict['ebs_block_device']['encrypted'], dict)
    assert isinstance(snake_dict['ebs_block_device']['iops'], dict)

# Generated at 2022-06-12 23:15:06.857028
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPS': True,
        'HTTPEndpoint': {
            'Attributes': {
                'Key': 'foo',
                'Value': 'bar'
            }
        },
        'Tags': [{
            'Key': 'foo',
            'Value': 'bar'
        }],
        'TargetGroupARNs': ['target_group_1','target_group_2']
    }

# Generated at 2022-06-12 23:15:14.615108
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'FooBar': {'Baz': 'qux'}}) == {'foo_bar': {'baz': 'qux'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'Baz': 'qux'}}) == {'h_t_t_p_endpoint': {'baz': 'qux'}}
    assert camel_dict_to_snake_dict({'FooBar': {'Baz': 'qux'}}, reversible=True) == {'foo_bar': {'baz': 'qux'}}

# Generated at 2022-06-12 23:15:21.750769
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    sources = [
        {
            'SchemaVersion': 2,
            'ResourceType': 'AWS::CloudFormation::Stack',
            'Tags': [
                {
                    'Key': 'Environment',
                    'Value': 'SIT'
                },
                {
                    'Key': 'Foo',
                    'Value': 'Bar'
                }
            ],
            'Timeouts': {}
        },
        {
            'schemaVersion': 2,
            'resourceType': 'AWS::CloudFormation::Stack',
            'tags': [
                {
                    'key': 'Environment',
                    'value': 'SIT'
                },
                {
                    'key': 'Foo',
                    'value': 'Bar'
                }
            ],
            'timeouts': {}
        }
    ]


# Generated at 2022-06-12 23:15:37.159362
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    error_info = "test_camel_dict_to_snake_dict(reversible=%s)"

    # default cannot be reversed
    camel_dict = {'fooBar': 'bar', 'bazQux': 'qux', 'HTTPEndpoint': 'http_endpoint'}
    snake_dict = {'foo_bar': 'bar', 'baz_qux': 'qux', 'h_t_t_p_endpoint': 'http_endpoint'}

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict, error_info % False

    # reversible can be reversed
    assert snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict, reversible=True)) == camel_dict, error_info % True

    # test

# Generated at 2022-06-12 23:15:46.054862
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'SomeKey': 'some_val', 'otherKey': 'other_val'}) == {'some_key': 'some_val', 'other_key': 'other_val'}
    assert camel_dict_to_snake_dict({'someKey': 'some_val', 'otherKey': 'other_val'}) == {'some_key': 'some_val', 'other_key': 'other_val'}
    assert camel_dict_to_snake_dict({'SomeKey': 'some_val', 'otherKey': 'other_val'}, True) == {'s_o_m_e_key': 'some_val', 'other_key': 'other_val'}

# Generated at 2022-06-12 23:15:56.173550
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test that the function works with a simple example
    camel_dict = {'fooFoo': 'bar', 'bazBaz': 42}
    snake_dict = {'foo_foo': 'bar', 'baz_baz': 42}

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

    # Test that the function works with a complex example

# Generated at 2022-06-12 23:16:05.132298
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'fooBar': True}) == {'foo_bar': True}
    assert camel_dict_to_snake_dict({'fooBar': True, 'fOOBAR': True}) == {'foo_bar': True, 'f_o_o_b_a_r': True}
    assert camel_dict_to_snake_dict({'fooBar': {'fooBar': True}}) == {'foo_bar': {'foo_bar': True}}
    assert camel_dict_to_snake_dict({'fooBar': {'fooBar': True}},
                                     reversible=True) == {'foo_bar': {'f_o_o_b_a_r': True}}

    # Non-reversible conversion is allowed to lose information from the original.
    #  For

# Generated at 2022-06-12 23:16:12.785247
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_input = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3, 'keyFour': [{'keyFive': 5, 'keySix': 6, 'keySeven': 7}], 'keyEight': 8}
    snake_output = camel_dict_to_snake_dict(camel_input)
    assert snake_output == {'key_one': 1, 'key_two': 2, 'key_three': 3, 'key_four': [{'key_five': 5, 'key_six': 6, 'key_seven': 7}], 'key_eight': 8}

    camel_input = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3, 'keyFour': [{'keyFive': 5, 'keySix': 6, 'keySeven': 7}], 'keyEight': 8}


# Generated at 2022-06-12 23:16:18.356319
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    item = {
        "keyName": "common-key",
        "KeyPairList": [
            {
                "keyFingerprint": "xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx",
                "keyName": "common-key",
                "key-pair-id": "key-12345678"
            }
        ],
        "key-pair-id": "key-12345678",
        "keyFingerprint": "xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx"
    }


# Generated at 2022-06-12 23:16:26.636979
# Unit test for function recursive_diff
def test_recursive_diff():
    '''Recursive diff test'''
    test_dict1 = {'a': {'b': 1, 'c': 2}, 'd': [{'e': 3}]}
    test_dict2 = {'a': {'b': 3, 'c': 2}, 'd': [{'e': 3}]}
    test_dict3 = {'a': {'b': 1, 'c': 2, 'g': 0}, 'd': [{'e': 3, 'f': 0}]}

    assert recursive_diff(test_dict1, test_dict2) == ({'a': {'b': 1}}, {'a': {'b': 3}})

# Generated at 2022-06-12 23:16:35.513066
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_camel_dict = {'MasterUsername': 'username',
                       'MasterUserPassword': 'password',
                       'SourceRegion': 'source region',
                       'VpcSecurityGroupIds': [1234, 5678],
                       'Tags': [{'Key': 'foo', 'Value': 'bar'}],
                       'ServiceAccessSecurityGroup': 'access_group_1',
                       'NestedCamelDict': {'Key1': 'value1', 'Key2': 'value2', 'NestedCamelList': [{'Name': 'John', 'Age': 30}, {'Name': 'Jill', 'Age': 25}]}}
