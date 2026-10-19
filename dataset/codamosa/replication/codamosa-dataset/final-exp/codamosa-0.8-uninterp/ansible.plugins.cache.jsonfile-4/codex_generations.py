

# Generated at 2022-06-13 11:29:18.257378
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()

# Generated at 2022-06-13 11:29:20.081465
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    #assert cm.get_db_filename('localhost') == 'localhost.json'

# Generated at 2022-06-13 11:29:23.444816
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.get_cache_timeout() == 86400
    assert cache.get_cache_basedir() == '/tmp'
    assert cache.get_cache_prefix() == ''

# Generated at 2022-06-13 11:29:26.709461
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({})
    assert cache._get_cache_file_path('a') == '.ansible_cached_data/ansible-a'

# Generated at 2022-06-13 11:29:28.821815
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()._load('nonExistantPath') is None

# Generated at 2022-06-13 11:29:33.117246
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """constructor of CacheModule class should return instance of the class"""
    module_jsonfile = CacheModule()
    assert isinstance(module_jsonfile, CacheModule)


# Generated at 2022-06-13 11:29:34.691392
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule._cachefile_suffix == '.cache'

# Generated at 2022-06-13 11:29:38.377629
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._connection == '_uri'
    assert module._timeout == '_timeout'
    assert module._prefix == '_prefix'
    assert type(module._timeout) == type(0)
    assert hasattr(module, 'get')
    assert hasattr(module, 'set')
    assert hasattr(module, 'keys')
    assert hasattr(module, 'delete')

# Generated at 2022-06-13 11:29:49.557150
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test default directory
    assert CacheModule()._directory == CacheModule._DEFAULT_DIRECTORY
    assert CacheModule()._directory == '/tmp/ansible-local'

    # Test invalid directory
    cache = CacheModule()
    cache._directory = 'invalid_dir'
    with open('/tmp/ansible-local/host1.json') as f:
        data = json.load(f)
        assert not data
        assert 'invalid_dir/host1.json' in str(data)

    # Test valid directory
    cache._directory = '/tmp/ansible-local'
    with open('/tmp/ansible-local/host1.json') as f:
        data = json.load(f)
        assert data
        assert data['test_key'] == 'test_value'

# Generated at 2022-06-13 11:30:01.291621
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import tempfile

    c = CacheModule()
    c.set_options({'_uri': tempfile.gettempdir()})

    c.flush()
    assert not c.has_expired('testhost', 'test')
    data = c.get('testhost', 'test')
    assert data is None
    data = {'a': 1}
    c.set('testhost', 'test', data)
    assert c.has_expired('testhost', 'test') is False

    filepath = c._load_path('testhost', 'test')
    assert os.path.exists(filepath)
    content = c._load(filepath)
    assert content == data

    data = {'b': 2}
    c.set('testhost', 'test', data)

# Generated at 2022-06-13 11:30:05.295754
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''Exercise the CacheModule class constructor.
    This is not a true unit test: it involves the filesystem, and it
    does not test the methods of CacheModule.  It does not have any
    assertions, so it can't be checked for success or failure.
    '''

    # Create the CacheModule object.
    cache_plugin = CacheModule()

# Generated at 2022-06-13 11:30:07.272263
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = "test/test"
    prefix = "prefix"
    timeout = 86400
    cache_module = CacheModule(connection, prefix, timeout)
    assert isinstance(cache_module, CacheModule)

# Generated at 2022-06-13 11:30:09.140670
# Unit test for constructor of class CacheModule
def test_CacheModule():
    
    # Create and return cache module for JSON
    cacheModule = CacheModule()

    # If created object is not null, then test case has passed
    assert cacheModule is not None

# Generated at 2022-06-13 11:30:10.159981
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict(), dict())

# Generated at 2022-06-13 11:30:13.067795
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cls_inst = CacheModule()
    assert cls_inst._timeout == 86400
    assert cls_inst._options['_timeout'] == 86400

# Generated at 2022-06-13 11:30:14.569862
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert isinstance(m, CacheModule)


# Generated at 2022-06-13 11:30:18.170848
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = "/tmp/ansible_fact_cache"
    expiration = 7200 # 2 hours
    cache = CacheModule({'_uri': path, '_timeout': expiration})

# Generated at 2022-06-13 11:30:19.389783
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._uri == "~/.ansible/tmp"

# Generated at 2022-06-13 11:30:20.233772
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict())


# Generated at 2022-06-13 11:30:25.446533
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test empty constructor
    cache_module = CacheModule()
    assert cache_module is not None

    # Test constructor with non-empty parameter
    cache_module = CacheModule({'A':'B'})
    assert cache_module is not None
    assert cache_module.keys() == ['A']
    assert cache_module['A'] == 'B'


# Generated at 2022-06-13 11:30:31.139883
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)
    assert hasattr(CacheModule, '_load')
    assert hasattr(CacheModule, '_dump')

# Generated at 2022-06-13 11:30:32.075349
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(None)

# Generated at 2022-06-13 11:30:37.061591
# Unit test for constructor of class CacheModule
def test_CacheModule():
    base_dir = '/path/to/directory'
    timeout = '100'
    env = {'ANSIBLE_CACHE_PLUGIN_CONNECTION': base_dir,
           'ANSIBLE_CACHE_PLUGIN_TIMEOUT': timeout}
    module = CacheModule(env)
    assert module
    assert module.get_basedir() == base_dir
    assert module.get_timeout() == int(timeout)

# Generated at 2022-06-13 11:30:38.512871
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Testing if we can create a variable of type CacheModule
    CacheModule()

# Generated at 2022-06-13 11:30:46.883544
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """ Check that the not implemented methods work correctly """
    cache = CacheModule()
    with pytest.raises(NotImplementedError):
        cache.get()
    with pytest.raises(NotImplementedError):
        cache.set()
    with pytest.raises(NotImplementedError):
        cache.keys()
    with pytest.raises(NotImplementedError):
        cache.contains()
    with pytest.raises(NotImplementedError):
        cache.delete()
    with pytest.raises(NotImplementedError):
        cache.flush()

# Generated at 2022-06-13 11:30:48.708279
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None
    assert cache.plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:30:50.861123
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:30:52.026386
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()

# Generated at 2022-06-13 11:30:53.371759
# Unit test for constructor of class CacheModule
def test_CacheModule():
  # Check that the constructor does not fail
  CacheModule()

# Generated at 2022-06-13 11:31:01.684019
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    test_values = {
        '_prefix': 'test_prefix',
        '_timeout': 1,
        '_load': cache_module._load,
        '_dump': cache_module._dump,
    }
    cache_module.set_options(test_values)

    for key in test_values:
        assert getattr(cache_module, key) == test_values[key]

# Generated at 2022-06-13 11:31:08.427462
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()

# Generated at 2022-06-13 11:31:09.925981
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:31:20.031746
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    # Assert setting fields as expected
    assert module.file_extension is '.json'
    assert module._timeout == 86400
    # Check constructor creates file cache directory
    assert os.path.exists(module._connection)
    # Check constructor creates host specific file
    test_host = 'test-host'
    test_file = os.path.join(module._connection, module.get_file_path(test_host, None))
    assert os.path.exists(test_file)
    # Check file exists with correct extension
    assert test_file.endswith('.json')

# Generated at 2022-06-13 11:31:20.581868
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()


# Generated at 2022-06-13 11:31:22.870638
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._load is not None

# Generated at 2022-06-13 11:31:32.646654
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_connection = '/var/tmp'
    cache_plugin_timeout = '86400'
    cache_plugin_prefix = 'cache'

    # Since we are running in tests, there are no env vars and config files
    # Set enrivornment variables and use them in Class CacheModule
    import os
    os.environ["ANSIBLE_CACHE_PLUGIN_CONNECTION"] = cache_plugin_connection
    os.environ["ANSIBLE_CACHE_PLUGIN_TIMEOUT"] = cache_plugin_timeout
    os.environ["ANSIBLE_CACHE_PLUGIN_PREFIX"] = cache_plugin_prefix

    c = CacheModule()
    assert c.get_options()['_uri'] == cache_plugin_connection
    assert c.get_options()['_timeout'] == cache_

# Generated at 2022-06-13 11:31:33.446355
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule() is not None


# Generated at 2022-06-13 11:31:34.541935
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule({})
    assert isinstance(cache_plugin, CacheModule)

# Generated at 2022-06-13 11:31:38.117966
# Unit test for constructor of class CacheModule
def test_CacheModule():
    facts = {'myvar': 'myval'}
    module = CacheModule({}, uri='/tmp', timeout=0)
    assert module.get('dummyhost') == None
    assert module.set('dummyhost', facts)
    assert module.get('dummyhost') == facts

# Generated at 2022-06-13 11:31:40.125858
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test constructor
    module = CacheModule()
    assert module._load_file is None
    assert module._dump_file is None

# Generated at 2022-06-13 11:31:52.969474
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)

# Generated at 2022-06-13 11:31:53.718849
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert not obj

# Generated at 2022-06-13 11:31:56.746699
# Unit test for constructor of class CacheModule
def test_CacheModule():

    c = CacheModule()
    assert c._cache_prefix == 'ansible_fact_cache_'
    assert c._timeout == 86400
    assert c.validate_filepath('localhost') == 'localhost'

# Generated at 2022-06-13 11:32:00.357977
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.timeout == 86400
    assert cache.cache_path == None
    assert cache.prefix == None
    assert cache.MAX_FAILED_REFRESHES == 0



# Generated at 2022-06-13 11:32:01.845908
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(cache is not None)

# Generated at 2022-06-13 11:32:03.353458
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert 'ansible.plugins.cache.jsonfile' == CacheModule.__module__

# Generated at 2022-06-13 11:32:06.919231
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(None, task_vars=dict())

    assert cache._connect() is None
    assert cache._prefix == "ansible-facts"
    assert cache._load(None) is None
    assert cache._dump(None, None) is None
    assert cache.get("test") is None
    assert cache.get_facts() is None
    assert cache.set("test", None) is None
    assert cache.set_facts("test") is None

# Generated at 2022-06-13 11:32:08.711310
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert len(CacheModule()) == 0
    assert len(CacheModule(timeout=200)) == 200

# Generated at 2022-06-13 11:32:11.926052
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Without a name, it should return the default plugin
    cache_plugin = CacheModule()
    assert "jsonfile" in cache_plugin.__module__

    # With a name it should return the given name plugin
    cache_plugin = CacheModule('memory')
    assert "memory" in cache_plugin.__module__

    # With a non existent name it should return the default plugin
    cache_plugin = CacheModule('foobar')
    assert "jsonfile" in cache_plugin.__module__

# Generated at 2022-06-13 11:32:19.107865
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = BaseFileCacheModule()
    assert cache_module.get_cache_file_path(filepath='test') == 'test'
    assert cache_module.get_cache_file_content() == False
    assert cache_module.get_set_cache() == False
    assert cache_module.get_cache_file_path(filepath='test') == 'test'
    assert cache_module.set_cache_file_path(filepath='test') == 'test'
    assert cache_module.get_cache_file_path(filepath='test') == 'test'
    assert cache_module.get_cache_file_content() == True
    assert cache_module.set_cache_file_content(cache_file_content={}) == {}
    assert cache_module.get_cache_file_content() == {}

# Generated at 2022-06-13 11:32:46.792564
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test constructor with no parameters
    cache = CacheModule()
    if type(cache.__class__).__name__ != 'CacheModule':
        # The constructor does not return an object of the correct type
        assert False
    # Test constructor with one parameter
    cache = CacheModule('test')
    if type(cache.__class__).__name__ != 'CacheModule':
        # The constructor does not return an object of the correct type
        assert False

# Generated at 2022-06-13 11:32:49.684199
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    test constructor for classe CacheModule.
    """
    cacheModule = CacheModule()
    if cacheModule:
        print("Class CacheModule loaded")


if __name__ == '__main__':
    # unit test to load the class
    test_CacheModule()

# Generated at 2022-06-13 11:32:51.256614
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)



# Generated at 2022-06-13 11:32:52.751385
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:32:55.098942
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert(cm is not None)

# Generated at 2022-06-13 11:32:56.634210
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()


# Generated at 2022-06-13 11:33:00.141782
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit tests for constructor of class CacheModule.
    """
    cachemodule = CacheModule()

    assert cachemodule is not None

# Generated at 2022-06-13 11:33:03.752131
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._connection == ''
    assert cache._prefix == 'ansible_'
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:33:05.149557
# Unit test for constructor of class CacheModule
def test_CacheModule():
    my_cache = CacheModule()
    assert my_cache.timeout == 86400

# Generated at 2022-06-13 11:33:06.358593
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin._timeout == 86400

# Generated at 2022-06-13 11:33:58.542446
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._timeout == 86400


# Generated at 2022-06-13 11:34:00.459192
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test just constructor, since CacheModule only defines __init__()
    assert CacheModule()

# Generated at 2022-06-13 11:34:01.222201
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:34:04.254081
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert isinstance(x, BaseFileCacheModule) == True, "Failed to create CacheModule instance"

# Generated at 2022-06-13 11:34:05.021513
# Unit test for constructor of class CacheModule
def test_CacheModule():
	CacheModule()

# Generated at 2022-06-13 11:34:07.497489
# Unit test for constructor of class CacheModule
def test_CacheModule():
  plugin = CacheModule()
  assert plugin is not None
  assert isinstance(plugin, BaseFileCacheModule)

# Generated at 2022-06-13 11:34:09.281181
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cachePlugin = CacheModule()
    assert cachePlugin._connection is None

# Generated at 2022-06-13 11:34:10.379047
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:34:11.752592
# Unit test for constructor of class CacheModule
def test_CacheModule():
   cache = CacheModule()
   assert cache.cache_plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:34:12.251434
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:36:00.758181
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c=CacheModule()

# Generated at 2022-06-13 11:36:02.637481
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Test constructor of class CacheModule"""
    mod = CacheModule()
    assert mod.CACHE_PLUGIN_TYPE == 'jsonfile'

# Generated at 2022-06-13 11:36:03.463168
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()



# Generated at 2022-06-13 11:36:05.538473
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule('/tmp')

    assert obj._timeout == 86400
    assert obj._prefix == ""
    assert obj._cache == '/tmp'
    assert obj._cache_key == 'cacheplugin'

# Generated at 2022-06-13 11:36:08.830459
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({'_uri': '/tmp', '_prefix': 'test'})
    # Test that `filepath` is hashed
    filepath = cache._get_file_path('example.com')
    assert 'example.com' not in filepath

# Unit tests for load/dump functions

# Generated at 2022-06-13 11:36:12.015232
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_connection = '/tmp'
    cache_plugin_timeout = 300
    cache_plugin_prefix = ''
    cm = CacheModule(cache_plugin_connection, cache_plugin_timeout, cache_plugin_prefix)
    assert cm._connection == '/tmp'
    assert cm._timeout == 300
    assert cm._prefix == ''

# Generated at 2022-06-13 11:36:13.859821
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, CacheModule) and module.__class__.__name__ == 'CacheModule'

# Generated at 2022-06-13 11:36:14.466552
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()


# Generated at 2022-06-13 11:36:15.499391
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test for constructor of class CacheModule
    """
    # Needs to be more specific
    assert True

# Generated at 2022-06-13 11:36:15.833596
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()