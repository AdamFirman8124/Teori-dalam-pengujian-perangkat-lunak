

# Generated at 2022-06-14 06:46:14.713553
# Unit test for function set_tree_node
def test_set_tree_node():
    # Arrange
    tree = {}

    # Act
    set_tree_node(tree, 'a:b:c:d:e:f:g:h:i', 'TEST')

    # Assert
    assert tree['a']['b']['c']['d']['e']['f']['g']['h']['i'] == 'TEST'



# Generated at 2022-06-14 06:46:27.751861
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'a': {
            'b': {
                'e': 'f',
                'g': {
                    'h': 'i',
                    'j': 'k'
                }
            },
        },
        'l': {
            'm': 'n'
        }
    }
    assert get_tree_node(d, 'a:b:e') == 'f'
    assert get_tree_node(d, 'a:b:g:j') == 'k'
    assert get_tree_node(d, 'l:m') == 'n'
    # Default
    assert get_tree_node(d, 'l:a:b:c:d', default='x') == 'x'

# Generated at 2022-06-14 06:46:37.501090
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    This is just a function that unit-tests for :func:`get_tree_node` function.
    """
    mapping = {
        'a': {
            'b': {
                'c': {
                    'd': 'e'
                },
                'f': 'g'
            }
        }
    }

    assert get_tree_node(mapping, 'a:b:c:d') == 'e'
    assert get_tree_node(mapping, 'a:b:f') == 'g'
    assert get_tree_node(mapping, 'a:b:c:d', parent=True) == {'d': 'e'}
    assert get_tree_node(mapping, 'a:b:c:d', default='h') == 'e'
    assert get_tree_node

# Generated at 2022-06-14 06:46:45.543963
# Unit test for function set_tree_node
def test_set_tree_node():
    mydict = {}
    set_tree_node(mydict, "key", "val")
    assert mydict['key'] == 'val'
    set_tree_node(mydict, "key2:key", "val")
    assert mydict['key2']['key'] == 'val'
    set_tree_node(mydict, "key3:key:key", "val")
    assert mydict['key3']['key']['key'] == 'val'
    set_tree_node(mydict, ":key", "val")
    assert mydict['key'] == 'val'



# Generated at 2022-06-14 06:46:56.434560
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test
    TESTS = [
        # Tree, Key, Default, Result
        ({}, 'foo', None, KeyError),
        ({}, ':foo:bar', None, KeyError),
        ({'foo': {'bar': 'baz'}}, ':foo:bar', None, 'baz'),
        ({'foo': {'bar': 'baz'}}, 'foo:bar', None, 'baz'),
        ({'foo': {'bar': 'baz'}}, 'foo:bar', 'qux', 'baz'),
        ({'foo': {'bar': 'baz'}}, 'foo:baz', 'qux', 'qux'),
    ]


# Generated at 2022-06-14 06:47:02.954777
# Unit test for function set_tree_node
def test_set_tree_node():
    """Test basic functionality of set_tree_node, which is used by :class:`Tree` and :class:`RegistryTree`."""
    d = {}
    set_tree_node(d, 'a:b:c:d:e', "something")
    assert d['a']['b']['c']['d']['e'] == "something"



# Generated at 2022-06-14 06:47:11.591350
# Unit test for function set_tree_node
def test_set_tree_node():
    test_mapping = {
        'test_key': {
            'test_sub': {
                'test_subsub': 'test_value'
            }
        }
    }
    test_set_node = set_tree_node(test_mapping, 'test_key:test_sub:test_subsub', 'value_should_be_this')
    return test_mapping['test_key']['test_sub']['test_subsub'] == test_set_node == 'value_should_be_this'



# Generated at 2022-06-14 06:47:23.004346
# Unit test for function get_tree_node
def test_get_tree_node():
    from nose.tools import eq_
    from itertools import izip

    tree = {
        'foo': {
            'bar': 'FooBar'
        },
        'bar': {
            'foo': 'BarFoo',
            'frob': 'Frobulous'
        }
    }

    # Test case: Retrieve nested node
    eq_(get_tree_node(tree, 'foo:bar'), 'FooBar')

    # Test case: Parent requested
    eq_(get_tree_node(tree, 'bar:foo', parent=True), tree['bar'])

    # Test case: Return default on KeyError
    eq_(get_tree_node(tree, 'bar:bar', default='baz'), 'baz')

    # Test case: Raise KeyError

# Generated at 2022-06-14 06:47:35.289981
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'db': {
            'port': '5432'
        },
        'paths': {
            'user': '~/tmp',
            'worker': '/tmp'
        }
    }

    assert get_tree_node(mapping, 'db:port') == '5432'
    assert get_tree_node(mapping, 'paths:user') == '~/tmp'
    assert get_tree_node(mapping, 'paths:worker') == '/tmp'
    assert get_tree_node(mapping, 'nosuchpath', default='') == ''

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'nosuchpath')



# Generated at 2022-06-14 06:47:47.989452
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test data
    test_data = {
        'a': {
            'b': {
                'c': 1,
                'd': 2,
            },
            'e': {
                'f': 3,
            },
        },
    }
    # Test that it works
    assert get_tree_node(test_data, 'a') == {'b': {'c': 1, 'd': 2}, 'e': {'f': 3}}
    assert get_tree_node(test_data, 'a:b') == {'c': 1, 'd': 2}
    assert get_tree_node(test_data, 'a:b:c') == 1
    assert get_tree_node(test_data, 'a:b:d') == 2

# Generated at 2022-06-14 06:47:57.150741
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping, 'foo:bar:baz', 'bingo')
    assert get_tree_node(mapping, 'foo') == {'bar': {'baz': 'bingo'}}



# Generated at 2022-06-14 06:48:02.252324
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    assert set_tree_node(t, 'a:b:c', 1) == {'b': {'c': 1}}
    assert set_tree_node(t, 'a:b:c', 2) == {'b': {'c': 2}}



# Generated at 2022-06-14 06:48:10.170026
# Unit test for function get_tree_node
def test_get_tree_node():
    """Unit test for function `get_tree_node`."""
    data = {'python': {'flask': {'views': 'views.py'}}}
    assert (get_tree_node(data,
                          'python',
                          default=_sentinel) == {'flask': {'views': 'views.py'}})  # No exception thrown
    assert (get_tree_node(data,
                          'python:flask',
                          default=_sentinel) == {'views': 'views.py'})  # No exception thrown
    assert (get_tree_node(data,
                          'python:flask:views',
                          default=_sentinel) == 'views.py')  # No exception thrown, get latest node

# Generated at 2022-06-14 06:48:22.303917
# Unit test for function get_tree_node
def test_get_tree_node():
    from unittest import TestCase # noqa

    class TestGetTreeNode(TestCase):
        """Test for get_tree_node."""

        def test_value(self):
            """Test for get_tree_node returning a value."""
            mydict = {
                'a': 'b',
                'b': {
                    'c': 'd'
                },
                'c': {
                    'd': {
                        'e': 'f'
                    }
                }
            }
            result = get_tree_node(mydict, 'a')
            self.assertEqual(result, 'b')

        def test_default(self):
            """Test for fallback default value."""
            mydict = {'a': 'b'}

# Generated at 2022-06-14 06:48:32.425770
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree(), 'foo:bar') == tree()['foo']['bar']
    assert get_tree_node(tree(), 'foo:bar') == get_tree_node(tree(), 'foo', parent=True)['bar']

    try:
        get_tree_node(tree(), 'foo:bar')
    except KeyError:
        assert True
    else:
        assert False

    try:
        get_tree_node(tree(), 'foo:bar', default=None)
    except KeyError:
        assert False
    else:
        assert True



# Generated at 2022-06-14 06:48:42.163215
# Unit test for function get_tree_node
def test_get_tree_node():
    data = {'one': {'two': {'three': 'This is the value'}}}
    assert get_tree_node(data, 'one') == \
        {'two': {'three': 'This is the value'}}
    assert get_tree_node(data, 'one:two') == \
        {'three': 'This is the value'}
    assert get_tree_node(data, 'one:two:three') == \
        'This is the value'
    assert get_tree_node(data, 'one:two:three:four') == \
        _sentinel
    assert get_tree_node(data, 'one:two:three:four', 'I lied') == \
        'I lied'



# Generated at 2022-06-14 06:48:50.625500
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(mapping, 'a:b:c') == 'd'

    with pytest.raises(KeyError):
        get_tree_node(mapping, 'not there')

    assert get_tree_node(mapping, 'not there', default=None) is None

    assert get_tree_node(mapping, 'not there', default=None, parent=True) is None



# Generated at 2022-06-14 06:48:57.152130
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'foo': {
            'bar': 'value!',
            'baz': {
                'key': 'value!'
            }
        }
    }
    assert get_tree_node(mapping, 'foo:bar') == 'value!'
    assert get_tree_node(mapping, 'foo:baz') == {'key': 'value!'}
    assert get_tree_node(mapping, 'foo:baz:key') == 'value!'
    assert get_tree_node(mapping, 'no:key') is _sentinel
    assert get_tree_node(mapping, 'no:key', default='no value') == 'no value'



# Generated at 2022-06-14 06:49:01.953386
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = tree()
    set_tree_node(mapping['foo'], 'bar:baz', 'quix')
    assert mapping['foo']['bar']['baz'] == 'quix'



# Generated at 2022-06-14 06:49:06.218399
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = {}
    set_tree_node(test_dict, 'a:b:c:d', 'test')
    test_dict['a']['b']['c']['d'] == 'test'



# Generated at 2022-06-14 06:49:25.605213
# Unit test for function get_tree_node
def test_get_tree_node():
    root = RegistryTree({
        'level_one': {
            'level_two': {
                'level_three': 'yay'
            },
        },
    })
    assert root.get('level_one:level_two:level_three') == 'yay'
    assert root.get('level_one:level_two:level_three:level_four:bad') is _sentinel



# Generated at 2022-06-14 06:49:28.422381
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    assert set_tree_node(t, 'a:b:c', 'foo')['a']['b']['c'] == 'foo'



# Generated at 2022-06-14 06:49:35.462282
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'node': 'value'}, 'node') == 'value'
    assert get_tree_node({'node': {'node': 'value'}}, 'node:node') == 'value'
    assert get_tree_node({'node': {'node': {'node': 'value'}}}, 'node:node:node') == 'value'



# Generated at 2022-06-14 06:49:41.670014
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Create a registry tree
    """
    registry = Tree()
    registry['this:that'] = 'something'
    assert registry['this:that'] == 'something'
    assert registry['this'] == {'that': 'something'}
    assert registry['this']['that'] == 'something'
    assert registry['this:that'] == registry['this']['that']

    # In case you're wondering, we can set it without traversing the tree
    # This will not create nested mappings, though, so it has its limits
    registry['this:that:theother'] = 'bananas'
    assert registry['this:that'] == 'something'
    assert registry['this:that:theother'] == 'bananas'



# Generated at 2022-06-14 06:49:47.302454
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {
        'foo': {
            'bar': {
                'baz': 42
            }
        }
    }

    assert get_tree_node(d, 'foo:bar:baz') == 42
    assert get_tree_node(d, 'no_such_key', default=None) is None



# Generated at 2022-06-14 06:49:51.155434
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'test:test:test', True)
    assert mapping['test']['test']['test'] is True



# Generated at 2022-06-14 06:49:56.761221
# Unit test for function get_tree_node
def test_get_tree_node():
    node = {
        'manager': {
            'user': 'J. Doe',
            'department': 'Department Name',
            'tel': '072-00-100'
        }
    }
    assert get_tree_node(node, 'manager:user') == 'J. Doe'



# Generated at 2022-06-14 06:50:10.291279
# Unit test for function get_tree_node
def test_get_tree_node():
    import pytest
    _tree = {
        'foobar': {
            'baz': "brew",

        }
    }
    assert get_tree_node(_tree, '') == _tree
    assert get_tree_node(_tree, 'foobar') == {'baz': "brew"}
    assert get_tree_node(_tree, 'foobar:baz') == "brew"
    with pytest.raises(KeyError):
        get_tree_node(_tree, 'dumb')
    assert get_tree_node(_tree, 'dumb', default=None) is None
    assert get_tree_node(_tree, 'foobar:baz', parent=True) == {'baz': "brew"}
    assert get_tree_node(_tree, 'foobar:baz', parent=True) is not _tree

# Generated at 2022-06-14 06:50:19.795764
# Unit test for function get_tree_node
def test_get_tree_node():
    test_mappings = [
        (tree(), 'foo:bar', 'cows'),
        (dict(), 'foo:bar', 'cows'),
        (RegistryTree(), 'foo:bar', 'cows'),
    ]

    for mapping, key, value in test_mappings:
        mapping['']['foo']['bar'] = 'cows'

        # Test fetching with delimiter
        assert get_tree_node(mapping, key) == value

        # Test fetching without delimiter
        assert get_tree_node(mapping, 'foo:bar') == value

        # Test fetching with different delimiters
        assert get_tree_node(mapping, 'foo::bar', delimiter='::') == value

        # Test fetching with default

# Generated at 2022-06-14 06:50:30.020621
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {'a': {'b': {'c': 'd'}}}
    assert get_tree_node(t, 'a:b:c') == 'd'
    assert get_tree_node(t, 'a:b:c:d', parent=True) == {'c': 'd'}
    assert get_tree_node(t, 'a:b') == {'c': 'd'}
    assert get_tree_node(t, 'a:b', default='not found') == {'c': 'd'}



# Generated at 2022-06-14 06:50:58.333320
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test basic traversal
    mapping = {
        'key': {
            'subkey': 'subvalue',
        },
    }
    result = get_tree_node(mapping, 'key:subkey')
    assert result == 'subvalue'

    # Test that KeyError is raised when key does not exist
    mapping = {
        'key': {},
    }
    with pytest.raises(KeyError):
        result = get_tree_node(mapping, 'key:subkey')

    # Test that KeyError is raised when key does not exist, but return default instead
    mapping = {
        'key': {},
    }
    result = get_tree_node(mapping, 'key:subkey', default='default')
    assert result == 'default'

# Generated at 2022-06-14 06:51:10.157722
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    set_tree_node(mapping, 'a.b.c', 'ABC')
    assert mapping == {'a': {'b': {'c': 'ABC'}, }}, "Tree node set correctly %s" % mapping
    # Set tree node to an existing node
    set_tree_node(mapping, 'a.b.c', 'ABC2')
    assert mapping['a']['b']['c'] == 'ABC2', "Tree node set correctly %s" % mapping
    # Set tree node to an existing node, part of traversal does not exist
    set_tree_node(mapping, 'a.b.c.d', 'ABCD')
    assert mapping['a']['b']['c'] == 'ABC2', "Tree node set correctly %s" % mapping

# Generated at 2022-06-14 06:51:20.658419
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = collections.defaultdict(dict)
    mapping[1]['sub']['subsub']['deepkey'] = 'DEEPKEY VALUE'
    assert get_tree_node(mapping, '1:sub:subsub:deepkey') == 'DEEPKEY VALUE'
    assert get_tree_node(mapping, '1:sub:subsub:deepkey', default='YERMOMMA') == 'DEEPKEY VALUE'
    assert get_tree_node(mapping, '1:sub:subsub:otherkey', default='YERMOMMA') == 'YERMOMMA'



# Generated at 2022-06-14 06:51:24.902921
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    :return:
    """
    tree = {
        'foo': {
            'bar': baz,
        }
    }

    assert get_tree_node(tree, 'foo:bar') is baz


# Unit test function set_tree_node

# Generated at 2022-06-14 06:51:37.597862
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test cases
    case_dict = {
        'a': {
            'b': {
                'c': 1,
                'd': 2,
                'e': {
                    'f': 3,
                    'g': 4,
                },
            },
            'h': 5,
        },
    }
    case_list = [
        'a:b:c',
        'a:b:d',
        'a:b:e:f',
        'a:b:e:g',
        'a:h',
    ]
    case_expected = [
        1,
        2,
        3,
        4,
        5,
    ]

    # Asserts
    for case_key, case_expect in zip(case_list, case_expected):
        assert get_tree_node

# Generated at 2022-06-14 06:51:42.819007
# Unit test for function set_tree_node
def test_set_tree_node():
    import unittest
    class TestSetTreeNode(unittest.TestCase):
        def test_set_tree_node(self):
            data = {}
            set_tree_node(data, 'a', 'b')
            self.assertEqual(data, {'a': 'b'})

    unittest.main()


# Generated at 2022-06-14 06:51:55.278747
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test for tree getter"""
    data = {
        'one': 1,
        'two': {
            'three': 3,
            'four': 4,
            'five': {
                'six': 6,
                'seven': 7,
                'eight': 8,
            },
        }
    }

    assert get_tree_node(data, 'one') == 1
    assert get_tree_node(data, 'two') == {
        'three': 3,
        'four': 4,
        'five': {
            'six': 6,
            'seven': 7,
            'eight': 8,
        },
    }
    assert get_tree_node(data, 'two:four') == 4
    assert get_tree_node(data, 'two:four:eight') is _sentinel
    assert get

# Generated at 2022-06-14 06:52:05.978000
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test for function :py:func:`get_tree_node`.
    """
    mapping = {
        'a': {'b': {'c': 0}},
        'd': {'e': {'f': 50}},
        'g': {'h': {'i': 100}}
    }

    assert get_tree_node(mapping, 'a:b:c') == 0
    assert get_tree_node(mapping, 'd:e:f') == 50
    assert get_tree_node(mapping, 'g:h:i') == 100

    assert get_tree_node(mapping, 'a:b:c', parent=True) == {'c': 0}

# Generated at 2022-06-14 06:52:15.457912
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {
        'foo': {
            'bar': 'baz'
        }
    }
    assert get_tree_node(t, 'foo:bar') == 'baz'
    assert get_tree_node(t, 'foo:bar:non-existent', 'default') == 'default'

    # Default is _sentinel (private object). Will raise KeyError.
    # with pytest.raises(KeyError):
    #     get_tree_node(t, 'foo:bar:non-existent')



# Generated at 2022-06-14 06:52:22.171875
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'foo': {
            'bar': {
                'a': 'A',
                'b': 'B',
            }
        },
        'spam': {
            'eggs': 'EGGS',
        },
    }

    assert get_tree_node(test_data, 'foo:bar:a') == 'A'  # Basic
    assert get_tree_node(test_data, 'spam:eggs') == 'EGGS'  # Basic 2
    assert get_tree_node(test_data, 'foo:bar:c') is None  # No Val
    assert get_tree_node(test_data, 'foo:bar:c', 'C') == 'C'  # Default

# Generated at 2022-06-14 06:53:04.313066
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    get_tree_node should:
        * allow for tree-like node access via :
        * return _sentinel when not found, unless default is set

        * if parent=True should return the parent node
    """
    mapping = {'a': {'b': {'c': 1}}}

    assert get_tree_node(mapping, 'a') is mapping['a']
    assert get_tree_node(mapping, 'a:b') is mapping['a']['b']
    assert get_tree_node(mapping, 'a:b:c') is mapping['a']['b']['c']

    assert get_tree_node(mapping, 'a:b:c:not:here') is _sentinel

# Generated at 2022-06-14 06:53:07.111046
# Unit test for function set_tree_node
def test_set_tree_node():
    data = {}
    set_tree_node(data, 'key', 'val')
    assert data == {'key': 'val'}



# Generated at 2022-06-14 06:53:11.056043
# Unit test for function set_tree_node
def test_set_tree_node():
    mapping = {}
    key = "level1:level2"
    value = Tree()
    set_tree_node(mapping, key, value)
    assert mapping == {'level1': {'level2': {}}}



# Generated at 2022-06-14 06:53:14.618106
# Unit test for function set_tree_node
def test_set_tree_node():
    test_tree = tree()
    assert set_tree_node(test_tree, 'one:two:three:four:five', 'test')['five'] == 'test'



# Generated at 2022-06-14 06:53:26.155071
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:53:29.752996
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = tree()
    test_dict = set_tree_node(test_dict, 'test:foo', 'bar')
    assert test_dict['test']['foo'] == 'bar'



# Generated at 2022-06-14 06:53:39.060140
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'a': {
            'b': {
                'c': 'd',
            },
        },
    }

    # Normal
    assert get_tree_node(tree, 'a:b:c') == 'd'

    # No matches
    assert get_tree_node(tree, 'a:b:c:d') is _sentinel
    try:
        get_tree_node(tree, 'a:b:c:d')
        assert False
    except KeyError:
        assert True

    # Default
    assert get_tree_node(tree, 'a:b:c:d', 'e') == 'e'



# Generated at 2022-06-14 06:53:49.002010
# Unit test for function get_tree_node
def test_get_tree_node():
    test_data = {
        'a': {
            'b': {
                'c': 'c'
            }
        }
    }

    assert get_tree_node(test_data, 'a:b:c') == 'c'
    assert get_tree_node(test_data, 'a:b:c:d:e:f:g') is _sentinel

    try:
        get_tree_node(test_data, 'a:b:c:d:e:f:g')
    except KeyError:
        pass
    else:
        raise Exception('Key error should have been raised')



# Generated at 2022-06-14 06:53:58.522285
# Unit test for function set_tree_node
def test_set_tree_node():
    # Set a empty dict
    mapping = {}
    set_tree_node(mapping, 'foo', 'bar')
    assert mapping == {'foo': 'bar'}
    # Set a new value
    set_tree_node(mapping, 'foo:baz', 'egg')
    assert mapping == {'foo': {'baz': 'egg'}}
    # Set an existing value
    set_tree_node(mapping, 'foo:baz', 'spam')
    assert mapping == {'foo': {'baz': 'spam'}}
    # Set an existing value to a new value
    set_tree_node(mapping, 'foo:baz', 'spam:egg')
    assert mapping == {'foo': {'baz': 'spam:egg'}}
    # Update an existing value to new value


# Generated at 2022-06-14 06:54:10.264828
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test for method to retrieve keys from nested mapping structures, allowing for : notation."""
    from nose.tools import assert_equal
    from nose.tools import assert_raises

    tree = {
        'a': {
            'b': {
                'c': {
                    'd': {
                        'e': 'eee',
                    },
                },
            },
        },
    }

    assert_equal(get_tree_node(tree, 'a:b:c:d:e'), 'eee')
    assert_equal(get_tree_node(tree, 'a:b:c:d:e', default=None), 'eee')

    assert_raises(KeyError, get_tree_node, tree, 'f:b:c:d:e')

# Generated at 2022-06-14 06:55:31.131581
# Unit test for function get_tree_node
def test_get_tree_node():
    tree_dict = {
        '1': {'11': '12'},
        '2': {'21': '22'}
    }
    assert get_tree_node(tree_dict, '1') == {'11': '12'}
    assert get_tree_node(tree_dict, '1:11', 'blah') == '12'
    assert get_tree_node(tree_dict, '2:21') == '22'
    assert get_tree_node(tree_dict, '1:11:12', 'blah') == 'blah'
    assert get_tree_node(tree_dict, '1:11:12', 'blah') == 'blah'
    assert get_tree_node(tree_dict, '1:11:12', 'blah') == 'blah'
    assert get

# Generated at 2022-06-14 06:55:42.000749
# Unit test for function get_tree_node
def test_get_tree_node():
    TREE = {
        'sessions': {
            'foo': {
                'bar': [
                    'baz'
                ],
                'quux': 1
            }
        }
    }

    assert get_tree_node(TREE, 'sessions:foo:bar:baz') == 'baz'
    assert get_tree_node(TREE, 'sessions:foo:bar') == ['baz']
    assert get_tree_node(TREE, 'sessions:foo:quux') == 1
    assert get_tree_node(TREE, 'baz', default=None) is None
    assert get_tree_node(TREE, 'baz') == KeyError()

# Generated at 2022-06-14 06:55:48.489194
# Unit test for function get_tree_node
def test_get_tree_node():
    """Tests for get_tree_node"""

    # Simple tree
    test_tree = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    # Assert deeper
    assert get_tree_node(test_tree, 'a:b:c') == 'd'

    # Assert shallow
    assert get_tree_node(test_tree, 'a') == {
        'b': {
            'c': 'd'
        }
    }

    # Assert missing key
    with pytest.raises(KeyError):
        assert get_tree_node(test_tree, 'a:b:z')

    # Assert missing key with default

# Generated at 2022-06-14 06:55:49.772724
# Unit test for function set_tree_node
def test_set_tree_node():
    pass



# Generated at 2022-06-14 06:55:58.798124
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'foo': 'bar'}, 'foo') == 'bar'
    assert get_tree_node({'foo': 'bar'}, 'foo:foo') is _sentinel
    assert get_tree_node({'foo': 'bar'}, 'foo:foo', default='baz') == 'baz'
    assert get_tree_node({'foo': 'bar'}, 'foo', default='baz') == 'bar'
    assert get_tree_node({'foo': {'foo': 'bar'}}, 'foo:foo') == 'bar'



# Generated at 2022-06-14 06:56:08.685277
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping['foo'] = {}
    mapping['foo']['bar'] = 'baz'
    assert get_tree_node(mapping, 'foo:bar', default='quux') == 'baz'
    assert get_tree_node(mapping, 'foo:bar', default='quux', parent=True) == {}
    assert get_tree_node(mapping, 'foo:baz') is _sentinel
    assert get_tree_node(mapping, 'foo:baz', default='quux') == 'quux'
    assert get_tree_node(mapping, 'faz:baz') is _sentinel
    assert get_tree_node(mapping, 'faz:baz', default='quux') == 'quux'