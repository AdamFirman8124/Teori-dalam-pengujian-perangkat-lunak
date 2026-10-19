

# Generated at 2022-06-12 21:09:19.057566
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    '''Unit test for method get_configuration_definitions of class ConfigManager'''

    # Setup
    # Tear down
    # Assertions
    raise ExceptionNotImplemented()



# Generated at 2022-06-12 21:09:20.513986
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    assert 'ansible.cfg' in find_ini_config_file()


# FIXME: can move to module_utils for use for yaml plugins also?

# Generated at 2022-06-12 21:09:30.825905
# Unit test for function get_config_type
def test_get_config_type():
    print("testing get_config_type()")
    test_config = [
        {'test_name': 'ini', 'test_file': 'test.ini', 'test_result': 'ini'},
        {'test_name': 'cfg', 'test_file': 'test.cfg', 'test_result': 'ini'},
        {'test_name': 'yaml', 'test_file': 'test.yaml', 'test_result': 'yaml'}
    ]

    for config in test_config:
        print("testing %s" % config['test_name'])
        result = get_config_type(config['test_file'])

# Generated at 2022-06-12 21:09:35.956765
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    config = ConfigManager('')
    # valid input types
    assert isinstance(config.get_configuration_definitions(), dict)
    assert isinstance(config.get_configuration_definitions('foo'), dict)
    assert isinstance(config.get_configuration_definitions('foo','bar'), dict)
    # invalid input types
    with pytest.raises(AssertionError):
        config.get_configuration_definitions(1)
    with pytest.raises(AssertionError):
        config.get_configuration_definitions('foo',1)


# Generated at 2022-06-12 21:09:40.355857
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # fakeos is used to test if the paths are expanded properly
    from ansible.module_utils import fakeos
    from ansible.module_utils.common._collections_compat import OrderedDict

    # Make sure fakeos is the default
    assert os is fakeos
    assert_is_expanded = OrderedDict()
    assert_is_not_expanded = OrderedDict()

    # Using SENTINEL to handle the case where ANSIBLE_CONFIG is not set
    SENTINEL = object

    # Build a fake version of os.path.expanduser because we can't mock it.
    fakeos.path.expanduser_dict = {}
    fakeos.path.expanduser_dict["/tmp"] = "/tmp"

# Generated at 2022-06-12 21:09:49.395104
# Unit test for function ensure_type
def test_ensure_type():
    assert ensure_type('ansible', 'string') == 'ansible'
    assert isinstance(ensure_type('1', 'int'), int)
    assert ensure_type('1', 'float') == 1.0
    assert ensure_type('dd,ee,ff', 'list') == ['dd', 'ee', 'ff']
    assert ensure_type(['1', '2', '3'], 'list') == ['1', '2', '3']
    assert ensure_type('', 'none') is None
    assert ensure_type('/tmp', 'tmp') == u'/tmp'
    assert ensure_type('/tmp', 'path') == u'/tmp'
    assert ensure_type(['/tmp', '/var/tmp'], 'pathlist') == [u'/tmp', u'/var/tmp']

# Generated at 2022-06-12 21:09:54.376857
# Unit test for function ensure_type
def test_ensure_type():
    assert ensure_type(1, 'integer') == u'1'
    assert ensure_type(1, 'str') == u'1'
    assert ensure_type('1', 'str') == u'1'
    assert ensure_type('1', 'float') == u'1.0'
    assert ensure_type(1.0, 'str') == u'1.0'
    assert ensure_type(1.0, 'integer') == u'1'
    assert ensure_type(True, 'str') == u'True'


# Generated at 2022-06-12 21:09:59.783220
# Unit test for function get_config_type
def test_get_config_type():
    '''
    Tests for get_config_type
    '''
    # Simple test. Uses default ansible config only
    data = get_config_type('/etc/ansible/ansible.cfg')
    assert data == 'ini'
    # invalid file
    try:
        data = get_config_type('/etc/ansible/ansible.cfg1')
        assert data is not None
    except AnsibleError as e:
        assert 'Unsupported configuration file extension for' in to_native(e)

    # YAML file
    data = get_config_type('/etc/ansible/ansible.yaml')
    assert data == 'yaml'


# Generated at 2022-06-12 21:10:03.904654
# Unit test for method get_plugin_vars of class ConfigManager
def test_ConfigManager_get_plugin_vars():
    config = ConfigManager()

# Generated at 2022-06-12 21:10:04.871224
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    assert find_ini_config_file() is not None
    assert os.path.isfile(find_ini_config_file()) is True

