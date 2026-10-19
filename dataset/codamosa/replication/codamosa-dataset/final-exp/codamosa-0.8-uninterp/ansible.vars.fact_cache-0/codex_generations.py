

# Generated at 2022-06-13 17:07:34.021924
# Unit test for constructor of class FactCache
def test_FactCache():
    obj = FactCache()
    assert obj._plugin  # pylint: disable=protected-access
    assert isinstance(obj._plugin, dict)  # pylint: disable=protected-access

# Generated at 2022-06-13 17:07:42.268281
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('host', {'ansible_distribution_release': '7.8'})
    assert cache['host'] == {u'ansible_distribution_release': u'7.8'}
    cache.first_order_merge('host', {'ansible_distribution_release': '9.9'})
    assert cache['host'] == {u'ansible_distribution_release': u'9.9'}
    cache.first_order_merge('host', {'ansible_os_family': 'RedHat'})



# Generated at 2022-06-13 17:07:42.852329
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()


# Generated at 2022-06-13 17:07:47.659085
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    key = 'key'
    value = {'key2': 'value2'}

    fc.first_order_merge(key, value)
    assert fc[key]['key2'] == value['key2']

    new_value = {'key2': 'new_value2'}
    fc.first_order_merge(key, new_value)
    assert fc[key]['key2'] == new_value['key2']

# Generated at 2022-06-13 17:07:51.804837
# Unit test for constructor of class FactCache
def test_FactCache():

    import ansible.plugins.cache as cache_plugins
    cache_plugins._fact_cache = None

    fact_cache = FactCache()

    assert fact_cache._plugin is not None
    assert isinstance(fact_cache, MutableMapping)

# Generated at 2022-06-13 17:07:55.242959
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key = "192.168.1.1"
    value = {"ansible_shell_type": "fish"}
    fact_cache.first_order_merge(key, value)
    assert fact_cache.get(key) == value



# Generated at 2022-06-13 17:08:06.273676
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    filename = 'test_FactCache.cache'

    fc_instance = FactCache()

    fc_instance._plugin.flush()
    assert fc_instance._plugin.contains('host1') == False
    assert fc_instance._plugin.contains('host2') == False

    # host1 facts are not in the fact cache
    # host1 facts should be stored in cache
    fc_instance.first_order_merge('host1', {'fact1': 'val1'})
    assert fc_instance._plugin.contains('host1') == True

    # host2 facts are not in the fact cache
    # host2 facts should be stored in cache
    fc_instance.first_order_merge('host2', {'fact1': 'val1'})

# Generated at 2022-06-13 17:08:10.064880
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Unit test for constructor of class FactCache
    """
    fact_cache = FactCache()
    fact_cache[u'localhost'] = {u'a': 1, u'b': 2}
    fact_cache[u'localhost'] = {u'b': 3, u'c': 4}

# Generated at 2022-06-13 17:08:19.955007
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_key = "test_key"
    test_value = {"test_key_value": "test_value"}
    test_m1 = {"test_key_m1": "test_m1"}
    test_m2 = {"test_key_m2": "test_m2"}

    test_cache = FactCache()
    test_cache.__setitem__(test_key, test_value)
    test_first_order_merge = test_cache.first_order_merge(test_key, test_m1)
    test_first_order_merge = test_cache.first_order_merge(test_key, test_m2)

    test_cache_item = test_cache.__getitem__(test_key)

# Generated at 2022-06-13 17:08:30.151438
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()

    # key and value exist
    key = 'test-key-0'
    value = {
        'test_fact_0': 'test-value-0'
    }
    host_cache = fc._plugin.get(key)
    assert not host_cache

    fc.first_order_merge(key, value)
    host_cache = fc._plugin.get(key)

    assert host_cache is not None
    assert host_cache['test_fact_0'] == 'test-value-0'

    # key and value do not exist
    key = 'test-key-1'
    host_cache = fc._plugin.get(key)
    assert not host_cache

    value = {
        'test_fact_1': 'test-value-1'
    }


# Generated at 2022-06-13 17:08:33.028969
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Run above constructor with no arguments
    """
    fact_cache = FactCache()


# Generated at 2022-06-13 17:08:39.311359
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('first_key', 'first_value')
    obj_1 = {'second_key': 'second_value'}
    fact_cache.first_order_merge('second_key', obj_1)
    obj_2 = {'third_key': 'third_value'}
    fact_cache.first_order_merge('third_key', obj_2)
    assert fact_cache['first_key'] == 'first_value'
    assert fact_cache['second_key'] == {'second_key': 'second_value'}
    assert fact_cache['third_key'] == {'third_key': 'third_value'}
    assert len(fact_cache) == 3

# Generated at 2022-06-13 17:08:40.773598
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert(isinstance(fc, FactCache))


# Generated at 2022-06-13 17:08:46.430449
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    # first test
    assert cache.first_order_merge('one','one') == {}
    cache.flush()
    # second test
    assert cache.first_order_merge('one','one') == {}
    cache['one'] = {'test':'test'}
    assert cache.first_order_merge('one','one') == {'one': {'test':'test'}}
    cache.flush()
    # third test
    assert cache.first_order_merge('one','one') == {}
    cache['one'] = {'test':'test'}
    assert cache.first_order_merge('one',{'test_2':'test_2'}) == {'one': {'test':'test'}}
    cache.flush()
    # fourth test

# Generated at 2022-06-13 17:08:48.146383
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fc = FactCache()
    except Exception:
        assert(0), "Failed to create FactCache object"

# Generated at 2022-06-13 17:08:54.673810
# Unit test for constructor of class FactCache
def test_FactCache():
    host_facts = {
        'ansible_all_ipv4_addresses': [
            '10.0.0.1', '10.0.0.2', '10.0.0.3'
        ]
    }

    fact_cache = FactCache()
    fact_cache.update(host_facts)

    assert 'ansible_all_ipv4_addresses' in fact_cache

    # Test that the value was added to the cache
    assert '10.0.0.1' in fact_cache['ansible_all_ipv4_addresses']

# Generated at 2022-06-13 17:08:55.847951
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:08:57.296122
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    fact_cache.__init__()

# Generated at 2022-06-13 17:09:07.973696
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    CACHE_PLUGIN = 'jsonfile'
    CACHE_PLUGIN_CONNECTION = './'
    CACHE_PLUGIN_TIMEOUT = 0
    cache_loader.set_fact_cache(CACHE_PLUGIN, CACHE_PLUGIN_CONNECTION, CACHE_PLUGIN_TIMEOUT)
    factcache = FactCache()

    factcache['key'] = {'a': 'b'}
    factcache.first_order_merge('key', {'c': 'd', 'e': 'f'})
    assert factcache['key'] == {'a': 'b', 'c': 'd', 'e': 'f'}

# Generated at 2022-06-13 17:09:09.348870
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin
    assert isinstance(fact_cache, MutableMapping)


# Generated at 2022-06-13 17:09:13.298639
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert 'localhost' in fact_cache


# Generated at 2022-06-13 17:09:13.821390
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact

# Generated at 2022-06-13 17:09:14.321216
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache != None

# Generated at 2022-06-13 17:09:18.637099
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    from ansible.plugins.cache import fact_cache
    from ansible.plugins.cache.memory import FactCacheModule

    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'memory'
    fac = FactCache()
    assert isinstance(fac._plugin, FactCacheModule)

    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'jsonfile'
    try:
        fac = FactCache()
        assert False
    except AnsibleError:
        assert True

# Generated at 2022-06-13 17:09:20.154324
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:09:22.001371
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    print("**cache:%s\n" % cache)

# Generated at 2022-06-13 17:09:24.031752
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    assert fact_cache.__class__.__name__ == 'FactCache'


# Generated at 2022-06-13 17:09:25.399969
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    # Test that there is no exception thrown

# Generated at 2022-06-13 17:09:34.167818
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.cache import fact_cache
    from ansible.utils import context_objects as co
    from unit.mock.loader import DictDataLoader

    loader = DictDataLoader({})
    co.GlobalCLIArgs._ansible_args = None
    co.GlobalCLIArgs._ansible_args_conf = None

    def fake_get_playbook_basedir(playbook_path):
        return playbook_path

    task_result = TaskResult()
    task_result.task_uuid = 'fake_uuid'
    task_result.task_path = 'fake_path'

    task_result._get_playbook_basedir = fake_get_playbook_basedir
    task_result._task = {}
    task_result._

# Generated at 2022-06-13 17:09:37.422669
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    fact_cache.flush()

    fact_cache['localhost'] = {'foo': 'foo_value'}

    fact_cache.first_order_merge('localhost', {'bar': 'bar_value'})

    assert fact_cache['localhost'] == {'foo': 'foo_value', 'bar': 'bar_value'}

# Generated at 2022-06-13 17:09:52.904512
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''
    Unit test for method first_order_merge of class FactCache.
    :return:
    '''
    fact_cache = FactCache()
    fact_cache.first_order_merge('localhost', {'somekey': 'somevalue'})


# Generated at 2022-06-13 17:09:54.699564
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert facts
    assert facts.keys() == []
    assert list(facts) == []


# Generated at 2022-06-13 17:10:00.897203
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    # Test default plugin
    assert fc._plugin.__class__.__name__ == 'FactCacheData'

    # Test when no fact_caching plugins are available
    for plugin_type in ['fact_cache', 'facter']:
        prev_plugins = cache_loader.all(include_hidden=True)
        cache_loader.all(include_hidden=True).pop(plugin_type, None)
        with pytest.raises(AnsibleError) as err:
            FactCache()
        assert 'Unable to load the facts cache plugin' in str(err)

        # Restore plugins
        cache_loader.all(include_hidden=True).update(prev_plugins)

# Generated at 2022-06-13 17:10:07.293686
# Unit test for constructor of class FactCache
def test_FactCache():
    test_facts = ['test_fact3', 'test_fact1', 'test_fact2']

    # Create new object of class FactCache
    fact_cache = FactCache()

    # Add facts to fact cache
    fact_cache['test_fact1'] = 'fact1'
    fact_cache['test_fact2'] = 'fact2'
    fact_cache['test_fact3'] = 'fact3'

    # Assert facts have been added to fact_cache
    assert sorted(fact_cache.keys()) == test_facts
    assert fact_cache.copy() == {'test_fact1': 'fact1', 'test_fact2': 'fact2', 'test_fact3': 'fact3'}

    # Remove a fact from fact_cache
    del fact_cache['test_fact2']

# Generated at 2022-06-13 17:10:08.390298
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    print(cache)



# Generated at 2022-06-13 17:10:19.035073
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    cache = FactCache()

    test_key = 'test_key'
    test_value = {'fact_1': 1, 'fact_2': 2}

    assert cache.first_order_merge(test_key, test_value) == None
    assert cache.first_order_merge(test_key, {'fact_1': 100, 'fact_3': 3}) == None
    assert cache[test_key] == {'fact_1': 100, 'fact_2': 2, 'fact_3': 3}

    cache[test_key] = test_value
    assert cache.first_order_merge(test_key, {'fact_4': 4}) == None
    assert cache[test_key] == {'fact_1': 1, 'fact_2': 2, 'fact_4': 4}


# Generated at 2022-06-13 17:10:27.336412
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.config.manager import ensure_type
    from ansible.utils.display import Display

    display = Display()
    config = ensure_type({'cache_plugin': 'BasicCacheModule', 'host_key_checking': True, 'display': display}, 'TheCache')
    fact_cache = FactCache(config)
    assert(len(fact_cache) == 0)
    assert(not fact_cache)
    fact_cache['abc'] = 'def'
    fact_cache['ghi'] = 'jkl'
    assert(len(fact_cache) == 2)
    assert('abc' in fact_cache)
    assert(fact_cache['abc'] == 'def')
    assert('ghi' not in fact_cache)
    assert(fact_cache['ghi'] == 'jkl')

# Generated at 2022-06-13 17:10:34.210449
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Generated by make test FETCHER_NAME=setup_module_info
    # Compare with file test/unit/plugins/cache/setup_module_info_test.py
    # When update test from test/unit/plugins/cache/setup_module_info_test.py
    # please remove this comment

# Generated at 2022-06-13 17:10:44.958383
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host = "dummy1"
    facts = {'key1': 'value1'}
    factcache = FactCache()
    factcache.load_facts(host, facts)
    host_facts = factcache[host]
    assert host_facts
    assert host_facts['key1'] == 'value1'
    assert factcache.contains(host)

    facts = {'key1': 'value2'}
    factcache.first_order_merge(host, facts)
    assert factcache.contains(host)
    assert factcache[host]
    assert factcache[host].get('key1') == 'value1'
    assert factcache[host].get('key2') is None

# Generated at 2022-06-13 17:10:48.492046
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("localhost", {"foo": "bar"})
    assert fc["localhost"]["foo"] == "bar"

    fc.first_order_merge("localhost", {"hello": "world"})
    assert fc["localhost"]["hello"] == "world"

# Generated at 2022-06-13 17:10:59.350815
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert isinstance(factcache, FactCache)


# Generated at 2022-06-13 17:11:06.118167
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('test_key', {'test_key1': 2})
    assert fc['test_key']['test_key1'] == 2
    fc.first_order_merge('test_key', {'test_key1': 5})
    assert fc['test_key']['test_key1'] == 5

# Generated at 2022-06-13 17:11:07.738111
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

# Generated at 2022-06-13 17:11:10.844391
# Unit test for constructor of class FactCache
def test_FactCache():
    # WHEN
    fc = FactCache()

    # THEN
    assert isinstance(fc, FactCache)
    assert hasattr(fc, '_plugin')
    assert isinstance(fc._plugin, MutableMapping)



# Generated at 2022-06-13 17:11:18.219058
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # a cache with 2 host
    cache = FactCache()
    cache['host1'] = dict(key1='value1', key2='value2')
    cache['host2'] = dict(key5='value5', key6='value6')

    # present facts for host1
    present_facts = dict(key1='new_value1', key3='new_value3')

    # merge present facts into cache
    cache.first_order_merge('host1', present_facts)

    # get cache for host1
    cache['host1']

    # assert that cache of host1 has 3 keys
    assert len(cache['host1'].keys()) == 3
    # assert that cache of host1 has updated values
    assert cache['host1']['key1'] == 'new_value1'

# Generated at 2022-06-13 17:11:19.452869
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    return cache

# Generated at 2022-06-13 17:11:20.714208
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert isinstance(f, FactCache)



# Generated at 2022-06-13 17:11:23.675071
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test that instanciation of an empty FactCache object is possible
    :return:
    """
    fc = FactCache()
    assert fc is not None



# Generated at 2022-06-13 17:11:28.987818
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('test','test')
    assert cache['test'] == 'test'
    cache.first_order_merge('test','test2')
    assert cache['test'] == 'test2'
    cache.first_order_merge('test2','test2')
    assert cache['test2'] == 'test2'

# Generated at 2022-06-13 17:11:30.405359
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache(dict())

# Generated at 2022-06-13 17:11:43.977120
# Unit test for constructor of class FactCache
def test_FactCache():
    # Run FactCache's constructor.
    # FactCache.__init__
    # FactCache.__init__ as FactCache._MutableMapping__init__

    # Verify that the object is of type FactCache.
    assert isinstance(FactCache, FactCache)

    # Verify that the constructor can accept the following arguments:
    # *args, **kwargs

# Generated at 2022-06-13 17:11:53.287607
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    # Ensure that we start with an empty cache
    assert len(fact_cache) == 0

    # Test basic insertion
    first_key = 'foo'
    first_value = ['first_entry']
    fact_cache.first_order_merge(first_key, first_value)

    assert fact_cache[first_key] == first_value
    assert len(fact_cache) == 1

    # Test insertion of a second key
    second_key = 'bar'
    second_value = ['second_entry']
    fact_cache.first_order_merge(second_key, second_value)

    assert fact_cache[first_key] == first_value
    assert fact_cache[second_key] == second_value
    assert len(fact_cache) == 2

    # Test re

# Generated at 2022-06-13 17:11:54.768417
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert ('_plugin' in fact_cache.__dict__)


# Generated at 2022-06-13 17:12:02.226432
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    plugin = fact_cache._plugin
    test_data = {'ansible_ssh_host': '127.0.0.1'}
    # add test data into fact_cache
    plugin.set('127.0.0.1', test_data)
    assert '127.0.0.1' in fact_cache
    # test get function
    assert fact_cache.get('127.0.0.1', {}) == test_data
    # test get function, with key not exist
    assert fact_cache.get('192.168.0.1', {}) == {}
    # test delitem function
    del fact_cache['127.0.0.1']
    assert '127.0.0.1' not in fact_cache
    # test flush function

# Generated at 2022-06-13 17:12:03.506950
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:12:04.505582
# Unit test for constructor of class FactCache
def test_FactCache():
    # Create a dummy cache object
    fc = FactCache()

# Generated at 2022-06-13 17:12:14.030832
# Unit test for constructor of class FactCache
def test_FactCache():
    class Type:
        def __init__(self, *args, **kwargs):
            pass
        def __getitem__(self, key):
            pass
        def __setitem__(self, key, value):
            pass
        def __delitem__(self, key):
            pass
        def __contains__(self, key):
            pass
        def __iter__(self):
            return iter(self._plugin.keys())
        def __len__(self):
            return len(self._plugin.keys())

    obj = Type()
    assert isinstance(obj, Type)
    assert "__len__" in dir(obj)
    assert "__contains__" in dir(obj)
    assert "__setitem__" in dir(obj)
    assert "__delitem__" in dir(obj)

# Generated at 2022-06-13 17:12:15.102986
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:12:15.878012
# Unit test for constructor of class FactCache
def test_FactCache():
    print(FactCache())

# Generated at 2022-06-13 17:12:22.905426
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # Check for fact cache file for fact caching
    fact_cache_file = loader.path_dwim('facts_cache')

    fact_cache = FactCache(fact_cache_file)

    hostname = 'myhostname'

    fact_cache.first_order_merge(hostname, {'first': 'fact', 'second': 'fact'})

    assert(hostname in fact_cache)
    assert(fact_cache[hostname]['first'] == 'fact')
    assert(fact_cache[hostname]['second'] == 'fact')

    new_facts = {'first': 'overwritten', 'second': 'fact', 'third': 'fact'}


# Generated at 2022-06-13 17:12:48.994682
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factCache = {'some_key': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}}
    test_cache = FactCache()
    for key in factCache:
        test_cache.first_order_merge(key, factCache.get(key))
    assert(test_cache == factCache)

# Generated at 2022-06-13 17:12:50.097618
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        f = FactCache()
    except Exception as e:
        assert e

# Generated at 2022-06-13 17:12:59.095607
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fc = FactCache()
    test_data = {
        'ansible_default_ipv4': {'address': '1.1.1.1'},
        'ansible_default_ipv6': {'address': '3001:3:3::3'},
        'ansible_interfaces': [],
    }
    test_value = {
        'ansible_default_ipv4': {'address': '8.8.8.8', 'gateway': '8.8.8.1'},
        'ansible_default_ipv6': {'address': 'fd00::1', 'gateway': 'fd00::1'},
        'ansible_interfaces': []
    }
    fc.update(test_data)

# Generated at 2022-06-13 17:12:59.861863
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    assert c is not None

# Generated at 2022-06-13 17:13:06.114459
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3

    my_cache = FactCache()

    if PY3:
        my_stdout = StringIO()
    else:
        my_stdout = StringIO(unicode(''))

    my_key = 'my_machine'
    my_value = {'fqdn': 'my_machine.my_domain', 'my_key_1': 'my_value_1', 'my_key_2': 'my_value_2'}

    my_cache.first_order_merge(my_key, my_value)
    assert len(my_cache) == 1
    assert my_cache[my_key] == my_value


# Generated at 2022-06-13 17:13:09.675447
# Unit test for constructor of class FactCache
def test_FactCache():
    '''

    This is a UnitTest for the constructor of class FactCache

    '''
    fact_cache = FactCache()
    display.display("Loaded FactCache")



# Generated at 2022-06-13 17:13:12.163693
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    if not fact_cache:
        print("Module error: test1")
    if not fact_cache.keys():
        print("Module error: test2")

# Generated at 2022-06-13 17:13:13.242122
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:13:19.827667
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''this function will return true if all test cases are passed, else returns false'''

    #creating instances for FactCache class
    fact_cache_obj = FactCache()
    fact_cache_obj_1 = FactCache()


    #test case 1
    try:
        fact_cache_obj['f1'] = {'g1':{'h1':None}}
        fact_cache_obj_1['f1'] = {'g1':{'h1':None}}
    except KeyError:
        print ('f1 is not present in cache')

     #test case 2

# Generated at 2022-06-13 17:13:21.124873
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache.keys() == []

# Generated at 2022-06-13 17:14:17.774043
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    print(fc.keys())
    print(fc.values())
    print(fc.items())

# Generated at 2022-06-13 17:14:21.774248
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("127.0.0.1", {"cmdline": "runas"})
    fc.first_order_merge("127.0.0.1", {"cmdline2": "runas2"})
    assert isinstance(fc["127.0.0.1"], dict)
    assert fc["127.0.0.1"]["cmdline"] == "runas"
    assert fc["127.0.0.1"]["cmdline2"] == "runas2"

# Generated at 2022-06-13 17:14:22.659030
# Unit test for constructor of class FactCache
def test_FactCache():
    a = FactCache()
    assert a

# Generated at 2022-06-13 17:14:24.466593
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc.__class__.__name__ == 'FactCache'

# Generated at 2022-06-13 17:14:26.565688
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("foo", "bar")
    assert fc.keys() == ["foo"]

# Generated at 2022-06-13 17:14:27.697720
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache(C.CACHE_PLUGIN)

#FactCache()

# Generated at 2022-06-13 17:14:29.144334
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    return fact_cache

# Unit test of method '__getitem__'

# Generated at 2022-06-13 17:14:36.131081
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    host_facts = {'test_host': {'test_key': 'test_value'}, 'other_host': {'other_key': 'other_value'}}
    cache.first_order_merge('test_host', host_facts['test_host'])
    cache.first_order_merge('other_host', host_facts['other_host'])
    cache.first_order_merge('test_host', {'test_key': 'new_test_value'})

    assert 'test_host' in cache
    assert cache['test_host']['test_key'] == 'new_test_value'

    assert 'test_host' not in cache['other_host']
    assert 'other_host' not in cache['test_host']

    assert 'test_host' in cache

# Generated at 2022-06-13 17:14:37.794180
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:14:48.215998
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache.first_order_merge('host.example.com', {'ansible_os_family': 'Debian'})
    factcache.first_order_merge('host.example.com', {'ansible_distribution': 'Debian', 'ansible_distribution_version': '8'})
    assert factcache['host.example.com'] == {'ansible_os_family': 'Debian', 'ansible_distribution': 'Debian', 'ansible_distribution_version': '8'}
    factcache.first_order_merge('host.example.com', {'ansible_os_family': 'RedHat', 'ansible_distribution': 'RedHat', 'ansible_distribution_version': '7'})
    assert factcache['host.example.com']

# Generated at 2022-06-13 17:16:45.193021
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    # Assert False for emptly fact_cache object
    assert(not fact_cache)

# Generated at 2022-06-13 17:16:46.327727
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache_object = FactCache()
    assert factcache_object is not None

# Generated at 2022-06-13 17:16:53.495622
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()

    # Test a key that doesn't already exist in the cache
    test_dict = {'test_key': 'test_value'}
    test_cache.first_order_merge('test_key', test_dict)
    assert test_cache['test_key'] == test_dict

    # Test a key that does already exist in the cache with a different vlaue
    # this should not overwrite
    test_dict2 = {'test_key': 'test_value2'}
    test_cache.first_order_merge('test_key', test_dict2)
    assert test_cache['test_key'] == {'test_key': 'test_value'}

    # Test a key that does already exist in the cache with the same value
    # this should not overwrite
    test_cache.first

# Generated at 2022-06-13 17:17:02.400792
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    data_new = {
        "facter_fact1" : "value1",
        "facter_fact2" : "value2"
    }
    data_updated = {
        "facter_fact1" : "value1",
        "facter_fact2" : "value2 updated"
    }
    test_cache.first_order_merge("host1", data_new)
    assert test_cache._plugin.get('host1') == data_new
    test_cache.first_order_merge("host1", data_updated)
    assert test_cache._plugin.get('host1') == data_updated

# Generated at 2022-06-13 17:17:04.859597
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('localhost', {'version': '2.7'})
    fact_cache.first_order_merge(
        'localhost', {'version': '2.6', 'foo': 'bar'})
    assert fact_cache['localhost'] == {'version': '2.6', 'foo': 'bar'}

# Generated at 2022-06-13 17:17:10.867666
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import pytest
    from ansible.plugins.terminal import TerminalPlugin
    from ansible.plugins.loader import cache_loader

    class TestPlugin(TerminalPlugin):
        NAME = 'test'
        CACHE_HIT = 0
        CACHE_MISS = 0

        def __init__(self):
            self._cache = {}

        def get(self, key):
            self.CACHE_HIT += 1
            return self._cache[key]

        def set(self, key, value):
            self._cache[key] = value

        def delete(self, key):
            del self._cache[key]

        def contains(self, key):
            return key in self._cache

        def keys(self):
            return self._cache.keys()

        def flush(self):
            self._cache = {}

# Generated at 2022-06-13 17:17:13.447287
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import BaseCacheModule
    import tests.unit.utils.plugins.my_cache_plugin as my_cache_plugin
    my_cache_plugin.set_loader(BaseCacheModule)

    fact = FactCache()
    assert fact._plugin is not False

# Generated at 2022-06-13 17:17:23.339031
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import memory

    display.verbosity = 1
    fc = FactCache()
    assert 'memory' == fc._plugin.__class__.__name__
    assert fc._plugin is memory.FactCacheModule()

    fc.__setitem__('testkey', 'testvalue')
    assert fc.__contains__('testkey')
    assert 'testvalue' == fc.__getitem__('testkey')
    assert len(fc) == 1
    fc.__delitem__('testkey')
    assert len(fc) == 0
    assert not fc.__contains__('testkey')

    fc.__setitem__('testkey1', 'testvalue1')
    fc.__setitem__('testkey2', 'testvalue2')
    fc.__

# Generated at 2022-06-13 17:17:24.796051
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:17:29.584175
# Unit test for constructor of class FactCache
def test_FactCache():
    import ansible.plugins.cache.jsonfile
    C.CACHE_PLUGIN = 'jsonfile'
    cache_plugins = cache_loader.all()
    assert 'jsonfile' in cache_plugins
    from ansible.executor.module_common import ModuleCommon

    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)
    assert fact_cache._plugin._connection._connection_info == {'conn_params': {}, 'conn_type': 'file', 'cache': True}

