

# Generated at 2022-06-13 04:52:38.153461
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    # Setup
    module_Mock = MagicMock(name='module_Mock')
    add_ppa_signing_keys_callback_Mock = MagicMock(name='add_ppa_signing_keys_callback_Mock')
    ubuntuSourcesList_instance = UbuntuSourcesList(module = module_Mock, add_ppa_signing_keys_callback = add_ppa_signing_keys_callback_Mock)
    # Exercise
    result = ubuntuSourcesList_instance.__deepcopy__()
    # Verify
    assert result.module == module_Mock
    assert result.add_ppa_signing_keys_callback == add_ppa_signing_keys_callback_Mock

# Generated at 2022-06-13 04:52:46.261696
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class MockModule(object):
        '''
        Mock module
        '''

        def __init__(self):
            self.params = {}
            self.fail_json = lambda msg: msg


    class MockApt(object):
        '''
        Mock apt
        '''

        @staticmethod
        def Config():
            return os.path

    class MockAptPkg(object):
        '''
        Mock apt_pkg
        '''

        class Config(object):
            '''
            Mock apt_pkg.Config
            '''

            @staticmethod
            def FindDir(dirspec):
                return "/tmp/{}".format(dirspec)

            @staticmethod
            def FindFile(filespec):
                return "/tmp/{}".format(filespec)


# Generated at 2022-06-13 04:52:58.529163
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils.six import PY3

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-13 04:53:11.458285
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    m = AnsibleModule(
        argument_spec=dict(
            codename='trusty'
        )
    )

    source_list = UbuntuSourcesList(m)

    source_list.add_source('ppa:foo/bar')
    assert source_list.files[source_list.default_file] == [(0, True, True, 'deb http://ppa.launchpad.net/foo/bar/ubuntu trusty main', '')]

    source_list.files.clear()
    source_list.add_source(
        'ppa:foo/bar',
        comment='test',
        file='test.list'
    )
    assert source_list.files['test.list'] == [(0, True, True, 'deb http://ppa.launchpad.net/foo/bar/ubuntu trusty main', 'test')]

# Generated at 2022-06-13 04:53:17.289252
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    with patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.distro.sys_info', return_value=UbuntuFacts({'distribution': 'Ubuntu', 'distribution_version': '18.04'})):
        uu = UbuntuSourcesList(FakeModule())

    assert uu.files == {}
    assert uu.codename == 'bionic'


# Generated at 2022-06-13 04:53:30.465301
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    # 1. create SourcesList instance
    sources_list = SourcesList(module)
    # 2. prepare input data
    input_data = '''
    # some comment
    deb http://archive.ubuntu.com/ubuntu bionic main universe restricted multiverse
    deb-src http://archive.ubuntu.com/ubuntu bionic main universe restricted multiverse
    '''
    # 3. prepare lines list
    lines = input_data.split('\n')
    # 4. prepare expected result

# Generated at 2022-06-13 04:53:30.945665
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass



# Generated at 2022-06-13 04:53:41.418199
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={})
    apt_stub = SourcesList(module)
    valid, enabled, source, comment = apt_stub._parse('deb http://archive.canonical.com/ubuntu trusty partner')

    apt_stub.files[apt_stub.default_file] = [(0, valid, enabled, source, comment)]
    apt_stub.modify(apt_stub.default_file, 0, enabled=False)
    assert apt_stub.files[apt_stub.default_file][0][2] == False
    # restore original enabled value
    apt_stub.modify(apt_stub.default_file, 0, enabled=True)
    assert apt_stub.files[apt_stub.default_file][0][2] == True
    # change only the

# Generated at 2022-06-13 04:53:53.344509
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({})
    sl = SourcesList(module)

# Generated at 2022-06-13 04:54:03.920771
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    from mock import MagicMock
    module = MagicMock()
    sl = SourcesList(module)
    sl._apt_cfg_dir_mock = MagicMock(return_value='/tmp/apt')
    module.atomic_move = MagicMock(return_value=True)
    module.set_mode_if_different = MagicMock(return_value=True)
    filename = '/tmp/apt/sources.list'
    sources = [
        (0, True, True, 'deb http://localhost:9999/ trusty main', ''),
        (1, True, True, 'deb http://localhost:9999/ trusty-updates main', ''),
    ]
    sl.files[filename] = sources
    result = sl.dump()
    for source in sources:
        _, valid, enabled, source, comment = source

# Generated at 2022-06-13 04:54:34.963018
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    pass


# Generated at 2022-06-13 04:54:42.441271
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    from ansible.module_utils._text import to_text
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock, patch
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible_collections.ansible.community.plugins.module_utils import basic
    from ansible_collections.ansible.community.plugins.module_utils.distro import module_distro_selector
    from ansible_collections.ansible.community.plugins.module_utils.facts import cache
    module = MagicMock(basic.AnsibleModule)
    module.params = {'codename': 'bionic'}
    module.params['add_ppa_signing_keys_callback'] = lambda command: True

# Generated at 2022-06-13 04:54:55.404569
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = AnsibleModule(argument_spec={})
    with tempfile.TemporaryDirectory() as tmpdir:
        default_file = os.path.join(tmpdir, 'sources.list')
        sl = SourcesList(module)
        sl.add_source('deb http://www.example.org/debian wheezy main', comment='test')
        sl.save()
        assert os.path.exists(default_file)
        with open(default_file) as f:
            assert 'http://www.example.org/debian wheezy main # test' in f.read()
        sl.remove_source('deb http://www.example.org/debian wheezy main')
        sl.save()
        assert not os.path.exists(default_file)


# Generated at 2022-06-13 04:55:07.719499
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda *_, **__: None
    ubuntu_sources_list = UbuntuSourcesList(module)
    ubuntu_sources_list.add_source('ppa:graphics-drivers/ppa')
    ubuntu_sources_list.add_source('ppa:graphics-drivers/ppa')
    ubuntu_sources_list.add_source('ppa:graphics-drivers/ppa')

    assert len(ubuntu_sources_list.files) == 1
    assert len(ubuntu_sources_list.files[next(iter(ubuntu_sources_list.files))]) == 3

    for _ in range(0, 3):
        ubuntu_sources_list.remove_source('ppa:graphics-drivers/ppa')


# Generated at 2022-06-13 04:55:18.239139
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import tempfile
    import os
    import shutil
    import ansible.module_utils.basic
    import ansible.module_utils.six.moves.builtins
    import ansible.module_utils.urls
    import ansible.module_utils._text
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    module.set_fs_attributes_if_different = lambda *args, **kwargs: None
    module.atomic_move = lambda *args, **kwargs: None
    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.fail_json = lambda *args, **kwargs: None
    module.get_bin_path = lambda *args, **kwargs: '/usr/bin/apt-get'

# Generated at 2022-06-13 04:55:26.578587
# Unit test for function revert_sources_list
def test_revert_sources_list():
    provider = {'codename': 'trusty'}
    module = AnsibleModule(argument_spec=dict(
        repo=dict(type='str', required=True),
        state=dict(type='str', default='present', choices=['absent', 'present']),
        filename = dict(type='str', required=False),
        codename = dict(type='str', required=False),
    ))

    # Make sure we don't break anything.
    TEST_FILE = '/etc/apt/sources.list.d/revert-sources-test.list'
    BACKUP_FILE = TEST_FILE + '.backup'
    SOURCES_BEFORE = {TEST_FILE: 'deb http://archive.ubuntu.com/ubuntu/ trusty main universe\n'}

# Generated at 2022-06-13 04:55:35.641169
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = type('', (object,), {})
    module.fail_json = lambda msg: None
    module.atomic_move = lambda src, dst: None

# Generated at 2022-06-13 04:55:47.764996
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    # set codename to zesty, the original codename is hard-coded
    distro.codename = 'artful'
    # test1: with the codename parameter
    # test1.1: with the codename parameter which is the same as the default codename
    module1 = AnsibleModule(argument_spec={'codename': {'type': 'str', 'default': 'artful'}})
    test1_1 = UbuntuSourcesList(module1)
    assert test1_1.codename == 'artful'
    # test1.2: with the codename parameter which is different from the default codename
    module2 = AnsibleModule(argument_spec={'codename': {'type': 'str', 'default': 'zesty'}})
    test1_2 = UbuntuSourcesList(module2)
    assert test1_2

# Generated at 2022-06-13 04:55:56.888441
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    mock_module = AnsibleModule(argument_spec={})
    mock_module.params = {'codename': 'bionic'}

    s = UbuntuSourcesList(mock_module)

    s._parse = Mock(return_value=(True, True, 'deb http://ppa.launchpad.net/foo/bar/ubuntu bionic main'))
    for i in range(2):
        s.add_source('ppa:foo/bar')

    s.remove_source('ppa:foo/bar')
    assert len(s.files) == 0



# Generated at 2022-06-13 04:56:08.576315
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    class Module(object):
        def __init__(self):
            self.params = {'filename': None}
            self.atomic_move = lambda *args: None
            self.set_mode_if_different = lambda *args, **kwargs: None

    sources = SourcesList(Module())

    # Test the default filename
    sources.add_source('deb http://archive.canonical.com/ubuntu hardy partner')
    assert sources.files.keys() == ['/etc/apt/sources.list']

    # Add another, check different default filenames depending on source
    sources.add_source('deb http://archive.canonical.com/ubuntu quantal partner')
    assert sources.files.keys() == ['/etc/apt/sources.list', '/etc/apt/sources.list.d/partner.list']

   

# Generated at 2022-06-13 04:57:14.388990
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():

    module = AnsibleModule({}, check_invalid_arguments=False)
    sl = SourcesList(module)

    test_files = {
        'test1': ['# test1\n', 'deb-src http://test1\n', '# test2\n', '# test3\n'],
        'test2': ['# test4\n', '# test5\n', 'deb http://test2\n', 'test1\n', 'test2\n', 'test3\n'],
        'test3': ['deb-src http://test3\n', 'test1\n', 'test2\n', 'test3\n', '# test6\n', '# test7\n'],
    }

    for filename, sources in test_files.items():
        f = open(filename, 'w')


# Generated at 2022-06-13 04:57:23.624268
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    def mock_atomic_move(src, dst):
        nonlocal src_value, dst_value
        if src == src_value and dst == dst_value:
            raise IOError()
        return (True, None)

    def mock_open(filename, mode):
        nonlocal mock_open_called_with
        mock_open_called_with = filename
        return mock_open_return

    class MockFile(object):
        def __init__(self, *args):
            pass

        def close(self):
            pass

        def write(self, *args):
            raise IOError()

    def mock_iter(self):
        nonlocal iter_called_with
        iter_called_with = self.files

        class MockIter(object):
            def __init__(self):
                pass


# Generated at 2022-06-13 04:57:35.896056
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    M = MagicMock()
    M.magic_method.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M.param.return_value = None
    M

# Generated at 2022-06-13 04:57:47.044610
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class MockModule:
        '''
        All methods and variables will be available for `SourcesList` as attributes,
        so we're not going to implement everything from real `Module` class
        '''

        def __init__(self):
            self.exit_json = None
            self.fail_json = None
            self.atomic_move = None

    class MockOpen:
        def __init__(self, sources):
            self.sources = sources

        def __call__(self, filename, mode='r'):
            self.filename = filename
            self.mode = mode
            return self

        def __iter__(self):
            return iter(self.sources)

        def close(self):
            pass

    module = MockModule()
    module.exit_json = lambda: None

# Generated at 2022-06-13 04:57:54.849031
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.debops.debops.repo_deb.apt_repository import get_add_ppa_signing_key_callback

# Generated at 2022-06-13 04:58:05.164104
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():

    def get_sources_list_wrapper(module_path='/module/path', content=''):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = os.path.join(tmp_dir, 'sources.list')
            with open(tmp_path, 'w') as f:
                f.write(content)

            module = AnsibleModule(
                argument_spec={},
                supports_check_mode=True,
                bypass_checks=True,
            )
            module.params['_ansible_debug'] = True
            module.exit_json = Mock()
            module.run_command = Mock(return_value=(0, '', ''))
            module.get_bin_path = Mock(return_value='/bin/path')
            module.atomic_move = Mock()

# Generated at 2022-06-13 04:58:13.458339
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({}, check_invalid_arguments=False)

# Generated at 2022-06-13 04:58:25.584195
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    m = SourcesList(module)

    m.load('''deb http://example.com/debian dist main
deb http://example.com/debian dist main
# deb http://example.com/debian dist main
''')

    assert m.dump() == {
            '': '''deb http://example.com/debian dist main
deb http://example.com/debian dist main
# deb http://example.com/debian dist main
''',
        }

    assert m.dump() == {
            '': '''deb http://example.com/debian dist main
deb http://example.com/debian dist main
# deb http://example.com/debian dist main
''',
        }


# Generated at 2022-06-13 04:58:37.167513
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = MockModule()
    module.params = {'codename': 'wily'}
    sl = UbuntuSourcesList(module)
    with open(os.path.join(os.path.dirname(__file__), "fixtures", "sources1.list"), 'r') as f:
        for line in f.readlines():
            sl.add_source(line)
    for filename, sources in sl.files.items():
        assert len(sources) == 1
    sl.remove_source('ppa:ubuntu-wine/ppa')
    assert len(sl.files) == 1
    assert sl.files['/etc/apt/sources.list'][0][3] == 'deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu wily main'

# Generated at 2022-06-13 04:58:47.178369
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import pytest
    import ansible_collections.community.general.plugins.module_utils.system.apt as apt_util

    sl = apt_util.SourcesList(None)
    sl.files = {'/tmp/foo.list': [
        (0, True, True, 'deb http://archive.canonical.com/ubuntu foo main', ''),
        (1, True, True, 'deb-src http://archive.canonical.com/ubuntu foo-updates main', '')
    ]}
    sl.save()
    with open('/tmp/foo.list', 'r') as foo:
        assert foo.read() == 'deb http://archive.canonical.com/ubuntu foo main\ndeb-src http://archive.canonical.com/ubuntu foo-updates main\n'



# Generated at 2022-06-13 05:01:35.040150
# Unit test for function install_python_apt
def test_install_python_apt():
    import apt_repository_mock_data as mock_data
    import apt_repository_mock_data.mock as mock
    import aptsources.distro as aptsources_distro
    global apt
    global apt_pkg
    global distro
    global HAVE_PYTHON_APT
    test_env = copy.deepcopy(mock_data.APT_ENV_DICT)
    apt_repository_mock_data.mock = mock
    aptsources_distro = mock_data.aptsources_distro
    apt = mock_data.apt
    apt_pkg = mock_data.apt_pkg
    distro = aptsources_distro.get_distro()
    HAVE_PYTHON_APT = True

# Generated at 2022-06-13 05:01:45.810574
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class MockModule:
        def __init__(self):
            self.params = {'state': 'present', 'filename': None, 'key_url': '', 'apt_key': 'apt-key'}
        def fail_json(self, msg):
            raise AssertionError("Should not reach this line, msg: %s" % msg)
        def run_command(self, cmd, check_rc=True):
            if cmd == 'apt-key export %s' % _MOCK_KEY_FINGERPRINT:
                return (1, '', '')
            else:
                raise AssertionError("Should not reach this line, cmd: %s" % cmd)

        def atomic_move(self, tmp_path, file):
            pass


# Generated at 2022-06-13 05:01:46.416543
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, "No test"

# Generated at 2022-06-13 05:01:55.503111
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule(argument_spec=dict(
        codename=dict(type='str'),
    ))
    repo_list = UbuntuSourcesList(module)
    tmp_file = '/tmp/ansible_test'