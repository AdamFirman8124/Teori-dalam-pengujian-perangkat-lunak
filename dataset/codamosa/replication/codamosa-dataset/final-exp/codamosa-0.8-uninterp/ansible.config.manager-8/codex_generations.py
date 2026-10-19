

# Generated at 2022-06-12 21:12:10.061283
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    # In this test we want to make sure that warning logic for cwd and
    # ANSIBLE_CONFIG works.
    warnings = set()
    path = find_ini_config_file(warnings=warnings)
    assert len(warnings) == 0
    assert path is not None

    # Try the test again, but this time drop a config in the cwd so that we get the warning
    warnings = set()
    path = find_ini_config_file(warnings=warnings)
    assert len(warnings) == 0
    assert path is not None

    # Try again with ANSIBLE_CONFIG
    os.environ['ANSIBLE_CONFIG'] = to_text(path)
    warnings = set()
    path = find_ini_config_file(warnings=warnings)

# Generated at 2022-06-12 21:12:18.002672
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type('/tmp/test.txt') == 'ini'
    assert get_config_type('/tmp/test.ini') == 'ini'
    assert get_config_type('/tmp/test.yaml') == 'yaml'
    assert get_config_type('/tmp/test.yml') == 'yaml'
    assert get_config_type(None) == None
    assert get_config_type('/tmp/test.cfg') == 'ini'
    #assert get_config_type('/tmp/test.txt') == 'ini'
    return True


# Generated at 2022-06-12 21:12:21.537644
# Unit test for function get_config_type
def test_get_config_type():
    test_vars = [['/path/to/config.ini', 'ini'],
                 ['/path/to/config.cfg', 'ini'],
                 ['/path/to/config.yml', 'yaml'],
                 ['/path/to/config.yaml', 'yaml']]

    for config_file, expected in test_vars:
        result = get_config_type(config_file)
        assert expected == result


# FIXME: see if we can do this in a more generic way with safe_load

# Generated at 2022-06-12 21:12:31.638163
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    saved_cwd = os.getcwd()
    saved_env = os.environ.get('ANSIBLE_CONFIG', None)
    os.environ['ANSIBLE_CONFIG'] = '/a/b/c/d'


# Generated at 2022-06-12 21:12:39.086723
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.constants import CONFIG_ARGS, CONFIG_FILE

    import pytest

    # Setup
    config_manager = ConfigManager(defs=CONFIG_ARGS, config_file=CONFIG_FILE)

    # Test
    with pytest.raises(AnsibleError):
        config_manager.get_config_value_and_origin('invalid_config')

    with pytest.raises(AnsibleError):
        config_manager.get_config_value_and_origin('ANSIBLE_CONFIG')

    with pytest.raises(AnsibleError):
        config_manager.get_config_value_and_origin('ANSIBLE_NOCOWS')

    result = config_manager.get_config_value_and_origin('ANSIBLE_COW_SELECTION')

# Generated at 2022-06-12 21:12:46.521669
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from ansible.module_utils.parsing.convert_bool import boolean
    cm = ConfigManager()
    cv = cm.get_config_value_and_origin
    cv = cm.get_config_value
    cv = cm.get_config_value_and_origin
    cv = cm.get_config_value
    cv = cm.get_config_value_and_origin
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value
    cv = cm.get_config_value

# Generated at 2022-06-12 21:12:52.021947
# Unit test for function get_config_type
def test_get_config_type():
    assert get_config_type("foo.ini") == 'ini'
    assert get_config_type("foo.cfg") == 'ini'
    assert get_config_type("foo.yaml") == 'yaml'
    assert get_config_type("foo.yml") == 'yaml'
    try:
        get_config_type("foo.xml")
        assert False
    except AnsibleOptionsError as e:
        assert "Unsupported configuration file extension" in e.message
    assert get_config_type(None) == None


# FIXME: generic file type?

# Generated at 2022-06-12 21:13:00.488973
# Unit test for function find_ini_config_file
def test_find_ini_config_file():
    import shutil
    import tempfile
    tmpdir = tempfile.mkdtemp()

    # ANSIBLE_CONFIG
    path_env = os.path.join(tmpdir, "ansible-env.cfg")
    os.environ['ANSIBLE_CONFIG'] = path_env
    path = find_ini_config_file()
    assert path == path_env
    del os.environ['ANSIBLE_CONFIG']

    # CWD
    cwd = os.getcwd()
    os.chdir(tmpdir)
    path_cwd = os.path.join(tmpdir, "ansible-cwd.cfg")
    path = find_ini_config_file()
    assert path == path_cwd

    # HOME

# Generated at 2022-06-12 21:13:10.260784
# Unit test for method get_configuration_definitions of class ConfigManager
def test_ConfigManager_get_configuration_definitions():
    # Test the following
        # 1. function Signature
        # 2. doc-string
        # 3. return value (type and value)

    configmanager = ConfigManager()
    expected_return_type = dict

# Generated at 2022-06-12 21:13:18.881719
# Unit test for method get_config_value_and_origin of class ConfigManager
def test_ConfigManager_get_config_value_and_origin():
    from collections import namedtuple
    from ansible import constants as C
    import sys
    
    class FakeSettings:
        pass
    
    # We are creating a file like object in order to make the return
    # value of load_config_file() in get_config_value_and_origin()
    # method to be a file like object.
    class FakeFile:
        def __init__(self,file_content):
            self.file_content = file_content
            self.currentIndex = 0

        def readline(self):
            if self.currentIndex != len(self.file_content):
                file_line = self.file_content[self.currentIndex]
                self.currentIndex += 1
                return file_line
            else:
                return '\n'

        def read(self):
            return ''.join