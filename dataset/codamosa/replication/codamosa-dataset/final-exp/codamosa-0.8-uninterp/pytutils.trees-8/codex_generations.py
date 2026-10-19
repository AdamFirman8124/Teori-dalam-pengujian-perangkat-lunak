

# Generated at 2022-06-14 06:46:17.232836
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test for `get_tree_node`
    """
    mapping = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    # Test with empty key
    try:
        get_tree_node(mapping, '')
    except KeyError:
        pass

    assert get_tree_node(mapping, 'a:b:c') == 'd'
    assert get_tree_node(mapping, 'a:b:c', parent=True) == {'c': 'd'}

    # Test with default
    assert get_tree_node(mapping, 'a:b:foo', default='bar') == 'bar'

    # Test with empty key and default

# Generated at 2022-06-14 06:46:27.291972
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'foo': 'bar',
        'list': ['food', 'bards'],
        'dict': {
            'foobar': 'baz'
        },
        'complex': {
            'list': [
                {
                    'foobar': 'baz'
                }
            ]
        }
    }

    # Test regular lookups
    assert get_tree_node(test_dict, 'foo') == 'bar'
    assert get_tree_node(test_dict, 'list:0') == 'food'
    assert get_tree_node(test_dict, 'dict:foobar') == 'baz'
    assert get_tree_node(test_dict, 'complex:list:0:foobar') == 'baz'

    # Test defaulting

# Generated at 2022-06-14 06:46:36.639933
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'one', 'one')
    assert mapping['one'] == 'one'

    set_tree_node(mapping, 'two:one', 'two_one')
    assert mapping['two']['one'] == 'two_one'

    set_tree_node(mapping, 'three:two:one', 'three_two_one')
    assert mapping['three']['two']['one'] == 'three_two_one'

    # Test replace
    set_tree_node(mapping, 'three:two:one', 'three_two_one_new')
    assert mapping['three']['two']['one'] == 'three_two_one_new'



# Generated at 2022-06-14 06:46:40.483881
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {"a": {"b": {"c": {'d': 'foo'}}}}
    assert get_tree_node(d, 'a:b:c:d') == 'foo'
    assert get_tree_node(d, 'a:b:c:foo', 'bar') == 'bar'
    assert get_tree_node(d, 'd') == _sentinel
    assert get_tree_node(d, 'a:b:c:d:x', 'bar') == 'bar'



# Generated at 2022-06-14 06:46:52.798442
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = dict(
        a=1,
        b=2,
        foo=dict(
            a=3,
            b=4,
        ),
        bar=dict(
            foo=5,
            baz=dict(
                yay=6,
            ),
        ),
    )

    assert get_tree_node(test_tree, 'a') == 1
    assert get_tree_node(test_tree, 'foo:a') == 3
    assert get_tree_node(test_tree, 'bar:foo') == 5
    assert get_tree_node(test_tree, 'bar:baz:yay') == 6

    try:
        assert get_tree_node(test_tree, 'bar:baz:yay:bar')
        assert False
    except KeyError:
        pass



# Generated at 2022-06-14 06:47:05.858594
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'root': {
            'a': {
                'b': {
                    'c': 5
                },
                'd': 6
            },
            'f': {
                'g': {
                    'h': {
                        'i': 'j'
                    }
                }
            }
        }
    }
    assert get_tree_node(data, 'root:a:b:c') == 5
    assert get_tree_node(data, 'root:a') == {'b': {'c': 5}, 'd': 6}
    assert get_tree_node(data, 'root:a:d') == 6
    assert get_tree_node(data, 'root:f:g:h:i') == 'j'

# Generated at 2022-06-14 06:47:17.040689
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree_obj, 'a:b') == tree_obj['a']['b']
    assert get_tree_node(tree_obj, 'a:b:c') == tree_obj['a']['b']['c']
    assert get_tree_node(tree_obj, 'a:b:c:d') == tree_obj['a']['b']['c']['d']
    assert get_tree_node(tree_obj, 'x') == tree_obj['x']
    assert get_tree_node(tree_obj, 'x:y') == tree_obj['x']['y']
    assert get_tree_node(tree_obj, 'x:y:z') == tree_obj['x']['y']['z']
    assert get_tree_node

# Generated at 2022-06-14 06:47:30.817693
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Function get_tree_node should return value at key if key exists.
    If key does not exist, raise KeyError.
    """
    test_mapping = {
        'foo': 'bar',
        'baz': {
            'quux': 'quuz',
        },
    }

    # Value of test_mapping['foo'] is 'bar', so we should get 'bar' back.
    result = get_tree_node(test_mapping, 'foo')
    assert result == 'bar'

    # Value of test_mapping['baz']['quux'] is 'quuz', so we should get 'quuz' back.
    result = get_tree_node(test_mapping, 'baz:quux')
    assert result == 'quuz'

    # Test that get_tree_node raises

# Generated at 2022-06-14 06:47:35.834644
# Unit test for function set_tree_node
def test_set_tree_node():
    test_data = {
        'foo': {
            'bar': 'baz'
        }
    }
    set_tree_node(test_data, 'foo:bar', 'somethingelse')
    assert test_data['foo']['bar'] == 'somethingelse'



# Generated at 2022-06-14 06:47:48.322700
# Unit test for function get_tree_node
def test_get_tree_node():
    # Simple tree
    tree = {
        'a': 1,
        'b': 2,
        'c': 3,
    }

    # Fetch value of node 'a'
    assert get_tree_node(tree, 'a') == 1

    # Fetch value of node 'b'
    assert get_tree_node(tree, 'b') == 2

    # Fetch value of node 'c'
    assert get_tree_node(tree, 'c') == 3

    # Fetch value of node 'b:a:c'
    tree = {
        'b': {
            'a': {
                'c': 5,
            },
        },
    }
    assert get_tree_node(tree, 'b:a:c') == 5

    # Fetch value of node 'a:b:c'
   

# Generated at 2022-06-14 06:48:04.461761
# Unit test for function get_tree_node
def test_get_tree_node():
    example_data = {
        'x': {
            'y': {
                'z': 42
            }
        },
        'a': {
            'b': {
                'c': 'foo'
            },
            'c': 'bar'
        }
    }
    for key, expected in [
        ('a:b:c', 'foo'),
        ('x:y:z', 42),
        ('a:c', 'bar'),
    ]:
        assert get_tree_node(example_data, key) == expected
    try:
        get_tree_node(example_data, 'n:o:p')
    except KeyError:
        pass
    else:
        assert False, 'Not found key did not raise KeyError'



# Generated at 2022-06-14 06:48:15.600661
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = collections.OrderedDict()
    set_tree_node(mapping, 'a', 'A')
    assert mapping == collections.OrderedDict([('a', 'A')])
    set_tree_node(mapping, 'b', 'B')
    assert mapping == collections.OrderedDict([('a', 'A'), ('b', 'B')])
    set_tree_node(mapping, 'b:c', 'C')
    assert mapping == collections.OrderedDict([('a', 'A'), ('b', collections.OrderedDict([('c', 'C')]))])
    set_tree_node(mapping, 'b:c:d', 'D')

# Generated at 2022-06-14 06:48:20.768302
# Unit test for function get_tree_node
def test_get_tree_node():
    root = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(root, 'a:b:c') == 'd'
    assert get_tree_node(root, 'a:b:e') == _sentinel



# Generated at 2022-06-14 06:48:24.401485
# Unit test for function set_tree_node
def test_set_tree_node():
    tree_data = {}
    set_tree_node(tree_data, 'data:hello', 'world')
    assert tree_data == {'data': {'hello': 'world'}}



# Generated at 2022-06-14 06:48:37.074041
# Unit test for function set_tree_node
def test_set_tree_node():
    nested_obj = {'a': {'b': {'c': 'test'}}}
    assert set_tree_node(nested_obj, 'a:b:c', '123') == {'a': {'b': {'c': '123'}}}
    assert set_tree_node(nested_obj, 'a:b', '123') == {'a': {'b': '123'}}
    assert set_tree_node(nested_obj, 'a', '123') == {'a': '123'}
    assert set_tree_node(nested_obj, 'a:b:c:d:e:f:g:h:i:j', '123') == {'a': {'b': {'c': '123'}}}

# Generated at 2022-06-14 06:48:42.849496
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit test for `set_tree_node()`"""
    mapping = tree()
    set_tree_node(mapping, 'who.hello', 'world')
    set_tree_node(mapping, 'who.longer.nested.dict', 'world')

    assert mapping['who']['hello'] == 'world', "Failed setting top-level key"
    assert mapping['who']['longer']['nested']['dict'] == 'world', "Failed setting arbitrary nested key"



# Generated at 2022-06-14 06:48:46.903767
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': 'c'}}
    assert get_tree_node(mapping, 'a:b') == 'c'
    assert get_tree_node(mapping, 'a:b:c') is _sentinel



# Generated at 2022-06-14 06:48:57.364409
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = {'one': {'two': {'three': 'four'}}}
    set_tree_node(test_mapping, 'one:two:three', 'four')
    assert test_mapping == {
        'one': {
            'two': {
                'three': 'four'
            }
        }
    }, 'First level setter'
    set_tree_node(test_mapping, 'one:two:three:four', 'five')
    assert test_mapping == {
        'one': {
            'two': {
                'three': {
                    'four': 'five'
                }
            }
        }
    }, 'Second level setter'
    set_tree_node(test_mapping, 'one:two:three:four:five', 'six')
    assert test_

# Generated at 2022-06-14 06:49:06.278740
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': {'c': {'d': 'e'}}}, 'f': 'g'}

    assert get_tree_node(d, 'f') == 'g'
    assert get_tree_node(d, 'a:b:c:d') == 'e'
    assert get_tree_node(d, 'a:b:c:d:z', None) is None
    assert get_tree_node(d, 'a:b:c:z', None) is None

# Generated at 2022-06-14 06:49:14.591604
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': 1,
            'c': {
                'x': 2
            },
            'd': [
                {
                    'h': 5,
                    'i': [6]
                }
            ]
        }
    }

    assert get_tree_node(tree, 'a:b') == 1
    assert get_tree_node(tree, 'a:c:x') == 2
    assert get_tree_node(tree, 'a:d:0:h') == 5
    assert get_tree_node(tree, 'a:d:0:i:0') == 6



# Generated at 2022-06-14 06:49:29.025441
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test function get_tree_node with dict, list and tuple
    """
    test_dict = {"a":{"b":{"c":{"d":{"e":{"f":"g"}}}}}}
    test_list = [1,2,3,4,5,6,[7,8,9,10]]
    test_tuple = (1,2,3,4,5,6,(7,8,9,10))
    print(get_tree_node(test_list, "5"))
    print(get_tree_node(test_tuple, "5"))
    print(get_tree_node(test_dict, "a:b:c:d:e:f"))
    print(get_tree_node(test_list, "6:0"))

# Generated at 2022-06-14 06:49:38.397366
# Unit test for function get_tree_node
def test_get_tree_node():
    config = {
        'foo': {
            'bar': [1, 2, 3],
            'baz': {
                'qux': [4, 5, 6]
            }
        }
    }
    assert get_tree_node(config, 'foo:bar') == [1, 2, 3]
    assert get_tree_node(config, 'foo:baz:qux') == [4, 5, 6]
    assert get_tree_node(config, 'foo:baz') == {'qux': [4, 5, 6]}



# Generated at 2022-06-14 06:49:44.552239
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 'FooBaz'
            }
        }
    }
    assert get_tree_node(tree, 'foo') == {'bar': {'baz': 'FooBaz'}}
    assert get_tree_node(tree, 'foo:bar') == {'baz': 'FooBaz'}
    assert get_tree_node(tree, 'foo:bar:baz') == 'FooBaz'

    tree = {
        'foo': [
            {'bar': [{'baz': 'FooBarBaz'}]}
        ]
    }
    # TODO Unlist my shit
    assert get_tree_node(tree, 'foo:bar:baz') == 'FooBarBaz'

   

# Generated at 2022-06-14 06:49:48.242379
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree()
    tree['a:b:c:d'] = 3

    assert 1 == get_tree_node(tree, 'a:b:c', parent=True)[':d']



# Generated at 2022-06-14 06:50:00.849755
# Unit test for function get_tree_node
def test_get_tree_node():
    '''Test `get_tree_node` function'''
    tree = {
        'a': {
            'b': {
                'c': 'foo',
            }
        },
        'bar': 'baz',
    }

    # Test standard traversal
    assert 'foo' == get_tree_node(tree, 'a:b:c')

    # Test traversal with default
    assert 'boo' == get_tree_node(tree, 'a:b:c:d', default='boo')

    # Test root level lookup
    assert 'baz' == get_tree_node(tree, 'bar')

    # Test retrieval of parent node
    assert tree['a']['b'] == get_tree_node(tree, 'a:b:c', parent=True)

    # Test KeyError without default
   

# Generated at 2022-06-14 06:50:06.427199
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test for function set_tree_node

    """
    tree = {}

    set_tree_node(tree, 'foo:bar:baz', 'test')

    assert get_tree_node(tree, 'foo') == {'bar': {'baz': 'test'}}



# Generated at 2022-06-14 06:50:16.008043
# Unit test for function get_tree_node
def test_get_tree_node():

    # Setup
    test_dict = {
        'one': {
            'foo': 'bar',
            'baz': 'boo',
        },
        'two': {
            'foo': 'bar',
            'baz': 'boo',
        },
    }

    # Test 1
    try:
        get_tree_node(test_dict, 'one:fuz')
        raise Exception('Test 1 failed, should have raised KeyError')
    except KeyError:
        pass

    # Test 2
    result = get_tree_node(test_dict, 'one:foo:')
    if result != 'bar':
        raise Exception('Test 2 failed.')

    # Test 3
    result = get_tree_node(test_dict, 'one:fuz', default='test')

# Generated at 2022-06-14 06:50:23.046058
# Unit test for function get_tree_node
def test_get_tree_node():
    node = tree()
    node['a']['b']['c'] = 'leaf'
    assert get_tree_node(node, 'a:b:c') == 'leaf'
    assert get_tree_node(node, 'a:b')['c'] == 'leaf'
    assert get_tree_node(node, 'a:b:d', default=None) is None



# Generated at 2022-06-14 06:50:27.521837
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Verify set_tree_node works as expected.
    """
    dataset = tree()
    set_tree_node(dataset, 'hello:world', 'yes')
    assert dataset['hello']['world'] == 'yes'



# Generated at 2022-06-14 06:50:31.069679
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': 1}}
    assert get_tree_node(d, 'a:b') == 1
    assert get_tree_node(d, 'a:c') is _sentinel



# Generated at 2022-06-14 06:50:52.225611
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'node_1': 'leaf_1',
        'node_2': {
            'node_2_1': {
                'node_2_1_1': 'leaf_2_1_1',
                'node_2_1_2': {
                    'node_2_1_2_1': 'leaf_2_1_2_1',
                }
            },
            'node_2_2': 'leaf2_2',
        },
        'node_3': 'leaf3'
    }

    # Test correct paths

# Generated at 2022-06-14 06:51:06.406544
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test error
    with pytest.raises(KeyError):
        get_tree_node({'a': 1}, 'b')
    with pytest.raises(KeyError):
        get_tree_node({'a': 1}, 'a:b')

    # Test Data
    assert get_tree_node({'a': 1}, 'a') == 1
    assert get_tree_node({'a': 1}, 'a:b') == {'b': 1}
    assert get_tree_node({'a': {'b': 1}}, 'a') == {'b': 1}
    assert get_tree_node({'a': {'b': 1}}, 'a:b') == 1

# Generated at 2022-06-14 06:51:16.026914
# Unit test for function get_tree_node
def test_get_tree_node():
    from nose.tools import assert_raises, assert_equal

    d = {'hello': {'world': '!'}}

    assert_equal(get_tree_node(d, 'hello:world'), '!')
    assert_raises(KeyError, get_tree_node, d, 'there:world')
    assert_equal(
        get_tree_node(d, 'there:world', default='?'),
        '?'
    )

    # Test parent
    assert_equal(
        get_tree_node(d, 'hello:world', parent=True),
        {'world': '!'}
    )



# Generated at 2022-06-14 06:51:19.167668
# Unit test for function set_tree_node
def test_set_tree_node():
    data = {}
    assert set_tree_node(data, 'rhea.ops.add', 'foo') == {'rhea': {'ops': {'add': 'foo'}}}
    assert data == {'rhea': {'ops': {'add': 'foo'}}}



# Generated at 2022-06-14 06:51:28.843692
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': {'baz': 'qux'}}}, 'foo:bar:baz') == 'qux'
    assert get_tree_node({'foo': {'bar': {'baz': 'qux'}}}, 'foo:bar:baz', default=None) == 'qux'
    assert get_tree_node({'foo': {'bar': {'baz': 'qux'}}}, 'foo:bar:not-baz') is _sentinel
    assert get_tree_node({'foo': {'bar': {'baz': 'qux'}}}, 'foo:bar:not-baz', default=None) is None

# Generated at 2022-06-14 06:51:41.100216
# Unit test for function get_tree_node
def test_get_tree_node():
    from pprint import pprint
    data = {
        'key1': {
            'key2': {
                'key4': 'value4',
            },
            'key3': 'value3',
        },
    }

    pprint(data)
    print('key1:key2:key4:', get_tree_node(data, 'key1:key2:key4:', default='default'))
    print('key1:key3:', get_tree_node(data, 'key1:key3:', default='default'))
    print('key1:key5:', get_tree_node(data, 'key1:key5:', default='default'))

# Generated at 2022-06-14 06:51:53.377531
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> _test_get_tree_node()
    """
    mapping = {
        'one': {
            'two': 'three'
        }
    }
    assert get_tree_node(mapping, 'one:two') == 'three'
    assert get_tree_node(mapping, 'one:two', default=None) == 'three'
    assert get_tree_node(mapping, 'one:two', default=None, parent=True) == {'two': 'three'}

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'one:bar')

    assert get_tree_node(mapping, 'one:bar', default='default') == 'default'



# Generated at 2022-06-14 06:51:57.559358
# Unit test for function set_tree_node
def test_set_tree_node():
    result = tree()
    set_tree_node(result, 'foo:bar:baz', 123)
    assert result['foo']['bar']['baz'] == 123



# Generated at 2022-06-14 06:52:02.902680
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    key = 'some:key'
    value = 'value'
    parent_node = set_tree_node(mapping, key, value)
    assert mapping['some']['key'] == value
    assert parent_node['key'] == value



# Generated at 2022-06-14 06:52:13.467989
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'users': {
            'john': {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'johndoe@example.com',
            },
            'jane': {
                'first_name': 'Jane',
                'last_name': 'Doe',
                'email': 'janedoe@example.com',
            },
        }
    }
    assert get_tree_node(test_tree, 'users', _sentinel) is not _sentinel



# Generated at 2022-06-14 06:52:33.569323
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        "key": "value",
        "key2": {
            "key3": "value3"
        }
    }

    assert get_tree_node(test_tree, 'key') == 'value'
    assert get_tree_node(test_tree, 'key2:key3') == 'value3'
    assert get_tree_node(test_tree, 'key3', 'defaultvalue') == 'defaultvalue'

    # Test parent
    assert get_tree_node(test_tree, 'key2:key3', parent=True) == {'key3': 'value3'}



# Generated at 2022-06-14 06:52:46.689417
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for function get_tree_node
    """

    # Unit test for function get_tree_node: Normal use
    dict_obj = {'a': {'b': 'b_value'}}
    check_value = get_tree_node(dict_obj, 'a:b')
    assert check_value == 'b_value'

    # Unit test for function get_tree_node: Return default when key not found
    dict_obj = {'a': {'b': 'b_value'}}
    check_value = get_tree_node(dict_obj, 'a:c', get_tree_node.DEFAULT)
    assert check_value is get_tree_node.DEFAULT

    # Unit test for function get_tree_node: Return parent when key not found

# Generated at 2022-06-14 06:52:53.947433
# Unit test for function set_tree_node
def test_set_tree_node():
    """Tests the set_tree_node function."""
    test_dict = {}
    set_tree_node(test_dict, 'hello:world:now:here:now:here:now:here', 'Hello')
    assert test_dict['hello']['world']['now']['here']['now']['here']['now']['here'] == 'Hello'



# Generated at 2022-06-14 06:52:59.363323
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = tree()
    test_tree2 = tree()

    set_tree_node(test_tree, u'one:two:three', u'3')
    set_tree_node(test_tree2, u'one:two:three', u'3')

    assert test_tree == test_tree2



# Generated at 2022-06-14 06:53:10.129163
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'foo': {
            'cats': ['meow', 'purr', 'yowl'],
            'dogs': ['bark', 'whine', 'woof'],
            'birds': ['chirp', 'caw', 'tweet'],
        },
        'bar': {
            'bugs': ['roaches', 'beetles', 'dragonflies'],
            'fish': ['clownfish', 'shark', 'stingray'],
            'snakes': ['cobra', 'python', 'anaconda'],
        },
    }

    assert get_tree_node(test_data, 'foo:cats:2') == 'yowl'
    assert get_tree_node(test_data, 'foo:dogs') == ['bark', 'whine', 'woof']
   

# Generated at 2022-06-14 06:53:16.192080
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }
    assert get_tree_node(mapping, 'foo') == get_tree_node(mapping, 'foo:')
    assert get_tree_node(mapping, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:53:28.946285
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Ensure that get_tree_node returns values correctly.
    """
    mapping = tree()
    mapping['d1:d2:d3:d4'] = 'final'
    assert get_tree_node(mapping, 'd1:d2:d3:d4') == 'final'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'd1:d2:d3:d4:d5')

    assert get_tree_node(mapping, 'd1:d2:d3:d4:d5', default='failsafe') == 'failsafe'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'd1:d2:d3:d4:d5', parent=True)
    assert get

# Generated at 2022-06-14 06:53:38.090145
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    mapping = {
        'one': {
            'two': {
                'three': 3,
            }
        },
        'four': 4
    }
    assert get_tree_node(mapping, 'one:two:three', default=1) == 3
    assert get_tree_node(mapping, 'four', default=1) == 4
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'five')

    assert get_tree_node(mapping, 'four:five:six', default=1) == 1



# Generated at 2022-06-14 06:53:50.618321
# Unit test for function set_tree_node
def test_set_tree_node():
    # Test with empty tree
    tree = {}
    assert set_tree_node(tree, 'a:b:c', 'test') == {'a': {'b': {'c': 'test'}}}

    # Test with filled tree
    tree = {'a': {'x': {'y': {'z': 'nu'}}}}
    assert set_tree_node(tree, 'a:b:c', 'test') == {'a': {'b': {'c': 'test'}, 'x': {'y': {'z': 'nu'}}}}

    # Test with filled tree and existing parent node
    tree = {'a': {'b': {'d': 'test'}, 'x': {'y': {'z': 'nu'}}}}

# Generated at 2022-06-14 06:53:57.805792
# Unit test for function get_tree_node
def test_get_tree_node():
    config = {'a': {'b': {'c': 3}}}
    # This is the case where we expect the node to be found
    assert get_tree_node(config, 'a:b:c') == 3
    # This is the case where we expect to throw a KeyError
    with pytest.raises(KeyError):
        get_tree_node(config, 'a:b:d')
    # This is the case where we expect the default value to be used
    assert get_tree_node(config, 'a:b:d', default='default') == 'default'



# Generated at 2022-06-14 06:54:42.109639
# Unit test for function get_tree_node
def test_get_tree_node():
    assert(get_tree_node({'foo': {}}, 'foo') == {})
    assert(get_tree_node({'foo': {'bar': {}}}, 'foo:bar') == {})
    assert(get_tree_node({'foo': {'bar': {}}}, 'foo:bar:baz', default=1) == 1)
    assert(get_tree_node({'foo': {'bar': {}}}, 'foo:baz:bar') is None)
    assert(get_tree_node({'foo': {'bar': {}}}, 'foo:baz:bar', default=1) == 1)
    assert(get_tree_node({'foo': {'bar': {}}}, 'foo:baz:bar', parent=True) == {})

# Generated at 2022-06-14 06:54:50.178140
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for get_tree_node function."""
    assert get_tree_node({'test': True}, 'test')
    assert get_tree_node({'test': {'test2': True}}, 'test:test2')
    assert get_tree_node({'test': {'test2': True}}, 'test:test2', default='foo') == 'foo'
    assert get_tree_node(Tree({'test': True}), 'test')



# Generated at 2022-06-14 06:54:54.107276
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'foo:bar:baz', 'test')
    assert mapping['foo']['bar']['baz'] == 'test'
    print('done!')



# Generated at 2022-06-14 06:55:00.881414
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 'huehue'
            },
            'asd': {
                'fgh': 'huehue'
            },
        }
    }

    assert get_tree_node(tree, 'foo:bar:baz') == 'huehue'

    assert get_tree_node(tree, 'foo:bar:baz') == 'huehue'
    with pytest.raises(KeyError):
        assert get_tree_node(tree, 'foo:non:existent:baz')

    assert get_tree_node(tree, 'foo:bar:baz', None) is None  # Don't yell
    assert get_tree_node(tree, 'foo:bar:baz', None) == get_tree_node

# Generated at 2022-06-14 06:55:14.447125
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    from types import MappingProxyType
    with pytest.raises(KeyError):
        foo = get_tree_node({'a': {'b': {'c': 'd'}}}, 'doesnt:exist')
    foo = get_tree_node({'a': {'b': {'c': 'd'}}}, 'doesnt:exist', default='default')
    assert foo == 'default'
    foo = get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c')
    assert foo == 'd'
    foo = get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c', parent=True)
    assert foo is {'c': 'd'}

# Generated at 2022-06-14 06:55:24.775286
# Unit test for function get_tree_node
def test_get_tree_node():
    from copy import deepcopy
    mapping = {
        'a': {
            'b': {
                'c': 1
            }
        }
    }
    assert get_tree_node(mapping, 'a') == {'b': {'c': 1}}
    assert get_tree_node(mapping, 'a:b') == {'c': 1}
    assert get_tree_node(mapping, 'a:b:c') == 1
    assert get_tree_node(mapping, 'a:b:e', default=None) is None
    assert get_tree_node(mapping, 'a:b:e', default=_sentinel) is _sentinel



# Generated at 2022-06-14 06:55:33.759122
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'key1': 'value1',
        'key2': {
            'key2_1': 'value2_1',
            'key2_2': 'value2_2'
        }
    }

    assert get_tree_node(tree, 'key2:key2_1') == 'value2_1'
    assert get_tree_node(tree, 'key2:key2_2') == 'value2_2'
    assert get_tree_node(tree, 'key1') == 'value1'

# Generated at 2022-06-14 06:55:44.009084
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for function `get_tree_node` .

    References:
        http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

    """
    mapping = {
        'foo': {
            'bar': [{
                'baz': ['qux']
            }]
        }
    }
    assert get_tree_node(mapping, 'foo:bar:0:baz:0') == 'qux'
    assert get_tree_node(mapping, 'foo:bar:0:baz:0:boo', 'boo') == 'boo'
    assert get_tree_node(mapping, 'foo:bar:0:baz:0', 'boo') == 'qux'

# Generated at 2022-06-14 06:55:53.703154
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'foo': {
            'bar': {
                'baz': {
                    'bing': 1,
                },
            },
        },
    }

    assert get_tree_node(d, 'foo:bar') == d['foo']['bar']
    assert get_tree_node(d, 'buzz', default=None) is None
    assert get_tree_node(d, 'foo:bar:bing') == 1
    assert get_tree_node(d, 'foo:bar::bing') == 1

# Generated at 2022-06-14 06:55:57.963369
# Unit test for function set_tree_node
def test_set_tree_node():
    x = set_tree_node({}, 'x:y:z', 42)
    assert x == {'x': {'y': {'z': 42}}}

