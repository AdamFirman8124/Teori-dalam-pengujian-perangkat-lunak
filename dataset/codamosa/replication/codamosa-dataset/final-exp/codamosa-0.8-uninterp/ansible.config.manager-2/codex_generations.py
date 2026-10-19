

# Generated at 2022-06-12 21:13:33.664894
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type('/path/to/config.ini') == 'ini'
    assert get_config_type('/path/to/config.cfg') == 'ini'
    assert get_config_type('/path/to/config.yaml') == 'yaml'
    assert get_config_type('/path/to/config.yml') == 'yaml'
    try:
        get_config_type('/path/to/config.foo')
    except:
        pass
    else:
        raise AssertionError("function get_config_type should raise AnsibleOptionsError on invalid extension")


# FIXME: this could be shared with InventoryLoader, CLI options, etc

# Generated at 2022-06-12 21:13:36.247632
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    c = ConfigManager()
    c._base_defs['DEFAULT_DEBUG_CALLBACK'] = {}
    c._base_defs['DEFAULT_DEBUG_CALLBACK']['default'] = 'debug'
    c._base_defs['DEFAULT_DEBUG_CALLBACK']['type'] = 'str'
    c.get_config_value_and_origin('DEFAULT_DEBUG_CALLBACK', configfile=None)




# Generated at 2022-06-12 21:13:44.485713
# Unit test for function ensure_type
def test_ensure_type():
    class TestClass(object):
        def __str__(self):
            return 'str'

        def __repr__(self):
            return 'repr'

        def __unicode__(self):
            return 'unicode'

    # str
    assert ensure_type('', 'str') == u''
    assert ensure_type(u'', 'str') == u''
    assert ensure_type(b'', 'str') == u''
    assert ensure_type(TestClass(), 'str') == u'repr'

    # list
    assert ensure_type('', 'list') == [u'']
    assert ensure_type(u'', 'list') == [u'']

# Generated at 2022-06-12 21:13:52.777585
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    cwd = os.getcwd()
    if cwd.startswith("/tmp"):
        # We're running under tox. Skip this unit test.
        return

    # unset ANSIBLE_CONFIG so that we can find the default config
    if "ANSIBLE_CONFIG" in os.environ:
        del os.environ["ANSIBLE_CONFIG"]
    real_path = find_ini_config_file()
    assert real_path == "/etc/ansible/ansible.cfg"

    # Test that we ignore world-writable directories
    warnings = set()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = to_text(temp_dir, errors='surrogate_or_strict')

# Generated at 2022-06-12 21:13:59.877783
# Unit test for function resolve_path
def test_resolve_path():
    # test with relative path and follow = False
    assert resolve_path('./somefile','/some/dir') == '/some/dir/somefile'
    assert resolve_path('./somefile','/some/dir/') == '/some/dir/somefile'
    assert resolve_path('./somefile','/some/dir//') == '/some/dir/somefile'
    assert resolve_path('../somefile','/some/dir/subdir') == '/some/dir/somefile'
    # test with relative path and follow = True
    assert resolve_path('../somefile','/some/dir/subdir', True) == '/some/dir/somefile'
    # test with absolute path and follow = True
    assert resolve_path('/somefile','/some/dir', True) == '/somefile'
    # test with environment