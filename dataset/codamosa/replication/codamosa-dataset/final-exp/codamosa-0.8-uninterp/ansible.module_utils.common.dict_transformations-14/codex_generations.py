

# Generated at 2022-06-12 23:06:53.304260
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    import json
    from ansible.module_utils.ec2 import camel_dict_to_snake_dict, snake_dict_to_camel_dict

    with open('tests/unit/ec2_test_library/test_data/test_camel_to_snake.json') as json_data:
        original_dict = json.load(json_data)

    snake_dict = camel_dict_to_snake_dict(original_dict, reversible=True)
    camel_dict = snake_dict_to_camel_dict(snake_dict)

    assert(original_dict == camel_dict)

    # Ensure a list of dicts is recursively converted
    original_list_dict = {'target_instances': original_dict['TargetInstances']}
    snake_list_dict = camel_dict_to_

# Generated at 2022-06-12 23:07:04.219615
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    input_dict = {
        u"HTTPEndpoint": {
            u"Protocol": u"HTTP",
            u"Endpoint": u"s3-accelerate.amazonaws.com",
            u"Method": u"GET"
        },
        u"IPAddress": {
            u"IP": {
                u"SourceIP": u"192.0.2.0/24"
            }
        },
        u"Status": u"ENABLED",
        u"Tags": {
            u"mytag1": u"myvalue1",
            u"mytag2": u"myvalue2"
        }
    }


# Generated at 2022-06-12 23:07:14.366292
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test no differences
    dict1 = dict(key1=dict(key12=1, key13=2), key2=2)
    dict2 = dict(key1=dict(key12=1, key13=2), key2=2)
    assert recursive_diff(dict1, dict2) is None

    dict1 = dict(key1=dict(key12=1, key13=2), key2=2)
    dict2 = dict(key1=dict(key12=1, key13=2))
    dict3 = dict(key1=dict(key12=1, key13=2), key3=3)
    dict4 = dict(key1=dict(key12=1, key13=2), key2=3)

# Generated at 2022-06-12 23:07:21.221895
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Basic unit tests for camel_dict_to_snake_dict function."""


# Generated at 2022-06-12 23:07:32.535186
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({'a': 1}, {'a': 1}) is None, 'Left and right are equal.'
    assert recursive_diff({'a': 1}, {}) == ({'a': 1}, {}), 'Left has one key not on right.'
    assert recursive_diff({}, {'a': 1}) == ({}, {'a': 1}), 'Right has one key not on left.'
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2}), 'Key exists on both sides but with different values.'
    assert recursive_diff({'a': 1, 'b': {'x': 1}}, {'a': 1, 'b': {'x': 1}}) is None, 'Left and right are equal.'

# Generated at 2022-06-12 23:07:36.067242
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict_1 = {'key1': 1, 'key2': 2}
    snake_dict_1 = {'key1': 1, 'key2': 2}
    snake_dict_2 = camel_dict_to_snake_dict(camel_dict_1)

    assert snake_dict_1 == snake_dict_2


# Generated at 2022-06-12 23:07:42.568437
# Unit test for function recursive_diff
def test_recursive_diff():
    import json
    #
    # execute test loop
    #
    test_files = ["tests/files/recursive_diff_test.json", "tests/files/recursive_diff_test2.json"]
    for test_file in test_files:
        with open(test_file, "r") as file:
            data = json.load(file)
        for test in data:
            dict1 = test["dict1"]
            dict2 = test["dict2"]
            expected_result = test.get("expected")
            result = recursive_diff(dict1, dict2)
            assert sorted(result) == sorted(expected_result), test_file + ": " + test["message"]

# Generated at 2022-06-12 23:07:53.758911
# Unit test for function recursive_diff
def test_recursive_diff():
    """
    Quick test of recursive_diff function
    """
    import json
    a = {
        "a": "a",
        "b": "b",
        "c": {
            "a": "a",
            "b": "b"
        }
    }
    b = {
        "a": "a",
        "b": "b",
        "c": {
            "a": "a",
            "b": "b"
        }
    }
    assert recursive_diff(a, b) == None
    a = {
        "a": "a",
        "b": "b",
        "c": {
            "a": "a",
            "b": "b"
        }
    }

# Generated at 2022-06-12 23:08:03.129155
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit tests for recursive_diff"""

    dict1 = dict(
            key1 = dict(
                key1_1 = dict(
                    key1_1_1 = "value1_1_1"
                ),
                key1_2 = "value1_2"
            ),
            key2 = "value2"
        )

    dict2 = dict(
            key1 = dict(
                key1_1 = dict(
                    key1_1_1 = "value1_1_1",
                    key1_1_2 = "value1_1_2"
                ),
                key1_3 = "value1_3"
            ),
            key2 = "value2"
        )

    result = recursive_diff(dict1, dict2)
    assert result

# Generated at 2022-06-12 23:08:13.806373
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # String with CamelCase
    assert _camel_to_snake('ThisIsCamelCase') == 'this_is_camel_case'
    assert _camel_to_snake('CamelCase') == 'camel_case'
    assert _camel_to_snake('CC') == 'cc'

    # String with MixedCase
    assert _camel_to_snake('ThisIsMixedCase') == 'this_is_mixed_case'
    assert _camel_to_snake('MixedCase') == 'mixed_case'
    assert _camel_to_snake('MC') == 'mc'

    # String with CamelCase + _
    assert _camel_to_snake('This_Is_Camel_Case') == 'this_is_camel_case'
    assert _c

# Generated at 2022-06-12 23:08:26.503754
# Unit test for function dict_merge
def test_dict_merge():
    dict1 = dict(A=1, B=2, C=dict(D=3, E=4, F=dict(G=5, H=6, I=7)))
    dict2 = dict(A=10, B=20, C=dict(D=30, F=dict(I=70)))
    dict3 = dict_merge(dict1, dict2)
    # check that merging dict1 and dict2 produced dict3
    assert dict3 == dict(A=10, B=20, C=dict(D=30, E=4, F=dict(G=5, H=6, I=70)))
    # check that merging dict2 and dict1 produces correct result
    dict4 = dict_merge(dict2, dict1)

# Generated at 2022-06-12 23:08:36.027829
# Unit test for function dict_merge
def test_dict_merge():
    '''in case we ever move it, ensure that our custom version behaves
    the same as the stdlib one'''

    def assertDictEqual(d1, d2, msg=None):
        '''Python < 2.7 compatibility'''
        # Simple version taken from 2.7's Docs
        # http://docs.python.org/library/unittest.html
        first_flattened = set(d1.items())
        second_flattened = set(d2.items())
        if first_flattened != second_flattened:
            standardMsg = '%s != %s' % (safe_repr(d1, True),
                                        safe_repr(d2, True))
            self.fail(self._formatMessage(msg, standardMsg))

    # Given

# Generated at 2022-06-12 23:08:46.090470
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({'fooBar': None}) == {'foo_bar': None}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'baz'}) == {'h_t_t_p_endpoint': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': []}) == {'foo_bar': []}
    assert camel_dict_to_snake_dict({'fooBar': True}) == {'foo_bar': True}

# Generated at 2022-06-12 23:08:52.133704
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    a = {'prop1': 'val1', 'prop2': 'val2', 'Tags': {'prop1': 'val1', 'prop2': 'val2'}}
    b = {'prop1': 'val1', 'prop2': 'val2', 'tags': {'prop1': 'val1', 'prop2': 'val2'}}

    assert camel_dict_to_snake_dict(a) == b



# Generated at 2022-06-12 23:08:57.657122
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:07.917093
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'KeyName': 'test',
        'SecurityGroup': [
            'test'
        ],
        'ResourceTag': {
            'test': 'test',
            'test_test': 'test'
        },
        'Tags': {
            'Test': 'test',
            'TestTest': 'test'
        }
    }

    snake_dict_expected = {
        'key_name': 'test',
        'security_group': [
            'test'
        ],
        'resource_tag': {
            'test': 'test',
            'test_test': 'test'
        },
        'tags': {
            'Test': 'test',
            'TestTest': 'test'
        }
    }


# Generated at 2022-06-12 23:09:18.677432
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        'HTTPEndpoint': {
            'IsEnabled': True
        },
        'TargetGroupARNs': ['test_arn_01', 'test_arn_02'],
        'Tags': {
            'Key': 'TestKey',
            'Value': 'TestValue'
        }
    }

    # Expected converter
    expected = {
        'h_t_t_p_endpoint': {
            'is_enabled': True
        },
        'target_group_ar_ns': ['test_arn_01', 'test_arn_02'],
        'tags': {
            'Key': 'TestKey',
            'Value': 'TestValue'
        }
    }

    # Test converter
    assert camel_dict_to_snake_dict(camel_dict) == expected

# Generated at 2022-06-12 23:09:26.369776
# Unit test for function dict_merge

# Generated at 2022-06-12 23:09:36.690773
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def test_dict(test_name, camel_dict, expected_snake_output):
        actual_snake_dict = camel_dict_to_snake_dict(camel_dict)
        assert actual_snake_dict == expected_snake_output, "test %s failed, got %s, expected %s" % (test_name,
                                                                                                     actual_snake_dict,
                                                                                                     expected_snake_output)

    test_dict("simple_dict", {"Foo": "bar"}, {"foo": "bar"})


# Generated at 2022-06-12 23:09:46.705799
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test case 1
    input_camel_dict = {"Test": "Value", "dromedaryCase": {'SubValue': 'test',
                                                           'SubList': [1, 2, "3", ["4", "5"]]}}

    expected_snake_dict = {"test": "Value", "dromedary_case": {'sub_value': 'test',
                                                          'sub_list': [1, 2, "3", ["4", "5"]]}}

    actual_snake_dict = camel_dict_to_snake_dict(input_camel_dict)

    assert actual_snake_dict == expected_snake_dict, "Test case 1 failed: expected %s but got %s" % \
                                                     (expected_snake_dict, actual_snake_dict)

   

# Generated at 2022-06-12 23:09:53.630625
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        {'HTTPEndpoint': {'URL': 'http://example.com', 'customerHeader': {'headerKey': 'HeaderValue'}}}
    ) == {
        'h_t_t_p_endpoint': {'url': 'http://example.com', 'customer_header': {'header_key': 'HeaderValue'}}
    }



# Generated at 2022-06-12 23:10:02.415486
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:12.073906
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'foo': 1,
        'bar': 2,
        'baz': {
            'quux': 3,
            'corge': 4,
            'grault': {
                'garply': 5
            },
            'HTTPEndpoint': 3
        },
        'waldo': 6,
        'fred': 7,
        'plugh': 8
    }


# Generated at 2022-06-12 23:10:22.765131
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'TestKeyA': 'TestValueA',
        'TestKeyB': {
            'NestedKeyA': ['TestValueB1', 'TestValueB2'],
            'NestedKeyB': {
                'MoreNestedKeyA': 'TestValueC'
            }
        },
        'TestKeyC': []
    }
    expected_result = {
        'test_key_a': 'TestValueA',
        'test_key_b': {
            'nested_key_a': ['TestValueB1', 'TestValueB2'],
            'nested_key_b': {
                'more_nested_key_a': 'TestValueC'
            }
        },
        'test_key_c': []
    }

    assert camel_dict_to_snake

# Generated at 2022-06-12 23:10:31.058693
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:38.693755
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_cases = (
            # Basic cases, reversible set to True
            ({'Endpoint': 'arn', 'HTTPEndpoint': 'arn'}, {'endpoint': 'arn', 'h_t_t_p_endpoint': 'arn'}, True),
            # Irreversible cases, reversible set to False
            ({'Endpoint': 'arn', 'HTTPEndpoint': 'arn'}, {'endpoint': 'arn', 'http_endpoint': 'arn'}, False),
    )

    for camel_dict, expected_value, irreversible in test_cases:
        assert camel_dict_to_snake_dict(camel_dict, not irreversible) == expected_value

# Generated at 2022-06-12 23:10:48.506204
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Unit test for function camel_dict_to_snake_dict"""

    # Two tests, first without the reversible flag, then with.
    # Code is easier to read if we separate them and avoid repetitive code

    camel_dict = {'theAnswer': {'Is': 42},
                  'things': ['foo', 'bar', {'a': 'b', 'c': 'd'}],
                  'something': None,
                  'somethingElse': 'foo',
                  'something_else': 'bar'}
    snake_dict = {'the_answer': {'is': 42},
                  'things': ['foo', 'bar', {'a': 'b', 'c': 'd'}],
                  'something': None,
                  'something_else': 'bar',
                  'something_else_': 'foo'}
    assert camel_dict_to

# Generated at 2022-06-12 23:10:54.329416
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Test case to check the functionality of camel_dict_to_snake_dict"""
    camel_d = {"HTTPEndpoint": {
                                 "Path": "/",
                                 "Port": 80,
                                 "Protocol": "HTTP"
                                }
              }
    snake_d = camel_dict_to_snake_dict(camel_d, True)
    expected_d = {'h_t_t_p_endpoint': {'path': '/', 'port': 80, 'protocol': 'HTTP'}}
    assert snake_d == expected_d



# Generated at 2022-06-12 23:10:59.915976
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camelDict = {'Name': 'Test', 'Values': [{'name': 'first', 'value': 'string'}, {'name': 'second', 'value': 1}]}
    snakeDict = {'name': 'Test', 'values': [{'name': 'first', 'value': 'string'}, {'name': 'second', 'value': 1}]}
    assert camel_dict_to_snake_dict(camelDict, True, ['values']) == snakeDict


# Generated at 2022-06-12 23:11:10.133744
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'CamelCase': 'value'}) == {'camel_case': 'value'}
    assert camel_dict_to_snake_dict({'CamelCamelCase': 'value'}) == {'camel_camel_case': 'value'}
    assert camel_dict_to_snake_dict({'camelCamelCase': 'value'}) == {'camel_camel_case': 'value'}
    assert camel_dict_to_snake_dict({'camelCamelCase': 'value'}, reversible=True) == {'c_a_m_e_l_camel_case': 'value'}

# Generated at 2022-06-12 23:11:25.548291
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:35.796786
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def conv_dict(d):
        return camel_dict_to_snake_dict(d, reversible=True)

    def assert_camel_to_snake(test_input, expected_output, regex=True):
        assert_conv_dict(test_input, expected_output, regex=regex, output_function=conv_dict)

    def assert_conv_dict(test_input, expected_output, regex=True, output_function=None):
        if isinstance(test_input, str):
            test_input = json.loads(test_input)
        if isinstance(expected_output, str):
            expected_output = json.loads(expected_output)

        assert_result = re.match if regex else operator.eq
        real_output = output_function(test_input)

# Generated at 2022-06-12 23:11:43.973960
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'HTTPEndpoint': 'http_endpoint',
        'HTTPEndpointReversible': 'h_t_t_p_endpoint_reversible',
        'targetGroupARNs': 'target_group_ar_ns',
        'TargetGroupARNs': 'target_group_ar_ns'
    }

    for k, v in test_dict.items():
        assert _camel_to_snake(k, reversible=False) == v, \
            'camel_dict_to_snake_dict: %s did not match expected value %s' % (k, v)

# Generated at 2022-06-12 23:11:50.317554
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:59.990159
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:10.360615
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {
        "HTTPEndpoint": "https://http.endpoint",
        "Subnets": ["subnet-1", "subnet-2"],
        "Tags": {
            "key1": "value1",
            "key2": "value2"
        },
        "SecurityGroups": ["sg-1", "sg-2"]
    }

    snake_dict = {
        'http_endpoint': 'https://http.endpoint',
        'subnets': ['subnet-1', 'subnet-2'],
        'tags': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'security_groups': ['sg-1', 'sg-2']
    }


# Generated at 2022-06-12 23:12:19.296328
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = dict(
        HTTPEndpoint=dict(
            s_t_r_e_a_m_e_d_m_e_d_i_a_types=['mp4', 'webm'],
            access_log_format='%h %l %u %t "%r" %>s %b',
            authentication=dict(
                resources=dict(
                    type='string',
                    items=['*', '?foo=*']
                ),
                secret_ref=dict(
                    name='secret-name',
                    optional=True
                )
            )
        ),
        Tags=[
            dict(
                Key='k1',
                Value='v1'
            ),
            dict(
                Key='k2',
                Value='v2'
            )
        ]
    )

    snake_

# Generated at 2022-06-12 23:12:29.296793
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Url': 'http://www.example.com',
            'Enabled': True,
        },
        'HTTPSEndpoint': {
            'Enabled': False,
            'URL': 'https://www.example.com',
            'HTTPHeaders': {'CustomKey': 'CustomValue'}
        }
    }

    result = camel_dict_to_snake_dict(camel_dict, reversible=True)


# Generated at 2022-06-12 23:12:39.794322
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_input_dict = {
        "HasMoreDataPoints": False,
        "Label": "CPUUtilization",
        "Timestamps": [
            "2019-02-01T00:00:00Z",
            "2019-02-01T01:00:00Z",
            "2019-02-01T02:00:00Z"
        ],
        "Values": [
            "17.590428571428572",
            "18.39285714285714",
            "18.39285714285714"
        ]
    }

    # Expected output

# Generated at 2022-06-12 23:12:47.564617
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:00.029822
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test the recursive_diff function."""

    from ansible.module_utils.common.dict_transformations import recursive_diff

    # Test dictionaries
    dict1 = {"a": {"aa": "aa1", "ab": "ab1"}, "b": "b1", "c": "c1"}
    dict2 = {"a": {"aa": "aa1", "ab": "ab2", "ac": "ac2"}, "b": "b2", "d": "d2"}
    dict3 = {"a": {"aa": "aa1", "ab": {"aba": "aba1", "abb": "abb1"}},
             "b": "b1", "c": "c1"}

# Generated at 2022-06-12 23:13:10.348239
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({'TestCase': 'description', 'TestCaseTwo': {'Key1': 'value1'}}) == \
        {'test_case': 'description', 'test_case_two': {'key1': 'value1'}}
    assert camel_dict_to_snake_dict({'TestCase': 'description', 'TestCaseTwo': {'Key1': 'value1'}}, reversible=True) == \
        {'test_case': 'description', 'test_case_two': {'k_ey1': 'value1'}}

# Generated at 2022-06-12 23:13:15.746933
# Unit test for function dict_merge
def test_dict_merge():
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    c = { 'second' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    d = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } }  ,
         'second' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }

# Generated at 2022-06-12 23:13:26.072934
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test for simple dict
    camel_dict = {'FooBar': 'foo_bar'}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'foo_bar': 'foo_bar'}
    # Test for complex dict
    camel_dict = {'FooBar': {'FooBaz': 'foo_baz'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'foo_bar': {'foo_baz': 'foo_baz'}}
    # Test for list values
    camel_dict = {'FooBar': [{'FooBaz': 'foo_baz'}]}

# Generated at 2022-06-12 23:13:35.677704
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:41.798452
# Unit test for function dict_merge
def test_dict_merge():
    dict1 = {'foo': 1,
             'bar': {'bam': 1,
                     'barf': [1,2,3,4]},
             }
    dict2 = {'foo': 2,
             'bar': {'bam': 2,
                     'barf': [5,6,7,8]},
             'foobar': 3}

    merged = dict_merge(dict1, dict2)
    assert merged['foo'] == 2
    assert merged['bar']['bam'] == 2
    assert merged['bar']['barf'][3] == 8
    assert merged['foobar'] == 3


# Generated at 2022-06-12 23:13:53.831285
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:02.259322
# Unit test for function recursive_diff
def test_recursive_diff():

    dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': {'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}}
    dict2 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key7': {'key8': 'value8', 'key9': 'value9'}}
    result = recursive_diff(dict1, dict2)
    result_left = {'key3': {'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}}
    result_right = {'key3': 'value3', 'key7': {'key8': 'value8', 'key9': 'value9'}}
    assert result_left == result

# Generated at 2022-06-12 23:14:07.183956
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    snake_dict = {'string_property': 'foo', 'boolean_property': True, 'integer_property': 5}
    camel_dict = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert camel_dict['StringProperty'] == 'foo'
    assert camel_dict['BooleanProperty'] == True
    assert camel_dict['IntegerProperty'] == 5

# Generated at 2022-06-12 23:14:17.663721
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    dict0 = dict(a=1, b=dict(b2=2, b3=3))
    dict1 = snake_dict_to_camel_dict(dict0)
    dict2 = snake_dict_to_camel_dict(dict0, capitalize_first=True)
    assert dict0 == {'a': 1, 'b': {'b2': 2, 'b3': 3}}
    assert dict1 == {'a': 1, 'b': {'b2': 2, 'b3': 3}}
    assert dict2 == {'A': 1, 'B': {'B2': 2, 'B3': 3}}
    dict0 = dict(a=1, b=dict(b2=2, b3=[1, 2, 3]))

# Generated at 2022-06-12 23:14:33.716463
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Destination': 'https://www.example.com/my-webhook/',
            'EndpointType': 'HTTPS',
            'Id': 'my-http-endpoint-id',
            'Name': 'my-http-endpoint-name',
            'RetryPolicy': {
                'MaxRetries': 3,
                'MaxRetriesExceededBehavior': 'FIX_DELAY',
                'PerRetryTimeoutInSeconds': 30,
                'TotalRetryPeriodInSeconds': 90
            },
            'Tags': {
                'TagKey': 'TagValue'
            }
        }
    }

# Generated at 2022-06-12 23:14:40.986063
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:51.132209
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    # Case where there is one level of nesting
    test_dict_variable = {
        "foo": "bar",
        "baz": "baz",
        "foo_bar": {
            "foo": "bar",
            "baz": "baz"
        },
        "foo_baz": {
            "foo": "bar",
            "baz": "baz"
        }
    }
    # Expected dictionary
    expected_dict_variable = {
        "foo": "bar",
        "baz": "baz",
        "fooBar": {
            "foo": "bar",
            "baz": "baz"
        },
        "fooBaz": {
            "foo": "bar",
            "baz": "baz"
        }
    }
    # Nested dictionary


# Generated at 2022-06-12 23:14:54.911801
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge({"foo": {"bar": "baz"}, "hello": "world"},
                      {"foo": {"newkey": "newvalue"}}) == \
        {"foo": {"bar": "baz", "newkey": "newvalue"}, "hello": "world"}


# Generated at 2022-06-12 23:15:04.466577
# Unit test for function dict_merge
def test_dict_merge():
    a = {
        'foo': 1,
        'bar': {
            'baz': 2,
            'qux': 3
        },
        'one': 1,
        'two': 2,
        'three': {
            'four': 4,
            'five': 5,
            'six': 6
        }
    }
    b = {
        'foo': 10,
        'bar': {
            'baz': 20
        },
        'one': 'one',
        'two': 'two',
        'three': {
            'four': 'four',
            'five': 'five'
        }
    }


# Generated at 2022-06-12 23:15:12.531592
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'camelCaseKey': 'snake_case_value',
        'HTTPEndpoint': 'snake_case_endpoint',
        'Tags': [{'Key': 'key', 'Value': 'value'}]
    }

    assert camel_dict_to_snake_dict(test_dict, reversible=False) == {
        'camel_case_key': 'snake_case_value',
        'http_endpoint': 'snake_case_endpoint',
        'tags': [{'key': 'key', 'value': 'value'}]
    }

# Generated at 2022-06-12 23:15:20.007850
# Unit test for function recursive_diff
def test_recursive_diff():
    d1 = {
        'k1': 'v1',
        'k2': {
            'k2_1': 'v2_1_1',
            'k2_2': 'v2_2_1',
            'k2_3': 'v2_3_1'
        }
    }
    d2 = {
        'k1': 'v1',
        'k2': {
            'k2_1': 'v2_1_2',
            'k2_2': 'v2_2_2',
            'k2_3': 'v2_3_2'
        }
    }
    import pprint
    pprint.pprint(recursive_diff(d1, d2))



# Generated at 2022-06-12 23:15:30.762265
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    assert snake_dict_to_camel_dict({'foo_bar': {'a_b': 2}}) == {'fooBar': {'aB': 2}}
    assert snake_dict_to_camel_dict({'foo_bar': {'a_b': 2}}, capitalize_first=True) == {'FooBar': {'AB': 2}}
    assert snake_dict_to_camel_dict({'foo_bar': 2}) == {'fooBar': 2}
    assert snake_dict_to_camel_dict({'foo_bar': 2}, capitalize_first=True) == {'FooBar': 2}
    assert snake_dict_to_camel_dict({'foo_bar': None}) == {'fooBar': None}

# Generated at 2022-06-12 23:15:40.876317
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:48.331729
# Unit test for function dict_merge
def test_dict_merge():
    a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    assert (dict_merge(a, b)) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }

    c = { 'second' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    d = { 'second' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    assert (dict_merge(c, d))