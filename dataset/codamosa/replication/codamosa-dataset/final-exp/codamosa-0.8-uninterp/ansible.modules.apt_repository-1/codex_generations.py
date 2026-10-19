

# Generated at 2022-06-13 04:52:32.589626
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({'name': 'apt-repository-modify'}, supports_check_mode=True)
    sources_list = SourcesList(module)

    sources_list.files = {
        '/test/test-file': [
            (0, True, True, 'deb http://ubuntu test/main amd64', ''),
            (1, True, False, 'deb http://ubuntu test/main amd64', ''),
            (2, True, True, 'deb-src http://ubuntu test/main amd64', ''),
            (3, True, False, 'deb-src http://ubuntu test/main amd64', ''),
            (4, False, False, 'deb http://ubuntu test/main amd64', ''),
        ],
    }

    # enable valid source

# Generated at 2022-06-13 04:52:41.345692
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves.urllib.error import HTTPError

    class MockFetchUrl(object):
        def __init__(self, expected_url, expected_request_headers, expected_return_status, expected_return_body):
            self.expected_url = expected_url
            self.expected_request_headers = expected_request_headers
            self.expected_return_status = expected_return_status
            self.expected_return_body = expected_return_body

        def __call__(self, module, url, headers=None):
            return_body = self.expected_return_body
            return_status = self.expected_return_status


# Generated at 2022-06-13 04:52:54.751577
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    from ansible.module_utils.basic import AnsibleModule

    # Setup AnsibleModule
    module = AnsibleModule(
        argument_spec={'a': {'type': 'int', 'required': True}},
        supports_check_mode=True
    )

    sources_list = UbuntuSourcesList(module)

    # Test attributes of class SourcesList
    assert sources_list.module == module
    assert os.path.abspath(sources_list.default_file) == '/etc/apt/sources.list'

    # Test attributes of class UbuntuSourcesList
    assert sources_list.codename == distro.codename
    assert sources_list.add_ppa_signing_keys_callback is None
    assert isinstance(sources_list.files, dict) is True     # Can't compare to an empty dict because it is filled

# Generated at 2022-06-13 04:52:59.909570
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule('apt_repository', 'msg', 'state')
    for env_name in ('APT_PACKAGE_CACHE', 'APT_STATE_DIR'):
        module.run_command(['mkdir', '-p', os.path.join(tempfile.gettempdir(), env_name)])
        os.environ[env_name] = os.path.join(tempfile.gettempdir(), env_name)

    # no error if check_mode is false and apt-get command is found
    install_python_apt(module, 'python-apt')



# Generated at 2022-06-13 04:53:03.209308
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = AnsibleModule(argument_spec={})
    interface = UbuntuSourcesList(module)


SourcesList = UbuntuSourcesList



# Generated at 2022-06-13 04:53:14.800505
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    """
    Testing if sources are completely removed.
    """
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+t') as f:
        f.write('# deb file:/foo bar main\n')
        f.write('deb file:/foo bar restricted\n')
        f.write('deb file:/foo bar main\n')
        f.write('# deb file:/foo bar main\n')
        f.write('# deb file:/foo bar main\n')
        f.write('# deb file:/foo bar main\n')
        f.write('# deb file:/foo bar main\n')
        f.flush()

        s = SourcesList(f.name)
        print("Remove 'deb file:/foo bar main' from file.")
        s.remove_source('deb file:/foo bar main')


# Generated at 2022-06-13 04:53:19.410652
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = AnsibleModule(argument_spec={})
    object = UbuntuSourcesList(module)
    new_object = copy.deepcopy(object)
    assert new_object == object
    assert new_object is not object
    assert isinstance(new_object, UbuntuSourcesList)
    assert isinstance(object, UbuntuSourcesList)


# Generated at 2022-06-13 04:53:30.797795
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule({})
    sl = SourcesList(module)
    sl.load('tests/sources.list')
    assert sl.dump() == {'tests/sources.list': '[valid-url] deb http://www.example.com/ubuntu distro component1 component2\n[disabled] # deb http://www.example.com/ubuntu distro component1 component2\n# deb http://www.example.com/ubuntu distro component1 component2\ndeb [arch=amd64] http://www.example.com/ubuntu distro component1 component2\n[invalid] deb http://www.example.com/ubuntu distro component1 component2\n'}


# Generated at 2022-06-13 04:53:41.230365
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    tmp_dir = tempfile.mkdtemp()
    test_file = os.path.join(tmp_dir, "testfile")
    print("Created dir ", tmp_dir)
    print("Created file ", test_file)
    f = open(test_file, "w")
    f.write("deb http://archive.canonical.com/ubuntu hardy partner\n")
    f.write("# deb-src http://archive.canonical.com/ubuntu hardy partner\n")
    f.write("deb http://archive.canonical.com/ubuntu hardy partner\n")
    f.close()
    print("Wrote entries to file")

    test_self = SourcesList(AnsibleModule)
    print("Created instance of SourcesList")
    test_self.load(test_file)

# Generated at 2022-06-13 04:53:42.842438
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    pass


# Generated at 2022-06-13 04:54:18.644523
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    lines = [
        'deb http://archive.ubuntu.com/ubuntu trusty main',
        'deb http://archive.ubuntu.com/ubuntu trusty multiverse',
        'deb http://archive.ubuntu.com/ubuntu trusty restricted',
        '# deb http://archive.ubuntu.com/ubuntu trusty main',
        '# deb http://archive.ubuntu.com/ubuntu trusty multiverse',
        '# deb http://archive.ubuntu.com/ubuntu trusty restricted'
    ]

# Generated at 2022-06-13 04:54:26.082256
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    data = {
        "Codename": "trusty",
        "Description": "Ubuntu 14.04 LTS",
        "ID": "ubuntu",
        "Release": "14.04",
        "Version": "14.04"
    }
    distro = Distro(data['ID'], data['Codename'], data['Description'], data['Version'], data['Release'])
    module = AnsibleModule(argument_spec={})
    sources_list = UbuntuSourcesList(module)
    sources_list.codename = distro.codename

    def run_command(*args, **kwargs):
        return (), {}, {'status': 200}

    sources_list.module.run_command = run_command
    sources_list.add_source("ppa:ansible/ansible")

# Generated at 2022-06-13 04:54:31.513239
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule({})
    module.exit_json = exit_json
    sources = SourcesList(module)
    test_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    path = os.path.abspath(test_file.name)
    test_file.write('# Comment 1\n')
    test_file.write('# Comment 2\n')
    test_file.write('deb http://other domain.com/mirror trusty main\n')
    test_file.write('# Comment 3\n')
    test_file.write('deb http://some domain.com/mirror trusty main\n')
    test_file.write('# Comment 4\n')
    test_file.write('deb-src http://some domain.com/mirror trusty main\n')

# Generated at 2022-06-13 04:54:40.269562
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    # UbuntuSourcesList.remove_source should remove any existing source that matches the source given, even if it is disabled.
    # Example:
    #      When UbuntuSourcesList(module=module) as sources:
    #         sources.remove_source('deb http://ppa.launchpad.net/foo/bar/ubuntu precise main')

    module = AnsibleModule({})
    ppa_url = 'deb http://ppa.launchpad.net/foo/bar/ubuntu precise main'

# Generated at 2022-06-13 04:54:43.530169
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible.module_utils.debops.apt_repo import UbuntuSourcesList

    class FakeModule:
        params = { 'codename': 'fake_codename' }

    ppa_callback = None

    ubuntu_sources_list = UbuntuSourcesList(FakeModule(), add_ppa_signing_keys_callback=ppa_callback)
    ubuntu_sources_list_copy = copy.deepcopy(ubuntu_sources_list)
    assert ubuntu_sources_list != ubuntu_sources_list_copy


# Generated at 2022-06-13 04:54:56.607585
# Unit test for function install_python_apt
def test_install_python_apt():
    if not PY3:
        if HAVE_PYTHON_APT:
            import apt
            import apt_pkg
            import aptsources.distro as aptsources_distro

            distro = aptsources_distro.get_distro()

            path = '/tmp/test_install_python_apt_test'
            apt_pkg_name = 'python-apt'
            module = AnsibleModule({'auto_install_python_apt': True})

            if os.path.exists(path):
                os.remove(path)

            # Reload the libraries after installation
            reload_module(apt)
            reload_module(apt_pkg)
            reload_module(aptsources_distro)

            assert HAVE_PYTHON_APT is True, "install_python_apt() installed %s" % apt

# Generated at 2022-06-13 04:55:06.525274
# Unit test for function install_python_apt
def test_install_python_apt():
    sys.modules['apt'] = None
    sys.modules['apt_pkg'] = None
    sys.modules['aptsources.distro'] = None
    module = AnsibleModule({}, supports_check_mode=True)
    install_python_apt(module, 'python-apt')
    assert sys.modules.get('apt') is not None
    assert sys.modules.get('apt_pkg') is not None
    assert sys.modules.get('aptsources.distro') is not None
    del sys.modules['apt']
    del sys.modules['apt_pkg']
    del sys.modules['aptsources.distro']



# Generated at 2022-06-13 04:55:14.195042
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    # let's create mock module
    module = AnsibleModule(argument_spec={})
    # and create fixture for SourcesList
    sl = SourcesList(module)

    fd, tmp_path = tempfile.mkstemp(prefix=".test-")
    os.write(fd, b"""\
deb http://archive.canonical.com/ubuntu hardy partner
# deb-src http://archive.canonical.com/ubuntu hardy partner

deb http://archive.canonical.com/ubuntu hardy partner
# deb-src http://archive.canonical.com/ubuntu hardy partner

""")
    os.close(fd)

    sl.load(tmp_path)

    assert len(sl.files[tmp_path]) == 3

# Generated at 2022-06-13 04:55:17.255598
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    SL = SourcesList(None)
    SL.load('test/sources.list')
    SL.remove_source('deb http://archive.canonical.com/ubuntu trusty partner')
    SL.save()


# Generated at 2022-06-13 04:55:22.575390
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    import mock
    md = mock.MagicMock()
    md._name = 'module'
    md.check_mode = False
    cb = get_add_ppa_signing_key_callback(md)
    cb(['command'])



# Generated at 2022-06-13 04:56:46.569562
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    def test_SourcesList_remove_source_setup(module):

        sourceslist = SourcesList(module)
        sourceslist.files = {}
        sourceslist.new_repos = set()
        sourceslist.default_file = '/etc/apt/sources.list'

        sourceslist.load(sourceslist.default_file)

        # read sources.list.d
        for file in glob.iglob('%s/*.list' % sourceslist._apt_cfg_dir('Dir::Etc::sourceparts')):
            sourceslist.load(file)

        return sourceslist

    module = {}
    module['run_command'] = lambda *args, **kwargs: (0, '', '')
    module['set_mode_if_different'] = lambda *args, **kwargs: None

# Generated at 2022-06-13 04:56:49.039846
# Unit test for function revert_sources_list
def test_revert_sources_list():
    # Nothing to test here since the file operations make it non-testable
    pass



# Generated at 2022-06-13 04:56:58.340118
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    import os
    import tempfile
    import shutil


# Generated at 2022-06-13 04:57:09.088113
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    sl = SourcesList('')
    for line, fl in [
        (
            'deb http://archive.ubuntu.com/ubuntu/ xenial main multiverse restricted universe',
            "ubuntu.list"
        ),
        (
            'deb http://archive.ubuntu.com/ubuntu/ xenial-updates main multiverse restricted universe',
            "ubuntu.list"
        ),
        (
            'deb http://archive.ubuntu.com/ubuntu/ xenial universe',
            "ubuntu.list"
        ),
        (
            'deb http://archive.ubuntu.com/ubuntu/ xenial universe',
            "ubuntu.list"
        )
    ]:
        sl._add_valid_source(line, "", fl)
    assert len(sl.files['/etc/apt/sources.list.d/ubuntu.list']) == 3

# Generated at 2022-06-13 04:57:19.597682
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockedModule(object):
        params = {'codename': 'dummy_codename'}

    mocked_module = MockedModule()
    mocked_module.run_command = lambda *args, **kwargs: (0, '', '')
    mocked_module.atomic_move = lambda *args, **kwargs: None
    mocked_module.set_mode_if_different = lambda *args, **kwargs: None
    mocked_module.fail_json = lambda *args, **kwargs: None

    mocked_sources_list = UbuntuSourcesList(mocked_module)
    mocked_sources_list.files = {'dummy_filename': []}
    mocked_sources_list.add_ppa_signing_keys_callback = lambda *args: None

    assert mocked_sources_list is not mocked_sources

# Generated at 2022-06-13 04:57:24.254071
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule(argument_spec={'install_python_apt': {'type': 'bool'}})
    rval = install_python_apt(module, 'python3-apt')
    assert not rval



# Generated at 2022-06-13 04:57:36.155512
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class FakeModule(object):  # pylint: disable=too-few-public-methods
        class FakeParams(object):  # pylint: disable=too-few-public-methods
            codename = 'precise'

        def __init__(self):
            self.params = self.FakeParams()

        def run_command(self, command, check_rc=False):
            return 0, '', ''

        def fail_json(self, msg):
            print(msg)

    sl = UbuntuSourcesList(FakeModule())
    assert 0 == len(sl.files)
    sl.add_source('deb http://ppa.launchpad.net/myppa/ppa/ubuntu precise main')
    assert 1 == len(sl.files)

# Generated at 2022-06-13 04:57:38.283799
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    assert type(SourcesList(None).dump()) == dict



# Generated at 2022-06-13 04:57:48.570330
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    import tempfile
    lines = ['# deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse\n', '# deb [arch=amd64] http://www.ubnt.com/downloads/unifi/debian stable ubiquiti\n']
    f = tempfile.NamedTemporaryFile(mode='w+')
    f.writelines(lines)
    f.flush()
    sourceslist = SourcesList(f.name)

# Generated at 2022-06-13 04:57:49.121317
# Unit test for function install_python_apt
def test_install_python_apt():
    pass



# Generated at 2022-06-13 04:59:48.351109
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule(argument_spec=dict(
        apt_pkg_name = dict(default="python-apt"),
        state = dict(default="present")
    ))
    apt_pkg_name = module.params["apt_pkg_name"]
    install_python_apt(module, apt_pkg_name)
# end test function install_python_apt



# Generated at 2022-06-13 04:59:55.469618
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(AnsibleModule):
        def __init__(self):
            self._ansible_module = None

        def __getattr__(self, name):
            return getattr(self._ansible_module, name)

    test_module = TestModule()
    test_module._ansible_module = AnsibleModule(argument_spec={})

    repos = UbuntuSourcesList(test_module)
    repos2 = deepcopy(repos)
    assert repos is not repos2
    assert repos.module is repos2.module
    assert repos.add_ppa_signing_keys_callback is repos2.add_ppa_signing_keys_callback
    assert repos.codename == repos2.codename



# Generated at 2022-06-13 05:00:07.688023
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    source_list = SourcesList(None)

# Generated at 2022-06-13 05:00:14.116275
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    sl = SourcesList(module)
    # No files, no error
    sources = [s for s in sl]
    assert len(sources) == 0

    # Empty sources.list
    fd, tmp = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.close()
    sl.load(tmp)
    os.unlink(tmp)
    sources = [s for s in sl]
    assert len(sources) == 0

    # Valid source
    fd, tmp = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write("deb http://archive.ubuntu.com/ubuntu trusty main\n")
    f.close()
    sl.load(tmp)
    os.un

# Generated at 2022-06-13 05:00:16.714194
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    pass
# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 05:00:29.547053
# Unit test for function revert_sources_list
def test_revert_sources_list():
    sources_before = {
        '/etc/apt/sources.list': 'deb http://example.com/ubuntu xenial main',
        '/etc/apt/sources.list.d/ansible-repo.list': 'deb http://example.com/ansible xenial main'
    }
    sources_after = {
        '/etc/apt/sources.list': 'deb http://example.com/ubuntu xenial main',
        '/etc/apt/sources.list.d/ansible-repo1.list': 'deb http://example.com/ansible xenial main',
        '/etc/apt/sources.list.d/ansible-repo2.list': 'deb http://example.com/ansible xenial main'
    }
    sourceslist_before = SourcesList()


# Generated at 2022-06-13 05:00:40.651135
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            codename=dict(default=None, required=False),
        ),
        supports_check_mode=True,
    )
    obj = UbuntuSourcesList(module)
    for source in obj:
        assert isinstance(source, tuple)
        assert isinstance(source[0], str)
        assert isinstance(source[1], int)
        assert isinstance(source[2], bool)
        assert isinstance(source[3], str)
        assert isinstance(source[4], str)


# Generated at 2022-06-13 05:00:50.519020
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    '''
    Test:
    # Check that the function returns None if in check mode

    @mock.patch('ansible.module_utils.basic.AnsibleModule.check_mode')
    def test_get_add_ppa_signing_key_callback_check_mode(self, mock_check_mode):
        '''

# Generated at 2022-06-13 05:00:56.291883
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    for line in ('ppa:name/ppa-what', 'deb http://ppa.launchpad.net/name/ppa-what/ubuntu focal main', 'deb http://ppa.launchpad.net/name/ppa-what/ubuntu bionic main'):
        with tempfile.TemporaryFile() as f:
            f.write('deb http://example.com/ubuntu bionic main\n'.encode('utf-8'))
            f.write('deb http://example.com/ubuntu focal main\n'.encode('utf-8'))
            f.write('# ' + line + '\n'.encode('utf-8'))
            f.write(line.encode('utf-8'))
            f.seek(0)
            m = module_mock.ModuleMock()
            sl = UbuntuSourcesList(m)

# Generated at 2022-06-13 05:00:59.047098
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={
        'codename': dict(type='str', default=''),
    })

    obj = UbuntuSourcesList(module)

    assert obj.codename == ''

    module = AnsibleModule(argument_spec={
        'codename': dict(type='str', default='trusty'),
    })

    obj = UbuntuSourcesList(module)

    assert obj.codename == 'trusty'
