

# Generated at 2022-06-14 06:46:08.603292
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': {'bar': 'baz'}}, 'foo:bar') == 'baz'



# Generated at 2022-06-14 06:46:17.552901
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        "foo": {
            "bar": {
                "baz": "spelunk"
            }
        },
        "fiz": "buzz"
    }

    assert get_tree_node(test_data, "foo:bar:baz") == "spelunk"
    assert get_tree_node(test_data, "fiz") == "buzz"

    try:
        assert get_tree_node(test_data, "blargh:blargh:blargh")
    except KeyError as exc:
        assert True
    else:
        assert False

    try:
        assert get_tree_node(test_data, "blargh:blargh:blargh", default=None) is None
    except KeyError:
        assert False

# Generated at 2022-06-14 06:46:25.803496
# Unit test for function get_tree_node
def test_get_tree_node():
    testing = Tree({'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': {'g': 5}})
    assert testing.get('a') == 1
    assert testing.get('b:c') == 2
    assert testing.get('f:g') == 5
    assert testing.get('b') == {'c': 2, 'd': 3}
    assert testing.get('g', default=666) == 666

# Generated at 2022-06-14 06:46:30.284608
# Unit test for function set_tree_node
def test_set_tree_node():
    registry = tree()
    set_tree_node(registry, 'one:two:three', 'four')
    assert registry['one']['two']['three'] == 'four'


if __name__ == '__main__':
    # Unit test for class Tree
    test_set_tree_node()

# Generated at 2022-06-14 06:46:33.513464
# Unit test for function set_tree_node
def test_set_tree_node():
    x = {}
    set_tree_node(x, 'hap:pity:the:fool', 'Mr T')
    assert x['hap']['pity']['the']['fool'] == 'Mr T'



# Generated at 2022-06-14 06:46:40.531292
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'foo': {
            'bar': {
                'qux': '!'
            }
        },
        'blep': 'blop'}
    assert get_tree_node(d, 'blep') == 'blop'
    assert get_tree_node(d, 'foo:bar:qux') == '!'



# Generated at 2022-06-14 06:46:52.859170
# Unit test for function get_tree_node
def test_get_tree_node():
    mock_data = {
        'foo': {
            'bar': {
                'baz': 'foobarbaz',
            },
            'bla': 'foobla',
        },
        'test': {
            'test': {
                'test': 'foobarbaz',
            },
            'test2': 'foobla',
        },
        'fail': {
            'bar': {
                'baz': 'fail',
            },
            'bla': 'fail',
        }
    }
    assert get_tree_node(mock_data, 'foo:bar:baz') == 'foobarbaz'
    assert get_tree_node(mock_data, 'foo:bar:bla',
                         default='test') == 'test'

# Generated at 2022-06-14 06:46:59.512302
# Unit test for function set_tree_node
def test_set_tree_node():
    m = {}
    # Set node, splitting via ':'
    set_tree_node(m, 'foo:bar', 1)
    assert m['foo']['bar'] == 1

    # Set node, but don't split via ':'
    set_tree_node(m, 'baz', 2)
    assert m['baz'] == 2



# Generated at 2022-06-14 06:47:12.569789
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = {
        'one': {
            'two': {
                'three': 'win'
            }
        },
        'two': 'fail'
    }

    assert get_tree_node(test_tree, 'one') == {
        'two': {
            'three': 'win'
        }
    }

    assert get_tree_node(test_tree, 'one:two') == {
        'three': 'win'
    }

    assert get_tree_node(test_tree, 'one:two:three') == 'win'

    assert get_tree_node(test_tree, 'one:two:four') is _sentinel

    assert get_tree_node(test_tree, 'one:two:four', default='win') == 'win'


# Generated at 2022-06-14 06:47:20.918631
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'a': 'a',
            'b': 'b',
            'c': 'c',
        },
        'b': {
            'a': 'A',
            'b': 'B',
            'c': 'C',
        },
    }

    assert get_tree_node(tree, 'a') == {
        'a': 'a',
        'b': 'b',
        'c': 'c',
    }

    assert get_tree_node(tree, 'a:a') == 'a'
    assert get_tree_node(tree, 'a:b') == 'b'
    assert get_tree_node(tree, 'a:c') == 'c'


# Generated at 2022-06-14 06:47:32.693197
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {
        'k1': {
            'k2': {
                'k3': 'v31',
                'k4': 'v41'
            },
            'k5': 'v5'
        }
    }
    assert get_tree_node(test_dict, 'k1:k2:k3') == 'v31'
    assert get_tree_node(test_dict, 'k1:k2:k4') == 'v41'
    assert get_tree_node(test_dict, 'k1:k5') == 'v5'



# Generated at 2022-06-14 06:47:39.321453
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 'value'}}}, 'a:b:c') == 'value'
    try:
        get_tree_node({}, 'a:b:c')
        assert False, 'KeyError was raised'
    except KeyError:
        pass



# Generated at 2022-06-14 06:47:50.456092
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test case 1: simple nested
    info = {
        'person': {
            'name': 'Jane Doe',
        }
    }
    assert 'Jane Doe' == get_tree_node(info, 'person:name')
    # Test case 2: default
    assert 'UNKNOWN' == get_tree_node(info, 'person:age', default='UNKNOWN')
    # Test case 3: KeyError
    with pytest.raises(KeyError):
        assert get_tree_node(info, 'person:age')
    # Test case 4: Multi-level nested
    info = {
        'parent': {
            'child': {
                'person': {
                    'name': 'Jane Doe',
                }
            }
        }
    }

# Generated at 2022-06-14 06:48:00.828719
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping[1][2][3] = 4
    assert get_tree_node(mapping, '1:2:3') == 4
    mapping['foo']['bar']['baz'] = 'spam'
    assert get_tree_node(mapping, 'foo:bar:baz') == 'spam'
    assert ':'.join(get_tree_node(mapping, 'foo:bar').keys()) == 'baz'
    assert get_tree_node(mapping, 'foo:bar:baz:pork') is _sentinel



# Generated at 2022-06-14 06:48:08.796219
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'a': 42,
        'b': {
            'c': {
                'd': 'test'
            },
            'e': [1, 2, 3, 4, 5]
        },
        'f': [1, 2, 3],
        'g': {
            'h': {
                'i': 'test2',
                'j': 'test3'
            }
        },
        'k': {
            'l': {
                'm': {
                    'n': 'test4'
                }
            },
            'o': [1, 2, 3, 4, 5]
        }
    }

    assert get_tree_node(mapping, 'a') == 42

# Generated at 2022-06-14 06:48:20.906656
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {
        'b': {
            'c': 3,
            'd': 4,
            'e': 5,
            'f': {
                'h': 7,
            }
        }
    }}
    assert get_tree_node(mapping, 'a:b:c') == 3
    assert get_tree_node(mapping, 'a:b:c', default=False) == 3
    assert get_tree_node(mapping, 'a:b:c', default=False, parent=True) == {'c': 3, 'd': 4, 'e': 5, 'f': {'h': 7}}
    assert get_tree_node(mapping, 'a:b:g', default=False) == False



# Generated at 2022-06-14 06:48:28.609354
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        '1': {'2': {'3': {'4': {'5': 'top'}}}}
    }
    assert get_tree_node(tree, '1:2:3:4:5') == 'top'
    assert get_tree_node(tree, '1:2:3') == {'4': {'5': 'top'}}
    assert get_tree_node(tree, '1:2:3', parent=True) == {'3': {'4': {'5': 'top'}}}
    assert get_tree_node(tree, '1:2:3:4:5:6', 'default') == 'default'



# Generated at 2022-06-14 06:48:40.738487
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, "a.b", 1)
    set_tree_node(tree, "a.c", 2)
    set_tree_node(tree, "a.a", 3)
    set_tree_node(tree["a"], "d", 4)
    set_tree_node(tree["a"]["e"], "f", 5)
    set_tree_node(tree, "a.e.g", 6)

    assert tree["a"]["b"] == 1
    assert tree["a"]["c"] == 2
    assert tree["a"]["a"] == 3
    assert tree["a"]["d"] == 4
    assert tree["a"]["e"]["f"] == 5
    assert tree["a"]["e"]["g"] == 6



# Generated at 2022-06-14 06:48:43.610081
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node(tree(), 'world:hello', 'world') == {'world': {'hello': 'world'}}



# Generated at 2022-06-14 06:48:49.610476
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Run the unit test.
    """
    config = {
        'a': {
            'b': {
                'c': "Hi there."
            }
        }
    }

    result = get_tree_node(config, 'a:b:c')
    assert result == 'Hi there.'



# Generated at 2022-06-14 06:49:06.124880
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'alpha': {
            'level_one': {
                'level_two': {
                    'level_three': {
                        'level_four': 'level_four'
                    }
                }
            }
        },
        'beta': {
            'level_one': 'level_one',
        }
    }
    # Test correct parsing of parents
    assert get_tree_node(data, 'alpha:level_one:level_two:level_three:level_four') == 'level_four'

    # Test correct parsing of root-level key

# Generated at 2022-06-14 06:49:14.750915
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'key1': 1,
        'key2': {
            'key1': 1,
            'key2': {
                'key1': 1,
                'key2': 2
            }
        }
    }

    assert get_tree_node(mapping, 'key1') == 1
    assert get_tree_node(mapping, 'key2:key1') == 1
    assert get_tree_node(mapping, 'key2:key2:key2') == 2
    try:
        get_tree_node(mapping, 'key1:key1')
    except KeyError:
        pass
    else:
        assert False



# Generated at 2022-06-14 06:49:22.685779
# Unit test for function get_tree_node
def test_get_tree_node():
    # Setup
    mapping = {'a': {'b': {'c': 0}}}

    # Execute + Verify
    assert get_tree_node(mapping, 'a:b:c') == 0
    assert get_tree_node(mapping, 'a:b:d') is _sentinel
    assert get_tree_node(mapping, 'a:b:d', 'test') == 'test'
    assert get_tree_node(mapping, 'a:b', parent=True) == {'c': 0}



# Generated at 2022-06-14 06:49:32.344344
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for :meth:`get_tree_node`
    """
    assert get_tree_node({
        'foo': {
            'bar': {
                'baz': 'baz',
                'spaz': 'spaz',
            }
        }
    }, 'foo:bar:baz') == 'baz'
    assert get_tree_node({
        'foo': {
            'bar': {
                'baz': 'baz',
                'spaz': 'spaz',
            }
        }
    }, 'foo:bar:spaz') == 'spaz'

# Generated at 2022-06-14 06:49:41.818454
# Unit test for function get_tree_node
def test_get_tree_node():
    import pdb; pdb.set_trace()
    data = {
        'hello': 'world',
        'this': {'is': {'good': 'value'}},
        'another': 'value',
        'he': None
    }
    assert get_tree_node(data, 'hello') == 'world'
    assert get_tree_node(data, 'this:is:good') == 'value'
    assert get_tree_node(data, 'this:is', default='not found') == {'good': 'value'}
    assert get_tree_node(data, 'this:is:good:si', default='not found') == 'not found'
    assert get_tree_node(data, 'he') is None



# Generated at 2022-06-14 06:49:44.904040
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = Tree()
    test_data['a:b:c'] = 'd'
    assert test_data['a:b:c'] == 'd'

# Generated at 2022-06-14 06:49:49.496778
# Unit test for function set_tree_node
def test_set_tree_node():
    t = {}
    set_tree_node(t, 'test:test2:var', 3)
    if not get_tree_node(t, 'test:test2:var') == 3:
        raise Exception('set_tree_node test failed')



# Generated at 2022-06-14 06:50:01.585099
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {'one': {'two': 'three'}}
    assert get_tree_node(test_data, 'one:two:three') is None
    assert get_tree_node(test_data, 'one:two') == 'three'
    test_data['one']['four'] = dict(five=dict(six='seven'))
    assert get_tree_node(test_data, 'one:four:five') == dict(six='seven')
    assert get_tree_node(test_data, 'one:four:five:six') == 'seven'
    assert get_tree_node(test_data, 'one:four:five:seven', default={}) == {}

# Generated at 2022-06-14 06:50:13.578428
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test behaviour of `set_tree_node`"""
    import pytest

    x = collections.defaultdict(dict)
    out = set_tree_node(x, 'test:test2:test2', 'hi')
    assert out == {'test2': 'hi'}
    assert x['test']['test2'] == 'hi'

    x = collections.defaultdict(dict)
    with pytest.raises(AttributeError):
        out = set_tree_node(x, 'test:test2:test2', 'hi')

    x = {}
    out = set_tree_node(x, 'test:test2:test2', 'hi')
    assert out == 'hi'
    assert x['test']['test2'] == 'hi'



# Generated at 2022-06-14 06:50:24.978844
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Get arbitrary node from arbitrary tree structure with arbitrary path via ':' notation.
    """
    tree_ = {
        'foo': {
            'baz': 'val'
        }
    }

    # Normal use, set arbitrary node
    set_tree_node(tree_, 'foo:bar', 'test')
    assert tree_['foo']['bar'] == 'test'

    # Set root node
    set_tree_node(tree_, 'root', 'val')
    assert tree_['root'] == 'val'

    # Create arbitrary depth of new branch
    set_tree_node(tree_, 'foo:bar:baz:baz:baz', 'val')



# Generated at 2022-06-14 06:50:32.540369
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }

    # Fetch simple value
    assert get_tree_node(mapping, 'foo:bar') == 'baz'

    # Fetch deep value
    assert get_tree_node(mapping, 'foo:bar:baz') is _sentinel

    # Fetch non existing value
    assert get_tree_node(mapping, 'missing') is _sentinel



# Generated at 2022-06-14 06:50:43.779899
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a':
        {
            'b':
            {
                'c': 'd'
            }
        }
    }
    assert get_tree_node(tree, 'a:b:c') == 'd'
    assert get_tree_node(tree, 'a:b:d') is _sentinel
    with pytest.raises(KeyError):
        get_tree_node(tree, 'a:b:d')
    assert get_tree_node(tree, 'a:b:d', default='e') == 'e'
    assert get_tree_node(tree, 'a:b', parent=True) == {'c': 'd'}



# Generated at 2022-06-14 06:50:53.449471
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'project': {
            'name': 'SuperCrazyCoolProject',
            'version': '1.1.1'
        },
        'info': {
            'docs': 'https://github.com/kordless/crazycoolproject'
        },
        'items': {
            'fruits': ['apple', 'banana', 'durian'],
            'animals': ['cat', 'dog', 'frog']
        }
    }
    assert (get_tree_node(tree, 'project:name') == 'SuperCrazyCoolProject')
    assert (get_tree_node(tree, 'items:fruits:0') == 'apple')
    assert (get_tree_node(tree, 'items:animals:1') == 'dog')


# Generated at 2022-06-14 06:51:00.975527
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(mapping, 'a:b') == {'c': 'd'}
    assert get_tree_node(mapping, 'a:b:c') == 'd'
    assert get_tree_node(mapping, 'a:b:c:', default=False) is False
    assert get_tree_node(mapping, 'a:b:c:') == _sentinel



# Generated at 2022-06-14 06:51:12.817994
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node"""
    root = tree()
    root[':foo'][':foo'][':bar'] = 'baz'
    assert get_tree_node(root, ':foo:foo:bar') == 'baz'
    assert get_tree_node(root, ':foo:foo:bar', default='baz') == 'baz'
    assert get_tree_node(root, ':not:here:bar') == _sentinel
    assert get_tree_node(root, ':not:here:bar', default='baz') == 'baz'
    assert get_tree_node(root, ':foo:foo:bar', parent=True)['bar'] == 'baz'

# Generated at 2022-06-14 06:51:25.070096
# Unit test for function get_tree_node
def test_get_tree_node():
    mytree = {
        'a': {
            'b': {
                'c': 123,
            },
        },
    }
    assert get_tree_node(mytree, 'a:b:c') == 123
    assert get_tree_node(mytree, 'a:b:d') is _sentinel
    assert get_tree_node(mytree, 'a:b:d', default=234) == 234
    assert get_tree_node(mytree, 'a:b:d', parent=True) == {'c': 123}
    assert get_tree_node(mytree, 'a:b:d', default=234, parent=True) == {'c': 123}
    assert get_tree_node(mytree, 'a:b:c:d', parent=True) == {'c': 123}


# Generated at 2022-06-14 06:51:37.777363
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'root': {
            'child1': 'child1-value',
            'child2': 'child2-value',
            'child3': {
                'child3.1': {
                    'child3.1.1': 'child3.1.1-value'
                }
            }
        }
    }
    # Check if 3 nodes exist
    assert get_tree_node(mapping, 'root:child1') == 'child1-value'
    assert get_tree_node(mapping, 'root:child2') == 'child2-value'
    assert get_tree_node(mapping, 'root:child3:child3.1:child3.1.1') == 'child3.1.1-value'
    # Check if parent node of one of them exists
    assert get_tree

# Generated at 2022-06-14 06:51:50.307758
# Unit test for function set_tree_node
def test_set_tree_node():
    assert set_tree_node({}, 'foo:bar', 34) == {'foo': {'bar': 34}}
    assert set_tree_node({'foo': {'bar': 4}}, 'foo:bar', 34) == {'foo': {'bar': 34}}
    assert set_tree_node({'foo': {'bar': 4}}, 'foo:baz', 34) == {'foo': {'bar': 4, 'baz': 34}}
    assert set_tree_node({'foo': {'bar': 4}}, 'foo:baz:baz', 34) == {'foo': {'bar': 4, 'baz': {'baz': 34}}}

# Generated at 2022-06-14 06:52:00.157165
# Unit test for function set_tree_node
def test_set_tree_node():

    a = {}
    b = set_tree_node(a, 'a', 1)
    assert a == {'a': 1}, 'One level nesting failed'

    b = set_tree_node(a, 'a:b', 2)
    assert a == {'a': {'b': 2}}, 'Two level nesting failed'

    b = set_tree_node(a, 'a:b:c', 3)
    assert a == {'a': {'b': {'c': 3}}}, 'Three level nesting failed'



# Generated at 2022-06-14 06:52:07.801869
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    for x in range(10):
        for y in range(10):
            mapping[x][y] = '%s:%s' % (x, y)

    assert get_tree_node(mapping, '8:8') == '8:8'
    assert get_tree_node(mapping, '8:8', default='nope') == '8:8'
    assert get_tree_node(mapping, '8:8', default='nope', parent=True) == {8: '8:8'}
    assert get_tree_node(mapping, '8:8', parent=True) == {8: '8:8'}


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:52:35.856438
# Unit test for function get_tree_node
def test_get_tree_node():
    m = {
        'base': {
            'a': {
                'b': {
                    'c': 'hello',
                }
            }
        },
        'parent': {
            'node': {
                'child': 'world',
            }
        }
    }

    assert get_tree_node(m, 'base:a:b:c') == 'hello'
    assert get_tree_node(m, 'parent:node:child') == 'world'

    # With parent node
    assert get_tree_node(m, 'parent:node:child', parent=True) == {
        'child': 'world',
    }

    # With default value
    assert get_tree_node(m, 'parent:non-existent', default='default') == 'default'

    # With default value as sentinel

# Generated at 2022-06-14 06:52:48.141318
# Unit test for function get_tree_node
def test_get_tree_node():
    """First, let's set up a tree"""
    tree = Tree({'foo': {'bar': {'baz': 'qux'}}})
    assert tree['foo:bar:baz'] == 'qux'
    assert tree['foo', 'bar', 'baz'] == 'qux'

    tree = Tree({'foo': {'bar': {'baz': {'qux': 'quux'}}}})

    # Get a leaf node
    assert tree['foo:bar:baz:qux'] == 'quux'
    assert tree['foo:bar:baz', 'qux'] == 'quux'

    # Get a parent node

# Generated at 2022-06-14 06:53:01.171670
# Unit test for function get_tree_node
def test_get_tree_node():
    # Tree to test against
    t = {
        'a': {
            'b': 'b',
            'c': {
                'd': 'd',
                'e': [
                    'e1',
                    'e2',
                    {
                        'f': 'f',
                        'g': 'g',
                    }
                ],
            },
            'a': {
                'h': 'h',
            }
        }
    }

    # Test simple traversal
    assert get_tree_node(t, 'a:c:d') == 'd'

    # Test traversal with indexing
    assert get_tree_node(t, 'a:c:e:1') == 'e2'

    # Test traversal with more indexing
    assert get_tree_node(t, 'a:a:h')

# Generated at 2022-06-14 06:53:06.606097
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'baz'
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:bar:baz') == _sentinel
    assert get_tree_node(mapping, 'foo:bar:baz', default=None) is None



# Generated at 2022-06-14 06:53:18.598323
# Unit test for function get_tree_node
def test_get_tree_node():
    data = dict(foo=dict(bar=dict(baz=1, quux=2)), corge=3, grault=('garply', 4))
    assert get_tree_node(data, 'foo:bar') == dict(baz=1, quux=2)
    assert get_tree_node(data, 'foo:bar:baz') == 1
    assert get_tree_node(data, 'corge') == 3
    assert get_tree_node(data, 'grault') == 'garply'
    assert get_tree_node(data, 'garply') == 4
    assert get_tree_node(data, 'foo:bar:baz', parent=True) == dict(baz=1, quux=2)
    assert get_tree_node(data, 'corge', default=None) == 3


# Generated at 2022-06-14 06:53:23.520827
# Unit test for function set_tree_node
def test_set_tree_node():
    a_dict = {}
    set_tree_node(a_dict, 'foo:bar:baz', 'value')
    assert a_dict == {
        'foo': {
            'bar': {
                'baz': 'value',
            }
        }
    }

# Generated at 2022-06-14 06:53:36.484039
# Unit test for function set_tree_node
def test_set_tree_node():
    test_struct = {}
    assert set_tree_node(test_struct, 'test:test2', 'blah') == test_struct['test']
    assert test_struct['test']['test2'] == 'blah'
    assert set_tree_node(test_struct, 'test:test3', 916) == test_struct['test']
    assert test_struct['test']['test3'] == 916
    assert set_tree_node(test_struct, 'test2:test3', 'bloo') == test_struct['test2']
    assert test_struct['test2']['test3'] == 'bloo'

# Generated at 2022-06-14 06:53:46.191189
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'data': {'a': {'b': {'c': 'd'}}}}, 'data:a:b:c') == 'd'
    with pytest.raises(KeyError):
        get_tree_node({'data': {'a': {'b': {'c': 'd'}}}}, 'data:a:b:e')
    assert get_tree_node({'data': {'a': {'b': {'c': 'd'}}}}, 'data:a:b:e', default='e') == 'e'



# Generated at 2022-06-14 06:53:56.372821
# Unit test for function get_tree_node
def test_get_tree_node():
    # setup
    test_dict = {
        'layer1': {
            'layer2a': {
                'result': 'thing1'
            },
            'layer2b': {
                'result': 'thing2'
            }
        }
    }

    def test(key, expected_result, default=_sentinel):
        result = get_tree_node(test_dict, key, default=default)
        assert result == expected_result, \
            'Expected %s, got %s'\
            % (expected_result, result)

    test('layer1:layer2a:result', 'thing1')
    test('layer1:layer2b:result', 'thing2')
    test('layer1:layer2c:result', _sentinel)

# Generated at 2022-06-14 06:54:05.404003
# Unit test for function set_tree_node
def test_set_tree_node():
    a = {}
    set_tree_node(a, 'a:b:c', 1)
    assert a['a']['b']['c'] == 1
    set_tree_node(a, 'e:f:g', 2)
    assert a['e']['f']['g'] == 2

    # Test that if the tree doesn't exist, it will be created
    set_tree_node(a, 'i:j:k', 3)
    assert a['i']['j']['k'] == 3

    # Test that if the tree does exist, it will be modified
    set_tree_node(a, 'i:l:m', 3)
    assert a['i']['l']['m'] == 3

    # Test that it returns the parent node

# Generated at 2022-06-14 06:54:32.056049
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': {
                    'd': 'e'
                }
            }
        }
    }
    assert get_tree_node(tree, 'a:b:c:d') == 'e'
    assert get_tree_node(tree, 'a:b:c:e') == _sentinel
    try:
        get_tree_node(tree, 'a:b:c:e')
    except KeyError:
        pass



# Generated at 2022-06-14 06:54:40.130964
# Unit test for function set_tree_node
def test_set_tree_node():
    # KeyError
    with pytest.raises(KeyError):
        node = set_tree_node({}, 'foo')

    assert set_tree_node({}, 'foo:bar:baz', 17) == {'foo': {'bar': {'baz': 17}}}
    assert set_tree_node({'foo': {'bar': {}}}, 'foo:bar:baz', 17) == {'foo': {'bar': {'baz': 17}}}



# Generated at 2022-06-14 06:54:44.133780
# Unit test for function set_tree_node
def test_set_tree_node():
    tree = {}
    set_tree_node(tree, 'a:b:c', True)
    foo = tree['a']['b']['c']
    assert foo is True



# Generated at 2022-06-14 06:54:55.391191
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function get_tree_node."""
    def dict_tree_node(key):
        return get_tree_node(tree_dict, key)

    tree_dict = {
        'a': {
            'b': {
                'c': True,
                'd': {'e': {'f': {'g': {'h': True}}}}
            },
            'c': {
                'b': {
                    'a': True
                }
            }
        }
    }
    assert dict_tree_node('a')['b'] == {'c': True, 'd': {'e': {'f': {'g': {'h': True}}}}}
    assert dict_tree_node('a:b:d:e:f:g:h') is True

# Generated at 2022-06-14 06:55:08.041494
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {
        'a': {
            'b': 'b',
            'c': {
                'b': 'cb',
            },
        },
        'd': 'd',
        'e': {
            'f': {
                'g': 'g',
            },
        },
    }
    # Normal access
    assert data['a']['b'] == get_tree_node(data, 'a:b')
    assert data['a']['c']['b'] == get_tree_node(data, 'a:c:b')
    assert data['e']['f']['g'] == get_tree_node(data, 'e:f:g')
    # Default value
    assert 'default' == get_tree_node(data, 'a:c:c', 'default')
   

# Generated at 2022-06-14 06:55:15.109770
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test for get_tree_node function."""
    assert get_tree_node({'x': {'y': 'z'}}, 'x:y') == 'z'
    assert get_tree_node({'x': {'y': 'z'}}, 'y') == _sentinel
    assert get_tree_node({'x': {'y': 'z'}}, 'y', default=None) is None



# Generated at 2022-06-14 06:55:25.894258
# Unit test for function set_tree_node
def test_set_tree_node():
    config = {}
    set_tree_node(config, 'foobar', 42)
    assert config == {'foobar': 42}

    config = {}
    set_tree_node(config, 'foobar:baz', [1, 2, 3])
    assert config == {'foobar': {'baz': [1, 2, 3]}}

    config = {}
    set_tree_node(config, 'foobar:baz:a', 'a')
    assert config == {'foobar': {'baz': {'a': 'a'}}}

    config = {}
    set_tree_node(config, 'foobar:baz:a:b:c:d:e:f:g', 'baz')

# Generated at 2022-06-14 06:55:35.052311
# Unit test for function set_tree_node
def test_set_tree_node():
    original = {}
    mapping = original
    key = 'test'
    value = 'value'
    expected = {'test': 'value'}
    set_tree_node(mapping, key, value)
    assert original == expected, "Expected %s, got %s" % (expected, original)

    key = 'test:test2'
    expected = {'test': {'test2': 'value'}}
    set_tree_node(mapping, key, value)
    assert original == expected, "Expected %s, got %s" % (expected, original)

# Generated at 2022-06-14 06:55:40.685952
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': {
                'baz': 'bazzle',
            }
        }
    }

    assert get_tree_node(mapping, 'foo:bar:baz') == 'bazzle'


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v', '-s'])

# Generated at 2022-06-14 06:55:46.331059
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test get_tree_node, allowing for : notation."""
    tree_ = {
        'a': {
            'b': {
                'c': 'd',
            },
        },
    }

    assert get_tree_node(tree_, 'a:b:c') == 'd'
    assert get_tree_node(tree_, 'a:b:c', default=1) == 'd'
    assert get_tree_node(tree_, 'a:b:d', default=1) == 1
    assert get_tree_node(tree_, 'a:b:c:d:e') is _sentinel

