

# Generated at 2022-06-12 23:06:53.768037
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "HTTPEndpoint": "my_http_endpoint",
        "Tags": {
            "my_first_key": "my_first_value"
        }
    }

    expected_dict = {
        "h_t_t_p_endpoint": "my_http_endpoint",
        "tags": {
            "my_first_key": "my_first_value"
        }
    }

    assert expected_dict == camel_dict_to_snake_dict(camel_dict)

    # Test two way conversion
    assert camel_dict == snake_dict_to_camel_dict(camel_dict_to_snake_dict(camel_dict, reversible=True))


# Generated at 2022-06-12 23:07:04.598377
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "fooBarFoo": "foobarfoo",
        "BazFooBar": "bazfoobar",
        "aB_cd_ef": "aB_cd_ef",
        "HTTPEndpoint": "httpendpoint",
        "HTTPSEndpoint": "http_sendpoint",
        "TargetGroupARNs": "target_group_ar_ns",
        "Tags": {
            "Environment": "dev",
            "Name": "aB_cd_ef"
        }
    }


# Generated at 2022-06-12 23:07:14.736011
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test 1:
    a = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': 4
        }
    }
    b = {
        'a': 1,
        'b': 2,
        'c': {
            'd': 3,
            'e': 5
        }
    }
    c = {
        'a': 2,
        'b': 3,
        'c': {
            'd': 4,
            'e': 4
        }
    }
    assert recursive_diff(a, b) == ({'c': {'e': 4}}, {'c': {'e': 5}})

# Generated at 2022-06-12 23:07:23.894471
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:07:34.569105
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    from collections import OrderedDict
    from ansible_collections.ansible.amazon.plugins.module_utils.core import camel_dict_to_snake_dict


# Generated at 2022-06-12 23:07:41.489918
# Unit test for function dict_merge
def test_dict_merge():
    a = {'a': 1, 'b': {'ba': 2, 'bb': 3}, 'c': {'ca': 4, 'cc': {'cca': 5, 'ccc': 6}}, 'd': 7}
    b = {'a': 1, 'b': {'ba': 20, 'bc': 30}, 'c': {'ca': 4, 'cc': {'ccb': 50, 'ccc': 60}}, 'g': 70}
    assert dict_merge(a, b) == {'a': 1, 'b': {'ba': 20, 'bb': 3, 'bc': 30}, 'c': {'ca': 4, 'cc': {'cca': 5, 'ccb': 50, 'ccc': 60}}, 'd': 7, 'g': 70}

# Generated at 2022-06-12 23:07:52.862321
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'common': {
            'str_value': 'value_1',
            'int_value': 2,
            'bool_value': True,
            'list_value': ['a', 'b'],
            'sub_dict': {
                'sub_str': 'sub_value_1'
            }
        },
        'diff': {
            'sub_sub_dict': {
                'subsub_str': 'subsub_value_1'
            }
        }
    }

# Generated at 2022-06-12 23:08:02.476260
# Unit test for function dict_merge
def test_dict_merge():
    a = { "a": 1, "d": { "a": 5, "b": 7 }, "c": 3 }
    b = { "b": 2, "c": { "a": 4 }, "d": { "c": 6 } }

    c = { "a": 1, "d": { "a": 5, "b": 7, "c": 6 },
          "b": 2, "c": { "a": 4 }, "e": 3 }

    assert dict_merge(a, b) == c

    a = { "a": 1 }
    b = { "b": 2 }

    c = { "a": 1, "b": 2 }

    assert dict_merge(a, b) == c

    a = { "a": 1, "b": 2 }
    b = { "b": 3 }


# Generated at 2022-06-12 23:08:07.266241
# Unit test for function dict_merge
def test_dict_merge():
    a = {
        'b': '1',
        'c': {
            'd': '2',
            'e': {
                'f': '3',
                'g': '4'
            }
        }
    }
    b = {
        'c': {
            'e': {
                'f': '5',
                'i': '6'
            }
        },
        'h': '7'
    }

    assert(dict_merge(a, b) == {
        'b': '1',
        'c': {
            'd': '2',
            'e': {
                'f': '5',
                'g': '4',
                'i': '6'
            }
        },
        'h': '7'
    })


# Generated at 2022-06-12 23:08:17.845612
# Unit test for function recursive_diff
def test_recursive_diff():
    dict1 = {
        'a': 1,
        'b': {
            'd': 2,
            'e': 3,
            'f': 4,
        },
        'c': 5,
    }
    dict2 = {
        'a': 10,
        'b': {
            'd': 20,
            'e': 3,
            'g': 4,
        },
        'c': 50,
        'h': 6,
    }
    diff = {
        'a': (1, 10),
        'b': {
            'd': (2, 20),
            'f': (4, None),
            'g': (None, 4),
        },
        'c': (5, 50),
        'h': (None, 6),
    }

# Generated at 2022-06-12 23:08:30.277970
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        u'expectThis': {
            u'toBeLikeThis': [{u'andThis': u'likeThis'}]
        },
        u'unless': {
            u'youPass': True,
            u"withThese_keys": u"which_won't_change",
            u"inWhich_case": u"nothing_changes",
        }
    }

    ansible_dict = camel_dict_to_snake_dict(test_dict)


# Generated at 2022-06-12 23:08:38.093868
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # True statements
    assert camel_dict_to_snake_dict({"A": 1, "B": 2}, reversible=False) == {"a": 1, "b": 2}
    assert camel_dict_to_snake_dict({"CamelCase": 1, "CamelCaseB": 2}, reversible=False) == {"camel_case": 1, "camel_case_b": 2}
    assert camel_dict_to_snake_dict({"CamelCase": 1, "camelCase": 2}, reversible=False) == {"camel_case": 1, "camel_case": 2}
    assert camel_dict_to_snake_dict({"CamelCase": 1, "Camel": 2}, reversible=False) == {"camel_case": 1, "camel": 2}
    assert camel_dict_to_

# Generated at 2022-06-12 23:08:48.353803
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoints': [{'HTTPEndpoint': {'EndpointName': 'test_endpoint', 'EndpointURL': 'https://this.is.an.endpoint'}}],
                  'Tags': [{'Key': 'This', 'Value': 'That'}, {'Key': 'These', 'Value': 'Those'}]}
    # Test normal conversion
    assert camel_dict_to_snake_dict(camel_dict) == {'http_endpoints': [{'http_endpoint': {'endpoint_name': 'test_endpoint', 'endpoint_url': 'https://this.is.an.endpoint'}}],
                                                   'tags': [{'key': 'This', 'value': 'That'}, {'key': 'These', 'value': 'Those'}]}
    # Test

# Generated at 2022-06-12 23:08:58.177071
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {'HTTPEndpoint': 'dummy_end_point',
                 'Tags': {'Key': 'dummy_tag_key',
                          'Value': 'dummy_tag_value'},
                 'ResourceArns': ['gfx_0'],
                 'ResourceArnList': ['gfx_0', 'gfx_1']
                 }

    test_dict_expected = {'h_t_t_p_endpoint': 'dummy_end_point',
                          'tags': {'Key': 'dummy_tag_key',
                                   'Value': 'dummy_tag_value'},
                          'resource_arns': ['gfx_0'],
                          'resource_arn_list': ['gfx_0', 'gfx_1']
                          }

    test_dict_re

# Generated at 2022-06-12 23:09:08.553393
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "InstanceName": "TestInstance",
        "SystemDisk": {
            "DiskSize": 40,
        },
        "Tags": {
            "Tags": [
                {
                    "Key": "TestKey1",
                    "Value": "TestValue1",
                }
            ]
        }
    }
    result_dict = camel_dict_to_snake_dict(test_dict, True)
    assert result_dict["instance_name"] == "TestInstance"
    assert result_dict["system_disk"]["disk_size"] == 40
    assert result_dict["tags"]["tags"][0]["key"] == "TestKey1"
    assert result_dict["tags"]["tags"][0]["value"] == "TestValue1"

    result_dict = camel_dict_

# Generated at 2022-06-12 23:09:17.764448
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': {'HTTPURL': 'https://abc.com', 'HTTPTimeout': 1, 'HTTPHeaders': [{'Key': 'a', 'Value': 'b'}]}}
    expected_output = {'h_t_t_p_endpoint': {'h_t_t_p_u_r_l': 'https://abc.com', 'h_t_t_p_timeout': 1, 'h_t_t_p_headers': [{'key': 'a', 'value': 'b'}]}}
    assert camel_dict_to_snake_dict(camel_dict) == expected_output


# Generated at 2022-06-12 23:09:24.775390
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:09:34.772270
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({}) == {}
    assert camel_dict_to_snake_dict({'name': 'value'}) == {'name': 'value'}
    assert camel_dict_to_snake_dict({'Name': 'value'}) == {'name': 'value'}
    assert camel_dict_to_snake_dict({'Name': {'Name': 'value'}}) == {'name': {'name': 'value'}}
    assert camel_dict_to_snake_dict({'names': ['one', 'two']}) == {'names': ['one', 'two']}
    assert camel_dict_to_snake_dict({'Names': ['one', 'two']}) == {'names': ['one', 'two']}
    assert camel_dict_to_snake_

# Generated at 2022-06-12 23:09:45.245473
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({"UserId": "test"}) == {'user_id': 'test'}
    assert camel_dict_to_snake_dict({"UserId": "test"}, reversible=True) == {'u_s_e_r_id': 'test'}

    assert camel_dict_to_snake_dict({"TargetGroupARNs": ["test", "test2"]}) == {'target_group_arns': ['test', 'test2']}
    assert camel_dict_to_snake_dict({"TargetGroupARNs": ["test", "test2"]}, reversible=True) == {'target_group_a_r_n_s': ['test', 'test2']}


# Generated at 2022-06-12 23:09:52.114604
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    input_dict = {'testList': [{'testListInList': []}],
                        'testCamelCase': ['string1', 'string2'],
                        'testCamelCaseTag': ['tag1', 'tag2'],
                        'testDict': {'testDictInDict': {'testDictInDictInDict': 'string'}},
                        'Tags': [{'Key': 'A', 'Value': 'B'}, {'Key': 'C', 'Value': 'D'}],
                        'testCamelCaseString': 'string'}
    snake_dict = camel_dict_to_snake_dict(input_dict, reversible=True)

# Generated at 2022-06-12 23:10:04.331082
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({ 'HTTPEndpoint': 'abc' }) == { 'http_endpoint': 'abc' }
    assert camel_dict_to_snake_dict({ 'HTTPEndpoint': 'abc' }, True) == { 'h_t_t_p_endpoint': 'abc' }
    assert camel_dict_to_snake_dict({'Tags': {'Key': 'abcd', 'Value': 'efgh'}}) == \
        {'tags': {'key': 'abcd', 'value': 'efgh'}}

# Generated at 2022-06-12 23:10:13.552403
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test various inputs to camel_dict_to_snake_dict function
    """

    original_dict = {'SomeKey': 'value',
                     'AnotherKey': 'value',
                     'Key': {'SubKey': 'value',
                             'SubKey2': 'value'},
                     'Key2': {'SubKey': 'value',
                              'SubKey2': {'SubSubKey': 'value'},
                              'SubKey3': 'value'}}


# Generated at 2022-06-12 23:10:24.742786
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'HTTPEndpoint': 'foo',
                  'HTTPEndpoints': [{'Name': 'foo'}, {'Name': 'bar'}],
                  'HTTPEndpointStatus': 'bar',
                  'HTTPEndpointStatuses': [{'Name': 'foo'}, {'Name': 'bar'}],
                  'name': 'bar'}


# Generated at 2022-06-12 23:10:32.229476
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {}
    camel_dict['ContainerDefinitions'] = [{'hostNetwork': True, 'logConfiguration': {'logDriver': 'awslogs', 'options': {'awslogs-group': '/ecs/ecsChallenge', 'awslogs-region': 'us-west-2', 'awslogs-stream-prefix': 'ecs'}}, 'name': 'test_network_host', 'privileged': True, 'readonlyRootFilesystem': False, 'memory': 128, 'essential': True, 'image': 'netcat', 'cpu': 0, 'portMappings': [{'protocol': 'tcp', 'containerPort': 80, 'hostPort': 1337}]}]

    snake_dict_out = camel_dict_to_snake_dict(camel_dict)

    snake_dict_expected = {}


# Generated at 2022-06-12 23:10:40.639526
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {"fooBar": {"fooBar": {"barBaz": {"fooBar": [1, 2, 3]}}},
                  "aBc": 1,
                  "PizzaToppings": ["pepperoni", "mozzarella", "salami"],
                  "ignoredDict": {"fooBar": "barBaz"},
                  "ignoredList": ["fooBar", {"barBaz": "ignoreMe"}],
                  "submissionMetadata": {"submissionId": "sdaflkjklsfdaf"},
                  "tags": {"key1": "value1"}}

    # Test both reversible and non-reversible functions

# Generated at 2022-06-12 23:10:49.942780
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'FooBar': {'TargetGroupHealthyThresholdCount': 2,
                             'TargetGroupName': 'foo-bar-tg',
                             'TargetGroupPort': 80,
                             'TargetGroupProtocol': 'HTTPS',
                             'TargetGroupUnhealthyThresholdCount': 2}}

    assert camel_dict_to_snake_dict(camel_dict) == \
        {'foo_bar': {'target_group_healthy_threshold_count': 2,
                     'target_group_name': 'foo-bar-tg',
                     'target_group_port': 80,
                     'target_group_protocol': 'HTTPS',
                     'target_group_unhealthy_threshold_count': 2}}

# Generated at 2022-06-12 23:10:57.934521
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    d = {'HTTPEndpoint': 'test',
         'LastSuccessfulInvocationTime': 'test',
         'LastSuccessfulExecutionTime': 'test',
         'LastSuccessfulHeartbeat': 'test',
         'LastFailureHeartbeat': 'test',
         'Tags': {'unique': 'dict'},
         'TargetGroupARNs': ['arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/6d0ecf831eec9f09']
         }

# Generated at 2022-06-12 23:11:07.116420
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {}
    test_dict["aCamelName"]="aCamelName"
    test_dict["Camel"]=1
    test_dict["aTwoCamelName"]=2
    test_dict["aTwoCamel"]=3
    test_dict["aTCamelName"] = {'aTCamelName':'aTCamelName', 'camel':1}
    test_dict["camel"]=4
    test_dict["CamelName"]=5
    test_dict["aTwoCamelName"]=6
    test_dict["aCamelName"]=7
    test_dict["aCamel"]=8
    test_dict["camelName"]=9


# Generated at 2022-06-12 23:11:14.224391
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """Unit tests for function camel_dict_to_snake_dict

    The function is tested for a variety of inputs & outputs, and
    also for behaviour when reversible=True and ignore_list=...
    """

    example_dict = {"HTTPEndpoint": {"HTTPPath": "/health",
                                     "HTTPMethod": "GET",
                                     "SuccessCodes": ["200-299"],
                                     "TimeoutSeconds": 7
                                     },
                    "source_version": "some_version"
                    }
    expected_dict = {"http_endpoint": {"http_path": "/health",
                                       "http_method": "GET",
                                       "success_codes": ["200-299"],
                                       "timeout_seconds": 7
                                       },
                     "source_version": "some_version"
                     }

    assert expected_dict

# Generated at 2022-06-12 23:11:20.808319
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
  assert(camel_dict_to_snake_dict({
      'HTTPEndpoint': {
          'EndpointURL': 'http://127.0.0.1:80'
      },
      'Type': 'HTTP'
  }) == {
      'h_t_t_p_endpoint': {
          'endpoint_url': 'http://127.0.0.1:80'
      },
      'type': 'HTTP'
  })



# Generated at 2022-06-12 23:11:34.595942
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:42.232671
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:11:49.369659
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    x = {'myAttribute': {'myList': [{'myItem': 5}, {'myItem': 6}, {'myItem': 7}],
                             'myBool': True,
                             'myInt': 1,
                             'myString': 'bla'}}
    y = {'my_attribute': {'my_list': [{'my_item': 5}, {'my_item': 6}, {'my_item': 7}],
                               'my_bool': True,
                               'my_int': 1,
                               'my_string': 'bla'}}
    assert camel_dict_to_snake_dict(x) == y


# Generated at 2022-06-12 23:11:59.163694
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        'Group': 'test_group',
        'SecurityGroups': ['sg-12345678', 'sg-abcdefgh'],
        'Tags': {
            'Name': 'test_name'
        }
    }
    test_dict_camel = {
        'Group': 'test_group',
        'SecurityGroups': ['sg-12345678', 'sg-abcdefgh'],
        'Taggs': {
            'Name': 'test_name'
        }
    }
    test_dict_camel_reversible = {
        'Group': 'test_group',
        'SecurityGroups': ['sg-12345678', 'sg-abcdefgh'],
        'HTTPPEndpoint': {
            'Name': 'test_name'
        }
    }
    test

# Generated at 2022-06-12 23:12:08.993980
# Unit test for function recursive_diff
def test_recursive_diff():
    from operator import ne
    dict1 = dict(a=[dict(b=1, c=[1, 2, 3, 4], d=dict(nested='dict', values='here'))])
    dict2 = dict(a=[dict(b=1, c=[1, 2, 3, 5], d=dict(nested='dict', values='here'))])
    expected_result = ({'a': [{'c': [{3: 4, 4: 5}]}]}, {'a': [{'c': [{3: 5, 4: 4}]}]})
    deep_eq = lambda x, y: all(map(ne, x, y))
    assert deep_eq(recursive_diff(dict1, dict2), expected_result)

# Generated at 2022-06-12 23:12:17.978744
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    x = {
        'Args': [
            '--foo'
        ],
        'AppName': 'MyApp',
        'Tags': {
            'Tag1': 'Tag1Value',
            'Tag2': 'Tag2Value'
        }
    }

    y = {
        'args': [
            '--foo'
        ],
        'app_name': 'MyApp',
        'tags': {
            'Tag1': 'Tag1Value',
            'Tag2': 'Tag2Value'
        }
    }

    z = {
        'app_name': 'MyApp',
        'tags': {
            'tag1': 'Tag1Value',
            'tag2': 'Tag2Value'
        }
    }


# Generated at 2022-06-12 23:12:23.876874
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'Action': 'RunInstances',
        'ImageId': 'ami-80f715e0',
        'MinCount': 1,
        'MaxCount': 1,
        'InstanceType': 't1.micro',
        'Tags': [{'Key': 'Name', 'Value': 'test'}],
    }

    correct_result = {
        'action': 'RunInstances',
        'image_id': 'ami-80f715e0',
        'min_count': 1,
        'max_count': 1,
        'instance_type': 't1.micro',
        'tags': [{'Key': 'Name', 'Value': 'test'}],
    }

    assert camel_dict_to_snake_dict(camel_dict) == correct_result



# Generated at 2022-06-12 23:12:34.935517
# Unit test for function recursive_diff
def test_recursive_diff():
    # Test a simple set of dictionaries
    simple_dict1 = {'a': 1, 'b': 2, 'c': 3}
    simple_dict2 = {'a': 1, 'b': 2, 'c': 4}
    simple_diff = recursive_diff(simple_dict1, simple_dict2)
    assert simple_diff == ({}, {'c': 4})
    assert recursive_diff(simple_dict2, simple_dict1) == ({'c': 4}, {})
    # Test a dictionary with a dictionary
    nested_dict1 = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': [1, 2, {'f': 3}, 4]}}

# Generated at 2022-06-12 23:12:44.321652
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert {'Id': 'id'} == camel_dict_to_snake_dict({'Id': 'id'})
    assert {'Id': {'Id': 'id'}} == camel_dict_to_snake_dict({'Id': {'Id': 'id'}})
    assert {'id': 'id'} == camel_dict_to_snake_dict({'Id': 'id'}, reversible=True)
    assert {'Id': 'id'} == camel_dict_to_snake_dict({'id': 'id'})
    assert {'Id': {'Id': 'id'}} == camel_dict_to_snake_dict({'Id': {'id': 'id'}})
    assert {'Cpu': 1} == camel_dict_to_snake_dict({'Cpu': 1})

# Generated at 2022-06-12 23:12:54.456532
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    camel_dict = {'Example':
                      [
                          {
                              'Key1': 'Value1',
                              'Key2': 'Value2',
                              'Key3': 'Value3',
                              'Key4': ['Value4', 'Value5', 'Value6'],
                              'Key5': 'Value7'
                          },
                          {
                              'Key1': 'Value8',
                              'Key2': 'Value9',
                              'Key3': 'Value10',
                              'Key4': ['Value11', 'Value12', 'Value13'],
                              'Key5': 'Value14'
                          }
                      ]
                  }

    # Test non-reversible mode

# Generated at 2022-06-12 23:13:13.572798
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'TestString': 'string',
        'TestNumber': 0,
        'TestBoolean': False,
        'TestList': [0, 1, 2],
        'TestObject': {
            'TestString': 'string',
            'TestNumber': 0,
            'TestBoolean': False,
        },
        'TestListOfObjects': [{
            'TestString': 'string',
            'TestNumber': 0,
            'TestBoolean': False,
        }, {
            'TestString': 'string',
            'TestNumber': 0,
            'TestBoolean': False,
        }],
    }

# Generated at 2022-06-12 23:13:22.028762
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        'HTTPEndpoint': {
            'Endpoint': {'DataType': 'string', 'StringValue': 'https://execute-api.us-east-1.amazonaws.com/Prod/MyFunction'},
            'RequestParameters': dict(),
            'Method': 'POST'
        },
        'TargetGroupARNs': {
            'Ref': 'TargetGroupARNs'
        },
        'Tags': {
            'tag1': 'value1',
            'tag2': 'value2'
        }
    }

# Generated at 2022-06-12 23:13:30.459699
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert camel_dict_to_snake_dict({'FooBar': 'baz', "sub": {'FooBar': 'baz'}},
                                    ignore_list=('Tags',)) == {'foo_bar': 'baz', "sub": {'foo_bar': 'baz'}}
    assert camel_dict_to_snake_dict({'FooBar': 'baz', "sub": {'FooBar': 'baz'}},
                                    ignore_list=('Tags',),
                                    reversible=True) == {'f_oo_bar': 'baz', "sub": {'f_oo_bar': 'baz'}}

# Generated at 2022-06-12 23:13:35.283703
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {
        "CamelCase": {
            "HTTPEndpoint": {
                "Target": "ml.m4.xlarge"
            }
        }
    }
    assert camel_dict_to_snake_dict(camel_dict) == {
        "camel_case": {
            "http_endpoint": {
                "target": "ml.m4.xlarge"
            }
        }
    }



# Generated at 2022-06-12 23:13:40.855132
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    # Case 1: simple dictionary with a single key value pair
    camel_dict = { 'key1' : 'value1' }
    expected_snake_dict = { 'key1' : 'value1' }
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert(expected_snake_dict == snake_dict)

    # Case 2: simple dictionary with multiple key value pairs
    camel_dict = { 'key1' : 'value1', 'key2' : 'value2' }
    expected_snake_dict = { 'key1' : 'value1', 'key2' : 'value2' }
    snake_dict = camel_dict_to_snake_dict(camel_dict)
    assert(expected_snake_dict == snake_dict)

    # Case 3: simple

# Generated at 2022-06-12 23:13:53.407183
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:01.929156
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:05.488945
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = {'Key1': 'Value1', 'Key2': 'Value2'}
    expected_result = {'key1': 'Value1', 'key2': 'Value2'}
    result = camel_dict_to_snake_dict(camel_dict)
    assert result == expected_result



# Generated at 2022-06-12 23:14:16.154077
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_list = [{
        'a': 'a',
        'b': {
            'b1': 'b1',
            'b2': {
                'b2a': 'b2a'
            }
        }
    }, {
        'c': 'c'
    }]


# Generated at 2022-06-12 23:14:23.913523
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """ Unit test for camel_dict_to_snake_dict """

    # pylint: disable=unused-variable
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    # List of test cases

# Generated at 2022-06-12 23:14:38.893490
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    test_dict = {
        "keyOne": "valueOne",
        "keyTwo": "valueTwo",
        "keyThree": [
            {
                "keyThreeA": "valueThreeA",
                "keyThreeB": "valueThreeB"
            },
            {
                "keyThreeC": "valueThreeC",
                "keyThreeD": "valueThreeD"
            }
        ],
        "keyFour": [
            {
                "keyFourA": "valueFourA",
                "keyFourB": "valueFourB"
            },
            "valueFourC"
        ],
        "tags": {
            "one": "one",
            "two": "two"
        }
    }


# Generated at 2022-06-12 23:14:48.766639
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:14:58.915075
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    assert _camel_to_snake('camelCase') == 'camel_case'
    assert _camel_to_snake('CamelCase') == 'camel_case'
    assert _camel_to_snake('CamelCase', True) == 'c_a_m_e_l_c_a_s_e'
    assert _camel_to_snake('HTTPEndpoint') == 'http_endpoint'
    assert _camel_to_snake('HTTPEndpoint', True) == 'h_t_t_p_endpoint'
    assert _camel_to_snake('TargetGroupARNs') == 'target_group_a_r_ns'
    assert _camel_to_snake('TargetGroupARNs', True) == 'target_group_a_r_ns'
   

# Generated at 2022-06-12 23:15:04.118915
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    for test_case, expected_output in [
        ({'Colors': ['Red', 'Green', 'Blue']}, {'colors': ['Red', 'Green', 'Blue']}),
        ({'Red': 1, 'Green': 2, 'Blue': 3}, {'red': 1, 'green': 2, 'blue': 3})
    ]:
        assert camel_dict_to_snake_dict(test_case) == expected_output

# Generated at 2022-06-12 23:15:12.277279
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {"Foo": {"Bar": 1, "Baz": 2, "Bam": {"Boom": "hello"}},
                 "Hello": "world",
                 "Where": "God",
                 "Tags": {'key': "value"},
                 "TagList": [{'key': "value"}, {'key': "value1"}, {'key': "value2"}],
                 "FooBarBaz": ["ham", "eggs"]}

    converted_dict = camel_dict_to_snake_dict(test_dict)
    assert 'foo' in converted_dict
    assert 'bar' in converted_dict['foo']
    assert 'baz' in converted_dict['foo']
    assert 'bam' in converted_dict['foo']
    assert 'boom' in converted_dict['foo']['bam']

# Generated at 2022-06-12 23:15:19.115930
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:29.348719
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    """
    Test:
        - dict has all keys converted to snake case
        - recursive dict has all keys converted to snake case
        - list of dicts has all keys converted to snake case
        - list of lists is not converted
        - map of string values is not converted
    """


# Generated at 2022-06-12 23:15:39.754554
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict(
        {'FooBar': {}},
        reversible=False,
    ) == {'foo_bar': {}}

    assert camel_dict_to_snake_dict(
        {'FooBar': {'FooBaz': {}}},
        reversible=False,
    ) == {'foo_bar': {'foo_baz': {}}}

    assert camel_dict_to_snake_dict(
        {'FooBar': {'FooBaz': {'FooQux': {}}}},
        reversible=False,
    ) == {'foo_bar': {'foo_baz': {'foo_qux': {}}}}


# Generated at 2022-06-12 23:15:47.725025
# Unit test for function camel_dict_to_snake_dict

# Generated at 2022-06-12 23:15:57.787939
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    test_dict = {
        "AutoScalingGroupName": "test_group",
        "DesiredCapacity": 1,
        "MaxSize": 1,
        "MinSize": 1,
        "Tags": [
            {
                "Key": "Name",
                "Value": "test_group"
            }
        ],
        "VPCZoneIdentifier": [
            "test"
        ]
    }

# Generated at 2022-06-12 23:16:23.438021
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():
    camel_dict = dict(
        OptionSettings=[
            dict(
                Namespace='aws:autoscaling:asg',
                OptionName='MinSize',
                Value='1'
            ),
            dict(
                Namespace='aws:autoscaling:asg',
                OptionName='MaxSize',
                Value='2'
            )

        ],
        Status='PROCESSING',
        TemplateName='MyTemplate',
        TemplateDescription='MyTemplate'
    )


# Generated at 2022-06-12 23:16:32.510100
# Unit test for function camel_dict_to_snake_dict
def test_camel_dict_to_snake_dict():

    assert camel_dict_to_snake_dict({"FooBar": "foobar"}) == {"foo_bar": "foobar"}
    assert camel_dict_to_snake_dict({"FooBar": "foobar"}, True) == {"f_oo_bar": "foobar"}
    assert camel_dict_to_snake_dict({"FooBar": "foobar", "Bar": "bar"}) == {"foo_bar": "foobar", "bar": "bar"}
    assert camel_dict_to_snake_dict({"FooBar": {"FooBar": "foobar"}}) == {"foo_bar": { "foo_bar": "foobar" }}
    assert camel_dict_to_snake_dict({"FooBar": ["foobar"]}) == {"foo_bar": ["foobar"]}
