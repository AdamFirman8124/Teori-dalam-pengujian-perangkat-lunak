

# Generated at 2022-06-13 17:07:36.105895
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert isinstance(fact_cache, MutableMapping)
    assert fact_cache._plugin is not None
    # Cleanup
    fact_cache.flush()



# Generated at 2022-06-13 17:07:37.707771
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:07:39.211126
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)

# Generated at 2022-06-13 17:07:46.440073
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    test_cache.first_order_merge("host1", "host_facts")
    # test that the facts_cache has a key host1
    assert "host1" in test_cache

    # test that the value stored is the same that has been inserted
    assert test_cache["host1"] == "host_facts"

    # test that elements are not repeated if the key already exist
    test_cache.first_order_merge("host1", "host_facts")
    assert len(test_cache["host1"]) == 1


# Generated at 2022-06-13 17:07:52.559403
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts = FactCache()
    facts.flush()

    facts.first_order_merge('foo.bar', {'baz': 1})
    assert facts['foo.bar']['baz'] == 1
    facts.first_order_merge('foo.bar', {'baz': 2})
    assert facts['foo.bar']['baz'] == 2
    facts.flush()

# Generated at 2022-06-13 17:07:59.226048
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Create a simple persistent cache with a pickle backend.
    import tempfile
    import pickle
    from ansible.cache import BaseCacheModule

    class TestCacheModule(BaseCacheModule):

        def __init__(self, *args, **kwargs):
            self._cache = {}
            self._last_updated = {}
            self._expiration_time = 0
            self._cachefile = tempfile.mktemp()

        def contains(self, key):
            return key in self._cache

        def get(self, key):
            return self._cache[key]

        def set(self, key, value):
            self._cache[key] = value

        def delete(self, key):
            del self._cache[key]

        def flush(self):
            self._cache = {}
            self._last_updated = {}

       

# Generated at 2022-06-13 17:08:00.752605
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:08:07.716415
# Unit test for constructor of class FactCache
def test_FactCache():

    f = FactCache()

    # Mock C.CACHE_PLUGIN
    setattr(C, 'CACHE_PLUGIN', 'memory')


    # Mock cache_loader.get
    import builtins
    old_get = builtins.getattr
    def new_get(self, plugin):
        assert plugin == C.CACHE_PLUGIN
        return 'memory'

    builtins.getattr = new_get
    with f:
        assert f._plugin == 'memory'
    builtins.getattr = old_get

# Generated at 2022-06-13 17:08:10.063948
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin
    assert cache._plugin.get_plugin_type() == 'memory'

# Generated at 2022-06-13 17:08:16.207779
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_facts = {'interfaces': ['eth0', 'eth1', 'lo0'], 'ansible_eth0': {'active': False}}
    cached_facts = {'interfaces': ['eth0', 'eth1', 'eth2', 'lo0'], 'ansible_eth1': {'active': True}}

    fact_cache = FactCache()
    fact_cache.first_order_merge('host1', host_facts)
    fact_cache.first_orde

# Generated at 2022-06-13 17:08:23.593723
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    _cache = FactCache()
    _cache.first_order_merge('foo', {'bar': 42})
    assert (_cache['foo']['bar'] == 42)
    _cache.first_order_merge('foo', {'bar': 43})
    assert (_cache['foo']['bar'] == 43)
    _cache.first_order_merge('foo', {'baz': 'hello'})
    assert (_cache['foo']['baz'] == 'hello')
    _cache.first_order_merge('foo', {'bar': 44})
    assert (_cache['foo']['bar'] == 44)
    assert (sorted(_cache['foo']) == ['bar', 'baz'])

# Generated at 2022-06-13 17:08:27.711170
# Unit test for constructor of class FactCache
def test_FactCache():
    import pytest
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert isinstance(fact_cache._plugin, cache_loader.get(C.CACHE_PLUGIN))

# Unit tests for get/set/delete/contains methods of class FactCache

# Generated at 2022-06-13 17:08:31.768918
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_fact_cache = FactCache()
    test_fact_cache.first_order_merge('host1', {'testing': True})
    test_fact_cache.first_order_merge('host2', {'testing': False})

    assert test_fact_cache == {'host1': {'testing': True}, 'host2': {'testing': False}}

# Generated at 2022-06-13 17:08:32.858366
# Unit test for constructor of class FactCache
def test_FactCache():
    result = FactCache()
    assert isinstance(result, FactCache)

# Generated at 2022-06-13 17:08:39.394225
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import pytest
    from ansible.plugins.loader import cache_loader
    from ansible.errors import AnsibleError

    cache_plugin = cache_loader.get('memory')
    if not cache_plugin:
        raise AnsibleError('Unable to load the facts cache plugin (memory).')

    fact_cache = FactCache()
    fact_cache._plugin = cache_plugin

    host = 'test_host'
    fact_cache.first_order_merge(host, {'new_fact': 'new_value'})

    assert fact_cache[host]['new_fact'] == 'new_value'

    fact_cache.first_order_merge(host, {'new_fact': 'new_value1'})

    assert fact_cache[host]['new_fact'] == 'new_value1'

# Unit test

# Generated at 2022-06-13 17:08:46.809043
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    new_facts = {'ansible_ssh_host': '127.0.0.1'}
    cache = FactCache()
    cache.first_order_merge('127.0.0.1', new_facts)
    assert cache['127.0.0.1'] == {'ansible_ssh_host': '127.0.0.1'}
    cache.first_order_merge('127.0.0.1', {'ansible_ssh_host': '127.0.1.1'})
    assert cache['127.0.0.1'] == {'ansible_ssh_host': '127.0.0.1'}
    cache.flush()

# Generated at 2022-06-13 17:08:55.537416
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    fact_cache.flush()
    fact_cache.first_order_merge('127.0.0.1', {'fact1': 'value1'})
    assert fact_cache['127.0.0.1'] == {'fact1': 'value1'}
    fact_cache.first_order_merge('127.0.0.1', {'fact2': 'value2'})
    assert fact_cache['127.0.0.1'] == {'fact1': 'value1', 'fact2': 'value2'}

    fact_cache.flush()
    fact_cache.first_order_merge('127.0.0.2', {'fact1': 'value1'})

# Generated at 2022-06-13 17:08:56.485739
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert fact_cache

# Generated at 2022-06-13 17:08:57.576223
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:09:09.300621
# Unit test for constructor of class FactCache
def test_FactCache():
    # Default cache plugin
    C.CACHE_PLUGIN='jsonfile'

    fc = FactCache()
    assert fc._plugin.__class__.__name__ == 'FactCachePlugin'
    assert fc._plugin._cache.__class__.__name__ == 'FileCache'
    assert fc._plugin._cache._load_name == 'facts'
    assert not fc._plugin._cache._cachefile

    # Redis cache plugin
    C.CACHE_PLUGIN='redis'
    C.CACHE_PLUGIN_CONNECTION='localhost:6379:0'

    fc = FactCache()
    assert fc._plugin.__class__.__name__ == 'FactCachePlugin'
    assert fc._plugin._cache.__class__.__name__ == 'RedisCache'


# Generated at 2022-06-13 17:09:11.601467
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:09:12.744419
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache(42)
    assert fc._plugin == None

# Generated at 2022-06-13 17:09:13.799145
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert(isinstance(cache, MutableMapping))

# Generated at 2022-06-13 17:09:15.089133
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    fact_cache.flush()
    fact_cache.keys()

# Generated at 2022-06-13 17:09:15.818257
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), MutableMapping)

# Generated at 2022-06-13 17:09:17.090584
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact._plugin 

# Generated at 2022-06-13 17:09:26.659175
# Unit test for constructor of class FactCache
def test_FactCache():
    import unittest
    import tempfile
    from ansible.plugins.cache.test import test_plugin
    from ansible.plugins.loader import cache_loader

    class TestFactCache(unittest.TestCase):

        def setUp(self):
            self._temp_dir = tempfile.mkdtemp(dir=C.DEFAULT_LOCAL_TMP)
            self.fake_loader_obj = test_plugin.TestFactCachePlugin({}, self._temp_dir)
            cache_loader._shared_loader_obj[C.CACHE_PLUGIN] = self.fake_loader_obj
            self.fact_cache = FactCache()

        def tearDown(self):
            del cache_loader._shared_loader_obj[C.CACHE_PLUGIN]


# Generated at 2022-06-13 17:09:35.040392
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup a mock cache plugin
    mock_plugin = MockFactCachePlugin()
    mock_plugin.set('cache_key1', {
        'fact1': 'value1',
        'fact2': 'value2',
    })

    # Setup a FactCache instance with the mock plugin
    fact_cache = FactCache(plugin=mock_plugin)

    # Call the first_order_merge method to update the cache
    fact_cache.first_order_merge('cache_key1', {
        'fact2': 'new_value2',
        'fact3': 'value3',
    })

    # Assert some values
    assert len(fact_cache) == 1
    assert 'cache_key1' in fact_cache
    assert fact_cache.get('cache_key1').get('fact1') == 'value1'


# Generated at 2022-06-13 17:09:39.912035
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Initialize the FactCache instance
    name = 'test_cache'
    cache = FactCache()
    cache._plugin = CacheMock()
    cache._plugin.set(name, {})

    # Initialize the first data to merge
    key = 'test_key1'
    value = 'test_value1'
    host_facts = {key: value}

    # Test first_order_merge
    cache.first_order_merge(key, value)

    # Check the result
    assert cache[name] == host_facts



# Generated at 2022-06-13 17:09:47.298005
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()
    assert not fact_cache

    fact_cache = FactCache()
    fact_cache.first_order_merge("host1", {"foo":"bar"})
    assert fact_cache.keys() == ["host1"]

    fact_cache = FactCache()
    fact_cache.first_order_merge("host2", {"foo":"bar"})
    fact_cache.first_order_merge("host2", {"foo":"baz"})
    assert fact_cache.keys() == ["host2"]
    assert fact_cache["host2"]["foo"] == "baz"

# Generated at 2022-06-13 17:09:53.062564
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache.__class__.__name__ == "FactCache"

# Generated at 2022-06-13 17:09:54.228457
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache)

# Generated at 2022-06-13 17:10:00.785647
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
  fc = FactCache()
  fc._plugin = CachePlugin()
  key = "example.com"
  value = {
    "foo": "bar"
  }
  fc.first_order_merge(key, value)
  assert fc._plugin.cache == {key: value}
  value2 = {
    "foo2": "bar2",
    "foo3": "bar3"
  }
  fc.first_order_merge(key, value2)
  assert fc._plugin.cache == {key: {
    "foo": "bar",
    "foo2": "bar2",
    "foo3": "bar3"
  }}

# Mock class of Ansible Cache Plugin CachePlugin

# Generated at 2022-06-13 17:10:02.519306
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert(cache is not None)

# Generated at 2022-06-13 17:10:04.093756
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        from ansible.plugins.loader import cache_loader
        cache_loader._find_plugin('memory')
        factcache = FactCache()
        assert factcache
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-13 17:10:04.781859
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    print (fact_cache)



# Generated at 2022-06-13 17:10:14.922053
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    invalid_keys = ['ansible_distribution_version', 'ansible_distribution_release']
    invalid_dict = dict.fromkeys(invalid_keys, 'new_value')
    cache.first_order_merge('localhost', invalid_dict)
    assert cache['localhost']['ansible_distribution_version'] == 'new_value'
    assert cache['localhost']['ansible_distribution_release'] == 'new_value'

    valid_dict = {'ansible_distribution': 'CentOS', 'ansible_distribution_version': '7.6.1810'}
    cache.first_order_merge('localhost', valid_dict)
    assert cache['localhost']['ansible_distribution'] == 'CentOS'

# Generated at 2022-06-13 17:10:24.649386
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # verify it works on an empty cache
    fact_cache = FactCache()
    fact_cache.first_order_merge('key1', {'merge_key': 1})
    assert fact_cache.get('key1').get('merge_key') == 1

    # verify the cache contains the new value
    fact_cache = FactCache()
    fact_cache.update({'key1': {'local_cache_value': 1}})
    fact_cache.first_order_merge('key1', {'merge_key': 1})
    assert fact_cache.get('key1').get('local_cache_value') == 1
    assert fact_cache.get('key1').get('merge_key') == 1

    # if a key already exists in the cache and in the "new" facts,
    # assert that the

# Generated at 2022-06-13 17:10:28.303240
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    c = FactCache()
    c.first_order_merge("foo", {"bar": "baz"})
    assert c["foo"]["bar"] == "baz"
    c.first_order_merge("foo", {"bar": "buz"})
    assert c["foo"]["bar"] == "buz"

# Generated at 2022-06-13 17:10:29.606841
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache(None)

    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:10:43.691519
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('host', {'fact_cache': {'some_fact': False}})
    assert fc['host'] == {'fact_cache': {'some_fact': False}}

    fc.first_order_merge('host', {'fact_cache': {'some_fact': True}})
    assert fc['host'] == {'fact_cache': {'some_fact': True}}

    fc.flush()

# Generated at 2022-06-13 17:10:44.854642
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_object = FactCache()
    assert 'Expected fact cache object to be initialized'

# Generated at 2022-06-13 17:10:46.113047
# Unit test for constructor of class FactCache
def test_FactCache():
    new_fact_cache = FactCache()
    print(new_fact_cache)

# Generated at 2022-06-13 17:10:49.790254
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fact_cache = FactCache()
        assert fact_cache is not None
        assert fact_cache._plugin is not None
    except AnsibleError as e:
        assert False, "Unable to create the fact cache"


# Generated at 2022-06-13 17:10:59.613473
# Unit test for constructor of class FactCache
def test_FactCache():
    class Plugin(object):
        def __init__(self):
            self.z = {}

        def set(self, key, value):
            self.z[key] = value

        def delete(self, key):
            del self.z[key]

        def get(self, key):
            return self.z[key]

        def keys(self):
            return self.z.keys()

        def flush(self):
            self.z.clear()

        def contains(self, key):
            return key in self.z

    plugin = Plugin()
    cache = FactCache(plugin)
    cache.flush()
    cache['key'] = 'value'
    assert cache.keys() == ['key']
    assert cache['key'] == 'value'

# Generated at 2022-06-13 17:11:02.660644
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc._plugin, cache_loader.get(C.CACHE_PLUGIN))


# Generated at 2022-06-13 17:11:04.374122
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin != None

# Generated at 2022-06-13 17:11:06.376893
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)

# Generated at 2022-06-13 17:11:15.553640
# Unit test for method first_order_merge of class FactCache

# Generated at 2022-06-13 17:11:19.000615
# Unit test for constructor of class FactCache
def test_FactCache():

    def run_test():
        assert FactCache(plugin='redis')
        assert FactCache(plugin='jsonfile')

    run_test()

# Generated at 2022-06-13 17:11:34.329019
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert 'localhost' in fact_cache

# Generated at 2022-06-13 17:11:36.540664
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.common._collections_compat import MutableMapping
    f_c = FactCache()
    assert isinstance(f_c, MutableMapping)

# Generated at 2022-06-13 17:11:38.053569
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

if __name__ == "__main__":
    test_FactCache()

# Generated at 2022-06-13 17:11:48.004694
# Unit test for constructor of class FactCache
def test_FactCache():
    # Use an empty dict for cache plugin
    class EmptyDictCache(dict):
        pass

    cache = EmptyDictCache()
    cache_loader.caches[EmptyDictCache] = None
    cache_loader.set_cache(EmptyDictCache())

    # Test if the constructor raises an error when the cache plugin is not
    # initialized
    try:
        FactCache()
    except AnsibleError as error:
        assert 'Unable to load the facts cache plugin' in str(error)
    else:
        raise AssertionError('Unable to load the facts cache plugin')
    finally:
        cache_loader.caches = {}
        cache_loader.cache = None

    # Test without errors
    cache_loader.caches[EmptyDictCache] = None
    cache_loader.set_cache(cache)
    Fact

# Generated at 2022-06-13 17:11:57.443551
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.verbosity = 5
    C.CACHE_PLUGIN = 'memory'
    C.CACHE_PLUGIN_CONNECTION = ''

# Generated at 2022-06-13 17:12:03.448845
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    print(fact_cache)
    print('---------------------------------------------------')
    fact_cache.flush()
    print(fact_cache)
    print('---------------------------------------------------')
    fact_cache.first_order_merge('key0', 'value0')
    fact_cache.first_order_merge('key1', 'value1')
    fact_cache.first_order_merge('key2', 'value2')
    fact_cache.first_order_merge('key3', 'value3')
    fact_cache.first_order_merge('key4', 'value4')
    fact_cache.first_order_merge('key5', 'value5')
    fact_cache.first_order_merge('key6', 'value6')

# Generated at 2022-06-13 17:12:04.681926
# Unit test for constructor of class FactCache
def test_FactCache():
    f_cache = FactCache()
    assert f_cache
    assert isinstance(f_cache, FactCache)

# Generated at 2022-06-13 17:12:14.030766
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json
    test_cache = FactCache()
    host = '127.0.0.2'
    key = 'ansible_facts'

# Generated at 2022-06-13 17:12:14.783574
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:12:15.571438
# Unit test for constructor of class FactCache
def test_FactCache():
    return FactCache()

# Generated at 2022-06-13 17:12:52.867437
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    key = 'host_name'

    class FakePlugin:
        def contains(self, k):
            return False

        def get(self, k):
            return 'old-value'

        def set(self, k, v):
            return

        def delete(self, k):
            return

        def keys(self):
            return [key]

        def flush(self):
            return

    fake_plugin = FakePlugin()

    new_value = 'new-value'

    fact_cache = FactCache()
    fact_cache._plugin = fake_plugin

    fact_cache.first_order_merge(key, new_value)

    assert fact_cache[key] == new_value

# Generated at 2022-06-13 17:12:54.279426
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache
    except Exception as e:
        assert False, "fact_cache.py - test_FactCache_constructor Exception: %s" % str(e)


# Generated at 2022-06-13 17:13:02.617562
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.vars.hostvars import HostVars
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    host_cache = HostVars()
    play = Play()
    templar = Templar(loader=None, variables=None)


# Generated at 2022-06-13 17:13:04.648162
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, MutableMapping)

# Generated at 2022-06-13 17:13:12.231258
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''
    Test that the first_order_merge function merges the given host facts
    with the cache for that host.
    '''
    fc = FactCache()
    host = dict(
        ansible_all_ipv4_addresses=['10.0.0.1', '10.0.0.2', '10.0.0.3'],
        ansible_architecture='x86_64',
        ansible_default_ipv4=dict(address='10.0.0.1', alias='enp0s8', interface='enp0s8')
    )
    fc['test_host'] = host
    assert fc['test_host'] == host

# Generated at 2022-06-13 17:13:12.909789
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()



# Generated at 2022-06-13 17:13:19.660761
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cached_facts = FactCache()

    test_facts = {
        'test': {
            'fact1': 'first_fact',
            'fact2': 'second_fact',
            'fact3': 'third_fact',
            'fact4': 'fourth_fact',
            'fact5': 'fifth_fact',
        }
    }

    # Read values from cached_facts
    #
    # [WARNING] below code will fail if any of the fact names are set as
    # variables with values that are "truthy" (e.g. if 'fact1' is set as 1)
    # in *config.yml* files.
    try:
        cached_facts['test']['fact1']
    except KeyError:
        pass

# Generated at 2022-06-13 17:13:20.908217
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact


# Generated at 2022-06-13 17:13:22.577791
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    ns = {}

# Generated at 2022-06-13 17:13:24.212925
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.fact_cache import FactCache
    fact_cache = FactCache()
    return fact_cache

# Generated at 2022-06-13 17:14:34.492685
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import pytest
    from ansible.module_utils._text import to_native

    fact_cache = FactCache()
    key = "localhost"
    value = {"foo": "bar"}

    fact_cache.first_order_merge(key, value)

    try:
        assert fact_cache[key] == value
    except AssertionError as e:
        pytest.fail(to_native(e))

    value = {"foo1": "bar1"}
    fact_cache.first_order_merge(key, value)

    try:
        assert fact_cache[key] != value
    except AssertionError as e:
        pytest.fail(to_native(e))

    value = {"foo": "bar1"}
    fact_cache.first_order_merge(key, value)


# Generated at 2022-06-13 17:14:41.947116
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host = "127.0.0.1"
    fact_dict = {u'foo': u'bar', u'baz': u'bar'}
    fact_cache.first_order_merge(host, fact_dict)
    cached_fact_dict = fact_cache["127.0.0.1"]
    assert 'bar' == cached_fact_dict['foo']
    assert 'bar' == cached_fact_dict['baz']
    assert '127.0.0.1' in fact_cache

# Generated at 2022-06-13 17:14:50.846270
# Unit test for constructor of class FactCache
def test_FactCache():
    import tempfile

    cache_dir = tempfile.mkdtemp()
    fact_cache = FactCache(directory=cache_dir)

    assert fact_cache.__getitem__('test') == {}
    fact_cache.__setitem__('test', {'foo': 'bar'})
    assert fact_cache.__getitem__('test') == {'foo': 'bar'}
    assert fact_cache.__contains__('test')
    assert fact_cache.keys() == ['test']
    assert fact_cache.copy() == {'test': {'foo': 'bar'}}
    fact_cache.__delitem__('test')
    assert fact_cache.keys() == []
    fact_cache.flush()
    assert fact_cache.keys() == []

# Generated at 2022-06-13 17:14:52.440848
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:14:54.142977
# Unit test for constructor of class FactCache
def test_FactCache():
    # create an instance of the FactCache class
    fact_cache = FactCache()
    assert fact_cache


# Generated at 2022-06-13 17:14:56.291811
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:14:57.753611
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    fc.flush()



# Generated at 2022-06-13 17:14:59.915154
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:15:01.566290
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
        assert(False)
    except AnsibleError:
        pass


# Generated at 2022-06-13 17:15:02.886612
# Unit test for constructor of class FactCache
def test_FactCache():

    display.debug("Test: test_FactCache()")

    test_fact_cache = FactCache()


# Generated at 2022-06-13 17:17:16.031468
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.constants import CACHE_PLUGIN
    class Cache(object):
        def __init__(self):
            self.contains = None
            self.delete = None
            self.flush = None
            self.get = None
            self.set = None

    cache = Cache()
    orig_CACHE = Cache()
    CACHE_PLUGIN = cache
    fact_cache = FactCache()
    assert fact_cache._plugin == cache
    CACHE_PLUGIN = orig_CACHE

# Generated at 2022-06-13 17:17:21.496098
# Unit test for constructor of class FactCache
def test_FactCache():
    with open("./test/test_utils.py", "r") as test_file:
        display.verbosity=2
        assert(test_file != None), "Unable to open ./test/test_utils.py"
        fc = FactCache()
        fc['test_key'] = test_file.read()
        assert(len(fc) == 1)


# Generated at 2022-06-13 17:17:27.863052
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Check that the constructor of class FactCache works as expected
    """
    facts_cache = FactCache()
    assert facts_cache
    assert isinstance(facts_cache, FactCache)
    # Raise error if cache plugin doesn't exist
    C.CACHE_PLUGIN = 'unexisting_plugin'
    try:
        facts_cache = FactCache()
    except AnsibleError as e:
        assert 'Unable to load the facts cache plugin' in e.message
    finally:
        C.CACHE_PLUGIN = '/dev/null'

# Generated at 2022-06-13 17:17:28.671536
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    fact_cache.flush()

# Generated at 2022-06-13 17:17:29.838568
# Unit test for constructor of class FactCache
def test_FactCache():

    fc = FactCache()
    assert isinstance(fc, FactCache)

