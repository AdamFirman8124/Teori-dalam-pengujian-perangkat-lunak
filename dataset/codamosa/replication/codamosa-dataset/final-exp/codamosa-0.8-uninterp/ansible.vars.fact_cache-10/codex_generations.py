

# Generated at 2022-06-13 17:07:33.334864
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()  # noqa

# Generated at 2022-06-13 17:07:44.131855
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.flush()

    # create a copy of the facts that can be serialized to the cache
    hostvars = {'ansible_ssh_host': 'test.example.org',
                'ansible_ssh_port': 22}
    facts = {'test_host': hostvars}

    # create a dict of the facts that were received before the host facts were
    # flushed in the host action plugin
    host_cache = {'ansible_ssh_host': 'test.example.com',
                  'ansible_ssh_port': 2222}

    # serialize the previous facts for the host to the cache
    cache.first_order_merge('test_host', host_cache)

    # assert that the fact cache has been updated
    cache_facts = cache.copy()

# Generated at 2022-06-13 17:07:50.045197
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    m_plugin = MockPlugin("")
    fc = FactCache(_plugin=m_plugin)

    host_facts = {"setup": {"some_key": "some_value"}}
    m_plugin.add_key("test_host", host_facts)
    fc.first_order_merge("test_host", host_facts)
    assert fc["test_host"]["setup"]["some_key"] == "some_value"

    host_facts = {"setup": {"some_key": "other_value"}}
    fc.first_order_merge("test_host", host_facts)
    assert fc["test_host"]["setup"]["some_key"] == "some_value"


# MockPlugin is used to mock the functionality of the plugin cache.
# It is used to unit test the Fact

# Generated at 2022-06-13 17:07:55.470999
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    assert 'host1' not in fact_cache
    fact_cache.first_order_merge('host1', {'init_system': 'systemd'})
    assert 'host1' in fact_cache
    assert 'init_system' in fact_cache.keys()

    fact_cache.first_order_merge('host1', {'init_system': 'sysvinit'})
    assert fact_cache['host1']['init_system'] == 'sysvinit'

# Generated at 2022-06-13 17:07:56.772921
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)


# Generated at 2022-06-13 17:08:07.907787
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.flush()

    host_cache = {u'hostvars': {u'host1': {u'ansible_facts': {u'fact1': u'value1'}}}}
    cache[u'host1'] = host_cache

    new_facts = {u'fact1': u'new_value1'}
    cache.first_order_merge(u'host1', new_facts)

    host_cache[u'hostvars'][u'host1'][u'ansible_facts'].update(new_facts)

    # The following should fail, since the new_facts contain only one key-value pair.
    assert cache[u'host1'] == host_cache

    # The following should work, since the new_facts contain two key-value pairs.

# Generated at 2022-06-13 17:08:09.167820
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None


# Generated at 2022-06-13 17:08:19.575963
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    #with py.test.raises(AnsibleError):
    #    fact_cache.first_order_merge('127.0.0.1', {'an':'as'})
    fact_cache.first_order_merge('127.0.0.1', {'ansible_env':{'HOME':'/home/abcd'}, 'ansible_facts':{'os':'Linux', 'distribution':'CentOS'}})
    assert fact_cache['127.0.0.1']['ansible_env']['HOME'] == '/home/abcd'
    assert fact_cache['127.0.0.1']['ansible_facts']['os'] == 'Linux'
    print(fact_cache['127.0.0.1'])



# Generated at 2022-06-13 17:08:20.112248
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:08:26.189461
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    plugin._fact_cache = {'all': {'ansible_distribution': 'UNKNOWN'}}
    fact_cache = FactCache()
    assert fact_cache._plugin == plugin
    assert fact_cache.copy() == {'all': {'ansible_distribution': 'UNKNOWN'}}


# Generated at 2022-06-13 17:08:35.388676
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    class FakePlugin:
        def get(self, key):
            key_list = {'ansible_facts': {'test_one': 'foo', 'test_two': 'bar'}}
            return key_list.get(key)

        def contains(self, key):
            return True if self.get(key) is not None else False

        def set(self, key, value):
            pass

        def delete(self, key):
            pass

        def flush(self):
            pass

        def keys(self):
            return ['ansible_facts']

    cache_plugin = FakePlugin()
    fact_cache = FactCache(cache_plugin)
    value_data = {'test_two': 'baz'}
    fact_cache.first_order_merge('ansible_facts', value_data)
    cache_list

# Generated at 2022-06-13 17:08:44.551342
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''
    Unit test for method FactCache.first_order_merge
    '''
    cache = FactCache()
    key = 'inventory_hostname'
    hostA_facts = {'hello': 'world', 'a': 1, 'b': 2}
    hostB_facts = {'a': 1, 'b': 2, 'c': 3}

    # Test update empty cache
    cache.first_order_merge(key, hostA_facts)
    assert cache == {'inventory_hostname': {'hello': 'world', 'a': 1, 'b': 2}}
    assert cache._plugin.get(key) == {'hello': 'world', 'a': 1, 'b': 2}

    cache.flush()
    assert len(cache) == 0

    # Test update a non-empty cache
    cache.first

# Generated at 2022-06-13 17:08:48.642918
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = None
    try:
        facts = FactCache()
        facts['testkey'] = 'testvalue'
        assert facts['testkey'] == 'testvalue'
        assert 'testkey' in facts
        assert len(facts) == 1
        facts.flush()
        assert len(facts) == 0
    finally:
        if facts is not None:
            facts.flush()

# Generated at 2022-06-13 17:08:49.855729
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None


# Generated at 2022-06-13 17:08:50.968782
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), FactCache)

# Generated at 2022-06-13 17:08:52.941046
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert isinstance(facts, FactCache)
    assert isinstance(facts, MutableMapping)



# Generated at 2022-06-13 17:08:59.994346
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    import os
    from ansible.module_utils._text import to_text

    class FakePlugin(object):

        def __init__(self):
            self.cache = {}

        def contains(self, key):
            return key in self.cache

        def get(self, key):
            return self.cache.get(key)

        def set(self, key, value):
            self.cache[key] = value

        def delete(self, key):
            self.cache.pop(key, None)

        def flush(self):
            self.cache = {}

        def keys(self):
            return self.cache.keys()

    # Create a fake cache plugin
    plugin = FakePlugin()

    # Create a cache
    fact_cache = FactCache()
    fact_cache._plugin = plugin

    # Create a non-cached

# Generated at 2022-06-13 17:09:02.405266
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc



# Generated at 2022-06-13 17:09:11.289258
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    ''' FactCache.first_order_merge with different interactions '''
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Empty value for key
    fc = FactCache()
    fc.first_order_merge('testhost1', {})
    assert fc['testhost1'] == {}

    # Value for key
    fc = FactCache()
    fc.first_order_merge('testhost1', {'new_key': 'new_value'})
    assert fc['testhost1'] == {'new_key': 'new_value'}

    # Value for key, empty cache
    fc = FactCache()
    fc.first_order_merge('testhost1', {'new_key': 'new_value'})
    fc.first_order

# Generated at 2022-06-13 17:09:11.918445
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache("hostname")
    return fc

# Generated at 2022-06-13 17:09:20.132431
# Unit test for constructor of class FactCache
def test_FactCache():
    class CacheMock(object):
        def __contains__(self, key):
            return True

        def __getitem__(self, key):
            return {"key": "value"}

        def __setitem__(self, key, value):
            pass

        def __delitem__(self, key):
            pass

        def delete(self, key):
            pass

        def get(self, key):
            return {"key": "value"}

        def set(self, key, value):
            pass

        def keys(self):
            return "keys"

        def contains(self, key):
            return True

        def flush(self):
            pass

    f = FactCache()
    f._plugin = CacheMock()
    assert f["key"] == {'key': 'value'}

# Generated at 2022-06-13 17:09:22.750421
# Unit test for constructor of class FactCache
def test_FactCache():
    # Simple test, because we cannot test the caching mechanism itself from here
    cache = FactCache()
    assert len(cache) == 0
    # cache should be empty

# Generated at 2022-06-13 17:09:31.914191
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_key = "test_host"
    new_facts = {"new_key": "new_value"}
    old_facts = {"old_key": "old_value"}
    ansible_facts = {"ansible_facts_key": "ansible_facts_value"}
    ansible_system_facts = {"ansible_system_facts_key": "ansible_system_facts_value"}
    ansible_network_resources = {"ansible_network_resources_key": "ansible_network_resources_value"}
    ansible_all_ipv4_addresses = ['127.0.0.1', '1.2.3.4']
    ansible_all_ipv6_addresses = ['::1', '2001:0db8:85a3:0000:0000:8a2e:0370:7334']

# Generated at 2022-06-13 17:09:32.749925
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

# Generated at 2022-06-13 17:09:35.115222
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), FactCache), "Failed: FactCache object could not be created"
    assert isinstance(FactCache(), CacheLoader), "Failed: FactCache object could not be created"

# Generated at 2022-06-13 17:09:38.336451
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('test',{'a':'c'})
    assert fact_cache['test']['a'] == 'c'
    # test update
    fact_cache.first_order_merge('test',{'a':'b'})
    assert fact_cache['test']['a'] == 'b'

# Generated at 2022-06-13 17:09:43.729046
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    foo = FactCache()
    key = 'key_of_dict'
    value = {'a': {'d': 'd', 'b': 'b'}, 'c': 'c'}
    foo.first_order_merge(key, value)
    foo.first_order_merge(key, {'a':{'d':'overwritten','c':'c'},'b':'b'})
    foo.first_order_merge(key, {'a':{'d':{'g':'g'},'e':'e'},'f':'f'})
    assert value == {'a': {'d': 'd', 'b': 'b'}, 'c': 'c'}

# Generated at 2022-06-13 17:09:54.190238
# Unit test for constructor of class FactCache
def test_FactCache():
    test = FactCache()

    # Test __init__ method of FactCache
    assert test._plugin is not None

    # Test __contains__ method of FactCache
    try:
        assert False is test.__contains__('Test')
    except KeyError:
        assert True

    # Test __setitem__ method of FactCache
    test.__setitem__('Test', 'Test_data')
    assert True is test.__contains__('Test')

    # Test __getitem__ method of FactCache
    assert 'Test_data' is test.__getitem__('Test')

    # Test __delitem__ method of FactCache
    test.__delitem__('Test')
    assert False is test.__contains__('Test')

# Generated at 2022-06-13 17:09:55.035688
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()


# Generated at 2022-06-13 17:09:56.759005
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache.__class__.__name__ == "FactCache"
#test ends here

# Generated at 2022-06-13 17:10:03.242110
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:10:08.894371
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # nothing in fact cache - update fact cache with facts
    fact_cache.first_order_merge('test_host', {'ansible_facts': {'key1': 'value1', 'key2': 'value2'}})
    assert fact_cache['test_host']['ansible_facts']['key1'] == 'value1'

    # facts in fact cache - update fact cache with facts
    fact_cache.first_order_merge('test_host', {'ansible_facts': {'key3': 'value3', 'key4': 'value4'}})
    assert fact_cache['test_host']['ansible_facts']['key3'] == 'value3'
    assert fact_cache['test_host']['ansible_facts']['key1']

# Generated at 2022-06-13 17:10:13.432964
# Unit test for constructor of class FactCache
def test_FactCache():
    #Create a new instance
    cf = FactCache()

    #Create a new item
    cf["test"]={"test1":"test1","test2":"test2","test3":"test3"}

    #Print out the newly created item

# Generated at 2022-06-13 17:10:22.351840
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test if the cache plugin can be loaded
    # If no cache plugin is defined in config, the default cache plugin 'Memory' should be loaded
    fc = FactCache()
    assert fc._plugin is not None

    # Test if the load of cache plugin fails with AnsibleError when an undefined cache plugin is defined in config
    # The config constants.yml is not loaded so the fake plugin 'AnsibleError' will be loaded
    from ansible.config import defaults
    defaults.CACHE_PLUGIN = 'AnsibleError'
    from ansible.plugins.loader import cache_loader
    cache_loader._plugins = {}
    try:
        FactCache()
        assert False
    except AnsibleError:
        assert True

# Generated at 2022-06-13 17:10:24.848316
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
        assert True
    except AnsibleError:
        assert False
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-13 17:10:27.531131
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    assert c._plugin == cache_loader.get(C.CACHE_PLUGIN)
    assert isinstance(c, MutableMapping)


# Generated at 2022-06-13 17:10:34.378207
# Unit test for constructor of class FactCache
def test_FactCache():

    import os
    import shutil
    from ansible.module_utils._text import to_bytes

    test_dir = '/tmp/test_fact_cache_dir'
    dir_old = C.CACHE_PLUGIN_CONNECTION

# Generated at 2022-06-13 17:10:37.286756
# Unit test for constructor of class FactCache
def test_FactCache():
    ca = FactCache()
    assert isinstance(ca, FactCache)
    assert ca._plugin is not None

# Generated at 2022-06-13 17:10:38.326903
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

# Generated at 2022-06-13 17:10:40.893939
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact._plugin is cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:10:54.732086
# Unit test for constructor of class FactCache
def test_FactCache():
    obj = FactCache()
    return obj


# Generated at 2022-06-13 17:10:57.025373
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:10:57.910831
# Unit test for constructor of class FactCache
def test_FactCache():
    obj = FactCache()
    assert obj

# Generated at 2022-06-13 17:11:09.513714
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    version_cache = {'ansible_facts': {'ansible_version': {'full': '2.1.1.0'}}}
    fact_var_cache = {'ansible_facts': {'fact_var': 'fact_value'}}

    fc = FactCache()
    fc.first_order_merge('10.1.1.1', version_cache)
    fc.first_order_merge('10.1.1.1', fact_var_cache)

    assert fc.keys() == ['10.1.1.1']
    assert fc['10.1.1.1'] == {'ansible_facts': {'fact_var': 'fact_value', 'ansible_version': {'full': '2.1.1.0'}}}

# Generated at 2022-06-13 17:11:17.269076
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()

    # Test if the specified key is not in cache,
    # the update logic will set key and value to cache
    # by calling the method first_order_merge
    key = 'host.example.com'
    value = {
        'ansible_kernel': '3.10.0-327.3.1.el7.x86_64',
        'ansible_machine': 'x86_64'
    }
    factcache.first_order_merge(key, value)
    assert key in factcache
    assert factcache[key] == value

    # Test if the specified key exists in cache,
    # only the value will be updated.
    key2 = 'host'
    value2 = 'host.example.com'

# Generated at 2022-06-13 17:11:27.311713
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('test_key', 'test_value')
    assert cache.get('test_key') == 'test_value'
    cache.first_order_merge('test_key', 'test_value2')
    assert cache.get('test_key') == 'test_value2'
    cache.first_order_merge('test_key', {'key1':'value1'})
    assert cache.get('test_key') == {'key1':'value1'}
    cache.first_order_merge('test_key', {'key2':'value2'})
    assert cache.get('test_key') == {'key2':'value2'}

# Generated at 2022-06-13 17:11:36.744417
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Test for '__setitem__' of class FactCache
    # test for 'contains' of class FactCache
    # test for 'get' of class FactCache
    cache = FactCache()
    assert (not cache.__contains__('key'))
    cache.__setitem__('key', 'value')
    assert (cache.__getitem__('key') == 'value')
    # test for 'update' of class FactCache
    cache2 = FactCache()
    fact = dict()
    fact['key'] = 'value2'
    cache2.first_order_merge('key', fact['key'])
    assert (cache2.__getitem__('key') == 'value2')
    cache2.first_order_merge('key', 'value')

# Generated at 2022-06-13 17:11:47.214749
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()

    host_facts_1 = {
        'aggregate': {
            'test_key': 42
        }
    }
    host_facts_2 = {
        'aggregate': {
            'test_key': 42,
            'test_key2': 43
        }
    }
    host_facts_3 = {
        'aggregate': {
            'test_key2': 44
        }
    }

    fc.first_order_merge('test_host', host_facts_1)
    assert fc['test_host'] == host_facts_1

    fc.first_order_merge('test_host', host_facts_2)
    assert fc['test_host'] == host_facts_2


# Generated at 2022-06-13 17:11:53.823086
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Init cache with test data
    cache = FactCache()
    cache['localhost'] = {"fact1": "value", "fact2": "value"}

    # Update cache with new test data
    new_facts = {"fact1": "new_value", "fact3": "new_value"}
    cache.first_order_merge('localhost', new_facts)

    # Check new merged facts
    assert cache['localhost'] == {"fact1": "new_value", "fact2": "value", "fact3": "new_value"}

# Generated at 2022-06-13 17:11:54.968824
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin is not None


# Generated at 2022-06-13 17:12:21.474227
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:12:28.038037
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    start_value = {
        "distribution_version": "7.3",
        "distribution": "CentOS",
        "distribution_major_version": "7",
        "architecture": "x86_64",
        "ipv4_address": "192.0.2.10",
        "ipv6_address": "2001:0db8:0:f101::1",
        "fqdn": "test1.example.com",
        "hostname": "test1",
        "os_family": "RedHat",
        "system": "Linux"
    }


# Generated at 2022-06-13 17:12:29.840781
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()

    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:12:32.555589
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    assert not fc
    fc.first_order_merge('host1', {'a': 'b'})
    assert fc['host1'] == {'a': 'b'}
    fc.first_order_merge('host1', {'c': 'd'})
    assert fc['host1'] == {'a': 'b', 'c': 'd'}

# Generated at 2022-06-13 17:12:37.310915
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('key1', {'fact1': 'value1', 'fact2': 'value2'})
    host_facts = cache.get('key1')
    assert host_facts['fact1'], 'value1'
    assert host_facts['fact2'], 'value2'
    cache.first_order_merge('key1', {'fact1': 'value3', 'fact3': 'value4'})
    assert host_facts['fact1'], 'value3'
    assert host_facts['fact2'], 'value2'
    assert host_facts['fact3'], 'value4'

# Generated at 2022-06-13 17:12:47.532901
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()

# Generated at 2022-06-13 17:12:55.763718
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.dict import CacheModule as dict
    from ansible.plugins.cache.redis import CacheModule as redis
    from ansible.module_utils.six.moves import reload_module


# Generated at 2022-06-13 17:12:58.211565
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    print(fact_cache.__dict__)
    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:13:01.099706
# Unit test for constructor of class FactCache
def test_FactCache():
    """Unit Test for constructor of class FactCache."""
    fact_cache = FactCache()
    assert fact_cache._plugin is not None
    assert fact_cache._plugin.__class__.__name__ == 'FactCacheData'


if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:13:04.264057
# Unit test for constructor of class FactCache
def test_FactCache():
    import pytest
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    aa = FactCache(plugin)
    with pytest.raises(AnsibleError):
        aa = FactCache()
        raise AnsibleError('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:14:00.375017
# Unit test for constructor of class FactCache
def test_FactCache():
    """Test the constructor of the class FactCache"""
    f = FactCache()


# Generated at 2022-06-13 17:14:04.749354
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("1.1.1.1", dict(a=1, b=2))
    fc.first_order_merge("1.1.1.1", dict(c=3))
    fc.first_order_merge("1.1.1.2", dict(b=2, c=3))
    assert dict(a=1, b=2, c=3) == fc["1.1.1.1"]
    assert dict(b=2, c=3) == fc["1.1.1.2"]


# Generated at 2022-06-13 17:14:07.647415
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.utils.plugin_docs import get_docstring
    if get_docstring(FactCache):
        print('SUCCESS: Test get_docstring for FactCache')
    else:
        print('FAILURE: Test get_docstring for FactCache')

# Generated at 2022-06-13 17:14:10.011204
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.jsonfile import CacheModule as jsonfile

    cache = FactCache()
    assert isinstance(cache, MutableMapping)
    assert isinstance(cache._plugin, jsonfile)


# Generated at 2022-06-13 17:14:16.743001
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ Unit test for method first_order_merge of class FactCache """
    fact_cache = FactCache()
    key = 'localhost'
    fact_cache[key] = {'foo': 'bar'}
    value = {'foo2': 'bar2'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'foo': 'bar', 'foo2': 'bar2'}
    value = {'foo3': 'bar3'}
    fact_cache.first_order_merge('localhost2', value)
    assert fact_cache['localhost2'] == {'foo3': 'bar3'}
    fact_cache.flush()

# Generated at 2022-06-13 17:14:18.428331
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 17:14:27.614412
# Unit test for constructor of class FactCache
def test_FactCache():
    import unittest
    from ansible.plugins.cache import BaseCacheModule

    class DummyCache(BaseCacheModule):
        def get(self, key):
            raise ValueError('Unmocked')

        def set(self, key, value):
            raise ValueError('Unmocked')

        def contains(self, key):
            raise ValueError('Unmocked')

        def keys(self):
            raise ValueError('Unmocked')

        def flush(self):
            raise ValueError('Unmocked')

    class TestFactCache(unittest.TestCase):
        def setUp(self):
            self.mocked_plugin = DummyCache()
            self.original_plugin = cache_loader._cache_plugins[C.CACHE_PLUGIN]

# Generated at 2022-06-13 17:14:35.199852
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Cases to test:
    # 1. key is not in cache, value is valid
    # 2. key is in cache, value is valid
    # 3. key is in cache, value is invalid
    # 4. key is not in cache, value is invalid
    #
    # Test case 1, 2, 3 and 4 are implemented by following code

    # Initialize FactCache object
    fact_cache = FactCache()

    # case 1
    test_key = "key1"
    test_value = "value1"
    fact_cache.first_order_merge(test_key, test_value)

    # case 2
    test_key = "key1"
    test_value = {"key1": "value1"}
    fact_cache.first_order_merge(test_key, test_value)

    # case 3


# Generated at 2022-06-13 17:14:37.259256
# Unit test for constructor of class FactCache
def test_FactCache():
    print(FactCache)

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:14:45.568007
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    assert len(fc) == 0
    fc.first_order_merge('demo_ip', 'demo_value')
    assert len(fc) == 1
    assert fc['demo_ip'] == 'demo_value'
    fc.first_order_merge('demo_ip', 'demo_value2')
    assert len(fc) == 1
    assert fc['demo_ip'] == 'demo_value2'


# TODO(pylint): disable=too-few-public-methods,unused-argument

# Generated at 2022-06-13 17:16:45.689149
# Unit test for constructor of class FactCache
def test_FactCache():
    class fake_fact_cache():
        def __init__(self):
            self.cache_plugin = 'jsonfile'

    my_fact_cache = FactCache()
    assert my_fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)



# Generated at 2022-06-13 17:16:50.949654
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    import os.path
    from shutil import rmtree
    from tempfile import mkdtemp
    from ansible.plugins.cache import FactCacheModule
    from ansible.utils.loader import load_plugin, path_dwim
    import subprocess

    tmpdir = mkdtemp(dir='/tmp')

# Generated at 2022-06-13 17:16:51.982179
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)

# Generated at 2022-06-13 17:16:57.201832
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fact = FactCache()
        fact['role'] = "ansible"
        fact['location'] = "chennai"
        assert fact['role'] == "ansible"
        assert fact['location'] == "chennai"
        assert fact.keys() == ['role', 'location']
        fact.flush()
        assert fact.keys() == []
        fact.flush()
    except AnsibleError:
        pass

# Generated at 2022-06-13 17:17:02.627138
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache("test")
    fc["test"]
    fc["test"] = ""
    assert fc["test"] == ""
    assert fc.keys() == [ "test" ]
    assert fc.copy() == { "test": "" }
    assert fc.first_order_merge("test", "new") == { "test": "new" }
    del fc["test"]

# Generated at 2022-06-13 17:17:09.873842
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import yaml
    yml_facts = """
    foo: bar
    bar: baz
    """
    facts = yaml.safe_load(yml_facts)

    cache = FactCache()
    cache.first_order_merge('foo.example.com', facts)

    # At this point cache should have an entry for 'foo.example.com' with the above
    # values for the second argument of first_order_merge.
    # Lets write more facts for 'foo.example.com'
    more_facts = """
    foo: bar
    bar: baz
    another_bar: biz
    """
    more_facts = yaml.safe_load(more_facts)

    # update the cache with the new facts for 'foo.example.com'

# Generated at 2022-06-13 17:17:12.301296
# Unit test for constructor of class FactCache
def test_FactCache():
    ansible_config = {}
    ansible_config['CACHE_PLUGIN'] = 'jsonfile'
    C.config.initialize(ansible_config)

    try:
        fc = FactCache()
    except Exception:
        raise
    else:
        fc.flush()


if __name__ == "__main__":
    test_FactCache()

# Generated at 2022-06-13 17:17:21.537904
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins import cache_loader
    from ansible.plugins.cache import BaseFileCacheModule
    cache_loader.all = {}

    class TestCache(BaseFileCacheModule):
        def contains(self, key):
            return False

        def get(self, key):
            return {}

        def set(self, key, value):
            pass

        def delete(self, key):
            pass

        def flush(self):
            pass

        def keys(self):
            return []

        def _load(self):
            pass

        def _save(self):
            pass


    filename = "/tmp/ansible-test-fact-cache"
    cache_loader.all["TestCache"] = TestCache
    cache = FactCache(filename)
    assert isinstance(cache._plugin, TestCache)

# Generated at 2022-06-13 17:17:29.648608
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache_obj = FactCache()
    key = "host_name"
    value = {"host_1": {"fact1": "value1", "fact2": "value2"}}
    fact_cache_obj.first_order_merge(key, value)
    assert key in fact_cache_obj
    assert fact_cache_obj[key] == value
    value = {"host_1": {"fact3": "value3", "fact4": "value4"}}
    fact_cache_obj.first_order_merge(key, value)
    assert key in fact_cache_obj
    assert fact_cache_obj[key] == {"host_1": {"fact1": "value1", "fact2": "value2", "fact3": "value3", "fact4": "value4"}}


# Generated at 2022-06-13 17:17:32.061050
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
    except Exception as e:
        pass
    else:
        raise AssertionError("FactCache constructor should raise exception, got %s" % fc)