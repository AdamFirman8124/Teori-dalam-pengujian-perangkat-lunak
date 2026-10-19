

# Generated at 2022-06-14 06:46:16.576338
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test function used by test function below."""
    mapping = {
        'foo': {
            'bar': {
                'baz': 'qux',
            },
        },
    }
    assert get_tree_node(mapping, 'foo:bar:baz') == 'qux'

test_cases_get_tree_node = (
    ('foo:bar:baz', 'qux', {'foo': {'bar': {'baz': 'qux'}}}),
    ('friendly_name', 'qux', {'foo': {'bar': {'baz': 'qux'}, 'friendly_name': 'qux'}}),
    ('foo:bar', {'baz': 'qux'}, mapping),
)



# Generated at 2022-06-14 06:46:29.540355
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = collections.defaultdict(collections.defaultdict)
    test_tree['a']['b'] = 1
    assert get_tree_node(test_tree, 'a:b', None) == 1
    assert get_tree_node(test_tree, 'x:z', None) is None
    assert get_tree_node(test_tree, 'x:z') == {}
    assert get_tree_node(test_tree, 'a', None) == {'b': 1}
    with pytest.raises(KeyError):
        # NOTE: default = _sentinel, will raise KeyError
        get_tree_node(test_tree, 'x:z')

    # Test parent
    assert get_tree_node(test_tree, 'a:b', parent=True) == {'b': 1}
   

# Generated at 2022-06-14 06:46:37.148292
# Unit test for function get_tree_node

# Generated at 2022-06-14 06:46:45.726788
# Unit test for function set_tree_node
def test_set_tree_node():
    t = {}
    set_tree_node(t, 'a:b:c', 1)
    set_tree_node(t, 'a:b:d', 2)
    set_tree_node(t, 'a:b:x:y', 3)
    set_tree_node(t, 'i:j:k', 4)
    set_tree_node(t, 'i', 5)

    assert t == {
        'a': {
            'b': {
                'c': 1,
                'd': 2,
                'x': {
                    'y': 3,
                },
            },
        },
        'i': 5,
    }



# Generated at 2022-06-14 06:46:54.278827
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test defaults
    mapping = tree()
    assert get_tree_node(mapping, 'foo:bar:foo:bar:baz') is mapping['foo']['bar']['foo']['bar']['baz']
    assert get_tree_node(mapping, 'foo:bar:foo:bar:baz', default='foobar') == 'foobar'

    # Test default provided as _sentinel.
    with pytest.raises(KeyError):
        assert get_tree_node(mapping, 'foo:bar:foo:bar:baz', _sentinel)

# Generated at 2022-06-14 06:47:06.175597
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = Tree()
    tree['foo:bar:baz'] = 'bink'
    tree['asdf:asdf'] = 'fdsa'
    tree['lol'] = 'rofl'

    assert(get_tree_node(tree, 'lol') == 'rofl')
    assert(get_tree_node(tree, 'asdf:asdf') == 'fdsa')
    assert(get_tree_node(tree, 'foo:bar:baz') == 'bink')
    assert(get_tree_node(tree, 'foo:bar:boop') is _sentinel)
    assert(get_tree_node(tree, 'foo:bar:boop', default='default') == 'default')



# Generated at 2022-06-14 06:47:09.451059
# Unit test for function get_tree_node
def test_get_tree_node():
    data = tree()
    data['date']['year'] = 2016
    assert get_tree_node(data, 'date:year') == 2016



# Generated at 2022-06-14 06:47:22.380482
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test for :function:`get_tree_node`."""
    test_tree = {
        'a': {
            'b': {
                'c': 'd'
            },
            'f': {
                'g': 'h'
            }
        },
        'e': 'f'
    }

    assert get_tree_node(test_tree, 'a:b:c') == 'd'
    assert get_tree_node(test_tree, 'e') == 'f'
    assert get_tree_node(test_tree, 'a:f:g') == 'h'
    assert get_tree_node(test_tree, 'a:f:g', default='i') == 'h'
    assert get_tree_node(test_tree, 'a:d', default='i') == 'i'

# Generated at 2022-06-14 06:47:33.992663
# Unit test for function set_tree_node
def test_set_tree_node():
    from os import path
    from pyq import q

    # Store the location of a test file
    # The '/' is taken care of for us, because it's a string, which is mutable.
    ts_input_file_tree = {'input': {'ts_input_file': path.join(path.dirname(__file__), 'input', 'test_input.csv')}}
    ts_input_file_tree_namespaced = {'input': {'ts': {'input_file': path.join(path.dirname(__file__),
                                                                              'input', 'test_input.csv')}}}

# Generated at 2022-06-14 06:47:45.260302
# Unit test for function set_tree_node
def test_set_tree_node():
    try:
        set_tree_node({}, 'a', 1)
    except KeyError:
        pass
    else:
        raise AssertionError

    data = tree()
    data[0][0][0] = 1
    data[0][0][1] = 2
    data[0][1][0] = 3

    assert_equal(data, {0: {0: {0: 1, 1: 2}, 1: {0: 3}}})

    try:
        set_tree_node(data, {0}, 1)
    except TypeError:
        pass
    else:
        raise AssertionError



# Generated at 2022-06-14 06:47:56.229539
# Unit test for function set_tree_node
def test_set_tree_node():
    d = {}

    set_tree_node(d, 'a', 'foo')
    set_tree_node(d, 'a:b', 'bar')
    set_tree_node(d, 'a:c', 'baz')
    set_tree_node(d, 'a:b:d', 'dik')
    set_tree_node(d, 'a:b:c:d', 'dee')

    assert d['a'] == 'foo'
    assert d['a']['b'] == 'bar'
    assert d['a']['c'] == 'baz'
    assert d['a']['b']['c'] == {}
    assert d['a']['b']['c']['d'] == 'dee'



# Generated at 2022-06-14 06:48:01.765979
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'a': {'b': {'d': 0, 'c': 3}}}
    assert get_tree_node(mapping, 'a:b:c') == 3
    assert get_tree_node(mapping, 'a:b:d') == 0
    # TODO test default
    # TODO test parent



# Generated at 2022-06-14 06:48:09.075700
# Unit test for function get_tree_node
def test_get_tree_node():  # noqa pylint: disable=missing-docstring
    # Test for get_tree_node
    assert get_tree_node({'test': 1}, 'test') == 1
    assert get_tree_node({'test': [1, 2]}, 'test:0') == 1
    assert get_tree_node({'test': {'test': 1}}, 'test:test') == 1
    assert get_tree_node({'test': {'test': 1}}, 'test:test:test', _sentinel) == _sentinel

    # Test for get_tree_node, parent=True
    assert get_tree_node({'test': [1, 2]}, 'test:0', parent=True) == [1, 2]

# Generated at 2022-06-14 06:48:21.724270
# Unit test for function get_tree_node
def test_get_tree_node():
    # Create a tree-like object
    data = {
        'mapping': {
            'with': {
                'dimension': {
                    'help': 'yay'
                }
            }
        },
        'nested': {
            'list': ['stuff'],
            'dict': {
                'also': 'here'
            },
            'other': 'data'
        }
    }

    # Fetch key with default
    assert get_tree_node(data, 'nested:list', default='not found') == ['stuff']
    assert get_tree_node(data, 'nested:list:notfound', default='not found') == 'not found'

    # Fetch key w/o default
    assert get_tree_node(data, 'mapping:with:dimension:help') == 'yay'

   

# Generated at 2022-06-14 06:48:35.231558
# Unit test for function get_tree_node
def test_get_tree_node():
    def tree_dfs(tree_dict, key, delim='.'):
        key_stack = key.split(delim)
        node = tree_dict
        for key in key_stack:
            node = node[key]
        return node

    # test.test.test
    tree_dict = {
        'test': {
            'test': {
                'test': True
            }
        }
    }
    assert get_tree_node(tree_dict, 'test.test.test') == tree_dfs(tree_dict, 'test.test.test') is True

    # test.test.test:False
    tree_dict = {
        'test': {
            'test': {
                'test': True
            }
        }
    }

# Generated at 2022-06-14 06:48:42.921445
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()
    mapping[0][1][2] = 'foo'
    mapping[3][4][5] = 'bar'
    mapping[0][6][7] = 'baz'

    assert get_tree_node(mapping, '0:1:2') == 'foo'
    assert get_tree_node(mapping, '0:1:8', default=_sentinel) is _sentinel
    assert get_tree_node(mapping, '0:1:8', default='qux') == 'qux'
    assert get_tree_node(mapping, '3:4:5') == 'bar'



# Generated at 2022-06-14 06:48:55.162658
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    >>> test_get_tree_node()
    """
    mapping = {
        'root': {
            'foo': {
                'bar': {
                    'baz': 'value',
                }
            }
        }
    }
    assert get_tree_node(mapping, 'root:foo:bar:baz', default='none') == 'value'
    assert get_tree_node(mapping, 'root:foo:bar:baz', default='none') == 'value'
    assert get_tree_node(mapping, 'root:foo:bar:barber', default='none') == 'none'  # noqa
    assert get_tree_node(mapping, 'root:foo:bar:barber') == 'value'

# Generated at 2022-06-14 06:49:07.183378
# Unit test for function get_tree_node
def test_get_tree_node():

    import nose
    from nose.tools import assert_equals, assert_raises, assert_true

    mapping = {
        'foo': 'bar',
        'baz': {
            'bang': 'bap'
        }
    }

    # Normal usage
    assert_equals(get_tree_node(mapping, 'foo'), 'bar')

    # Recursive usage
    assert_equals(get_tree_node(mapping, 'baz:bang'), 'bap')

    # Default usage
    assert_equals(get_tree_node(mapping, 'foo:bang', default='baz'), 'baz')

    # Non-existent key, default=None
    assert_equals(get_tree_node(mapping, 'foo:bang', default=None), None)

    # Non-existent key, default

# Generated at 2022-06-14 06:49:14.093539
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'
    with pytest.raises(KeyError) as exc:
        get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:d')
    assert exc.value.args[0] == "'d'"

# Generated at 2022-06-14 06:49:20.080892
# Unit test for function set_tree_node
def test_set_tree_node():
    t = tree()
    set_tree_node(t, 'a:b:c:d', 'foo')
    assert t['a']['b']['c']['d'] == 'foo', 'Tree t["a"]["b"]["c"]["d"] is not "foo" (is "%s")' % t['a']['b']['c']['d']



# Generated at 2022-06-14 06:49:35.704233
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(tree(), 'test') is None

    tree_test = tree()
    tree_test['test']['test2'] = 'hello'
    assert get_tree_node(tree_test, 'test:test2') == 'hello'
    assert get_tree_node(tree_test, 'test:test3') is None

    tree_test = tree()
    tree_test['test']['test2'] = 'hello'
    assert get_tree_node(tree_test, 'test:test2', 'foo') == 'hello'
    assert get_tree_node(tree_test, 'test:test3', 'foo') == 'foo'

    tree_test = tree()
    tree_test['test']['test2'] = 'hello'

# Generated at 2022-06-14 06:49:42.232050
# Unit test for function get_tree_node
def test_get_tree_node():
    # Make a Tree, fill with random data
    tree = Tree()
    tree['a'] = 1
    tree['b'] = {'b1': 1, 'b2': 2, 'b3': 3}
    tree['c'] = {'c1': 1, 'c2': 2, }

    # Test 1, get root-level item
    assert tree.get_tree_node('a') == 1

    # Test 2, fetch deeper
    assert tree.get_tree_node('b:b3') == 3

    # Test 3, fetch deeper with default
    assert tree.get_tree_node('b:b5', default=5) == 5

    # Test 4, fetch deeper without default
    with pytest.raises(KeyError):
        tree.get_tree_node('b:b5')

    # Test 5, fetch

# Generated at 2022-06-14 06:49:54.192030
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = tree()

    test_dict['first'] = 'leaf_value'
    test_dict['second']['leaf'] = 'second_leaf_value'
    test_dict['second']['third']['third_leaf'] = 'third_leaf_value'

    correct_value = 'leaf_value'

# Generated at 2022-06-14 06:50:03.413844
# Unit test for function get_tree_node
def test_get_tree_node():
    # Example data
    tree = {
        'main': {
            'sub': {
                'foo': 'bar',
                'baz': 'quux',
            },
            'sub2': {
                'foo': 'bar',
                'baz': 'quux',
            },
        },
        'main2': {
            'sub': {
                'foo': 'bar',
                'baz': 'quux',
            },
            'sub2': {
                'foo': 'bar',
                'baz': 'quux',
            },
        },
    }

    def _test_get_tree_node_value(mapping, key, expected_value, expected_parent_value):
        """Helper function to test a single input against expected values."""
        value = get_tree_node(tree, key)

# Generated at 2022-06-14 06:50:14.894487
# Unit test for function get_tree_node
def test_get_tree_node():
    # Example: setting an item with : in key on a regular dict
    mapping = {}
    mapping.update({'spam:eggs:foo:bar': 42})

    # Check that we get the right value
    assert 42 == get_tree_node(mapping, 'spam:eggs:foo:bar')

    # Check that we get the right parent node
    assert mapping['spam']['eggs']['foo'] == get_tree_node(mapping, 'spam:eggs:foo:bar', parent=True)

    # Check that we get the right parents parent
    assert mapping['spam']['eggs'] == get_tree_node(mapping, 'spam:eggs:foo:bar', parent=True, parent=True)

    ### Now for a tree

    # Reset mapping and make it a tree
   

# Generated at 2022-06-14 06:50:23.104394
# Unit test for function get_tree_node
def test_get_tree_node():
    """Test that get_tree_node works as expected."""
    d = dict(f=dict(g=dict(h=1)))
    assert 1 == get_tree_node(d, 'f:g:h')
    assert _sentinel is get_tree_node(d, 'f:g:i', _sentinel)
    with pytest.raises(KeyError):
        get_tree_node(d, 'f:g:i')



# Generated at 2022-06-14 06:50:30.637214
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = dict(
        a=dict(b=dict(c=dict(d=1))),
        foo='bar',
    )
    # Check root node access
    assert get_tree_node(mapping, 'foo') == 'bar'
    # Check deep node access
    assert get_tree_node(mapping, 'a:b:c:d') == 1
    # Check for KeyError when an intermediate node is missing
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:d:e')



# Generated at 2022-06-14 06:50:38.209348
# Unit test for function get_tree_node
def test_get_tree_node():
    d = {'a': {'b': {'c': 5}}}

    assert get_tree_node(d, 'a:b:c') == 5
    assert get_tree_node(d, 'a:b:c', parent=True) == {'c': 5}
    assert get_tree_node(d, 'a:b:c', default=0) == 0

# Generated at 2022-06-14 06:50:50.738478
# Unit test for function get_tree_node
def test_get_tree_node():

    # Test 1
    test_node = {'a': {'b': {'c': 7}}}
    assert get_tree_node(test_node, 'a:b:c') == 7
    assert get_tree_node(test_node, 'a:b:c', default=None) == 7
    assert get_tree_node(test_node, 'a:b:z', default=None) is None

    # Test 2
    test_node = {'a': {'b': {}}}
    assert get_tree_node(test_node, 'a:b:z', default=None) is None

    # Test 3
    test_node = {'a': {'b': {'c': 7}}}

# Generated at 2022-06-14 06:51:02.034511
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test general functionality
    mapping = tree()
    mapping['a:b:c'] = 'A:B:C'
    assert get_tree_node(mapping, 'a:b:c') == 'A:B:C'
    assert get_tree_node(mapping, 'a:b') == {'c': 'A:B:C'}
    mapping['a:b:c'] = 'D'
    assert get_tree_node(mapping, 'a:b:c') == 'D'
    assert get_tree_node(mapping, 'a:b') == {'c': 'D'}
    mapping['a:b:c']['d'] = {'e': 'F'}

# Generated at 2022-06-14 06:51:23.847453
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {
        'var1': 'val1',
        'var2': {
            'var3': 'val3'
        }
    }
    assert get_tree_node(mapping, 'var1') == 'val1'
    assert get_tree_node(mapping, 'var2:var3') == 'val3'
    assert get_tree_node(mapping, 'var2:var4', default='val4') == 'val4'
    try:
        get_tree_node(mapping, 'var2:var4')
    except KeyError:
        pass
    else:
        assert False, 'Expected key error'
    assert get_tree_node(mapping, 'var2:var4', default='val4') == 'val4'

# Generated at 2022-06-14 06:51:30.254405
# Unit test for function set_tree_node
def test_set_tree_node():
    """
    Unit test for function set_tree_node
    """
    test_mapping = {
        "key1": None,
        "key2:subkey1": None,
        "key3": None,
    }
    test_key = "key3:subkey2"
    test_value = "some_value"
    result = set_tree_node(test_mapping, test_key, test_value)
    assert result == {"subkey2": "some_value"}
    assert test_mapping == {
        "key1": None,
        "key2:subkey1": None,
        "key3": {"subkey2": "some_value"},
    }



# Generated at 2022-06-14 06:51:41.166012
# Unit test for function get_tree_node
def test_get_tree_node():
    t = tree()
    t['a']['b']['c'] = 1
    assert get_tree_node(t, 'a') == {'b': {'c': 1}}
    assert get_tree_node(t, 'a:b') == {'c': 1}
    assert get_tree_node(t, 'a:b:c') == 1
    assert get_tree_node(t, 'a:b:c:d') is _sentinel
    assert get_tree_node(t, 'a:b:c:d', default=False) is False
    assert get_tree_node(t, 'a:b:c:d', default=False, parent=True) == 1



# Generated at 2022-06-14 06:51:50.777309
# Unit test for function get_tree_node
def test_get_tree_node():
    tree = {
        'foo': {
            'bar': {
                'baz': '☃'
            }
        }
    }
    print(get_tree_node(tree, 'foo:bar:baz'))
    try:
        print(get_tree_node(tree, 'foo:bar:buzz'))
    except KeyError as exc:
        print('Failed to get baz', exc)

    print(get_tree_node(tree, 'foo:bar:buzz', default='Quux'))



# Generated at 2022-06-14 06:52:00.282104
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = tree()

    # Test nonexistent key
    assert get_tree_node(mapping, 'key')

    mapping['key'] = 'value'

    assert get_tree_node(mapping, 'key') == 'value'

    mapping['key:subkey'] = 'value'
    mapping['key:subkey2'] = 'value'

    assert get_tree_node(mapping, 'key:subkey') == 'value'
    assert get_tree_node(mapping, 'key:subkey2') == 'value'



# Generated at 2022-06-14 06:52:06.584229
# Unit test for function get_tree_node
def test_get_tree_node():
    data = dict(
        a=dict(
            b=1,
            c=2
        )
    )

    # Base test
    assert get_tree_node(data, 'a:b') == 1
    assert get_tree_node(data, 'a:c') == 2

    # Test with bad key
    with pytest.raises(KeyError):
        assert get_tree_node(data, 'a:d')

    # Test with default
    assert get_tree_node(data, 'a:d', default=12) == 12



# Generated at 2022-06-14 06:52:19.225997
# Unit test for function get_tree_node
def test_get_tree_node():
    from pprint import pprint
    from types import NoneType
    import pytest

    objs = {'a:b:c': 1, 'd:e:f': 2, 'g:h:i': 3, 'j': 4, 'k': {'l': 5}, 'o:p:': 6, 'q:r:': 7}
    objs.update(tree())


# Generated at 2022-06-14 06:52:23.040504
# Unit test for function get_tree_node
def test_get_tree_node():
    test_dict = {'one': {'two': {'three': 'value'}}}
    assert get_tree_node(test_dict, 'one:two:three') == 'value'



# Generated at 2022-06-14 06:52:35.888960
# Unit test for function get_tree_node
def test_get_tree_node():
    def check_node(node, name, assert_equal=True, **kw):
        for k, v in kw.iteritems():
            if assert_equal is True:
                eq_(node[name][k], v)
            else:
                assert_equal(node[name][k], v)

    # Setup
    node = tree()
    node['a']['b']['c'] = 'd'

    # Test
    check_node(node, 'a:b', c='d', assert_equal=eq_)
    check_node(node, 'a:b:c', d=True)

    # Check parent
    check_node(node, 'a:b:c', assert_equal=False, d=True)
    check_node(node, 'a:b:c', parent=True, c='d')

# Generated at 2022-06-14 06:52:42.354528
# Unit test for function get_tree_node
def test_get_tree_node():

    """
    Get node from mapping, with : notation for multiple dimensions.

    >>> test_mapping = {'a': 1, 'b': {'c': 1}}
    >>> get_tree_node(test_mapping, 'b:c')
    1

    """
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:53:08.810092
# Unit test for function set_tree_node
def test_set_tree_node():

    mapping = tree()
    assert isinstance(mapping, Tree)

    set_tree_node(mapping, 'a:b:c', 'one')
    set_tree_node(mapping, 'a:b:d', 'two')
    set_tree_node(mapping, 'a:e:f', 'three')
    set_tree_node(mapping, 'a:e:g', 'four')

    # We should have a tree looking like
    # a
    # |-- b
    # |   |
    # |   |-- c
    # |   |-- d
    # |-- e
    #     |
    #     |-- f
    #     |-- g

    assert mapping['a:b:c'] == 'one'
    assert mapping['a:b:d'] == 'two'

# Generated at 2022-06-14 06:53:19.659212
# Unit test for function get_tree_node
def test_get_tree_node():

    # Base
    test = {
        'a': {
            'b': 'c',
            'd': {
                'e': 'f',
            },
        },
    }
    assert get_tree_node(test, 'a:b') == 'c'
    assert get_tree_node(test, 'a:d:e') == 'f'

    # Can return the parent node
    assert get_tree_node(test, 'a:d:e', parent=True) == test['a']['d']

    # Has a default value
    assert get_tree_node(test, 'a:does:not:exist', default='woop') == 'woop'

    # Raises a key error by default if not found

# Generated at 2022-06-14 06:53:31.941853
# Unit test for function set_tree_node
def test_set_tree_node():
    """Set a tree node using : notation."""
    # Set a brain node
    brain = {
        'emotions': {
            'sadness': 0,
            'joy': 0,
            'surprise': 0,
        }
    }

    # Set arbitrary key
    set_tree_node(brain, 'emotions:sadness', 10)
    assert brain['emotions']['sadness'] == 10

    # Set arbitrary key in list
    set_tree_node(brain, 'emotions:sadness', [10, 15, 20])
    assert brain['emotions']['sadness'] == [10, 15, 20]

    # Set arbitrary key in list of list
    set_tree_node(brain, 'emotions:sadness:1', 15)

# Generated at 2022-06-14 06:53:40.801792
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'foo': {'bar': 'baz', 'wat': {'wer': 'qwr'}, 'bar2': 'baz2'}}
    assert get_tree_node(mapping, 'foo:bar') == 'baz'
    assert get_tree_node(mapping, 'foo:wat:wer') == 'qwr'
    assert get_tree_node(mapping, 'foo:bar2') == 'baz2'
    assert get_tree_node(mapping, 'foo:wat:wer', parent=True) == {'wer': 'qwr'}
    assert get_tree_node(mapping, 'foo:bar2', parent=True) == mapping['foo']
    assert get_tree_node(mapping, 'foo:wat:wer', default='default') == 'qwr'
    assert get

# Generated at 2022-06-14 06:53:52.316531
# Unit test for function get_tree_node
def test_get_tree_node():
    """
    Unit test function for get_tree_node.

    Raises:
        AssertionError if any unit test fails.

    """
    given = {
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

    assert get_tree_node(given, 'a:b:c:d:e') == 'f'
    assert get_tree_node(given, 'a:b:c:d:e', default=1) == 'f'
    assert get_tree_node(given, 'a:b:c:d:e', parent=True) == {'e': 'f'}

# Generated at 2022-06-14 06:54:01.215542
# Unit test for function get_tree_node
def test_get_tree_node():
    # test for empty structure
    mapping = {}
    key = 'a:b:c'
    expected_value = 'e'
    set_tree_node(mapping, key, expected_value)
    assert get_tree_node(mapping, key) == expected_value
    # test for non-empty structure
    structure = {
        'a': {
            'b': {
                'c': expected_value
            }
        }
    }
    assert get_tree_node(structure, key) == expected_value



# Generated at 2022-06-14 06:54:05.339202
# Unit test for function get_tree_node
def test_get_tree_node():

    data = Tree(
        {'foo': {'bar': {
            'baz': 1
        }}}
    )
    assert get_tree_node(data, 'foo:bar:baz') == 1



# Generated at 2022-06-14 06:54:17.601894
# Unit test for function get_tree_node
def test_get_tree_node():
    arr = {
        'a': {
            'b': {
                'c': 'c',
                'd': 'd',
            },
        },
    }
    # Test 1: Array access
    assert get_tree_node(arr, 'a:b:c') == 'c'
    assert get_tree_node(arr, 'a:b:c:d') == 'd'
    # Test 2: Parent node access
    assert get_tree_node(arr, 'a:b:c:d', parent=True) == {
        'c': 'c',
        'd': 'd',
    }
    # Test 3: Default behavior
    assert get_tree_node(arr, 'a:b:c:e', default='default') == 'default'
    # Test 4: Exception behavior

# Generated at 2022-06-14 06:54:24.678543
# Unit test for function get_tree_node
def test_get_tree_node():
    test_tree = tree()
    test_tree['test:test:test:test'] = 'test'
    assert get_tree_node(test_tree, 'test:test:test:test') == 'test'
    assert get_tree_node(test_tree, 'test:test:test', default='fail') == 'fail'


if __name__ == '__main__':
    test_get_tree_node()

# Generated at 2022-06-14 06:54:37.216658
# Unit test for function get_tree_node
def test_get_tree_node():
    mapping = {'foo': {'bar': {'baz': 'yay'}, 'buzz': 'kazam'}}
    assert get_tree_node(mapping, 'foo:bar:baz') == 'yay'
    assert get_tree_node(mapping, 'foo:buzz') == 'kazam'
    assert get_tree_node(mapping, 'foo:not_a_key') is _sentinel
    assert get_tree_node(mapping, 'foo:not_a_key', default=None) is None
    try:
        get_tree_node(mapping, 'foo:not_a_key')
    except KeyError:
        pass
    else:
        assert False, "Did not throw KeyError!"

    # Test `parent` argument

# Generated at 2022-06-14 06:55:24.009109
# Unit test for function set_tree_node
def test_set_tree_node():
    _mapping, _key, _value, _expected = None, None, None, None

    # Simple subnode
    _mapping = {}
    _key = 'fruit:orange'
    _value = 'delicious'
    _expected = {'fruit': {'orange': 'delicious'}}
    assert set_tree_node(_mapping, _key, _value) == _expected

    # Overwrite node
    _mapping = {'fruit': {'orange': 'disgusting'}}
    _key = 'fruit:orange'
    _value = 'delicious'
    _expected = {'fruit': {'orange': 'delicious'}}
    assert set_tree_node(_mapping, _key, _value) == _expected

    # Empty key

# Generated at 2022-06-14 06:55:36.563433
# Unit test for function get_tree_node
def test_get_tree_node():
    # Test basic functionality
    mapping = {
        'a': {
            'b': 'win'
        }
    }
    assert get_tree_node(mapping, 'a:b') == 'win'
    # Test default
    assert get_tree_node(mapping, 'a:b:c', default=None) is None
    # Test KeyError
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'a:b:c')
    # Test parent
    assert get_tree_node(mapping, 'a:b:c', parent=True) == {'a': {'b': 'win'}}
    # Test parent keyerror
    with pytest.raises(KeyError):
        get_tree_node(mapping, 'x:y:c', parent=True)

# Generated at 2022-06-14 06:55:43.692256
# Unit test for function set_tree_node
def test_set_tree_node():
    test_dict = {}
    set_tree_node(test_dict, 'test:test:test:test:test', 'test')
    assert test_dict['test']['test']['test']['test']['test'] == 'test'

    test_dict = {}
    set_tree_node(test_dict, 'test:test:test:test:test===test', 'test')
    assert test_dict['test']['test']['test']['test']['test===test'] == 'test'



# Generated at 2022-06-14 06:55:49.898295
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node({'a': {'b': {'c': 'd'}}}, 'a:b:c') == 'd'

    # This should cause an error
    try:
        get_tree_node({}, 'a:b:c')
    except KeyError:
        pass


# Unit tests for class Tree

# Generated at 2022-06-14 06:55:53.586887
# Unit test for function get_tree_node
def test_get_tree_node():
    assert get_tree_node(
        {'parent': {'child': 'value'}},
        'parent:child'
    ) == 'value'



# Generated at 2022-06-14 06:56:01.972725
# Unit test for function get_tree_node
def test_get_tree_node():
    t = {
        'a': {
            'x': 1
        },
        'b': {
            'y': 2
        }
    }

    assert get_tree_node(t, 'b:y') == 2
    try:
        get_tree_node(t, 'b:z')
    except KeyError:
        pass
    else:
        raise ValueError('KeyError not raised')

