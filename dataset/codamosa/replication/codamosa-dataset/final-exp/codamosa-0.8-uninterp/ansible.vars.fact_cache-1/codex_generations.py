

# Generated at 2022-06-13 17:07:41.112239
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    This test requires that the 'redis' plugin is loaded for
    the cache_plugins directory.
    """
    cache = FactCache({})
    cache._plugin.flush()
    assert len(cache) == 0
    print("Loaded redis plugin through cache_plugins")

    # Test method 'set'
    cache['test_key'] = 'test_value'
    assert len(cache) == 1

    # Test method 'contains'
    assert 'test_key' in cache

    # Test method 'get'
    assert cache['test_key'] == 'test_value'

    # Test method 'delete'
    del cache['test_key']
    assert len(cache) == 0

    # Test method 'flush'
    cache['test_key1'] = 'test_value1'
    cache['test_key2']

# Generated at 2022-06-13 17:07:43.636309
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()
    assert isinstance(facts, MutableMapping)
    assert facts._plugin != None

# Generated at 2022-06-13 17:07:45.197636
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert(fact_cache != None)

# Generated at 2022-06-13 17:07:55.358923
# Unit test for constructor of class FactCache
def test_FactCache():
    display.verbosity = 3
    import sys
    import os
    sys.path.append(os.path.dirname(sys.path[0]))
    from ansible.plugins import cache_loader

    fact_cache = FactCache()
    fact_cache['localhost'] = 1
    assert fact_cache['localhost'] == 1
    fact_cache['localhost'] = 2
    assert fact_cache['localhost'] == 2
    del fact_cache['localhost']
    assert fact_cache.keys() == []
    fact_cache['localhost'] = 1
    fact_cache.flush()
    assert fact_cache.keys() == []
    fact_cache['localhost'] = 1
    assert fact_cache.copy() != {}
    fact_cache_sec = FactCache()
    fact_cache_sec['localhost'] = 2
    fact_cache.first

# Generated at 2022-06-13 17:08:06.353174
# Unit test for constructor of class FactCache
def test_FactCache():
    
    # Instantiate a FactCache object called fc
    fc = FactCache()

    fc['test_key'] = 'test_value'
    assert fc['test_key'] == 'test_value'

    fc['test_key'] = 'test_value_updated'
    assert fc['test_key'] == 'test_value_updated'
    assert len(fc) == 1
    assert 'test_key' in fc

    del fc['test_key']
    assert len(fc) == 0
    assert 'test_key' not in fc

    # Test the copy feature
    fc['test_key'] = 'test_value'
    assert len(fc.copy()) == 1
    assert fc.copy()['test_key'] == 'test_value'

    # Test the keys feature
   

# Generated at 2022-06-13 17:08:09.685394
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache_fact = FactCache()
    cache_fact.first_order_merge('host', {'a': 1, 'b': 2})
    assert isinstance(cache_fact['host'], dict)
    assert cache_fact['host']['a'] == 1
    assert cache_fact['host']['b'] == 2

# Generated at 2022-06-13 17:08:11.300237
# Unit test for constructor of class FactCache
def test_FactCache():
    test_facts = FactCache()
    assert len(test_facts) == 0


# Generated at 2022-06-13 17:08:20.705401
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = {u'a1': u'1.1', u'a2': u'2.1'}

    fact_cache.first_order_merge(u'localhost', host_facts)
    assert fact_cache['localhost'] == host_facts
    assert fact_cache.keys() == [u'localhost']

    host_facts = {u'a1': u'1.2', u'a3': u'3.1'}
    fact_cache.first_order_merge(u'localhost', host_facts)
    assert fact_cache['localhost'] == {u'a1': u'1.2', u'a2': u'2.1', u'a3': u'3.1'}

# Generated at 2022-06-13 17:08:30.946144
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge("example.com", { "ansible_facts": { "ansible_os_family": "RedHat", "ansible_lsbrelease": { "full": "7.6", "major": "7", "minor": "6", "id": "RedHatEnterpriseServer", "id_like": "rhel fedora", "version": "7.6", "codename": "Maipo", "release": "7.6" } } })

# Generated at 2022-06-13 17:08:37.935944
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    local_cache = {}
    assert len(local_cache) == 0
    k1 = "key1"
    v1 = {"attribute1": "value1"}
    fc = FactCache(local_cache)

    fc.first_order_merge(k1, v1)
    assert len(local_cache) == 1
    assert local_cache[k1] == v1
    fc.first_order_merge(k1, v1)
    assert len(local_cache) == 1
    assert local_cache[k1] == v1
    fc.first_order_merge(k1, {"attribute2": "value2"})
    assert len(local_cache) == 1
    assert local_cache[k1]["attribute1"] == "value1"

# Generated at 2022-06-13 17:08:41.575524
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()

    assert cache._plugin.get_cache_type() == C.CACHE_PLUGIN

# Generated at 2022-06-13 17:08:49.981202
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    # Create a fact cache object
    fact_cache = FactCache()

    # Usual case: new fact not in cache yet
    hostname="test1"
    key="ansible_eth0"
    value="enp3s0"
    fact_cache.first_order_merge(hostname, {key: value})

    # Verify entry has been stored in cache
    assert fact_cache[hostname][key] == value

    # Usual case: new fact already in cache
    hostname="test1"
    key="ansible_eth1"
    value="eno3"
    fact_cache.first_order_merge(hostname, {key: value})

    # Verify entry has been stored in cache
    assert fact_cache[hostname][key] == value

    # The key for the new fact matches a key in the host

# Generated at 2022-06-13 17:08:58.359563
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    hostvars = {
        'host1': {
            'ansible_kernel': 'Linux',
            'ansible_os_family': 'RedHat',
            'ansible_system': 'Linux'
        },
        'host2': {
            'ansible_kernel': 'Linux',
            'ansible_os_family': 'RedHat',
            'ansible_system': 'Linux'
        },
        'host3': {
            'ansible_kernel': 'Linux',
            'ansible_os_family': 'RedHat',
            'ansible_system': 'Linux'
        }
    }

    fc = FactCache()
    for hostname, value in hostvars.items():
        fc.first_order_merge(hostname, value)

    assert(hostvars == fc)

# Generated at 2022-06-13 17:09:09.630855
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.verbosity = 4

    # Test with None values
    fact_cache=FactCache()
    host_facts={'key': None}
    host_cache={'key': None}
    fact_cache.first_order_merge(host_facts,host_cache)
    assert(host_facts==host_cache)

    # Test with simple values
    fact_cache=FactCache()
    host_facts={'key': 'value'}
    host_cache={'key': 'value'}
    fact_cache.first_order_merge(host_facts,host_cache)
    assert(host_facts==host_cache)

    # Test with list values
    fact_cache=FactCache()
    host_facts={'key': ['value','value']}
    host_cache={'key': ['value','value']}

# Generated at 2022-06-13 17:09:16.790003
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    test_key = 'test_key1'
    test_value = {'test_key2': 'test_value2'}
    updated_value = {'test_key2': 'updated_value2'}
    fact_cache.first_order_merge(test_key, test_value)
    assert fact_cache[test_key]['test_key2'] == 'test_value2'

    fact_cache.first_order_merge(test_key, updated_value)
    assert fact_cache[test_key]['test_key2'] == 'updated_value2'

    fact_cache.flush()

# Generated at 2022-06-13 17:09:26.581046
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    host = 'localhost'
    key = 'ansible_os_family'
    value = 'Debian'
    factcache.first_order_merge(host, {key:value})
    assert factcache[host][key] == value
    # Modify key ansible_os_family
    newvalue = 'Ubuntu'
    factcache.first_order_merge(host, {key:newvalue})
    assert factcache[host][key] == newvalue
    # Add new key ansible_foo
    newkey = 'ansible_foo'
    newvalue = 'bar'
    factcache.first_order_merge(host, {newkey:newvalue})
    assert factcache[host][newkey] == newvalue
    # Flush keys

# Generated at 2022-06-13 17:09:30.453331
# Unit test for constructor of class FactCache
def test_FactCache():
    data = {'test_key1': 'test_value1', 'test_key2': 'test_value2'}
    fact_cache = FactCache(data)
    assert fact_cache._plugin.get('test_key1') == 'test_value1'
    assert fact_cache.get('test_key2') == 'test_value2'

# Generated at 2022-06-13 17:09:31.376248
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()

# Generated at 2022-06-13 17:09:33.509015
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Unit test if the mock object(set in cache_loader) was called when class FactCache constructor is called

# Generated at 2022-06-13 17:09:38.666859
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()
    test_data = {'testkey': 'testvalue'}
    fact_cache.first_order_merge('testhostname', test_data)
    assert fact_cache['testhostname'] == test_data
    test_data = {'testkey': 'testvalue2'}
    fact_cache.first_order_merge('testhostname', test_data)
    assert fact_cache['testhostname'] == {'testkey': 'testvalue2'}

# Generated at 2022-06-13 17:09:44.976241
# Unit test for constructor of class FactCache
def test_FactCache():
    assert C.CACHE_PLUGIN == 'jsonfile'
    C.CACHE_PLUGIN = 'memory'
    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:09:46.106359
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc._plugin is not None



# Generated at 2022-06-13 17:09:53.575469
# Unit test for constructor of class FactCache
def test_FactCache():
    display.verbosity = 3
    cache = FactCache()
    host_facts = {'localhost': {'ansible_facts': {'a': 1, 'b': 2}}}
    cache.update(host_facts)
    assert list(cache.keys()) == ['localhost']
    assert cache.get('localhost') == {'ansible_facts': {'a': 1, 'b': 2}}
    cache.flush()
    del cache['localhost']
    assert len(cache) == 0
    assert list(cache.keys()) == []

# Generated at 2022-06-13 17:10:00.785807
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    host_cache = {'test': {'t1': {'val1': '1', 'val2': '2'}, 't2': {'val3': '3', 'val4': '4'}}}
    facts_cache.update(host_cache)
    host_facts = {'test': {'t1': {'val1': '10', 'val2': '20'}, 't3': {'val5': '5', 'val6': '6'}}}
    expected_facts = {'test': {'t1': {'val1': '10', 'val2': '20'}, 't2': {'val3': '3', 'val4': '4'}, 't3': {'val5': '5', 'val6': '6'}}}


# Generated at 2022-06-13 17:10:07.293846
# Unit test for constructor of class FactCache
def test_FactCache():
    import os

    # initializa FactCache
    cacher = FactCache()

    # insert a fact
    cacher['pre-insertion-test'] = 'pre-insertion-test'
    assert cacher[u'pre-insertion-test'] == 'pre-insertion-test'

    # update a fact
    cacher['update-test'] = 'pre-insertion-test'
    assert cacher[u'update-test'] == 'pre-insertion-test'
    cacher['update-test'] = 'update-test'
    assert cacher[u'update-test'] == 'update-test'

    # delete a fact
    del cacher['del-test']
    cacher['del-test'] = 'del-test'
    assert cacher[u'del-test'] == 'del-test'

# Generated at 2022-06-13 17:10:07.790826
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:10:09.313371
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert (fact_cache is not None)


# Generated at 2022-06-13 17:10:11.088799
# Unit test for constructor of class FactCache
def test_FactCache():
    c = FactCache()
    c['1'] = 'foo'
    assert c['1'] == 'foo'

# Generated at 2022-06-13 17:10:14.050278
# Unit test for constructor of class FactCache
def test_FactCache():
    factCache = FactCache()
    factCache['foo'] = 'bar'
    assert factCache['foo'] == 'bar'
    assert factCache.keys() == ['foo']
    factCache.flush()

# Generated at 2022-06-13 17:10:17.808858
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache(1, 2, 3)
    except Exception as err:
        assert(err.__class__ == NotImplementedError)
    assert(True) # FIXME: More tests needed.

# Generated at 2022-06-13 17:10:30.461406
# Unit test for constructor of class FactCache
def test_FactCache():
    import tempfile
    import shutil
    import os

    # get temp directory
    temp_dir = tempfile.mkdtemp()

    # set config
    os.environ[C.DEFAULT_LOCAL_TMP] = temp_dir
    C.CACHE_PLUGIN = 'jsonfile'
    C.CACHE_PLUGIN_CONNECTION = ''
    C.CACHE_PLUGIN_PREFIX = ''

    fact_cache = FactCache()
    assert fact_cache

    # clean up temp directory
    shutil.rmtree(temp_dir)

# Generated at 2022-06-13 17:10:35.524470
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_cache = {'test_key': {'level1': {'level2': 'key'}}}
    facts = {'level1': {'level2': 'key'}}
    plugin = cache_loader.get(C.CACHE_PLUGIN)
    plugin.set('test_key', host_cache['test_key'])
    fact_cache = FactCache()
    fact_cache.first_order_merge('test_key', facts['level1'])
    for key in facts:
        for key1 in facts[key]:
            assert facts[key][key1] == fact_cache['test_key'][key][key1], "key values not equal"
    plugin.flush()

# Generated at 2022-06-13 17:10:46.232872
# Unit test for constructor of class FactCache
def test_FactCache():
    class TestPlugin:
        def __init__(self):
            self.data = {'test_host': {'test_fact': 'test_value'}}

        def contains(self, key):
            return key in self.data

        def get(self, key):
            return self.data[key]

        def set(self, key, value):
            self.data[key] = value

        def delete(self, key):
            del self.data[key]

        def flush(self):
            self.data = {}

        def keys(self):
            return self.data.keys()

    C.CACHE_PLUGIN = 'TestPlugin'
    fact_cache = FactCache()

    assert 'test_host' in fact_cache

# Generated at 2022-06-13 17:10:57.411418
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    hostvars = {
        'host': {
            'ansible_facts': {
                'foo': 'bar',
                'baz': 'qux',
                'hello': 'world'
            }
        }
    }
    # Testing for a missing key (None)
    fact_cache.first_order_merge('host', hostvars['host']['ansible_facts'])
    assert fact_cache == hostvars

    # Trying to add same key
    fact_cache.first_order_merge('host', hostvars['host']['ansible_facts'])
    assert fact_cache == hostvars

    # Trying to merge two facts
    hostvars['host']['ansible_facts'].update({'new_fact': 'new_value'})

# Generated at 2022-06-13 17:11:03.065155
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import json
    cache_json = open('facts_cache.json', 'r')

    cache_dict = json.load(cache_json)

    fact_cache = FactCache(cache_dict)
    new_facts = {'new facts': 'new_value'}
    fact_cache.first_order_merge('test.testdomain.com', new_facts)

    return fact_cache

# Generated at 2022-06-13 17:11:08.790751
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('localhost', {'a': 'b'})
    cache.first_order_merge('localhost', {'c': 'd'})
    assert cache.get('localhost').get('a') == 'b'
    assert cache.get('localhost').get('c') == 'd'

# Generated at 2022-06-13 17:11:11.003936
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_plugin = cache_loader.get(C.CACHE_PLUGIN)
    fact_cache = FactCache()
    assert cache_plugin == fact_cache._plugin

# Generated at 2022-06-13 17:11:17.111729
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache['test_host'] = {'rhel': 'rhel7'}
    fact_cache.first_order_merge('test_host', {'rhel': 'rhel6'})
    print(fact_cache['test_host']) # {'rhel': 'rhel7'}
    fact_cache.first_order_merge('test_host', {'rhel': None})
    print(fact_cache['test_host']) # {'rhel': None}
    fact_cache.flush()
    print(fact_cache['test_host']) # {'rhel': None}

# Generated at 2022-06-13 17:11:21.127368
# Unit test for constructor of class FactCache
def test_FactCache():
    try:
        FactCache()
    except AnsibleError as e:
        if "Unable to load the facts cache plugin" in e.message:
            pass
        else:
            return False
    return True

# Generated at 2022-06-13 17:11:22.930336
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache


# Generated at 2022-06-13 17:11:36.033382
# Unit test for constructor of class FactCache
def test_FactCache():
    cache_loader.set_fact_cache(None)

# Generated at 2022-06-13 17:11:40.189638
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    facts_cache = FactCache()
    host_cache = {"ansible_facts": {"fact1": "value1"}}
    facts_cache.first_order_merge("host1", host_cache)
    host_cache = {"ansible_facts": {"fact2": "value2"}}
    facts_cache.first_order_merge("host1", host_cache)
    assert facts_cache["host1"]["ansible_facts"] == {"fact1": "value1", "fact2": "value2"}

# Generated at 2022-06-13 17:11:42.010804
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f

# Generated at 2022-06-13 17:11:50.328829
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_name = "test_host_1"
    test_facts = {
        "some_fact": "some_value",
        "some_other_fact": "some_other_value",
        "some_nested_fact": {"some_key": "some_value"}
    }

    test_cache = FactCache()

    #Get empty cache
    cache_facts = test_cache.copy()
    assert len(cache_facts) == 0

    #Save first fact to cache
    test_cache.first_order_merge(test_name, test_facts)
    cache_facts = test_cache.copy()
    assert len(cache_facts) == 1
    assert cache_facts.get(test_name) == test_facts

    #Update fact with same value

# Generated at 2022-06-13 17:11:52.360528
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:11:57.369833
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.plugins.cache.memory import CacheModule as Memory
    import ansible.plugins.cache as cache_plugins

    # test for invalid cache plugin
    try:
        cache_plugins.get('not_a_valid_name')
    except AnsibleError as e:
        assert 'Unable to load the facts cache plugin' in str(e)

    # test for valid cache plugin
    plugin = cache_plugins.get('memory')
    assert isinstance(plugin, Memory) is True

# Generated at 2022-06-13 17:12:04.682670
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = {
        'ansible_kernel': 'Linux',
        'ansible_distribution': 'Ubuntu',
        'ansible_distribution_release': '16.04',
        'ansible_distribution_version': '16.04',
        'ansible_os_family': 'Debian',
    }
    old_facts = {
        'ansible_distribution': 'Ubuntu',
        'ansible_distribution_release': '16.04',
        'ansible_distribution_version': '14.04',
        'ansible_os_family': 'Debian',
    }
    fact_cache._plugin.set('hostname', old_facts)
    fact_cache.first_order_merge('hostname', host_facts)
    assert fact_

# Generated at 2022-06-13 17:12:05.640229
# Unit test for constructor of class FactCache
def test_FactCache():
    _ = FactCache()

# Generated at 2022-06-13 17:12:07.592007
# Unit test for constructor of class FactCache
def test_FactCache():
    """Test constructor of class FactCache
    """
    # Create instance of FactCache
    instantiated_object = FactCache()

    assert instantiated_object._plugin

# Generated at 2022-06-13 17:12:12.106302
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge("myhost", {"a": "b"})
    cache.first_order_merge("myhost", {"b": "c"})
    cache.first_order_merge("myhost", {"a": "b2"})
    assert(cache["myhost"] == {"a": "b2", "b": "c"})

# Generated at 2022-06-13 17:12:40.277287
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None
    assert isinstance(fact_cache, MutableMapping)


# Generated at 2022-06-13 17:12:49.768974
# Unit test for constructor of class FactCache
def test_FactCache():

    import tempfile

    fact_cache = FactCache()

    with tempfile.NamedTemporaryFile() as fact_cache_file:

        fact_cache.flush()
        fact_cache['localhost'] = {'foo': 'bar'}

        assert fact_cache.copy()['localhost']['foo'] == 'bar'

        assert fact_cache['localhost']['foo'] == 'bar'

        fact_cache.flush()
        assert fact_cache.copy() == {}

        # set a fact in the cache
        fact_cache['localhost'] = {'foo': 'bar'}
        # update a fact in the cache
        fact_cache['localhost'] = {'foo': 'baz'}

        # assert the fact from the cache is equal to the updated value
        assert fact_cache['localhost']['foo'] == 'baz'

# Generated at 2022-06-13 17:12:53.789788
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.__setitem__("host1", {"ansible_host": "host1"})
    cache.first_order_merge("host1", {"ansible_port": 22})
    assert(cache.__getitem__("host1") == {"ansible_host": "host1", "ansible_port": 22})

# Generated at 2022-06-13 17:12:54.265678
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()

# Generated at 2022-06-13 17:12:56.158279
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache(C.CACHE_PLUGIN)
    assert fact_cache._plugin.__class__.__name__ == "FactCache"

# Generated at 2022-06-13 17:13:04.106592
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.ledger import HostLedger
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    class OBJECT(object):
        pass

    class VARS(object):
        def __init__(self):
            self.loader = OBJECT()
            self.loader.load = lambda x: x

    pc = PlayContext()
    loader = DataLoader()
    new_play = Play().load(dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[dict(
            action=dict(
                module='setup',
                args=dict(),
            )
        )]
    ), loader=loader)
    pc.setup_cache()


# Generated at 2022-06-13 17:13:04.989228
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache() is not None

# Generated at 2022-06-13 17:13:12.426625
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.vars.facts import FactCache
    from ansible.vars.facts import FactManager
    from ansible.vars.facts import default_fact_cache
    from ansible.plugins.loader import cache_loader
    from ansible.utils.display import Display
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.errors import AnsibleError
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.role_include import RoleInclude
    from ansible.inventory.host import Host

    default_

# Generated at 2022-06-13 17:13:19.362674
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()

    assert fact_cache.keys() == []
    fact_cache.flush()
    fact_cache["key1"] = "value1"

    assert fact_cache.keys() == ["key1"]
    assert fact_cache["key1"] == "value1"

    fact_cache["key1"] = "updated value1"
    assert fact_cache["key1"] == "updated value1"

    assert fact_cache.keys() == ["key1"]
    fact_cache.flush()
    fact_cache["key2"] = "value2"

    assert fact_cache.keys() == ["key2"]
    assert fact_cache["key2"] == "value2"

    del fact_cache["key2"]
    assert fact_cache.keys() == []


# Generated at 2022-06-13 17:13:26.616487
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache.first_order_merge('localhost', {'a': 1, 'b': {'c': 2}})

    assert factcache['localhost']['a'] == 1
    assert factcache['localhost']['b']['c'] == 2

    factcache.first_order_merge('localhost', {'b': {'d': 3}})

    assert factcache['localhost']['b']['d'] == 3

    factcache.first_order_merge('localhost', {'b': None})

    assert 'b' not in factcache['localhost']

# Generated at 2022-06-13 17:14:22.247512
# Unit test for constructor of class FactCache
def test_FactCache():
    assert FactCache()._plugin is not None


# Generated at 2022-06-13 17:14:23.552808
# Unit test for constructor of class FactCache
def test_FactCache():

    from ansible.plugins.cache import BaseCacheModule

    assert issubclass(FactCache, BaseCacheModule)
    assert issubclass(FactCache, MutableMapping)

# Generated at 2022-06-13 17:14:32.099415
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    import time
    import pickle
    from ansible.plugins.cache import filesystem
    from ansible.utils.path import makedirs_safe

    cache_dir = '/tmp/ansible_fact_cache.test'

# Generated at 2022-06-13 17:14:32.878542
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact == FactCache()

# Generated at 2022-06-13 17:14:33.446819
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()


# Generated at 2022-06-13 17:14:34.196411
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin.name == 'memory'

# Generated at 2022-06-13 17:14:38.605182
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc
    assert hasattr(fc, '_plugin')
    assert fc._plugin

    fc = FactCache({'key': 'value'})
    assert fc
    assert hasattr(fc, '_plugin')
    assert fc._plugin

    fc = FactCache([('key', 'value')])
    assert fc
    assert hasattr(fc, '_plugin')
    assert fc._plugin

    fc = FactCache(iter([('key', 'value')]))
    assert fc
    assert hasattr(fc, '_plugin')
    assert fc._plugin

    fc = FactCache(iter({'key': 'value'}))
    assert fc
    assert hasattr(fc, '_plugin')
    assert fc._plugin

    fc = Fact

# Generated at 2022-06-13 17:14:40.083007
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None

# Generated at 2022-06-13 17:14:49.316697
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    d = FactCache() # The method __init__() of FactCache will be executed

    # Case 1
    key = "192.168.124.10"
    value = {'local_fqdn': 'MASTER-734.localdomain', 'local_group': 'master', 'local_zone': 'master'}
    d.first_order_merge(key, value)
    print(d.copy())
    print("")

    # Case 2
    key = "192.168.124.10"
    value = {'local_fqdn': 'MASTER-734.localdomain', 'local_group': 'master'}
    d.first_order_merge(key, value)
    print(d.copy())
    print("")

    # Case 3

# Generated at 2022-06-13 17:14:55.945563
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fact_cache = FactCache()

    host_cache = {
        'ansible_facts': {
            'ansible_devices': {
                'sda': {
                    'holders': [],
                    'partitions': {
                        'sda1': {
                            'mount': '/boot'
                        },
                        'sda2': {
                            'mount': '/'
                        }
                    }
                }
            }
        }
    }

    test_key = '127.0.0.1'

    fact_cache.first_order_merge(test_key, host_cache)

    assert fact_cache[test_key]['ansible_facts']['ansible_devices']['sda']['partitions']['sda2']['mount'] == '/'

# Generated at 2022-06-13 17:16:00.710470
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache['hostname'] = {'ansible_architecture': 'x86_64'}
    fact_cache.first_order_merge('hostname', {'ansible_distribution': 'CentOS', 'ansible_distribution_major_version': '7', 'ansible_distribution_version': '7.4.1708', 'ansible_os_family': 'RedHat'})
    assert fact_cache['hostname']['ansible_os_family'] == 'RedHat'

# Generated at 2022-06-13 17:16:02.325754
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert(factcache)

# Generated at 2022-06-13 17:16:07.876220
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    host_facts_1 = {"a": 1, "b": 2}
    result = {"a": 1, "b": 2}
    assert fact_cache.first_order_merge("host1", host_facts_1) == result

    host_facts_2 = {"a": 0, "c": 3}
    result = {"a": 0, "b": 2, "c": 3}
    assert fact_cache.first_order_merge("host1", host_facts_2) == result

# Generated at 2022-06-13 17:16:09.012370
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test: create an instance of class FactCache
    fact_cache = FactCache()
    assert fact_cache != None

# Generated at 2022-06-13 17:16:13.249890
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host='localhost'
    fact_cache = FactCache()
    fact_cache.first_order_merge(host, {'test1': 'ansible'})
    assert fact_cache[host]['test1'] == 'ansible'

# Generated at 2022-06-13 17:16:21.139000
# Unit test for constructor of class FactCache
def test_FactCache():
    import os
    # The constructor should raise AnsibleError if can not load the facts_cache_plugin
    try:
        c = FactCache(C.CACHE_PLUGIN)
        assert False # should not reach here
    except AnsibleError as e:
        assert "Unable to load the facts cache plugin (jsonfile)" in str(e) # the value of C.CACHE_PLUGIN

    cache_dir = os.path.join(os.path.dirname(__file__), "test_cache_dir")
    c = FactCache(cache_dir)

    # Add some items
    c.__setitem__('a', {'a': 1})
    c.__setitem__('b', {'b': 2})
    assert c.__getitem__('a') == {'a': 1}

# Generated at 2022-06-13 17:16:22.064409
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc.flush() == None

# Generated at 2022-06-13 17:16:30.286225
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    test_key = "ansible_local"
    test_value = {"first_value": "first"}
    cache.first_order_merge(test_key, test_value)
    assert cache[test_key] == test_value

    test_value = {"second_value": "second"}
    cache.first_order_merge(test_key, test_value)

    # ensure first_order_merge() merges values and doesn't replace them
    assert cache[test_key]["first_value"] == "first"
    assert cache[test_key]["second_value"] == "second"

# Generated at 2022-06-13 17:16:35.109364
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    # GIVEN
    key1 = 'my_key1'
    key2 = 'my_key2'
    value1 = {
        'fact1': 'value1',
        'fact2': 'value2',
    }
    value2 = {
        'fact1': 'value3',
        'fact3': 'value4',
    }

    # WHEN
    fact_cache = FactCache()
    fact_cache[key1] = value1
    fact_cache.first_order_merge(key2, value2)

    # THEN
    assert len(fact_cache) == 2
    assert key1 in fact_cache
    assert key2 in fact_cache

    assert len(fact_cache[key1]) == 2
    assert fact_cache[key1]['fact1'] == 'value1'
    assert fact

# Generated at 2022-06-13 17:16:42.503268
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.first_order_merge('key1', 'value1')
    fact_cache.first_order_merge('key2', 'value2')

    assert fact_cache['key1'] == 'value1'
    assert fact_cache['key2'] == 'value2'

    fact_cache.first_order_merge('key1', 'value3')
    assert fact_cache['key1'] == 'value3'