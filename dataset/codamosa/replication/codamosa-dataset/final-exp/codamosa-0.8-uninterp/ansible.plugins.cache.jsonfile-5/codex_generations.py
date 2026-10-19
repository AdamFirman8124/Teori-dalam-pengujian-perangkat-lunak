

# Generated at 2022-06-13 11:29:14.887974
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:29:16.323341
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:29:17.840486
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert isinstance(cache_module, CacheModule)

# Generated at 2022-06-13 11:29:19.647761
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._prefix == 'ansible-fact'
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:29:20.545548
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mod = CacheModule()
    assert mod is not None

# Generated at 2022-06-13 11:29:21.258967
# Unit test for constructor of class CacheModule
def test_CacheModule():
	assert CacheModule()

# Generated at 2022-06-13 11:29:23.297301
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache import CacheModule
    cache_module = CacheModule()
    cache_module

# Generated at 2022-06-13 11:29:27.791404
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # All this does is test that it doesn't crash. It doesn't do any mocking, so can't be expected to actually test
    # anything useful.
    cache_module = CacheModule()
    assert cache_module

# Generated at 2022-06-13 11:29:34.031589
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_obj = CacheModule()
    assert cache_obj._load('temp.json') == None
    cache_obj._dump('temp.json')
    assert cache_obj.get('temp.json') == None
    assert cache_obj.set('temp.json') == None

# Generated at 2022-06-13 11:29:35.607867
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert(x)

# Generated at 2022-06-13 11:29:39.970323
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test to check whether object is created
    """
    plugin_obj = CacheModule()
    assert plugin_obj is not None

# Generated at 2022-06-13 11:29:40.635776
# Unit test for constructor of class CacheModule
def test_CacheModule():
    t = CacheModule()

# Generated at 2022-06-13 11:29:42.009803
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c != None

# Generated at 2022-06-13 11:29:51.733811
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import uuid
    from re import sub
    from tempfile import mkdtemp
    from ansible.plugins.loader import cache_loader

    name = "jsonfile"
    class_name = "CacheModule"
    rm_dir = None
    tmp_dir = mkdtemp()
    tmp_json_file = os.path.join(tmp_dir,'test.json')
    tmp_uuid = sub('-','_',str(uuid.uuid4()))

    def rm_tmp_dir():
        import shutil
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

    plugin = cache_loader.get(name, class_name)
    assert plugin._load is not None
    assert plugin._dump is not None

# Generated at 2022-06-13 11:29:54.177509
# Unit test for constructor of class CacheModule
def test_CacheModule():
    fake_uri = "/tmp/somewhere"
    fake_prefix = "prefix"
    fake_timeout = 12345
    cache = CacheModule(fake_uri, fake_prefix, fake_timeout)
    assert cache._connection == fake_uri
    assert cache._prefix == fake_prefix
    assert cache._timeout == fake_timeout

# Generated at 2022-06-13 11:29:57.620801
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars=dict())
    assert cache._timeout == 86400
    assert cache._load("tests/unit/plugins/cache/jsonfile/test_file.json") == {"test": 123}


# Generated at 2022-06-13 11:30:00.230444
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._timeout == 86400
    assert c._connection == ''
    assert c._prefix == ''

# Generated at 2022-06-13 11:30:07.641244
# Unit test for constructor of class CacheModule
def test_CacheModule():

    # Given
    import json
    import os
    import tempfile

    # AnsibleModule is only used for unit testing
    from ansible.module_utils.basic import AnsibleModule

    test_data = {
        u'foo': u'bar',
        u'baz': {
            u'qux': u'quux'
        }
    }

    # When
    module = AnsibleModule(
        argument_spec={
            '_uri': {'required': True, 'type': 'path'},
        }
    )
    cm = CacheModule(module)
    test_dir = tempfile.mkdtemp()
    test_path = os.path.join(test_dir, 'test_file')


# Generated at 2022-06-13 11:30:08.701913
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test = CacheModule()
    assert isinstance(test, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:09.556333
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({}) is None

# Generated at 2022-06-13 11:30:13.185830
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({})._timeout == 86400

# Generated at 2022-06-13 11:30:14.192108
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule('_uri')

# Generated at 2022-06-13 11:30:16.031752
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Test to check if correct class is returned for different type of plugin.
    """
    assert issubclass(CacheModule, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:17.874380
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm, CacheModule)
    assert cm._timeout == 86400

# Generated at 2022-06-13 11:30:18.463361
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:25.133481
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert getattr(CacheModule, 'do_clear', None) is not None, \
        'CacheModule.do_clear method must be implemented'
    assert getattr(CacheModule, 'do_persist', None) is not None, \
        'CacheModule.do_persist method must be implemented'
    assert getattr(CacheModule, 'get', None) is not None, \
        'CacheModule.get method must be implemented'
    assert getattr(CacheModule, 'set', None) is not None, \
        'CacheModule.set method must be implemented'

# Generated at 2022-06-13 11:30:26.107524
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule(task=None)

# Generated at 2022-06-13 11:30:28.514370
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._load(None) == None
    assert cache_module._dump(None, None) == None

# Generated at 2022-06-13 11:30:30.279671
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)


# Generated at 2022-06-13 11:30:36.096700
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = {'_uri': 'foo', '_prefix': 'bar', '_timeout': 'baz'}
    cache = CacheModule(connection, 'ansible_facts')
    assert cache._connection == connection
    assert cache._timeout == connection['_timeout']
    assert cache._plugin_name == 'ansible_facts'
    assert cache._plugin_specific_keys == ['_prefix', '_timeout']

    # Test the _load() method.
    cache._load('test')


# Generated at 2022-06-13 11:30:49.546003
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = "test.json"
    test_obj = CacheModule(filename)
    assert test_obj.basedir == filename, 'Test Failed. Expected basedir to be %s. Got %s' % (filename, test_obj.basedir)
    assert test_obj.plugin_name == 'jsonfile', 'Test Failed. Expected plugin_name to be jsonfile. Got %s' % test_obj.plugin_name
    assert test_obj.lock_path == filename, 'Test Failed. Expected basedir to be %s. Got %s' % (filename, test_obj.lock_path)


# Generated at 2022-06-13 11:30:51.504529
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, CacheModule)

# Generated at 2022-06-13 11:31:02.623948
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = 'uri'
    prefix = 'prefix'
    timeout = 'timeout'
    _data = {}
    cache_plugin = CacheModule(uri, prefix, timeout)

    assert cache_plugin.uri == uri
    assert cache_plugin.prefix == prefix
    assert cache_plugin._timeout == timeout
    assert cache_plugin._data == _data

    _data = {}
    cache_plugin = CacheModule(uri)

    assert cache_plugin.uri == uri
    assert cache_plugin.prefix == ''
    assert cache_plugin._timeout == 86400
    assert cache_plugin._data == _data

# Generated at 2022-06-13 11:31:03.801632
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm

# Generated at 2022-06-13 11:31:05.666831
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(cache._uri == "")
    assert(cache._options == {})
    assert(cache._timeout == 0)


# Generated at 2022-06-13 11:31:11.595477
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # test no parameters
    cm = CacheModule()
    # verify values
    assert cm._connection is None
    assert cm._timeout == 86400
    assert cm._prefix is None
    # test with parameters
    cm = CacheModule(connection='test_connection', timeout=123, prefix='test_prefix')
    # verify values
    assert cm._connection == 'test_connection'
    assert cm._timeout == 123
    assert cm._prefix == 'test_prefix'

# Generated at 2022-06-13 11:31:12.050536
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({})

# Generated at 2022-06-13 11:31:13.775855
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin != None
    assert 'jsonfile' == cache_plugin.CACHE_PLUGIN_TYPE


# Generated at 2022-06-13 11:31:22.670287
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # construct a dict
    data = dict(one=1, two=2)
    # construct a class
    my_obj = CacheModule()
    # check members
    assert my_obj._cachefile
    assert my_obj._cachefile_contents
    assert my_obj._connection
    assert my_obj._timeout
    assert my_obj._prefix
    assert my_obj.cache
    # call methods
    assert my_obj._load("./test/helpers/write_data.json") == data

# Generated at 2022-06-13 11:31:24.000867
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule() is not None

# Generated at 2022-06-13 11:31:31.393299
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("Testing constructor for class CacheModule")
    myCacheModule = CacheModule()
    assert myCacheModule is not None, \
        "Failed to create object from class CacheModule"


# Generated at 2022-06-13 11:31:34.723534
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule(task=None)
    cache_module._timeout = 86400
    json_string = json.dumps(AnsibleJSONEncoder().default(cache_module))
    assert("_timeout" in json_string)
    assert("86400" in json_string)

# Generated at 2022-06-13 11:31:35.313458
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:31:38.197275
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Initialize a CacheModule object
    jsonfile = CacheModule()
    assert(jsonfile._load(
            "/home/brent/projects/core/ansible/plugins/cache/jsonfile") is not None)

# Generated at 2022-06-13 11:31:39.886023
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None
    assert cm.path is None


# Generated at 2022-06-13 11:31:41.093400
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule('./testdir') is not None


# Generated at 2022-06-13 11:31:42.506583
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule(None)
    assert isinstance(cm, CacheModule)

# Generated at 2022-06-13 11:31:49.695127
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_name = "jsonfile"
    plugin = CacheModule(cache_plugin_name)
    # Verify that the object is initialized as expected.
    assert plugin._cache_plugin_name == cache_plugin_name
    assert isinstance(plugin._cache_dir, str)
    assert isinstance(plugin._timeout, int)
    assert isinstance(plugin._prefix, str)
    assert isinstance(plugin.validate, bool)
    assert plugin.validate == False

# Generated at 2022-06-13 11:31:50.920856
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'_uri': '/tmp'}, None)

# Generated at 2022-06-13 11:31:52.400510
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(dict(), '')
    assert cache is not None

# Generated at 2022-06-13 11:32:00.286543
# Unit test for constructor of class CacheModule
def test_CacheModule():
    inst = CacheModule('/dummy/path')
    assert inst._plugin_options['_uri'] == '/dummy/path'

# Generated at 2022-06-13 11:32:00.896126
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:32:01.538029
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:32:03.827695
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_cachemodule = CacheModule()
    assert test_cachemodule.cache_prefix == "ansible_file"

# Generated at 2022-06-13 11:32:06.946898
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_obj = CacheModule()
    test_obj._load("/home/ansible/test.json")
    test_obj._dump("test", "/home/ansible/test1.json")

# Generated at 2022-06-13 11:32:09.860494
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin.file_extension == '.json'
    assert isinstance(cache_plugin.file_extension, str)

# Generated at 2022-06-13 11:32:14.336556
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule('/some/path')

    assert cache._connected == False
    assert cache._cache_dir == '/some/path'
    assert cache._timeout == 86400
    assert cache._prefix == 'ansible-cache'
    assert cache.lock_path == cache._cache_dir + "/ansible-cache.lock"

# Generated at 2022-06-13 11:32:16.448956
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Unit test for constructor of class CacheModule
    """
    ts = CacheModule()
    assert isinstance(ts, CacheModule)

# Generated at 2022-06-13 11:32:24.603007
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c.cache_plugin_name == 'jsonfile'
    assert c.cache_plugin_timeout == 86400
    assert c.cache_plugin_connection == '~/.ansible/tmp/ansible-fact-cache'
    assert c.cache_plugin_prefix == 'ansible_facts'
    # Test constructor with different settings
    timeout = 600
    cache_plugin_name = 'jsonfile2'
    cache_plugin_connection = '/tmp/ansible/plugin_connection'
    cache_plugin_prefix = 'ansible_facts'
    c = CacheModule(timeout=timeout,
                    cache_plugin_name=cache_plugin_name,
                    cache_plugin_connection=cache_plugin_connection,
                    cache_plugin_prefix=cache_plugin_prefix)
    assert c.cache_plugin_name

# Generated at 2022-06-13 11:32:25.878436
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:32:39.031070
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert False

# Generated at 2022-06-13 11:32:40.610666
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """ This is a constructor test of a class CacheModule"""
    CacheModule('/')


# Generated at 2022-06-13 11:32:42.643113
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/tmp/ansible/cache'
    timeout = 3600
    obj = CacheModule(cache_dir, timeout)
    assert obj._directory == cache_dir
    assert obj._timeout == timeout

# Generated at 2022-06-13 11:32:45.995727
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._cache_dir == ''
    assert cache_module._prefix == 'ansible_fact_cache'
    assert cache_module._timeout == 86400

# Generated at 2022-06-13 11:32:53.343255
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # If a _datadir is specified, ensure that the directory is created.
    from ansible.plugins.cache.jsonfile import CacheModule
    from ansible.utils.path import makedirs_safe
    from tempfile import TemporaryDirectory
    from os import path
    from shutil import rmtree
    import os
    import pytest
    import platform

    if platform.system() == 'Windows':
        ansible_cache_dir = path.join(os.env['USERPROFILE'], 'AppData', 'Local', 'Temp', 'ansible_fact_caching')
    else:
        ansible_cache_dir = "/var/tmp/ansible_fact_caching"

    # the temp directory will contain some files, so the
    # makedirs_safe method will not raise exception if
    # directory already exists

# Generated at 2022-06-13 11:32:54.459007
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:32:55.345142
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:32:57.518450
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule) == True


# Generated at 2022-06-13 11:32:59.073995
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

# Generated at 2022-06-13 11:33:00.639862
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert str(CacheModule()) == "jsonfile"

# Generated at 2022-06-13 11:33:26.896463
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)

# Generated at 2022-06-13 11:33:31.270832
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a CacheModule object and test its properties
    cache_module = CacheModule()
    assert cache_module._prefix == 'ansible_fact_cache'
    assert cache_module._timeout == 86400
    assert cache_module._uri == ''

# Generated at 2022-06-13 11:33:33.821847
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert(CacheModule(dict(
        _uri = 'test_uri',
        _prefix = 'test_prefix',
        _timeout = 0
    )) is None)

# Generated at 2022-06-13 11:33:35.775362
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = "/var/tmp/ansible/cache/"
    timeout = 43200
    CacheModule(uri, timeout)

# Generated at 2022-06-13 11:33:40.801366
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = "/tmp/ansible-cache/"
    timeout = 86400
    prefix = ""
    cache_plugin = CacheModule(uri, timeout=timeout, prefix=prefix)
    assert cache_plugin.cache_timeout == timeout
    assert cache_plugin.cache_dir == uri
    assert cache_plugin.cache_prefix == prefix

# Generated at 2022-06-13 11:33:42.607884
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._load(None) == None
    assert cm._dump(None, None) == None

# Generated at 2022-06-13 11:33:44.305334
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    assert a

# Generated at 2022-06-13 11:33:45.470668
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(CacheModule(dict()),CacheModule)

# Generated at 2022-06-13 11:33:53.771847
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert 'jsonfile' == CacheModule.CACHE_PLUGIN_NAME
    assert 'jsonfile' == CacheModule.CACHE_PLUGIN_NAME
    assert 'JSON formatted files.' == CacheModule.CACHE_PLUGIN_DESCRIPTION
    assert True == CacheModule.CACHE_PLUGIN_CONNECTION
    assert '~/.ansible/tmp' == CacheModule.CACHE_PLUGIN_CONNECTION_NAME
    assert None == CacheModule.CACHE_PLUGIN_PREFIX
    assert 'ANSIBLE_CACHE_PLUGIN_PREFIX' == CacheModule.CACHE_PLUGIN_PREFIX_NAME
    assert 86400 == CacheModule.CACHE_PLUGIN_TIMEOUT

# Generated at 2022-06-13 11:33:56.274502
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        cm = CacheModule(dict(plugin_name=None, task_vars=None))
    except:
        assert False, 'Unable to initialize CacheModule'
    assert True, 'CacheModule initialized'

# Generated at 2022-06-13 11:34:50.008023
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    This test simply runs the __init__ method of the CacheModule class
    and checks whether it runs smoothly or not
    """
    mocker.patch('ansible.plugins.cache.jsonfile.CacheModule._load')
    mocker.patch('ansible.plugins.cache.jsonfile.CacheModule._dump')
    jsonfile.CacheModule()

# Generated at 2022-06-13 11:34:51.006440
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # create example class for testing
    cache_module = CacheModule()
    cache_module._load
    cache_module._dump

# Generated at 2022-06-13 11:34:57.688131
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)  # class CacheModule(BaseFileCacheModule):
    assert issubclass(CacheModule, object)
    assert CacheModule.__doc__
    assert CacheModule._options
    assert hasattr(CacheModule, '_load')
    assert hasattr(CacheModule, '_dump')



# Generated at 2022-06-13 11:35:04.244364
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

    assert c.FMT == 'json'
    assert c.HASH_KEYS == ['data']

    assert c.CacheBaseFile.CLS == 'jsonfile'
    assert c.CacheBaseFile.EXT == '.cache'
    assert c.CacheBaseFile.ENCODING == 'utf-8'
    assert c.CacheBaseFile.ENV == 'ANSIBLE_' + c.CacheBaseFile.CLS.upper()
    assert c.CacheBaseFile.ENV_TIMEOUT == 'ANSIBLE_CACHE_PLUGIN_TIMEOUT'

    str_path = '/path/to/file'
    c.set_basedir(str_path)
    assert c.basedir == str_path

    str_name = 'test1_cachefile_name'
    c.set_plugin_name

# Generated at 2022-06-13 11:35:09.457839
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__
    assert CacheModule.__name__ == 'CacheModule'
    assert isinstance(CacheModule.do_cache_del, BaseFileCacheModule._del)
    assert isinstance(CacheModule.do_cache_get, BaseFileCacheModule._get)
    assert isinstance(CacheModule.do_cache_set, BaseFileCacheModule._set)

# Generated at 2022-06-13 11:35:13.263335
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a CacheModule object.
    obj = CacheModule()
    assert obj._options is not None
    assert obj._connection is not None
    assert obj._prefix is not None
    assert obj._timeout is not None
    assert obj._load_from_file is not None
    assert obj._dump_to_file is not None

# Generated at 2022-06-13 11:35:19.635956
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor uses ConfigParser for configuration.
    # ConfigParser does not raise exception for bad configuration.
    # Hence, do not test constructor, but do test _load and _dump methods.
    #
    # Skip execution of _load and _dump tests, if JSON support is missing.
    # Given an empty file, _load should raise exception, if JSON support is missing.
    # Given an empty file, _dump should raise exception, if JSON support is missing.
    try:
        cm = CacheModule()
        value = cm._load('./test_files/empty.txt')
    except Exception:
        return

    # Given an empty file, _load should return an empty value.
    assert (value == {})

    # Given an empty file, _dump should create an empty file.
    cm._dump({}, './test_files/empty.txt')

# Generated at 2022-06-13 11:35:26.027620
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    cache_module.set_options({'_uri': 'my_uri', '_prefix': 'my_prefix', '_timeout': 'my_timeout'})
    assert cache_module.get_options()['_uri'] == 'my_uri'
    assert cache_module.get_options()['_prefix'] == 'my_prefix'
    assert cache_module.get_options()['_timeout'] == 'my_timeout'
    cache_module.flush()

# Generated at 2022-06-13 11:35:29.692403
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule()
    assert x
    try:
        x._load("")
        assert False
    except NotImplementedError:
        assert True
    try:
        x._dump("", "")
        assert False
    except NotImplementedError:
        assert True

# Generated at 2022-06-13 11:35:33.990998
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_obj = CacheModule()
    assert cache_obj is not None
    assert cache_obj._timeout == 86400
    assert cache_obj._options['_prefix'] is None
    assert cache_obj._options['_uri'] is None
    return cache_obj

# Generated at 2022-06-13 11:37:34.096264
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.utils.path import makedirs_safe
    from ansible.plugins.cache import BaseFileCacheModule
    from ansible.plugins.cache import class_name_to_filename
    from tempfile import mkdtemp
    from shutil import rmtree

    cache_dir = mkdtemp()

# Generated at 2022-06-13 11:37:36.804763
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule({'_uri': 'test'})
    assert c._uri == 'test'
    assert c._prefix == 'ansible_facts'
    assert c._timeout == 86400

# Generated at 2022-06-13 11:37:37.961163
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c


# Generated at 2022-06-13 11:37:39.390519
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule({})

# Generated at 2022-06-13 11:37:40.655565
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c

# Generated at 2022-06-13 11:37:47.002313
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''
    Unit test for constructor of class CacheModule
    '''

    from ansible.cache import CacheModule
    from ansible.module_utils.six import string_types

    # Construct an instance of class CacheModule with params
    # _load and _dump are private function in class CacheModule
    # and should not be passed to __init__ of class CacheModule
    cache = CacheModule({'_load': 'this is _load', '_dump': 'this is _dump'})

    assert cache._timeout == 86400
    assert cache._prefix is None
    assert isinstance(cache._connection, string_types)

    # Construct an instance of class CacheModule without params
    cache = CacheModule({})

    assert cache._timeout == 86400
    assert cache._prefix is None
    assert isinstance(cache._connection, string_types)

# Generated at 2022-06-13 11:37:54.243898
# Unit test for constructor of class CacheModule
def test_CacheModule():
    config = dict(
        _uri='/tmp',
        _prefix='unit_test_',
        _timeout=300,
    )

    cache = CacheModule(config)

    assert cache._config == config
    assert config['_uri'] == '/tmp'
    assert config['_prefix'] == 'unit_test_'
    assert config['_timeout'] == 300

# Generated at 2022-06-13 11:37:56.682034
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin._connection is None
    assert cache_plugin._prefix == ''

# Generated at 2022-06-13 11:37:57.311433
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert True

# Generated at 2022-06-13 11:37:58.172808
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module != None