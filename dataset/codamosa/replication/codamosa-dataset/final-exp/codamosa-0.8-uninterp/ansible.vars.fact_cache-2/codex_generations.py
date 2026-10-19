

# Generated at 2022-06-13 17:07:37.482077
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    key = "system_architecture"
    value = "x86_64"
    cache.flush()
    assert cache.keys() == []
    cache.first_order_merge(key, value)
    assert cache.keys() == [key]
    assert cache[key] == value
    cache.flush()

# Generated at 2022-06-13 17:07:46.877083
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()

    key = 'first_order_merge_test'
    value = { 'foo' : 'bar'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value

    value = { 'test' : 'test'}
    fact_cache.first_order_merge(key, value)
    expected = { 'foo' : 'bar', 'test' : 'test'}
    assert fact_cache[key] == expected

    value = { 'foo' : 'test', 'bar' : 'foo'}
    fact_cache.first_order_merge(key, value)
    expected = { 'foo' : 'test', 'test' : 'test', 'bar' : 'foo'}

# Generated at 2022-06-13 17:07:51.535591
# Unit test for constructor of class FactCache
def test_FactCache():

    fc = FactCache()
    if fc._plugin is None:
        raise AssertionError

    fc = FactCache({'a': 1})
    if fc._plugin is None or fc != {'a': 1}:
        raise AssertionError

# Generated at 2022-06-13 17:07:53.462195
# Unit test for constructor of class FactCache
def test_FactCache():
    obj = FactCache()
    assert isinstance(obj, FactCache)
    assert isinstance(obj._plugin, object)


# Generated at 2022-06-13 17:07:59.745559
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    tmp_cache = FactCache()
    host_cache = {'ansible_local': {'a': 'b', 'c': 'd'}, 'ansible_facts': {'a': 'b', 'c': 'd'}, 'ansible_distribution': 'cisco'}
    cache_key = 'test'
    user_facts = {'ansible_local': {'a': 'b', 'c': 'd'}, 'ansible_facts': {'a': 'b', 'c': 'd'}, 'ansible_distribution': 'cisco'}

    # Test case where host_cache is none and user_facts is none
    tmp_cache._plugin.set(cache_key, host_cache)
    tmp_cache.first_order_merge(cache_key, None)

# Generated at 2022-06-13 17:08:02.374544
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert isinstance(fact_cache, MutableMapping)

# Generated at 2022-06-13 17:08:06.274041
# Unit test for constructor of class FactCache
def test_FactCache():

    from ansible.module_utils.common._collections_compat import Mapping

    # Create a fact cache instance
    cache = FactCache()

    # Check that parent class is MutableMapping
    assert isinstance(cache, MutableMapping)

    # Check that it is initialized empty
    assert len(cache) == 0

# Generated at 2022-06-13 17:08:12.327836
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_fact_cache = FactCache()

    assert not test_fact_cache.keys()

    test_fact_cache.first_order_merge('host1', {'fact1': 1, 'fact2': 2})
    assert test_fact_cache.keys() == ['host1']
    assert test_fact_cache['host1']['fact1'] == 1

    test_fact_cache.first_order_merge('host1', {'fact2': 3, 'fact3': 4})
    assert test_fact_cache.keys() == ['host1']
    assert test_fact_cache['host1']['fact1'] == 1
    assert test_fact_cache['host1']['fact2'] == 3
    assert test_fact_cache['host1']['fact3'] == 4

    test_fact_cache

# Generated at 2022-06-13 17:08:21.663589
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """
    Test first_order_merge function

    Check if facts are correctly merged.
    - when facts are in cache: update,
    - when facts are not already in cache: create facts
    """
    host_name = 'test_host'
    fact_name = 'fact'
    fact_content = {'key1': 'value1', 'key2': 'value2'}
    new_fact = {'key3': 'value3'}
    updated_fact = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    # test when facts are not in cache
    fact_cache = FactCache()
    assert (not fact_cache._plugin.contains(host_name))

# Generated at 2022-06-13 17:08:30.984078
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    from ansible.plugins.cache import memory

    facts_cache = FactCache({}, 'memory')
    facts_cache._plugin = memory.FactCacheModule()
    facts_cache.first_order_merge('host#1', {'fact1': 'value1', 'fact2': 'value2'})
    assert facts_cache['host#1']['fact1'] == 'value1'
    assert facts_cache['host#1']['fact2'] == 'value2'
    facts_cache.first_order_merge('host#1', {'fact2': 'value2_2'})
    assert facts_cache['host#1']['fact1'] == 'value1'
    assert facts_cache['host#1']['fact2'] == 'value2_2'

# Generated at 2022-06-13 17:08:34.077262
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache
    assert cache._plugin
    assert cache._plugin.__class__.__name__ == "FactCacheData"


# Generated at 2022-06-13 17:08:35.422871
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache
    assert cache._plugin
    assert cache._plugin.flush() is None

# Generated at 2022-06-13 17:08:38.140431
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin
    assert not fact_cache._plugin.contains('anything')

# Generated at 2022-06-13 17:08:46.537641
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """Unit-test for method first_order_merge of class FactCache"""
    facts_cache = FactCache()
    facts_cache.first_order_merge("test", {"key1": "value1"})
    assert facts_cache["test"] == {"key1": "value1"}
    facts_cache.first_order_merge("test", {"key2": "value2"})
    assert facts_cache["test"] == {"key1": "value1", "key2": "value2"}
    facts_cache.first_order_merge("test", {"key1": "another_value1", "key2": "another_value2"})
    assert facts_cache["test"] == {"key1": "another_value1", "key2": "another_value2"}

# Generated at 2022-06-13 17:08:47.912020
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc is not None
    assert '_plugin' in dir(fc)

# Generated at 2022-06-13 17:08:48.702679
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    return

# Generated at 2022-06-13 17:08:49.602140
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:08:53.152909
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.plugins import cache_loader

    try:
        cache = FactCache()
    except:
        assert False

    assert cache._plugin.__dict__ == cache_loader.get(C.CACHE_PLUGIN).__dict__

# Generated at 2022-06-13 17:08:58.735066
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    assert not fact_cache.keys()

    value = {'not_ansible_fact': 'somthing'}
    key = 'localhost'
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == value

    value = {'not_ansible_fact': 'something_else'}
    fact_cache.first_order_merge(key, value)
    assert fact_cache[key] == {'not_ansible_fact': 'something_else'}


# Generated at 2022-06-13 17:09:05.351406
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    factcache['test-key'] = 'test-value'
    assert factcache['test-key'] == 'test-value'
    assert 'test-key' in factcache
    assert len(factcache) == 1
    assert factcache.keys() == ['test-key']
    factcache.flush()

# Generated at 2022-06-13 17:09:08.113202
# Unit test for constructor of class FactCache
def test_FactCache():
#    FactCache()
    pass


# Generated at 2022-06-13 17:09:16.388564
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    test_hosts = ['test_host1', 'test_host2']
    test_facts = {
        'test_fact1': 'test_value1',
        'test_fact2': 'test_value2'
    }

    for test_host in test_hosts:
        fact_cache.first_order_merge(test_host, test_facts)

    # Check that all facts have been added in the cache
    for key, value in fact_cache.items():
        assert key in test_hosts
        for fact_name, fact_value in value.items():
            assert fact_name in test_facts
            assert fact_value == test_facts[fact_name]

    # Emulate the fact collecting process by updating the facts
    # in the cache with new values
    test_

# Generated at 2022-06-13 17:09:17.390808
# Unit test for constructor of class FactCache
def test_FactCache():
    from . import cache_loader
    cache_loader.get()


# Generated at 2022-06-13 17:09:22.186682
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    '''Unit test for method first_order_merge of class FactCache'''
    test_fact_cache = FactCache()
    test_fact_cache.first_order_merge('test_host_1',{'test_fact_1':'test_value_1','test_fact_2':'test_value_2','test_fact_3':'test_value_3'})
    assert test_fact_cache['test_host_1']['test_fact_1'] == 'test_value_1'
    assert test_fact_cache['test_host_1']['test_fact_2'] == 'test_value_2'
    assert test_fact_cache['test_host_1']['test_fact_3'] == 'test_value_3'
    test_fact_cache.first_order_mer

# Generated at 2022-06-13 17:09:23.788151
# Unit test for constructor of class FactCache
def test_FactCache():
    if not FactCache():
        raise Exception('fact_cache.py: Failed to instantiate FactCache()')

# Generated at 2022-06-13 17:09:25.139681
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()

    # Test if class is constructed correctly
    assert f is not None

# Generated at 2022-06-13 17:09:26.376637
# Unit test for constructor of class FactCache
def test_FactCache():
    factcache = FactCache()
    assert factcache._plugin

# Generated at 2022-06-13 17:09:27.608536
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin is not None

# Generated at 2022-06-13 17:09:35.862109
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.verbosity = 3

    def get(key):
        return None

    def set(key, value):
        return None

    def delete(key):
        return None

    def contains(key):
        return False

    def keys():
        return []

    def flush():
        return None

    # mocking cache plugin by defining new functions
    def setitem(key, value):
        return None

    def update(other):
        return None

    setattr(FactCache, "setitem", setitem)
    setattr(FactCache, "update", update)

    def setattr_get(self, attr):
        return getattr(self, attr)

    setattr(FactCache, "__getattr__", get)
    setattr(FactCache, "get", get)

# Generated at 2022-06-13 17:09:42.284093
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import get_file_vault_secret

    vault_secret_file = False
    vault_filename = None
    vault_secret = None
    vault_password = None
    vault_password_file = None

    display.vvvv("Vault password for ansible-vault operations:")
    vault_password = get_file_vault_secret(filename=vault_secret_file, vault_password=vault_password,
                                           ask_vault_pass=vault_secret_file is None and vault_password is None,
                                           vault_password_file=vault_password_file)

    vault = VaultLib(vault_password)

    fact_cache = FactCache()


# Generated at 2022-06-13 17:09:45.414623
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache._plugin

# Generated at 2022-06-13 17:09:48.039411
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin == cache_loader.get(C.CACHE_PLUGIN)

# Generated at 2022-06-13 17:09:57.165843
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    host_facts = {'interfaces': ['eth0', 'eth1']}
    fc.first_order_merge('localhost', host_facts)
    assert 'localhost' in fc

    host_facts = {'interfaces': ['eth2']}
    fc.first_order_merge('localhost', host_facts)
    assert fc['localhost']['interfaces'] == ['eth0', 'eth1', 'eth2']

    fc.first_order_merge('localhost', {})
    assert fc['localhost']['interfaces'] == ['eth0', 'eth1', 'eth2']

    assert 'localhost' in fc.keys()
    assert fc.copy()['localhost']['interfaces'] == ['eth0', 'eth1', 'eth2']
   

# Generated at 2022-06-13 17:09:58.877221
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:10:04.765752
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fc = FactCache()
    fc.first_order_merge('a_hostname', {'some_fact': 'some_value'})
    assert(fc['a_hostname'] == {'some_fact': 'some_value'})

    fc.first_order_merge('a_hostname', {'other_fact': 'other_value'})
    assert(fc['a_hostname'] == {'some_fact': 'some_value', 'other_fact': 'other_value'})


# Generated at 2022-06-13 17:10:06.385543
# Unit test for constructor of class FactCache
def test_FactCache():
    fcache = FactCache()
    assert(fcache._plugin)

# Generated at 2022-06-13 17:10:13.708546
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
  fact_cache = FactCache()
  fact_cache._plugin.set("test", {"ec2_instance_type": "m3.large", "architecture": "amd_64"})

  fact_cache.first_order_merge("test", {"ec2_instance_type": "m3.xlarge"})

  assert len(fact_cache) == 1
  assert fact_cache.get("test").get("ec2_instance_type") == "m3.xlarge"
  assert fact_cache.get("test").get("architecture") == "amd_64"

# Generated at 2022-06-13 17:10:15.387464
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    #assert isinstance(fact_cache, FactCache)

# Generated at 2022-06-13 17:10:17.217255
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:10:23.230183
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    host_facts = { 'fact1': 'value1', 'fact2': 'value2'}
    cache.first_order_merge( 'localhost', host_facts )
    cache.first_order_merge( 'localhost', { 'fact2': 'value2_' } )
    assert cache['localhost'] == { 'fact1': 'value1', 'fact2': 'value2_' }
    assert cache.copy() == { 'localhost': { 'fact1': 'value1', 'fact2': 'value2_' } }

# Generated at 2022-06-13 17:10:27.978928
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache

# Generated at 2022-06-13 17:10:33.956168
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.module_utils.facts.cache import FactCache
    from ansible.module_utils._text import to_bytes
    import os

    pref = u'\u20ac'
    bpref = to_bytes(pref, encoding=None)
    if not isinstance(pref, str):
        name = pref.encode('utf-8')
    else:
        name = pref

    facts = {'var1': 'hello'}

    os.environ['ANSIBLE_CACHE_PLUGIN'] = 'jsonfile'
    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = '/tmp'

    fact_cache = FactCache()
    fact_cache[name] = facts
    assert fact_cache[name] == facts

# Generated at 2022-06-13 17:10:36.464367
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:10:43.475487
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    host_name = "localhost"
    fc = FactCache()
    fc.first_order_merge(host_name, {'first': 1})
    fc.first_order_merge(host_name, {'second': 2})
    assert fc[host_name]['first'] == 1, "Facts cache doesn't work as expected"
    assert fc[host_name]['second'] == 2, "Facts cache doesn't work as expected"

# Generated at 2022-06-13 17:10:50.962769
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    """
    This is a unit test for the method first_order_merge of class FactCache.
    This test was introduced to fix a bug in Ansible.

    The first order merge is used to combine different facts gathered
    by Ansible with various plugins. It ensures that facts
    gathered later in the play win over facts gathered earlier.
    However, this is only true for non-container facts
    (e.g. dict, list, str, int) for scalar facts.
    Container facts (e.g. dict) are recursively updated.

    The bug was caused by the fact that 'list' was implemented as
    a container fact. Therefore, without knowing it, a later
    fact could override an earlier fact.
    """
    fc = FactCache()

    # The test data has a list fact 'foo' that is later
    # updated with a str

# Generated at 2022-06-13 17:11:01.007392
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()

    # test_host1 facts from fact_cache:
    facts1 = {'fact1': 'old_fact', 'fact2': 'old_fact'}
    fact_cache['test_host1'] = facts1

    # Test when new_facts for test_host1 contain fact3
    new_facts1 = {'fact1': 'new_fact', 'fact2': 'new_fact', 'fact3': 'new_fact'}
    fact_cache.first_order_merge('test_host1', new_facts1)

    # Test when new_facts for test_host2 has no fact3
    facts2 = {'fact1': 'old_fact', 'fact2': 'old_fact'}
    fact_cache['test_host2'] = facts2

# Generated at 2022-06-13 17:11:12.368800
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    factcache = FactCache()
    factcache.first_order_merge("localhost", {"a": 2})
    assert factcache["localhost"]["a"] == 2
    factcache.first_order_merge("localhost", {"b": 3})
    assert factcache["localhost"]["a"] == 2
    assert factcache["localhost"]["b"] == 3
    factcache.first_order_merge("localhost", {"c": 4})
    assert factcache["localhost"]["a"] == 2
    assert factcache["localhost"]["b"] == 3
    assert factcache["localhost"]["c"] == 4
    factcache.first_order_merge("localhost", {"b": 5})
    assert factcache["localhost"]["a"] == 2
    assert factcache["localhost"]["b"] == 5
    assert fact

# Generated at 2022-06-13 17:11:14.078707
# Unit test for constructor of class FactCache
def test_FactCache():

    result = None

    try:
        result = FactCache()
    except:
        result = None

    assert result is not None

# Generated at 2022-06-13 17:11:15.032041
# Unit test for constructor of class FactCache
def test_FactCache():
    plugin = FactCache();


# Generated at 2022-06-13 17:11:19.043288
# Unit test for constructor of class FactCache
def test_FactCache():
    import tempfile
    fd, fname = tempfile.mkstemp()
    FactCache(fname, 'yaml')
    os.close(fd)
    os.remove(fname)

# Generated at 2022-06-13 17:11:34.976739
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    host_facts = {'fact_cache': {'i1': 1, 'i2': 2}}
    keys = ['fact_cache']

    assert fact_cache != host_facts

    for key in keys:
        fact_cache.first_order_merge(key, host_facts[key])

    assert fact_cache == host_facts

# Generated at 2022-06-13 17:11:41.080723
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('localhost', {'fact_cache_value': 'value'})
    assert cache['localhost']['fact_cache_value'] == 'value'
    # Check for merge for key 'localhost'
    cache.first_order_merge('localhost', {'fact_cache_value2': 'value2'})
    assert cache['localhost']['fact_cache_value'] == 'value'
    assert cache['localhost']['fact_cache_value2'] == 'value2'
    # Check for merge for key 'dummy'
    cache.first_order_merge('dummy', {'fact_cache_value': 'value'})
    assert cache['dummy']['fact_cache_value'] == 'value'

# Generated at 2022-06-13 17:11:45.401438
# Unit test for constructor of class FactCache
def test_FactCache():

    # Test when cache plugin is not exist without error
    cache = FactCache()

    assert len(cache.copy()) == 0
    assert cache.keys() == []
    assert cache.flush() is None
    assert cache.first_order_merge("key", "value") is None
    assert len(cache.copy()) == 1
    cache.flush()
    assert len(cache.copy()) == 0

# Generated at 2022-06-13 17:11:46.580392
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    assert fact_cache is not None

# Generated at 2022-06-13 17:11:52.400127
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache.first_order_merge('127.0.0.1', {'some_fact': 'some_value'})
    cache.first_order_merge('127.0.0.1', {'some_fact': 'some_other_value'})
    assert cache['127.0.0.1']['some_fact'] == 'some_other_value'
    cache.flush()

# Generated at 2022-06-13 17:12:00.342308
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    instance = FactCache()
    # create a basic fact set
    fact_set = {'fact1': 'value1', 'fact2': 'value2'}
    # create an updated fact set
    fact_set_new = {'fact1': 'value1', 'fact2': 'value2', 'fact3': 'value3'}
    # test the first_order_merge method
    instance.first_order_merge('testhostname', fact_set)
    # assert that facts were merged
    with instance.get('testhostname') as facts:
        assert facts == fact_set
    # assert that previously merged facts are not overwritten
    instance.first_order_merge('testhostname', fact_set_new)
    with instance.get('testhostname') as facts:
        assert facts == fact_set_new

# Generated at 2022-06-13 17:12:02.503693
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()
    cache['1.1.1.1'] = {'a': 1}
    cache.first_order_merge('1.1.1.1', {'b': 2})
    assert cache['1.1.1.1'] == {'a': 1, 'b': 2}

# Generated at 2022-06-13 17:12:03.749058
# Unit test for constructor of class FactCache
def test_FactCache():
    fact = FactCache()
    assert fact
    fact.flush()

# Generated at 2022-06-13 17:12:04.709461
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert isinstance(f, MutableMapping)

# Generated at 2022-06-13 17:12:06.105796
# Unit test for constructor of class FactCache
def test_FactCache():
    p = FactCache()
    assert p

# Generated at 2022-06-13 17:12:32.577819
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    assert True

# Generated at 2022-06-13 17:12:41.047770
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    host_name = 'host1'
    fact_cache.first_order_merge(host_name, {'fact1': 'value1'})
    assert {'fact1': 'value1'} == fact_cache[host_name]

    fact_cache.first_order_merge(host_name, {'fact2': 'value2'})
    assert {'fact1': 'value1', 'fact2': 'value2'} == fact_cache[host_name]

    fact_cache.first_order_merge(host_name, {'fact2': 'new_value2'})
    assert {'fact1': 'value1', 'fact2': 'new_value2'} == fact_cache[host_name]

# Generated at 2022-06-13 17:12:50.392380
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    testcache = FactCache()
    testcache[u'host1'] = {u'fact1': u'val1', u'fact2': u'val2'}
    testcache[u'host2'] = {u'fact1': u'val1', u'fact2': u'val2'}
    testcache[u'host3'] = {u'fact1': u'val1', u'fact2': u'val2'}

    host4_facts = {u'fact1': u'val1', u'fact2': u'val2', u'fact3': u'val3'}
    testcache.first_order_merge(u'host4', host4_facts)
    assert testcache[u'host4'][u'fact3'] == u'val3'


# Generated at 2022-06-13 17:12:52.513169
# Unit test for constructor of class FactCache
def test_FactCache():
    import pytest
    display = Display()

    with pytest.raises(AnsibleError):
        factcache = FactCache()

# Generated at 2022-06-13 17:12:53.098373
# Unit test for constructor of class FactCache
def test_FactCache():
    f = FactCache()
    assert f is not None

# Generated at 2022-06-13 17:12:54.319348
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    if not isinstance(fact_cache, FactCache):
        raise AssertionError('Not an instance of FactCache')

# Generated at 2022-06-13 17:12:54.643552
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    pass

# Generated at 2022-06-13 17:12:55.309352
# Unit test for constructor of class FactCache
def test_FactCache():
    fc = FactCache()
    assert fc

# Generated at 2022-06-13 17:13:03.471946
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    cache = FactCache()

    data = {'ansible_test': {'test1': 'test1-value'}}
    cache.first_order_merge('ansible_test', data['ansible_test'])
    assert cache['ansible_test'] == data['ansible_test']

    cache = FactCache()

    data = {'ansible_test': {'test1': 'test1-value', 'test2': 'test2-value'}}
    cache['ansible_test'] = data['ansible_test']
    cache.first_order_merge('ansible_test', {'test2': 'test2-value-updated', 'test4': 'test4-value'})

# Generated at 2022-06-13 17:13:07.013704
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.utils.display import Display
    from ansible.plugins.cache import picklefile
    display = Display()
    cache = FactCache()
    cache_ = picklefile.Picklefile(display)
    assert cache._plugin == cache_

# Generated at 2022-06-13 17:14:02.981832
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()
    fact_cache.flush()
    host_facts = {'hostname': 'foobar'}
    fact_cache.first_order_merge('hostvars', host_facts)

if __name__ == "__main__":
    test_FactCache_first_order_merge()

# Generated at 2022-06-13 17:14:05.093175
# Unit test for constructor of class FactCache
def test_FactCache():
    fac = FactCache()
    print(fac)
    print("test case FactCache passed")

test_FactCache()

# Generated at 2022-06-13 17:14:08.795464
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    test_cache = FactCache()
    test_cache.first_order_merge('host1', {'foo': 'bar'})
    assert test_cache['host1']['foo'] == 'bar'
    test_cache.first_order_merge('host1', {'foo': 'bar2'})
    assert test_cache['host1']['foo'] == 'bar2'

# Generated at 2022-06-13 17:14:11.599067
# Unit test for constructor of class FactCache
def test_FactCache():
    from ansible.constants import CACHE_PLUGIN
    from ansible.plugins.loader import cache_loader

    # set cache plugin to memory, needed for test
    CACHE_PLUGIN = 'memory'
    cache_loader.get(CACHE_PLUGIN)
    FactCache()
    # cache_loader is now loaded with the memory plugin
    assert cache_loader.get(CACHE_PLUGIN)

# Unit tests for FactCache merge functionality

# Generated at 2022-06-13 17:14:14.923251
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fc = FactCache()
    fc.first_order_merge("my_key", "my_value")
    assert fc["my_key"] == "my_value"
    fc.first_order_merge("my_key", "my_new_value")
    assert fc["my_key"] == "my_new_value"

# Generated at 2022-06-13 17:14:18.537611
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    mock_facts = {'a': 123, 'b': 456}
    fact_cache = FactCache()
    assert not fact_cache
    fact_cache.first_order_merge('test_host_name', mock_facts)
    assert fact_cache


fact_cache = FactCache()

# Generated at 2022-06-13 17:14:19.000689
# Unit test for constructor of class FactCache
def test_FactCache():
    facts = FactCache()

# Generated at 2022-06-13 17:14:21.573491
# Unit test for constructor of class FactCache
def test_FactCache():
    ansible_cache = FactCache()
    assert ansible_cache._plugin == ('jsonfile', '', 'ansible.cache.jsonfile.CacheModule')



# Generated at 2022-06-13 17:14:22.508077
# Unit test for constructor of class FactCache
def test_FactCache():
    fcache = FactCache()
    assert fcache is not None


# Generated at 2022-06-13 17:14:26.628569
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    fact_cache = FactCache()

    # Test first call to first_order_merge
    key = '127.0.0.1'
    value = {'ansible_facts': {'foo': 'bar'}}
    fact_cache.first_order_merge(key, value)
    assert(len(fact_cache) == 1)

    # Test second call to first_order_merge
    key = '127.0.0.1'
    value = {'ansible_facts': {'bar': 'foo'}}
    fact_cache.first_order_merge(key, value)
    assert(len(fact_cache) == 1)
    assert(fact_cache[key]['ansible_facts']['foo'] == 'bar')

# Generated at 2022-06-13 17:16:19.557987
# Unit test for constructor of class FactCache
def test_FactCache():
    cache = FactCache()
    assert cache._plugin
    assert cache._plugin.__name__ == C.CACHE_PLUGIN
    assert isinstance(cache, MutableMapping)

# Generated at 2022-06-13 17:16:20.278208
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache_object = FactCache()


# Generated at 2022-06-13 17:16:21.031998
# Unit test for constructor of class FactCache
def test_FactCache():
    fat = FactCache()
    assert isinstance(fat, FactCache)

# Generated at 2022-06-13 17:16:24.854486
# Unit test for constructor of class FactCache
def test_FactCache():
    # Test the constructor
    fc = FactCache()

    # Save some facts
    fc['test_fact'] = 'test'

    # Test the keys
    assert fc.keys() == ['test_fact']
    # Test the length
    assert len(fc) == 1
    # Test the copy function
    assert fc.copy() == {'test_fact': 'test'}
    # Test the retrieval
    assert fc['test_fact'] == 'test'
    # Test the contains function
    assert 'test_fact' in fc
    # Test the flush function
    fc.flush()
    assert len(fc) == 0
    assert fc.keys() == []

# Generated at 2022-06-13 17:16:32.285382
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    display.verbosity = 3
    C.CACHE_PLUGIN = "memory"
    fact_cache = FactCache()
    fact_cache.flush()
    fact_cache.first_order_merge("key_1", {"fact_1": "value_1", "fact_2": "value_2"})
    assert fact_cache["key_1"] == {"fact_1": "value_1", "fact_2": "value_2"}
    fact_cache.first_order_merge("key_1", {"fact_3": "value_3"})
    assert fact_cache["key_1"] == {"fact_1": "value_1", "fact_2": "value_2", "fact_3": "value_3"}

# Generated at 2022-06-13 17:16:43.256593
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():

    fac = FactCache()

    def display():
        pass

    fac._plugin.get = lambda x: {'a': 1, 'b': 2}
    fac._plugin.set = lambda x, y: None

    from ansible.compat.tests import unittest
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import VariableManager
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.manager import combine_facts
    import ansible.vars.hostvars
    import ansible.vars.manager

    class MockDisplay:
        def display(self):
            pass
    ansible.vars.hostvars.display = MockDisplay()


# Generated at 2022-06-13 17:16:51.200935
# Unit test for constructor of class FactCache
def test_FactCache():
    """
    Test that the constructor for class FactCache does not fail when
    ansible.cfg contains valid cache plugin option and the plugin is installed
    """
    plugin_name = 'jsonfile'

    # reset the cache_plugin value so it can be imported - otherwise 
    # cache_loader.get() will fail
    C.CACHE_PLUGIN = plugin_name

    # import the jsonfile plugin so it is available to cache_loader.get()
    from ansible_collections.ansible.community.plugins.cache import jsonfile
    jsonfile.CACHE_PLUGIN = plugin_name

    # test that object creation does not fail
    fact_cache_obj = FactCache()

    # clean up - remove module from sys.modules so it doesn't cause subsequent
    # tests to fail
    import sys

# Generated at 2022-06-13 17:16:52.212384
# Unit test for constructor of class FactCache
def test_FactCache():
    fact_cache = FactCache()
    fact_cache.flush()

# Generated at 2022-06-13 17:16:52.702609
# Unit test for constructor of class FactCache
def test_FactCache():
    FactCache()

# Generated at 2022-06-13 17:17:02.917304
# Unit test for method first_order_merge of class FactCache
def test_FactCache_first_order_merge():
    try:
        import __builtin__ as builtins  # pylint: disable=redefined-builtin
    except ImportError:
        import builtins
    import mock

    mock_get = mock.patch.object(
        FactCache._plugin,
        'get',
        return_value={'secrets': 'kept'},
        )
    mock_set = mock.patch.object(
        FactCache._plugin,
        'set',
        return_value=None
        )
    with mock_get as plugin_get, mock_set as plugin_set:
        fact_cache = FactCache()
        fact_cache.first_order_merge(
            'test_host',
            {'ansible_facts': {'new_facts': 'set'}}
            )
        # Validation.