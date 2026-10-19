

# Generated at 2022-06-13 17:07:39.018621
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Prepare test
    fact_cache = FactCache()
    fact_cache._plugin.set('foo', {'bar': 'baz'})

    # Execute method
    fact_cache.first_order_merge('foo', {'bar': 'baz'})

    # Retrieve test
    assert len(fact_cache.copy()) == 1
    assert fact_cache.copy()['foo']['bar'] == 'baz'

# Generated at 2022-06-13 17:07:47.893378
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    facts_cache = FactCache()
    test_host = 'testhost.ansible.com'
    random_variable = 'random_variable'

    assert not facts_cache

    assert test_host not in facts_cache

    # update host in cache with new facts
    facts_cache.first_order_merge(test_host, {random_variable: 1})
    assert test_host in facts_cache

    # test that the host is there and that the facts are correct
    assert facts_cache[test_host][random_variable] == 1
    assert facts_cache[test_host].get(random_variable) == 1

    # update host in cache with new facts
    facts_cache.first_order_merge(test_host, {random_variable: 2})
    assert test_host in facts_cache

    # test that the host is

# Generated at 2022-06-13 17:07:57.203884
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host="127.0.0.1"
    fact_cache.first_order_merge(host, {"a": 1}) == {host: {"a": 1}}
    fact_cache.first_order_merge(host, {"b": 2}) == {host: {"a": 1, "b": 2}}
    fact_cache.first_order_merge(host, {"a": 3}) == {host: {"a": 3, "b": 2}}
    fact_cache.first_order_merge(host, {"c": 3}) == {host: {"a": 3, "b": 2, "c": 3}}
    fact_cache.first_order_merge(host, {"a": 1}) == {host: {"a": 1, "b": 2, "c": 3}}
    fact_

# Generated at 2022-06-13 17:08:04.324785
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()

    cache_key = 'localhost'
    cache_value = {'foo': 'bar'}
    fact_cache.first_order_merge(cache_key, cache_value)
    fact_cache.first_order_merge(cache_key, {'foo': 'foo'})
    assert fact_cache[cache_key] == {'foo': 'foo'}

# Generated at 2022-06-13 17:08:06.313580
# Unit test for constructor of class FactCache
def test_FactCache():
    factCache = FactCache()
    assert factCache._plugin == cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:08:10.088261
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    test_cache.first_order_merge('foo', {'bar': 'baz'})

    assert test_cache.get('foo') == {'bar': 'baz'}

    test_cache.first_order_merge('foo', {'bar': 'baz2'})

    assert test_cache.get('foo') == {'bar': 'baz2'}

# Generated at 2022-06-13 17:08:17.835599
# Unit test for constructor of class FactCache
def test_FactCache():

    # check for bad CACHE_PLUGIN value
    orig_cache_plugin = C.CACHE_PLUGIN
    try:
        C.CACHE_PLUGIN = 'foo'
        try:
            cache = FactCache()
            assert False, "failed to raise error on bad CACHE_PLUGIN value"
        except AnsibleError:
            # expected error
            pass
    finally:
        C.CACHE_PLUGIN = orig_cache_plugin

    # check for valid CACHE_PLUGIN value
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:08:18.595006
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:08:20.195741
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache()._plugin, MutableMapping)


# Generated at 2022-06-13 17:08:30.436293
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_facts = {'ansible_distribution': 'Ubuntu', 'ansible_distribution_version': '14.10'}
    hostname = 'test_hostname'

    # Initialize fact_cache
    fact_cache = FactCache()

    # Run first_order_merge method
    fact_cache.first_order_merge(hostname, host_facts)

    # Verify that fact cache contains the hostname
    assert hostname in fact_cache

    # Verify that self contains the hostname
    assert hostname in fact_cache

    # Verify that fact cache contains the key ansible_distribution
    assert 'ansible_distribution' in fact_cache[hostname]

    # Verify that fact cache contains the key ansible_distribution_version

# Generated at 2022-06-13 17:08:32.714217
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache

# Generated at 2022-06-13 17:08:37.290559
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader, action_loader

    fact_cache = FactCache()

    # Check that fact cache is properly initialized
    assert fact_cache is not None
    assert fact_cache._plugin is not None
    assert fact_cache._plugin.__class__ is cache_loader.get(C.CACHE_PLUGIN).__class__
    # Check that the action loader has access to the fact cache
    assert action_loader._shared_loader_obj.fact_cache is fact_cache

# Generated at 2022-06-13 17:08:45.768099
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import unittest
    import tempfile
    import os

    class TestPlugin:

        def __init__(self, file_path):
            self._file_path = file_path

        def set(self, key, value):
            if key in self.__fs:
                self.__fs[key].update(value)
            else:
                self.__fs[key] = value

        def contains(self, key):
            return key in self.__fs

        def get(self, key):
            return self.__fs[key]

        def delete(self, key):
            del self.__fs[key]

        def keys(self):
            return self.__fs.keys()

        def flush(self):
            for key in self.__fs:
                del self.__fs[key]


# Generated at 2022-06-13 17:08:46.883215
# Unit test for constructor of class FactCache
def test_FactCache():
    fca = FactCache()
    assert isinstance(fca, FactCache)

# Generated at 2022-06-13 17:08:48.642634
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin ==  cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:08:50.416571
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache, "Constructor of class FactCache is not working"

# Generated at 2022-06-13 17:08:51.331202
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f is not None

# Generated at 2022-06-13 17:08:56.545170
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    f = FactCache()

    d1 = {'a': 1}
    d2 = {'a': 2}
    d3 = {'a': 3}

    f['host1'] = d1
    f.first_order_merge('host1', d2)
    assert f['host1'] == {'a': 2}

    f.first_order_merge('host2', d3)
    assert f['host2'] == {'a': 3}

# Generated at 2022-06-13 17:08:57.620497
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()


# Generated at 2022-06-13 17:08:58.898003
# Unit test for constructor of class FactCache
def test_FactCache():
    a = FactCache()


# Generated at 2022-06-13 17:09:03.275093
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None



# Generated at 2022-06-13 17:09:06.031908
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    try:
        assert fact_cache._plugin
    except:
        raise ValueError
    return fact_cache


# Generated at 2022-06-13 17:09:07.534714
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc.copy() == {}
    assert isinstance(fc, MutableMapping)

# Generated at 2022-06-13 17:09:08.763600
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    # TODO: Add more unit tests


# Generated at 2022-06-13 17:09:09.658497
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache
    assert cache._plugin


# Generated at 2022-06-13 17:09:12.969935
# Unit test for constructor of class FactCache
def test_FactCache():
    ansible_fact_cache = FactCache()
    assert isinstance(ansible_fact_cache, FactCache), 'ansible_fact_cache should be FactCache instance'

# Generated at 2022-06-13 17:09:16.990189
# Unit test for constructor of class FactCache
def test_FactCache():
    data = dict()
    data["_plugin"] = cache_loader.get(C.CACHE_PLUGIN)
    display.display("_plugin: %s" % (data["_plugin"]))
    assert (data["_plugin"] is not None)

    fact_cache = FactCache()
    display.display("FactCache: %s" % (fact_cache))
    assert (fact_cache is not None)
    return;


# Generated at 2022-06-13 17:09:17.726000
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:09:22.362113
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.flush()
    cache.first_order_merge("host1", {"ansible_all_ipv4_addresses": ["192.168.1.1", "192.168.1.2"], "ansible_all_ipv6_addresses": ["fe80::1"], "ansible_default_ipv4": {"address": "192.168.1.1", "netmask": "255.255.255.0"}})

# Generated at 2022-06-13 17:09:27.177207
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('127.0.0.1', {'foo': 'bar'})
    fc.first_order_merge('127.0.0.1', {'foo': 'bla'})
    assert fc['127.0.0.1']['foo'] == 'bla'

# Generated at 2022-06-13 17:09:34.850979
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_factory = {}
    plugin = cache_loader.get('memory')
    cache_factory['memory'] = plugin
    cache = FactCache()
    cache['testkey'] = 'testvalue'
    assert cache['testkey'] == 'testvalue'
    cache.flush()

# Generated at 2022-06-13 17:09:35.937513
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    print (fc.flush())

# Generated at 2022-06-13 17:09:36.682478
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:09:42.678649
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # create a test cache object, set first_order_merge on it.
    test_cache = FactCache(C.CACHE_PLUGIN)

    # create a test dict object
    test_dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    # create a second test dict object
    test_dict2 = {'one': 1, 'two': 2, 'three': 3, 'four': 1, 'five': 5, 'six': 6}

    # test_cache should be empty
    assert len(test_cache) == 0

    # calls first_order_merge to update the cache
    test_cache.first_order_merge('host_name', test_dict1)

    # test_cache should not be empty

# Generated at 2022-06-13 17:09:44.819770
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert len(fact_cache.keys()) == 0
    assert fact_cache._plugin



# Generated at 2022-06-13 17:09:50.795446
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test only when `CACHE_PLUGIN` is not set, because the plugin creation
    # will be tested by other UT
    if not C.CACHE_PLUGIN:
        try:
            fact_cache = FactCache()
        except AnsibleError:
            pass
        assert fact_cache is not None
        assert fact_cache.flush() is None
        assert fact_cache.keys() == []

# Generated at 2022-06-13 17:09:53.218505
# Unit test for constructor of class FactCache
def test_FactCache():
    display.vvvv('@@@ FactCache.__init__()')
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:10:00.517956
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    host_facts = {
        'ansible_distribution': 'CentOS',
        'ansible_distribution_version': '6.9',
        'ansible_distribution_release': 'Final'
    }
    
    facts_cache.update(host_facts)
    updated_facts = {
        'ansible_distribution': 'Fedora',
        'ansible_distribution_major_version': '28',
        'ansible_distribution_release': '1.2.3'
    }
    facts_cache.first_order_merge('testhost', updated_facts)

# Generated at 2022-06-13 17:10:02.695322
# Unit test for constructor of class FactCache
def test_FactCache():
    fac_cache = FactCache()
    assert fac_cache._plugin is not None


# Generated at 2022-06-13 17:10:08.637054
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
        fc['key'] = 'value'
    except Exception as e:
        # If we have an exception here, we failed at the constructor level
        assert False, "test_FactCache: constructor test of FactCache failed with: %s" % to_text(e)

    # Verify we stored the key
    assert 'key' in fc.keys(), "test_FactCache: missing key"

    # Verify we can get the key back
    assert 'key' in fc, "test_FactCache: key not in"
    assert fc.get('key') == 'value', "test_FactCache: value not as expected"

    assert 'key' in fc.copy(), "test_FactCache: copy() missing key"

    # Verify we can delete the key
    del fc['key']


# Generated at 2022-06-13 17:10:22.869142
# Unit test for constructor of class FactCache
def test_FactCache():

    test_fact_cache = FactCache()
    assert test_fact_cache._plugin
    assert test_fact_cache._plugin.keys()==[]

# Generated at 2022-06-13 17:10:24.075067
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:10:31.597946
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('key', {'a': 1, 'b': 'val', 'c': True})

    # Test overwriting existing key
    fact_cache.first_order_merge('key', {'a': 2, 'b': 'newval', 'd': False})
    assert fact_cache['key']['a'] == 2
    assert fact_cache['key']['b'] == 'newval'
    assert fact_cache['key']['c'] == True
    assert fact_cache['key']['d'] == False

    # Test adding a new key
    fact_cache.first_order_merge('key2', {'a': 2, 'b': 'newval', 'd': False})

# Generated at 2022-06-13 17:10:32.386353
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:33.990729
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

# Generated at 2022-06-13 17:10:36.511665
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin


# Generated at 2022-06-13 17:10:46.914121
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'test_key'
    value = {'test_fact_1': 1,
             'test_fact_2': 2,
             'test_fact_3': 3}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value
    value = {'test_fact_1': 4,
             'test_fact_2': 5,
             'test_fact_4': 6}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'test_fact_1': 4,
                               'test_fact_2': 5,
                               'test_fact_3': 3,
                               'test_fact_4': 6}

# Generated at 2022-06-13 17:10:56.392613
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.errors import AnsibleError
    from ansible import constants as C
    # Test that when we initialize FactCache, it will try to get a cache plugin.
    # If we don't supply the cache plugin, it should raise an error.
    try:
        FC_instance = FactCache()
        assert False
    except AnsibleError:
        assert True

    C.CACHE_PLUGIN = 'BasePlugin'
    # Test if the cache_plugin is available in C.CACHE_PLUGIN,
    # it should create the class instance.
    try:
        FC_instance = FactCache()
        assert True
    except AnsibleError:
        assert False



# Generated at 2022-06-13 17:11:06.417145
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    test_key = 'test_key'
    test_value = {'test_key': {'test_first': 'first', 'test_second': 'second'}}
    test_value_second = {'test_key': {'test_second': 'second', 'test_third': 'third'}}
    test_res = {'test_first': 'first', 'test_second': 'second', 'test_third': 'third'}
    test_cache.first_order_merge(test_key, test_value)
    test_cache.first_order_merge(test_key, test_value_second)
    assert test_res == test_cache[test_key]

# Generated at 2022-06-13 17:11:08.523681
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:11:36.744007
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:11:42.386864
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # testing empty cache
    key = 'system.platform'
    value = 'darwin'
    fact_cache.first_order_merge(key, value)
    assert fact_cache.get(key) == value

    # testing cache with existing value
    key = 'system.platform_family'
    value = 'Darwin'
    fact_cache.first_order_merge(key, value)
    assert fact_cache.get(key) == value

    # testing cache with existing value, _and_ existing value is a dict
    key = 'system.platform_family'
    value = {'a_dict_key': 'a_dict_value'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache.get(key) == value

# Generated at 2022-06-13 17:11:44.438805
# Unit test for constructor of class FactCache
def test_FactCache():
    fact={'ansible_system': 'Linux'}
    fc=FactCache()
    fc['host']=fact
    assert fact == fc['host']


# Generated at 2022-06-13 17:11:52.102990
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache_plugin = cache_loader.get('jsonfile')
    host_list = ['host1', 'host2', 'host3']
    fact_cache = FactCache(host_list, cache_plugin)
    key = 'host1'
    value = {'value1': 'host1', 'value2': 'host1'}
    host_cache = {'value1': 'host1'}
    cache_plugin.set(key, host_cache)
    fact_cache.first_order_merge(key, value)
    assert cache_plugin.get(key) == host_cache
    assert fact_cache[key] == value

# Generated at 2022-06-13 17:11:56.238252
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = "key"
    value = {"key1": "value1", "key2": "value2"}
    fact_cache.first_order_merge(key, value)
    assert (fact_cache[key]["key1"] == "value1")
    assert (fact_cache[key]["key2"] == "value2")

# Generated at 2022-06-13 17:12:00.555332
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_host = "hostname"
    test_facts = {u'ansible_facts': {u'one': 1, u'two': 2}}
    test_facts_copy = test_facts.copy()

    test = FactCache()
    test.first_order_merge(test_host, test_facts)
    assert test[test_host]['ansible_facts'] == test_facts_copy['ansible_facts']



# Generated at 2022-06-13 17:12:01.770537
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin
    assert cache._plugin.cache_name
    assert cache._plugin.cache_length


# Generated at 2022-06-13 17:12:02.980384
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert isinstance(f, FactCache)



# Generated at 2022-06-13 17:12:04.280107
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(cache_loader=cache_loader.CacheModule()), FactCache)

# Generated at 2022-06-13 17:12:13.072095
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import pytest
    m = FactCache()
    m["test1"] = {"key1": "value1"}
    # Update the dictionary with new value of "key1"
    m.first_order_merge("test1", {"key1": "value2"})
    assert m["test1"]["key1"] == "value2"
    # Append new key "key2"
    m.first_order_merge("test1", {"key2": "value3"})
    assert m["test1"]["key2"] == "value3"
    # test2 key should not exist
    with pytest.raises(KeyError) as e:
        m["test2"]
    assert e.type == KeyError

# Generated at 2022-06-13 17:13:11.877665
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    # Test that __init__ creates self._plugin correctly
    assert isinstance(fact_cache._plugin, cache_loader.get(C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:13:12.632213
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache


# Generated at 2022-06-13 17:13:19.506576
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # init the fact cache
    fact_cache = FactCache()
    display.display('fact cache: %s' % fact_cache)

    # get the plugin
    plugin = cache_loader.get('jsonfile')
    display.display('plugin: %s' % plugin)

    # test the plugin
    assert plugin.contains('test') is False
    assert plugin.get('test') is None
    plugin.set('test', 'test')
    assert plugin.contains('test') is True
    assert plugin.get('test') == 'test'
    plugin.delete('test')
    assert plugin.contains('test') is False

    # test the fact cache
    fact_cache['test'] = [{'a': 'test2'}]
    assert fact_cache['test'] == [{'a': 'test2'}]


# Generated at 2022-06-13 17:13:20.773318
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache)

# Generated at 2022-06-13 17:13:21.764592
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:13:30.078406
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import os
    import json
    import shutil
    from os.path import dirname, join
    from tempfile import mkdtemp

    # Required by cache_loader.get()
    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'jsonfile'
    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = join(mkdtemp(), 'ansible-test')
    os.makedirs(os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'])
    with open(join(dirname(os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION']), 'ansible.cfg'), 'w') as ansible_cfg:
        ansible_cfg.write('[defaults]\n')

# Generated at 2022-06-13 17:13:30.955262
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:13:31.882704
# Unit test for constructor of class FactCache
def test_FactCache():
    """ FactCache: test constructor """
    FactCache()

# Generated at 2022-06-13 17:13:37.093256
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Create a test instance of the class FactCache 
    cache = FactCache()
    # Create a test data structure to cache the facts
    # in this test case we are looking for a dictionary
    data = {'test1': 123, 'test2': 456}
    key = 'somekey'
    cache[key] = data
    # Adding a key which is existing in the cache to the new data
    # like the call of cache.first_order_merge('somekey', {'test1': 999}) 
    # would do.
    # The value in the cache should stay untouched
    data_with_update = {'test1': 999, 'test2': 456}
    cache.first_order_merge(key, data_with_update)
    assert cache[key] == data
    # Adding a key which is not existing in

# Generated at 2022-06-13 17:13:43.259279
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    for key in ("key1", "key2"):
        factcache.first_order_merge(key, {'key': 'value'})
    assert factcache.get("key1")['key'] == 'value'
    assert factcache.get("key2")['key'] == 'value'
    factcache.first_order_merge("key1", {'key': 'value2'})
    assert factcache.get("key1")['key'] == 'value2'
    assert factcache.get("key2")['key'] == 'value'
    factcache.flush()

# Generated at 2022-06-13 17:15:45.630945
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    class test_fact:
        def __init__(self, fact_name, fact_value):
            self.name = fact_name
            self.value = fact_value

    fact_cache = FactCache()

    fact_list = [test_fact("test_fact", "test_value"),
                 test_fact("test_fact_1", "test_value_1")]

    fact_cache.first_order_merge("test_host", fact_list[0])
    assert "test_host" in fact_cache
    assert fact_cache["test_host"]["test_fact"] == "test_value"

    fact_cache.first_order_merge("test_host", fact_list[1])
    assert "test_host" in fact_cache

# Generated at 2022-06-13 17:15:52.876870
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # https://realpython.com/blog/python/python-mock-quickstart/
    # https://docs.python.org/2/library/unittest.mock.html
    from ansible.module_utils.six import iteritems
    from ansible.plugins.cache.jsonfile import CacheModule as MockCacheModule
    from ansible.utils.collection_loader import all_collection_directories
    import os
    import shutil
    import tempfile
    import unittest

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary Ansible configuration directory
    tmpansiblecfg = os.path.join(tmpdir, 'ansible.cfg')
    os.mkdir(tmpansiblecfg)

# Generated at 2022-06-13 17:15:53.993395
# Unit test for constructor of class FactCache
def test_FactCache():
    # create factcache instance
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:16:04.432168
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factCache = FactCache()
    host_facts = {}
    host_cache = {'key1': None}
    factCache._plugin = cache_loader.get(C.CACHE_PLUGIN)
    factCache._plugin.set('host1', host_cache)
    host_facts['host1'] = host_cache
    assert('host1' in factCache._plugin.keys())
    assert(factCache._plugin.get('host1')['key1'] == None)
    factCache.first_order_merge('host1', {})
    assert(factCache._plugin.get('host1')['key1'] == None)
    factCache.first_order_merge('host1', {'key1': 'val1'})

# Generated at 2022-06-13 17:16:11.087820
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge(
        'some_host', {'ansible_lsb': {'distributor_id': 'Some_Distro'}})
    assert fact_cache['some_host']['ansible_lsb']['distributor_id'] == 'Some_Distro', 'Test 1: This should be Some_Distro'
    fact_cache.first_order_merge(
        'some_host', {'ansible_lsb': {'distributor_id': 'Another_Distro'}})
    assert fact_cache['some_host']['ansible_lsb']['distributor_id'] == 'Another_Distro', 'Test 2: This should be Another_Distro'

# Generated at 2022-06-13 17:16:11.498236
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:16:12.857655
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(isinstance(fact_cache, FactCache))

# Generated at 2022-06-13 17:16:18.057117
# Unit test for constructor of class FactCache
def test_FactCache():
    '''
    ansible.vars.FactCache:
    '''
    cache    = FactCache()
    assert cache

    with open(__file__, 'r') as f:
        data = f.read()

    cache['foo'] = data
    assert 'foo' in cache
    assert cache['foo'] == data
    assert len(cache) == 1

    cache.flush()
    assert len(cache) == 0

    with open(__file__, 'r') as f:
        data = f.read()

    cache['foo'] = data
    cache['bar'] = data

    assert len(cache) == 2

    cache.flush()
    assert len(cache) == 0

# Generated at 2022-06-13 17:16:19.119815
# Unit test for constructor of class FactCache
def test_FactCache():
    with pytest.raises(AnsibleError):
        FactCache(cache_plugin='foobar')

# Generated at 2022-06-13 17:16:19.676474
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache