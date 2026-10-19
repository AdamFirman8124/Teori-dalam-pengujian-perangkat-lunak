

# Generated at 2022-06-12 23:06:53.650872
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # single level dictionary
    camel_dict = {'HTTPEndpoint': 'http://data.example.com/'}
    snake_dict = {'http_endpoint': 'http://data.example.com/'}
    assert camel_dict_to_snake_dict(camel_dict, False) == snake_dict
    # multiple level dictionary
    camel_dict = {'Foo': {'HTTPEndpoint': 'http://data.example.com/'}}
    snake_dict = {'foo': {'http_endpoint': 'http://data.example.com/'}}
    assert camel_dict_to_snake_dict(camel_dict, False) == snake_dict
    # multiple level dictionary, with list

# Generated at 2022-06-12 23:07:01.419799
# Unit test for function recursive_diff
def test_recursive_diff():
    a = {'a': 1, 'b': {'c': 3, 'd': 4}, 'e': 5}
    b = {'a': 1, 'b': {'c': 3, 'd': 6}, 'f': 5}

    expected = ({'b': {'d': 4}, 'e': 5}, {'b': {'d': 6}, 'f': 5})

    result = recursive_diff(a, b)

    assert result == expected, "Recursive diff does not work as expected"

test_recursive_diff()

# Generated at 2022-06-12 23:07:11.534249
# Unit test for function recursive_diff
def test_recursive_diff():

    # Default is dictionary with no differences
    assert not recursive_diff({}, {})

    # Single level dictionaries differ because they have different keys
    left, right = recursive_diff({'name': 'foo'}, {'name': 'bar'})
    assert set(left) == set(right)
    assert left['name'] == 'foo'
    assert right['name'] == 'bar'

    # Single level dictionaries have same keys but one key is different
    left, right = recursive_diff({'name': 'foo', 'id': 123}, {'name': 'bar', 'id':123})
    assert left == {'name': 'foo'}
    assert right == {'name': 'bar'}

    # Two level dictionaries have different keys at different levels

# Generated at 2022-06-12 23:07:19.604343
# Unit test for function recursive_diff
def test_recursive_diff():
    assert recursive_diff({}, {}) == None

    assert recursive_diff({'a': {'b': {}}}, {}) == ({'a': {'b': {}}}, {})

    assert recursive_diff({}, {'a': {'b': {}}}) == ({}, {'a': {'b': {}}})

    assert recursive_diff({'a': {'b': {}}}, {'a': {'b': {}}}) == None

    assert recursive_diff({'a': {'b': {}}}, {'a': {'c': {}}}) == ({'a': {'b': {}}}, {'a': {'c': {}}})


# Generated at 2022-06-12 23:07:31.312125
# Unit test for function recursive_diff
def test_recursive_diff():
    # dictionary of dictionaries
    a = {'a':
            {'x':1, 'y':2},
         'z':3}
    b = {'a':
            {'x':1, 'y':2},
         'z':4}
    assert recursive_diff(a,b) == ({}, {'z':4})

    a = {'a':
            {'x':1, 'y':2},
         'z':3}
    b = {'a':
            {'y':2},
         'z':3}
    assert recursive_diff(a,b) == ({'a':{ 'x':1}}, {'a':{}})

    a = {'a':
            {'x':1, 'y':2},
         'z':3}

# Generated at 2022-06-12 23:07:38.964810
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:49.460213
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff

    Compare:
    * empty dicts
    * dicts with same keys but differnt values
    * dicts with different keys and values
    * dicts with dict values
    """

    dict1 = dict()
    dict2 = dict()
    assert recursive_diff(dict1, dict2) is None

    dict1 = dict(abcd=1234)
    dict2 = dict(abcd=1234)
    assert recursive_diff(dict1, dict2) is None

    dict1 = dict(abcd=4321)
    dict2 = dict(abcd=1234)
    result = recursive_diff(dict1, dict2)
    assert dict1 == result[0]
    assert dict2 == result[1]

    dict1 = dict(abcd=1234)
    dict2

# Generated at 2022-06-12 23:07:59.815985
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for recursive_diff

    :return: None
    """

    import pytest

    # Test for single level deep dictionary
    dict1 = {'key1': 'value1', 'key2': 'value2'}
    dict2 = {'key1': 'value1', 'key3': 'value3'}
    expected_result = ({'key2': 'value2'}, {'key3': 'value3'})
    result = recursive_diff(dict1, dict2)
    assert result == expected_result

    # Test for multi-level deep dictionary
    dict1 = {'key1': 'value1', 'key2': {'key3': 'value3', 'key4': 'value4'}}

# Generated at 2022-06-12 23:08:05.116122
# Unit test for function recursive_diff
def test_recursive_diff():
    def assert_dict(dict1, dict2):
        assert recursive_diff(dict1, dict2) == (dict1, dict2)
        assert recursive_diff(dict2, dict1) == (dict2, dict1)

    def assert_none(dict1, dict2):
        assert recursive_diff(dict1, dict2) is None

    assert_none({}, {})
    assert_none({1: 2}, {1: 2})
    assert_dict({1: 3}, {1: 2})
    assert_dict({2: 2}, {1: 2})
    assert_dict({1: {}}, {1: 2})
    assert_dict({1: 2}, {1: {}})
    assert_dict({1: 2}, {2: 2})

# Generated at 2022-06-12 23:08:15.597490
# Unit test for function recursive_diff
def test_recursive_diff():
    dict_base = dict(d=1, z=dict(e=1, f=1), x=6, list1=[1, 2], list2=['a', 'b'])
    dict_no_diffs = dict_base.copy()
    dict_no_diffs.update(dict(d=1, z=dict(e=1, f=1), x=6, list1=[1, 2], list2=['a', 'b']))
    dict_diffs = dict_base.copy()
    dict_diffs.update(dict(d=1, z=dict(e=1, f=2), x=6, list1=[1, 2], list2=['a', 'b']))
    assert recursive_diff(dict_base, dict_no_diffs) is None

# Generated at 2022-06-12 23:08:26.021755
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    sentinel = object()
    camel_dict = dict(CamelCase=1, CamelCaseCamel=dict(CamelSub=dict(Camel=sentinel, camel=['camel'],
                                                                     CamelDict=dict(camel=sentinel))))
    correct_dict = dict(camel_case=1, camel_case_camel=dict(camel_sub=dict(Camel=sentinel, camel=['camel'],
                                                                           camel_dict=dict(camel=sentinel))))
    assert camel_dict_to_snake_dict(camel_dict) == correct_dict



# Generated at 2022-06-12 23:08:35.716361
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({'a': {}}) == {'a': {}}
    assert camel_dict_to_snake_dict({'a': {}, 'A': {}}) == {'a': {}, 'a_': {}}
    assert camel_dict_to_snake_dict({'a': {'b': 'c'}}) == {'a': {'b': 'c'}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {}}) == {'http_endpoint': {}}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {}}, True) == {'h_t_t_p_endpoint': {}}
    assert camel_dict_to

# Generated at 2022-06-12 23:08:45.800989
# Unit test for function dict_merge
def test_dict_merge():
    a = {'x': 1, 'y': 2}
    b = {'y': 3, 'z': 4}
    c = dict_merge(a, b)
    assert c == {'x': 1, 'y': 3, 'z': 4}

    a = {'x': {'x1': 1, 'x2': 2}}
    b = {'x': {'x2': 3, 'x3': 4}}
    c = dict_merge(a, b)
    assert c == {'x': {'x1': 1, 'x2': 3, 'x3': 4}}

    a = {'x': {'x1': 1, 'x2': {'x3': 2}}}
    b = {'x': {'x2': {'x3': 3, 'x4': 4}}}


# Generated at 2022-06-12 23:08:56.047347
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test irreversible conversion
    def test_irreversible(camel_dict, expected_snake_dict):
        # Test basic conversation
        actual_snake_dict = camel_dict_to_snake_dict(camel_dict)
        assert actual_snake_dict == expected_snake_dict
        # Test that the dict is unchanged after recamelizing
        assert expected_snake_dict == snake_dict_to_camel_dict(actual_snake_dict)

    test_irreversible({'testKeys': {'key1': 'value1', 'key2': 'value2'}},
                      {'test_keys': {'key1': 'value1', 'key2': 'value2'}})


# Generated at 2022-06-12 23:09:00.750433
# Unit test for function dict_merge
def test_dict_merge():
    a = {'a': 1, 'b': {1: 1, 2: 2}, 'c': 3}
    b = {'a': 'not one', 'b': {2: 7}, 'd': 4}
    expected = {'a': 'not one', 'b': {1: 1, 2: 7}, 'c': 3, 'd': 4}
    result = dict_merge(a, b)
    assert result == expected



# Generated at 2022-06-12 23:09:11.689880
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        camel_dict_to_snake_dict({'CamelCase': {'DoNotCamelizeMe': {'DoNotCamelizeMe': 'KeepMe'}, 'CamelizeMe': 'CamelizeMe'}}, reversible=True),
        reversible=True) == {'CamelCase': {'DoNotCamelizeMe': {'DoNotCamelizeMe': 'KeepMe'}, 'camelize_me': 'CamelizeMe'}}


# Generated at 2022-06-12 23:09:21.607554
# Unit test for function dict_merge
def test_dict_merge():
    a = {'greeting': 'hello',
         'recursive': {
             'greeting': 'hello',
             'recursive': {
                 'greeting': 'hello'
             }
         }
    }
    b = {'greeting': 'hi',
         'recursive': {
             'greeting': 'hi',
             'recursive': {
                 'greeting': 'hello'
             }
         }
    }
    result = {
        'greeting': 'hi',
        'recursive': {
            'greeting': 'hi',
            'recursive': {
                'greeting': 'hello'
            }
        }
    }
    assert result == dict_merge(a, b)


# Generated at 2022-06-12 23:09:24.847803
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge({'a': {'x': 1, 'y': 2, 'z': 3}, 'b': 2},
                      {'a': {'w': 10}, 'b': 20, 'c': 3}) == \
                      {'a': {'w': 10, 'x': 1, 'y': 2, 'z': 3}, 'b': 20, 'c': 3}

# Generated at 2022-06-12 23:09:34.864666
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Define a dictionary representing a complete example
    of all types of key in a camelcase dict and run the
    conversion to snakecase.
    """
    camel_dict = {"ApiKeyRequired": True, "AuthorizationType": "NONE", "AuthorizerId": None,
                  "ModelSelectionExpression": "$request.body.id", "OperationName": "GetPet",
                  "RequestModels": { "application/json": "AWS::Serverless::Api.Model" },
                  "RequestParameters": { "method.request.path.pet_id": True },
                  "RouteKey": "$default", "RouteResponseSelectionExpression": "$default",
                  "Target": "test-function" }
    snake_dict = camel_dict_to_snake_dict(camel_dict)


# Generated at 2022-06-12 23:09:45.332090
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:56.991325
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camelDict = {
        "HTTPResponseCodeRanges": [
            {
                "From": 0,
                "To": 399,
                "Status": "Healthy"
            }
        ],
        "HTTPEndpoint": {
            "Endpoint": "http://example.com"
        },
        "Tags": [
            {
                "Key": "CloudwatchLogGroup",
                "Value": "/aws/app-autoscaling/aws-elasticbeanstalk-us-east-1-123456789012"
            }
        ]
    }


# Generated at 2022-06-12 23:10:04.511437
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Simple test
    camel_dict = {'keyCamel': 'val'}
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert snake_dict == {'key_camel': 'val'}

    # Reversible test
    camel_dict = {'keyCamel': 'val'}
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)
    assert snake_dict == {'k_e_y_camel': 'val'}

    # Ignore list test

# Generated at 2022-06-12 23:10:13.698403
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndPoint': {
            'Description': 'My http endpoint',
            'Name': 'My http endpoint',
            'LoadBalancerArns': ['arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188']
        },
        'a': {
            'b': {
                'c': 1,
                'd': 2
            }
        },
        'e': {
            'f': 3
        },
        'Tags': {
            'a': 'b'
        }
    }


# Generated at 2022-06-12 23:10:24.930714
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Normal use case
    camel_dict = {'StringKey': 'StringValue', 'IntegerKey': 42, 'DictionaryKey': {'CamelKey': 'SnakeValue'}}
    expected = {'string_key': 'StringValue', 'integer_key': 42, 'dictionary_key': {'camel_key': 'SnakeValue'}}
    assert camel_dict_to_snake_dict(camel_dict) == expected

    # Other use cases
    camel_dict = {'StringKey': 'StringValue', 'IntegerKey': 42,
                  'DictionaryKey': {'CamelKey': 'SnakeValue'}, 'ListKey': [{'ListKey': 'ListValue'}, 42]}

# Generated at 2022-06-12 23:10:32.331469
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    When testing the function, we want to be sure the conversion is
    1 to 1 in both directions. The original input should give the same
    output as the algorithm is run twice.
    """


# Generated at 2022-06-12 23:10:39.220246
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': True}) == {'http_endpoint': True}
    assert camel_dict_to_snake_dict({'HttpEndpoint': True}) == {'http_endpoint': True}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': True}, reversible=True) == {'h_t_t_p_endpoint': True}
    assert camel_dict_to_snake_dict({'HTTPRedirectCode': '301'}) == {'http_redirect_code': '301'}



# Generated at 2022-06-12 23:10:49.241282
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:56.709035
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'A': 1}, False) == {"a": 1}
    assert camel_dict_to_snake_dict({'A': 1, 'B': 2}) == {"a": 1, "b": 2}
    assert camel_dict_to_snake_dict({'A': 1, 'B': 2}, True) == {"h_t_t_p_endpoint": 1, "b": 2}
    assert camel_dict_to_snake_dict({'A': 1, 'B': 2}, sort=True, ignore_list=['a']) == {"a": 1, "b": 2}

# Generated at 2022-06-12 23:11:04.592503
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'fooBar': 'bar',
        'fooBaz': {
            'baz': 'ok',
            'clients': [
                {
                    'name': 'Bob',
                    'age': 19
                },
                {
                    'name': 'Alice',
                    'age': 23
                }
            ],
            'tags': {
                'name': 'Amsterdam'
            },
            'HTTPEndpoint': 'http://ansible.com',
            'Targets': [
                {
                    'Id': 'bbcaf723-3db3-42c0-ac67-f2eacb5e1ef0'
                }
            ]
        }
    }


# Generated at 2022-06-12 23:11:14.240323
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:29.890625
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"Key1": "value1", "Key2": "value2", "Key3": {"Key4": "value3", "Key5": "value4"}}

    assert({"key1": "value1", "key2": "value2", "key3": {"key4": "value3", "key5": "value4"}} == camel_dict_to_snake_dict(camel_dict))

    camel_dict = {"Key1": "value1", "Key2": "value2", "Key3": {"Key4": "value3", "Key5": "value4"}}
    camel_dict['Tags'] = {'Tag1': 'Value1', 'Tag2': 'Value2'}

# Generated at 2022-06-12 23:11:38.237502
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Sample dictionary
    camel_dict = {
        "HTTPEndpoint": {
            "ContentType": "aws_vpc"
        },
        "CloudWatchDestination": {
            "DefaultTag": ["aws_vpc"]
        },
        "TagKey": "aws_vpc"
    }

    result = camel_dict_to_snake_dict(camel_dict)

    assert result == {
        'http_endpoint': {
            'content_type': 'aws_vpc'
        },
        'cloud_watch_destination': {
            'default_tag': ['aws_vpc']
        },
        'tag_key': 'aws_vpc'
    }


# Generated at 2022-06-12 23:11:46.464500
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    example_dict = {
        "Foo": ["foo"],
        "HTTPEndpoint": {
            "Protocol": "http",
            "Host": "example.com",
            "#foo": "bar"
        },
        "Bar": "bar",
        "Baz": {
            "Bar": "bar",
            "Tags": {
                "Key": "Key",
                "Value": "Value"
            }
        },
        "FooBar": {
            "Bar": {
                "Bar": "bar",
                "BarBar": "BarBar"
            },
            "BarBar": {
                "Bar": {
                    "Bar": "bar"
                },
                "BarBar": "BarBar"
            }
        }
    }


# Generated at 2022-06-12 23:11:56.082656
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:03.355004
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:11.671776
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'SnsTopicArn': 'arn:aws:sns:us-east-1:123456789012:MyTopic',
                  'KmsKeyArn': 'arn:aws:kms:us-east-1:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef',
                  'Tags': {'Name': 'ansible'}}

# Generated at 2022-06-12 23:12:18.529351
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_input = {
        'Tags': {
            'Key': 'string',
            'Value': 'string'
        },
        'Type': 'string',
        'Name': 'string',
        'Data': 'string'
    }

    snake_output = {
        'tags': {
            'Key': 'string',
            'Value': 'string'
        },
        'type': 'string',
        'name': 'string',
        'data': 'string'
    }

    assert camel_dict_to_snake_dict(camel_input) == snake_output


# Generated at 2022-06-12 23:12:27.411243
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': True}) == {'http_endpoint': True}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': True}, reversible=True) == {'h_t_t_p_endpoint': True}
    assert camel_dict_to_snake_dict({'Tags': [{'Key': 'a', 'Value': 'b'}]}, ignore_list=['Tags']) == {'tags': [{'Key': 'a', 'Value': 'b'}]}

    # regex for testing reversed camelCase has 5 or more consecutive
    # capital letters and followed by a 's'
    camel_s = re.compile('(?P<reversed_camel_s>_[A-Z]{5,}s$)')



# Generated at 2022-06-12 23:12:38.534150
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {}
    camel_dict['TagKey'] = 'TagValue'
    camel_dict['Id'] = 'IdValue'
    camel_dict['Ids'] = ['IdValue1', 'IdValue2']
    camel_dict['Tags'] = {'TagKey1': 'TagValue1', 'TagKey2': 'TagValue2'}
    camel_dict['TagGroups'] = [{'TagKey1': 'TagValue1', 'TagKey2': 'TagValue2'},
                               {'TagKey3': 'TagValue3', 'TagKey4': 'TagValue4'}]

# Generated at 2022-06-12 23:12:45.448585
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    snake_dict = {
        "location": "westus",
        "tags": {
            "key1": "val1",
            "key2": "val2"
        }
    }
    ans_dict = {
        "location": "westus",
        "tags": {
            "key1": "val1",
            "key2": "val2"
        },
        "tags_key2": "val2",
        "tags_key1": "val1"
    }
    camel_dict = camel_dict_to_snake_dict(snake_dict)
    assert(camel_dict == ans_dict)



# Generated at 2022-06-12 23:12:57.718172
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:07.906639
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:17.022373
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {
        'someKey': 'someValue',
        'anotherKey': 'anotherValue',
        'subDict': {
            'subKey': 'subValue',
            'subDict': {
                'subsubKey': 'subsubValue'
            }
        },
        'subList': [
            {
                'subsubKey': 'subsubValue'
            }
        ],
    }

# Generated at 2022-06-12 23:13:27.776475
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test function camel_dict_to_snake_dict
    """


# Generated at 2022-06-12 23:13:35.034961
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:40.012241
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'LocationType': 'VPC', 'Location': 'arn:aws:ec2:us-west-2:123456789012:vpc/vpc-3a3b9f56'}) == {'location_type': 'VPC', 'location': 'arn:aws:ec2:us-west-2:123456789012:vpc/vpc-3a3b9f56'}


# Generated at 2022-06-12 23:13:51.652129
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "ContentHandlingStrategy": "CONVERT_TO_TEXT",
            "TimeoutInMillis": 29000,
            "URL": "https://my-test-api.com/event"
        }
    }
    result_dict = {
        'h_t_t_p_endpoint': {
            'content_handling_strategy': 'CONVERT_TO_TEXT',
            'timeout_in_millis': 29000,
            'url': 'https://my-test-api.com/event'
        }
    }
    assert result_dict == camel_dict_to_snake_dict(camel_dict, reversible=False)



# Generated at 2022-06-12 23:14:00.563609
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(camel_dict_to_snake_dict({'foo': 'bar'}) == {'foo': 'bar'})
    assert(camel_dict_to_snake_dict({'fooBar': 'bar'}) == {'foo_bar': 'bar'})
    assert(camel_dict_to_snake_dict({'HTTPEndpoint': 'bar'}) == {'h_t_t_p_endpoint': 'bar'})
    assert(camel_dict_to_snake_dict({'fooBar': 'bar'}, reversible=True) == {'foo_b_a_r': 'bar'})
    assert(camel_dict_to_snake_dict({'HTTPEndpoint': 'bar'}, reversible=True) == {'h_t_t_p_endpoint': 'bar'})

# Generated at 2022-06-12 23:14:09.290299
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({
        "KeyPairId": "test-key",
        "PrivateIpAddress": "172.0.0.1",
        "InstanceId": "test-instance",
        "PublicIpAddress": "54.0.0.1",
        "Tags": {
            "tag1": "tag-value"
        }
    }, reversible=False) == {
        "key_pair_id": "test-key",
        "private_ip_address": "172.0.0.1",
        "instance_id": "test-instance",
        "public_ip_address": "54.0.0.1",
        "tags": {
            "tag1": "tag-value"
        }
    }

# Generated at 2022-06-12 23:14:19.583849
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}, reversible=False) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}, reversible=True) == {'f_o_o_bar': 'baz'}

    assert camel_dict_to_snake_dict({'ListPolicies': 'baz'}) == {'list_policies': 'baz'}
    assert camel_dict_to_snake_dict({'ListPolicies': 'baz'}, reversible=False) == {'list_policies': 'baz'}


# Generated at 2022-06-12 23:14:33.081254
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    '''
    This unit test is being kept as a scaffold and can be extended or removed.
    '''
    assert camel_dict_to_snake_dict({'CamelCase': 'CamelCase'}) == {'camel_case': 'CamelCase'}
    assert camel_dict_to_snake_dict({'CamelCase': 'CamelCase'}, True) == {'c_a_m_e_l_c_a_s_e': 'CamelCase'}
    assert camel_dict_to_snake_dict({'httpEndpoint': 'httpEndpoint'}) == {'http_endpoint': 'httpEndpoint'}

# Generated at 2022-06-12 23:14:40.459791
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test basic conversion
    test_dict = {"AString": "a string", "ANumber": 1, "ABoolean": False}
    test_dict_expected = {"a_string": "a string", "a_number": 1, "a_boolean": False}
    assert camel_dict_to_snake_dict(test_dict) == test_dict_expected

    # Test nested conversions
    test_dict = {"AString": "a string", "ANumber": 1, "ABoolean": False, "Nested": {"AString": "a string", "ANumber": 1, "ABoolean": False}}

# Generated at 2022-06-12 23:14:50.509950
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict1 = {'InstanceId': 'i-01234567890abcdef',
                   'PrivateIpAddress': '10.0.0.1',
                   'PublicIpAddress': '1.2.3.4',
                   'randomKey': 'randomValue'}
    snake_dict1 = {'instance_id': 'i-01234567890abcdef',
                   'private_ip_address': '10.0.0.1',
                   'public_ip_address': '1.2.3.4',
                   'random_key': 'randomValue'}

    camel_dict2 = {'Status': 'CREATE_COMPLETE',
                   'Outputs': [{'OutputKey': 'KeyName',
                                'OutputValue': 'ansiblekey'}]}

# Generated at 2022-06-12 23:15:00.689923
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:08.375954
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:13.596109
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'http'}) == {'http_endpoint': 'http'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'http'}, reversible=True) == {'h_t_t_p_endpoint': 'http'}
    assert camel_dict_to_snake_dict({'HTTPEndpoint': 'http'}, irreversible=True) == {'http_endpoint': 'http'}



# Generated at 2022-06-12 23:15:21.205831
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:31.647915
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_case1 = {
        'Tags': [{'Key': 'foo', 'Value': 'bar'}, {'Key': 'baz', 'Value': 'qux'}],
        'HTTPEndpoint': 'http://foo:8080',
        'TargetGroupARNs': ['arn:foo:bar:baz:qux', 'arn:foo:bar:baz:qux'],
        'Name': 'foo-bar',
    }

# Generated at 2022-06-12 23:15:39.432209
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {"k1": "v1", "k2": "v2", "k3": {"kc1": "vc1", "kc2": "vc2", "kc3": ["vl1", "vl2"]}}
    # test for camelCase conversion to snake_case
    assert camel_dict_to_snake_dict(d) == {'k1': 'v1', 'k2': 'v2', 'k3': {'kc1': 'vc1', 'kc2': 'vc2', 'kc3': ['vl1', 'vl2']}}



# Generated at 2022-06-12 23:15:42.535219
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({'foo': {'bar': 'baz'}, 'BaR': 'BaZ'}) == {'foo': {'bar': 'baz'}, 'bar': 'BaZ'}



# Generated at 2022-06-12 23:15:58.632628
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {
        "fooBar": [
            {
                "fooBarBaz": [
                    {
                        "fooBarBazBat": []
                    }
                ]
            }
        ]
    }
    snake = {
        u'foo_bar': [
            {
                u'foo_bar_baz': [
                    {
                        u'foo_bar_baz_bat': []
                    }
                ]
            }
        ]
    }
    assert(camel_dict_to_snake_dict(camel, False) == snake)
    assert(camel_dict_to_snake_dict(camel, True) != snake)



# Generated at 2022-06-12 23:16:07.318826
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'List': [{'Tag': 1}, {'HTTPResponse': '200'}, {'CamelCase': 'True'}, {'Location': 'a'}],
                  'HTTPEndpoint': 'a', 'Tags': {'Tag': 1, 'HTTPEndpoint': 'a'}, 'Location': 'b'}
    expected_dict = {'list': [{'tag': 1}, {'http_response': '200'}, {'camel_case': 'True'}, {'location': 'a'}],
                     'h_t_t_p_endpoint': 'a', 'tags': {'Tag': 1, 'HTTPEndpoint': 'a'}, 'location': 'b'}
    result_dict = camel_dict_to_snake_dict(camel_dict, True, 'Tags')


# Generated at 2022-06-12 23:16:12.825754
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:19.229449
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'foo': 'bar'}) == {'foo': 'bar'}
    assert camel_dict_to_snake_dict({'fooBar': 'baz'}) == {'foo_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooBarBaz': 'qux'}) == {'foo_bar_baz': 'qux'}
    assert camel_dict_to_snake_dict({'fooHTTPBar': 'baz'}) == {'foo_h_t_t_p_bar': 'baz'}
    assert camel_dict_to_snake_dict({'fooHTTPBar': 'baz'}, reversible=True) == {'foo_h_t_t_pbar': 'baz'}
    assert camel

# Generated at 2022-06-12 23:16:25.385774
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Create test dict
    camel_dict = {'HTTPEndpoint': 1, 'TargetGroupARNs': [],
                  'Tags': {'run': '', 'name': ''}, 'ScheduleExpression': ''}
    # Set expected result
    expected_result = {'http_endpoint': 1, 'target_group_ar_ns': [],
                       'tags': {'run': '', 'name': ''}, 'schedule_expression': ''}
    # Run test dict through function
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_result



# Generated at 2022-06-12 23:16:34.349719
# Unit test for function camel_dict_to_snake_dict