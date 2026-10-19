

# Generated at 2022-06-12 23:07:06.183880
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # The initial dictionary to be converted.
    input_dict = {
        "camelCaseString": "Hello",
        "CamelCaseString": "Hello",
        "CamelCaseNumber": 123,
        "CamelCaseList": ["Hello", "World"],
        "CamelCaseDict": {
            "CamelCaseDictString": "Hello"
        },
        "dictWithIgnoredKey": {
            "CamelCaseIgnoredKey": "Should not be converted"
        },
        "listWithIgnoredKey": [
            {
                "CamelCaseIgnoredKey": "Should not be converted"
            }
        ],
        "_underscore": "Should not be converted",
        "camelCaseTag": {
            "TAG": "Should not be converted"
        }
    }

    # The expected output.
   

# Generated at 2022-06-12 23:07:16.154539
# Unit test for function recursive_diff
def test_recursive_diff():
    """Test function recursive_diff
    """
    assert recursive_diff({}, {}) is None
    assert recursive_diff({'key1': 'value1', 'key2': 'value2'}, {'key1': 'value1', 'key2': 'value2'}) is None
    assert recursive_diff({'key1': 'value1', 'key2': 'value2'}, {'key2': 'value2', 'key1': 'value1'}) is None
    assert recursive_diff({'key1': 'value1', 'key2': 'value2'}, {'key1': 'value0', 'key2': 'value2'}) == ({'key1': 'value1'}, {'key1': 'value0'})

# Generated at 2022-06-12 23:07:26.464210
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:35.121905
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {'key': {'key1': 'value1'}}
    dict2 = {'key': {'key2': 'value2'}}
    result = recursive_diff(dict1, dict2)
    assert result == ({'key': {'key1': 'value1'}}, {'key': {'key2': 'value2'}})

    dict3 = dict1.copy()
    dict3['key1'] = 'value1'
    dict4 = dict2.copy()
    dict4['key1'] = 'value2'
    result1 = recursive_diff(dict3, dict4)
    assert result1 == ({'key1': 'value1'}, {'key1': 'value2'})

# Generated at 2022-06-12 23:07:42.442720
# Unit test for function dict_merge
def test_dict_merge():
    a = dict(
        dict1=dict(
            dict1_1=dict(a=1, b=2, c=3),
            dict1_2=dict(a=1, b=2, c=3),
            dict1_3={'item1': 'value1',
                     'item2': 'value2',
                     'item3': {'subitem1': 'subvalue1',
                               'subitem2': 'subvalue2'}},
            dict1_4=dict(a=1, b=2, c=3)
        )
    )


# Generated at 2022-06-12 23:07:53.706904
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test empty dicts
    assert recursive_diff({}, {}) is None
    assert recursive_diff({}, {'a': 1, 'b': 2, 'c': 3}) == ({}, {'a': 1, 'b': 2, 'c': 3})
    assert recursive_diff({'a': 1, 'b': 2, 'c': 3}, {}) == ({'a': 1, 'b': 2, 'c': 3}, {})
    # Test same key and value
    assert recursive_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 2}) is None
    assert recursive_diff({'a': 1}, {'a': 1}) is None
    assert recursive_diff({'a': 1}, {'b': 1}) == ({'a': 1}, {'b': 1})
    # Test different key

# Generated at 2022-06-12 23:08:03.059442
# Unit test for function dict_merge
def test_dict_merge():
    dict_a = dict(one=1, two=2)
    dict_b = dict(three=3)
    dict_c = dict(four=4)

    # Init tests
    assert dict_a.get('one') == 1
    assert dict_a.get('two') == 2

    assert dict_b.get('three') == 3
    assert dict_b.get('four') is None

    assert dict_c.get('four') == 4
    assert dict_c.get('one') is None

    # Merge dict_a and dict_b
    dict_merged = dict_merge(dict_a, dict_b)

    # Ensure merged dict values behave as expected
    assert dict_merged.get('one') == 1
    assert dict_merged.get('two') == 2

# Generated at 2022-06-12 23:08:11.209854
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    d = {
        "InstanceIds": ["i-01f2y2c3"],
        "Tags": [
            {
                "Key": "Name",
                "Value": "Ansible-Instance"
            }
        ]
    }

    d_snake = {
        "instance_ids": ["i-01f2y2c3"],
        "tags": [
            {
                "key": "Name",
                "value": "Ansible-Instance"
            }
        ]
    }

    assert camel_dict_to_snake_dict(d) == d_snake



# Generated at 2022-06-12 23:08:21.749925
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'TestKey': 'TestValue'}) == {'test_key': 'TestValue'}
    assert camel_dict_to_snake_dict({'TestKey': {'TestSubKey': {'TestSubSubKey': 'TestValue'}}}) == {'test_key': {'test_sub_key': {'test_sub_sub_key': 'TestValue'}}}
    assert camel_dict_to_snake_dict({'TestKey': ['TestValueOne', {'TestSubKey': 'TestValueTwo'}]}) == {'test_key': ['TestValueOne', {'test_sub_key': 'TestValueTwo'}]}

# Generated at 2022-06-12 23:08:30.695089
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'someKey': 'someValue', 'someOtherKey': 'someOtherValue',
                  'someDict': {'someKey': 'someValue', 'someOtherKey': 'someOtherValue'},
                  'someOtherDict': {'someKey': 'someValue', 'someOtherKey': 'someOtherValue'},
                  'someList': [{'someKey': 'someValue', 'someOtherKey': 'someOtherValue'},
                               {'someKey': 'someValue', 'someOtherKey': 'someOtherValue'}],
                  'someOtherList': [{'someKey': 'someValue', 'someOtherKey': 'someOtherValue'},
                                    {'someKey': 'someValue', 'someOtherKey': 'someOtherValue'}],
                  }


# Generated at 2022-06-12 23:08:47.503976
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    module = AnsibleModule(argument_spec={})
    test_dict = {'FooBar': 'baz', 'fooBar': 'baz', 'FooBarBaz': {'fooBarBaz': 'baz', 'FooBarBaz': 'baz'}}

    snake_dict = camel_dict_to_snake_dict(test_dict)

    assert snake_dict == {'foo_bar': 'baz', 'foo_bar_baz': {'foo_bar_baz': 'baz', 'foo_bar_baz': 'baz'}}

    # check that a recursive call is handled correctly
    snake_dict2 = camel_dict_to_snake_dict(snake_dict)


# Generated at 2022-06-12 23:08:57.463368
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict_camel = {
        'SHOULD_NOT_CHANGE': "This value should not change",
        'PORTMAPPINGS': [
            {
                'CONTAINERPORT': 80,
                'PROTOCOL': 'tcp'
            }
        ],
        'TAGS': [
            {
                'KEY': "test",
                'VALUE': "test"
            }
        ],
        'IMAGE': 'wordpress',
        'HTTP_ENDPOINT': {
            'VIRTUAL_NAME': 'test',
            'CONTAINER_NAME': 'test'
        }
    }

# Generated at 2022-06-12 23:09:07.618832
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:18.397103
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "EC2InstanceId": "i-06cee6f8d0e7b6a19",
        "Hostname": "ip-10-0-0-19",
        "OSType": "linux",
        "Architecture": "x86_64",
        "SSHKeyName": "mykey",
        "MemoryGiB": "16.0",
        "CPUCount": "2",
        "DiskSizeGB": "50",
        "Cost": "0.016667",
        "State": "running",
        "Platform": None,
        "Tags": {
            "Name": "ip-10-0-0-19",
            "CostCode": "12345"
        }
    }

# Generated at 2022-06-12 23:09:25.929713
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_name = {
      "parent": {
        "stringField": "string",
        "longField": 1,
        "longListField": [
          1,
          2
        ],
        "stringListField": [
          "a",
          "b"
        ],
        "leaf": {
          "stringField": "string",
          "longField": 1,
          "longListField": [
            1,
            2
          ],
          "stringListField": [
            "a",
            "b"
          ]
        }
      },
      "int": 5
    }


# Generated at 2022-06-12 23:09:36.154422
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "fooBar": "a",
        "foobar": "b",
        "FooBar": "c",
        "fooBAR": "d",
        "foobAR": "e",
        "fooBAr": "f",
        "FOOBar": "g",
        "TargetGroupARNs": "h",
    }
    assert {
        "foo_bar": "a",
        "foobar": "b",
        "FooBar": "c",
        "foo_b_a_r": "d",
        "foob_a_r": "e",
        "foo_b_ar": "f",
        "F_o_o_Bar": "g",
        "target_group_a_r_ns": "h",
    } == camel_dict_to

# Generated at 2022-06-12 23:09:46.293592
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'Path': '/foo', 'Host': 'example.com'}, 'name': 'foo', 'tags': {'key':'value'}}
    assert camel_dict_to_snake_dict(camel_dict) == {'h_t_t_p_endpoint': {'path': '/foo', 'host': 'example.com'}, 'name': 'foo', 'tags': {'key': 'value'}}
    assert snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict)) == {'H_t_t_p_endpoint': {'Path': '/foo', 'Host': 'example.com'}, 'Name': 'foo', 'Tags': {'Key': 'value'}}
    assert camel_dict_to_snake

# Generated at 2022-06-12 23:09:53.111570
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:10:01.948903
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"HelloWorld": "foo"}, ignore_list=('Tags',)) == {'hello_world': 'foo'}
    assert camel_dict_to_snake_dict({"HTTPEndpoint": "foo"}) == {'http_endpoint': 'foo'}
    assert camel_dict_to_snake_dict({"HTTPSEndpoint": "foo"}) == {'https_endpoint': 'foo'}
    assert camel_dict_to_snake_dict({"HTTPS_Endpoint": "foo"}) == {'https_endpoint': 'foo'}
    assert camel_dict_to_snake_dict({"HTTPEndpoints": "foo"}) == {'http_endpoints': 'foo'}

# Generated at 2022-06-12 23:10:11.568374
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'camelCase': {'camelCase2': 'camelCase3',
                                'camel-dash': {'camel-dash2': 'camel-dash3'}}}
    camel_dict = camel_dict_to_snake_dict(camel_dict)
    assert camel_dict == {'camel_case': {'camel_case2': 'camelCase3',
                                         'camel_dash': {'camel_dash2': 'camel-dash3'}}}
    camel_dict = {'camelCase': {'camelCase2': 'camelCase3',
                                'camel-dash': {'camel-dash2': 'camel-dash3'}}}
    camel_dict = camel_dict_to_snake_dict(camel_dict, True)


# Generated at 2022-06-12 23:10:25.923546
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    data = {
        "BatchSize": 70,
        "HTTPEndpoint": {
            "ContentType": "text/plain",
            "Enabled": True,
            "EndpointUrl": "https://example.com/endpoint"
        },
        "Name": "test",
        "Tags": {
            "TagKey": "TagValue"
        }
    }

    expected = {
        "batch_size": 70,
        "h_t_t_p_endpoint": {
            "content_type": "text/plain",
            "enabled": True,
            "endpoint_url": "https://example.com/endpoint"
        },
        "name": "test",
        "tags": {
            "TagKey": "TagValue"
        }
    }

    result = camel_dict_to_sn

# Generated at 2022-06-12 23:10:35.802720
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "A": "a",
        "B": "b",
        "CamelAdminState": "camel_admin_state",
        "ResourceName": "resource_name",
        "Tags": {
            "HTTPEndpoint": "http_endpoint"
        },
        "Lists": [
            {
                "D": "d",
                "E": "e"
            },
            [
                {
                    "F": "f",
                    "G": "g"
                }
            ]
        ]
    }


# Generated at 2022-06-12 23:10:45.149031
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    def camel_to_snake_dict_test(input_camel_dict, expected_snake_dict, reversible=False):
        actual_snake_dict = camel_dict_to_snake_dict(input_camel_dict,
                                                     reversible=reversible)
        assert actual_snake_dict == expected_snake_dict, \
            "camel_dict_to_snake_dict failed with reversible %s" % \
            str(reversible)

    camel_dict = dict(KeyName="test")
    expected_camel_dict = dict(key_name="test")
    camel_to_snake_dict_test(camel_dict, expected_camel_dict)

    camel_dict = dict(HTTPEndpoint="test")

# Generated at 2022-06-12 23:10:53.824161
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:02.104181
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # test general
    camel_dict = {
        'testKey': 'testValue',
        'testKey1': 'testValue1',
        'testKey2': ['testValue2-0', 'testValue2-1'],
        'testKey3': {
            'testKey3-0': 'testValue3-0',
            'testKey3-1': ['testValue3-1-0', 'testValue3-1-1'],
        },
        'testKey4': {
            'testKey4-0': 'testValue4-0',
            'testKey4-1': {
                'testKey4-1-0': 'testValue4-1-0',
            },
        },
    }


# Generated at 2022-06-12 23:11:12.235141
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'LoadBalancerName': 'fake-elb',
        'LoadBalancerAttributes': {
            'CrossZoneLoadBalancing': {
                'Enabled': True
            },
            'AccessLog': {
                'Enabled': True,
                'S3BucketName': 'fake-bucket',
                'EmitInterval': 1
            }
        },
        'Instances': [
            'fake-instance-1',
            'fake-instance-2'
        ],
        'Tags': [
            {
                'Key': 'Name',
                'Value': 'fake-elb'
            }
        ]
    }

# Generated at 2022-06-12 23:11:22.759942
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
  # Given
  camel_dict = {
    'registeredAt': '2018-04-09T05:10:11.000Z',
    'accountId': '123456789012',
    'awsRegion': 'us-east-1',
    'tags': {
    'Name': 'test',
    'Owner': 'test@test.com',
    },
    'taskDefinitionArn': 'arn:aws:ecs:us-east-1:123456789012:task-definition/test-daemon:1',
    'type': 'daemon',
    'desiredCount': 1,
    'status': 'ACTIVE',
    'clusterArn': 'arn:aws:ecs:us-east-1:123456789012:cluster/test-cluster'
  }

  # When
  result

# Generated at 2022-06-12 23:11:30.239534
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {"StringList": ["test"], "String": "test", "Nested": {"Key": 1, "List": [1, 2], "String": "test"}}

    result = camel_dict_to_snake_dict(test_dict)
    assert result["string_list"] == ["test"]
    assert result["string"] == "test"
    assert result["nested"]["key"] == 1
    assert result["nested"]["list"] == [1, 2]
    assert result["nested"]["string"] == "test"


# Generated at 2022-06-12 23:11:36.998859
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {"TestValue1": "Value1", "TestValue2": {"TestValue3": "Value3", "TestValue4": "Value4", "TestValue5": "Value5"}}
    snake_dict = {"test_value1": "Value1", "test_value2": {"test_value3": "Value3", "test_value4": "Value4", "test_value5": "Value5"}}

    assert(camel_dict_to_snake_dict(camel_dict) == snake_dict)


# Generated at 2022-06-12 23:11:45.174171
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "StringType": "test_string",
        "IntegerType": 42,
        "HTTPDomainName": "mytest.test.com",
        "CamelCase": {
            "StringType": "test_string2"
        },
        "List":[{
            "StringType": "test_string3"
        }],
        "Tags": {
            "Environment": "Test",
            "Application": "Ansible"
        }
    }


# Generated at 2022-06-12 23:11:58.087077
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict(
        {"HttpEndpoint": "https://example.com",
         "Region": "eu-west-1",
         "StackName": "test-stack",
         "Tags": [{"Key": "ansible:stack", "Value": "test"}],
         "TunnelIds": ["tunnel-1", "tunnel-2"]}
        ) == {
            u'h_t_t_p_endpoint': 'https://example.com',
            u'region': 'eu-west-1',
            u'stack_name': 'test-stack',
            u'tags': [{'key': 'ansible:stack', 'value': 'test'}],
            u'tunnel_ids': ['tunnel-1', 'tunnel-2']
            }



# Generated at 2022-06-12 23:12:07.896845
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "fooBar": "baz",
        "URL": "http://example.com",
        "HTTPEndpoint": "http://http_endpoint.com",
        "tags": {
            "Key": "foo",
            "Value": "bar"
        }
    }

    snake_dict = {
        "foo_bar": "baz",
        "url": "http://example.com",
        "h_t_t_p_endpoint": "http://http_endpoint.com",
        "tags": {
            "Key": "foo",
            "Value": "bar"
        }
    }

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict



# Generated at 2022-06-12 23:12:16.845497
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'HTTPEndpoint': {
            'Type': 'HTTP',
            'URL': 'http://some.url',
            'Name': 'HTTPEndpoint',
            'Method': 'GET',
            'Payload': 'payload',
            'Headers': {
                'key': 'value'
            }
        },
        'SnsTopic': {
            'Type': 'SNS',
            'Topic': 'arn:aws:sns:region:account:topic',
            'Subject': 'subject',
            'Message': 'message'
        },
        'Tags': {
            'Tags': [
                {
                    'key': 'value'
                },
                {
                    'key': 'value'
                }
            ]
        }
    }

# Generated at 2022-06-12 23:12:24.611057
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Test for CamelCase
    assert camel_dict_to_snake_dict({'Key1': 'value1', 'Key2': 2}) == {'key1': 'value1', 'key2': 2}

    # Test for true CamelCase
    assert camel_dict_to_snake_dict({'Key1': 'value1', 'Key2': 2}, False, ['Tags']) == {'key1': 'value1', 'key2': 2}

    # Test for dromedaryCase
    assert camel_dict_to_snake_dict({'key1': 'value1', 'key2': 2}, False, ['Tags']) == {'key1': 'value1', 'key2': 2}

    # Test for snake_case

# Generated at 2022-06-12 23:12:35.791695
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "Protocols": [
                "http",
                "https"
            ],
            "Port": 80,
            "Path": "/webhook"
        },
        "Tags": {
            "Name": "test",
            "Stage": "dev"
        },
        "TargetGroups": [
            {
                "Name": "test",
                "TargetType": "instance"
            },
            {
                "Name": "test",
                "TargetType": "ip"
            }
        ]
    }
    original_camel_dict = deepcopy(camel_dict)
    assert original_camel_dict == camel_dict
    # Convert dict
    converted_camel_dict = camel_dict_to_snake_dict(camel_dict)

# Generated at 2022-06-12 23:12:41.868895
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    source_dict = {
        "HTTPEndpoint": {
            "HTTPPath": "/path",
            "HTTPMethod": "POST",
            "Detail": {
                "Foo": "Bar"
            },
            "TargetGroupARNs": [
                "1",
                "2"
            ]
        },
        "Tags": {
            "Foo": "Bar",
            "Bar": "Foo"
        }
    }

    result = camel_dict_to_snake_dict(source_dict)
    assert(result["h_t_t_p_endpoint"]["h_t_t_p_path"] == "/path")
    assert(result["h_t_t_p_endpoint"]["target_group_ar_ns"] == ["1", "2"])

# Generated at 2022-06-12 23:12:48.858185
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'FooBar': 'Baz', 'NotFun': 'Too',
                 'Tags': {"Key": "Name", "Value": "MyInstance"}}
    # Check that camel_dict_to_snake_dict works properly.
    assert camel_dict_to_snake_dict(test_dict) ==\
        {'foo_bar': 'Baz', 'not_fun': 'Too',
         'tags': {"Key": "Name", "Value": "MyInstance"}}

    # Check that snake_dict_to_camel_dict works properly.
    test_dict = {'foo_bar': 'Baz', 'not_fun': 'Too',
                 'tags': {"Key": "Name", "Value": "MyInstance"}}

# Generated at 2022-06-12 23:12:58.228358
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Given
    test_dict = {
        "key1": "value1",
        "key2": {
            "key3": "value3",
            "key4": "value4",
            "key5": "value5"
        },
        "key6": {
            "key7": {
                "key8": "value8"
            }
        }
    }
    # When
    result = camel_dict_to_snake_dict(test_dict)
    # Then

# Generated at 2022-06-12 23:13:04.480275
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:14.293488
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:13:32.209353
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {"Key1": "Value1", "Key2": "Value2", "Key3": {"subKey3": "subValue3"}}
    snake_dict = {"key1": "Value1", "key2": "Value2", "key3": {"sub_key3": "subValue3"}}
    result1 = camel_dict_to_snake_dict(camel_dict, True)
    result2 = camel_dict_to_snake_dict(camel_dict, False)
    assert result1 == {"H_key1": "Value1", "H_key2": "Value2", "H_key3": {"H_sub_key3": "subValue3"}}, \
        "camel_dict_to_snake_dict did not return expected results with reversible=True"
    assert result2 == snake_

# Generated at 2022-06-12 23:13:38.903862
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {
            "HTTPPath": "/ping",
            "HTTPMethod": "GET",
            "HTTPHeaders": [
                {
                    "Name": "header1",
                    "Value": "value1"
                },
                {
                    "Name": "header2",
                    "Value": "value2"
                }
            ]
        },
        "FooBarBaz": [{
            "FooBaz": [{
                "FooBar": [{
                    "Foo": "Foo",
                    "Bar": "Foo"
                }]
            }]
        }]
    }
    # OrderedDict is required for tests to pass on PY3
    from collections import OrderedDict
    expected_snake_dict = OrderedD

# Generated at 2022-06-12 23:13:50.956588
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    name = {'HTTPEndpoint': {'Name': 'EndpointName',
                             'HostName': 'hostname',
                             'HTTPS': {'Enabled': False,
                                       'CertificateSource': 'CLOUD'}}
            }
    assert camel_dict_to_snake_dict(name) == {'h_t_t_p_endpoint': {'name': 'EndpointName',
                                                                   'host_name': 'hostname',
                                                                   'https': {'enabled': False,
                                                                             'certificate_source': 'CLOUD'}}}

# Generated at 2022-06-12 23:14:00.040735
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_record = {
        'FirstName': 'John',
        'LastName': 'Doe',
        'LastModified': '2017-01-01',
        'WorkDone': {
            'Assignment': 'Development',
            'Length': '5 Days',
            'Width': '3 Feet',
            'Tags': [{
                'Tag': 'Brick',
                'Color': 'Red',
            }, {
                'Tag': 'Tile',
                'Color': 'Blue',
            }]
        }
    }

    # Test for conversion to snake case and ignore list

# Generated at 2022-06-12 23:14:08.326733
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel = {'foo': 'bar', 'Foo': 'bar'}
    bar_dict = camel_dict_to_snake_dict(camel)
    assert bar_dict['foo'] == 'bar'
    assert 'Foo' not in bar_dict
    assert bar_dict['foo'] == bar_dict['foo_1']

    camel = {'fooBar': 'bar'}
    bar_dict = camel_dict_to_snake_dict(camel)
    assert bar_dict['foo_bar'] == 'bar'

    camel = {'fooBar': {'bazBam': 'bar'}}
    bar_dict = camel_dict_to_snake_dict(camel)
    assert bar_dict['foo_bar']['baz_bam'] == 'bar'


# Generated at 2022-06-12 23:14:18.677611
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Test camel_dict_to_snake_dict function"""
    camel_dict = {
        'HTTPEndpoint': {
            'Enabled': True,
            'Path': '/path/to/endpoint',
            'Port': 12345
        },
        'MyString': 'weird string',
        'MyNumber': 123,
        'Tags': {
            'Name': 'MyTag'
        }
    }
    expected_snake_dict = {
        'h_t_t_p_endpoint': {
            'enabled': True,
            'path': '/path/to/endpoint',
            'port': 12345
        },
        'my_string': 'weird string',
        'my_number': 123,
        'tags': {
            'Name': 'MyTag'
        }
    }

   

# Generated at 2022-06-12 23:14:28.305656
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    class_name = 'camelDictTest'

    # Camel Case
    test_camel_case = {
        'CamelCase': True,
        'CamelDict': None,
        'CamelList': [
            {'Camel': 'Case'},
            {'List': 'Item'}
        ],
        'CamelNested': {
            'NestedList': [
                'Value1',
                'Value2'
            ]
        }
    }

    # Expected result of camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:31.894650
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": {}
    }

    snake_dict = {
        "h_t_t_p_endpoint": {}
    }

    assert camel_dict_to_snake_dict(camel_dict) == snake_dict



# Generated at 2022-06-12 23:14:39.552110
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:49.078251
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_camel = {'HTTPEndpoint': 'foo', 'targetGroups': [], 'Tags': {'foo': 'bar'}}
    expected_output_1 = {'h_t_t_p_endpoint': 'foo', 'target_groups': [], 'tags': {'foo': 'bar'}}
    expected_output_2 = {'HTTPEndpoint': 'foo', 'target_groups': [], 'tags': {'foo': 'bar'}}
    assert camel_dict_to_snake_dict(input_camel, ignore_list=('tags',)) == expected_output_1
    assert camel_dict_to_snake_dict(input_camel, reversible=True, ignore_list=('tags',)) == expected_output_2

# Generated at 2022-06-12 23:15:04.949697
# Unit test for function recursive_diff
def test_recursive_diff():
    # Initialize two dictionaries
    dict1 = {'name': {'firstname': 'John', 'lastname': 'Doe'},
             'job': 'Software Developer',
             'email': 'jdoe@example.com',
             'phone': '1234567'
             }

    dict2 = {'name': {'firstname': 'Jane', 'lastname': 'Doe'},
             'job': 'Software Developer',
             'email': 'jdoe@example.com',
             'phone': '1234567'
             }

    # Recursively diff two dictionaries
    assert recursive_diff(dict1, dict2) == ({'name': {'firstname': 'John'}},
                                            {'name': {'firstname': 'Jane'}})

    # Another test case

# Generated at 2022-06-12 23:15:12.874119
# Unit test for function dict_merge
def test_dict_merge():
    assert dict_merge({}, {'key': 'value'}) == {'key': 'value'}
    assert dict_merge({'key': 'value'}, {}) == {'key': 'value'}
    assert dict_merge({'key': 'value'}, {'key': 'value'}) == {'key': 'value'}
    assert dict_merge({'key': 'value'}, {'key': 'value1'}) == {'key': 'value1'}
    assert dict_merge({'key': 'value1'}, {'key': 'value2'}) == {'key': 'value2'}
    assert dict_merge({'key1': 'value1'}, {'key2': 'value2'}) == {'key1': 'value1', 'key2': 'value2'}



# Generated at 2022-06-12 23:15:20.768298
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():
    # Testing of basic case
    test_dict = {
        'foo_bar': {
            'baz_quux': 'quuz'
        }
    }
    expected_output = {
        'fooBar': {
            'bazQuux': 'quuz'
        }
    }
    assert(expected_output == snake_dict_to_camel_dict(test_dict))

    # Testing of basic case with first letter capitalized
    expected_output = {
        'FooBar': {
            'BazQuux': 'quuz'
        }
    }
    assert(expected_output == snake_dict_to_camel_dict(expected_output, capitalize_first=True))

    # Testing of complex case

# Generated at 2022-06-12 23:15:31.646958
# Unit test for function dict_merge
def test_dict_merge():
    a = {}
    b = {"key1": "value1", "key2": "value2"}
    c = {}
    d = {"key1": "value1", "key2": {"key2-1": "value2-1", "key2-2": "value2-2"}, "key3": "value3"}
    e = {"key1": "value1", "key2": {"key2-1": "value2-1", "key2-2": "value2-2", "key2-3": "value2-3"}, "key3": "value3"}
    f = {"key1": "value1", "key3": "value3"}
    g = {"key1": "v1", "key2": "v2", "key3": "v3"}

# Generated at 2022-06-12 23:15:41.636989
# Unit test for function recursive_diff
def test_recursive_diff():
    """Unit test for function recursive_diff"""
    # Empty dictionaries
    assert not recursive_diff({}, {})

    # One empty dictionary
    assert recursive_diff({}, {'foo': {'bar': 'baz'}}) == ({}, {'foo': {'bar': 'baz'}})

    # One empty dictionary
    assert recursive_diff({'foo': {'bar': 'baz'}}, {}) == ({'foo': {'bar': 'baz'}}, {})

    # Equal dictionaries
    assert not recursive_diff({'foo': {'bar': 'baz'}}, {'foo': {'bar': 'baz'}})

    # Dictionaries with difference at root level

# Generated at 2022-06-12 23:15:48.779022
# Unit test for function snake_dict_to_camel_dict
def test_snake_dict_to_camel_dict():

    camel_dict = {
            "requiredTags": [],
            "resourceType": "EC2",
            "optionalTags": [
                "Department",
                "Environment",
                "Project",
                "Purpose",
                "Service"
            ],
            "resourceIds": [
                "i-03f1223cf44a0bca9"
            ],
            "resourceArns": [],
            "remainingTimeInDays": 60
        }


# Generated at 2022-06-12 23:15:58.849778
# Unit test for function dict_merge
def test_dict_merge():
    '''
    tests the dict_merge function with a variety of inputs
    '''
    a = {'a': 1, 'b': {1: 1, 2: 2}, 'd': 6}
    b = {'c': 3, 'b': {2: 7}, 'd': {'z': [1, 2, 3]}}

    merge = dict_merge(a, b)
    assert merge ==  {'a': 1,
                      'b': {1: 1, 2: 7},
                      'c': 3,
                      'd': {'z': [1, 2, 3]}}

    a = {'a': 1, 'b': {1: 1, 2: 2}, 'd': 6}

# Generated at 2022-06-12 23:16:07.510719
# Unit test for function recursive_diff
def test_recursive_diff():
    left = {'foo': {'bar': 'baz'}, 'spam': 'foo'}
    right = {'foo': {'bar': 'foo'}, 'spam': 'baz'}
    expected = ({'foo': {'bar': 'baz'}}, {'foo': {'bar': 'foo'}})
    assert(recursive_diff(left, right) == expected)

    left = {'foo': {'bar': 'baz'}, 'spam': 'foo'}
    right = {'foo': {'bar': 'foo'}, 'baz': 'baz'}
    expected = ({'foo': {'bar': 'baz'}, 'spam': 'foo'}, {'foo': {'bar': 'foo'}, 'baz': 'baz'})

# Generated at 2022-06-12 23:16:14.495921
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert(camel_dict_to_snake_dict(
        {'Foo': 'bar',
         'Baz': 'qux'}
    ) == {'foo': 'bar', 'baz': 'qux'})

# Generated at 2022-06-12 23:16:19.776861
# Unit test for function dict_merge
def test_dict_merge():
    a = {"k1": "v1", "k2": {"k22": "v22", "k23": "v23"}}
    b = {"k1": "v2", "k2": {"k21": "v21", "k23": "v24"}}
    assert dict_merge(a, b) == {'k1': 'v2', 'k2': {'k21': 'v21', 'k22': 'v22', 'k23': 'v24'}}
    assert dict_merge(a, a) == a

    a = {"k1": "v1", "k2": {"k22": "v22", "k23": "v23"}, "k3": {"1": 1, "2": 2}}