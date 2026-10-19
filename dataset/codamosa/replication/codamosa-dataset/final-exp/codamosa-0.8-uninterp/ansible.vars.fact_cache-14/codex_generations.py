

# Generated at 2022-06-13 17:07:39.211306
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('some_key', {'a' : 'b', 'c' : 'd'})
    assert(cache['some_key'] == {'a' : 'b', 'c' : 'd'})
    cache.first_order_merge('some_key', {'a' : 'e', 'f' : 'g'})
    assert(cache['some_key'] == {'a' : 'e', 'c' : 'd', 'f' : 'g'})

# Generated at 2022-06-13 17:07:47.614880
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    facts_cache.first_order_merge("myhost", {"foo": "foo_value"})
    assert facts_cache["myhost"]["foo"] == "foo_value"
    facts_cache.first_order_merge("myhost", {"foo": "foo_value", "bar": "bar_value"})
    assert facts_cache["myhost"]["foo"] == "foo_value"
    assert facts_cache["myhost"]["bar"] == "bar_value"
    facts_cache.first_order_merge("myhost", {"foo": "new_foo_value"})
    assert facts_cache["myhost"]["foo"] == "new_foo_value"

# Generated at 2022-06-13 17:07:57.035300
# Unit test for constructor of class FactCache
def test_FactCache():

    import tempfile
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 17:08:02.000143
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin is None
    assert cache.__getitem__ is not None
    assert cache.__setitem__ is not None
    assert cache.__delitem__ is not None
    assert cache.__contains__ is not None

# Generated at 2022-06-13 17:08:10.115295
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Init FactCache
    fact_cache = FactCache()

    # first use_fact_cache
    use_fact_cache = [
        None,
        False,
        True
    ]

    for use_c in use_fact_cache:
        C.CACHE_PLUGIN_CONNECTION = use_c
        display.debug("C.CACHE_PLUGIN_CONNECTION: %s" % C.CACHE_PLUGIN_CONNECTION)

        fact_cache.flush()

        # init host_facts
        host_facts = {
            'a': {'a1': 'a1'},
            'b': {'b1': 'b1'},
            'c': {'c1': 'c1'}
        }

        # init host_cache

# Generated at 2022-06-13 17:08:12.432628
# Unit test for constructor of class FactCache
def test_FactCache():

    try:
        fc = FactCache()
        fc[1] = 'value'
    except Exception as e:
        print(e)

test_FactCache()

# Generated at 2022-06-13 17:08:21.718033
# Unit test for constructor of class FactCache
def test_FactCache():
    init_args = []
    init_kwargs = {}
    fact_cache = FactCache(*init_args, **init_kwargs)
    fact_cache_dict = {}

    print("Test that the variables in fact_cache and fact_cache_dict are the same")
    for key in fact_cache_dict.keys():
        print("Checking if " + key + " are the same between the dictionaries")
        assert fact_cache[key] == fact_cache_dict[key]

    print("Test that the variables in fact_cache_dict and fact_cache are the same")
    for key in fact_cache.keys():
        print("Checking if " + key + " are the same between the dictionaries")
        assert fact_cache[key] == fact_cache_dict[key]

    new_key = 'key'
    new_

# Generated at 2022-06-13 17:08:29.438046
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factCache = FactCache()
    factCache.flush()
    fact_key = "fact_key"
    fact_value = dict()
    fact_value[fact_key] = "fact_value"
    factCache.first_order_merge(fact_key, fact_value)
    assert factCache[fact_key] == fact_value
    fact_value_2 = dict()
    fact_value_2[fact_key] = "fact_value_2"
    factCache.first_order_merge(fact_key, fact_value_2)
    assert factCache[fact_key] == fact_value

# Generated at 2022-06-13 17:08:36.863142
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence
    from ansible.module_utils.facts.system.distribution import Distribution

    host = 'localhost'
    ansible_facts = { 'some_fact': AnsibleUnicode('some_fact_value'), 'some_list': AnsibleSequence([AnsibleUnicode('item1'), AnsibleUnicode('item2')]),
                      'some_dict': AnsibleMapping({'key1': AnsibleUnicode('value1'), 'key2': AnsibleUnicode('value2')}) }
    ansible_distribution = Distribution('distro', '1.0', 'codename')

    # Create fact cache
    fact_cache = FactCache()

    # Assert fact cache is empty
    assert len

# Generated at 2022-06-13 17:08:45.711367
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Create fact cache object
    facts = FactCache()

    # Create test data
    host_cache = {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key31": "value3",
            "key32": "value4"
        },
        "key4": "value5",
        "key5": "value6"
    }

    host_cache1 = {
        "key1": "value11",
        "key2": "value12",
        "key3": {
            "key31": "value3",
            "key32": "value4"
        },
        "key4": "value15",
        "key5": "value16"
    }

    # Test first order merge

# Generated at 2022-06-13 17:08:50.373555
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
        assert False
    except AnsibleError:
        assert True

# Generated at 2022-06-13 17:08:58.555580
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    host = 'localhost'
    key = 'ansible_facts'
    facts = dict(ansible_architecture='x86_64', ansible_distribution='CentOS', ansible_distribution_version='7.6.1810',
                 ansible_os_family='RedHat', ansible_system='Linux')
    # call for first time should retrieve the same facts
    facts_cache.first_order_merge(host, facts)
    assert facts_cache[host] == facts

    # second can do a different facts because of ansible_facts.update

# Generated at 2022-06-13 17:09:01.509242
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin is not None

# Generated at 2022-06-13 17:09:02.975198
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        f = FactCache()
    except:
        raise


# Generated at 2022-06-13 17:09:04.839174
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert (fact_cache)

# Generated at 2022-06-13 17:09:06.706902
# Unit test for constructor of class FactCache
def test_FactCache():
    # assert constructor of FactCache
    assert FactCache()

# Generated at 2022-06-13 17:09:08.811011
# Unit test for constructor of class FactCache
def test_FactCache():
    # Fill args and kwargs
    args = []
    kwargs = {}
    fact_cache = FactCache(*args, **kwargs)
    assert fact_cache is not None 



# Generated at 2022-06-13 17:09:11.783589
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin.__class__.__name__ in ['JsonFileFactCacheModule', 'DictFactCacheModule']



# Generated at 2022-06-13 17:09:15.985443
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fixture_data = {'ansible_facts': {'os_family': 'Debian'}, 'tmp_var': {'local_tmp_var': 'foo'}}
    test_data = {'local_tmp_var': 'foo'}
    cache = FactCache()
    cache.update(fixture_data)
    cache.first_order_merge('tmp_var', test_data)
    assert cache['tmp_var'] == test_data

# Generated at 2022-06-13 17:09:18.482030
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    new_fact = 'new_fact'
    fact_cache[new_fact] = 'new_value'
    fact_cache[new_fact] = 'newer_value'
    assert fact_cache[new_fact] == 'newer_value'

# Generated at 2022-06-13 17:09:31.215685
# Unit test for constructor of class FactCache
def test_FactCache():
    test_fact_cache = FactCache()
    test_fact_cache["test_host"] = {}
    test_fact_cache["test_host"]["test_fact"] = "test_value"
    
    assert test_fact_cache["test_host"]["test_fact"] == "test_value"
    assert len(test_fact_cache) == 1
    assert "test_host" in test_fact_cache
    
    assert "test_host" in test_fact_cache.keys()
    
    test_fact_cache.flush()
    assert "test_host" not in test_fact_cache

# Generated at 2022-06-13 17:09:32.072986
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:09:39.550611
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_facts = {
        'ansible_distribution': 'CentOS',
        'ansible_distribution_major_version': '7',
        'ansible_userspace_architecture': 'x86_64',
        'ansible_kernel': 'Linux',
        'ansible_machine': 'x86_64',
        'ansible_processor': 'x86_64',
        'student': '1'
    }

# Generated at 2022-06-13 17:09:42.022993
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.__class__.__getitem__ = lambda x,y: "test"
    fact_cache.__class__.__setitem__ = lambda x,y,z: "test"
    fact_cache.first_order_merge("test_key", "test_value")

# Generated at 2022-06-13 17:09:47.868625
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    cache.get('name')
    cache.set('name', 'value')
    cache.delete('name')
    cache.contains('name')
    cache.keys()
    cache.flush()
    cache.update({'name': 'value'})
    cache.copy()
    cache.first_order_merge('name', 'value')
    cache.get('name')

# Generated at 2022-06-13 17:09:49.001369
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    assert(fact_cache)

# Generated at 2022-06-13 17:09:50.499024
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:09:53.376457
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        assert(C.CACHE_PLUGIN == 'jsonfile')
        FactCache()
        assert(True)
    except Exception as e:
        assert(False)

# Generated at 2022-06-13 17:09:54.228657
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:04.818032
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    # copy()
    test_dict = {'test1': 'test1'}
    assert fc.copy() == {}

    # __contains__()
    assert 'test1' not in fc
    fc['test1'] = 'test1'
    assert 'test1' in fc

    # __getitem__()
    assert fc['test1'] == 'test1'
    fc['test1'] = test_dict
    assert fc['test1'] == test_dict

    # __setitem__()
    assert fc['test2'] == 'test2'
    fc['test2'] = test_dict
    assert fc['test2'] == test_dict

    # __delitem__()
    assert fc['test2'] == test_dict
    del f

# Generated at 2022-06-13 17:10:10.812488
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()



# Generated at 2022-06-13 17:10:16.636983
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        if not C.CACHE_PLUGIN:
            raise AnsibleError('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))
    except AnsibleError as e:
        display.error("Unable to load cache plugin: %s" % (e.message))
        return -1
    return 0

# Generated at 2022-06-13 17:10:25.384891
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import BaseCacheModule

    class DummyCache(BaseCacheModule):
        def __init__(self):
            pass

        def get(self, key, *args, **kwargs):
            if key == 'a':
                return 1
            else:
                raise KeyError

        def set(self, key, value, *args, **kwargs):
            pass

        def keys(self):
            return ['a']

        def contains(self, key):
            if key == 'a':
                return True
            else:
                return False

        def delete(self, key):
            pass

        def flush(self):
            pass

        def copy(self):
            pass

    cache_loader.cache_modules['dummy'] = DummyCache
    assert cache_loader.get('dummy') is Dummy

# Generated at 2022-06-13 17:10:32.426872
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('hostvars', {'hostvars':{
                                                     'host1':{
                                                             'ansible_facts':{'fact1':{'fact2':2,'fact3':3}},
                                                             'ansible_facter':{
                                                             'factter2':{'factter3':3}
                                                             }
                                                          }
                                                      }
                                              }
                                 )
    assert fact_cache['hostvars']['host1']['ansible_facter']['factter2']['factter3'] == 3

# Generated at 2022-06-13 17:10:33.032948
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact._plugin

# Generated at 2022-06-13 17:10:37.618995
# Unit test for constructor of class FactCache
def test_FactCache():

    # Initialize fact cache object
    fact_cache = FactCache()
    # All values should be empty
    for key in fact_cache.keys():
        value = fact_cache[key]
        assert value is None


# Generated at 2022-06-13 17:10:47.648019
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('10.8.8.8', {'a': 1, 'b': 2})
    assert fact_cache['10.8.8.8'] == {'a': 1, 'b': 2}
    fact_cache.first_order_merge('10.8.8.8', {'c': 3})
    assert fact_cache['10.8.8.8'] == {'a': 1, 'b': 2, 'c': 3}
    fact_cache['10.8.8.8'] = {}
    fact_cache.first_order_merge('10.8.8.8', {'a': 1, 'b': 2, 'c': 3})

# Generated at 2022-06-13 17:10:54.138034
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    mock_cache = FactCache()
    key1 = 'key1'
    value1 = 'value1'
    mock_cache[key1] = value1
    key2 = 'key2'
    value2 = 'value2'
    mock_cache.first_order_merge(key2, value2)
    assert mock_cache[key1] == value1
    assert mock_cache[key2] == value2

# Generated at 2022-06-13 17:10:55.126312
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:56.520818
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache.keys() == []

# Generated at 2022-06-13 17:11:08.917764
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin is not None


# Generated at 2022-06-13 17:11:15.776246
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()
    empty_fact_cache = {'cache_name': 'facts', '_plugin': 'memory', '_facts': {}}
    # Negative test case
    assert fact_cache != empty_fact_cache
    # Positive test case
    fact_cache.first_order_merge('_plugin', 'memory')
    fact_cache.first_order_merge('cache_name', 'facts')
    assert fact_cache == empty_fact_cache
    # Negative test case
    fact_cache.first_order_merge('shinji', 'ikari')
    assert fact_cache == empty_fact_cache

# Generated at 2022-06-13 17:11:18.608918
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache()
        assert True
    except Exception as ex:
        print(ex)
        assert False

# Generated at 2022-06-13 17:11:19.576645
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_cache = FactCache()

# Generated at 2022-06-13 17:11:23.146698
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('cache_key', 'cache_value')
    assert('cache_key' in fact_cache)
    assert(fact_cache['cache_key'] == 'cache_value')

# Generated at 2022-06-13 17:11:30.327425
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json

    # save cache
    host_cache = {
        "cache_key_1": {"result_key_1": {"result_val_1": "old_val_1", "result_val_2": "old_val_2"}},
        "cache_key_2": {"result_key_2": {"result_val_3": "old_val_3", "result_val_4": "old_val_4"}}
    }

    # new value - new key
    result_1 = {"result_key_3": {"result_val_5": "new_val_1", "result_val_6": "new_val_2"}}

    # new value - modified key

# Generated at 2022-06-13 17:11:31.833501
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:11:35.704171
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    fact_cache['test_key'] = 'test_val'
    assert fact_cache['test_key'] == 'test_val'
    assert len(fact_cache) == 1
    del fact_cache['test_key']
    assert not fact_cache.keys()

# Generated at 2022-06-13 17:11:41.698676
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.module_utils.six import PY3

    fact_cache = FactCache()
    cache_key = 'test_FactCache_first_order_merge'

    # If we call this first, the cache will contain the facts for this host
    # which will cause a KeyError in the real Ansible run when calling this
    # so, we populate the cache with an empty dictionary first
    fact_cache[cache_key] = {}

    # Test first that the cache is empty
    assert len(fact_cache) == 1
    assert cache_key in fact_cache
    assert isinstance(fact_cache[cache_key], dict)
    assert len(fact_cache[cache_key]) == 0

    # Test that first_order_merge updates the cache

# Generated at 2022-06-13 17:11:42.649123
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)


# Generated at 2022-06-13 17:12:14.032998
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    class FakeCache(object):

        def __init__(self):
            self.store = {}

        def get(self, key):
            return self.store.get(key)

        def set(self, key, value):
            self.store[key] = value

        def contains(self, key):
            return key in self.store

        def delete(self, key):
            if key in self.store:
                del self.store[key]

        def keys(self):
            return self.store.keys()

        def flush(self):
            self.store.clear()

    # Create a test fact cache and fake cache plugin
    fc = FactCache()
    fc._plugin = FakeCache()

    # Test case where no previous facts exist in the fact cache

# Generated at 2022-06-13 17:12:16.635923
# Unit test for constructor of class FactCache
def test_FactCache():
    # When cache plugin is not set.
    try:
        fact_cache = FactCache()
        assert False, 'AnsibleError is not raised.'
    except AnsibleError:
        pass

    # When cache plugin is set.
    C._CACHE_PLUGIN = 'jsonfile'
    fact_cache = FactCache()

# Generated at 2022-06-13 17:12:21.624321
# Unit test for constructor of class FactCache
def test_FactCache():

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from pytest import raises
    from ansible.plugins.loader import cache_loader

    fake_plugin = object()
    with patch.dict('ansible.plugins.loader.cache_loader._plugins',
                    {'my_cache_plugin': lambda *args, **kwargs: fake_plugin}):
        fact_cache = FactCache()
        assert fact_cache._plugin is fake_plugin
        raises(AnsibleError, FactCache)

# Generated at 2022-06-13 17:12:22.736002
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test creation of a new FactCache instance.
    """
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:12:23.588839
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert factcache is not None

# Generated at 2022-06-13 17:12:28.588984
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    if c is None:
        raise Exception("Failed to create an instance of FactCache")

    try:
        c = FactCache(None, "key")
    except Exception:
        pass

    try:
        c = FactCache("key", None)
    except Exception:
        pass

    try:
        c = FactCache("key", "value")
    except Exception:
        pass

    try:
        c = FactCache({"key": "value"})
    except Exception:
        pass
    

# Generated at 2022-06-13 17:12:35.964947
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''
    This is an unit test for method first_order_merge of class FactCache
    '''
    new_facts = {
        'local_facts': {'a': 1, 'b': 2},
        'ansible_facts': {'a': 1, 'c': 3},
    }
    old_facts = {
        'local_facts': {'a': 1, 'b': 2},
        'ansible_facts': {'b': 2, 'c': 3},
    }
    fact_cache = FactCache()
    for key, value in new_facts.items():
        fact_cache.first_order_merge(key, value)
    assert fact_cache['ansible_facts'] == {'a': 1, 'b': 2, 'c': 3}
    assert fact_cache['local_facts']

# Generated at 2022-06-13 17:12:36.573928
# Unit test for constructor of class FactCache
def test_FactCache():
    #TODO
    assert False

# Generated at 2022-06-13 17:12:37.719037
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:12:47.931444
# Unit test for constructor of class FactCache
def test_FactCache():
    print("\n")

    # Using parameters for constructor for class
    f = FactCache()
    print("FactCache object: ", f)
    print("Type of factCache Object: ", type(f))
    print("\n")
    print("\n")
    # Using instance methods of class FactCache
    print("Keys present in factCache Object: ", f.keys())
    print("First-Order Merge: ", f.first_order_merge("Test", {'Name': 'Ansible', 'Version': '2.9.0'}))
    print("Data present in factCache object: ", f.copy())
    #Using MutableMapping.update() method
    f.update({'Test': {'Name': 'Ansible Tower', 'Version': '3.0.0'}})

# Generated at 2022-06-13 17:13:17.897926
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    value = {'a': 1, 'b': 2}
    cache.first_order_merge('test', value)
    assert value == cache['test']

    # nonexistent key
    cache.first_order_merge('key1', {'a': 1})
    assert cache['key1'] == {'a': 1}

    # overwrite old value
    cache.first_order_merge('key1', {'a': 2})
    assert cache['key1'] == {'a': 2}

    # merge test
    cache.first_order_merge('key1', {'a': 1, 'b': 2})
    assert cache['key1'] == {'a': 1, 'b': 2}

    # new key

# Generated at 2022-06-13 17:13:19.719003
# Unit test for constructor of class FactCache
def test_FactCache():
    assert hasattr(FactCache, '__init__') and callable(getattr(FactCache, '__init__'))


# Generated at 2022-06-13 17:13:20.263212
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

# Generated at 2022-06-13 17:13:22.665223
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache
    return fact_cache


# Generated at 2022-06-13 17:13:25.463968
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    assert '_plugin' in fact_cache.__dict__

    if not isinstance(fact_cache._plugin, cache_loader.get(C.CACHE_PLUGIN)):
        assert False

# Generated at 2022-06-13 17:13:33.153703
# Unit test for constructor of class FactCache
def test_FactCache():
    import tempfile
    import os

    if not C.DEFAULT_CACHE_PLUGIN: # if cache module is not available, we cannot test
        return

    cache_file = tempfile.NamedTemporaryFile(delete=False).name
    C.CACHE_PLUGIN = "jsonfile"
    C.CACHE_PLUGIN_CONNECTION = cache_file

    fc = FactCache()
    assert isinstance(fc, FactCache)
    assert cache_file == C.CACHE_PLUGIN_CONNECTION or os.unlink(cache_file)

    # Issue #26186: jsonfile module does not have contains() method.
    if C.CACHE_PLUGIN != "jsonfile":
        # Test contains()
        assert not fc.__contains__("aaa")



# Generated at 2022-06-13 17:13:34.745083
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:13:35.860426
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    assert True

# Generated at 2022-06-13 17:13:37.479561
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache._plugin == cache_loader.get(C.CACHE_PLUGIN)
    assert not FactCache._plugin

# Generated at 2022-06-13 17:13:44.348883
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    print("\nTest for first_order_merge method of class FactCache")
    print("1. Test for when there is no key and value present in FactCache")
    print("Fact cache prior to call of first_order_merge: ", factcache)
    factcache.first_order_merge("key1","value1")
    print("Fact cache after call of first_order_merge: ", factcache)
    print("2. Test for when there is a key but no value present in FactCache")
    factcache.first_order_merge("key1","value2")
    print("Fact cache after call of first_order_merge: ", factcache)


# Generated at 2022-06-13 17:14:32.194269
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:14:34.840835
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = {}
    host_cache = {}
    host_facts['test'] = host_cache

    fact_cache.update({'test': host_cache})

    assert(fact_cache == host_facts)

# Generated at 2022-06-13 17:14:37.181863
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    print(fact_cache)

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:14:47.617434
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json
    facts_cache = FactCache()
    key = 'www.abc.com'
    facts_cache.flush()
    facts_cache.first_order_merge(key, None)

    value = {'a': 'b'}

    facts_cache.first_order_merge(key, value)
    assert(facts_cache[key] == value)
    assert(not facts_cache._plugin.get(key))
    facts_cache.flush()

    host_cache = {'c': 'd'}

    facts_cache._plugin.set(key, host_cache)
    facts_cache.first_order_merge(key, value)
    assert('a' in facts_cache[key])
    assert('c' in facts_cache[key])

# Generated at 2022-06-13 17:14:53.370499
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_obj = FactCache()
    # check it raises error if cache_plugin is not loaded
    try:
        # intentionally not loading the cache plugin
        C.CACHE_PLUGIN = 'testplugin'
        cache_obj = FactCache()
    except AnsibleError as e:
        # reset plugin to default
        C.CACHE_PLUGIN = 'fact_cache'
        if "Unable to load the facts cache plugin" not in str(e):
            raise AnsibleError


# Generated at 2022-06-13 17:14:55.441675
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin.cache_type == "memory"
    display.display("OK")

# Generated at 2022-06-13 17:15:02.641052
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_data = {
        'key1': {'test1': 'test1', 'test2': 'test2'},
        'key2': {'test3': 'test3', 'test4': 'test4', 'test5': {'test6': 'test6', 'test7': 'test7'}}
    }
    ansible_facts = {'ansible_facts': {'test1': 'test1', 'test2': 'test2'}}
    facts_cache = FactCache()

    # Checking empty cache
    facts_cache.first_order_merge('key1', ansible_facts['ansible_facts'])
    assert facts_cache['key1'] == test_data['key1']
    facts_cache.first_order_merge('key2', ansible_facts['ansible_facts'])
   

# Generated at 2022-06-13 17:15:09.583538
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("localhost", {'fact2': 'value2', 'fact1': 'value1'})
    assert fc["localhost"]["fact1"] == 'value1'
    assert fc["localhost"]["fact2"] == 'value2'
    fc.first_order_merge("localhost", {'fact1': 'value3', 'fact3': 'value3'})
    # FactCache should have overwritten the values of fact1 and
    # have kept the previous value of fact2 as it didn't exist in the new
    # update and added fact3
    assert fc["localhost"]["fact1"] == 'value3'
    assert fc["localhost"]["fact2"] == 'value2'

# Generated at 2022-06-13 17:15:15.179844
# Unit test for constructor of class FactCache
def test_FactCache():
    # the loader plugin is not loaded when the test runs
    # so we remove the required check on the constructor
    # so we can test the constructor of the class
    save_required_plugin = FactCache._FactCache__require_plugin
    FactCache._FactCache__require_plugin = lambda *_: None

    facts_cache = FactCache()
    assert facts_cache is not None

    # restore the original constructor
    FactCache._FactCache__require_plugin = save_required_plugin

# Generated at 2022-06-13 17:15:16.724894
# Unit test for constructor of class FactCache
def test_FactCache():
    test_factCache = FactCache()
    assert(test_factCache)


# Generated at 2022-06-13 17:16:57.701452
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    list_of_factcache_keys = factcache.keys()
    if list_of_factcache_keys:
        factcache.flush()

# Generated at 2022-06-13 17:16:58.666273
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:17:03.568237
# Unit test for constructor of class FactCache
def test_FactCache():

    # Test for plugin is None
    none_plugin = 'plugin_is_none'
    fact_cache = FactCache(plugin=none_plugin)
    assert fact_cache._plugin is not None

    # Test for plugin is not None
    plugin = 'yaml'
    fact_cache = FactCache(plugin=plugin)
    assert fact_cache._plugin is not None



# Generated at 2022-06-13 17:17:04.394849
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()


# Generated at 2022-06-13 17:17:05.575576
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    # Validate an object returned by the constructor
    assert isinstance(fc, FactCache)

# Generated at 2022-06-13 17:17:12.428124
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_color = {'color': 'blue'}
    fact_gender = {'gender': 'male'}
    fact_foo = {'foo': 'bar'}

    fact_cache = FactCache()
    fact_cache.first_order_merge('hostA', fact_color)
    fact_cache.first_order_merge('hostB', fact_gender)
    fact_cache.first_order_merge('hostC', fact_foo)

    assert 'hostA' in fact_cache
    assert 'hostB' in fact_cache
    assert 'hostC' in fact_cache

    assert 'hostA' in fact_cache.copy()
    assert 'hostB' in fact_cache.copy()
    assert 'hostC' in fact_cache.copy()

    assert fact_cache['hostA'] == fact_color

# Generated at 2022-06-13 17:17:21.701996
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    # test for case 1:
    #   if host cache does not exist
    key = 'localhost'
    cur_cache = {
        'changed': False,
        'example_key_2': 'example_value_2',
        'example_key_3': 'example_value_3'
    }
    fact_cache.first_order_merge(key, cur_cache)

    assert fact_cache[key]['changed'] == cur_cache['changed']
    assert fact_cache[key]['example_key_2'] == cur_cache['example_key_2']
    assert fact_cache[key]['example_key_3'] == cur_cache['example_key_3']

    # test for case 2:
    #   if host cache does exist
    key = 'localhost'


# Generated at 2022-06-13 17:17:29.520607
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Given
    fc = FactCache()

    # When
    fc.first_order_merge('127.0.0.1', 'this is a test')
    fc.first_order_merge('127.0.0.1', {'a': {'b': 'c'}})
    fc.first_order_merge('127.0.0.1', {'a': 'b'})

    # Then
    assert fc.get('127.0.0.1') == {
        'a': {'b': 'c'},
        'ansible_facts': {
            'cache': {
                '_ansible_no_log': False,
                'changed': False
            },
            'a': 'b'
        }
    }