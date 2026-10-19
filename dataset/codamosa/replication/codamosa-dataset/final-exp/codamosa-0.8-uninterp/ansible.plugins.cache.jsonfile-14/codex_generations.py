

# Generated at 2022-06-13 11:29:19.201240
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None
    assert bool(cache_module.get_options())
    assert bool(cache_module.get_option('_uri'))

# Generated at 2022-06-13 11:29:21.117121
# Unit test for constructor of class CacheModule
def test_CacheModule():

    module = CacheModule()
    assert isinstance(module, CacheModule)
    assert module._connection.get('_uri') == '/tmp/ansible-cachedir'

# Generated at 2022-06-13 11:29:22.403016
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin

# Generated at 2022-06-13 11:29:23.968518
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c != None

# Generated at 2022-06-13 11:29:27.880760
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert isinstance(cache_plugin.get_cache_timeout(), int), "get_cache_timeout() returns integer value"


# Generated at 2022-06-13 11:29:41.713941
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''
    Test case for CacheModule constructor.
    '''
    # When: object is created
    cachemodule = CacheModule()

    # Then: should return a CacheModule object
    assert isinstance(cachemodule, CacheModule)

    # And: object should have expected attribute values
    assert cachemodule._plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:29:43.500400
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert type(obj) == CacheModule
    #assert obj.__class__ == CacheModule

# Generated at 2022-06-13 11:29:45.856260
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._load != None
    assert cache_module._dump != None

# Generated at 2022-06-13 11:29:47.292314
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule

    assert CacheModule._load({}, 'filepath') == None

# Generated at 2022-06-13 11:29:49.199422
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    # Check if plugin is compatible with this version of Ansible
    assert cm.has_plugin_dependencies

# Generated at 2022-06-13 11:29:52.447259
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # TODO: Write me
    pass

# Generated at 2022-06-13 11:29:54.610006
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.file_extension == '.json'

# Generated at 2022-06-13 11:29:55.207666
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:30:04.068498
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()

# Generated at 2022-06-13 11:30:05.683514
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict(
        config_path='data',
        timeout=300
    ))

# Generated at 2022-06-13 11:30:08.591618
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(dict(uri='/some/directory', _prefix='some_prefix'))
    assert cache.directory == '/some/directory'
    assert cache.prefix == 'some_prefix'
    assert cache.ext == '.json'

# Generated at 2022-06-13 11:30:10.186659
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("Testing loading of ansible.plugins.cache.jsonfile")
    yaml_cache = CacheModule()
    print(yaml_cache.__dict__)

# Generated at 2022-06-13 11:30:19.182078
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({ '_uri': '/tmp/ansible_fact_cache' })

    assert cache._get_cache_basedir() == '/tmp/ansible_fact_cache', \
    '_get_cache_basedir is invalid'

    assert cache._load('/tmp/ansible_fact_cache/host1') == None, \
    '_load is invalid'

    cache.set('host1', 'ansible_user', 'brian')
    assert cache._load('/tmp/ansible_fact_cache/host1') == { 'ansible_user': 'brian' }, \
    '_load is invalid'

    cache.set('host1', 'ansible_user', 'brian')

# Generated at 2022-06-13 11:30:20.028123
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({})


# Generated at 2022-06-13 11:30:22.324628
# Unit test for constructor of class CacheModule
def test_CacheModule():
    my_CacheModule = CacheModule()
    assert my_CacheModule._timeout == 86400
    assert my_CacheModule._prefix is None
    assert my_CacheModule._uri is not None

# Generated at 2022-06-13 11:30:33.864017
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin.cache_version == 1
    assert cache_plugin._load == CacheModule._load
    assert cache_plugin._dump == CacheModule._dump
    assert cache_plugin.get_cache_dir() == "/tmp/ansible-cached-facts/"
    assert cache_plugin.get_cache_filename("test.test.test") == "/tmp/ansible-cached-facts/test.test.test"
    assert cache_plugin.get_cache_max_age() == 86400
    assert cache_plugin.get_cache_prefix() == "ansible_fact_cache_"
    assert cache_plugin.get_cache_timeout() == 86400
    assert cache_plugin.get_cache_update_cachefile() == False

# Generated at 2022-06-13 11:30:35.037500
# Unit test for constructor of class CacheModule
def test_CacheModule():    
    print('Testing CacheModule constructor...')    
    cache_plugin = CacheModule()

# Generated at 2022-06-13 11:30:42.380534
# Unit test for constructor of class CacheModule
def test_CacheModule():
    query_module = CacheModule()

    assert query_module.set_options is None
    assert query_module.get_options is None
    assert query_module.flush_options is None
    assert query_module.delete_options is None
    assert query_module.keys_options is None
    assert query_module.has_option('path')
    assert query_module.get_option('path') == '/tmp/ansible_facts'
    assert query_module.has_option('timeout')
    assert query_module.get_option('timeout') == 3600

# Generated at 2022-06-13 11:30:43.566489
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict()) != None

# Generated at 2022-06-13 11:30:44.942823
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert(cm._timeout == 86400)

# Generated at 2022-06-13 11:30:49.063869
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    print(obj._load)
    print(obj._dump)
    print(obj._uri)
    print(obj._prefix)
    print(obj._timeout)
    print(obj)

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:30:50.789485
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module is not None

# Generated at 2022-06-13 11:31:01.123743
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_m = CacheModule()
    assert cache_m._get_cache('/Users/chandan/workspace/ansible_1_9/plugins/cache/tmp/ansible-cache-chandankumarjha') == {'_timeout': 86400}
    assert cache_m._load('/Users/chandan/workspace/ansible_1_9/plugins/cache/tmp/ansible-cache-chandankumarjha/facts_chandankumarjha.json') == {'uptime_seconds': 17063}



# Generated at 2022-06-13 11:31:08.162198
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._load_cache_plugin_options(dict()) == False
    assert cache._load_cache_plugin_options(dict({
        '_prefix': 'test_cache',
        '_timeout': 60,
        '_uri': '/tmp/ansible-test-cache'
    })) == True
    assert cache._load_cache_plugin_options(dict({
        '_prefix': 'test_cache',
        '_timeout': 60,
    })) == False
    assert cache._load_cache_plugin_options(dict({
        '_prefix': 'test_cache',
        '_uri': '/tmp/ansible-test-cache',
    })) == False

# Generated at 2022-06-13 11:31:09.193425
# Unit test for constructor of class CacheModule
def test_CacheModule():
	module = CacheModule({}, {})
	assert True

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:31:21.062626
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()

    # _load not implemented yet
    try:
        module._load('test')
        assert(False)
    except NotImplementedError:
        assert(True)

    # _dump not implemented yet
    try:
        module._dump('test', 'test')
        assert(False)
    except NotImplementedError:
        assert(True)

# Generated at 2022-06-13 11:31:27.202531
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._prefix == ''
    assert cache_module._timeout == 86400
    assert cache_module.get_cache_size() == 0
    assert cache_module.get_max_cache_size() == 0
    assert cache_module.get_cache_size_limit() == 0
    assert cache_module.get_cache_timeout() == 86400


# Generated at 2022-06-13 11:31:29.569100
# Unit test for constructor of class CacheModule
def test_CacheModule():
  a=CacheModule()
  a.set('filename',{'hello':'world'})
  b=a.get('filename')
  print (b)

# Generated at 2022-06-13 11:31:34.332252
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    file_name="CACHE_PLUGIN_TEST"
    file_path = os.path.join('temp',file_name)
    cache = CacheModule()
    cache._uri = file_path
    cache._timeout = 0
    cache._prefix = ''
    cache._connection = cache
    data = cache._load_data() #Should load the data from file_path
    assert (data == {})
    data = [{'a':5, 'b':6}]
    cache._dump_data(data)
    data2 = cache._load_data() #Should load the data from file_path
    assert (data == data2)
    #Now deleting the file
    os.remove(file_path)

# Generated at 2022-06-13 11:31:42.262210
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = __file__
    my_CacheModule = CacheModule(filename)
    assert my_CacheModule is not None
    assert my_CacheModule.plugin_name == 'jsonfile'
    assert my_CacheModule.cachefile_extension == 'json'
    assert my_CacheModule.cache_lockfile_timeout == 1
    assert my_CacheModule.cache_timeout == 86400
    assert my_CacheModule.cache_max_age == -1
    assert my_CacheModule.cache_expiration_interval == 3600
    assert my_CacheModule.cache_basedir == 'fact_caching_connection'
    assert my_CacheModule.cache_prefix == 'fact_caching_prefix'
    assert my_CacheModule.cache_tmp_dir is None

# Generated at 2022-06-13 11:31:43.696469
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule('test', 'test-prefix', 'test-directory', 1)


# Generated at 2022-06-13 11:31:44.884869
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cls = CacheModule({})
    assert cls.get_timeout() == 86400

# Generated at 2022-06-13 11:31:48.114729
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule(None)
    assert isinstance(cache_module, CacheModule)
    assert cache_module._timeout == 86400
    assert cache_module._prefix == ''

# Generated at 2022-06-13 11:31:52.949049
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c=CacheModule()
    assert c._prefix == 'ansible_facts'
    assert c._timeout == 86400
    assert c._dump(None, None) is None
    assert c._load(None, None) is None
    #assert c.get("key") is None
    assert c.set("key", "value") is None

# Generated at 2022-06-13 11:31:54.622749
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._load == CacheModule._load
    assert module._dump == CacheModule._dump

# Generated at 2022-06-13 11:32:08.285956
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule({
        '_uri': '',
        '_prefix': '',
        '_timeout': '',
    })
    assert cache_module is not None

# Generated at 2022-06-13 11:32:15.545096
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module_obj = CacheModule(None, {}, *[], **{})
    print(cache_module_obj._load(('/home/asus/GitDev/ansible/test/units/modules/test_ansible_module_json_file.json')))
    #cache_module_obj._load(('/home/asus/GitDev/ansible/test/units/modules/test_ansible_module_json_file.json'))

if __name__ == "__main__":
    test_CacheModule()

# Generated at 2022-06-13 11:32:16.077526
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:32:17.529945
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert isinstance( cache_plugin, CacheModule)
    assert isinstance( cache_plugin, BaseFileCacheModule)

# Generated at 2022-06-13 11:32:25.878941
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Unit test for constructor with parameter uri
    cache_module = CacheModule(uri='/tmp/ansible_cache')
    assert cache_module._connection is None
    assert cache_module._timeout == 3600
    assert cache_module._prefix == 'ansible-local'
    assert cache_module._load_cache() == dict()

    # Unit test for constructor with parameter uri, timeout, prefix
    cache_module2 = CacheModule(uri='/tmp/ansible_cache', timeout=60, prefix='prefix')
    assert cache_module2._connection == '/tmp/ansible_cache'
    assert cache_module2._timeout == 60
    assert cache_module2._prefix == 'prefix'
    assert cache_module2._load_cache() == dict()


# Generated at 2022-06-13 11:32:28.705366
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert (obj._load('/tmp/obj.json') == 'value')
    assert (obj._dump('value', '/tmp/obj.json') == None)

# Generated at 2022-06-13 11:32:31.250149
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin

    cache_plugin_init = CacheModule(task_vars=dict())
    assert cache_plugin_init

# Generated at 2022-06-13 11:32:36.890439
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test when not all parameter are given
    cache_module = CacheModule('/path/to/file')
    # Test default values
    assert cache_module.get_option('_timeout') == 86400
    assert cache_module.get_option('_prefix') == 'ansible_facts_'
    assert cache_module._cache == '/path/to/file/ansible_facts_'

# Generated at 2022-06-13 11:32:39.365849
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Testing the constructor of the class CacheModule
    cache_module = CacheModule()
    # In this case we only test if the object is created
    assert isinstance(cache_module, CacheModule)

# Generated at 2022-06-13 11:32:45.110769
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Set the required env variables for class CacheModule to run
    import os
    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = "/tmp/ansible/cache"
    os.environ['ANSIBLE_CACHE_PLUGIN_TIMEOUT'] = "60"

    cache_mod = CacheModule()
    assert cache_mod.get('host', 'data') is None

# Generated at 2022-06-13 11:33:08.938070
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin._load == CacheModule._load
    assert cache_plugin._dump == CacheModule._dump

# Generated at 2022-06-13 11:33:10.283748
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.cache_type == 'jsonfile'

# Generated at 2022-06-13 11:33:14.099204
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.__module__ == 'ansible.plugins.cache.jsonfile'
    assert cache_module._timeout == 86400
    assert cache_module._cache_dir is None
    assert cache_module._cache_prefix == ''

# Generated at 2022-06-13 11:33:14.818171
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

# Generated at 2022-06-13 11:33:20.342440
# Unit test for constructor of class CacheModule
def test_CacheModule():
    my_path = "my/path"
    my_prefix = "my_prefix"
    my_timeout = 123

    cache = CacheModule()

    cache._uri = my_path
    cache._prefix = my_prefix
    cache._timeout = my_timeout

    assert cache._uri == my_path
    assert cache._prefix == my_prefix
    assert cache._timeout == my_timeout

# Generated at 2022-06-13 11:33:23.198096
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # _uri required
    # _prefix
    # _timeout
    cm = CacheModule()
    assert cm._timeout == 86400
    assert cm._prefix is None
    assert cm._uri is None

# Generated at 2022-06-13 11:33:24.401363
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin

# Generated at 2022-06-13 11:33:27.005247
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    testcase_defaults = {
        '_uri': '/tmp/ansible-test-facts',
        '_prefix': None,
        '_timeout': 86400,
    }
    assert module.get_options() == testcase_defaults, "Options defaults not matching"

# Generated at 2022-06-13 11:33:27.753965
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule('/tmp')

# Generated at 2022-06-13 11:33:31.561544
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c1 = CacheModule()
    c2 = CacheModule(basedir='/tmp/')
    c3 = CacheModule(basedir='/tmp/', timeout=3600)

# Generated at 2022-06-13 11:34:22.007105
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()
    print("Unit test for cache plugin jsonfile:", cacheModule)

# Generated at 2022-06-13 11:34:26.804184
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test with bogus _uri
    c = CacheModule({'_uri': 'bogus', '_prefix': 'bogus'})
    assert c._uri == ''

    # Test with bogus _prefix
    c = CacheModule({'_uri': 'bogus', '_prefix': 'bogus'})
    assert c._prefix == 'bogus'

# Generated at 2022-06-13 11:34:27.805233
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), CacheModule)

# Generated at 2022-06-13 11:34:29.448399
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._cache is None

# Generated at 2022-06-13 11:34:38.446570
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = '/tmp/cache/file'
    cache = CacheModule()
    cache_plugin_timeout = cache._get_cache_plugin_timeout()
    assert cache._cache_plugin_timeout == cache_plugin_timeout

    # test if the default value is returned if plugin_timeout is not set
    assert cache._get_cache_plugin_timeout() is None

    # test if the correct value is returned if plugin_timeout is set
    cache.set_options(timeout=cache_plugin_timeout)
    assert cache._get_cache_plugin_timeout() == cache_plugin_timeout

    # test if the value is correctly set when _load is called
    cache._load(filename)
    assert cache.get(filename) == cache.get(filename)

    # test if the value is correctly set when _dump is called
    cache._dump(filename, filename)


# Generated at 2022-06-13 11:34:40.560786
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # create an instance
    am = CacheModule()
    # assert __init__ method
    assert isinstance(am, CacheModule)

# Generated at 2022-06-13 11:34:42.979359
# Unit test for constructor of class CacheModule
def test_CacheModule():
  print('inside of test_CacheModule')
  cache_module = CacheModule()
  print(cache_module.__doc__)

# Generated at 2022-06-13 11:34:46.052549
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''
    Unit test for constructor of class CacheModule
    '''
    cache = CacheModule()
    assert cache.get_basedir() is None

# Generated at 2022-06-13 11:34:51.073609
# Unit test for constructor of class CacheModule
def test_CacheModule():
  # Create a new instance of the CacheModule class
  cm = CacheModule("/tmp", "fact", 3600)
  assert cm._timeout == 3600
  assert cm._connection == "/tmp"
  assert cm._prefix == "fact"
test_CacheModule()

# Generated at 2022-06-13 11:34:53.035062
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module=CacheModule()
    cache_module._Connection__uri='/home/test/.ansible/cache/ansible-fact'
    assert cache_module._Connection__uri=='/home/test/.ansible/cache/ansible-fact'

# Generated at 2022-06-13 11:36:44.100239
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(None) is not None

# Generated at 2022-06-13 11:36:54.252285
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # This test won't run with py3.4 because the constructor of BaseFileCacheModule
    # uses super() which is not supported by unittest.mock.patch in py3.4

    from unittest import TestCase
    from unittest.mock import patch, MagicMock

    class Test(TestCase):
        def __init__(self, *args, **kwargs):
            super(Test, self).__init__(*args, **kwargs)
            self.uri = '/path/to/facts'
            self.prefix = 'plugin'
            self.timeout = 3600

        def test_CacheModule(self, *args, **kwargs):
            with patch('ansible.plugins.cache.BaseFileCacheModule._init_cache_dir'):
                CacheModule(self.uri, self.prefix, self.timeout)


# Generated at 2022-06-13 11:36:58.099757
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Arrange
    cache_plugin_connection = './file/path'
    cache_plugin_timeout = 100

    # Act
    cache_module_instance = CacheModule(
        cache_plugin_connection=cache_plugin_connection,
        cache_plugin_timeout=cache_plugin_timeout
    )

    # Assert
    assert cache_module_instance
    assert cache_module_instance._cache_path == cache_plugin_connection
    assert cache_module_instance._timeout == cache_plugin_timeout/86400

# Generated at 2022-06-13 11:37:01.146068
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.get_timeout() == 86400
    assert callable(cache.get_connect_info()['connector'])
    assert callable(cache.get_connect_info()['conn_func'])

# Generated at 2022-06-13 11:37:01.794425
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule

# Generated at 2022-06-13 11:37:09.090101
# Unit test for constructor of class CacheModule
def test_CacheModule():
    data_dir = '/tmp'
    plugin = 'jsonfile'
    timeout = 86400
    prefix = 'ansible_facts'

    plugin_options = {
        '_prefix': prefix,
        '_timeout': timeout,
        '_uri': data_dir
    }

    cache = CacheModule()
    cache.set_plugin_options(plugin_options)
    assert cache.data_dir == data_dir
    assert cache.plugin == plugin
    assert cache.timeout == timeout
    assert cache.prefix == prefix

# Generated at 2022-06-13 11:37:11.025705
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m is not None

# Make sure that constructor of class CacheModule works
m = CacheModule()

# Generated at 2022-06-13 11:37:17.131967
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filepath = '/root/ansible/test/'
    fact_caching_connection = 'filepath'
    fact_caching_timeout = 86400
    fact_caching_prefix = 'myprefix'
    my_instance = CacheModule(fact_caching_connection, fact_caching_timeout, fact_caching_prefix)
    assert my_instance.filepath == filepath
    assert my_instance.timeout == 86400
    assert my_instance.prefix == "myprefix"

# Generated at 2022-06-13 11:37:18.385611
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert(x._timeout == 86400)

# Generated at 2022-06-13 11:37:21.112247
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''Test for class CacheModule'''
    obj = CacheModule(task=None)
    assert obj._options == dict(
        _prefix='ansible-factcache', _timeout=86400, _uri='/tmp/ansible-factcache')