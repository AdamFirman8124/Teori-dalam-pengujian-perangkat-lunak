

# Generated at 2022-06-12 21:10:56.757873
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    manager = ConfigManager()
    manager.load()
    from ansible.constants import DEFAULT_HOST_LIST, DEFAULT_PATTERN, DEFAULT_REMOTE_TMP, DEFAULT_LOCAL_TMP, DEFAULT_MODULE_PATH

    def test_config_value_and_origin(config, value, origin):
        assert(manager.get_config_value_and_origin(config)[0] == value)
        assert(manager.get_config_value_and_origin(config)[1] == origin)

    test_config_value_and_origin('inventory', DEFAULT_HOST_LIST, 'default')
    test_config_value_and_origin('pattern', DEFAULT_PATTERN, 'default')

# Generated at 2022-06-12 21:11:05.032707
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    # TODO: unit test for method get_config_value_and_origin
    #assert True == False
    cm = ConfigManager()
    args = [ '-vvvv', '-a', 'uptime' ]
    config = 'verbosity'
    cfile = None
    plugin_type = None
    plugin_name = None
    keys = None
    variables = None
    direct = cm.parse_options(args)
    r = cm.get_config_value_and_origin(config, cfile=cfile, plugin_type=plugin_type, plugin_name=plugin_name,
                                       keys=keys, variables=variables, direct=direct)
    print(r)



# Generated at 2022-06-12 21:11:10.859317
# Unit test for function ensure_type
def test_ensure_type():
    assert ensure_type('123', 'float') == '123'
    assert ensure_type('3.1415', 'float') == '3.1415'
    assert ensure_type('3.1415', 'int') == '3'
    assert ensure_type('3.99999', 'int') == '3'
    assert ensure_type(b'a string', 'str') == 'a string'
    assert ensure_type(b' True ', 'bool') is True
    assert ensure_type(b'FALSE', 'bool') is True
    assert ensure_type(b'False', 'bool') is True
    assert ensure_type(b' no ', 'bool') is False
    assert ensure_type('no', 'bool') is False
    assert ensure_type('no', 'bool') is False

# Generated at 2022-06-12 21:11:21.855727
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # For this test, we want to ignore any existing configs on the filesystem, but
    # we want to assert that if any of those exist, that we don't error. To do that,
    # we delete those existing paths before running the test so that they won't exist

    tmpdirs = []

    def create_fake_config_dir(path):
        ''' Creates a fake config directory in the temp directory. '''
        dirname = os.path.join(path, "ansible")
        makedirs_safe(dirname, 0o700)

        config_path = os.path.join(dirname, "ansible.cfg")
        with open(config_path, 'w') as f:
            f.write("[defaults]\n")

# Generated at 2022-06-12 21:11:30.357764
# Unit test for function get_ini_config_value
def test_get_ini_config_value():
    assert get_ini_config_value(None, None) is None
    p = configparser.SafeConfigParser()
    assert get_ini_config_value(p, None) is None
    p.readfp(io.BytesIO(b'''
[defaults]
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
[inventory]
localhost
[privilege_escalation]
become=True
[paramiko_connection]
no_agent=False
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersistent=60s -o ControlPath=~/.ssh/ansible-%%h-%%p-%%r
'''))
    assert get_ini_config_value(p, None) is None

# Generated at 2022-06-12 21:11:38.329063
# Unit test for function resolve_path
def test_resolve_path():
    def mygetcwd():
        return 'current-working-directory'
    old_getcwd = os.getcwd

# Generated at 2022-06-12 21:11:41.211821
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():

    config_manager=ConfigManager()
    plugin_type=None
    name=None
    ignore_private=False
    ret=config_manager.get_configuration_definitions(plugin_type, name, ignore_private)
    assert isinstance(ret, dict)
    assert isTrue(ret)


# Generated at 2022-06-12 21:11:47.361761
# Unit test for function resolve_path
def test_resolve_path():
    assert resolve_path('', 'default-basedir') == 'default-basedir'
    assert resolve_path('/tmp') == '/tmp'
    assert resolve_path('/tmp', '/tmp/cwd') == '/tmp'
    assert resolve_path('/tmp/../tmp') == '/tmp'
    assert resolve_path('/tmp/.././tmp') == '/tmp'
    assert resolve_path('/./tmp') == '/tmp'
    assert resolve_path('../tmp') == '../tmp'
    assert resolve_path('/tmp', '/tmp/cwd') == '/tmp'
    assert resolve_path('../../tmp', '/tmp/cwd') == '../../tmp'
    assert resolve_path('../.././tmp', '/tmp/cwd') == '../../tmp'

# Generated at 2022-06-12 21:11:48.737268
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    manager = ConfigManager()
    manager.get_configuration_definitions(plugin_type=None, name=None, ignore_private=None)
    pass



# Generated at 2022-06-12 21:11:52.918829
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    from ansible.utils.path import makedirs_safe

    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as tmp:
        pass
