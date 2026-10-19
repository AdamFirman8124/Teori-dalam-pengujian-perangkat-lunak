

# Generated at 2022-06-13 11:29:19.593364
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin

# Generated at 2022-06-13 11:29:21.114750
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin.type == 'jsonfile'

# Generated at 2022-06-13 11:29:23.546295
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule(None, task_vars={}, env={}, uri="http://example.com/")
    assert obj._timeout == 86400

# Generated at 2022-06-13 11:29:26.862102
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin is not None
    assert cache_plugin.plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:29:28.358158
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:29:30.978543
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    This is the unit test for construct of class CacheModule
    """
    # Check if create instance of class 'CacheModule' is possible.
    cache_module = CacheModule()
    assert isinstance(cache_module, CacheModule)

# Generated at 2022-06-13 11:29:33.444416
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:29:39.759735
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({'_uri': 'some_dir'})
    assert cache.file_extension == '.json'
    assert cache.timeout == 86400
    assert cache._timeout == 86400
    assert cache.file_extension == '.json'
    assert cache._prefix == ''

# Generated at 2022-06-13 11:29:44.101148
# Unit test for constructor of class CacheModule
def test_CacheModule():
    data = {"a": 1, "b": 2}
    obj = CacheModule()
    # Basic info
    assert getattr(obj, 'cache_plugin_name') == "jsonfile"
    assert getattr(obj, 'cache_plugin_timeout') is None
    # Default timeout
    obj = CacheModule(timeout=86400)
    assert getattr(obj, 'cache_plugin_timeout') == 86400
    # Write data
    obj.set('somekey', data)
    # Read data
    assert obj.get('somekey') == data

# Generated at 2022-06-13 11:29:46.030408
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = _CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:29:55.108498
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Tests will be done by checking the length of attributes
    cacheModule = CacheModule()
    length = len(vars(cacheModule))
    assert length == 4
    # Test cache module is an instance of BaseFileCacheModule
    assert isinstance(cacheModule, BaseFileCacheModule)

# Unit tests for method _load

# Generated at 2022-06-13 11:29:57.666783
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Makes sure that the constructor for the class does not fail on initialization.
    """
    p = CacheModule()
    assert isinstance(p, CacheModule)

# Generated at 2022-06-13 11:30:03.281165
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule(dict(path='/tmp', timeout=5))
    assert cacheModule.count() == 0
    assert cacheModule._timeout == 5
    assert cacheModule._connection == '/tmp'
    assert cacheModule._prefix == 'ansible_'
    assert cacheModule._load('nofile') == {}
    cacheModule._dump('noobj', 'nofile')
    assert isinstance(cacheModule._plugin_name, str)
    assert isinstance(cacheModule._display.warning, object)

# Generated at 2022-06-13 11:30:04.637415
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mycache = CacheModule()
    assert isinstance(mycache, CacheModule)


# Generated at 2022-06-13 11:30:05.514173
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert(isinstance(CacheModule(), BaseFileCacheModule))

# Generated at 2022-06-13 11:30:15.220510
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import sys
    import tempfile

    if sys.version_info[0] != 2:
        print("Test is incompatible with python version %s" % sys.version_info)
        return

    # To avoid using the environment variable and .ini config, we set them here and reset them after the test
    os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION'] = tempfile.mkdtemp()
    os.environ['ANSIBLE_CACHE_PLUGIN_TIMEOUT'] = '10'
    os.environ['ANSIBLE_CACHE_PLUGIN_PREFIX'] = 'test_cache_'

    # Test the CacheModule class
    cache_dir = os.environ['ANSIBLE_CACHE_PLUGIN_CONNECTION']

# Generated at 2022-06-13 11:30:18.108502
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.parsing.ajson import AnsibleJSONEncoder, AnsibleJSONDecoder
    from ansible.plugins.cache import BaseFileCacheModule
    x = CacheModule(None)
    assert isinstance(x, CacheModule)
    assert isinstance(x, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:18.942485
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:30:22.483631
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    cm = CacheModule()
    assert isinstance(cm, CacheModule)
    assert os.path.basename(cm._connection_info) == 'tmp'
    assert cm._prefix == 'ansible-cache'
    assert cm._timeout == 86400

# Generated at 2022-06-13 11:30:25.584524
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    cm = CacheModule()
    assert cm.is_valid is False
    assert cm.plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:30:31.226223
# Unit test for constructor of class CacheModule
def test_CacheModule():
    class ConstructorTest():
        name = 'jsonfile'
        settings = dict()
    cache = CacheModule(ConstructorTest())
    assert cache._plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:30:32.398160
# Unit test for constructor of class CacheModule
def test_CacheModule():
    tCache = CacheModule()
    assert tCache # TODO: unit test

# Generated at 2022-06-13 11:30:35.260722
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    a._timeout=7
    a._prefix="a"
    a._uri="/a"
    assert a._timeout is 7
    assert a._prefix == "a"
    assert a._uri == "/a"

# Generated at 2022-06-13 11:30:37.017905
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.get_extension() == 'cache'

# Generated at 2022-06-13 11:30:43.429177
# Unit test for constructor of class CacheModule
def test_CacheModule():
    data = {'name': 'test', 'age': 35}
    cache = CacheModule()
    cache.set('test', data)
    # This is the JSON file we use for unit tests
    file = open('/home/prashanth/pyansible/facts_cache/facts_test_facts.json', 'r')
    # Convert JSON file to python dictonary
    data_dict = json.loads(file.read())
    assert data == data_dict

# Generated at 2022-06-13 11:30:44.072406
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:30:45.379248
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()

    # Check object of CacheModule is created
    assert cm != None

# Generated at 2022-06-13 11:30:47.383152
# Unit test for constructor of class CacheModule
def test_CacheModule():
    #  Testing constructor of class CacheModule
    cacheModule = CacheModule(CONNECTION=None, TIMEOUT=86400)

# Generated at 2022-06-13 11:30:48.350996
# Unit test for constructor of class CacheModule
def test_CacheModule():
    return CacheModule()

# Generated at 2022-06-13 11:30:56.852678
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_cases = (
        (dict(timeout=3600), dict(timeout=3600)),  # normal case
        (dict(timeout=-3600), dict(timeout=3600)),  # negative timeout
    )
    for (opts, expected) in test_cases:
        cm = CacheModule(opts)
        assert(cm._timeout == expected['timeout'])

from ansible.plugins.cache.jsonfile import CacheModule


# Generated at 2022-06-13 11:31:04.336137
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor  for class CacheModule
    assert CacheModule('prefix', 'connection', 'timeout')

# Generated at 2022-06-13 11:31:06.188631
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = "/tmp/"
    timeout = 300
    cache = CacheModule(connection, timeout)
    assert cache._timeout == timeout
    assert cache._prefix == ''
    assert cache._uri == connection

# Generated at 2022-06-13 11:31:08.695132
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModuleObj = CacheModule()

# Generated at 2022-06-13 11:31:09.975006
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c.get_cache_prefix() == "ansible_facts"


# Generated at 2022-06-13 11:31:12.737090
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_cache = CacheModule({'_uri': 'cache_uri', '_prefix': 'cache_prefix', '_timeout': 'cache_timeout'})

    assert test_cache._uri == 'cache_uri'
    assert test_cache._prefix == 'cache_prefix'
    assert test_cache._timeout == 'cache_timeout'

# Generated at 2022-06-13 11:31:15.823696
# Unit test for constructor of class CacheModule
def test_CacheModule():

    data = {'a': 'b'}
    f = '/tmp/ansible_facts'

    cache = CacheModule()

    # Write to file
    cache._dump(data, f)
    assert cache._load(f) == data

    # Remove file
    cache._load(f)
    assert not cache.has_expired(f)

# Generated at 2022-06-13 11:31:17.310561
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:31:18.312069
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cmodule = CacheModule()
    assert(cmodule.file_extension == '.json')

# Generated at 2022-06-13 11:31:29.945447
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Constructor test
    """
    import os
    import shutil
    cache_dir = '/var/tmp/ansible-test-cache-dir'
    cache_plugin = 'jsonfile'
    cache_connection = os.path.join(cache_dir, cache_plugin)
    cache_timeout = 777

# Generated at 2022-06-13 11:31:31.092797
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:31:46.258023
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        connection = 'path/to/file'
        prefix = 'test'
        timeout = 100
        CacheModule(connection, prefix=prefix, timeout=timeout)
    except:
        raise

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:31:50.260113
# Unit test for constructor of class CacheModule
def test_CacheModule():
    hostvars = dict(ansible_os_family="RedHat", ansible_distribution="CentOS")
    host = "test"
    cache = CacheModule()
    cache.set(host, hostvars)
    assert cache.has_expired(host, 10) is False
    assert cache.get(host) == hostvars

# Generated at 2022-06-13 11:31:51.184549
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert x is not None

# Generated at 2022-06-13 11:31:52.647561
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c


# Generated at 2022-06-13 11:31:53.250101
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:31:54.209487
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:31:59.875486
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cfg=dict(
        _uri='/root/test',
        _prefix='testPrefix',
        _timeout=86400
    )
    cacheMod = CacheModule(cfg)
    assert cacheMod.path == '/root/test'
    assert cacheMod.plugin_name == 'jsonfile'
    assert cacheMod.timeout == 86400
    assert cacheMod._prefix == 'testPrefix'


# Generated at 2022-06-13 11:32:01.895701
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c
    assert c._prefix == 'ansible-fact'
    assert c._timeout == 86400
    assert c._connection == ''

# Generated at 2022-06-13 11:32:03.371066
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # No default value exists for _timeout
    with pytest.raises(TypeError):
        CacheModule()
    assert CacheModule(12)._timeout == 12

# Generated at 2022-06-13 11:32:09.157088
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache._load = lambda x: '{h1: "v1", h2: "v2"}'
    # test: get the value for key h1
    assert cache.get('h1') == 'v1'
    cache._dump = lambda x, y: None
    # test: put value v3 for key h3
    cache.set('h3', 'v3')

# Generated at 2022-06-13 11:32:36.890504
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._load("/tmp") == module._dump("/tmp", "value")

# Generated at 2022-06-13 11:32:37.835723
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:32:39.589644
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm, CacheModule), 'CacheModule constructor should return an instance of CacheModule'

# Generated at 2022-06-13 11:32:43.696927
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    obj = cache._get_cache_path("test_file")
    assert obj == "test_file"

    obj = cache._load("test_file")
    assert obj is None

    cache._dump("dummy_data", "test_file")
    assert True

# Generated at 2022-06-13 11:32:51.838000
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor test
    try:
        from ansible.plugins.cache.jsonfile import CacheModule
        cache_module = CacheModule(task_vars=dict())
        assert cache_module
    except Exception as e:
        assert False, "Constructor test failed: " + str(e)

    # load test
    try:
        import tempfile
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write('{\n "1": "1"\n}')
        f.close()
        result = cache_module._load(filepath=f.name)
        assert result == {u"1": u"1"}
    except Exception as e:
        assert False, "Test load failed: " + str(e)

    # dump test

# Generated at 2022-06-13 11:32:53.286803
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

# Generated at 2022-06-13 11:32:56.315324
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm, CacheModule)
    assert cm._loaded_data == None

# Generated at 2022-06-13 11:33:03.751738
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert not cache.get("test_CacheModule")
    cache.set("test_CacheModule", "test_CacheModule")
    assert cache.get("test_CacheModule") == "test_CacheModule"
    cache.flush()
    assert not cache.get("test_CacheModule")
    cache.close()

# Generated at 2022-06-13 11:33:04.658587
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:33:06.244334
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache import BaseFileCacheModule
    assert issubclass(CacheModule, BaseFileCacheModule)

# Generated at 2022-06-13 11:34:09.095499
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = 'test_filename.json'
    data = {'test' : 'data'}
    testmod = CacheModule()
    testmod.set_plugin_name('test')
    testmod.set_plugin_options({'_prefix' : None})
    # Test setting filename and data
    testmod.set_filename(filename)
    testmod.set_data(data)
    assert testmod.get_filename() == filename
    assert testmod.get_data() == data
    # Test to_file()
    testmod.to_file()
    # Test from_file()
    testmod.from_file()
    assert testmod.get_data() == data

# Generated at 2022-06-13 11:34:11.518261
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert isinstance(cache_module, BaseFileCacheModule)

# Generated at 2022-06-13 11:34:16.167515
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    print(m._load("/home/junaid/ansible/plugins/cache/jsonfile.py"))
    m._dump({"Test": "ansible"}, "/home/junaid/ansible/plugins/cache/jsonfile.py")
if __name__ == "__main__":
    test_CacheModule()


# Generated at 2022-06-13 11:34:17.909918
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.file_extension == 'json'
    assert cm.load('') == {}
    assert cm.dump({}) == {}

# Generated at 2022-06-13 11:34:21.332114
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_plugin = CacheModule()
    assert type(test_plugin) is CacheModule
    assert hasattr(test_plugin, '_load')
    assert hasattr(test_plugin, '_dump')
    assert hasattr(test_plugin, '_load_file')
    assert test_plugin.config is not None
    assert test_plugin.get_basedir() == '/tmp'

# Generated at 2022-06-13 11:34:21.947377
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:34:23.292593
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule({})
    assert cacheModule.root

# Generated at 2022-06-13 11:34:29.447637
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''Unit test for constructor of class CacheModule'''
    # Instantiate object
    cache = CacheModule()

    # Verify default values
    assert cache._connection == '~/.ansible/tmp'
    assert cache._timeout == 86400

    # Set connection value
    cache._connection = '/tmp'

    # Verify connection value changed
    assert cache._connection == '/tmp'

    # Set timeout value
    cache._timeout = 10

    # Verify timeout value changed
    assert cache._timeout == 10

# Generated at 2022-06-13 11:34:32.056587
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._load('/tmp/file.json') is None
    cache._dump('value', '/tmp/file.json')

# Generated at 2022-06-13 11:34:32.986628
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:36:27.314717
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:36:28.578899
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c

# Generated at 2022-06-13 11:36:30.365743
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None
    cache.flush()

# Generated at 2022-06-13 11:36:31.625034
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

# Generated at 2022-06-13 11:36:32.868423
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}) is not None

# Generated at 2022-06-13 11:36:34.569846
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(['/tmp']), CacheModule)

# Generated at 2022-06-13 11:36:36.249423
# Unit test for constructor of class CacheModule
def test_CacheModule():
    err_msg = "CacheModule object error"
    assert CacheModule() is not None, err_msg

# Generated at 2022-06-13 11:36:38.478931
# Unit test for constructor of class CacheModule
def test_CacheModule():
    jsonApi = CacheModule()
    assert isinstance(jsonApi, BaseFileCacheModule)

# Generated at 2022-06-13 11:36:43.155890
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()
    assert hasattr(m, '_load')
    assert hasattr(m, '_dump')
    assert hasattr(m, '_get_cache_basedir')
    assert hasattr(m, '_get_cache_basedir')

# Generated at 2022-06-13 11:36:49.759086
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, BaseFileCacheModule)
    assert cache.plugin_name == 'jsonfile'
    assert cache.cache_root == '~/.ansible/cache'
    assert cache.timeout == 86400
    assert cache.cache_connector == '_uri'
    assert cache.cache_prefix == '_prefix'
    assert cache.cache_timeout == '_timeout'