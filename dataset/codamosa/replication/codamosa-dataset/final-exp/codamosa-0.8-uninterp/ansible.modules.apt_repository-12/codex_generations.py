

# Generated at 2022-06-13 04:52:38.854120
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    '''Test dump() method of class SourcesList.

    Create a dummy class with the same interface as SourcesList.
    Add content to it.
    Test dump() result against expected output.
    '''
    class TestSourcesList(object):
        def __init__(self, something):
            self.files = {}

# Generated at 2022-06-13 04:52:45.577111
# Unit test for function main
def test_main():
    import argparse
    module = argparse.Namespace()
    module.params = {'repo': 'deb http://ppa.launchpad.net/ansible/ansible-2.9/ubuntu bionic main',
                     'state': 'present',
                     'mode': None,
                     'update_cache': False,
                     'filename': None,
                     'update_cache_retries': 5,
                     'update_cache_retry_max_delay': 12,
                     'install_python_apt': True,
                     'validate_certs': True,
                     'codename': 'bionic'}
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:57.864135
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    sources_list = SourcesList(module)

    sources_list.add_source('deb http://example.com/ubuntu trusty main')
    sources_list.add_source('deb http://example.com/ubuntu trusty main')
    sources_list.add_source('# deb http://example.com/ubuntu trusty multiverse')
    sources_list.add_source('# deb http://example.com/ubuntu trusty universe')
    sources_list.add_source('# deb http://example.com/ubuntu trusty restricted')
    sources_list.add_source('deb http://example.com/ubuntu trusty main')
    sources_list.add_source('deb http://example.com/ubuntu trusty main')
    sources_list.add_source('foo http://example.com/ubuntu trusty main')

# Generated at 2022-06-13 04:53:10.817978
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class ModuleStub(object):
        @staticmethod
        def fail_json(msg):
            sys.stderr.write('FAILED: %s\n' % msg)

        @staticmethod
        def get_bin_path(binary):
            return binary

    class TempFileStub(object):
        def __init__(self, name, mode='w'):
            self.name = name
            self.mode = mode
            self.content = []
            self.d = {}

        def write(self, s):
            self.content.append(s)

        def close(self):
            fn = self.name.split('/')[-1]
            self.d[fn] = ''.join(self.content)

    sys.modules['apt'] = apt
    sys.modules['apt_pkg'] = apt

# Generated at 2022-06-13 04:53:17.273257
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    class Module(object):
        def __init__(self):
            self.params = {}
            self.called = []
            self.warnings = []

        def fail_json(self, **args):
            self.called.append(('fail', args.copy()))

        def warn(self, warn):
            self.warnings.append(warn)

        def atomic_move(self, source, dest):
            pass

        def set_mode_if_different(self, *args):
            pass

    module = Module()
    sources_list = SourcesList(module)
    sources_list.load('testdata/sources_list')

    file = sources_list.files['testdata/sources_list']
    assert len(file) == 4

# Generated at 2022-06-13 04:53:28.363718
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass


PY3_IMP_ERR = None
try:
    if PY3:
        import urllib.parse as urlparse
        import urllib.request as urllib2
        import urllib.error as urllib_error
        import urllib.request as urllib_request
        import xmlrpc.client as xmlrpclib
    else:
        import urlparse
        import urllib2
        urllib_error = urllib2
        import urllib as urllib_request
        import xmlrpclib
except ImportError as e:
    PY3_IMP_ERR = e



# Generated at 2022-06-13 04:53:38.696011
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import ansible.module_utils.six.moves.builtins as builtins

    module = AnsibleModule(argument_spec={})
    if not hasattr(builtins, 'open'):
        builtins.open = None

    source = SourcesList(module)
    source.load("tests/fixtures/sources.list")
    source.save()

    with open("tests/fixtures/sources.list", "r") as fd:
        content = fd.read()

    assert content == "#\ndeb http://example.com trusty main\n"
    os.remove("tests/fixtures/sources.list")



# Generated at 2022-06-13 04:53:48.707142
# Unit test for function revert_sources_list
def test_revert_sources_list():
    os.environ['DEBIAN_FRONTEND'] = 'noninteractive'
    os.environ['APT_LISTBUGS_FRONTEND'] = 'none'
    os.environ['APT_LISTCHANGES_FRONTEND'] = 'none'
    os.environ['LC_ALL'] = 'C'
    os.environ['LANG'] = 'C'
    os.environ['LANGUAGE'] = 'C'

    module = AnsibleModule(
        argument_spec=dict(
            filename=dict(required=True, type='str'),
            state=dict(required=True, type='str'),
            src=dict(required=True, type='str')
        ),
        supports_check_mode=True
    )
    m_open = mock_open()

# Generated at 2022-06-13 04:53:57.219379
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModuleMock()
    module.params['codename'] = None
    module.params['filename'] = None
    module.params['mode'] = None
    module.params['state'] = None
    module.params['update_cache'] = None
    module.params['update_cache_valid_time'] = None
    ubuntu_sources_list = UbuntuSourcesList(module, add_ppa_signing_keys_callback=None)


# Generated at 2022-06-13 04:54:09.380283
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    from ansible.module_utils import basic
    import ansible.module_utils.common.text.converters as conv

    # Test data
    sources_file = """# deb cdrom:[Debian GNU/Linux 9.7.1 _Stretch_ - Official amd64 DVD Binary-1 20190216-10:45]/ stretch contrib main
# deb cdrom:[Debian GNU/Linux 9.7.1 _Stretch_ - Official amd64 DVD Binary-1 20190216-10:45]/ stretch main

deb http://debian.mirror.iweb.com/debian/ stretch main contrib
# deb-src http://ftp.debian.org/debian/ stretch main"""

    # Create mock module
    module = basic.AnsibleModule(argument_spec={})

    # Create SourcesList object and test load method

# Generated at 2022-06-13 04:55:04.239613
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = None
    sl = SourcesList(module)
    sl.files = {'a': [(0, True, True, 'foo', ""), (1, True, True, 'bar', ""), (2, True, True, 'baz', "")]}
    sl.remove_source(u'bar')
    sl.remove_source(u'  bar  ')
    assert sl.files == {'a': [(0, True, True, 'foo', ""), (1, True, True, 'baz', "")]}


# Generated at 2022-06-13 04:55:12.657037
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule({'codename': 'xenial'})
    sl = UbuntuSourcesList(module)
    sl.load(os.path.join(os.path.dirname(__file__), 'sources.list'))
    assert len(sl.files) == 1
    assert len(sl.repos_urls) == 1
    assert len(sl.files['/etc/apt/sources.list']) == 2
    assert len(sl.repos_urls) == 1
    assert len(sl.repos_urls) == 1
    assert '/etc/apt/sources.list' in sl.files
    assert len(sl.files['/etc/apt/sources.list']) == 2
    sl.remove_source('aa')
    assert len(sl.files) == 1
    assert len

# Generated at 2022-06-13 04:55:24.390858
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    fake_main = FakeDebianSourcesList()
    fake_module = FakeModule()

    fake_module.params = dict(
        codename='bionic',
    )

    sources_list = UbuntuSourcesList(fake_module)

    try:
        sources_list.add_source(line='ppa:ansible/ansible')
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise

    assert sources_list.files == {
        u'/etc/apt/sources.list.d/ansible_ansible_bionic.list': [
            (0, True, True, u'deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main', '')
        ]
    }

# Generated at 2022-06-13 04:55:35.260226
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = AnsibleModule(argument_spec=dict())
    sources = SourcesList(module)

    assert sources.default_file == '/etc/apt/sources.list'
    assert sources.files == {}

    # malformed file
    filename = '/tmp/foo.list'
    open(filename, 'w').write('\n')
    sources.load(filename)
    assert sources.files == {}

    # malformed file
    open(filename, 'w').write('malformed')
    sources.load(filename)
    assert sources.files == {}

    # malformed source
    open(filename, 'w').write('malformed\n')
    sources.load(filename)
    assert sources.files == {}

    # valid source, but included in sources.list

# Generated at 2022-06-13 04:55:41.899062
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec={})
    module.params['filename'] = 'test.list'
    sourceslist = test_SourcesList_add_source()
    dumpstruct = sourceslist.dump()
    assert 'test.list' in dumpstruct
    assert len(dumpstruct) == 1
    for filename, lines in dumpstruct.items():
        assert filename == 'test.list'
        assert len(lines.splitlines()) == 1

# Generated at 2022-06-13 04:55:43.402281
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    pass



# Generated at 2022-06-13 04:55:52.710149
# Unit test for function main
def test_main():
    import ansible_collections.community.systemd.tests.unit.modules.utils.fixtures_loader as fixtures_loader

    def pkg_exists(name):
        # We need this function because apt.cache.Cache.has_key() doesn't handle
        # packages that have multiple versions installed, but only one of that
        # version will be considered "installed". We can't use
        # apt.cache.Cache.installed() for the same reason.
        # Example repository: "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted"
        # Example package: "ansible"
        return name in {pkg.name for pkg in apt.Cache().values()}

    def get_sources_list():
        sources_list = []

# Generated at 2022-06-13 04:56:04.232406
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module_mock = MagicMock()

    sources_list = UbuntuSourcesList(module_mock)
    sources_list.new_repos.add('/some/file')

    source_mock = MagicMock()
    with patch('ansible_collections.ansible.community.plugins.modules.source_control.SourcesList._parse', lambda self, x, raise_if_invalid_or_disabled=True: (True, True, source_mock, '')):
        with patch('ansible_collections.ansible.community.plugins.modules.source_control.SourcesList._suggest_filename', lambda self, x: '/some/file'):
            sources_list.add_source('some line')

    assert sources_list.files == {'/some/file': [(0, True, True, source_mock, '')]}

# Generated at 2022-06-13 04:56:05.535290
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    m = AnsibleModule(argument_spec={})
    sl = UbuntuSourcesList(m)
#

# Generated at 2022-06-13 04:56:11.262932
# Unit test for function install_python_apt
def test_install_python_apt():
    class FakeModule(object):
        def __init__(self):
            class FakeRunCommand(object):
                def __init__(self):
                    self.rc = 0
                    self.se = "stderr"
                def __call__(self, *args, **kwargs):
                    return self.rc, "stdout", self.se

            self.run_command = FakeRunCommand()

            class FakeCheckMode(object):
                def __init__(self):
                    self.called = False

                def __call__(self, *args, **kwargs):
                    self.called = True

            self.fail_json = FakeCheckMode()

        def get_bin_path(self, *args, **kwargs):
            return "apt-get"

    apt_pkg_name = "python-apt"
    m = FakeModule

# Generated at 2022-06-13 04:57:22.382081
# Unit test for function install_python_apt
def test_install_python_apt():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import json
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)
    cmd = ["apt-get", "update"]
    rc, out, err = module.run_command(cmd)
    assert rc == 0
    cmd = ["apt-get", "install", "python-apt", "-y", "-q"]
    rc, out, err = module.run_command(cmd)
    assert rc != 0



# Generated at 2022-06-13 04:57:29.166062
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={
        'filename': {'type': 'path'},
        'mode': {'type': 'int'},
        'codename': {'type': 'str'},
    })
    module.exit_json = Mock()

    UbuntuSourcesList(module)

    assert module.exit_json.called == True


# Generated at 2022-06-13 04:57:31.136012
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    sources_list = SourcesList(apt, 'deb foo/bar baz')
    assert sources_list.__iter__() == [(0,True,'deb foo/bar baz','')]

# Generated at 2022-06-13 04:57:35.760217
# Unit test for function revert_sources_list
def test_revert_sources_list():
    sl = SourcesList(module)
    sl.load('/etc/apt/apt.conf.d/50unattended-upgrades')
    sl1 = copy.deepcopy(sl)
    sl.save()
    assert(sl.dump() == sl1.dump())
    sl2 = copy.deepcopy(sl)
    sl.modify('/etc/apt/apt.conf.d/50unattended-upgrades', 0, comment='reverting test')
    sl.save()
    assert(sl.dump() != sl1.dump())
    sl3 = copy.deepcopy(sl)
    revert_sources_list(sl1.dump(), sl2.dump(), sl)
    assert(sl.dump() == sl1.dump())
    revert_sources_list(sl1.dump(), sl3.dump(), sl)

# Generated at 2022-06-13 04:57:46.472622
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    class Module(object):
        def __init__(self, **kwargs):
            self.params = dict(filename='test.list')
            self.params.update(kwargs)

        def fail_json(self, msg):
            print(msg)
            raise ValueError(msg)

    m = Module()
    s = SourcesList(m)
    s.add_source('deb http://localhost/ /', comment='test')
    assert s.dump()['test.list'] == 'deb http://localhost/ / # test\n'
    s.modify('test.list', 0, enabled=False, comment=None)
    assert s.dump()['test.list'] == '# deb http://localhost/ /\n'



# Generated at 2022-06-13 04:57:54.824617
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    """
    Test for method __iter__ of class SourcesList.
    """
    sl = SourcesList(AnsibleModule(argument_spec={}))

# Generated at 2022-06-13 04:58:02.372268
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec={})
    failed_files = []
    for test_file in os.listdir('test/input/sources_list_load'):
        with open('test/input/sources_list_load/%s' % test_file, 'r') as input:
            sl = SourcesList(module)
            sl.load(input.read())
        with open('test/expected/sources_list_load/%s' % test_file, 'r') as expected:
            if json.load(expected) != sl.files:
                failed_files.append(test_file)
    return failed_files


# Generated at 2022-06-13 04:58:07.265986
# Unit test for function main
def test_main():
    myargs = {"repo":"/tmp/test_aptrepo_dir/ansible_1372117518.5","state":"present"}
    set_module_args(myargs)
    result = main()
    assert result['changed'] == True


# Generated at 2022-06-13 04:58:11.230276
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    import copy
    import mock
    sl = UbuntuSourcesList(
        mock.Mock(),
        add_ppa_signing_keys_callback=mock.Mock()
    )
    new_sl = copy.deepcopy(sl)
    assert new_sl.add_ppa_signing_keys_callback is not None



# Generated at 2022-06-13 04:58:23.850996
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = MockAnsibleModule({'mode': DEFAULT_SOURCES_PERM})

    # Create a simple test sources list
    source_file = 'test_SourcesList_save_sources_list'
    sources_content = '''\
# first line
deb http://archive.ubuntu.com/ubuntu quantal main restricted universe multiverse # quantal-updates
'''
    fs = MockFileSystem({source_file: sources_content})
    sources_list = SourcesList(module)
    sources_list.load(source_file)

    # Create a simple test sources list
    path_parts = os.path.split(source_file)
    sources_list.add_source('deb http://archive.canonical.com/ubuntu quantal main restricted universe multiverse', file=path_parts[1])

    # Test saving
   

# Generated at 2022-06-13 04:59:40.788845
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    # Create a SourcesList object with mocked module object
    sl = UbuntuSourcesList(MockModule())
    # Add a source list
    sl.add_source('ppa:danielrichter2007/grub-customizer', 'Added for Grub2 Customizer')
    # Add a source list
    sl.add_source('deb http://download.virtualbox.org/virtualbox/debian bionic contrib', 'Added for Virtual Box')
    # Add a source list
    sl.add_source('ppa:team-xbmc/ppa', 'Added for Kodi')
    # Remove a source list
    sl.remove_source('ppa:danielrichter2007/grub-customizer')
    # Assert number of sources list
    assert len(sl.repos_urls) == 2

# Generated at 2022-06-13 04:59:50.742842
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # __iter__ is an iterator, so we can not test it directly
    # We need to convert it to list
    src = SourcesList(None)

# Generated at 2022-06-13 04:59:56.999762
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class module:
        class __dict__:
            filename = None
    x = UbuntuSourcesList(module)
    x.files['1.txt'] = [(0, False, False, '', '')]
    x.codename = 'codename'
    x.add_source('ppa:<name>/<name2>', '', '3.txt')
    assert x.files['3.txt'] == [(0, True, True, 'deb http://ppa.launchpad.net/<name>/<name2>/ubuntu codename main', '')]
    x.add_source('deb', '', '1.txt')
    assert x.files['1.txt'] == [(0, False, False, '', ''), (1, True, True, 'deb', '')]
    x.files['1.txt'] = []

# Generated at 2022-06-13 05:00:09.430248
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec={})

    default_file = '/etc/apt/sources.list'
    file = '/tmp/mock.list'
    d = '/tmp/sources.list.d'

    content = '#deb\n' \
              'deb http://no1.com stable main\n' \
              'deb-src http://no2.com stable main\n' \
              'deb-src http://no3.com stable main # comment\n' \
              '# deb http://no4.com stable main\n'

# Generated at 2022-06-13 05:00:19.385023
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    '''
    Test the load method of class SourcesList.
    This is based off of test_apt_repository.py from Ansible.
    '''
    from io import StringIO
    from ansible.module_utils.common.validation import check_type_bool, check_type_dict, check_type_list, fail_json
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION

    class FakeModule(object):
        def __init__(self, params, check_mode=False, diff=False, run_command_check_rc=True, atomic_move_failure=False):
            self.params = params
            self.check_mode = check_mode
            self.has_diff = diff
            self.run_command_check_rc = run_command_check_rc

# Generated at 2022-06-13 05:00:31.218808
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    # set params
    params = dict(
        codename=None,
        filename=None,
        mode=None
    )

    # Execute 
    # expected result: __deepcopy__
    result = UbuntuSourcesList(params)
    assert result == '__deepcopy__'
    # Unit test for method _expand_ppa of class UbuntuSourcesList
    def test_UbuntuSourcesList__expand_ppa():
        # set params
        path = 'ppa:canonical-kernel-team/ppa'

        # Execute 
        # expected result: __expand_ppa
        result = UbuntuSourcesList._expand_ppa(path)
        assert result == '__expand_ppa'
    # Unit test for method _get_ppa_info of class UbuntuSourcesList

# Generated at 2022-06-13 05:00:44.891602
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    # mock module
    module = type('', (), dict(fail_json=lambda self, msg: None,
                               params=dict(state='absent')))()
    t = SourcesList(module)
    t.files['/etc/apt/sources.list'] = [
        (0, True, True, 'deb http://example.com/ubuntu precise main universe', ''),
        (0, True, True, 'deb http://example.com/ubuntu precise main universe', ''),
        (0, True, True, 'deb http://example.com/ubuntu precise main universe', ''),
    ]
    t.modify('/etc/apt/sources.list', 0)

# Generated at 2022-06-13 05:00:53.188069
# Unit test for method load of class SourcesList

# Generated at 2022-06-13 05:01:04.879914
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule(
        argument_spec = dict(
        )
    )

# Generated at 2022-06-13 05:01:13.353712
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    import unittest
    import tempfile
    import shutil
    from ansible.module_utils.apt import SourcesList
    from ansible.module_utils.common.respawn import has_respawned, probe_interpreters_for_module, respawn_module

    # I take a lot of inspiration from:
    # https://testing.googleblog.com/2013/05/just-say-no-to-more-end-to-end-tests.html
    # This is not at all the same but it does help to enforce a disciplined approach
    class SourcesListTestCase(unittest.TestCase):
        def _add_sources(self, sl, sources):
            sl.files = {}
            for source in sources:
                sl.add_source(source, comment='')
                sl.save()
