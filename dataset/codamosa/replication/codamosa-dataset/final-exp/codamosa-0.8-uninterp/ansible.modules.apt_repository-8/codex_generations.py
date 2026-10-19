

# Generated at 2022-06-13 04:52:43.913888
# Unit test for function main

# Generated at 2022-06-13 04:52:51.713480
# Unit test for function main

# Generated at 2022-06-13 04:53:04.644023
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={})
    sl = SourcesList(module)
    sl.load('/tmp/testfile')
    enabled = None
    source = 'deb http://archive.ubuntu.com/ubuntu trusty main'
    comment = '# Ubuntu'
    for filename, n, enabled_old, source_old, comment_old in sl:
        sl.modify(filename, n, enabled=enabled, source=source, comment=comment)
    assert sl.files['/tmp/testfile'][0][1] == True
    assert sl.files['/tmp/testfile'][0][2] == enabled
    assert sl.files['/tmp/testfile'][0][3] == source
    assert sl.files['/tmp/testfile'][0][4] == comment


# Generated at 2022-06-13 04:53:16.104348
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, msg):
            raise AssertionError(msg)

        def atomic_move(self, tmp_path, filename):
            pass


# Generated at 2022-06-13 04:53:20.212481
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    sl = SourcesList()
    sl.load('/etc/apt/sources.list.d/git-core-ubuntu-ppa-xenial.list')
    assert sl.files['/etc/apt/sources.list.d/git-core-ubuntu-ppa-xenial.list'][0][3] == 'deb http://ppa.launchpad.net/git-core/ppa/ubuntu xenial main'

if __name__ == '__main__':
    test_SourcesList_load()


# Generated at 2022-06-13 04:53:32.799390
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    ubuntu_sources_list = UbuntuSourcesList(None)

# Generated at 2022-06-13 04:53:36.948517
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = AnsibleModule(argument_spec={})
    sources_list = SourcesList(module)
    assert sources_list.default_file == '/etc/apt/sources.list'



# Generated at 2022-06-13 04:53:47.988238
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible.module_utils.six import PY2
    if not PY2:
        # Python 3 has no __deepcopy__ method
        return True

    class MockModule(object):
        def __init__(self):
            self.params = dict()
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            self.fail_json_called = True

    class MockDistro(object):
        def __init__(self):
            self.codename = 'fooname'

    class MockAddPpaSigningKeysCallback(object):
        def __call__(self, *args, **kwargs):
            pass

    module = MockModule()
    distro = MockDistro()
    add_ppa_signing_

# Generated at 2022-06-13 04:53:56.107046
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    example = UbuntuSourcesList(None)
    mycopy = copy.deepcopy(example)
    ans = isinstance(mycopy, UbuntuSourcesList)
    assert ans == True


### Linux Distribution specific implementations ###

# All classes have to have:
# 1. Each of them has to be a subclass of RepoManager
# 2. distro_name class attribute
# 3. get_managers() method
# 4. has_manager_for() method


# Generated at 2022-06-13 04:54:05.937657
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    test_sources_list = '/tmp/ansible_test_source_list_dump'
    test_sources_list_generated = '/tmp/ansible_test_source_list_dump_generated'

    test_content = """
# deb cdrom:[Ubuntu-Server 16.04.2 LTS _Xenial Xerus_ - Release amd64 (20170215.2)]/ xenial main restricted
deb http://security.ubuntu.com/ubuntu xenial-security main restricted
deb http://archive.ubuntu.com/ubuntu xenial main restricted
# deb-src http://archive.ubuntu.com/ubuntu xenial main restricted
# deb-src http://archive.ubuntu.com/ubuntu xenial main
# commented out
"""
    f = open(test_sources_list, 'w')
    f.write(test_content)

# Generated at 2022-06-13 04:54:40.900607
# Unit test for method save of class SourcesList
def test_SourcesList_save():

    test_file = 'test/test_SourcesList_save.list'
    test_dir = 'test/test_SourcesList_save.d'
    test_file2 = os.path.join(test_dir, 'test_SourcesList_save2.list')

    clsname = 'AnsibleModule'
    if PY3:
        clsname = 'AnsibleModule3'
    module = type(clsname, (object,), dict(exit_json=lambda *a, **k: None, fail_json=lambda *a, **k: None, atomic_move=lambda *a, **k: None, set_mode_if_different=lambda *a, **k: None))()

    sources = SourcesList(module)
    assert not os.path.exists(test_file)

    # test with empty list

# Generated at 2022-06-13 04:54:45.325220
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    # Make and load sources list
    sl = UbuntuSourcesList(None)
    sl.load(os.path.abspath(os.path.join(os.path.dirname(__file__), 'sample-sources.list')))

    # Test repositories urls
    repos_urls = sl.repos_urls
    assert 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main' in repos_urls
    assert 'deb http://download.virtualbox.org/virtualbox/debian bionic contrib' in repos_urls
    assert 'deb http://download.virtualbox.org/virtualbox/debian bionic contrib' in repos_urls
    assert 'deb http://deb.debian.org/debian buster main' not in repos_urls

# Generated at 2022-06-13 04:54:46.999857
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, 'This test needs to be implemented!'



# Generated at 2022-06-13 04:55:00.332909
# Unit test for method dump of class SourcesList

# Generated at 2022-06-13 04:55:01.147978
# Unit test for function install_python_apt
def test_install_python_apt():
    pass


# Generated at 2022-06-13 04:55:11.548777
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    from ansible.module_utils.six import StringIO
    from contextlib import contextmanager

    filename = 'test_SourcesList_save.list'
    tmp_path = filename + '.tmp'
    content = '''# comment here for a complete line
deb http://deb.example.com/ /
deb http://deb.example.com/ stable main
deb http://deb.example.com/ stable main restricted
deb http://deb.example.com/ stable main restricted # a comment
# deb http://deb.example.com/ stable main restricted
'''

    class FakeModule:
        def __init__(self, params):
            self.params = params

        def check_mode(self):
            return self.params['check_mode']


# Generated at 2022-06-13 04:55:17.212048
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    mock_module = MagicMock(
        check_mode=False,
        run_command="called"
    )
    callback = get_add_ppa_signing_key_callback(mock_module)
    callback("check")
    assert mock_module.run_command.called
# end unit test



# Generated at 2022-06-13 04:55:24.358463
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    m = MockAnsibleModule('apt_repository')
    sl = SourcesList(m)
    sl.load('tests/sources.list')
    sl.load('tests/sources.list.d/google-chrome.list')

    assert list(sl)[0] == ('tests/sources.list.d/google-chrome.list', 0, True, 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main', '')
    assert list(sl)[1] == ('tests/sources.list.d/google-chrome.list', 1, True, 'deb-src http://dl.google.com/linux/chrome/deb/ stable main', '')

# Generated at 2022-06-13 04:55:32.772970
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module_mock = AnsibleModuleMock(name='apt', params={})
    sources_list = UbuntuSourcesList(module_mock)
    sources_list.add_source('ppa:deadsnakes/ppa')
    expected_result = {
        '/etc/apt/sources.list.d/deadsnakes_ppa.list':
            'deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu xenial main\n'
    }
    assert sources_list.dump() == expected_result

# Generated at 2022-06-13 04:55:43.756486
# Unit test for function revert_sources_list
def test_revert_sources_list():
    class FakeModule(object):
        def fail_json(self, msg):
            raise Exception(msg)
    module = FakeModule()
    sources_before = {
        '/etc/apt/sources.list.d/foo.list': 'deb http://example.com/ wheezy main\n',
    }
    sources_after = {
        '/etc/apt/sources.list.d/foo.list': 'deb http://example.com/ wheezy main\n',
    }
    sourceslist_before = SourcesList(module)
    sourceslist_before.files = sources_before
    try:
        revert_sources_list(sources_before, sources_after, sourceslist_before)
    except Exception:
        # Expected that no exception will be raise by the function
        assert False



# Generated at 2022-06-13 04:56:56.124622
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # Prepare test data
    test_data = {
        'default_file': '/etc/apt/sources.list',
        'files': {
            '/etc/apt/sources.list': [
                (0, True, True, 'deb http://some-url.com stable', ''),
                (1, False, False, 'deb http://disabled-some-url.com stable', ''),
                (2, True, True, 'deb http://another-some-url.com stable', ''),
                (3, False, False, 'deb http://disabled-another-some-url.com stable', ''),
            ]
        }
    }

# Generated at 2022-06-13 04:57:00.699344
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from copy import deepcopy
    ubuntu_sources_list = UbuntuSourcesList(module=None)
    new_ubuntu_sources_list = deepcopy(ubuntu_sources_list)
    old_repositories = ubuntu_sources_list.repos_urls
    new_repositories = new_ubuntu_sources_list.repos_urls
    assert len(old_repositories) == len(new_repositories)



# Generated at 2022-06-13 04:57:07.361083
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    # use a custom config file for all tests
    os.environ['APT_CONFIG'] = "/tmp/apt_test/apt.conf"
    modmock = AnsibleModule(argument_spec={})
    listmock = SourcesList(modmock)
    # create test data
    listmock.files["test1.list"] = [(0, True, False, "deb http://some.url/some.repo some.release main", "comment1"), (1, True, True, "deb http://some.url/some.repo some.release main", "comment2")]

# Generated at 2022-06-13 04:57:14.184171
# Unit test for method load of class SourcesList
def test_SourcesList_load():

    # Read the sources
    sources_list = SourcesList(None)

    # Get the path to the sources.list file
    sources_file = sources_list._apt_cfg_file('Dir::Etc::sourcelist')

    # Assert file is there
    assert os.path.isfile(sources_file)

    # Read the contents of the file
    f = open(sources_file, 'r')
    sources = []
    for line in f:
        sources.append(line.strip())

    # Call load
    sources_list.load(sources_file)

    # Compare
    for source in sources:
        assert source in [s[3] for s in sources_list.files[sources_file]]


# Generated at 2022-06-13 04:57:15.557545
# Unit test for function revert_sources_list
def test_revert_sources_list():
    assert False, "No test for revert_sources_list"

# Generated at 2022-06-13 04:57:24.396069
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})

    class FakeFile(object):
        def __init__(self, lines):
            self.lines = lines
            self.pos = 0

        def readline(self):
            self.pos += 1
            if self.pos <= len(self.lines):
                return self.lines[self.pos - 1]
            else:
                return ''

        def close(self):
            pass

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

        def _expand_path(self, filename):
            return filename

        def _apt_cfg_file(self, filespec):
            return ''

        def _apt_cfg_dir(self, dirspec):
            return ''


# Generated at 2022-06-13 04:57:25.124983
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    pass



# Generated at 2022-06-13 04:57:36.804686
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    sl = SourcesList('', {})
    sl.files = {'/etc/apt/sources.list': [
        (0, True, True, 'deb http://archive.ubuntu.com/ubuntu xenial main universe', '')
    ]}
    sl.new_repos = set()
    sl._add_valid_source('deb http://archive.ubuntu.com/ubuntu xenial main universe', '', '/etc/apt/sources.list')
    # This call shouldn't actually add duplicates.
    assert set(sl.files) == {'/etc/apt/sources.list'}
    assert len(sl.files['/etc/apt/sources.list']) == 1

# Generated at 2022-06-13 04:57:47.714383
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    import doctest
    import ansible.modules.packaging.os.apt_repository
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    class TestModule(AnsibleModule):
        def fail_json(self, *a, **kw):
            self.exit_args = kw
            self.exit_args['failed'] = True
            self.exit_args['msg'] = a[0]
            raise SystemExit()

        def atomic_move(self, _a, _b):
            pass

# sample sources.list

# Generated at 2022-06-13 04:57:55.814493
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # Create a mock module
    module = AnsibleModule(argument_spec={})

    # Create a mock apt_pkg module
    apt_pkg = sys.modules['ansible.module_utils.basic.apt_pkg']
    apt_pkg.config.find_dir.return_value = '/'
    # Iterate over our instance
    sources_list = SourcesList(module)
    iterator = iter(sources_list)
    assert isinstance(iterator, object)