

# Generated at 2022-06-13 11:29:19.694704
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._encoder_class == AnsibleJSONEncoder
    assert cache._decoder_class == AnsibleJSONDecoder

# Generated at 2022-06-13 11:29:20.337682
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()

# Generated at 2022-06-13 11:29:20.970214
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:29:22.269192
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(CacheModule, BaseFileCacheModule)

# Generated at 2022-06-13 11:29:26.862263
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule(task_vars=dict(ansible_facts=dict(foo='bar')))
    assert cache._task_vars == dict(ansible_facts=dict(foo='bar'))

# Generated at 2022-06-13 11:29:29.678634
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None
    assert isinstance(c, CacheModule)


# Generated at 2022-06-13 11:29:34.698981
# Unit test for constructor of class CacheModule
def test_CacheModule():
    uri = './tmp/ansible_cache'
    prefix = 'ansible_cache'
    timeout = 86500

    CacheModule(uri=uri, prefix=prefix, timeout=timeout)

# Generated at 2022-06-13 11:29:35.569357
# Unit test for constructor of class CacheModule
def test_CacheModule():
    #TODO - implement test_CacheModule()
    assert()

# Generated at 2022-06-13 11:29:44.168885
# Unit test for constructor of class CacheModule

# Generated at 2022-06-13 11:29:44.565563
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:29:46.913352
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule()
    #Call to constructor passes

# Generated at 2022-06-13 11:29:48.266473
# Unit test for constructor of class CacheModule
def test_CacheModule():
	cacheModule = CacheModule()
	assert(type(cacheModule) == CacheModule)


# Generated at 2022-06-13 11:29:49.481625
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, BaseFileCacheModule)

# Generated at 2022-06-13 11:29:51.984596
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    assert isinstance(obj, CacheModule)

# Generated at 2022-06-13 11:29:52.447046
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule('/tmp/cache')

# Generated at 2022-06-13 11:29:54.668861
# Unit test for constructor of class CacheModule
def test_CacheModule():
    f = CacheModule()
    assert type(f._load) is  type(lambda: 1)
    assert type(f._dump) is  type(lambda: 1)

# Generated at 2022-06-13 11:29:57.667457
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(dict(timeout=10, _prefix='cachetest'), 'foo_')
    assert CacheModule(dict(timeout=10, _prefix='cachetest', _uri='/foo'), 'foo_')

# Generated at 2022-06-13 11:29:59.281861
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule is not None

# Generated at 2022-06-13 11:30:03.913785
# Unit test for constructor of class CacheModule
def test_CacheModule():
    class RunnerMock(object):
        def __init__(self):
            self.options = {}
            self.options['fact_caching_connection'] = '/tmp'

    runner_mock = RunnerMock()
    cache_module = CacheModule(runner_mock)
    assert cache_module.path == '/tmp'



# Generated at 2022-06-13 11:30:05.430115
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # A test plugin object
    module = CacheModule()

    assert module._options['_uri'] is None
    assert module._options['_timeout'] == 86400



# Generated at 2022-06-13 11:30:10.077114
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache import BaseFileCacheModule

    new = CacheModule()
    assert isinstance(new, CacheModule)
    assert isinstance(new, BaseFileCacheModule)

# Generated at 2022-06-13 11:30:12.100714
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cachemodule = CacheModule()
    assert(isinstance(cachemodule, CacheModule))
    assert(cachemodule.get_timeout() == 86400)



# Generated at 2022-06-13 11:30:15.687712
# Unit test for constructor of class CacheModule
def test_CacheModule():
    t = CacheModule()
    assert t._connection is None
    assert t._cachefile is None
    assert t._timeout == 86400
    assert not t._load_from_cache
    assert not t._write_to_cache
    assert t._cache_enabled

# Generated at 2022-06-13 11:30:18.504376
# Unit test for constructor of class CacheModule
def test_CacheModule():
    from ansible.plugins.cache.jsonfile import CacheModule
    assert CacheModule
    assert CacheModule.__doc__ == "    A caching module backed by json files."

# Generated at 2022-06-13 11:30:19.004761
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:22.605337
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/tmp/.ansible'
    timeout = 86400
    cache = CacheModule(cache_dir, timeout)
    assert cache._timeout == timeout
    assert cache._prefix == 'ansible-cache'
    assert cache._basedir == '/tmp/.ansible/ansible-cache'

# Generated at 2022-06-13 11:30:23.993895
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({})._uri == ''

# Generated at 2022-06-13 11:30:26.960218
# Unit test for constructor of class CacheModule
def test_CacheModule():
    '''
    This is a constructor unit test for class CacheModule.
    '''
    assert hasattr(CacheModule, '__init__')
    assert callable(CacheModule.__init__)


# Generated at 2022-06-13 11:30:30.324291
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule({
        '_prefix': 'test_jsonfile_',
        '_uri': '/tmp/ansible/cache'
    })

    assert module is not None, 'constructor of class CacheModule returned None'

# Generated at 2022-06-13 11:30:31.546967
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module is not None

# Generated at 2022-06-13 11:30:39.437789
# Unit test for constructor of class CacheModule
def test_CacheModule():
    ca = CacheModule(None, task_vars={'inventory_hostname': 'fake_hostname'})
    assert type(ca) == CacheModule

# Generated at 2022-06-13 11:30:41.109701
# Unit test for constructor of class CacheModule
def test_CacheModule():
    a = CacheModule()
    assert(a.origin == 'jsonfile')

# Generated at 2022-06-13 11:30:43.973577
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin is not None

if __name__ == '__main__':
    def main():
        plugin = CacheModule()
    main()

# Generated at 2022-06-13 11:30:44.571518
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:30:47.617169
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin.cache_dir == None
    assert cache_plugin.cache_prefix == None
    assert cache_plugin.cache_timeout == 86400
    

# Generated at 2022-06-13 11:30:50.751577
# Unit test for constructor of class CacheModule
def test_CacheModule():
  cache_data = {
        'host1': {'module1': 'module1_data'},
        'host2': {'module2': 'module2_data'}
    }
  CacheModule(base_path='./test/cached', data=cache_data)


# Generated at 2022-06-13 11:30:55.702675
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c._prefix == ''
    assert c._timeout == 86400
    assert c._plugin_type == 'jsonfile'
    assert c._cache_dir is None
    assert c._load() == {}
    assert c._dump() == None


# Generated at 2022-06-13 11:30:56.531484
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule

# Generated at 2022-06-13 11:30:58.058719
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:31:04.674351
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

    assert cache_module._timeout == 86400
    assert cache_module._prefix == "ansible_fact_cache"
    assert cache_module._namespace == "cache"

    cache_module = CacheModule(prefix="prefix", timeout=100)

    assert cache_module._timeout == 100
    assert cache_module._prefix == "prefix"

# Generated at 2022-06-13 11:31:17.281436
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create object of class CacheModule
    cache = CacheModule()

    assert cache is not None

# Generated at 2022-06-13 11:31:19.904523
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    print(cache)

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

# Generated at 2022-06-13 11:31:23.164740
# Unit test for constructor of class CacheModule
def test_CacheModule():
    obj = CacheModule()
    # _uri is required
    obj._uri = None
    assert not obj.get('test')
    # _uri is required
    obj._uri = None
    assert not obj.set('test', 'test')
    obj._uri = './.ansible/tmp'
    assert not obj.get('test')
    assert obj.set('test', 'test')

# Generated at 2022-06-13 11:31:24.120467
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache
    assert cache._load("setup/facts.cache") == {"localhost": {"ansible_facts": {}}}

# Generated at 2022-06-13 11:31:26.537014
# Unit test for constructor of class CacheModule
def test_CacheModule():
    #without passing any argument, DirectoryCache should not raise error
    cache_module = CacheModule()
    assert cache_module._load == CacheModule._load
    assert cache_module._dump == CacheModule._dump

# Generated at 2022-06-13 11:31:29.569238
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule({'_timeout': 10, '_uri': 'test'})

    assert cache._timeout == 10
    assert cache._uri == 'test'
    assert cache._plugin_name == 'jsonfile'

# Generated at 2022-06-13 11:31:31.361697
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Create a new instance of class CacheModule
    cache = CacheModule()

    # Test the value of instance attributes
    assert cache._timeout == 86400

    # Test the return value of method "get"
    result = cache.get()
    assert result == {}
    assert type(result) == dict

# Generated at 2022-06-13 11:31:33.486193
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_path = "/var/tmp"
    cache = CacheModule(cache_path)
    assert cache._basedir == cache_path
    assert cache._timeout == 86400

# Generated at 2022-06-13 11:31:34.279310
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_class = CacheModule()

# Generated at 2022-06-13 11:31:36.430027
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.file_extension == 'json'
    assert cm.file_prefix == 'ansible-cache'

# Generated at 2022-06-13 11:32:02.437489
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin_connection = "test"
    cache_plugin_timeout = 1
    cache_plugin_prefix = "test"
    cache = CacheModule(cache_plugin_connection, cache_plugin_timeout, cache_plugin_prefix)
    assert cache._connection == cache_plugin_connection
    assert cache._timeout == cache_plugin_timeout
    assert cache._prefix == cache_plugin_prefix

# Generated at 2022-06-13 11:32:03.097686
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()

# Generated at 2022-06-13 11:32:08.613258
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test case1: uri is None and prefix is None,
    # test when it is not passed any arguments
    assert CacheModule() is not None

    # Test case2: uri is not None and prefix is not None,
    # test when it is passed the valid arguments
    cache_module = CacheModule(uri='/home/ansible/cache/', prefix='ansible', timeout=None)
    assert cache_module is not No

# Generated at 2022-06-13 11:32:10.775592
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = ControlModule(connection=None, module_name="")
    assert isinstance(cm, CacheModule)

# Generated at 2022-06-13 11:32:17.721045
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule() 
    assert cache_module.debug == False
    assert '_load' in dir(cache_module)
    assert '_dump' in dir(cache_module)
    assert 'get' in dir(cache_module)
    assert 'set' in dir(cache_module)
    assert 'keys' in dir(cache_module)
    assert 'contains' in dir(cache_module)
    assert 'delete' in dir(cache_module)
    assert 'flush' in dir(cache_module)
    assert 'get_stats' in dir(cache_module)

# Generated at 2022-06-13 11:32:23.390146
# Unit test for constructor of class CacheModule
def test_CacheModule():
    import os, tempfile, json

    # Create a temporary directory and data file, load with some data
    cache_dir = tempfile.mkdtemp()
    json_file = os.path.join(cache_dir, "ansible_file.json")
    data = { "a": 1, "b": 2, "c": 3, "d": { "a": "test" }, "e": [1, 2, 3] }

# Generated at 2022-06-13 11:32:24.648909
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_CacheModule = CacheModule()
    assert test_CacheModule

# Generated at 2022-06-13 11:32:25.645558
# Unit test for constructor of class CacheModule
def test_CacheModule():
  c = CacheModule()


# Generated at 2022-06-13 11:32:27.671829
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(cache.__class__.__name__ == 'CacheModule')

# Generated at 2022-06-13 11:32:30.977530
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        cache = CacheModule()
        cache.get('test', 'hihi')
    except Exception as e:
        print(e)
        print('test_CacheModule(): Fail')
        return

# test_CacheModule()

# Generated at 2022-06-13 11:33:17.311829
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert callable(CacheModule)

# Generated at 2022-06-13 11:33:18.542791
# Unit test for constructor of class CacheModule
def test_CacheModule():
    conn = CacheModule()
    assert conn._load.__name__ == '_load' and conn._dump.__name__ == '_dump' and conn.flush.__name__ == 'flush'

# Generated at 2022-06-13 11:33:23.113693
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # initial test object
    cache = CacheModule(1000, '', prefix='')
    # hard to test private methods, so here are the assertions
    assert cache._timeout == 1000
    assert cache._connection == ''
    assert cache._prefix == ''
    assert cache._load('/tmp/jack.json') == {}


# Generated at 2022-06-13 11:33:28.459687
# Unit test for constructor of class CacheModule
def test_CacheModule():
    connection = 'some/path/'
    cache_plugin_prefix = 'ansible_test_'
    cache_plugin_timeout = 1000
    cache_plugin_connection = connection
    cache_plugin_timeout = cache_plugin_timeout
    cache_plugin_prefix = cache_plugin_prefix

    cache = CacheModule()
    assert cache._connection == connection
    assert cache._timeout == cache_plugin_timeout
    assert cache._prefix == cache_plugin_prefix

# Generated at 2022-06-13 11:33:34.795543
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._timeout == 86400
    assert cache._prefix == 'ansible-facts'
    assert cache._load(cache._cache_dir + '/test') == None
    cache._dump("test", cache._cache_dir + '/test')
    result = {u'test': u'test'}
    assert cache._load(cache._cache_dir + '/test') == result

# Generated at 2022-06-13 11:33:41.384853
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # create an instance of class CacheModule
    test_cachemodule = CacheModule()
    # test if the object is an instance of CacheModule class
    assert isinstance(test_cachemodule, CacheModule)
    # test if the object is an instance of CacheModule class
    assert isinstance(test_cachemodule, BaseFileCacheModule)

# Generated at 2022-06-13 11:33:42.821542
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()


# Generated at 2022-06-13 11:33:43.338377
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule

# Generated at 2022-06-13 11:33:44.749274
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()

    assert(isinstance(module, CacheModule))
    assert(isinstance(module, BaseFileCacheModule))

# Generated at 2022-06-13 11:33:45.651387
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:35:27.188890
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin.get_cache_timeout() == 86400

# Generated at 2022-06-13 11:35:30.714973
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({
        "_uri": "ansible-test",
        "_prefix": "ansible-test",
        "_timeout": 86400
    }) == {
        "_uri": "ansible-test",
        "_prefix": "ansible-test",
        "_timeout": 86400
    }

# Generated at 2022-06-13 11:35:31.242578
# Unit test for constructor of class CacheModule
def test_CacheModule():
	assert CacheModule

# Generated at 2022-06-13 11:35:34.726242
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()
    assert cache_module.extension == '.json'
    assert cache_module._load("") == None
    assert cache_module._dump(None, "") == None

# Generated at 2022-06-13 11:35:38.323720
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule(None, dict(timeout=1, _uri='/test'), None, False)
    assert(c.timeout == 1)
    assert(c.plugin_name == '/test')
    assert(c._plugin_name == '/test')

# Generated at 2022-06-13 11:35:39.425422
# Unit test for constructor of class CacheModule
def test_CacheModule():
    mod = CacheModule()
    assert mod

# Generated at 2022-06-13 11:35:44.194157
# Unit test for constructor of class CacheModule
def test_CacheModule():
    my_cache = CacheModule({'_uri': 'tmp'})
    assert my_cache._connection == ('tmp',)
    assert my_cache._prefix == ''
    assert my_cache._timeout == 86400

    my_cache = CacheModule({'_uri': 'tmp', '_prefix': 'my', '_timeout': '3600'})
    assert my_cache._connection == ('tmp',)
    assert my_cache._prefix == 'my'
    assert my_cache._timeout == 3600

# Generated at 2022-06-13 11:35:44.996686
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()
    assert c is not None

# Generated at 2022-06-13 11:35:46.306813
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(None, task_vars={})

# Generated at 2022-06-13 11:35:47.156398
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin is not None