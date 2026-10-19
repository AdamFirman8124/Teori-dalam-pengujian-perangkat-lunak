

# Generated at 2022-06-13 04:52:38.563209
# Unit test for function revert_sources_list
def test_revert_sources_list():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock, patch
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args

    args = {
        'state': 'absent',
        'repo': 'ansible-testing',
        'filename': 'testing-ppa.list'
    }


# Generated at 2022-06-13 04:52:47.190579
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule({})
    sl = UbuntuSourcesList(module)
    sl.files = {}
    line = 'deb http://mirror.centos.org/centos/7.4.1708/os/x86_64/ centos main'
    file = 'mirror.centos.org.list'
    sl.add_source(line, file=file)
    sl.remove_source('http://mirror.centos.org/centos/7.4.1708/os/x86_64/ centos main')
    # assert sl.files == {}


# Generated at 2022-06-13 04:52:59.718266
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class Module:
        pass

    def run_command():
        pass

    def fetch_url():
        pass

    module = Module()
    module.run_command = run_command
    module.fetch_url = fetch_url
    module.params = {'codename': 'xenial'}
    module.atomic_move = lambda x, y: x

    s = UbuntuSourcesList(module)
    s.files = {}
    s.new_repos = set()
    s.codename = 'xenial'


# Generated at 2022-06-13 04:53:02.228231
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, "No real test yet"



# Generated at 2022-06-13 04:53:12.818518
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class C(object):
        pass

    
    m = C()
    m.params = {
        'codename': 'trusty',
    }
    m.tmpdir = '/tmp'
    m.run_command = Mock(return_value=(0,'ok',''))
    m.fail_json = Mock(return_value=None)
    m.atomic_move = Mock(return_value=None)
    m.set_mode_if_different = Mock(return_value=None)
    
    sl = UbuntuSourcesList(m, add_ppa_signing_keys_callback=lambda a: None)
    
    sl.add_source('ppa:smoser/test', file='myfile')

# Generated at 2022-06-13 04:53:24.897971
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    import unittest.mock as mock
    mock_apt_pkg_Config = mock.MagicMock()
    mock_apt_pkg_Config.side_effect = lambda arg: arg
    with mock.patch('ansible.module_utils.basic.apt.apt_pkg.Config', new=mock_apt_pkg_Config):
        with mock.patch('ansible.module_utils.basic.apt.apt_pkg.config.find_file', return_value='/etc/apt/sources.list'):
            with mock.patch('ansible.module_utils.basic.apt.apt_pkg.Config.FindFile', return_value='/etc/apt/sources.list'):
                sl = UbuntuSourcesList(None)
                #
                # add_source with file=None, and ppa: should be inserted into suggested file


# Generated at 2022-06-13 04:53:37.723469
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    global apt  # Ansible uses global apt for finding the python apt package
    mock_apt = MockAptModule()
    apt = mock_apt
    apt_pkg = importlib.import_module(apt.apt_pkg_name)

    sl = SourcesList(mock_apt)
    sl.files = {'/etc/apt/sources.list': [(0, True, True, 'deb http://foo bar', 'c1')]}

    sl.modify('/etc/apt/sources.list', 0, enabled=False, comment='c2')
    assert sl.files == {'/etc/apt/sources.list': [(0, True, False, 'deb http://foo bar', 'c2')]}


# Generated at 2022-06-13 04:53:48.238903
# Unit test for function install_python_apt
def test_install_python_apt():
    apt_pkg_name = 'python-apt'
    import sys
    import tempfile
    from ansible.module_utils.basic import AnsibleModule, get_exception
    from ansible.module_utils._text import to_bytes, to_native, to_text
    from ansible.module_utils.six import iteritems

    try:
        import apt
    except ImportError:
        pass
    else:
        tmpdir = tempfile.mkdtemp()
        path = tmpdir + "/ansible_apt_repository_payload"

# Generated at 2022-06-13 04:54:01.501132
# Unit test for constructor of class SourcesList
def test_SourcesList():
    class TestFixture:
        def __init__(self):
            self.files = {}
            self.messages = []

        def fail_json(self, msg):
            self.messages.append(msg)

        def run_command(self, cmd):
            return 0, '', ''

        def get_bin_path(self, bin_name):
            return bin_name

        def atomic_move(self, src, dest):
            self.files[dest] = self.files[src]
            del self.files[src]

        def set_mode_if_different(self, file, mode, follow, diff=None):
            pass

    import json
    import tempfile
    import shutil

    fixture = TestFixture()

    # create default sources.list
    default_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 04:54:10.756855
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    sources_list = SourcesList(mock)
    sources_list.load('/etc/apt/sources.list')
    result = sources_list.dump()

# Generated at 2022-06-13 04:54:53.781625
# Unit test for function install_python_apt
def test_install_python_apt():
    import platform

    def get_bin_path(module, executable):
        return '/bin/' + executable

    def run_command(module, cmd):
        return (random.randint(0, 10), None, None)

    setattr(AnsibleModule, 'mock_apt_repository', {'get_bin_path': get_bin_path, 'run_command': run_command, 'get_distribution': lambda: 'ubuntu'})
    setattr(apt, 'mock_apt_repository', True)
    setattr(apt_pkg, 'mock_apt_repository', True)
    setattr(aptsources_distro, 'mock_apt_repository', True)
    setattr(distro, 'mock_apt_repository', True)

# Generated at 2022-06-13 04:54:55.106630
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    assert get_add_ppa_signing_key_callback(dict()) is None
    assert get_add_ppa_signing_key_callback(dict(check_mode=False)) == 'function'



# Generated at 2022-06-13 04:55:07.337930
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    class Module(object):
        class parse_function_result(object):
            class module_args(object):
                filename = None
                mode = None
        def run_command(self, command):
            pass
        def fail_json(self, message):
            pass
        def atomic_move(self, tmp_path, filename):
            pass
        def set_mode_if_different(self, filename, this_mode, *other_params):
            pass
    class Fakesubprocess(object):
        def check_output(*args, **kwargs):
            return b''
    sys.modules['subprocess'] = Fakesubprocess
    class Fakeopen(object):
        def open(self, path, mode):
            self.lines = []
        def write(self, line):
            self.lines.append(line)

# Generated at 2022-06-13 04:55:09.247277
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    obj = SourcesList(AnsibleModule({}))
    obj.load("sources.list")



# Generated at 2022-06-13 04:55:22.841511
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})

    # Note: we have to mock get_bin_path here and use local file as sources.list
    module.get_bin_path = lambda x: ''
    sources_list = SourcesList(module)
    sources_list.default_file = os.path.join('test-data', 'sources-list.1')
    sources_list.load(sources_list.default_file)

    files = {}
    for file, n, enabled, source, comment in sources_list:
        if file not in files:
            files[file] = []
        files[file].append((n, enabled, source, comment))


# Generated at 2022-06-13 04:55:34.582661
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    '''
    Test of class UbuntuSourcesList method _add_valid_source
    '''

    class FauxModule(object):
        '''
        A faux module
        '''

        def __init__(self):
            self.params = {
                'codename': 'trusty',
                'filename': None,
                'mode': None
            }
            self._tmp_paths = []

        def fail_json(self, msg=None):
            raise AssertionError(msg)
        def atomic_move(self, path1, path2):
            pass
        def set_mode_if_different(self, path, mode, changed):
            pass
        def mkstemp(self, prefix=None, dir=None):
            '''
            Returns os file descriptor, fake path
            '''
            tmpfile = temp

# Generated at 2022-06-13 04:55:44.719144
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    sources_file_path = '/tmp/test_apt_sources_list'
    sources_file_content = [
        '# deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu xenial main',
        '# deb-src http://ppa.launchpad.net/deadsnakes/ppa/ubuntu xenial main\n'
    ]
    with open(sources_file_path, 'w') as sources_file:
        sources_file.writelines(sources_file_content)

    module = MagicMock()
    module.params = {'codename': 'xenial'}

    sources_list = UbuntuSourcesList(module)

    assert sources_file_content == sources_list.dump()[sources_file_path]


# Generated at 2022-06-13 04:55:47.653961
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = AnsibleModule({})
    sources_list = SourcesList(module)
    assert os.path.isfile(sources_list.default_file)



# Generated at 2022-06-13 04:56:00.605799
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible.module_utils.basic import create_ansible_module, AnsibleModule
    from . import UbuntuSourcesList

    def _fake_add_ppa_signing_keys_callback(command):
        pass

    def test_func_no_args(module):
        return None

    module = create_ansible_module(
        argument_spec=dict(),
        supports_check_mode=False
    )
    module.run_command = AnsibleModule.run_command
    module.fail_json = AnsibleModule.fail_json
    module.atomic_move = AnsibleModule.atomic_move
    module.set_mode_if_different = AnsibleModule.set_mode_if_different
    module.exit_json = AnsibleModule.exit_json

# Generated at 2022-06-13 04:56:14.291851
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule({})
    lines = []
    lines.append("deb http://us.archive.ubuntu.com/ubuntu/ trusty main restricted")
    lines.append("# Some comments")
    lines.append("deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates main restricted")
    lines.append("deb-src http://us.archive.ubuntu.com/ubuntu/ trusty multiverse")
    lines.append("")
    lines.append("deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe")
    lines.append("")
    lines.append("# deb http://us.archive.ubuntu.com/ubuntu/ trusty universe")
    lines.append("# deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates multiverse")
    lines

# Generated at 2022-06-13 04:58:41.491379
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    # We need apt module to run
    if not HAVE_PYTHON_APT:
        return

    class FakeModule:
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise Exception(msg)

        def atomic_move(self, a, b):
            if a != '/target/1.list.lock':
                raise Exception("atomic_move: Something went wrong: %s" % a)

        def set_mode_if_different(self, a, b, c):
            pass

    fm = FakeModule()

    sl = SourcesList(fm)


# Generated at 2022-06-13 04:58:50.949275
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    class test_SourcesList(SourcesList):
        def __init__(self, module, value):
            self.files = {'test.list': value}
    test_object_of_SourcesList = test_SourcesList(AnsibleModule(''),
                                                  [(0, True, False, 'deb http://test1', ''),
                                                   (1, True, True, 'deb http://test2', ''),
                                                   (2, True, False, 'deb http://test3', ''),
                                                   (3, True, True, 'deb http://test2', ''),
                                                   (4, True, True, 'deb http://test1', ''),
                                                   (5, True, True, 'deb http://test3', '')])

# Generated at 2022-06-13 04:58:59.161197
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    import unittest
    import tempfile
    from ansible.module_utils import basic

    class TestAnsibleModule(object):
        def __init__(self):
            self.params = None
            self.fail_json = self.exit_json = self.fail_json_sanity_check = lambda *args, **kwargs: None

        def atomic_move(self, a, b):
            shutil.move(a, b)

    class TestModuleUtilsBasic(object):
        def __init__(self):
            self.params = None

    class TestDistro(object):
        codename = 'bionic'

    class TestSourcesList(UbuntuSourcesList):
        def __init__(self, module):
            module = TestAnsibleModule()
            mod = TestModuleUtilsBasic()
            mod.Dist

# Generated at 2022-06-13 04:59:09.961716
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    """
    Test for :func:`SourcesList.remove_source()`
    Here's an example of how this library is used by ansible.builtin.apt_repository,
    https://github.com/ansible/ansible/blob/stable-2.9/lib/ansible/builtin/apt_repository.py#L98-L115
    """

# Generated at 2022-06-13 04:59:21.085680
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class FakeModule:
        def __init__(self):
            self.params = {'source': 'deb http://archive.canonical.com/ubuntu hardy partner', 'state': 'present', 'filename': None}
    module = FakeModule()
    self = SourcesList(module)

    with open('/etc/apt/sources.list', 'w') as f:
        f.write('deb http://archive.canonical.com/ubuntu hardy partner\n')
    self.load('/etc/apt/sources.list')

    with open('/etc/apt/sources.list.d/1.list', 'w') as f:
        f.write('deb http://archive.canonical.com/ubuntu hardy partner\n')
    self.load('/etc/apt/sources.list.d/1.list')

# Generated at 2022-06-13 04:59:27.514400
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class Module:
        def __init__(self, result):
            self.result = result
        def fail_json(self, *args, **kwargs):
            pass
        def check_mode(self):
            return False
        def get_bin_path(self, *args, **kwargs):
            return None
        def run_command(self, *args, **kwargs):
            return self.result
    def check_results(result, expected):
        for n, (file, n, enabled, source, comment) in enumerate(result):
            assert file in expected
            assert n in expected[file]
            assert enabled == expected[file][n][0]
            assert source == expected[file][n][1]
            assert comment == expected[file][n][2]

# Generated at 2022-06-13 04:59:38.708668
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    class TestModule(object):
        def __init__(self, failures=None):
            self.failures = failures

        def run_command(self, command, check_rc=True):
            if self.failures and len(self.failures) > 0:
                failure = self.failures.pop(0)
                if 'rc' in failure:
                    return failure['rc'], '', 'Cannot add key'
                else:
                    raise Exception('Cannot add key')

            return 0, '', ''

        def check_mode(self):
            return False

    # normal
    test_module = TestModule()
    callback = get_add_ppa_signing_key_callback(test_module)
    assert callback != None

    # check_mode
    test_module = TestModule()
    test_module.check_

# Generated at 2022-06-13 04:59:50.263451
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    sources = SourcesList(module)
    sources.load('tests/data/sources.list.test')


# Generated at 2022-06-13 04:59:54.252985
# Unit test for function install_python_apt
def test_install_python_apt():
    module_mock = AnsibleModule(argument_spec={})
    module_mock.get_bin_path = lambda a: '/bin/apt-get'
    module_mock.run_command = lambda a: (0, "", "")
    install_python_apt(module_mock, 'python3-apt')


# Generated at 2022-06-13 05:00:05.959639
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class FakeModule(object):
        def __init__(self):
            self.fail_json_calls = []
            self.debug_calls = []
        def fail_json(self, *args, **kwargs):
            self.fail_json_calls.append((args, kwargs))
        def debug(self, *args, **kwargs):
            self.debug_calls.append((args, kwargs))

    # Init SourcesList class
    module = FakeModule()
    sources_list = SourcesList(module)

    # Init test file
    fd, file = tempfile.mkstemp()