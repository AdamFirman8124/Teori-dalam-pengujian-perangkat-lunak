

# Generated at 2022-06-13 04:52:34.785176
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():

    class Dummy(object):
        def __init__(self):
            self.params = {
                'codename': '',
                'default_release': ''
            }

        def run_command(self, cmd, check_rc=False):
            return 0, 'Out', 'Err'

        def fail_json(self, msg):
            pass

        def atomic_move(self, src, dst):
            pass

        def set_mode_if_different(self, path, mode, changed):
            pass

    class DummyPopen(object):
        def __init__(self, dummy_module, cmd, **kwargs):
            pass

        def communicate(self):
            return '', ''

    source = 'deb https://example.com/repo stable main'
    module = Dummy()
    u = UbuntuSourcesList

# Generated at 2022-06-13 04:52:42.575621
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class MockModule:
        params = {'codename': 'xenial'}

        run_command = MagicMock(return_value=(1, '', 'err'))
        fail_json = MagicMock()
        atomic_move = MagicMock()
        set_mode_if_different = MagicMock()

    class MockFetchURL:
        def __init__(self, code, content):
            self.code = code
            self.content = content

        def read(self):
            return self.content

    sources_list = UbuntuSourcesList(MockModule())
    sources_list.add_source('http://foo.bar:8080/ubuntu')
    sources_list.add_source('http://example.com/ubuntu')
    sources_list.add_source('ppa:test/ppa')

    # ppa repository

# Generated at 2022-06-13 04:52:55.855542
# Unit test for constructor of class SourcesList
def test_SourcesList():
    class M(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, shellcmd, required=False, opt_dirs=[]):
            if shellcmd == 'apt-get':
                return '/usr/bin/apt-get'
            return None

        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None, binary_data=None):
            if cmd[0] == '/usr/bin/apt-get':
                return 0, '', ''
            raise Exception('unhandled command ' + repr(cmd))

        def fail_json(self, **kwargs):
            raise Exception('fail_json called with ' + repr(kwargs))


# Generated at 2022-06-13 04:52:57.173293
# Unit test for function revert_sources_list
def test_revert_sources_list():
    pass



# Generated at 2022-06-13 04:52:58.138965
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    assert False, "No implemented"


# Generated at 2022-06-13 04:53:07.716572
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = AnsibleModule({})
    sources_list = SourcesList(module)
    sources_list.files = {
           '/etc/apt/sources.list': [(0, True, True, 'deb http://kernel.org stretch', None)],
           '/etc/apt/sources.list.d/kernel.list': [(0, True, False, 'deb http://kernel.org stretch', None),
                                                   (1, True, True, 'deb http://kernel.org stretch', None)],
           '/etc/apt/sources.list.d/kernel_org.list': [(0, True, False, 'deb http://kernel.org stretch', None),
                                                       (1, True, True, 'deb http://kernel.org stretch', None)],
          }

# Generated at 2022-06-13 04:53:18.819817
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    class FakeModule(object):
        def fail_json(self, msg):
            raise AssertionError(msg)

        def atomic_move(self, src, dst):
            os.rename(src, dst)

        def set_mode_if_different(self, file, mode, changed):
            pass

        def get_bin_path(self, executable, opt_dirs=None):
            return executable

        def run_command(self, args):
            return 0, '', ''


# Generated at 2022-06-13 04:53:31.927867
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    dumps = {
        'apt_repository1.list' : \
        '''
        deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
        deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
        ''',
        'apt_repository2.list' : \
        '''
        deb http://us.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
        ''',
}

    class Args(object):
        pass

    args = Args()
    args.makedirs = None
    args.atomic_move = None
    args.set_mode_if_different = None
    args.fail_json = None
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)

# Generated at 2022-06-13 04:53:44.695211
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    new_line = 'deb http://archive.canonical.com/ubuntu hardy partner'
    module = AnsibleModule(argument_spec={})
    new_filepath = '/etc/apt/sources.list.d/hardy-partner.list'
    sl = SourcesList(module)
    sl.add_source(new_line)

    # sources should exist in file
    assert sl.files[new_filepath][0][3] == new_line

    # test that when we add a duplicate source it does not add a new entry
    sl.add_source(new_line)
    assert len(sl.files[new_filepath]) == 1
    # test that we can add a comment to the new source
    sl.remove_source(new_line)
    comment = 'this is a comment'
    sl.add_source

# Generated at 2022-06-13 04:53:57.911109
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    module = MagicMock()
    module.params = {}
    module.get_bin_path.return_value = '/bin/true'
    # Patch the distro.codename return value
    module.distro.codename.return_value = 'trusty'

    s = UbuntuSourcesList(module)
    assert s.codename == 'trusty'

    # Patch the distro.codename return value
    module.distro.codename.return_value = 'xenial'
    module.params['codename'] = 'yakkety'
    s = UbuntuSourcesList(module)
    assert s.codename == 'yakkety'
    assert module.params['codename'] == 'yakkety'

# Generated at 2022-06-13 04:54:37.186068
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    module = MagicMock()
    module.params = {}
    module.params['codename'] = 'codename'
    module.params['filename'] = 'filename'
    module.params['mode'] = 'mode'
    sourcelist = AnsibleDistro(module).get_sourcelist()
    sourcelist.add_source('deb http://ppa.launchpad.net/foo/bar/ubuntu codename main', file = 'filename')
    module.set_mode_if_different.assert_has_calls([call('filename', 'mode', False)])
    module.run_command.assert_has_calls([call(['apt-key', 'adv', '--recv-keys', '--no-tty', '--keyserver', 'hkp://keyserver.ubuntu.com:80', 'fingerprint'])])

# Generated at 2022-06-13 04:54:46.279843
# Unit test for function main

# Generated at 2022-06-13 04:54:59.019163
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    from ansible.module_utils.common.respawn import respawn_with_fallback
    from ansible.module_utils.basic import AnsibleModule

    test_data = []
    test_data.append(dict(
        filename='test_file',
        module_args=dict(
            state="present",
            repo="deb http://example.com/ubuntu trusty main",
        ),
    ))
    test_data.append(dict(
        filename='test_file',
        module_args=dict(
            state="absent",
            repo="deb http://example.com/ubuntu trusty main",
        ),
    ))

# Generated at 2022-06-13 04:55:00.185704
# Unit test for function main
def test_main():
	pass


# Generated at 2022-06-13 04:55:10.271365
# Unit test for function main

# Generated at 2022-06-13 04:55:23.129757
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    import tempfile
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic

    testlines = {
        "filename1": """
#kommentar
deb http://de.archive.ubuntu.com/ubuntu/ xenial main
deb http://de.archive.ubuntu.com/ubuntu/ xenial universe

deb http://de.archive.ubuntu.com/ubuntu/ xenial multiverse

# source
deb-src http://de.archive.ubuntu.com/ubuntu/ xenial main restricted
""",
        "filename2": """
#kommentar
deb http://de.archive.ubuntu.com/ubuntu/ xenial main
"""
    }

    #need a module
    module = basic.AnsibleModule(
        argument_spec={},
    )


# Generated at 2022-06-13 04:55:24.125944
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    pass

# Generated at 2022-06-13 04:55:35.224051
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = None
    sources = SourcesList(module)

    dumpstruct = {
        '1.list': 'deb http://archive.canonical.com/ubuntu hardy partner\n',
        '2.list': 'deb-src http://archive.canonical.com/ubuntu hardy partner\n',
        '3.list': 'deb http://archive.canonical.com/ubuntu hardy partner #\n',
    }

    for filename, content in dumpstruct.items():
        d, fn = os.path.split(filename)
        try:
            os.makedirs(d)
        except OSError as err:
            if not os.path.isdir(d):
                raise Exception("Failed to create directory %s: %s" % (d, to_native(err)))
        fd, tmp_path = temp

# Generated at 2022-06-13 04:55:45.641913
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    class Module(object):
        def __init__(self):
            self.fail_json = fail_json
        def atomic_move(self, old, new):
            return True
        def set_mode_if_different(self, path, mode, follow, changed=False):
            return True
        def params(self):
            return {}
        def get_bin_path(self, path):
            return '/usr/bin' + path
        def exit_json(self, *args, **kwargs):
            pass

    class FauxAptPkg(object):
        class Config(object):
            @staticmethod
            def FindDir(spec):
                return '/etc/apt/sources.list.d'
            @staticmethod
            def FindFile(spec):
                return '/etc/apt/sources.list'

    module

# Generated at 2022-06-13 04:55:51.235390
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    sl = UbuntuSourcesList(None)
    sl.codename = 'codename'
    sl.module = 'module'

    assert isinstance(deepcopy(sl), UbuntuSourcesList)
    assert deepcopy(sl).codename == 'codename'
    assert deepcopy(sl).module == 'module'


# Generated at 2022-06-13 04:57:09.856040
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    import os


# Generated at 2022-06-13 04:57:20.910147
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module_name = 'ansible.builtin.apt_repository'
    module_path = 'library/' + module_name.replace('.', '/') + '.py'
    module_args = {
        'repo': 'deb http://archive.canonical.com/ubuntu hardy partner',
        'state': 'present',
    }
    module_state = dict()

    tmpdir = tempfile.mkdtemp(prefix='ansible-tmp-%s-' % os.getpid())

# Generated at 2022-06-13 04:57:27.431809
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    module = FakeModule()
    module.check_mode = True
    assert get_add_ppa_signing_key_callback(module) is None

    module.check_mode = False
    cb = get_add_ppa_signing_key_callback(module)
    assert cb is not None

    cb(['apt-key', 'adv', '--recv-keys', '--no-tty', '--keyserver', 'hkp://keyserver.ubuntu.com:80', '123ABC'])

    # assert that command was called for check_mode = False
    assert len(module.run_command_calls) == 1
    assert len(module.run_command_calls[0].args) == 1

# Generated at 2022-06-13 04:57:35.693161
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    class DummyModule:
        def __init__(self):
            self.sources_list = SourcesList(self)
            self.sources_list.load(__file__ + '.sources')
    
    dummy_module = DummyModule()
    dummy_module.sources_list.remove_source(dummy_module.sources_list.dump()[__file__ + '.sources'])
    assert len(dummy_module.sources_list.dump()) == 0


# Generated at 2022-06-13 04:57:46.920610
# Unit test for method load of class SourcesList

# Generated at 2022-06-13 04:57:57.972934
# Unit test for function install_python_apt
def test_install_python_apt():
    # Mock the module and its return values
    sys.modules['apt'] = sys.modules['apt_pkg'] = sys.modules['aptsources.distro'] = None
    mock = type('module', (object,), {
        'check_mode': False,
        'get_bin_path': lambda self, binary: '/usr/bin/%s' % binary,
        'run_command': lambda self, command: (0, 'MOCK:%s' % command[-1], '')
    })
    global apt_pkg, apt, aptsources_distro  # pylint: disable=global-statement
    apt_pkg = apt = aptsources_distro = mock()
    install_python_apt(mock(), 'python-apt')
    # pylint: disable=protected-access
    assert 'apt' in sys

# Generated at 2022-06-13 04:58:05.334845
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = AnsibleModule(argument_spec=dict(repo="str", state="str"))
    sources_list=SourcesList(module)
    sources_list.files = {'/etc/apt/sources.list': [(0, True, True, 'deb http://archive.canonical.com/ubuntu hardy partner', '')], '/etc/apt/sources.list.d/google-chrome.list': [(0, True, True, 'deb http://dl.google.com/linux/chrome/deb/ stable main', '')]}
    sources_list.remove_source('deb http://archive.canonical.com/ubuntu hardy partner')

# Generated at 2022-06-13 04:58:13.635989
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    import shutil
    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.run_command_calls = []
            self.run_command_rcs = []
            self.run_command_msgs = []

        def run_command(self, args, check_rc=False):
            self.run_command_calls.append(args)
            if check_rc:
                if self.run_command_rcs:
                    rc = self.run_command_rcs.pop(0)
                    sout = ''
                    serr = self.run_command_msgs.pop(0)
                    return rc, sout, serr
            return 0, '', ''

        def fail_json(self, *args, **kwargs):
            raise Exception(args[0])

# Generated at 2022-06-13 04:58:25.043295
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    '''
    FIXME: the test is commented as it requires sudo.
    '''
    return False
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.apt import SourcesList
    module = AnsibleModule({})
    sl = SourcesList(module)
    sl.default_file = '/tmp/sources.list'
    sl.add_source('deb http://ftp.debian.org/debian jessie main contrib', file='debian_jessie.list')
    sl.add_source('deb-src http://ftp.debian.org/debian jessie main contrib', comment='This is a test')
    sl.save()


# Generated at 2022-06-13 04:58:36.854919
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    '''
    Unit test for method __deepcopy__ of class UbuntuSourcesList
    '''
    sources_list = UbuntuSourcesList.__new__(UbuntuSourcesList)
    sources_list.__init__ = MagicMock(spec=UbuntuSourcesList.__init__)
    sources_list.__init__.return_value = None
    sources_list.add_ppa_signing_keys_callback = 'test_add_ppa_signing_keys_callback'

    assert sources_list.__deepcopy__() == UbuntuSourcesList(sources_list.module, sources_list.add_ppa_signing_keys_callback)
    sources_list.__init__.assert_called_once_with(sources_list.module, sources_list.add_ppa_signing_keys_callback)

