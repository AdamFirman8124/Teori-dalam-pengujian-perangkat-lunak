

# Generated at 2022-06-13 11:29:20.719397
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert (module is not None)

# Generated at 2022-06-13 11:29:21.305355
# Unit test for constructor of class CacheModule
def test_CacheModule():
    f = CacheModule()

# Generated at 2022-06-13 11:29:26.239324
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    Constructor of CacheModule
    :return:
    """
    cm = CacheModule()
    assert cm._load('./test/unit/plugins/cache/files/fact_cache') == {'test': 'test'}
    assert cm._dump({'test': 'test'}, './test/unit/plugins/cache/files/test') == None

# Generated at 2022-06-13 11:29:27.061176
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:29:28.900236
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.plugin_name == 'jsonfile'
    assert cache.timeout == 86400


# Generated at 2022-06-13 11:29:42.282492
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import tempfile
    import shutil

    # Get a temporary directory
    test_dir = tempfile.mkdtemp()

    # Verify the class constructor with no arguments
    plugin_obj = CacheModule()
    assert(test_dir == plugin_obj.get_option('_uri'))
    assert('ansible_facts' == plugin_obj.get_option('_prefix'))
    assert(3600 == plugin_obj.get_option('_timeout'))

    # Verify the class constructor with arguments
    plugin_obj = CacheModule(CACHE_PLUGIN_CONNECTION=os.path.join(test_dir, 'test_connect'), CACHE_PLUGIN_PREFIX='unit_test', CACHE_PLUGIN_TIMEOUT=600)

# Generated at 2022-06-13 11:29:44.059019
# Unit test for constructor of class CacheModule
def test_CacheModule():
    if __name__ == '__main__':
        test_obj = CacheModule()
        print(test_obj)

# Generated at 2022-06-13 11:29:49.162284
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''Unit test for constructor of class CacheModule'''
    from ansible.plugins.cache.jsonfile import CacheModule
    uri_dir = '/tmp/cache_dir'
    prefix = 'prefix'

    cache_mod = CacheModule(uri_dir, prefix)

    assert(cache_mod.cache_dir == uri_dir)
    assert(cache_mod.prefix == prefix)

# Generated at 2022-06-13 11:29:54.611017
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_namespace = 'test_cache'
    data_structure = {'key': 'test_value'}
    instance = CacheModule(cache_namespace, data_structure)

    assert isinstance(instance, CacheModule)

# Generated at 2022-06-13 11:29:57.936428
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Get a CacheModule object from cache.py
    cache = CacheModule()

    # Check initial values for properties and attributes
    assert cache._load_function == cache._load
    assert cache._dump_function == cache._dump
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:30:01.918003
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({})

# Generated at 2022-06-13 11:30:04.925628
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test plain constructor
    c = CacheModule(dict())

    # Test constructor with extra lines, without the '-' character.
    c = CacheModule(dict(
        _uri='/tmp/ansible-cache'
    ))

# Generated at 2022-06-13 11:30:08.895414
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("\n# Unit test of the constructor of class CacheModule")
    # create the cache
    cache = CacheModule(task_vars=dict(ansible_facts=dict(ansible_os_facts=dict())))
    # print the path of the cache
    print("    cache path:", cache._connection._options['_uri'])


# Generated at 2022-06-13 11:30:10.760253
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule(None)
    assert cache_module._plugin_name == 'jsonfile'
    assert cache_module._timeout == 86400
    assert cache_module._prefix is None
    assert cache_module._connection is None

# Generated at 2022-06-13 11:30:13.117676
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars=dict())
    assert(isinstance(cache, CacheModule))

# Generated at 2022-06-13 11:30:14.918027
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'path': '/tmp/var/tmp'}, 'test.example.com')

# Generated at 2022-06-13 11:30:16.264265
# Unit test for constructor of class CacheModule
def test_CacheModule():
  assert True

# Generated at 2022-06-13 11:30:17.376042
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cached = CacheModule()


# Generated at 2022-06-13 11:30:17.918901
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:30:19.117184
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._timeout == 86400

# Generated at 2022-06-13 11:30:23.626172
# Unit test for constructor of class CacheModule
def test_CacheModule():
  print("Testing CacheModule constructor, this is a unit test")

#test_CacheModule()

# Generated at 2022-06-13 11:30:24.075017
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:25.913536
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({'_uri': '', '_prefix': '', '_timeout': ''})

# Generated at 2022-06-13 11:30:28.791544
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """
    This is a test for constructor of class CacheModule
    """
    module_args = {'_uri': '/tmp'}

    cache_moudle = CacheModule()
    cache_moudle.set_options(module_args)

# Generated at 2022-06-13 11:30:30.558813
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mgr = CacheModule()
    assert isinstance(mgr, CacheModule)

# Generated at 2022-06-13 11:30:31.753818
# Unit test for constructor of class CacheModule
def test_CacheModule():

    cache_plugin = CacheModule()

    assert cache_plugin._connection is None

# Generated at 2022-06-13 11:30:36.970030
# Unit test for constructor of class CacheModule
def test_CacheModule():
    path = '/path/to/cachedir'
    prefix = 'cache_'
    timeout = '3600'
    plugin = CacheModule()
    plugin.set_options(direct={"_uri": path, "_prefix": prefix, '_timeout': timeout})
    assert plugin.plugin_name == 'jsonfile'
    assert plugin._connection == '/path/to/cachedir'
    assert plugin._prefix == 'cache_'
    assert plugin._timeout == 3600

# Generated at 2022-06-13 11:30:42.424727
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule(load_options=dict(_uri="test_path", _prefix="test_prefix", _timeout="test_timeout"))
    assert obj.file_extension == '.json'
    assert obj.cachefile is None
    assert obj.cache_timeout == "test_timeout"

# Generated at 2022-06-13 11:30:46.748516
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm.configuration.get_configuration_value('_uri'), str)
    assert isinstance(cm.configuration.get_configuration_value('_prefix'), str)
    assert isinstance(cm.configuration.get_configuration_value('_timeout'), int)

# Generated at 2022-06-13 11:30:48.907859
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache._load, type(json.load))
    assert isinstance(cache._dump, type(json.dump))

# Generated at 2022-06-13 11:30:58.058303
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = "/tmp/json_cache"
    cache = CacheModule(uri, task_vars={})
    assert cache.hash_name == "jsonfile"

# Generated at 2022-06-13 11:31:01.059208
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm._options == {'_prefix': None, '_timeout': 86400, '_uri': None}

# Generated at 2022-06-13 11:31:06.443725
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import ansible.plugins.cache.jsonfile
    cm = ansible.plugins.cache.jsonfile.CacheModule()
    assert "ANSIBLE_CACHE_PLUGIN_CONNECTION" in cm.get_options()
    assert "ANSIBLE_CACHE_PLUGIN_TIMEOUT" in cm.get_options()
    assert "ANSIBLE_CACHE_PLUGIN_PREFIX" in cm.get_options()
    assert "ANSIBLERC" in cm.get_options()

# Generated at 2022-06-13 11:31:09.309064
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule('setup').__name__ == CacheModule.__name__

# Generated at 2022-06-13 11:31:10.591667
# Unit test for constructor of class CacheModule
def test_CacheModule():

    # Uncomment for debugging
    print(CacheModule())

# Generated at 2022-06-13 11:31:12.031662
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:31:22.450672
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    assert CacheModule.__name__ == 'CacheModule'
    assert CacheModule.__doc__ == '\n    A caching module backed by json files.\n    '
    assert CacheModule.data == {}
    assert CacheModule.default_timeout == 86400
    assert CacheModule.cache_plugin_name == 'jsonfile'
    assert isinstance(CacheModule.json_encoder, AnsibleJSONEncoder)
    assert isinstance(CacheModule.json_decoder, AnsibleJSONDecoder)
    assert CacheModule.supports_multiple() == True

# Generated at 2022-06-13 11:31:24.371235
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule('/tmp')
    assert cache_module


# Generated at 2022-06-13 11:31:24.908526
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:31:28.384770
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_obj = CacheModule({'_uri': "/tmp", '_prefix': 'ans'})
    assert cache_plugin_obj.__class__.__name__ == "CacheModule"

# Generated at 2022-06-13 11:31:47.112219
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    cache_plugin.set_options(direct)
    cache_plugin._load('/Users/aalvarez/Projects/ansible-workspace/cache_plugins/jsonfile/data')
    cache_plugin._dump({'jose': 'perez'}, '/Users/aalvarez/Projects/ansible-workspace/cache_plugins/jsonfile/data')
    print('Ejecucion de la prueba: SUCCESS')


if __name__ == '__main__':
    direct = {'_uri': '/Users/aalvarez/Projects/ansible-workspace/cache_plugins/jsonfile/data'}
    test_CacheModule()

# Generated at 2022-06-13 11:31:49.487468
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    print(c.__class__.__name__)

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:31:51.445091
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import ansible.plugins.cache.jsonfile
    cache_module = ansible.plugins.cache.jsonfile.CacheModule()
    assert cache_module

# Generated at 2022-06-13 11:31:57.230796
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._load == c.load
    assert c._dump == c.dump
    assert c._load('test_file') == json.load('test_file', cls=AnsibleJSONDecoder)
    assert c._dump('test_file', 'test_value') == json.dumps('test_file', 'test_value', cls=AnsibleJSONEncoder, sort_keys=True, indent=4)

# Generated at 2022-06-13 11:32:06.751814
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = 'test'
    test_cache = CacheModule(dict(), filename)
    test_cache_data = {"test": "test"}
    test_json = '{"test":"test"}'
    # Writing data to file
    test_cache.set(test_cache_data, filename)
    # Reading data from file
    cache_read = test_cache.get(filename)
    # Converting data to json format
    json_cache = json.dumps(cache_read, cls=AnsibleJSONEncoder, sort_keys=True, indent=4)
    if json_cache == test_json:
        print("test_CacheModule passed")
    else:
        print("test_CacheModule failed")

# Generated at 2022-06-13 11:32:08.514141
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module._load is not None
    assert cache_module._dump is not None

# Generated at 2022-06-13 11:32:09.771741
# Unit test for constructor of class CacheModule
def test_CacheModule():
    argVal = 86400
    cacheModule = CacheModule(argVal)
    assert argVal == cacheModule._timeout


# Generated at 2022-06-13 11:32:10.605664
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(None).__class__.__name__=='CacheModule'

# Generated at 2022-06-13 11:32:11.647955
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.type == 'jsonfile'
    assert CacheModule.priority == 0

# Generated at 2022-06-13 11:32:12.644062
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    print(cache)

# Generated at 2022-06-13 11:32:38.918695
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.cache_type == 'jsonfile'

# Generated at 2022-06-13 11:32:39.863472
# Unit test for constructor of class CacheModule
def test_CacheModule():
    myCache = CacheModule()

# Generated at 2022-06-13 11:32:41.553128
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_CacheModule = CacheModule({'_timeout': 1, '_prefix': 'TEST', '_uri': 'TEST'})
    assert test_CacheModule is not None

# Generated at 2022-06-13 11:32:43.332671
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert "jsonfile" == cache.namespace
    assert "jsonfile" == cache.default_suffix
    assert type(cache._timeout) is int

# Generated at 2022-06-13 11:32:46.938809
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = "/path/to/connection/file"
    prefix = "some-prefix"
    timeout = 900
    cache = CacheModule(connection=connection, prefix=prefix, timeout=timeout)
    assert cache._connection == connection
    assert cache._prefix == prefix
    assert cache._timeout == timeout

# Generated at 2022-06-13 11:32:48.043361
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()
    assert cacheModule is not None

# Generated at 2022-06-13 11:32:48.831902
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:32:52.940330
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import tempfile
    import os
    import pytest

    class DummyConfig:

        def __init__(self):
            self.fact_caching_connection = None
            self.fact_caching_timeout = 3600
            self.fact_caching_prefix = None

    class DummyModule:

        def __init__(self):
            self.params = None

    class DummyHost:

        # pylint: disable=unused-argument
        def __init__(self, host, config, *args, **kwargs):
            self.name = host

    class DummyInventory:

        def __init__(self, *args, **kwargs):
            self.hosts = {}


# Generated at 2022-06-13 11:32:59.239078
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_path = '/tmp/test'
    timeout = 3600
    plugin = CacheModule(timeout=timeout, cache_path=cache_path)
    assert plugin.cache_path == cache_path
    assert plugin.timeout == timeout

# Unit tests for constructor of class BaseFileCacheModule

# Generated at 2022-06-13 11:33:02.100859
# Unit test for constructor of class CacheModule
def test_CacheModule():
    __name__ = ''
    import ansible_collections.ansible.builtin.plugins.module_utils.cache.jsonfile

    module = CacheModule(__name__)
    assert module.CACHE_PLUGIN_PREFIX == 'ansible-factcache'
    assert module.CACHE_PLUGIN_TIMEOUT == 86400
    assert module.CACHE_PLUGIN_CONNECTION == '/tmp'

# Generated at 2022-06-13 11:33:52.641861
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule({'_uri': '_uri'})
    assert cm.plugin_name == 'jsonfile'


# Generated at 2022-06-13 11:33:53.771521
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

# Generated at 2022-06-13 11:33:55.029750
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None


# Generated at 2022-06-13 11:34:00.582293
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule(task=None, manager=None)
    assert m.lock_path is None
    assert m._timeout == 86400
    assert m._prefix == 'ansible_'
    assert m.cache_files_dir == '/tmp/ansible-fact-cache'


# Generated at 2022-06-13 11:34:04.122577
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # TODO: Mock the constructor of class BaseFileCacheModule.
    # TODO: test default values, _uri, _prefix, _timeout, _cachefile.
    pass


# Generated at 2022-06-13 11:34:06.720500
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.file_extension == ".json"
    assert cache.file_prefix == "ansible_fact_"

# Generated at 2022-06-13 11:34:11.282792
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os
    import tempfile

    data = {'param1': 'value1', 'param2': [1, 2, 3, 4], 'param3': {'subparam1': 1, 'subparam2': 2}}

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create instance of CacheModule
    cache = CacheModule({'_uri': temp_dir, '_timeout': '1'})
    cache.set('testkey', data)
    out = cache.get('testkey')
    assert(out == data)

    # Remove temporary directory
    os.rmdir(temp_dir)

# Generated at 2022-06-13 11:34:13.277728
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mod = CacheModule()
    assert mod._load == mod.load
    assert mod._dump == mod.dump

# Generated at 2022-06-13 11:34:13.892175
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:34:15.378352
# Unit test for constructor of class CacheModule
def test_CacheModule():
    instance = CacheModule()

    assert(isinstance(instance, CacheModule))

# Generated at 2022-06-13 11:36:10.416160
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create an instance of class CacheModule
    cache_module = CacheModule()
    # Check if parameter _load is of type function
    assert(callable(cache_module._load))
    # Check if parameter _dump is of type function
    assert(callable(cache_module._dump))
    # Check if parameter _exists is of type function
    assert(callable(cache_module._exists))
    # Check if parameter _remove is of type function
    assert(callable(cache_module._remove))
    # Check if parameter _list is of type function
    assert(callable(cache_module._list))
    # Check if parameter _get is of type function
    assert(callable(cache_module._get))
    # Check if parameter _set is of type function
    assert(callable(cache_module._set))

# Generated at 2022-06-13 11:36:11.243800
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_module = BaseFileCacheModule()

# Generated at 2022-06-13 11:36:11.745142
# Unit test for constructor of class CacheModule
def test_CacheModule():
    m = CacheModule()

# Generated at 2022-06-13 11:36:14.504745
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars={}, tmp_path='/home/tmp')
    assert cache.task_vars == {}, 'task_vars works ok'
    assert cache.tmp_path == '/home/tmp', 'tmp_path works ok'

# Generated at 2022-06-13 11:36:16.041662
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule(dict(persistent=True))
    assert isinstance(cm, CacheModule)

# Generated at 2022-06-13 11:36:22.609285
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os.path, os, shutil
    module = CacheModule()
    assert module._uri == os.path.expanduser('~/.ansible/tmp/ansible-local')
    assert module._timeout == 86400
    if os.path.exists(module._uri):
        shutil.rmtree(module._uri)
    os.makedirs(module._uri)
    data = {"test": "a"}
    module.set("test", data)
    # Check that data is saved to file
    assert module.get("test") == data
    # Check that file cache is deleted
    if os.path.exists(module._uri):
        shutil.rmtree(module._uri)

# Generated at 2022-06-13 11:36:23.320318
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule

# Generated at 2022-06-13 11:36:25.005312
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:36:31.810376
# Unit test for constructor of class CacheModule
def test_CacheModule():
    myname = "test_CacheModule"
    mypath = "/tmp"
    my_cache_module = CacheModule(myname,mypath)
    assert my_cache_module.name == myname
    assert my_cache_module.cache == {}
    assert my_cache_module.cache_max_age == 86400
    assert my_cache_module.cache_path == "/tmp/test_CacheModule"

# Generated at 2022-06-13 11:36:33.538126
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module._timeout == 86400