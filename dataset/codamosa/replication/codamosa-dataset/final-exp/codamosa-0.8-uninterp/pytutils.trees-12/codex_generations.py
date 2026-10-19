

# Generated at 2022-06-14 06:46:19.637016
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c') == 1
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c', parent=True) == {'c': 1}
    assert get_tree_node({'a': {'b': {'a': 1}}}, 'a:b:c') is None
    try:
        get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c', default=_sentinel)
    except Exception as exc:
        assert type(exc) == KeyError
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b:c', default=None) is None


#

# Generated at 2022-06-14 06:46:23.565572
# Unit test for function set_tree_node
def test_set_tree_node():
    structure = tree()
    set_tree_node(structure, 'a:b:c', 'd')
    assert structure['a']['b']['c'] == 'd'



# Generated at 2022-06-14 06:46:34.772966
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test tree-like mapping
    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': 'This is a test.'
                }
            }
        }
    }

    # Test nested retrieval
    assert get_tree_node(mapping, 'a:b:c:d') == 'This is a test.'

    # Test that we can retrieve parent nodes as well
    assert get_tree_node(mapping, 'a:b:c:d', parent=True) == {'d': 'This is a test.'}
    assert get_tree_node(mapping, 'a:b:c:d', default='Nope.', parent=True) == {'d': 'This is a test.'}

# Generated at 2022-06-14 06:46:47.304238
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function `get_tree_node`"""
    mapping = tree()
    mapping[':country:region:city'][':name'] = 'Leipzig'
    mapping[':country:region:city'][':postcode'] = '04109'
    mapping[':country'][':population'] = '1Mio'
    mapping[':country'][':region'][':name'] = 'Sachsen'
    mapping[':country'][':region'][':capital'] = 'Dresden'

    assert get_tree_node(mapping, 'country:region:city:name') == 'Leipzig'
    assert get_tree_node(mapping, 'country:region:city:postcode') == '04109'
    assert get_tree_node(mapping, 'country:population') == '1Mio'


# Generated at 2022-06-14 06:46:56.297903
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {'a': {'b': {'c': 'd'}}}

    assert get_tree_node(t, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(t, 'a:b') == {'c': 'd'}

    with pytest.raises(KeyError):
        get_tree_node(t, 'a:b:d')

    assert get_tree_node(t, 'a:b:d', default='wot') == 'wot'

    assert get_tree_node(t, 'a:b:c', parent=True) == {'c': 'd'}

# Generated at 2022-06-14 06:46:59.006727
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'namespace:test', 'test')
    assert mapping == {
        'namespace': {
            'test': 'test'
        }
    }



# Generated at 2022-06-14 06:47:11.145933
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'a': {
                'a': True
            }
        },
        'b': {
            'a': True
        },
        'c': {
            'a': {
                'b': True
            }
        }
    }

    assert get_tree_node(tree, 'a:a:a') is True

    # Test missing key
    with pytest.raises(KeyError):
        get_tree_node(tree, 'c:a:b:a:a:a')

    # Test with default
    assert get_tree_node(tree, 'c:a:b:a:a:a', default=False) is False



# Generated at 2022-06-14 06:47:16.575247
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'Foo': {'Bar': 'Baz'}}, 'Foo:Bar') == 'Baz'
    assert not get_tree_node({'Foo': {'Bar': 'Baz'}}, 'Foo:Bar:Baz', default=False)



# Generated at 2022-06-14 06:47:24.717421
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node"""
    tree = {
        'one': {
            'two': {
                'three': {}
            }
        }
    }
    assert get_tree_node(tree, 'one:two:three') is tree['one']['two']['three']
    assert get_tree_node(tree, 'three:two:one') is None



# Generated at 2022-06-14 06:47:34.956555
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test case for set_tree_node."""
    obj = {"foo": "bar"}
    set_tree_node(obj, "foo:bar:baz", "foobarbaz")
    set_tree_node(obj, "bar:baz:foobar", "foobarbaz2")
    assert obj['foo']['bar']['baz'] == "foobarbaz"

    # This should raise an exception as there is no key "foo"
    set_tree_node(obj, "foo:bar:baz", "foobarbaz")



# Generated at 2022-06-14 06:47:50.141424
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = tree()
    assert tree == collections.defaultdict(tree)
    assert tree is not None
    # `tree` behaves exactly like a dict would.
    # We can set attributes on it using the familiar dict syntax.
    tree['test'] = 'test'
    # Does not raise
    assert tree['test'] == 'test'

    # Let's try to set something on a deeper level, similar to 1.2.3.
    tree['foo']['bar']['foobar'] = 'test'
    # Does not raise
    assert tree['foo']['bar']['foobar'] == 'test'
    # Let's try to set the same thing with our new set_tree_node helper.
    set_tree_node(tree, 'foo:bar:foobar', 'test')
    # Does not raise

# Generated at 2022-06-14 06:48:03.536863
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree(), 'a') == {}
    assert get_tree_node(tree(), 'a:b') == {}
    assert get_tree_node(tree(), 'a:b:c') == {}
    assert get_tree_node(tree(), 'a:b:c:d') == {}
    assert get_tree_node(tree(), 'a:b:c:d', parent=True) == {}

    data = tree()
    data['a']['b']['c'] = 'd'

    assert get_tree_node(data, 'a') == {}
    assert get_tree_node(data, 'a:b') == {}
    assert get_tree_node(data, 'a:b:c') == 'd'

# Generated at 2022-06-14 06:48:07.309215
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        },
    }

    assert get_tree_node(mapping, 'foo:bar') == 'baz'

# Generated at 2022-06-14 06:48:15.355865
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests for the `get_tree_node` function.

    Returns:
        bool: True if tests pass, raise exception if tests fail

    """

    root = {'a': {'b': {'c': {'d': 123}}}}

    assert get_tree_node(root, 'a:b:c:d') == 123
    assert get_tree_node(root, 'x', default=None) is None



# Generated at 2022-06-14 06:48:23.968416
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test set_tree_node."""
    # Set up two trees for comparing
    base_tree = tree()
    test_tree = tree()
    paths = ['test:test1:1', 'test:test1:2', 'test1:test2:test3', 'test:test1:3']
    for path in paths:
        set_tree_node(base_tree, path, 'value')
        test_tree[path] = 'value'

    # Compare
    assert base_tree == test_tree

# Generated at 2022-06-14 06:48:33.108149
# Unit test for function set_tree_node
def test_set_tree_node():
    for test in (('a:b:c', 'foo'), ('a:b:c:d:e', 'bar')):
        mapping = {'a': {'b': {'c': 'foo'}}}
        set_tree_node(mapping, test[0], test[1])
        assert test[1] == mapping[test[0].split(':')[0]][test[0].split(':')[1]][test[0].split(':')[2]]



# Generated at 2022-06-14 06:48:38.415217
# Unit test for function get_tree_node
def test_get_tree_node():
    node = {
        'foo': {
            'bar': 'baz'
        }
    }
    result = get_tree_node(node, 'foo:bar')
    assert result == 'baz', "get_tree_node could not extract value 'baz' from node dict"



# Generated at 2022-06-14 06:48:43.118146
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:48:49.454830
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': ['f', 'g']
                    }
                }
            }
        }
    }

    assert get_tree_node(test_mapping, 'a:b:c:d:e:0') == 'f'



# Generated at 2022-06-14 06:48:58.294557
# Unit test for function set_tree_node
def test_set_tree_node():
    assert ({'a': {'b': {'c': 3}}} == set_tree_node({}, 'a:b:c', 3))
    assert ({'a': {'b': {'c': 3}}} == set_tree_node({'a': {}}, 'a:b:c', 3))
    assert ({'a': {'b': {'c': 3}}} == set_tree_node({'a': {'b': {}}}, 'a:b:c', 3))
    # TODO This should be different behavior.
    assert ({'a': {'b': {'c': 4}}} == set_tree_node({'a': {'b': {'c': 3}}}, 'a:b:c', 4))

# Generated at 2022-06-14 06:49:15.834730
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:49:28.381653
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test ``get_tree_node``

    .. note::
        This code must be moved to a test suite in test_utils!
    """
    # Set up tree
    tree_node = {}
    tree_node['a'] = {}
    tree_node['a']['b'] = {}
    tree_node['a']['b']['c'] = 'd'

    # Try to fetch something that exists
    assert get_tree_node(tree_node, 'a:b:c') == 'd'
    assert get_tree_node(tree_node, 'a:b') == {'c': 'd'}
    assert get_tree_node(tree_node, 'a') == {'b': {'c': 'd'}}

    # Try to fetch a thing that doesn't exist
    assert get_

# Generated at 2022-06-14 06:49:38.578350
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test for get_tree_node."""
    assert get_tree_node(tree(), 'foo') == {}
    assert get_tree_node(tree(), 'foo:bar') == {}
    assert get_tree_node(
        tree(), 'foo:baz', default='default') == 'default'
    assert get_tree_node(tree(), 'foo:baz') == {}
    assert get_tree_node(
        tree(), 'foo:baz:bar', default='default') == 'default'
    assert get_tree_node(tree(), 'foo:baz:bar') == {}



# Generated at 2022-06-14 06:49:41.484572
# Unit test for function set_tree_node
def test_set_tree_node():
    data = dict()
    set_tree_node(data, 'foo:bar:baz', 'value')
    assert data['foo']['bar']['baz'] == 'value'
    set_tree_node(data, 'foo:bar', 'value')
    assert data['foo'] == 'value'



# Generated at 2022-06-14 06:49:52.149992
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    >>> d = {}
    >>> set_tree_node(d, 'a:b', 'c')
    {'a': {'b': 'c'}}
    >>> set_tree_node(d, 'a:b', 'd')
    {'a': {'b': 'd'}}
    >>> set_tree_node(d, 'a:c', 'd')
    {'a': {'b': 'd', 'c': 'd'}}
    >>> set_tree_node(d, 'b', 'd')
    {'a': {'b': 'd', 'c': 'd'}, 'b': 'd'}
    """



# Generated at 2022-06-14 06:50:02.759277
# Unit test for function get_tree_node
def test_get_tree_node():
    # Given a tree of dictionaries like this:
    tree = {
        'foo': {
            'bar': {
                'baz': 'quux'
            }
        }
    }

    # It should be possible to traverse it like this:
    assert get_tree_node(tree, 'foo:bar:baz') == 'quux'

    # Default values should be supported:
    assert get_tree_node(tree, 'foo:bar:bop', default='beep') == 'beep'
    assert get_tree_node(tree, 'foo:bar:bop', default='beep') == 'beep'

    # Default values should not be supported:
    try:
        get_tree_node(tree, 'foo:bar:bop')
        assert False
    except KeyError:
        pass

    #

# Generated at 2022-06-14 06:50:10.182148
# Unit test for function set_tree_node
def test_set_tree_node():
    test_key = 'value:to:lookup'
    test_value = 'value'
    test_dict = {'value': {'to': 'lookup'}}
    test_dict_update = {'value': {'to': 'lookup'}}
    test_dict_update[test_key] = test_value
    assert set_tree_node(test_dict, test_key, test_value) == test_dict_update



# Generated at 2022-06-14 06:50:19.746769
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': {
                'baz': 'woo',
            },
            'bla': 'foo',
        },
        'fee': 'baa',
    }

    assert get_tree_node(mapping, 'foo:bar:baz') == 'woo'
    assert get_tree_node(mapping, 'foo:bla') == 'foo'
    assert get_tree_node(mapping, 'fee') == 'baa'

    # Test default
    assert get_tree_node(mapping, 'bla', default='woo') == 'woo'

    # Test raise
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'bla')

    # Test parent

# Generated at 2022-06-14 06:50:24.428301
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'foo': 'bar',
        'lol': {
            'rofl': 'copter'
        }
    }

    assert get_tree_node(test_data, 'lol:rofl') == 'copter'


# Generated at 2022-06-14 06:50:34.484598
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest

    mapping1 = {'node1': {'child1': 1, 'child2': 2},
                'node2': 2}

    mapping2 = {'node1': {'child1': 1, 'child2': 2},
                'node3': 2}

    def test_lookup_key_node1(mapping):
        assert get_tree_node(mapping, 'node1') == {'child1': 1, 'child2': 2}

    def test_lookup_key_node2(mapping):
        assert get_tree_node(mapping, 'node2') == 2

    def test_lookup_key_node1_child1(mapping):
        assert get_tree_node(mapping, 'node1:child1') == 1


# Generated at 2022-06-14 06:50:52.031376
# Unit test for function get_tree_node
def test_get_tree_node():
    # setup
    mapping = {
        'one': 1,
        'another': {
            'level': {
                'two': 2
            },
            'level2': {
                'more': 3
            }
        }
    }

    # tests
    assert get_tree_node(mapping, 'one') == 1
    assert get_tree_node(mapping, 'another:level:two') == 2

    try:
        assert get_tree_node(mapping, 'three')
    except KeyError:
        assert True
    else:
        assert False

    assert get_tree_node(mapping, 'three', default=False) is False



# Generated at 2022-06-14 06:51:06.223133
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_flat = {'foo': 1, 'bar:baz': 2, 'bar:qux': 3}
    tree_deep = {'foo': 1, 'bar': {'baz': 2, 'qux': 3}}

    assert get_tree_node(tree_deep, 'foo') == 1
    assert get_tree_node(tree_deep, 'bar:baz') == 2
    assert get_tree_node(tree_deep, 'bar:qux') == 3
    assert get_tree_node(tree_flat, 'foo') == 1
    assert get_tree_node(tree_flat, 'bar:baz') == 2
    assert get_tree_node(tree_flat, 'bar:qux') == 3
    assert get_tree_node(tree_deep, 'bar:baz:bar:baz')

# Generated at 2022-06-14 06:51:17.367935
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'foo:bar', 'baz')
    assert d[u'foo'][u'bar'] == u'baz'

    d = {}
    set_tree_node(d, 'foo:bar:baz', 'baz')
    assert d[u'foo'][u'bar'][u'baz'] == u'baz'

    d = {}
    set_tree_node(d, 'foo:bar:1:baz', 'baz')
    assert d[u'foo'][u'bar'][u'1'][u'baz'] == u'baz'

    d = {}
    set_tree_node(d, 'foo:bar:', 'baz')

# Generated at 2022-06-14 06:51:27.950389
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node"""
    assert get_tree_node({'foo': {'bar': {'baz': 'bif'}}}, 'foo:bar:baz') == 'bif'
    assert get_tree_node({'foo': {'bar': {'baz': 'bif'}}}, 'foo:bar') == {'baz': 'bif'}
    assert get_tree_node({'foo': {'bar': {'baz': 'bif'}}}, 'foo:bar:baz', parent=True) == {'baz': 'bif'}
    assert get_tree_node({'foo': {'bar': {'baz': 'bif'}}}, 'foo:bar:baz', default='default') == 'bif'

# Generated at 2022-06-14 06:51:35.911167
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'foo': {
            'bar': 'baz',
            'foobar': {
                'bazbar': 'foobaz'
            }
        }
    }
    assert get_tree_node(test_mapping, 'foo:bar') == 'baz'
    assert get_tree_node(test_mapping, 'foo') is test_mapping['foo']
    assert get_tree_node(test_mapping, 'foo:foobar:bazbar') == 'foobaz'
    assert get_tree_node(test_mapping, 'foo:foobar:bazbar:foo') is None

# Generated at 2022-06-14 06:51:44.337906
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = tree()
    set_tree_node(test_mapping, 'foo:0', 'bar')
    assert test_mapping['foo'][0] == 'bar'

    set_tree_node(test_mapping, 'foo:1', 'baz')
    assert test_mapping['foo'][1] == 'baz'

    try:
        set_tree_node(test_mapping, 'foo:3:3:3:3:3:3:3', True)
    except TypeError:
        assert False



# Generated at 2022-06-14 06:51:49.782343
# Unit test for function set_tree_node
def test_set_tree_node():
    # Make a dict for us to play with
    mapping = {
        'a': {
            'x': 1
        }
    }

    # Show that the original mapping is intact

# Generated at 2022-06-14 06:51:59.334659
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Unit test for function set_tree_node
    """
    mapping = {
        'a': {
            'b': {'c': 'c'},
        },
    }
    set_tree_node(mapping, 'x:y:z', 'z')
    assert mapping is {
        'a': {
            'b': {'c': 'c'},
        },
        'x': {
            'y': {
                'z': 'z',
            }
        }
    }



# Generated at 2022-06-14 06:52:07.281036
# Unit test for function get_tree_node
def test_get_tree_node():
    test = {
        'this': {
            'is': {
                'a': {
                    'test': 'leet'
                }
            }
        }
    }

    assert get_tree_node(test, 'this:is:a:test') == 'leet'
    assert get_tree_node(test, 'this:is:a', default=None) == {
        'test': 'leet'
    }



# Generated at 2022-06-14 06:52:12.747620
# Unit test for function set_tree_node
def test_set_tree_node():
    dictionary = {'a': 'b', 'c': {'d': 'e'}}
    set_tree_node(dictionary, 'c:d:f', 'g')
    assert dictionary == {'a': 'b', 'c': {'d': {'f': 'g'}}}



# Generated at 2022-06-14 06:52:38.128896
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for `get_tree_node`."""
    test_map = {
        'foo': {
            'bar': 'baz',
            'spam': {
                'eggs': 'spam',
            },
        },
    }

    assert get_tree_node(test_map, 'foo:bar') == 'baz'
    assert get_tree_node(test_map, 'foo:spam:eggs') == 'spam'
    assert get_tree_node(test_map, 'nonexistent:key', default='something else') == 'something else'
    assert get_tree_node(test_map, 'nonexistent:key') == _sentinel



# Generated at 2022-06-14 06:52:41.273244
# Unit test for function get_tree_node
def test_get_tree_node():
    a = {'1': {'2': {'3': 'abc'}}}
    assert get_tree_node(a, '1:2:3') == 'abc'



# Generated at 2022-06-14 06:52:45.097165
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'root:sub1:subsub1', 1)
    assert tree == {'root': {'sub1': {'subsub1': 1}}}



# Generated at 2022-06-14 06:52:49.215244
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'key1': [{'key2': 1}],
        'key3': {'key4': 2}
    }
    assert get_tree_node(test_dict, 'key1:0:key2') == 1
    assert get_tree_node(test_dict, 'key3:key4') == 2

# Generated at 2022-06-14 06:53:01.068368
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit tests for function `get_tree_node`."""
    # Given a properly nested dict
    a = {
        'a': {
            'b': {
                'c': 'd'
            },
            'c': 'd'
        },
        'b': {
            'c': 'd'
        }
    }
    # When fetching a value
    assert get_tree_node(a, 'a:b:c') == 'd'
    assert get_tree_node(a, 'a:b:c:d', default='e') == 'e'
    # Then an exception should be raised
    # todo get_tree_node(a, 'a:b:c:d')  # Uncomment to test for KeyError



# Generated at 2022-06-14 06:53:10.283482
# Unit test for function get_tree_node
def test_get_tree_node():
    # Define test data structure
    test_data = {
        'foo': {
            'bar': 'baz',
            'baz': {
                'bar': 'baz',
            },
        },
    }

    assert 'baz' == get_tree_node(test_data, 'foo:bar')
    assert 'baz' == get_tree_node(test_data, 'foo:baz:bar')
    assert 'baz' == get_tree_node(test_data, 'foo:baz:bar', parent=True)
    assert test_data['foo'] == get_tree_node(test_data, 'foo:baz:bar', parent=True, default=None)

# Generated at 2022-06-14 06:53:14.432730
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    assert set_tree_node(mapping, 'MyMapping:is:awesome', True)
    assert mapping['MyMapping']['is']['awesome']



# Generated at 2022-06-14 06:53:20.126549
# Unit test for function set_tree_node
def test_set_tree_node():
    try:
        set_tree_node({}, 'hello', 'world')
    except NameError:
        assert False, 'Expected set_tree_node() to not raise NameError when trying to update tree_node'

    assert {'world'} == set_tree_node({}, 'hello', 'world')
    assert {'world'} == set_tree_node({}, 'hello:world', 'world')



# Generated at 2022-06-14 06:53:33.442677
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'a': {
            'b': {
                'c': 'd',
                'f': 'g',
            },
            'h': 'i',
        },
    }

    assert get_tree_node(test_dict, 'a') == {
        'b': {
            'c': 'd',
            'f': 'g',
        },
        'h': 'i',
    }

    assert get_tree_node(test_dict, 'a:b:c', default='foo') == 'd'
    assert get_tree_node(test_dict, 'a:b:z', default='foo') == 'foo'

    with pytest.raises(KeyError):
        get_tree_node(test_dict, 'a:z')



# Generated at 2022-06-14 06:53:37.650883
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({
        'a': {'b': {'c': 'eureka'}}
    }, 'a:b:c') == 'eureka'

    assert get_tree_node({
        'a': {'b': {'c': 'eureka'}}
    }, 'c:d:e', default='not found') == 'not found'



# Generated at 2022-06-14 06:54:19.440852
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        "level1": {
            'level2': {
                'level3': {
                    'value': True
                }
            }
        }
    }

    assert get_tree_node(test_tree, 'level1:level2:level3:value') is True
    assert get_tree_node(test_tree, 'level1:level2:level3:value1', default=True) is True
    with pytest.raises(KeyError):
        get_tree_node(test_tree, 'level1:level2:level3:value1')



# Generated at 2022-06-14 06:54:26.701891
# Unit test for function get_tree_node
def test_get_tree_node():
    test = {'one': {'two': {'three': 'four'}, 'five': 'six'}}
    assert get_tree_node(test, 'one:two:three') == 'four'
    assert get_tree_node(test, 'five') == 'six'
    assert get_tree_node(test, 'one:five') == 'six'
    assert get_tree_node(test, 'one:seven', default='eight') == 'eight'
    with pytest.raises(KeyError):
        get_tree_node(test, 'one:seven')



# Generated at 2022-06-14 06:54:38.243110
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 'd', 'e': 'f'}}}, 'a:b') == {'c': 'd', 'e': 'f'}
    assert get_tree_node({'a': {'b': {'c': 'd', 'e': 'f'}}}, 'a:b:c') == 'd'
    assert get_tree_node({'a': {'b': {'c': 'd', 'e': 'f'}}}, 'a:b:foo') == _sentinel
    assert get_tree_node({'a': {'b': {'c': 'd', 'e': 'f'}}}, 'a:b', default='bar') == {'c': 'd', 'e': 'f'}

# Generated at 2022-06-14 06:54:46.134161
# Unit test for function get_tree_node
def test_get_tree_node():
    mock_tree = {
        'root': {
            'branch_1': {
                'leaf_1': 'value_1',
                'leaf_2': 'value_2',
            },
            'branch_2': {
                'leaf_3': 'value_3',
                'leaf_4': 'value_4',
            },
        },
    }

    assert get_tree_node(mock_tree, 'root:branch_1:leaf_1', default=_sentinel) == 'value_1'
    assert get_tree_node(mock_tree, 'root:branch_2:leaf_dne', default=_sentinel) is _sentinel
    assert get_tree_node(mock_tree, 'root:branch_2:leaf_dne', default='DEFAULT_VALUE')

# Generated at 2022-06-14 06:54:57.737485
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> test_get_tree_node()
    True
    """
    import pprint
    my_dict = {'colors': {'red': 1, 'green': 2, 'blue': 3,
                          'subcolors': {'lightred': 4, 'lightgreen': 5, 'lightblue': 6
                                        }}}
    node = get_tree_node(my_dict, 'colors:subcolors:lightred')
    assert node == 4, 'Light red is not 4'
    node = get_tree_node(my_dict, 'colors:subcolors', default='No subcolors')
    pprint.pprint(node)
    assert node == {'lightblue': 6, 'lightgreen': 5, 'lightred': 4}, 'Subcolors are not correct'
    assert get_tree_

# Generated at 2022-06-14 06:55:09.876323
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 3
            }
        }
    }

    assert get_tree_node(mapping, 'a:b:c') == 3
    assert get_tree_node(mapping, 'a:b') == {'c': 3}
    assert get_tree_node(mapping, 'a') == {'b': {'c': 3}}

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:c:d')
        get_tree_node(mapping, 'd')

    assert get_tree_node(mapping, 'd', default=None) is None
    assert get_tree_node(mapping, 'a:b:c:d', default=None) is None



# Generated at 2022-06-14 06:55:20.090790
# Unit test for function get_tree_node
def test_get_tree_node():
    from collections import OrderedDict
    test_dict = OrderedDict([('a', 1), ('b', {'c': {'d': 4}})])
    assert get_tree_node(test_dict, 'a') == 1, "First dimension works"
    assert get_tree_node(test_dict, 'b:c:d') == 4, "Second dimension works"
    assert get_tree_node(test_dict, 'b:c:d:e') == None, "Nonexistent key returns None"
    assert get_tree_node(test_dict, 'b:c:d:e', default={}) == {}, "Nonexistent key returns default"
    assert get_tree_node(test_dict, 'b:c:d', parent=True) == {'d': 4}, "Parent node returns correct node"


# Generated at 2022-06-14 06:55:24.286495
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = tree()
    test_tree['hello:world']['foo'] = 'bar'

    assert get_tree_node(test_tree, 'hello:world:foo') == 'bar'



# Generated at 2022-06-14 06:55:32.727300
# Unit test for function get_tree_node
def test_get_tree_node():
    my_tree = {'a': {'b': {'c': 'bla'}}}

    assert get_tree_node(my_tree, 'a:b:c') == 'bla'
    assert get_tree_node(my_tree, 'a:b:c:d', default=42) == 42
    assert get_tree_node(my_tree, 'a:b:c:d') == 'bla'  # parent node
    assert get_tree_node(my_tree, 'a:b') == {'c': 'bla'}

    with pytest.raises(KeyError):
        get_tree_node(my_tree, 'a:b:c:d')  # noqa


if __name__ == '__main__':
    pytest.main()

# Generated at 2022-06-14 06:55:35.585647
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo:bar', 'baz')
    assert mapping == {'foo': {'bar': 'baz'}}

