

# Generated at 2022-06-13 11:29:19.836807
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert isinstance(cm.get_timeout(), int)

# Generated at 2022-06-13 11:29:21.797797
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)

# Generated at 2022-06-13 11:29:27.543188
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert cache_plugin._load('hosts') == cache_plugin.file_load('hosts')
    assert cache_plugin._dump('test_value', 'hosts') == cache_plugin.file_dump('test_value', 'hosts')

# Generated at 2022-06-13 11:29:28.440852
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c = CacheModule()

# Generated at 2022-06-13 11:29:34.692875
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()

    print("_cache_files_dir=" + cacheModule._cache_files_dir)
    print("_cache_prefix=" + cacheModule._cache_prefix)
    print("_cache_timeout=" + str(cacheModule._cache_timeout))



# Generated at 2022-06-13 11:29:36.939596
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_module = CacheModule()

    assert cache_module is not None


# Generated at 2022-06-13 11:29:39.841242
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/some/dir/'
    timeout = 100

    assert CacheModule({'_uri': cache_dir}).cache
    assert CacheModule({'_uri': cache_dir, '_prefix': 'pre'}).cache
    assert CacheModule({'_uri': cache_dir, '_timeout': timeout}).cache

# Generated at 2022-06-13 11:29:41.387111
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule(None,
                       {"_uri": "any/path"},
                       prefix='someprefix',
                       timeout=3600) is None

# Generated at 2022-06-13 11:29:42.411140
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__

# Generated at 2022-06-13 11:29:46.622817
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module == {   "plugin": "jsonfile", 
                         "connection": "", 
                            "timeo": "",
                            "path": "", 
                         "content": {}, 
                            "sha1": None }

# Generated at 2022-06-13 11:29:53.350331
# Unit test for constructor of class CacheModule
def test_CacheModule():

    # Create instance of cachedir module
    c = CacheModule()

    # Assert that _cache_dir is set to /tmp
    assert c._cache_dir == '/tmp'

    # Assert that _timeout is set to 86400
    assert c._timeout == 86400


# Generated at 2022-06-13 11:29:54.209962
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:29:55.729800
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._prefix == 'ansible-factcache'

# Generated at 2022-06-13 11:29:57.846311
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor of class CacheModule
    cm = CacheModule()
    assert cm.get_option('_timeout') == 86400

# Generated at 2022-06-13 11:29:58.413588
# Unit test for constructor of class CacheModule
def test_CacheModule():
	pass

# Generated at 2022-06-13 11:30:01.080878
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache.name == 'jsonfile'
    assert cache._load
    assert cache._dump
    assert cache._timeout == 86400
    assert cache._connection == None

# Generated at 2022-06-13 11:30:04.109152
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print('Testing CacheModule class')
    cache_module = CacheModule()
    assert cache_module.cache_prefix('localhost') == 'localhost_ansible_fact_cache'
    print('done.')



# Generated at 2022-06-13 11:30:06.130606
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Test empty constructor
    cache_jsonfile = CacheModule()
    assert cache_jsonfile.get_options() == {'_uri': '', '_prefix': 'ansible_facts', '_timeout': 86400}

# Generated at 2022-06-13 11:30:11.996679
# Unit test for constructor of class CacheModule
def test_CacheModule():
   import tempfile
   tempdir = tempfile.mkdtemp()
   print(tempdir)

   t = CacheModule({'_uri': tempdir, '_timeout': 86400, '_prefix': 'test_CacheModule'})
   assert t._prefix == 'test_CacheModule'
   assert t._timeout == 86400
   assert t._uri == tempdir
   assert t._load == t.load
   assert t._dump == t.dump


# Generated at 2022-06-13 11:30:18.849144
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_plugin = CacheModule()
    assert "cache" in cache_plugin.get_valid_cache_types()
    assert cache_plugin.validate_plugin_configuration() is True
    cache_plugin._uri = True
    assert cache_plugin.validate_plugin_configuration() is False
    cache_plugin._uri = False
    cache_plugin._timeout = True
    assert cache_plugin.validate_plugin_configuration() is False
    cache_plugin._timeout = False
    cache_plugin._prefix = True
    assert cache_plugin.validate_plugin_configuration() is False

# Unit tests for constructor of class CacheModule with options

# Generated at 2022-06-13 11:30:23.066636
# Unit test for constructor of class CacheModule
def test_CacheModule():
    try:
        cm = CacheModule()
        assert True
    except:
        assert False

# Generated at 2022-06-13 11:30:26.402908
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("test_CacheModule")
    cm = CacheModule()
    print(cm)
    assert cm
    #print("dir(cm) => %s"%dir(cm))
    return


# Generated at 2022-06-13 11:30:27.771659
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:30:31.267141
# Unit test for constructor of class CacheModule
def test_CacheModule():
    file_name = "/tmp/file_name"
    cache = CacheModule()
    assert cache._prefix == 'ansible-facts'
    assert cache._timeout == 86400
    assert cache._load(file_name) == {}

# Generated at 2022-06-13 11:30:33.796517
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # test_CacheModule is not a real test. This constructor is just needed to show the documentation.
    cm = CacheModule()
    # no further tests, as this is an abstract class

# Generated at 2022-06-13 11:30:34.664342
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cacheModule = CacheModule()

# Generated at 2022-06-13 11:30:36.317283
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule( { '_uri': '/tmp' } )
    assert cache is not None

# Generated at 2022-06-13 11:30:39.994061
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_obj = CacheModule(parms={'_uri':'/tmp/ansible_test', '_timeout':86400})
    assert cache_obj.timeout == 86400
    assert cache_obj.plugin_name == 'JSON file'

# Generated at 2022-06-13 11:30:49.958078
# Unit test for constructor of class CacheModule
def test_CacheModule():
    
    #test_CacheModule_on_empty_uri
    try:
        CacheModule(dict())
    except:
        print('test_CacheModule_on_empty_uri passed')

    #test_CacheModule_with_uri_and_prefix
    cm = CacheModule({'_uri':'/tmp/_ansible_caching',
                      '_prefix':'ansible'})
    assert cm._prefix == 'ansible'
    assert cm._basedir == '/tmp/_ansible_caching'

    #test_CacheModule_with_uri_and_no_prefix
    cm = CacheModule({'_uri':'/tmp/_ansible_caching'})
    assert cm._prefix == ''
    assert cm._basedir == '/tmp/_ansible_caching'

    #test_CacheModule_with_uri_and_prefix_and

# Generated at 2022-06-13 11:30:56.855519
# Unit test for constructor of class CacheModule
def test_CacheModule():
    print("Type of class 'CacheModule' changed to <class 'ansible.plugins.cache.jsonfile.CacheModule'>")

# Making all methods of class as private
#def __init__(self, *args, **kwargs):
#def _load(self,filepath):
#def _dump(self,value,filepath):

# Generated at 2022-06-13 11:31:03.875633
# Unit test for constructor of class CacheModule
def test_CacheModule():
    CacheModule({}, dict())

# Generated at 2022-06-13 11:31:07.125584
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_dir = '/tmp/ansible-test-dir'
    test_timeout = 42
    cache = CacheModule({'_uri': test_dir, '_timeout': test_timeout})

    assert cache is not None
    assert cache._prefix == 'ansible-facts'
    assert cache._directory == test_dir
    assert cache._timeout == test_timeout

# Generated at 2022-06-13 11:31:09.535674
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert isinstance(cache, CacheModule)

# Generated at 2022-06-13 11:31:10.011295
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:31:11.516646
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_m = CacheModule()
    from ansible.plugins.cache import CacheModule
    assert isinstance(cache_m,CacheModule)


# Generated at 2022-06-13 11:31:13.485987
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filepath = '/tmp/file.tmp'
    value = {'a':1}
    CacheModule()._dump(value, filepath)
    assert CacheModule()._load(filepath)['a'] == value['a']

# Generated at 2022-06-13 11:31:15.490946
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert cache._connection == '$HOME/.ansible/cache'
    assert cache._prefix == 'ansible-fact'
    assert cache._timeout == 86400



# Generated at 2022-06-13 11:31:19.763312
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule('testpath', 'testprefix', 3600)
    assert module.plugin_name == 'jsonfile'
    assert module._connection == 'testpath'
    assert module._prefix == 'testprefix'
    assert module._timeout == 3600

# Generated at 2022-06-13 11:31:23.139304
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # A none uri and prefix should raise an Exception
    try:
        cm = CacheModule()
    except Exception:
        pass

# Generated at 2022-06-13 11:31:23.772421
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm is not None

# Generated at 2022-06-13 11:31:40.240548
# Unit test for constructor of class CacheModule
def test_CacheModule():
    test_data = {'a': 1, 'b': 'bad_value', 'c': ['val1', 'val2', 'val3']}
    test_cache = CacheModule({'_uri': '/tmp/ansible/test'})
    test_cache.set('test_data', test_data)
    assert test_cache.get('test_data') == test_data

# Generated at 2022-06-13 11:31:44.780186
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache_dir = '/var/tmp/cachedir'
    expire = 86400
    file_prefix = 'prefix'
    cm = CacheModule({'_uri': cache_dir,
                      '_prefix': file_prefix,
                      '_timeout': expire})
    assert cm.cache_dir == cache_dir
    assert cm.expire == expire
    assert cm.file_prefix == file_prefix

# Generated at 2022-06-13 11:31:46.622306
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    assert(cache._load("c:\\temp\\f.json") == None)

# Generated at 2022-06-13 11:31:48.606193
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # create instance of class CacheModule
    cacheModule = CacheModule()
    assert isinstance(cacheModule, CacheModule)


# Generated at 2022-06-13 11:31:49.532472
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module != None

# Generated at 2022-06-13 11:31:51.140527
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Constructor should not have other options except for the ones that it takes
    assert CacheModule.OPTIONS == ['_connection']

# Generated at 2022-06-13 11:31:52.211753
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule.__doc__ == __doc__

# Generated at 2022-06-13 11:31:53.848375
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({u'_uri': u'/tmp/ansiblecachedir', u'_prefix': u'mypref'})

# Generated at 2022-06-13 11:31:58.668871
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # successful creation of a CacheModule object with valid input
    cache_module_obj = CacheModule()

    # test whether the object created is of type CacheModule
    assert isinstance(cache_module_obj, CacheModule), \
        "CacheModule object creation failed"

# Unit tests for _load() function

# Generated at 2022-06-13 11:31:59.862245
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule._add_host_prefix("foo") == "ansible-localhost-foo"

# Generated at 2022-06-13 11:32:25.646908
# Unit test for constructor of class CacheModule
def test_CacheModule():
    filename = ""
    CacheModule(filename)

# Generated at 2022-06-13 11:32:27.280428
# Unit test for constructor of class CacheModule
def test_CacheModule():
    ins = CacheModule(None)
    assert isinstance(ins, BaseFileCacheModule)

# Generated at 2022-06-13 11:32:29.613500
# Unit test for constructor of class CacheModule
def test_CacheModule():
    c=CacheModule()
    assert c.get_basedir() == "~/.ansible/tmp/ansible-fact-cache"

# Generated at 2022-06-13 11:32:30.858588
# Unit test for constructor of class CacheModule
def test_CacheModule():
    with CacheModule() as cm:
        print("Finished with {}".format(cm))

# Generated at 2022-06-13 11:32:34.436084
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Test constructor of class CacheModule"""
    cache = CacheModule()
    #print("CacheModule - test_CacheModule - cache:{}".format(cache))
    return cache


if __name__ == '__main__':
    cache = test_CacheModule()

# Generated at 2022-06-13 11:32:38.144424
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cache = CacheModule()
    cache.set('test_key', 'test_value')
    value = cache.get('test_key')
    assert value == 'test_value'


if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:32:40.247322
# Unit test for constructor of class CacheModule
def test_CacheModule():
	test = CacheModule()
	assert type(test) is CacheModule, 'Expected CacheModule'

# Test the _load function

# Generated at 2022-06-13 11:32:46.638131
# Unit test for constructor of class CacheModule
def test_CacheModule():
    temp_path = "/tmp"
    # Test that a file-cache module can be instantiated
    cm = CacheModule("jsonfile", temp_path)
    assert cm.__class__.__name__ == 'CacheModule'
    # Test that a file-cache module can be instantiated with a prefix
    cm = CacheModule("jsonfile", temp_path, prefix="prefix")
    assert cm.__class__.__name__ == 'CacheModule'
    # Test that a file-cache module can be instantiated with a timeout
    cm = CacheModule("jsonfile", temp_path, timeout=500)
    assert cm.__class__.__name__ == 'CacheModule'
    # Test that a file-cache module can be instantiated with a prefix and a timeout
    cm = CacheModule("jsonfile", temp_path, prefix="prefix", timeout=500)

# Generated at 2022-06-13 11:32:47.779489
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm.default_sep in ['/']

# Generated at 2022-06-13 11:32:50.338771
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Run the constructor.
    test_obj = CacheModule()
    assert isinstance(test_obj, CacheModule)
    assert isinstance(test_obj, BaseFileCacheModule)


# Unit tests for the class CacheModule.

# Generated at 2022-06-13 11:33:41.700233
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:33:48.798577
# Unit test for constructor of class CacheModule
def test_CacheModule():
    file = 'test.json'
    _timeout = 86400
    _uri = 'http://ansible.com'
    cm = CacheModule(file, _timeout, _uri)
    assert(cm._timeout == _timeout and cm._uri == _uri and cm._prefix == 'ansible_facts')

# Generated at 2022-06-13 11:33:50.666662
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin.get('foo') is None

# Test set/get without prefix and key foo

# Generated at 2022-06-13 11:33:51.176461
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule()

# Generated at 2022-06-13 11:33:52.048672
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module

# Generated at 2022-06-13 11:34:00.300561
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """ Unit test for CacheModule class of module jsonfile """

    # Define a class cache_plugin to test module jsonfile.
    class cache_plugin(object):

        # Initialize environment path variables.
        def __init__(self):
            self.env = {'ANSIBLE_CACHE_PLUGIN_CONNECTION': '/var/tmp', 'ANSIBLE_CACHE_PLUGIN_PREFIX': '', 'ANSIBLE_CACHE_PLUGIN_TIMEOUT': 86400}

        # Return environment path variables.
        def get_env(self, var):
            if var in self.env:
                return self.env.get(var)
            return None

    cache_p = cache_plugin()

    # Initialize base cache class.

# Generated at 2022-06-13 11:34:02.043378
# Unit test for constructor of class CacheModule
def test_CacheModule():
    plugin = CacheModule()
    assert plugin.myfile() == None

# Generated at 2022-06-13 11:34:03.982288
# Unit test for constructor of class CacheModule
def test_CacheModule():

    # Making sure CacheModule class is constructed
    assert CacheModule is not None

# Generated at 2022-06-13 11:34:14.194399
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Without specifying prefix, should load the defaults
    module = CacheModule()
    assert module.plugin_name == 'jsonfile'
    assert module.plugin_prefix == 'ansible_facts_'
    assert module.plugin_timeout == 86400
    assert module.plugin_connection == '/tmp/ansible_facts'

    # Specify the prefix, the default timeout should not change
    module = CacheModule(plugin_prefix='test_')
    assert module.plugin_name == 'jsonfile'
    assert module.plugin_prefix == 'test_'
    assert module.plugin_timeout == 86400
    assert module.plugin_connection == '/tmp/ansible_facts'

    # Specify the timeout, the default prefix should not change
    module = CacheModule(plugin_timeout=1000)
    assert module.plugin_name == 'jsonfile'


# Generated at 2022-06-13 11:34:15.631140
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert isinstance(module, CacheModule)

# Generated at 2022-06-13 11:36:15.016710
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Test the constructor of class CacheModule"""
    cache_module = CacheModule()
    assert cache_module._options['_uri'] is None
    assert cache_module._options['_prefix'] is None
    assert cache_module._options['_timeout'] is 86400


if __name__ == "__main__":
    # Unit test
    import pytest
    pytest.main(["-v", "jsonfile"])

# Generated at 2022-06-13 11:36:21.341782
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert isinstance(
        CacheModule(
            {
                '_uri': 'some_dir'
            }
        )._CacheModule__cache_dir,
        str
    )
    assert isinstance(
        CacheModule(
            {
                '_uri': 'some_dir',
                '_prefix': 'some_prefix'
            }
        )._CacheModule__cache_prefix,
        str
    )
    assert isinstance(
        CacheModule(
            {
                '_uri': 'some_dir',
                '_timeout': 'some_timeout'
            }
        )._CacheModule__timeout,
        int
    )

# Generated at 2022-06-13 11:36:23.975538
# Unit test for constructor of class CacheModule
def test_CacheModule():
    module = CacheModule()
    assert module is not None

if __name__ == '__main__':
    test_CacheModule()

# Generated at 2022-06-13 11:36:31.251110
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert issubclass(getattr(CacheModule, '__module__', None), 'ansible.plugins.cache') == True
    assert issubclass(CacheModule, object) == True
    assert issubclass(CacheModule, BaseFileCacheModule) == True
    assert hasattr(CacheModule, '__init__') == True
    assert hasattr(CacheModule, '_load') == True
    assert hasattr(CacheModule, '_dump') == True



# Generated at 2022-06-13 11:36:33.475672
# Unit test for constructor of class CacheModule
def test_CacheModule():
    x = CacheModule({'_uri': 'test', '_timeout': 86400})
    assert x

# Generated at 2022-06-13 11:36:35.375421
# Unit test for constructor of class CacheModule
def test_CacheModule():
    # Assert that the class can be instantiated without any exceptions.
    CacheModule()

# Generated at 2022-06-13 11:36:36.153285
# Unit test for constructor of class CacheModule
def test_CacheModule():
    pass

# Generated at 2022-06-13 11:36:37.215934
# Unit test for constructor of class CacheModule
def test_CacheModule():
    cm = CacheModule()
    assert cm


# Generated at 2022-06-13 11:36:39.499339
# Unit test for constructor of class CacheModule
def test_CacheModule():
    """Unit test for constructor of class CacheModule."""
    cache = CacheModule()
    assert cache is not None

# Generated at 2022-06-13 11:36:42.681058
# Unit test for constructor of class CacheModule
def test_CacheModule():
    assert CacheModule({
        '_prefix': 'test',
        '_timeout': 60,
        '_uri': 'ansible_test_path'
    }) is not None