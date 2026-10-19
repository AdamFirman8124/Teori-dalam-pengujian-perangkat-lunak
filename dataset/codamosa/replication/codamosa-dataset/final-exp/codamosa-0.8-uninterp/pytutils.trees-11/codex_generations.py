

# Generated at 2022-06-14 06:46:11.257752
# Unit test for function get_tree_node
def test_get_tree_node():
    # Set up
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }

    # Assert
    assert get_tree_node(mapping, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:46:16.931010
# Unit test for function get_tree_node
def test_get_tree_node():
    from copy import copy
    import collections
    import pytest
    data = tree()
    data['a']['b']['c']['d'] = 'e'

    assert get_tree_node(data, 'a:b:c:d') == 'e'
    with pytest.raises(KeyError):
        get_tree_node(data, 'a:b:c:d:e')



# Generated at 2022-06-14 06:46:29.923194
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    assert set_tree_node(tree, 'a', {'foo': 'bar'}) == tree
    assert set_tree_node(tree, 'b', {'baz': 'quux'}) == tree
    assert set_tree_node(tree, 'c', {'foobar': 'bar'}) == tree
    assert set_tree_node(tree, 'd:f', {'baz': 'quux'}) == tree['d']
    assert set_tree_node(tree, 'a:b:c', {'foobar': 'bar'}) == tree['a']['b']


# Generated at 2022-06-14 06:46:31.603414
# Unit test for constructor of class RegistryTree
def test_RegistryTree():
    tree = {}
    view = RegistryTree(tree)

    assert view is tree

# Generated at 2022-06-14 06:46:45.192890
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['1']['2']['3']['4'] = '4'
    t['1:2:3:4'] = '4'
    t['1:2']['3:4'] = '4'
    t['1']['2']['3']['4'] = '4'

# Generated at 2022-06-14 06:46:51.225339
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'test': {
                'dimension': 123,
                'another_dimension': 456
            },
            'test2': {
                'dimension': 123,
                'another_dimension': 456
            }
        }
    }

    assert get_tree_node(mapping, 'foo:test:dimension') == 123



# Generated at 2022-06-14 06:46:54.159832
# Unit test for constructor of class RegistryTree
def test_RegistryTree():
    """

    Returns:

    """

    r = RegistryTree()
    r.register('foo', 'bar')
    assert r['foo'] == 'bar'

# Generated at 2022-06-14 06:47:06.723628
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:47:17.485857
# Unit test for function get_tree_node
def test_get_tree_node():
    class Test(object):
        foo = {
            'bar': 'baz',
            'qux': {
                'quux': 'corge',
            }
        }

        def __init__(self, data, **kwargs):
            self.data = data
            self.__dict__.update(kwargs)

    test = Test(foo='bar', baz='qux')

    # Test no parent
    assert get_tree_node(test.data, 'bar', '(fail)') == 'baz'

    # Test no parent
    assert get_tree_node(test.data, 'qux', '(fail)').pop('quux') == 'corge'

    # Test no parent, KeyError

# Generated at 2022-06-14 06:47:26.098176
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': 1,
        'b': {
            'c': 2
        }
    }
    assert get_tree_node(tree, 'a') == 1
    assert get_tree_node(tree, 'b:c') == 2
    assert get_tree_node(tree, 'b:c:d', default=3) == 3
    assert get_tree_node(tree, 'b:c:d') is _sentinel



# Generated at 2022-06-14 06:47:38.961903
# Unit test for function get_tree_node
def test_get_tree_node():
    class MyTree(dict):
        def __getitem__(self, key, default=None):
            try:
                return super(MyTree, self).__getitem__(key)
            except KeyError:
                if default is None:
                    raise
                return default

    test_tree = MyTree({
        'key': {
            'sub': 'val'
        }
    })
    assert get_tree_node(test_tree, 'foo') is None
    assert get_tree_node(test_tree, 'key') == {'sub': 'val'}
    assert get_tree_node(test_tree, 'key:sub') == 'val'



# Generated at 2022-06-14 06:47:42.736317
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': 'c',
        },
    }
    assert get_tree_node(mapping, 'a:b') == 'c'
    assert get_tree_node(mapping, 'a', default=None) == {'b': 'c'}
    assert get_tree_node(mapping, 'x', default=None) is None
    assert get_tree_node(mapping, 'a:b:c', default=None) is None

# Generated at 2022-06-14 06:47:46.800026
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'a': {
            'b': 'moo',
            'c': 'hacker'
        }
    }
    assert get_tree_node(d, 'a:b') == 'moo'



# Generated at 2022-06-14 06:47:56.291356
# Unit test for function set_tree_node
def test_set_tree_node():
    # Test that a value can be set at root
    assert set_tree_node({}, 'foo', 'bar') == {'foo': 'bar'}

    # Test that a value can be set at a one level depth
    assert set_tree_node({}, 'foo:bar', 'baz') == {'foo': {'bar': 'baz'}}

    # Test that a value can be set at a two level depth
    assert set_tree_node({}, 'foo:bar:baz', 1) == {'foo': {'bar': {'baz': 1}}}

    # Test that a value can be set at a three level depth

# Generated at 2022-06-14 06:48:03.178751
# Unit test for function get_tree_node
def test_get_tree_node():
    # GIVEN a tree-like dict
    mapping = {
        'a': {
            'b': {
                'c': 'foobar',
            }
        }
    }

    # WHEN we try to get a node
    result = get_tree_node(mapping, 'a:b:c')

    # THEN it should evaluate to "foobar"
    assert result == 'foobar', 'Could not fetch tree node.'



# Generated at 2022-06-14 06:48:11.637043
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'foo': {
            'bar': {
                'baz': True,
            },
        },
    }
    assert get_tree_node(test_dict, 'foo:bar:baz') is True
    try:
        get_tree_node(test_dict, 'foo:bar:qux')
        assert False, "Should've raised KeyError"
    except KeyError:
        pass
    assert get_tree_node(test_dict, 'foo:bar:qux', default=False) is False



# Generated at 2022-06-14 06:48:22.999311
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for the function `get_tree_node`."""
    mapping = {'a': 'A'}
    assert get_tree_node(mapping, 'a') == 'A'
    assert get_tree_node(mapping, 'b') is _sentinel
    assert get_tree_node(mapping, 'b', default='B') == 'B'
    mapping = {'a': {'b': 'B'}}

# Generated at 2022-06-14 06:48:30.560753
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {'a': {'b': {'c': 'abc'}}}
    assert get_tree_node(tree, 'a:b:c') == 'abc'
    with pytest.raises(KeyError):
        get_tree_node(tree, 'a:b:x')
    assert get_tree_node(tree, 'a:b:x', default=None) is None



# Generated at 2022-06-14 06:48:38.884809
# Unit test for function get_tree_node
def test_get_tree_node():
    settings = {
        'foo': {
            'bar': {
                'baz': 1337
            }
        }
    }

    assert get_tree_node(settings, 'foo:bar:baz') == 1337
    assert get_tree_node(settings, 'foo:bar:baz:break') == _sentinel

    try:
        get_tree_node(settings, 'foo:bar:baz:break')
        assert False
    except KeyError:
        assert True



# Generated at 2022-06-14 06:48:50.174521
# Unit test for function get_tree_node
def test_get_tree_node():

    import pytest

    # Setup
    d = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    # Run
    res = get_tree_node(mapping=d, key='a:b:c')

    # Verify
    assert res == 'd'

    # Run
    with pytest.raises(KeyError):
        get_tree_node(mapping=d, key='a:b:e')

    # Run
    res = get_tree_node(mapping=d, key='a:b:e', default='foo')

    # Verify
    assert res == 'foo'



# Generated at 2022-06-14 06:49:02.652298
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'a': {
            'b': {
                'c': 'd',
            },
        },
    }
    assert get_tree_node(test_dict, 'a') == {'b': {'c': 'd'}}
    assert get_tree_node(test_dict, 'a:b') == {'c': 'd'}
    assert get_tree_node(test_dict, 'a:b:c') == 'd'



# Generated at 2022-06-14 06:49:11.300532
# Unit test for function get_tree_node
def test_get_tree_node():
    t = collections.defaultdict(dict)
    t['a']['b'] = 'c'

    assert get_tree_node(t, 'a') == {'b': 'c'}
    assert get_tree_node(t, 'a:b') == 'c'
    assert get_tree_node(t, 'a:b:c') == KeyError
    _unused = get_tree_node(t, 'a:b:c', default='d')
    assert _unused == 'd'



# Generated at 2022-06-14 06:49:16.249480
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'A:B:C', 'Hello World!')

# Generated at 2022-06-14 06:49:22.824314
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'app:server:address', 'localhost')
    set_tree_node(tree, 'app:server:port', 9000)
    assert tree == {
        'app': {
            'server': {
                'address': 'localhost',
                'port': 9000,
            }
        }
    }



# Generated at 2022-06-14 06:49:28.779562
# Unit test for function get_tree_node
def test_get_tree_node():

    tree = {
        'level1': {
            'level2': {
                'level3': 'value',
                'level3-2': 'value-2',
            }
        }
    }

    ret = get_tree_node(tree, 'level1:level2:level3')

    assert 'value' == ret, "get_tree_node should return value"



# Generated at 2022-06-14 06:49:41.474932
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'x': 1,
                'y': 2,
                'z': 3
            }
        },
        'c': 12,
        'd': 13,
        'e': 14,
    }

    assert mapping['a']['b']['x'] == get_tree_node(mapping, 'a:b:x')
    assert mapping['a']['b']['x'] == get_tree_node(mapping, 'a:b:x:c:d:e:f:g:h:i:j')
    assert mapping['c'] == get_tree_node(mapping, 'c')


# Generated at 2022-06-14 06:49:47.186976
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 1,
        'foo': {
            'b': 2
        }
    }
    assert get_tree_node(mapping, 'a') == 1
    assert get_tree_node(mapping, 'foo:b') == 2
    assert get_tree_node(mapping, 'foo:b:c') is None

# Generated at 2022-06-14 06:50:00.670754
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    assert set_tree_node(tree, 'foo', 1) == {'foo': 1}
    assert set_tree_node(tree, 'foo', 2) == {'foo': 2}
    assert set_tree_node(tree, 'foo:bar', 3) == {'foo': 2, 'bar': 3}
    assert set_tree_node(tree, 'foo:bar:baz', 4) == {'foo': 2, 'bar': 3, 'baz': 4}
    assert set_tree_node(tree, 'foo:bar:buzz', 5) == {'foo': 2, 'bar': 3, 'buzz': 5}
    assert set_tree_node(tree, 'foo:bazz', 6) == {'foo': 2, 'bazz': 6}



# Generated at 2022-06-14 06:50:10.504029
# Unit test for function get_tree_node
def test_get_tree_node():
    m = tree()
    m['a']['b']['c'] = 1
    assert get_tree_node(m, 'a:b:c') == 1
    assert get_tree_node(m, 'a:b')['c'] == 1
    assert get_tree_node(m, 'a:b:c:d', default=None) is None
    assert get_tree_node(m, 'a:b:c:d') is _sentinel
    try:
        get_tree_node(m, 'a:b:c:d')
    except KeyError:
        pass



# Generated at 2022-06-14 06:50:19.889405
# Unit test for function set_tree_node
def test_set_tree_node():
    dict_ = dict()
    dict_['keyone'] = 'valueone'
    dict_['keytwo'] = 'valuetwo'
    dict_['keythree'] = 'valuethree'

    dict_['keyfour:one'] = 'valuefour'
    dict_['keyfour:two'] = 'valuefive'
    dict_['keyfour:three'] = {'three': 'threetwo'}

    dict_['keyfour:three:three'] = 'threetwo'
    dict_['keyfour:three:four'] = 'threefour'
    dict_['keyfour:three:four:five'] = 'five'

    set_tree_node(dict_, 'keyfour:three:four:five', 'fourfive')
    assert dict_['keyfour:three:four:five'] == 'fourfive'



# Generated at 2022-06-14 06:50:30.579271
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}
    set_tree_node(d, 'foo:bar:baz:bop', 42)
    assert d == {'foo': {'bar': {'baz': {'bop': 42}}}}



# Generated at 2022-06-14 06:50:44.026298
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'a': {
            'b': {
                'c': 1,
            }
        },
        'd': {
            'b': 2,
        }
    }

    test_list = [
        {
            'a': {
                'b': {
                    'c': 1
                }
            },
            'd': {
                'b': 2
            }
        }
    ]

    def check_get_tree_node(ds, test_key, expected, expected_exc=False, default=_sentinel):
        try:
            result = get_tree_node(ds, test_key, default)
        except KeyError:
            result = _sentinel
        if expected_exc:
            assert result is _sentinel, 'Expected KeyError; got %s' % result

# Generated at 2022-06-14 06:50:53.586126
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'bar': {'baz': 'bing'}}, 'bar:baz') == 'bing'
    assert get_tree_node({'bar': {'baz': 'bing'}}, 'bar:baz', default='default') == 'bing'
    assert get_tree_node({'bar': {'baz': 'bing'}}, 'bar:baz:bing', default='default') == 'default'
    assert get_tree_node({'bar': {'baz': 'bing'}}, 'bar:baz:bing') is _sentinel

# Generated at 2022-06-14 06:51:02.652979
# Unit test for function get_tree_node
def test_get_tree_node():
    node = {
        'foo': {
            'bar': 'baz'
        }
    }

    result = get_tree_node(node, 'foo:bar')
    assert result == 'baz'

    result = get_tree_node(node, 'foobar:baz')
    assert result is _sentinel

    result = get_tree_node(node, 'foobar:baz', default='qux')
    assert result == 'qux'

# Generated at 2022-06-14 06:51:14.915460
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Test get_tree_node
    """
    m = {
        'name': {
            'first': 'One',
            'last': 'Drone',
        },
        'job': 'scout',
        'recent': {
            'employer': 'Army',
            'salary': 100,
        },
    }

    assert get_tree_node(m, 'name:first') == 'One'
    assert get_tree_node(m, 'name:last') == 'Drone'
    assert get_tree_node(m, 'job') == 'scout'
    assert get_tree_node(m, 'recent:employer') == 'Army'
    assert get_tree_node(m, 'name')['first'] == 'One'

# Generated at 2022-06-14 06:51:22.706962
# Unit test for function get_tree_node
def test_get_tree_node():
    string_dict = {'level_1': {'level_2': {'level_3': 'value'}}}

    assert get_tree_node(string_dict, 'level_1:level_2:level_3') == 'value'
    assert get_tree_node(string_dict, 'level_1:level_2') == {'level_3': 'value'}
    assert get_tree_node(string_dict, 'level_1') == {'level_2': {'level_3': 'value'}}

# Generated at 2022-06-14 06:51:25.504574
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:51:35.404614
# Unit test for function get_tree_node
def test_get_tree_node():
    print("Testing get_tree_node function")
    data = {'a': {'b': {'c': 0}}}
    assert get_tree_node(data, 'a:b') == {'c': 0}
    assert get_tree_node(data, 'a:b', parent=True) == {'b': {'c': 0}}
    assert get_tree_node(data, 'a:b:c') == 0
    assert get_tree_node(data, 'a:b:c:d') is None
    assert get_tree_node(data, 'a:b:c:d', default=False) is False



# Generated at 2022-06-14 06:51:43.969398
# Unit test for function get_tree_node
def test_get_tree_node():  # noqa
    from pytest import raises

    mapping = tree()
    mapping['c1']['c2'] = 'test'

    assert get_tree_node(mapping, 'c1:c2') == 'test'
    assert get_tree_node(mapping, 'c1:c2:x') is _sentinel
    assert get_tree_node(mapping, 'c1:c2:x', default='fail') == 'fail'
    with raises(KeyError):
        get_tree_node(mapping, 'c1:c2:x')



# Generated at 2022-06-14 06:51:49.500741
# Unit test for function set_tree_node
def test_set_tree_node():
    a = tree()
    set_tree_node(a, 'a:b:c', 3)
    set_tree_node(a, 'a:b:d', 4)

# Generated at 2022-06-14 06:52:22.915723
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['a']['b']['c'] = 'f'
    mapping.pickle = 'g'

    assert 'f' == get_tree_node(mapping, 'a:b:c')
    assert 'g' == get_tree_node(mapping, 'pickle')
    try:
        get_tree_node(mapping, 'f')
        assert False, "Should not reach this point, should have thrown KeyError"
    except KeyError:
        pass



# Generated at 2022-06-14 06:52:32.684581
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    mapping['a']['b']['c'] = 1
    mapping['a']['d'] = 2
    assert mapping['a']['b']['c'] == 1
    assert mapping['a']['d'] == 2

    mapping = tree()
    set_tree_node(mapping, 'a:b:c', 1)
    set_tree_node(mapping, 'a:d', 2)
    assert mapping['a']['b']['c'] == 1
    assert mapping['a']['d'] == 2



# Generated at 2022-06-14 06:52:40.054933
# Unit test for function get_tree_node
def test_get_tree_node():
    a = {
        'a': 'b',
        'c': {
            'd': 'e'
        }
    }

    # Test for simple key to value retrieval
    assert get_tree_node(a, 'a') == 'b'

    # Test for nested key to value retrieval
    assert get_tree_node(a, 'c:d') == 'e'

    # Test for parent node retrieval
    assert get_tree_node(a, 'c:d', parent=True) == {'d': 'e'}

    # Test for failure scenario
    with pytest.raises(KeyError):
        get_tree_node(a, 'c:x')

    # Test for non-failure scenario
    assert get_tree_node(a, 'c:x', default='fooo') == 'fooo'




# Generated at 2022-06-14 06:52:46.337704
# Unit test for function set_tree_node
def test_set_tree_node():
    data = tree()
    data['one'] = 1
    data['two'] = 2
    data['three'] = 3

    data['foo']['bar'] = 1

    for i in range(4):
        assert i == data[str(i)]

    assert len(data['foo']) == 1
    assert data['foo']['bar'] == 1



# Generated at 2022-06-14 06:52:49.905537
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {
        'one': {
            'two': {
                'three': 'four',
            },
        },
    }

    set_tree_node(mapping, 'four:five:six', 'seven')

    assert mapping['four'] == {'five': {'six': 'seven'}}



# Generated at 2022-06-14 06:53:00.742919
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 'value'
            }
        }
    }

    assert get_tree_node(mapping, 'a') == {'b': {'c': 'value'}}
    assert get_tree_node(mapping, 'a:b') == {'c': 'value'}
    assert get_tree_node(mapping, 'a:') == {'b': {'c': 'value'}}
    assert get_tree_node(mapping, 'a:b:c') == 'value'
    assert get_tree_node(mapping, 'a:b:') == {'c': 'value'}
    assert get_tree_node(mapping, 'a:b:d') is _sentinel

# Generated at 2022-06-14 06:53:07.943708
# Unit test for function get_tree_node
def test_get_tree_node():
    c = {
        'a': {
            'b': {
                'c': 123,
                'd': 456,
            },
            'c': {},
        }
    }
    assert get_tree_node(c, 'a:b:c') == 123
    assert get_tree_node(c, 'a:b:d') == 456
    assert get_tree_node(c, 'a:b:e', default='nothing') == 'nothing'

    with pytest.raises(KeyError):
        get_tree_node(c, 'a:b:e')

# Generated at 2022-06-14 06:53:16.302273
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree(), 'foo', default=None) is None

    tr = tree()
    tr['foo']['bar']['baz'] = 'ok'
    assert get_tree_node(tr, 'foo') == {'bar': {'baz': 'ok'}}
    assert get_tree_node(tr, 'foo:bar') == {'baz': 'ok'}
    assert get_tree_node(tr, 'foo:bar:baz') == 'ok'



# Generated at 2022-06-14 06:53:20.109075
# Unit test for function set_tree_node
def test_set_tree_node():
    store = {}
    set_tree_node(store, 'foo:bar:baz', 123)
    eq_(store, {'foo': {'bar': {'baz': 123}}})



# Generated at 2022-06-14 06:53:33.383311
# Unit test for function get_tree_node
def test_get_tree_node():
    dict = {'a': {'b': {'c': 42}}}
    assert get_tree_node(dict, 'a:b:c') == 42
    assert get_tree_node(dict, 'a:b', default=None) == {'c': 42}
    assert get_tree_node(dict, 'a:b:c', parent=True) == {'c': 42}
    assert get_tree_node(dict, 'a:b:d', default=None) is None

    dict = {'a': {'b': ['c', 'd']}}
    assert get_tree_node(dict, 'a:b') == ['c', 'd']
    assert get_tree_node(dict, 'a:b:0') == 'c'
    assert get_tree_node(dict, 'a:b:1')

# Generated at 2022-06-14 06:54:25.506069
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {"a": {"b": {"c": [1, 2, 3]}}}
    e = get_tree_node(d, 'a:b:c')
    assert e == [1, 2, 3]

    e = get_tree_node(d, 'a:d:c', default=None)
    assert e is None

    e = get_tree_node(d, 'a:b:d')
    assert e is _sentinel

    e = get_tree_node(d, 'a:b:c', default=_sentinel)
    assert e == [1, 2, 3]

    e = get_tree_node(d, 'a:b:d', default=_sentinel)
    assert e is _sentinel



# Generated at 2022-06-14 06:54:34.452587
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    assert get_tree_node(mapping, 'key') is _sentinel
    assert get_tree_node(mapping, 'key', default='def') == 'def'
    assert get_tree_node(mapping, 'a:b:c') == 'd'
    assert get_tree_node(mapping, 'a:b:c', parent=True) == {'c': 'd'}



# Generated at 2022-06-14 06:54:42.651868
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'test': {'test2': 2}}, 'test:test2') == 2
    assert get_tree_node({'test': {'test2': 2}}, 'test:test3', 'default') == 'default'
    assert get_tree_node({'test': {'test2': 2}}, 'test:test3') == KeyError
    assert get_tree_node({'test': {'test2': 2}}, 'test:test2', parent=True) == {'test2': 2}



# Generated at 2022-06-14 06:54:54.909314
# Unit test for function get_tree_node
def test_get_tree_node():
    class MyMapping(object):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, key):
            return self.data[key]

        def get(self, key, default=_sentinel):
            if default is _sentinel:
                # No default provided
                return self[key]
            return self.data.get(key, default)

    # Test all combinations of whether the key is present or not, and whether a default value is supplied
    for present in (True, False):
        for default in (_sentinel, 'default'):
            # Create a simple mapping
            mapping = MyMapping({
                'test': {
                    'test': True,
                }
            })

            # If we expect the key to be present, set it

# Generated at 2022-06-14 06:55:04.258547
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function get_tree_node"""
    test_mapping = {"0": {"1": "2", "3": "4"}}
    assert get_tree_node(test_mapping, "0:1") == "2"
    assert get_tree_node(test_mapping, "0:3") == "4"
    assert get_tree_node(test_mapping, "0:4") is _sentinel
    assert get_tree_node(test_mapping, "0:4", "default") == "default"



# Generated at 2022-06-14 06:55:09.867581
# Unit test for function set_tree_node
def test_set_tree_node():
    my_dict = {}
    set_tree_node(my_dict, '1:2:3', 'what')
    assert my_dict['1']['2']['3'] == 'what'


if __name__ == '__main__':
    test_set_tree_node()

# Generated at 2022-06-14 06:55:14.560165
# Unit test for function set_tree_node
def test_set_tree_node():
    import pprint
    d = {}
    set_tree_node(d, 'foo:bar:baz', True)
    pprint.pprint(d)
    assert d == {'foo': {'bar': {'baz': True}}}



# Generated at 2022-06-14 06:55:25.122287
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': {
                            'f': 'g',
                        },
                    },
                },
            },
        },
        'h': {
            'i': {
                'j': {
                    'k': {
                        'l': {
                            'm': 'n',
                        },
                    },
                },
            },
        },
    }
    assert get_tree_node(test_tree, 'a:b:c:d:e:f') == 'g'
    assert get_tree_node(test_tree, 'h:i:j:k:l:m') == 'n'



# Generated at 2022-06-14 06:55:33.251914
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = tree()
    set_tree_node(test_dict, 'child_1:child_2:child_3', 'data')
    assert test_dict['child_1']['child_2']['child_3'] == 'data'
    test_dict['child_1']['child_2']['child_3'] = 'data_mod'
    set_tree_node(test_dict, 'child_1:child_2:child_3', 'data')



# Generated at 2022-06-14 06:55:40.995810
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'foo': {'bar': {'baz': 'value'}}}
    v = get_tree_node(d, 'foo:bar:baz')
    assert v == 'value'

    try:
        v = get_tree_node(d, 'foo:bar:qux')
    except KeyError:
        pass
    else:
        raise AssertionError('Failed to raise KeyError')

    v = get_tree_node(d, 'foo:bar:qux', default=None)
    assert v is None

