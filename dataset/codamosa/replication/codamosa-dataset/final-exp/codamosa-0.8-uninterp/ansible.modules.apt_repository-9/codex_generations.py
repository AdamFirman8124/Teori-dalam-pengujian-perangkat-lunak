

# Generated at 2022-06-13 04:52:33.713668
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class MockedModule(object):
        def __init__(self):
            self.params = {
                'backup': False,
                'filename': None,
                'name': None,
                'origin': None,
                'state': 'present',
                'fail_key': True,
            }
        def fail_json(self, msg=''):
            raise AssertionError(msg)
        def get_bin_path(self, name):
            return None
        def run_command(self, cmd):
            return (0, '', '')
        def atomic_move(self, src, dst):
            pass
    module = MockedModule()
    sources_list = SourcesList(module)

# Generated at 2022-06-13 04:52:37.816705
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule({})
    sourceslist = SourcesList(module)
    sourceslist.load('test/test_sources.list')
    for file, n, enabled, source, comment in sourceslist:
        assert comment.strip() == 'some comment'



# Generated at 2022-06-13 04:52:49.293115
# Unit test for method dump of class SourcesList

# Generated at 2022-06-13 04:53:02.342866
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    def temp_test_file(data):
        d = tempfile.mkdtemp(prefix='ansible_test')
        fn = os.path.join(d, 'sources.list')
        f = open(fn, 'w')
        f.write(data)
        f.close()
        return fn

    class MockModule(object):
        def __init__(self):
            self.params = {}
    module = MockModule()

    # Constructor test.
    sl = SourcesList(module)
    assert sl.files == {}

    # Load test.
    fn = temp_test_file("""# This is a comment
deb http://fakeuri.example.org/ubuntu/ jaunty main restricted # Ubuntu German mirror
# Another comment
""")
    sl.load(fn)
    os.remove(fn)
   

# Generated at 2022-06-13 04:53:13.840260
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    # This test is to check if the method add_source of class UbuntuSourcesList
    # adds the valid sources to the sources list.
    class Module(object):
        def __init__(self):
            self.params = {}
            self.params['codename'] = 'trusty'

        def fail_json(self, msg):
            import sys
            sys.exit(msg)

        def atomic_move(self, tmp_path, filename):
            pass


# Generated at 2022-06-13 04:53:20.049898
# Unit test for function main
def test_main():

    import tempfile
    import shutil

    # First test of the file that does not exist
    module = AnsibleModule(argument_spec=dict(
        repo=dict(type='str', required=True),
        state=dict(type='str', default='present', choices=['absent', 'present']),
        mode=dict(type='raw'),
        update_cache=dict(type='bool', default=True, aliases=['update-cache']),
        filename=dict(type='str'),
        # This should not be needed, but exists as a failsafe
        install_python_apt=dict(type='bool', default=True),
        validate_certs=dict(type='bool', default=True),
        codename=dict(type='str'),
    ),
        supports_check_mode=True
    )


# Generated at 2022-06-13 04:53:23.884834
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={})
    sources_list = UbuntuSourcesList(module)
    assert isinstance(sources_list, UbuntuSourcesList)



# Generated at 2022-06-13 04:53:35.155608
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # prepare
    module = AnsibleModule({})
    sourceslist = SourcesList(module)

    # make sources.list with two invalid sources and one valid
    content = """
        Invalid source
        #Second invalid source
        deb http://archive.ubuntu.com/ubuntu trusty main
    """
    # save sources.list
    tmp_path = tempfile.mkdtemp()
    file = os.path.join(tmp_path, 'sources.list')
    with open(file, 'w') as f:
        f.write(content)

    # intention of test is to add one valid source in file
    sourceslist.load(file)
    for file, n, enabled, source, comment in sourceslist:
        assert file == os.path.abspath(file)
        assert enabled is True

# Generated at 2022-06-13 04:53:47.617982
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    obj = SourcesList(None)
    new_files = {
        '/etc/apt/sources.list': [
            (0, True, True, 'some', None)
        ],
        '/etc/apt/sources.list.d/0.list': [
            (0, True, True, 'some_other', None)
        ]
    }
    obj.files = new_files
    res = obj.modify('/etc/apt/sources.list', 0, source='some_new', enabled=False, comment='new_comment')

# Generated at 2022-06-13 04:54:00.928888
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class MockModule(object):
        pass

    module = MockModule()

    sourcelist = SourcesList(module)

    sourcelist.load('test/test1.list')

    # check the result

# Generated at 2022-06-13 04:54:39.804348
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule(argument_spec={})
    module.params['install_python_apt'] = False
    module.params['update_cache'] = True
    module.params['repo'] = 'ppa:nginx/stable'
    module.fail_json = MagicMock()
    install_python_apt(module, 'python-apt')
    assert module.fail_json.called
    module.fail_json.reset_mock()
    module.params['install_python_apt'] = True

    module.get_bin_path = MagicMock()
    module.get_bin_path.return_value = '/bin/true'
    module.run_command = MagicMock()
    module.run_command.return_value = 0, None, None
    install_python_apt(module, 'python-apt')
   

# Generated at 2022-06-13 04:54:42.027610
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule(argument_spec={'codename': {'required': True, 'type': 'str'}})
    sl = UbuntuSourcesList(module)
    file = sl.default_file
    f = open(file, 'r')
    f.close()
    sl.add_source('ppa:brightbox/ruby-ng')



# Generated at 2022-06-13 04:54:55.512836
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec={})
    sl = SourcesList(module)
    default_file = sl._apt_cfg_file('Dir::Etc::sourcelist')
    file1 = os.path.join(sl._apt_cfg_dir('Dir::Etc::sourceparts'), 'some.list')
    file2 = os.path.join(sl._apt_cfg_dir('Dir::Etc::sourceparts'), 'other.list')
    sl.files = {default_file: [], file1: [], file2: []}

    # check empty sources
    assert sl.dump() == {}

    # check non-empty sources

# Generated at 2022-06-13 04:54:57.523529
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    func = getattr(UbuntuSourcesList, '__deepcopy__')
    assert func



# Generated at 2022-06-13 04:55:08.072851
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    # This is a stub for testing SourcesList.load
    class apt_pkg_config(object):
        pass
    class apt_pkg_Config(object):
        pass
    try:
        apt_pkg.config.find_file("Dir::Etc::sourcelist")
    except AttributeError:
        apt_pkg.Config.FindFile("Dir::Etc::sourcelist")
    try:
        apt_pkg.config.find_dir("Dir::Etc::sourceparts")
    except AttributeError:
        apt_pkg.Config.FindDir("Dir::Etc::sourceparts")
    class os(object):
        pass
    try:
        os.path.isdir("Dir::Etc::sourceparts")
    except AttributeError:
        os.path.isdir("Dir::Etc::sourceparts")
# Unit test

# Generated at 2022-06-13 04:55:18.449289
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.debug = False
            self.check_mode = False

        def fail_json(self, **kwargs):
            raise Exception(kwargs)

        def atomic_move(self, path1, path2):
            pass

        def get_bin_path(self, name, *args, **kwargs):
            return name

        def run_command(self, cmd, *args, **kwargs):
            return (0, '', '')

    module = MockModule()

# Generated at 2022-06-13 04:55:28.654215
# Unit test for function main
def test_main():
    ansible_module = AnsibleModule(argument_spec=dict(repo=dict(type='str', required=True),state=dict(type='str', default='present', choices=['absent', 'present']),mode=dict(type='raw'),update_cache=dict(type='bool', default=True, aliases=['update-cache']),update_cache_retries=dict(type='int', default=5),update_cache_retry_max_delay=dict(type='int', default=12),filename=dict(type='str'),install_python_apt=dict(type='bool', default=True),validate_certs=dict(type='bool', default=True),codename=dict(type='str'),), supports_check_mode=True,)

# Generated at 2022-06-13 04:55:41.929901
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    # replace module checks with simple asserts
    class FakeModule:
        def _assert_file_present(self, dump):
            for file, lines in dump.items():
                if not os.path.isfile(file):
                    raise ValueError("source file %s does not exist" % (file))

        def _assert_file_absent(self, dump):
            for file, lines in dump.items():
                if os.path.isfile(file):
                    raise ValueError("source file %s exists" % (file))

        def _assert_file_contains(self, dump):
            for file, lines in dump.items():
                with open(file) as f:
                    if f.read() != lines:
                        raise ValueError("source file %s does not contain expected content" % (file))


# Generated at 2022-06-13 04:55:55.068160
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    tmppath = tempfile.mkdtemp(prefix="ansible_apt_repository_")
    print("Created temporary directory %s" % tmppath)

# Generated at 2022-06-13 04:56:01.049705
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from copy import deepcopy

    class TestModule(ArgumentSpec):
        pass

    original = UbuntuSourcesList(TestModule, add_ppa_signing_keys_callback=None)
    new = deepcopy(original)
    assert new.__dict__ == original.__dict__
    assert new.module == original.module
    assert new.add_ppa_signing_keys_callback == original.add_ppa_signing_keys_callback
    assert new.codename == original.codename


# Generated at 2022-06-13 04:57:42.465801
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    module = AnsibleModuleMock()
    sl = UbuntuSourcesList(module)
    sl.add_source('ppa:foo/bar', '')
    sl.add_source('ppa:foo/bar', '')
    sl.add_source('http://ppa.launchpad.net/foo/bar/ubuntu xenial main', '')
    sl.add_source('http://ppa.launchpad.net/foo/bar/ubuntu trusty main', '')
    sl.add_source('deb http://ppa.launchpad.net/foo/bar/ubuntu xenial main', '')

    sl.remove_source('ppa:foo/bar')
    for repo in sl:
        assert repo[3] != 'http://ppa.launchpad.net/foo/bar/ubuntu xenial main'

# Generated at 2022-06-13 04:57:52.714079
# Unit test for function main
def test_main():
    IS_WINDOWS = False
    module = MagicMock()
    module.params = {
        'state': 'present',
        'repo': 'https://www.duosecurity.com/apt/ansible/ubuntu'
    }

    with patch.dict(apt_repository.__salt__, {'config.option': MagicMock(return_value='/path/to/cache')}), patch.object(apt, 'Cache', side_effect=[ModuleNotFoundError(), apt.Cache()]), patch.dict(apt_repository.__opts__, {'cachedir': '/path/to/cache'}):
        apt_repository.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:57:58.581334
# Unit test for function main
def test_main():
    app_name = 'ansible-test'
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:58:10.424367
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    SL = SourcesList(None)

# Generated at 2022-06-13 04:58:11.975794
# Unit test for constructor of class SourcesList
def test_SourcesList():
    src_list = SourcesList()



# Generated at 2022-06-13 04:58:24.442032
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    '''
    Test for method dump of class SourcesList.
    '''
    # Prepare a temporary directory and create a test file.
    import tempfile
    tdir = tempfile.mkdtemp()
    test_file_path = os.path.join(tdir, 'test_file.list')

    with open(test_file_path, 'w') as test_file:
        test_file.write('# Test file')

    # Test if dump works correctly with the sample file.
    sl = SourcesList(None)
    sl.files = {test_file_path: []}
    result_dumpstruct = sl.dump()

    os.remove(test_file_path)
    os.rmdir(tdir)

    assert result_dumpstruct == {test_file_path: ''}



# Generated at 2022-06-13 04:58:30.705016
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    import tempfile
    import shutil

    test_data = '''
# comment
deb http://ftp.ubuntu.com/ubuntu/ precise multiverse
deb http://ftp.ubuntu.com/ubuntu/ precise restricted
# comment 2
'''

    module = AnsibleModule({})

    class SourcesListTest(SourcesList):

        def _apt_cfg_file(self, filespec):
            return '/dev/null'

        def _apt_cfg_dir(self, dirspec):
            return '/dev/null'

    slt = SourcesListTest(module)

    tmpdir = tempfile.mkdtemp()
    testfile = '%s/testfile.list' % tmpdir
    with open(testfile, 'w') as testfile_fh:
        testfile_fh.write(test_data)

    slt

# Generated at 2022-06-13 04:58:36.388265
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    file = '/etc/apt/sources.list'
    f = open(file, 'r')
    f.readline()
    f.readline()
    source = f.readline()
    f.close()
    sourceslist = SourcesList() 
    sourceslist.load(file)
    assert source in sourceslist.files


# Generated at 2022-06-13 04:58:39.216943
# Unit test for constructor of class SourcesList
def test_SourcesList():
    module = AnsibleModule({}, supports_check_mode=True)
    sl = SourcesList(module)
    module.exit_json(changed=False, ansible_facts={'sl': sl.dump()})



# Generated at 2022-06-13 04:58:48.867551
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():

    # Create test input
    input_lines = [
        "deb http://example.com stable main",
        "deb http://example.com stable main # comment 1",
        "deb http://example.com stable main # comment 2",
        "# deb http://example.com stable main # comment 3",
    ]

    # Create test output
    output_lines = [
        "deb http://example.com stable main",
        "deb http://example.com stable main # comment 1",
        "# deb http://example.com stable main # comment 2",
        "deb http://example.com stable main # comment 3",
    ]

    # Check that method modify works
    with tempfile.NamedTemporaryFile(mode="wt") as tmpf:
        # Write input to temporary file
        for line in input_lines:
            tmpf.write(line)

# Generated at 2022-06-13 05:01:10.501850
# Unit test for function install_python_apt
def test_install_python_apt():
    m = AnsibleModule(argument_spec={})
    assert m.check_mode == False
    assert m.get_bin_path('apt-get') != ''
    assert m.run_command([m.get_bin_path('apt-get'), 'update'])[0] == 0
    assert m.run_command([m.get_bin_path('apt-get'), 'install', 'python-apt', '-y', '-q'])[0] == 0



# Generated at 2022-06-13 05:01:16.184940
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
  module = AnsibleModule(argument_spec=dict(line=dict(required=True, type='str')))
  line = module.params['line']
  s = SourcesList(module)
  s.remove_source(line)
  data = s.dump()
  assert data == {'/etc/apt/sources.list': 'deb http://archive.canonical.com/ubuntu hardy partner\n'}

# Generated at 2022-06-13 05:01:17.799095
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    return UbuntuSourcesList(AnsibleModule(argument_spec=dict(codename=dict(type='str'))))

# Begin module execution

# Generated at 2022-06-13 05:01:20.382996
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec=dict())
    sources = SourcesList(module)
    assert sources.dump() == {}
    sources.load(__file__)
    assert sources.dump() != {}

# Generated at 2022-06-13 05:01:26.117169
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    # Test params
    file = "test_filename"
    # Test data
    line = "deb http://archive.canonical.com/ubuntu hardy partner"
    comment = "This is comment"
    file = "test_filename"
    # Test code
    """
    # Test code
    if __name__ == '__main__':
        sources_list = SourcesList(file)
        sources_list.add_source(line, comment, file)
        print(sources_list.dump())
    """
    sources_list = SourcesList(file)
    sources_list.add_source(line, comment, file)
    print(sources_list[file])
    print(sources_list.dump())
    # Test output
    print(sources_list)
    #assert sources_list == True

# Unit test

# Generated at 2022-06-13 05:01:30.542121
# Unit test for function main
def test_main():
    # This test is only valid when run in the same process
    # These environment variables are only available when running in Ansible
    if 'ANSIBLE_MODULE_ARGS' in os.environ:
        content = ('deb http://security.debian.org/ jessie/updates main non-free contrib\n'
                   'deb http://security.debian.org/ jessie/updates main\n'
                   'deb-src http://security.debian.org/ jessie/updates main')
        test_sourceslist = SourcesList('/etc/apt/sources.list', content)
        assert test_sourceslist.list[0].uri == 'http://security.debian.org/'
        assert test_sourceslist.list[0].dist == 'jessie/updates'

# Generated at 2022-06-13 05:01:31.297112
# Unit test for constructor of class SourcesList
def test_SourcesList():
    m = AnsibleModule({})
    SourcesList(m)



# Generated at 2022-06-13 05:01:32.997268
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = FakeModule()
    helper = SourcesList(module)
    helper.load('foo.list')
    helper.load('bar.list')
    # File not found.
    helper.load('foobar.list')


# Generated at 2022-06-13 05:01:33.558781
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    raise NotImplementedError()



# Generated at 2022-06-13 05:01:38.621540
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = AnsibleModule({}, check_invalid_arguments=False)
    source_list = SourcesList(module)

    # test removing source from source list
    source_list.files['/etc/apt/sources.list'] = [
        (0, True, False, '', ''),
        (1, True, True, 'deb http://example.com stretch main', ''),
        (2, True, True, 'deb http://example.org stretch main', ''),
        (3, True, True, 'deb http://example.com stretch contrib', ''),
        (4, True, True, 'deb http://example.org stretch contrib', ''),
        (5, True, True, 'deb http://example.org stretch contrib', '# this is a comment'),
    ]
