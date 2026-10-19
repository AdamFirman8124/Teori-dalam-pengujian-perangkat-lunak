

# Generated at 2022-06-12 23:06:51.590039
# Unit test for function dict_merge
def test_dict_merge():
    d1 = {'b': {'c': 1}, 'a': 12, 'd': [1, 2, 3]}
    d2 = {'b': {'c': 2}, 'a': 12, 'd': [4, 5, 6]}
    expected = {'b': {'c': 2}, 'a': 12, 'd': [4, 5, 6]}
    assert dict_merge(d1, d2) == expected


# Generated at 2022-06-12 23:06:57.066906
# Unit test for function dict_merge
def test_dict_merge():
    dict1 = dict(a=1, c=dict(b=1, c=1))
    dict2 = dict(a=2, c=dict(b=2))
    dict3 = dict_merge(dict1, dict2)
    dict4 = dict(a=2, c=dict(b=2, c=1))
    assert dict3 == dict4

# Generated at 2022-06-12 23:07:07.289806
# Unit test for function recursive_diff
def test_recursive_diff():
    """Return the diff of two dictionaries."""

    is_equal = {
        'this is a test': {
            'and': 'should work'
        },
        'dictionary': {
            'is': {
                'nested': 3
            }
        },
        2: 'two',
        None: None,
    }

    # Test simple diff
    not_equal = {
        'this is a test': {
            'and': 'should work'
        },
        'dictionary': {
            'is': {
                'nested': 5
            }
        },
        2: 'two',
        None: None,
    }
    master_dict = is_equal
    changed_dict = not_equal
    diff = recursive_diff(master_dict, changed_dict)

# Generated at 2022-06-12 23:07:11.390306
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    some_dict = {'Name': 'testname', 'KeyName': 'testkey'}
    expected = {'name': 'testname', 'key_name': 'testkey'}

    assert camel_dict_to_snake_dict(some_dict) == expected



# Generated at 2022-06-12 23:07:19.528248
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'Region': 'us-east-1',
    }

    dict2 = {
        'Region': 'us-east-1',
    }
    assert recursive_diff(dict1, dict2) is None

    dict1 = {
        'Region': 'us-east-1',
    }

    dict2 = {
        'Region': 'us-east-2',
    }
    assert recursive_diff(dict1, dict2) == ({'Region': 'us-east-1'}, {'Region': 'us-east-2'})

    dict1 = {
        'Region': 'us-east-1',
        'SourceDestCheck': False,
    }

    dict2 = {
        'Region': 'us-east-2',
        'SourceDestCheck': True,
    }

# Generated at 2022-06-12 23:07:31.271365
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Snake_to_camel helper
    def _s_to_c(s):
        return camel_dict_to_snake_dict(s, False, True)

    # Camel_to_snake helper
    def _c_to_s(c):
        return snake_dict_to_camel_dict(c, True)

    def _test_c_to_s(string, expected):
        assert _c_to_s({'DromedaryCase': string}) == {'DromedaryCase': expected}

    def _test_s_to_c(string, expected):
        assert _s_to_c({string: 'DromedaryCase'}) == {expected: 'DromedaryCase'}

    # Happy Path

# Generated at 2022-06-12 23:07:38.934477
# Unit test for function recursive_diff
def test_recursive_diff():
    dict_a = {'a': 1}
    dict_b = {'a': 1}
    assert recursive_diff(dict_a, dict_b) is None

    dict_a = {'a': 1}
    dict_b = {'b': 1}
    assert recursive_diff(dict_a, dict_b) == ({'a': 1}, {'b': 1})

    dict_a = {'a': 1}
    dict_b = {'a': 2}
    assert recursive_diff(dict_a, dict_b) == ({'a': 1}, {'a': 2})

    dict_a = {'a': {'b': 1}}
    dict_b = {'a': {'b': 1}}
    assert recursive_diff(dict_a, dict_b) is None


# Generated at 2022-06-12 23:07:49.459554
# Unit test for function recursive_diff
def test_recursive_diff():
    # No difference
    assert recursive_diff({'a': 1}, {'a': 1}) is None

    # Difference in value
    assert recursive_diff({'a': 1}, {'a': 2}) == ({'a': 1}, {'a': 2})

    # Difference in key
    assert recursive_diff({'a': 1}, {'b': 2}) == ({'a': 1}, {'b': 2})

    # Difference in root keys
    assert recursive_diff({'a': {}}, {'b': {}}) == ({'a': None}, {'b': None})

    # Difference in nested keys
    assert recursive_diff({'a': {'a': 1}}, {'a': {'b': 1}}) == ({'a': {'a': None}}, {'a': {'b': None}})

    # Difference

# Generated at 2022-06-12 23:07:59.815594
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:05.139382
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:20.980327
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'HTTPEndpoint': {'protocol': 'HTTP'}}) == {'http_endpoint': {'protocol': 'HTTP'}}
    assert camel_dict_to_snake_dict({'MyString': 'string'}) == {'my_string': 'string'}
    assert camel_dict_to_snake_dict({'MyBoolean': False}) == {'my_boolean': False}
    assert camel_dict_to_snake_dict({'MyStringList': ['string', 'string2']}) == {'my_string_list': ['string', 'string2']}
    assert camel_dict_to_snake_dict({'MyIntegers': [1, 2, 3, 4]}) == {'my_integers': [1, 2, 3, 4]}

# Generated at 2022-06-12 23:08:28.874707
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Check that a transform to snake case works
    camel_dict = {'HTTPEndpoint':{'Protocol': 'http', 'Port': 80}}
    transformed_dict = {'h_t_t_p_endpoint':{'protocol': 'http', 'port': 80}}
    assert camel_dict_to_snake_dict(camel_dict) == transformed_dict

    # Check that a transform to reversible snake case works
    camel_dict = {'HTTPEndpoint':{'Protocol': 'http', 'Port': 80}}
    transformed_dict = {'h_t_t_p_endpoint':{'p_rotocol': 'http', 'p_ort': 80}}
    assert camel_dict_to_snake_dict(camel_dict, reversible=True) == transformed_dict

    # Check that a transform to snake

# Generated at 2022-06-12 23:08:37.291757
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Tests the camel_dict_to_snake_dict function
    """


# Generated at 2022-06-12 23:08:47.652302
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:08:57.620820
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(KeyName='foo')
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)

    assert snake_dict == {'Key_name': 'foo'}, "KeyName should be Key_name"

    camel_dict = dict(KeyName='foo', DBSubnetGroups=[])
    snake_dict = camel_dict_to_snake_dict(camel_dict, reversible=True)

    assert snake_dict == {'Key_name': 'foo', 'Db_subnet_groups': []}, \
        "DBSubnetGroups should be Db_subnet_groups"

    camel_dict = dict(KeyName='foo', DBSubnetGroups=[
        dict(DBSubnetGroupName='bar')])
    snake_dict = camel_

# Generated at 2022-06-12 23:09:07.868166
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        'KeyName': 'name',
        'Tags': [{'Key': '1', 'Value': '2'}],
        'NetworkInterfaceId': 'interface_id',
        'HTTPEndpoint': 'http_endpoint',
        'TargetGroupARNs': 'target_group_arns',
        'TargetGroups': [{
            'TargetGroupArn': 'group_arn',
            'TargetGroupARNs': 'group_arns'
        }]
    }


# Generated at 2022-06-12 23:09:18.634344
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'DBSnapshotIdentifier': 'snoopy-snap-1', 'AllocatedStorage':100, 'AvailabilityZone': 'us-east-1b',
                  'DBInstanceClass': 'db.m1.small', 'Engine': 'mysql', 'EngineVersion': '5.6.23',
                  'Tags': {'Application': 'Snoopy', 'Network': 'Public'}}
    snake_dict = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:09:26.325375
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:36.619544
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_schema = {"Accounts": [{"name": "accounts", "type": "list", "required": True, "members": {"shape": "AccountInfo"}}],
                    "AccountInfo": {"type": "structure", "members": {"AccountId": {"shape": "AccountId"},
                                                                     "Name": {"shape": "Name"},
                                                                     "TagKeys": {"shape": "TagKeyList"}}},
                    "AccountId": {"type": "string", "min": 12, "max": 12, "pattern": "[0-9]+"},
                    "Name": {"type": "string"},
                    "TagKeyList": {"type": "list", "members": {"shape": "TagKey"}},
                    "TagKey": {"type": "string"}}


# Generated at 2022-06-12 23:09:46.665264
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:57.535634
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({}) == {}                                             # Test empty dict
    assert camel_dict_to_snake_dict({"DockerVolumeConfiguration":{"Scope":"shared"}}) == {"docker_volume_configuration":{"scope":"shared"}}  # Test first level only
    assert camel_dict_to_snake_dict({"DockerVolumeConfiguration":{"AUTOMOUNTLABEL":"TEST"}}) == {"docker_volume_configuration":{"automountlabel":"TEST"}}  # Test last level
    assert camel_dict_to_snake_dict({"DockerVolumeConfiguration":{"Scope":"shared","AUTOMOUNTLABEL":"TEST"}}) == {"docker_volume_configuration":{"scope":"shared","automountlabel":"TEST"}}  # Test more than one level
    assert camel_dict_to_snake_

# Generated at 2022-06-12 23:10:05.083235
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:09.888942
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'Host': 'test.com', 'EndpointStatus': 'test'}}
    assert camel_dict_to_snake_dict(camel_dict) == {'http_endpoint': {'host': 'test.com', 'endpoint_status': 'test'}}



# Generated at 2022-06-12 23:10:19.147581
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Path': '/foo',
            'Protocol': 'HTTPS'
        },
        'Function': {
            'FunctionName': 'Function',
            'Description': "Description"
        }
    }
    assert camel_dict != camel_dict_to_snake_dict(camel_dict)
    camel_dict = {
        'HTTPEndpoint': {
            'Path': '/foo',
            'Protocol': 'HTTPS'
        },
        'Function': {
            'FunctionName': 'Function',
            'Description': "Description"
        },
        'Tags': {
            'key': 'value'
        }
    }

# Generated at 2022-06-12 23:10:28.603267
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camelized_dict = {
        "HTTPEndpoint": {
            "Endpoint": "https://cloudwatch.us-east-1.amazonaws.com",
            "Protocol": "HTTPS"
        },
        "Enabled": True,
        "Id": "MyMetricTransformer",
        "MetricTransformation": {
            "MetricName": "MyMetric",
            "MetricNamespace": "EC2",
            "MetricValue": "2",
            "DefaultValue": 1.0
        },
        "Name": "MyMetricTransformer"
    }


# Generated at 2022-06-12 23:10:34.500281
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:41.765267
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"CamelCase": "camel", "NotCamel": "snake"}) == \
            {"camel_case": "camel", "not_camel": "snake"}
    assert camel_dict_to_snake_dict({"TagFilters": {"CamelCase": "camel", "NotCamel": "snake"}},
            ignore_list=["TagFilters"]) == \
            {"tag_filters": {"CamelCase": "camel", "NotCamel": "snake"}}
    assert camel_dict_to_snake_dict({"HTTPEndpoint": "camel", "HTTPSEndpoint": "camel"}) == \
            {"http_endpoint": "camel", "https_endpoint": "camel"}
    assert camel_dict

# Generated at 2022-06-12 23:10:51.539456
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:55.163878
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(
        camel_dict_to_snake_dict(
            {"FooBar": {"FooBaz": [{"Bar": 123}, {"Bar": 456}]}}
        ) ==
        {"foo_bar": {"foo_baz": [{"bar": 123}, {"bar": 456}]}}
    )



# Generated at 2022-06-12 23:11:02.633824
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:14.085179
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {u'HTTPEndpoint': {u'Name': u'CurrentState', u'Value': u'UP'}, u'HTTPSEndpoint': {u'Name': u'CurrentState', u'Value': u'UP'}}
    assert camel_dict_to_snake_dict(camel_dict) == {u'httpEndpoint': {u'name': u'CurrentState', u'value': u'UP'}, u'httpsEndpoint': {u'name': u'CurrentState', u'value': u'UP'}}
    camel_dict = {u'HTTPEndpoint': {u'Name': u'CurrentState', u'Value': u'UP'}, u'HTTPSEndpoint': {u'Name': u'CurrentState', u'Value': u'UP'}}
    assert camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:24.957076
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Tests camel_dict_to_snake_dict function"""
    camel_input_dict = dict(HTTPEndpoint="ecs.amazonaws.com",
                            Counter=[{"Name": "my-counter", "Value": 10}, {"Name": "my-counter", "Value": 20}],
                            Tag=[{"Key": "Tag", "Value": "Value"}],
                            Tags=[{"Key": "Tag", "Value": "Value"}])

# Generated at 2022-06-12 23:11:34.545897
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camelized_dict = {'network': {'ipv6T': 'spaghetti'},
                      'network1': {'ipv4T': 'spaghetti'},
                      'network2': {'ipv6S': [['spaghetti', {'ipv6': 'spaghetti'}]]}}

    expected_dict = {'network_1': {'ipv6_t': 'spaghetti'},
                     'network_2': {'ipv4_t': 'spaghetti'},
                     'network_3': {'ipv6_s': [['spaghetti', {'ipv6': 'spaghetti'}]]}}

    assert(camel_dict_to_snake_dict(camelized_dict) == expected_dict)



# Generated at 2022-06-12 23:11:42.156625
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:49.141874
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'CamelCaseKey1': 1, 'HTTPEndpoint': 2,
                 'ExternalEndpoints':
                     [{'CamelCaseKey1': 1, 'HTTPEndpoints':
                           [{'CamelCaseKey1': 1, 'HTTPEndpoint': 2}]
                      }],
                 'Tags':
                     [{'Key': 'key1', 'Value': 'value1'}],
                 'ListMember':
                     [{'CamelCaseKey1': 1, 'HTTPEndpoint': 2}, {'CamelCaseKey1': 3, 'HTTPEndpoint': 4}]}


# Generated at 2022-06-12 23:11:58.926791
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_camel_dict = {
        "results": [
            {
                "foo": {
                    "bar": {
                        "baz": "bark",
                        "qux": "quack"
                    }
                },
                "a": {
                    "b": "c"
                },
                "bar": "baz"
            },
            {
                "a": {
                    "a": "a",
                    "b": "b"
                },
                "b": "c",
                "c": {
                    "a": "b",
                    "b": {
                        "a": "b"
                    }
                }
            }
        ]
    }


# Generated at 2022-06-12 23:12:09.342014
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:12:18.334599
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(dict(HTTPEndpoint='192.168.1.1'), True) == dict(h_t_t_p_endpoint='192.168.1.1')
    assert camel_dict_to_snake_dict(dict(TargetGroupARNs=[]), True) == dict(target_group_a_r_ns=[])
    assert camel_dict_to_snake_dict(dict(TargetGroupARNs=['arn1']), True) == dict(target_group_a_r_ns=['arn1'])

# Generated at 2022-06-12 23:12:27.149835
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'Body': 'body', 'IsDisabled': False, 'URL': 'http://example.com/', 'ConnectionTimeoutInSeconds': 10, 'RequestTimeoutInSeconds': 10}, 'IsEnabled': False, 'Postfix': 'string', 'Prefix': 'string', 'Tags': {'key': 'value'}}

# Generated at 2022-06-12 23:12:38.277655
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "myProp": "myvalue",
        "HTTPEndpoint": {
            "HTTPEndpoint": {
                "HTTPEndpoint": "myvalue"
            },
            "testKey2": "testValue2"
        },
        "testKey": "testValue",
        "IntProp": 42,
        "tags": {
            "Tags": [
                {
                    "Key": "tag_key",
                    "Value": "tag_value"
                }
            ]
        }
    }

# Generated at 2022-06-12 23:12:45.227044
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Create a camelCase dictionary
    camel_dict = {'Key1': 'value1', 'Key2':{'NestedKey': 'value2'}}

    # Convert to snake_case and compare
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    if snake_dict['key1'] == 'value1' and snake_dict['key2']['nested_key'] == 'value2':
        return True
    else:
        return False

# Generated at 2022-06-12 23:12:55.336400
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:02.599728
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:12.876230
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Check that camel_dict_to_snake_dict returns a properly formatted
    dictionary.
    """

    sample = {
        'HTTPEndpoint': {
            'Enabled': True,
            'VPCOnly': True,
            'HTTPPath': '/foo',
            'New': 'x',
            'Create': 'y',
            'tags': 'z'
        },
        'AllTags': {
            'one': 'a',
            'two': 'b',
            'three': 'c'
        },
        'CamelOnly': 'CamelCase',
        'CamelList': ['CamelCase', 'DromedaryCase']
    }


# Generated at 2022-06-12 23:13:18.845458
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {'HttpEndpoint': {'Endpoint': 'http://jenkins.example.com', 'HostHeader': None},
                 'LogRetentionInDays': 3, 'Tags': {'Environment': 'production', 'Project': 'albatross'}}
    expected_result = {'log_retention_in_days': 3, 'http_endpoint': {'endpoint': 'http://jenkins.example.com', 'host_header': None},
                       'tags': {'environment': 'production', 'project': 'albatross'}}
    assert camel_dict_to_snake_dict(test_dict) == expected_result


# Generated at 2022-06-12 23:13:29.711443
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    input_dict = {
        "Tags": {
            "aTagKey": "aTagValue",
        },
        "VpcId": "myVpcId",
        "LoadBalancerName": "myLoadBalancer",
        "SecurityGroups": [
            "sg-123456"
        ],
        "Subnets": [
            "subnet-123456",
            "subnet-234567"
        ],
    }

    output_dict = camel_dict_to_snake_dict(input_dict)


# Generated at 2022-06-12 23:13:38.920432
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Test camel_dict_to_snake_dict"""

    camel_dict = {
        "Key": "Value",
        "MyKey": "MyValue",
        "ABCDef": "GHI",
        "JSON": "true",
        "MyList": [
            "a",
            "b",
            "c"
        ],
        "MyNestedDict": {
            "Key": "Value",
            "MyKey": "MyValue",
            "ABCDef": "GHI",
            "JSON": "true",
            "MyList": [
                "a",
                "b",
                "c"
            ]
        },
    }


# Generated at 2022-06-12 23:13:51.001848
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'aCamel': {
            'camelCase': 'camel',
            'HttpEndpoint': 'http',
            'camel_case': '',
            'S3Bucket': [123, 'abc'],
            'Tags': [{'Key': '1'}, {'Value': '2'}]
        },
        'snake_case': '',
        'JsonDatabase': {
            'Fn::Join': [
                '',
                [
                    '{"foo":"',
                    'bar',
                    '"}'
                ]
            ]
        }
    }


# Generated at 2022-06-12 23:14:00.080464
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:04.266620
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': True,
        'Tags': {
            'Tag1': True,
            'Tag2': True
        }
    }

    snake_dict = camel_dict_to_snake_dict(camel_dict)

    assert snake_dict == {
        'http_endpoint': True,
        'tags': {
            'Tag1': True,
            'Tag2': True
        }
    }


# Generated at 2022-06-12 23:14:18.123486
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    my_dict = {
        "InstanceIds": ["i-123456789", "i-abcdefghi"],
        "ActivityIds": [],
        "Tags": {
            "Application": "app",
            "Environment": "dev"
        },
        "TagFilters": [
            {
                "Key": "Application",
                "Values": ["app"]
            }
        ]
    }

    new_dict = camel_dict_to_snake_dict(my_dict)
    assert new_dict['instance_ids'] == ['i-123456789', 'i-abcdefghi']
    assert new_dict['activity_ids'] == []
    assert new_dict['tags']['application'] == 'app'
    assert new_dict['tags']['environment'] == 'dev'
    assert new

# Generated at 2022-06-12 23:14:21.311498
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    result = camel_dict_to_snake_dict(camel_dict_to_snake_dict({'AaaBbb': 'foo'}, reversible=True), reversible=True)
    assert result == {'AaaBbb': 'foo'}


# Generated at 2022-06-12 23:14:32.142868
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {'key1': 'value1', 'key2': {'camelCaseKey': 'value2'}, 'key3': [{'listKey': 'listValue1'}, 'listValue2']}
    snake_result = {'key1': 'value1', 'key2': {'camel_case_key': 'value2'}, 'key3': [{'list_key': 'listValue1'}, 'listValue2']}
    assert(camel_dict_to_snake_dict(camel) == snake_result)

    camel = {'HTTPEndpoint': {'Endpoint': 'http://www.ansible.com'}, 'Tags': {'Key1': 'value1'}}

# Generated at 2022-06-12 23:14:36.623791
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_key = 'testCamelKey'
    snake_key = 'test_camel_key'
    camel_dict = {camel_key: 'test'}
    test_dict = camel_dict_to_snake_dict(camel_dict)
    assert test_dict[snake_key] == 'test'
    assert test_dict['test_camel_key'] == 'test'


# Generated at 2022-06-12 23:14:45.531869
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Unit tests for camel_dict_to_snake_dict function
    """
    camel_dict = {
        "ResponseMetadata": {
            "Description": "foo"
        },
        "HTTPHeaders": {
            "HTTPHeaders": {
                "X-Frame-Options": "DENY"
            }
        },
        "HTTPStatusCode": 200
    }

    snake_dict = {
        "response_metadata": {
            "description": "foo"
        },
        "h_t_t_p_headers": {
            "h_t_t_p_headers": {
                "x_frame_options": "DENY"
            }
        },
        "h_t_t_p_status_code": 200
    }


# Generated at 2022-06-12 23:14:55.722102
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:05.057141
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Tests of camel_dict_to_snake_dict
    assert camel_dict_to_snake_dict(dict(HTTPEndpoint="foo.com")) == dict(h_t_t_p_endpoint="foo.com")
    assert camel_dict_to_snake_dict(dict(HTTPRule=dict(HTTPRedirectCode="200"))) == dict(http_rule=dict(h_t_t_p_redirect_code="200"))
    assert camel_dict_to_snake_dict(dict(HTTPRule=dict(HTTPRedirectCode="200", HTTPHeader=dict(Value="value")))) == dict(http_rule=dict(h_t_t_p_redirect_code="200", http_header=dict(value="value")))
    assert camel_dict_to_

# Generated at 2022-06-12 23:15:12.921524
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():


    input = {"HTTPEndpoint": "test",
            "SnsTopicArn": "arn:aws:sns:us-east-1:1234:testTopic",
            "Destinations": [
                {
                    "HTTPEndpoint": "http://example.com",
                    "ID": "httpExample"
                }
            ]
        }

    expected_output = {
            "h_t_t_p_endpoint": "test",
            "sns_topic_arn": "arn:aws:sns:us-east-1:1234:testTopic",
            "destinations": [
                {
                    "h_t_t_p_endpoint": "http://example.com",
                    "id": "httpExample"
                }
            ]
        }

    output = camel_dict_to_snake_

# Generated at 2022-06-12 23:15:20.050882
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert(_camel_to_snake('fakeKey') == 'fake_key')
    assert(_camel_to_snake('fakeA') == 'fakea')
    assert(_camel_to_snake('fakeKey1') == 'fake_key1')
    assert(_camel_to_snake('aggregate') == 'aggregate')
    assert(_camel_to_snake('httpEndpoint') == 'http_endpoint')
    assert(_camel_to_snake('HTTPMetrics') == 'http_metrics')
    assert(_camel_to_snake('TargetGroupARNs') == 'target_group_arns')
    assert(_camel_to_snake('TargetGroupARNs', True) == 'target_group_arns')

# Generated at 2022-06-12 23:15:30.812291
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'To': 'email@example.com',
        'Source': 'email@example.com',
        'Parameters': {
            'RecipientName': 'name',
            'SenderName': 'name',
            'OrderUrl': 'url'
        },
        'ConfigurationSetName': 'string',
        'Template': 'string',
        'TemplateData': 'string'
    }


# Generated at 2022-06-12 23:15:46.123125
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPMethod': 'GET',
        'HTTPEndpoint': 'https://www.ansible.com',
        'HTTPEndpointList': ['https://www.ansible.com', 'https://www.redhat.com'],
        'MyTags': [
            {'Tag': {
                'Key': 'foo',
                'Value': 'bar'
            }},
            {'Tag': {
                'Key': 'answer',
                'Value': '42'
            }},
        ],
        'Tags': [
            {'Key': 'foo',
             'Value': 'bar'}
        ]
    }


# Generated at 2022-06-12 23:15:56.241736
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'myTest': 'mytestvalue',
        'myRecursiveCamelTest': {
            'MyRecursiveCamelTest': 'mytestvalue',
            'MyTestList': [
                {
                    'MyTestListItem': 'item value'
                }
            ]
        },
        'myTestList': [
            {
                'myTestListItem': 1
            }, {
                'myTestListItem': 2
            }
        ]
    }

    # Standard case

# Generated at 2022-06-12 23:16:05.246653
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input = {'HTTPEndpoint': {'URL': 'http://example.com', 'HttpMethod': 'POST'},
             'Castle': 'Cloud',
             'Knight': 'Lancelot',
             'CastleArray': ['Cloud', 'Windy'],
             'NumberArray': [3, 5, 7],
             'Tags': {'Tag1': 'Tag2'},
             'NestedTag': {'NestedTag': {'NestedTag': {'NestedTag': 'Tag'}}}}

# Generated at 2022-06-12 23:16:12.876964
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"fooBar": 1}) == {"foo_bar": 1}
    assert camel_dict_to_snake_dict({"fooBar": {"fooBar": 2}}) == {"foo_bar": {"foo_bar": 2}}
    assert camel_dict_to_snake_dict({"fooBar": {"fooBar": 2, "childTag": {}}}, ignore_list=["childTag", "childTag1"]) == {"foo_bar": {"foo_bar": 2, "childTag": {"childTag": {}}}}

# Generated at 2022-06-12 23:16:19.254643
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:16:27.512349
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    # Test for dictionary
    expected_result_dict = {'test_snake': 'test_snake', 'test_camel': {'nested_test_snake': 'test_snake'}}
    test_dict = {'testSnake': 'test_snake', 'testCamel': {'nestedTestSnake': 'test_snake'}}
    result_dict = camel_dict_to_snake_dict(test_dict)
    assert result_dict == expected_result_dict

    # Test for list
    expected_result_list = ['test_snake', 'test_snake']
    test_list = ['testSnake', 'testSnake']
    result_list = camel_dict_to_snake_dict(test_list)
    assert result_list == expected_result_list



# Generated at 2022-06-12 23:16:36.119054
# Unit test for function camel_dict_to_snake_dict