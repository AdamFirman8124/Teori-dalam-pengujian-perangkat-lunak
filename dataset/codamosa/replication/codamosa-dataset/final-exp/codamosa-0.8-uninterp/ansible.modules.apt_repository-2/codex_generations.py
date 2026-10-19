

# Generated at 2022-06-13 04:52:34.102179
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 04:52:42.018090
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    from tempfile import mktemp

    class FakeModule(object):
        def __init__(self, params, distro_codename='trusty'):
            self.params = params
            self.state = 'present'
            self.check_mode = False
            self.fail_json = lambda **kwargs: None
            self.path_exists = lambda **kwargs: True
            self.atomic_move = lambda arg1, arg2: None
            self.set_mode_if_different = lambda *args: None
            self.run_command = lambda *args, **kwargs: (0, "", "")

            self.distributor = _DistroInfo()
            self.distributor.codename = distro_codename
            self.distributor.id = 'centos'


# Generated at 2022-06-13 04:52:48.395115
# Unit test for function main
def test_main():
    #Load the module
    # Mocking
    import ansible.utils.template
    real_template = ansible.utils.template.template
    ansible.utils.template.template = lambda a, b: b # return original string

    import ansible.modules.packaging.os.apt_repository
    ansible_apt_repository = ansible.modules.packaging.os.apt_repository


    # Init

# Generated at 2022-06-13 04:52:49.438828
# Unit test for function install_python_apt
def test_install_python_apt():
    pass



# Generated at 2022-06-13 04:53:02.398071
# Unit test for method remove_source of class SourcesList

# Generated at 2022-06-13 04:53:13.890142
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    
    # Hack to disable function install_python_apt for test
    # install_python_apt is called from SourcesList.__init__
    # This way we can avoid instaling python-apt package
    def noop(*args, **kwargs):
        pass
    module = AnsibleModule({})
    module.install_python_apt = noop

    test_module_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_module.py')
    test_module_realpath = os.path.realpath(test_module_path)
    test_module_realpath_in_default_file = os.path.realpath(test_module_path)
    # Allows to use both python2 and python3 to run tests
    if not PY3:
        filetypes

# Generated at 2022-06-13 04:53:26.139237
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    class MockModule(object):
        def __init__(self):
            params = {
                'codename': 'codename',
            }

            self.params = params

    module = MockModule()

    obj = UbuntuSourcesList(module)
    obj.codename = 'codename'

    assert issubclass(UbuntuSourcesList, SourcesList), "Class UbuntuSourcesList does not inherit from class SourcesList."

    deep_copied_obj = deepcopy(obj)

    assert obj.module is not deep_copied_obj.module, "Field module of object not copied."
    assert obj.add_ppa_signing_keys_callback is deep_copied_obj.add_ppa_signing_keys_callback, "Field add_ppa_signing_keys_callback of object not correct."
    assert obj.codename is not deep_cop

# Generated at 2022-06-13 04:53:33.472441
# Unit test for function install_python_apt
def test_install_python_apt():
    """In this unit test we're going to test install_python_apt function.
       The function does not return anything. But, we would like to verify
       that module fails when apt-get is not installed.
    """
    module = AnsibleModule(argument_spec={})
    module.exit_json = verify_exit_json
    module.run_command = verify_run_command
    module.fail_json = verify_fail_json
    # Not sure how to test if apt-get is installed, so I'm going to create
    # a fake one with get_bin_path method.
    module.get_bin_path = mock_get_bin_path
    install_python_apt(module, 'python-apt')


# Generated at 2022-06-13 04:53:39.793994
# Unit test for function main
def test_main():
# This import is not required for Ansible, but is used by the unit tests
    from ansible.module_utils import basic
    from ansible.module_utils import url_filename
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.six import string_types

    module = _load_params(basic.AnsibleModule, url_filename, open_url, string_types)
    main(module)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:49.433087
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class MockModule:
        class MockParams:
            def __init__(self, codename):
                self.codename = codename
        mock_params = MockParams(codename='xenial')
        def __init__(self):
            self.params = self.mock_params

        def run_command(self, cmd, check_rc=False):
            return None, None, None

        def fail_json(self, msg):
            raise Exception(msg)
    m = MockModule()
    s = UbuntuSourcesList(m)

    # Test ppa line (ppa: ondrej/php)
    ppa_source_line = 'ppa:ondrej/php'
    s.add_source(ppa_source_line, 'comment')
    assert len(s.files.keys()) == 1

# Generated at 2022-06-13 04:54:20.158081
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    pass


# Generated at 2022-06-13 04:54:34.097391
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    '''Unit test for method modify of class SourcesList'''
    # The apt_repository module
    apt_repository_module = sys.modules['ansible.modules.packaging.os.apt_repository']

    # Create a module for the unit test
    module = apt_repository_module.AnsibleModule(argument_spec={}, supports_check_mode=True)

    # Create a SourcesList Object
    sl = SourcesList(module)

    # Create some files with sources
    aptsources_distro = sys.modules['aptsources.distro']

    # Create a dictionary with sources
    files = {}

# Generated at 2022-06-13 04:54:35.109744
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    '''@classmethod
    def add_source(self, line, comment='', file=None)'''
    pass

# Generated at 2022-06-13 04:54:39.560024
# Unit test for method dump of class SourcesList
def test_SourcesList_dump():
    module = AnsibleModule(
        argument_spec=dict()
    )
    p = SourcesList(module)
    p.load('/home/ubuntu/mytest/foo.list')
    assert p.dump() == {'/home/ubuntu/mytest/foo.list': 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable\n'}


# Generated at 2022-06-13 04:54:44.312016
# Unit test for method remove_source of class UbuntuSourcesList
def test_UbuntuSourcesList_remove_source():
    ubuntusourceslist = UbuntuSourcesList(module)
    assert ubuntusourceslist.files == {}
    assert list(ubuntusourceslist) == []

    ubuntusourceslist.files['deb http://ppa.launchpad.net/testuser/testppa/ubuntu focal main'] = [(0, True, True, 'deb http://ppa.launchpad.net/testuser/testppa/ubuntu focal main', '')]
    ubuntusourceslist.remove_source('ppa:testuser/testppa')
    assert ubuntusourceslist.files == {}
    assert list(ubuntusourceslist) == []



# Generated at 2022-06-13 04:54:47.752253
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    module = AnsibleModule(argument_spec={'_ansible_check_mode': {'type': 'bool'}, '_ansible_debug': {'type': 'bool'}})
    module.exit_json = exit_json
    sources_list = SourcesList(module)
    for a,b,c,d,e in sources_list:
        assert True


# Generated at 2022-06-13 04:55:01.078190
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    '''
    Test for method save of class SourcesList:

    '''
    global distro
    module = AnsibleModule({'state': ['present']})
    aptsources_distro.get_distro = lambda *args, **kwargs: distro
    sources_list = SourcesList(module)

    # Test for when source dumps correctly
    sources_list.files = {'test_file_path': [('test_n', True, True, 'test_source', 'test_comment'), ('test_n', True, True, 'test_source', 'test_comment')]}
    sources_list._apt_cfg_file = lambda *args, **kwargs: 'test_file_path'
    sources_list._apt_cfg_dir = lambda *args, **kwargs: '.'

# Generated at 2022-06-13 04:55:03.563218
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    module = AnsibleModule(argument_spec={})
    assert get_add_ppa_signing_key_callback(module) is None
    module = AnsibleModule(argument_spec={}, check_mode=False)
    callback = get_add_ppa_signing_key_callback(module)
    assert isinstance(callback, types.FunctionType)
    assert_raises(AnsibleError, callback, [])



# Generated at 2022-06-13 04:55:14.520463
# Unit test for method save of class SourcesList
def test_SourcesList_save():
    class MockModule:
        changed = False

        def fail_json(self, msg):
            assert False, msg

        def atomic_move(self, src, dest):
            abs_src = os.path.abspath(src)
            abs_dest = os.path.abspath(dest)
            if abs_src in self._temp_files:
                self._temp_files[abs_dest] = self._temp_files[abs_src]
                del self._temp_files[abs_src]
                self._moved_files.append(abs_dest)
            else:
                assert False, "MockModule failed to move %s to %s" % (abs_src, abs_dest)


# Generated at 2022-06-13 04:55:22.806281
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class TestModule:
        def __init__(self):
            class TestParams:
                def __init__(self):
                    self.mode = None
                def get(self, thing, default=None):
                    return default
            self.params = TestParams()
            class TestFailJson:
                def __init__(self):
                    pass
                def __call__(self, msg):
                    raise Exception(msg)

            self.fail_json = TestFailJson()

            class TestSetModeIfDifferent:
                def __init__(self):
                    pass
                def __call__(self, filename, mode, changed=True):
                    pass
            self.set_mode_if_different = TestSetModeIfDifferent()
            class TestAtomicMove:
                def __init__(self):
                    pass

# Generated at 2022-06-13 04:56:30.727853
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    module = basic.AnsibleModule({})
    main()


# Generated at 2022-06-13 04:56:37.696731
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    module = AnsibleModule({})
    sl = SourcesList(module)
    sl.load('/home/sashka/sources.list')
    sl.remove_source("""
  # deb http://osmirror.delivery.puppetlabs.net/ubuntu-16.04 xenial main
  # deb-src http://osmirror.delivery.puppetlabs.net/ubuntu-16.04 xenial main
  """)
    sl.remove_source("""
  # deb https://apt.puppetlabs.com xenial main
  # deb-src https://apt.puppetlabs.com xenial main
  """)

# Generated at 2022-06-13 04:56:46.849282
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    line = 'deb http://archive.canonical.com/ubuntu hardy partner'
    expected = {'Dir::Etc::sourcelist': '''\
# Added by Ansible
deb http://archive.canonical.com/ubuntu hardy partner


'''}
    sources = SourcesList(None)
    sources.add_source(line)
    result = sources.dump()
    assert result == expected

    line = 'deb-src http://archive.canonical.com/ubuntu hardy partner'
    expected = {'Dir::Etc::sourcelist': '''\
# Added by Ansible
deb http://archive.canonical.com/ubuntu hardy partner
deb-src http://archive.canonical.com/ubuntu hardy partner


'''}
    sources = SourcesList(None)
    sources.add_source(line)
    result

# Generated at 2022-06-13 04:56:57.279664
# Unit test for method remove_source of class SourcesList
def test_SourcesList_remove_source():
    # get sources file name
    sources_file = SourcesList(None).default_file
    # create file
    f = open(sources_file, 'w')
    # add valid source
    f.write('deb http://archive.canonical.com/ubuntu hardy partner\n')
    # add invalid source
    f.write('deb http://archive.canonical.com/ubuntu hardy partner\n')
    # add valid source
    f.write('deb http://archive.canonical.com/ubuntu hardy partner\n')
    # close file
    f.close()
    # create object
    sources_list = SourcesList(None)
    # it should have 3 lines
    assert 3 == sum(1 for _ in sources_list)
    # remove all of them

# Generated at 2022-06-13 04:56:58.122531
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:57:08.743144
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    module = AnsibleModule(argument_spec={
        'repos': {'required': False, 'type': 'list'},
    })
    sl = SourcesList(module)
    sl.load('tests/fixtures/apt/sources.list')
    expected = {
        'sources.list': ["deb http://debian.org/jessie main\n"],
        'sources.list.d/debian-jessie-backports.list': ["deb http://debian.org/jessie-backports main\n"],
        'sources.list.d/debian-jessie-nonfree.list': ["deb http://debian.org/jessie non-free\n"],
    }

# Generated at 2022-06-13 04:57:15.224782
# Unit test for function main

# Generated at 2022-06-13 04:57:17.140863
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    UbuntuSourcesList(module)



# Generated at 2022-06-13 04:57:27.555857
# Unit test for method modify of class SourcesList
def test_SourcesList_modify():
    import io
    import textwrap
    import unittest

    _module = AnsibleModule(argument_spec={})

    class TestCase(unittest.TestCase):
        def test(self):
            sl = SourcesList(_module)

            default_file = sl._apt_cfg_file('Dir::Etc::sourcelist')
            dir = sl._apt_cfg_dir('Dir::Etc::sourceparts')
            listname = 'test.list'

            try:
                os.makedirs(dir)
            except OSError:
                pass

            listpath = os.path.join(dir, listname)
            if os.path.isfile(listpath):
                os.remove(listpath)
            if os.path.isfile(default_file):
                os.remove(default_file)

            #

# Generated at 2022-06-13 04:57:28.723856
# Unit test for function get_add_ppa_signing_key_callback
def test_get_add_ppa_signing_key_callback():
    module = Mock()

    callback = get_add_ppa_signing_key_callback(module)

    assert(callback is None)


# Generated at 2022-06-13 04:59:08.462809
# Unit test for method add_source of class SourcesList
def test_SourcesList_add_source():
    module = AnsibleModule({})

# Generated at 2022-06-13 04:59:13.782557
# Unit test for constructor of class SourcesList
def test_SourcesList():
    sources = SourcesList(None)
    sources.add_source('deb http://example.com stable main', comment='test')
    assert len(sources.files) == 1

    lines = sources.dump().values()
    assert lines == ['deb http://example.com stable main # test\n']



# Generated at 2022-06-13 04:59:15.939604
# Unit test for method __deepcopy__ of class UbuntuSourcesList
def test_UbuntuSourcesList___deepcopy__():
    assert True, "Failed to prove that UbuntuSourcesList.deepcopy() works."



# Generated at 2022-06-13 04:59:24.954739
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    class MockModule(object):
        def __init__(self, file=None):
            self.debug = None
            self.fail_json = None
            self.params = {'mode': None, 'filename': file}

        def fail_json(self, msg):
            raise IOError(msg)

    class MockDistroInfo(object):
        def __init__(self, codename=None):
            self._codename = codename

        @property
        def codename(self):
            return self._codename

    global distro
    distro = MockDistroInfo('dummy')

    global apt_pkg
    apt_pkg = MagicMock()
    apt_pkg.config = MagicMock()
    apt_pkg.Config = MagicMock()

# Generated at 2022-06-13 04:59:36.723077
# Unit test for method load of class SourcesList
def test_SourcesList_load():
    from tempfile import NamedTemporaryFile
    from shutil import copy2

    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda x: x

    test = SourcesList(module)
    # add old file
    fd = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    fd.write(b'deb http://archive.canonical.com/ubuntu trusty partner\n')
    fd.write(b'deb http://ftp.us.debian.org/debian testing main\n')
    fd.write(b'deb http://dl.google.com/linux/chrome/deb/ stable main\n')
    fd.write(b'deb-src http://archive.canonical.com/ubuntu trusty partner\n')
    fd.close()


# Generated at 2022-06-13 04:59:41.635538
# Unit test for constructor of class UbuntuSourcesList
def test_UbuntuSourcesList():
    class DummyModule(object):
        def __init__(self):
            self.params = {'codename': 'precise'}

        def fail_json(self, *args, **kwargs):
            raise Exception('Failed')

    sources_list = UbuntuSourcesList(DummyModule())
    assert sources_list.codename == 'precise'
    sources_list.add_source("http://foo.bar precise-updates main restricted")
    assert sources_list.files["/etc/apt/sources.list"] == [(0, True, True, "deb http://foo.bar precise-updates main restricted", "")]


# Generated at 2022-06-13 04:59:51.301552
# Unit test for method add_source of class UbuntuSourcesList
def test_UbuntuSourcesList_add_source():
    import json
    import os
    from distutils.version import LooseVersion
    from unittest import mock
    from urllib.parse import urlparse
    from urllib.request import urlopen

    from ansible.modules.packaging.os import ubuntu_sources_list as module_class

    basepath = os.path.dirname(os.path.realpath(__file__))
    repos_files = [
        'ansible_test_repo_1_1_1.list',
        'ansible_test_repo_2_2_2.list',
        'ansible_test_repo_3_3_3.list',
        'ansible_test_repo_4_4_4.list',
    ]

# Generated at 2022-06-13 04:59:58.178926
# Unit test for function install_python_apt
def test_install_python_apt():
    setattr(sys, "version_info", (2, 7))
    module = AnsibleModule({
        'install_python_apt': True,
        'check_mode': False,
    })
    class MockModule(object):
        def __init__(self):
            self.run_command_results = [
                (0, "", ""),
                (0, "", ""),
            ]
            self.run_command_calls = []
            self.fail_json_results = []
            self.fail_json_calls = []

        def run_command(self, command):
            self.run_command_calls.append(command)
            return self.run_command_results.pop(0)


# Generated at 2022-06-13 05:00:03.408245
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile
    import filecmp
    import subprocess
    import textwrap


# Generated at 2022-06-13 05:00:14.433351
# Unit test for method __iter__ of class SourcesList
def test_SourcesList___iter__():
    class FakeModule:
        def __init__(self):
            pass
        def fail_json(self, **args):
            raise(Exception(args))
        def atomic_move(self, src, dest):
            pass
        def get_bin_path(self, bin_name):
            pass
        def run_command(self, cmd):
            pass
        def check_mode(self):
            return False
        def set_mode_if_different(self, path, mode, changed):
            pass
        def params(self):
            return {}
    sources = SourcesList(FakeModule())
    sources._add_valid_source('deb http://example.com/debian sample', '')
    sources._add_valid_source('deb-src http://example.com/debian sample', '')