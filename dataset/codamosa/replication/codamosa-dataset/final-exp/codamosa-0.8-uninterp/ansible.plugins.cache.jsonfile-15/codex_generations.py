

# Generated at 2022-06-13 11:29:16.701992
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()

# Generated at 2022-06-13 11:29:19.351258
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module_mock = Mock()
    CacheModule(module_mock)
    module_mock.fail_json.assert_not_called()


# Generated at 2022-06-13 11:29:21.862586
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()
    assert cacheModule._cache_files_dir == "/tmp/ansible_batavi_payments_cache"

# Generated at 2022-06-13 11:29:25.182868
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._connection is None
    assert c._prefix is None
    assert c._timeout == 86400

# Generated at 2022-06-13 11:29:26.632127
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)

# Generated at 2022-06-13 11:29:33.445197
# Unit test for constructor of class CacheModule
def test_CacheModule():
    options = {
        "_uri": "/path/to/the/cache/dir",
        "_prefix": "ansible_test-poiuytrewq1234567890",
        "_timeout": 100
    }

    cache = CacheModule(None, options)
    assert cache
    assert cache.options == options


# Generated at 2022-06-13 11:29:35.027684
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mod = CacheModule()
    assert mod is not None

# Generated at 2022-06-13 11:29:38.675778
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # test with empty params
    cm = CacheModule()
    assert cm is not None

# vim: set ts=4 sw=4 et:

# Generated at 2022-06-13 11:29:43.760462
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a path for unit test
    path = '/tmp/test.json'
    # Create a CacheModule object
    cache = CacheModule(path)
    # Test the __init__ function
    assert cache.get_basedir() == path
    # Test the _load function
    value = {'a': 'b'}
    cache._dump(value, path)
    assert cache._load(path) == value
    # Test the _dump function
    value = {'b': 'c'}
    cache._dump(value, path)
    assert cache._load(path) == value

# Generated at 2022-06-13 11:29:46.778530
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin.get_prefix() == 'ansible-fact'
    assert cache_plugin.get_timeout() == 86400

# Generated at 2022-06-13 11:29:54.274713
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin._load("/tmp/hosts.json") is None
    assert plugin._dump("", "/tmp/hosts.json") is None

# Generated at 2022-06-13 11:29:54.963303
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert True

# Generated at 2022-06-13 11:29:56.765544
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert '/tmp/ansible-fact-cache' == cache.cache_dir

# Generated at 2022-06-13 11:29:58.770225
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m._connection == {}
    assert m._timeout == 86400
    assert m._prefix == ''

# Generated at 2022-06-13 11:30:06.628631
# Unit test for constructor of class CacheModule

# Generated at 2022-06-13 11:30:07.302455
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Unit test for constructor of class CacheModule
    assert True

# Generated at 2022-06-13 11:30:12.865436
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_cache_dir = 'my_test_dir'
    test_cache_plugin_prefix = 'ansible_cache.json'
    test_cache_plugin_timeout = '60'
    test_cache_plugin_connection = test_cache_dir + '/' + test_cache_plugin_prefix

    cm = CacheModule({'_uri': test_cache_dir, '_prefix': test_cache_plugin_prefix, '_timeout': test_cache_plugin_timeout})

    assert cm._prefix == test_cache_plugin_prefix
    assert cm._timeout == 60
    assert cm._connection == test_cache_plugin_connection


# Generated at 2022-06-13 11:30:15.018606
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._timeout == 86400
    assert cm._prefix == ''
    assert cm._uri == ''

# Generated at 2022-06-13 11:30:18.926391
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule({
        '_prefix': 'prefix',
        '_timeout': 42,
        '_uri': 123
    })
    assert plugin._prefix == 'prefix'
    assert plugin._timeout == 42
    assert plugin._uri == 123

# Generated at 2022-06-13 11:30:21.509420
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule(None)
    assert isinstance(plugin, BaseFileCacheModule)
    assert not hasattr(plugin, '_load')
    assert not hasattr(plugin, '_dump')

# Generated at 2022-06-13 11:30:25.334568
# Unit test for constructor of class CacheModule
def test_CacheModule():
    conn = CacheModule()
    assert conn

# Generated at 2022-06-13 11:30:27.001764
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(isinstance(cache, CacheModule) == True)


# Generated at 2022-06-13 11:30:29.837839
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None
    assert cache._connection is None
    assert cache._prefix is None
    assert cache._timeout == 86400


# Generated at 2022-06-13 11:30:30.793183
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm

# Generated at 2022-06-13 11:30:32.181449
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module.cache_dir is not None

# Generated at 2022-06-13 11:30:32.700479
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:34.334788
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin._cache_prefix == 'ansible-factcache'


# Generated at 2022-06-13 11:30:35.816073
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None
    assert isinstance(cm, CacheModule)

# Generated at 2022-06-13 11:30:40.394240
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._timeout == 86400
    assert cache_module._connection == None
    assert cache_module._prefix == None
    assert cache_module._load('cache/dummy') == None
    assert cache_module._dump('some value', 'cache/dummy_test') == None

# Generated at 2022-06-13 11:30:44.074704
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = '/tmp'
    prefix = 'ansible-test'
    timeout = 900

    module = CacheModule(path, prefix, timeout)

    assert module._cachefile_prefix == 'ansible-test'
    assert module._cachefile_timeout == 900

# Generated at 2022-06-13 11:30:56.012216
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._plugin_name == "jsonfile"
    assert cache_module._load('test_file') == None
    cache_module._dump('test_value', 'test_file')
    assert cache_module._load('test_file') == 'test_value'

# Generated at 2022-06-13 11:31:01.884667
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert json.dumps(cache._load('testfile'), cls=AnsibleJSONEncoder, sort_keys=True, indent=4) == '{}'
    cache._dump('testvalue', 'testfile')
    assert cache._load('testfile') == 'testvalue'

# Generated at 2022-06-13 11:31:06.158260
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._load("/tmp/test.json") == json.load("/tmp/test.json", cls=AnsibleJSONDecoder)
    assert module._dump("{'a':'b'}", "/tmp/test2.json") == json.dumps("{'a':'b'}", cls=AnsibleJSONEncoder, sort_keys=True, indent=4)

# Generated at 2022-06-13 11:31:20.157796
# Unit test for constructor of class CacheModule
def test_CacheModule():
    class _CacheModule(CacheModule):
        """
        A caching module backed by ``json`` files.
        """

        def _load(self, filepath):
            # Valid JSON is always UTF-8 encoded.
            with codecs.open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f, cls=AnsibleJSONDecoder)

        def _dump(self, value, filepath):
            with codecs.open(filepath, 'w', encoding='utf-8') as f:
                f.write(json.dumps(value, cls=AnsibleJSONEncoder, sort_keys=True, indent=4))

    _CacheModule_obj = _CacheModule(None)
    assert(_CacheModule_obj != None)

# Generated at 2022-06-13 11:31:21.692879
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    # Should be None at this point
    assert cache.plugin_name is None

    # Call the super class constructor
    cache = CacheModule('jsonfile')
    # Should be 'jsonfile' at this point
    assert cache.plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:31:25.510692
# Unit test for constructor of class CacheModule
def test_CacheModule():
    def Test_Load():
        # Test loading of a JSON file
        pass

    def Test_Dump():
        # Test dumping of a JSON file
        pass

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:31:38.915174
# Unit test for constructor of class CacheModule
def test_CacheModule():
  options = {
    "_timeout": 86400,
    "_uri": "/tmp/test_CacheModule",
    "_prefix": "ansible-test",
  }

  cm = CacheModule(plugin_options=options)
  assert cm.plugin_options == options

  # call method _load
  cm._load("/tmp/test_CacheModule/ansible-test_localhost")

  # call method _dump
  cm._dump([], "/tmp/test_CacheModule/ansible-test_localhost")

  # call method get
  cm.get('localhost')

  # call method set
  cm.set('localhost', [])

  # call method keys
  cm.keys()

  # call method contains
  cm.contains('localhost')

# Generated at 2022-06-13 11:31:40.247404
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__bases__ == (BaseFileCacheModule,)

# Generated at 2022-06-13 11:31:42.357002
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    cls_attr = set(('_load', '_dump'))
    obj_attr = set(obj.__dict__)
    assert cls_attr.issubset(obj_attr)

# Generated at 2022-06-13 11:31:43.239216
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Dummy instantaition of the class
    _ = CacheModule(task=None)

# Generated at 2022-06-13 11:31:56.839966
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m._cachefile is None
    assert m._timeout == 86400
    assert m._prefix == 'ansible-facts'

# Generated at 2022-06-13 11:32:01.298706
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = '/home/example_uri'
    prefix = 'prefix'
    timeout = 3600
    cm = CacheModule(uri, prefix, timeout)
    assert cm._uri == '/home/example_uri/prefix'
    assert cm._prefix == 'prefix'
    assert cm._timeout == 3600

# Generated at 2022-06-13 11:32:05.777224
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule(task_vars = {'ansible_cache_plugin': 'jsonfile', 'ansible_cache_plugin_timeout': 86400, 'ansible_cache_plugin_connection': '/root', 'ansible_cache_plugin_prefix': 'abc'})
    assert 'abc' == module._prefix

# Generated at 2022-06-13 11:32:06.342116
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

# Generated at 2022-06-13 11:32:06.993164
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:32:08.000927
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}, "") is not None

# Generated at 2022-06-13 11:32:10.600697
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cM = CacheModule
    assert cM._load('filepath')
    assert cM._dump('value', 'filepath')

# Generated at 2022-06-13 11:32:12.000950
# Unit test for constructor of class CacheModule
def test_CacheModule():
   x = CacheModule()
   assert(x is not None)


# Generated at 2022-06-13 11:32:19.132160
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Arrange
    module_name = 'jsonfile'
    env_key = 'ANSIBLE_CACHE_PLUGIN'
    timeout_key = 'ANSIBLE_CACHE_PLUGIN_TIMEOUT'
    connection_key = 'ANSIBLE_CACHE_PLUGIN_CONNECTION'
    prefix_key = 'ANSIBLE_CACHE_PLUGIN_PREFIX'
    default_plugins_path = '/usr/lib/python3.6/site-packages/ansible/plugins/cache/'
    temp_dir = '/tmp/ansible-cache'

    # Act
    module = CacheModule(module_name,env_key, timeout_key, connection_key, prefix_key, default_plugins_path, temp_dir)
    # Assert
    assert module.module_name == module_name

# Generated at 2022-06-13 11:32:20.588192
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import tempfile
    import shutil

    path = tempfile.mkdtemp()
    cache = CacheModule({
        '_uri': path
    })
    shutil.rmtree(path)


# Generated at 2022-06-13 11:32:50.715888
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a CacheModule object
    cache_obj = CacheModule()

    # Assert file_prefix is set to 'ansible-fact'
    assert cache_obj._file_prefix == 'ansible-fact'


    # Assert _load method works
    cache_obj._load("../../plugins/cache/jsonfile.py")


# Generated at 2022-06-13 11:32:56.795259
# Unit test for constructor of class CacheModule
def test_CacheModule():
  result = CacheModule(FakeContext())
  assert 'jsonfile' == result._connection._options['_uri']
  assert 3600 == result._connection._options['_timeout']
  assert 'ansible_facts' == result._connection._options['_prefix']



# Generated at 2022-06-13 11:32:58.334814
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert(obj)

# Generated at 2022-06-13 11:32:59.243329
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

# Generated at 2022-06-13 11:33:03.917361
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = 'test'
    config = ['foo', 'bar']
    try:
        CacheModule(connection, config)
    except NameError:
        assert False, "Class CacheModule has constructor with wrong arg list."

# Generated at 2022-06-13 11:33:06.243072
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.path == '/tmp/ansible_fact_cache'
    assert cm.timeout == 86400
    assert cm.file_extension == 'json'

# Generated at 2022-06-13 11:33:08.233953
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert x.get_options() == {'_prefix': None, '_timeout': 86400}

# Generated at 2022-06-13 11:33:11.097123
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert(CacheModule(dict(
        _uri="/tmp",
        _prefix="cachetest.",
        _timeout=86400,
    )) is not None)

# Generated at 2022-06-13 11:33:15.116315
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = '~/ansible_test_dir'

    test_cache = CacheModule(path)
    assert(test_cache.name == 'jsonfile')
    assert(test_cache._timeout == 86400)
    assert(test_cache._connection_info == path)

    return True

# Generated at 2022-06-13 11:33:16.602507
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule(None, 'test')

# Generated at 2022-06-13 11:34:10.447042
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule(task_vars={'some':'vars'})
    assert cache_module.task_vars['some'] == 'vars'

# Generated at 2022-06-13 11:34:11.060496
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule({})

# Generated at 2022-06-13 11:34:11.676922
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:34:14.597025
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # This test is testing the constructor of the class
    # assert True is used because we just want to make sure the constructor doesn't throw an error
    assert True == CacheModule().__init__()

# Generated at 2022-06-13 11:34:15.257935
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(), CacheModule)

# Generated at 2022-06-13 11:34:17.002821
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Unit test for constructor of class CacheModule"""
    cache = CacheModule()
    assert cache.file_extension == ".json"

# Generated at 2022-06-13 11:34:18.175954
# Unit test for constructor of class CacheModule

# Generated at 2022-06-13 11:34:23.093922
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import tempfile

    from ansible.plugins.cache import BaseFileCacheModule

    x = tempfile.mkdtemp()
    config = dict(
        _uri = x
    )
    test = CacheModule(config)
    assert isinstance(test, BaseFileCacheModule)


# Generated at 2022-06-13 11:34:24.824096
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._load != None
    assert cache_module._dump != None

# Generated at 2022-06-13 11:34:25.538558
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()

# Generated at 2022-06-13 11:36:16.620510
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule({})
    assert module.cache == {}
    assert module.timeout == 86400

# Generated at 2022-06-13 11:36:16.998911
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:36:17.381267
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print(CacheModule())

# Generated at 2022-06-13 11:36:18.661109
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        cm = CacheModule()
    except Exception as e:
        assert(False)

    return True

# Generated at 2022-06-13 11:36:19.656872
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert obj is not None

# Generated at 2022-06-13 11:36:21.677395
# Unit test for constructor of class CacheModule
def test_CacheModule():

    module = CacheModule(task_vars={})
    assert module.get_options()


# Generated at 2022-06-13 11:36:24.824190
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule(None)
    assert isinstance(obj._load(""), dict) or isinstance(obj._load(""), list)
    #assert obj._dump("test", "") == None

# Generated at 2022-06-13 11:36:26.040316
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert(isinstance(CacheModule(), BaseFileCacheModule))

# Generated at 2022-06-13 11:36:31.374689
# Unit test for constructor of class CacheModule
def test_CacheModule():
    prefix_to_use = "test_prefix"
    timeout = 600
    connection = "test_connection"

    cache = CacheModule(prefix_to_use, timeout, connection)
    assert cache.prefix == prefix_to_use
    assert cache.timeout == timeout
    assert cache.basedir == connection

# Generated at 2022-06-13 11:36:32.393654
# Unit test for constructor of class CacheModule
def test_CacheModule():
    tmp_obj = CacheModule()