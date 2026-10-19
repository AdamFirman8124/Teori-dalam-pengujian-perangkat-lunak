

# Generated at 2022-06-13 04:52:53.536938
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    sourcelist=SourcesList(object)
    sourcelist.files={'/etc/apt/sources.list':[(0, True, True, 'dub http://archive.canonical.com/ubuntu hardy partner', '')]}
    sourcelist.remove_source('deb http://archive.canonical.com/ubuntu hardy partner')
    assert not(sourcelist.files)


# Generated at 2022-06-13 04:53:00.576366
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    sl = SourcesList(module)
    test_file = '/tmp/test_SourcesList_load.sources.list'
    test_data = '''
# comment
deb http://example.com/foo foo main

# comment
# comment 2
'''.strip()
    with open(test_file, 'w') as f:
        f.write(test_data)
    sl.load(test_file)
    os.remove(test_file)

    # without raise_if_invalid_or_disabled so it's default behaviour
    assert sl._parse('# comment') == (False, False, '', 'comment')
    assert sl._parse('') == (False, True, '', '')

# Generated at 2022-06-13 04:53:06.253462
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = MagicMock()
    add_ppa_signing_keys_callback = MagicMock()
    sl = UbuntuSourcesList(module, add_ppa_signing_keys_callback)

    assert isinstance(sl.__deepcopy__(), UbuntuSourcesList)
    assert sl.add_ppa_signing_keys_callback == add_ppa_signing_keys_callback



# Generated at 2022-06-13 04:53:17.417353
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    sl = UbuntuSourcesList(None)
    sl.files['test'] = [(0, True, True, 'deb https://ppa.launchpad.net/ansible/bubblewrap/ubuntu focal main', ''),
                        (1, True, True, 'deb [arch=amd64] http://ppa.launchpad.net/ansible/bubblewrap/ubuntu focal main', ''),
                        (2, True, False, 'deb [arch=amd64] http://ppa.launchpad.net/ansible/bubblewrap/ubuntu focal main', ''),
                        (3, False, True, 'deb [arch=amd64] http://ppa.launchpad.net/ansible/bubblewrap/ubuntu focal main', ''),
                        ]
    sl.remove_source('ppa:ansible/bubblewrap')

# Generated at 2022-06-13 04:53:30.637537
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda *args, **kwargs: None
    module.fail_json = lambda *args, **kwargs: None
    module.atomic_move = lambda *args, **kwargs: None
    module.set_mode_if_different = lambda *args, **kwargs: None

    try:
        import apt
        import apt_pkg
        import aptsources.distro as aptsources_distro

        distro = aptsources_distro.get_distro()

        HAVE_PYTHON_APT = True
    except ImportError:
        HAVE_PYTHON_APT = False

    sources = SourcesList(module)

# Generated at 2022-06-13 04:53:41.038724
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import os
    import random
    import shutil
    import sys
    import tempfile

    try:
        import apt
        import apt_pkg
        import aptsources.distro as aptsources_distro
    except ImportError:
        print('Python-apt is not installed')
        sys.exit(1)

    distro = aptsources_distro.get_distro()

    dir = tempfile.mkdtemp()
    os.chmod(dir, 0o777)


# Generated at 2022-06-13 04:53:50.000397
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default='present', choices=['absent', 'present']),
            repo=dict(required=True),
            filename=dict(default=None),
            update_cache=dict(default=False, type='bool'),
            validate_certs=dict(default=True, type='bool'),
            mode=dict(default=None, type='raw'),
            install_python_apt=dict(default=True, type='bool'),
        ),
        supports_check_mode=True,
    )
    if not HAVE_PYTHON_APT:
        if module.params.get('install_python_apt'):
            install_python_apt(module, 'python-apt')

# Generated at 2022-06-13 04:54:02.766921
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    m = AnsibleModule(argument_spec={'test_variable': {'required': True, 'type': 'str'}})
    sl = SourcesList(m)
    sources_file1 = os.path.join(m.tmpdir, 'etc', 'apt', 'sources.list')
    sources_file2 = os.path.join(m.tmpdir, 'etc', 'apt', 'sources.list.d', 'aaa.list')
    sources = ['deb http://deb.debian.org/debian/ stretch main',
            'deb-src http://deb.debian.org/debian/ stretch main',
            '# deb http://deb.debian.org/debian/ stretch main']
    sl.files[sources_file1] = []
    sl.files[sources_file2] = []

# Generated at 2022-06-13 04:54:07.116788
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module_args = {}
    module = AnsibleModule(
        argument_spec=module_args,
    )

    assert get_add_ppa_signing_key_callback(module) is not None

    module.check_mode = True
    assert get_add_ppa_signing_key_callback(module) is None



# Generated at 2022-06-13 04:54:12.241358
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    import apt
    import tempfile
    import shutil

    ppa = 'ppa:ansible/ansible'

    def mock_key_already_exists(key_fingerprint):
        return True


# Generated at 2022-06-13 04:54:41.337121
# Unit test for function main
def test_main():
    import inspect

    with open(inspect.getfile(inspect.currentframe())) as f:
        lines = [line.strip() for line in f]
    code = "".join(lines[17:])
    #print(code)

    with open(inspect.getfile(object())) as f:
        lines = [line.strip() for line in f]
    code = "".join(lines)
    print(code)


#test_main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:55.402588
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModule(argument_spec={})
    module.params = {'filename': 'some/file/name', 'codename': 'bionic'}
    sources_list = UbuntuSourcesList(module)

    # test remove ppa
    sources_list.add_source('ppa:k-moore/fsl')
    assert sources_list.repos_urls == ['deb http://ppa.launchpad.net/k-moore/fsl/ubuntu bionic main']

    sources_list.remove_source('ppa:k-moore/fsl')
    assert sources_list.repos_urls == []

    # test remove full repository path
    sources_list.add_source('deb http://ppa.launchpad.net/k-moore/fsl/ubuntu bionic main')
    assert sources_list.repos_

# Generated at 2022-06-13 04:54:56.648278
# Unit test for function install_python_apt
def test_install_python_apt():
    assert True is True



# Generated at 2022-06-13 04:55:07.383896
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():

    # Override `apt_pkg.config.find_file` for testing purpose.
    sources_list_file = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'data',
                'test_SourcesList_dump',
                'sources.list'
        ))
    sources_list_d_dir = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'data',
                'test_SourcesList_dump',
                'sources.list.d'
        ))


# Generated at 2022-06-13 04:55:08.935490
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # Unit test for method __iter__ of class SourcesList

    pass


# Generated at 2022-06-13 04:55:22.786636
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec={})
    tpl = tempfile.NamedTemporaryFile()

# Generated at 2022-06-13 04:55:34.509649
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    with open(os.path.join(os.path.dirname(__file__), 'sources.list.example')) as f:
        sourceslist = SourcesList(object())
        sourceslist.files = {'/etc/apt/sources.list': f.readlines()}

        sources = []
        for file, n, enabled, source, comment in sourceslist:
            sources.append((file, n, enabled, source, comment))


# Generated at 2022-06-13 04:55:46.705821
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class ModuleMock(object):
        pass

    module = ModuleMock()
    sl = SourcesList(module)
    sl.files = {}
    test_file = '/tmp/test.sources.list'
    test_lines = [
        'deb http://archive.canonical.com/ubuntu hardy partner',
        '# deb http://archive.canonical.com/ubuntu hardy partner',
        '# invalid source',
        '',
        '#comment',
        '     deb-src http://archive.canonical.com/ubuntu hardy partner',
    ]
    with open(test_file, 'w') as f:
        f.writelines(test_lines)
    sl.load(test_file)


# Generated at 2022-06-13 04:55:59.164382
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    import tempfile
    temp_dir = tempfile.mkdtemp()

    module = MagicMock()
    module.params = {}
    module.params['filename'] = os.path.join(temp_dir, 'test')
    module.params['codename'] = 'trusty'
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.fail_json = MagicMock(side_effect=SystemExit(1))
    module.atomic_move = os.rename
    module.set_mode_if_different = MagicMock()

    def add_ppa_signing_keys_callback(command):
        pass

    l = UbuntuSourcesList(module, add_ppa_signing_keys_callback)
    new_l = deepcopy(l)

    assert id(l) != id

# Generated at 2022-06-13 04:56:03.798853
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule({}, check_mode=True)
    install_python_apt(module, 'python3-apt')
    install_python_apt(module, None)


# Generated at 2022-06-13 04:56:43.527997
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    # get the file as a list of lines
    # [source, comment, enabled]
    test_values = [
                ['deb http://mirror.example.com/debian/ jessie main'],
                ['deb http://mirror.example.com/debian/ jessie main', 'comment', False],
                ['deb http://mirror.example.com/debian/ jessie main', 'comment', True],
                ['deb http://mirror.example.com/debian/ jessie main', None, False],
                ['deb http://mirror.example.com/debian/ jessie main', 'comment', None]
                ]
    # with different combinations of initial values

# Generated at 2022-06-13 04:56:55.801952
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda **kwargs: None
    sources_list = SourcesList(module)

# Generated at 2022-06-13 04:57:03.409807
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={})
    sources_list = SourcesList(module)

    repo = 'deb http://archive.canonical.com/ubuntu hardy partner'
    # should re-add if comment is not specified
    sources_list.add_source(repo)
    sources_list.add_source(repo)
    assert len(list(sources_list)) == 1

    # add comment to last of the duplicates
    sources_list.add_source('#' + repo)

    sources_list.add_source(repo, comment='duplicate')
    assert len(list(sources_list)) == 1

    # add comments to rest of the duplicates

# Generated at 2022-06-13 04:57:13.121792
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    m = AnsibleModule(argument_spec=dict())
    lines = [
        'deb http://www.example.org/debian wheezy-backports main',
        'deb http://www.example.org/debian wheezy main',
        '# deb http://www.example.org/debian wheezy-updates main',
        '',
        '# some comment',
        '# deb http://www.example.org/debian wheezy-updates main',
        '# another comment',
        'deb http://www.example.org/debian wheezy-updates main',
    ]

# Generated at 2022-06-13 04:57:18.675376
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    """Unit tests for the method `UbuntuSourcesList.__deepcopy__`"""
    module = AnsibleModule(argument_spec={'codename': {'type': 'str'}})
    _test_obj = UbuntuSourcesList(module)
    _result = _test_obj.__deepcopy__()
    assert isinstance(_result, UbuntuSourcesList)


# Generated at 2022-06-13 04:57:25.887152
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    import os
    import tempfile
    class FakeModule():
        def __init__(self):
            self.check_mode = False
            self.debug = False
            self.failed = False
            self.params = {'files': {'Foo': ['deb cdrom:[Ubuntu-MATE 17.04 _Zesty Zapus_ - Release amd64 (20170412)]/ zesty main'], 'Bar': []}}

        def get_bin_path(self, arg):
            return '/tmp'

        def run_command(self, cmd):
            return 0, '', ''

        def atomic_move(self, src, dst):
            f1 = open(src, 'r')
            f2 = open(dst, 'w')
            f2.write(f1.read())
            f1.close()
            f2

# Generated at 2022-06-13 04:57:35.439270
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = MagicMock(name='module')
    add_ppa_signing_keys_callback = MagicMock(name='add_ppa_signing_keys_callback')
    ubuntu_sources_list = UbuntuSourcesList(module, add_ppa_signing_keys_callback)
    copy_ubuntu_sources_list = copy.deepcopy(ubuntu_sources_list)
    assert copy_ubuntu_sources_list.module is module
    assert copy_ubuntu_sources_list.add_ppa_signing_keys_callback is add_ppa_signing_keys_callback


# Generated at 2022-06-13 04:57:43.065940
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    import inspect
    import sys
    import types
    import unittest
    if sys.version_info[:2] <= (2, 6):
        import unittest2 as unittest
    from mock import MagicMock, Mock

    # Create a fake AnsibleModule object
    class FakeAnsibleModule(object):
        def __init__(self):
           self.params = { 'codename': 'xenial' }
           self.fail_json = Mock()
           self.atomic_move = Mock()
           self.set_mode_if_different = Mock()
           self.run_command = Mock()

    # Create a fake AnsibleModule object

# Generated at 2022-06-13 04:57:47.757756
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    import doctest
    failure_count, test_count = doctest.testmod(UbuntuSourcesList)
    assert failure_count == 0


# Generated at 2022-06-13 04:57:55.052849
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    list = UbuntuSourcesList(None)
    list.load("/usr/share/unit_test_data/sources.list")
    list.remove_source("ppa:whatever/ppa")
    assert "deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu vivid main" not in [source for _, _, _, source, _ in list], \
        "This source should not be found in the list"
    list.remove_source("deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu vivid main")
    assert "deb http://ppa.launchpad.net/ubuntu-wine/ppa/ubuntu vivid main" in [source for _, _, _, source, _ in list], \
        "This source should be found in the list"
# Test unit


# Generated at 2022-06-13 04:59:26.875425
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    sl = UbuntuSourcesList(None)
    sl.files = {
        '/etc/apt/sources.list.d/ansible_python3_ppa.list': [
            (0, True, True, 'deb http://ppa.launchpad.net/ansible/python3/ubuntu bionic main', ''),
            (1, True, True, 'deb-src http://ppa.launchpad.net/ansible/python3/ubuntu bionic main', ''),
        ]
    }
    sl.remove_source('ppa:ansible/python3')
    assert '/etc/apt/sources.list.d/ansible_python3_ppa.list' not in sl.files

    sl = UbuntuSourcesList(None)

# Generated at 2022-06-13 04:59:38.271861
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    # Patch for Python 2.5 compatibility
    apt_pkg.Config = type('', (), {})
    apt_pkg.Config.FindFile = lambda filespec: False
    apt_pkg.Config.FindDir = lambda dirspec: False

    # Mock add_ppa_signing_keys_callback
    def add_ppa_signing_keys_callback(command):
        pass

    module = Mock()
    module.params = dict(codename='xenial')

    apt_sources = UbuntuSourcesList(module, add_ppa_signing_keys_callback)

    class MockFetchUrl(object):
        def read(self):
            return '{"signing_key_fingerprint": "1234"}'

    module.fetch_url = Mock()
    module.fetch_url.return_value = MockFetchUrl(), dict()

# Generated at 2022-06-13 04:59:49.641687
# Unit test for function main

# Generated at 2022-06-13 04:59:52.712044
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    u = UbuntuSourcesList('module')
    u1 = copy.deepcopy(u)
    assert u.module == u1.module
    assert u.add_ppa_signing_keys_callback == u1.add_ppa_signing_keys_callback
    assert u.codename == u1.codename



# Generated at 2022-06-13 04:59:58.489547
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockAddPpaSigningKeysCallback(object):
        def __init__(self, *args, **kwargs):
            pass

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            raise NotImplementedError

        def set_mode_if_different(self, *args, **kwargs):
            raise NotImplementedError

    class MockDistro(object):
        codename = 'test_codename'

    class MockUbuntuSourcesList(UbuntuSourcesList):
        def __init__(self, *args, **kwargs):
            raise NotImplementedError

    distro.linux_distribution = lambda *args, **kwargs: ('Test Distribution', 'test_version', '')


# Generated at 2022-06-13 05:00:11.456597
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    class UbuntuSourcesList_mock(UbuntuSourcesList):
        def __init__(self, module, add_ppa_signing_keys_callback=None):
            self.module = module
            self._parse = lambda x, y: (True, True, x, '')
            self.files = {'file1': [(1, True, True, 'first', ''), (2, True, True, 'second', '')],
                          'file2': [(1, True, False, 'third', '')]}

        def _remove_valid_source(self, source):
            # Just check that it's been called with the same argument as in remove_source
            self.files['file1'].pop(0)

    module = dict()
    add_ppa_signing_keys_callback = lambda x: 'callback'
    sl = UbuntuSources

# Generated at 2022-06-13 05:00:22.249589
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    module = AnsibleModule({'filename': '/dev/null'})

    def load(file):
        pass

    def save(self):
        pass

    sl = SourcesList(module)
    sl.load = load
    sl.save = save

    # test1
    sl.add_source('deb http://archive.canonical.com/ hardy partner', comment='comment', file='/dev/null')
    assert sl.files['/dev/null'] == [(-1, True, True, 'deb http://archive.canonical.com/ hardy partner', 'comment')], sl.files

    # test2
    sl.files = {}
    sl.new_repos = set()
    sl.add_source('deb http://archive.canonical.com/ hardy partner', comment='comment')

# Generated at 2022-06-13 05:00:23.605184
# Unit test for function main
def test_main():
  from ansible.modules.packaging.os import apt_repository
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils._text import to_byt

# Generated at 2022-06-13 05:00:34.140045
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class Module:
        def __init__(self):
            self.params = {
                'mode': 'new'
            }

        def set_mode_if_different(self, filename, this_mode, recursive):
            pass

        def atomic_move(self, tmp_path, filename):
            pass

        def fail_json(self, msg):
            pass

    o = UbuntuSourcesList(Module())
    o.add_source('ppa:kkruz/random')
    assert o.files[o._expand_path('kkruz_random.list')][0][3] == 'deb http://ppa.launchpad.net/kkruz/random/ubuntu DEFAULT main'

    o = UbuntuSourcesList(Module())
    o.add_source('ppa:kkruz/random', 'random')

# Generated at 2022-06-13 05:00:44.059308
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    DEFAULT_SOURCES_PERM = 0o0644
    VALID_SOURCE_TYPES = ('deb', 'deb-src')

    line = "deb http://archive.canonical.com/ubuntu hardy partner"
    comment = ''
    file = 'my_simple.list'
    source_list = SourcesList()
    source_list._add_valid_source(line, comment, file)

    assert(source_list.files.keys() == ['/etc/apt/sources.list.d/my_simple.list'])
