

# Generated at 2022-06-13 04:52:39.846081
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({}, check_invalid_arguments=False)
    module.run_command = MagicMock(return_value=(0, '', ''))
    sl = SourcesList(module)

    # Create a directory for testing
    tmpd = tempfile.mkdtemp()
    # Create a test sources list
    test_sources_path = os.path.join(tmpd, "sources.list")
    test_sources_list = ["deb http://www.example.com", "deb-src http://www.example.com"]
    write_to_file(test_sources_path, '\n'.join(test_sources_list))

    # Create a test sources.list.d folder

# Generated at 2022-06-13 04:52:45.917731
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    test_module = AnsibleModule({})
    sudo_mock = MagicMock()
    sudo_mock.return_value = True
    test_module.get_bin_path = lambda x: ''
    test_module.get_bin_path.return_value = ''
    test_module.run_command = lambda *args, **kwargs: (1, '', '')
    test_module.run_command.return_value = (1, '', '')
    test_module.run_command_environ_update = MagicMock()
    test_module.run_command_environ_update.return_value = True
    test_module.boolean = lambda x: x
    test_module.boolean.return_value = True
    test_module.tmpdir = tempfile.gettempdir()

    test_case

# Generated at 2022-06-13 04:52:53.031432
# Unit test for function main

# Generated at 2022-06-13 04:53:05.505442
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.called_commands = []

        def run_command(self, command, check_rc=False):
            self.called_commands.append(command)
            return True, '', ''

    # test that false check_mode does not set a callback function
    module = FakeModule()
    assert get_add_ppa_signing_key_callback(module) is None

    # test that true check_mode sets a callback function
    module = FakeModule()
    module.check_mode = True
    assert get_add_ppa_signing_key_callback(module) is None

    # test that non check_mode sets a callback function
    module = FakeModule()
    module.check_mode = False
    module.run_

# Generated at 2022-06-13 04:53:16.858270
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    test_file = '/tmp/SourcesList.test'


# Generated at 2022-06-13 04:53:25.113697
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    '''
    Unit test for method remove_source of class SourcesList
    '''
    module = AnsibleModule({})
    sources = SourcesList(module)
    line = 'deb http://nonexistent deb/'
    sources.add_source(line)
    sources.save()
    sources.load(sources.default_file)
    sources.remove_source(line)
    sources.save()
    match = []
    with open(sources.default_file, 'r') as fd:
        for line in fd:
            if line.strip() == line.strip().lstrip('#'):
                match.append(True)
    assert not any(match)

# Add tests to the module
from ansible.utils.path import unfrackpath
p, root, ent = unfrackpath(__file__)


# Generated at 2022-06-13 04:53:37.926047
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    line1 = 'deb http://archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse'
    line2 = 'deb http://archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse'
    line3 = 'deb http://archive.ubuntu.com/ubuntu/ trusty-proposed main restricted universe multiverse'
    line4 = 'deb http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse'
    lines = '\n'.join([line1, line2, line3, line4])

    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    mod.exit_json = mock.MagicMock()

    d = tempfile.mkdtemp()

# Generated at 2022-06-13 04:53:48.365507
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module_mock = MagicMock()
    # set module_mock.check_mode to False
    module_mock.check_mode = False
    os_path_exists_mock = MagicMock()
    os_path_exists_mock.return_value = True
    os_remove_mock = MagicMock()
    os_remove_mock.return_value = True
    os_makedirs_mock = MagicMock()
    os_makedirs_mock.return_value = True
    os_mkstemp_mock = MagicMock()
    os_mkstemp_mock.return_value = (19, '/var/tmp/ansible_apt_sources_list_module.fJG7O1')
    os_fdopen_mock = MagicMock()


# Generated at 2022-06-13 04:53:54.770340
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    """Test SourcesList load() method"""
    module = AnsibleModule({})
    sl = SourcesList(module)
    filename = tempfile.mktemp()
    f = open(filename, 'w')
    f.write("""#deb http://archive.canonical.com/ubuntu feisty partner
deb http://archive.ubuntu.com/ubuntu xenial main
garbage
deb-src http://archive.ubuntu.com/ubuntu xenial-proposed main multiverse
# deb-src http://archive.ubuntu.com/ubuntu feisty-proposed main multiverse
""")
    f.close()
    sl.load(filename)
    os.remove(filename)
    assert len(sl.files) == 1
    assert len(sl.files[filename]) == 4

    # Test last (garbage) line

# Generated at 2022-06-13 04:54:03.786075
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins

    builds_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(builds_dir, 'unit', 'test_data', 'UbuntuSourcesList.bin')
    test_file_orig = os.path.join(builds_dir, 'unit', 'test_data', 'UbuntuSourcesList.orig')
    shutil.copy(test_file_orig, test_file)

    class ModuleStub:    # pylint: disable=too-few-public-methods
        tmpdir = None
        params = None
        check_mode = False

        def __init__(self):
            self.debug = False
           

# Generated at 2022-06-13 04:54:39.739705
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({'fromfile': False})
    sources = SourcesList(module)
    path = os.path.join(os.path.dirname(__file__), 'list.txt')
    sources.load(path)
    dumpstruct = sources.dump()
    for key, value in dumpstruct.items():
        if os.path.dirname(key) == '/etc/apt':
            with open(key, 'r') as f:
                content = f.read()
            assert value == content
        else:
            assert value == ''.join(["deb http://ppa.launchpad.net/diwic/test/ubuntu/ trusty main universe\n",
                                     "deb-src http://ppa.launchpad.net/diwic/test/ubuntu/ trusty main universe\n"])



# Generated at 2022-06-13 04:54:53.305313
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec={'state': {'default': 'present'}})
    line = 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable'
    # Unit test for method _parse which is called by method load
    valid, enabled, src, comment = SourcesList._parse(line)
    assert valid
    assert enabled
    assert src == line
    assert comment == ''
    # Unit test for method load
    sl = SourcesList(module)
    assert sl.files == dict()
    sl.load('tests/Data/sources.list')
    assert sl.files == {'tests/Data/sources.list': [(0, True, True, 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable', '')]}
    sl.load

# Generated at 2022-06-13 04:55:03.778215
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    test_obj = SourcesList()
    test_source_new = "my source line"
    test_source_en = "my source line en"
    test_source_dis = "my source line dis"
    test_source_comment = "this is a comment"
    test_source_file = "test.list"
    # Add a disabled source
    test_source_dis_full = "# {0}".format(test_source_dis)
    test_obj._add_valid_source(test_source_dis_full, "", file=test_source_file)
    # Add an enabled source
    test_source_en_full = "{0}".format(test_source_en)
    test_obj._add_valid_source(test_source_en_full, "", file=test_source_file)
    # Check

# Generated at 2022-06-13 04:55:08.583409
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    test_module = AnsibleModule({}, {}, {})
    sources_list = SourcesList(test_module)
    file_name = sources_list._apt_cfg_file('Dir::Etc::sourcelist')
    sources_list.load(file_name)
    assert sources_list.files != {}


# Generated at 2022-06-13 04:55:21.216915
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    line = 'deb [arch=amd64] http://download:8111/repositories/LocalRepo/Ubuntu_16.04  Release'
    comment = 'Local Repo'
    file = '/etc/apt/sources.list.d/localrepo.list'
    fake_module = AnsibleModule({})
    fake_ubuntu_sources_list = UbuntuSourcesList(fake_module)
    fake_ubuntu_sources_list.add_source(line, comment, file)
    assert line in fake_ubuntu_sources_list.dump()
    fake_ubuntu_sources_list.remove_source(line)
    assert line not in fake_ubuntu_sources_list.dump()



# Generated at 2022-06-13 04:55:32.799899
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    sl = UbuntuSourcesList(None)
    sl.add_source('deb http://www.example.com/ubuntu natty main', codename='natty')
    sl.add_source('ppa:runlevel1/test-repo', codename='precise')
    sl.add_source('ppa:runlevel1/test-repo/test-repo-1', codename='precise')

    sl.add_source('deb http://www.example.com/ubuntu natty main', codename='natty')
    sl.add_source('ppa:runlevel1/test-repo', codename='precise')
    sl.add_source('ppa:runlevel1/test-repo/test-repo-1', codename='precise')

# Generated at 2022-06-13 04:55:45.008354
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    tmp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

# Generated at 2022-06-13 04:55:57.645416
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    test_fixture_dir = os.path.join(os.path.dirname(__file__), 'unit')
    fixture_file = os.path.join(test_fixture_dir, 'fixture')
    actual = SourcesList(None)

    # load fixture sources.list and sources.list.d
    actual.load(fixture_file)

    # test dump result

# Generated at 2022-06-13 04:56:01.049823
# Unit test for function install_python_apt
def test_install_python_apt():
    m = AnsibleModule(argument_spec={
        'install_python_apt': {'type': 'bool', 'default': True},
    })
    install_python_apt(m, 'apt_pkg')
    install_python_apt(m, 'python-apt')



# Generated at 2022-06-13 04:56:07.986933
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    from urllib.request import urlopen, Request
    from unittest import mock
    from ansible.module_utils.urls import ConnectionError
    import ansible.module_utils.six as six
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    # mock import of module and check functions

# Generated at 2022-06-13 04:56:44.641959
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class MockModule:

        class MockParams:
            codename = distro.codename

        class MockDistro:
            codename = MockParams.codename

        params = MockParams()
        distro = MockDistro()
        _atomic_move_called = False

        def atomic_move(self, before, after):
            assert after == '/etc/apt/sources.list.d/ansible_test_ppa.list'
            self.atomic_move_called = True

    usl = UbuntuSourcesList(MockModule())
    usl.add_source('ppa:ansible/test')


# Generated at 2022-06-13 04:56:56.125896
# Unit test for method remove_source of class SourcesList

# Generated at 2022-06-13 04:57:01.762546
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    lines = [
        'deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main',
        'deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main',
        'deb http://ppa.launchpad.net/ansible/ansible/ubuntu yakkety main',
        'deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main',
    ]
    # Simple test - one ppa
    sources_list = UbuntuSourcesList(None)
    sources_list.add_source('ppa:ansible/ansible')
    assert sources_list.repos_urls == lines


# Generated at 2022-06-13 04:57:04.585327
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = AnsibleModule(argument_spec={'codename': {'type': 'str', 'required': True, 'choices': ['trusty', 'xenial', 'bionic']}, 'ppa': {'type': 'dict', 'required': True}})
    instance_obj = UbuntuSourcesList(module)
    deepcopy_obj = instance_obj.__deepcopy__()
    assert deepcopy_obj.codename == module.params['codename']

# Generated at 2022-06-13 04:57:13.453423
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    sourceslist = class_to_test
    sourceslist_method = 'save'
    #
    # Test 1
    dump_class = {'/etc/apt/sources.list': """deb http://deb.debian.org/debian stretch main
deb-src http://deb.debian.org/debian stretch main
deb http://deb.debian.org/debian stretch-updates main
deb-src http://deb.debian.org/debian stretch-updates main
deb http://security.debian.org/debian-security stretch/updates main
deb-src http://security.debian.org/debian-security stretch/updates main
""", '/etc/apt/sources.list.d/test.list': "deb http://deb.debian.org/debian stretch main\ndeb-src http://deb.debian.org/debian stretch main\n"}
    arg_

# Generated at 2022-06-13 04:57:17.579284
# Unit test for function install_python_apt
def test_install_python_apt():
    apt_pkg_name = 'python-apt'
    module = AnsibleModule({})
    install_python_apt(module, apt_pkg_name)
    assert(HAVE_PYTHON_APT)



# Generated at 2022-06-13 04:57:31.934786
# Unit test for function install_python_apt
def test_install_python_apt():
    # Create a fake module for testing
    module = AnsibleModule(
        argument_spec=dict(),
    )
    # Create a fake apt-get binary
    apt_get_path = os.path.join(tempfile.mkdtemp(), 'apt-get')

    # Create a function that succeeds when asked to install python-apt
    def run_command_success(args, **kwargs):
        packages = args[-1].split()
        if apt_get_path in args and 'update' in args:
            return 0, '', ''
        elif apt_get_path in args and 'install' in args and packages.pop() == 'python-apt':
            return 0, '', ''
        # Unhandled case
        return 1, '', ''

    # Create a function that fails when asked to install python-apt

# Generated at 2022-06-13 04:57:40.444518
# Unit test for constructor of class SourcesList
def test_SourcesList():
    # This is just a simple unit test that actually does not need AnsibleModule, but needs real apt sources.
    assert(os.path.isdir('/etc/apt/sources.list.d'))
    obj = SourcesList(None)
    # Get list of sources from apt sources.
    expected = set(s for s in apt_pkg.SourceList() if s.type in ('deb', 'deb-src'))
    observed = set(obj.dump().values())
    assert(observed == expected)



# Generated at 2022-06-13 04:57:41.514986
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass



# Generated at 2022-06-13 04:57:51.615384
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    import tempfile
    import shutil
    import os
    import time

    # Create temp dir for testing.
    tmpdir = tempfile.mkdtemp()
    os.rmdir(tmpdir)
    os.mkdir(tmpdir)

    # Replace `apt_pkg` module's methods to return path to this dir.
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = lambda a: a
    module.run_command = lambda a: (0, a, '')

    def _apt_cfg_file(filespec):
        return os.path.join(tmpdir, 'etc', filespec)

    def _apt_cfg_dir(dirspec):
        return os.path.join(tmpdir, 'etc', dirspec)


# Generated at 2022-06-13 04:59:10.173860
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    class mod:
        pass
    module = mod()
    module.check_mode = False
    module.run_command = my_run_command
    module.get_bin_path = my_get_bin_path
    module.fail_json = my_fail_json
    module.atomic_move = my_atomic_move
    module.set_mode_if_different = my_set_mode_if_different

    sources = SourcesList(module)

    sources.add_source('deb http://archive.canonical.com/ubuntu hardy partner')
    sources.add_source('deb http://dl.google.com/linux/chrome/deb/ stable main')
    sources.add_source('deb-src http://archive.canonical.com/ubuntu hardy partner')

# Generated at 2022-06-13 04:59:18.126067
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    module = AnsibleModule({})
    sl = SourcesList(module)
    sl.add_source('deb-src http://archive.ubuntu.com/ubuntu trusty main restricted')
    sl.add_source('# ppa:nginx/stable')
    result = json.dumps(sl.dump(), indent=4)
    assert result == '''\
    {
        "/etc/apt/sources.list": "deb-src http://archive.ubuntu.com/ubuntu trusty main restricted\\n"
    }'''



# Generated at 2022-06-13 04:59:20.795353
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleFailJson):
        main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:27.292052
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    ## If a source is detected, it must be iterated in the end.
    # Create a source list that contains three sources.
    test_src_1 = ('deb', True, 'http://archive.ubuntu.com/ubuntu/ xenial main restricted', '')
    test_src_2 = ('deb', True, 'http://archive.ubuntu.com/ubuntu/ xenial-updates main restricted', '')
    test_src_3 = ('deb', True, 'http://archive.ubuntu.com/ubuntu/ xenial universe', '')
    for type_, enabled, source, comment in [test_src_1, test_src_2, test_src_3]:
        fake_sources_list = SourcesList({'run_command': ({'rc': 0}, 'stdout', 'stderr')})
        # Generate a valid source file in /

# Generated at 2022-06-13 04:59:38.580850
# Unit test for method add_source of class SourcesList

# Generated at 2022-06-13 04:59:50.107245
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    DATA = '''
# deb cdrom:[Debian GNU/Linux 8.0.0 _Jessie_ - Official i386 NETINST Binary-1 20150110-11:10]/ jessie main

deb http://security.debian.org/ jessie/updates main contrib non-free
deb-src http://security.debian.org/ jessie/updates main contrib non-free
# deb http://httpredir.debian.org/debian jessie main contrib non-free
# deb http://ftp.debian.org/debian jessie-backports main contrib non-free
# deb-src http://httpredir.debian.org/debian jessie main contrib non-free
# deb-src http://ftp.debian.org/debian jessie-backports main contrib non-free
'''
   

# Generated at 2022-06-13 04:59:57.525545
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    class Module(object):
        def __init__(self):
            self.exit_json = None

        def fail_json(self, msg=None):
            self.exit_json = None

        def atomic_move(self, src, dest):
            self.src = src
            self.dest = dest
        def set_mode_if_different(self, mode, src, dest, recursive):
            self.mode = mode
            self.src = src
            self.dest = dest
            self.recursive = recursive

    class TestModule(object):
        def __init__(self):
            self.params = None
    test = Module()
    test_m = TestModule()
    test_m.params = None
    test_s = SourcesList(test_m)


# Generated at 2022-06-13 05:00:10.773202
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    '''
    Unit test for class UbuntuSourcesList and method add_source
    '''
    class ModuleMock:
        '''
        This class is a mock of AnsibleModule class
        '''
        def __init__(self):
            self.params = {'codename':'bionic'}

        def fail_json(self, msg):
            raise AssertionError(msg)

        @staticmethod
        def atomic_move(src, dst):
            pass

        @staticmethod
        def set_mode_if_different(file, mode, changed):
            pass

        @staticmethod
        def run_command(*args, **kwargs):
           return 1, '', ''

    def add_ppa_signing_keys_callback(command):
        pass


# Generated at 2022-06-13 05:00:21.504634
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    sl = SourcesList('dummy')
    # makes sure that iterator doesn't contain invalid lines
    sl.files = {
        'file1': [(0, False, False, '', ''),  # invalid source + disabled
                  (1, True, False, 'deb http://archive.ubuntu.com/ubuntu trusty main', ''),
                  (2, False, False, '', ''),  # invalid source + disabled
                  (3, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty main', '')],
        'file2': [(0, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty main', '')],
        'file3': []
    }

# Generated at 2022-06-13 05:00:31.262806
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = AnsibleModule(argument_spec={
        'before': {'type': 'list', 'default': []},
        'after': {'type': 'list', 'default': []},
        'codename': {'type': 'str', 'default': ''},
    })
    sl = UbuntuSourcesList(module)

    # Test ppa validation
    for ppa in ['ppa:user1/repo1', 'ppa:user2']:
        try:
            sl.add_source(ppa)
        except AnsibleModuleFail:
            pass
        else:
            raise AssertionError('ppa %s should be invalid' % ppa)
    for ppa in ['ppa:user1/repo1', 'ppa:user2']:
        sl._parse(ppa, raise_if_invalid_or_disabled=True)

