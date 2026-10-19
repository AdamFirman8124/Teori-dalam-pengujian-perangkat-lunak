

# Generated at 2022-06-13 02:09:19.246598
# Unit test for constructor of class LibMgr
def test_LibMgr():

    class TestLibMgr(LibMgr):
        LIB = 'unavailable'

    test_lib_mgr = TestLibMgr()
    assert False == test_lib_mgr.is_available()


# Generated at 2022-06-13 02:09:21.906769
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    for obj in get_all_pkg_managers():
        assert(get_all_pkg_managers()[obj]().is_available() is not None)


# Generated at 2022-06-13 02:09:31.793735
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    import os

    cm = CLIMgr()
    assert cm._cli == None

    os.environ['PATH'] = '/bin'
    cm = CLIMgr()
    assert cm._cli == None

    from tempfile import mkdtemp
    from shutil import rmtree

    tmpdir = mkdtemp()
    binpath = os.path.join(tmpdir, 'bin')
    os.makedirs(binpath)
    os.environ['PATH'] = binpath

    cm = CLIMgr()
    assert cm._cli == None

    with open(os.path.join(binpath, 'unclicommand'), 'w') as f:
        f.write('')
    cm = CLIMgr()
    assert cm._cli == None


# Generated at 2022-06-13 02:09:32.758675
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    pass


# Generated at 2022-06-13 02:09:36.585115
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    cli = CLIMgr()
    # Test with a CLI manager that is definitely not installed
    cli._cli = 'does_not_exist'
    assert not cli.is_available()
    # Test with a CLI manager that is definitely installed
    cli._cli = 'grep'
    assert cli.is_available()


# Generated at 2022-06-13 02:09:43.859566
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+') as tf:
        tf.write("#!/usr/bin/env python\n")
        tf.flush()
        c = CLIMgr()
        c.CLI = tf.name
        # create an executable file
        assert c.is_available() == True
        # remove execute permission from file
        import os
        os.chmod(c.CLI, 0o644) 
        assert c.is_available() == False

# Generated at 2022-06-13 02:09:47.957823
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    test = CLIMgr()
    assert test._cli is None

    test = CLIMgr()
    test.CLI = 'ls'
    assert test.is_available() is True


# Generated at 2022-06-13 02:09:54.422294
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    pm_list = PkgMgr.__subclasses__()
    for pm in pm_list:
        pm_name = pm.__name__
        pm_obj = pm()
        result = pm_obj.is_available()
        if pm_name == 'LibMgr':
            print("%s: %s" % (pm_name, result))
        else:
            print("%s: %s (%s)" % (pm_name, result, pm_obj._cli))

# Generated at 2022-06-13 02:10:04.901232
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    # We will use a arbitrary package manager as example, dpkg:
    tst_PkgMgr = PkgMgr()
    packages_installed = tst_PkgMgr.list_installed()
    # Check that packages_installed is not empty:
    assert packages_installed != None and len(packages_installed) > 0
    # Check that packages_installed is a list:
    assert type(packages_installed) == list
    # Check that all items of packages_installed are strings:
    assert all(isinstance(item, str) for item in packages_installed)
    # Finally, check that the list of installed packages is correct by checking that
    # a sample package from the list, bash, is installed:
    assert all('bash' in packages for packages in packages_installed)


# Generated at 2022-06-13 02:10:05.689437
# Unit test for constructor of class LibMgr
def test_LibMgr():
    libMgr = LibMgr()

# Generated at 2022-06-13 02:10:10.317373
# Unit test for constructor of class LibMgr
def test_LibMgr():
    lib = LibMgr()
    lib.is_available()


# Generated at 2022-06-13 02:10:11.289491
# Unit test for constructor of class LibMgr
def test_LibMgr():
    pm = LibMgr()
    assert pm._lib == None


# Generated at 2022-06-13 02:10:12.517362
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    pm = PkgMgr()
    print(pm.get_packages())

# Generated at 2022-06-13 02:10:13.502236
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    assert CLIMgr()



# Generated at 2022-06-13 02:10:20.915688
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    '''
    get_all_pkg_managers function will return the list of all PkgManagers
    alphabetically sorted based on the name of PkgManager
    '''
    try:
        packages_mgr = get_all_pkg_managers()
        next_key = None
        for key in packages_mgr:
            if next_key is not None:
                assert key >= next_key
            next_key = key
    except Exception:
        assert False, 'get_all_pkg_managers failed in returning expected PkgMgr list.'

# Generated at 2022-06-13 02:10:28.466606
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    # Test class that inherits PkgMgr
    class TestPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['package1 = 1.0', 'package2 = 2.0', 'package3 = 3.0', ]

        def get_package_details(self, package):
            package_details = {}
            package_details['name'] = package.split('=')[0].strip(' ')
            package_details['version'] = package.split('=')[1].strip(' ')
            return package_details

    # Test result

# Generated at 2022-06-13 02:10:31.752287
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.system.pkg_mgr import CLIMgr
    try:
        get_bin_path('yum')
    except ValueError:
        assert not CLIMgr().is_available()
    else:
        assert CLIMgr().is_available()


# Generated at 2022-06-13 02:10:32.885212
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    pkg_class = LibMgr()
    assert(pkg_class.is_available() == False)


# Generated at 2022-06-13 02:10:43.888135
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class PkgMgrMock(PkgMgr):
        def __init__(self):
            self.list_packages = []
            self.packages = {}
        def is_available(self):
            pass
        def list_installed(self):
            return self.list_packages
        def get_package_details(self, package):
            return self.packages[package]

    pm = PkgMgrMock()
    pm.list_packages = ['liba', 'libb', 'libfoo']
    pm.packages['libfoo'] = {
        'name': 'libfoo',
        'version': '1.0',
        'arch': 'x86_64',
        'source': 'yum'
    }

# Generated at 2022-06-13 02:10:45.851542
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():

    obj = LibMgr()
    assert obj.is_available() is False


# Generated at 2022-06-13 02:10:54.640731
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    assert list_installed == None


# Generated at 2022-06-13 02:11:04.020987
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class FakePkgMgr(PkgMgr):
        def is_available(self):
            return True
        def list_installed(self):
            return ['pkg1', 'pkg2']
        def get_package_details(self, package):
            return {"name": package, "version": "1.0.0"}
    print(get_all_pkg_managers())
    pkgmgr = get_all_pkg_managers()['fakepkgmgr']()
    assert pkgmgr.get_packages() == {"pkg1": [{"name": "pkg1", "version": "1.0.0", "source": "fakepkgmgr"}], "pkg2": [{"name": "pkg2", "version": "1.0.0", "source": "fakepkgmgr"}]}



# Generated at 2022-06-13 02:11:05.747037
# Unit test for function get_all_pkg_managers
def test_get_all_pkg_managers():
    pkg_managers = get_all_pkg_managers()
    assert 'npm' in pkg_managers

# Generated at 2022-06-13 02:11:08.816690
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    print("Start unit test for method is_available of class CLIMgr")
    c = CLIMgr()
    c.CLI = "ls"

    assert(c.is_available() == True)
    c.CLI = "lsdasdsadsadsadsa"
    assert(c.is_available() == False)
    print("End unit test for method is_available of class CLIMgr")


# Generated at 2022-06-13 02:11:10.724670
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    import unittest
    cl = CLIMgr()
    result = cl.is_available()
    cl.CLI = "doesnotexist"
    result = cl.is_available()
    assert result == False

# Generated at 2022-06-13 02:11:12.724058
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestMgr1(LibMgr):
        LIB = 'testlib'

    assert TestMgr1().is_available() == False



# Generated at 2022-06-13 02:11:15.780072
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    for _, cls in get_all_pkg_managers().items():
        if cls.__name__ not in ('CLIMgr', 'LibMgr'):
            print("%s: %s" % (cls.__name__, cls().list_installed()))

# Generated at 2022-06-13 02:11:25.932991
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    cli_package = "cowsay"
    cli_version = "3.03+dfsg2-4"
    cli_package_details = {"name": "cowsay", "version": "3.03+dfsg2-4", "source": "apt" }
    assert get_all_pkg_managers()['apt']().get_package_details(cli_package) == cli_package_details

    lib_package = "ansible"
    lib_version = "2.8.3"
    lib_package_details = {"name": "ansible", "version": "2.8.3"}
    assert get_all_pkg_managers()['pip']().get_package_details(lib_package) == lib_package_details

# Generated at 2022-06-13 02:11:35.565849
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    class TestPkgMgr(PkgMgr):

        def __init__(self):
            self.installed_packages = {}
            super(TestPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return self.installed_packages.keys()

        def get_package_details(self, package):
            return self.installed_packages[package]

    pm = TestPkgMgr()

    # Test 1: empty package list
    packages = pm.get_packages()
    assert len(packages) == 0

    # Test 2: test a single package
    pm.installed_packages = {'package_a': {'name': 'package_a', 'version': '1-0'}, '': ''}
    packages = pm.get_packages()


# Generated at 2022-06-13 02:11:39.636959
# Unit test for constructor of class LibMgr
def test_LibMgr():
    import sys
    import pytest
    class TestLibMgr(LibMgr):
        LIB = 'sys'

    a = TestLibMgr()
    sys_reference = sys
    b = a._lib
    assert sys_reference == b


# Generated at 2022-06-13 02:12:06.022716
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import ansible.module_utils.software_def as software_def
    import ansible.module_utils.six as six

    class PkgMgrTest(PkgMgr):
        def list_installed(self):
            return ['test1', 'test2']
        def get_package_details(self, package):
            if package == 'test1':
                return {'name': 'test1', 'version': '1.0.0', 'status': 'installed'}
            elif package == 'test2':
                return {'name': 'test2', 'version': '1.0.0', 'status': 'installed'}

    mgr = PkgMgrTest()
    # Test get_packages

# Generated at 2022-06-13 02:12:10.409348
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    mgrs = get_all_pkg_managers()
    for mgr in mgrs.values():
        try:
            pkg_mgr = mgr()
        except:
            pass
        for pkg in pkg_mgr.list_installed():
            pkg_mgr.get_package_details(pkg)

# Generated at 2022-06-13 02:12:19.410617
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    """Check the is_available method of class CLIMgr"""
    # Define a class that inherits from CLIMgr
    # The class will be tested as if it is a package manager
    class MyPkgMgr(CLIMgr):
        CLI = 'my_cli'

    # Check that is_available() returns False when the package manager is not available
    mypkg = MyPkgMgr()
    assert not mypkg.is_available()

    # install the package manager (defined by CLI)
    import os
    OM_DIR = os.path.join(os.path.dirname(__file__), 'data')
    OF_PATH = os.path.join(OM_DIR, 'my_cli')
    os.symlink(OF_PATH, '/usr/bin/my_cli')
    # Check that is_available() returns

# Generated at 2022-06-13 02:12:25.800068
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():
    import ansible.module_utils.common.packages.yum as yum
    import ansible.module_utils.common.packages.apt as apt
    from ansible.module_utils.six import b

    # test yum
    p = yum.Yum()
    assert p.get_package_details(b('mc')) == {'name': 'mc', 'version': '4.8.19-1.el7.x86_64', 'arch': 'x86_64'}

    # test apt
    p = apt.Apt()
    assert p.get_package_details(b('mc')) == {'name': 'mc', 'version': '1:4.8.14-1', 'arch': 'amd64', 'source': 'apt'}

# Generated at 2022-06-13 02:12:36.201039
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class DummyPkgMgr(PkgMgr):
        def is_available(self): return True
        def list_installed(self): return ['package1', 'package2']
        def get_package_details(self, package): return {'name': package, 'version': '1.0.0'}
    dpkgm = DummyPkgMgr()
    package_dict = dpkgm.get_packages()
    assert 'package1' in package_dict
    assert 'package2' in package_dict
    assert package_dict['package1'][0]['version'] == '1.0.0'
    assert package_dict['package2'][0]['version'] == '1.0.0'


# Generated at 2022-06-13 02:12:37.125603
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    print(get_all_pkg_managers())

# Generated at 2022-06-13 02:12:47.830742
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    """
    Unit test for method list_installed of class PkgMgr
    """
    from ansible.module_utils.packaging import repobased, pip, pklg, dnf, yum, gem, pacman, freebsd, homebrew, rpm, apk, apt, pkgng, openbsd, dpkg, pacman, pkg5, pkg8, pkgin, pkgutil, solaris, bsdpkg
    pm = PkgMgr()
    assert pm.list_installed() == None
    pm = repobased.RepositoryPackageManager()
    try:
        assert pm.list_installed() == []
    except AttributeError:
        pass
    pm = pip.Pip()
    assert pm.list_installed() == []
    pm = pklg.Pkgtool()

# Generated at 2022-06-13 02:12:50.752487
# Unit test for method list_installed of class PkgMgr
def test_PkgMgr_list_installed():
    package_manager = PkgMgr()
    packages = package_manager.list_installed()
    assert packages == None, "list_installed did not return None"


# Generated at 2022-06-13 02:12:53.261321
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    mgr = CLIMgr()
    assert mgr.CLI is None
    assert mgr._cli is None


# Generated at 2022-06-13 02:13:00.770759
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MockPkgMgr(PkgMgr):
        def is_available(self):
            return True

        def list_installed(self):
            return ['foo', 'bar']

        def get_package_details(self, package):
            return {'name': package, 'version': '1', 'source': 'test'}

    mockMgr = MockPkgMgr()
    installed_packages = mockMgr.get_packages()
    assert installed_packages['foo'] == [{'name': 'foo', 'version': '1', 'source': 'test'}]
    assert installed_packages['bar'] == [{'name': 'bar', 'version': '1', 'source': 'test'}]

# Generated at 2022-06-13 02:13:40.395770
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():

    from ansible.module_utils.common.collections import ImmutableDict

    class TestPkgMgr(PkgMgr):
        def __init__(self):
            self.list_installed_side_effect = ['python2', 'python3']
            self.get_package_details_data = {
                'python2': {'name': 'python', 'version': '2.7.11', 'source': 'yum'},
                'python3': {'name': 'python', 'version': '3.6.2', 'source': 'yum'},
            }
            super(TestPkgMgr, self).__init__()

        def is_available(self):
            return True

        def list_installed(self):
            return self.list_installed_side_effect


# Generated at 2022-06-13 02:13:43.280407
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    class TestCliMgr(CLIMgr):
        CLI = 'blah'

    pkg_manager = TestCliMgr()
    if not pkg_manager._cli:
        print("_cli is not set")


# Generated at 2022-06-13 02:13:44.464250
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False

# Generated at 2022-06-13 02:13:45.375461
# Unit test for constructor of class CLIMgr
def test_CLIMgr():
    pkgmgr = CLIMgr()
    assert pkgmgr

# Generated at 2022-06-13 02:13:51.947073
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    pm=PkgMgr()
    pm.CLI="a_bogus_cli"
    assert pm.is_available() == False

    pm1=CLIMgr()
    pm1.CLI="rpm"
    pm1.list_installed = lambda: [1,2]
    pm1.get_package_details = lambda x: dict(name="package"+str(x),version=str(x))
    assert pm1.is_available() == True

    packages = pm1.get_packages()
    assert "package1" in packages
    assert "package2" in packages
    assert len(packages) == 2

# Generated at 2022-06-13 02:13:53.315942
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    testMgr = PkgMgr()
    assert testMgr.is_available() == False, "Returned True when False was expected"


# Generated at 2022-06-13 02:13:58.022609
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    py_version = 'python-{0}.{1}.{2}-1'.format(ansible_version[0], ansible_version[1], ansible_version[2])
    class PkgMgrMock(PkgMgr):
        def list_installed(self):
            return [py_version]
        def get_package_details(self, package):
            if package == py_version:
                return {'name': 'python', 'version': ansible_version}
    p = PkgMgrMock()
    packages = p.get_packages()
    assert len(packages) == 1
    assert packages['python'][0]['source'] == 'pkgmgrmock'

# Generated at 2022-06-13 02:13:58.527989
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():  # noqa
    pass

# Generated at 2022-06-13 02:13:59.752651
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    obj = LibMgr()
    assert obj.is_available() is False


# Generated at 2022-06-13 02:14:08.868924
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():
    """Dummy test for class PkgMgr implemented by methods
    """
    class PkgMgrDummy(PkgMgr):
        """Dummy class for testing class PkgMgr
        """
        def is_available(self):
            return True

        def list_installed(self):
            return ["pkg1", "pkg2"]

        def get_package_details(self, pkg):
            if pkg == "pkg1":
                return {"name": "pkg1", "version": "1.0.0"}
            else:
                return {"name": "pkg2", "version": "2.0.0"}

    pkg_mgr = PkgMgrDummy()
    pkgs = pkg_mgr.get_packages()

# Generated at 2022-06-13 02:15:29.426090
# Unit test for method is_available of class LibMgr
def test_LibMgr_is_available():
    class TestPkgMgr(LibMgr):
        LIB = 'gi'
    test_pkg_mgr = TestPkgMgr()
    if hasattr(test_pkg_mgr, '_lib'):
        del test_pkg_mgr._lib
    assert test_pkg_mgr.is_available() == True
    assert getattr(test_pkg_mgr, '_lib') is not None


# Generated at 2022-06-13 02:15:32.512358
# Unit test for method get_package_details of class PkgMgr
def test_PkgMgr_get_package_details():

    class Foo(object):
        pass
    class Bar(PkgMgr):
        pass

    assert not PkgMgr.get_package_details(Foo())
    assert not Bar().get_package_details(object)



# Generated at 2022-06-13 02:15:33.871406
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    assert CLIMgr().is_available() == False


# Generated at 2022-06-13 02:15:40.624134
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.package_manager import CLIMgr
    import sys
    import os

    class test_CLIMgr(CLIMgr):
        CLI = 'test_CLIMgr'
        BINARY_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

    manager = test_CLIMgr()
    # check for a non-existing binary in the system
    assert(manager.is_available() == False)

    # check for a existing binary in the path
    sys.path.append(manager.BINARY_FILES_PATH)
    assert(manager.is_available() == True)

# Generated at 2022-06-13 02:15:47.217183
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class my_pkg_mgr(PkgMgr):
        pass

    class my_lib_mgr(LibMgr):
        LIB = 'ansible.module_utils.facts.system.distribution'

    class my_cli_mgr(CLIMgr):
        CLI = 'python2'

    pkg_mgr = my_pkg_mgr()
    assert pkg_mgr.get_packages() == {}
    lib_mgr = my_lib_mgr()
    pkg_mgr = my_pkg_mgr()
    assert pkg_mgr.get_packages() == {}
    cli_mgr = my_cli_mgr()
    pkg_mgr = my_pkg_mgr()
    assert pkg_mgr.get_packages() == {}

# Generated at 2022-06-13 02:15:57.525926
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class MyPkgMgr():
        def list_installed(self):
            return ['pkg1', 'pkg2']

        def get_package_details(self, package):
            return {'name': package,
                    'version': package[3]
                    }

    class OtherPkgMgr():
        def list_installed(self):
            return ['pkg1', 'pkg2', 'pkg1', 'pkg2']

        def get_package_details(self, package):
            return {'name': package,
                    'version': package[3],
                    'source': 'other'
                    }

    class PkgMgr4Test(PkgMgr):
        def list_installed(self):
            return ['pkg1', 'pkg2', 'pkg1', 'pkg2']


# Generated at 2022-06-13 02:15:59.544364
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    cli_mgr = CLIMgr()
    assert cli_mgr.is_available() == True

# Generated at 2022-06-13 02:16:01.926520
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
  n_CLI_mgr = CLIMgr()
  n_CLI_mgr.CLI = "python"
  assert (True==n_CLI_mgr.is_available())


# Generated at 2022-06-13 02:16:08.194048
# Unit test for method is_available of class CLIMgr
def test_CLIMgr_is_available():
    from ansible.module_utils.common.ansible_collector.collector import get_os_family
    from ansible.module_utils.common.ansible_collector.plugins.module_utils.software_rhel import YUM
    from ansible.module_utils.common.ansible_collector.plugins.module_utils.software_debian import APT

    class TestCLIMgr(CLIMgr):
        CLI = "ls"

    class TestCLIMgr2(CLIMgr):
        CLI = "/usr/bin/yum"
    
    # Test esxcli as it's only available on all ESXi hosts
    class TestCLIMgr3(CLIMgr):
        CLI = "esxcli"
    
    class TestCLIMgr4(CLIMgr):
        CLI = "apt"


# Generated at 2022-06-13 02:16:09.330909
# Unit test for method is_available of class PkgMgr
def test_PkgMgr_is_available():

    p = PkgMgr()
    assert p.is_available() == NotImplemented


# Generated at 2022-06-13 02:19:07.043532
# Unit test for constructor of class LibMgr
def test_LibMgr():
    class LibMgrTest(LibMgr):
        LIB = "abc"

    libmgr = LibMgrTest()
    assert libmgr._lib is None



# Generated at 2022-06-13 02:19:16.230211
# Unit test for method get_packages of class PkgMgr
def test_PkgMgr_get_packages():
    class pkg(PkgMgr):
        def __init__(self):
            self.fake = True
            super(pkg, self).__init__()
        def is_available(self):
            return True
        def list_installed(self):
            return [(self, 'aaa'), (self, 'bbb:1:1:1:1:1:1:1')]
        def get_package_details(self, package):
            return {'name': package[1]}
    class pkg_t(PkgMgr):
        def __init__(self):
            self.fake = True
            super(pkg_t, self).__init__()
        def is_available(self):
            return True