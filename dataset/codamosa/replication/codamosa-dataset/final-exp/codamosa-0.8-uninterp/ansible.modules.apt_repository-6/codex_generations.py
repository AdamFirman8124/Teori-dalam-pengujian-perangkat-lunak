

# Generated at 2022-06-13 04:52:33.272721
# Unit test for function revert_sources_list
def test_revert_sources_list():
    '''Tests for the revert_sources_list function'''
    test_dir = '/test/testdir'
    tmp_dir = '/test/testdir_backup'

    def _do_test(test_name, filenames_before, filenames_after, filenames_after_expected):
        '''Helper function that checks that filenames_after_expected is the same
           as the result of reverting filenames_after from filenames_before.'''
        sources_before = dict((filename, '') for filename in filenames_before)
        sources_after = dict((filename, '') for filename in filenames_after)
        sourceslist_before = mock.Mock()
        sourceslist_before.files = dict((filename, []) for filename in filenames_before)

        revert_sources

# Generated at 2022-06-13 04:52:39.101190
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({})
    sources = SourcesList(module)
    sources.files['test'] = [
        (0, True, True, 'source line', 'comment'),
        (1, False, False, 'not a source', 'another comment'),
    ]

    expected = {
        'test': 'source line # comment\n'
    }
    assert sources.dump() == expected



# Generated at 2022-06-13 04:52:46.849719
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    import os
    import tempfile
    import shutil
    import textwrap

    contrib_file_content = textwrap.dedent('''\
    # deb-src http://cdn-aws.deb.debian.org/debian wheezy-backports main
    deb-src http://cdn-aws.deb.debian.org/debian wheezy-backports contrib
    # deb http://cdn-aws.deb.debian.org/debian wheezy-backports main
    deb http://cdn-aws.deb.debian.org/debian wheezy-backports contrib
    ''')


# Generated at 2022-06-13 04:52:59.224253
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    from tempfile import mkdtemp
    from ansible.module_utils import basic
    from ansible.module_utils.common.systemd import systemd

    tmpdir = mkdtemp()

    m = basic.AnsibleModule(argument_spec={
        'state': dict(default='present', choices=['present', 'absent']),
    })

    m.atomic_move = lambda src, dst: os.rename(src, dst)
    m.set_mode_if_different = lambda fn, m, d: os.chmod(fn, m)
    systemd.get_running_systemd_version = lambda: 0

    sl = SourcesList(m)

# Generated at 2022-06-13 04:53:00.658562
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    sl = SourcesList(module)
    assert isinstance(sl, SourcesList)


# Generated at 2022-06-13 04:53:05.454699
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={})
    module.params['filename'] = None
    module.params['key_file'] = None
    module.params['mode'] = None
    module.params['codename'] = None
    sl = UbuntuSourcesList(module)
    assert sl



# Generated at 2022-06-13 04:53:16.815757
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import shutil
    import tempfile
    import time

    class TestModule(object):
        def __init__(self, params={}):
            self.params = params
            self.fail_json_called = False

        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True
            self.fail_json_args = (args, kwargs)

        def atomic_move(self, tmp_path, filename):
            shutil.move(tmp_path, filename)

        def set_mode_if_different(self, filename, this_mode, False_):
            pass

    class TestAptPkg(object):
        def __init__(self, string):
            self.string = string
            self.configed = None


# Generated at 2022-06-13 04:53:22.044583
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    line = "deb-src http://security.ubuntu.com/ubuntu xenial-security main multiverse universe"
    s = SourcesList()
    s.load("./test_sources.list")
    print(s.dump())
    s._remove_valid_source(line)
    print(s.dump())




# Generated at 2022-06-13 04:53:33.779534
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class module(object):
        class params(object):
            pass
        class fail_json(object):
            pass
        class run_command(object):
            pass
        class atomic_move(object):
            pass
        class set_mode_if_different(object):
            pass
        class check_mode(object):
            pass
        @staticmethod
        def check_mode():
            pass

    class distro(object):
        class codename(object):
            pass
        @staticmethod
        def codename():
            pass

    _m = module()
    _d = distro()
    _s = UbuntuSourcesList(_m, _d)

    class response(object):
        class read(object):
            pass

        @staticmethod
        def read():
            return '{}'

    _r = response()



# Generated at 2022-06-13 04:53:42.301268
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    from ansible.module_utils import basic

    module = basic.AnsibleModule({}, {})
    sl = SourcesList(module)
    sl.load('''# My comment
deb http://repo-domain.com/deb/ stable main
deb http://repo-domain.com/deb/ trusty main
#deb http://repo-domain.com/deb/ whezzy main
deb-src http://repo-domain.com/deb/ stable main
''')

# Generated at 2022-06-13 04:54:26.052302
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    m = AnsibleModule(argument_spec={})
    sources_list = SourcesList(m)
    assert sources_list.dump() == {}

    m = AnsibleModule(argument_spec={})
    fd, tmp_path = tempfile.mkstemp(prefix='.sources.list-')
    f = os.fdopen(fd, 'w')
    f.write('deb http://www.example.com/debian stable main\n')
    f.close()
    sources_list = SourcesList(m)
    sources_list.load(tmp_path)
    assert sources_list.dump()['/' + tmp_path] == 'deb http://www.example.com/debian stable main\n'

    m = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 04:54:37.544196
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    from ansible.module_utils import basic
    from ansible.module_utils.six import StringIO

    test_string=StringIO("""# Source line
disable deb http://example.com/ubuntu trusty universe\n""")
    test_module = basic.AnsibleModule(
        argument_spec={},
    )
    test_module.fail_json = lambda msg: None
    sl = SourcesList(test_module)
    assert sl.files == {}
    sl.load(test_string)
    assert sl.files[test_string.name] == [(0, False, False, '# Source line', ''),
                                          (1, True, False, 'disable deb http://example.com/ubuntu trusty universe', '')]


# Generated at 2022-06-13 04:54:44.203982
# Unit test for function install_python_apt
def test_install_python_apt():

    import sys
    from ansible.module_utils.basic import AnsibleModule

    apt_pkg_name = 'python3-apt'
    fake_module = AnsibleModule(
        argument_spec=dict(
            install_python_apt=dict(type='bool', default=True)
        ),
        supports_check_mode=True,
    )
    if sys.version_info[0] < 3:
        apt_pkg_name = 'python-apt'

    try:
        import apt
        import apt_pkg
        import aptsources.distro as aptsources_distro
        distro = aptsources_distro.get_distro()
        fake_module.exit_json(changed=False)
    except ImportError:
        install_python_apt(fake_module, apt_pkg_name)
        fake

# Generated at 2022-06-13 04:54:45.673056
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    assert get_add_ppa_signing_key_callback(dict(check_mode=False)) is not None
    assert get_add_ppa_signing_key_callback(dict(check_mode=True)) is None


# Generated at 2022-06-13 04:54:57.391841
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    a = ansible_module_SourcesList()
    a.load(a.default_file)

# Generated at 2022-06-13 04:55:08.013534
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec={})
    filename = 'testfile.list'
    sources = [
        'deb http://archive.ubuntu.com/ubuntu/ hardy main restricted universe multiverse',
        '# deb http://archive.ubuntu.com/ubuntu/ hardy-updates main restricted universe multiverse',
        'deb http://archive.ubuntu.com/ubuntu/ hardy-security main restricted universe multiverse',
        'deb http://archive.ubuntu.com/ubuntu/ hardy-backports main restricted universe multiverse',
        ''
    ]
    f = open(filename, 'w')
    f.write('\n'.join(sources))
    f.close()
    s = SourcesList(module)
    s.load(filename)
    os.remove(filename)
    assert len(s.files[filename]) == 4

# Generated at 2022-06-13 04:55:18.409239
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={'param': {'required': True, 'type': 'str'}})
    sl = SourcesList(module)

    def do(input_src, enabled, comment, expected_enabled, expected_comment):
        sl.files = {}
        sl.files['test_file'] = []
        sl.load('test_file')
        sl.modify('test_file', 0, enabled, input_src, comment)
        assert sl.files['test_file'][0][1:] == (True, expected_enabled, input_src, expected_comment)

    do('deb http://archive.ubuntu.com/ubuntu/ Intrepid main restricted', True, ' Test Comment ', True, ' Test Comment ')

# Generated at 2022-06-13 04:55:28.663587
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = Mock()
    self = UbuntuSourcesList(module)


    # Test with line.startswith('ppa:')
    line = 'ppa:test'
    self.files = {
        '/etc/apt/sources.list.d/test.list': [
            (
                0,
                True,
                True,
                'deb http://ppa.launchpad.net/test/ubuntu yakkety main',
                'some comment'
            )
        ]
    }
    self.remove_source(line)
    assert self.files == {}

    # Test with line.startswith('#')
    line = '#deb http://ppa.launchpad.net/test/ubuntu yakkety main'

# Generated at 2022-06-13 04:55:41.898817
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(supports_check_mode=True)
    sl = SourcesList(module)
    # Add valid source
    sl.add_source('deb http://example.com/ubuntu trusty main', comment='comment', file='example.list')
    # Modify
    sl.modify('example.list', 0, source='deb http://ex2.com/ubuntu trusty main')
    # Validate
    changed = 0
    valid = 0
    for filename, n, enabled, source, comment in sl:
        changed = 1
        if source == 'deb http://ex2.com/ubuntu trusty main':
            valid = 1
    assert changed == 1
    assert valid == 1
    # Cleanup
    sl.remove_source('deb http://ex2.com/ubuntu trusty main')
    changed = 0
    valid

# Generated at 2022-06-13 04:55:51.818165
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    class MockModule(object):
        def __init__(self, params, debug=False):
            self.params = params
            self.debug = debug
            self.check_mode = False
            self.files = {}
            self.files_old = {}
            self.tmpdir = None

        def run_command(self, cmd, check_rc=True):
            return 0, cmd, ''

        def get_bin_path(self, name, opt_dirs=[]):
            return '%s_test' % name

        def fail_json(self, **kwargs):
            return dict(failed=True, **kwargs)

        def exit_json(self, **kwargs):
            return dict(**kwargs)


# Generated at 2022-06-13 04:56:29.011726
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    require_if = None
    files = {}
    files_expected = {
        '/etc/apt/sources.list.d/myrepo.list': '\n'.join([
            'deb http://http.debian.net/debian jessie-backports main',
        ]),
    }

    params = {
        'filename': 'myrepo.list',
    }
    sources_list = SourcesList(AnsibleModule(
        argument_spec={
            'filename': dict(default=None),
        }
    ))

    # Test that we create a new file if it doesn't exist yet.
    sources_list.files = copy.deepcopy(files)
    sources_list.add_source('deb http://http.debian.net/debian jessie-backports main')
    assert files_expected == sources_list

# Generated at 2022-06-13 04:56:36.993837
# Unit test for method remove_source of class SourcesList

# Generated at 2022-06-13 04:56:42.773764
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule({})
    sources = UbuntuSourcesList(module)
    assert len(sources.files) == 0

# Generated at 2022-06-13 04:56:49.772428
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    '''
    This test checks saving of sources.list.
    '''
    class MockModule(object):
        def __init__(self, sources_list):
            self.sources_list = sources_list

        def atomic_move(self, src, dst):
            self.saved_src = src
            self.saved_dst = dst
            # Copy contents.
            with open(src, 'r') as f:
                self.saved_contents = f.read()
            self.saved_contents_b = [s.encode('utf-8') for s in self.saved_contents.splitlines(True)]

        def fail_json(self, msg):
            raise AssertionError(msg)


# Generated at 2022-06-13 04:56:58.727752
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def _ansible_params(self):
            return self.params

    class FakeDistro(object):
        codename = 'trusty'

    old_distro = distro
    distro = FakeDistro()

    module = FakeModule({ 'codename': None })
    sl = UbuntuSourcesList(module)

    # Verify that the parent class' deepcopy method is called.
    with patch.object(SourcesList, '__deepcopy__') as mock_super:
        sl_copy = deepcopy(sl)
        mock_super.assert_called_once_with(sl, memo=ANY)

    # Verify that the copy has all the expected attributes.
    assert sl_copy.module is sl.module
    assert sl_copy

# Generated at 2022-06-13 04:57:05.869278
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    # Set up.
    filename = 'test.list'
    file = '/etc/apt/sources.list.d/' + filename

    sources = SourcesList(None)
    sources.files[file] = [(0, True, True, "deb http://archive.canonical.com/ubuntu precise partner", ""),
                           (1, True, True, "deb-http://archive.canonical.com/ubuntu precise partner", ""),
                           (2, True, True, "deb http://archive.canonical.com/ubuntu precise multiverse", ""),
                           (3, False, False, "# deb-http://archive.canonical.com/ubuntu precise partner", ""),
                           (4, False, False, "# deb http://archive.canonical.com/ubuntu precise multiverse", "")]


    # Test.
    sources.remove

# Generated at 2022-06-13 04:57:09.967708
# Unit test for constructor of class SourcesList
def test_SourcesList():
    '''
    SourcesList class constructor test.

    This function only creates an object of class SourcesList and checks nothing.
    '''
    # Create a fake module, because SourcesList takes "module" as a parameter
    module = AnsibleModule(argument_spec={})
    SourcesList(module)



# Generated at 2022-06-13 04:57:14.971493
# Unit test for function install_python_apt
def test_install_python_apt():
    run_args = ['apt-get', 'install', 'python-apt', '-y', '-q', '/tmp']
    for rc in (0,1):
        for se in ('Success', 'Failed'):
            yield (rc, 'Success', se, rc == 0)


# Generated at 2022-06-13 04:57:24.063630
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = Mock()
    module.run_command = Mock()
    module.run_command.return_value = (0, b"", "")
    module.fail_json = Mock()
    usl = UbuntuSourcesList(module)
    usl.files = {"sources.list": [1, True, True, "deb http://ppa.launchpad.net/ppa/ubuntu bionic main", ""]}
    usl.remove_source("ppa:ppa")
    assert len(usl.files["sources.list"]) == 0
    usl.files = {"sources.list": [1, True, True, "deb http://ppa.launchpad.net/ppa/ubuntu bionic main", ""]}
    usl.remove_source("deb http://ppa.launchpad.net/ppa/ubuntu bionic main")
    assert len

# Generated at 2022-06-13 04:57:36.098101
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    params = dict(
        owner_name='leannogasawara',
        ppa_name='ubuntu-liatest',
        codename='xenial',
        mode=DEFAULT_SOURCES_PERM,
    )
    m = AnsibleModule(**params)
    u = UbuntuSourcesList(m)
    u.add_source('ppa:%s/%s' % (params['owner_name'], params['ppa_name']), file="_%s_%s.list" % (params['owner_name'], params['ppa_name']))
    u.remove_source('ppa:%s/%s' % (params['owner_name'], params['ppa_name']))

    assert len(u.files) == 1

# Generated at 2022-06-13 04:58:45.592975
# Unit test for function revert_sources_list
def test_revert_sources_list():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock, patch
    from ansible_collections.community.general.plugins.modules.apt_repository import SOURCE_TYPES
    import shutil

    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = False

        def fail_json(self, **kwargs):
            pass

        def set_mode_if_different(self, filename, mode, changed):
            pass

        def run_command(self, command, check_rc=True):
            pass

        def atomic_move(self, src, dest):
            shutil.move(src, dest)


# Generated at 2022-06-13 04:58:53.332762
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    import pytest

    from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.common.network.debian import UbuntuSourcesList

    module_params = {'codename': 'bionic'}

    def add_ppa_signing_keys_callback(command):
        pass

    usl = UbuntuSourcesList(None, add_ppa_signing_keys_callback)
    usl.add_source('ppa:foo/bar')
    assert len(usl.files) == 1

    usl3 = copy.deepcopy(usl)
    assert usl3.files == usl.files

    usl4 = usl.__deepcopy__()
    assert usl4.files == usl.files

# Generated at 2022-06-13 04:59:05.397089
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    test_module = AnsibleModule({})
    test_module.fail_json = fail_json
    test_module.exit_json = exit_json
    test_module.set_mode_if_different = lambda *args: None
    test_module.params = {
        'filename': None
    }
    test_sources_list = SourcesList(test_module)

    test_sources_list._apt_cfg_file = lambda x: '/etc/apt/sources.list'
    test_sources_list._apt_cfg_dir = lambda x: '/etc/apt/sources.list.d'
    test_sources_list._suggest_filename = lambda x: '0.list'


# Generated at 2022-06-13 04:59:12.318697
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    import copy
    def test_add_ppa_signing_keys_callback(command):
        pass

    module = AnsibleModule(argument_spec={})
    sources_list = UbuntuSourcesList(module, add_ppa_signing_keys_callback=test_add_ppa_signing_keys_callback)
    sources_list.add_source("ppa:foo/bar", comment='', file=None)
    new_sources_list = copy.deepcopy(sources_list)
    assert not new_sources_list.files
    assert new_sources_list.codename == sources_list.codename
    assert new_sources_list.LP_API == sources_list.LP_API
    assert new_sources_list.add_ppa_signing_keys_callback == sources_list.add_ppa_signing_

# Generated at 2022-06-13 04:59:23.610020
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:59:36.107090
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible_module_apt import ModuleParameters
    module = ModuleParameters(
        {'comment': 'test'},
        module_paths=['/ansible/test/utils/module_utils/apt/modules']
    )

    def raise_err(*args, **kwargs):
        raise ValueError("this is a test exception")

    sl = UbuntuSourcesList(module, add_ppa_signing_keys_callback=raise_err)


# Generated at 2022-06-13 04:59:41.613608
# Unit test for function revert_sources_list
def test_revert_sources_list():
    module = FakeModule()
    sources_before = dict(s1='deb file:///path/to/something something',
                          s2='deb http://ppa.launchpad.net/test/test/ubuntu focal main')
    sources_after = dict(s1='deb file:///path/to/something something',
                         s2='deb http://ppa.launchpad.net/test/test/ubuntu focal main')
    sourceslist_before = SourcesList(module)
    sourceslist_before.save()
    try:
        revert_sources_list(sources_before, sources_after, sourceslist_before)
    except Exception as e:
        raise Exception(e)



# Generated at 2022-06-13 04:59:49.475095
# Unit test for function revert_sources_list
def test_revert_sources_list():
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {}
            self.check_mode = False
            self.atomic_move = False

    module = AnsibleModuleMock()
    module.atomic_move = True
    sourceslist_before = UbuntuSourcesList(module)
    sources_before = sourceslist_before.dump()
    module.atomic_move = False
    sourceslist_after = UbuntuSourcesList(module)
    sources_after = sourceslist_after.dump()
    revert_sources_list(sources_before, sources_after, sourceslist_before)



# Generated at 2022-06-13 04:59:53.028333
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = DummyModule()
    sources = SourcesList(module)
    for file, sources in sources.files.items():
        for n, valid, enabled, source, comment in sources:
            assert valid
            assert enabled



# Generated at 2022-06-13 04:59:59.157621
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    sl = SourcesList(None)
    sl.add_source('deb http://archive.ubuntu.com/ubuntu/ bionic main restricted')
    sl.add_source('deb http://archive.ubuntu.com/ubuntu/ bionic-security main restricted')
    sl.add_source('deb http://archive.ubuntu.com/ubuntu/ bionic-updates main restricted')

    found = [line for line in sl]
    assert len(found) == 3
    assert found[0][2]
    assert found[1][2]
    assert found[2][2]

    sl2 = SourcesList(None)
    assert len([line for line in sl2]) == 0
    sl2.add_source('deb http://archive.ubuntu.com/ubuntu/ bionic main restricted')
    assert len([line for line in sl2]) == 1

    sl2