

# Generated at 2022-06-13 11:29:20.720399
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Testing existence of CacheModule class
    assert CacheModule

# Generated at 2022-06-13 11:29:23.968325
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_connection = "/tmp/ansible_fact_caching/"
    assert CacheModule({'_uri': "/tmp/ansible_fact_caching/"} , task_vars={})._connection == cache_connection

# Generated at 2022-06-13 11:29:26.198088
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a CacheModule object
    test = CacheModule()
    # Assert the property of the class
    assert test._connection['_timeout'] == 86400

# Generated at 2022-06-13 11:29:27.061169
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module is not None

# Generated at 2022-06-13 11:29:28.296959
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule({}, 'test')
    assert a._connection == 'test'

# Generated at 2022-06-13 11:29:31.090826
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert(CacheModule({'_uri': 'cache/dir'}) is not None)



# Generated at 2022-06-13 11:29:32.864796
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule(dict())


# Generated at 2022-06-13 11:29:37.104051
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule('/path/to/my/cache')
    assert isinstance(c, CacheModule)
    assert c._connection == '/path/to/my/cache'

# Generated at 2022-06-13 11:29:38.136325
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:29:44.061170
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import tempfile

    # create temporary directory
    tempdir = tempfile.mkdtemp()
    path = os.path.join(tempdir, "ansible.cache")
    assert os.path.exists(tempdir)
    assert not os.path.exists(path)

    # test constructor of base class
    cache = BaseFileCacheModule(path)
    assert cache.cache._conn_params['_uri'] == path

    # test constructor of child class
    jcache = CacheModule(path)
    assert jcache.cache._conn_params['_uri'] == path

    # test set method
    jcache.set("foo", "bar")
    assert os.path.exists(path)

    # test get method
    value = jcache.get("foo")
    assert value == "bar"

    #

# Generated at 2022-06-13 11:29:51.582598
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    from ansible.plugins.cache import get_cache_plugin
    cachedir = os.path.join(os.getcwd(), 'cachedir')
    module = get_cache_plugin(cachedir, 'jsonfile')
    assert isinstance(module, CacheModule)
    assert module.cache_dir == cachedir
    assert module.cache_file == os.path.join(cachedir, 'ansible_facts.json')
    assert module.cache_timeout == 86400

# Generated at 2022-06-13 11:29:59.245493
# Unit test for constructor of class CacheModule
def test_CacheModule():

    try:
        assert CacheModule()
    except:
        assert False, 'Test for class CacheModule constructor failed!'

#test1 for constructor of class CacheModule
fake_plugin_name = 'test'
fake_plugin_args = {'_uri': 'fake_uri', '_prefix': 'fake_prefix', '_timeout': 'fake_timeout', '_expires': 'fake_expires'}

try:
    fake_cache_module = CacheModule(fake_plugin_name, fake_plugin_args)
    assert fake_cache_module.plugin == fake_plugin_name
    assert fake_cache_module.plugin_args == fake_plugin_args
except:
    assert False, 'Test1 for constructor of class CacheModule failed!'

#test2 for constructor of class CacheModule
fake_plugin_name = 'test'
fake_

# Generated at 2022-06-13 11:30:03.088888
# Unit test for constructor of class CacheModule
def test_CacheModule():
    tmp_config = {'_uri': '/tmp/foo', '_timeout': 86400}
    cache_module = CacheModule(tmp_config)
    assert cache_module.file_extension == '.json'
    assert cache_module.pickle_version == 2

# Generated at 2022-06-13 11:30:03.887592
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule({}, 'ansible_facts')

# Generated at 2022-06-13 11:30:05.609845
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mod_path = "ansible.plugins.cache.jsonfile"
    mod = __import__(mod_path, globals(), locals(), ["CacheModule"])
    obj = mod.CacheModule()
    assert obj

# Generated at 2022-06-13 11:30:07.359593
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, BaseFileCacheModule)
    assert isinstance(cache, CacheModule)


# Generated at 2022-06-13 11:30:08.664734
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert isinstance(cache_plugin, CacheModule)


# Generated at 2022-06-13 11:30:09.604614
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({})
    assert cache.plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:30:12.513495
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.get_timeout() == 86400
    assert cm.get_connection() is None
    assert cm.get_prefix() is None

# Generated at 2022-06-13 11:30:17.500063
# Unit test for constructor of class CacheModule
def test_CacheModule():

    from ansible.plugins.loader import cache_loader

    cache_plugin = cache_loader.get('jsonfile', 'D:\\ansible\\ansible_cache')
    assert type(cache_plugin) is CacheModule
    assert cache_plugin._prefix == 'ansible_facts'
    assert cache_plugin._timeout == 604800
    assert cache_plugin._basedir.rstrip('/') == 'D:\\ansible\\ansible_cache'

# Generated at 2022-06-13 11:30:22.272033
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert obj._cache_prefix is None
    assert obj._cache_timeout == 86400
    assert obj._connection is not None
    assert obj._plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:30:25.733043
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    print(cm.connection, cm.plugin_name, cm.cache_dir, cm.timeout)


if __name__ == "__main__":
    test_CacheModule()

# Generated at 2022-06-13 11:30:26.306703
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = CacheModule()

# Generated at 2022-06-13 11:30:27.999782
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c


# Generated at 2022-06-13 11:30:28.882842
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(task=None)

# Generated at 2022-06-13 11:30:30.181928
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

# Generated at 2022-06-13 11:30:34.076785
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    # CacheModule.__init__ calls BaseFileCacheModule.__init__, a method that
    # does not exist in BaseFileCacheModule.  CacheModule uses this
    # non-existent method, which should raise a TypeError
    assert isinstance(c, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:35.224507
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None


# Generated at 2022-06-13 11:30:37.326892
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.connection == 'facts'
    assert cache_module.timeout == 86400



# Generated at 2022-06-13 11:30:39.256651
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(cache.get_prefix() == u'')

# Generated at 2022-06-13 11:30:49.656200
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    # Create a new class instance by calling constructor
    cache_plugin2 = CacheModule()
    assert cache_plugin is not None
    assert cache_plugin2 is not None
    assert cache_plugin is not cache_plugin2
    assert type(cache_plugin) == type(cache_plugin2)



# Generated at 2022-06-13 11:30:51.093060
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert not CacheModule('no_prefix')

# Generated at 2022-06-13 11:30:54.146163
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin._load is not None
    assert cache_plugin._dump is not None

# Generated at 2022-06-13 11:30:56.011547
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    cache = CacheModule()

# Generated at 2022-06-13 11:30:59.241696
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars=dict(ansible_connection='local'))
    assert not cache.get('test')

# Generated at 2022-06-13 11:31:01.059192
# Unit test for constructor of class CacheModule
def test_CacheModule():
    ca = CacheModule()
    assert isinstance(ca, CacheModule)

# Generated at 2022-06-13 11:31:08.140023
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("TEST_CACHE_MODULE:")
    print("Testing __new__ function")
    # Test if the class is actually a subclass of BaseFileCacheModule
    assert issubclass(CacheModule, BaseFileCacheModule)

    print("Testing __init__ function")
    module = CacheModule()
    assert module._timeout == 86400
    assert module._get_options() == {}
    assert module._connection == {}

    # Test _load and _dump
    value = {
        "key1": "val1",
        "key2": 2,
        "key3": None
    }
    filepath = "test.json"
    module._dump(value, filepath)
    result = module._load(filepath)
    assert value == result

    print("Testing _get_cache plugin")
    assert module._get_

# Generated at 2022-06-13 11:31:10.507667
# Unit test for constructor of class CacheModule
def test_CacheModule():
    class TestModule(CacheModule):
        def __init__(self, *args, **kwargs):
            self.called = True
            super(TestModule, self).__init__(*args, **kwargs)

    assert TestModule({}).called

# Generated at 2022-06-13 11:31:11.484982
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_object = url_facts.CacheModule()
    assert test_object is not None

# Generated at 2022-06-13 11:31:12.227266
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:31:25.358790
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert m.get_timeout() == 86400

# Generated at 2022-06-13 11:31:26.671754
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

# Generated at 2022-06-13 11:31:29.104904
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    assert type(a) == CacheModule, "Error: 'a' is not a CacheModule"

# Generated at 2022-06-13 11:31:30.530643
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test = CacheModule()
    assert test._connection is not None
    assert test._prefix is not None

# Generated at 2022-06-13 11:31:31.533213
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:31:35.562983
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ == """
    A caching module backed by json files.
    """

    cache_module = CacheModule()
    assert cache_module._load.__doc__ == """
        Valid JSON is always UTF-8 encoded.
        """
    assert cache_module._dump.__doc__ == """
        Write value out to filepath, in a json format.
        """

# Generated at 2022-06-13 11:31:40.125246
# Unit test for constructor of class CacheModule
def test_CacheModule():
    params = {'_uri':  '/tmp/ansible',
              '_prefix': None,
              '_timeout': 86400
              }
    cm = CacheModule(params)

    assert cm._options['_uri'] == '/tmp/ansible'
    assert cm._options['_prefix'] is None
    assert cm._options['_timeout'] == 86400

# Generated at 2022-06-13 11:31:46.292979
# Unit test for constructor of class CacheModule
def test_CacheModule():
    conn = {'conn_str':'/tmp/ansible'}
    t = 86400
    prefix = 'some_prefix'

    test = CacheModule()
    test.set_options(conn)
    assert test.get_options() == {}
    test.set_options(t)
    assert test.get_options() == {}
    test.set_options(prefix)
    assert test.get_options() == {}
    test.set_options(conn, t, prefix)
    assert test.get_options() == {'_timeout': 86400, '_conn': '/tmp/ansible', '_prefix': 'some_prefix'}

    assert test.get_timeout() == 86400
    assert test.get_connection() == '/tmp/ansible'
    assert test.get_prefix() == 'some_prefix'

# Generated at 2022-06-13 11:31:51.005514
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()

    # The _dump() method is called in the constructor,
    # so there will be a file in the one-level directory created.
    assert not obj.validate(None)('')

    # The method name is _load, not load.
    obj.load('data')

    # The method name is _load, and the parameter is not valiation.
    obj.load('data', 'valiation')

# Generated at 2022-06-13 11:32:00.502953
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Test the constructor of class CacheModule.
    """
    cache_plugin_connection = '/tmp/test_ansible_plugin_connection'
    cache_plugin_prefix = 'test_ansible_plugin_prefix'
    cache_plugin_timeout = 'test_ansible_plugin'
    cache_module = CacheModule(
        cache_plugin_connection=cache_plugin_connection,
        cache_plugin_prefix=cache_plugin_prefix,
        cache_plugin_timeout=cache_plugin_timeout,
        )
    assert cache_module.cache_plugin_connection == cache_plugin_connection
    assert cache_module.cache_plugin_prefix == cache_plugin_prefix
    assert cache_module.cache_plugin_timeout == cache_plugin_timeout

# Generated at 2022-06-13 11:32:28.489639
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c.get_cache_prefix("/foo/bar.json") == "bar"

# Generated at 2022-06-13 11:32:34.715801
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test passing two arguments
    cache_module = CacheModule(None, None)
    assert cache_module.plugin_name == 'jsonfile'
    assert cache_module._options == {}

    # Test passing three arguments
    cache_module = CacheModule(None, None, '_timeout')
    assert cache_module.plugin_name == 'jsonfile'
    assert cache_module._options['_timeout'] == '_timeout'

    # Test passing an invalid number of arguments
    try:
        cache_module = CacheModule(None)
    except TypeError:
        pass
    else:
        assert False



# Generated at 2022-06-13 11:32:39.544643
# Unit test for constructor of class CacheModule
def test_CacheModule():
    result = True

    obj = CacheModule()
    if not obj.get("test"):
        result = False

    if obj.set("test", {"test1": 123}):
        result = False

    if obj.delete("test"):
        result = False

    if obj.keys("test"):
        result = False

    return result

# Generated at 2022-06-13 11:32:43.998649
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache._load = True
    cache._dump = True
    cache.get = True
    cache.set = True
    cache.has_expired = True
    assert cache._load
    assert cache._dump
    assert cache.get
    assert cache.set
    assert cache.has_expired

# Generated at 2022-06-13 11:32:45.521071
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({})
    assert isinstance(cache, CacheModule)

# Generated at 2022-06-13 11:32:49.126325
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Test constructor.
    Expceted result: error raised (exception) when argument C is missing.
    """
    try:
        CacheModule(A=1, B=2)
        assert True
    except TypeError as e:
        if 'expected at least 5 arguments' in e.message:
            assert True
        else:
            assert False

# Generated at 2022-06-13 11:32:51.048564
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert isinstance(plugin, CacheModule)
    assert plugin._timeout == 86400
    assert plugin._encoding == "utf-8"


# Generated at 2022-06-13 11:32:59.156654
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test with invalid URI.
    assert CacheModule(None, {'_uri': '../../../../../../dev/null'})._local_path == '../../../../../../dev/null'
    # Test with valid URI.
    assert CacheModule(None, {'_uri': '~/local'})._local_path == '~/local'


# Generated at 2022-06-13 11:33:08.187186
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Test constructor"""
    module = CacheModule()
    assert module.get_options() == {
        '_prefix': {'default': 'ansible_', 'ini': 'fact_caching_prefix', 'env': 'ANSIBLE_CACHE_PLUGIN_PREFIX'},
        '_timeout': {'default': 86400, 'ini': 'fact_caching_timeout', 'env': 'ANSIBLE_CACHE_PLUGIN_TIMEOUT', 'type': 'integer'},
        '_uri': {'required': True, 'ini': 'fact_caching_connection', 'env': 'ANSIBLE_CACHE_PLUGIN_CONNECTION', 'type': 'path'}
    }

# Generated at 2022-06-13 11:33:11.851542
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    # This can't be tested as the uri is set by calling plugin()
    assert cm._uri is None
    assert cm.cache_plugin_name == 'jsonfile'
    assert cm.valid_extensions == ['.json']

# Generated at 2022-06-13 11:34:11.520945
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = {'_timeout': 3600, '_uri': '/root/.ansible/tmp/ansible-local', '_prefix': 'ansible-local'}
    file_cache = CacheModule(connection)
    assert file_cache.CACHE_PLUGIN_PREFIX == '/root/.ansible/tmp/ansible-local/facts'
    assert file_cache.CACHE_PLUGIN_TIMEOUT == 3600



# Generated at 2022-06-13 11:34:12.326148
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache

# Generated at 2022-06-13 11:34:15.413168
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.CACHE_PLUGIN_PREFIX == 'ansible_jsonfile_'
    assert CacheModule.CACHE_PLUGIN_CONNECTION == '/tmp'
    assert CacheModule.CACHE_PLUGIN_TIMEOUT == 86400


# Generated at 2022-06-13 11:34:17.911883
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = "/tmp/.ansible/tmp"
    cache_plugin_timeout = 1
    cache = CacheModule()
    assert cache.cache_dir == cache_dir
    assert cache.timeout == cache_plugin_timeout


# Generated at 2022-06-13 11:34:18.550939
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin

# Generated at 2022-06-13 11:34:20.097625
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor
    cache_module = CacheModule()

# Generated at 2022-06-13 11:34:23.829460
# Unit test for constructor of class CacheModule
def test_CacheModule():
	data = {'a': 'b'}
	encoded_data = json.dumps(data, cls=AnsibleJSONEncoder)
	decoded_data = json.loads(encoded_data, cls=AnsibleJSONDecoder)
	assert data == decoded_data

# Generated at 2022-06-13 11:34:30.599282
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test for constructor of class CacheModule
    """

    class Test():
        """Test class to simulate connection object."""
        def __init__(self, uri, host):
            """Constructor."""
            self.host = host
            self.uri = uri


    test = Test('/tmp', 'local')
    cache = CacheModule(test)
    assert cache._connection == test
    assert cache._connection.uri == '/tmp'
    assert cache._connection.host == 'local'

# Generated at 2022-06-13 11:34:33.599793
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache.set("foo", {'mydict': {'a':1, 'b':2}})
    assert cache.get("foo") == {'mydict': {'a':1, 'b':2}}


# Generated at 2022-06-13 11:34:34.553871
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:36:35.972012
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._prefix == 'ansible-factcache'
    assert cache_module._timeout == 86400
    assert cache_module._load({}) == {}
    assert cache_module._dump({"test": True}) == '{\n    "test": true\n}'

# Generated at 2022-06-13 11:36:38.204632
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule('/tmp/cache')
    assert cache is not None


# Generated at 2022-06-13 11:36:38.909876
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:36:45.548288
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_timeout = 10
    fact_caching_connection = '/opt/ansible/data/'
    fact_caching_prefix = 'ansible'
    connection = 'local'
    module = CacheModule(connection=fact_caching_connection, fact_caching_prefix=fact_caching_prefix,
                         fact_caching_timeout=cache_timeout)
    assert module.file_extension == ".json"

# Generated at 2022-06-13 11:36:47.726289
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin.file_extension == ".json"

# Generated at 2022-06-13 11:36:52.306932
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(filename='test', basedir='/tmp/')
    assert cache._load('/tmp/test') == {}
    cache.set('foo', 'bar')
    assert cache._load('/tmp/test') == {'foo': 'bar'}

# Generated at 2022-06-13 11:36:56.347749
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({'_uri': '/path/'})
    assert cache._connection_info == {'_uri': '/path/'}
    assert cache._timeout == 86400



# Generated at 2022-06-13 11:36:57.891513
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule == type(CacheModule())

# Generated at 2022-06-13 11:37:01.082030
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule

    cache_plugin = CacheModule()

    assert cache_plugin.ANON_FILE

# Generated at 2022-06-13 11:37:04.594106
# Unit test for constructor of class CacheModule
def test_CacheModule():
    _test_cache_module = CacheModule()
    assert isinstance(_test_cache_module,CacheModule)
    #assert id(_test_cache_module) == id(None) 
  