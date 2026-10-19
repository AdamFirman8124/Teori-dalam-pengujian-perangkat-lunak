

# Generated at 2022-06-13 11:29:20.071559
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin_instance = CacheModule(task=None, play_context=None, new_stdin=None)
    assert isinstance(plugin_instance, CacheModule)

# Generated at 2022-06-13 11:29:21.622615
# Unit test for constructor of class CacheModule
def test_CacheModule():
    myCache = CacheModule()
    assert isinstance(myCache, CacheModule) is True

# Generated at 2022-06-13 11:29:24.335710
# Unit test for constructor of class CacheModule
def test_CacheModule():
    json_file_path = 'test/test.json'
    cache_module = CacheModule(json_file_path)
    assert cache_module.file_path == json_file_path

# Generated at 2022-06-13 11:29:31.573294
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin._timeout == 86400
    assert plugin._connection == '~/.ansible/tmp/ansible-local/fact_cache'
    assert plugin._prefix == 'ansible_facts'

    plugin = CacheModule(timeout=300)
    assert plugin._timeout == 300
    assert plugin._connection == '~/.ansible/tmp/ansible-local/fact_cache'
    assert plugin._prefix == 'ansible_facts'

    plugin = CacheModule(connection='/tmp/.cache/facts')
    assert plugin._timeout == 86400
    assert plugin._connection == '/tmp/.cache/facts'
    assert plugin._prefix == 'ansible_facts'

    plugin = CacheModule(prefix='facts')
    assert plugin._timeout == 86400

# Generated at 2022-06-13 11:29:32.704573
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:29:38.343274
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m._load == m.load
    assert m._dump == m.dump
    assert m.get_cache_prefix == get_cache_prefix
    assert m.get_cache_timeout == get_cache_timeout

# Generated at 2022-06-13 11:29:39.839725
# Unit test for constructor of class CacheModule
def test_CacheModule():

    """
    This function will be used for testing the constructor.

    :return:
    """
    cache_module = CacheModule()

# Generated at 2022-06-13 11:29:42.563520
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacher = CacheModule()
    cacher._timeout = 86400
    cacher._prefix = 'foobar'
    cacher._uri = '/tmp'

# Generated at 2022-06-13 11:29:43.552284
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ is not None

# Generated at 2022-06-13 11:29:44.109922
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print(CacheModule())

# Generated at 2022-06-13 11:29:47.802816
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ == "A caching module backed by json files."
    cache_module=CacheModule()
    assert cache_module._load("") == None
    assert cache_module._dump(None, "") == None

# Generated at 2022-06-13 11:29:56.375724
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._cache_files_dir == c._CLI_CACHE_PLUGIN_CONN
    assert c._prefix == c._CLI_CACHE_PLUGIN_PREFIX
    assert c._timeout == c._CLI_CACHE_PLUGIN_TIMEOUT

    c2 = CacheModule(u'foo', u'bar', u'timeout')
    assert c2._cache_files_dir == 'foo'
    assert c2._prefix == 'bar'
    assert c2._timeout == 'timeout'

# Generated at 2022-06-13 11:29:57.713513
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # unit test to construct a class named CacheModule
    CacheModule()

# Generated at 2022-06-13 11:29:59.710669
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Set instance
    cache = CacheModule()
    # AssertionError if cache directory is not specified
    assert cache.cache_dir == None

# Generated at 2022-06-13 11:30:01.585770
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert isinstance(cache_plugin, BaseFileCacheModule)


# Generated at 2022-06-13 11:30:03.088803
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c.file_extension == 'json'

# Generated at 2022-06-13 11:30:04.112260
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__

# Generated at 2022-06-13 11:30:05.390138
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin is not None


# Generated at 2022-06-13 11:30:07.314894
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache._setup('/path/to/dir')
    assert cache.get_basedir() == '/path/to/dir'

# Generated at 2022-06-13 11:30:13.910406
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test = CacheModule()
    assert test._cache_dir == ''

    # Environment
    test = CacheModule(environ_config={"ANSIBLE_CACHE_PLUGIN_CONNECTION": "/tmp",
                                       "ANSIBLE_CACHE_PLUGIN_PREFIX": "test",
                                       "ANSIBLE_CACHE_PLUGIN_TIMEOUT": "60"})
    assert test._cache_dir == '/tmp'
    assert test._prefix == 'test'
    assert test._timeout == 60

    # Ini
    test = CacheModule(ini_config={'defaults': {"fact_caching_connection": "/tmp",
                                                "fact_caching_prefix": "test",
                                                "fact_caching_timeout": 60}})
    assert test._cache_dir == '/tmp'


# Generated at 2022-06-13 11:30:17.734241
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_name = 'jsonfile'
    plugin = BaseFileCacheModule.load_plugin(cache_plugin_name)
    assert isinstance(plugin, CacheModule)

# Generated at 2022-06-13 11:30:19.868679
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()
    assert cacheModule is not None

    # Test for inherited method
    cacheModule._load("filepath")
    cacheModule._dump("value","filepath")

# Generated at 2022-06-13 11:30:20.858862
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__name__ == 'CacheModule'

# Generated at 2022-06-13 11:30:22.685789
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    print(cache_plugin.__dict__)
    assert cache_plugin._load('file1.json') == {}

# Generated at 2022-06-13 11:30:24.049241
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(load_on_init=False)

# Generated at 2022-06-13 11:30:31.099304
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = "/home/myhome/Documents/ansible/tests/fixtures/cache"
    prefix = "myprefix"
    timeout = 123456789
    cache_plugin = CacheModule(uri, prefix, timeout)
    assert(cache_plugin.plugin_timeout == 123456789)
    assert(cache_plugin.plugin_prefix == "myprefix")
    assert(cache_plugin.plugin_basedir == "/home/myhome/Documents/ansible/tests/fixtures/cache")
    assert(cache_plugin.file_extension == '.json')

# Generated at 2022-06-13 11:30:33.134424
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test of class CacheModule
    """
    cache = CacheModule()
    assert cache.validate() == (True, None)
    assert cache.get('localhost') == None

# Generated at 2022-06-13 11:30:35.777144
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._cache_dir == '/tmp/ansible_facts'
    assert cache._prefix == 'ansible_facts'
    assert cache._timeout == 86400


# Generated at 2022-06-13 11:30:36.464843
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

# Generated at 2022-06-13 11:30:37.415258
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), CacheModule)

# Generated at 2022-06-13 11:30:51.678006
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Init test
    cm = CacheModule()
    assert cm._uri == '~/.ansible/tmp/ansible-fact-cache'
    assert cm._options == {'_prefix': None, '_timeout': 86400}
    assert cm._cache == {}
    
    # Constructor called with valid arguments
    cm = CacheModule({'_uri': '~/.ansible/tmp/ansible-fact-cache', '_timeout': 300})
    assert cm._uri == '~/.ansible/tmp/ansible-fact-cache'
    assert cm._options == {'_prefix': None, '_timeout': 300}
    assert cm._cache == {}

    # Constructor called with invalid arguments

# Generated at 2022-06-13 11:31:04.674016
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    # The '_uri'  property can be any path
    test_path = 'test_path'
    # Create an instance of the CacheModule class
    cm = CacheModule(path=test_path)
    # Create a file with the name of the host
    test_host = 'test_host'
    test_file = os.path.join(test_path, test_host)
    # Create some test data
    test_data = {'test': 1, 'another test': 'here'}
    # Write the data to the file
    cm._dump(test_data, test_file)
    # Read back the data from the file
    returned_data = cm._load(test_file)
    # Clean up test file
    os.remove(test_file)

# Generated at 2022-06-13 11:31:07.320689
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.loader import cache_loader
    x = cache_loader.get("jsonfile", class_only=True)
    assert x is not None

    # Create a class instance
    x = cache_loader.get("jsonfile")
    assert x is not None

# Generated at 2022-06-13 11:31:11.969090
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Initialize instance of class CacheModule
    cache_module = CacheModule()

    # Check if 'path' is part of instance variables
    assert hasattr(cache_module, 'path'), "The `path` instance variable should exist!"

# Generated at 2022-06-13 11:31:25.151883
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

    # Method is_valid_cache_plugin_option
    assert cache.is_valid_cache_plugin_option(None, None, '_uri') == True
    assert cache.is_valid_cache_plugin_option(None, None, '_prefix') == True
    assert cache.is_valid_cache_plugin_option(None, None, '_timeout') == True
    assert cache.is_valid_cache_plugin_option(None, None, '_timeout_raw') == False
    assert cache.is_valid_cache_plugin_option(None, None, '_invalid') == False
    
    # Method cache_plugin_setup
    assert cache.cache_plugin_setup(None, None) == True
    
    # Method _load (coverage)

# Generated at 2022-06-13 11:31:29.827903
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    from ansible.parsing.ajson import AnsibleJSONEncoder, AnsibleJSONDecoder
    cache = CacheModule()
    assert type(cache) == CacheModule

# Generated at 2022-06-13 11:31:34.677063
# Unit test for constructor of class CacheModule
def test_CacheModule():
    conn = {'_uri': 'path/to/facts'}
    adapter = CacheModule(conn)
    assert adapter._connection == conn
    assert adapter._prefix == 'ansible_facts'
    assert adapter._timeout == 86400


# Generated at 2022-06-13 11:31:37.809562
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule(dict())
    assert cache_plugin._timeout == 86400
    assert cache_plugin._expiretime == 86400

# Generated at 2022-06-13 11:31:38.257269
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:31:40.918877
# Unit test for constructor of class CacheModule
def test_CacheModule():
    client = CacheModule()
    assert client._timeout == 86400
    assert client._prefix is None
    assert client._load_file_path is None
    assert client._dump_file_path is None

# Generated at 2022-06-13 11:31:53.844807
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._load is not None
    assert cm._dump is not None

# Generated at 2022-06-13 11:31:55.305402
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, CacheModule)

# Generated at 2022-06-13 11:31:57.065441
# Unit test for constructor of class CacheModule
def test_CacheModule():
    object = CacheModule()
    #assertEqual(object.class_name.__str__(), 'CacheModule')

# Generated at 2022-06-13 11:32:01.041446
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/path/to/dir'
    prefix = 'cache_prefix'
    timeout = 10
    cache = CacheModule(cache_dir, timeout, prefix)
    assert cache.cache._basedir == cache_dir
    assert cache.timeout == timeout
    assert cache._prefix == prefix

# Generated at 2022-06-13 11:32:11.847333
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert 'CacheModule' == CacheModule.__name__
    # test without required parameter
    c = CacheModule(None)
    assert 'Not possible to create cache file object without a path' == c.fail_msg
    # test with valid required parameter
    c = CacheModule('/tmp')
    assert '/tmp' == c._connection
    assert 'jsonfile' == c._cache_prefix
    assert isinstance(c._filecache, dict)
    assert not c._filecache
    assert not c._fail_msg
    assert BaseFileCacheModule == c.__class__.__bases__[0]
    assert BaseFileCacheModule is CacheModule.__bases__[0]
    assert '/tmp' == c._get_cache_path()
    # test setting parameter _timeout
    c._set_timeout(42)
    assert 42 == c

# Generated at 2022-06-13 11:32:14.290063
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module_path = CacheModule
    assert(module_path._load.__name__ == '_load')
    assert(module_path._dump.__name__ == '_dump')

# Generated at 2022-06-13 11:32:14.874835
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:32:16.882150
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._cache_prefix == "ansible_facts"
    assert cache._timeout == 86400
    assert cache._connection == '~/.ansible/cache'

# Generated at 2022-06-13 11:32:18.561229
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test constructor when no args
    assert CacheModule()
    # Test constructor when args is not empty
    assert CacheModule(args={'_uri': 'test_uri'})



# Generated at 2022-06-13 11:32:19.148637
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:32:44.513630
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm, CacheModule) == True

# Generated at 2022-06-13 11:32:45.425627
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module.file_extension == 'json'

# Generated at 2022-06-13 11:32:46.625206
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict(path='/path/to/dir', timeout=300))

# Generated at 2022-06-13 11:32:50.280897
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._load("/tmp/test.json")
    assert cache_module._dump("test_value", "/tmp/test.json")

# Generated at 2022-06-13 11:32:51.569963
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule('/tmp/')
    print(cache.get('test_host', 'test_fact'))

# Generated at 2022-06-13 11:33:00.389616
# Unit test for constructor of class CacheModule
def test_CacheModule():
    table = 'test'
    connection = '/tmp'
    prefix = 'test-'
    timeout = 60
    test_cache_module = CacheModule(table, connection, prefix, timeout)

    assert table == test_cache_module.table()
    assert connection == test_cache_module.connection()
    assert prefix == test_cache_module.prefix()
    assert timeout == test_cache_module.timeout()

# Generated at 2022-06-13 11:33:03.280331
# Unit test for constructor of class CacheModule
def test_CacheModule():
    myCacheModule = CacheModule()
    assert(isinstance(myCacheModule, BaseFileCacheModule))

# Generated at 2022-06-13 11:33:06.203771
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Instantiate a CacheModule object
    cm = CacheModule()

    # Get default _timeout from CacheModule
    assert cm._timeout == 86400

    # Get default _prefix from CacheModule
    assert cm._prefix == 'ansible_facts'

# Generated at 2022-06-13 11:33:11.187240
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Setting the constructor's parameters manually and check the output
    cache_plugin = CacheModule({
        '_uri': '/tmp/ansible_fact_cache',
        '_prefix': 'test'
    })
    assert cache_plugin.cache._timeout == 86400
    assert cache_plugin.cache._prefix == 'test'
    assert cache_plugin.cache._basedir is not None

# Generated at 2022-06-13 11:33:12.224309
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), BaseFileCacheModule)

# Generated at 2022-06-13 11:34:11.668877
# Unit test for constructor of class CacheModule
def test_CacheModule():
    def _load(filepath):
        return "data"
    def _dump(value, filepath):
        return
    cache = CacheModule({
        "_uri": "",
        "_prefix": "",
        "_timeout": "",
    }, _load=_load, _dump=_dump)
    # test _load
    assert cache._load("") == "data"
    # test _dump
    assert cache._dump("", "") is None
    # test get
    assert cache.get("") is None
    # test set
    assert cache.set("", "") is None
    # test keys()
    assert cache.keys() == []

# Generated at 2022-06-13 11:34:14.596241
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'_uri': 'test_caching_connection', '_prefix': 'test_caching_prefix', '_timeout': 'test_caching_timeout'})

# Generated at 2022-06-13 11:34:15.555009
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), CacheModule)

# Generated at 2022-06-13 11:34:16.039464
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:34:16.593937
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:34:17.361512
# Unit test for constructor of class CacheModule
def test_CacheModule():
    global CacheModule
    CacheModule()

# Generated at 2022-06-13 11:34:18.267292
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.name == 'jsonfile'

# Generated at 2022-06-13 11:34:23.880770
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule({'ANSIBLE_CACHE_PLUGIN_CONNECTION': '/', 'ANSIBLE_CACHE_PLUGIN_TIMEOUT':'3000',
                     'ANSIBLE_CACHE_PLUGIN_PREFIX':'prefix'})
    assert x._connection ==  '/'
    assert x._prefix == 'prefix'
    assert x._timeout == 3000

# Generated at 2022-06-13 11:34:27.126450
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache._load = lambda x: {'key': 'value'}
    cache.get('test')
    assert cache.data == {'test': {'key': 'value'}}


# Generated at 2022-06-13 11:34:29.904643
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin is not None

# Module import to execute cache tests with pytest -m cache
from ansible.modules.test import cache

# Generated at 2022-06-13 11:36:29.288661
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """ Test for constructor of class CacheModule """
    # Arrange
    # no args
    # Act
    cache_module = CacheModule()

    # Assert
    assert cache_module._plugin_name == 'jsonfile'
    assert cache_module._cache_backend == 'jsonfile'
    assert cache_module._connection is None
    assert cache_module._prefix is None
    assert cache_module._timeout == 86400
    assert cache_module._load_cache == cache_module._load
    assert cache_module._dump_cache == cache_module._dump



# Generated at 2022-06-13 11:36:30.556416
# Unit test for constructor of class CacheModule
def test_CacheModule():
	cm = CacheModule()
	assert cm

# Generated at 2022-06-13 11:36:32.805043
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        cache = CacheModule()
    except Exception:
        raise AssertionError()

# Generated at 2022-06-13 11:36:35.329136
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # initialize the ansible.plugins.cache.BaseFileCacheModule class
    cache_module = CacheModule()
    return cache_module

# Generated at 2022-06-13 11:36:36.965398
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert hasattr(cache, '_load')
    assert hasattr(cache, '_dump')
    cache.flush()

# Generated at 2022-06-13 11:36:45.590683
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._connection == '~/.ansible/cache'
    assert cache_module._prefix == 'ansible-facts'
    assert cache_module._timeout == 86400

    cache_module = CacheModule(timeout=86400)
    assert cache_module._timeout == 86400

    cache_module = CacheModule(connection='/home/USER/.ansible/cache')
    assert cache_module._connection == '/home/USER/.ansible/cache'
    assert cache_module._timeout == 86400

# Generated at 2022-06-13 11:36:46.307701
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:36:49.029426
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    assert a.__class__.__name__ == "CacheModule"

# Unit tests for method _load

# Generated at 2022-06-13 11:36:54.150072
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.errors import AnsibleCacheError
    from os import path

    test_dir = '/tmp'
    test_dict = {'h': 'localhost', 'a': {'answer': 42}}

    cache = CacheModule()

    # constructor takes no arguments
    assert cache._options == {}

    # default uri is /tmp
    assert path.abspath(cache._connection) == path.abspath(test_dir)

    # default prefix is ansible_facts
    assert cache._prefix == 'ansible_facts'

    # default timeout is 86400
    assert cache._timeout == 86400

    # set uri, prefix and timeout
    cache._options = {
        '_uri': test_dir + '/test_uri',
        '_prefix': 'test_prefix',
        '_timeout': 30
    }



# Generated at 2022-06-13 11:36:54.755212
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)