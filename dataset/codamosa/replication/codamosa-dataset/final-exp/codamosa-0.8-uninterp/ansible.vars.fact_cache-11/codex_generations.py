

# Generated at 2022-06-13 17:07:37.483957
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('localhost', {'a': {'b': 'x'}})
    cache.first_order_merge('localhost', {'a': {'c': 'z'}})
    assert cache.keys() == ['localhost']
    assert cache['localhost'] == {'a': {'b': 'x', 'c': 'z'}}

# Generated at 2022-06-13 17:07:40.998179
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'localhost'
    fact_cache[key] = {}
    value = {'a': 1, 'b': 2}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value



# Generated at 2022-06-13 17:07:46.816259
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = 'key_test'
    value = {'a': 'aaa'}
    cache.first_order_merge(key, value)

    assert cache == {'key_test': {'a': 'aaa'}}
    cache.first_order_merge(key, {'b': 'bbb'})
    assert cache == {'key_test': {'a': 'aaa', 'b': 'bbb'}}

# Generated at 2022-06-13 17:07:48.776724
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f
    assert isinstance(f, FactCache)


# Generated at 2022-06-13 17:07:55.208175
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    value = {'a': 1, 'b': 2}
    fact_cache.first_order_merge("test", value)

    assert(fact_cache._plugin.get("test") == value)

    value = {'b': 3, 'c': 4}
    fact_cache.first_order_merge("test", value)

    assert(fact_cache._plugin.get("test") == {'a': 1, 'b': 3, 'c': 4})

# Generated at 2022-06-13 17:07:59.127128
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ test for method first_order_merge of class FactCache"""
    new_dict = {'a': 1}
    old_dict = {'a': 1, 'b': 2}
    hostname = 'localhost'
    # Since ansible-2.4, old_dict will be merged into new_dict
    FactCache().first_order_merge(hostname, new_dict)
    FactCache().first_order_merge(hostname, old_dict)
    assert FactCache()[hostname] == old_dict

# Generated at 2022-06-13 17:08:08.392226
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    host = 'test_host'
    key = 'stdout_lines'
    value = [b'hello', b'world']

    fc.first_order_merge(host, {key: value})
    assert fc[host][key] == value

    fc.first_order_merge(host, {key: None})
    assert fc[host][key] is None

    fc.first_order_merge(host, {key: b'foo'})
    assert fc[host][key] == [b'foo']

    fc.first_order_merge(host, {key: 'bar'})
    assert fc[host][key] == [b'foo', b'bar']

# Generated at 2022-06-13 17:08:15.150992
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    key = 'localhost'
    value = {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Debian',
        'ansible_distribution_version': '10'
    }
    fact_cache.first_order_merge(key, value)
    # print(fact_cache)
    # assert fact_cache[key] == value
    # print(fact_cache.copy())



# Generated at 2022-06-13 17:08:21.105264
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    test_cache["test"] = {}
    test_cache.first_order_merge("test", {"a":"b"})
    assert test_cache["test"] == {"a":"b"}
    test_cache.first_order_merge("test", {"a":"c"})
    assert test_cache["test"] == {"a":"c"}
    test_cache.first_order_merge("test", {"b":"d"})
    assert test_cache["test"] == {"a":"c", "b":"d"}

# Generated at 2022-06-13 17:08:25.034162
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'localhost'
    value = {
        'ansible_distribution': 'Fedora',
        'ansible_distribution_major_version': '26',
        'ansible_distribution_version': '26 (Rawhide)',
        'ansible_interfaces': [
            'ens34',
            'lo'
        ]
    }
    fact_cache.first_order_merge(key, value)
    assert len(fact_cache) == 1
    assert fact_cache['localhost'] == value

# Generated at 2022-06-13 17:08:34.448847
# Unit test for constructor of class FactCache
def test_FactCache():
    # Construct an instance of fact cache using the constructor.
    fact_cache = FactCache()

    # Check for the keys in the fact cache instance.
    assert(iter(fact_cache) == list())

    # Check for the length of the keys in the fact cache instance.
    assert(len(fact_cache) == 0)

    # Check whether the fact cache instance is empty or not.
    assert(fact_cache.__contains__("test_host") == False)

    # Get the values for the key in the fact cache instance.
    assert(fact_cache.__getitem__("test_host") == None)

    # Set the values for the key in the fact cache instance.
    fact_cache.__setitem__("test_host", "test")

    # Check whether the fact cache instance is empty or not.

# Generated at 2022-06-13 17:08:38.678129
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    hostname = "key1"
    host_facts = {"fact1": "val1", "fact2": "val2"}
    cache.first_order_merge(hostname, host_facts)
    assert cache[hostname] == host_facts
    host_facts.update({"fact3": "val3"})
    cache.first_order_merge(hostname, host_facts)
    assert cache[hostname] == host_facts


# Generated at 2022-06-13 17:08:39.825688
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:08:44.870640
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    new_fact_value = {
        "first_fact": "value1",
        "second_fact": "value2"
    }

    host_cache = {
        "first_fact": "value1",
        "second_fact": "value2"
    }

    fact_cache.first_order_merge(host="test_host", value=new_fact_value)
    assert fact_cache["test_host"] == host_cache

# Generated at 2022-06-13 17:08:46.808592
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test the __init__ of class FactCache
    """
    cache = FactCache(plugin='jsonfile')
    assert cache._plugin

# Generated at 2022-06-13 17:08:55.537402
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # fixtures
    cache_key = 'localhost'
    host_facts = {
        'ansible_distribution': 'Ubuntu',
        'ansible_distribution_version': '16.04',
        'ansible_hostname': 'ansible-test-hostname'
    }

    # patch
    class mock_cache:
        def __init__(self):
            self.cache_key = None
            self.cache_value = None

        def get(self, key):
            if key == self.cache_key:
                return self.cache_value
            else:
                raise KeyError

        def set(self, key, value):
            self.cache_key = key
            self.cache_value = value

    mock_cache = mock_cache()

    # test
    fact_cache = FactCache()
    fact

# Generated at 2022-06-13 17:08:59.755710
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Arrange
    test_cache = FactCache()

    # Act
    test_cache.first_order_merge("key1", {"hello": "world"})

    # Assert
    assert test_cache == {"key1": {"hello": "world"}}

    # Act
    test_cache.first_order_merge("key1", {"foo": "bar"})

    # Assert
    assert test_cache == {"key1": {"hello": "world", "foo": "bar"}}

# Generated at 2022-06-13 17:09:00.532512
# Unit test for constructor of class FactCache
def test_FactCache():
    setup_cache = FactCache()
    assert setup_cache._plugin

# Generated at 2022-06-13 17:09:01.992411
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    return f

# Generated at 2022-06-13 17:09:08.711509
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = { "ansible_os_family": "RedHat" }

    fact_cache.first_order_merge('localhost', host_facts)
    assert(fact_cache['localhost'] == host_facts)

    # update and check that the dictionary was really updated
    host_facts = { "ansible_os_family": "Debian" }
    fact_cache.first_order_merge('localhost', host_facts)
    assert(fact_cache['localhost'] == host_facts)

# Generated at 2022-06-13 17:09:13.159188
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)
    assert cache._plugin is not None


# Generated at 2022-06-13 17:09:19.604284
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible.plugins.cache import jsonfile

    key1 = 'key1'
    data_value1_1 = 'data_value1_1'
    data_value1_2 = 'data_value1_2'
    data_value1_3 = 'data_value1_3'
    data_value1_4 = 'data_value1_4'
    key2 = 'key2'
    data_value2_1 = 'data_value2_1'
    data_value2_2 = 'data_value2_2'
    data_value2_3 = 'data_value2_3'

    # test invalid ansible_cache_plugin setting
    # case 1: ansible_cache_plugin is set

# Generated at 2022-06-13 17:09:28.657607
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache['test_key'] = {'a': 'hello', 'b': 'goodbye'}
    new_value = {'a': 'goodnight', 'c': 'something new'}
    cache.first_order_merge('test_key', new_value)
    assert cache['test_key'] == {'a': 'goodnight', 'b': 'goodbye', 'c': 'something new'}

    cache = FactCache()
    new_value = {'a': 'goodnight', 'c': 'something new'}
    cache.first_order_merge('test_key', new_value)
    assert cache['test_key'] == {'a': 'goodnight', 'c': 'something new'}

# Generated at 2022-06-13 17:09:33.550450
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    key = 'dummyhost'
    value = {'a':'b'}
    factcache = FactCache()
    factcache.first_order_merge(key, value)
    assert factcache[key] == value
    value = {'b':'c'}
    factcache.first_order_merge(key, value)
    assert factcache[key] == {'a':'b', 'b':'c'}

# Generated at 2022-06-13 17:09:39.904380
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    host_1 = "host_1"
    host_2 = "host_2"
    host_1_facts = {
        "host1_fact1": "host1_fact1_value_1",
        "host1_fact2": "host1_fact2_value_1",
        "host1_fact3": "host1_fact3_value_1"
    }

    host_2_facts = {
        "host1_fact1": "host1_fact1_value_2",
        "host1_fact2": "host1_fact2_value_2",
        "host1_fact3": "host1_fact3_value_2"
    }


# Generated at 2022-06-13 17:09:40.602701
# Unit test for constructor of class FactCache
def test_FactCache():
    print("I am in test")

# Generated at 2022-06-13 17:09:50.837902
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ Unit test for method first_order_merge of class FactCache """
    fact_cache = FactCache()
    fact_cache.first_order_merge("a", {"b": 1})
    fact_cache.first_order_merge("a", {"c": 2})
    fact_cache.first_order_merge("b", {"d": 3})
    fact_cache.first_order_merge("b", {"e": 4})

    # There should be two dictionary keys in fact_cache
    assert len(fact_cache) == 2
    # and each of those keys should contain two dictionary items
    assert len(fact_cache["a"]) == 2
    assert len(fact_cache["b"]) == 2


# Test invocation of FactCache via AnsibleContext

# Generated at 2022-06-13 17:09:51.706649
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

    assert isinstance(cache, MutableMapping) is True


# Generated at 2022-06-13 17:09:53.612304
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    assert factcache.first_order_merge('key','value') == {'key':'value'}

# Generated at 2022-06-13 17:10:00.815549
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache('facts')
    assert cache is not None
    assert cache.__class__.__name__ == 'FactCache'
    assert cache.__class__.__module__ == 'ansible.plugins.cache.fact_cache'
    assert cache.__class__.__bases__ == (MutableMapping,)
    assert cache.__len__() == 0
    assert cache.keys() == []
    assert cache.get('missing') is None
    cache['test_key'] = 'test_value'
    assert cache.__len__() == 1
    assert cache.keys() == ['test_key']
    assert cache.get('test_key') == 'test_value'
    assert cache['test_key'] == 'test_value'
    assert cache.first_order_merge('test_key', 'test_value')

# Generated at 2022-06-13 17:10:07.115395
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:08.276753
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert fc._plugin

# Generated at 2022-06-13 17:10:10.323026
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test for creating object for class FactCache
    """
    fact_cache_obj = FactCache()
    assert fact_cache_obj

# Generated at 2022-06-13 17:10:20.467132
# Unit test for constructor of class FactCache
def test_FactCache():

    from ansible.module_utils.facts import ansible_facts

    fc = FactCache()
    assert(fc)
    assert(isinstance(fc, MutableMapping))
    assert(isinstance(fc, FactCache))
    assert(fc._plugin)

    new_facts_dict = ansible_facts(loader=None)
    fc.first_order_merge('foo.bar.faz', new_facts_dict)
    assert(fc['foo.bar.faz'])
    assert(fc.keys()[0] == 'foo.bar.faz')
    assert(len(fc) == 1)
    assert(fc['foo.bar.faz'] == new_facts_dict)

    fc.flush()
    assert(len(fc) == 0)

# Generated at 2022-06-13 17:10:22.630264
# Unit test for constructor of class FactCache

# Generated at 2022-06-13 17:10:30.488259
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    qm = TaskQueueManager(
        inventory=PlaybookExecutor(playbooks=['test_playbook.yml'])._inventory,
        variable_manager=PlaybookExecutor(playbooks=['test_playbook.yml'])._variable_manager,
        loader=PlaybookExecutor(playbooks=['test_playbook.yml'])._loader,
        options=Play()._options,
        passwords=PlaybookExecutor(playbooks=['test_playbook.yml'])._passwords,
        stdout_callback='default',
    )
    assert isinstance(FactCache(), FactCache)


# Unit

# Generated at 2022-06-13 17:10:32.529647
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = cache_loader.get('memory')

    FactCacheTest = FactCache()
    assert(isinstance(FactCacheTest,MutableMapping))
    assert(isinstance(FactCacheTest._plugin, type(plugin)))



# Generated at 2022-06-13 17:10:34.694542
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:10:46.035664
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    test_host = "192.168.1.1"

# Generated at 2022-06-13 17:10:51.972487
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = {'key': {'fact1': 'value1', 'fact2': 'value2'}}
    fact_cache._plugin = {'key': {'fact1': 'value1'}}
    fact_cache.first_order_merge(host_facts)

    assert(fact_cache == {'key': {'fact1': 'value1', 'fact2': 'value2'}})

    fact_cache = FactCache()
    host_facts = {'key': {'fact1': 'value1', 'fact2': 'value2'}}
    fact_cache.first_order_merge(host_facts)

    assert(fact_cache == host_facts)

# Generated at 2022-06-13 17:11:10.020368
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    Input = {'host_key': {'host_var': 'host_val'}}
    fact_cache['host_key'] = {'host_var': 'host_val'}
    assert fact_cache['host_key'] == Input
    fact_cache.first_order_merge('host_key', {'host_var2': 'host_val2'})
    assert fact_cache['host_key'] == {'host_var2':'host_val2'}

# Generated at 2022-06-13 17:11:11.229245
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    assert c



# Generated at 2022-06-13 17:11:18.457021
# Unit test for constructor of class FactCache
def test_FactCache():
    class CachePlugin():
        def __init__(self):
            self._storage = {}

        def set(self, key, value):
            self._storage[key] = value

        def get(self, key):
            return self._storage.get(key)

        def contains(self, key):
            return key in self._storage

        def delete(self, key):
            del self._storage[key]

        def keys(self):
            return self._storage.keys()

        def flush(self):
            self._storage = {}

    class CachePluginException(Exception):
        pass

    class CachePluginWithoutPlugins(object):
        def get(self):
            pass

    class CachePluginWithoutGet(object):
        def get(self):
            pass

    cache_plugin = CachePlugin()

# Generated at 2022-06-13 17:11:19.240702
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache



# Generated at 2022-06-13 17:11:27.638319
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    def _plugin_get(key):
        if key == 'test_host':
            return {'fact_c': 'c'}
        else:
            return None

    def _plugin_set(key, value):
        pass

    def _plugin_flush():
        pass

    plugin = type('', (), {'get': _plugin_get, 'set': _plugin_set, 'flush': _plugin_flush})()

    fc = FactCache()

    fc._plugin = plugin
    fc.first_order_merge('test_host', {'fact_a': 'a', 'fact_b': 'b'})

    assert fc['test_host'] == {'fact_a': 'a', 'fact_b': 'b', 'fact_c': 'c'}

# Generated at 2022-06-13 17:11:28.731899
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.name is not None

# Generated at 2022-06-13 17:11:37.954897
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    assert fc
    host_cache = {
        "test_key1": [1,2],
        "test_key2": "test_val"
    }
    fc.first_order_merge("localhost", host_cache)
    assert "localhost" in fc
    assert len(fc) == 1
    new_host_cache = {
        "test_key1": [3],
        "test_key3": "new_val"
    }
    fc.first_order_merge("localhost", new_host_cache)
    assert len(fc["localhost"]) == 3
    assert fc["localhost"]["test_key1"] == [1,2,3]
    assert fc["localhost"]["test_key2"] == "test_val"

# Generated at 2022-06-13 17:11:38.887857
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)

# Generated at 2022-06-13 17:11:46.137271
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible_collections.ansible.community.plugins.cache.file import FactCache as FC 
    fc = FC()
    facts = {'a': 1, 'b': 2}
    fc.first_order_merge('sri', facts)
    assert fc.get('sri') == {'a': 1, 'b': 2}
    fc.first_order_merge('sri', {'b': 3, 'c': 4})
    assert fc.get('sri') == {'a': 1, 'b': 3, 'c': 4}

# Generated at 2022-06-13 17:11:47.525179
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        _ = FactCache()
    except Exception:
        raise Exception('Failed to instantiate FactCache.')

# Generated at 2022-06-13 17:12:20.074106
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()
    fact_cache.first_order_merge('some_key', {'first': 'first_value'})
    assert fact_cache.get('some_key')['first'] == 'first_value'
    fact_cache.first_order_merge('some_key', {'second': 'second_value'})
    assert fact_cache.get('some_key')['first'] == 'first_value'
    assert fact_cache.get('some_key')['second'] == 'second_value'
    fact_cache.first_order_merge('some_key', {})
    assert fact_cache.get('some_key')['first'] == 'first_value'


# Generated at 2022-06-13 17:12:21.650908
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.__class__.__name__ == 'MemoryFactCache'

# Generated at 2022-06-13 17:12:27.962814
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.cache.jsonfile import CacheModule as jsonfile
    from ansible.constants import CACHE_PLUGIN
    from ansible.errors import AnsibleError
    cache_loader.set_directory('./ansible/plugins/cache')
    cache_loader.add('jsonfile', jsonfile)
    assert cache_loader.get(CACHE_PLUGIN) == jsonfile
    try:
        cache_loader.get('not_valid')
        raise AssertionError('Did not raise exception')
    except AnsibleError as e:
        assert str(e) == 'Unable to load the facts cache plugin (not_valid).'
    fact_cache = FactCache()

test_FactCache()

# Generated at 2022-06-13 17:12:28.588780
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:12:29.762220
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:12:30.250766
# Unit test for constructor of class FactCache
def test_FactCache():
    return FactCache()

# Generated at 2022-06-13 17:12:36.653023
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_name = 'dummy_host'
    key = host_name
    value = {'ansible_facts': {'test_fact': 'fact value'}}

    fact_cache.first_order_merge(key, value)
    cache_dictionary = fact_cache[key]
    assert ('ansible_facts' in cache_dictionary), 'ansible_facts key not in cache'
    assert ('test_fact' in cache_dictionary['ansible_facts']), 'test_fact value not in ansible_facts'

    value2 = {'ansible_facts': {'test_fact': 'fact value new'}}
    fact_cache.first_order_merge(key, value2)
    cache_dictionary = fact_cache[key]

# Generated at 2022-06-13 17:12:37.800637
# Unit test for constructor of class FactCache
def test_FactCache():
    fac=FactCache()
    # if not self._plugin:
    assert fac._plugin

# Generated at 2022-06-13 17:12:39.199814
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f is not None

# Generated at 2022-06-13 17:12:46.837132
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'test_key_1'
    value = {'a': 'A', 'b': 'B'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value
    old_value = {'a': 'old', 'c': 'C'}
    fact_cache[key] = old_value
    value_updated = {'a': 'A', 'b': 'B', 'c': 'C'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value_updated

# Generated at 2022-06-13 17:13:18.010912
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache._plugin = CacheStub()

    cache_item = {'some_item': 'some_value'}
    cache.first_order_merge('test', cache_item)
    assert cache['test'] == cache_item

    new_item = {'some_item': 'new_item'}
    cache.first_order_merge('test', new_item)
    assert cache['test'] != new_item
    assert cache['test']['some_item'] == new_item['some_item']



# Generated at 2022-06-13 17:13:19.885724
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache(cache_plugin='jsonfile')
    assert f._plugin.__class__.__name__ == 'JSONFactCacheModule'

# Generated at 2022-06-13 17:13:22.664929
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin._cache_prefix == 'ansible_fact_'


# Generated at 2022-06-13 17:13:24.935871
# Unit test for constructor of class FactCache
def test_FactCache():
    """check if constructor argument and default value are the same"""
    fact_cache = FactCache()
    assert C.CACHE_PLUGIN == fact_cache._plugin._type

# Generated at 2022-06-13 17:13:26.300224
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    f['test'] = 'test'
    assert(f['test'] == 'test')

# Generated at 2022-06-13 17:13:32.915525
# Unit test for constructor of class FactCache
def test_FactCache():
    # CACHE_PLUGIN doesn't set, to set 'jsonfile' as default
    if not C.CACHE_PLUGIN:
        C.CACHE_PLUGIN = 'jsonfile'
    hostcache = FactCache()
    assert hostcache._plugin is not None
    assert C.CACHE_PLUGIN == 'jsonfile'

    # CACHE_PLUGIN sets, to set 'redis' for test.
    C.CACHE_PLUGIN = 'redis'
    hostcache_redis = FactCache()
    assert hostcache_redis._plugin is not None
    assert C.CACHE_PLUGIN == 'redis'

# Generated at 2022-06-13 17:13:34.074047
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import FactCache
    # Cache = FactCache()
    pass

# Generated at 2022-06-13 17:13:42.925237
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.plugins.cache.memory import CacheModule as Cache
    from ansible.plugins.loader import cache_loader
    from ansible.module_utils.six import PY2, PY3

    class TestCache(Cache):
        def __init__(self, *args, **kwargs):
            super(TestCache, self).__init__(*args, **kwargs)
            self._cache = {}

        def get(self, key):
            return self._cache[key]

        def set(self, key, value):
            self._cache[key] = value

        def contains(self, key):
            return key in self._cache

        def delete(self, key):
            del self._cache[key]

        def keys(self):
            return self._cache.keys()

        def flush(self):
            self._cache

# Generated at 2022-06-13 17:13:49.896320
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Initialize sample data
    factCache = FactCache()
    factCache['key1'] = {'ipv4': '192.168.1.1'}
    factCache['key2'] = {'ipv4': '192.168.1.2'}

    # Update sample data
    factCache.first_order_merge('key2', {'ipv4': '192.168.1.5'})
    
    # Update sample data
    factCache.first_order_merge('key3', {'ipv4': '192.168.1.6'})

    # Check data
    assert factCache['key1'] == {'ipv4': '192.168.1.1'}
    assert factCache['key2'] == {'ipv4': '192.168.1.5'}
   

# Generated at 2022-06-13 17:13:50.561402
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), FactCache)

# Generated at 2022-06-13 17:14:52.264962
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

# Generated at 2022-06-13 17:15:01.101008
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Test with invalid keys
    fact_cache = FactCache()
    assert fact_cache.first_order_merge('localhost', {'ansible_os_family': 'RedHat'}) == None
    assert fact_cache.first_order_merge('localhost', {'ansible_os_family': 'Debian'}) == None
    assert fact_cache.first_order_merge('localhost', {'ansible_os_family': 'RedHat'}) == None
    assert fact_cache.get('localhost') == {'ansible_os_family': 'RedHat'}

    # Test with valid keys
    fact_cache = FactCache()
    assert fact_cache.first_order_merge('localhost', {'ansible_processor_vcpus': 12, 'ansible_processor_cores': 16}) == None
    assert fact

# Generated at 2022-06-13 17:15:02.164264
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:15:07.682682
# Unit test for constructor of class FactCache
def test_FactCache():
    # create a fact cache object
    fact = FactCache()
    fact['key1'] = 'value1'
    fact['key2'] = 'value2'
    assert len(fact) == 2
    assert fact.keys() == fact.keys()
    assert fact['key1'] == 'value1'
    assert fact['key2'] == 'value2'
    fact.flush()
    assert len(fact) == 0
    assert fact.keys() == fact.keys()
    with open('testfile', 'w+') as f:
        f.write('foo')

# Generated at 2022-06-13 17:15:13.593780
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    value = {'test_key': 1}
    test_key = 'test_key'
    fact_cache.first_order_merge(test_key, value)
    assert fact_cache['test_key'] == {'test_key': 1}

    value.update({'test_key': 2})
    fact_cache.first_order_merge(test_key, value)
    assert fact_cache['test_key'] == {'test_key': 2}

    value.update({'test_key2': 3})
    fact_cache.first_order_merge(test_key, value)
    assert fact_cache['test_key'] == {'test_key': 2, 'test_key2': 3}

# Generated at 2022-06-13 17:15:19.362176
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # test for normal execution
    a = FactCache()
    a.first_order_merge("127.0.0.1", {"test_fact":"test_value"})
    assert a["127.0.0.1"] == {"test_fact": "test_value"}

    # test for execution when there is a fact cache
    a.first_order_merge("127.0.0.1", {"test_fact2":"test_value2"})
    assert a["127.0.0.1"] == {"test_fact": "test_value", "test_fact2":"test_value2"}

    # test for execution when key is not found
    b = FactCache()
    try:
        b["127.0.0.1"]
    except KeyError:
        pass
    else:
        assert False

    # test

# Generated at 2022-06-13 17:15:27.099306
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup the test case
    key = 'host_key'
    value = {'key1': 'value1'}
    fact_cache = {key: value.copy()}

    # Instantiate the FactCache class
    fact_cache_object = FactCache()

    # Test happy case of no cache contents
    fact_cache_object.first_order_merge(key, value)
    assert fact_cache_object[key] == fact_cache[key]

    # Test happy case of cache contents
    fact_cache[key].update({'key2': 'value2'})
    fact_cache_object.first_order_merge(key, value)
    assert fact_cache_object[key] == fact_cache[key]

# Generated at 2022-06-13 17:15:30.953041
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('test', {'arbitrary': 'value'})
    assert fact_cache['test']['arbitrary'] == 'value'
    fact_cache.first_order_merge('test', {'arbitrary': 'value2'})
    assert fact_cache['test']['arbitrary'] == 'value2'

# Generated at 2022-06-13 17:15:32.314982
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:15:36.617102
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    #ARRANGE
    fact_cache = FactCache()
    fact_cache._sections = {'key': 'value'}
    key = "hostname"
    value = "hostname.contoso.com"
    #ACT
    fact_cache.first_order_merge(key, value)
    #ASSERT
    assert fact_cache._sections["hostname"] == "hostname.contoso.com"

# Generated at 2022-06-13 17:17:30.230452
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Test case 1: no cache, no existing value
    key1 = 'key1'
    value_new = {'key1_1': 'value1_1'}
    fact_cache.first_order_merge(key1, value_new)
    assert fact_cache == {key1: {'key1_1': 'value1_1'}}

    # Test case 2: no cache, existing value
    key2 = 'key2'
    value_new = {'key2_1': 'value2_1'}
    fact_cache[key2] = value_new
    fact_cache.first_order_merge(key2, {'key2_2': 'value2_2'})