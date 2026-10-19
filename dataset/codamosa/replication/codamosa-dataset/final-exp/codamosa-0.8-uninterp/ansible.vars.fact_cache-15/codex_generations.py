

# Generated at 2022-06-13 17:07:32.958092
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:07:37.254019
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    assert cache.first_order_merge('test',{'test':'123'})

    cache_1 = cache.copy()
    assert cache_1.keys().__len__() != 0
    assert cache_1.keys()[0] == 'test'

# Generated at 2022-06-13 17:07:46.698806
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json
    my_cache = FactCache()
    # Test with an empty cache
    key = 'abcdefg'
    value = {'a': 1, 'b': 'foo', 'c': None}
    my_cache.first_order_merge(key, value)
    assert json.loads(my_cache._plugin.get(key)) == value

    # Test for update of existing cache
    value = {'a': 2, 'b': 'bar', 'd': None}
    my_cache.first_order_merge(key, value)
    assert json.loads(my_cache._plugin.get(key)) == dict(value, c=None, d=None)

    # Test for another key
    key = '12345'
    value = {'a': 1, 'b': 'foo', 'c': None}

# Generated at 2022-06-13 17:07:50.551882
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache(1)
    a = fc.keys()
    b = fc.first_order_merge('a','b')
    c = fc['a']

# Generated at 2022-06-13 17:07:54.424499
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc == {}
    fc['key1'] = 'value1'
    assert fc['key1'] == 'value1'
    fc['key1'] = 'value2'
    assert fc['key1'] == 'value2'
    del fc['key1']
    assert fc == {}

# Generated at 2022-06-13 17:08:00.250672
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    def _reset():
        # empty the cache before each test
        f = FactCache()
        f.flush()
        return f

    def _init_cache(hostvars={}):
        f = _reset()
        for hostv in hostvars:
            f.setdefault(hostv, {}).update(hostvars[hostv])
        assert len(f) == len(hostvars)
        return f

    # test host facts do not exist in cache
    f = _reset()
    host_facts = {'ansible_ssh_host': '192.168.1.1'}
    key = "test_host"
    f.first_order_merge(key, host_facts)
    assert len(f) == 1
    assert f[key] == host_facts

    # test cache miss
    f

# Generated at 2022-06-13 17:08:06.190851
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.utils.display import Display
    display = Display()
    fact_cache = FactCache()

    if not C.CACHE_PLUGIN:
        raise AnsibleError('Unable to load the facts cache plugin (%s).' % (C.CACHE_PLUGIN))

    display.display("CACHE_PLUGIN: %s" % C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:08:07.939421
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('test_key_1', {'test_key_2': 'test_value_2'})
    fact_cache.first_order_merge('test_key_1', {'test_key_2': 'test_value_2'})

# Generated at 2022-06-13 17:08:18.553264
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    foo = FactCache()
    foo['host'] = {}
    foo.first_order_merge('host', {'foo': 'bar'})
    assert len(foo['host']) == 1
    assert foo['host']['foo'] == 'bar'

    # this should update the value of existing key 'foo'
    foo.first_order_merge('host', {'foo': 'baz'})
    assert len(foo['host']) == 1
    assert foo['host']['foo'] == 'baz'

    # this should just add new key/value pair
    foo.first_order_merge('host', {'fuzz': 'buzz'})
    assert len(foo['host']) == 2
    assert foo['host']['fuzz'] == 'buzz'


# Generated at 2022-06-13 17:08:19.691978
# Unit test for constructor of class FactCache
def test_FactCache():
    factCache_test = FactCache()
    print(factCache_test)

# Generated at 2022-06-13 17:08:27.422767
# Unit test for constructor of class FactCache
def test_FactCache():
    from nose.tools import assert_true, assert_false, assert_equal

    fact_cache = FactCache()

    # Check that fact cache does not have any keys
    assert_false(fact_cache._plugin.contains("localhost"))

    # Check that fact cache does not have a key that does not exist
    assert_true("localhost" not in fact_cache)
    assert_false("localhost" in fact_cache)

    return fact_cache


# Generated at 2022-06-13 17:08:28.277318
# Unit test for constructor of class FactCache
def test_FactCache():

    assert isinstance(FactCache(), FactCache)



# Generated at 2022-06-13 17:08:30.187550
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache(caffeinism='The desire for more coffee')
    assert fact_cache.caffeinism == 'The desire for more coffee'

# Generated at 2022-06-13 17:08:31.187502
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:08:31.952657
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    v = c.keys()

# Generated at 2022-06-13 17:08:33.632804
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        fact_cache = FactCache()
    except Exception as e:
        assert False, str(e)



# Generated at 2022-06-13 17:08:37.546288
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    c = FactCache()
    new_value = {'new_key': 'new_value'}
    c.first_order_merge('hostname', new_value)
    assert c['hostname'] == new_value

    old_value = {'old_key': 'old_value'}
    c.first_order_merge('hostname', old_value)
    assert c['hostname'] == dict(new_value, **old_value)

# Generated at 2022-06-13 17:08:38.731960
# Unit test for constructor of class FactCache
def test_FactCache():
    test_fc = FactCache()
    assert(test_fc is not None)

# Generated at 2022-06-13 17:08:39.867075
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache)

# Generated at 2022-06-13 17:08:43.677485
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)
    # assert fact_cache.__class__.__name__ == 'FactCache'
    # assert fact_cache.__class__.__bases__ == (collections.MutableMapping,)


# Generated at 2022-06-13 17:08:46.552855
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin

# Generated at 2022-06-13 17:08:51.941162
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    import pytest
    import tempfile
    import shutil
    from ansible.module_utils.six import string_types

    # test the default cache plugin
    default_cache = FactCache()
    assert isinstance(default_cache, FactCache)

    # test the env cache plugin
    test_plugin = 'env'
    with pytest.raises(AnsibleError):
        FactCache('', test_plugin)

    # test the memory cache plugin
    test_plugin = 'memory'
    os.environ['ANSIBLE_CACHE_PLUGIN'] = test_plugin
    memory_cache = FactCache()
    assert isinstance(memory_cache, FactCache)

    # test the redis cache plugin
    test_plugin = 'redis'

# Generated at 2022-06-13 17:08:56.437729
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache_test_obj = FactCache()
    fact_cache_test_obj.first_order_merge('test_key', {'test_key': {'test_fact': 'test_value'}})

    assert type(fact_cache_test_obj) == FactCache
    assert fact_cache_test_obj['test_key']['test_fact'] == 'test_value'

# Generated at 2022-06-13 17:09:08.321720
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_plugin_name = 'redis'
    cache_plugin_name_bogus = 'redis_bogus'
    cache_plugin_options = {'foo': 'bar'}
    cache_plugin_options_list = [{'foo': 'bar'}]

    try:
        plugin = cache_loader.get(cache_plugin_name_bogus)
        # we should not get here, plugin should be None
        raise ValueError

    except AnsibleError as e:
        # we should get here, plugin should be None
        assert str(e) == "Unable to load the facts cache plugin (%s)." % (cache_plugin_name_bogus)


# Generated at 2022-06-13 17:09:09.686464
# Unit test for constructor of class FactCache
def test_FactCache():
    fake_plugin = 'fake_plugin'
    facts_cache = FactCache()
    assert facts_cache._plugin == fake_plugin


# Generated at 2022-06-13 17:09:12.077577
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)


# Generated at 2022-06-13 17:09:13.189742
# Unit test for constructor of class FactCache
def test_FactCache():
    my_cache = FactCache()
    assert my_cache


# Generated at 2022-06-13 17:09:19.629091
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    def _test(input_, output_):
        fc = FactCache()
        fc.first_order_merge('test', input_)
        assert fc.copy() == output_

    _test(
        input_={'a': 1, 'b': 2, 'c': 3},
        output_={'test': {'a': 1, 'b': 2, 'c': 3}})

    _test(
        input_={'a': 1, 'b': 2, 'c': 3},
        output_={'test': {'a': 1, 'b': 2, 'c': 3, 'd': 4}})


# Generated at 2022-06-13 17:09:21.009865
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin.__class__.__name__ == 'FactCacheData'

# Generated at 2022-06-13 17:09:23.989607
# Unit test for constructor of class FactCache
def test_FactCache():
    fac = FactCache()
    print('FactCache:\n', fac)
    print('fac.keys():\n', fac.keys())

#test_FactCache()

# Generated at 2022-06-13 17:09:29.748070
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:09:37.901420
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    import tempfile

# Generated at 2022-06-13 17:09:41.095787
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.facts.cache import FactCache
    from ansible.module_utils.facts.cache.base import BaseFactCacheModule
    from ansible.module_utils.facts.cache.memory import MemoryFactCacheModule
    fc = FactCache()
    assert isinstance(fc._plugin, BaseFactCacheModule)
    assert isinstance(fc._plugin, MemoryFactCacheModule)

# Generated at 2022-06-13 17:09:43.728357
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache != None)
    fact_cache._plugin.set("127.0.0.1", "test key")
    assert(fact_cache._plugin.get("127.0.0.1") == "test key")
    fact_cache._plugin.delete("127.0.0.1")
    assert(fact_cache._plugin.contains("127.0.0.1") == False)

# Generated at 2022-06-13 17:09:54.191365
# Unit test for constructor of class FactCache
def test_FactCache():
    assert C.CACHE_PLUGIN == 'jsonfile'
    # Note: using cache_loader.keys() is not reliable in testing when ansible.cfg uses
    # something other than jsonfile for CACHE_PLUGIN.
    # CACHE_PLUGIN was previously initialized to 'memory' in ansible.cfg, verify that
    # we can create a cachedir, set a config setting and use a valid cache plugin
    assert 'jsonfile' in cache_loader.keys()
    # We have a test in annex_init_dir.yml that checks for the presence of 'jsonfile' in
    # cache_loader.keys(), so we can't safely remove anything else here.
    # cache_loader.keys() will always contain 'memory'.
    cache_loader.remove('memory')
    # create cachedir and populate
    plugin = cache

# Generated at 2022-06-13 17:09:55.320582
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None


# Generated at 2022-06-13 17:09:55.837113
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:09:59.773842
# Unit test for constructor of class FactCache
def test_FactCache():
    my_fact_cache = FactCache()
    assert(isinstance(my_fact_cache, FactCache) is True)
    assert(isinstance(my_fact_cache, MutableMapping) is True)

# Generated at 2022-06-13 17:10:06.293225
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Using a subclass of 'MutableMapping' in this method, since
    'MutableMapping' does not have a constructor and it is the
    superclass of 'FactCache'
    :return:
    """

    class MyFactCache(MutableMapping):
        """
        MyFactCache is the sample class of the class FactCache.
        The constructor of MyFactCache has the same parameters
        as the constructor of FactCache.
        """
        def __init__(self, *args, **kwargs):
            """
            The constructor of MyFactCache
            :param args:
            :param kwargs:
            :return:
            """
            pass

    my_fact_cache = MyFactCache()

# Generated at 2022-06-13 17:10:10.439688
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = cache_loader.get(C.CACHE_PLUGIN)
    if not fact_cache:
        raise("FactCache constructor does not create the instance of fact_cache")
    else:
        print("FactCache constructor creates the instance of fact_cache")

test_FactCache()

# Generated at 2022-06-13 17:10:15.967539
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache


# Generated at 2022-06-13 17:10:18.473615
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache()
    except Exception as e:
        assert False, "Test failed because exception was raised:  %s" % str(e)



# Generated at 2022-06-13 17:10:20.425299
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin
    assert fact_cache._plugin.__class__.__name__ == 'FactCachePlugin'

# Generated at 2022-06-13 17:10:28.638786
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    # if a fact is present and cache is empty, it should return a keyError exception
    try:
        cache['test']
    except KeyError:
        pass
    else:
        raise KeyError
    # if a fact is not present and cache is empty, it should return a keyError exception
    try:
        cache['test'] = 'test'
    except KeyError:
        raise KeyError
    else:
        pass
    # if a fact is not present and cache is not empty, it should return a keyError exception
    try:
        cache['test_1']
    except KeyError:
        pass
    else:
        raise KeyError
    # if a fact is not present and cache is empty, it should return a keyError exception

# Generated at 2022-06-13 17:10:34.927189
# Unit test for constructor of class FactCache
def test_FactCache():

    # Test for constructor with kwargs as input
    fact_cache = FactCache(**{'test': 'ansible'})

    # Test _plugin initialization
    assert fact_cache._plugin == 'json_file'

    # Test __getitem__
    fact_cache['test'] = 'ansible'
    try:
        assert fact_cache['test'] == 'ansible'
    except KeyError:
        pass

    # Test __contains__
    assert 'test' in fact_cache

    # Test __iter__
    assert next(iter(fact_cache)) == 'test'

    # Test __len__
    assert len(fact_cache) == 1

    # Test __delitem__
    del fact_cache['test']
    assert len(fact_cache) == 0

    # Test flush()
    fact_cache.flush()

# Generated at 2022-06-13 17:10:40.592647
# Unit test for constructor of class FactCache
def test_FactCache():
    # Requires an initialized C.ANSIBLE_CACHE_PLUGIN_PREFIX
    assert C.ANSIBLE_CACHE_PLUGIN_PREFIX is not None

    # Requires that the `jsonfile` cache plugin is available
    assert cache_loader.find_plugin('jsonfile') is not None

# Generated at 2022-06-13 17:10:42.701015
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin is not None
    cache_dict = cache.copy()
    assert len(cache_dict) == 0

# Generated at 2022-06-13 17:10:48.196121
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # host_facts = {}
    host_cache = {}
    host_facts = {'domain': {'stdout': 'test_domain'}}
    host_cache = {'domain': {'stdout': 'test_domain1'}}
    host_cache.update(host_facts)
    #host_facts = dict(host_cache)
    host_facts['domain'] = host_cache

# Generated at 2022-06-13 17:10:48.810668
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache().__class__.__name__ == 'FactCache'


# Generated at 2022-06-13 17:10:59.997421
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.display('Warning: this is a testing function for the' +
                    ' function: test_FactCache_first_order_merge')

    cache = FactCache()

    # with this test we want to verify that the fact cache gets updated
    key = 'localhost'
    value = {'fact1': 'value1', 'fact2': 'value2'}
    cache.first_order_merge(key, value)
    host_facts = cache[key]
    assert host_facts == value

    # with this test we want to verify that the fact cache gets updated
    new_value = {'fact2': 'new_value2'}
    cache.first_order_merge(key, new_value)
    host_facts = cache[key]

# Generated at 2022-06-13 17:11:17.144925
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts = {"ansible_distribution_version": "7.3"}
    #Test for new cache
    cache = FactCache()
    cache.first_order_merge("test", facts)
    assert cache["test"] == facts

    #Test for update existing cache
    new_facts = {"ansible_distribution_version": "7.4", "ansible_hostname": "test_host"}
    cache.first_order_merge("test", new_facts)
    assert cache["test"] == {"ansible_distribution_version": "7.4", "ansible_hostname": "test_host"}

# Generated at 2022-06-13 17:11:27.312335
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    key1 = "key1"
    key2 = "key2"
    key3 = "key3"
    key4 = "key4"
    value1 = "value1"
    value2 = "value2"
    value3 = "value3"
    value4 = "value4"
    value5 = "value5"
    dict1 = {key1: value1, key2: value2}
    dict2 = {key3: value3, key4: value4}
    dict3 = {key1: value5, key2: value2, key3: value3, key4: value4}
    fact_cache[key1] = dict1
    fact_cache.first_order_merge(key2, dict2)

# Generated at 2022-06-13 17:11:28.400974
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)


# Generated at 2022-06-13 17:11:36.403383
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    random_facts = {}
    random_facts['version'] = 2
    random_facts['version_info'] = [2, 7, 9]
    random_facts['release'] = [{'distribution': 'Ubuntu', 'major': '16', 'minor': '04'}]

    factsCache = FactCache()
    factsCache.first_order_merge('localhost', random_facts)

    facts = {'version': 2, 'version_info': [2, 7, 9], 'release': [{'distribution': 'Ubuntu', 'major': '16', 'minor': '04'}]}

    assert facts == factsCache['localhost']

# Generated at 2022-06-13 17:11:37.659858
# Unit test for constructor of class FactCache
def test_FactCache():
    facts_cache = FactCache()
    assert 'localhost' in facts_cache


# Generated at 2022-06-13 17:11:39.340840
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_loader_test = cache_loader.get(C.CACHE_PLUGIN)
    cache_test = FactCache()

    assert cache_test._plugin == cache_loader_test

# Generated at 2022-06-13 17:11:47.561417
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    
    cache_dict = {}
    cache_dict["fact_cache"] = {"local": "value"}

    plugin_dict = {}
    
    fc = FactCache(cache_dict=cache_dict, cache_plugin="dict")

    fc._plugin.get = lambda key : plugin_dict.get(key, {})
    fc._plugin.set = lambda key , value : plugin_dict.update({key: value})
    
    key = "fact_cache"
    value = {"local": "value", "remote": "value"}

    fc.first_order_merge(key, value)

    assert plugin_dict["fact_cache"] == value
    assert cache_dict["fact_cache"] == value

# Generated at 2022-06-13 17:11:48.721601
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache != None

# Generated at 2022-06-13 17:11:53.366744
# Unit test for constructor of class FactCache
def test_FactCache():
    if C.CACHE_PLUGIN == 'memory':
        assert True
    else:
        display.display("~"*100)
        display.display("Note: this test requires a cache plugin of 'memory'")
        display.display("~"*100)
        assert False

# Generated at 2022-06-13 17:12:01.133407
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()
    # Fixture to test first_order_merge of class FactCache
    # key,value : Parameters of first_order_merge
    # expectation: Expected value of fact cache

# Generated at 2022-06-13 17:12:35.439255
# Unit test for method first_order_merge of class FactCache

# Generated at 2022-06-13 17:12:36.841320
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert(fc is not None)
    assert(fc._plugin is not None)

# Generated at 2022-06-13 17:12:40.634121
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    class MockFactCache(FactCache):
        def __init__(self):
            self._plugin = MockCache()

    class MockCache():
        def __init__(self):
            self.cache = {'foo': {'test1': 'test1', 'test2': 'test2'}}

        def get(self, key):
            return self.cache[key]

        def contains(self, key):
            return key in self.cache

        def set(self, key, val):
            self.cache[key] = val


# Generated at 2022-06-13 17:12:44.405387
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader

    def __init__(self, *args, **kwargs):
        self._plugin = cache_loader.get(C.CACHE_PLUGIN)

    plugin = __init__('json')
    assert plugin is not None

# Generated at 2022-06-13 17:12:45.901601
# Unit test for constructor of class FactCache
def test_FactCache():

    # class FactCache is an abstract class.
    # TODO: The unit test for this class is an open issue
    pass

# Generated at 2022-06-13 17:12:48.547148
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert hasattr(cache, '_plugin'), "cache missing cached_plugin attribute"
    assert cache._plugin is not None, "cached_plugin is None"

# Generated at 2022-06-13 17:12:49.692773
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert hasattr(facts, '_plugin')

# Generated at 2022-06-13 17:12:58.718980
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''test FactCache.first_order_merge() method'''
    fact_cache = FactCache()

    # test that the default value is merge
    new_dict = {'key1': True, 'key2': False}
    new_dict_merged = {'key1': True, 'key2': False, 'key3': 'content1'}
    fact_cache['key1'] = new_dict
    fact_cache.first_order_merge(key='key1', value={'key3': 'content1'})
    assert fact_cache['key1'] == new_dict_merged

    # test that a merged dict is replace if the value is not merge
    new_dict = {'key1': True, 'key2': False}
    fact_cache['key1'] = new_dict

# Generated at 2022-06-13 17:13:01.833806
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    FactCache constructor should create a cache plugin using the
    cache_loader to load the plugin specified in the configuration
    ansible.cfg.
    """
    cache = FactCache()
    assert isinstance(cache, FactCache)


if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:13:03.322305
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert (fc)
    assert (fc._plugin == cache_loader.get(C.CACHE_PLUGIN))

# Generated at 2022-06-13 17:14:03.688584
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import pytest
    f_c = FactCache()
    assert list(f_c.keys()) == [], "Keys of empty fact cache is not empty"

    f_c.first_order_merge("key1", {"key1":"value1"})
    assert list(f_c.keys()) == ["key1"], "New key1 was not added to the fact cache"

    f_c.first_order_merge("key1", {"key1":"value"})
    assert list(f_c.keys()) == ["key1"], "New key1 was not added to the fact cache, instead was added with new key1 "

    f_c.first_order_merge("key1", {"key1":"value", "key2":"value2"})

# Generated at 2022-06-13 17:14:08.663477
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('a', {'b': 'c'})

    assert cache['a'] == {'b': 'c'}

    cache.first_order_merge('a', {'b': 'd'})

    assert cache['a'] == {'b': 'c'} # because it is first order


if __name__ == '__main__':
    test_FactCache_first_order_merge()

# Generated at 2022-06-13 17:14:16.199962
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    from ansible.module_utils.common._collections_compat import MutableMapping

    path = os.path.dirname(os.path.abspath(__file__))
    cache_plugin_path = os.path.join(path, '../cache_plugins/yaml.py')

    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = '.'
    os.environ['ANSIBLE_CACHE_PLUGINS'] = cache_plugin_path
    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'yaml'

    fact_cache = FactCache()

    assert issubclass(fact_cache.__class__, MutableMapping)

# Generated at 2022-06-13 17:14:19.461377
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin is not None
    assert fact_cache._plugin.contains('test') is False
    fact_cache.__setitem__('test', 'test')
    assert fact_cache._plugin.contains('test') is True
    fact_cache.__delitem__('test')
    assert fact_cache._plugin.contains('test') is False
    assert 'test' not in fact_cache

# Generated at 2022-06-13 17:14:28.909194
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    FactCache.first_order_merge = first_order_merge
    test_cache = FactCache()

    key = "testing_key"
    key2 = "testing_key2"
    value = {"a": "A", "b": "B"}
    value2 = {"a": "A2", "b": "B2"}
    value3 = {"a": "A3", "b": "B3"}

    FactCache.first_order_merge(test_cache, key, value)
    assert test_cache[key] == value

    FactCache.first_order_merge(test_cache, key, value2)
    assert test_cache[key] == {"a": "A2", "b": "B2"}

    FactCache.first_order_merge(test_cache, key2, value)
   

# Generated at 2022-06-13 17:14:30.724019
# Unit test for constructor of class FactCache
def test_FactCache():
    ''' test the constructor of class FactCache '''
    facts = FactCache()
    assert facts == {}, "constructor of class FactCache may not work fine"

# Generated at 2022-06-13 17:14:33.793777
# Unit test for constructor of class FactCache
def test_FactCache():
    my_facts = FactCache()
    assert my_facts.keys() == []
    my_facts['localhost'] = {}
    assert my_facts.keys() == ['localhost'], my_facts.keys()
    my_facts.flush()
    assert my_facts.keys() == []

# Generated at 2022-06-13 17:14:34.725012
# Unit test for constructor of class FactCache
def test_FactCache():
    fcache = FactCache()
    assert fcache != None


# Generated at 2022-06-13 17:14:36.139098
# Unit test for constructor of class FactCache
def test_FactCache():
    display.verbosity = 3
    fc = FactCache()
    assert isinstance(fc, MutableMapping)

# Generated at 2022-06-13 17:14:39.398439
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin
    assert '_plugin' in dir(fc)



# Generated at 2022-06-13 17:16:45.427024
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    hostname = 'test_host'

    # Test for set fact into cache if its clear
    fact_cache.first_order_merge(hostname, {'fact': 'value1'})
    assert fact_cache.get(hostname) == {'fact': 'value1'}

    # Test for set fact into cache if it already exists
    fact_cache.first_order_merge(hostname, {'fact': 'value2'})
    assert fact_cache.get(hostname) == {'fact': 'value1'}

    # Test for update facts with new fact
    fact_cache.first_order_merge(hostname, {'new_fact': 'value1'})

# Generated at 2022-06-13 17:16:46.632965
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f

    assert isinstance(f, MutableMapping)

# Generated at 2022-06-13 17:16:53.706837
# Unit test for constructor of class FactCache
def test_FactCache():
    import re
    import time
    from ansible.utils.display import Display
    from ansible.utils.path import makedirs_safe
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import cache_loader

    # Create the files directory if it does not exist
    makedirs_safe(C.DEFAULT_LOCAL_TMP)

    display = Display()
    vars = combine_vars(loader=None, variables=None, include_role_vars=False)
    m = re.search('[a-zA-Z0-9\+\/]{10}', time.ctime() + time.ctime())
    token = m.group(0)
    fc = FactCache(loader=None, variables=vars, play=None)
    print(fc)

# Generated at 2022-06-13 17:17:03.786223
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ Unit test code for merging the cache with a set of facts.
    
    """
    # Create a mock cache to use
    mock_cache_store = {}
    mock_cache = FactCache()
    mock_cache._plugin.contains = lambda key: key in mock_cache_store
    mock_cache._plugin.get = lambda key: mock_cache_store[key]
    mock_cache._plugin.set = lambda key, value: mock_cache_store.setdefault(key, value)
    mock_cache._plugin.delete = lambda key: mock_cache_store.pop(key, None)
    mock_cache._plugin.keys = lambda: list(mock_cache_store.keys())
    mock_cache._plugin.flush = lambda: mock_cache_store.clear()

    # Test the first case where there are no cached facts


# Generated at 2022-06-13 17:17:04.320797
# Unit test for constructor of class FactCache
def test_FactCache():
    assert not bool(FactCache())

# Generated at 2022-06-13 17:17:05.657574
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:17:06.150039
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:17:08.536410
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test Case:
    1. test the constructor of class FactCache
    Expected Result:
    1. no exception raised
    """
    try:
        my_fact_cache = FactCache()
    except Exception as e:
        print(e)

# Generated at 2022-06-13 17:17:10.332759
# Unit test for constructor of class FactCache
def test_FactCache():
    # Call constructor as if Ansible would
    fact_cache = FactCache()
    assert type(fact_cache) == FactCache, "FactCache() should return an object of type FactCache"

# Generated at 2022-06-13 17:17:16.357387
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    host_facts = {"ansible_all_ipv4_addresses": ["192.168.100.100"],
                                                    "ansible_all_ipv6_addresses": ["fe80::5abc:91ff:fe07:8b80"]}

    cache.first_order_merge("example", host_facts)
    assert cache.keys() == {'example'}

    #Change IP of host facts
    host_facts_updated = {"ansible_all_ipv4_addresses": ["192.168.100.99"],
                                                    "ansible_all_ipv6_addresses": ["fe80::5abc:91ff:fe07:8b69"]}

    cache.first_order_merge("example", host_facts_updated)