

# Generated at 2022-06-13 04:52:43.418982
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    # Test when sources.list is empty
    m = AnsibleModule({}, supports_check_mode=True)
    s = SourcesList(m)
    dumpstruct = s.dump()
    assert dumpstruct == {}
    m.fail_json.assert_called_with(msg='Source does not exist.')

    # Test when sources.list is not empty
    m = AnsibleModule({}, supports_check_mode=True)
    s = SourcesList(m)
    s.add_source('deb http://archive.ubuntu.com/ubuntu/ bionic main restricted', '# line 1')
    dumpstruct = s.dump()
    lines = dumpstruct['/etc/apt/sources.list'].split('\n')
    assert 'deb http://archive.ubuntu.com/ubuntu/ bionic main restricted' in lines

# Generated at 2022-06-13 04:52:51.257079
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os import virt
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3


# Generated at 2022-06-13 04:53:04.238326
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    class Module(object):
        def fail_json(self, **kwargs):
            raise AssertionError(kwargs['msg'])
        @staticmethod
        def get_bin_path(binary):
            return ''
        class params_dict(object):
            pass
    module = Module()
    print("Testing SourcesList.remove_source")
    sl = SourcesList(module)
    print("Testing SourcesList.remove_source invalid source")
    fd, tmp_path = tempfile.mkstemp()
    test_file = os.fdopen(fd, 'w')
    test_file.write("file with invalid sources\n")
    test_file.write("invalid source\n")
    test_file.close()
    sl.load(tmp_path)

# Generated at 2022-06-13 04:53:15.733794
# Unit test for function install_python_apt
def test_install_python_apt():
    class Module(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = True
            self.run_command_rc = 0
            self.run_command_output = (0, 'ok', '')
            self.fail_json_msg = None
            self.changed = False

        def get_bin_path(self, path):
            return ''
        def run_command(self, command, tmpdir=None):
            if path in ['/usr/bin/apt-get', 'apt-get']:
                return self.run_command_rc, self.run_command_output
            raise ValueError
        def fail_json(self, msg):
            self.fail_json_msg = msg


# Generated at 2022-06-13 04:53:21.737255
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.dict_transformations import recursive_diff

    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()
    module.fail_json = MagicMock(side_effect=lambda x: True)
    usl = UbuntuSourcesList(
        module,
        lambda command: None
    )

    class FakeModify:
        def __init__(self, usl):
            self.usl = usl

        def add_source(self, line, comment='', file=None):
            self.usl.add_source(line, comment, file)

    fake_modify = FakeModify(usl)
    usl.modify = MagicMock()

# Generated at 2022-06-13 04:53:32.400963
# Unit test for function revert_sources_list
def test_revert_sources_list():
    """Hit revert_sources_list() with some fake SourcesList data
    to ensure it survives."""

    class FakeModule():
        params = {}

        def fail_json(self, **kwargs):
            # No fail_json() in check mode.
            pass

        def atomic_move(self, source, dest):
            os.rename(source, dest)

        def set_mode_if_different(self, path, mode, changed):
            pass


    class FakeSource(dict):
        # Pretend to be a dictionary of sources (incl. comments) with
        # filename as key.
        def __getitem__(self, key):
            # If not found send back an empty list
            return self.get(key, [])

        def keys(self):
            return self.keys


# Generated at 2022-06-13 04:53:36.205671
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    range1 = range(4)
    new_obj = SourcesList(range1)
    new_obj.add_source(1, 2)
    assert '1' == new_obj.add_source(1, 2)


# Generated at 2022-06-13 04:53:42.131291
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    class TestModule:
        params = {'codename': 'trusty'}

        def fail_json(self, msg):
            raise RuntimeError(msg)

    ls = UbuntuSourcesList(TestModule())
    ls.add_source('ppa:ansible/ansible')
    ls.add_source('deb http://mirror.example.com/mirror trusty main')
    ls.remove_source('ppa:ansible/ansible')
    ls.remove_source('deb http://mirror.example.com/mirror trusty main')

    assert len(ls.files) == 0
    try:
        ls.remove_source('invalid')
    except InvalidSource as e:
        assert to_native(e) == 'invalid'
    else:
        assert False, 'InvalidSource was not raised'

# Generated at 2022-06-13 04:53:42.826292
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, 'Test not implemented'


# Generated at 2022-06-13 04:53:50.647494
# Unit test for function main

# Generated at 2022-06-13 04:54:28.979117
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    sl = SourcesList(AnsibleModule({}))
    sl.files = {'foo' : [(0, True, True, 't', 'c')]}
    sl.modify('foo', 0, enabled=True, source='new source', comment='new comment')
    assert sl.files == {'foo': [(0, True, True, 'new source', 'new comment')]}

# Generated at 2022-06-13 04:54:36.877649
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    # Initialization of UbuntuSourcesList object with method add_source
    usl = UbuntuSourcesList(None)
    # Add new source line 'deb http://ppa.launchpad.net/%s/%s/ubuntu %s main'
    # class value will be added for codename
    usl.add_source('ppa:owner/repo')
    # Tests various file names for the source
    usl.add_source('http://deb.debian.org/debian/ sid main', file='dpkg')
    usl.add_source('http://deb.debian.org/debian/ sid main')



# Generated at 2022-06-13 04:54:46.703948
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    sl = SourcesList(module)
    assert sl.files == {}
    sl.load('/etc/apt/sources.list')
    assert len(sl.files) == 1
    sl.modify('/etc/apt/sources.list', 0, comment='not comment')
    assert sl.files['/etc/apt/sources.list'][0] == (0, True, True, 'deb http://archive.ubuntu.com/ubuntu trusty main restricted', 'not comment')
    sl.modify('/etc/apt/sources.list', 1, source='deb-src http://archive.ubuntu.com/ubuntu trusty main restricted')

# Generated at 2022-06-13 04:55:00.007825
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = MockModule({})
    assert module.params['codename'] is None
    assert module.params['architecture'] is None
    assert module.params['update_cache'] is False
    assert module.params['cache_valid_time'] is None
    assert module.params['state'] == 'present'
    assert module.params['list_action'] == 'list'
    assert module.params['list_target'] == ''
    assert module.params['filename'] is None
    assert module.params['mode'] == '0644'
    assert module.params['purge'] is False
    assert module.params['deb_src'] is False
    assert module.params['validate_certs'] is True
    assert module.params['cwd'] is None
    assert module.params['allow_unauthenticated'] is False
    assert module.params

# Generated at 2022-06-13 04:55:10.160784
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    tmpfile = tempfile.NamedTemporaryFile(
        prefix='ansible_test_sourceslist_load',
        delete=False,
        mode='w',
    )


# Generated at 2022-06-13 04:55:13.388387
# Unit test for function revert_sources_list
def test_revert_sources_list():
    result = revert_sources_list('', '', '')
    assert result is None
    assert result != 'foo'



# Generated at 2022-06-13 04:55:19.159483
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockModule:
        pass
    
    class MockAptPkgConfig:
        def __init__(self):
            self.Dir = MockAptPkgConfigDir()
            
    class MockAptPkgConfigDir:
        def __init__(self):
            self.Etc = MockAptPkgConfigDirEtc()
            
        class MockAptPkgConfigDirEtc:
            def __init__(self):
                self.sourcelist = 'mock-sourcelist'
                self.sourceparts = 'mock-sourceparts'
    
    class MockGlob:
        def __init__(self):
            self.iglob_results = []
        
        def iglob(self, glob_expression):
            return self.iglob_results

    apt_pkg.config = MockAptPkg

# Generated at 2022-06-13 04:55:26.686929
# Unit test for function revert_sources_list

# Generated at 2022-06-13 04:55:27.456399
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass



# Generated at 2022-06-13 04:55:40.857612
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    # Test saving of sources.list
    def test_save(tmpdir):
        '''Test saving of sources.list'''
        sl = SourcesList(None)
        sl.add_source('deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main')
        filename = os.path.join(tmpdir.dirname, 'sources.list')
        sl.files[filename] = sl.files[sl.default_file]
        del sl.files[sl.default_file]
        sl.default_file = filename
        sl.save()
        with open(filename, 'r') as f:
            text = f.read()
        assert text == 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main\n'

    assert test_save
    # Test saving to

# Generated at 2022-06-13 04:56:49.522915
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    class ModuleMock:
        def __init__(self, param):
            self.params = param

        def get_bin_path(self, s):
            return s

        def set_mode_if_different(self, s, s1, s2):
            pass

        def fail_json(self, msg):
            print('fail_json:', msg)

        def atomic_move(self, src, dst):
            print('atomic_move:', src, dst)

    param = {'repo': "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main",
             'state': 'present',
             'codename': 'trusty',
             'install_python_apt': False,
             'update_cache': False}
    module = ModuleMock(param)
    sources_list = Sources

# Generated at 2022-06-13 04:56:58.567275
# Unit test for function revert_sources_list
def test_revert_sources_list():
    # It is a bit tricky to test this function; this is the best we can do:
    import io
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import BytesIO

    temp_dir = tempfile.mkdtemp()
    module_params = dict(name=['universe'], state='present')
    m = AnsibleModule(module_params)
    target_files = set(ubuntu_sources_list(m))
    module_params = dict(name=['universe'], state='absent')
    m = AnsibleModule(module_params)

    module_params = dict(name=['universe'], state='present')
    m = AnsibleModule(module_params)

    sl = SourcesList(m)

# Generated at 2022-06-13 04:57:01.718442
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = AnsibleModule(argument_spec=dict(
        codename=dict(type='str'),
    ))
    fa = UbuntuSourcesList(module)
    fa.add_source("deb http://ppa.launchpad.net/teward/testppa/ubuntu bionic main", comment='', file=None)
    fa.add_source("deb http://ppa.launchpad.net/teward/testppa/ubuntu bionic main", comment='', file=None)

# Generated at 2022-06-13 04:57:08.116290
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import shutil
    import filecmp
    import tempfile
    import os

    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'sources.list.d'))
    module = AnsibleModule(argument_spec={})
    sources = SourcesList(module)
    sources.add_source('deb http://example.com/debian wheezy main', file=os.path.join(d, 'sources.list'))
    sources.add_source('deb http://example.net/debian wheezy main', file=os.path.join(d, 'sources.list'))

# Generated at 2022-06-13 04:57:13.965723
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    # Creating fake module object
    class FakeModule():
        pass
    module = FakeModule()

    # prepare arguments for function call
    module.params = dict()
    module.params['filename'] = None
    module.params['mode'] = None

    # creating argument expected to be returned
    expected = UbuntuSourcesList(
        module,
        add_ppa_signing_keys_callback=None
    )

    # create object to be tested
    obj = UbuntuSourcesList(
        module,
        add_ppa_signing_keys_callback=None
    )
    # test function call
    assert obj.__deepcopy__() == expected

# Generated at 2022-06-13 04:57:22.235593
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    # TODO: fix this test
    return # module.exit_json(changed=False)
    m = AnsibleModule({}, supports_check_mode=False)

    sl = SourcesList(m)
    s = 'deb http://archive.canonical.com/ubuntu hardy partner'
    sl.add_source(s)
    s = 'deb-src http://archive.canonical.com/ubuntu hardy partner'
    sl.add_source(s)
    s = 'deb http://archive.canonical.com/ubuntu hardy partner'
    sl.add_source(s)

    for filename, n, enabled, source, comment in sl:
        assert enabled



# Generated at 2022-06-13 04:57:23.053271
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    pass


# Generated at 2022-06-13 04:57:35.654910
# Unit test for function revert_sources_list
def test_revert_sources_list():
    module = AnsibleModule(argument_spec={})
    newmodule = module
    newmodule.params = {'sources': [{'sourceline': 'deb http://http.debian.net/debian stretch main', 'filename': 'joe_package.list'}], 'state': 'present', 'keyserver': 'keyserver.ubuntu.com'}
    sources_before = {}
    sources_after = {'/etc/apt/sources.list.d/joe_package.list': 'deb http://http.debian.net/debian stretch main'}
    sourceslist_before = UbuntuSourcesList(newmodule, add_ppa_signing_keys_callback=None)
    sourceslist_before.load(filename='/etc/apt/sources.list.d/joe_package.list')
    sourceslist_before.files = {}

   

# Generated at 2022-06-13 04:57:46.334578
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    class Module:
        class RunCommand:
            def __init__(self, arg):
                self.arg = arg
            def run_command(self, arg):
                return self.arg
        module = RunCommand
        def get_bin_path(self, arg):
            return self.module.run_command(arg)
    module = Module
    module.module = Module
    module.RunCommand.run_command = 'bin_path'
    module.RunCommand.run_command = 'dir_path'
    args ={
        'repo': 'package',
        'state': 'present',
        'filename': 'filename'
    }
    result = SourcesList(module, args)
    assert result != None


# Generated at 2022-06-13 04:57:54.347579
# Unit test for function revert_sources_list
def test_revert_sources_list():
    '''
    Test function revert_sources_list
    '''
    sources_before = {
        '/etc/apt/sources.list': '',
        '/etc/apt/sources.list.d/ansible.list': 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main'
    }
    sources_after = {
        '/etc/apt/sources.list': 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main',
        '/etc/apt/sources.list.d/ansible.list': 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main'
    }
    sourceslist_before = SourcesList()


# Generated at 2022-06-13 05:01:21.387792
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule({'test': 'install_python_apt'}, check_invalid_arguments=False)
    module.install_python_apt('test')
    module.exit_json({'changed': True, 'failed': False})



# Generated at 2022-06-13 05:01:24.577555
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(
        argument_spec={},
    )
    sourcelist = SourcesList(module)
    sourcelist.add_source('deb http://archive.canonical.com/ubuntu hardy partner')
    sourcelist.save()

    assert sourcelist.dump() == {'/etc/apt/sources.list': 'deb http://archive.canonical.com/ubuntu hardy partner\n'}



# Generated at 2022-06-13 05:01:28.997833
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    import os
    import tempfile
    sys.modules['apt'] = object()
    sys.modules['apt_pkg'] = object()
    from ansible.module_utils.apt import SourcesList
    sources_list_test = SourcesList(object())
    sources_list_test.files.clear()
    d, fn = os.path.split(sources_list_test.default_file)
    fd, tmp_path = tempfile.mkstemp(prefix=".%s-" % fn, dir=d)
    sources_list_test.files[tmp_path] = [(0, True, True, 'deb http://foo/', ' ')]
    sources_list_test.files[tmp_path].append((1, True, True, 'deb-src http://foo/', ' '))
    sources_list_test.remove_

# Generated at 2022-06-13 05:01:30.380960
# Unit test for function install_python_apt
def test_install_python_apt():
    module = AnsibleModule({})
    install_python_apt(module, 'python-apt')



# Generated at 2022-06-13 05:01:33.438463
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    test_file = os.path.join(os.path.dirname(__file__), 'test_sources.list')
    aptsources_distro.DISTRO_INTERFACES.remove('lsb_release')
    try:
        sources = SourcesList(AnsibleModule(argument_spec={}))
        sources.load(test_file)
        return sources
    finally:
        aptsources_distro.DISTRO_INTERFACES.append('lsb_release')



# Generated at 2022-06-13 05:01:38.465131
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    md = AnsibleModule(argument_spec={})
    sl = SourcesList(md)
    
    assert len(sl.files) == 0

    def touch(filename):
        open(filename, 'a').close()

    test_dir = tempfile.mkdtemp()
    test_files = [os.path.join(test_dir, 'sources.list'),
                  os.path.join(test_dir, 'sources.list.other'),
                  os.path.join(test_dir, 'other.list'),
                  os.path.join(test_dir, 'dir1', 'dir2', 'dir3', 'dir4.list')]
    for f in test_files:
        touch(f)

    # load default sources list if it exists
    assert os.path.isfile(sl.default_file)
   

# Generated at 2022-06-13 05:01:40.777657
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = AnsibleModule(argument_spec={'src': {'type': 'path'}, 'method':{'type': 'str'}, 'dest': {'type': 'path'}, 'mode': {'type': 'raw'}})
    SourcesList(module)
    return module


# Generated at 2022-06-13 05:01:50.276477
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = Dummy()
    module.params = dict(
        codename='trusty',
    )
    ubuntu_sources_list = UbuntuSourcesList(module)

    assert len(ubuntu_sources_list.files) == 2
    # 2 sources
    assert len(list(ubuntu_sources_list)) == 2
    # dump() to a dict
    assert len(ubuntu_sources_list.dump()) == 2

    # some properties
    assert ubuntu_sources_list.codename == 'trusty'
    assert ubuntu_sources_list.default_file == '/etc/apt/sources.list'

    # add a ppa
    ubuntu_sources_list.add_source('ppa:chris-lea/node.js')
    assert len(list(ubuntu_sources_list)) == 3