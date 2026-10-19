

# Generated at 2022-06-13 17:07:37.945796
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    print (fc)

# Generated at 2022-06-13 17:07:43.007393
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    hostname = "testhost"
    value = {"test": "pass"}
    cache.first_order_merge(hostname, value)

    assert cache[hostname]["test"] == "pass"
    assert cache[hostname].get("hostname", None) is None
    assert cache.get("hostname", None) is None

# Generated at 2022-06-13 17:07:44.300314
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()._plugin

# Generated at 2022-06-13 17:07:45.765012
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:07:55.920157
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    assert cache.first_order_merge("test_host1", {"var1": 1, "var2": 2}) == {"test_host1": {"var1": 1, "var2": 2}}
    assert cache.first_order_merge("test_host1", {"var1": 2, "var3": 3}) == {"test_host1": {"var1": 2, "var2": 2, "var3": 3}}
    assert cache.first_order_merge("test_host2", {"var4": 4, "var5": 5}) == {"test_host2": {"var4": 4, "var5": 5}}

# Generated at 2022-06-13 17:08:07.092024
# Unit test for constructor of class FactCache
def test_FactCache():
    import yaml
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2, assertRegex
    from io import BytesIO
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import os
    import shutil
    import tempfile
    import warnings

    if PY2:
        from ansible.module_utils.six.moves import builtins
    else:
        import builtins

    def assertIsInstance(obj, cls):
        assert isinstance(obj, cls), "Expected %r" % (cls,)

    def assertIsNotNone(obj):
        assert obj is not None, "Unexpected None"



# Generated at 2022-06-13 17:08:11.425981
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None and type(fact_cache) is FactCache
    assert len(fact_cache) == 0
    fact_cache['example'] = 'hello'
    assert fact_cache['example'] == 'hello'
    fact_cache.flush()

# Generated at 2022-06-13 17:08:14.991554
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_obj = FactCache()
    test_obj.first_order_merge("test_key", "test_value")
    assert test_obj["test_key"] == "test_value"

# Generated at 2022-06-13 17:08:22.852755
# Unit test for method first_order_merge of class FactCache

# Generated at 2022-06-13 17:08:24.852143
# Unit test for constructor of class FactCache
def test_FactCache():
    d = FactCache()
    assert d.keys() == d._plugin.keys()

# Generated at 2022-06-13 17:08:34.520693
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes

    datastore = tempfile.NamedTemporaryFile(delete=False)
    datastore.close()
    os.unlink(datastore.name)

    config = {
        'CACHE_PLUGIN': 'jsonfile',
        'CACHE_PLUGIN_CONNECTION': datastore.name,
    }

    fc = FactCache(config)

    key = 'key1'
    value = {'var': 'var1'}
    fc[key] = value

    assert fc[key] == value
    assert key in fc

    assert len(fc) == 1

    fc.flush()

    assert len(fc) == 0


# Generated at 2022-06-13 17:08:40.617260
# Unit test for constructor of class FactCache
def test_FactCache():
    global display
    display = type('Display', (object,), {'warning': print})

    class CacheLoader(object):
        def get(self, name):
            global display

            if name == 'plugins':
                return CacheLoader()
            elif name == 'Fact_Cache':
                raise AnsibleError('Unable to load the facts cache plugin (Fact_Cache).')
            else:
                display.warning('Unable to load the facts cache plugin (%s).' % (name,))

    display.warning = print
    cache_loader.get = CacheLoader().get
    try:
        FactCache()
    except SystemExit:
        print('Success test of FactCache')
    else:
        print('Failed test of FactCache')

if __name__ == '__main__':
    test_FactCache()

# Generated at 2022-06-13 17:08:41.278855
# Unit test for constructor of class FactCache
def test_FactCache():
    x = FactCache()
    assert x != None

# Generated at 2022-06-13 17:08:49.648040
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    # Add first fact
    ipa_facts = dict()
    ipa_facts['ipa'] = dict()
    ipa_facts['ipa']['domain'] = 'example.com'
    ipa_facts['ipa']['server'] = 'ipa.example.com'
    fc.first_order_merge('ipa', ipa_facts['ipa'])
    assert 'ipa' in fc
    assert fc['ipa']['domain'] == 'example.com'
    assert fc['ipa']['server'] == 'ipa.example.com'
    # Add second fact
    ipa_facts['ipa']['trust_status'] = 'trusted'

# Generated at 2022-06-13 17:08:50.801363
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache=FactCache()

# Generated at 2022-06-13 17:08:51.376514
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()

# Generated at 2022-06-13 17:08:52.600832
# Unit test for constructor of class FactCache
def test_FactCache():

    factcache = FactCache()
    assert factcache is not None

# Generated at 2022-06-13 17:08:53.155357
# Unit test for constructor of class FactCache
def test_FactCache():
    c

# Generated at 2022-06-13 17:08:57.185626
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache import FactCache
    fact_cache = FactCache()
    assert ('default' == C.CACHE_PLUGIN)
    assert ('ansible.plugins.cache.dict' == C.DEFAULT_CACHE_PLUGIN)
    assert ('ansible.plugins.cache.dict' == C.CACHE_PLUGIN)


# Generated at 2022-06-13 17:09:08.818990
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    class CacheFake(object):
        def __init__(self):
            self.host_cache = {'a': 1}

        def get(self, key):
            return self.host_cache

    cf = CacheFake()

    fc = FactCache()
    fc._plugin = cf

    # This test is meant to make sure first_order_merge will call
    # MutableMapping.update and not MutableMapping.__setitem__.
    # The reason we want to do this is because Mapping.__setitem__
    # takes precedence over MutableMapping.update.
    # See https://docs.python.org/2/library/abc.html#abc.MutableMapping
    fc.first_order_merge('a', {'b': 2})
    assert 'b' in fc['a']

# Generated at 2022-06-13 17:09:12.895493
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert type(fact_cache).__name__ == 'FactCache'

# Generated at 2022-06-13 17:09:19.100759
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.plugins.cache import fact_cache

    key = "test"
    value = {"a": 1, "b": 2}

    tempdir = tempfile.TemporaryDirectory()

    # test merge with plugin that does nothing
    fact_cache.plugin_class = fact_cache.BaseFactCacheModule
    cache = fact_cache.FactCache()
    cache.first_order_merge(key, value)
    # reload plugin
    cache._plugin = None
    cache._plugin = fact_cache.get(C.CACHE_PLUGIN)
    assert cache[key] == value

    # test merge with plugin that sets the fact cache
    fact_cache.plugin_class = fact_cache.Jsonfile

# Generated at 2022-06-13 17:09:28.735236
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge('test', {'ansible_default_ipv4': {'address': '1.1.1.3', 'alias': 'eth0', 'gateway': '1.1.1.1', 'interface': 'eth0', 'macaddress': '02:03:00:04:00:05', 'mtu': 1490, 'netmask': '255.255.255.0', 'network': '1.1.1.0'}})

# Generated at 2022-06-13 17:09:29.244286
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    pass

# Generated at 2022-06-13 17:09:37.417745
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    def _merge_nested_dicts(base, other):
        for k, v in base.items():
            if k in other:
                if isinstance(v, dict):
                    _merge_nested_dicts(v, other[k])
                    if not set(v.keys()) - set(other[k].keys()):
                        other[k] = v
                        del v

    class _FactCache(FactCache):
        def __init__(self):
            self._plugin = {}
            self.initial_cache_size = 0

        def set(self, key, value):
            self._plugin[key] = value

        def get(self, key):
            try:
                return self._plugin[key]
            except KeyError:
                return None

        def flush(self):
            self._plugin = {}



# Generated at 2022-06-13 17:09:39.612408
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert facts
    assert isinstance(facts, FactCache)
    assert isinstance(facts, MutableMapping)
    assert len(facts) == 0
    assert facts._plugin.name == 'memory'


# Generated at 2022-06-13 17:09:41.228289
# Unit test for constructor of class FactCache
def test_FactCache():
    tests = [
        {'name': 'test1', 'param1': 1, 'param2': '2'}
    ]
    for test in tests:
        FactCache(test)

# Generated at 2022-06-13 17:09:43.296560
# Unit test for constructor of class FactCache
def test_FactCache():
    factCache = FactCache()
    factCache.keys()
    factCache.flush()
    factCache.copy()

# Generated at 2022-06-13 17:09:53.968864
# Unit test for constructor of class FactCache
def test_FactCache():
    # Initialize the class FactCache
    cache_data = FactCache()

    # Set the data
    cache_data[1] = 1
    cache_data[2] = 2

    # Check if the key exists
    assert 1 in cache_data
    assert 3 not in cache_data

    # Get the value for the key
    assert cache_data[1] == 1

    # Delete the key
    del cache_data[1]
    assert 1 not in cache_data

    # Check the length of the cache
    assert len(cache_data) == 1

    # Check if the iterator can be iterated
    for k in cache_data:
        assert True

    # Check if the cache can be converted to dictionary
    assert isinstance(cache_data.copy(), dict)

    # Check if the keys are fetched correctly
    assert cache_data

# Generated at 2022-06-13 17:09:57.658321
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Unit tests for first_order_merge of class FactCache

# Generated at 2022-06-13 17:10:08.111391
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    test_cache = FactCache()
    # Empty cache
    assert(len(test_cache) == 0)
    assert(test_cache.keys() == [])


    # Test merging into an empty cache
    test_cache.first_order_merge('127.0.0.1', { 'hello': 'world' })
    assert(len(test_cache) == 1)
    assert('127.0.0.1' in test_cache)
    assert(test_cache['127.0.0.1'] == { 'hello': 'world' })


    # Test merging into an existing cache
    test_cache.first_order_merge('127.0.0.1', { 'answer': 42 })
    assert(len(test_cache) == 1)

# Generated at 2022-06-13 17:10:16.866266
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()
    hostname = 'testhost.example.com'
    fact_cache[hostname] = {'foo': 'bar'}

    # Overwrite foo fact with baz fact
    fact_cache.first_order_merge(hostname, {'foo': 'baz'})
    assert fact_cache[hostname]['foo'] == 'baz'

    # Add new fact
    fact_cache.first_order_merge(hostname, {'ansible_facts': {'test': 'success'}})
    assert fact_cache[hostname]['ansible_facts']['test'] == 'success'

# Generated at 2022-06-13 17:10:25.583388
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    global FactCache
    class Plugin():
        def contains(self,key):return True
        def get(self,key):
            return {'fact1': 'old_value_fact1', 'fact2': 'old_value_fact2'}
        def set(self,key,value):pass
        def delete(self,key):pass
        def keys(self):return []
        def flush(self):pass
    FactCache = FactCache()
    FactCache._plugin = Plugin()
    FactCache.first_order_merge('192.168.1.1', {'fact1': 'new_value_fact1', 'fact3': 'new_value_fact3'})
    assert FactCache['192.168.1.1']['fact1'] == 'new_value_fact1'

# Generated at 2022-06-13 17:10:26.898972
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache._plugin, object)

# Generated at 2022-06-13 17:10:28.016707
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache,FactCache)

# Generated at 2022-06-13 17:10:28.903173
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:10:29.819118
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()


# Generated at 2022-06-13 17:10:30.818923
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert isinstance(cache, FactCache)

# Generated at 2022-06-13 17:10:36.240402
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # initialize the fact cache plugin
    fact_cache = cache_loader.get(C.CACHE_PLUGIN)
    if fact_cache:
        fact_cache.flush()

    # initialize the fact cache
    fact_cache = FactCache()
    assert len(fact_cache) == 0
    assert fact_cache.keys() == []

    # use the first_order_merge method to store a fact for the first time
    fact_key   = 'ansible_processor_cores'
    fact_value = 4
    fact_cache['ansible_processor_cores'] = fact_value
    fact_cache.first_order_merge('localhost', {'ansible_processor_cores': 8})
    assert fact_cache['localhost']['ansible_processor_cores'] == 8

# Generated at 2022-06-13 17:10:39.498231
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    display.v("Fact cache plugin is: %s" % fact_cache._plugin)
    assert fact_cache._plugin is not None, "Can not load fact cache plugin"

# Generated at 2022-06-13 17:10:48.354823
# Unit test for constructor of class FactCache
def test_FactCache():
    assert isinstance(FactCache(), FactCache)

# Generated at 2022-06-13 17:10:49.756119
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:10:50.808159
# Unit test for constructor of class FactCache
def test_FactCache():

    cache = FactCache()
    cache.set_plugin(cache_loader.get('jsonfile'))
    fact_cache = FactCache()
    assert fact_cache._plugin == cache._plugin

# Generated at 2022-06-13 17:10:55.087080
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge(key="localhost", value={"ansible_facts": {"dummy": True}})
    assert fact_cache["localhost"]["ansible_facts"]["dummy"] == True

test_FactCache_first_order_merge()

# Generated at 2022-06-13 17:10:59.804778
# Unit test for constructor of class FactCache
def test_FactCache():
    display = Display()
    cache_loader.set(cache_loader.CACHE_PLUGIN, 'jsonfile')
    assert isinstance(FactCache(), FactCache)
    cache_loader.flush()
    cache_loader.set(cache_loader.CACHE_PLUGIN, 'yaml')
    assert isinstance(FactCache(), FactCache)
    cache_loader.flush()

# Generated at 2022-06-13 17:11:00.440220
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:11:04.131167
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin == cache_loader.get(C.CACHE_PLUGIN)
    

# Generated at 2022-06-13 17:11:12.447574
# Unit test for constructor of class FactCache
def test_FactCache():
    # test with no error
    try:
        fc = FactCache()
    except Exception as err:
        assert False, 'unexpected error, %s' % str(err)

    # test with error
    old_value = C.CACHE_PLUGIN
    C.CACHE_PLUGIN = "FactCacheNoExist"
    try:
        fc = FactCache()
        assert False, 'expected error not raised'
    except AnsibleError as err:
        assert str(err) == 'Unable to load the facts cache plugin (FactCacheNoExist).'
    C.CACHE_PLUGIN = old_value

# Generated at 2022-06-13 17:11:16.936730
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fcache = FactCache()
    fcache.first_order_merge('test1', {'key': 'val'})
    assert fcache._plugin.get('test1') == {'key': 'val'}
    fcache.first_order_merge('test1', {'key': 'val2'})
    assert fcache._plugin.get('test1') == {'key': 'val2'}

# Generated at 2022-06-13 17:11:19.495304
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin


# Generated at 2022-06-13 17:11:28.093729
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

# Generated at 2022-06-13 17:11:33.149626
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.__class__.__name__ == 'FactCacheData'
    assert fact_cache._plugin.cache_key == 'ansible_facts'
    assert fact_cache._plugin._cache.__class__.__name__ == 'MemcachedCache'


# Generated at 2022-06-13 17:11:34.252122
# Unit test for constructor of class FactCache
def test_FactCache():
  fc = FactCache()
  assert fc._plugin != None

# Generated at 2022-06-13 17:11:35.859659
# Unit test for constructor of class FactCache
def test_FactCache():
    param = 'test_param'
    c = FactCache(param)
    assert c[param] == param

# Generated at 2022-06-13 17:11:37.955286
# Unit test for constructor of class FactCache
def test_FactCache():
    # test constructor
    obj = FactCache()

    # test file plugin, obj is not a file
    assert isinstance(obj._plugin, cache_loader.get(C.CACHE_PLUGIN)) is not False

# Generated at 2022-06-13 17:11:42.051124
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

    # Test Constructor
    if not isinstance(cache, FactCache):
        raise AssertionError('Cache is not an object of type FactCache')

# Generated at 2022-06-13 17:11:44.696119
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    persist_cache = FactCache()
    persist_cache.first_order_merge('test_host', {'test_fact': 'test_value'})
    assert persist_cache['test_host']['test_fact'] == 'test_value'

# Generated at 2022-06-13 17:11:50.586198
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """ Unit tests for method first_order_merge of class FactCache """
    fact_cache = FactCache()
    fact_cache.flush()
    fact_cache.first_order_merge('hostname.local', {'var1': 1, 'var2': 2})
    fact_cache.first_order_merge('hostname.local', {'var2': 3, 'var3': 3})

    assert fact_cache['hostname.local'] == {'var1': 1, 'var2': 3, 'var3': 3}

# Generated at 2022-06-13 17:11:55.883867
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Initialising empty variables for merging facts
    key = ['ansible_facts', 'ansible_local', 'ansible_play_hosts']
    value = {'ansible_facts': {}, 'ansible_local': {}, 'ansible_play_hosts': []}

    # Calling the first_order_merge method of the FactCache class
    FactCache.first_order_merge(key, value)

# Generated at 2022-06-13 17:12:03.402559
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import tempfile

    # pylint: disable=no-member

    # create an instance of the plugin
    cache_folder = tempfile.mkdtemp(prefix='ansible-fact-cache')

    plugin = cache_loader.get(C.DEFAULT_CACHE_PLUGIN)
    plugin_options = {
        'fact_caching': 'jsonfile',
        'fact_caching_connection': cache_folder,
        'fact_caching_timeout': 3600
    }

    plugin.set_options(plugin_options)

    cache = FactCache()

    first_dict = {'a': 0, 'b': 1}
    second_dict = {'a': 'A', 'b': 'B', 'c': 'C'}

    cache.first_order_merge('localhost', first_dict)
   

# Generated at 2022-06-13 17:12:34.535046
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge(
        'test_alpha.example.com',
        {'apples': 'red', 'bananas': 'yellow', 'oranges': 'orange'}
    )
    fact_cache.first_order_merge(
        'test_beta.example.com',
        {'bananas': 'green', 'pears': 'green'}
    )
    fact_cache.first_order_merge(
        'test_gamma.example.com',
        {'apples': 'green'}
    )
    fact_cache.first_order_merge(
        'test_delta.example.com',
        {'bananas': 'yellow', 'plums': 'purple', 'strawberries': 'red'}
    )

# Generated at 2022-06-13 17:12:35.438209
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc


# Generated at 2022-06-13 17:12:44.957043
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_facts = {'ansible_lsb': {
        'major_release': '14.04',
        'id': 'Ubuntu',
        'release': '14.04',
        'description': 'Ubuntu 14.04.1 LTS',
        'codename': 'trusty'}}

    cached_host_facts = {'ansible_lsb': {
        'major_release': '14.04',
        'id': 'Ubuntu',
        'distro': 'Ubuntu',
        'release': '14.04.5 LTS, Trusty Tahr',
        'description': 'Ubuntu 14.04.5 LTS',
        'codename': 'trusty'}}

    result = None
    fact_cache = FactCache()

    # test merge

# Generated at 2022-06-13 17:12:48.641053
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin.get('test') is None
    assert cache['test'] == {}
    assert cache.get('test') == {}
    assert len(cache) == 1
    cache.flush()
    assert cache._plugin.get('test') is None

# Generated at 2022-06-13 17:12:54.446248
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = "host_cache"
    value = {'some_fact': 'some_value'}

    cache.first_order_merge(key, value)
    assert cache[key] == value

    cache.first_order_merge(key, value)
    assert cache[key] == value

    more = {'some_other_fact': 'some_other_value'}
    cache.first_order_merge(key, more)
    value.update(more)
    assert cache[key] == value

# Generated at 2022-06-13 17:13:01.393688
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.loader import cache_loader
    from ansible.errors import AnsibleError
    from ansible.plugins.cache import mocked_cache_plugin
    cache_loader.set_all_plugins(mocked_cache_plugin)
    assert isinstance(FactCache(), MutableMapping)
    cache_loader.reset()
    assert isinstance(FactCache(), MutableMapping)
    cache_loader.set_all_plugins(None)
    try:
        FactCache()
    except AnsibleError as e:
        assert e.message == 'Unable to load the facts cache plugin (memory).'
    cache_loader.reset()

# Generated at 2022-06-13 17:13:10.059687
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """Test for update facts in fact cache in first order merge mode"""
    FACTS_CACHE = FactCache()

# Generated at 2022-06-13 17:13:11.433227
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

# Generated at 2022-06-13 17:13:12.215811
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f is not None

# Generated at 2022-06-13 17:13:19.217834
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    cache = FactCache()

    host_facts = {'test': {'a': 'a', 'b': 'b', 'c': 'c'}}

    cache['test'] = host_facts

    # verify that host_cache is the same as host_facts
    assert cache.keys()
    assert cache['test'] == host_facts['test']

    # merge {'test': {'c': 'c1'}} into cache
    new_facts = {'c': 'c1'}
    cache.first_order_merge('test', new_facts)

    # verify that the value of key 'c' of 'test' has been updated.
    assert cache['test'] == {'a': 'a', 'b': 'b', 'c': 'c1'}

    # merge {'test': {'d': 'd1'}}

# Generated at 2022-06-13 17:14:15.591287
# Unit test for constructor of class FactCache
def test_FactCache():
    assertion = FactCache()
    assert assertion


# Generated at 2022-06-13 17:14:16.029516
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()

# Generated at 2022-06-13 17:14:21.055301
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Set a key, value pair in the cache
    host_name = 'test_host'
    host_facts = {'test': 'value'}
    fact_cache[host_name] = host_facts

    # Append a value to the host_facts, so that it can be added to the cache by first_order_merge
    host_facts_append = {'test_2': 'value_2'}
    expected_host_facts = {'test': 'value', 'test_2': 'value_2'}

    fact_cache.first_order_merge(host_name, host_facts_append)

    assert fact_cache[host_name] == expected_host_facts

# Generated at 2022-06-13 17:14:22.935877
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert fc._plugin
    assert not fc._plugin.contains("192.168.5.5") 
    assert fc._plugin.contains("127.0.0.1")

# Generated at 2022-06-13 17:14:23.662805
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache is not None


# Generated at 2022-06-13 17:14:30.639027
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache['name'] = {'bri': 'is me'}
    factcache['name2'] = {'bri': 'is me'}
    factcache.first_order_merge('name', {'mich': 'is not me'})
    factcache.first_order_merge('name2', {'mich': 'is not me'})
    assert factcache['name'] == {'bri': 'is me', 'mich': 'is not me'}
    assert factcache['name2'] == {'bri': 'is me', 'mich': 'is not me'}

# Generated at 2022-06-13 17:14:31.733723
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert fc['test_key']

# Generated at 2022-06-13 17:14:36.491405
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = 'os_version'
    host1_facts = {key: 'twolower'}
    host2_facts = {key: 'OneUPPER'}

    cache.first_order_merge('host1', host1_facts)

    assert(key in cache.keys())
    assert(cache['host1'][key] == 'twolower')
    cache.first_order_merge('host1', host2_facts)
    assert(cache['host1'][key] == 'OneUPPER')

    assert(cache['host2'][key] == 'OneUPPER')

# Generated at 2022-06-13 17:14:37.222558
# Unit test for constructor of class FactCache
def test_FactCache():
    pass

# Generated at 2022-06-13 17:14:40.632249
# Unit test for constructor of class FactCache
def test_FactCache():
    ''' Testing constructor of class FactCache
    '''
    fact_cache = FactCache()

    assert fact_cache['localhost'] == {'localhost': {}}, "Failed to create fact_cache object."

# Generated at 2022-06-13 17:16:35.775243
# Unit test for constructor of class FactCache
def test_FactCache():

    cache = FactCache()

    for _ in cache:
        pass

# Generated at 2022-06-13 17:16:36.991866
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:16:39.314233
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache
    assert isinstance(cache, FactCache)

# Generated at 2022-06-13 17:16:42.557406
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    f = FactCache()
    f.first_order_merge('test_facts', {'facts': 'here'})
    assert f['test_facts'] == {'facts': 'here'}


# Generated at 2022-06-13 17:16:44.530435
# Unit test for constructor of class FactCache
def test_FactCache():

    # Pass object of class FactCache and assert for True
    assert isinstance(FactCache(), FactCache)


# Generated at 2022-06-13 17:16:45.408663
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    assert c is not None

# Generated at 2022-06-13 17:16:46.426828
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache


# Generated at 2022-06-13 17:16:50.218942
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible import constants as C
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import cache_loader
    cache = FactCache()
    assert isinstance(cache._plugin, cache_loader.get(C.CACHE_PLUGIN).__class__)
    assert cache._plugin.__class__.__name__ == 'FactCache'


# Generated at 2022-06-13 17:16:52.668232
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.config.manager import ConfigManager

    config_manager = ConfigManager()
    config_manager._config_data = {'CACHE_PLUGIN': 'jsonfile'}
    cache = FactCache()
    assert cache

# Generated at 2022-06-13 17:17:00.606538
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Case when key is not present in cache
    key = "localhost"
    value = {"key1": "val1", "key2": "val2"}
    fact_cache.first_order_merge(key, value)

    assert key in fact_cache
    assert fact_cache[key] == value

    # Case when key is not present in cache
    key = "localhost"
    value = {"key1": "val1", "key2": "val2"}
    fact_cache.first_order_merge(key, value)

    assert key in fact_cache
    assert fact_cache[key] == value