

# Generated at 2022-06-13 04:41:48.568524
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class TestYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            return False

    # Test if lockfile does not exist
    my_YumDnf = TestYumDnf(None)
    my_YumDnf.lockfile = tempfile.mkstemp()[1]
    if my_YumDnf._is_lockfile_present():
        raise AssertionError("test_YumDnf_wait_for_lock_test_01 failed")
    os.remove(my_YumDnf.lockfile)

    # Test if lockfile exists but invalid pid
    my_YumDnf = TestYumDnf(None)

# Generated at 2022-06-13 04:41:56.786503
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:42:06.832090
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    """Unit test for method is_lockfile_pid_valid of class YumDnf"""
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible_collections.ansible.community.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
    module = MagicMock()
    module.check_mode = False
    module.exit_json = MagicMock(return_value=AnsibleExitJson())
    module.fail_json = MagicMock(return_value=AnsibleFailJson())

    class MockYumDnf(YumDnf):
        def __init__(self, module):
            super(MockYumDnf, self).__init__

# Generated at 2022-06-13 04:42:14.473228
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():

    import sys
    import unittest

    def mocked_is_lockfile_pid_valid(self):
        return True

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught
        by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught
        by the test case"""
        pass

    class ModuleMock(object):
        """
        Mock class for Ansible module
        """
        def __init__(self):
            self.params = {
                'lock_timeout': 30,
                'lockfile': '/var/lock/yum.pid',
            }
            self.fail_json = Mock(side_effect=AnsibleFailJson)

# Generated at 2022-06-13 04:42:25.725207
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """
    Mock module argument spec and test the wait_for_lock method of class YumDnf
    """

    from ansible.module_utils.yum_dnf.yum_dnf import YumDnf


# Generated at 2022-06-13 04:42:36.085015
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class TestModule(object):
        def fail_json(self, msg):
            raise Exception(msg)

    class TestYumDnf(YumDnf):
        """Subclass YumDnf class to test wait_for_lock method only."""
        def __init__(self, module):
            super(TestYumDnf, self).__init__(module)
            self.wait_for_lock()

        def is_lockfile_pid_valid(self):
            return True

        def run(self):
            pass

    class TestModule(object):
        def __init__(self, lock_timeout):
            self.params = {'lock_timeout': lock_timeout}
            self.fail_json = self._fail_json


# Generated at 2022-06-13 04:42:44.897680
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    test_class = YumDnf(None)

    # Case 1: No lock file present
    test_class._is_lockfile_present = MagicMock(return_value=False)
    test_class._is_lockfile_pid_valid = MagicMock(return_value=True)
    test_class.module = MagicMock()
    test_class.module.fail_json = MagicMock()
    test_class.module.params = {'lock_timeout': 0}
    test_class.wait_for_lock()

    # Case 2: Lock held by another process
    test_class._is_lockfile_present = MagicMock(return_value=True)
    test_class._is_lockfile_pid_valid = MagicMock(return_value=True)

# Generated at 2022-06-13 04:42:48.917105
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yumdnf = YumDnf(None)

    test_list = [
        ['a,b,c', 'd', 'e', 'f,g,h'],
        'a,b,c,d,e,f,g,h'.split(','),
        ['a,b,c,d,e,f,g,h'],
    ]
    expect = 'a,b,c,d,e,f,g,h'.split(',')

    for arg in test_list:
        result = yumdnf.listify_comma_sep_strings_in_list(arg)
        assert result == expect, 'failed listify_comma_sep_strings_in_list'



# Generated at 2022-06-13 04:42:57.254580
# Unit test for constructor of class YumDnf
def test_YumDnf():
    # Arrange
    test_module = MockModule()

# Generated at 2022-06-13 04:43:03.483876
# Unit test for constructor of class YumDnf
def test_YumDnf():

    module = MockAnsibleModule()
    yum = YumDnf(module)

    assert yum.names == ['apache', 'git']
    assert yum.disablerepo == ['epel', 'rpmforge']
    assert yum.enablerepo == ['epel', 'rpmforge']
    assert yum.exclude == ['apache', 'vim']
    assert yum.state == 'present'
    assert yum.update_only is True

test_YumDnf()


# Mock classes

# Generated at 2022-06-13 04:43:25.086819
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    import platform
    import pytest
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils import yum

    class FakeModule(object):
        def __init__(self):
            self.fail_json = lambda **kwargs: pytest.fail(**kwargs)

        def get_bin_path(self, _, required=True, opt_dirs=[]):
            return "/my/yum"

    class FakeArgs(object):
        def __init__(self):
            self.conf_file = None
            self.disable_gpg_check = False
            self.disable_excludes = None
            self.installroot = "/"
            self.install_repoquery = True
            self.install_weak_deps = True
            self.security = False
            self

# Generated at 2022-06-13 04:43:35.769472
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yd = YumDnf(None)
    assert(yd.listify_comma_sep_strings_in_list(['pkg1,pkg2', 'pkg3']) == ['pkg1', 'pkg2', 'pkg3'])

    # Test with multiple comma separated strings
    result = yd.listify_comma_sep_strings_in_list(['pkg1,pkg2,pkg3', 'pkg4,pkg5', 'pkg6, pkg7'])
    assert(result == ['pkg1', 'pkg2', 'pkg3', 'pkg4', 'pkg5', 'pkg6', 'pkg7'])

    # Test with no comma separated strings
    result = yd.listify_comma_sep_strings_in_list(['pkg1', 'pkg2', 'pkg3'])

# Generated at 2022-06-13 04:43:40.358961
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    import sys
    import pdb
    d = {}
    d['argument_spec'] = yumdnf_argument_spec['argument_spec']
    module = AnsibleModule(argument_spec=d['argument_spec'], supports_check_mode=False)
    setattr(module, '_ansible_debug', True)
    #pdb.set_trace()
    yumdnf = YumDnf(module)

    # Test 1
    expected_results = ['somepackage', 'someotherpackage', 'yetanotherpackage']
    some_list = ['somepackage', 'someotherpackage,yetanotherpackage']
    result = yumdnf.listify

# Generated at 2022-06-13 04:43:46.170904
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.packaging.os import yumdnf

    class DummyModule(AnsibleModule):

        def __init__(self):
            super(DummyModule, self).__init__(argument_spec=yumdnf_argument_spec, supports_check_mode=True)

    module = DummyModule()
    yum_dnf = yumdnf.YumDnf(module)
    yum_dnf.is_lockfile_pid_valid()

# Generated at 2022-06-13 04:43:53.463972
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class YumDnfMock(YumDnf):
        pkg_mgr_name = 'Yum'
        def is_lockfile_pid_valid(self):
            return False

    yum_dnf_mock = YumDnfMock(None)

    with tempfile.NamedTemporaryFile() as lockfile:
        lockfile.write(to_native("123"))
        lockfile.flush()
        yum_dnf_mock.lockfile = lockfile.name
        yum_dnf_mock.lock_timeout = 0
        yum_dnf_mock.wait_for_lock()

    with tempfile.NamedTemporaryFile() as lockfile:
        lockfile.write(to_native("123"))
        lockfile.flush()
        yum_dnf

# Generated at 2022-06-13 04:44:02.569897
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    yd = YumDnf(None)
    assert yd.listify_comma_sep_strings_in_list(['foo', 'bar, ', 'baz', 'qux']) == ['foo', 'bar', 'baz', 'qux']
    assert yd.listify_comma_sep_strings_in_list(['foo', 'bar, ', 'baz', 'qux,', 'qaz']) == ['foo', 'bar', 'baz', 'qux', 'qaz']
    assert yd.listify_comma_sep_strings_in_list(['foo', 'bar, ', 'baz', 'qux,', 'qaz,foo', 'bar']) == ['foo', 'bar', 'baz', 'qux', 'qaz', 'foo', 'bar']
   

# Generated at 2022-06-13 04:44:11.896592
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """
    :setup initialize yumdnf instance
    :steps
        1. Touch lockfile
        2. Invoke wait_for_lock with timeout 1
        3. Invoke wait_for_lock with timeout -1
        4. Invoke wait_for_lock with timeout 0
        5. Invoke wait_for_lock with timeout 1
        6. Remove lockfile
    :teardown remove tempdir
    :expectedresults
        1. pass
        2. pass
        3. pass
        4. pass
        5. wait 1s
        6. pass
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import iteritems

# Generated at 2022-06-13 04:44:19.216778
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    """
    Check that list listify_comma_sep_strings_in_list returns correct values
    for multiple input values
    """
    # Create temporary class for testing method
    class YumDnf_test(YumDnf):
        def __init__(self):
            self._module = 'something'

    test_obj = YumDnf_test()
    assert test_obj.listify_comma_sep_strings_in_list([]) == []
    assert test_obj.listify_comma_sep_strings_in_list(['foo', 'bar']) == ['foo', 'bar']
    assert test_obj.listify_comma_sep_strings_in_list(['foo, bar']) == ['foo', 'bar']
    assert test_obj.listify_comma

# Generated at 2022-06-13 04:44:24.874840
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import ansible.module_utils.basic
    import ansible.module_utils.yum_dnf
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=yumdnf_argument_spec)
    names = [p.strip() for p in module.params['name']]
    yumdnf = ansible.module_utils.yum_dnf.YumDnf(module)
    assert yumdnf.module == module
    assert yumdnf.allow_downgrade == module.params['allow_downgrade']
    assert yumdnf.autoremove == module.params['autoremove']
    assert yumdnf.bugfix == module.params['bugfix']
    assert yumdnf.cacheonly == module.params['cacheonly']
    assert yumdnf

# Generated at 2022-06-13 04:44:35.067265
# Unit test for constructor of class YumDnf
def test_YumDnf():
    '''Unit test for constructor of class YumDnf'''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback

    env_fallback('yum_disable_excludes')

    module = AnsibleModule(
        argument_spec=yumdnf_argument_spec,
        supports_check_mode=True,
    )

    yumdnf_instance = YumDnf(module)    # pylint: disable=abstract-class-instantiated

    assert yumdnf_instance.allow_downgrade is False
    assert yumdnf_instance.autoremove is False
    assert yumdnf_instance.bugfix is False
    assert yumdnf_instance.cacheonly is False
    assert yumdnf_instance

# Generated at 2022-06-13 04:45:18.721439
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.yum import Yum
    from ansible.module_utils.dnf import Dnf
    import ansible.module_utils.yum
    import ansible.module_utils.dnf
    import contextlib
    import tempfile
    import mock

    # Test yum and dnf
    for module_utils, cls in (
        (ansible.module_utils.yum, Yum),
        (ansible.module_utils.dnf, Dnf),
    ):

        # If the cls runs without error, the test should pass
        if get_bin_path(cls.pkg_mgr_name):
            yum

# Generated at 2022-06-13 04:45:30.474715
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    yumdnf = YumDnf(module)

    assert yumdnf.listify_comma_sep_strings_in_list(['python', 'python-libs']) == ['python', 'python-libs']
    assert yumdnf.listify_comma_sep_strings_in_list(['python', 'python-libs,python-crypto']) == ['python', 'python-libs', 'python-crypto']
    assert yumdnf.listify_comma_sep_strings_in_list(['python-libs, python-crypto']) == ['python-libs', 'python-crypto']
    assert yumdnf.listify_com

# Generated at 2022-06-13 04:45:44.718196
# Unit test for constructor of class YumDnf
def test_YumDnf():
    """
    Test constructor of class YumDnf
    """

    class TestYumDnf(YumDnf):
        """
        Mock class to test the constructor of class YumDnf. It will inherit
        from abstract class YumDnf.
        """
        def __init__(self, module):
            super(TestYumDnf, self).__init__(module)
            self.pkg_mgr_name = 'test_yum'

        def is_lockfile_pid_valid(self):
            return True

        def run(self):
            pass

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:45:53.291745
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    yumdnf = YumDnf()
    lockfile = '/var/run/yum.pid'
    yumdnf.lockfile = lockfile

    def is_lockfile_pid_valid():
        return True

    yumdnf.is_lockfile_pid_valid = is_lockfile_pid_valid

    def _is_lockfile_present():
        return True

    yumdnf._is_lockfile_present = _is_lockfile_present

    def module_fail_json(msg):
        return('fail_json')

    yumdnf.module.fail_json = module_fail_json

    (os.path.isfile, glob.glob)=(lambda x: True, lambda x: True)

    # Test 1: timeout -ve, lock file present
    yumdnf.lock_

# Generated at 2022-06-13 04:46:03.845596
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.yum_dnf import YumDnf

    yd = YumDnf("")

    # test case 1
    test_list_1 = ["a", "b", "c,d,e"]
    expected_result_1 = ["a", "b", "c", "d", "e"]
    result_1 = yd.listify_comma_sep_strings_in_list(test_list_1)
    assert result_1 == expected_result_1

    # test case 2
    test_list_2 = ["a", "b", "c,d,e", "f, g,h"]
    expected_result_2 = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Generated at 2022-06-13 04:46:09.140914
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:46:20.812693
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """Unit test for method wait_for_lock of class YumDnf"""

    class FakeModule(object):
        """Fake ansible module class for use in unit testing"""
        def __init__(self):
            self.params = {'lock_timeout': 30}

    def is_lockfile_pid_valid():
        """Fake the is_lockfile_pid_valid method for unit testing"""
        return False

    test_file = '/var/run/yum.pid'
    test_class = YumDnf(module=FakeModule())
    test_class.is_lockfile_pid_valid = is_lockfile_pid_valid
    test_class.lockfile = test_file

    def test_fail_pid_valid():
        """Test if the unit test fails when the lockfile is valid"""

# Generated at 2022-06-13 04:46:31.259934
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    temp_fd, temp_path = tempfile.mkstemp(prefix='ansible-pid-')
    with open(temp_path, 'w') as tmp_file:
        tmp_file.write('12345')
    yum_dnf = YumDnf(None)
    yum_dnf.lockfile = temp_path
    try:
        assert yum_dnf.is_lockfile_pid_valid(), "Unit test failure"
    finally:
        os.close(temp_fd)
        os.remove(temp_path)

    temp_fd, temp_path = tempfile.mkstemp(prefix='ansible-pid-')
    with open(temp_path, 'w') as tmp_file:
        tmp_file.write('1234')
    yum_dnf = YumDnf

# Generated at 2022-06-13 04:46:40.951351
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module = type('MockModule', (object,), {})

# Generated at 2022-06-13 04:46:51.617163
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    t = YumDnf()

    initial_list = ['a', 'b,c', 'd', 'e, f, g']
    expected_list = ['a', 'd', 'b', 'c', 'e', 'f', 'g']
    result_list = t.listify_comma_sep_strings_in_list(initial_list)
    assert expected_list == result_list

    initial_list = ['a', 'b,', 'd']
    expected_list = ['a', 'd', 'b']
    result_list = t.listify_comma_sep_strings_in_list(initial_list)
    assert expected_list == result_list


# Generated at 2022-06-13 04:47:42.974157
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    yumdnf = YumDnf(module)
    assert yumdnf.listify_comma_sep_strings_in_list(['a','b','c','d','e','f']) == ['a','b','c','d','e','f']
    assert yumdnf.listify_comma_sep_strings_in_list(['a','b,c','d','e','f']) == ['a','b','c','d','e','f']
    assert yumdnf.listify_comma_sep_strings_in_list(['a','b,c','d, e, f']) == ['a','b','c','d','e','f']
    assert y

# Generated at 2022-06-13 04:47:55.749288
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # unit test for method listify_comma_sep_strings_in_list()
    yum_dnf = YumDnf(object)
    assert not yum_dnf.listify_comma_sep_strings_in_list([0,1,2])
    assert yum_dnf.listify_comma_sep_strings_in_list([1,2,3,'a,b']) == [1,2,3,'a','b']
    assert not yum_dnf.listify_comma_sep_strings_in_list(['','','','','','','','','','','','','','',''])

# Generated at 2022-06-13 04:48:04.120982
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class FakeYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            self.validate_certs = True

    class FakeModule(object):
        def __init__(self, params):
            self.params = params

    params = {'lockfile': '/var/run/yum.pid', 'lock_timeout': 30}
    foo = FakeYumDnf(FakeModule(params))
    assert foo.validate_certs == True, 'should be True'



# Generated at 2022-06-13 04:48:13.339739
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    fd, temp_pid_file = tempfile.mkstemp()
    # create a fake lockfile
    with os.fdopen(fd, 'w') as tmp:
        tmp.write("1")
    # create a fake process
    pid = os.fork()
    # in the child process return False

# Generated at 2022-06-13 04:48:19.583851
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import ansible.module_utils.yum
    module = ansible.module_utils.yum.construct_ansible_module(yumdnf_argument_spec)
    ydf = ansible.module_utils.yum.YumDnf(module)
    assert ydf.module == module



# Generated at 2022-06-13 04:48:31.175524
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=yumdnf_argument_spec,
        required_one_of=[['name', 'list', 'update_cache']],
        mutually_exclusive=[['name', 'list']],
        supports_check_mode=True,
    )

    p = module.params

    p['name'] = ['foo']
    obj = YumDnf(module)
    assert obj.names == ['foo']

    p['name'] = ['foo', 'bar']
    obj = YumDnf(module)
    assert obj.names == ['foo', 'bar']

    p['name'] = ['foo,bar']
    obj = YumDnf(module)
    assert obj.names == ['foo', 'bar']

   

# Generated at 2022-06-13 04:48:43.367284
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.yum_dnf import YumDnf

    yd = YumDnf(None)
    yd.lockfile = ''
    yd._is_lockfile_present = lambda: False
    yd.module = None
    yd.lock_timeout = 0
    yd.wait_for_lock()

    yd.lockfile = ''
    yd._is_lockfile_present = lambda: False
    yd.module = None
    yd.lock_timeout = 30
    yd.wait_for_lock()

    yd.lockfile = ''
    yd._is_lockfile_present = lambda: True
    yd.module = None
    yd.lock_timeout = 30
    yd

# Generated at 2022-06-13 04:48:46.742216
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule

    yumdnf = YumDnf(AnsibleModule(**yumdnf_argument_spec))
    assert yumdnf is not None

# Generated at 2022-06-13 04:48:58.932651
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils import yum, dnf
    y = yum.YumDnf(None)
    d = dnf.YumDnf(None)

    test_list = []
    list1 = y.listify_comma_sep_strings_in_list(test_list)
    list2 = d.listify_comma_sep_strings_in_list(test_list)
    assert list1 == []
    assert list2 == []

    test_list = [""]
    list1 = y.listify_comma_sep_strings_in_list(test_list)
    list2 = d.listify_comma_sep_strings_in_list(test_list)
    assert list1 == []
    assert list2 == []


# Generated at 2022-06-13 04:49:08.725435
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    '''
    This is a unit test for wait_for_lock of class YumDnf
    '''

    module = AnsibleModule(**yumdnf_argument_spec)

    yum = YumDnf(module)

    # case 1: No lockfile
    assert not yum._is_lockfile_present()
    try:
        yum.wait_for_lock()
    except Exception as e:
        msg = "Expected: No exception, got %s" % str(e)
        module.fail_json(msg="%s" % (msg))

    # case 2: lockfile exists and is locked by another process
    yum.is_lockfile_pid_valid = MagicMock(return_value=True)

# Generated at 2022-06-13 04:50:56.304653
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class foo(YumDnf):
        def __init__(self, module):
            super(foo, self).__init__(module)

        def is_lockfile_pid_valid(self):
            pass

    class ModuleMock(object):
        params = {}

    module = ModuleMock()
    d = foo(module)

    assert d.listify_comma_sep_strings_in_list(["foo", "foo-devel", "bar", "foobar", "bar,foo", "foo, bar,", " bar,", "bar ,foo"]) \
            == ["foo", "foo-devel", "bar", "foobar", "bar", "foo", "bar", "foo", "bar", "foo"]


# Generated at 2022-06-13 04:51:06.412117
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    a_list = ["foo", "foo,bar", "foo,bar,baz"]
    expected_list_comma_sep_strings_in_list = ["foo", "foo", "bar", "baz"]
    from ansible.module_utils.yum import YumDnf
    y = YumDnf(None)
    actual_list_comma_sep_strings_in_list = y.listify_comma_sep_strings_in_list(a_list)
    assert expected_list_comma_sep_strings_in_list == actual_list_comma_sep_strings_in_list


# Generated at 2022-06-13 04:51:17.323189
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    """
    Testcase for wait_for_lock method of YumDnf class which is defined as
    abstractmethod in class, so we need to create a subclass in order to test
    the method. This subclass doesn't need to contain any implementation.
    """
    class TestYumDnf(YumDnf):
        """
        Subclass of YumDnf class which carries dummy implementation of
        abstractmethod 'is_lockfile_pid_valid' so that testcase runs successfully
        """
        def __init__(self, module):
            super(TestYumDnf, self).__init__(module)

        def is_lockfile_pid_valid(self):
            return False

    m = MockModule()
    yd = TestYumDnf(m)
    temp_dir = tempfile.mkdtemp

# Generated at 2022-06-13 04:51:27.327315
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    module = MockModule()
    yum = YumDnf(module)

    yum.lockfile = None
    yum.wait_for_lock()
    assert not module.fail_json.called

    module.fail_json.reset_mock()

    yum.lockfile = '/var/run/yum.pid'
    yum.is_lockfile_pid_valid = Mock(return_value=None)
    yum.lock_timeout = 0
    yum.wait_for_lock()
    assert not module.fail_json.called

    module.fail_json.reset_mock()

    yum.lockfile = '/var/run/yum.pid'
    yum.is_lockfile_pid_valid = Mock(return_value=None)
    yum.lock_timeout = -1