

# Generated at 2022-06-13 04:52:42.662519
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    # Initialize the instance of class UbuntuSourcesList
    usl = UbuntuSourcesList(
        module=None,
        add_ppa_signing_keys_callback=None
    )

    # Test method add_source() with ppa:
    ppa = 'ppa:wiznote-team/ppa'
    comment = 'This is a test.'

    # call method
    usl.repos_urls = []

# Generated at 2022-06-13 04:52:55.963307
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    def dump(sl):
        return {f: [(enabled, source, comment) for n, valid, enabled, source, comment in sources] for f, sources in sl.files.items()}
    module = AnsibleModule({})
    sl = SourcesList(module)

# Generated at 2022-06-13 04:53:01.771389
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule
    module.run_command = MagicMock()
    module.get_bin_path = MagicMock()
    module.get_bin_path.return_value = True
    module.check_mode = False

    install_python_apt(module, 'python-apt')



# Generated at 2022-06-13 04:53:13.338005
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    sources_list = SourcesList(module)
    sources_list.files["/path/to/fake/file"] = [(0, False, False, '' , ''), (1, True, True, "fake deb line" , ""), (2, False, False, '' , '')]
    assert sources_list.files["/path/to/fake/file"] == [(0, False, False, '' , ''), (1, True, True, "fake deb line" , ""), (2, False, False, '' , '')]
    test_iter = iter(sources_list)
    for file, n, enabled, source, comment in test_iter:
        assert file == "/path/to/fake/file"
        assert n == 1
        assert enabled
        assert source == "fake deb line"

# Generated at 2022-06-13 04:53:25.502541
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    module = type('module', (object,), dict(
        params=dict(
            repo='deb http://example.com/trusty trusty main',
            update_cache=False,
            filename='example.list'
        ),
        atomic_move=lambda *args: None,
        set_mode_if_different=lambda *args: None,
        fail_json=lambda *args: None,
        exit_json=lambda *args: None
    ))()

    sources_list = SourcesList(module)
    sources_list.add_source(module.params['repo'], file=module.params['filename'])

    assert len(sources_list.new_repos) == 1
    assert list(sources_list.new_repos)[0] == module.params['filename']
    assert module.params['repo']

# Generated at 2022-06-13 04:53:38.374359
# Unit test for constructor of class SourcesList
def test_SourcesList():
    # Empty sources.list means empty dict:
    sources_list = SourcesList()
    assert list(sources_list.files.keys()) == []

    # One source line means one entry in sources.list:
    sources_list = SourcesList(['deb http://foo'])
    assert list(sources_list.files.keys()) == ['sources.list']

    # Empty sources.list means empty SourcesList:
    sources_list = SourcesList([])
    assert list(sources_list.files.keys()) == ['sources.list']
    assert list(sources_list) == []

    # One source line means one source:
    sources_list = SourcesList(['deb http://foo'])
    assert list(sources_list) == [('sources.list', 0, True, 'deb http://foo', '')]

   

# Generated at 2022-06-13 04:53:47.803177
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = AnsibleModule(
        argument_spec=dict(
            codename=dict(default=None)
        )
    )

    def add_ppa_signing_key_dummy(command):
        return command

    sl = UbuntuSourcesList(module, add_ppa_signing_keys_callback=add_ppa_signing_key_dummy)
    sl.add_source('ppa:ondrej/php')

    repo_urls = sl.repos_urls

    assert len(repo_urls) == 1
    assert repo_urls[0] == 'deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main'


# Generated at 2022-06-13 04:53:48.619566
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    pass

# Generated at 2022-06-13 04:54:01.739892
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={'state': dict(default='present', choices=['absent', 'present']),
                                          'deb': dict(required=False),
                                          'codename': dict(required=False),
                                          'filename': dict(required=False),
                                          'update_cache': dict(default=False, type='bool')})
    instance = UbuntuSourcesList(module)
    assert instance._apt_cfg_file('Dir::Etc::sourceparts') == '/etc/apt/sources.list.d'
    assert instance._apt_cfg_dir('Dir::Etc::sourceparts') == '/etc/apt/sources.list.d'
    assert instance.default_file == '/etc/apt/sources.list'
    assert len(list(instance)) >= 1


# Unit test

# Generated at 2022-06-13 04:54:10.885596
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    s = SourcesList(module)
    assert s.dump() == {}

    file = "/etc/apt/sources.list"
    s.files[file] = [(0, True, True, 'deb http://archive.canonical.com/ubuntu utopic partner', 'Archive partner'),
                     (1, True, True, 'deb-src http://archive.canonical.com/ubuntu utopic partner', 'Archive partner'),
                     (2, False, False, '# deb http://archive.ubuntu.com/ubuntu utopic main restricted', 'Main restricted')]

    d = s.dump()

# Generated at 2022-06-13 04:54:56.750690
# Unit test for function install_python_apt
def test_install_python_apt():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.apt_pkg as apt_pkg
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    try:
        import apt
        import apt_pkg
        import aptsources.distro as aptsources_distro
        distro = aptsources_distro.get_distro()
    except ImportError:
        from unittest import mock
        import sys
        import io

        # install_python_apt() does not work in check mode if python-apt is not installed

# Generated at 2022-06-13 04:55:08.854833
# Unit test for function install_python_apt
def test_install_python_apt():
    import random
    import string
    import os
    import sys

    # Create a temporary file to stand in for module.run_command
    # Python 2: returns byte string
    # Python 3: returns str
    def get_random_string():
        if PY3:
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        else:
            return b''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    fd, path = tempfile.mkstemp()
    os.write(fd, get_random_string())
    os.close(fd)
    os.environ["ANSIBLE_MODULE_RUN_COMMAND"] = path


# Generated at 2022-06-13 04:55:22.725709
# Unit test for function revert_sources_list
def test_revert_sources_list():

    sources_before = {
        '/fake/aptsources': 'yes I am a fake aptsources file',
        '/fake/aptsources2': 'yes I am a fake aptsources file too'
    }
    sources_after = {
        '/fake/aptsources': 'yes I am a fake aptsources file',
        '/fake/aptsources2': 'yes I am a fake aptsources file too',
        '/fake/aptsources3': 'yes I am a fake aptsources file too and should be removed'
    }


# Generated at 2022-06-13 04:55:27.804906
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    class FakeModule:
        '''Fake module class'''
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            raise Exception(to_native(kwargs.get('msg', '')))

        def get_bin_path(self, arg):
            return None

        def run_command(self, command, *args, **kwargs):
            return 0, '', ''

        def atomic_move(self, src, dest):
            pass

        def set_mode_if_different(self, src, dest, bools):
            pass

    fake_module = FakeModule()
    apt_pkg.Config.FindFile = lambda x: '/etc/apt/sources.list'
    sl = SourcesList(fake_module)

# Generated at 2022-06-13 04:55:41.259671
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class FakeModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise AssertionError(msg)

    fake_module = FakeModule()

    sources = SourcesList(fake_module)

    sources.load('test/data/apt/sources.list')

# Generated at 2022-06-13 04:55:48.231480
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = Mock(name='module')
    add_ppa_signing_keys_callback = Mock(name='add_ppa_signing_keys_callback')
    sourcelist = UbuntuSourcesList(module, add_ppa_signing_keys_callback=add_ppa_signing_keys_callback)
    new_sourcelist = deepcopy(sourcelist)

    assert new_sourcelist.module == module
    assert new_sourcelist.add_ppa_signing_keys_callback == add_ppa_signing_keys_callback


# Generated at 2022-06-13 04:55:50.649937
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    _SourcesList___iter__(Avail)


# Generated at 2022-06-13 04:56:02.410178
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    _module = mock.MagicMock()

    _ubuntu_sources_list_1 = UbuntuSourcesList(_module)
    _ubuntu_sources_list_2 = copy.deepcopy(_ubuntu_sources_list_1)

    assert not _ubuntu_sources_list_1 == _ubuntu_sources_list_2  # the objects are different
    assert _ubuntu_sources_list_1.module == _ubuntu_sources_list_2.module
    assert _ubuntu_sources_list_1.add_ppa_signing_keys_callback == _ubuntu_sources_list_2.add_ppa_signing_keys_callback
    assert _ubuntu_sources_list_1.codename == _ubuntu_sources_list_2.codename

# Generated at 2022-06-13 04:56:15.428146
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    fake_module = type('', (), {'params': {'filename': 'dummy_filename'}})
    fake_SourcesList = type('DummySourcesList', (), {'module': fake_module, '_apt_cfg_dir': lambda self, x: None, '_apt_cfg_file': lambda self, x: None})
    sl = fake_SourcesList()
    sl.load(None)
    sl.files[None] = [(0, True, False, 'dummy1', ''), (1, True, True, 'dummy2', ''), (2, True, True, 'dummy2', ''), (3, True, True, 'dummy3', '')]
    sl.modify(None, 0, enabled=False)

# Generated at 2022-06-13 04:56:26.803444
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    sl = SourcesList()
    t = tempfile.NamedTemporaryFile(delete=False)
    sl.files[t.name] = []
    new_content = '''
deb http://httpredir.debian.org/debian jessie main
# deb-src http://httpredir.debian.org/debian jessie main
'''
    sl.files[t.name] = [(new_content.find(line), *sl._parse(line)) for line in new_content.splitlines()]
    sl._add_valid_source('deb http://httpredir.debian.org/debian jessie main', '')
    sl._add_valid_source('# deb-src http://httpredir.debian.org/debian jessie main', '')
    sl.save()

# Generated at 2022-06-13 04:59:10.778806
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    class ModuleMock(object):
        class _Params(object):
            add_ppa_signing_keys_callback = None
        params = _Params()
    moduleMock = ModuleMock()
    ubuntuSourcesList = UbuntuSourcesList(moduleMock, None)

    # test SetUp
    ubuntuSourcesList.files = {
        'any': [
            (0, True, True, 'ppa:testppa/testppa1', 'testppa'),
            (1, True, True, 'ppa:testppa/testppa2', 'testppa'),
            (2, True, True, 'ppa:testppa/testppa3', 'testppa'),
        ]
    }
    ubuntuSourcesList.remove_source('ppa:testppa/testppa1')

    # test normal case: find and remove a repository
    assert len

# Generated at 2022-06-13 04:59:21.629501
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockModule(object):
        def fail_json(self, msg):
            raise Exception(msg)

    m = MockModule()
    m.params = {'codename': 'trusty'}
    m.run_command = lambda cmd, check_rc: (0, '', '')
    m.atomic_move = lambda src, dest: None
    m.set_mode_if_different = lambda fn, mode, changed: None
    m.fail_json = lambda msg: None

    s = UbuntuSourcesList(m)

    s.add_source('ppa:test/test')

    s2 = copy.deepcopy(s)

    assert s is not s2
    assert s.module is not s2.module
    assert s.add_ppa_signing_keys_callback is not s2.add_ppa_signing_

# Generated at 2022-06-13 04:59:22.444451
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, "Test if implemented"

# Generated at 2022-06-13 04:59:26.376798
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    mod = AnsibleModule(argument_spec=dict(test=dict(required=False, default=False, type='bool')))
    sl = SourcesList(mod)
    sl.load('../../../../../library/apt_repository/tests/sources.list')
    sl.load('../../../../../library/apt_repository/tests/sources.list.d/google-chrome.list')
    for source in sl:
        pass


# Generated at 2022-06-13 04:59:38.006092
# Unit test for function main

# Generated at 2022-06-13 04:59:49.388762
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import json
    from ansible_collections.ansible.debian.plugins.module_utils import aptsources_distro
    from ansible_collections.ansible.community.plugins.module_utils._text import to_text
    from ansible_collections.ansible.community.plugins.module_utils.distribution import Distribution

    distro = Distribution()
    repo = "deb http://httpredir.debian.org/debian jessie main"
    state = "present"
    update_cache = "True"
    update_cache_retries = 5
    update_cache_retry_max_delay = 12
    distro = Distribution()
    filename = None

    tempdir = None


# Generated at 2022-06-13 04:59:56.105122
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    import StringIO
    import tempfile
    import os
    module = AnsibleModule(argument_spec={})

    sources = SourcesList(module)
    sources.files = {}
    filename = 'foo'

# Generated at 2022-06-13 05:00:07.841618
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    def test_function():
        pass
    module = AnsibleModule(argument_spec={})
    ubuntu_sources_list = UbuntuSourcesList(module, add_ppa_signing_keys_callback=test_function)
    deep_copied_ubuntu_sources_list = copy.deepcopy(ubuntu_sources_list)
    assert ubuntu_sources_list.codename == deep_copied_ubuntu_sources_list.codename
    assert ubuntu_sources_list.add_ppa_signing_keys_callback.__name__ == deep_copied_ubuntu_sources_list.add_ppa_signing_keys_callback.__name__



# Generated at 2022-06-13 05:00:18.171458
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    sourceslist = SourcesList(module)

    file_name = '/tmp/test_sources.list'
    fp = open(file_name, 'w')
    fp.write('deb http://archive.ubuntu.com/ubuntu/ xenial main\n')
    fp.write('#deb-src http://archive.ubuntu.com/ubuntu/ xenial main\n')
    fp.write('deb http://archive.ubuntu.com/ubuntu/ xenial-security main\n')
    fp.write('# deb http://archive.ubuntu.com/ubuntu xenial main\n')
    fp.close()
    sourceslist.load(file_name)

    sourceslist.modify(file_name, 2, enabled=False)

# Generated at 2022-06-13 05:00:30.371309
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={})
    file = "/tmp/sources.list"
    f = open(file, 'w')
    f.write("deb cdrom:[Ubuntu 17.10 _Artful Aardvark_ - Release amd64 (20171018)]/ artful main restricted\n")
    f.write("# deb cdrom:[Ubuntu-Server 17.10 _Artful Aardvark_ - Release amd64 (20171018)]/ artful main restricted\n")
    f.close()

    sources_list = SourcesList(module)
    sources_list.load(file)

    sources_list.modify(file, 0, enabled=True, source='deb http://archive.ubuntu.com/ubuntu/ artful main restricted', comment='# test comment')