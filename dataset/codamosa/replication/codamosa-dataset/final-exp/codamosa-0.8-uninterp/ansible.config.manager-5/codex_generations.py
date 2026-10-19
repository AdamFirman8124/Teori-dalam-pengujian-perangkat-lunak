

# Generated at 2022-06-12 21:08:48.900827
# Unit test for method get_plugin_vars of class ConfigManager
def test_ConfigManager_get_plugin_vars():
	name = 'fake_name'
	plugin_type = 'fake_plugin_type'

	defs = {'fake_option_name': {'vars': [{'name': 'fake_var_name'}]}}
	plugin = {'fake_name': defs}
	
	with patch.dict(ConfigManager._plugins, plugin):
		c = ConfigManager()
		result = c.get_plugin_vars(plugin_type, name)
		assert result == ['fake_var_name']


# Generated at 2022-06-12 21:08:55.297235
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type('./test.ini') == 'ini'
    # TODO: test must be updated after removing old config files
    # assert get_config_type('./test.conf') == 'ini'
    assert get_config_type('./test.yaml') == 'yaml'
    assert get_config_type('./test.yml') == 'yaml'
    try:
        get_config_type('./test.txt')
        # We should not get here
        assert False
    except AnsibleOptionsError:
        pass



# Generated at 2022-06-12 21:09:02.850843
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    c = ConfigManager()

# Generated at 2022-06-12 21:09:07.514151
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type('/foo/bar/ansible.cfg') == 'ini'
    assert get_config_type('/foo/bar/ansible.yml') == 'yaml'
    assert get_config_type('/foo/bar/ansible.yaml') == 'yaml'
    assert get_config_type('/foo/bar/ansible.foo') == None

# FIXME: generic file type?

# Generated at 2022-06-12 21:09:16.016183
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    from ansible.compat.mock import patch, mock_open

    def assert_find_config(env_config, cwd, home, etc, expected, expect_warning=False):
        """
        :type env_config: str | None
        :type cwd: str | None
        :type home: str | None
        :type etc: str | None
        :type expected: str | None
        :type expect_warning: bool
        """
        warning_msgs = []

        mocks = {
            '/etc/ansible/ansible.cfg': etc,
        }
        if env_config:
            mocks[env_config] = env_config.rstrip('cfg')

        if cwd:
            mocks[cwd] = cwd.rstrip('cfg')


# Generated at 2022-06-12 21:09:21.665002
# Unit test for function resolve_path
def test_resolve_path():
    '''Unit test for function resolve_path'''
    # Test data generated with the following python code,
    # which should be kept in sync with the actual code
    # in the function.
    #
    # import os
    #
    # def test_resolve_path(path, expected):
    #     if '{{CWD}}' in path:
    #         path = path.replace('{{CWD}}', os.getcwd())
    #     actual = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
    #     if actual != expected:
    #         print('%r != %r' % (actual, expected))
    #
    # test_resolve_path('/home/user/path',     '/home/user/path')
    # test_res

# Generated at 2022-06-12 21:09:31.445318
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    class Test(object):
        class ParsingException(Exception):
            pass
        class AnsibleError(Exception):
            pass
        class AnsibleOptionsError(Exception):
            pass
        def __init__(self, file_type, parser, config_file):
            self.file_type = file_type
            self.parser = parser
            self.config_file = config_file
        def get_configuration_definition(self, name, plugin_type=None, plugin_name=None):
            if name in self.parser:
                return self.parser[name]
            else:
                return {}
        def _parse_config_file(self, configfile):
            if configfile == 'bad_ini':
                raise self.ParsingException("")
            return

# Generated at 2022-06-12 21:09:42.707272
# Unit test for method initialize_plugin_configuration_definitions of class ConfigManager
def test_ConfigManager_initialize_plugin_configuration_definitions():
    A = ConfigManager()
    B = ConfigManager()

    assert A is not B

    A.initialize_plugin_configuration_definitions("plugin_type", "name", {"CONFIG_FILE": {}})

    assert "plugin_type" in A._plugins
    print("Type of plugin: %s" % type(A._plugins["plugin_type"]))
    assert isinstance(A._plugins["plugin_type"], dict)
    assert "name" in A._plugins["plugin_type"]
    assert "CONFIG_FILE" in A._plugins["plugin_type"]["name"]
    assert len(A._plugins["plugin_type"]["name"]) == 1

    assert "plugin_type" in B._plugins

    print("Type of plugin: %s" % type(B._plugins["plugin_type"]))

#  Unit

# Generated at 2022-06-12 21:09:50.781346
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    import tempfile
    path = tempfile.mkdtemp()
    # The following is ordered the same as the code in find_ini_config_file.
    # Used to validate the results of the code.
    environ = {"ANSIBLE_CONFIG": os.path.join(path, "ansible.cfg")}
    os.mkdir(os.path.join(path, "ansible"))
    ansible_cfg = os.path.join(path, "ansible", "ansible.cfg")
    def setup_file(filename):
        if filename is None:
            return
        with open(filename, "w") as f:
            f.write("[defaults]\n")
    setup_file(environ["ANSIBLE_CONFIG"])
    setup_file(ansible_cfg)

# Generated at 2022-06-12 21:09:58.251201
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    import ansible

    ##############################################################################
    # Set up the config manager
    cm = ConfigManager()
    
    # Build config file

# Generated at 2022-06-12 21:12:20.231719
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    global find_ini_config_file
    import shutil
    import tempfile
    import os
    import stat
    import warnings

    find_ini_config_file_orig = find_ini_config_file
    def find_ini_config_file_w_mock(warnings):
        find_ini_config_file = find_ini_config_file_orig
        return find_ini_config_file(warnings)
    find_ini_config_file = find_ini_config_file_w_mock

    class fake_open(object):
        exists = False
        def __init__(self, path, mode):
            self.file = open(path, mode)
            fake_open.exists = True
        def __enter__(self):
            return self.file

# Generated at 2022-06-12 21:12:25.151480
# Unit test for function resolve_path
def test_resolve_path():
    # Test cwd and tmp directories with relative path
    pwd = os.getcwd()
    assert resolve_path("./data") == os.path.join(pwd, "data")
    assert resolve_path("./data1/../data") == os.path.join(pwd, "data")
    tempdir = tempfile.mkdtemp()
    assert resolve_path(os.path.join(tempdir, "data")) == os.path.join(tempdir, "data")
    # Test cwd and tmp directories with absolute path
    assert resolve_path("/data") == "/data"
    assert resolve_path(os.path.join(tempdir, "/data")) == os.path.join(tempdir, "/data")
    os.rmdir(tempdir)



# Generated at 2022-06-12 21:12:33.264548
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible import constants
    from ansible.errors import AnsibleError, AnsibleOptionsError
    from ansible.module_utils import common_koji, common_splunk, common_gce
    from ansible.plugins.connection.winrm import Connection as ConnectionWinRM
    from ansible.plugins.connection.paramiko_ssh import Connection as ConnectionParamiko
    from ansible.utils.display import Display
    import shutil
    import tempfile
    import os

    display = Display()
    config_manager = ConfigManager(None, constants.ConfigManager._DEFAULT_CONFIG_FILE, display)
    config_manager.parse_config_files()

    const_file = tempfile.mkstemp()[1]
    os.environ["ANSIBLE_CONFIG"] = const_file

# Generated at 2022-06-12 21:12:36.653235
# Unit test for function resolve_path
def test_resolve_path():
    # Test the behavior of resolving paths with and without variable expansion.
    # Ideally we could test all possible variable expansions, but with assertRaises
    # it is hard to do that in an elegant way.
    assert resolve_path('home/user') == 'home/user'
    assert resolve_path('/home/{{user}}') == '/home/{{user}}'



# Generated at 2022-06-12 21:12:44.201403
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    import ansible.constants as C
    import ansible.parsing.dataloader as dataloader
    import ansible.playbook.play_context as play_context

    config_manager = ConfigManager()
    options = config_manager._read_config_data(None)
    options.update(C.configuration_definitions)
    config_manager.initialize(options, os.path.join(C.DEFAULT_CONFIG_FILE, C.CONFIG_FILE_NAME))

    loader = dataloader.DataLoader()
    context = play_context.PlayContext()

    assert config_manager.get_config_value('host_key_checking') == C.DEFAULT_HOST_KEY_CHECKING

# Generated at 2022-06-12 21:12:51.780481
# Unit test for function ensure_type
def test_ensure_type():
    import pytest
    assert None == ensure_type(None, 'none')
    assert None == ensure_type('None', 'none')
    assert None == ensure_type('', 'none')
    assert None == ensure_type(None, 'int')
    assert 42 == ensure_type(42, 'int')
    assert 42 == ensure_type('42', 'int')
    assert 42 == ensure_type('42', 'integer')
    assert 3.14 == ensure_type('3.14', 'float')
    assert True == ensure_type(True, 'bool')
    assert True == ensure_type('True', 'bool')
    assert False == ensure_type(False, 'boolean')
    assert False == ensure_type('False', 'boolean')

    assert '/tmp' == ensure_type('/tmp', 'path')

# Generated at 2022-06-12 21:13:00.249893
# Unit test for function ensure_type
def test_ensure_type():
    # boolean is lower of bool
    assert isinstance(ensure_type('true', 'bool'), bool)
    assert isinstance(ensure_type('True', 'boolean'), bool)
    # integers
    assert isinstance(ensure_type('14', 'int'), int)
    assert isinstance(ensure_type('14', 'integer'), int)
    # floats
    assert isinstance(ensure_type('14', 'float'), float)
    assert isinstance(ensure_type('14.0', 'float'), float)
    assert ensure_type('14.0', 'float') == 14.0
    assert ensure_type('14', 'float') == 14.0
    # list
    assert isinstance(ensure_type('a,b,c', 'list'), list)

# Generated at 2022-06-12 21:13:09.967633
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    data = '''
[defaults]
[ssh_connection]

context_path = /api/v2
host = localhost
port = 80
private_key_file =
remote_user = postgres
ssh_common_args =
ssh_executable = ssh
ssh_extra_args =
ssh_parallel = False
ssh_private_key_file =
timeout = 10
'''
    fd, pb_cfg = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        f.write(data)
    cfg = ConfigManager()
    cfg._parse_config_file(pb_cfg)
    value, origin = cfg.get_config_value_and_origin('context_path', cfile=pb_cfg)
    assert value == '/api/v2'

# Generated at 2022-06-12 21:13:18.598972
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    #Test with no ANSIBLE_CONFIG set
    assert find_ini_config_file() == unfrackpath("~/.ansible.cfg", follow=False)

    #Test with ANSIBLE_CONFIG set
    os.environ['ANSIBLE_CONFIG'] = "/tmp/test_find_ini_config_file"
    assert find_ini_config_file() == "/tmp/test_find_ini_config_file"
    os.unsetenv('ANSIBLE_CONFIG')

    #Test with ini file in cwd
    cwd = os.getcwd()
    perms = os.stat(cwd)
    cwd_cfg = os.path.join(cwd, "ansible.cfg")

# Generated at 2022-06-12 21:13:26.610971
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    expected_paths = [
        '~/.ansible.cfg',
        '/etc/ansible/ansible.cfg'
    ]
    # Test if the function returns the expected paths list if there is no ANSIBLE_CONFIG defined
    assert expected_paths == find_ini_config_file(warnings=None)

    # Test if the function returns the ANSIBLE_CONFIG path if there is one defined
    os.environ['ANSIBLE_CONFIG'] = '/test/my.cfg'
    assert '/test/my.cfg' == find_ini_config_file(warnings=None)

