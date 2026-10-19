

# Generated at 2022-06-13 11:29:20.516721
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache=CacheModule({
        '_uri': '/tmp',
        '_prefix': 'test',
        '_timeout': 5
    })

    assert cache._timeout == 5
    assert cache._prefix == 'test'
    assert cache._connection == '/tmp'
    assert cache._cache == {}



# Generated at 2022-06-13 11:29:22.621769
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars={})
    assert cache is not None


# Generated at 2022-06-13 11:29:24.808867
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None


# Generated at 2022-06-13 11:29:40.473324
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_data = [{"_ansible_parsed": True, "ansible_facts": {"fact1": "value1"}}]
    # Test creation of object of class CacheModule
    test_object = CacheModule(timeout=10)

    data_path = '/tmp/ansible_test'
    file_name = 'host1'
    expected_result = {'ansible_facts': {'fact1': 'value1'}, '_ansible_parsed': True}
    test_object._dump(test_data, data_path + '/' + file_name)
    actual_result = test_object._load(data_path + '/' + file_name)

    assert actual_result == expected_result
    print('Test_CacheModule SUCCESS')

# Generated at 2022-06-13 11:29:42.259302
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm



# Generated at 2022-06-13 11:29:46.195681
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.get_options() == {'_prefix': 'ansible_fact_', '_timeout': 86400, '_uri': '~/.ansible/cached_facts'}

# Generated at 2022-06-13 11:29:48.161775
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)
    assert isinstance(cache._load, object)
    assert isinstance(cache._dump, object)

# Generated at 2022-06-13 11:29:56.524572
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_connection = "/tmp"
    cache_plugin_prefix = "ansible_cache"
    cache_plugin_timeout = 86400
    cache_type = "jsonfile"

    cache = CacheModule(cache_plugin_connection, cache_type, cache_plugin_prefix, cache_plugin_timeout)
    assert cache.cache_plugin_connection == cache_plugin_connection
    assert cache.cache_plugin_prefix == cache_plugin_prefix
    assert cache.cache_plugin_timeout == cache_plugin_timeout
    assert cache._plugin_type == cache_type

# Generated at 2022-06-13 11:29:57.483351
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Tests __init__ method
    CacheModule()

# Generated at 2022-06-13 11:30:05.686689
# Unit test for constructor of class CacheModule

# Generated at 2022-06-13 11:30:11.349796
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cls = type('CacheModule', (object,), {})
    obj = CacheModule(cls)
    assert obj is not None
    # Test init method of parent class
    obj.init({'_uri': '/tmp'})
    assert obj._cachefile is not None

# Generated at 2022-06-13 11:30:22.269924
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import shutil

    module_name = 'jsonfile'
    module_path = os.path.join(os.path.dirname(__file__), module_name + '.py')
    module_args = {'_timeout': '60', '_prefix': 'foo', '_uri': os.path.dirname(os.path.abspath(__file__))}
    test_instance = CacheModule(module_args, module_path)
    assert test_instance is not None

    # Remove the cache directory
    shutil.rmtree(module_args['_uri'])

# Generated at 2022-06-13 11:30:25.994482
# Unit test for constructor of class CacheModule
def test_CacheModule():
    d = None
    c = CacheModule(d)
    assert c._connection == d
    assert c._prefix == ''
    assert c._timeout == 86400

# Generated at 2022-06-13 11:30:27.251958
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm  # object is created successfully

# Generated at 2022-06-13 11:30:30.793287
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # wrong type of argument
    try:
        CacheModule(1)
        assert False
    except TypeError:
        assert True
    # proper type of argument
    try:
        CacheModule({})
        assert True
    except TypeError:
        assert False

# Generated at 2022-06-13 11:30:32.181341
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:32.791905
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({})
    assert isinstance(cache, CacheModule)

# Generated at 2022-06-13 11:30:33.241570
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:30:35.505232
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_manager = CacheModule()
    assert cache_manager
    assert hasattr(cache_manager, "get")
    assert hasattr(cache_manager, "set")

# Generated at 2022-06-13 11:30:36.509189
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache != None

# Generated at 2022-06-13 11:30:41.883801
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Use a memory backed CacheModule for testing.
    cache_plugin = CacheModule()
    assert(cache_plugin is not None)

# Generated at 2022-06-13 11:30:42.894785
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:30:45.216665
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._timeout == 86400
    assert cache._prefix is None
    assert cache._uri == '.'

# Generated at 2022-06-13 11:30:46.152223
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule, type)

# Generated at 2022-06-13 11:30:47.430694
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_obj = CacheModule()
    assert test_obj

# Generated at 2022-06-13 11:30:50.185654
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.valid is True
    assert cache_module.retrieved is False
    assert cache_module.plugin_name == 'jsonfile'
    assert cache_module.plugin_timeout == 86400

# Generated at 2022-06-13 11:30:56.088666
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = '/tmp/test/path'
    prefix = 'my_prefix'
    timeout = 2
    cache_connection = CacheModule({'_uri': path, '_prefix': prefix, '_timeout': timeout})
    assert cache_connection._basedir == path
    assert cache_connection._prefix == prefix
    assert cache_connection._timeout == timeout

# Generated at 2022-06-13 11:30:57.588477
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin

# Generated at 2022-06-13 11:31:00.160433
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    assert a.file_extension == '.json'
    assert a._connection is None

# Generated at 2022-06-13 11:31:04.673959
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._options["_uri"] == "~/.ansible/tmp/ansible-fact-cache"
    assert cache_module._options["_timeout"] == 86400
    assert cache_module._options["_prefix"] == "ansible_facts"

# Generated at 2022-06-13 11:31:13.446789
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()._prefix == 'ansible_fact_caching_'
    assert CacheModule()._timeout == 86400

test_CacheModule()

# Generated at 2022-06-13 11:31:14.705313
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:31:16.011396
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.name == 'jsonfile', "name is jsonfile"

# Generated at 2022-06-13 11:31:18.774009
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = '/tmp/ansible-cache/'
    cm = CacheModule(uri)
    assert cm.cachefile == uri
    assert cm.timeout == 86400

# Generated at 2022-06-13 11:31:20.620593
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)


# Generated at 2022-06-13 11:31:31.417757
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_path = "/tmp/ansible-test-cache"
    cache_timeout = 60
    cache_plugin_name = 'jsonfile'
    cls = CacheModule()

    module_args = dict(
        _uri=cache_path,
        _timeout=cache_timeout,
    )

    cls.set_options(direct=module_args)
    assert cls.get_options() == module_args
    assert cls.has_expired()

    cls._connection = {"test1": "test1value", "test2": "test2value"}
    cls._dirty = True

    cls._load_cache()
    assert cls._connection == {"test1": "test1value", "test2": "test2value"}
    assert cls._dirty is False

    tmp_cache_path = cls._

# Generated at 2022-06-13 11:31:32.657068
# Unit test for constructor of class CacheModule
def test_CacheModule():
    data = {}
    cache = CacheModule(data)


# Generated at 2022-06-13 11:31:33.754431
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

# Generated at 2022-06-13 11:31:34.243020
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:31:39.134342
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    # If a class is created without any constructor, then it will not have any attributes
    # of this class.
    assert not cache._connection
    assert not cache._timeout
    assert not cache._prefix



# Generated at 2022-06-13 11:31:52.016259
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}, {})

# Generated at 2022-06-13 11:31:53.400675
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'_uri': '/tmp'})._uri == '/tmp'

# Generated at 2022-06-13 11:31:56.000885
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert isinstance(cache_module, CacheModule) == True

# Generated at 2022-06-13 11:31:57.405743
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin is not None

# Generated at 2022-06-13 11:32:01.041226
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._get_plugin_option('_uri') is None
    assert cache._get_plugin_option('_prefix') == ''
    assert cache._get_plugin_option('_timeout') == 86400

# Generated at 2022-06-13 11:32:02.151603
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), BaseFileCacheModule)

# Generated at 2022-06-13 11:32:02.880792
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert not CacheModule() == None

# Generated at 2022-06-13 11:32:04.911975
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._serializer == 'json'
    assert c._timeout == 86400

# Generated at 2022-06-13 11:32:06.629780
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._timeout == 86400
    assert c._load("testfile") == {}

# Generated at 2022-06-13 11:32:10.332843
# Unit test for constructor of class CacheModule
def test_CacheModule():
    __tracebackhide__ = True
    (jsonfile, uri, timeout) = CacheModule(None)
    assert jsonfile is not None
    assert uri == '/tmp/ansible-plugincache'
    assert timeout == 86400

# Generated at 2022-06-13 11:32:36.701945
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:32:46.740949
# Unit test for constructor of class CacheModule
def test_CacheModule():
    hostname = 'host1'
    source_backup_file = '/tmp/ansible-fact-cache-' + hostname
    source_cache_file = source_backup_file + '.cache'
    cache_plugin_connection = '/tmp'
    cache = CacheModule(plugin_connection=cache_plugin_connection)
    assert cache._get_cache_basedir() == cache_plugin_connection + '/'
    assert cache._get_cache_file(hostname) == cache_plugin_connection + '/ansible-fact-cache-' + hostname
    cache.set(hostname, 'data1')
    cache.get(hostname)
    cache.set(hostname, 'data2')
    cache.get(hostname)
    cache.set(hostname, None)
    cache.get(hostname)

# Generated at 2022-06-13 11:32:48.158011
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache = CacheModule({'_uri': 'test_path'})

# Generated at 2022-06-13 11:32:49.832240
# Unit test for constructor of class CacheModule
def test_CacheModule():
    jsonfile = CacheModule()
    jsonfile._load("/tmp/key")
    jsonfile._dump("/tmp/key", "value")

# Generated at 2022-06-13 11:32:53.895868
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ == 'A caching module backed by json files.'
    assert CacheModule._load.__doc__ == '''\
        Valid JSON is always UTF-8 encoded.
        '''
    assert CacheModule._dump.__doc__ == '''\
        with codecs.open(filepath, 'w', encoding='utf-8') as f:
            f.write(json.dumps(value, cls=AnsibleJSONEncoder, sort_keys=True, indent=4))
        '''


# Generated at 2022-06-13 11:32:56.071159
# Unit test for constructor of class CacheModule
def test_CacheModule():
  cache = CacheModule()

  # Test template extension
  assert cache.ext == '.json'

# Generated at 2022-06-13 11:32:57.015530
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ == "A caching module backed by json files."

# Generated at 2022-06-13 11:32:59.099372
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert 'CacheModule' in globals()
    obj = globals()['CacheModule']()
    assert hasattr(obj, 'get')
    assert hasattr(obj, 'set')
    with obj.plugin_lock:
        assert hasattr(obj, '_load')
        assert hasattr(obj, '_dump')

# Generated at 2022-06-13 11:33:00.012302
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert x.get('foo') == None

# Generated at 2022-06-13 11:33:00.992750
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(play_context=None, new_stdin=None)


# Generated at 2022-06-13 11:33:33.573916
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c.ext == '.json'
    assert c.prefix == 'ansible-facts'
    assert c.timeout == 86400
    assert c.plugin_name == 'jsonfile'
    assert c._connection is None
    assert c.plugin_args == {'_prefix': 'ansible-facts', '_timeout': 86400}
    assert c._load == CacheModule._load
    assert c._dump == CacheModule._dump

# Generated at 2022-06-13 11:33:43.229780
# Unit test for constructor of class CacheModule
def test_CacheModule():
    set_env_var('ANSIBLE_CACHE_PLUGIN_CONNECTION', 'jsonfile')
    set_env_var('ANSIBLE_CACHE_PLUGIN_PREFIX', 'jsonfile')
    set_env_var('ANSIBLE_CACHE_PLUGIN_TIMEOUT', 'jsonfile')
    _uri = 'jsonfile'
    _prefix = 'jsonfile'
    _timeout = 'jsonfile'
    cache = CacheModule(_uri, _prefix, _timeout)
    assert isinstance(cache, CacheModule)
    assert isinstance(cache, BaseFileCacheModule)
    assert cache._uri == 'jsonfile'
    assert cache._prefix == 'jsonfile'
    assert cache._timeout == 'jsonfile'

# Generated at 2022-06-13 11:33:49.636961
# Unit test for constructor of class CacheModule
def test_CacheModule():
    base_dir = '/var/tmp'
    obj = CacheModule(
        base_dir,
        'jsonfile',
        False,
        False,
        '/tmp/ansible/facts',
    )

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:33:50.307714
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:33:51.445717
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule().__class__.__name__ == 'CacheModule'

# Generated at 2022-06-13 11:33:55.260210
# Unit test for constructor of class CacheModule
def test_CacheModule():
    config = {
        '_uri': 'foo',
        '_prefix': 'prefix',
        '_timeout': 42
    }
    cache = CacheModule(config)
    assert cache['_uri'] == 'foo'
    assert cache['_prefix'] == 'prefix'
    assert cache['_timeout'] == 42

# Generated at 2022-06-13 11:33:57.405964
# Unit test for constructor of class CacheModule
def test_CacheModule():
    instance = CacheModule()
    assert isinstance(instance, BaseFileCacheModule)

# Generated at 2022-06-13 11:33:59.379035
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert(cm.file_extension == 'json')

# Generated at 2022-06-13 11:34:04.058384
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)
    assert cache.get_extension() == ".json"
    assert cache.is_valid_content(b"")
    assert cache.is_valid_content(b"{}")

# Generated at 2022-06-13 11:34:14.286749
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert (plugin.plugin_name == 'jsonfile')

# Generated at 2022-06-13 11:35:10.944338
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.cache_prefix == ''
    assert cache._timeout == 86400

if __name__ == '__main__':
    cache = CacheModule()
    print('toto')
    pass

# Generated at 2022-06-13 11:35:12.157057
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule(None)
    assert cache_module is not None

# Generated at 2022-06-13 11:35:13.413979
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict(path='.'))

# Generated at 2022-06-13 11:35:14.410490
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule(None)
    assert isinstance(c, CacheModule)

# Generated at 2022-06-13 11:35:17.476804
# Unit test for constructor of class CacheModule
def test_CacheModule():
    args = {}
    args['_uri'] = 'test/'
    args['_prefix'] = 'test_'
    args['_timeout'] = 60
    obj = CacheModule(args)
    assert obj is not None
    assert obj._prefix == 'test_'
    assert obj._timeout == 60
    assert obj._connection == 'test/'

# Generated at 2022-06-13 11:35:20.474993
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        CacheModule()
    except Exception:
        raise AssertionError


if __name__ == '__main__':
    cache = CacheModule()
    cache.set('testing', 'value')
    print(cache.get('testing'))

# Generated at 2022-06-13 11:35:21.299047
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:35:25.118780
# Unit test for constructor of class CacheModule
def test_CacheModule():
    with open('./.test.js', 'r') as f:
        content = f.read()
    assert 'ansible_memory_mb' in content
    assert 'ansible_processor_cores' in content

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:35:26.767634
# Unit test for constructor of class CacheModule
def test_CacheModule():
    current = CacheModule(None)

# Generated at 2022-06-13 11:35:28.193305
# Unit test for constructor of class CacheModule
def test_CacheModule():
    result = CacheModule()

    assert isinstance(result, CacheModule)


# Generated at 2022-06-13 11:37:27.099920
# Unit test for constructor of class CacheModule
def test_CacheModule():
	test_module = CacheModule()
	assert test_module is not None

# Generated at 2022-06-13 11:37:30.036121
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.get_timeout() == 86400
    assert cm.supports_eviction()
    assert not cm.supports_get_options()
    assert not cm.supports_get_multi()
    assert not cm.supports_set_options()

# Generated at 2022-06-13 11:37:33.207124
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._prefix == 'ansible_facts'
    assert module._timeout == 86400
    assert module._connection == None

# Generated at 2022-06-13 11:37:34.101962
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

# Generated at 2022-06-13 11:37:35.153960
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    print(cache)

# Generated at 2022-06-13 11:37:37.004700
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.__class__.__name__ == 'CacheModule'



# Generated at 2022-06-13 11:37:40.679500
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm1 = CacheModule()
    assert cm1.get_cache_file_for_host("localhost") == "/var/tmp/ansible/localhost"
    assert cm1._timeout == 24 * 60 * 60



# Generated at 2022-06-13 11:37:43.818461
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Test CacheModule class constructor
    """
    cache_plugin = CacheModule()
    assert cache_plugin._connection is None
    assert cache_plugin._prefix == 'cache'
    assert cache_plugin._timeout == 86400
    assert cache_plugin._cache_files == {}


# Generated at 2022-06-13 11:37:48.119450
# Unit test for constructor of class CacheModule
def test_CacheModule():

    c = CacheModule()
    if c is None:
        raise ValueError("Object is empty")
    if not isinstance(c, CacheModule):
        raise ValueError("Invalid object type")

    return

# Generated at 2022-06-13 11:37:52.415375
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test for constructor of class CacheModule
    """

    # initialize cache object
    cache_obj = CacheModule()

    # assert values
    assert cache_obj.get_timeout() == 86400

    return