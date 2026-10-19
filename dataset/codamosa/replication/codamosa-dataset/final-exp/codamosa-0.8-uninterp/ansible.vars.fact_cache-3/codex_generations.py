

# Generated at 2022-06-13 17:07:35.310807
# Unit test for constructor of class FactCache
def test_FactCache():
    """Unit test for constructor of class FactCache"""
    facts = FactCache()

    assert isinstance(facts, MutableMapping)
    assert not facts

    facts['key1'] = 'value1'

    assert 'key1' in facts
    assert len(facts) == 1


# Generated at 2022-06-13 17:07:45.729596
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('127.0.0.1', {'1':'1'})
    assert cache['127.0.0.1'] == {'1':'1'}
    cache.first_order_merge('127.0.0.1', {'2':'2'})
    assert cache['127.0.0.1'] == {'1':'1', '2':'2'}
    cache.first_order_merge('127.0.0.1', {'1':'3'})
    assert cache['127.0.0.1'] == {'1':'3', '2':'2'}
    cache.first_order_merge('127.0.0.2', {'3':'3'})

# Generated at 2022-06-13 17:07:53.734488
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    f = FactCache()
    f.first_order_merge('host1', {'key1': 'value1'})
    assert f['host1']['key1'] == 'value1'
    f.first_order_merge('host1', {'key2': 'value2'})
    assert f['host1']['key2'] == 'value2'
    f.first_order_merge('host1', {'key1': 'value3'})
    assert f['host1']['key1'] == 'value3'
    f.flush()

# Generated at 2022-06-13 17:07:59.903085
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """
    Test the 'first_order_merge' method of class FactCache.
    Creates a FactCache object and uses it to emulates the
    behaviour of the 'first_order_merge' method in the play context.
    :return:
    """
    fact_cache = FactCache()

    host1 = 'host1'
    host2 = 'host2'

    facts1 = {'facts1': {'fact1': 'fact1'}}
    facts2 = {'facts2': {'fact2': 'fact2'}}

    fact_cache.first_order_merge(host1, facts1)
    fact_cache.first_order_merge(host2, facts2)


# Generated at 2022-06-13 17:08:04.758022
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    a_dict = {'test_key' : 'test_value'}
    a_dict_updated = {'test_key' : 'updated_value'}

    return "[" + str(fact_cache.first_order_merge('test_host', a_dict)) + "]"

# Generated at 2022-06-13 17:08:09.789609
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert fc.keys() == fc.__iter__()
    assert fc.copy() == dict(fc)
    fc['foo'] = 'bar'
    assert 'foo' in fc
    assert fc.__contains__('foo')
    assert fc.__getitem__('foo') == 'bar'
    assert fc.__len__() == 1
    fc.flush()
    assert fc.__len__() == 0

# Generated at 2022-06-13 17:08:10.333079
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()

# Generated at 2022-06-13 17:08:11.981958
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        obj = FactCache()
        assert True
    except Exception:
        assert False


# Generated at 2022-06-13 17:08:12.878572
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:08:17.786569
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache['test'] = {'a': 1, 'b': 2}
    fact_cache.first_order_merge('test', {'a': 3, 'c': 4})
    assert(fact_cache['test'] == {'a': 3, 'b': 2, 'c': 4})

# Generated at 2022-06-13 17:08:29.361909
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.jsonfile import CacheModule as json_cache
    cache_loader.add('jsonfile', json_cache)
    C.CACHE_PLUGIN = 'jsonfile'
    C.CACHE_PLUGIN_CONNECTION = 'memory'
    cache = FactCache('')
    assert cache._plugin.name == 'jsonfile'
    cache['hostname.localdomain'] = {'hostvars': {}}
    assert 'hostname.localdomain' in cache
    assert len(cache) == 1
    assert list(cache) == ['hostname.localdomain']
    assert cache['hostname.localdomain'] == {'hostvars': {}}
    del cache['hostname.localdomain']
    assert len(cache) == 0

# Generated at 2022-06-13 17:08:35.541985
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Test case where the host_cache is absent
    host_facts = {'key': 'value'}
    fact_cache.first_order_merge('key', 'value')
    assert host_facts.keys() == fact_cache.keys()
    assert host_facts == fact_cache.copy()

    # Test case where the host_cache is present and has some facts
    host_facts = {'key': 'value'}
    fact_cache.first_order_merge('key', 'value')
    assert host_facts.keys() == fact_cache.keys()
    assert host_facts == fact_cache.copy()

# Generated at 2022-06-13 17:08:40.062550
# Unit test for constructor of class FactCache
def test_FactCache():

    # Using Ansible's display instance here so that the whole test module
    # doesn't have to be run with -v
    display.verbosity = 6

    # If the cache plugin can't be found then this will raise an error
    fact_cache = FactCache()


# Unit tests for the getter/setter methods of class FactCache

# Generated at 2022-06-13 17:08:41.311893
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    if not isinstance(fact_cache, FactCache):
        raise AssertionError


# Generated at 2022-06-13 17:08:42.477087
# Unit test for constructor of class FactCache
def test_FactCache():

    fc = FactCache()
    assert fc is not None
    # assert type(fc) == FactCache


# Generated at 2022-06-13 17:08:43.403369
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()


# Generated at 2022-06-13 17:08:46.693546
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3

    # init object
    factCache = FactCache()

    # check init object
    assert isinstance(factCache._plugin, cache_loader.get(C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:08:48.550319
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    hostname = 'localhost'
    key = 'test_fact'
    value = {'a':'b'}
    fc.first_order_merge(hostname, key, value)
    assert key in fc
    assert fc[key] == value


# Generated at 2022-06-13 17:08:54.433976
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache_object = FactCache()

    # Verify we can add a new key and value to the facts cache
    factcache_object.first_order_merge("test_key", "test_value")
    assert factcache_object["test_key"] == "test_value"

    # Verify we can update the value of an existing key
    factcache_object.first_order_merge("test_key", "updated_value")
    assert factcache_object["test_key"] == "updated_value"

# Generated at 2022-06-13 17:08:58.527226
# Unit test for constructor of class FactCache
def test_FactCache():
    # instantiate
    cache = FactCache()
    # Should be able to set arbitrary key
    key = "mykey"
    value = "myvalue"
    cache[key] = value

    assert(key in cache)
    # Should be able to get key
    assert(cache[key] == value)
    # Should be able to delete key
    del cache[key]
    assert(key not in cache)

# Generated at 2022-06-13 17:09:01.893885
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()



# Generated at 2022-06-13 17:09:11.066251
# Unit test for constructor of class FactCache
def test_FactCache():
    # test with pass plugin
    factsCache = FactCache(CACHE_PLUGIN='memory')
    #add data to cache
    factsCache['user']='user1'
    # test with fail plugin
    try:
        factsCache = FactCache(CACHE_PLUGIN='null')
    except AnsibleError:
        assert True

    # test with null plugin
    factsCache = FactCache(CACHE_PLUGIN='null')
    assert factsCache['user'] == 'user1'
    # test with exist plugin
    assert factsCache._plugin
    # remove data from cache
    del factsCache['user']
    #test with not exist data
    try:
        factsCache['user']
    except KeyError:
        assert True
    # test with empty cache
    assert factsCache.keys() == []
    #add

# Generated at 2022-06-13 17:09:12.892485
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    cache._plugin = MagicMock()
    cache.__init__()

# Generated at 2022-06-13 17:09:17.726073
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    host_facts1 = dict(ansible_hostname='host1')
    host_facts2 = dict(ansible_hostname='host2')

    cache.first_order_merge('host1', host_facts1)

    assert len(cache.keys()) == 1
    assert cache['host1'] == host_facts1

    cache.first_order_merge('host1', host_facts2)

    assert len(cache.keys()) == 1
    assert cache['host1'] == host_facts2

# Generated at 2022-06-13 17:09:19.706838
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    # following is assertion that
    # importing the required libraries
    # and creation of the fact cache succeeds
    assert isinstance(fact_cache, Cache)

# Generated at 2022-06-13 17:09:23.230909
# Unit test for constructor of class FactCache
def test_FactCache():
    # Valid constructor
    fact_cache = FactCache()
    # Invalid constructor
    try:
        C.CACHE_PLUGIN = "Invalid"
        fact_cache = FactCache()
    except Exception:
        assert True



# Generated at 2022-06-13 17:09:32.083616
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup
    new_facts = {
        "a": {
            "b": {
                "c": 1,
                "d": 2,
            },
        },
    }
    old_facts = {
        "a": {
            "b": {
                "d": 3,
            },
        },
    }
    cache = {
        "host_name": old_facts,
    }

    expected = {
        "host_name": {
            "a": {
                "b": {
                    "d": 3,
                },
            },
        },
    }

    # Test
    f = FactCache(cache)
    f.first_order_merge("host_name", new_facts)

    assert f == expected



# Generated at 2022-06-13 17:09:32.594006
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

# Generated at 2022-06-13 17:09:33.116766
# Unit test for constructor of class FactCache
def test_FactCache():
  factcache = FactCache()


# Generated at 2022-06-13 17:09:38.864183
# Unit test for constructor of class FactCache
def test_FactCache():
    factCache = FactCache()
    factCache.__setitem__('test','test')
    assert factCache.__contains__('test') == True
    assert factCache.__getitem__('test') == 'test'
    assert factCache.__iter__() != None
    assert factCache.__len__() == 1
    assert factCache.keys() == ['test']
    factCache.__delitem__('test')
    assert factCache.__contains__('test') == False
    assert factCache.__len__() == 0
    factCache.flush()
    assert factCache.__len__() == 0

# Generated at 2022-06-13 17:09:49.853733
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'key1'
    value = {'fact1': '1', 'fact2': '2'}
    # adding value for the first time
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value
    # updating value for existing key
    value = {'fact1': '11', 'fact2': '22'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'fact1': '11', 'fact2': '22'}

# Generated at 2022-06-13 17:09:58.477500
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Set the cache plugin
    cache_plugin = "jsonfile"

    # Create a fact_cache object
    fact_cache = FactCache(cache_plugin)

    # Set variables for mock data
    key = "localhost"
    cache_value = dict({'ansible_kernel': 'Linux', 'ansible_os_family': 'RedHat',
                        'ansible_distribution': 'CentOS', 'ansible_distribution_version': '6.4'})

    # Mock the cache value
    fact_cache[key] = cache_value

    # Set variables for test data
    value = dict({'ansible_distribution': 'CentOS', 'ansible_distribution_version': '6.4',
                  'ansible_kernel': 'linux', 'ansible_os_family': 'redhat'})

    # Run the test


# Generated at 2022-06-13 17:10:02.806111
# Unit test for constructor of class FactCache
def test_FactCache():
    global C
    C.CACHE_PLUGIN = 'memory'

    fact_cache = FactCache()
    assert fact_cache.keys() == []
    fact_cache.flush()

    fact_cache = FactCache(a=1)
    assert fact_cache.keys() == []
    fact_cache.flush()

# Generated at 2022-06-13 17:10:04.780391
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    display.debug(fc)

if __name__ == '__main__':
    # Execute this module to see the output.
    test_FactCache()

# Generated at 2022-06-13 17:10:12.228502
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    facts = {'version': {'release': "7.3.1611"}}
    cache.first_order_merge('127.0.0.1', facts)
    assert cache['127.0.0.1']['version']['release'] == "7.3.1611"
    facts = {'architecture': "x86_64"}
    cache.first_order_merge('127.0.0.1', facts)
    assert cache['127.0.0.1']['architecture'] == "x86_64"

# Generated at 2022-06-13 17:10:13.954947
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, collections.MutableMapping)

# Generated at 2022-06-13 17:10:23.758767
# Unit test for constructor of class FactCache
def test_FactCache():
    keys=['linux','windows','mac','unix','sun','linux','windows','mac','unix','sun','linux','windows','mac','unix','sun']
    keys=keys+keys+keys
    values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    values=values+values+values
    cachehostbatch=dict(zip(keys,values))
    cachehostbatch_keys=cachehostbatch.keys()
    #Set UUID in Cache Plugin
    C.CACHE_PLUGIN = "jsonfile"
    f = FactCache(cachehostbatch)
    # Test if all keys and values are cached
    assert f._plugin.contains(cachehostbatch_keys)
    # Test for fetch of cached value

# Generated at 2022-06-13 17:10:31.398172
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    # empty cache
    assert not fact_cache.keys()
    fact_cache.first_order_merge('test_host', {'test_key': 'test_value'})
    assert len(fact_cache.keys()) == 1
    assert fact_cache['test_host']['test_key'] == 'test_value'
    fact_cache.first_order_merge('test_host', {'test_key': 'test_value2'})
    assert len(fact_cache.keys()) == 1
    assert fact_cache['test_host']['test_key'] == 'test_value2'
    fact_cache.first_order_merge('test_host', {'test_key2': 'test_value2'})
    assert len(fact_cache.keys()) == 1

# Generated at 2022-06-13 17:10:34.226145
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge(key = "key_one", value = {
        "facts": {
            "fact_one": "fact_one",
            "fact_two": "fact_two"
        }
    })
    host_cache = cache._plugin.get(key = "key_one")
    assert host_cache == {
        "facts": {
            "fact_one": "fact_one",
            "fact_two": "fact_two"
        }
    }

# Generated at 2022-06-13 17:10:45.989991
# Unit test for constructor of class FactCache
def test_FactCache():

    # Uncommenting this line will raise an exception with message:
    # "Unable to load the facts cache plugin (NotACache)."
    # C.CACHE_PLUGIN = 'NotACache'
    obj = FactCache()
    assert isinstance(obj, FactCache)
    assert isinstance(obj, MutableMapping)

    class NotACache:
        pass

    obj._plugin = NotACache()
    try:
        obj.__contains__('abc')
        assert False
    except AttributeError:
        assert True

    try:
        obj.__getitem__('abc')
        assert False
    except AttributeError:
        assert True

    try:
        obj.__setitem__('abc', 'def')
        assert False
    except AttributeError:
        assert True


# Generated at 2022-06-13 17:11:00.966965
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup local objects for testing
    factcache = FactCache()
    factcache['host1'] = {'fact1': 'val1', 'fact3': {'fact4': 'val4'}}
    factcache['host2'] = {'fact1': 'val1', 'fact2': ['val2', 'val2'], 'fact3': 'val3'}

    # Create an object of type MutableMapping
    class MyMapping(MutableMapping):
        def __init__(self, *args, **kwargs):
            self._store = dict()
            self.update(dict(*args, **kwargs))

        def __getitem__(self, key):
            return self._store[key]

        def __setitem__(self, key, value):
            self._store[key] = value


# Generated at 2022-06-13 17:11:04.226391
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.common._collections_compat import Mapping

    assert isinstance(FactCache(), Mapping)


# Generated at 2022-06-13 17:11:12.173608
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_fact_cache = FactCache()
    test_fact_cache.first_order_merge("test", {"a": 1, "b": 2})
    assert test_fact_cache['test']["a"] == 1
    assert test_fact_cache['test']["b"] == 2
    test_fact_cache.first_order_merge("test", {"a": 3, "c": 4})
    assert test_fact_cache['test']["a"] == 3
    assert test_fact_cache['test']["b"] == 2
    assert test_fact_cache['test']["c"] == 4

# Generated at 2022-06-13 17:11:19.069613
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Create an instance of FactCache
    fact_cache = FactCache()
    # Add some items into the cache

# Generated at 2022-06-13 17:11:24.994281
# Unit test for constructor of class FactCache
def test_FactCache():

    with open("./test/unit/modules/test_fact_cache.py", "r") as f:
        code_str = f.read()
    exec(code_str)

    fact_cache = FactCache()
    fact_cache.__init__()

    fact_cache = FactCache()
    if not fact_cache._plugin:
        raise Exception('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:11:27.184384
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)
    assert isinstance(fc, MutableMapping)


# Generated at 2022-06-13 17:11:36.744686
# Unit test for constructor of class FactCache
def test_FactCache():
    from six import StringIO
    from ansible.module_utils.six import binary_type

    ansible_stdout = StringIO()
    display.verbosity = 3  # make sure to show messages (lowest level)
    display.ansible_stdout = ansible_stdout

    # Create object for FactCache class
    fact_cache = FactCache()
    # Test FactCache object
    assert fact_cache

    fact_cache["cache_key_1"] = "cache_value_1"
    fact_cache["cache_key_2"] = "cache_value_2"
    fact_cache["cache_key_3"] = "cache_value_3"

    # Read cache_key_2
    assert fact_cache["cache_key_2"] == "cache_value_2"

    # Delete cache_key_3
   

# Generated at 2022-06-13 17:11:44.772230
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache.first_order_merge("127.0.0.1", {'key1': 'value1'})
    assert factcache.get('127.0.0.1') == {'key1': 'value1'}

    factcache.first_order_merge("127.0.0.1", {'key2': 'value2'})
    assert factcache.get('127.0.0.1') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2022-06-13 17:11:54.134008
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.memory import FactCacheModule as testcache
    from ansible.constants import CACHE_PLUGIN

    assert testcache.__class__.__name__ == 'MemoryCacheModule'
    C.CACHE_PLUGIN = 'memory'
    fact_cache = FactCache()
    assert fact_cache._plugin.__class__.__name__ == 'MemoryCacheModule'
    assert fact_cache.keys() == []
    try:
        fact_cache.__getitem__('test')
        assert False
    except KeyError:
        assert True
    try:
        fact_cache.__delitem__('test')
        assert False
    except KeyError:
        assert True
    fact_cache.__setitem__('testkey', 'testval')

# Generated at 2022-06-13 17:12:01.749408
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    # Test the case where value is an empty dict
    host_facts = {'test_key': {}}
    fact_cache.first_order_merge('test_key', host_facts['test_key'])
    assert fact_cache == host_facts
    assert fact_cache['test_key'] == {}
    # Test the case where value is a dict with an element
    fact_cache = FactCache()
    host_facts = {'test_key': {'test_value': 'test_value'}}
    fact_cache.first_order_merge('test_key', host_facts['test_key'])
    assert fact_cache == host_facts
    assert fact_cache['test_key'] == {'test_value': 'test_value'}
    # Test the case where the cache

# Generated at 2022-06-13 17:12:14.390336
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert isinstance(fact_cache._plugin, cache_loader.get(C.CACHE_PLUGIN))


# Generated at 2022-06-13 17:12:15.173822
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:12:16.183080
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache is not None)


# Generated at 2022-06-13 17:12:20.587382
# Unit test for constructor of class FactCache
def test_FactCache():
    # setup
    plugin_key = 'cache'
    plugin_instance = 'memory'
    cache_dict = dict()

    # testing
    fact_cache = FactCache({'CACHE_PLUGIN': plugin_instance})

    # assertion
    assert fact_cache._plugin.get_cache_plugin_name() == plugin_key
    assert fact_cache._plugin.get_plugin_instance_name() == plugin_instance


# Generated at 2022-06-13 17:12:21.710942
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)



# Generated at 2022-06-13 17:12:23.318419
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.common._collections_compat import MutableMapping
    assert issubclass(FactCache, MutableMapping)

# Generated at 2022-06-13 17:12:27.219989
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Pre-req: fact_cache == {}
    # fact_cache only contains cached results of fact gathering
    fact_cache = FactCache()
    assert len(fact_cache.keys()) == 0

    # Pre-req: value == {'ansible_os_family': 'Debian'}
    # value is new result of fact gathering
    value = {'ansible_os_family': 'Debian'}

    # 1st call to first_order_merge:
    # key == '127.0.0.1' (first time cache is populated)
    # fact_cache == {'127.0.0.1': {'ansible_os_family': 'Debian'}}
    key = '127.0.0.1'
    fact_cache.first_order_merge(key, value)

# Generated at 2022-06-13 17:12:35.183011
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.plugins import cache as cache_module
    #Mocking _get_cache_instance method using mock_get_cache_instance
    cache_module._get_cache_instance = mock_get_cache_instance
    cache_obj = cache_module.get_cache(
        'redis',
        'redis_host',
        'redis_port',
        0,
        'redis_db',
        expire=86400
    )
    cache_obj.set('host_name', {'test_key': 'test_value'})
    cache_obj.set('host_name2', {'test_key': 'test_value'})
    fact_cache = FactCache()

# Generated at 2022-06-13 17:12:36.003944
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    return fact_cache

# Generated at 2022-06-13 17:12:42.099443
# Unit test for constructor of class FactCache
def test_FactCache():
    # Instantiate the class
    obj = FactCache()

    # Add an item to the `dict` of the object
    obj['key_name'] = 'value'

    # Check if the `dict` contains the key
    if 'key_name' in obj:
        del obj['key_name']

    # Check if the `dict` does not contain the key
    if 'key_name' not in obj:
        pass

    # Get the `dict` of the object
    dict_obj = obj.copy()

# Generated at 2022-06-13 17:13:09.827747
# Unit test for constructor of class FactCache
def test_FactCache():
    display.display = MockDisplay()
    fact_cache = FactCache()


# Generated at 2022-06-13 17:13:14.076504
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_cache = {'foo': 'bar', 'fizz': 'buzz'}
    fact_cache._plugin._fact_cache_cache.update(host_cache)
    host_facts = {'1': '2', '3': '4'}
    fact_cache.first_order_merge('test', host_facts)

    assert fact_cache['test'] == host_facts

# Generated at 2022-06-13 17:13:18.596508
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()

    assert fact_cache == {}

    host_facts = {'foo': 'bar'}
    host_cache = {'foo': 'bar', 'buz': 'quux'}

    fact_cache[hostname] = host_cache
    assert fact_cache[hostname] == host_cache
    fact_cache.first_order_merge(hostname, host_facts)
    assert fact_cache[hostname] == host_cache

# Generated at 2022-06-13 17:13:22.703700
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert 'localhost' not in fact_cache
    fact_cache['localhost'] = 'bigtime'
    assert 'localhost' in fact_cache
    del fact_cache['localhost']
    assert 'localhost' not in fact_cache
    fact_cache.flush()

# Generated at 2022-06-13 17:13:25.791330
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import FactCacheModule
    from ansible.module_utils.common._collections_compat import MutableMapping
    fact_cache = FactCache(FactCacheModule())
    assert isinstance(fact_cache, MutableMapping)


# Generated at 2022-06-13 17:13:26.265814
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

# Generated at 2022-06-13 17:13:31.392712
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_facts = {'version': 6, 'release': '3.4', 'kernel': '2.6.32'}
    fact_cache = FactCache({'foo': 'bar'})
    fact_cache.first_order_merge('foo', test_facts)
    assert fact_cache['foo']['version'] == 6
    assert fact_cache['foo']['release'] == '3.4'
    assert fact_cache['foo']['kernel'] == '2.6.32'



# Generated at 2022-06-13 17:13:34.617726
# Unit test for constructor of class FactCache
def test_FactCache():

    from ansible.cache.memory import MemoryCacheModule
    from ansible.plugins.loader import cache_loader

    cache_loader.add(C.CACHE_PLUGIN, MemoryCacheModule())
    fc = FactCache()
    assert fc is not None

# Generated at 2022-06-13 17:13:42.561913
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    local_facts = {u'is_vm': u'True'}
    host = u'host1'
    cache = {}
    host_facts = {u'is_vm': u'True'}

    cache = FactCache()
    cache[host] = {}
    cache.first_order_merge(host, local_facts)
    assert cache[host] == host_facts

    cache[host] = host_facts
    cache.first_order_merge(host, local_facts)
    assert cache[host] == host_facts

    cache = {host: {}}
    cache[host].update(host_facts)
    assert cache == host_facts
    cache[host].update(local_facts)
    assert cache == host_facts

# Generated at 2022-06-13 17:13:45.810579
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    c = FactCache()
    c.first_order_merge('key', {'foo':'bar'})
    assert c['key'] == {'foo':'bar'}
    c.first_order_merge('key', {'foo2':'bar2'})
    assert c['key'] == {'foo':'bar', 'foo2':'bar2'}

# Generated at 2022-06-13 17:14:42.759068
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache

    if not cache:
        raise Exception("Failed test_FactCache")

# Generated at 2022-06-13 17:14:45.686131
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert 'plugin' in facts.__dict__.keys()
    assert '_plugin' in facts.__dict__.keys()
    assert '__init__' in facts.__dict__.keys()

# Generated at 2022-06-13 17:14:47.388310
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache()
    except ValueError as e:
        print(e)


# Generated at 2022-06-13 17:14:48.486106
# Unit test for constructor of class FactCache
def test_FactCache():
    test = FactCache()
    assert type(test) is FactCache
    assert test.get('test') is None


# Generated at 2022-06-13 17:14:50.612278
# Unit test for constructor of class FactCache
def test_FactCache():
    # Check if fact cache is created
    cache = FactCache()
    assert isinstance(cache, MutableMapping)



# Generated at 2022-06-13 17:14:52.826187
# Unit test for constructor of class FactCache
def test_FactCache():
    F=FactCache()
    assert F
    assert F._plugin

# Generated at 2022-06-13 17:14:58.627142
# Unit test for constructor of class FactCache
def test_FactCache():
    # Initialize the fact cache
    fact_cache = FactCache()

    # Add a dictionary of facts to the fact cache
    fact_cache["localhost"] = dict({"ansible_facts": dict({"ansible_hostname": "localhost.localdomain"})})

    # Check that the above fact has been successfully added to the fact cache
    assert fact_cache["localhost"]["ansible_facts"]["ansible_hostname"] == "localhost.localdomain"

# Generated at 2022-06-13 17:15:03.511547
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('testing', {'testing': 'testing'})
    assert fact_cache['testing']['testing'] == 'testing'
    fact_cache.first_order_merge('testing', {'testing': 'overwriting'})
    assert fact_cache['testing']['testing'] == 'overwriting'
    assert fact_cache['testing']['testing'] != 'testing'

# Generated at 2022-06-13 17:15:09.641441
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """
    Tests the first_order_merge method of class FactCache.  Assumes that
    the __init__ method of the class does not fail
    """

    c = FactCache()
    host_facts = {'first_fact': 'first_value'}

    try:
        c.first_order_merge('first_fact', host_facts['first_fact'])
        assert c['first_fact'] == host_facts['first_fact']
    except KeyError:
        # If the fact is not in the local cache or in the cache plugin,
        # the first_order_merge method should add it to the local cache
        assert False

    # Add to the local cache and the cache plugin
    c.first_order_merge('second_fact', {'second_fact': 'second_value'})

# Generated at 2022-06-13 17:15:10.727386
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc.keys() == []

# Generated at 2022-06-13 17:17:07.920692
# Unit test for constructor of class FactCache
def test_FactCache():
    class Plugin:
        def get(self, key=''):
            return {}

        def set(self, key='', value={}):
            return []

    plugin = Plugin()
    assert isinstance(FactCache(plugin), FactCache)

# Generated at 2022-06-13 17:17:10.782897
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache(
        display=display
    )

    # Expecting a dict and not an object
    if isinstance(fact_cache, MutableMapping):
        pass
    else:
        raise AssertionError("Expected a dict and not an object")


# Generated at 2022-06-13 17:17:12.006818
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin != None
    assert type(cache) == FactCache

# Generated at 2022-06-13 17:17:12.689608
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc != None

# Generated at 2022-06-13 17:17:16.150469
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('127.0.0.1', {'foo': 'bar'})
    assert fact_cache.first_order_merge('127.0.0.1', {'baz': 'qux'}) == {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 17:17:26.504580
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import datetime
    from ansible.module_utils._text import to_bytes

    test_facts = {'facts': {'test': 'test'}}
    hostname = 'test.example.org'
    facts_content = {
        'test.example.org': {
            'test': 'test',
            '_ansible_no_log': False,
            '_ansible_verbose_always': True,
            '_ansible_version': to_bytes(datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")),
        }
    }
    expected = {'test.example.org': {'test': 'test'}}

    class mock_plugin(object):
        def __init__(self):
            self.cache = facts_content


# Generated at 2022-06-13 17:17:27.780342
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc._plugin, cache_loader.get(C.CACHE_PLUGIN))


# Generated at 2022-06-13 17:17:28.400422
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    cache.flush()