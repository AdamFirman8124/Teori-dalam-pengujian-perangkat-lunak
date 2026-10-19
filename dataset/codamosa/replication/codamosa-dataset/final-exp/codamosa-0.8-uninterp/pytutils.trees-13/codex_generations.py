

# Generated at 2022-06-14 06:46:16.495188
# Unit test for function set_tree_node
def test_set_tree_node():
    tree_ = {}
    set_tree_node(tree_, 'key1:key2', 'value')
    assert tree_['key1']['key2'] == 'value'
    set_tree_node(tree_, 'key1:key3', 'value2')
    assert tree_['key1']['key3'] == 'value2'
    set_tree_node(tree_, 'key4:key5', 'value3')
    assert tree_['key4']['key5'] == 'value3'
    set_tree_node(tree_, 'key4:key3', 'value4')
    assert tree_['key4']['key3'] == 'value4'


# Generated at 2022-06-14 06:46:29.483900
# Unit test for function set_tree_node
def test_set_tree_node():
    # Instantiate a tree
    tree = {}
    # Let's set some values
    tree = set_tree_node(tree, 'foo:bar:baz', 'buzz')
    # Make sure it's what we expect
    assert 'bar' in tree['foo']
    assert 'baz' in tree['foo']['bar']
    assert tree['foo']['bar']['baz'] == 'buzz'

    # Now let's make sure we don't lose arbitrary data when we re-set it
    tree = set_tree_node(tree, 'foo:bar:baz', 'meow')
    # Make sure it's what we expect
    assert 'bar' in tree['foo']
    assert 'baz' in tree['foo']['bar']

# Generated at 2022-06-14 06:46:32.380914
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'hello:world', 'foobar')
    assert mapping['hello']['world'] == 'foobar'



# Generated at 2022-06-14 06:46:36.665446
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'a:b:c', 3)
    assert d['a']['b']['c'] == 3



# Generated at 2022-06-14 06:46:42.273776
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }
    # We should be able to set a value in a dictionary and get it back
    set_tree_node(mapping, 'foo:bar', 'baz')
    assert get_tree_node(mapping, 'foo:bar') == 'baz'

    # We should be able to set a value and get it back
    set_tree_node(mapping, 'foo:bar:baz', 'quux')
    assert get_tree_node(mapping, 'foo:bar:baz') == 'quux'

    # We should be able to create a new tree
    set_tree_node(mapping, 'a:b:c', 'd')

# Generated at 2022-06-14 06:46:54.933579
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test simple case
    assert get_tree_node({'foo': {'bar': {'baz': 'bat'}}}, 'foo:bar:baz') == 'bat'

    # Test invalid key case
    with pytest.raises(KeyError):
        get_tree_node({'foo': {'bar': {'baz': 'bat'}}}, 'foo:bar:bat')

    # Test default
    assert get_tree_node({'foo': {'bar': {'baz': 'bat'}}}, 'foo:bar:bat', default='x') == 'x'

    # Test parent node
    assert get_tree_node({'foo': {'bar': {'baz': 'bat'}}}, 'foo:bar:baz', parent=True) == {'baz': 'bat'}


# Unit test

# Generated at 2022-06-14 06:47:03.144695
# Unit test for function get_tree_node
def test_get_tree_node():
    base = {'foo': {'bar': 'baz'}}
    subject = get_tree_node(base, 'foo:bar')
    assert subject == 'baz'
    subject = get_tree_node(base, 'foo:bar:qux')
    assert subject == 'baz'
    # TODO Unfuck this shit
    #assert_raises(KeyError, get_tree_node, (base, 'foo:qux'))



# Generated at 2022-06-14 06:47:10.041763
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test the function `get_tree_node`."""
    test_mapping = {
        'foo': {
            'bar': {
                'baz': 'baz_value',
            }
        }
    }

    assert get_tree_node(test_mapping, 'foo:bar:baz', _sentinel) == 'baz_value'
    assert get_tree_node(test_mapping, 'foo:bar:baz', 'default_value') == 'baz_value'
    assert get_tree_node(test_mapping, 'foo:bar', _sentinel) == {'baz': 'baz_value'}
    assert get_tree_node(test_mapping, 'foo:bar:qux', 'default_value') == 'default_value'
    assert get_tree_node

# Generated at 2022-06-14 06:47:21.047845
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node({}, 'key', 1) == {'key': 1}
    assert set_tree_node({}, 'key:key2', 1) == {'key': {'key2': 1}}
    assert set_tree_node({'key': {'key2': {}}}, 'key:key2:key3', 1) == {'key': {'key2': {'key3': 1}}}
    assert set_tree_node({'key': {'key2': 1}}, 'key:key2:key3', 1) == {'key': {'key2': {'key3': 1}}}



# Generated at 2022-06-14 06:47:27.358737
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': 3
            }
        }
    }
    assert get_tree_node(tree, 'foo:bar:baz') == 3
    with pytest.raises(KeyError):
        get_tree_node(tree, 'foobar:baz')

# Generated at 2022-06-14 06:47:38.777433
# Unit test for function get_tree_node
def test_get_tree_node():
    _test_tree = tree()
    _test_tree['a'] = {
        'b': {
            'c': 'd',
        },
    }
    # Tree:
    # tree(['a']['b']['c']) == 'd'
    #
    # Desired outcome:
    # get_tree_node(_test_tree, 'a:b:c') == 'd'
    assert get_tree_node(_test_tree, 'a:b:c') == 'd'



# Generated at 2022-06-14 06:47:43.057609
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'my:key:list', ['my', 'list'])
    assert(tree['my']['key']['list'] == ['my', 'list'])



# Generated at 2022-06-14 06:47:48.426808
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 1,
                'd': 2,
            },
        },
    }
    assert get_tree_node(tree, 'a:b:c') == 1



# Generated at 2022-06-14 06:47:57.671170
# Unit test for function set_tree_node
def test_set_tree_node():
    """Unit tests for set_tree_node"""
    tree = {}
    set_tree_node(tree, 'a:b:c', 'd')
    assert tree == {'a': {'b': {'c': 'd'}}}
    set_tree_node(tree, 'a:b:c', 'e')
    assert tree == {'a': {'b': {'c': 'e'}}}
    set_tree_node(tree, 'a:b:f', 'g')
    assert tree == {'a': {'b': {'c': 'e', 'f': 'g'}}}
    set_tree_node(tree, 'a:b:f', 'g:h:i:j')

# Generated at 2022-06-14 06:48:03.539583
# Unit test for function get_tree_node
def test_get_tree_node():
    x = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': 'f'
                    }
                }
            }
        }
    }

    assert get_tree_node(x, 'a:b:c:d:e') == 'f', 'get_tree_node is broken'



# Generated at 2022-06-14 06:48:07.308860
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:baz', 'value')
    assert mapping['foo']['bar']['baz'] == 'value'



# Generated at 2022-06-14 06:48:20.714165
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'first': {
            'second': {
                'third': 'testvalue'
            }
        }
    }
    assert get_tree_node(mapping=test_mapping, key='first:second:third') == 'testvalue'
    assert get_tree_node(mapping=test_mapping, key='first:second:third:fourth', default='testdefault') == 'testdefault'
    assert get_tree_node(mapping=test_mapping, key='first:second:third:fourth') == _sentinel  # Raise KeyError

    # Test parent
    assert get_tree_node(mapping=test_mapping, key='first:second:third:fourth', default='testdefault', parent=True) == {
        'third': 'testvalue'
    }

    # Test

# Generated at 2022-06-14 06:48:27.358631
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {'a': {'b': {'c': True}}}
    assert get_tree_node(test_tree, 'a:b:c')
    with pytest.raises(KeyError):
        get_tree_node(test_tree, 'a:b:c:d')
    assert get_tree_node(test_tree, 'a:b:c:d', default=None) is None
    assert get_tree_node(test_tree, 'a', parent=True) == {'b': {'c': True}}

# Generated at 2022-06-14 06:48:37.930976
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:48:51.379051
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a1': {
            'b1': {
                'c1': 1
            },
            'b2': 2
        }
    }

    assert get_tree_node(mapping=mapping, key='a1:b1:c1') == 1
    assert get_tree_node(mapping=mapping, key='a1:b2') == 2
    assert get_tree_node(mapping=mapping, key='a1:b3', default=None) is None
    assert get_tree_node(mapping=mapping, key='a2:b2', default=None) is None
    with pytest.raises(KeyError):
        get_tree_node(mapping=mapping, key='a1:b3')



# Generated at 2022-06-14 06:49:12.253006
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Test get_tree_node

    """
    mappy = {}

    set_tree_node(mappy, 'a:b:c:d', 'hello')
    set_tree_node(mappy, 'a:b:c:e', 'world')
    assert len(mappy) == 1
    assert mappy == {'a': {'b': {'c': {'d': 'hello', 'e': 'world'}}}}
    set_tree_node(mappy, 'a:b:c:f', ['hello', 'world'])
    assert mappy == {'a': {'b': {'c': {'d': 'hello', 'e': 'world', 'f': ['hello', 'world']}}}}

# Generated at 2022-06-14 06:49:22.985490
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    :func:`get_tree_node` should...
    """
    mapping = {'a': {'b': 'c'}}
    assert get_tree_node(mapping, 'a:b') == 'c'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:foo') == 'c'

    assert get_tree_node(mapping, 'a:foo') == 'plop'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:foo:plop') == 'c'



# Generated at 2022-06-14 06:49:32.511980
# Unit test for function get_tree_node
def test_get_tree_node():
    from assertpy import assert_that

    registry = {
        'cat': {
            '_meta': {
                'default': True,
            },
            'snow-leopard': {
                '_meta': {
                    'default': True,
                },
            },
        },
    }

    # Test get by key
    assert_that(get_tree_node(registry, 'cat:_meta:default')).is_true()
    assert_that(get_tree_node(registry, 'cat:snow-leopard')).is_equal_to(
        {'_meta': {'default': True}})

    # Test get tree by key

# Generated at 2022-06-14 06:49:39.674951
# Unit test for function get_tree_node
def test_get_tree_node():
    import json
    data = json.loads("""
        {
            "a": {
                "b": {
                    "c": [{"d": [1, 2, 3]}, {"e": [4, 5, 6]}, {"f": [7, 8, 9]}]
                }
            }
        }
    """)
    assert get_tree_node(data, 'a:b:c:2:f:1') == 8



# Generated at 2022-06-14 06:49:43.318075
# Unit test for function get_tree_node
def test_get_tree_node():
    t = Tree({'foo': {'bar': 42}})
    assert get_tree_node(t, 'foo:bar') == 42



# Generated at 2022-06-14 06:49:54.346497
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test the get_tree_node function."""
    test_data = {
        "hello": {
            "world": {
                "people": {
                    "of": {
                        "the": "wunderbar"
                    }
                }
            }
        }
    }
    assert get_tree_node(test_data, "hello:world:people") == {'of': {'the': 'wunderbar'}}
    assert get_tree_node(test_data, "hello:world:people:of") == {'the': 'wunderbar'}
    assert get_tree_node(test_data, "hello:world:people:of:the") == "wunderbar"



# Generated at 2022-06-14 06:49:57.563013
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = Tree()
    mapping['foo:baz'] = 'bar'
    assert get_tree_node(mapping, 'foo:baz') == 'bar'
    assert get_tree_node(mapping, 'foo') == {'baz': 'bar'}

# Generated at 2022-06-14 06:50:06.612302
# Unit test for function get_tree_node
def test_get_tree_node():
    obj = {
        '1': {
            '2': {
                '3': {
                    '4': 4
                }
            }
        }
    }
    assert get_tree_node(obj, '1:2:3:4') == 4
    assert get_tree_node(obj, '1:2:3:3', 'test') == 'test'
    assert get_tree_node(obj, '1:2:3:4', parent=True) == {'4': 4}

# Generated at 2022-06-14 06:50:16.078153
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'foo': 'bar',
        'test': {
            'test_foo': 'test_bar',
            'test_test': {
                'test_test_foo': 'test_test_bar',
            }
        }
    }

    assert get_tree_node(test_tree, 'foo') == 'bar'
    assert get_tree_node(test_tree, 'test:test_foo') == 'test_bar'
    assert get_tree_node(test_tree, 'test:test_test:test_test_foo') == 'test_test_bar'

    assert get_tree_node(test_tree, 'test:test_test:test_test_foo:foo') == _sentinel

# Generated at 2022-06-14 06:50:28.860171
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:50:53.975470
# Unit test for function get_tree_node
def test_get_tree_node():
    # Simple key access
    d = {'ponies': 'fuzzy'}
    assert get_tree_node(d, 'ponies') == 'fuzzy'
    assert get_tree_node(d, 'homies') == _sentinel
    assert get_tree_node(d, 'homies', 'no homies') == 'no homies'
    # Delve down one level
    d = {'ponies': {'are': 'fuzzy'}}
    assert get_tree_node(d, 'ponies:are') == 'fuzzy'
    # Delve down two levels
    d = {'ponies': {'are': {'fuzzy': True}}}
    assert get_tree_node(d, 'ponies:are:fuzzy') is True



# Generated at 2022-06-14 06:51:03.474859
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = collections.defaultdict(dict)
    set_tree_node(mapping, 'foo:bar:baz', 'val')
    assert mapping['foo']['bar']['baz'] == 'val'

    mapping = collections.defaultdict(dict)
    set_tree_node(mapping, 'foo', 'val')
    assert mapping['foo'] == 'val'

    mapping = collections.defaultdict(dict)
    set_tree_node(mapping, ':foo:bar:baz', 'val')
    assert mapping['foo']['bar']['baz'] == 'val'

    mapping = collections.defaultdict(dict)
    set_tree_node(mapping, 'foo:bar:baz', 'val')
    assert mapping['foo']['bar']['baz'] == 'val'



# Generated at 2022-06-14 06:51:06.863730
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': 'x'}}}
    assert get_tree_node(tree, 'a:b:c') == 'x'



# Generated at 2022-06-14 06:51:11.352862
# Unit test for function get_tree_node
def test_get_tree_node():
    structure = {
        'a': {
            'b': {
                'c': {
                    'd': 'd'
                }
            }
        }
    }
    assert get_tree_node(structure, 'a:b:c:d') == 'd'



# Generated at 2022-06-14 06:51:20.324586
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function `get_tree_node`."""
    test_dict = {
        'a': 'a',
        'b': (1, 2, 3),
        'c': {
            'd': {
                'e': 'e'
            }
        }
    }
    test_dict = Tree(test_dict)
    assert test_dict.get('a') == 'a'
    assert test_dict.get('b') == (1, 2, 3)
    assert test_dict.get('c:d:e') == 'e'

# Generated at 2022-06-14 06:51:25.344470
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mapping = {
        'foo': 'bar'
    }
    test_mapping = Tree(test_mapping, namespace='scope')

    assert test_mapping.get('boo') == 'bar'
    assert test_mapping.get('boo', namespace='scope') == 'bar'



# Generated at 2022-06-14 06:51:36.558430
# Unit test for function set_tree_node
def test_set_tree_node():
    t = Tree()
    assert set_tree_node(t, 'foo:bar:baz', 5) == {'baz': 5}

    # Default value
    assert set_tree_node(t, 'a:b:c', 6) == {'c': 6}

    # Override value
    assert set_tree_node(t, 'foo:bar', 10) == {'bar': 10}

    # Parent override
    assert set_tree_node(t, 'foo:x:y', 15) == {'bar': 10, 'x': {'y': 15}}

    # Parent overwrite
    assert set_tree_node(t, 'foo:x', 16) == {'bar': 10, 'x': 16}

    assert t['foo:x'] == 16
    assert t['foo:bar'] == 10
    assert t

# Generated at 2022-06-14 06:51:42.177400
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree, 'key') == tree
    assert get_tree_node(tree, 'key:subkey') == tree['key']
    assert get_tree_node(tree, 'key:subkey', parent=True) == tree
    try:
        get_tree_node(tree, 'key')
    except KeyError:
        assert True
    else:
        assert False



# Generated at 2022-06-14 06:51:50.839602
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}

    set_tree_node(tree, 'k1', 'v1')
    assert tree == {'k1': 'v1'}

    set_tree_node(tree, 'k2:k3', 'v2')
    set_tree_node(tree, 'k4', tree['k2:k3'])
    assert tree == {'k1': 'v1', 'k2': {'k3': 'v2'}, 'k4': 'v2'}



# Generated at 2022-06-14 06:52:03.560681
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test get_tree_node method."""
    test_mapping = {
        'nested': {
            'name': 'obj1',
            'size': 'large',
        },
        'heavier': {
            'name': 'obj2',
            'size': 'massive',
        }
    }

    assert get_tree_node(test_mapping, 'nested:size') == 'large'
    assert get_tree_node(test_mapping, 'no_nodes:size') is _sentinel
    assert get_tree_node(test_mapping, 'no_nodes:size', default='unknown') == 'unknown'
    assert get_tree_node(test_mapping, 'heavier:size', parent=True) == {'name': 'obj2', 'size': 'massive'}

# Generated at 2022-06-14 06:52:48.439035
# Unit test for function get_tree_node
def test_get_tree_node():

    mapping = collections.OrderedDict(
        [
            ('a', 'A0'),
            ('b:b0', 'B0'),
            ('b:b1', 'B1'),
            ('b:b2', 'B2'),
            ('c', 'C0'),
            ('d:d0', 'D0'),
            ('d:d1', 'D1'),
            ('d:d2', 'D2'),
            ('e', 'E0'),
            ('f:f0', 'F0'),
            ('f:f1:f1', 'F1'),
            ('f:f2', 'F2')])

    def test_node(node, key, expected):
        value = get_tree_node(node, key)

# Generated at 2022-06-14 06:53:01.385878
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    UNIT TEST of :func:`get_tree_node`

    Testing:

        * Get node
        * Get node via parent
        * Get node via parent with default value

    """
    # Test 1
    t = tree()
    t["foo"]["bar"]["baz"] = 123
    assert get_tree_node(t, "foo:bar:baz") == 123

    # Test 2
    # Test parent node-fetching
    t = tree()
    t["foo"]["bar"]["baz"] = 123
    assert get_tree_node(t, "foo:bar:baz", parent=True) == t["foo"]["bar"]

    # Test 3
    # Test defaulting

# Generated at 2022-06-14 06:53:10.540704
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test recursive lookup of keys in tree-like objects."""
    config = {
        'foo': {
            'bar': 1,
            'baz': 2,
        }
    }
    assert get_tree_node(config, 'foo:bar') == 1
    with pytest.raises(KeyError):
        get_tree_node(config, 'foo:bar:baz')

    # Test the default argument
    assert get_tree_node(config, 'foo:bar:baz', default=1) == 1

    # Test the parent argument
    assert get_tree_node(config, 'foo:bar:baz', default=1, parent=True) == config['foo']
    config = {
        'foo': {
            'bar': [1, 2, 3, 4],
        }
    }

# Generated at 2022-06-14 06:53:19.973154
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': 1}, 'a') == 1
    assert get_tree_node({'a': {'b': 2}}, 'a:b') == 2
    assert get_tree_node({'a': {'b': 2}}, 'a:c') is _sentinel
    assert get_tree_node({'a': {'b': 2}}, 'a:c', default=1) == 1
    assert get_tree_node({'a': {'b': 2}}, 'a:b', parent=True) == {'b': 2}
    assert get_tree_node({'a': {'b': 2, 'c': 3}}, 'a:c:d') is _sentinel

# Generated at 2022-06-14 06:53:30.171732
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'name': 'My Program',
        'version': '1.0',
        'lang': {
            'en': 'English',
            'zh': 'Chinese',
        },
        'log': ['foo', 'bar', 'baz'],
    }

    assert get_tree_node(tree, 'name') == 'My Program'
    assert get_tree_node(tree, 'lang:en') == 'English'
    assert get_tree_node(tree, 'not_here', default='N/A') == 'N/A'
    assert get_tree_node(tree, 'not_here') == KeyError



# Generated at 2022-06-14 06:53:37.560530
# Unit test for function get_tree_node
def test_get_tree_node():
    data = tree()
    data['users']['by_id'][1]['name'] = "Mark"
    data['users']['by_name']["Mark"] = 1
    data['users']['by_name']["Tim"] = 2

    assert get_tree_node(data, 'users:by_id:1:name') == "Mark"
    assert get_tree_node(data, 'users:by_name:Mark') == 1



# Generated at 2022-06-14 06:53:45.306141
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'test': {
            'test': {
                'test': 'test'
            }
        }
    }

    assert get_tree_node(data, 'test:test:test') == 'test'
    assert get_tree_node(data, 'test:test:test', parent=True) == {'test': 'test'}
    assert get_tree_node(data, 'derp:test:test', default=None) is None

# Generated at 2022-06-14 06:53:50.842664
# Unit test for function get_tree_node
def test_get_tree_node():
    """Ensure we get the very deep node"""
    assert get_tree_node({
        'one': {
            'two': {
                'three': 'four'
            }
        }
    }, 'one:two:three') == 'four'



# Generated at 2022-06-14 06:53:59.979116
# Unit test for function get_tree_node
def test_get_tree_node():
    # Sample tree
    test_tree = tree()
    test_tree['level1']['level2']['level3'] = 'value'

    # Test key lookup
    assert get_tree_node(test_tree, 'level1:level2:level3') == test_tree['level1']['level2']['level3']
    assert get_tree_node(test_tree, 'level1') == test_tree['level1']
    assert get_tree_node(test_tree, 'level1:level2') == test_tree['level1']['level2']

    # Test key not found
    try:
        get_tree_node(test_tree, 'level1:not_found:level3')
        assert False
    except KeyError:
        pass

# Generated at 2022-06-14 06:54:11.079747
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> test_get_tree_node()
    """

    t = tree()
    t['test'] = 'test'
    t['test:test'] = 'test:test'
    t['test']['test'] = 'test.test'
    t['test']['test:test'] = 'test.test:test'
    t['test']['test']['test'] = 'test.test.test'
    t['test']['test']['test']['test'] = 'test.test.test.test'


    # TODO Test more dimensions

    assert get_tree_node(t, 'test') == 'test'
    assert get_tree_node(t, 'test:test') == 'test:test'

# Generated at 2022-06-14 06:55:42.142127
# Unit test for function get_tree_node
def test_get_tree_node():
    # Tree-like mapping structure for testing
    my_tree = {
        'x': ['A', 'B', 'C'],
        'y': {
            'tim': {
                'name': 'Tim',
                'age': 1,
            },
            'jill': {
                'name': 'Jill',
                'age': 2,
            }
        },
        'z': {
            'foo': {
                'bar': {
                    'xxx': 'Hello World',
                    'yyy': 'Foo Bar',
                }
            }
        }
    }

    # Test normal usage
    assert get_tree_node(my_tree, 'x:1') == 'B'
    assert get_tree_node(my_tree, 'y:jill:age') == 2
    assert get_tree_node

# Generated at 2022-06-14 06:55:52.584551
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': None,
                'd': None,
            }
        }
    }

    assert get_tree_node(tree, 'a:b:c') == None
    assert get_tree_node(tree, 'a:b:d') == None
    assert get_tree_node(tree, 'a:b:e', default="d") == "d"
    assert get_tree_node(tree, 'e:f:g', default="d") == "d"


# Unit tests for function set_tree_node

# Generated at 2022-06-14 06:56:00.564326
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'doggo'
        },
        'foo2': {
            'bar': 'hello_world'
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'doggo'
    assert get_tree_node(mapping, 'foo2:bar') == 'hello_world'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'baz')

    assert get_tree_node(mapping, 'baz', default='default') == 'default'



# Generated at 2022-06-14 06:56:07.341330
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'Baz'
        },
        'foo:bar': {
            'baz': 'Boom'
        }
    }
    assert get_tree_node(mapping, 'foo:baz:bar') == 'Boom'
    assert get_tree_node(mapping, 'foobar:bar:baz') is _sentinel

