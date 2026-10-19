

# Generated at 2022-06-13 17:07:42.831813
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    # Test with a valid plugin
    try:
        assert plugin, 'Test with a valid cache plugin.'
        fc = FactCache()
    except Exception:
        raise AssertionError('Fail to initialize the class FactCache.')
    # Test without a valid plugin
    try:
        plugin = cache_loader.get('invalidCachePlugin')
        assert not plugin, 'Test without a valid cache plugin.'
        fc = FactCache()
    except Exception:
        pass
    else:
        raise AssertionError('Fail to check the validation of cache plugin.')

# Generated at 2022-06-13 17:07:46.238080
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    if not plugin:
        raise AnsibleError('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))
    else:
        assert plugin

# Generated at 2022-06-13 17:07:47.661176
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

# Generated at 2022-06-13 17:07:51.500223
# Unit test for constructor of class FactCache
def test_FactCache():
    # If no args, return a FactCache object with empty dict
    a = FactCache()
    assert isinstance(a, FactCache)
    assert len(a) == 0

# test __getitem__() function

# Generated at 2022-06-13 17:07:53.119201
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache.__class__.__name__ == 'FactCache'

# Generated at 2022-06-13 17:07:59.544563
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    assert not cache

    # Verify the returned facts for the first host
    cache.first_order_merge('1.1.1.1', {'fact_1': 'value_1'})
    assert len(cache) == 1
    assert cache['1.1.1.1'] == {'fact_1': 'value_1'}

    # Verify the returned facts for the second host
    cache.first_order_merge('2.2.2.2', {'fact_2': 'value_2'})
    assert len(cache) == 2
    assert cache['2.2.2.2'] == {'fact_2': 'value_2'}

    # Verify the returned facts for a third host with a fact to be merged

# Generated at 2022-06-13 17:08:06.191511
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge("test_host", {"test_key": "test_value.1"})
    assert fact_cache["test_host"] == {"test_key": "test_value.1"}

    fact_cache.first_order_merge("test_host", {"test_key": "test_value.2"})
    assert fact_cache["test_host"] == {"test_key": "test_value.2"}

# Generated at 2022-06-13 17:08:10.010573
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('ip', '123.4.5.6')
    fact_cache.first_order_merge('ip', '999.8.7.6')
    assert fact_cache._plugin.get('ip') == '999.8.7.6'
    assert fact_cache['ip'] == '999.8.7.6'

# Generated at 2022-06-13 17:08:18.176842
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    my_cache = FactCache(C.CACHE_PLUGIN)
    # key is not in cache
    key = "my_key"
    first_value = {"first_key": "first_value"}
    my_cache.first_order_merge(key, first_value)
    assert my_cache[key] == first_value

    # key is in cache, new value will be merged with old value
    second_value = {"second_key": "second_value"}
    my_cache.first_order_merge(key, second_value)
    assert my_cache[key] == dict(first_value, **second_value)

# Generated at 2022-06-13 17:08:18.852267
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    factcache.flush()


# Generated at 2022-06-13 17:08:30.306793
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_facts = FactCache()
    test_facts.first_order_merge('192.168.100.100', {'ansible_kernel': 'Linux'})
    assert test_facts['192.168.100.100'] == {'ansible_kernel': 'Linux'}
    test_facts.first_order_merge('192.168.100.100', {'ansible_distribution_version': '6.7'})
    assert test_facts['192.168.100.100'] == {'ansible_kernel': 'Linux', 'ansible_distribution_version': '6.7'}
    test_facts.first_order_merge('192.168.100.120', {'ansible_kernel': 'Linux'})

# Generated at 2022-06-13 17:08:36.253908
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache._plugin = DummyPlugin()

    fact_cache.first_order_merge("target_host", {'foo':'bar'})
    
    # check that "target_host" is added in cache
    assert 'target_host' in fact_cache._plugin.cache.keys()

    # update host cache
    fact_cache.first_order_merge("target_host", {'foo':'bar2'})
    
    # check that the host cache is updated
    assert 'bar2' in fact_cache._plugin.cache.values()

# Dummy plugin for testing purpose

# Generated at 2022-06-13 17:08:45.332620
# Unit test for constructor of class FactCache
def test_FactCache():

    factcache = FactCache()
    factcache['host1'] = 'host1_facts'
    factcache['host2'] = 'host2_facts'

    assert factcache['host1'] == 'host1_facts'
    assert factcache['host2'] == 'host2_facts'
    assert len(factcache) == 2
    assert 'host1' in factcache
    assert 'host2' in factcache
    assert 'host3' not in factcache

    # try to delete the fact from cache
    del factcache['host1']
    assert len(factcache) == 1
    assert 'host1' not in factcache

    # update the fact for host2
    factcache['host2'] = 'host2_facts_updated'
    assert factcache['host2'] == 'host2_facts_updated'

    # first_

# Generated at 2022-06-13 17:08:45.920944
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:08:46.732197
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:08:52.819527
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert not fc._plugin.__dict__
    fc = FactCache(a=5)
    assert fc
    assert 'a' in fc.__dict__
    assert fc.__dict__['a'] == 5
    fc = FactCache(**{'a': 9})
    assert fc
    assert 'a' in fc.__dict__
    assert fc.__dict__['a'] == 9
    assert not fc._plugin.__dict__

# Generated at 2022-06-13 17:08:56.922972
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache_plugin = cache_loader.get(C.CACHE_PLUGIN)
    fact_cache = FactCache(plugin=fact_cache_plugin, key="host_name")
    assert fact_cache.keys() == []
    assert fact_cache.copy() == {}
    assert fact_cache.first_order_merge({"fact_name":"fact_value"})

# Generated at 2022-06-13 17:09:08.783284
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    host_cache = {'ansible_system': 'Ubuntu'}
    expected_result = {'192.168.0.1': {'ansible_system': 'RedHat'}}

    # Test when plugin returns fact cache
    fact_value = {'ansible_system': 'RedHat'}
    facts_cache._plugin.get = lambda key: value
    facts_cache.first_order_merge('192.168.0.1', fact_value)

    assert facts_cache == expected_result
    facts_cache.flush()

    # Test when plugin does not return fact cache
    facts_cache._plugin.get = lambda key: None
    facts_cache.first_order_merge('192.168.0.1', fact_value)

    assert facts_cache == expected_result


# Generated at 2022-06-13 17:09:10.237562
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:09:18.373830
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # TODO: Most effective way to test this method is to use
    #       mocks for includes and variable manager objects,
    #       but it is not so simple and fast to do, so here
    #       we have to test it with real objects.
    import tempfile
    from ansible.context import initialize_context
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultSecret

    context = initialize_context(None, vault_password=VaultSecret('password'))
    variable_manager = VariableManager()
    inventory = ':memory:'
    loader = context.loader
    cache_options = ImmutableDict(connection='memory')

# Generated at 2022-06-13 17:09:30.752790
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factCache = FactCache()
    value = {"key1": "value1"}

    factCache.first_order_merge("localhost", value)
    assert factCache["localhost"] == value

    value = {"key1": "value1", "key2": "value2"}
    factCache.first_order_merge("localhost", value)
    assert factCache["localhost"] == value

    factCache = FactCache()
    factCache.first_order_merge("localhost", value)
    factCache.first_order_merge("localhost", value)
    assert factCache["localhost"] == value

    factCache = FactCache()
    factCache.first_order_merge("localhost", value)
    assert factCache["localhost"] == value

    value = {"key2": "value1", "key1": "value2"}
    factCache

# Generated at 2022-06-13 17:09:34.167883
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    display.display("Type of object returned by constructor %s" % (type(fact_cache)))
    display.display("Value of object returned by constructor %s" % (fact_cache))

if __name__ == '__main__':
    # Unit test
    test_FactCache()

# Generated at 2022-06-13 17:09:41.112376
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import os
    from ansible.module_utils.facts import get_file_facts
    from ansible.module_utils.six import string_types

    cache = FactCache()
    facts = os.path.join(os.path.dirname(__file__), '../ansible/module_utils/facts/test_files/test_fact')
    test_file_facts = get_file_facts(facts)
    test_file_facts['ansible_fact'] = "ansible_test_fact"

    cache.first_order_merge("test_host", test_file_facts)
    assert cache["test_host"] == test_file_facts
    assert cache["test_host"]["ansible_fact"] == "ansible_test_fact"


# Generated at 2022-06-13 17:09:42.342582
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache

# Generated at 2022-06-13 17:09:53.118491
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import tempfile
    import ansible.plugins.cache.jsonfile
    def _assert(cache_factory, key, new_facts, expected_facts):
        cache_dir = tempfile.mkdtemp()
        cache = cache_factory(cache_dir)
        cache[key] = new_facts
        assert cache[key] == expected_facts

    new_facts = {"a": 1, "b": {"b1": 1, "b2": 2}}
    expected_facts = {"a": 1, "b": {"b1": 1, "b2": 2}}
    _assert(lambda cache_dir: FactCache(ansible.plugins.cache.jsonfile.CacheModule(cache_dir)), "host", new_facts, expected_facts)


# Generated at 2022-06-13 17:10:00.424304
# Unit test for constructor of class FactCache
def test_FactCache():

    fc = FactCache()
    assert isinstance(fc, FactCache)

    assert len(fc) == 0
    assert [k for k in fc] == []

    assert fc.get('xyz') == None
    assert fc.get('xyz', 7) == 7

    fc['xyz'] = 3
    assert fc['xyz'] == 3
    assert fc.get('xyz') == 3
    assert fc.get('xyz', 7) == 3

    assert len(fc) == 1
    assert [k for k in fc] == ['xyz']

    del fc['xyz']
    assert 'xyz' not in fc

    assert len(fc) == 0
    assert [k for k in fc] == []

    fc.flush()

# Generated at 2022-06-13 17:10:03.191268
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    fc = FactCache()
    assert fc._plugin == plugin

# Generated at 2022-06-13 17:10:06.854492
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.name() == 'memory'

    # test the default plugin
    assert isinstance(FactCache(C.CACHE_PLUGIN), FactCache)

    # test other plugins
    assert isinstance(FactCache('jsonfile'), FactCache)
    assert isinstance(FactCache('yaml'), FactCache)
    assert isinstance(FactCache('redis'), FactCache)

# Generated at 2022-06-13 17:10:12.228938
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_cache = FactCache()

    # Check that cache is empty
    assert len(test_cache) == 0

    # Insert an item
    test_cache.first_order_merge("host1", {"foo": "bar"})

    # Check that cache has one item
    assert len(test_cache) == 1

    # Check that the item has the right content
    assert test_cache["host1"] == {"foo": "bar"}


# Generated at 2022-06-13 17:10:14.672771
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()
    assert fact_cache._plugin
    assert fact_cache._plugin.__class__.__name__ == 'RedisCacheModule'

# Generated at 2022-06-13 17:10:26.095037
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_host = "test.host"
    test_fact = "test_fact"

    cache = FactCache()

    existing_facts = {
        "existing_fact": "existing_fact"
    }

    new_facts = {
        test_fact: "new_fact",
        "removed_fact": "removed_fact"
    }

    updated_facts = {
        "existing_fact": "existing_fact",
        test_fact: "new_fact"
    }

    cache.first_order_merge(test_host, existing_facts)
    assert cache[test_host] == existing_facts

    cache[test_host] = {}
    cache.first_order_merge(test_host, new_facts)
    assert cache[test_host] == new_facts

    # Test that the order

# Generated at 2022-06-13 17:10:27.253122
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache == {}

# Generated at 2022-06-13 17:10:30.228323
# Unit test for constructor of class FactCache
def test_FactCache():
    display.display('test_FactCache::test_FactCache:: begin')
    fact_cache = FactCache()
    assert fact_cache
    display.display('test_FactCache::test_FactCache:: end')


# Generated at 2022-06-13 17:10:33.226805
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()
    assert fact_cache._plugin

    # ensures that we don't raise in case of a missing cache plugin
    C.CACHE_PLUGIN = 'invalid-cache-plugin'
    try:
        FactCache()
    except Exception:
        assert False
    finally:
        C.CACHE_PLUGIN = 'fact_cache'

# Generated at 2022-06-13 17:10:33.843545
# Unit test for constructor of class FactCache
def test_FactCache():
    fac= FactCache()

# Generated at 2022-06-13 17:10:34.614176
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin is not None

# Generated at 2022-06-13 17:10:36.420372
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:45.561690
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = {}
    facts_1 = {'ansible_facts': {'key1': 'value'}}
    FactCache().first_order_merge('127.0.0.1', facts)
    assert facts == {'ansible_facts': {}}
    FactCache().first_order_merge('127.0.0.1', facts)
    assert facts == {'ansible_facts': {}}
    FactCache().first_order_merge('127.0.0.1', facts_1)
    assert facts == {'ansible_facts': {}}
    assert facts_1 == {'ansible_facts': {'key1': 'value'}}

# Generated at 2022-06-13 17:10:46.358780
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()

    assert(fact_cache._plugin is not None)



# Generated at 2022-06-13 17:10:47.481781
# Unit test for constructor of class FactCache
def test_FactCache():
    fn = FactCache()
    assert(fn)

# Generated at 2022-06-13 17:10:55.324853
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    print(fact)



# Generated at 2022-06-13 17:11:00.218636
# Unit test for constructor of class FactCache
def test_FactCache():

    import shutil
    import tempfile

    temp_dir = tempfile.mkdtemp()
    try:
        cache_test = FactCache()
        cache_test["test_key"] = "test_value"
        assert cache_test["test_key"] =="test_value"
    finally:
        shutil.rmtree(temp_dir)

# Generated at 2022-06-13 17:11:00.885193
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()

# Generated at 2022-06-13 17:11:03.552871
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)


# Generated at 2022-06-13 17:11:05.098676
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    assert(fc._plugin)


# Generated at 2022-06-13 17:11:08.568568
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert factcache._plugin.__class__.__name__ == 'CacheModule'
    assert factcache[1] == 'file'


# Generated at 2022-06-13 17:11:16.306870
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # setup
    fact_cache = FactCache()
    key = 'localhost'

    # test logic
    initial_facts = {'fact1': 'value1', 'fact2': 'value2'}
    fact_cache[key] = initial_facts
    # test fact1 from first_order_merge with value from initial_facts
    fact_cache.first_order_merge(key, {'fact1': 'value'})
    assert fact_cache[key]['fact1'] == 'value1'
    # test fact3 from first_order_merge with value from first_order_merge
    fact_cache.first_order_merge(key, {'fact3': 'value'})
    assert fact_cache[key]['fact3'] == 'value'

# Generated at 2022-06-13 17:11:26.455585
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache_loader.set_directory(C.DEFAULT_LOCAL_TMP)
    fact_cache = FactCache()

    # First Cache Update
    # fact_cache will be empty
    fact_cache.first_order_merge('host_id', {'ansible_all_ipv4_addresses': ['192.168.56.11', '10.0.2.15'], 'ansible_distribution': 'Ubuntu', 'ansible_system': 'Linux'})

    # Assert cache facts
    assert 'host_id' in fact_cache

# Generated at 2022-06-13 17:11:27.952521
# Unit test for constructor of class FactCache
def test_FactCache():
    import pytest

    with pytest.raises(AnsibleError):
        FactCache()

# Generated at 2022-06-13 17:11:29.137375
# Unit test for constructor of class FactCache
def test_FactCache():
    test_cache = FactCache()
    assert test_cache


# Generated at 2022-06-13 17:11:45.665295
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)
    assert cache.flush() is None
    assert cache.keys() == []
    assert cache.copy() == {}
    cache['key'] = 'value'
    assert cache['key'] == 'value'
    assert cache.copy() == {'key': 'value'}
    del cache['key']
    assert cache.copy() == {}
    assert cache.flush() is None
    assert cache.keys() == []
    assert cache.copy() == {}

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:11:51.833379
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # when not cached and cache is boolean
    test_key = 'test_key'
    test_value = 'test_value'
    fact_cache.first_order_merge(test_key, test_value)
    assert fact_cache[test_key] == test_value

    # when not cached and cache is dict
    test_value = {'test_key': 'test_value'}
    fact_cache.first_order_merge(test_key, test_value)
    assert fact_cache[test_key] == test_value

    # when cached and cache is boolean
    test_value = 'test_value'
    new_test_value = 'new_test_value'
    fact_cache.first_order_merge(test_key, test_value)

# Generated at 2022-06-13 17:11:56.922264
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    key = 'a_host'
    value = {'foo': 'bar'}
    fc.first_order_merge(key, value)
    assert fc['a_host'] == {'foo': 'bar'}
    fc.first_order_merge(key, {'baz': 'baz'})
    assert fc['a_host'] == {'foo': 'bar', 'baz': 'baz'}

# Generated at 2022-06-13 17:11:57.995521
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)

# Generated at 2022-06-13 17:12:02.311939
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache['host1'] = {'key1': 'value1'}
    factcache['host2'] = {'key2': 'value2'}
    factcache.first_order_merge('host2', {'key2': 'value2.1'})
    assert factcache['host2']['key2'] == 'value2.1'
    assert factcache['host1']['key1'] == 'value1'

# Generated at 2022-06-13 17:12:03.646124
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f._plugin is not None

# Generated at 2022-06-13 17:12:05.515796
# Unit test for constructor of class FactCache
def test_FactCache():
    assert not FactCache

# Generated at 2022-06-13 17:12:06.838153
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert isinstance(fc, FactCache)



# Generated at 2022-06-13 17:12:10.873202
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # arrange
    cache = FactCache()

    # act
    cache.first_order_merge('key', {'key': 'value'})
    result = cache['key']

    # assert
    assert len(result) == 1
    assert result['key'] == 'value'



# Generated at 2022-06-13 17:12:18.689246
# Unit test for constructor of class FactCache
def test_FactCache():

    # Test initialization with no plugin name
    try:
        cache = FactCache()
        assert False, "AnsibleError expected to be raised"
    except AnsibleError as e:
        assert "Unable to load the facts cache plugin" in str(e), "AnsibleError '%s' not raised" % e

    # Test initialization with invalid plugin name
    try:
        C.CACHE_PLUGIN = 'no_such_plugin'
        cache = FactCache()
        assert False, "AnsibleError expected to be raised"
    except AnsibleError as e:
        assert "Unable to load the facts cache plugin" in str(e), "AnsibleError '%s' not raised" % e

    # Test initialization with valid plugin name
    C.CACHE_PLUGIN = 'memory'
    cache = Fact

# Generated at 2022-06-13 17:12:46.066290
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert(factcache)

# Generated at 2022-06-13 17:12:54.931429
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache_plugin = cache_loader.get('memory')
    fact_cache = FactCache()
    fact_cache._plugin = fact_cache_plugin
    fact_cache.flush()
    host_1 = 'foo'
    facts_1 = {
        'fact_1': '1',
        'fact_2': '2',
        'fact_3': '3'
    }
    facts_2 = {
        'fact_1': '4',
        'fact_2': '5'
    }
    fact_cache.first_order_merge(host_1, facts_1)
    assert(fact_cache.get(host_1) == facts_1)
    fact_cache.first_order_merge(host_1, facts_2)

# Generated at 2022-06-13 17:12:58.249964
# Unit test for constructor of class FactCache
def test_FactCache():
    '''

    :return:
    '''
    fact_cache = FactCache()
    if fact_cache._plugin:
        assert True
    else:
        assert False

# Test for __getitem__ method of class FactCache

# Generated at 2022-06-13 17:12:59.386451
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)
    assert fact_cache._plugin is not None


# Generated at 2022-06-13 17:13:04.685569
# Unit test for constructor of class FactCache
def test_FactCache():

    plugin = cache_loader.get(C.CACHE_PLUGIN)
    if not plugin:
        raise AnsibleError('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))

    factcache = FactCache()
    assert isinstance(factcache, FactCache)


# Generated at 2022-06-13 17:13:12.215696
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    host_facts = {'hoge': 'fuga'}
    fc.first_order_merge('dummy_host', host_facts)
    assert fc.copy() == {'dummy_host': {'hoge': 'fuga'}}
    host_facts = {'foo': 'bar'}
    host_facts2 = {'foo': 'bar', 'hoge': 'fuga'}
    host_facts_result = {'dummy_host': {'foo': 'bar', 'hoge': 'fuga'}}
    fc.first_order_merge('dummy_host', host_facts)
    assert fc.copy() == host_facts_result
    host_facts = {'hoge': 'fugafuga'}
    assert fc.first_

# Generated at 2022-06-13 17:13:19.218328
# Unit test for constructor of class FactCache
def test_FactCache():
    if C.CACHE_PLUGIN == 'jsonfile':
        import os
        import shutil
        from ansible.module_utils.facts import cache as cache

        test_cache_path = '/var/tmp/ansible/facts'
        test_key = 'localhost'
        test_value = {'f1': 'v1', 'f2': 'v2'}
        test_fact_cache = cache.FactCache()

        if os.path.exists(test_cache_path):
            shutil.rmtree(test_cache_path)

        assert os.path.exists(test_cache_path) == False

        test_fact_cache[test_key] = test_value
        assert test_fact_cache[test_key] == test_value

        test_fact_cache.flush()

# Generated at 2022-06-13 17:13:20.525160
# Unit test for constructor of class FactCache
def test_FactCache():
    test_cache = FactCache()
    assert test_cache


# Generated at 2022-06-13 17:13:22.007568
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

    assert fc._plugin

# Generated at 2022-06-13 17:13:23.136713
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None

# Generated at 2022-06-13 17:14:19.383713
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin

# Generated at 2022-06-13 17:14:20.493609
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:14:25.270001
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('localhost', {'ansible_all_ipv4_addresses': ['10.0.0.1'], 'ansible_device_links': {'eth0': '1'}})
    assert fc['localhost'] == {'ansible_all_ipv4_addresses': ['10.0.0.1'], 'ansible_device_links': {'eth0': '1'}}

    fc.first_order_merge('localhost', {'ansible_all_ipv4_addresses': ['10.0.0.2'], 'ansible_device_links': {'eth1': '2'}})

# Generated at 2022-06-13 17:14:28.276290
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    test_data = {'test_key': 'test_value'}
    fact_cache.update(test_data)
    assert fact_cache.copy() == test_data
    fact_cache.flush()

# Generated at 2022-06-13 17:14:35.618010
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()

    # This is the value for which first order merge happens
    test_value = {
        'ansible_facts': {
            'hardware': {
                'not_to_merge': 'old value'
            }
        }
    }

    # This is the value which is in the cache.
    test_cache_value = {
        'ansible_facts': {
            'hardware': {
                'to_merge': 'old value'
            }
        }
    }

    # This is the value which is new
    test_merged_value = {
        'ansible_facts': {
            'hardware': {
                'new': 'new value'
            }
        }
    }

    # Set the host fact cache

# Generated at 2022-06-13 17:14:46.716558
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    # ensure that the fact cache has no data points
    assert len(fact_cache) == 0

    # ensure that we get a key error when attempting to retrieve a non-existant key
    try:
        fact_cache['this_key_is_not_in_the_cache']
        assert False
    except KeyError:
        # that's what we wanted
        assert True

    # ensure that the fact cache's first_order_merge method is functioning properly
    fact_cache.first_order_merge('this_key_is_in_the_cache', 'this_value_is_in_the_cache')

    # ensure that we can retrieve the key
    assert fact_cache['this_key_is_in_the_cache'] == 'this_value_is_in_the_cache'

   

# Generated at 2022-06-13 17:14:51.308480
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    hostname = 'www.example.org'
    key = {'file': 'ansible_facts', 'host': hostname}
    value = {'ansible_all_ipv4_addresses': ['192.168.22.21', '192.168.22.22', '192.168.22.23']}
    cache.first_order_merge(key, value)
    assert len(cache.keys()) == 1

    # check that the cache contains the key
    assert key in cache

    # check the value of the key in the cache
    assert value == cache[key]

    # update the value

# Generated at 2022-06-13 17:14:52.953683
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()


# Generated at 2022-06-13 17:14:55.402169
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    assert isinstance(fact_cache, MutableMapping)

# Generated at 2022-06-13 17:14:56.785860
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None


# Generated at 2022-06-13 17:16:52.563076
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:16:59.362346
# Unit test for constructor of class FactCache
def test_FactCache():

    fact_cache = FactCache()

    # Constructor should load the cache plugin and create a cache object
    assert fact_cache is not None

    # Check that set and get methods work as expected
    test_key = 'test_key'
    test_value = 'test_value'

    fact_cache[test_key] = test_value
    assert test_value == fact_cache[test_key]

    # Delete test_key from cache and verify that it has been deleted
    del fact_cache[test_key]
    assert test_key not in fact_cache

# Generated at 2022-06-13 17:17:05.099672
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()
    # Test case 1
    key = "localhost"
    value = {"kernel": "Linux"}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value

    # Test case 2
    value2 = {"kernel": "Linux2"}
    fact_cache.first_order_merge(key, value2)
    assert fact_cache[key] == value2

# Generated at 2022-06-13 17:17:05.865504
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert True

# Generated at 2022-06-13 17:17:12.717681
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # create a test set of facts
    host_facts = {'host_facts': {'fact1': 'val1'}}

    # should populate the fact cache
    fact_cache.first_order_merge('host1', host_facts['host_facts'])
    assert 'host_facts' in fact_cache
    assert host_facts == fact_cache['host_facts']

    # should update the host cache since it already exists
    host_facts = {'host_facts': {'fact2': 'val2'}}
    fact_cache.first_order_merge('host1', host_facts['host_facts'])
    assert {'fact1': 'val1', 'fact2': 'val2'} == fact_cache['host_facts']

# Generated at 2022-06-13 17:17:13.588769
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert ""

# Generated at 2022-06-13 17:17:14.815439
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()


# Generated at 2022-06-13 17:17:15.882010
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)

# Generated at 2022-06-13 17:17:16.893662
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    return fact_cache


# Generated at 2022-06-13 17:17:22.241997
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    test_dict = {'key1':'value1', 'key2':'value2'}
    fc.update(test_dict)
    assert (fc['key1']=='value1' and fc['key2']=='value2')
    assert (len(fc)==2)
