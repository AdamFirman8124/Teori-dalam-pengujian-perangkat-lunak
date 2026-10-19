

# Generated at 2022-06-12 23:06:53.745449
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(Name='example', Password='password', Tags=[])
    snake_dict = dict(name='example', password='password', tags=[])
    assert camel_dict_to_snake_dict(camel_dict) == snake_dict

    camel_dict = dict(
        CidrBlock='127.0.0.0/24',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp',
        IpRanges=[
            {
                'CidrIp': '127.0.0.0/32',
                'Description': 'Localhost'
            },
            {
                'CidrIp': '127.0.0.0/24',
                'Description': 'Local subnet'
            }

        ]
    )


# Generated at 2022-06-12 23:06:58.739148
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"Hello": "World", "FooBar": {"FooBaz": "Baz"}, "Foo": "Bar"}, ignore_list=['Tags']) == {"hello": "World", "foo_bar": {"foo_baz": "Baz"}, "foo": "Bar"}



# Generated at 2022-06-12 23:07:07.329992
# Unit test for function recursive_diff
def test_recursive_diff():
    d = {
        'a': 1,
        'b': 2,
        'child': {
            'c': 3,
            'd': 4,
            'grandchild': {
                'e': 5
            }
        }
    }
    e = {
        'a': 1,
        'b': 2,
        'child': {
            'c': 3,
            'e': 5
        }
    }
    left, right = recursive_diff(d, e)
    assert left == {'child': {'d': 4, 'grandchild': {'e': 5}}}
    assert right == {'child': {'d': None, 'grandchild': None}}

# Generated at 2022-06-12 23:07:16.955478
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:28.137657
# Unit test for function recursive_diff
def test_recursive_diff():

    # Test for empty dictionaries
    assert recursive_diff({}, {}) == None

    # Test for dictionaries with same keys, one with different values
    assert recursive_diff({1:1, 'b':'2', 3:3}, {1:1, 'b':'0', 3:3}) == ({'b': '2'}, {'b': '0'})

    # Test for dictionary with extra keys in one vs the other
    assert recursive_diff({1:1, 'b':'2', 3:3}, {1:1, 'b':'0', 3:3, 'c': '5'}) == ({'b': '2'}, {'b': '0', 'c': '5'})

    # Test for dictionary containing nested dictionaries

# Generated at 2022-06-12 23:07:36.633927
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff()
    (Recursively diff two dictionaries)"""
    dict1_on_disk = dict(
        Name='test_resource',
        GroupName='test',
        InstanceType='t2.micro',
        KeyName='test_key',
        Tags=[
            {'Key': 'Name', 'Value': 'test_resource'},
            {'Key': 'Environment', 'Value': 'test'}
        ]
    )

# Generated at 2022-06-12 23:07:43.964986
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'A': {}}, reversible=True) == {'a': {}}
    assert camel_dict_to_snake_dict({'A': {}}, reversible=False) == {'a': {}}
    assert camel_dict_to_snake_dict({'A': {'B': {}}}, reversible=True) == {'a': {'b': {}}}
    assert camel_dict_to_snake_dict({'A': {'B': {}}}, reversible=False) == {'a': {'b': {}}}
    assert camel_dict_to_snake_dict({'A': [{}]}, reversible=True) == {'a': [{}]}

# Generated at 2022-06-12 23:07:55.040373
# Unit test for function recursive_diff
def test_recursive_diff():
    """ Unit test for recursive_diff """
    left = {'user_id': 'anand', 'age': 35, 'email': 'anand@test.com',
            'address': {'street': '11/1', 'city': 'Bangalore',
                        'state': 'Karnataka', 'pincode': 560001,
                        'signature': '123456'},
            'phones': [{'mobile': '9876543210', 'home': '1234561234'}]}

# Generated at 2022-06-12 23:08:03.889985
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"key1" : "value1", "key2" : "value2", "key3" : "value3" }
    snake_dict = camel_dict_to_snake_dict(camel_dict, False)
    assert snake_dict == {"key1" : "value1", "key2" : "value2", "key3" : "value3" }

    camel_dict = {"Key1" : "value1", "key2" : "value2", "key3" : "value3" }
    snake_dict = camel_dict_to_snake_dict(camel_dict, False)
    assert snake_dict == {"key1" : "value1", "key2" : "value2", "key3" : "value3" }


# Generated at 2022-06-12 23:08:09.462518
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_list = [
        ['abcDef', 'abc_def'],
        ['String', 'string'],
        ['HTTPEndpoint', 'h_t_t_p_endpoint'],
        ['99Bottles', '99_bottles'],
    ]

    for test in test_list:
        assert(_camel_to_snake(test[0]) == test[1])



# Generated at 2022-06-12 23:08:22.603577
# Unit test for function recursive_diff
def test_recursive_diff():
    assert None == recursive_diff(
        {},
        {}
    )
    assert ({'b': 'value'}, {'a': 'value'}) == recursive_diff(
        {'a': 'value'},
        {'b': 'value'}
    )
    assert ({'a': 'value'}, {'b': 'value'}) == recursive_diff(
        {'a': 'value', 'b': 'value'},
        {'b': 'value'}
    )
    assert ({'b': 'value'}, {'a': 'value'}) == recursive_diff(
        {'b': 'value'},
        {'a': 'value', 'b': 'value'}
    )
    assert ({'b': 'value', 'z': 'value'}, {'a': 'value'}) == recursive_

# Generated at 2022-06-12 23:08:32.245011
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = { 'HTTPEndpoint':{'attribute': ['a','b','c'], 'link': 'link1'}, 'HTTPSEndpoint':{'attribute': ['a','b','c'], 'link': 'link1'}}
    expected_output = {'h_t_t_p_endpoint': {'attribute': ['a', 'b', 'c'], 'link': 'link1'}, 'h_t_t_p_s_endpoint': {'attribute': ['a', 'b', 'c'], 'link': 'link1'}}
    assert(camel_dict_to_snake_dict(input_dict) == expected_output)

    input_dict = {'Id': 'testId', 'Name': {'test': 'test'}}

# Generated at 2022-06-12 23:08:40.128119
# Unit test for function dict_merge
def test_dict_merge():
    a = {'key1': {'nest_key1': 'nest_value1'}}
    b = {'key1': {'nest_key1': 'nest_value1', 'nest_key2': 'nest_value2'}}
    c = {'key1': {'nest_key1': 'nest_value1', 'nest_key2': {'nest_key3': 'nest_value3'}}}
    d = {'key1': {'nest_key1': 'nest_value1', 'nest_key2': {'nest_key3': 'nest_value3'}}, 'key2': 'value2'}

    assert dict_merge(a, b) == b
    assert dict_merge(b, c) == d
    assert dict

# Generated at 2022-06-12 23:08:50.610204
# Unit test for function recursive_diff
def test_recursive_diff():

    dict1 = dict(changed=False,
                 invocations=dict(module_args=dict(a="a", b="b")),
                 item=dict(ansible_host="host1",
                           ansible_hostname="host1",
                           ansible_network_os="ios",
                           ansible_ssh_host="host1",
                           ansible_ssh_host_key_file=
                           [u"/home/a/.ssh/known_hosts", u"/home/a/.ssh/config"],
                           ansible_ssh_host_key_checking=False),
                 no_log=False)


# Generated at 2022-06-12 23:08:59.484323
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unittest for function recursive_diff
    """
    dict1 = {
        "key1": [1, 2, 3],
        "key2": {
            "subkey1": 1,
            "subkey2": [2, 3, 4, 5],
        },
        "key3": {
            "subkey1": {
                "subsubkey1": 1,
                "subsubkey2": 2,
            },
        },
    }

# Generated at 2022-06-12 23:09:10.218613
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'FooBar': {
            'a': 1,
            'b': 2,
            'nested': {
                'fooBar': '1',
                'barFoo': '2'
            }
        },
        'BarBaz': [
            {
                'a': 1,
                'b': 2,
                'nested': {
                    'fooBar': '1',
                    'barFoo': '2'
                }
            },
            {
                'a': 3,
                'b': 4,
                'nested': {
                    'fooBar': '3',
                    'barFoo': '4'
                }
            }
        ],
        'Tags': {
            'tagKey': 'tagValue'
        }
    }


# Generated at 2022-06-12 23:09:20.432593
# Unit test for function dict_merge
def test_dict_merge():
    # Simple merge
    d1 = {'a': 1}
    d2 = {'b': 2}
    d3 = dict_merge(d1, d2)
    d3.should.be.equal({'a': 1, 'b': 2})

    # Overwrite value
    d1 = {'a': 1}
    d2 = {'a': 2}
    d3 = dict_merge(d1, d2)
    d3.should.be.equal({'a': 2})

    # Merge 2 levels deep
    d1 = {'a': {'x': 1}}
    d2 = {'a': {'y': 2}}
    d3 = dict_merge(d1, d2)

# Generated at 2022-06-12 23:09:26.657100
# Unit test for function recursive_diff
def test_recursive_diff():

    """Test case for recursive_diff function"""

    dict1 = {'a':1,'b':2,'c':{'d':6,'e':3}}
    dict2 = {'a':1,'b':2,'c':{'d':7,'e':3}}
    dict3 = {'a':1,'b':2,'c':{'d':6,'e':3,'f':6}}
    dict4 = {'a':1,'b':2,'c':{'d':7,'e':3,'f':7}}
    dict5 = {'a':1,'b':2}
    dict6 = {'f':3,'g':4}
    dict7 = {'a':1,'b':2,'c':{'d':6,'e':8,'f':6}}

# Generated at 2022-06-12 23:09:30.740504
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Simple test
    camel_dict = {'FooBar': 12345}
    test = camel_dict_to_snake_dict(camel_dict)
    assert test == {'foo_bar': 12345}

    # Test not overwriting existing value
    camel_dict = {'FooBar': 12345, 'foo_bar': 6789}
    test = camel_dict_to_snake_dict(camel_dict)
    assert test == {'foo_bar': 6789}

    # Test complex value overwriting
    camel_dict = {'foo_bar': {'FooBar': 12345}}
    test = camel_dict_to_snake_dict(camel_dict)
    assert test == {'foo_bar': {'foo_bar': 12345}}

    # Test reversible (ensure Tags

# Generated at 2022-06-12 23:09:41.393466
# Unit test for function recursive_diff
def test_recursive_diff():
    from collections import OrderedDict

    def check(a, b, expected):
        result = recursive_diff(a, b)
        assert result == expected, \
            "result {0} does not match expected {1}".format(result, expected)

    # Basic test for correctness
    a = { 'a': 1, 'b': 1, 'c': { 'c1': 1} }
    b = { 'a': 2, 'b': 2, 'c': { 'c1': 2} }
    expected = ({ 'a': 1, 'b': 1 }, { 'a': 2, 'b': 2 })
    check(a, b, expected)
    a = { 'a': 1, 'b': 1, 'c': { 'c1': 1} }

# Generated at 2022-06-12 23:09:57.482195
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict1 = {
        'HTTPEndpoint': {
            'EndpointURL': "string",
            'Format': "string",
            'AuthorizationHeader': "string",
        },
        'Tags': {
            'Key': "string"
        },
        'ListParam': ["string"],
        'StringParam': "string",
    }
    expected_dict1 = {
        'h_t_t_p_endpoint': {
            'endpoint_u_r_l': "string",
            'format': "string",
            'authorization_header': "string",
        },
        'tags': {
            'Key': "string"
        },
        'list_param': ["string"],
        'string_param': "string",
    }
    result_dict1 = camel_dict_to_snake

# Generated at 2022-06-12 23:10:03.494402
# Unit test for function dict_merge
def test_dict_merge():
    d1 = {'x': 1, 'y': {'a': 5, 'b': 10}}
    d2 = {'x': 5, 'y': {'a': 5, 'c': 15}}
    d1_copy = deepcopy(d1)
    d2_copy = deepcopy(d2)
    d1_copy['y']['c'] = 15
    d1_copy['x'] = 5
    assert dict_merge(d1, d2) == d1_copy
    assert d1 == d2
    assert d2 == d2_copy


# Generated at 2022-06-12 23:10:12.952561
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    test_dict = {
        'foo_bar': 'baz',
        'foo_goo': {
            'bar_baz': 'qux',
            'bar_qux': [
                'quxx',
                {
                    'corge_grault': 'garply',
                    'corge_waldo': 'fred',
                    'corge_plugh': 'xyzzy',
                    'corge_thud': [
                        'test1',
                        'test2'
                    ]
                }
            ]
        }
    }
    res = snake_dict_to_camel_dict(test_dict)

# Generated at 2022-06-12 23:10:23.939279
# Unit test for function recursive_diff
def test_recursive_diff():
    from collections import OrderedDict
    assert recursive_diff({}, {}) is None
    assert recursive_diff(['a', 'b'], ['a', 'c']) == (['b'], ['c'])
    assert recursive_diff({'a': 'b'}, {'a': 'b'}) is None
    assert recursive_diff({'a': 'b'}, {'a': 'c'}) == ({'a': 'b'}, {'a': 'c'})
    assert recursive_diff({1: {2: 3}}, {1: {3: 4}}) == ({1: {2: 3}}, {1: {3: 4}})

# Generated at 2022-06-12 23:10:31.780907
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():

    test_case = [
        {
            "snake_key": 1,
            "snake_key_2": [
                1, 2, 3
            ],
            "snake_key_3": {
                "snake_key": 1,
                "snake_key_2": 2
            },
            "snake_key_4": {
                "snake_key": 1,
                "snake_key_2": [
                    {
                        "snake_key": 1
                    }, {
                        "snake_key": 2
                    }
                ]
            }
        }
    ]

    for case in test_case:
        if snake_dict_to_camel_dict(case) == case:
            raise ValueError("Failed to convert %s", case)


# Generated at 2022-06-12 23:10:40.424306
# Unit test for function snake_dict_to_camel_dict

# Generated at 2022-06-12 23:10:45.974490
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    camel_dict = {'InstanceIds': [], 'MaxResults': 100, 'NextToken': '', 'Tags': {'tag_key': 'tag_value'}}
    result = snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict, True, ignore_list=['Tags']))
    assert result == camel_dict


# Generated at 2022-06-12 23:10:54.398762
# Unit test for function dict_merge
def test_dict_merge():
    dict1 = dict(a=1, b=2, c=3, d=dict(e=4, f=5))
    dict2 = dict(a=1, b=dict(c=2, d=3), e=4)
    dict3 = dict(a=1, b=2, c=3, d=dict(e=4, f=5))
    dict4 = dict(a=1, b=dict(c=2, d=3), e=4, f=dict(h=5))
    dict5 = dict(a=1, b=dict(c=dict(d=2)))

    dict_merge(dict1, dict2)
    assert dict1 == dict3

    dict_merge(dict2, dict1)
    assert dict2 == dict4


# Generated at 2022-06-12 23:11:02.665727
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    import collections

    snake_dict = {
        "a_nested_complex_dict": {
            "deep_nested_dict": {
                "a_key": "a_value"
            },
            "a_key": "a_value",
            "a_list": [
                "a_value_1",
                "a_value_2"
            ]
        },
        "a_key": "a_value",
        "a_list": [
            "a_value_1",
            "a_value_2"
        ]
    }

    # Check the function is behaving as expected
    # (test for camelCase keys)
    camel_dict = snake_dict_to_camel_dict(snake_dict)

    assert(isinstance(camel_dict, collections.Mapping))

# Generated at 2022-06-12 23:11:12.779814
# Unit test for function recursive_diff
def test_recursive_diff():
    print (recursive_diff({"firstName":"John", "lastName":"Doe", "age":0, "skill":{"python":True, "ansible":False}, "tome":{"linux":True, "ansible":True}},
    {"firstName":"John", "lastName":"Doe", "age":0, "skill":{"python":False, "ansible":True}, "tome":{"linux":True, "ansible":True}}))

# Generated at 2022-06-12 23:11:25.351564
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff."""
    dict1 = {'a': {1: "one", 2: "two"}, 'b': {3: "three", 4: "four"}}
    dict2 = {'a': {1: "one", 2: "two"}, 'b': {3: "three", 4: "five"}}
    dict3 = {'a': {1: "one", 2: "two"}, 'b': {3: "three", 4: "four"}, 'c': {5: "five"}}
    assert recursive_diff(dict1, dict2) == ({'b': {4: 'four'}}, {'b': {4: 'five'}})
    assert recursive_diff(dict1, dict3) == ({}, {'c': {5: "five"}})

# Generated at 2022-06-12 23:11:35.673053
# Unit test for function recursive_diff

# Generated at 2022-06-12 23:11:43.715445
# Unit test for function recursive_diff
def test_recursive_diff():
    left = {
        'foo': 'bar',
        'bar': {
            'bar1': 'foo1',
            'bar2': 'foo2',
            'bar3': {
                'bar3a': 'foo3a',
                'bar3b': 'foo3b',
            },
            'bar4': ['a', 'b', 'c', 'd', 'e'],
        },
        'foobar': [
            {'foobar1': 'foobar1'},
            {'foobar2': 'foobar2'},
            {'foobar3': 'foobar3'},
            {'foobar4': 'foobar4'},
        ],
        'barfoo': 'foobar',
    }

# Generated at 2022-06-12 23:11:51.156208
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    # snake_cased to dromedaryCase
    assert snake_dict_to_camel_dict({'all_kinds_of_snake': {'need_to_be_camelized': 'correct?'}}) == {'allKindsOfSnake': {'needToBeCamelized': 'correct?'}}
    # snake_cased to CamelCase
    assert snake_dict_to_camel_dict({'all_kinds_of_snake': {'need_to_be_camelized': 'correct?'}}, capitalize_first=True) == {'AllKindsOfSnake': {'NeedToBeCamelized': 'correct?'}}



# Generated at 2022-06-12 23:12:00.444311
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = dict(list1=[1,2,3], list2=[3,2,1], dict1=dict(a=1, b=2, c=3, d=4))
    dict2 = dict(list1=[2,2,3], list2=[1,2,3], dict1=dict(a=1, b=1, c=3, d=4))
    result = recursive_diff(dict1, dict2)
    assert result == ({'list1': [1]}, {'list1': [2], 'list2': [3, 1], 'dict1': {'b': 2}})


# Generated at 2022-06-12 23:12:10.744477
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'x':5, 'y':{'a':'abc', 'b':'bcd', 'c':3}, 'z':'aaa'}
    dict2 = {'y':{'a':'abc', 'c':3, 'd':3}, 'z':'bbb', 'w':'bcd'}
    assert recursive_diff(dict1, dict2) == ({'x': 5, 'z': 'aaa'}, {'w': 'bcd', 'y': {'b': 'bcd', 'd': 3}, 'z': 'bbb'})
    dict3 = {'x':5, 'y':{'a':'abc', 'b':'bcd', 'c':3}, 'z':'aaa'}

# Generated at 2022-06-12 23:12:19.516032
# Unit test for function snake_dict_to_camel_dict

# Generated at 2022-06-12 23:12:26.249326
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    assert snake_dict_to_camel_dict({'load_balancers': {'target_group_arns': [],
                                                       'load_balancer_names': [],
                                                       'target_group_arn': '',
                                                       'load_balancer_name': ''}},
                                   True) == {'LoadBalancers': {'TargetGroupArns': [],
                                                               'LoadBalancerNames': [],
                                                               'TargetGroupArn': '',
                                                               'LoadBalancerName': ''}}



# Generated at 2022-06-12 23:12:37.394532
# Unit test for function dict_merge
def test_dict_merge():
    dict1 = dict.fromkeys(('A', 'B', 'C', 'D', 'E'))
    dict2 = dict.fromkeys(('B', 'C', 'E', 'F'))
    dict3 = dict.fromkeys(('D', 'E', 'F', 'G'))
    dict4 = dict.fromkeys(('D', 'E', 'F', 'G'))

    # Test case 1
    dict_merge(dict1, dict2)
    dict1_expected = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    assert dict1 == dict1_expected

    # Test case 2
    dict_merge(dict2, dict3)

# Generated at 2022-06-12 23:12:46.025063
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    thing = {
        'snake': [
            {
                'case': [
                    {'dict': None}
                ]
            },
        ],
        'pluralized_with_underscore': {
            'key': 'value',
        },
        'pluralized_without_underscore': {
            'key': 'value',
        },
        'has_spaces': {
            'key': 'value',
        },
        'tags': {
            'some': 'tags'
        }
    }