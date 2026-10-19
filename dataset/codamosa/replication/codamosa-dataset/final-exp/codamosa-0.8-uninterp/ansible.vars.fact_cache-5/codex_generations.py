

# Generated at 2022-06-13 17:07:33.237632
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.__class__.__name__ == 'JsonFileCacheModule'

# Generated at 2022-06-13 17:07:35.622030
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Constructor of class FactCache
    :return:
    """
    factCache = FactCache()
    assert factCache

# Generated at 2022-06-13 17:07:43.672210
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('f', {'k': 'v'})
    assert fc['f'] == {'k': 'v'}
    fc.first_order_merge('f', {'k2': 'v2'})
    assert fc['f'] == {'k': 'v', 'k2': 'v2'}
    fc.first_order_merge('f', {'k': 'v_test'})
    assert fc['f'] == {'k': 'v_test', 'k2': 'v2'}

# Generated at 2022-06-13 17:07:45.763385
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
    except AnsibleError as e:
        assert True
    else:
        assert False


# Generated at 2022-06-13 17:07:47.781590
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f.__class__.__name__ == 'FactCache'

# Generated at 2022-06-13 17:07:48.538897
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:07:57.034315
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    key = 'some_host'
    value1 = dict(foo='bar')
    value2 = dict(bar='baz')

    # Test initialization
    assert key not in facts_cache

    # Test adding a value
    facts_cache.first_order_merge(key, value1)
    assert key in facts_cache
    assert facts_cache[key] == value1

    # Test updating a value
    facts_cache.first_order_merge(key, value2)
    assert facts_cache[key] != value1
    assert facts_cache[key] != value2
    assert facts_cache[key]['foo'] == 'bar'
    assert facts_cache[key]['bar'] == 'baz'

# Generated at 2022-06-13 17:07:58.008369
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()

# Generated at 2022-06-13 17:08:08.388528
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # create a new object
    fact_cache = FactCache()
    
    # update the cache
    fact_cache.update({"a": "value1", "b": "value2"})

    # test the method first_order_merge
    fact_cache.first_order_merge("a", "value3")
    fact_cache.first_order_merge("c", "value4")
    fact_cache.first_order_merge("d", "value5")
    
    assert fact_cache.keys() == ["a", "b", "c", "d"] == list(fact_cache.keys())
    assert fact_cache["a"] == "value3"
    assert fact_cache["b"] == "value2"
    assert fact_cache["c"] == "value4"
    assert fact_cache["d"]

# Generated at 2022-06-13 17:08:18.864244
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader
    from ansible.utils.display import Display
    from ansible.utils.path import unfrackpath
    from ansible.cli.playbook import PlaybookCLI, PlaybookCLIError
    import datetime, os, pytest
    from units.mock.loader import DictDataLoader
    from ansible.plugins.cache.jsonfile import CacheModule as JsonFileCacheModule

    mytestdir = os.path.dirname(unfrackpath(__file__))
    c = PlaybookCLI(['ansible-playbook'])
    c._cleanup_processed_args()
    c._load_config_file()
    # create an empty json file, and set the CACHE_PLUGIN to be jsonfile

# Generated at 2022-06-13 17:08:24.217967
# Unit test for constructor of class FactCache
def test_FactCache():
    fcache = FactCache()

    # assert all variables
    assert fcache._plugin != None

# assert that FactCache class is of type MutableMapping
assert issubclass(FactCache, MutableMapping)

# Generated at 2022-06-13 17:08:32.752290
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.config.manager import ConfigManager
    from ansible.constants import FAKE_COLLECTION_PATHS
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    config_manager = ConfigManager()

    config_manager.push_basedir(FAKE_COLLECTION_PATHS)

    config_manager.set('cache_plugin', 'memory')

    cache_loader.add("memory", collections_paths=FAKE_COLLECTION_PATHS)

    display.verbosity = 3

    collection_loader = AnsibleCollectionLoader()

    fact_cache = FactCache(None, config_manager, collection_loader)

    assert fact_cache.flush() is None
    assert fact_cache.copy() == {}
    assert fact_cache.keys() is None
    assert fact_cache.first_order

# Generated at 2022-06-13 17:08:41.928651
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = "test_key"
    value = {"a": "b"}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'a': 'b'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'a': 'b'}

    value = {"a": "c"}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'a': 'b', 'a': 'c'}
    # cache contains two 'a' keys - this is because the first :
    # fact_cache.first_order_merge(key, value) adds {'a': 'b'}
    # and the second :

# Generated at 2022-06-13 17:08:44.409161
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('key1', {'key2': 'value2'})
    fact_cache.first_order_merge('key1', {'key2': 'value2new', 'key3': 'value3'})

    assert fact_cache.get('key1')['key3'] == 'value3'

# Generated at 2022-06-13 17:08:53.268915
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setup host_facts and host_cache
    host_facts_a = {'a': 'b', 'c': {'d': 'e'}}
    host_cache_a = {'a': 'b'}
    host_cache_b = {'a': 'b', 'c': {'d': 'e'}}
    host_cache_c = {'c': 'd'}
    host_cache_d = {'e': 'f'}
    host_cache_e = {'c': 'd', 'e': 'f'}
    expected_host_facts_a = {'a': 'b', 'c': {'d': 'e'}}

    # Create a new instance of FactCache
    fact_cache = FactCache()

    # Call first_order_merge with host_facts and host_cache returned by

# Generated at 2022-06-13 17:08:54.421666
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)


# Generated at 2022-06-13 17:08:58.932526
# Unit test for constructor of class FactCache
def test_FactCache():
    import pytest
    fact_cache = FactCache()
    assert pytest.isinstance(fact_cache, FactCache)
    assert len(fact_cache) == 0
    fact_cache["host1"] = {"data": "here"}
    assert "host1" in fact_cache
    assert fact_cache["host1"] == {"data": "here"}
    fact_cache.flush()
    assert len(fact_cache) == 0
    assert "host1" not in fact_cache

# Generated at 2022-06-13 17:09:10.134366
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

    assert cache._plugin
    assert cache.__class__.__name__ == 'FactCache'

    # Test if keys of the cache are empty before we set the items in it
    assert cache.keys() == []

    # Test __contains__ method
    assert (False == ('test_fact_key' in cache))

    # Test __setitem__ method
    cache['test_fact_key'] = 'test_fact_value'

    # Test the keys in the cache
    assert cache.keys() == ['test_fact_key']

    # Test __getitem__ method
    assert cache['test_fact_key'] == 'test_fact_value'

    # Test __delitem__ method
    del cache['test_fact_key']

    # Test __contains__ method

# Generated at 2022-06-13 17:09:18.347308
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = 'key_for_test'
    value = {'fact_1': {'sub_fact_1': 'sub_fact_val_1'},
             'fact_2': {'sub_fact_2': 'sub_fact_val_2'},
             'fact_3': {'sub_fact_3': 'sub_fact_val_3'}
            }
    # This is the first time we are setting this key, so no conflict expected
    fact_cache.first_order_merge(key, value)
    # Verify the fact is correctly added
    assert fact_cache.__contains__(key)
    assert fact_cache.get(key) == value

    # Simulate a second plugin sending a fact with same key

# Generated at 2022-06-13 17:09:27.726284
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    # Create a sample fact, with a single entry
    test_fact = {
        "ansible_eth0": {
            "active": True,
            "device": "eth0",
            "ipv4": {
                "address": "192.168.1.9",
                "broadcast": "192.168.1.255",
                "netmask": "255.255.255.0",
                "network": "192.168.1.0"
            },
            "ipv6": [
            ],
            "macaddress": "08:00:27:e7:65:e0",
            "module": "e1000",
            "mtu": 1500,
            "promisc": False,
            "type": "ether"
        }
    }
    # Update the fact

# Generated at 2022-06-13 17:09:31.045101
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache


# Generated at 2022-06-13 17:09:38.767451
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    from datetime import datetime

    class MockCachePlugin(object):
        def __init__(self):
            self.cache = {}

        def get(self, key):
            return self.cache[key]

        def set(self, key, value):
            self.cache[key] = value

        def delete(self, key):
            del self.cache[key]

        def contains(self, key):
            return key in self.cache

        def keys(self):
            return self.cache.keys()

        def flush(self):
            self.cache = {}

    # Create mock plugin
    plugin = MockCachePlugin()

    # Create cache
    cache = FactCache()
    cache._plugin = plugin

    # Inject some facts
    cache["foo.example.com"] = {"ansible_uptime_seconds": 100}


# Generated at 2022-06-13 17:09:39.998039
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    # FIXME: add more tests here, assert exceptions, etc.


# Generated at 2022-06-13 17:09:40.549596
# Unit test for constructor of class FactCache
def test_FactCache():
    print('In test_FactCache')

# Generated at 2022-06-13 17:09:51.073081
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    C.CACHE_PLUGIN = 'jsonfile'
    fc = FactCache()
    # test case 1: key does not exist in facts cache
    facts = dict(ansible_os_family='Linux')
    fc.first_order_merge('testhost', facts)
    assert(fc['testhost'] == facts)
    del fc['testhost']

    # test case 2: key exists in facts cache
    facts = dict(ansible_os_family='Linux')
    fc['testhost'] = facts
    facts = dict(ansible_os_family='RedHat', ansible_distribution='Fedora')
    fc.first_order_merge('testhost', facts)

# Generated at 2022-06-13 17:09:55.912570
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # test with no previous facts
    cache = FactCache()
    cache.first_order_merge('key1', {'a': 1})
    assert cache['key1'] == {'a': 1}

    # test with previous facts
    cache.first_order_merge('key1', {'b': 2})
    assert cache['key1'] == {'a': 1, 'b': 2}


# Generated at 2022-06-13 17:10:01.980911
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    facts_cache.first_order_merge('localhost', {'foo': 42})
    assert facts_cache['localhost'] == {'foo': 42}

    facts_cache.first_order_merge('localhost', {'bar': 'baz'})
    assert facts_cache['localhost'] == {'foo': 42, 'bar': 'baz'}

# Generated at 2022-06-13 17:10:04.602739
# Unit test for constructor of class FactCache
def test_FactCache():
    obj = FactCache()
    assert isinstance(obj, FactCache)
    assert hasattr(obj, 'flush')
    assert hasattr(obj, 'first_order_merge')
    assert hasattr(obj, '__contains__')
    assert hasattr(obj, 'keys')

# Generated at 2022-06-13 17:10:12.863444
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('host1', {'ansible_os_family': 'Linux'})
    assert 'host1' in fact_cache
    fact_cache.first_order_merge('host1', {'ansible_os_family': 'Windows'})
    assert fact_cache['host1']['ansible_os_family'] == 'Windows'
    fact_cache.first_order_merge('host1', {'ansible_distribution': 'Ubuntu'})
    assert fact_cache['host1']['ansible_distribution'] == 'Ubuntu'



# Generated at 2022-06-13 17:10:20.835699
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge("localhost", {'test': 'hello'})
    assert cache[("localhost", 'test')] == "hello"
    cache.first_order_merge("localhost", {'test': 'world'})
    assert cache[("localhost", 'test')] == "world"
    cache.first_order_merge("me", {'test': 'hello'})
    assert cache[("me", 'test')] == "hello"

if __name__ == '__main__':
    test_FactCache_first_order_merge()

# Generated at 2022-06-13 17:10:26.170361
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)

# Generated at 2022-06-13 17:10:29.909264
# Unit test for constructor of class FactCache
def test_FactCache():
    def invoke_init( plugin_name ):
        from ansible import context
        context.CLIARGS = {'fact_caching':'memory'}
        from ansible import constants
        constants.CACHE_PLUGIN = plugin_name
        return FactCache()

    try:
        invoke_init('memory')
        assert True
    except Exception:
        assert False

# Generated at 2022-06-13 17:10:34.512181
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    actual_result = {}
    new_facts = { 'fact1': 'value1' }
    fact_cache.first_order_merge('host1', new_facts)
    expected_result = {'host1': {'fact1': 'value1'}}
    assert actual_result == expected_result
    new_facts = { 'fact1': 'value2' }
    fact_cache.first_order_merge('host1', new_facts)
    expected_result = {'host1': {'fact1': 'value2'}}
    assert actual_result == expected_result

# Generated at 2022-06-13 17:10:36.721659
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact.keys() == []

# Generated at 2022-06-13 17:10:37.938046
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()



# Generated at 2022-06-13 17:10:46.348720
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    fact_name = 'my_fact'
    fact_value = "my_fact_value"
    fact_dict = {'fact_name': fact_value}

    factcache.first_order_merge(fact_name, fact_dict)
    fact_dict['new_fact'] = 'new_fact_value'
    factcache.first_order_merge(fact_name, fact_dict)

    assert factcache.get(fact_name)['fact_name'] == fact_value
    assert factcache.get(fact_name)['new_fact'] == 'new_fact_value'

# Generated at 2022-06-13 17:10:57.548650
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ Method to unit test first_order_merge method of FactCache class """

    # Test 1: No key in cache
    fact_cache = FactCache()
    key = 'test1'
    value = {'ansible_facts': {'test': 'test_value'}}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value

    # Test 2: No key in cache
    fact_cache = FactCache()
    key = 'test2'
    value = {'ansible_facts': {'test': 'test_value1'}}
    fact_cache.first_order_merge(key, value)
    value = {'ansible_facts': {'test': 'test_value2'}}
    fact_cache.first_order_merge(key, value)

# Generated at 2022-06-13 17:11:06.468220
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache['1.1.1.1'] = {}
    fact_cache['1.1.1.1']['A'] = 'a'
    fact_cache['1.1.1.1']['B'] = 'b'
    fact_cache.first_order_merge('1.1.1.1', {'C':'c','A':'z'})
    print(fact_cache['1.1.1.1'])
# {'B': 'b', 'C': 'c', 'A': 'a'}

# Generated at 2022-06-13 17:11:11.537382
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins import cache_loader
    fc = cache_loader.get("memory")
    fc.flush()

    fc.set("test", {'a': 1})
    assert fc.get("test") == {'a': 1}

    fc.set("test", {'b': 2})
    assert fc.get("test") == {'b': 2}

    fc.set("test", {'a': 1, 'b': 2, 'c': 3})
    assert fc.get("test") == {'a': 1, 'b': 2, 'c': 3}

    fc.flush()
    assert fc.get("test") is None

# Generated at 2022-06-13 17:11:17.789522
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    my_cache = FactCache()
    key = 'testkey'
    first_value = {'first': 'firstvalue'}
    second_value = {'second': 'secondvalue'}

    # No key available, should not raise an Exception
    my_cache.first_order_merge(key, first_value)

    # The first key should be available
    assert my_cache[key] == first_value

    # Change the value of the key
    my_cache.first_order_merge(key, second_value)

    # The second value has to be in the dict
    assert my_cache[key] == {'first': 'firstvalue', 'second': 'secondvalue'}

# Generated at 2022-06-13 17:11:35.472078
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_cache = {'hostname01': {'ansible_facts': {'a': 1, 'b': 1}}, 'hostname02': {'ansible_facts': {'a': 2, 'b': 2}}}
    
    fact_cache = FactCache()
    fact_cache._plugin = {'test': test_cache}

    fact_cache.first_order_merge('hostname01', {'ansible_facts': {'a': 1, 'b': 2}})
    assert fact_cache['hostname01']['ansible_facts']['a'] == 1
    assert fact_cache['hostname01']['ansible_facts']['b'] == 2

# Generated at 2022-06-13 17:11:39.807223
# Unit test for constructor of class FactCache
def test_FactCache():
  import tempfile
  import shutil
  from ansible.plugins.cache import jsonfile
  C.CACHE_PLUGIN = 'jsonfile'
  temp_dir = tempfile.mkdtemp()
  try:
    jsonfile.FactsCacheModule.CACHE_DIR = temp_dir
    cache_path = jsonfile.FactsCacheModule.CACHE_DIR
    assert FactCache
    assert cache_path
  finally:
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 17:11:42.679330
# Unit test for constructor of class FactCache
def test_FactCache():
    ''' Unit test for class FactCache '''
    fact_cache = FactCache()
    assert fact_cache._plugin


# Generated at 2022-06-13 17:11:44.110919
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache != None and fact_cache._plugin != None

# Generated at 2022-06-13 17:11:44.881007
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:11:47.623103
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    ret = cache._plugin.__class__.__name__
    assert ret == "GenericFactCacheModule"


# Generated at 2022-06-13 17:11:57.077063
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.DEBUG("test_FactCache_first_order_merge() init")
    fact_cache = FactCache()
    facts = dict(
        ansible_eth1=dict(
            active=True,
            device="eth1",
            ipv4=dict(
                address="192.168.1.10",
                netmask="255.255.255.0",
                network="192.168.1.0"
            ),
            ipv6=[],
            macaddress="fe:54:00:1e:65:d0",
            module="e1000",
            mtu=1500,
            promisc=True,
            type="ether"
        )
    )
    fact_cache.first_order_merge('localhost', facts)

# Generated at 2022-06-13 17:12:04.443988
# Unit test for constructor of class FactCache
def test_FactCache():

    cache = FactCache()

    # test __init__
    cached = cache_loader.get(C.CACHE_PLUGIN)
    assert isinstance(cached, cache._plugin.__class__)

    # test __getitem__
    cache['fizz'] = 'buzz'
    assert cache['fizz'] == 'buzz'

    # test __setitem__
    cache['fizz'] = 'buzz'
    assert cache['fizz'] == 'buzz'

    # test __contains__
    assert 'fizz' in cache.keys()

    # test __delitem__
    del cache['fizz']
    assert 'fizz' not in cache.keys()

    # test __iter__
    cache['fizz'] = 'buzz'
    cache['mike'] = 'mike'

# Generated at 2022-06-13 17:12:12.106458
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()

    host = 'host'
    cache[host] = {}

    key = 'test'

    value = 'value'
    cache.first_order_merge(host, {key: value})

    result = cache[host][key]
    assert result == value, "'%s' != '%s'" % (result, value)

    value = 'value2'
    cache.first_order_merge(host, {key: value})

    result = cache[host][key]
    assert result == value, "'%s' != '%s'" % (result, value)

# Generated at 2022-06-13 17:12:18.208250
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''Test merging of facts'''

    factCache = FactCache()
    factCache.__setitem__('host1', {'hostname': 'host1'})

    # Test relations when the cache_key is present in the cache but not
    # the host_fact
    factCache.first_order_merge('host1', {'ip': '1.2.3.4'})
    assert factCache.__getitem__('host1') == {'ip': '1.2.3.4', 'hostname': 'host1'}

    # Test relations when the cache_key is present in the cache and also
    # in the host_fact.
    # If host_fact is cached it is expected to be later in the execution
    # and hence its value should be used.

# Generated at 2022-06-13 17:12:35.368896
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:12:41.047664
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_cache = FactCache()

    # Test every method of class CachePlugin
    facts_cache.__getitem__('test')
    facts_cache.__setitem__('test', 'test')
    facts_cache.__delitem__('test')
    assert 'test' in facts_cache
    facts_cache.flush()
    assert len(facts_cache) == 0
    assert facts_cache.copy() == {}
    assert facts_cache.keys() == []

# Generated at 2022-06-13 17:12:45.401230
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader

    cache_plugin = cache_loader.get(C.CACHE_PLUGIN)

    fc = FactCache()
    result = fc._plugin == cache_plugin
    assert result == True

    if not cache_plugin:
        fc = FactCache()
        assert fc == None

# Generated at 2022-06-13 17:12:46.796979
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)

# Generated at 2022-06-13 17:12:51.457892
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()

    factcache.first_order_merge('foo', {'a': 1, 'b': 2})
    assert factcache['foo'] == {'a': 1, 'b': 2}

    factcache.first_order_merge('foo', {'c': 3})
    assert factcache['foo'] == {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-13 17:12:52.119210
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:12:58.974186
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache({"one": {"a": 1}})
    assert facts_cache.keys() == ["one"]

    facts_cache.first_order_merge("one", {"a": 2})
    assert facts_cache.keys() == ["one"]
    assert facts_cache["one"] == {"a": 2}

    facts_cache.first_order_merge("two", {"b": 2})
    assert facts_cache.keys() == ["one", "two"]
    assert facts_cache["one"] == {"a": 2}
    assert facts_cache["two"] == {"b": 2}

# Generated at 2022-06-13 17:13:00.642819
# Unit test for constructor of class FactCache
def test_FactCache():
    loader = cache_loader.get('jsonfile')
    fc = FactCache(loader)
    assert isinstance(fc, FactCache) == True

# Generated at 2022-06-13 17:13:04.134675
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    host_cache = test_cache['testinventory'] = {'testkey': 'testvalue'}
    test_cache.first_order_merge('testinventory', {'testkey': 'testvalue2', 'testkey2': 'testvalue2'})
    assert test_cache['testinventory'] == {'testkey': 'testvalue2', 'testkey2': 'testvalue2'}

# Generated at 2022-06-13 17:13:05.391762
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.name == 'memory'

# Generated at 2022-06-13 17:13:40.367112
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:13:45.294495
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache.first_order_merge(u'localhost', {u'ansible_os_family': u'Debian'})
    assert u'localhost' in factcache
    assert list(factcache.keys()) == [u'localhost']
    assert u'ansible_os_family' in factcache[u'localhost']
    assert factcache[u'localhost'][u'ansible_os_family'] == u'Debian'

# Generated at 2022-06-13 17:13:51.357427
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # Setting up fact_cache object
    fact_cache = FactCache()
    # Set the plugin
    fact_cache._plugin = cache_loader.get('memory')

    # Set the host fact
    host_facts = {"ansible_default_ipv4": {"address": "10.0.0.10"}}

    # Add the host fact in cache
    fact_cache.first_order_merge('123', host_facts)

    merged_facts = fact_cache.get('123')
    # Asserting the merged fact

# Generated at 2022-06-13 17:13:52.215764
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache



# Generated at 2022-06-13 17:13:54.713304
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    my_FactCache = FactCache()

    host_facts = {
        "foo": {
            "bar": "bam",
            "baz": "buz"
        }
    }

    my_FactCache.first_order_merge("foo", host_facts)
    # Assert that KeyError was not raised
    assert True

# Generated at 2022-06-13 17:13:56.414480
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    # TODO: test that get/set/delete/contains/flush/keys/copy/first_order_merge are called

# Generated at 2022-06-13 17:13:58.503383
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.facts.cache import FactCache
    facts = FactCache()
    assert isinstance(facts, FactCache)
    facts._plugin.flush()


# Generated at 2022-06-13 17:13:59.425124
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None

# Generated at 2022-06-13 17:14:04.158405
# Unit test for constructor of class FactCache
def test_FactCache():
    # The constructor of class FactCache should raise an AnsibleError if an invalid cache plugin name
    # is provided
    try:
        fact_cache = FactCache(None)
        raise Exception("AnsibleError should have been raised")
    except AnsibleError:
        pass

# Generated at 2022-06-13 17:14:06.181139
# Unit test for constructor of class FactCache
def test_FactCache():

    c = FactCache()

    import sys
    assert c is not None
    assert sys.version_info[0] < 3 or isinstance(c, MutableMapping)

# Generated at 2022-06-13 17:15:11.397594
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    assert len(fact_cache) == 0



# Generated at 2022-06-13 17:15:11.817722
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:15:14.274517
# Unit test for constructor of class FactCache
def test_FactCache():
    """ Unit test for constructor of class FactCache """
    fc = FactCache()
    assert(fc)

# Generated at 2022-06-13 17:15:15.908153
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.facts import default_collectors
    test = FactCache(default_collectors)
    assert test._plugin


# Generated at 2022-06-13 17:15:19.502561
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin_name = 'memory'
    C.CACHE_PLUGIN = plugin_name
    C.FACTS_CACHE = True
    assert cache_loader.get(plugin_name) is not None
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:15:20.253388
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    assert fact_cache

# Generated at 2022-06-13 17:15:21.599529
# Unit test for constructor of class FactCache
def test_FactCache():

    cache = FactCache(stdout_callback='json')
    assert cache

# Generated at 2022-06-13 17:15:22.825006
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    assert c is not None
    assert isinstance(c, FactCache)

# Generated at 2022-06-13 17:15:24.463385
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        a = FactCache()
        assert False
    except AnsibleError:
        assert True

# Generated at 2022-06-13 17:15:26.698366
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)
