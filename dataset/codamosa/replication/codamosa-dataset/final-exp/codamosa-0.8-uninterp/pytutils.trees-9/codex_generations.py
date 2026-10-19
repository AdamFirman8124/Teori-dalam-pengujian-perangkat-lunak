

# Generated at 2022-06-14 06:46:16.821794
# Unit test for function get_tree_node
def test_get_tree_node():
    mock = collections.defaultdict(dict)
    mock['a']['b']['c'] = 1

    assert get_tree_node(mock, 'a:b:c') == 1
    assert get_tree_node(mock, 'a:b:c:d:e:') == _sentinel
    assert get_tree_node(mock, 'a:b:c:d:e:', _sentinel) == _sentinel
    assert get_tree_node(mock, 'a:b:c:d:e:', _sentinel) == _sentinel
    assert get_tree_node(mock, 'a:b:c:d:e:', default='aaaaaaaa') == 'aaaaaaaa'

# Generated at 2022-06-14 06:46:25.747144
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'foo': {
            'bar': {
                'baz': 'yay',
            },
        },
    }
    assert get_tree_node(d, 'foo') == {'bar': {'baz': 'yay'}}
    assert get_tree_node(d, 'foo:bar') == {'baz': 'yay'}
    assert get_tree_node(d, 'foo:bar:baz') == 'yay'



# Generated at 2022-06-14 06:46:36.188464
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'root': {
            'level_one': {
                'level_two_a': 'value_1',
                'level_two_b': 'value_2'
            }
        }
    }

    # Test getting a root node
    assert get_tree_node(tree, 'root') == {
        'level_one': {
            'level_two_a': 'value_1',
            'level_two_b': 'value_2'
        }
    }

    # Test getting an inner node
    assert get_tree_node(tree, 'root:level_one:level_two_a') == 'value_1'

    # Test getting an inner node using no colons
    assert get_tree_node(tree, 'root:level_one:level_two_a', parent=True)

# Generated at 2022-06-14 06:46:42.020492
# Unit test for function get_tree_node
def test_get_tree_node():
    # _sentinel never raises
    assert get_tree_node({}, 'test', default=get_tree_node) is get_tree_node

    # Tree should raise KeyError
    with pytest.raises(KeyError):
        get_tree_node({}, 'test')

    # Simulate get_tree_node on a tree-like mapping structure
    # Should yield something along the lines of {'some': {'deep': 'node'}}
    assert get_tree_node({}, 'some:deep:node') == {'some': {'deep': {'node': None}}}

    # If a node is not found via : notation, should yield the relevant parent
    assert get_tree_node({}, 'some:deep:node:', parent=True) == {'some': {'deep': {}}}

# Generated at 2022-06-14 06:46:51.997533
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_lookup = {
        'a': {
            'b': {
                'c': 1
            }
        }
    }
    assert get_tree_node(tree_lookup, 'a:b:c') == 1

    assert get_tree_node(tree_lookup, 'a:b') == {'c': 1}

    tree_lookup = {
        'b': {
            'c': {
                'd': 1
            }
        }
    }
    assert get_tree_node(tree_lookup, 'b:c') == {'d': 1}



# Generated at 2022-06-14 06:47:05.419464
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
        },
        'e': 4,
        'f': {
            'g': {
                'h': 5
            }
        }
    }

    # Simple lookup
    assert get_tree_node(mapping, 'a') == 1
    assert get_tree_node(mapping, 'f:g:h') == 5

    assert get_tree_node(mapping, 'g', default=6) == 6

    # Traversal should be case-insensitive
    assert get_tree_node(mapping, 'F:G:H') == 5

    # Parent should be returned, as we are looking for 'g' not 'g:h'

# Generated at 2022-06-14 06:47:15.113171
# Unit test for function get_tree_node
def test_get_tree_node():
    sample_json = {
        "title": "something",
        "foo": {
            "bar": {
                "baz": "foo"
            }
        }
    }
    assert get_tree_node(sample_json, "title") == "something"
    assert get_tree_node(sample_json, "foo:bar:baz") == "foo"
    assert get_tree_node(sample_json, "spam:eggs:crack") is _sentinel
    assert get_tree_node(sample_json, "spam:eggs:crack", "foo") == "foo"



# Generated at 2022-06-14 06:47:19.241296
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = collections.defaultdict(collections.defaultdict)
    set_tree_node(test_tree, 'a.b.c', 42)
    assert test_tree['a']['b']['c'] == 42



# Generated at 2022-06-14 06:47:23.905352
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'x:y:z', 'foo')
    assert tree == {'x': {'y': {'z': 'foo'}}}



# Generated at 2022-06-14 06:47:29.384845
# Unit test for function set_tree_node
def test_set_tree_node():
    d = tree()
    set_tree_node(d, 'foo:bar:baz', 'abc')
    assert d['foo']['bar']['baz'] == 'abc'
    assert d['foo']['bar'] == {'baz': 'abc'}
    

# Generated at 2022-06-14 06:47:38.911416
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {
        'foo': {
            'bar': {
                'baz': 1,
            },
        },
    }
    set_tree_node(mapping, 'foo:bar:baz', 2)
    assert mapping['foo']['bar']['baz'] == 2



# Generated at 2022-06-14 06:47:46.393061
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {'a': {'b': {'c': 'foo'}},
                 'd': {'e': 'bar'}}
    assert get_tree_node(test_data, 'a:b:c') == 'foo'
    assert get_tree_node(test_data, 'd:e') == 'bar'

    # Test parent node
    assert get_tree_node(test_data, 'a:b:c', parent=True) == {'c': 'foo'}

# Generated at 2022-06-14 06:47:56.260299
# Unit test for function set_tree_node
def test_set_tree_node():
    import json
    # Pretty simple, just test if this works as expected
    data = {}
    assert set_tree_node(data, 'key:is:here', 'value') == {'key': {'is': {'here': 'value'}}}

    # Now try to do stuff with a non-empty tree
    data = tree()
    set_tree_node(data, 'key:is:here', 'value')
    set_tree_node(data, 'key:is:also:here', 'other_value')
    print(json.dumps(data, indent=4))
    assert data == {'key': {'is': {'here': 'value', 'also': {'here': 'other_value'}}}}

    # How about something a bit more advanced?

# Generated at 2022-06-14 06:48:00.068100
# Unit test for function set_tree_node
def test_set_tree_node():
    mydict = dict(a=1)
    set_tree_node(mydict, 'b:c:d', 2)
    assert mydict['b']['c']['d'] == 2



# Generated at 2022-06-14 06:48:08.550875
# Unit test for function get_tree_node
def test_get_tree_node():
    test = {
        'foo': 'bar',
        'baz': {
            'qux': 'quux',
            'bla': {
                'bla': 'bla',
            }
        }
    }

    # Normal cases
    assert get_tree_node(test, 'foo') == 'bar'
    assert get_tree_node(test, 'baz:qux') == 'quux'
    assert get_tree_node(test, 'baz:bla:bla') == 'bla'

    # Parent cases
    assert get_tree_node(test, 'baz:qux', parent=True) == {
        'qux': 'quux',
        'bla': {
            'bla': 'bla',
        }
    }

# Generated at 2022-06-14 06:48:15.714081
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a':
            {'aa': {
                'aaa': 'val1'
            }},
        'b': 'val2',
    }

    assert get_tree_node(mapping, 'a:aa') == {'aaa': 'val1'}
    assert get_tree_node(mapping, 'a:aa:aaa') == 'val1'

    assert get_tree_node(mapping, 'b') == 'val2'



# Generated at 2022-06-14 06:48:27.074867
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'foobar',
            'baz': 'foobaz',
        },
        'bar': {
            'baz': {
                'foo': 'barbazfoo',
            }
        },
    }

    # From root
    assert get_tree_node(mapping, 'foo:bar') == 'foobar'
    assert get_tree_node(mapping, 'bar:baz:foo') == 'barbazfoo'
    assert get_tree_node(mapping, 'bar:baz:foo', parent=True) == {'foo': 'barbazfoo'}

    # Using specified parent
    assert get_tree_node(mapping['bar'], 'baz:foo') == 'barbazfoo'

# Generated at 2022-06-14 06:48:37.820129
# Unit test for function get_tree_node
def test_get_tree_node():
    from copy import deepcopy
    from os.path import join
    from pprint import pformat


# Generated at 2022-06-14 06:48:51.378008
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:baz') is _sentinel

    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar', default='foobar') == 'baz'
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar:baz', default='foobar') == 'foobar'

    assert get_tree_node({'foo': {'bar': {'baz': 'foobar'}}}, 'foo:bar:baz') == 'foobar'

# Generated at 2022-06-14 06:48:59.002129
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    # Test traversal
    assert get_tree_node(test_mapping, 'a:b:c') == 'd'

    # Test KeyError
    with pytest.raises(KeyError):
        get_tree_node(test_mapping, 'foo')

    # Test with non-sentineled default
    assert get_tree_node(test_mapping, 'foo', default='foo_default') == 'foo_default'

    # Test parent node
    assert get_tree_node(test_mapping, 'a:b:c', parent=True) == {'c': 'd'}



# Generated at 2022-06-14 06:49:13.349965
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'mykey': {
            'mykey2': 'value'
        },
        'mykey3': 'value2'
    }

    assert get_tree_node(tree, 'mykey:mykey2') == {
        'mykey': {
            'mykey2': 'value'
        },
        'mykey3': 'value2'
    }.get('mykey:mykey2')

    assert get_tree_node(tree, 'mykey:mykey2') == {
        'mykey': {
            'mykey2': 'value'
        },
        'mykey3': 'value2'
    }.get('mykey:mykey2')


# Generated at 2022-06-14 06:49:26.336587
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': 1,
        'b': {'a': 2},
        'c': {'a': 3,
              'b': {'a': 4}},
        'd': {'a': 5,
              'b': {'a': 6},
              'c': {'a': 7,
                    'b': {'a': 8}}}}

    assert get_tree_node(tree, 'a') == 1
    assert get_tree_node(tree, 'b:a') == 2
    assert get_tree_node(tree, 'c:a') == 3
    assert get_tree_node(tree, 'c:b:a') == 4
    assert get_tree_node(tree, 'd:a') == 5

# Generated at 2022-06-14 06:49:30.977169
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {
            'b': {
                'c': {
                    'd': 'e',
                }
            }
        }
    }
    result = get_tree_node(data, 'a:b:c:d')
    assert result == 'e'



# Generated at 2022-06-14 06:49:37.214076
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {'a': {'b': {'c': {'d': 'I am d'}}}}
    assert get_tree_node(data, 'a:b:c:d') == 'I am d'
    assert get_tree_node(data, 'a:b:c:d:e:f:g:h:i') is _sentinel



# Generated at 2022-06-14 06:49:41.469238
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Quick and dirty unit test for set_tree_node.
    """
    tree = {}
    set_tree_node(tree, 'foo:bar:baz', 'qux')
    assert tree['foo']['bar']['baz'] == 'qux', tree

# Generated at 2022-06-14 06:49:54.086765
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'foo': {'bar': 'foobar'}}, 'foo:bar') == 'foobar'
    assert get_tree_node({'foo': {'bar': {'foobar': 'baz'}}}, 'foo:bar:foobar') == 'baz'
    assert get_tree_node({'foo': ['bar', 'baz']}, 'foo:1') == 'baz'
    assert get_tree_node({'foo': {'bar': 'foobar'}}, 'foo:bar') == 'foobar'
    assert get_tree_node({'foo': {'bar': 'foobar'}}, 'nope', default='bar') == 'bar'

# Generated at 2022-06-14 06:49:56.375402
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 3}}}, 'a:b:c') == 3



# Generated at 2022-06-14 06:50:01.075380
# Unit test for function set_tree_node
def test_set_tree_node():
    md = collections.defaultdict(collections.defaultdict)
    set_tree_node(md, 'a:b:c', 'test')
    assert md['a']['b']['c'] == 'test'



# Generated at 2022-06-14 06:50:13.578493
# Unit test for function get_tree_node
def test_get_tree_node():
    # Given a mapping
    mapping = {'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}}

    # When I try to get a, c and f with get_tree_node()
    a = get_tree_node(mapping, 'a')
    c = get_tree_node(mapping, 'b:c')
    f = get_tree_node(mapping, 'd:e:f')

    # Then it should be found
    assert a == 1
    assert c == 2
    assert f == 3

    # When I try to get a non-existing node
    # Then it should raise an exception
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'g')

    # When I pass a default value
    # Then it

# Generated at 2022-06-14 06:50:17.912240
# Unit test for function set_tree_node
def test_set_tree_node():
    f1 = tree()
    f2 = tree()
    set_tree_node(f1, 'reg:f1:f2', f2)
    assert f1['reg']['f1']['f2'] == f2



# Generated at 2022-06-14 06:50:33.091547
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for `get_tree_node` function."""
    # Set up test input
    tree = {
        'AA': {
            'BB': 'foo',
        },
        'CC': {
            'DD': 'bar',
        },
    }
    # Perform unit test
    assert get_tree_node(tree, 'AA') == {'BB': 'foo'}
    assert get_tree_node(tree, 'AA:BB') == 'foo'
    assert get_tree_node(tree, 'CC') == {'DD': 'bar'}
    assert get_tree_node(tree, 'CC:DD') == 'bar'
    # No special exception handling required if key is not found - KeyError is raised.

# Generated at 2022-06-14 06:50:37.890033
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree()
    tree['foo'] = {'bar': 'baz'}
    assert get_tree_node(tree, 'foo:bar') == 'baz'
    assert tree['foo:bar'] == 'baz'



# Generated at 2022-06-14 06:50:50.521562
# Unit test for function get_tree_node
def test_get_tree_node():
    import unittest

    class TestGetTreeNode(unittest.TestCase):
        def setUp(self):
            self.mapping = tree()
            self.mapping['foo']['bar']['ham'] = 'SPAM'
            self.mapping['foo']['spam'] = 'LARD'

        def test_get_key(self):
            self.assertEquals(get_tree_node(self.mapping, 'foo:bar:ham'), 'SPAM')

        def test_get_key_parent(self):
            self.assertEquals(get_tree_node(self.mapping, 'foo:bar:ham', parent=True), {'ham': 'SPAM'})


# Generated at 2022-06-14 06:50:55.887876
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {'a': {'b': {'c': 1}}}
    set_tree_node(mapping, 'b:c:d:e:f:g:h', 'foo')

    assert mapping['a']['b']['c']['d']['e']['f']['g']['h'] == 'foo'

# Generated at 2022-06-14 06:51:09.020383
# Unit test for function set_tree_node
def test_set_tree_node():
    tree1 = {0: {}}
    assert set_tree_node(tree1, '0:0', 'tree1') == {0: {'0': 'tree1'}}
    tree2 = {1: []}
    assert set_tree_node(tree2, '1:0', 'tree2') == {1: ['tree2']}
    tree3 = {'a': {}}
    assert set_tree_node(tree3, 'a:b', 'tree3') == {'a': {'b': 'tree3'}}
    tree4 = {2: {}}
    assert set_tree_node(tree4, '3:4', []) == {2: {}, '3': {'4': []}}
    tree5 = {'m': {}}

# Generated at 2022-06-14 06:51:22.216099
# Unit test for function get_tree_node
def test_get_tree_node():
    # Set up our environment for testing
    doc = {
        'dim1': {
            'dim2': {
                'dim3': 'value',
            }
        }
    }

    # ... but then we can't use assert because it's a fucking keyword.
    # python, why.
    assert get_tree_node(doc, 'dim1:dim2:dim3') == 'value'
    assert get_tree_node(doc, 'dim1:dim2:dim3', default='notfound') == 'value'
    assert get_tree_node(doc, 'dim1:dim2:dim3', default='notfound', parent=True) == {
        'dim3': 'value'
    }

# Generated at 2022-06-14 06:51:27.163159
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = {'a': {'b': {'c': 'd'}}}
    key = 'a:b'
    value = 'e'
    expect = {'a': {'b': 'e'}}
    set_tree_node(test_mapping, key, value)
    assert test_mapping == expect



# Generated at 2022-06-14 06:51:37.094718
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'foo': {'bar': 1}}
    assert get_tree_node(mapping, 'foo:bar') == 1

    assert get_tree_node(mapping, 'foo:baz') is _sentinel

    assert get_tree_node(mapping, 'foo:baz', default=2) == 2

    mapping = collections.OrderedDict()
    mapping['foo'] = collections.OrderedDict()
    mapping['foo']['bar'] = collections.OrderedDict()
    mapping['foo']['bar']['baz'] = 1
    assert get_tree_node(mapping, 'foo:bar') == mapping['foo']['bar']
    assert get_tree_node(mapping, 'foo:bar:baz') == 1

    mapping = collections.OrderedDict()
   

# Generated at 2022-06-14 06:51:39.709301
# Unit test for function set_tree_node
def test_set_tree_node():
    from copy import copy

    data = tree()
    data_copy = copy(data)
    set_tree_node(data, 'one', 1)
    assert data != data_copy



# Generated at 2022-06-14 06:51:48.141784
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'first': {
            'second': {
                'third': {
                    'four': 'value',
                }
            }
        }
    }
    assert get_tree_node(mapping, 'first:second:third:four') == 'value'
    mapping = tree()
    assert get_tree_node(mapping, 'first:second:third:four') == mapping['first']['second']['third']['four']



# Generated at 2022-06-14 06:52:29.633163
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'foo': {
            'bar': 'baz'
        }
    }

    # Test assertions
    assert get_tree_node(test_data, 'foo:bar') == 'baz'
    assert get_tree_node(test_data, 'foo') == {'bar': 'baz'}
    assert get_tree_node(test_data, 'foo:bar:baz', default='default') == 'default'

    # Make sure error is raised when we expect it
    try:
        get_tree_node(test_data, 'foo:bar:baz')
    except KeyError as exc:
        pass
    else:
        raise AssertionError('KeyError was not raised. Expected it to.')



# Generated at 2022-06-14 06:52:36.814169
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, "foo:bar", "baz")
    set_tree_node(tree, "foo:bing", 1)
    set_tree_node(tree, "buzz", 100)

    assert tree == {
        "foo": {
            "bar": "baz",
            "bing": 1,
        },
        "buzz": 100,
    }

# Generated at 2022-06-14 06:52:45.279477
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': 1}}, 'a') == {'b': 1}
    assert get_tree_node({'a': {'b': {'c': 1}}}, 'a:b') == {'c': 1}
    assert get_tree_node({'a': {'b': 1}}, 'a:b') == 1
    assert get_tree_node({'a': {'b': 1}}, 'a:b:c', default=0) == 0



# Generated at 2022-06-14 06:52:51.534170
# Unit test for function get_tree_node
def test_get_tree_node():
    d = tree()
    d['a']['b']['c'] = 'd'
    assert get_tree_node(d, 'a:b:c') == 'd'
    assert get_tree_node(d, 'a:b') == {'c': 'd'}
    try:
        get_tree_node(d, 'a:b:x')
    except KeyError:
        pass
    else:
        assert False, "should raise"



# Generated at 2022-06-14 06:53:02.817466
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest

    test_data = collections.defaultdict(collections.defaultdict(int))
    test_data[0][0] = 0
    test_data[0][1] = 1
    test_data[1][0] = 2
    test_data[1][1] = 3

    test_data[0][0] = collections.defaultdict(int)
    test_data[0][0][0] = 0

    result = get_tree_node(test_data, '0:0:0')
    assert result == 0

    result = get_tree_node(test_data, '0:0:0:0')
    assert result == _sentinel
    with pytest.raises(KeyError):
        get_tree_node(test_data, '0:0:0:0')

    result = get

# Generated at 2022-06-14 06:53:14.255564
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for get_tree_node
    """
    mapping = tree()
    set_tree_node(mapping, 'foo', 'bar')
    assert get_tree_node(mapping, 'foo') == 'bar'
    set_tree_node(mapping, 'foo:bar:baz', 'baz')
    assert get_tree_node(mapping, 'foo:bar:baz') == 'baz'
    assert get_tree_node(mapping, 'foo:bar:baz:blah', default='foo') == 'foo'
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'foo:bar:baz:blah')



# Generated at 2022-06-14 06:53:21.065922
# Unit test for function set_tree_node
def test_set_tree_node():
    data = {}
    assert set_tree_node(data, 'a:b', 1) == {'a': {'b': 1}}
    assert set_tree_node(data, 'a:c', 2) == {'a': {'b': 1, 'c': 2}}
    assert set_tree_node(data, 'a:d:e', 3) == {'a': {'b': 1, 'c': 2, 'd': {'e': 3}}}
    assert set_tree_node(data, 'a:d:f', 4) == {'a': {'b': 1, 'c': 2, 'd': {'e': 3, 'f': 4}}}



# Generated at 2022-06-14 06:53:33.055074
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'foo': {
            'bar': {
                'baz': 'foo-bar-baz',
                'biz': 'foo-bar-biz',
            },
            'bar2': 'foo-bar2',
        }
    }


# Generated at 2022-06-14 06:53:40.852093
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_ = {
        'foo': {
            'bar': {
                'baz': 'qux'
            }
        }
    }

    assert get_tree_node(tree_, 'foo:bar:baz') == 'qux'
    assert get_tree_node(tree_, 'foo:bar:qux', default='default') == 'default'
    assert get_tree_node(tree_, 'foo:bar:baz', parent=True) == {'baz': 'qux'}
    try:
        get_tree_node(tree_, 'foo:bar:qux')
    except KeyError:
        pass
    else:
        raise AssertionError('KeyError not raised on missing node')



# Generated at 2022-06-14 06:53:51.589635
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> new_mapping = {
    ...     'foo':
    ...         {
    ...             'bar': 'baz',
    ...         }
    ... }
    >>> get_tree_node(new_mapping, 'foo:bar')
    'baz'
    >>> get_tree_node(new_mapping, 'foo:notbar')
    Traceback (most recent call last):
        ...
    KeyError: 'notbar'
    >>> get_tree_node(new_mapping, 'foo:notbar', default='foobar')
    'foobar'
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:54:40.712448
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['a'][2]['b'] = 'b'
    mapping['a']['b'] = 'c'

    # Test that we are accessing the correct value
    assert get_tree_node(mapping, 'a:2:b') == 'b'

    # Test that we stop on first match
    assert get_tree_node(mapping, 'a:b') == 'c'


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:54:46.394981
# Unit test for function get_tree_node
def test_get_tree_node():
    map = Tree()
    map['key'] = {'sub1': 'sub1value'}
    assert get_tree_node(map, 'key:sub1') == 'sub1value'
    assert get_tree_node(map, 'key') == {'sub1': 'sub1value'}



# Generated at 2022-06-14 06:54:52.523541
# Unit test for function set_tree_node
def test_set_tree_node():
    node = {}
    assert set_tree_node(node, 'foo:bar', 'baz') == {'foo': {'bar': 'baz'}}
    assert set_tree_node(node, 'foo:baz', 'qux') == {'foo': {'bar': 'baz', 'baz': 'qux'}}



# Generated at 2022-06-14 06:54:57.214328
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree({'foo': {'bar': 'baz'}})
    assert tree.get('foo:bar') == 'baz'

    assert get_tree_node(tree, 'foo:bar') == 'baz'
    assert get_tree_node(tree, 'foo:baz') is _sentinel

# Generated at 2022-06-14 06:55:08.379904
# Unit test for function get_tree_node
def test_get_tree_node():
    # Set up test tree
    _tree = {
        'a': {'b': {'c': 2}},
        'd': {'e': {'f': 5}}
    }

    # Test that it works
    assert get_tree_node(_tree, 'a:b:c') == 2
    assert get_tree_node(_tree, 'd:e:f') == 5

    # Test that it throws error if not found
    with pytest.raises(KeyError):
        get_tree_node(_tree, 'a:b:c:d')

    # Test that it works with default
    assert get_tree_node(_tree, 'a:b:c:d', default=3) == 3



# Generated at 2022-06-14 06:55:19.297985
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Basic tests for :func:`get_tree_node`.

    """
    test_cases = (
        # Basic lookup
        ({'foo': 'bar'}, 'foo', 'bar'),
        ({'foo': 'bar'}, 'bar', _sentinel, KeyError),
        # Indexing
        ({'foo': ['bar', 'baz']}, 'foo:1', 'baz'),
        # Dict
        ({'foo': {'bar': 'baz'}}, 'foo:bar', 'baz'),
    )

    for test_case in test_cases:
        if isinstance(test_case, tuple):
            mapping, key, expected, error = test_case + (_sentinel,) * (4 - len(test_case))
        else:
            mapping, key, expected = test_case, None, test

# Generated at 2022-06-14 06:55:23.902385
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = tree()
    test_data['a']['b']['c'] = 'value'
    assert get_tree_node(test_data, 'a:b:c') == 'value'



# Generated at 2022-06-14 06:55:26.175168
# Unit test for function set_tree_node
def test_set_tree_node():
    test = {}
    set_tree_node(test, 'foo', 'bar')
    assert test == {'foo': 'bar'}



# Generated at 2022-06-14 06:55:38.036020
# Unit test for function get_tree_node
def test_get_tree_node():
    import string
    test_mapping = {
        'things': {
            'more_things': {
                'evenmorethings': [dict, object]
            }
        }
    }
    assert get_tree_node(test_mapping, 'things:more_things:evenmorethings') == [dict, object]
    assert get_tree_node(test_mapping, 'things:more_things') == {'evenmorethings': [dict, object]}
    assert get_tree_node(test_mapping, 'things') == {'more_things': {'evenmorethings': [dict, object]}}
    assert get_tree_node(test_mapping, 'things:more_things:evenmorethings:1') == object

# Generated at 2022-06-14 06:55:39.108990
# Unit test for function set_tree_node
def test_set_tree_node():
    pass

