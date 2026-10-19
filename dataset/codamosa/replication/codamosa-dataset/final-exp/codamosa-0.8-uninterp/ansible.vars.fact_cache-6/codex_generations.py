

# Generated at 2022-06-13 17:07:43.414392
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.inventory.host import Host
    host = Host('localhost')
    fact_cache = FactCache()

    # Test for both first and second order merge
    fact_cache.first_order_merge(host, {'first': 0, 'second': 0})
    fact_cache.first_order_merge(host, {'second': 1})
    expected_result = {host: {'first': 0, 'second': 0}}
    assert fact_cache == expected_result

    # Test for first order merge only
    fact_cache.flush()
    fact_cache.first_order_merge(host, {'first': 0, 'second': 0})
    fact_cache.first_order_merge(host, {'first': 1})
    expected_result = {host: {'first': 1, 'second': 0}}

# Generated at 2022-06-13 17:07:49.875136
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = '192.168.1.1'
    value = {'foo': 'bar'}
    cache.first_order_merge(key, value)
    cache[key] = value

    # first_order_merge should be called with a different fact,
    # because the first_order_merge method will update the cache
    value = {'baz': 'boo'}
    cache.first_order_merge(key, value)
    assert cache[key] == {'foo': 'bar', 'baz': 'boo'}


# Ansible 2.x
ANSIBLE20_CACHE = FactCache()

# Ansible 2.4+
ANSIBLE24_CACHE = FactCache()

# Legacy FactCache (Ansible 2.3 and earlier)

# Generated at 2022-06-13 17:07:51.126037
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None


# Generated at 2022-06-13 17:07:58.417364
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc,MutableMapping)
    try:
        fc = FactCache(1)
    except:
        pass
    assert isinstance(fc,MutableMapping)
    try:
        fc = FactCache(1,2,3)
    except:
        pass
    assert isinstance(fc,MutableMapping)
    try:
        fc = FactCache(1,2,3,4,5)
    except:
        pass
    assert isinstance(fc,MutableMapping)
    try:
        fc = FactCache(1,2,3,4,5,6,7)
    except:
        pass
    assert isinstance(fc,MutableMapping)

# Generated at 2022-06-13 17:08:08.569542
# Unit test for method first_order_merge of class FactCache

# Generated at 2022-06-13 17:08:10.368194
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:08:16.830856
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    This function tests the fact cache structure
    """
    fact_cache = FactCache()
    fact_cache['host1'] = {'key1': 'value1'}
    assert fact_cache['host1']['key1'] == 'value1'
    assert fact_cache.keys() == ['host1']
    assert fact_cache.copy() == {'host1': {'key1': 'value1'}}
    assert len(fact_cache) == 1
    fact_cache.flush()

# Generated at 2022-06-13 17:08:24.126621
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    class testDict(MutableMapping):
        def __init__(self):
            self._dict = {}

        def __getitem__(self, key):
            if not self._dict.contains(key):
                raise KeyError
            return self._dict.get(key)

        def __setitem__(self, key, value):
            self._dict.set(key, value)

        def __delitem__(self, key):
            self._dict.delete(key)

        def __contains__(self, key):
            return self._dict.contains(key)

        def __iter__(self):
            return iter(self._dict.keys())

        def __len__(self):
            return len(self._dict.keys())

        def flush(self):
            self._dict.flush()


# Generated at 2022-06-13 17:08:32.712861
# Unit test for constructor of class FactCache
def test_FactCache():
    # use plugin as a global
    plugin = None

    # set up a fake plugin to back the cache
    class FakePlugin:
        def __init__(self):
            self.keys = ['a', 'b', 'c']
            self.data = {'a': 1, 'b': 2, 'c': 3}

        def contains(self, key):
            return key in self.keys

        def get(self, key):
            return self.data[key]

        def set(self, key, value):
            self.data[key] = value
            self.keys.append(key)

        def delete(self, key):
            del(self.data[key])

        def flush(self):
            self.data = {}
            self.keys = []

    global plugin
    plugin = FakePlugin()
    assert plugin.keys

# Generated at 2022-06-13 17:08:34.657064
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)
    assert fact_cache._plugin is not None
    return fact_cache


# Generated at 2022-06-13 17:08:39.667121
# Unit test for constructor of class FactCache
def test_FactCache():

    from ansible.plugins.cache import fact_cache
    fc = fact_cache.FactCache()

    assert fc is not None
    assert isinstance(fc._plugin, fact_cache.FactCachePlugin)


# Generated at 2022-06-13 17:08:42.082282
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test for correct initilization of class with correct path
    display.verbosity = 3
    fc = FactCache()
    assert fc._plugin.flush
    display.verbosity = 0


# Generated at 2022-06-13 17:08:50.756822
# Unit test for constructor of class FactCache
def test_FactCache():
    import json
    from ansible.errors import AnsibleError
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.loader import cache_loader
    from ansible.utils.display import Display
    from ansible.plugins.cache.jsonfile import CacheModule as Jsonfile
    from ansible.module_utils._text import to_bytes

    display = Display()
    cache = FactCache()
    assert isinstance(cache, MutableMapping)
    assert isinstance(cache._plugin, Jsonfile)

    test_key = 'test_key'
    test_value = {'data': 123}
    cache[test_key] = test_value
    assert cache[test_key]['data'] == test_value['data']


# Generated at 2022-06-13 17:08:56.961146
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    cache = FactCache()
    cache.flush()

    cache_key = "foo"
    cache_value = {"bar": "baz"}

    cache.first_order_merge(cache_key, cache_value)

    assert cache[cache_key] == cache_value

    new_cache_value = {"fizz": "buzz"}

    cache.first_order_merge(cache_key, new_cache_value)

    assert cache[cache_key] != cache_value
    assert cache[cache_key] == {"bar": "baz", "fizz": "buzz"}

# Generated at 2022-06-13 17:08:58.776139
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None

# Generated at 2022-06-13 17:09:03.056256
# Unit test for constructor of class FactCache
def test_FactCache():
    display.display('Initializing test')
    my_fc = FactCache(cache_plugin=C.CACHE_PLUGIN)
    assert my_fc
    display.display('Done')

# Generated at 2022-06-13 17:09:06.916471
# Unit test for constructor of class FactCache
def test_FactCache():
    """ Test constructor of class FactCache """
    # Test without plugin

    C._CACHE_PLUGIN = None

    failed = False

    try:
        FactCache()
    except AnsibleError:
        failed = True

    assert failed


# Generated at 2022-06-13 17:09:08.025452
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:09:08.692710
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

    assert cache is not None

# Generated at 2022-06-13 17:09:09.412058
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()



# Generated at 2022-06-13 17:09:13.477538
# Unit test for constructor of class FactCache
def test_FactCache():
    if __name__ == '__main__':
        # Unit test for constructor of class FactCache
        assert display.verbosity == 3

# Generated at 2022-06-13 17:09:16.179167
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()
    key = '127.0.0.1'
    value = {'ansible_facts': {}}

    if '127.0.0.1' not in fact_cache:
        fact_cache.first_order_merge(key, value)

# Generated at 2022-06-13 17:09:21.472716
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()

    # Ensure cache is empty
    assert len(fc.keys()) == 0

    # Insert first set of facts
    fact_list = [('b', 'ab'), ('a', 'va'), ('c', 'ac')]
    for fact in fact_list:
        fc.first_order_merge('host', {fact[0]: fact[1]})

    # Ensure inserted facts in correct order
    assert len(fc.keys()) == 1
    host_facts = fc['host']
    for i in range(len(fact_list)):
        assert fact_list[i][0] in host_facts
        assert fact_list[i][1] == host_facts[fact_list[i][0]]

    # Insert second set of facts out of order

# Generated at 2022-06-13 17:09:23.708766
# Unit test for constructor of class FactCache
def test_FactCache():
    print('testing object FactCache')
    fc = FactCache()
    assert isinstance(fc, FactCache)
    return fc

# Generated at 2022-06-13 17:09:26.103999
# Unit test for constructor of class FactCache
def test_FactCache():
    print("Testing class FactCache for __init__()")
    fact_cache = FactCache()
    assert fact_cache is not None



# Generated at 2022-06-13 17:09:27.020228
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()

# Generated at 2022-06-13 17:09:32.199898
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()

    key = 'test_key'
    value1 = {'fact1': 'foo'}
    value2 = {'fact1': 'bar'}
    value3 = {'fact1': 'bar', 'fact2': 'foo'}

    cache.first_order_merge(key, value1)
    assert cache[key] == value1

    cache.first_order_merge(key, value2)
    assert cache[key] == value3

# Generated at 2022-06-13 17:09:36.491732
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache('test')
    cache.flush()
    assert cache.keys() == [], "Failed: Cache was not cleared"
    cache.first_order_merge('test_key', 'test_value')
    assert cache['test_key'] == 'test_value', "Failed: Cache did not set key"
    cache['test_key2'] = 'test_value2'
    assert 'test_key' in cache, "Failed: Cache did not find key"
    del cache['test_key2']
    assert 'test_key2' not in cache, "Failed: Cache could not delete key"

# Generated at 2022-06-13 17:09:37.715320
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:09:43.328574
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # test first_order_merge of FactCache
    fact_cache = FactCache()
    key = 'testkey'
    value = {'key1': 'value1'}
    fact_cache.first_order_merge(key, value)

    # test key missing
    try:
        fact_cache.__getitem__('notexistkey')
        assert False, 'the key should not exist'
    except KeyError:
        pass

    # test key exists with dictionary type (value is a dictionary)
    assert fact_cache[key]['key1'] == 'value1'

    # add another key-value pair to fact_cache
    value2 = {'key2': 'value2'}
    fact_cache.first_order_merge(key, value2)

# Generated at 2022-06-13 17:09:49.195338
# Unit test for constructor of class FactCache
def test_FactCache():
   fact_cache = FactCache()
   assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:09:58.181185
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.constants import CACHE_PLUGIN
    from ansible.plugins.cache.jsonfile import CacheModule as jsonfile

    assert CACHE_PLUGIN == "jsonfile"
    fact_cache = FactCache()
    assert isinstance(fact_cache._plugin, jsonfile)

    fact_cache['test_key'] = "test_value"
    assert fact_cache['test_key'] == "test_value"
    assert "test_key" in fact_cache
    assert len(fact_cache) == 1

    fact_cache.flush()
    assert len(fact_cache) == 0

    # insert test data
    fact_cache['test_key1'] = { 'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# Generated at 2022-06-13 17:09:59.648451
# Unit test for constructor of class FactCache
def test_FactCache():
    test_object = FactCache()
    return test_object._plugin

# Generated at 2022-06-13 17:10:06.216793
# Unit test for constructor of class FactCache
def test_FactCache():
    # Set a custom plugin
    cache_plugin = 'jsonfile'
    cache_plugin_path = '~/ansible/plugins/cache'
    cache_plugin_class = 'CacheModule'

    # Update global variable
    C.CACHE_PLUGIN = cache_plugin
    C.CACHE_PLUGIN_PATH = cache_plugin_path
    C.CACHE_PLUGIN_CLASS = cache_plugin_class

    fact_cache = FactCache()

    # Assertions
    assert fact_cache._plugin._plugin_type is cache_plugin
    assert fact_cache._plugin._plugin_path is cache_plugin_path
    assert fact_cache._plugin._plugin_class is cache_plugin_class

# Generated at 2022-06-13 17:10:12.863075
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    # basic plugin test assumes the plugin cache_type can be set to memory
    assert f._plugin.cache_type == 'memory'
    # basic assignment test, should be no exception
    f['key'] = 1
    # basic contains test
    assert f._plugin.contains('key')
    # basic __getitem__ test
    assert f['key'] == 1
    # basic __delitem__ test
    del f['key']
    assert not f._plugin.contains('key')

# Generated at 2022-06-13 17:10:22.788047
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    facts_cache = FactCache()

    # case 01: 
    # host_facts changes the host_cache
    # update the host_cache with new host_facts
    host_cache = {'foo': '01', 'bar': '02'}
    host_facts = {'foo': '01', 'bar': '03'}
    facts_cache._plugin.set('host01', host_cache)

    facts_cache.first_order_merge('host01', host_facts)
    # verify host_cache has been updated
    assert facts_cache['host01'] == {'foo': '01', 'bar': '03'}

    # case 02: 
    # host_facts changes the host_cache
    # update the host_cache with new host_facts

# Generated at 2022-06-13 17:10:23.618489
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin

# Generated at 2022-06-13 17:10:24.848647
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache()
    except Exception:
        pass

# Generated at 2022-06-13 17:10:25.735214
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), MutableMapping)

# Generated at 2022-06-13 17:10:29.518850
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    host = 'test_host'
    key = 'ansible_distribution'
    value = 'test_distro'
    facts = {key: value}

    fact_cache.first_order_merge(host, facts)
    fact_cache.flush()

    fact_cache.first_order_merge(host, facts)

# Generated at 2022-06-13 17:10:47.924900
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_facts = {'facter_user': 'ansible_user',
                  'ansible_ssh_host': '192.168.1.1',
                  'setup_package_names': 'my_packages'}
    fc = FactCache(host_facts)
    fc.first_order_merge('myhost', host_facts)
    assert fc['myhost'] == host_facts
    fc['myhost']['ansible_ssh_host'] = '192.168.1.2'
    fc.first_order_merge('myhost', host_facts)
    assert fc['myhost']['ansible_ssh_host'] == '192.168.1.2'

# Generated at 2022-06-13 17:10:59.098286
# Unit test for constructor of class FactCache
def test_FactCache():
    import imp
    import os
    import sys

    imp.reload(sys)

    test_cache_plugin = imp.load_source(
        'test_cache_plugin',
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + '/test/test_cache_plugin.py'
    )

    class FakeCachePluginModule(object):
        def get(self, key):
            return {key:
                    {
                        'testfacts': 'testfacts',
                        'test': 'working'
                    }
                    }

        def set(self, key, value):
            return True

        def delete(self, key):
            return True

        def contains(self, key):
            return True


# Generated at 2022-06-13 17:11:05.293467
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.verbosity = 3
    f = FactCache()
    f.first_order_merge('test_key', 'test_value')
    assert(f['test_key'] == 'test_value')
    f.first_order_merge('test_key', 'another_test_value')
    assert(f['test_key'] == 'test_value')

# Generated at 2022-06-13 17:11:10.098998
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc.__getitem__('key') == None
    fc.__setitem__('key', 'value')
    assert fc.__contains__('key') == True
    fc.__delitem__('key')
    assert fc.__len__() == 0

# Generated at 2022-06-13 17:11:15.665979
# Unit test for constructor of class FactCache
def test_FactCache():
    import unittest
    import ansible.plugins.cache.jsonfile

    C.CACHE_PLUGIN = 'jsonfile'
    cache_loader.get(C.CACHE_PLUGIN)

    class TestFactCache(unittest.TestCase):

        def setUp(self):
            self.mock_plugin = ansible.plugins.cache.jsonfile.CacheModule()

        def test_init(self):
            with self.assertRaises(AnsibleError):
                FactCache()

    unittest.main()

# Generated at 2022-06-13 17:11:26.168281
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.urls import ConnectionInfo
    from ansible.plugins.cache import BaseCacheModule

    class CachePlugin(BaseCacheModule):
        def __init__(self, *args, **kwargs):
            pass

        def get(self, key):
            return {key: "test_value"}

        def set(self, key, value):
            pass

        def contains(self, key):
            return True

        def delete(self, key):
            pass

        def keys(self):
            return ["test_key"]

        def flush(self):
            pass

        @staticmethod
        def get_cache_connection_info(connection):
            return ConnectionInfo()

    def my_get_cache_plugin(name):
        if name == 'test':
            return CachePlugin()


# Generated at 2022-06-13 17:11:28.953251
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert not isinstance(fact_cache, FactCache)
    fact_cache = FactCache(cache_plugin='jsonfile')
    assert isinstance(fact_cache, FactCache)


# Generated at 2022-06-13 17:11:30.854908
# Unit test for constructor of class FactCache
def test_FactCache():
    # Without init
    fc = FactCache()


# Generated at 2022-06-13 17:11:32.550097
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:11:37.660246
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    factcache = FactCache()
    factcache.first_order_merge('localhost', {'ansible_os_family': 'RedHat'})
    assert factcache is not None
    assert factcache == {u'localhost': {u'ansible_os_family': u'RedHat'}}

    factcache.first_order_merge('localhost', {'ansible_os_family': 'Debian'})
    assert factcache == {u'localhost': {u'ansible_os_family': u'Debian'}}

# Generated at 2022-06-13 17:12:05.430640
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test that no cache plugin raises an exception
    try:
        cache = FactCache()
        assert False
    except Exception:
        pass

# Generated at 2022-06-13 17:12:07.045946
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_cache = FactCache()
    assert(facts_cache.__class__.__name__ == 'FactCache')

# Generated at 2022-06-13 17:12:13.541187
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_FactCache = FactCache()
    test_FactCache.first_order_merge("localhost", {"ansible_facts": {"var1": "value1"}})
    assert(test_FactCache["localhost"] == {"ansible_facts": {"var1": "value1"}})
    test_FactCache.first_order_merge("localhost", {"ansible_facts": {"var2": "value2"}})
    assert(test_FactCache["localhost"] == {"ansible_facts": {"var1": "value1", "var2": "value2"}})

# Generated at 2022-06-13 17:12:15.775980
# Unit test for constructor of class FactCache
def test_FactCache():
    assert issubclass(FactCache, MutableMapping)
    assert set(['_init__', '_getitem__', '_setitem__']) <= set(FactCache.__dict__)

# Generated at 2022-06-13 17:12:18.170837
# Unit test for constructor of class FactCache
def test_FactCache():

    display.deprecated('FactCache()', 'Use AnsibleCollectionRef.from_module_name("ansible.builtin.fact_cache").object')
    assert(isinstance(FactCache(), FactCache))

# Generated at 2022-06-13 17:12:19.348047
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc['ansible_facts'] is not None

# Generated at 2022-06-13 17:12:23.395200
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test __init__, getitem, and keys
    fact_cache = FactCache()
    assert fact_cache.keys() == list()
    # Test __setitem__ and __contains__
    fact_cache["key_test"] = 1
    assert "key_test" in fact_cache
    # Test __getitem__
    assert fact_cache["key_test"] == 1
    # Test __delitem__
    del fact_cache["key_test"]
    assert "key_test" not in fact_cache

# Generated at 2022-06-13 17:12:25.399209
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    # Verify if it really does not raise the error
    fc.flush()
    fc.keys()
    fc.copy()
    fc.first_order_merge('key', 'value')

# Generated at 2022-06-13 17:12:33.864603
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    assert cache.keys() == []

    # Test with empty cache
    hostname = 'example.com'
    key = 'example_key'
    value = {'first': 1, 'second': 2}

    cache.first_order_merge(hostname, {key: value})
    assert cache[hostname][key] == value

    # Test with non-empty cache
    key = 'another_key'
    another_value = {'third': 3, 'fourth': 4}
    cache[hostname].update({key: another_value})

    key = 'example_key'
    yet_another_value = {'first': 10}
    cache.first_order_merge(hostname, {key: yet_another_value})


# Generated at 2022-06-13 17:12:39.236301
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    def __getitem__(self, key):
        return self._plugin.get(key)

    def __setitem__(self, key, value):
        self._plugin.set(key, value)

    def __delitem__(self, key):
        self._plugin.delete(key)

    def __contains__(self, key):
        return self._plugin.contains(key)

    def __iter__(self):
        return iter(self._plugin.keys())

    def __len__(self):
        return len(self._plugin.keys())

    def copy(self):
        """ Return a primitive copy of the keys and values from the cache. """
        return dict(self)

    def keys(self):
        return self._plugin.keys()


# Generated at 2022-06-13 17:13:40.660134
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Create instance of FactCache class
    obj = FactCache()
    # Create variables that will be used during test
    key = "key_value"
    value = "value_value"
    # Make first test
    # During this test should be created instance of plugin which will be used for tests
    obj.first_order_merge(key, value)
    # Create variables for next tests
    key2 = "key2_value"
    value2 = "value2_value"
    key3 = "key3_value"
    value3 = "value3_value"
    # Make second test
    obj[key2] = value2
    # Make third test
    obj[key3] = value3
    # Make last test

# Generated at 2022-06-13 17:13:41.241250
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()

# Generated at 2022-06-13 17:13:42.257741
# Unit test for constructor of class FactCache
def test_FactCache():
    pc = FactCache()
    assert isinstance(pc, FactCache)

# Generated at 2022-06-13 17:13:43.514628
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    assert len(fc) == 0
    assert fc._plugin


# Generated at 2022-06-13 17:13:46.912822
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge("host_one", {"a": 1, "b": 2})
    fact_cache.first_order_merge("host_one", {"b": 2, "c": 3})
    assert fact_cache == {"host_one": {"a": 1, "b": 2, "c": 3}}
    fact_cache.flush()

# Generated at 2022-06-13 17:13:50.168924
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    remote_host = 'remote_host'
    fact_cache[remote_host] = {'ansible_facts': None}
    fact_cache.first_order_merge(remote_host, {'ansible_facts': 'test_ansible_facts'})
    assert fact_cache[remote_host]['ansible_facts'] == 'test_ansible_facts'

# Generated at 2022-06-13 17:13:51.244691
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:13:56.103267
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_fact_cache = FactCache()
    # Update method overrides the entry for key in case of duplicate
    # so both updates shall result in a single entry for the key 'a'
    # with a value 'b' in result_dict
    result_dict = {'a': 'b'}
    test_fact_cache.first_order_merge('a', 'b')
    test_fact_cache.first_order_merge('a', 'b')
    assert result_dict == test_fact_cache
    # Test with some data
    test_dict = {'a': 'b', 'd': 'e'}
    result_dict = {'a': 'b', 'd': 'e'}
    test_fact_cache.first_order_merge('a', 'b')
    test_fact_cache.first_

# Generated at 2022-06-13 17:14:05.590158
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache_dict_old = {
        'host1': {
            'ansible_facts': {
                'fact1': 'fact1_old',
                'fact2': 'fact2_old'
            }
        },
    }
    fact_cache_dict_new = {
        'host1': {
            'ansible_facts': {
                'fact1': 'fact1_new',
                'fact3': 'fact3_new',
            }
        }
    }
    expected = {
        'host1': {
            'ansible_facts': {
                'fact1': 'fact1_new',
                'fact2': 'fact2_old',
                'fact3': 'fact3_new',
            }
        }
    }

# Generated at 2022-06-13 17:14:08.147321
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader

    cache = FactCache()
    assert cache._plugin == cache_loader.get(C.CACHE_PLUGIN)

# Unit tests for first_order_merge() method

# Generated at 2022-06-13 17:16:08.405529
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = {}
    fact_cache['test_host'] = {}
    fact_cache['test_host']['test_fact'] = 'test_host_test_fact'
    fact_cache['test_host']['test_fact2'] = 'test_host_test_fact2'

    fact_cache_plugin = {}
    fact_cache_plugin['test_host'] = {}
    fact_cache_plugin['test_host']['test_fact'] = 'test_host_test_fact'
    fact_cache_plugin['test_host']['test_fact2'] = 'test_host_test_fact2'
    fact_cache_plugin['test_host']['test_fact3'] = 'test_host_test_fact3'

    fact_cache_key = 'test_host'
    fact

# Generated at 2022-06-13 17:16:10.942839
# Unit test for constructor of class FactCache
def test_FactCache():
    host_cache = FactCache()
    assert host_cache.keys() == []


# Generated at 2022-06-13 17:16:11.708055
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(isinstance(fact_cache, FactCache))

# Generated at 2022-06-13 17:16:12.265174
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

# Generated at 2022-06-13 17:16:16.024617
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    try:
        fc[C.DEFAULT_HOST_LIST]
    except KeyError:
        return True
    else:
        raise Exception('Value should not exist')

# Generated at 2022-06-13 17:16:17.271332
# Unit test for constructor of class FactCache
def test_FactCache():

    fc = FactCache()
    print(fc)

test_FactCache()

# Generated at 2022-06-13 17:16:18.001837
# Unit test for constructor of class FactCache
def test_FactCache():
    assert(True)

# Generated at 2022-06-13 17:16:23.346054
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Test empty fact cache
    factcache = FactCache()
    factcache.flush()
    factcache.first_order_merge('ansible_all_ipv4_addresses', ['192.0.2.1'])
    factcache.first_order_merge('ansible_all_ipv4_addresses', ['198.51.100.1'])
    assert factcache.get('ansible_all_ipv4_addresses') == ['192.0.2.1', '198.51.100.1']

    # Test with pre-existing fact cache
    factcache.flush()
    factcache.first_order_merge('ansible_all_ipv4_addresses', ['192.0.2.1'])

# Generated at 2022-06-13 17:16:25.270190
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:16:32.912957
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()

    # When the fact is not cached yet
    key = 'test_host'