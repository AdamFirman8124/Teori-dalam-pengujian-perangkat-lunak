

# Generated at 2022-06-13 04:52:33.489996
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec=dict())

    sources_list = SourcesList(module)
    with open("sources_list", "r") as f:
        for line in f.readlines():
            sources_list.add_source(line)
    module.exit_json(changed=True, sources_list=sources_list.dump())



# Generated at 2022-06-13 04:52:44.021666
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    repo = 'deb http://archive.canonical.com/ubuntu xenial partner'
    comment = 'This is comment'
    # Test 'enabled' parameter
    enabled_value_1 = False
    # Create temporary list file
    temp_dir = os.path.dirname(tempfile.mkdtemp())
    filename_1 = os.path.join(temp_dir, "sources.list.1")
    with open(filename_1, 'w'):
        pass
    # Create SourcesList object with temp file
    source_1 = SourcesList(AnsibleModule(argument_spec={}, check_invalid_arguments=False))
    source_1.add_source(repo, comment=comment)
    source_1.save()
    # Modify source line in temp file

# Generated at 2022-06-13 04:52:57.173785
# Unit test for constructor of class SourcesList
def test_SourcesList():
    sl = SourcesList(AnsibleModule(argument_spec={}))
    disabled_default = 0
    disabled_sourceslistd = 0
    for file, n, enabled, source, comment in sl:
        if not enabled:
            disabled_default += 1
        if file.startswith(sl._apt_cfg_dir('Dir::Etc::sourceparts')):
            disabled_sourceslistd += 1
    # This is expected number of entries in /etc/apt/sources.list.
    # See UNIT_TEST_EXPECTED_NUMBER_OF_ENTRIES below.
    assert len(sl.files[sl.default_file]) == 34
    assert disabled_default == 25
    assert disabled_sourceslistd == 2



# Generated at 2022-06-13 04:53:09.921111
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    run_command_input = []

    class Module:
        def __init__(self):
            self.check_mode = False

        def run_command(self, command, check_rc):
            assert check_rc
            run_command_input.append(command)

    module = Module()
    callback = get_add_ppa_signing_key_callback(module)
    callback(['apt-key', 'adv', '--recv-keys', '--no-tty', '--keyserver', 'hkp://keyserver.ubuntu.com:80', 'ABCD1234'])

    assert len(run_command_input) == 1

# Generated at 2022-06-13 04:53:21.264433
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    """
    Test function for constructor of class UbuntuSourcesList
    """
    # test with invalid path

# Generated at 2022-06-13 04:53:25.169859
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # Unit test for method _add_valid_source of class SourcesList
    '''

    :return:
    '''
    # Unit test for method _remove_valid_source of class SourcesList

# Generated at 2022-06-13 04:53:37.977355
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    
    class fake_module(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = None
        def get_bin_path(self, file):
            return None
        def run_command(self, cmd):
            if cmd == [apt_get_path, 'update']:
                if rc != 0:
                    self.fail_json(msg="Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, se.strip()))

# Generated at 2022-06-13 04:53:48.396983
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    lst = SourcesList(None)
    lst.files['test.list'] = [(0, True, False, 'deb http://example.com', '# valid disabled source')]
    lst.files['test2.list'] = [(0, True, False, 'deb http://example.com', '# valid disabled source')]
    lst.modify('test.list', 0)
    assert lst.files['test.list'][0][2] is True
    lst.modify('test.list', 0, enabled=False)
    assert lst.files['test.list'][0][2] is False
    lst.modify('test.list', 0, source='deb http://example.org')
    assert lst.files['test.list'][0][3] == 'deb http://example.org'
   

# Generated at 2022-06-13 04:53:50.736868
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    dummy_module = None
    assert get_add_ppa_signing_key_callback(dummy_module) is None


# Generated at 2022-06-13 04:53:52.541498
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule({}, {})
    install_python_apt(module, 'python2-apt')


# Generated at 2022-06-13 04:54:35.431729
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    def result_for(file, source, enabled, comment):
        return (file, source, enabled, comment)

    result = []
    sl = SourcesList(AnsibleModule(''))

    # add two sources in one repo,
    # add two sources in two repos
    sl.add_source('deb http://archive.canonical.com/ubuntu hardy partner')
    result.append(result_for('/etc/apt/sources.list', 'deb http://archive.canonical.com/ubuntu hardy partner', True, ''))

    sl.add_source('deb http://archive.ubuntu.com/ubuntu zesty main', comment='this is main')
    result.append(result_for('/etc/apt/sources.list', 'deb http://archive.ubuntu.com/ubuntu zesty main', True, 'this is main'))

# Generated at 2022-06-13 04:54:42.785807
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = make_mock_module_obj()
    sources_list = UbuntuSourcesList(module)

    sources_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    sources_file.write("deb http://ppa.launchpad.net/foo/bar/ubuntu bionic main")
    sources_file.write("\n")
    sources_file.write("deb http://ppa.launchpad.net/foo/baz/ubuntu bionic main")
    sources_file.write("\n")
    sources_file.close()

    sources_list.load(sources_file.name)

    with open(sources_file.name, 'r') as f:
        sources = f.readline()
    sources_list.remove_source(sources)


# Generated at 2022-06-13 04:54:56.353963
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    import tempfile
    import os
    import shutil
    import stat

    class module(object):
        def __init__(self):
            self.params = {'codename': 'focal'}

            self.fail_json_called = False
            self.fail_json_called_msg = None
            self.atomic_move_called = False
            self.atomic_move_called_src = None
            self.atomic_move_called_dest = None
            self.set_mode_if_different_called = False
            self.set_mode_if_different_called_file = None
            self.set_mode_if_different_called_mode = None

        def fail_json(self, msg):
            self.fail_json_called = True
            self.fail_json_called_msg = msg


# Generated at 2022-06-13 04:55:08.540610
# Unit test for function main
def test_main():
    # Test case 1
    # Test valid cert
    def test_install_python_apt_cert_valid(self):
        self.assertTrue(install_python_apt(self))

    # Test failure to install on system that can't install packages
    def test_install_python_apt_yum(self):
        self.assertFalse(install_python_apt(self.yum_distro))

    # Test case 2
    # Test invalid cert
    def test_install_python_apt_cert_invalid(self):
        self.assertFalse(install_python_apt(self))

    # Test case 3
    # Test empty repo param
    def test_empty_repo_param(self):
        self.assertFalse(install_python_apt(self))

    # Test case 4
    # Test negative

# Generated at 2022-06-13 04:55:22.666026
# Unit test for function main
def test_main():

    import pytest

    from ansible.module_utils.apt.repository import InvalidSource, SourcesList

    from units.compat.mock import MagicMock, patch, Mock
    from units.modules.utils import set_module_args

    def _get_mock_environment(os_family='Debian',
                              executable='/usr/bin/python3.6',
                              pkg_mgr='apt',
                              codename='buster'):
        env_facts = {
            'ansible_os_family': os_family,
            'ansible_pkg_mgr': pkg_mgr,
            'ansible_distribution_codename': codename,
            'ansible_distribution_release': '10',
            'ansible_python': executable,
        }
        return env_facts


# Generated at 2022-06-13 04:55:34.393996
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins


# Generated at 2022-06-13 04:55:46.594682
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    module = AnsibleModule()
    # Initialize sourceslist
    s = SourcesList(module)
    # Add the following line to sources.list
    s._add_valid_source('deb http://archive.ubuntu.com/ubuntu/ xenial main universe', comment_new='ubuntu')
    # Make sure that the output is not null
    assert len(s.dump()) > 0
    # Check if the output contains only 1 file
    assert len(s.dump()) == 1
    for filename, sources in list(s.dump().items()):
        # Check if the file is sources.list
        assert filename == '/etc/apt/sources.list'
        # Check if the file contains the line we added
        assert sources.find('deb http://archive.ubuntu.com/ubuntu/ xenial main universe # ubuntu') > 0
    # Add the following line

# Generated at 2022-06-13 04:55:56.088082
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    """
    Test for class UbuntuSourcesList method add_source
    """
    module = AnsibleModule(
        argument_spec={},
    )

    test_obj = UbuntuSourcesList(module)

    # AssertionError: File /etc/apt/sources.list.d/hvr-ppa_ansible_test_ubuntu_trusty_main.list must not exists
    test_obj.add_source('ppa:hvr/ansible-test', 'ppa_test', file='hvr-ppa_ansible_test_ubuntu_trusty_main.list')


# Generated at 2022-06-13 04:56:04.469455
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    assert SourcesList._parse('deb http://ftp.mydomain.tld/debian/ jessie contrib non-free', raise_if_invalid_or_disabled=True)[2] == 'deb http://ftp.mydomain.tld/debian/ jessie contrib non-free'
    assert SourcesList._parse('deb [arch=i386] http://ftp.mydomain.tld/debian/ jessie contrib non-free', raise_if_invalid_or_disabled=True)[2] == 'deb [arch=i386] http://ftp.mydomain.tld/debian/ jessie contrib non-free'

# Generated at 2022-06-13 04:56:10.236851
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockObject(object):
        pass

    mock_module = MockObject()
    mock_module.params = {'filename': None}
    mock_module.atomic_move = lambda source, destination: None
    mock_module.set_mode_if_different = lambda source, mode, changed: None
    mock_module.run_command = lambda cmd, check_rc=True: None
    mock_module.fail_json = lambda msg: None

    mock_add_ppa_signing_keys_callback = lambda cmd: None

    src_list = UbuntuSourcesList(
        mock_module,
        add_ppa_signing_keys_callback=mock_add_ppa_signing_keys_callback
    )
    deepcopy(src_list)


# Generated at 2022-06-13 04:58:01.643337
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    import inspect
    import os
    import shutil
    import tempfile
    import unittest

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


    class SourcesListTestCase(unittest.TestCase):
        SOURCE = 'deb http://archive.ubuntu.com/ubuntu trusty main'
        SOURCE_TWO = 'deb http://archive.ubuntu.com/ubuntu trusty main restricted'
        SOURCE_THREE = 'deb http://archive.ubuntu.com/ubuntu trusty main restricted universe'
        SOURCE_FOUR = 'deb http://archive.ubuntu.com/ubuntu trusty main restricted universe multiverse'
        SOURCE_FIVE = 'deb http://archive.ubuntu.com/ubuntu trusty main restricted universe multiverse foobar'

# Generated at 2022-06-13 04:58:03.473479
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    apt = UbuntuSourcesList(None)
    assert apt



# Generated at 2022-06-13 04:58:06.640857
# Unit test for function install_python_apt
def test_install_python_apt():

    module = AnsibleModule({
        'install_python_apt': True,
    })
    if HAS_PYTHON_APT is False:
        install_python_apt(module, 'python3-apt')

    else:
        module.fail_json(msg="Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, se.strip()))



# Generated at 2022-06-13 04:58:14.248602
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    mod = MockModule()
    repo_spec = 'ppa:user/ppa-name'
    repo_spec_alt = 'ppa:user/ppa-name-alt/ubuntu codename'
    sl = UbuntuSourcesList(mod)
    sl.add_source(repo_spec)
    default_file = sl._apt_cfg_file('Dir::Etc::sourcelist')
    if os.path.isfile(default_file):
        sl.load(default_file)
    assert repo_spec in sl
    file = sl._suggest_filename(repo_spec)
    sl.add_source(repo_spec, file=file)
    assert repo_spec in sl
    new_repos = set()
    sl.new_repos = new_repos

# Generated at 2022-06-13 04:58:26.466174
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    class MockModule(object):
        def __init__(self):
            self.CHECK_MODE = False
        def run_command(self, args):
            return 0, 'stdout', 'stderr'
        def atomic_move(self, tmp, dest):
            return
        def fail_json(self, msg):
            print(msg)
        def get_bin_path(self, cmd):
            return 'apt-get'
        def set_mode_if_different(self, fn, this_mode, silent):
            return

    class Test_SourcesList(object):
        def __init__(self, module):
            self.module = module
            self.files = {}  # group sources by file
            self.new_repos = set()
            self.default_file = '/etc/apt/sources.list'



# Generated at 2022-06-13 04:58:37.824978
# Unit test for function install_python_apt
def test_install_python_apt():
    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = kwargs['fail_json']
            self.run_command = kwargs['run_command']
            self.check_mode = False
        def get_bin_path(self,bin):
            return bin

    class TestCommand(object):
        def __init__(self, **kwargs):
            self.rc = kwargs['rc']
            self.stdout = kwargs['stdout']
            self.stderr = kwargs['stderr']

        def __call__(self, *args, **kwargs):
            return (self.rc, self.stdout, self.stderr)

    # Test that output is ok if the installation is succes

# Generated at 2022-06-13 04:58:47.686957
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    test_filename = '/tmp/test.sources.list'
    with open(test_filename, 'w') as test_file:
        test_file.write('deb http://example.com precise main\n')
        test_file.write('deb-src http://example.com precise main\n')
        test_file.write('# deb http://example.com precise main\n')
        test_file.write('# deb-src http://example.com precise main\n')
        test_file.write('# deb http://example.com precise main # comment \n')
        test_file.write('# deb-src http://example.com precise main # comment \n')
        test_file.write('# comment\n')
        test_file.write('garbage\n')

# Generated at 2022-06-13 04:58:55.648269
# Unit test for method save of class SourcesList

# Generated at 2022-06-13 04:59:08.508310
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    sl = SourcesList(None)

    # Duplicated sources should be squashed
    line = 'deb-src http://archive.ubuntu.com/ubuntu/ trusty main restricted'
    sl.add_source(line, comment=' Unit testing!')
    sl.add_source(line, comment=' Unit testing!')
    assert len(list(sl)) == 1

    # Source uri
    line = 'deb http://archive.ubuntu.com/ubuntu/ trusty main restricted'
    sl.add_source(line)
    assert len(list(sl)) == 2
    sl.add_source(line)
    assert len(list(sl)) == 2

    # Source uri with component
    line = 'deb http://archive.ubuntu.com/ubuntu/ trusty main restricted multiverse'
    sl.add_source(line)

# Generated at 2022-06-13 04:59:20.853713
# Unit test for function install_python_apt
def test_install_python_apt():
    '''
    Test the install_python_apt function
    :return:
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path

    def fail_json(*args, **kwargs):
        '''function that just throws an exception'''
        pass

    def run_command(*args, **kwargs):
        '''function that returns a tuple as if you ran apt-get update'''
        return (0, '', '')

    # init module names to keep pylint happy
    apt = apt_pkg = aptsources_distro = distro = None
