

# Generated at 2022-06-13 04:52:41.342309
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(argument_spec=dict(repo=dict(required=True),
                                              state=dict(choices=['absent', 'present'], default='present'),
                                              mode=dict(default=None, type='raw'),
                                              filename=dict(default=None, type='raw'),
                                              update_cache=dict(default=False, type='bool'),
                                              cache_valid_time=dict(default=0, type='int'),
                                              install_python_apt=dict(default=True, type='bool')))
    apt_repository = AptRepository(module)

    sl = apt_repository.sources_list
    test1 = '''deb http://archive.canonical.com/ubuntu hardy partner\n'''

# Generated at 2022-06-13 04:52:54.750805
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = AnsibleModule(argument_spec=dict())
    if not module.check_mode:
        apt_get_path = module.get_bin_path('apt-get')
        if apt_get_path:
            rc, so, se = module.run_command([apt_get_path, 'update'])
            if rc != 0:
                module.fail_json(msg="Failed to auto-install %s. Error was: '%s'" % (apt_pkg_name, se.strip()))
            rc, so, se = module.run_command([apt_get_path, 'install', apt_pkg_name, '-y', '-q'])

# Generated at 2022-06-13 04:52:59.001710
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule({})
    sources = SourcesList(module)
    path = os.path.dirname(os.path.realpath(__file__))
    sources.load(os.path.join(path, 'sources.list.test'))
    assert(len(sources.dump()) == 3)
    sources.modify('/tmp/sources.list', 0, enabled=False)
    assert(len(sources.dump()) == 4)


# Generated at 2022-06-13 04:53:11.862102
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    from ansible.module_utils.common._collections_compat import Mapping

    good_lines = [
        'deb http://example.com/debian stable main',
        'deb http://example.com/debian stable main # This is an example'
    ]

    bad_lines = [
        '# deb http://example.com/debian stable main',
        '# deb http://example.com/debian stable main # This is an example'
    ]

    sl = SourcesList(None)
    sl.files = {
        '/etc/apt/sources.list': [],
        '/etc/apt/sources.list.d/file.list': [],
    }
    # Populate files

# Generated at 2022-06-13 04:53:23.744531
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    import unittest
    class UbuntuSourcesList_remove_source_TestCase(unittest.TestCase):
        '''
        Unit test for method remove_source of class UbuntuSourcesList
        '''
        def setUp(self):
            '''
            stub function
            '''
            self.module = object()
            self.add_ppa_signing_keys_callback = object()
            self.codename = object()
            self.obj = UbuntuSourcesList(
                self.module,
                add_ppa_signing_keys_callback=self.add_ppa_signing_keys_callback
            )
            return

        def tearDown(self):
            '''
            stub function
            '''
            self.obj = None
            return


# Generated at 2022-06-13 04:53:35.029825
# Unit test for constructor of class SourcesList
def test_SourcesList():
    class Module(object):
        '''
        This is fake module class for unit test
        '''

        def get_bin_path(self, application):
            return None

        def fail_json(self, msg):
            raise Exception(msg)

        def atomic_move(self, source, dest):
            try:
                os.rename(source, dest)
            except OSError as e:
                if e.errno != errno.EXDEV:
                    raise

    sources = SourcesList(Module())
    # Check valid sources.

# Generated at 2022-06-13 04:53:47.580939
# Unit test for function main
def test_main():
    class FakeModule(object):
        def __init__(self, params, result):
            self.params = params
            self.result = result

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_args = kwargs

    class FakeAptDistro(object):
        pass

    class FakeAptSourcesDistro(object):
        pass

    monkeypatch = MonkeyPatch()

    monkeypatch.setattr('ansible_collections.ansible.community.plugins.modules.apt_repository.distro', FakeAptDistro())

# Generated at 2022-06-13 04:53:54.016148
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    class FakeModule:
        def run_command(self, command, check_rc=False):
            self.command_run = command

    fm = FakeModule()
    result = get_add_ppa_signing_key_callback(fm)
    assert result == fm.run_command

    fm.command_run = []
    result(['foo'])
    assert fm.command_run == ['foo']



# Generated at 2022-06-13 04:53:59.773064
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    """
    >>> m = AnsibleModuleStub(params=dict(
    ...   codename = 'eoan',
    ...   state = 'present',
    ... ))
    >>> s = UbuntuSourcesList(m)
    >>> m.params['state'] = 'absent'
    >>> s = UbuntuSourcesList(m)
    """



# Generated at 2022-06-13 04:54:05.826062
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = '''
module: apt_repository
name: another_test_repo
repo: "deb http://ppa.launchpad.net/osmoma/audio-recorder/ubuntu jessie main"
state: present
'''

# Generated at 2022-06-13 04:54:53.305982
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():

    class FakeModule(object):
        class FakeParams(object):
            def __init__(self):
                self.filename = None
                self.mode = DEFAULT_SOURCES_PERM

        params = FakeParams()
        check_mode = False
        atomic_move = lambda self, a, b: None
        set_mode_if_different = lambda self, a, b, c: None

    files = {}
    sl = SourcesList(FakeModule())
    sl._suggest_filename = lambda a: '/etc/apt/sources_list.suggested_filename'
    sl._expand_path = lambda a: a
    sl.files = files
    sl._add_valid_source = lambda a, b, c=None: None
    sl.save = lambda: None
    sl.dump = lambda: None

    sl

# Generated at 2022-06-13 04:54:53.981591
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass

# Generated at 2022-06-13 04:55:06.418558
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    m = MagicMock()

    r = UbuntuSourcesList(m)
    r.files['/etc/apt/sources.list.d/test.list'] = [(0, True, True, 'deb [arch=amd64] http://ppa.launchpad.net/thopiekar/test/ubuntu xenial main', '')]

    r.remove_source('ppa:thopiekar/test')

    m.assert_not_called()
    assert r.files['/etc/apt/sources.list.d/test.list'] == []

    r.files['/etc/apt/sources.list.d/test.list'] = [(0, True, True, 'deb [arch=amd64] http://ppa.launchpad.net/thopiekar/test/ubuntu xenial main', '')]


# Generated at 2022-06-13 04:55:17.206088
# Unit test for function install_python_apt
def test_install_python_apt():
    '''
    Test auto installation of Python Apt library in check mode
    '''
    aptsources_distro_mock = {}
    apt_pkg_mock = {}
    apt_mock = {}

    sys.modules['apt'] = apt_mock
    sys.modules['apt_pkg'] = apt_pkg_mock
    sys.modules['ansible.module_utils.ansible_module_commonutils'] = {}
    sys.modules['aptsources.distro'] = aptsources_distro_mock

    from ansible.module_utils.common.process import get_bin_path
    this_module = AnsibleModule({})
    this_module.get_bin_path = get_bin_path
    this_module.run_command = run_command

    # check_mode = True, install_python

# Generated at 2022-06-13 04:55:24.164060
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    # Create the temporary file, with a temporary filename
    (file_descriptor, temp_filename) = tempfile.mkstemp(suffix='.list', dir=temp_dir)
    # Create a file object
    temp_file = os.fdopen(file_descriptor, 'w')
    # Write our test content to the file
    temp_file.write('deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main\n')
    # Close the file object
    temp_file.close()

    # Compute path to test file
    test_file_basename = os.path.basename(temp_filename)
    test_file_dirname = os.path.dirname(temp_filename)
    test

# Generated at 2022-06-13 04:55:35.227197
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    from .__mock__ import Mock
    m = Mock()
    m.params = {
        'codename': None,
    }

    def _add_ppa_signing_keys_callback(command):
        pass

    o = UbuntuSourcesList(m, add_ppa_signing_keys_callback=_add_ppa_signing_keys_callback)
    o.files = {
        '/etc/apt/sources.list': '-',
    }
    o.codename = 'codename'

    o_ = copy.deepcopy(o)
    assert isinstance(o_, UbuntuSourcesList)
    assert not o_ is o
    assert o_.module is m
    assert o_.add_ppa_signing_keys_callback is _add_ppa_signing_keys_callback
    assert o_.files is not o

# Generated at 2022-06-13 04:55:47.351497
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    def _run_command(command):
        return (0, 'stdout', 'stderr')

    def _fail_command(command):
        raise RuntimeError('exception')

    def _fail_module(msg):
        raise RuntimeError('exception')

    def _probe_interpreters(interpreters, module):
        return '/path/to/interpreter'


# Generated at 2022-06-13 04:55:59.627952
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class MockModule(object):
        def __init__(self, filename, content):
            self.params = {'filename': filename}
            self.DEFAULT_SOURCES_PERM = 0o0644
            self.files = ['/etc/apt/sources.list', '/etc/apt/sources.list.d/%s.list' % filename, content]

        def get_bin_path(self, path, opt_dirs=[]):
            return '/usr/bin/%s' % path

        def run_command(self, list_of_args, check_rc=True):
            if list_of_args == ['/usr/bin/add-apt-repository', 'ppa:nginx/stable']:
                return (0, '', '')

# Generated at 2022-06-13 04:56:11.235880
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    class Module:
        def __init__(self, params):
            self.params = params

        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

        def atomic_move(self, tmp_path, filename):
            pass

    sources_list = SourcesList(Module({}))

    source_line1 = "# deb http://archive.ubuntu.com/ubuntu xenial main restricted\n"
    source_line2 = "deb-src http://archive.ubuntu.com/ubuntu xenial main restricted # comment\n"

    files = {
        '1.list': [source_line1],
        '2.list': [source_line1, source_line2, "# comment"]
    }

    sources_list.files = {}

# Generated at 2022-06-13 04:56:22.920278
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    def test_module():
        module = MagicMock()
        module.params = dict(
            codename='bionic'
        )

        def test_version_info():
            return dict(distro='Ubuntu', version_info=(18, 4, 0))
        module.version_info = test_version_info

        class test_fail_json():
            def __init__(self, msg):
                self.msg = msg
        module.fail_json = test_fail_json

        return module

    module = test_module()

    sl = UbuntuSourcesList(module)
    assert isinstance(sl, UbuntuSourcesList)

    sl_clone = copy.deepcopy(sl)
    assert isinstance

# Generated at 2022-06-13 04:58:29.982253
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = AnsibleModule({
        'codename': 'xenial',
        'deb': ['ppa:someuser/ppa', 'ppa:someuser/ppa2'],
        'deb-src': ['ppa:someuser/someppa'],
        'options': {},
        'state': 'present',
        'update_cache': False,
    })

    sourceslist = UbuntuSourcesList(module)
    expected_files = [
        '/etc/apt/sources.list.d/someuser_ppa.list',
        '/etc/apt/sources.list.d/someuser_ppa2.list',
        '/etc/apt/sources.list.d/someuser_someppa.list'
    ]

# Generated at 2022-06-13 04:58:41.492644
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule

    # Create temporary file
    tmp_file = StringIO()
    tmp_file.name = 'test.list'
    tmp_file.write('deb http://example.com/ubuntu trusty main universe multiverse\n')
    tmp_file.write('deb-src http://example.com/ubuntu trusty main universe multiverse\n')
    tmp_file.write('# deb http://example.com/ubuntu trusty special-repository\n')
    tmp_file.write('deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main\n')
    tmp_file.seek(0)

    # Create temporary module

# Generated at 2022-06-13 04:58:50.949387
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    def assert_dump(text, expected):
        module = AnsibleModule({})
        sourceslist = SourcesList(module)
        sourceslist.load(text)
        assert sourceslist.dump() == expected
    assert_dump('', {})
    assert_dump('\n', {})
    assert_dump('#\n', {})
    assert_dump('#\n\n', {})
    assert_dump('# \n', {})
    assert_dump('# \n\n', {})
    assert_dump('deb http://deb.devuan.org/merged jessie main\n', {'/etc/apt/sources.list': 'deb http://deb.devuan.org/merged jessie main\n'})

# Generated at 2022-06-13 04:58:57.563196
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    module = AnsibleModule({'state': 'present', 'repo': 'deb http://archive.ubuntu.com/ubuntu trusty main'})
    # Set up temp directory
    name = tempfile.mkdtemp(prefix='ansible_apt_repository', dir='/tmp')

    class _Module(object):
        def __init__(self, name):
            self.params = {'mode': -1}
            self.fail_json = lambda a: sys.exit(1)
            self.atomic_move = os.rename
            self.set_mode_if_different = lambda a, b, c: True
            self.get_bin_path = lambda a: name

    sources_list = SourcesList(_Module(name))

# Generated at 2022-06-13 04:59:08.890678
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    '''
    A test case to check if `add_source` method of UbuntuSourcesList class
    is thread safe.

    References:
        https://github.com/ansible/ansible/pull/38404
    '''

    import tempfile
    import threading
    import time
    import traceback

    def test_thread(sources_list, lock):
        '''
        A thread to test if `add_source` method of `UbuntuSourcesList` class is thread safe.

        Args:
            sources_list (:obj:`UbuntuSourcesList`): An instance of `UbuntuSourcesList` class.
            lock (:obj:`threading.Lock`): A lock for thread synchronisation.

        Returns:
            Nothing.
        '''


# Generated at 2022-06-13 04:59:10.502785
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    pass # TODO: write test for UbuntuSourcesList.__deepcopy__


# Generated at 2022-06-13 04:59:22.642426
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    module = AnsibleModuleMock()
    module.check_mode = False
    module.debug = False
    module.params = {'update_cache': False}
    module.run_command = ruc_mock
    module.atomic_move = am_mock
    module.fail_json = fj_mock
    module.exit_json = ej_mock
    sl = UbuntuSourcesList(module)
    sl.add_source("ppa:ansible/ansible")
    sl.add_source("ppa:ansible/ansible")
    sl.add_source("ppa:ansible/ansible")
    sl.add_source("ppa:ansible/ansible")
    sl.__deepcopy__()
    # Can't easily test for deepcopy, let's make sure it copies the class in any case
    assert type

# Generated at 2022-06-13 04:59:35.267064
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():

    class MockedModule:
        def __init__(self, debug=False):
            self.debug = debug
            self.params = {
                'mode': DEFAULT_SOURCES_PERM,
            }
            self.base_tmpdir = tempfile.mkdtemp()

        def fail_json(self, msg=None):
            if self.debug:
                print(to_native(msg))
            else:
                raise Exception(to_native(msg))

        def atomic_move(self, tmp_path, filename):
            d, fn = os.path.split(filename)

# Generated at 2022-06-13 04:59:36.841984
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    import doctest
    doctest.testmod()



# Generated at 2022-06-13 04:59:38.982119
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    # Do we want to test class methods?
    # if not hasattr(SourcesList, 'save'):
    #     SourcesList.save = SourcesList._save
    pass

