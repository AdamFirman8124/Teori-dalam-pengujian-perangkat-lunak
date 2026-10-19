

# Generated at 2022-06-13 11:29:17.120095
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()
    assert cacheModule

    # checking if the import fails
    import sys
    import os
    sys.modules['json'] = None
    fp = '_temp_json.json'
    with open(fp, 'w') as f:
        f.write("some stuff")
    cacheModule._load(fp)
    os.unlink(fp)

# Generated at 2022-06-13 11:29:25.406081
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Initialize self.cachedir, self.timeout and self.basedir as CacheModule will
    # Check cachedir exists, create if it doesn't
    # Check basedir exists, create if it doesn't
    # Initialize self.cachefile
    CUT = CacheModule()
    # assert type(CUT.cachedir) == type(self.cachedir)
    # assert type(CUT.timeout) == type(self.timeout)
    # assert type(CUT.basedir) == type(self.basedir)
    # assert type(CUT.cachefile) == type(self.cachefile)

# Generated at 2022-06-13 11:29:27.278746
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert type(cm) is CacheModule
    assert cm.get_option('_timeout') == '86400'

# Generated at 2022-06-13 11:29:28.498123
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'_timeout': '86400'}) is not None


# Generated at 2022-06-13 11:29:35.440785
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)
    assert cache._load( filepath = 'c:\\cache\\ansible\\file.txt') == None
    assert cache._dump( value = 'Test', filepath = 'c:\\cache\\ansible\\file.txt') == None

# Generated at 2022-06-13 11:29:36.381234
# Unit test for constructor of class CacheModule
def test_CacheModule():
    temp_fact_cache = CacheModule()  
    return

# Generated at 2022-06-13 11:29:37.097131
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

# Generated at 2022-06-13 11:29:40.265244
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/tmp/ansible_cachedir'
    host_name = 'localhost'
    test_obj = CacheModule(cache_dir)
    assert test_obj._cache_dir == cache_dir
    assert host_name in test_obj._keys(host_name)
    assert test_obj.get('test_key') is None

# Generated at 2022-06-13 11:29:48.908052
# Unit test for constructor of class CacheModule
def test_CacheModule():
    prefix = 'cachetest'
    uri    = '/tmp/'
    timeout = 1234
    # Ensure that the plugin was constructed correctly.
    cache_plugin = CacheModule(prefix=prefix, uri=uri, timeout=timeout)

    # Constructor should have set the values from the parameters.
    assert cache_plugin._prefix == prefix
    assert cache_plugin._timeout == timeout
    assert cache_plugin._uri == uri

    # Constructor should have initialized _plugin_data correctly.
    assert cache_plugin._plugin_data['meta'] == {}
    assert cache_plugin._plugin_data['data'] == {}



# Generated at 2022-06-13 11:29:49.328287
# Unit test for constructor of class CacheModule
def test_CacheModule():
  assert CacheModule()

# Generated at 2022-06-13 11:29:54.859210
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule(None)
    assert obj._cache_dir == None



# Generated at 2022-06-13 11:30:03.851665
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # test 1
    try:
        test_obj = CacheModule()
    except Exception as e:
        assert type(e) == TypeError
        assert str(e) == "Can't instantiate abstract class CacheModule with abstract methods get, get_multi, keys, set"

    # test 2
    class CacheModule():
        DEFAULT_MEMCACHE_PORT = None
        DEFAULT_MEMCACHE_HOST = None

        def __init__(self):
            self.plugin_name = "jsonfile"
            self._connection = None

        def get(self, host, variable):
            pass

        def set(self, host, variable, value, expire=None):
            pass

        def keys(self, host):
            pass

        def get_multi(self, host, variables):
            pass


# Generated at 2022-06-13 11:30:05.415962
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Run the constructor
    cache = CacheModule()

    # Test the type of the object
    assert isinstance(cache, CacheModule)


# Generated at 2022-06-13 11:30:06.152298
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache

# Generated at 2022-06-13 11:30:07.091235
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.name == 'jsonfile'

# Generated at 2022-06-13 11:30:11.451279
# Unit test for constructor of class CacheModule
def test_CacheModule():
    tmp_path = './'
    cm = CacheModule({'_uri': tmp_path,
                     '_timeout': 60,
                     '_prefix': 'test'})
    assert cm._connection == tmp_path
    assert cm._timeout == 60
    assert cm._prefix == 'test'
    assert cm._cache_dir == os.path.join(tmp_path, 'test')
    assert cm._load_cache == cm._load
    assert cm._dump_cache == cm._dump

# Generated at 2022-06-13 11:30:13.289679
# Unit test for constructor of class CacheModule
def test_CacheModule():
    ''' This function will test the constructor of class CacheModule'''
    test = CacheModule()

# Generated at 2022-06-13 11:30:16.359171
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._prefix == 'ansible-cache'
    assert c._timeout == 86400


# Generated at 2022-06-13 11:30:28.668964
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

    # Test variables
    cache_module.set_options(task_vars=dict())
    cache_module._timeout = 86400
    cache_module._prefix = "ansible"
    cache_module._uri = "/etc/ansible/facts"
    cache_module._connection = "/etc/ansible/facts"
    cache_module.validate_options()

    # Test module
    assert cache_module._timeout == 86400
    assert cache_module._prefix == "ansible"
    assert cache_module._uri == "/etc/ansible/facts"
    assert cache_module._connection == "/etc/ansible/facts"


# Generated at 2022-06-13 11:30:30.464359
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}, '/tmp').cachedir == '/tmp'

# Generated at 2022-06-13 11:30:38.631385
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''
    constructor test
    '''
    cache_mod = CacheModule()
    assert cache_mod._load is not None
    assert cache_mod._dump is not None

# Generated at 2022-06-13 11:30:40.342846
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.file_extension == '.json'

# Generated at 2022-06-13 11:30:43.237456
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Initialize an instance of class CacheModule
    cacheModule = CacheModule()

    # Ensure that CacheModule() successfully returns an instance of class CacheModule
    assert isinstance(cacheModule, CacheModule)

# Generated at 2022-06-13 11:30:46.054430
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.encoding in ['utf-8', 'utf-8-sig']
    assert cm.decoder is AnsibleJSONDecoder
    assert cm.encoder is AnsibleJSONEncoder

# Generated at 2022-06-13 11:30:51.260566
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create object for class CacheModule
    # and when object is created call the constructor
    cm = CacheModule()
    # Print the object as json str
    print(json.dumps(cm, default=lambda o: o.__dict__,
                     sort_keys=True, indent=4))

    # Print the doc of the class
    print(CacheModule.__doc__)


if __name__ == '__main__':
    # Unit testing
    test_CacheModule()

# Generated at 2022-06-13 11:30:52.438589
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert True

# Generated at 2022-06-13 11:30:53.247148
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:56.470014
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._load == CacheModule._load
    assert cache._dump == CacheModule._dump

# Generated at 2022-06-13 11:31:00.810604
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert obj.get_timeout() == 86400
    assert obj.get_prefix() == 'ansible-cache'
    assert obj.get_connection() == '~/.ansible/cache'

# Generated at 2022-06-13 11:31:05.666513
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = 'test_uri'
    prefix = 'test_prefix'
    ttl = '123456789'
    cache = CacheModule(uri, prefix, ttl)
    # test whether the cache module is initialized with the correct parameters
    assert cache.plugin_name == 'jsonfile'
    assert cache.plugin_path == '_uri'
    assert cache.timeout == '123456789'

# Generated at 2022-06-13 11:31:15.137726
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Pass a fake filename to the constructor for the class CacheModule,
    create a real instance, and return it."""

    filename = "myfactcache.json"
    cm = CacheModule(filename)
    return cm

# Generated at 2022-06-13 11:31:21.062159
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module_args = {
        "_uri": "./ansible_facts.d",
        "_prefix": "localhost",
        "_timeout": 86400
    }
    x = CacheModule(module_args)
    assert x.cachefile == "./ansible_facts.d/localhost/ansible_facts.cache"
    assert x.timeout == 86400

# Generated at 2022-06-13 11:31:26.529429
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule('/test/test', '/test/test/test')

# Unit test fot function _load
#def test_load():
#    cache = CacheModule('/test/test', '/test/test/test')
#    cache._load('/test/test')

# Unit test fot function _dump

# Generated at 2022-06-13 11:31:29.569705
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m.cache_dir == ''
    assert m.prefix == 'ansible-factcache'
    assert m._timeout == 86400
    assert m.content == {}

# Generated at 2022-06-13 11:31:31.020854
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.get_timeout() == 86400

# Generated at 2022-06-13 11:31:32.722934
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    print('Plugin is used to cache data to json file')
    print(plugin)

# Generated at 2022-06-13 11:31:41.361206
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test with different urls
    CacheModule(dict(
        _uri='/tmp/'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='/'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='//'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='///'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='/tmp/'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='/tmp/'
    ))

    # Test with different urls
    CacheModule(dict(
        _uri='/tmp/'
    ))

    # Test with different urls

# Generated at 2022-06-13 11:31:42.851911
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = {}
    a = CacheModule(a)
    assert isinstance(a, CacheModule)


# Generated at 2022-06-13 11:31:44.556455
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test the constructor
    c = CacheModule()
    assert c != None
    assert c.plugin != None


# Generated at 2022-06-13 11:31:46.686477
# Unit test for constructor of class CacheModule
def test_CacheModule():
    directory = "some_directory"
    timeout = 60
    prefix = "some_prefix"
    json_cache = CacheModule(directory, timeout, prefix)
    assert json_cache._connection is directory
    assert json_cache._timeout is timeout
    assert json_cache._prefix is prefix

# Generated at 2022-06-13 11:31:59.223286
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert isinstance(obj, CacheModule)

# Generated at 2022-06-13 11:32:01.932320
# Unit test for constructor of class CacheModule
def test_CacheModule():
    arguments = {'_uri': '/tmp/ansible_test/', '_prefix': 'test_prefix', '_timeout': 10}
    cache_plugin = CacheModule(**arguments)

    assert isinstance(cache_plugin, CacheModule)

# Generated at 2022-06-13 11:32:02.969137
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache=CacheModule()
    assert cache

# Generated at 2022-06-13 11:32:04.031338
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule is not None

# Generated at 2022-06-13 11:32:07.184274
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Verify CacheModule instance is created
    """
    module = CacheModule()
    assert isinstance(module, CacheModule)
    assert module._load == CacheModule._load
    assert module._dump == CacheModule._dump

# Generated at 2022-06-13 11:32:15.544857
# Unit test for constructor of class CacheModule
def test_CacheModule():

    import os

    test_dir = '/tmp/ansible_test_json_fact_cache'
    cache_path = os.path.join(test_dir, 'test_host.json')

    # Create the test directory.
    os.mkdir(test_dir)

    test_value = {'foo': 'bar'}

    module = CacheModule()
    assert module._load(cache_path) == {}
    module._dump(test_value, cache_path)
    assert module._load(cache_path) == test_value

    # Clean up
    os.remove(cache_path)
    os.rmdir(test_dir)

# Generated at 2022-06-13 11:32:17.839129
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert isinstance(cache_plugin, CacheModule), 'Expected CacheModule to be an instance of CacheModule, but it was not.'

# Generated at 2022-06-13 11:32:18.806333
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule('')
    assert isinstance(c, CacheModule)

# Generated at 2022-06-13 11:32:23.123273
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = 'default'
    timeout = 86400
    prefix = 'cachefile'
    _uri = '/tmp/'

    cache = CacheModule(connection, timeout, prefix, _uri)
    assert cache.timeout == 86400
    assert cache.prefix == 'cachefile'
    assert cache._base_dir == '/tmp/'


# Generated at 2022-06-13 11:32:27.184071
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = '/tmp/ansible-cache'
    prefix = 'ansible_cache_'
    timeout = 123
    cache_module = CacheModule(path, prefix, timeout)
    assert cache_module._connection.dir == path
    assert cache_module._connection.prefix == prefix
    assert cache_module._timeout == timeout

# Generated at 2022-06-13 11:32:52.751012
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert isinstance(cache_module, CacheModule)

# Generated at 2022-06-13 11:32:54.456215
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm

# Generated at 2022-06-13 11:32:55.988712
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass


# Generated at 2022-06-13 11:33:03.446349
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = "cache_dir"
    timeout = 10

    configuration.setting = MagicMock(return_value=cache_dir)

    cache = CacheModule(timeout)
    assert cache.file_extension == '.json'
    assert cache.cache_dir == cache_dir
    assert cache.timeout == timeout



# Generated at 2022-06-13 11:33:08.192637
# Unit test for constructor of class CacheModule
def test_CacheModule():
    inputs = {
        "_prefix": "",
        "_timeout": 60,
        "_uri": "/tmp/"
    }

    test_object = CacheModule(inputs)
    assert test_object._timeout == 60
    assert test_object._prefix == ""
    assert test_object._basedir == "/tmp/"
    assert test_object._plugin_name == "jsonfile"
    assert test_object._per_host == True

# Generated at 2022-06-13 11:33:09.414794
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule('') is not None

# Generated at 2022-06-13 11:33:20.340968
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test with default args
    cache = CacheModule()
    assert cache._connection == ''
    assert cache._timeout == 86400
    assert cache._prefix == ''

    # Test with '/foo/bar' as cache directory
    connection = '/foo/bar'
    cache = CacheModule(connection=connection)
    assert cache._connection == connection
    assert cache._timeout == 86400
    assert cache._prefix == ''

    # Test with 10 as timeout
    timeout = 10
    cache = CacheModule(timeout=timeout)
    assert cache._connection == connection
    assert cache._timeout == timeout
    assert cache._prefix == ''

    # Test with 'ansible-cache-' as prefix
    prefix = 'ansible-cache-'
    cache = CacheModule(prefix=prefix)
    assert cache._connection == connection
    assert cache._timeout == timeout

# Generated at 2022-06-13 11:33:20.977670
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}) is not None

# Generated at 2022-06-13 11:33:22.397578
# Unit test for constructor of class CacheModule
def test_CacheModule():
    result = CacheModule()
    assert isinstance(result, BaseFileCacheModule)

# Generated at 2022-06-13 11:33:23.325743
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module

# Generated at 2022-06-13 11:34:14.794035
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, CacheModule)

# Generated at 2022-06-13 11:34:19.447111
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    # Test for cache path
    assert cache._connection is None, "cache._connection was not reset to its default value"
    # Test for cache expiration in seconds
    assert cache._timeout == 86400, "cache._timeout was not reset to its default value"
    # Test for filename extension
    assert cache._extension == 'json', "cache._extension was not reset to its default value"

# Generated at 2022-06-13 11:34:22.716252
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._connection is None
    assert cm._timeout == 86400
    assert cm._plugin_name == 'jsonfile'
    assert cm._load_cache is None
    assert cm._dump_cache is None

# Generated at 2022-06-13 11:34:23.681713
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # create a CacheModule object
    x = CacheModule()

# Generated at 2022-06-13 11:34:24.274458
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()

# Generated at 2022-06-13 11:34:25.335519
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:34:27.008725
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._load == 'undefined'
    assert cm._dump == 'undefined'

# Generated at 2022-06-13 11:34:34.981804
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cachePlugin = CacheModule(None)
    assert cachePlugin.get_cache_path() == "/tmp/ansible-cachedir"
    assert cachePlugin.has_expired is True
    assert cachePlugin.timeout == 86400
    assert cachePlugin.prefix == "ansible_facts_"
    assert cachePlugin._cache_lock is False
    assert hasattr(cachePlugin, 'dir_name')
    assert hasattr(cachePlugin, 'dir_path')
    assert cachePlugin.dir_name == "ansible_facts"
    assert cachePlugin.dir_path == "/tmp/ansible-cachedir/ansible_facts"


# Generated at 2022-06-13 11:34:42.200714
# Unit test for constructor of class CacheModule

# Generated at 2022-06-13 11:34:46.409387
# Unit test for constructor of class CacheModule
def test_CacheModule():
    #Create instance of CacheModule class
    assert isinstance(CacheModule, type)
    #Check if CacheModule is an instance of BaseFileCacheModule
    assert isinstance(CacheModule(), BaseFileCacheModule)

# Generated at 2022-06-13 11:36:40.241822
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:36:44.340528
# Unit test for constructor of class CacheModule
def test_CacheModule():
    file_system_path = 'Ansible_test_file'
    cache = CacheModule(file_system_path)
    assert cache.file_system_path == file_system_path
    cache.get('')
    cache.set('', '')

# Generated at 2022-06-13 11:36:46.065609
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin


# Generated at 2022-06-13 11:36:48.308620
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin._prefix.startswith('ansible_facts')

# Generated at 2022-06-13 11:36:52.340863
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._prefix == 'ansible-factcache'
    assert cache._timeout == 86400
    assert cache._load == CacheModule._load
    assert cache._dump == CacheModule._dump

# Generated at 2022-06-13 11:36:53.395319
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._load('/') is None
    cache._dump('', '/')

# Generated at 2022-06-13 11:36:55.077883
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule('/path/to/cache', {}).connection == '/path/to/cache'
    assert CacheModule('/path/to/cache', {'_prefix':'something'})._prefix == 'something'

# Generated at 2022-06-13 11:36:59.008946
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._load("filename") == json.load(open("filename", 'r'), cls=AnsibleJSONDecoder)
    assert c._dump("value", "filename") == json.dump("value", open("filename", 'w'), cls=AnsibleJSONEncoder, sort_keys=True, indent=4)
    assert c._sanitize_dict({"test": "value", ".test": "nope"}) == {"test": "value"}
    assert c._sanitize_dict({"test": "value", "_test": "nope"}) == {"test": "value"}

# Generated at 2022-06-13 11:37:09.946051
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import tempfile
    import os
    import shutil
    import datetime
    import time
    import stat

    # Create temporary working directory
    tmp_dir = tempfile.mkdtemp()

    # Construct CacheModule
    cache = CacheModule()
    cache._config_path = tmp_dir
    cache._prefix = cache._config_path + os.sep + cache.path_sep

    # Test get_set_cache method
    cache.get_set_cache('1', 'test')
    cache_file = cache._prefix + '1.cache'
    # Test get_cache method
    assert cache.get_cache('1') == 'test'
    # Test set_cache method
    cache.set_cache('1', 'test1')
    assert cache.get_cache('1') == 'test1'
    # Test _

# Generated at 2022-06-13 11:37:19.438453
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_id = 'test_id'
    cache_plugin_host = 'test_host'
    cache_plugin_vars = {'test_key': 'test_value'}
    cache_plugin_path = 'test_path'
    cache_plugin_timeout = 10
    cache_plugin_prefix = 'test_prefix'

    cache_plugin = CacheModule(
        plugin_id=cache_plugin_id,
        host=cache_plugin_host,
        vars=cache_plugin_vars,
        path=cache_plugin_path,
        timeout=cache_plugin_timeout,
        prefix=cache_plugin_prefix
    )

    assert cache_plugin.plugin_id == cache_plugin_id
    assert cache_plugin.host == cache_plugin_host
    assert cache_plugin.vars == cache_plugin