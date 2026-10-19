

# Generated at 2022-06-13 17:07:33.893282
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    #assert 'succeed'
    print('succeed')

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:07:35.149370
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache=FactCache()

# Generated at 2022-06-13 17:07:37.737412
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test the constructor of class FactCache
    """
    # Test the constructor
    fact_cache = FactCache()



# Generated at 2022-06-13 17:07:46.572214
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible import constants as C
    C.CACHE_PLUGIN = 'memory'
    # create an instance of fact_cache with required parameters
    fact_cache = FactCache()
    assert fact_cache is not None
    # since cache_plugin is memory, flush will remove all the keys/values from cache
    fact_cache.flush()
    # update with a few values
    fact_cache["host1"] = {'ansible_os_family': 'RedHat'}
    fact_cache["host2"] = {'ansible_os_family': 'Centos'}
    assert len(fact_cache) == 2
    # flush will remove all the keys/values from cache
    fact_cache.flush()
    assert len(fact_cache) == 0

# Generated at 2022-06-13 17:07:48.456037
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()

    assert fact_cache is not None

# Generated at 2022-06-13 17:07:54.997213
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Given
    fc = FactCache()
    fc['127.0.0.1'] = {'foo': 1}
    # When
    fc.first_order_merge('127.0.0.1', {'foo': 2})
    fc.first_order_merge('127.0.0.1', {'bar': 2})
    # Then
    assert fc['127.0.0.1'] == {'foo': 2, 'bar': 2}


# Generated at 2022-06-13 17:07:58.804361
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    host_fact = {'hello': 'world'}
    host = '192.168.1.1'
    fc.first_order_merge(host, host_fact)
    assert fc[host] == host_fact
    new_fact = {'hello': 'universe'}
    fc.first_order_merge(host, new_fact)
    assert fc[host] == {'hello': 'universe'}

# Generated at 2022-06-13 17:08:04.923471
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts = FactCache()
    hostname = 'myhost'
    facts['myhost'] = {'fact': 'value'}
    new_facts = {'new_fact': 'value'}
    expected = {'myhost': {'fact': 'value', 'new_fact': 'value'}}

    facts.first_order_merge(hostname, new_facts)

    assert facts == expected

# Generated at 2022-06-13 17:08:06.843950
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert isinstance(facts, FactCache)
    assert isinstance(facts, MutableMapping)


# Generated at 2022-06-13 17:08:08.278385
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache


# class FactCache


# Generated at 2022-06-13 17:08:19.949935
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.memory import CacheModule as MemoryCacheModule


# Generated at 2022-06-13 17:08:20.751461
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin

# Generated at 2022-06-13 17:08:30.982854
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts = {
            'ansible_facts': {
                'hostname': 'localhost',
                'os_version': 'ubuntu 16.04',
                'ansible_distribution_version': 'ubuntu 16.04',
                'file_system_type': 'ext4',
                'disk_size': '10G',
                'distribution_release': 'ubuntu',
                'distribution_version': '16.04',
                'distribution': 'ubuntu'},
            'version': 'ansible 2.8.3',
            'time': '2019-08-07 10:44:40'
            }

# Generated at 2022-06-13 17:08:32.025830
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_cache = FactCache()
    assert isinstance(facts_cache, FactCache)

# Generated at 2022-06-13 17:08:33.124253
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:08:34.149157
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Tests for FactCache constructor
    """
    pass

# Generated at 2022-06-13 17:08:35.763277
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    :description: Test that the constructor for the FactCache class works
    """
    assert FactCache()



# Generated at 2022-06-13 17:08:39.905239
# Unit test for constructor of class FactCache
def test_FactCache():
    ''' Unit test for constructor of class FactCache '''
    fact_cache = FactCache()
    return fact_cache

if __name__ == '__main__':
    FACT_CACHE_TEST = test_FactCache()
    print(FACT_CACHE_TEST)

# Generated at 2022-06-13 17:08:40.773603
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:08:49.110118
# Unit test for constructor of class FactCache
def test_FactCache():
    class FakeCacheLoader(object):
        def __init__(self):

            return
        def contains(self, key):
            return True
        def get(self, key):
            return 'test'
        def delete(self, key):
            return
        def set(self, key, value):
            return
        def keys(self):
            return ['key1']
        def flush(self):
            return

    cache = FactCache()
    cache._plugin = FakeCacheLoader()

    # assert an error
    result = cache.__getitem__('test')
    assert result == 'test'

    result = cache['test']
    assert result == 'test'

    result = cache['test']
    assert result == 'test'

    result = cache.__setitem__('test', 'test')
    assert result is None

    result

# Generated at 2022-06-13 17:08:58.556884
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Create a test fact cache with a local plugin
    class TestPlugin():

        def __init__(self, *args, **kwargs):
            self._data = {}

        def set(self, key, value):
            self._data[key] = value

        def get(self, key):
            return self._data[key]

        def keys(self):
            return self._data.keys()

        def flush(self):
            self._data = {}

        def contains(self, key):
            return key in self._data

    plugin = TestPlugin()
    facts = FactCache(plugin)

    # Try to merge a local fact with an empty fact cache
    facts.first_order_merge('fact1', {'attr1': 'val1'})
    assert('fact1' in facts)

# Generated at 2022-06-13 17:09:04.839565
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = 'jsonfile'
    cache_loader.set(plugin, 'ansible.plugins.cache.jsonfile')
    C.CACHE_PLUGIN = plugin
    f1 = FactCache()
    assert f1._plugin.__class__.__name__ == 'JsonfileCacheModule'

# Generated at 2022-06-13 17:09:06.972218
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)



# Generated at 2022-06-13 17:09:13.417420
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    m = FactCache()
    m.first_order_merge('fiz', {'foo': 1})
    assert set(m['fiz'].keys()) == set(['foo'])
    m.first_order_merge('fiz', {'bar': 2})
    assert set(m['fiz'].keys()) == set(['foo', 'bar'])
    m.flush()
    m.first_order_merge('fiz', {'bar': 2})
    assert set(m['fiz'].keys()) == set(['bar'])

# Generated at 2022-06-13 17:09:19.788027
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_key = 'dummy_key'
    host_value = {
        'ansible_facts': {
            'test_vars': {
                'variable1': 'value1',
                'variable2': 'value2'
            }
        }
    }
    # set host_value in fact_cache.
    fact_cache.first_order_merge(host_key, host_value)
    # check if host_key is in fact_cache.
    assert host_key in fact_cache
    assert fact_cache[host_key] == host_value

    # check if facts can be updated correctly in fact cache.
    # changed host_value will update fact_cache.

# Generated at 2022-06-13 17:09:20.920231
# Unit test for constructor of class FactCache
def test_FactCache():
    def __init__():
        pass

    factcache = FactCache(__init__)

# Generated at 2022-06-13 17:09:23.234650
# Unit test for constructor of class FactCache
def test_FactCache():
    # TODO: mock plugin_loader.get(C.CACHE_PLUGIN)
    assert False

# Generated at 2022-06-13 17:09:24.192037
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()

# Generated at 2022-06-13 17:09:33.230765
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    host_facts = {
        "ansible_default_ipv4": {
            "address": "1.1.1.1"
        },
        "ansible_host": "host1"
    }

    fact_cache.first_order_merge("host1", host_facts)
    assert fact_cache["host1"] == {
        "ansible_default_ipv4": {
            "address": "1.1.1.1"
        },
        "ansible_host": "host1"
    }

    host_facts = {
        "ansible_default_ipv4": {
            "address": "1.1.1.1"
        }
    }

    fact_cache.first_order_merge("host1", host_facts)
   

# Generated at 2022-06-13 17:09:34.484476
# Unit test for constructor of class FactCache
def test_FactCache():

    pass
#    assert file_system_plugin.get('key1') == None
#    assert file_system_plugin.get('key2') == None

# Generated at 2022-06-13 17:09:37.555469
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    pass

# Generated at 2022-06-13 17:09:41.007951
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.cache import memory
    cache = FactCache()
    assert type(cache) == FactCache
    assert cache._plugin == memory.CacheModule()
    cache = FactCache(dict(k1='v1'))
    assert type(cache) == FactCache
    assert cache._plugin == memory.CacheModule()

# Generated at 2022-06-13 17:09:45.066855
# Unit test for constructor of class FactCache
def test_FactCache():
    assert C.CACHE_PLUGIN == 'memory'

    plugin = 'memory'
    plugin = cache_loader.get(plugin)
    assert plugin is not None
    plugin.flush()
    assert plugin.get('TEST') is None
    assert plugin.contains('TEST') is False
    assert plugin.keys() == []
    assert plugin.delete('TEST') is None

    plugin.set('KEY', 'VAL')
    assert plugin.keys() == ['KEY']
    assert plugin.contains('KEY') is True
    assert plugin.get('KEY') == 'VAL'
    assert plugin.delete('KEY') == 'VAL'
    assert plugin.contains('KEY') is False
    assert plugin.get('KEY') is None
    assert plugin.keys() == []
    plugin.flush()

# Generated at 2022-06-13 17:09:48.347424
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache() # not the same as fact_cache = None
    if fact_cache:
        print("pass: test_FactCache() OK.")


# Generated at 2022-06-13 17:09:54.739704
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache_dict = {'f1': {'facts1': 'facts1'}, 'f2': {'facts2': 'facts2'}}
    fact_cache = FactCache()
    fact_cache.__setitem__ = dict.update
    fact_cache.first_order_merge('f1', {'facts1': 'facts1'})
    fact_cache.first_order_merge('f2', {'facts2': 'facts2'})
    assert fact_cache_dict == fact_cache

# Generated at 2022-06-13 17:09:59.349574
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import memory

    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert fact_cache._plugin is memory



# Generated at 2022-06-13 17:10:04.403726
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert fc.copy() == {}
    fc['key'] = 'value'
    assert fc['key'] == 'value'
    with display.override_verbosity(3):
        assert fc.keys()[0] == 'key'
    assert fc.first_order_merge('key', 'value2') is None
    assert fc['key'] == 'value2'

# Generated at 2022-06-13 17:10:05.210308
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert factcache is not None

# Generated at 2022-06-13 17:10:07.473086
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None


# Generated at 2022-06-13 17:10:11.229196
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge("test_host", {"test_key":"test_value"})
    fact_cache_dict = fact_cache.copy()
    assert fact_cache_dict["test_host"]["test_key"] == "test_value"

# Generated at 2022-06-13 17:10:25.778945
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    first_order_merge_args = [
        ('host1', {'a': 1, 'b': 2}),
        ('host2', {'b': 3, 'c': 4}),
        ('host1', {'a': 2, 'b': 3, 'c': 5}),
        ('host2', {'b': 4, 'c': 5, 'd': 6})
    ]
    expected = {
        'host1': {'a': 2, 'b': 3, 'c': 5},
        'host2': {'b': 4, 'c': 5, 'd': 6}
    }

    for key, value in first_order_merge_args:
        fact_cache.first_order_merge(key, value)


# Generated at 2022-06-13 17:10:26.978105
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache
    assert len(cache) == 0

# Generated at 2022-06-13 17:10:29.284286
# Unit test for constructor of class FactCache
def test_FactCache():

    # Setup

    def test_flush():
        cache = FactCache()
        cache.flush()

        # Assertions
        assert len(cache) == 0
    test_flush()

    # Teardown

# Generated at 2022-06-13 17:10:32.001113
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache_plugin = cache_loader.get(C.CACHE_PLUGIN)  # fall back to 'memory'
    fact_cache = FactCache(fact_cache_plugin)

    assert fact_cache.__getitem__('_plugin') == fact_cache_plugin


# Generated at 2022-06-13 17:10:32.877530
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    cache.first_order_merge('a', 'b')

# Generated at 2022-06-13 17:10:33.727549
# Unit test for constructor of class FactCache
def test_FactCache():
    # test if this initialize FactCache successfully
    ansible.cache.FactCache()

# Generated at 2022-06-13 17:10:36.487702
# Unit test for constructor of class FactCache
def test_FactCache():

    C.CACHE_PLUGIN = 'redis'
    fc = FactCache()

    assert 'CACHE_PLUGIN' in vars(C)
    assert '_plugin' in vars(fc)

    C.CACHE_PLUGIN = 'jsonfile'
    fc = FactCache()

    assert 'CACHE_PLUGIN' in vars(C)
    assert '_plugin' in vars(fc)

# Generated at 2022-06-13 17:10:38.471433
# Unit test for constructor of class FactCache
def test_FactCache():
    # Valid constructor, should work without raising any exceptions
    fact_cache = FactCache()


# Generated at 2022-06-13 17:10:40.649677
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin is not None

# Generated at 2022-06-13 17:10:41.870265
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache != None

# Generated at 2022-06-13 17:10:55.797156
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache != None

# Generated at 2022-06-13 17:10:56.775557
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), FactCache)

# Generated at 2022-06-13 17:11:08.702812
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Unit test for testing the constructor of FactCache.
    This will raise a system error for the absence of cache plugin
    """
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.loader import cache_loader
    from ansible.errors import AnsibleError
    from ansible.plugins.cache.memory import CacheModule as CacheMemory

    C.CACHE_PLUGIN = 'memory'
    cache_loader.__cache = {'memory': CacheMemory()}
    fac = FactCache()
    assert issubclass(fac.__class__, MutableMapping)

    C.CACHE_PLUGIN = 'random'
    try:
        fac2 = FactCache()
        assert False
    except AnsibleError:
        assert True


# Generated at 2022-06-13 17:11:09.935729
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:11:17.568702
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    hostname = 'foobar.example.com'
    fact = 'ipv4'
    value = ['10.0.0.1', '2001:db8:85a3:0:0:8a2e:370:7334']
    cache.first_order_merge(hostname, {fact: value})
    assert cache.keys() == [hostname]
    assert cache[hostname] == {fact: value}
    value2 = ['10.0.0.1', '2001:db8:85a3:0:0:8a2e:370:7334', '10.0.0.2']
    cache.first_order_merge(hostname, {fact: value2})
    assert cache.keys() == [hostname]

# Generated at 2022-06-13 17:11:27.345377
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    # Test merge of aci_config
    config_list = [(1, "test"), (3, "test3")]
    config = {'aci_config': {'view': {'tenants': config_list}}}
    fact_cache.first_order_merge("test_host", config)
    config_list = [(1, "test1"), (3, "test3")]
    config = {'aci_config': {'view': {'tenants': config_list}}}
    fact_cache.first_order_merge("test_host", config)
    config_list = [(1, "test1"), (2, "test2"), (3, "test3")]
    config = {'aci_config': {'view': {'tenants': config_list}}}
    fact_cache

# Generated at 2022-06-13 17:11:36.195756
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('localhost', {'fact_a': 'm'})
    assert(cache['localhost']['fact_a'] == 'm')
    cache.first_order_merge('localhost', {'fact_a': 'n'})
    assert(cache['localhost']['fact_a'] == 'n')
    cache.first_order_merge('localhost', {'fact_b': 'o'})
    assert(cache['localhost']['fact_a'] == 'n')
    assert(cache['localhost']['fact_b'] == 'o')
    cache.flush()

if __name__ == '__main__':
    test_FactCache_first_order_merge()

# Generated at 2022-06-13 17:11:36.938632
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

# Generated at 2022-06-13 17:11:38.431426
# Unit test for constructor of class FactCache
def test_FactCache():
    test_obj = FactCache()
    assert isinstance(test_obj, MutableMapping)
    assert test_obj  #is not None

# Generated at 2022-06-13 17:11:42.367301
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    FactCache class constructor takes no arguments
    """
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)



# Generated at 2022-06-13 17:12:15.266587
# Unit test for constructor of class FactCache
def test_FactCache():
    # This funciton tests the constructor of the class FactCache.
    #
    # Note:
    #   Testing of AnsibleError is not possible because AnsibleError is a subclass of Exception.
    #   The opportunity to test exceptions is not available in Python 2.7.
    #   In Python 3.x it is possible to test exceptions.
    #
    # Args:
    #     None
    #
    # Returns:
    #     None
    #
    # Raises:
    #     None

    test_invalid_path = FactCache()
    assert test_invalid_path._plugin != None
    assert test_invalid_path._plugin.name == C.CACHE_PLUGIN

# Generated at 2022-06-13 17:12:20.015210
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    host_cache = {'old_fact': 'old_fact_value'}
    new_fact = {'new_fact': 'new_fact_value'}
    host_facts = {'test_fact': 'test_fact_value'}

    fc._plugin = FakePlugin(host_cache)
    fc.first_order_merge('test_host', new_fact)
    assert host_facts == fc.copy()


# Generated at 2022-06-13 17:12:21.068960
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc != None
    fc["key"] = "value"
    assert len(fc) != 0
    len(fc)

# Generated at 2022-06-13 17:12:24.860636
# Unit test for constructor of class FactCache
def test_FactCache():
    test_cache_plugin = 'jsonfile'
    test_cache_dir = '/tmp/ansible-test'
    display.verbosity = 3
    C.CACHE_PLUGIN = test_cache_plugin
    C.CACHE_PLUGIN_CONNECTION = test_cache_dir
    test_fact_cache = FactCache()
    # Test if __init__ call super
    test_fact_cache['test'] = 1
    assert(test_fact_cache['test'] == 1)

# Generated at 2022-06-13 17:12:27.407361
# Unit test for constructor of class FactCache
def test_FactCache():
    display_test = Display()
    display_test.verbosity = 3

    cache = FactCache()

    assert cache._plugin

    if cache._plugin.__class__ == None:
        return False
    else:
        return True

# Generated at 2022-06-13 17:12:35.240582
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import sys

    test_key = "redhat"
    test_value = 517

    # test_value > host_cache
    host_cache = 518
    host_facts = {test_key: host_cache}
    fact_cache = FactCache()
    fact_cache_copy = fact_cache.copy()
    fact_cache._plugin.set(test_key, host_cache)
    fact_cache.first_order_merge(test_key, test_value)
    assert fact_cache.copy() == fact_cache_copy
    assert fact_cache[test_key] == host_cache

    # test_value == host_cache
    host_cache = 517
    host_facts = {test_key: host_cache}
    fact_cache = FactCache()
    fact_cache_copy = fact_cache

# Generated at 2022-06-13 17:12:36.079479
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:12:45.590507
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()

# Generated at 2022-06-13 17:12:54.560532
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.update({'host1': {'test_fact1': 'test_value1', 'test_fact2': 'test_value2'}})
    fact_cache.first_order_merge('host2', {'test_fact3': 'test_value3', 'test_fact4': 'test_value4'})
    assert fact_cache == {'host1': {'test_fact1': 'test_value1', 'test_fact2': 'test_value2'}, 'host2': {'test_fact3': 'test_value3', 'test_fact4': 'test_value4'}}

# Generated at 2022-06-13 17:12:59.552933
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    test_data = dict(a=dict(name='glob',title='The One And Only'),
                     b=dict(name='tim',title='Mr. Python'),
                     c=dict(name='barry',title='Champion of the Sun'))

    # Test replacing cache key
    fact_cache.first_order_merge('a', test_data)
    assert fact_cache.get('a').get('name') == 'glob', 'Key "a" has wrong value in cache.'

    # Test updating cache key
    test_data.get('a').update(dict(name='Tim'))
    fact_cache.first_order_merge('a', test_data)

# Generated at 2022-06-13 17:13:55.111589
# Unit test for constructor of class FactCache
def test_FactCache():
    # test for invalid cache plugin
    C.CACHE_PLUGIN = 'json'
    cache = None
    try:
        cache = FactCache()
    except AnsibleError as e:
        assert 'Unable to load the facts cache plugin (json).' in str(e)
    assert cache is None

# Generated at 2022-06-13 17:13:58.837321
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert isinstance(facts, FactCache)
    assert 'windows' in facts

    # testing invalid constructor when no plugin was found
    from ansible.plugins.loader import cache_loader
    orig_loader = cache_loader.get
    cache_loader.get = lambda *args, **kwargs: None
    try:
        facts = FactCache()
    except AnsibleError as e:
        assert 'Unable to load the facts cache plugin' in str(e)
    else:
        assert False

    # testing the failure of the flush function
    assert 0 == facts.flush()

    cache_loader.get = orig_loader
    assert facts.flush() == 1

# Generated at 2022-06-13 17:14:04.327433
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache._plugin = FakeCache()

    cache.first_order_merge("127.0.0.1", {"a": "b"})
    assert cache == {"127.0.0.1": {"a": "b"}}

    cache.first_order_merge("127.0.0.1", {"a": "new"})
    assert cache == {"127.0.0.1": {"a": "new"}}

    cache.first_order_merge("127.0.0.1", {"b": "b"})
    assert cache == {"127.0.0.1": {"a": "new", "b": "b"}}

    cache.first_order_merge("192.168.0.1", {"a": "b"})

# Generated at 2022-06-13 17:14:06.361430
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert fact_cache._plugin
    assert fact_cache._plugin.cache_name


# Generated at 2022-06-13 17:14:13.205750
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup
    key = 'myhost.mydomain.tld'
    value = {'ansible_os_family': 'Debian',
             'ansible_pkg_mgr': 'apt'}
    host_facts = {key: value}

    host_cache = {key: value}
    host_cache['ansible_pkg_mgr'] = 'yum'

    class cache_loader_stub():
        def get(self, key):
            return host_cache

    # Test
    cache = FactCache()

    # Mute output
    from ansible.plugins.loader import cache_loader
    cache_loader.display = display.verbosity = display.debug = display.deprecated = lambda *a, **kw: None

    test_cache = FactCache()
    test_cache._plugin = cache_loader_stub()

# Generated at 2022-06-13 17:14:16.572972
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    ret = cache.first_order_merge('foo', 'bar')
    assert ret == {'foo': 'bar'}
    ret = cache.first_order_merge('foo', 'zap')
    assert ret == {'foo': 'zap'}

# Generated at 2022-06-13 17:14:17.652522
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache=FactCache()
    print(fact_cache)

# Generated at 2022-06-13 17:14:22.961336
# Unit test for constructor of class FactCache
def test_FactCache():
    def test_plugin():
        def contains():
            return True

        def get():
            return dict()

        def set():
            return None

        def delete():
            return None

        def keys():
            return ["test"]

        def flush():
            return None

    # test if plugin is not found
    try:
        cache = FactCache()
    except AnsibleError:
        # TODO: check error message
        pass
    
    # test if plugin not loaded
    try:
        cache = FactCache()
        cache.__getitem__("test")
    except AnsibleError:
        # TODO: check error message
        pass
    
    C.CACHE_PLUGIN = "memcached"
    cache = FactCache()



# Generated at 2022-06-13 17:14:28.561949
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = cache_loader.get(C.CACHE_PLUGIN)

    assert(isinstance(cache, MutableMapping))
    assert(isinstance(cache, FactCache))

    assert(hasattr(cache, '_plugin'))
    assert(hasattr(cache, '_plugin'))
    assert(hasattr(cache, '_plugin'))

    assert(cache._plugin == cache_loader.get(C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:14:30.921333
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_cache = {'ansible_host': '127.0.0.1', 'ansible_facts': {'ansible_local': {'test_fact': 'test_value'}}}
    host_facts = {'test_fact': 'test_value'}
    cached_facts = FactCache()
    cached_facts.first_order_merge('127.0.0.1', host_facts)
    assert host_cache == cached_facts['127.0.0.1']

# Generated at 2022-06-13 17:16:31.889275
# Unit test for constructor of class FactCache
def test_FactCache():
    import sys
    import os
    import shutil
    from ansible.module_utils._text import to_bytes

    # Create temp directory
    fct_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../../test/integration/facts'))
    temp_dir = os.path.realpath(os.path.join(fct_path, '../../tmp/facts_' + sys._getframe().f_code.co_name))
    if os.path.isdir(temp_dir):
        shutil.rmtree(temp_dir)

    # Create cache class
    fct_cache = FactCache()

    # Create cache file
    temp_file = temp_dir + '/.cache_facts'

# Generated at 2022-06-13 17:16:33.483311
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)



# Generated at 2022-06-13 17:16:34.674711
# Unit test for constructor of class FactCache
def test_FactCache():

    # Tests will be added later
    assert True

# Generated at 2022-06-13 17:16:45.799323
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    f = FactCache()
    new_facts = {'net0': {'name': 'eth0'}, 'ipv4': {'address': '192.168.0.2'}}
    f.first_order_merge('127.0.0.1', new_facts)

    existing_facts = {'net0': {'name': 'eth0'}, 'ipv4': {'address': '192.168.0.1'}}
    f.first_order_merge('127.0.0.1', existing_facts)

    assert '127.0.0.1' in f
    cached_facts = f['127.0.0.1']
    assert cached_facts['net0'] == {'name': 'eth0'}

# Generated at 2022-06-13 17:16:46.508117
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:16:47.633788
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None

# Generated at 2022-06-13 17:16:54.325821
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    merge_result = {'test_fact1': 'test_fact1_value1', 'test_fact2': 'test_fact2_value2'}

    fact_cache.first_order_merge('127.0.0.1', {'test_fact1': 'test_fact1_value1', 'test_fact2': 'test_fact2_value2'})
    assert fact_cache['127.0.0.1'] == merge_result
    assert fact_cache['127.0.0.1'] == fact_cache.copy()['127.0.0.1']
    assert fact_cache.keys() == ['127.0.0.1']
    

# Generated at 2022-06-13 17:16:55.379036
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()


# Generated at 2022-06-13 17:17:00.728574
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = "test"
    value_1 = {"a":1, "b":3}
    value_2 = {"a":2, "c":5}
    cache.first_order_merge(key, value_1)
    cache.first_order_merge(key, value_2)
    assert cache[key] == {"a":2, "b":3, "c":5}

# Generated at 2022-06-13 17:17:08.877433
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    cache = FactCache()

    cache._plugin.set('testhost', {'cache': 'value'})

    # No update
    cache.first_order_merge('testhost', {'cache': 'value'})
    assert cache['testhost'] == {'cache': 'value'}

    # Add new key
    cache.first_order_merge('testhost', {'newkey': 'newvalue'})
    assert cache['testhost'] == {'cache': 'value', 'newkey': 'newvalue'}

    # Update existing key (method first_order_merge do not overwrite the value)
    cache.first_order_merge('testhost', {'cache': 'newvalue'})
    assert cache['testhost'] == {'cache': 'value', 'newkey': 'newvalue'}

    # Not fail on inex